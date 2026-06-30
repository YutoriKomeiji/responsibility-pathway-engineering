# Checker Coverage

This document summarizes the current coverage of bounded repository-maintenance checkers.

The checkers are bounded repository-maintenance tools. They are not schema validation systems, certification processes, compliance reviews, legal reviews, safety reviews, fairness reviews, moral accountability judgments, production-readiness assessments, connector-correctness proofs, adapter-correctness proofs, runtime-correctness proofs, conformance evidence, or AI final-responsibility transfer mechanisms.

## `scripts/check_examples.py`

`scripts/check_examples.py` checks pathway examples under `examples/*.yaml`.

It does not check JSON fixtures such as `examples/adapter-input-event-minimal.json` or `examples/minimal-synthetic-runtime-fixture.json`.

For pathway examples, the checker currently inspects:

- required top-level keys
- non-empty `nodes`
- `edges` list presence
- human return-point signals
- `responsibility_boundary.ai_final_responsibility_allowed: false`
- AI final-responsibility flags such as `assumes_final_responsibility`
- formalization-scope excluded-claim signals
- optional `review_metadata` structure when present
- lifecycle-aware structural signals for `originating`, `repaired`, `suspended`, `returning`, and `closed`

These checks are bounded structural checks only. A pass does not certify the record, the workflow, the system, the organization, or the real-world decision.

### Action-class-specific checks

Current checkers do not yet enforce action-class-specific requirements from [docs/action-class-matrix.md](action-class-matrix.md).

Future bounded checker work may inspect structural signals such as declared `action_class`, Class C approval-gate presence, Class D rollback or repair paths, Class E high-impact boundaries, or Class F stop-trigger boundaries.

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

`examples/adapter-input-event-minimal.json` is the selected synthetic runtime-event JSON fixture and is checked by `scripts/check_runtime_events.py` for bounded structural runtime-event signals only.

`examples/minimal-synthetic-runtime-fixture.json` is a minimal synthetic runtime observation fixture for reading and review only. It is checked by `scripts/check_runtime_events.py` for bounded structural runtime-boundary signals only. It is not runtime-event schema validation and is not a runtime implementation, connector, workflow, or production runtime integration.

`docs/runtime-event-schema-fixture-alignment.md` records the current structural alignment between the draft runtime-event schema, selected JSON fixtures, and the bounded runtime-event checker without treating alignment as validation.

`docs/event-to-pathway-relation-checker-plan.md` records planned future structural relation-checker boundaries between selected runtime-event JSON fixtures and pathway YAML examples. It is not current checker behavior and does not authorize implementation by itself.

`docs/minimal-runtime-candidate-design.md` records the boundary for selecting a minimal synthetic runtime fixture or bounded runtime-checking stub before any further runtime candidate is added.

`docs/runtime-event-checking-plan.md` records the path, preconditions, exclusions, implementation order, and non-certifying boundary for future runtime-event schema checking, broader JSON fixture checking, checker expansion, or workflow expansion.

A pass for the runtime-event-to-pathway example means only that the generated draft pathway record preserves the currently required structural signals. It does not validate the runtime event schema, certify an adapter, approve a connector, prove the event mapping correct, prove JSON fixture correctness, prove schema correctness, prove runtime fixture correctness, or make the record production ready.

## `scripts/check_runtime_events.py`

`scripts/check_runtime_events.py` performs bounded local structural checks on the selected synthetic runtime-event and minimal synthetic runtime observation JSON fixtures.

By default, it checks:

- `examples/adapter-input-event-minimal.json`
- `examples/minimal-synthetic-runtime-fixture.json`

The first local observation for `examples/adapter-input-event-minimal.json` is recorded in `docs/runtime-event-checker-local-observation.md`.

Workflow observations for the runtime-event checker are recorded in `docs/runtime-event-workflow-current-status.md`.

The observed workflow success after `examples/minimal-synthetic-runtime-fixture.json` was added to the bounded checker coverage is recorded in `docs/minimal-runtime-fixture-checker-workflow-observation.md` and `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md`.

For `examples/adapter-input-event-minimal.json`, the current runtime-event checker inspects only whether:

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

For `examples/minimal-synthetic-runtime-fixture.json`, the current runtime-event checker inspects only whether:

- the selected file is parseable JSON
- the top-level JSON value is a mapping
- required top-level minimal runtime fixture fields are present
- the fixture remains a minimal synthetic runtime observation
- `non_production`, `synthetic`, `vendor_neutral`, and `review_required` are explicitly `true`
- `certification_claimed` is explicitly `false`
- runtime scope preserves non-production, no service connector, no automatic approval, no automatic execution, and no external side effects
- runtime observation source remains non-vendor-specific and non-production
- observed sequence entries preserve AI final-responsibility non-claim, missing approval evidence, missing execution evidence, human review requirement, and source event reference
- expected boundary-preservation flags remain explicit
- candidate status does not include production runtime, service connector, automatic approval, or automatic execution
- excluded claims include the expected non-certifying runtime-fixture boundaries

The current runtime-event checker does not validate:

- `spec/runtime-event.schema.yaml`
- runtime-event schema completeness
- JSON semantic correctness
- adapter mapping correctness
- semantic correctness of the event-to-pathway transformation
- responsibility assignment correctness
- service-specific connector behavior
- production runtime behavior
- workflow completeness
- vendor API behavior
- legal validity
- safety
- compliance
- fairness
- moral resolution
- production readiness
- connector correctness
- adapter correctness
- runtime correctness
- conformance
- AI final-responsibility transfer

A pass from `scripts/check_runtime_events.py` may mean only that the selected synthetic runtime-event or minimal synthetic runtime observation JSON fixture satisfies the bounded structural requirements implemented by the local checker. It is not schema validation, JSON semantic correctness proof, adapter correctness proof, connector correctness proof, runtime correctness proof, production readiness, certification, conformance evidence, or AI final-responsibility transfer.

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

## `scripts/check_issue_form.py`

`scripts/check_issue_form.py` checks the AI-assisted work GitHub Issue Form definition.

By default, it checks:

- `.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml`

The checker note is recorded in `docs/issue-form-checker-note.md`.

The workflow is `.github/workflows/check-issue-form.yml`.

The current issue-form checker inspects only whether:

- expected top-level GitHub Issue Form keys are present
- selected RPE field IDs are present
- AI assistance boundary field is present
- human or institutional review field is present
- evidence log field is present
- missing context field is present as an uncertainty signal
- responsibility return point field is present
- repair / reopening field is present as a repair signal
- non-claim checkbox field is present
- non-claim checkbox options are required
- non-final-AI responsibility boundary text is present
- selected non-claim boundary keywords are present

The AI-assisted work template and Issue Form evidence-log guidance now include `observed_at`, `recorded_at`, and `timezone` so evidence can be reviewed in time order. The current issue-form checker does not enforce those timestamp fields inside created issue bodies.

The current issue-form checker does not validate created issue content, timestamp completeness, timestamp correctness, time-zone correctness, URL validity, evidence quality, reviewer authority, approval quality, legal validity, safety, compliance, fairness, production readiness, conformance, social acceptance, certification, or final responsibility assignment.

A pass from `scripts/check_issue_form.py` means only that the Issue Form definition preserves selected RPE structural fields and non-claim boundary signals. It does not mean that any filled issue is correct, complete, time-ordered, safe, compliant, legally valid, fair, production ready, externally reviewed, socially accepted, certified, or conformance-ready.

Future warning-only planning for filled issue bodies is recorded in `docs/issue-body-warning-checker-plan.md`. That plan is not current checker behavior, does not add a workflow, and does not introduce live issue access.

## Responsibility Pathway record review alignment

`docs/responsibility-pathway-record-review.md` defines a plain-language review and recheck guide for Responsibility Pathway records.

`spec/pathway.schema.yaml` includes review aliases, review metadata, and record-review alignment notes.

`spec/review-result.schema.yaml` defines the bounded review-result output structure.

`examples/record-review-minimal.yaml` provides a small readable record-review example that follows the existing originating lifecycle checker path.

`fixtures/review-results/record-review-result-minimal.yaml` provides a review-result output fixture checked by `scripts/check_review_results.py`.

`docs/review-result-schema-fixture-alignment.md` documents that the current fixture includes the current schema's required fields and boundary lists.

Future checker work should remain bounded to structural signals and must not treat a review pass as legal validity, safety, compliance, fairness, moral resolution, certification, or production readiness.

## Current example coverage map

| Example or fixture | Declared lifecycle state | Lifecycle-specific checker rule | Optional review metadata check | Current checker coverage |
| --- | --- | --- | --- | --- |
| `examples/minimal-pathway.yaml` | `originating` | yes | no | checked by `scripts/check_examples.py` |
| `examples/action-class-matrix-minimal.yaml` | `originating` | yes | no | checked by `scripts/check_examples.py` |
| `examples/internal-document-update.yaml` | `originating` | yes | no | checked by `scripts/check_examples.py` |
| `examples/missed-support-boundary-minimal.yaml` | `returning` | yes | no | checked by `scripts/check_examples.py` |
| `examples/emergency-stop-flow.yaml` | `suspended` | yes | no | checked by `scripts/check_examples.py` |
| `examples/reversible-external-action.yaml` | `originating` | yes | no | checked by `scripts/check_examples.py` |
| `examples/runtime-event-to-pathway-minimal.yaml` | `originating` | yes | no | checked by `scripts/check_examples.py` |
| `examples/adapter-input-event-minimal.json` | not a pathway example | no | no | checked by `scripts/check_runtime_events.py` |
| `examples/minimal-synthetic-runtime-fixture.json` | not a pathway example | no | no | checked by `scripts/check_runtime_events.py` |
