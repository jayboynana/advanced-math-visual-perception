# Mathematical Visual Perception Dataset

[Browse the dataset](https://jayboynana.github.io/advanced-math-visual-perception/)

1,000 image pairs, four conditions, and English labels. Each pair includes two original images, one visual target, mathematical meanings, a yes/no judgment, and a rationale. Labels are an AI-reviewed draft.

| Condition | Pairs |
|---|---:|
| Numeric representation | 250 |
| Geometric markers | 250 |
| Symbolic roles | 250 |
| Graphical roles | 250 |

[Annotations](annotations.json) · [Labels](labels.jsonl) · [CSV](pairs_summary.csv)

Sources include [MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse), [MathVista](https://huggingface.co/datasets/AI4Math/MathVista), [MATH-VISION](https://huggingface.co/datasets/MathLLMs/MathVision), [MV-MATH](https://huggingface.co/datasets/PeijieWang/MV-MATH), [VisioMath](https://github.com/Nefefilibata/VisioMath), [DynaMath](https://huggingface.co/datasets/DynaMath/DynaMath_Sample), and [We-Math](https://huggingface.co/datasets/We-Math/We-Math).

The gallery fetches VisioMath images from the pinned official ZIP when they first appear on screen. The annotations identify the archive URL and each image's member path. The We-Math images are subject to the upstream noncommercial license. [Source records](sources/SOURCE_REGISTRY.json)

GitHub Pages serves this static gallery from the `main` branch root. After changing annotations, run `python scripts/render_minimal.py` and `python scripts/validate_pages.py`.
