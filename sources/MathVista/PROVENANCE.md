# MathVista source provenance

- Official dataset: https://huggingface.co/datasets/AI4Math/MathVista
- Official project: https://github.com/lupantech/MathVista
- Fixed Hugging Face revision: `2b6ad69445fbb5695c9b165475e8decdbeb97747`.
- Acquired: 2026-11-09 (Asia/Shanghai).
- Configuration: default; split: testmini; 1,000 source records.
- Downloaded parquet: `data/testmini-00000-of-00001-725687bf7a18d64b.parquet`.
- The local `images/` files preserve the exact embedded `decoded_image.bytes` payloads from that parquet. No cropping, recoloring, text overlay, image generation, or recompression was applied. Native extensions reflect the encoded image format, which may differ from the upstream `image` field's extension.
- `records.json` retains the non-image fields of all source rows. Question answers are not included in evaluation inputs and are not required to interpret the selected image-only targets.
- `catalog.json` maps namespaced IDs to local paths, revision, source IDs, metadata, image dimensions, and SHA-256 values. `SOURCE_IMAGE_MANIFEST.jsonl` mirrors this catalog. Image type is visually assigned for selected images; unused entries can remain unclassified.
- `README.md`, `source.json`, `annot_testmini.json`, and `hf_api_snapshot.json` preserve official release metadata. `acquisition_hashes.json` records downloaded file sizes and SHA-256 values.
- The official dataset card declares CC BY-SA 4.0. MathVista combines multiple underlying datasets with their own original sources; consult the saved README and source.json for source-specific provenance and terms. The benchmark's new English pair annotations do not claim ownership of the source images.
- Source problem IDs are retained, without inventing unavailable original textbook page IDs or URLs.

The new pair annotations are AI visually reviewed drafts pending independent human review. Review contact sheets are derived browsing aids; only unmodified individual source images are used as model inputs.
