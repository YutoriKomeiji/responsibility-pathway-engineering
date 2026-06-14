# Checker Coverage

This document summarizes the current coverage of bounded repository-maintenance checkers.

The checkers are bounded repository-maintenance tools. They are not schema validation systems, certification processes, compliance reviews, legal reviews, safety reviews, fairness reviews, moral accountability judgments, production-readiness assessments, connector-correctness proofs, adapter-correctness proofs, or AI final-responsibility transfer mechanisms.

## `scripts/check_examples.py`

`scripts/check_examples.py` checks pathway examples under `examples/*.yaml`.

It does not check JSON fixtures such as `examples/adapter-input-event-minimal.json` or `examples/minimal-synthetic-runtime-fixture.json`.

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

This is intentional for the current repository state because examples and schema fields are still being stabilized before deliberate action-class-specific checker migration.

Future bounded checker work may inspect structural signals such as:

- declared `action_class`
- Class C or higher Approval Gate presence
- Class D or higher rollback or repair path presence
- Class E high-impact and non-autonomous boundary language
- Class F stop trigger, Stop Authority, pending responsibility owner, and restart/return fields

Any such rule must remain bounded to structural signals.

A checker pass must not be interpreted as legal validity, safety, compliance, fairness, moral resolution, institutional approval, production readiness, or AI final-responsibility transfer.

### Support-call and missed-support note

`examples/missed-support-boundary-minimal.yaml` is checked only as a pathway example under the current structural and `returning` lifecycle checker rules.

The example includes a `support_call_policy` block for readability and concept mapping, but the current checker does not enforce support-call policy semantics.

The current checker does not validate whether support should have been requested, whether support was materially beneficial, whether a missed-support signal is correct, or whether the support-call policy is optimal.

A pass for this example means only that the file preserves the currently required bounded structural signals for pathway examples. It is not support-call policy validation, missed-support validation, approval quality validation, legal review, safety review, compliance review, fairness review, production readiness, runtime correctness, or connector correctness.

### Runtime-event bridge note

`examples/runtime-event-to-pathway-minimal.yaml` is checked only as a pathway example under the current structural and originating-lifecycle rules.

`scripts/check_examples.py` does not validate `spec/runtime-event.schema.yaml` or JSON fixtures such as `examples/adapter-input-event-minimal.json` or `examples/minimal-synthetic-runtime-fixture.json`.

`examples/minimal-synthetic-runtime-fixture.json` is a minimal synthetic runtime observation fixture for reading and review only. It is not currently checked by `scripts/check_examples.py` or `scripts/check_runtime_events.py`, is not runtime-event schema validation, and is not a runtime implementation, connector, workflow, or production runtime integration.

`docs/minimal-runtime-candidate-design.md` records the boundary for selecting a minimal synthetic runtime fixture or bounded runtime-checking stub before any runtime candidate is added.

`docs/runtime-event-checking-plan.md` records the planned path, preconditions, exclusions, suggested implementation order, and non-certifying boundary for runtime-event schema checking, JSON fixture checking, `scripts/check_runtime_events.py`, or a runtime-event workflow.

A pass for the runtime-event-to-pathway example means only that the generated draft pathway record preserves the currently required structural signals. It does not validate the runtime event schema, certify an adapter, approve a connector, prove the event mapping correct, prove JSON fixture correctness, prove schema correctness, prove runtime fixture correctness, or make the record production ready.

## `scripts/check_runtime_events.py`

`scripts/check_runtime_events.py` performs bounded local structural checks on `examples/adapter-input-event-minimal.json` by default.

The current runtime-event checker inspects only whether:

- the selected file is parseable JSON
- the top-level JSON value is a mapping
- required top-level runtime-event fields are present
- `source_system.vendor_specific` is explicitly `false`
- the first minimal fixture remains synthetic or warns if it does not
- an AI-agent observed actor does not claim final responsibility
- `evidence.captured_fields` is a non-empty list
- `evidence.missing_fields` is present as a list
- `evidence.uncertainty_notes` is present as a list
- `evidence.raw_event_available` is explicitly `true`
- `review_requirement.human_or_institutional_review_required` is explicitly `true`
- `review_requirement.reason` is present
- `excluded_claims` includes the expected non-certifying boundary items

The current runtime-event checker does not validate:

- `spec/runtime-event.schema.yaml`
- `examples/minimal-synthetic-runtime-fixture.json`
- adapter mapping correctness
- semantic correctness of the event-to-pathway transformation
- service-specific connector behavior
- production runtime behavior
- vendor API behavior
- legal validity
- safety
- compliance
- fairness
- moral resolution
- production readiness
- connector correctness
- adapter correctness
- responsibility assignment correctness
- AI final-responsibility transfer

There is no runtime-event workflow yet, and no observed runtime-event checker status has been recorded yet.

A pass from `scripts/check_runtime_events.py` may mean only that the selected synthetic runtime-event JSON fixture satisfies the bounded structural requirements implemented by the local checker. It is not schema validation, JSON semantic correctness proof, adapter correctness proof, connector correctness proof, runtime correctness proof, production readiness, certification, or AI final-responsibility transfer.

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
| `examples/missed-support-boundary-minimal.yaml` | `returning` | yes | no | not yet |
| `examples/emergency-stop-flow.yaml` | `suspended` | yes | no | not yet |
| `examples/reversible-external-action.yaml` | `originating` | yes | no | not yet |
| `examples/runtime-event-to-pathway-minimal.yaml` | `originating` | yes | no | not yet |
| `examples/adapter-input-event-minimal.json` | not a pathway example | no | no | checked by `scripts/check_runtime_events.py` |
| `examples/minimal-synthetic-runtime-fixture.json` | not a pathway example | no | no | not yet |
| `examples/record-review-minimal.yaml` | `originating` | yes | yes | not yet |
| `examples/repair-flow.yaml` | `repaired` | yes | no | not yet |
| `examples/suspended-pathway.yaml` | `suspended` | yes | no | not yet |
| `examples/returning-pathway.yaml` | `returning` | yes | no | not yet |
| `examples/closed-pathway.yaml` | `closed` | yes | no | not yet |

## Review-result fixture coverage map

| Fixture | Schema reference | Alignment note | Current checker coverage |
| --- | --- | --- | --- |
| `fixtures/review-results/record-review-result-minimal.yaml` | `spec/review-result.schema.yaml` | `docs/review-result-schema-fixture-alignment.md` | checked by `scripts/check_review_results.py` |

## Runtime-event checker coverage map

| Checked area | Current bounded signal | Boundary |
| --- | --- | --- |
| Runtime-event JSON fixture | valid JSON, required top-level runtime-event fields, synthetic source signal, review requirement, evidence lists, missing context notes, excluded claims | not JSON semantic correctness, schema correctness, adapter correctness, connector correctness, runtime correctness, production readiness, or certification |

## Planned runtime-event coverage map

This is future work, not current checker behavior.

| Planned area | Possible bounded signal | Boundary |
| --- | --- | --- |
| Minimal synthetic runtime fixture | valid JSON, explicit non-production scope, review-required status, missing approval evidence, missing execution evidence, excluded claims | not production runtime behavior, service connector correctness, adapter mapping correctness, runtime correctness, or production readiness |
| Runtime-event schema | readable and parseable schema shape aligned with the current minimal fixture | not schema completeness proof or production schema certification |
| Runtime-event to pathway relation | explicit source reference, missing context, review requirement, and non-certifying excluded claims | not semantic mapping correctness or responsibility assignment proof |
| Runtime-event workflow | observed checker status after a workflow exists and is actually observed | not certification or deployment approval |

## Planned action-class coverage map

This is future work, not current checker behavior.

| Planned area | Possible bounded signal | Boundary |
| --- | --- | --- |
| Class A Observe-Only | source/context visibility where observation affects later judgment | not safety or manipulation-proofing certification |
| Class B Suggest-Only | AI proposal separated from human adoption | not semantic correctness certification |
| Class C Approval-Required | Approval Gate, Execution Actor, Evidence Log | not approval quality certification |
| Class D Reversible External Action | rollback or correction path | not harmlessness, reversibility completeness, or compliance proof |
| Class E High-Impact | high-impact boundary signals and explicit non-autonomous control | not permission to execute high-impact action |
| Class F Emergency Stop | stop trigger, stop authority, pending responsibility, and restart/return boundary | not correctness of emergency response |
