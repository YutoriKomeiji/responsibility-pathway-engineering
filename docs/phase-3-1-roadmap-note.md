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
- operation-document roles have been clarified: `CHANGELOG.md` is archival/investigative, sync logs are detailed synchronization records, roadmap notes are short current-planning companions, BEACON is the reconnection entrance, and current snapshots are detailed current-state records

## Roadmap interpretation

Phase 3.1 is not yet a connector phase.

Phase 3.1 is also not yet a production runtime phase.

Phase 3.1 may consider a minimal synthetic runtime fixture or bounded runtime-checking stub only after the runtime-event checking plan preconditions are satisfied.

It does not yet include:

- service-specific connectors
- production runtime integration
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

## Priority order across remaining work

Use this priority order while continuing from the current repository state.

### Priority 1: preserve current operation and restartability

Do first when the repository has gained several operation-policy commits or the session has become heavy:

- keep `BEACON.md` as the short reconnection entrance
- keep `docs/phase-3-1-current-snapshot.md` as the detailed current-state record
- keep `docs/operation-index.md` aligned with document-role changes
- avoid letting `CHANGELOG.md` become the construction-time restart path
- avoid letting roadmap notes become changelogs or sync logs become phase plans

### Priority 2: stabilize Phase 3.1 before runtime work

Do before any runtime checker or runtime fixture work:

- confirm that `docs/runtime-event-checking-plan.md` preconditions remain satisfied or update the plan if they do not
- keep `examples/runtime-event-to-pathway-minimal.yaml` readable as a pathway example
- keep `examples/adapter-input-event-minimal.json` synthetic, vendor-neutral, and review-required
- keep runtime-event schema and JSON fixture checking deferred unless deliberately opened

### Priority 3: minimal runtime candidate

After Priority 1 and Priority 2 are stable, consider one narrow runtime candidate:

- either a minimal synthetic runtime fixture
- or a bounded runtime-checking stub

The candidate must be:

- non-production
- synthetic
- local to the repository
- review-required
- non-certifying
- disconnected from service-specific connectors
- disconnected from automatic approval or execution
- explicit about missing context and excluded claims

Do not start production runtime integration.

Do not add a runtime workflow until the local runtime candidate and checking boundary are stable.

### Priority 4: checker expansion only after examples stabilize

Only after the minimal runtime candidate is stable, consider bounded checker work.

Possible future checker work remains limited to structural checks and must not claim:

- adapter mapping correctness
- service connector correctness
- schema completeness
- JSON semantic correctness
- legal validity
- safety
- compliance
- fairness
- production readiness
- AI final-responsibility transfer

### Priority 5: defer larger expansion

Keep the following deferred until lower-risk layers are stable:

- service-specific connectors
- production conversion code
- production runtime integration
- Class E positive examples
- Lean expansion around adapter or runtime-event concepts
- action-class-specific checker enforcement beyond documented future work

## Next low-risk work

The next low-risk work is planning and bounded artifact preparation only:

1. keep runtime-event checking deferred until the plan preconditions are explicitly satisfied
2. prepare a minimal runtime candidate design note or fixture only if it remains synthetic, non-production, review-required, and non-certifying
3. keep service-specific connectors deferred
4. keep production conversion code deferred
5. keep production runtime integration deferred
6. keep Lean expansion deferred
7. keep Class E positive examples deferred
8. use periodic operation review if BEACON, snapshots, sync logs, roadmap notes, CHANGELOG usage, checker interpretation, session load, or deferred boundaries drift from actual practice

## Stop conditions

Stop and preserve the current state if:

- a long file update is blocked
- a reader-path update risks overwriting unrelated content
- a checker failure appears
- a proposed runtime candidate starts implying production runtime integration
- a proposed runtime candidate depends on a service-specific connector
- a proposed runtime candidate implies automatic approval or execution
- a proposed change implies certification, production readiness, legal validation, safety certification, compliance certification, fairness certification, moral resolution, connector correctness, adapter correctness, semantic mapping correctness, schema correctness, JSON fixture correctness, or AI final-responsibility transfer

## Restart point

Restart from:

- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/runtime-event-checking-plan.md`
- `docs/operation-index.md`
- this note

Do not continue directly into service-specific connector implementation.

Do not continue directly into production runtime integration.

Do not continue directly into runtime-event checker implementation unless the runtime-event checking plan preconditions are satisfied.
