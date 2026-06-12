# Checker Coverage

This document summarizes the current coverage of `scripts/check_examples.py`.

The checker is a bounded repository-maintenance tool. It is not schema validation, certification, compliance review, legal review, safety review, fairness review, moral accountability judgment, or production-readiness assessment.

## General checks

For each YAML example, the checker currently inspects:

- required top-level keys
- non-empty `nodes`
- `edges` list presence
- human return-point signals
- `responsibility_boundary.ai_final_responsibility_allowed: false`
- AI final-responsibility flags such as `assumes_final_responsibility`
- formalization-scope excluded-claim signals
- optional `review_metadata` structure when present

## Lifecycle-aware checks

### `originating`

The checker inspects whether the example includes:

- a human-capable `decision_owner`
- a human-capable `stop_authority`
- an empty `repairs` list
- a human return-point signal

This does not mean the originating pathway is complete, safe, compliant, legally valid, morally resolved, or production ready.

### `repaired`

The checker inspects whether the example includes:

- a non-empty `repairs` list
- a human-capable `repair_owner`
- repair-record signals for trigger, repair owner, and repair state
- repair-boundary signals in `formalization_scope`

This does not mean repair is complete in the real world, harm is eliminated, legal responsibility is resolved, or moral responsibility is resolved.

### `suspended`

The checker inspects whether the example includes:

- a top-level `suspension` block
- continuation and closure boundary signals
- required-before-continuation records
- disallowed-interpretation signals

This does not mean suspension is justified in a real-world setting.

### `returning`

The checker inspects whether the example includes:

- a top-level `returning` block
- prior lifecycle-state signal
- automatic-continuation, automatic-closure, and automatic-repair-completion boundary signals
- required-before-next-state records
- disallowed-interpretation signals

This does not mean return is equivalent to continuation, repair completion, closure, or approval.

### `closed`

The checker inspects whether the example includes:

- a top-level `closure` block
- closure basis records
- residual-obligation records
- reopening-condition records
- automatic-reopening, automatic-closure, and AI-closure-authority boundary signals
- closure-specific excluded-claim signals

This does not mean closure erases responsibility history, grants immunity, completes repair, certifies safety, or resolves legal or moral responsibility.

## Optional record-review metadata checks

When an example includes `review_metadata`, the checker now inspects whether:

- `review_tool_version` is present
- `checked_items` is present as a non-empty list
- `unchecked_items` is present as a non-empty list
- `review_result` is present as a mapping
- `review_result.not_claimed` is present as a non-empty list
- `unchecked_items` and `review_result.not_claimed` include non-certifying signals such as legal, safety, compliance, fairness, moral, and production boundaries

These checks are optional and apply only when `review_metadata` is present.

They remain bounded structural checks. A pass does not certify the record, the workflow, the system, the organization, or the real-world decision.

## Review-result schema and fixture coverage

`spec/review-result.schema.yaml` defines the minimum structure for bounded review-result outputs.

`fixtures/review-results/record-review-result-minimal.yaml` provides a small readable review-result output fixture.

The current checker does not read `fixtures/review-results/*.yaml`.

The current checker also does not validate `spec/review-result.schema.yaml`.

This separation is intentional for now:

- pathway examples remain under `examples/*.yaml`
- review-result output fixtures remain under `fixtures/review-results/*.yaml`
- `scripts/check_examples.py` remains focused on pathway examples
- review-result validation is not yet implemented

Future review-result checking should be added separately, for example by a future `scripts/check_review_results.py`, only after the review-result schema and fixture boundaries remain stable.

A future review-result checker must remain bounded and structural. It must not turn a review result into legal validation, safety certification, compliance certification, fairness certification, moral resolution, institutional certification, production approval, or AI final-responsibility transfer.

## Responsibility Pathway record review alignment

`docs/responsibility-pathway-record-review.md` defines a plain-language review and recheck guide for Responsibility Pathway records.

`spec/pathway.schema.yaml` now includes review aliases, review metadata, and record-review alignment notes for concepts such as:

- `pathway_id`
- `schema_version`
- `ai_support_nodes`
- `human_or_institutional_return_point`
- `stop_authority`
- `evidence_records`
- `repair_record`
- `suspension_condition`
- `return_condition`
- `closure_record`
- `reopening_condition`
- `excluded_claims`
- `review_tool_version`

`spec/review-result.schema.yaml` defines the bounded review-result output structure.

`examples/record-review-minimal.yaml` provides a small readable record-review example that follows the existing originating lifecycle checker path.

`fixtures/review-results/record-review-result-minimal.yaml` provides a review-result output fixture that is not currently consumed by the checker.

The current checker has been minimally expanded to inspect optional `review_metadata` structure when present. It still does not fully validate every record-review field, and it does not validate review-result fixtures.

Future checker work should remain bounded to structural signals and must not treat a review pass as legal validity, safety, compliance, fairness, moral resolution, certification, or production readiness.

## Current example coverage map

| Example | Declared lifecycle state | Lifecycle-specific checker rule | Optional review metadata check |
| --- | --- | --- | --- |
| `examples/minimal-pathway.yaml` | `originating` | yes | no |
| `examples/record-review-minimal.yaml` | `originating` | yes | yes |
| `examples/repair-flow.yaml` | `repaired` | yes | no |
| `examples/suspended-pathway.yaml` | `suspended` | yes | no |
| `examples/returning-pathway.yaml` | `returning` | yes | no |
| `examples/closed-pathway.yaml` | `closed` | yes | no |

## Review-result fixture coverage map

| Fixture | Schema reference | Current checker coverage |
| --- | --- | --- |
| `fixtures/review-results/record-review-result-minimal.yaml` | `spec/review-result.schema.yaml` | not yet checked |

## Interpretation boundary

A checker pass means only that the example satisfies the bounded structural rules implemented by the current checker version.

A checker pass does not mean that the example is correct in all contexts, semantically complete, legally valid, ethically valid, safe, fair, compliant, certified, approved, or ready for production use.

The human author or maintainer remains responsible for deciding whether an example, schema, document, or public claim should be changed, published, or relied upon.
