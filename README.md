# Mathematical Visual Perception Dataset

[Browse the dataset](https://jayboynana.github.io/advanced-math-visual-perception/)

500 image pairs, four conditions, and English labels. Each pair includes its original images, one visual target, mathematical meanings, a yes/no judgment, and a rationale. Labels are an AI-reviewed draft.

| Condition | Pairs |
|---|---:|
| Numeric representation | 125 |
| Geometric markers | 125 |
| Symbolic roles | 125 |
| Graphical roles | 125 |

[Annotations](annotations.json) · [Labels](labels.jsonl) · [CSV](pairs_summary.csv)

Sources: [MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse), [MathVista](https://huggingface.co/datasets/AI4Math/MathVista), and [MATH-VISION](https://huggingface.co/datasets/MathLLMs/MathVision). Original images retain their source attribution and upstream terms; see [source records](sources/SOURCE_REGISTRY.json).

The prepared website is served from the `main` branch root with `.nojekyll`. After changing annotations, run `python scripts/render_minimal.py`, then `python scripts/validate_pages.py`, and push the update.
