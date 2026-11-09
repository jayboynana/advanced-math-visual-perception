# MATH-Vision source record

- Official dataset: https://huggingface.co/datasets/MathLLMs/MathVision
- Official project repository: https://github.com/mathllm/MATH-V/
- Immutable Hugging Face revision: `2837ddb3f13abaf6b3997c12d80753e5470bd46a`
- Source split/config: `test` / `default`; 3,040 records.
- Download: `data/test-00000-of-00001-3532b8d3f1b4047a.parquet` at that revision.
- Local parquet SHA-256: `bcb3078a77bd6ee0e4e22135d53b9a48604fcd1b62dec69e279e812ba4dd7d37`.
- Upstream README SHA-256: `b4ad8098a1cf1fca7b60b746398252a6b3226e61f770c71e296d453f3cea57d6`.

The original `decoded_image.bytes` are extracted without re-encoding, cropping,
or annotation overlays. Native file extensions are preserved. `metadata.json`
keeps the public non-image records; `catalog.json` records original IDs, dimensions,
hashes, revision, source paths, subjects, and metadata. `hf_api_snapshot.json` and
`README.upstream.md` preserve the upstream discovery and dataset card. `acquire.py`
reproduces extraction from the pinned source.

The upstream dataset card declares `mit`. This is a record of that declaration,
not a separate rights clearance for every competition illustration. Per-problem
competition/book URLs are not supplied by this source and have not been invented.

Image types in the full source catalog are provisional suggestions from the source
subject. Selected pairs override those suggestions after visual inspection. For
example, coordinate drawings containing a triangle remain geometry, and a cube
net is solid geometry. Contact sheets are derived review aids; benchmark images
remain original image bytes. Pair annotations are AI-reviewed drafts, pending
independent human verification.
