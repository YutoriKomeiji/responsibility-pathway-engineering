# Runtime Event Checking Plan

This document defines the path for adding bounded runtime-event and JSON-fixture checks.

It is a planning and boundary document. It is not a production connector, production runtime integration, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, connector correctness proof, adapter correctness proof, or AI final-responsibility transfer mechanism.

## Purpose

Phase 3.1 currently includes a draft runtime-event bridge:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`

The pathway checker treats `examples/runtime-event-to-pathway-minimal.yaml` only as a pathway example.

A first bounded runtime-event checker stub now exists at `scripts/check_runtime_events.py`.

It checks `examples/adapter-input-event-minimal.json` by default and performs only local structural checks on the selected synthetic runtime-event JSON fixture.

The first local observation is recorded in `docs/runtime-event-checker-local-observation.md`.

Observed local result:

```text
exit code: 0
PASS: bounded runtime-event checks completed without failures
```

This was a local checker observation only. No runtime-event workflow existed at the time of observation, and no GitHub Actions runtime-event workflow status has been observed yet.

The checker does not yet validate:

- `spec/runtime-event.schema.yaml`
- `examples/minimal-synthetic-runtime-fixture.json`
- adapter mapping correctness
- semantic correctness of event-to-pathway transformation
- service-specific connector behavior
- production runtime behavior
- workflow status

This plan records what is now checked, what may be checked later, what must remain out of scope, and what conditions should be met before workflow or broader checker implementation starts.

## Current bounded runtime-event checks

`scripts/check_runtime_events.py` currently inspects only whether:

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

## Planned future checks

A future bounded runtime-event checker may inspect:

- additional runtime-event JSON fixtures after they are deliberately added
- whether `spec/runtime-event.schema.yaml` remains readable and parseable
- whether the minimal runtime-event schema still reflects the current fixture shape
- whether schema changes preserve review requirement, missing-context recording, evidence references, and excluded claims
- whether `examples/minimal-synthetic-runtime-fixture.json` preserves explicit non-production scope, review-required status, missing approval evidence, missing execution evidence, and excluded claims

## Not planned for the first checker layer

The first checker layer should not check:

- adapter mapping correctness
- semantic correctness of event-to-pathway transformation
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
- AI final-responsibility transfer

These items require separate boundaries, examples, and review rules before they can be considered.

## Preconditions before expanding implementation

Do not add a runtime-event workflow, schema checker, minimal-runtime-fixture checker, service connector check, or broader runtime-event checker until the following conditions remain satisfied after the first checker stub and local observation:

1. `spec/runtime-event.schema.yaml` remains small and readable.
2. `examples/adapter-input-event-minimal.json` remains synthetic, vendor-neutral, and review-required.
3. `examples/runtime-event-to-pathway-minimal.yaml` remains readable as a draft generated record requiring human or institutional review.
4. The relation between the JSON fixture and the pathway example is explainable without service-specific connector assumptions.
5. Missing context, missing approval evidence, missing execution evidence, and excluded claims remain explicit.
6. Checker output can be described as a bounded repository-maintenance signal only.
7. The checker can fail safely without implying that passing examples are certified.
8. Documentation updates can be kept small and traceable through the operation model, operation index, current snapshot, checker coverage, and changelog or roadmap notes where needed.

## Suggested next implementation order

Use this order after the first local checker observation:

1. record the first local observation in `docs/phase-3-1-current-snapshot.md`, `docs/phase-3-1-sync-log.md`, and `docs/current-task-inventory.md`
2. consider a minimal runtime-event workflow only if the maintainer decides the local checker behavior is stable enough to observe in GitHub Actions
3. record observed workflow status only after the workflow has actually been observed
4. update `docs/checker-coverage.md` after any checker behavior changes
5. update `docs/example-index.md` only if the interpretation of examples changes
6. defer schema checking, minimal-runtime-fixture checking, service connectors, production runtime, semantic responsibility correctness checking, conformance claims, public standardization claims, and Lean expansion until their own preconditions are satisfied

## Boundary for passing checks

A passing runtime-event check may mean only that a selected synthetic runtime-event JSON fixture satisfies the bounded structural requirements implemented by the checker.

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
- proof that a generated pathway record is complete
- proof that responsibility has been correctly assigned
- AI final-responsibility transfer

## Current decision

A first bounded runtime-event checker stub exists.

A first local observation of the checker against `examples/adapter-input-event-minimal.json` recorded exit code `0` and bounded checks completed without failures.

Runtime-event workflow implementation remains deferred until the maintainer decides the local checker behavior is stable enough to observe in GitHub Actions.

Runtime-event schema checking remains deferred.

Minimal synthetic runtime fixture checking remains deferred.

Service-specific connectors, production runtime integration, adapter mapping correctness checking, semantic responsibility correctness checking, and AI final-responsibility transfer remain out of scope.
