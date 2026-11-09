"""Render the dataset-first gallery from its unchanged pair annotations."""
from pathlib import Path
import html
import json

ROOT=Path(__file__).resolve().parents[1]
annotations=json.loads((ROOT/'annotations.json').read_text(encoding='utf-8'))
escape=html.escape
condition_names={
    'numeric_representation':'Numeric representation',
    'geometric_markers':'Geometric markers',
    'symbolic_roles':'Symbolic roles',
    'graphical_roles':'Graphical roles',
}
cards=[]
for annotation in annotations:
    pid=annotation['pair_id'];target=annotation['target'];label=annotation['label']
    sources=' / '.join(f"{annotation[s]['dataset']}:{annotation[s]['problem_index']}" for s in ['left','right'])
    datasets=' '.join(sorted({annotation[s]['dataset'] for s in ['left','right']}))
    type_text='Same type' if annotation['type_class']=='same type' else 'Different types'
    cards.append(f'''<article id="{pid}" data-type="{annotation['type_class']}" data-condition="{annotation['condition']}" data-semantic="{annotation['semantic_relation']}" data-datasets="{datasets}">
<h2>{pid}<span>{condition_names[annotation['condition']]}</span></h2>
<p class="meta">{type_text} · {escape(annotation['left']['image_type'])} / {escape(annotation['right']['image_type'])}<br>{escape(sources)}</p>
<div class="pair-images"><a class="image-panel" href="{escape(annotation['left']['image_path'])}" target="_blank" rel="noopener" aria-label="Open {pid} left image"><span>Left</span><img loading="lazy" src="{escape(annotation['left']['image_path'])}" alt="{pid} left source image"></a><a class="image-panel" href="{escape(annotation['right']['image_path'])}" target="_blank" rel="noopener" aria-label="Open {pid} right image"><span>Right</span><img loading="lazy" src="{escape(annotation['right']['image_path'])}" alt="{pid} right source image"></a></div>
<p class="target"><b>Visual target</b> {escape(label['shared_or_similar_visual_information'])}</p>
<details><summary>View label</summary>
<p><b>Same mathematical meanings:</b> <span class="judgment">{label['same_mathematical_meanings']}</span></p>
<p>{escape(label['mathematical_meanings'])}</p>
<h3>Rationales</h3><p>{escape(label['Rationales'])}</p>
<p class="evidence"><b>Left-image evidence:</b> {escape(target['left_evidence'])}<br><b>Right-image evidence:</b> {escape(target['right_evidence'])}</p>
<p class="files"><a href="{escape(annotation['left']['image_path'])}" target="_blank" rel="noopener">Left original image ↗</a> · <a href="{escape(annotation['right']['image_path'])}" target="_blank" rel="noopener">Right original image ↗</a><br><a href="pairs/{pid}/label.json">Label JSON</a> · <a href="pairs/{pid}/annotation.json">Full annotation</a></p>
</details></article>''')
template=(ROOT/'scripts/minimal_template.html').read_text(encoding='utf-8')
assert template.count('<!-- PAIRS -->')==1
(ROOT/'index.html').write_text(template.replace('<!-- PAIRS -->','\n'.join(cards)),encoding='utf-8')
print(f'Rendered {len(cards)} dataset cards.')
