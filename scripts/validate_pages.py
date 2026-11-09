"""Validate this buildless GitHub Pages project and the complete dataset gallery."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
errors = []

class Gallery(HTMLParser):
    def __init__(self):
        super().__init__()
        self.articles = 0
        self.links = set()
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'article':
            self.articles += 1
        if 'id' in attrs:
            self.anchors.add(attrs['id'])
        for key in ['src', 'href']:
            if key not in attrs:
                continue
            value = attrs[key]
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme != 'https':
                    errors.append('Unexpected external/local scheme: ' + value)
            elif parsed.path:
                if parsed.path.startswith('/'):
                    errors.append('Root-relative link would escape the project URL: ' + value)
                self.links.add(unquote(parsed.path))
            elif parsed.fragment:
                self.links.add('#' + unquote(parsed.fragment))

page = (ROOT / 'index.html').read_text(encoding='utf-8')
gallery = Gallery()
gallery.feed(page)
for target in gallery.links:
    if target.startswith('#'):
        if target[1:] not in gallery.anchors:
            errors.append('Missing anchor: ' + target)
    elif not (ROOT / target).is_file():
        errors.append('Missing linked file: ' + target)

annotations = json.loads((ROOT / 'annotations.json').read_text(encoding='utf-8'))
if len(annotations) != 500 or gallery.articles != 500:
    errors.append('Expected 500 annotations and 500 gallery articles')
if page.count('<h3>Rationales</h3>') != 500:
    errors.append('Expected 500 displayed rationales')
if page.count('original image ↗') != 1000:
    errors.append('Expected 1,000 original-image links')
for annotation in annotations:
    pair_id = annotation['pair_id']
    label = json.loads((ROOT / 'pairs' / pair_id / 'label.json').read_text(encoding='utf-8'))
    if annotation['label'] != label:
        errors.append(pair_id + ': label mismatch')
    for side in ['left', 'right']:
        entity = annotation[side]
        image = ROOT / entity['image_path']
        if not image.is_file() or hashlib.sha256(image.read_bytes()).hexdigest() != entity['sha256']:
            errors.append(pair_id + ': source-image mismatch, ' + side)
    comparison = (ROOT / 'pairs' / pair_id / 'comparison.md').read_text(encoding='utf-8')
    for name in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', comparison):
        if not (ROOT / 'pairs' / pair_id / name).is_file():
            errors.append(pair_id + ': broken comparison image link')
script = re.search(r'<script>(.*?)</script>', page, re.S).group(1)
syntax = subprocess.run(['node', '--check'], input=script, text=True, capture_output=True)
if syntax.returncode:
    errors.append('Gallery script syntax error: ' + syntax.stderr)
if not (ROOT / '.nojekyll').is_file():
    errors.append('Missing .nojekyll')
if (ROOT / '.openai').exists() or (ROOT / 'CNAME').exists():
    errors.append('Unexpected hosting-specific metadata')
if re.search(r'chatgpt\.site|regalscarf14|file:///|[CDE]:[\\/]', page):
    errors.append('Unexpected previous host or local path in the public page')
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts]
report = dict(status='passed' if not errors else 'failed',
    pair_count=len(annotations), gallery_articles=gallery.articles,
    original_images_verified=2 * len(annotations), local_html_targets=len(gallery.links),
    files=len(files), total_bytes=sum(p.stat().st_size for p in files),
    javascript_syntax='passed' if not syntax.returncode else 'failed', errors=errors)
print(json.dumps(report, indent=2))
if errors:
    raise SystemExit(1)
