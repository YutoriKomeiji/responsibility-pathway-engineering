# Phase 3.1 Current Snapshot

This snapshot records the current Phase 3.1 position for the adapter boundary, runtime event bridge, runtime-event checking plan, minimal runtime candidate planning, minimal synthetic runtime fixture, minimal runtime fixture review, current task inventory, and repository operation layer.

Phase 3.1 is the bridge from external logs, API events, workflow results, and runtime observations into draft Responsibility Pathway records.

It is not a production connector, production runtime, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Current artifacts

Current Phase 3.1 artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `examples/minimal-synthetic-runtime-fixture.json`
- `docs/runtime-event-checking-plan.md`
- `docs/minimal-runtime-candidate-design.md`
- `docs/minimal-runtime-fixture-review.md`
- `docs/minimal-runtime-fixture-review-connection.md`
- `docs/current-task-inventory.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/phase-3-1-roadmap-note.md`
- `docs/repository-operation-model.md`
- `docs/operation-index.md`

Repository-wide reader-path and operation records now also include:

- `README.md`
- `README.ja.md`
- `BEACON.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `docs/checker-coverage.md`
- `docs/example-index.md`

## Adapter boundary

`docs/adapter-boundary.md` defines the planned adapter layer as a support layer that may extract, normalize, summarize, classify, and transform external event data into draft Responsibility Pathway records.

An adapter may support:

- source event extraction
- event-field normalization
- source reference preservation
- candidate action-class suggestion
- candidate role detection
- uncertainty and missing-context recording
- draft record generation for human or institutional review

An adapter must not decide responsibility, approve actions, certify records, prove safety, prove compliance, resolve legal or moral responsibility, or transfer final responsibility to AI.

## Runtime event schema

`spec/runtime-event.schema.yaml` defines a minimal vendor-neutral input event shape.

The first runtime event schema is intentionally small. It preserves:

- event identity
- schema version
- source system
- observation timestamp
- observed actor
- observed action
- observed target
- evidence and missing-context notes
- review requirement
- excluded claims

The schema is draft-only and does not assume a vendor-specific connector.

## Minimal input fixture

`examples/adapter-input-event-minimal.json` is the first synthetic runtime event input fixture.

The fixture models an AI support agent drafting an internal document update proposal.

The fixture explicitly records that:

- the source system is synthetic and vendor-neutral
- the observed actor is an AI agent
- the AI agent does not claim final responsibility
- the event is a draft proposal only
- human approval evidence is missing
- execution evidence is missing
- human or institutional review is required
- the proposed action class is an adapter suggestion, not certification

## Event-to-pathway example

`examples/runtime-event-to-pathway-minimal.yaml` is the first runtime-event-to-pathway draft example.

It maps the synthetic runtime event into a Responsibility Pathway record with:

- lifecycle state `originating`
- AI support agent node
- human decision owner node
- internal document system node
- return-to-authority edge
- possible future execution edge after human approval
- Decision Owner
- Approval Gate
- Execution Actor
- Stop Authority
- Repair Owner
- Evidence Log
- Human Return Point
- review requirement
- adapter boundary fields
- excluded claims

The generated pathway record remains a draft requiring human review.

## Runtime-event checking plan

`docs/runtime-event-checking-plan.md` defines the planned path for adding bounded runtime-event schema and JSON-fixture checks.

The plan exists before implementation so that runtime-event checking can remain small, structural, reviewable, and non-certifying.

The plan records:

- what a future runtime-event checker may inspect
- what the first checker must not inspect
- preconditions before adding `scripts/check_runtime_events.py`
- suggested implementation order
- the boundary for passing checks
- the current decision that runtime-event checking remains deferred

The plan does not implement a checker and does not certify schema correctness, JSON fixture correctness, adapter mapping correctness, service-specific connector behavior, production runtime behavior, legal validity, safety, compliance, fairness, moral resolution, production readiness, or AI final-responsibility transfer.

## Minimal runtime candidate design

`docs/minimal-runtime-candidate-design.md` defines the narrowest acceptable shape for an early runtime candidate.

The design note exists before any runtime fixture, runtime checker, runtime workflow, connector, or production runtime implementation.

It allows only one first candidate:

- a minimal synthetic runtime fixture
- or a bounded runtime-checking stub

The current preferred first candidate, if the runtime path is opened, is a minimal synthetic runtime fixture rather than a checker stub.

The candidate must remain non-production, synthetic, local to the repository, review-required, non-certifying, disconnected from service-specific connectors, disconnected from automatic approval or execution, and explicit about missing context, missing approval evidence, missing execution evidence, and excluded claims.

The design note does not implement a runtime, connector, checker, workflow, adapter, production integration, approval system, execution system, certification system, legal decision system, safety certification system, compliance engine, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Minimal synthetic runtime fixture

`examples/minimal-synthetic-runtime-fixture.json` is the first minimal synthetic runtime observation fixture.

It is a runtime-like observation point, not a runtime implementation.

The fixture is:

- non-production
- synthetic
- vendor-neutral
- local to the repository
- review-required
- non-certifying
- disconnected from service-specific connectors
- disconnected from automatic approval
- disconnected from automatic execution
- explicit about missing approval evidence
- explicit about missing execution evidence
- explicit about excluded claims

It references `examples/adapter-input-event-minimal.json` as the source event reference for the observed draft proposal.

The fixture is not currently checked by `scripts/check_examples.py` and does not unlock runtime-event checker implementation, runtime workflow implementation, service-specific connector work, production conversion code, or production runtime integration.

## Minimal runtime fixture review

`docs/minimal-runtime-fixture-review.md` records the first review of `examples/minimal-synthetic-runtime-fixture.json` as a minimal synthetic runtime observation fixture for reading and review.

The first review found that the fixture is acceptable as a first minimal synthetic runtime observation fixture.

No change to `examples/minimal-synthetic-runtime-fixture.json` was required by that review.

`docs/minimal-runtime-fixture-review-connection.md` records the reader path connecting the review note to the current Phase 3.1 operation documents.

The review note and connection note do not unlock production runtime integration, service-specific connectors, production conversion code, runtime-event checker implementation, runtime fixture checker implementation, runtime workflow implementation, schema correctness claims, JSON semantic correctness claims, adapter mapping correctness claims, connector correctness claims, responsibility assignment correctness claims, Class E positive examples, or Lean expansion around runtime events.

## Current task inventory

`docs/current-task-inventory.md` records the current P0-P4 task inventory across active and near-active phases.

Use it before selecting the next task, especially before checker work, workflow work, runtime work, Lean expansion, connector work, Class E examples, or public-claim expansion.

For Phase 3.1, the inventory currently treats runtime fixture review as bounded artifact preparation and keeps runtime fixture checking, runtime-event checker implementation, runtime workflows, service-specific connectors, production conversion code, production runtime integration, Class E positive examples, support-call schema fields, missed-support schema fields, support-call semantic checking, missed-support correctness checking, and Lean expansion around runtime events, support-call policy, or missed-support signals deferred or conditional.

The task inventory is a planning and prioritization note only. It is not certification, production approval, legal review, safety review, compliance review, fairness review, connector correctness proof, adapter correctness proof, runtime correctness proof, Lean completeness proof, or AI final-responsibility transfer.

## Runtime-event checking synchronization

The runtime-event checking plan has been synchronized across the repository-maintenance reader path.

Current synchronization status:

- `docs/operation-index.md` points runtime-event schema checking, JSON fixture checking, and future runtime-event checker work to `docs/runtime-event-checking-plan.md` first
- `docs/operation-index.md` points runtime candidate selection to `docs/minimal-runtime-candidate-design.md` before any runtime candidate is added
- `docs/operation-index.md` points minimal runtime fixture review to `docs/minimal-runtime-fixture-review.md` before changing the minimal runtime fixture or treating its first review as current
- `docs/operation-index.md` points task selection to `docs/current-task-inventory.md` before starting higher-risk work
- `docs/phase-3-1-sync-log.md` records the runtime-event checking plan synchronization as one responsibility unit split across multiple small commits
- `docs/phase-3-1-roadmap-note.md` records that Phase 3.1 is not yet a runtime-event checker implementation phase or production runtime phase
- `docs/example-index.md` records the minimal synthetic runtime fixture as a runtime candidate fixture for reading and review only
- `docs/checker-coverage.md` records that current checkers do not validate `spec/runtime-event.schema.yaml`, `examples/adapter-input-event-minimal.json`, or `examples/minimal-synthetic-runtime-fixture.json`
- `ROADMAP.md` records the runtime-event checking rule before implementation
- `CHANGELOG.md` records the runtime-event checking plan as a conceptual milestone before checker implementation

This synchronization does not unlock runtime-event checker implementation, runtime workflow implementation, service-specific connectors, or production runtime integration.

## Open-source review intent

The repository is prepared so that future open-source review can inspect boundaries, responsibility paths, examples, schemas, checker limits, runtime fixture limits, and deferred implementation choices.

Open-source review is intended to help others examine whether the repository preserves return paths from claims to definitions, examples, schemas, checker boundaries, excluded claims, operation documents, runtime candidate boundaries, and deferred work.

Opening the repository for review does not itself certify the repository, approve production use, prove connector correctness, prove adapter correctness, prove schema correctness, prove runtime correctness, or transfer final responsibility to reviewers, users, or AI systems.

## Repository operation layer

Phase 3.1 now has an explicit repository-operation layer.

`docs/repository-operation-model.md` records:

- document purpose and usage phase policy
- staged update operation
- synchronization unit operation
- session load and handoff policy
- sync-log and roadmap-note separation policy
- document roles
- snapshot roles
- sync-log roles
- roadmap-note roles
- commit granularity policy
- periodic operation review policy
- workflow observation policy
- checker interpretation policy
- long-file update policy
- log organization policy
- non-certifying operation boundaries
- restart rules

`docs/operation-index.md` records which operation-related document to read for each maintenance situation.

The operation index is now connected from:

- `docs/repository-operation-model.md`
- `README.md`
- `README.ja.md`
- `BEACON.md`

`docs/runtime-event-checking-plan.md` is now connected from `docs/operation-index.md` as the plan to read before considering runtime-event schema checking, JSON fixture checking, or future runtime-event checker work.

`docs/minimal-runtime-candidate-design.md` is now connected from `docs/operation-index.md` as the design note to read before considering a minimal synthetic runtime fixture or bounded runtime-checking stub.

`docs/minimal-runtime-fixture-review.md` is now connected from `docs/operation-index.md` as the review note to read before changing the minimal runtime fixture or treating its first review as current.

`docs/current-task-inventory.md` is now connected from `docs/operation-index.md` as the task-priority note to read before selecting the next task.

`docs/operation-index.md` also now points readers to the session load and handoff policy when session load is becoming heavy or a durable restart path is needed.

`docs/operation-index.md` now states that `CHANGELOG.md` is not part of the primary construction-time reconnection path and should be used mainly for archival, investigative, historical, or retrospective milestone review.

`docs/operation-index.md` now separates `docs/phase-3-1-sync-log.md` as the detailed synchronization record from `docs/phase-3-1-roadmap-note.md` as the short current-planning companion.

`docs/operation-index.md` now separates `BEACON.md` as the short reconnection entrance from current snapshots as detailed current-state records.

`CHANGELOG.md` now records the periodic operation review policy as a conceptual milestone.

## Document usage phases

Current construction should use the document whose purpose matches the task.

For active construction and restart, prefer:

- `BEACON.md`
- this current snapshot
- `docs/operation-index.md`
- `docs/phase-3-1-sync-log.md`
- `docs/phase-3-1-roadmap-note.md`
- `docs/current-task-inventory.md`
- `docs/checker-coverage.md`
- `docs/example-index.md`
- the primary artifact being changed

Use `CHANGELOG.md` mainly for archival review, serious error investigation, historical cause tracing, or retrospective explanation of when and why a boundary or policy changed.

If active construction starts relying on `CHANGELOG.md` as the primary restart path, use periodic operation review to correct the reading path.

## BEACON and current snapshot separation

`BEACON.md` is the reconnection entrance.

It should stay compact and focus on:

- current focus
- read-first order
- restart pointer
- short boundary reminders
- continuity across sessions

This current snapshot is the detailed current-state record.

It should preserve:

- current artifacts
- current synchronization state
- observed bounded checks
- detailed deferred boundaries
- next low-risk work
- stop conditions
- restart details

Do not use `BEACON.md` as a full snapshot or second changelog.

Do not use this snapshot to replace the short reconnection role of `BEACON.md`.

If `BEACON.md` grows too large, move detailed state into this snapshot, a sync log, a roadmap note, checker coverage, or example index, then keep BEACON focused on reconnection.

## Sync log and roadmap note separation

`docs/phase-3-1-sync-log.md` and `docs/phase-3-1-roadmap-note.md` are complementary but separate.

Use the sync log to understand:

- what changed across several commits
- which reader paths, coverage maps, or checker interpretations were synchronized
- what checker status or bounded interpretation was current at the time
- what work remained deferred after a synchronization unit

Use the roadmap note to understand:

- the current near-term roadmap position
- the next low-risk work
- current phase rules and stop conditions
- what should not be started yet
- how to avoid changing a long `ROADMAP.md` section too early

Do not use the roadmap note as a second changelog.

Do not use the sync log as a phase plan.

## Commit granularity, session load, and operation review

The current repository operation rule is responsibility-unit based.

Prefer one commit per responsibility unit, not one commit per file, where the tooling permits. When the GitHub contents API requires per-file updates, treat the synchronized set as one responsibility unit in planning and reporting.

Session load should affect working size:

- early sessions may handle larger but coherent synchronization units
- middle sessions should use smaller responsibility units and frequent fetch confirmation
- late sessions should avoid broad edits and prefer snapshots, sync logs, roadmap notes, BEACON updates, or handoff notes
- before session migration, preserve current state if the restart path would otherwise be unclear

Use periodic operation review when:

- commit granularity feels too small or too large
- reader paths become long or scattered
- BEACON starts carrying detailed snapshot history or changelog-like content
- operation documents, snapshots, sync logs, or roadmap notes start multiplying
- task inventories drift from actual repository state
- sync logs and roadmap notes start duplicating each other
- active construction starts relying on `CHANGELOG.md` as the primary restart path
- checker interpretation and actual practice drift apart
- deferred boundaries need to be reconsidered
- observed workflow results need to remain bounded and non-certifying
- session load becomes heavy or a session handoff needs a durable restart path

Periodic operation review is a repository-maintenance practice only. It is not production approval, connector correctness proof, adapter correctness proof, legal review, safety review, compliance review, fairness review, Lean completeness proof, or AI final-responsibility transfer.

## Observed check status

`Check examples #16` was observed green on commit `d377be2` on `main`.

The GitHub Actions run was `27463999395`.

The job was `Bounded structural example checks`.

The job completed successfully after fixing `examples/runtime-event-to-pathway-minimal.yaml` to use the required top-level `return_points` key and to include `human_responsibility_capacity: true` on the human decision owner node.

This observed green status means only that the bounded structural example checker passed for that repository state.

It is not certification.

## Staged update operation

Phase 3.1 uses staged update operation for repository-wide synchronization.

The general repository operation model is documented in `docs/repository-operation-model.md`.

The operation document index is documented in `docs/operation-index.md`.

This means large documentation or reader-path updates should be split into small, reviewable commits instead of replacing several long files at once.

The recommended order is:

1. create or update the primary artifact
2. observe or verify the bounded checker result when applicable
3. create or update a current snapshot when the change crosses multiple documents
4. synchronize operation index or reader paths when navigation changes
5. synchronize README, README.ja, BEACON, ROADMAP, and CHANGELOG in small commits or responsibility-unit batches where supported
6. synchronize example index and checker coverage in separate small commits when examples or checker interpretation change
7. fetch the changed files after each commit
8. record observed green workflow status only after it has been observed
9. run periodic operation review when operation no longer matches actual practice
10. reduce work size and preserve a handoff path when session load becomes heavy

If a large full-file update is blocked or becomes risky, stop the full update and preserve the current state in a smaller snapshot file first.

If session load becomes heavy, avoid broad edits and preserve the current state in a snapshot, sync log, roadmap note, BEACON update, or handoff note before continuing elsewhere.

This staged operation is a repository-maintenance practice. It does not certify the repository, examples, schemas, generated records, operation documents, or future adapters.

## Current boundary

The current Phase 3.1 set does not provide:

- service-specific connectors
- production runtime integration
- production conversion code
- runtime-event schema validation by the checker
- JSON fixture validation by the checker
- runtime fixture validation by the checker
- runtime-event schema correctness proof
- JSON fixture correctness proof
- runtime fixture correctness proof
- adapter mapping correctness checks
- service-specific connector behavior checks
- automatic responsibility decisions
- automatic approval
- automatic execution
- legal validation
- safety certification
- compliance certification
- fairness certification
- moral resolution
- production readiness
- AI final-responsibility transfer

## Next low-risk work

Next safe synchronization steps:

1. use `docs/current-task-inventory.md` before selecting the next task
2. keep service-specific connectors deferred
3. keep production conversion code deferred
4. keep runtime-event schema checking deferred until the schema and examples remain stable and `docs/runtime-event-checking-plan.md` preconditions are satisfied
5. keep JSON fixture checking deferred until the current event-to-pathway bridge remains readable and reviewable and `docs/runtime-event-checking-plan.md` preconditions are satisfied
6. keep runtime fixture checking deferred until the minimal runtime fixture remains stable and `docs/minimal-runtime-candidate-design.md` and `docs/runtime-event-checking-plan.md` boundaries are satisfied
7. keep runtime-event checker implementation deferred until `docs/runtime-event-checking-plan.md` preconditions are satisfied
8. keep runtime workflow implementation deferred until local runtime-checking behavior exists and has been observed
9. use `docs/minimal-runtime-candidate-design.md` before selecting any further runtime candidate
10. keep Class E positive examples deferred
11. keep Lean expansion around adapter and runtime events deferred
12. maintain `docs/operation-index.md` when operation documents, snapshots, sync logs, roadmap notes, task inventories, checker plans, session handoff rules, document usage phase rules, sync-log/roadmap-note role separation, BEACON/snapshot role separation, runtime candidate planning, or minimal runtime fixture review links change
13. use periodic operation review when commit granularity, reader paths, logs, roadmap notes, task inventories, checker interpretation, document usage phase, BEACON/snapshot separation, sync-log/roadmap-note separation, session load, runtime candidate planning, fixture review status, or deferred boundaries feel misaligned with actual practice
14. add only short ROADMAP or CHANGELOG references after the detailed state has a stable snapshot, sync log, roadmap note, checker plan, runtime candidate note, fixture review note, task inventory, or operation document to point to

## Restart point

Restart from this file when continuing Phase 3.1.

Also read:

1. `BEACON.md`
2. `docs/repository-operation-model.md`
3. `docs/operation-index.md`
4. `docs/current-task-inventory.md`
5. `docs/phase-3-1-sync-log.md`
6. `docs/phase-3-1-roadmap-note.md`
7. `docs/adapter-boundary.md`
8. `docs/runtime-event-checking-plan.md`
9. `docs/minimal-runtime-candidate-design.md`
10. `docs/minimal-runtime-fixture-review.md`
11. `docs/checker-coverage.md`
12. `docs/example-index.md`
13. `spec/runtime-event.schema.yaml`
14. `examples/adapter-input-event-minimal.json`
15. `examples/minimal-synthetic-runtime-fixture.json`
16. `examples/runtime-event-to-pathway-minimal.yaml`

Use `CHANGELOG.md` after these current-state documents only when a milestone, historical cause, serious inconsistency, or prior boundary decision needs investigation.

If continuing after a long or heavy session, use `docs/repository-operation-model.md` and `docs/operation-index.md` to confirm the session load and handoff policy before making broad changes.

The next direct implementation step should not be a production connector.

The next direct runtime step should not be production runtime integration. Any further runtime candidate must go through `docs/minimal-runtime-candidate-design.md` and remain non-production, synthetic, local, review-required, and non-certifying.

The next direct checker step should not begin until `docs/runtime-event-checking-plan.md` preconditions are satisfied.
