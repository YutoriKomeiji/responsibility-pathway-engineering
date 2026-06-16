# Runtime Event Schema / Fixture Alignment

This note records the current alignment between the draft runtime-event schema, the selected JSON fixtures, and the bounded runtime-event checker.

It is an alignment note only. It is not schema validation, JSON semantic correctness proof, adapter mapping correctness proof, connector correctness proof, runtime correctness proof, production-readiness evidence, legal review, safety review, compliance review, fairness review, moral-resolution evidence, certification, conformance evidence, or AI final-responsibility transfer mechanism.

## Connected artifacts

This note connects:

- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/minimal-synthetic-runtime-fixture.json`
- `scripts/check_runtime_events.py`
- `docs/checker-coverage.md`
- `docs/runtime-event-workflow-current-status.md`
- `docs/minimal-runtime-fixture-checker-workflow-observation.md`

## Schema status

`spec/runtime-event.schema.yaml` is a draft, vendor-neutral input-event shape for future adapters that may transform external logs, API events, workflow results, or runtime observations into draft Responsibility Pathway records.

The schema boundary explicitly keeps out:

- production connectors
- production runtime
- certification systems
- legal decision systems
- safety certification tools
- compliance engines
- fairness certification tools
- AI final-responsibility transfer

The schema interpretation treats an event as an observation, not an approval, certification, legal resolution, moral resolution, or final record. Generated pathway records remain review-required.

## Runtime-event fixture alignment

`examples/adapter-input-event-minimal.json` is the first selected synthetic runtime-event JSON fixture.

It aligns with the draft runtime-event schema at the current structural level by including:

| Schema field | Fixture signal | Current checker status |
| --- | --- | --- |
| `event_id` | present as `event_minimal_001` | checked for required key presence |
| `schema_version` | present as `0.1.0` | checked for required key presence |
| `source_system` | synthetic source, `vendor_specific: false` | checked for mapping and vendor-specific false |
| `observed_at` | present timestamp | checked for required key presence only |
| `observed_actor` | AI agent with `final_responsibility_claimed: false` | checked for mapping and AI final-responsibility non-claim |
| `observed_action` | draft proposal with adapter-suggested action class | checked for required key presence only |
| `observed_target` | internal document target with low impact flags | checked for required key presence only |
| `evidence` | captured fields, missing fields, uncertainty notes, raw event available | checked for list and raw-event structural signals |
| `review_requirement` | human/institutional review required with reason | checked for required review and reason |
| `excluded_claims` | expected non-certifying boundary list | checked for expected boundary items |

This is structural alignment only. The checker does not prove the JSON fixture is semantically correct, complete, well-modeled, safe, legally valid, production-ready, or adapter-correct.

## Minimal synthetic runtime fixture alignment

`examples/minimal-synthetic-runtime-fixture.json` is not an instance of `spec/runtime-event.schema.yaml` in the same way as `examples/adapter-input-event-minimal.json`.

It is a runtime-like observation fixture that references the selected runtime-event fixture and records runtime-boundary preservation signals.

The current alignment is therefore indirect:

| Runtime fixture signal | Relation to runtime-event bridge | Current checker status |
| --- | --- | --- |
| `fixture_type: minimal_synthetic_runtime_observation` | marks the fixture as runtime-like observation, not schema instance | checked |
| `non_production: true` | preserves non-production boundary | checked |
| `synthetic: true` | preserves synthetic/local boundary | checked |
| `vendor_neutral: true` | preserves vendor-neutral boundary | checked |
| `review_required: true` | preserves review-required boundary | checked |
| `certification_claimed: false` | prevents certification interpretation | checked |
| `runtime_scope.production_runtime: false` | prevents production-runtime interpretation | checked |
| `runtime_scope.service_specific_connector: false` | prevents connector-correctness interpretation | checked |
| `runtime_scope.automatic_approval: false` | prevents automatic approval interpretation | checked |
| `runtime_scope.automatic_execution: false` | prevents automatic execution interpretation | checked |
| `runtime_scope.external_side_effects: false` | preserves no external side-effect boundary | checked |
| `runtime_observation.source_system.vendor_specific: false` | preserves vendor-neutral runtime observation source | checked |
| `runtime_observation.source_system.production_system: false` | preserves non-production source boundary | checked |
| `observed_sequence[].actor_final_responsibility_claimed: false` | preserves AI final-responsibility non-claim | checked |
| `observed_sequence[].approval_evidence_present: false` | preserves missing approval evidence | checked |
| `observed_sequence[].execution_evidence_present: false` | preserves missing execution evidence | checked |
| `observed_sequence[].human_review_required: true` | preserves human review requirement | checked |
| `observed_sequence[].source_event_reference` | points back to `examples/adapter-input-event-minimal.json` | checked for presence |
| `expected_boundary_preservation` flags | records which boundary claims remain explicitly false or review-required | checked |
| `candidate_status` | records no production runtime, connector, automatic approval, or automatic execution | checked |
| `excluded_claims` | records runtime-fixture-specific non-claims | checked |

This indirect alignment means only that the runtime-like fixture preserves bounded runtime-boundary signals that are relevant to the runtime-event bridge.

It does not mean the runtime fixture is a production runtime, validated runtime trace, schema-certified event, semantic mapping proof, responsibility assignment proof, or adapter correctness proof.

## Checker boundary

`scripts/check_runtime_events.py` currently checks both selected JSON fixtures by default:

```text
examples/adapter-input-event-minimal.json
examples/minimal-synthetic-runtime-fixture.json
```

The checker remains bounded to local structural checks.

A checker pass may mean only that the selected synthetic runtime-event fixture and selected minimal synthetic runtime observation fixture preserve the currently implemented bounded structural signals.

A checker pass must not be interpreted as:

- schema validation
- JSON semantic correctness
- adapter mapping correctness
- connector correctness
- runtime correctness
- production readiness
- legal validity
- safety
- compliance
- fairness
- moral resolution
- institutional approval
- conformance
- certification
- AI final-responsibility transfer

## Current workflow observation

The selected fixtures are currently included in the bounded runtime-event workflow path.

The observed workflow success after `examples/minimal-synthetic-runtime-fixture.json` was added to checker coverage is recorded in:

- `docs/runtime-event-workflow-current-status.md`
- `docs/minimal-runtime-fixture-checker-workflow-observation.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md`

Observed run:

```text
https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/runs/27607798655
```

Observed job:

```text
job id: 81624113270
job name: Bounded runtime-event checks
job status: completed
job conclusion: success
step: Run bounded runtime-event checker: completed / success
```

This workflow observation records bounded checker execution only. It does not expand the meaning of a checker pass.

## Known gaps

The following remain intentionally unvalidated or deferred:

- full schema validation against `spec/runtime-event.schema.yaml`
- runtime-event schema completeness
- JSON semantic correctness
- source-event hash validation
- date-time format validation
- enum-value enforcement beyond the currently coded structural checks
- adapter mapping correctness
- event-to-pathway semantic correctness
- responsibility assignment correctness
- connector behavior
- production runtime behavior
- workflow completeness
- conformance model drafting
- public standardization claims
- Lean expansion around runtime-event or adapter concepts

## Next safe work

The next safe work is not to claim correctness.

The next safe work is to improve reviewability by one of the following:

1. connect this note from `docs/operation-index.md`
2. connect this note from `docs/current-task-inventory.md`
3. consider a future bounded plan for event-to-pathway relation checking
4. consider a future checklist for external reviewers

Do not add schema validation, semantic checking, connector work, production runtime, conformance claims, public standardization claims, or Lean expansion from this alignment note alone.
