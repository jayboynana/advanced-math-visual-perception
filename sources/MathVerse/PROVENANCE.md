# MathVerse 数据来源与版本记录

本文件记录本轮 100 对跨图视觉感知试验所使用的 **MathVerse testmini / Vision Dominant 图像池**。核验日期：2026-11-03（Asia/Shanghai）。这是对已发布 MathVerse 资源的本地追溯记录，不表示本试验拥有全部上游图片的独立版权。

## 1. 官方发布来源

- 论文：[MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](https://arxiv.org/abs/2403.14624)，ECCV 2024。
- 官方项目页：[MathVerse](https://mathverse-cuhk.github.io/)。
- 官方 GitHub：[ZrrSkywalker/MathVerse](https://github.com/ZrrSkywalker/MathVerse)。
- 官方 Hugging Face 数据集：[AI4Math/MathVerse](https://huggingface.co/datasets/AI4Math/MathVerse)。

官方仓库 README 的 Data Usage 部分说明，公开 testmini 包含 788 道原题；testmini.json 为每题的五个有图版本，共 3,940 条记录。另有 788 条 Text Only 记录，位于单独的 testmini_text_only 配置/文件中。本轮未使用 Text Only、未将同题不同版本当成不同原题。

## 2. 本轮使用的固定快照

本地获取脚本最初从 resolve/main 下载；后续通过 Git blob 和 LFS SHA-256 核对，确认本地三个原始文件**逐字节对应**以下固定 revision。因此即使 main 以后变化，也可按固定链接复现。

- Hugging Face repo：AI4Math/MathVerse。
- 固定 HF revision：**3bc86196678bad115a923d2851c6821dbe235939**。
- HF API 的 lastModified：2025-05-15T05:58:46Z。
- 固定 GitHub 参考 revision：**937b090597aeafb8e82b35d310a4bc5b9e2ea29d**。GitHub 快照用于保留发布说明与 LICENSE；图像和题目 JSON 实际来自 HF。
- 使用配置/数据划分：config=testmini，split=testmini。
- 选用的图像版本：**Vision Dominant**；其 image 字段均为 images_version_5/image_N.png。
- 本地展开位置：images/images_version_5/image_N.png。
- 不使用题干、query_wo、query_cot 或 answer 来替代图像中的可见标注；这些字段属于上游解题数据，亦不构成本试验的视觉真值。

| 本地文件 | 固定下载 URL | 字节数 | SHA-256 |
|---|---|---:|---|
| testmini.json | [固定 JSON](https://huggingface.co/datasets/AI4Math/MathVerse/resolve/3bc86196678bad115a923d2851c6821dbe235939/testmini.json) | 5,130,700 | f4ce9b18d111b23d5950dcbc8f377c6a05955a458db6a3103aec706fa63b0e9b |
| images.zip | [固定图像包](https://huggingface.co/datasets/AI4Math/MathVerse/resolve/3bc86196678bad115a923d2851c6821dbe235939/images.zip) | 136,055,983 | 40de79d29048e7a8d37e3307cd2ca0f2e94001167e3a395167c4ee4f6fb58f92 |
| README.md | [固定数据卡](https://huggingface.co/datasets/AI4Math/MathVerse/resolve/3bc86196678bad115a923d2851c6821dbe235939/README.md) | 6,151 | ab1bc7664ebbc929ca216bbe6c74e15999864c7e973ed755fce0a983fa18bd0f |

核对方式：

- testmini.json 的 Git blob SHA-1 为 af5ffc96b71c55deb72ee10d13face6c01b7334a，匹配 HF tree API。
- README.md 的 Git blob SHA-1 为 a35dcc1965ec8f91cce30d0d2dedff0b5ec9453d，匹配 HF tree API。
- images.zip 的本地 SHA-256 与 HF LFS oid 完全一致。
- Git blob SHA-1 含 Git 的 blob 头部，不是直接对裸文件执行 SHA-1 得到的值。

API 原始快照与 GitHub 许可文件保存在 upstream_snapshots/；便于审计，不作为视觉标注答案。

## 3. 原题 ID 与图像 ID

保留上游的三个字段，不能互相替代：

- problem_index：**MathVerse 内部原题 ID**，同一道题的不同版本共享该 ID。本轮去重、分组均应使用该字段。
- sample_index：MathVerse 版本样本 ID；题号相同、版本不同，sample_index 不同。
- image：具体图像相对路径；与 problem_version 一起确定本轮实际输入图。

例如：

| MathVerse 原题 ID | 版本样本 ID | problem_version | 图像成员路径 | metadata.source |
|---|---|---|---|---|
| 439 | 2194 | Vision Dominant | images_version_5/image_439.png | Geo2D_collected |
| 530 | 2649 | Vision Dominant | images_version_5/image_530.png | Functions_collected |

SOURCE_IMAGE_MANIFEST.jsonl 记录全部 788 张候选图的这些 ID、原始 source/subject/subfield、固定来源 URL、图像 SHA-256 和归档内路径。最终实际选图可据此回溯。

**限制**：发布的 JSON 仅提供 metadata.source 等来源名称，没有逐题的 GeoQA/Geometry3K/教材原始题号或网页 URL。因此 problem_index=439 只能称“MathVerse 原题 439”，不能声称它也是某本教材的第 439 题。manifest 中 upstream_original_problem_id 和 upstream_original_url 保留为 null，未猜测补全。

按 788 个 Vision Dominant 原题去重，本地 metadata.source 统计为：

| 上游来源标记 | 原题数 |
|---|---:|
| GeoQA | 197 |
| Geo2D_collected | 147 |
| Geometry3K | 129 |
| Geo3D_collected | 119 |
| Functions_collected | 161 |
| GEOS | 35 |
| 合计 | 788 |

## 4. 许可记录与复用边界

- 本次下载的 HF README 数据卡在 YAML 中标注 **license: mit**；这是发布者的数据卡声明。
- 固定 GitHub [LICENSE](https://github.com/ZrrSkywalker/MathVerse/blob/937b090597aeafb8e82b35d310a4bc5b9e2ea29d/LICENSE) 为 MIT，署名 Copyright (c) 2024 Renrui Zhang；本地原样保存于 upstream_snapshots/GitHub_LICENSE.txt。
- **上述声明不应被扩大解释为“所有上游教材、竞赛、网站及既有数据集图像都具有无条件再发布许可”。** 图像来自多个来源，当前公开元数据未给出逐图上游许可或权利链。
- 本轮保留来源与原文件，不移除原图署名；如对外发布独立派生数据集，应按来源进一步确认可再分发范围，保留 MathVerse 与必要上游引用、许可声明。对无法核清的图片，可发布匹配标注及固定原题 ID/下载脚本而不重分发图片。
- 本文件没有为自建标注层指定许可证，也没有给第三方原图重新授权。

## 5. 本轮图像使用约定

选图以 MathVerse 发布的 Vision Dominant 原图为证据；“geometry / function / solid_geometry”为本试验的**视觉类型**，不必逐字等同于原 metadata.subject。例如 metadata.subject=Functions 的单位圆图，可在本试验视觉类型中标为 geometry，但仍保存原始 subject。

联系表仅用于AI视觉审阅，非人工双人标注；细节已回看相应原图。数值等价、符号对应、数学角色或结构关系由本轮另行标注，上游解题答案不直接用作这些标签。没有因数值相同而默认角色、单位或完整坐标相同。

