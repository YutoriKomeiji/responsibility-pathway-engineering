# Phase 3.1 Roadmap Note

This note records the current roadmap position for Phase 3.1 Adapter Boundary and Runtime Event Bridge.

It exists as a short roadmap companion so that the long `ROADMAP.md` file does not need to be replaced in one large update when repository-wide synchronization is underway.

## Phase 3.1 status

Phase 3.1 has started.

The current Phase 3.1 work establishes a draft, vendor-neutral, review-required bridge from runtime observations to Responsibility Pathway draft records.

Current artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`

## What has been reached

The following checkpoint has been reached:

- adapter boundary documented
- minimal runtime event schema added
- minimal synthetic JSON input event added
- minimal runtime-event-to-pathway draft example added
- `Check examples #16` observed green on commit `d377be2`
- reader paths synchronized in README, README.ja, BEACON, example index, and checker coverage
- staged update operation documented in the Phase 3.1 current snapshot

## Roadmap interpretation

Phase 3.1 is not yet a connector phase.

It does not yet include:

- service-specific connectors
- production conversion code
- runtime-event schema checker
- JSON fixture checker
- adapter mapping correctness checker
- action-class-specific checker enforcement
- Class E positive examples
- Lean expansion around adapter or runtime-event concepts

## Next low-risk work

The next low-risk work is documentation synchronization only:

1. add a short reference from `ROADMAP.md` to this note and `docs/phase-3-1-current-snapshot.md`
2. add a short reference from `CHANGELOG.md` to `docs/phase-3-1-sync-log.md`
3. avoid replacing long files in a single update if the update becomes risky
4. keep service-specific connectors deferred
5. keep production conversion code deferred
6. keep Lean expansion deferred

## Stop conditions

Stop and preserve the current state if:

- a long file update is blocked
- a reader-path update risks overwriting unrelated content
- a checker failure appears
- a proposed change implies certification, production readiness, legal validation, safety certification, compliance certification, fairness certification, moral resolution, or AI final-responsibility transfer

## Restart point

Restart from:

- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- this note

Do not continue directly into service-specific connector implementation.
