# Runtime Event Checking Plan

This document defines the planned path for adding bounded runtime-event and JSON-fixture checks.

It is a planning document only. It is not a checker implementation, production connector, production runtime integration, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, connector correctness proof, adapter correctness proof, or AI final-responsibility transfer mechanism.

## Purpose

Phase 3.1 currently includes a draft runtime-event bridge:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`

The current checker treats `examples/runtime-event-to-pathway-minimal.yaml` only as a pathway example.

It does not yet validate:

- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- adapter mapping correctness
- service-specific connector behavior
- production runtime behavior

This plan records what may be checked later, what must remain out of scope, and what conditions should be met before implementation starts.

## Planned future checks

A future bounded runtime-event checker may inspect:

- whether a runtime-event JSON fixture is valid JSON
- whether required top-level runtime-event fields exist
- whether schema version, source system, observation timestamp, observed actor, observed action, observed target, evidence notes, missing-context notes, review requirement, and excluded claims are present where required
- whether `review_required` remains true for generated or transformed records
- whether missing approval evidence and missing execution evidence remain explicit when applicable
- whether excluded claims include non-certifying boundaries
- whether the fixture remains synthetic or otherwise clearly scoped when no service-specific connector exists

A future schema-related check may inspect:

- whether `spec/runtime-event.schema.yaml` remains readable and parseable
- whether the minimal runtime-event schema still reflects the current fixture shape
- whether schema changes preserve review requirement, missing-context recording, evidence references, and excluded claims

## Not planned for the first checker

The first runtime-event checker should not check:

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

## Preconditions before implementation

Do not add `scripts/check_runtime_events.py` or a runtime-event workflow until the following conditions are met:

1. `spec/runtime-event.schema.yaml` remains small and readable.
2. `examples/adapter-input-event-minimal.json` remains synthetic, vendor-neutral, and review-required.
3. `examples/runtime-event-to-pathway-minimal.yaml` remains readable as a draft generated record requiring human or institutional review.
4. The relation between the JSON fixture and the pathway example is explainable without service-specific connector assumptions.
5. Missing context, missing approval evidence, missing execution evidence, and excluded claims remain explicit.
6. Checker output can be described as a bounded repository-maintenance signal only.
7. The checker can fail safely without implying that passing examples are certified.
8. Documentation updates can be kept small and traceable through the operation model, operation index, current snapshot, checker coverage, and changelog or roadmap notes where needed.

## Suggested implementation order

When the preconditions are met, use this order:

1. Add a small `scripts/check_runtime_events.py` that validates only one JSON fixture.
2. Keep the first check structural and local.
3. Add a minimal GitHub Actions workflow only after the local checker is stable.
4. Update `docs/checker-coverage.md` to distinguish current runtime-event checks from planned future checks.
5. Update `docs/example-index.md` only if the interpretation of examples changes.
6. Update `docs/phase-3-1-current-snapshot.md` after observed checker behavior is known.
7. Record observed green workflow status only after the workflow has actually been observed.

## Boundary for passing checks

A passing runtime-event check may mean only that a JSON fixture or runtime-event schema satisfies the bounded structural requirements implemented by the checker.

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

Runtime-event checking remains deferred.

This plan exists to make the deferral explicit, reviewable, and reversible when the schema, fixture, pathway example, checker boundary, and repository operation path are stable enough to proceed.
