# Runtime Event Checking Plan

This document defines the path for bounded runtime-event and JSON-fixture checks.

It is a planning and boundary document. It is not a production connector, production runtime integration, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, connector correctness proof, adapter correctness proof, runtime correctness proof, or AI final-responsibility transfer mechanism.

## Purpose

Phase 3.1 currently includes a draft runtime-event bridge:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `examples/minimal-synthetic-runtime-fixture.json`

The pathway checker treats `examples/runtime-event-to-pathway-minimal.yaml` only as a pathway example.

A first bounded runtime-event checker stub exists at `scripts/check_runtime_events.py`.

It checks the following JSON fixtures by default:

```text
examples/adapter-input-event-minimal.json
examples/minimal-synthetic-runtime-fixture.json
```

It performs only bounded local structural checks on the selected synthetic runtime-event JSON fixture and selected minimal synthetic runtime observation fixture.

The first local observation is recorded in `docs/runtime-event-checker-local-observation.md`.

Observed local result:

```text
exit code: 0
PASS: bounded runtime-event checks completed without failures
```

A minimal runtime-event workflow now exists at `.github/workflows/check-runtime-events.yml`.

Observed workflow status is recorded in `docs/runtime-event-workflow-current-status.md`, `docs/minimal-runtime-fixture-checker-workflow-observation.md`, and focused Phase 3.1 connection or sync notes.

The observed workflow success after `examples/minimal-synthetic-runtime-fixture.json` was added to checker coverage is:

```text
run id: 27607798655
job id: 81624113270
job name: Bounded runtime-event checks
job status: completed
job conclusion: success
step: Run bounded runtime-event checker: completed / success
```

The checker does not validate:

- `spec/runtime-event.schema.yaml`
- runtime-event schema completeness
- JSON semantic correctness
- adapter mapping correctness
- semantic correctness of event-to-pathway transformation
- responsibility assignment correctness
- service-specific connector behavior
- production runtime behavior
- workflow completeness

This plan records what is now checked, what may be checked later, what must remain out of scope, and what conditions should be met before broader checker, schema, workflow, connector, or runtime implementation starts.

## Current bounded runtime-event checks

For `examples/adapter-input-event-minimal.json`, `scripts/check_runtime_events.py` currently inspects only whether:

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

For `examples/minimal-synthetic-runtime-fixture.json`, the checker currently inspects only whether selected structural runtime-boundary signals are preserved, including:

- the selected file is parseable JSON
- the top-level JSON value is a mapping
- required top-level minimal-runtime-fixture fields are present
- fixture type remains `minimal_synthetic_runtime_observation`
- `non_production`, `synthetic`, `vendor_neutral`, and `review_required` are explicitly `true`
- `certification_claimed` is explicitly `false`
- runtime scope preserves no production runtime, no service connector, no automatic approval, no automatic execution, and no external side effects
- runtime observation source remains non-vendor-specific and non-production
- observed sequence entries preserve AI final-responsibility non-claim, missing approval evidence, missing execution evidence, human review requirement, and source event reference
- expected boundary-preservation flags remain explicit
- candidate status preserves no production runtime, service connector, automatic approval, or automatic execution
- `excluded_claims` includes expected runtime-fixture non-certifying boundary items

## Planned future checks

A future bounded runtime-event or fixture checker may inspect:

- additional runtime-event JSON fixtures after they are deliberately added
- whether `spec/runtime-event.schema.yaml` remains readable and parseable
- whether the minimal runtime-event schema still reflects the current fixture shape
- whether schema changes preserve review requirement, missing-context recording, evidence references, and excluded claims
- whether date-time fields remain well-formed after a bounded format-checking decision is explicitly reopened
- whether allowed enum values remain aligned after a bounded enum-checking decision is explicitly reopened
- whether a future event-to-pathway relation checker can inspect only structural source-reference, missing-context, review-required, and excluded-claim signals

## Not planned for the current checker layer

The current checker layer should not check:

- full schema validation
- JSON semantic correctness
- adapter mapping correctness
- semantic correctness of event-to-pathway transformation
- responsibility assignment correctness
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
- runtime correctness
- conformance
- AI final-responsibility transfer

These items require separate boundaries, examples, and review rules before they can be considered.

## Preconditions before expanding implementation

Do not add runtime-event schema checking, broader JSON schema-fixture checking, service connector checks, production runtime integration, semantic checking, or broader runtime-event checker behavior until the following conditions remain satisfied after the first checker stub, fixture expansion, and workflow observations:

1. `spec/runtime-event.schema.yaml` remains small and readable.
2. `examples/adapter-input-event-minimal.json` remains synthetic, vendor-neutral, and review-required.
3. `examples/minimal-synthetic-runtime-fixture.json` remains synthetic, local, non-production, vendor-neutral, review-required, non-certifying, and disconnected from automatic approval or execution.
4. `examples/runtime-event-to-pathway-minimal.yaml` remains readable as a draft generated record requiring human or institutional review.
5. The relation between the JSON fixture, runtime-like observation fixture, and pathway example is explainable without service-specific connector assumptions.
6. Missing context, missing approval evidence, missing execution evidence, and excluded claims remain explicit.
7. Checker output can be described as a bounded repository-maintenance signal only.
8. The checker can fail safely without implying that passing examples are certified.
9. Documentation updates can be kept small and traceable through the operation model, operation index, current snapshot, checker coverage, alignment notes, and focused sync or roadmap notes where needed.

## Suggested next implementation order

Use this order after the first checker, workflow, and minimal runtime fixture checker observations:

1. keep `docs/checker-coverage.md`, `docs/runtime-event-schema-fixture-alignment.md`, `docs/phase-3-1-current-snapshot.md`, `docs/current-task-inventory.md`, and `docs/operation-index.md` aligned
2. keep workflow observation notes current only after workflow status has actually been observed
3. keep `docs/example-index.md` aligned only if the interpretation of examples changes
4. prefer focused connection or sync notes when long-file updates would duplicate state without improving restartability
5. consider a future bounded event-to-pathway relation checker plan only after the current schema/fixture/checker alignment remains stable
6. defer full schema validation, semantic responsibility correctness checking, service connectors, production runtime, conformance claims, public standardization claims, and Lean expansion until their own preconditions are satisfied

## Boundary for passing checks

A passing runtime-event check may mean only that the selected synthetic runtime-event JSON fixture and selected minimal synthetic runtime observation fixture satisfy the bounded structural requirements implemented by the checker.

It must not be interpreted as:

- legal validation
- safety certification
- compliance certification
- fairness certification
- moral resolution
- institutional approval
- production readiness
- service connector correctness
- adapter mapping correctness
- runtime correctness
- proof that a generated pathway record is complete
- proof that responsibility has been correctly assigned
- conformance
- AI final-responsibility transfer

## Current decision

A first bounded runtime-event checker stub exists.

A first local observation of the checker against `examples/adapter-input-event-minimal.json` recorded exit code `0` and bounded checks completed without failures.

A first minimal runtime-event workflow exists and has observed bounded success.

The checker now covers both `examples/adapter-input-event-minimal.json` and `examples/minimal-synthetic-runtime-fixture.json` by default.

The observed minimal runtime fixture checker workflow success is recorded in focused observation, connection, sync, snapshot, task-inventory, operation-index, and alignment documents.

Runtime-event schema checking remains deferred.

Further runtime fixture checking remains deferred unless a new fixture is deliberately designed and the current preconditions still hold.

Service-specific connectors, production runtime integration, adapter mapping correctness checking, semantic responsibility correctness checking, conformance claims, public standardization claims, and AI final-responsibility transfer remain out of scope.
