# Expansion review record · v0.3.0

The release preserves the original 100 pairs and adds 100 pairs in each of the four conditions. Each added pair was authored from a selected visible cue and image context. Original source answers were not used to infer hidden values for labels.

## Visual review

- Numeric representation: 100 pairs reviewed using MathVista geometry/function contact sheets and selected original images. Ambiguous square-interior numbers were removed rather than assigning an area meaning from a question. Direct degree/radian and yard/foot conversions, coordinate components, coefficients, exponents, constants and angle indices are included.
- Geometric markers: 100 pairs reviewed using selected MATH-VISION originals and marker banks. All 100 decoded pairs were checked for self-pairs and duplicates. A second AI reviewer checked 22 stratified pairs against the originals without finding an additional error.
- Symbolic roles: 100 pairs authored from a visible-occurrence inventory. An independent AI reviewer read all 100 labels and checked approximately 30 selected source contexts. Initial authoring corrections removed nonexistent axis-letter cues and corrected a point label from D to C. Parentheses, letter attachment, matrices, reference points, variables and function names were checked.
- Graphical roles: all 100 pair previews reviewed. A second AI reviewer inspected all previews and deeply checked 26 varied cases. Its correction to V03GR027 selects the visible R2 region between the sine and cosine curves. Other corrections distinguish a hyperbola from an ellipse, avoid assuming sampled functions are empirical charts, and replace an axis with no visible arrowhead.

## Integration

- Two collisions between condition drafts were replaced with other visually checked pairs. The original 100 pair IDs, images, meanings and four-field labels are retained.
- Namespaced source IDs prevent an ID in one upstream dataset from colliding with the same numeral in another dataset.
- Existing image filenames are preserved along with their bytes. MathVerse image 626 is named with a PNG extension upstream but contains JPEG bytes; its inherited AVP0011 path remains unchanged. Added files use an extension matching the actual encoded format.
- All 500 unordered source pairs and unordered decoded-RGB image pairs are distinct. No pair compares an image with an exact copy of itself.
- Four selected MathVista source-ID groups contain identical decoded images: 154/950, 308/770, 329/973, and 671/926. Their pair partners differ. These are recorded as groups rather than represented as independent images in the decoded-image count.
- Reference exports, both classification views, native image paths, CSV, evaluation inputs and the English offline gallery are generated together. The evaluation input export excludes reference meanings, judgments, evidence and rationales.

`validation_report.json` records structural/provenance validation. `exact_image_groups.json` records exact pixel groups for future splitting. Source-family and near-duplicate adjudication, independent human double annotation, train/dev/test assignment, and model evaluation remain future work. AI cross-review is not human gold certification.

Source coverage is intentionally targeted rather than balanced within every condition. MATH-VISION additions focus on markers. Per-condition source counts and the remaining type/judgment correlation are disclosed in the dataset statistics and guide.
