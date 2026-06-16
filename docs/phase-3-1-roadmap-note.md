# Phase 3.1 Roadmap Note

This note records the current roadmap position for Phase 3.1 Adapter Boundary and Runtime Event Bridge.

It exists as a short roadmap companion so that the long `ROADMAP.md` file does not need to be replaced in one large update when repository-wide synchronization is underway.

This note is planning-only. It is not certification, legal review, safety review, compliance review, fairness review, production approval, connector correctness proof, runtime correctness proof, schema correctness proof, JSON semantic correctness proof, conformance evidence, or AI final-responsibility transfer mechanism.

## Phase 3.1 status

Phase 3.1 has reached a bounded runtime-event bridge checkpoint.

The current Phase 3.1 work establishes a draft, vendor-neutral, review-required bridge from runtime observations to Responsibility Pathway draft records.

It now includes:

- a draft runtime-event schema
- a selected synthetic runtime-event JSON fixture
- a selected minimal synthetic runtime observation fixture
- a runtime-event-to-pathway draft example
- a bounded runtime-event checker stub
- observed local checker behavior
- a minimal runtime-event workflow
- observed workflow successes
- focused workflow observation notes
- a runtime-event schema/fixture alignment note
- operation-index, current-snapshot, current-task-inventory, and focused sync-note connections

Current artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/minimal-synthetic-runtime-fixture.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `scripts/check_runtime_events.py`
- `.github/workflows/check-runtime-events.yml`
- `docs/runtime-event-checking-plan.md`
- `docs/runtime-event-schema-fixture-alignment.md`
- `docs/runtime-event-workflow-current-status.md`
- `docs/minimal-runtime-fixture-checker-workflow-observation.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-connection.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md`
- `docs/minimal-runtime-candidate-design.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/current-task-inventory.md`
- `docs/repository-operation-model.md`
- `docs/operation-index.md`

## What has been reached

The following checkpoint has been reached:

- adapter boundary documented
- minimal runtime event schema added
- minimal synthetic JSON input event added
- minimal runtime-event-to-pathway draft example added
- minimal synthetic runtime observation fixture added and reviewed
- `scripts/check_runtime_events.py` added as a bounded structural checker for selected JSON fixtures
- `examples/adapter-input-event-minimal.json` is checked by the bounded runtime-event checker
- `examples/minimal-synthetic-runtime-fixture.json` is checked by the bounded runtime-event checker for runtime-boundary signals
- `.github/workflows/check-runtime-events.yml` added as a minimal runtime-event workflow
- first runtime-event workflow success observed on run `27501847137`
- minimal runtime fixture checker workflow success observed on run `27607798655`
- `docs/runtime-event-schema-fixture-alignment.md` added as an alignment note, not validation
- reader paths synchronized in operation index, current snapshot, task inventory, checker coverage, focused observation notes, and focused sync notes
- repository operation layer added through `docs/repository-operation-model.md` and `docs/operation-index.md`
- periodic operation review policy added for repository-maintenance alignment
- operation-document roles clarified: `CHANGELOG.md` is archival/investigative, sync logs are detailed synchronization records, roadmap notes are short current-planning companions, BEACON is the reconnection entrance, and current snapshots are detailed current-state records

## Roadmap interpretation

Phase 3.1 is still not a connector phase.

Phase 3.1 is still not a production runtime phase.

The current runtime-event checker and workflow are bounded repository-maintenance tools only.

The current schema/fixture alignment note records structural alignment and reviewability only. It does not validate the schema, prove semantic correctness, prove adapter mapping correctness, prove runtime correctness, or provide conformance evidence.

Phase 3.1 does not yet include:

- service-specific connectors
- production runtime integration
- production conversion code
- full runtime-event schema validation
- full JSON schema-fixture validation
- event-to-pathway semantic correctness checking
- adapter mapping correctness checker
- responsibility assignment correctness checker
- action-class-specific checker enforcement
- Class E positive examples
- conformance-model drafting
- Lean expansion around adapter or runtime-event concepts

## Runtime-event checking rule

The current `scripts/check_runtime_events.py` checker may be maintained as a bounded structural checker for selected synthetic JSON fixtures.

Any future passing runtime-event check must remain a bounded repository-maintenance signal only.

A passing runtime-event check must not be interpreted as certification, legal review, safety review, compliance review, fairness review, production approval, connector correctness proof, adapter correctness proof, schema correctness proof, JSON fixture correctness proof, semantic mapping correctness proof, responsibility assignment proof, conformance evidence, or AI final-responsibility transfer.

Do not expand runtime-event schema checking, broad JSON schema-fixture validation, event-to-pathway semantic checking, connector work, production runtime work, conformance claims, public standardization claims, or Lean runtime expansion from the current checker pass alone.

## Minimal runtime candidate rule

Use `docs/minimal-runtime-candidate-design.md` before adding any further runtime candidate.

The first candidate now exists as a minimal synthetic runtime observation fixture.

The candidate must remain:

- non-production
- synthetic
- local to the repository
- review-required
- non-certifying
- disconnected from service-specific connectors
- disconnected from automatic approval or execution
- explicit about missing context, missing approval evidence, missing execution evidence, and excluded claims

This design note does not unlock production runtime integration, service-specific connectors, production conversion code, automatic approval, automatic execution, certification, runtime correctness claims, or AI final-responsibility transfer.

## Priority order across remaining work

Use this priority order while continuing from the current repository state.

### Priority 1: preserve current operation and restartability

Do first when the repository has gained several operation-policy commits or the session has become heavy:

- keep `BEACON.md` as the short reconnection entrance
- keep `docs/phase-3-1-current-snapshot.md` as the detailed current-state record
- keep `docs/operation-index.md` aligned with document-role and reader-path changes
- keep `docs/current-task-inventory.md` aligned with actual Phase 3.1 status
- avoid letting `CHANGELOG.md` become the construction-time restart path
- avoid letting roadmap notes become changelogs or sync logs become phase plans

### Priority 2: stabilize schema / fixture / checker alignment

Do before any semantic or schema-validation expansion:

- keep `docs/runtime-event-schema-fixture-alignment.md` current when schema, fixture, or checker interpretation changes
- keep `docs/checker-coverage.md` explicit about what is checked and what is not checked
- keep `examples/adapter-input-event-minimal.json` synthetic, vendor-neutral, and review-required
- keep `examples/minimal-synthetic-runtime-fixture.json` synthetic, local, non-production, vendor-neutral, review-required, non-certifying, and disconnected from automatic approval or execution
- keep runtime-event schema checking deferred unless deliberately opened
- keep semantic responsibility correctness checking deferred

### Priority 3: external review preparation

After Priority 1 and Priority 2 remain stable, prepare focused external-review material only when it improves reviewability.

Possible next artifacts:

- external review readiness checklist
- event-to-pathway relation checker plan
- source-based related-work comparison notes
- terminology stabilization notes

These artifacts must remain review aids only and must not imply certification, conformance, legal validity, safety, compliance, fairness, production readiness, connector correctness, runtime correctness, or AI final-responsibility transfer.

### Priority 4: checker expansion only after examples stabilize

Only after the current schema/fixture/checker alignment remains stable, consider bounded checker work.

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
- conformance
- AI final-responsibility transfer

### Priority 5: defer larger expansion

Keep the following deferred until lower-risk layers are stable:

- service-specific connectors
- production conversion code
- production runtime integration
- Class E positive examples
- Lean expansion around adapter or runtime-event concepts
- action-class-specific checker enforcement beyond documented future work
- conformance-model drafting
- public standardization claims

## Next low-risk work

The next low-risk work is repository reviewability and alignment work only:

1. keep `docs/runtime-event-schema-fixture-alignment.md` connected from operation index, task inventory, and snapshot paths
2. keep `docs/checker-coverage.md`, `docs/example-index.md`, and current snapshot aligned after any checker or fixture interpretation change
3. prepare an external review readiness checklist only if it makes a specific boundary easier to inspect
4. prepare an event-to-pathway relation checker plan only as a plan, not as semantic correctness checking
5. keep service-specific connectors deferred
6. keep production conversion code deferred
7. keep production runtime integration deferred
8. keep Lean expansion deferred
9. keep Class E positive examples deferred
10. use periodic operation review if BEACON, snapshots, sync logs, roadmap notes, CHANGELOG usage, checker interpretation, session load, or deferred boundaries drift from actual practice

## Stop conditions

Stop and preserve the current state if:

- a long file update is blocked
- a reader-path update risks overwriting unrelated content
- a checker failure appears
- a proposed runtime candidate starts implying production runtime integration
- a proposed runtime candidate depends on a service-specific connector
- a proposed runtime candidate implies automatic approval or execution
- a proposed change implies certification, production readiness, legal validation, safety certification, compliance certification, fairness certification, moral resolution, connector correctness, adapter correctness, semantic mapping correctness, schema correctness, JSON fixture correctness, conformance evidence, or AI final-responsibility transfer

## Restart point

Restart from:

- `BEACON.md`
- `docs/operation-index.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/current-task-inventory.md`
- `docs/runtime-event-schema-fixture-alignment.md`
- `docs/runtime-event-checking-plan.md`
- `docs/runtime-event-workflow-current-status.md`
- `docs/phase-3-1-minimal-runtime-fixture-checker-sync-note.md`
- this note

Do not continue directly into service-specific connector implementation.

Do not continue directly into production runtime integration.

Do not continue directly into schema validation, semantic checking, or conformance drafting unless the relevant preconditions are deliberately reopened and still satisfied.
