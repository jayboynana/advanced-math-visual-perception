# Minimal Evaluation Protocol · v0.3.0

## Task

Supply two source images, one specified shared or similar target and the uniform English prompt. Ask for both mathematical meanings, a yes/no matching-meaning judgment, and the rationale or evidence. `evaluation_inputs.jsonl` excludes reference meanings, judgments, rationales, labels and original answers.

Specifying the target aligns responses with the single-target annotation. The model still finds and interprets it; reference evidence descriptions are not supplied.

Suggested output:

```json
{"pair_id":"AVP0001","left_meaning":"...","right_meaning":"...","same_mathematical_meanings":"yes","Rationales":"..."}
```

## Scoring

Score `same_mathematical_meanings` as a yes/no decision and report accuracy, balanced accuracy and macro-F1 by condition and image-type group. Prefer balanced accuracy within same-type and different-type groups followed by macro-averaging, to reduce benefits from the pilot's type-label correlation. Missing responses count as errors; duplicate or unknown IDs are format errors. Valid decision strings are exactly `yes` and `no`.

Review both meanings, object attachments and `Rationales` separately. A rationale must connect the selected visual evidence to the mathematical functions, rather than merely repeat yes/no. Exact natural-language string matching is inappropriate. Automatic explanation adjudication is not implemented, and a correct yes/no guess alone is not evidence of full understanding.

Complete success requires correct target localization, both contextual meanings and the semantic judgment. Joint scores require reviewed evidence beyond the Boolean answer.

## Diagnostics and limitations

Separate questions about visible form can help distinguish reading from contextual-interpretation failures. This task alone cannot identify which stage caused an error.

No model evaluation has been run. Fix model versions, resolution, prompts and decoding. Do not expose reference labels, source answers or expanded browser cards as model input.

Image type does not determine the semantic label; every condition includes both classes. There is no train/dev/test split. Group source images and variants before splitting. Public images may have entered model pretraining; no contamination-free claim is made.
