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
stats = json.loads((ROOT / 'dataset_stats.json').read_text(encoding='utf-8'))
total = len(annotations)
archive_count = sum('image_archive' in a[side] for a in annotations for side in ('left', 'right'))
if total != stats['pair_count'] or gallery.articles != total:
    errors.append('Dataset statistics, annotations and displayed pairs disagree')
if page.count('<h3>Rationales</h3>') != total:
    errors.append('Expected one rationale per pair')
if page.count('original image ↗') != 2 * total - archive_count or page.count('official archive ↗') != archive_count:
    errors.append('Unexpected count of original-image or source-archive links')
for annotation in annotations:
    pair_id = annotation['pair_id']
    label = json.loads((ROOT / 'pairs' / pair_id / 'label.json').read_text(encoding='utf-8'))
    if annotation['label'] != label:
        errors.append(pair_id + ': label mismatch')
    for side in ['left', 'right']:
        entity = annotation[side]
        archive = entity.get('image_archive')
        if archive:
            if (entity['image_path'] is not None or archive['member'] != entity['original_relative_path']
                    or archive['start'] < 0 or archive['length'] <= 0 or archive['method'] not in (0, 8)):
                errors.append(pair_id + ': invalid source archive reference, ' + side)
            if any((ROOT / 'pairs' / pair_id).glob(f'{side}.*')) or (ROOT / 'pairs' / pair_id / 'preview.jpg').exists():
                errors.append(pair_id + ': archive-hosted image copied to the site, ' + side)
            continue
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
archive_syntax = subprocess.run(['node', '--check', str(ROOT / 'scripts/archive_images.js')], capture_output=True, text=True)
if archive_syntax.returncode:
    errors.append('Source archive script syntax error: ' + archive_syntax.stderr)
if not (ROOT / '.nojekyll').is_file():
    errors.append('Missing .nojekyll')
if (ROOT / '.openai').exists() or (ROOT / 'CNAME').exists():
    errors.append('Unexpected hosting-specific metadata')
if re.search(r'chatgpt\.site|regalscarf14|file:///|[CDE]:[\\/]', page):
    errors.append('Unexpected previous host or local path in the public page')
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts]
report = dict(status='passed' if not errors else 'failed',
    pair_count=len(annotations), gallery_articles=gallery.articles,
    local_original_images_verified=2 * total - archive_count, archive_image_references=archive_count,
    local_html_targets=len(gallery.links),
    files=len(files), total_bytes=sum(p.stat().st_size for p in files),
    javascript_syntax='passed' if not (syntax.returncode or archive_syntax.returncode) else 'failed', errors=errors)
print(json.dumps(report, indent=2))
if errors:
    raise SystemExit(1)
