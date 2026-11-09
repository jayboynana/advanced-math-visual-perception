# Advanced Mathematical Visual Perception · GitHub Pages

This repository hosts the complete static website for **500 mathematical image pairs**. Each pair has one shared or similar visual target, English mathematical meanings, a yes/no judgment, and a rationale. Images are sampled from MathVerse, MathVista, and MATH-VISION; annotations are AI-reviewed drafts awaiting independent human review.

The website uses relative asset paths, so it works at a GitHub Pages project URL. No Node build, external image server, or application backend is required.

## Publish with GitHub Pages

In the repository settings, open **Pages**, choose **Deploy from a branch**, select **main** and **/(root)**, and save. The empty .nojekyll file serves the prepared HTML and data files directly.

The repository contains all 500 pair previews, 1,000 original-image occurrences, English labels, annotation exports, and source attribution. Full upstream corpora, historical archives, question-answer collections, and machine credentials are excluded.

To validate a local copy, run python scripts/validate_pages.py with Python and Node.js available. Changes pushed to the configured publishing branch are deployed by GitHub Pages.

---

# New Visual Perception Benchmark · v0.3.0 · English

Each of the 500 image pairs has exactly one shared or similar visual target. Its label explains the mathematical meaning in each image, records a yes/no judgment, and gives the rationale. The meanings field remains a direct explanation of the two images, without an appended conclusion sentence. The original AVP0001–AVP0100 are preserved; AVP0101–AVP0500 are new pairs.

## Browse and inspect

- Open `index.html` for the offline English browser, with filters for type, condition and semantic judgment.
- `pairs_summary.csv`: Excel-compatible UTF-8 BOM table, one target per row.
- `labels.jsonl`: four-field labels for all pairs.
- `annotations.json` / `manifest.jsonl`: full annotations and provenance.
- `evaluation_inputs.jsonl`: image paths, one specified target and a uniform English prompt, without reference meanings or answers.
- `PROBLEM_STATEMENT.md`, `ANNOTATION_GUIDE.md`, and `BENCHMARK_PROTOCOL.md`: task definitions and evaluation conventions.

## Directory layout

```text
type/
  same type/AVPxxxx/
  different type/AVPxxxx/
condition/
  numeric_representation/AVPxxxx/
  geometric_markers/AVPxxxx/
  symbolic_roles/AVPxxxx/
  graphical_roles/AVPxxxx/
pairs/AVPxxxx/                 # Canonical current samples
review/en_*.json               # Original 100 English specifications
review/expansion_*.json        # Additional 400 English specifications
sources/MathVerse/             # Fixed upstream data and provenance
sources/MathVista/             # Official testmini images and records
sources/MathVision/            # Official MATH-VISION test images and records
archive/v0.1/                  # Earlier multi-observation version
archive/v0.2-zh/               # Previous Chinese outputs and generator snapshots
```

Type and condition directories are two views of the same 500 pairs. Each folder contains `left` and `right` images with their native extensions, `preview.jpg`, `label.json`, `annotation.json`, and `comparison.md`. Use `annotation.json` or `evaluation_inputs.jsonl` for the exact image paths.

`label.json` has exactly four English keys:

```json
{
  "shared_or_similar_visual_information": "One selected visual target",
  "mathematical_meanings": "Left image: ... Right image: ...",
  "same_mathematical_meanings": "yes",
  "Rationales": "Evidence explaining why the selected meanings match or differ."
}
```

`same_mathematical_meanings` is exactly the lowercase string `yes` or `no`; `Rationales` preserves the capital R and provides the reason or evidence. These fields concern the same single target, not additional targets. The internal Boolean `target.same_meaning` is retained for compatibility and must agree with the yes/no label. CSV exports contain both the legacy Boolean column and the new string field.

## Conditions and counts

| Directory | Focus | Pairs |
|---|---|---:|
| numeric_representation | Numeric representation and conversion | 125 |
| geometric_markers | Geometric markers | 125 |
| symbolic_roles | Mathematical roles of symbols | 125 |
| graphical_roles | Mathematical roles of graphical elements | 125 |

- Pairs: 500; targets: 500; exactly one per pair.
- Unique source records across datasets: 387.
- Unique decoded images: 383.
- Selected source-record counts: {"MathVerse": 147, "MathVista": 167, "MathVision": 73}.
- Pairs containing each source (these counts overlap): {"MathVerse": 252, "MathVision": 100, "MathVista": 293}.
- Cross-dataset pairs: 145.
- Image-type counts: {"same type": 302, "different type": 198}.
- Semantic judgments: {"same_meaning": 249, "different_meaning": 251}.
- Maximum reuse of one source image: 11 pairs.
- Maximum reuse after decoded-image grouping: 11 pairs.

Joint type/meaning counts: {"same type|same_meaning": 216, "same type|different_meaning": 86, "different type|different_meaning": 165, "different type|same_meaning": 33}. Type and semantic labels are correlated in this pilot. Compute balanced accuracy within each image-type group and then macro-average; later versions can add cross-type matching-meaning and same-type differing-meaning examples.

## Source and annotation status

Images are sampled from the official [MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse), [MathVista](https://huggingface.co/datasets/AI4Math/MathVista), and [MATH-VISION](https://huggingface.co/datasets/MathLLMs/MathVision) datasets. Fixed upstream revisions, split names, IDs, native formats, source metadata and SHA-256 hashes are retained. Original embedded image bytes are unchanged. Previews are review composites. See `sources/SOURCE_REGISTRY.json` and each source's `PROVENANCE.md`.

Visual types follow image content. Unit-circle and angle-circle diagrams, closed circles/ellipses and conics explicitly annotated with foci/vertices/center are geometry; ordinary function/relation plots are function. Solid diagrams, statistical charts, and symbolic expressions receive their own visual types where applicable. Upstream subject labels are stored separately.

This is an **AI visual-review draft, not independently double-annotated or adjudicated by humans**. Semantic judgments concern the selected local target, rather than identity of whole images, points or functions. Hidden values are not solved and original problem answers do not complete visual labels. No train/dev/test split or model-performance experiment has been run.

See `sources/selected_images_v03.json` for the current selected source records and `review/exact_image_groups.json` for exact decoded-image grouping. Public datasets can share underlying diagrams: record counts are not necessarily independent-image counts. Exact decoded-image pairs are deduplicated; remaining source-family and near-duplicate relationships must be grouped before any future split. Original Chinese authoring specifications remain in `review/v02_*.json` as translation references. Historical outputs in `archive` are not active samples.

Sampling is targeted rather than a random or source-balanced benchmark sample. In this release MATH-VISION additions focus on geometric markers, while MathVista additions span numerical, symbolic and graphical targets. Source-by-condition coverage is recorded in `dataset_stats.json`; future expansion should balance source coverage within each condition before interpreting differences between conditions as model capability gaps.

## Rebuild and validate

Edit `review/en_*.json` for original pairs or `review/expansion_*.json` for added pairs, then run:

```powershell
python scripts/build_dataset.py
python scripts/write_docs.py
python scripts/validate_dataset.py
```

For numeric targets, compare the given value and specific role. For unknown variables and names, compare their selected symbolic function without claiming equality of unknown values. Resolve semantic-scope disputes through annotation review before scoring model errors.
