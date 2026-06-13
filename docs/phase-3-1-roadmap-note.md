# Phase 3.1 Roadmap Note

This note records the current roadmap position for Phase 3.1 Adapter Boundary and Runtime Event Bridge.

It exists as a short roadmap companion so that the long `ROADMAP.md` file does not need to be replaced in one large update when repository-wide synchronization is underway.

## Phase 3.1 status

Phase 3.1 has started.

The current Phase 3.1 work establishes a draft, vendor-neutral, review-required bridge from runtime observations to Responsibility Pathway draft records.

The current Phase 3.1 work also establishes a runtime-event checking plan before any runtime-event checker implementation.

Current artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `docs/runtime-event-checking-plan.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/repository-operation-model.md`
- `docs/operation-index.md`

## What has been reached

The following checkpoint has been reached:

- adapter boundary documented
- minimal runtime event schema added
- minimal synthetic JSON input event added
- minimal runtime-event-to-pathway draft example added
- `Check examples #16` observed green on commit `d377be2`
- reader paths synchronized in README, README.ja, BEACON, example index, and checker coverage for the initial runtime-event bridge
- repository operation layer added through `docs/repository-operation-model.md` and `docs/operation-index.md`
- periodic operation review policy added for repository-maintenance alignment
- runtime-event checking plan added before checker implementation
- `docs/operation-index.md` points runtime-event checker planning to `docs/runtime-event-checking-plan.md`
- `docs/checker-coverage.md` records that runtime-event schema checking and JSON fixture checking remain unimplemented and deferred
- `docs/example-index.md` records that `examples/runtime-event-to-pathway-minimal.yaml` is currently checked only as a pathway example
- `ROADMAP.md` and `CHANGELOG.md` record the runtime-event checking plan as a non-certifying milestone before implementation

## Roadmap interpretation

Phase 3.1 is not yet a connector phase.

Phase 3.1 is also not yet a runtime-event checker implementation phase.

It does not yet include:

- service-specific connectors
- production conversion code
- runtime-event schema checker
- JSON fixture checker
- `scripts/check_runtime_events.py`
- runtime-event workflow
- adapter mapping correctness checker
- action-class-specific checker enforcement
- Class E positive examples
- Lean expansion around adapter or runtime-event concepts

## Runtime-event checking rule

Do not add `scripts/check_runtime_events.py`, a runtime-event workflow, runtime-event schema checking, or JSON fixture checking until `docs/runtime-event-checking-plan.md` preconditions are satisfied.

Any future passing runtime-event check must remain a bounded repository-maintenance signal only.

A passing runtime-event check must not be interpreted as certification, legal review, safety review, compliance review, fairness review, production approval, connector correctness proof, adapter correctness proof, schema correctness proof, JSON fixture correctness proof, semantic mapping correctness proof, responsibility assignment proof, or AI final-responsibility transfer.

## Next low-risk work

The next low-risk work is synchronization and boundary maintenance only:

1. update `docs/phase-3-1-current-snapshot.md` only if the restart point should explicitly say that checker coverage and example index are now connected to the runtime-event checking plan
2. keep runtime-event checking deferred until the plan preconditions are satisfied
3. keep service-specific connectors deferred
4. keep production conversion code deferred
5. keep Lean expansion deferred
6. keep Class E positive examples deferred
7. use periodic operation review if commit granularity, reader paths, logs, roadmap notes, checker interpretation, or deferred boundaries drift from actual practice

## Stop conditions

Stop and preserve the current state if:

- a long file update is blocked
- a reader-path update risks overwriting unrelated content
- a checker failure appears
- a proposed change implies certification, production readiness, legal validation, safety certification, compliance certification, fairness certification, moral resolution, connector correctness, adapter correctness, semantic mapping correctness, schema correctness, JSON fixture correctness, or AI final-responsibility transfer

## Restart point

Restart from:

- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/runtime-event-checking-plan.md`
- `docs/operation-index.md`
- this note

Do not continue directly into service-specific connector implementation.

Do not continue directly into runtime-event checker implementation unless the runtime-event checking plan preconditions are satisfied.
