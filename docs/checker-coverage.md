# Checker Coverage

This document summarizes the current coverage of bounded repository-maintenance checkers.

The checkers are bounded repository-maintenance tools. They are not schema validation systems, certification processes, compliance reviews, legal reviews, safety reviews, fairness reviews, moral accountability judgments, or production-readiness assessments.

## `scripts/check_examples.py`

`scripts/check_examples.py` checks pathway examples under `examples/*.yaml`.

### General checks

For each YAML example, the checker currently inspects:

- required top-level keys
- non-empty `nodes`
- `edges` list presence
- human return-point signals
- `responsibility_boundary.ai_final_responsibility_allowed: false`
- AI final-responsibility flags such as `assumes_final_responsibility`
- formalization-scope excluded-claim signals
- optional `review_metadata` structure when present

### Lifecycle-aware checks

#### `originating`

The checker inspects whether the example includes:

- a human-capable `decision_owner`
- a human-capable `stop_authority`
- an empty `repairs` list
- a human return-point signal

This does not mean the originating pathway is complete, safe, compliant, legally valid, morally resolved, or production ready.

#### `repaired`

The checker inspects whether the example includes:

- a non-empty `repairs` list
- a human-capable `repair_owner`
- repair-record signals for trigger, repair owner, and repair state
- repair-boundary signals in `formalization_scope`

This does not mean repair is complete in the real world, harm is eliminated, legal responsibility is resolved, or moral responsibility is resolved.

#### `suspended`

The checker inspects whether the example includes:

- a top-level `suspension` block
- continuation and closure boundary signals
- required-before-continuation records
- disallowed-interpretation signals

This does not mean suspension is justified in a real-world setting.

#### `returning`

The checker inspects whether the example includes:

- a top-level `returning` block
- prior lifecycle-state signal
- automatic-continuation, automatic-closure, and automatic-repair-completion boundary signals
- required-before-next-state records
- disallowed-interpretation signals

This does not mean return is equivalent to continuation, repair completion, closure, or approval.

#### `closed`

The checker inspects whether the example includes:

- a top-level `closure` block
- closure basis records
- residual-obligation records
- reopening-condition records
- automatic-reopening, automatic-closure, and AI-closure-authority boundary signals
- closure-specific excluded-claim signals

This does not mean closure erases responsibility history, grants immunity, completes repair, certifies safety, or resolves legal or moral responsibility.

### Optional record-review metadata checks

When an example includes `review_metadata`, the checker now inspects whether:

- `review_tool_version` is present
- `checked_items` is present as a non-empty list
- `unchecked_items` is present as a non-empty list
- `review_result` is present as a mapping
- `review_result.not_claimed` is present as a non-empty list
- `unchecked_items` and `review_result.not_claimed` include non-certifying signals such as legal, safety, compliance, fairness, moral, and production boundaries

These checks are optional and apply only when `review_metadata` is present.

They remain bounded structural checks. A pass does not certify the record, the workflow, the system, the organization, or the real-world decision.

### Action-class-specific checks

Current checkers do not yet enforce action-class-specific requirements from [docs/action-class-matrix.md](action-class-matrix.md).

This is intentional for the current repository state because existing examples were created before the source-aligned Class A-F structure was stabilized.

Future bounded checker work may inspect structural signals such as:

- declared `action_class`
- Class C or higher Approval Gate presence
- Class D or higher rollback or repair path presence
- Class E high-impact and non-autonomous boundary language
- Class F stop trigger, Stop Authority, pending responsibility owner, and restart/return fields

Any such rule must remain bounded to structural signals.

A checker pass must not be interpreted as legal validity, safety, compliance, fairness, moral resolution, institutional approval, production readiness, or AI final-responsibility transfer.

## `scripts/check_review_results.py`

`scripts/check_review_results.py` checks review-result fixtures under `fixtures/review-results/*.yaml` against `spec/review-result.schema.yaml`.

The checker currently inspects:

- YAML parseability
- top-level mapping structure
- schema-defined required fields
- allowed `review_scope` values
- allowed `review_status` values
- non-empty `checked_items`
- expected `not_checked` boundary items
- expected `not_claimed` boundary items
- expected `responsibility_boundary` flags

This checker does not check pathway examples. It does not decide whether the reviewed workflow, organization, system, decision, or deployment is valid, safe, compliant, fair, morally resolved, certified, approved, production ready, or complete.

A pass means only that the current review-result fixture preserves the bounded structure and responsibility-boundary fields required by the current review-result schema.

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

`fixtures/review-results/record-review-result-minimal.yaml` provides a review-result output fixture checked by `scripts/check_review_results.py`.

`docs/review-result-schema-fixture-alignment.md` documents that the current fixture includes the current schema's required fields and boundary lists.

Future checker work should remain bounded to structural signals and must not treat a review pass as legal validity, safety, compliance, fairness, moral resolution, certification, or production readiness.

## Current example coverage map

| Example | Declared lifecycle state | Lifecycle-specific checker rule | Optional review metadata check | Action-class-specific check |
| --- | --- | --- | --- | --- |
| `examples/minimal-pathway.yaml` | `originating` | yes | no | not yet |
| `examples/action-class-matrix-minimal.yaml` | `originating` | yes | no | not yet |
| `examples/internal-document-update.yaml` | `originating` | yes | no | not yet |
| `examples/emergency-stop-flow.yaml` | `suspended` | yes | no | not yet |
| `examples/record-review-minimal.yaml` | `originating` | yes | yes | not yet |
| `examples/repair-flow.yaml` | `repaired` | yes | no | not yet |
| `examples/suspended-pathway.yaml` | `suspended` | yes | no | not yet |
| `examples/returning-pathway.yaml` | `returning` | yes | no | not yet |
| `examples/closed-pathway.yaml` | `closed` | yes | no | not yet |

## Review-result fixture coverage map

| Fixture | Schema reference | Alignment note | Current checker coverage |
| --- | --- | --- | --- |
| `fixtures/review-results/record-review-result-minimal.yaml` | `spec/review-result.schema.yaml` | `docs/review-result-schema-fixture-alignment.md` | checked by `scripts/check_review_results.py` |

## Planned action-class coverage map

This is future work, not current checker behavior.

| Planned area | Possible bounded signal | Boundary |
| --- | --- | --- |
| Class A Observe-Only | source/context visibility where observation affects later judgment | not safety or manipulation-proofing certification |
| Class B Suggest-Only | AI proposal separated from human adoption | not semantic correctness certification |
| Class C Approval-Required | Approval Gate, Execution Actor, Evidence Log | not approval quality certification |
| Class D Reversible External Action | rollback or repair path, external-impact boundary | not proof of harmless reversibility |
| Class E Irreversible or High-Impact Action | high-impact boundary, non-autonomous language, repair owner | not legal/safety/compliance approval |
| Class F Emergency Stop | stop trigger, Stop Authority, pending responsibility owner, restart/return boundary | not proof that the system is safe |

## Interpretation boundary

A checker pass means only that the checked file satisfies the bounded structural rules implemented by the current checker version.

A checker pass does not mean that the example or fixture is correct in all contexts, semantically complete, legally valid, ethically valid, safe, fair, compliant, certified, approved, or ready for production use.

The human author or maintainer remains responsible for deciding whether an example, fixture, schema, document, or public claim should be changed, published, or relied upon.
