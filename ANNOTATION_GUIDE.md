# Single-Target Annotation Guide · v0.3.0

1. Each sample has one target, visibly present and locatable in both images. Complete absence is not a differing-meaning example.
2. Labels have exactly `shared_or_similar_visual_information`, `mathematical_meanings`, `same_mathematical_meanings` and `Rationales`. The meanings field contains only `Left image: ... Right image: ...`, without an appended conclusion. The judgment is the string `yes` or `no`; `Rationales` explains the concrete basis. `annotation.target` structures the same target and retains a compatible Boolean judgment and rationale.
3. Evidence specifies location, visible content and attachment. Do not add unrelated similarities or whole-image differences. Disambiguate repeated letters by location.
4. Numeric targets require matching values and local roles, including explicit unit conversion. π/4 radians and 45° as angles match; π/4 as an angle and an x-coordinate differ. Do not extract arbitrary digits from longer values.
5. For unknown variables and names, compare the selected local function. Two x labels can be angle variables without asserting equal angles. Two f labels can name curves without making those functions identical. Angle and length variables differ.
6. Two right-angle squares can encode perpendicularity. A dedicated angle square differs from a coordinate-grid cell, even though the grid is orthogonal: the cell supports coordinate spacing and reading.
7. Require agreement of specific graphical function. A geometric auxiliary dashed line differs from a dashed function curve. A length-dimension arrow differs from a wave-period arrow; “both auxiliary” or “both show a span” is insufficient.
8. Matching meaning concerns conventional function or content, not object identity across images. Avoid disputed granularity and document scope for review.
9. Use visible evidence, conventional markers and explicit simple normalization. Do not estimate angles from pixels, solve unmarked lengths, infer exact curve formulas, or import hidden facts from the original question or answer.
10. Do not alter source images. Retain source IDs, versions, upstream subjects, visual types and hashes. Each unordered pair appears once, with distinct source problems and pixel images.
11. Type and condition folders mirror the same pairs. Each pair has one primary condition. Earlier multi-observation arrays and focus-presence fields are excluded.
12. Status is `ai_visually_reviewed_draft`, without human double annotation or adjudication. Group future splits and confidence intervals by source-image/problem families because images are reused.
