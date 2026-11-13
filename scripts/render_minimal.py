"""Render the dataset-first gallery from its unchanged pair annotations."""
from pathlib import Path
import html
import json
import math

ROOT=Path(__file__).resolve().parents[1]
annotations=json.loads((ROOT/'annotations.json').read_text(encoding='utf-8'))
registry=json.loads((ROOT/'sources/SOURCE_REGISTRY.json').read_text(encoding='utf-8'))
escape=html.escape
condition_names={
    'numeric_representation':'Numeric representation',
    'geometric_markers':'Geometric markers',
    'symbolic_roles':'Symbolic roles',
    'graphical_roles':'Graphical roles',
}
cards=[]

def image_panel(annotation, side):
    pair_id = annotation['pair_id']
    entity = annotation[side]
    archive = entity.get('image_archive')
    href = escape(archive['url'] if archive else entity['image_path'])
    identifier = f'{pair_id}-{side}'
    if archive:
        attrs = (f'data-archive-url="{href}" data-start="{archive["start"]}" '
                 f'data-length="{archive["length"]}" data-method="{archive["method"]}" '
                 f'data-member="{escape(archive["member"])}"')
        source_link = f'<a data-image="{identifier}" href="{href}" target="_blank" rel="noopener">{side.title()} official archive ↗</a>'
    else:
        attrs = f'loading="lazy" src="{href}"'
        source_link = f'<a href="{href}" target="_blank" rel="noopener">{side.title()} original image ↗</a>'
    panel = (f'<a class="image-panel" href="{href}" target="_blank" rel="noopener" aria-label="Open {pair_id} {side} image">'
             f'<span>{side.title()}</span><img id="{identifier}" {attrs} alt="{pair_id} {side} source image"></a>')
    return panel, source_link

for annotation in annotations:
    pid=annotation['pair_id'];target=annotation['target'];label=annotation['label']
    sources=' / '.join(f"{annotation[s]['dataset']}:{annotation[s]['problem_index']}" for s in ['left','right'])
    datasets=' '.join(sorted({annotation[s]['dataset'] for s in ['left','right']}))
    type_text='Same type' if annotation['type_class']=='same type' else 'Different types'
    left_panel, left_link = image_panel(annotation, 'left')
    right_panel, right_link = image_panel(annotation, 'right')
    cards.append(f'''<article id="{pid}" data-type="{annotation['type_class']}" data-condition="{annotation['condition']}" data-semantic="{annotation['semantic_relation']}" data-datasets="{datasets}">
<h2>{pid}<span>{condition_names[annotation['condition']]}</span></h2>
<p class="meta">{type_text} · {escape(annotation['left']['image_type'])} / {escape(annotation['right']['image_type'])}<br>{escape(sources)}</p>
<div class="pair-images">{left_panel}{right_panel}</div>
<p class="target"><b>Visual target</b> {escape(label['shared_or_similar_visual_information'])}</p>
<details><summary>View label</summary>
<p><b>Same mathematical meanings:</b> <span class="judgment">{label['same_mathematical_meanings']}</span></p>
<p>{escape(label['mathematical_meanings'])}</p>
<h3>Rationales</h3><p>{escape(label['Rationales'])}</p>
<p class="evidence"><b>Left-image evidence:</b> {escape(target['left_evidence'])}<br><b>Right-image evidence:</b> {escape(target['right_evidence'])}</p>
<p class="files">{left_link} · {right_link}<br><a href="pairs/{pid}/label.json">Label JSON</a> · <a href="pairs/{pid}/annotation.json">Full annotation</a></p>
</details></article>''')
template=(ROOT/'scripts/minimal_template.html').read_text(encoding='utf-8')
assert template.count('<!-- PAIRS -->')==1
source_options = []
source_links = []
for source in registry['sources']:
    name = escape(source['dataset'])
    display_name = escape(source.get('display_name', source['dataset']))
    source_options.append(f'<option value="{name}">{display_name}</option>')
    source_links.append(f'<a href="{escape(source["url"])}">{display_name}</a>')
page = (template.replace('PAIR_COUNT', str(len(cards)))
        .replace('PAGE_COUNT', str(math.ceil(len(cards) / 24)))
        .replace('RELEASE_VERSION', escape(registry['release']))
        .replace('<!-- SOURCE OPTIONS -->', ''.join(source_options))
        .replace('<!-- SOURCE LINKS -->', ' · '.join(source_links))
        .replace('<!-- PAIRS -->', '\n'.join(cards)))
(ROOT/'index.html').write_text(page,encoding='utf-8')
print(f'Rendered {len(cards)} dataset cards.')
