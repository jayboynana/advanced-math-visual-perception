# We-Math source record

- [Official Hugging Face dataset card at the acquired revision](https://huggingface.co/datasets/We-Math/We-Math/tree/527c44d4d94c4e3c7c98157460146a8b18c8420a)
- [Official project repository](https://github.com/We-Math/We-Math)
- [Qiao et al., We-Math, ACL 2025](https://arxiv.org/abs/2407.01284)
- Config `default`, split `testmini`, 1,740 rows and 1,010 distinct embedded image byte hashes.
- Source parquet SHA-256 `bb16b217ec8ca2f4cd8aa5f1fb041896d9a5341735e0ae9be236982ccd0b2a4b`.
- Acquired 2026-11-13 (Asia/Shanghai).

The upstream card declares [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). The source benchmark is credited to Qiao et al. and the We-Math authors. This local dataset retains original image payloads and adds separate pair selections and semantic annotations. Attribution and noncommercial terms apply to the sourced materials. The upstream declaration does not independently resolve third-party rights in every illustration.

`acquire.py` extracts the original `image_path.bytes` from the pinned parquet. The upstream `question number` uniquely identifies the 1,740 rows, while the upstream `ID` groups related step variants and can repeat. The catalog preserves the group ID, step variant, original embedded path, dimensions, byte hash, and revision. Preview contact sheets are for visual review. The catalog leaves visual types unclassified until the corresponding source is visually reviewed in a pair.
