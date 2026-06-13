# Phase 3.1 Current Snapshot

This snapshot records the current Phase 3.1 position for the adapter boundary, runtime event bridge, runtime-event checking plan, and repository operation layer.

Phase 3.1 is the bridge from external logs, API events, workflow results, and runtime observations into draft Responsibility Pathway records.

It is not a production connector, production runtime, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Current artifacts

Current Phase 3.1 artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `docs/runtime-event-checking-plan.md`
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

## Runtime-event checking synchronization

The runtime-event checking plan has been synchronized across the repository-maintenance reader path.

Current synchronization status:

- `docs/operation-index.md` points runtime-event schema checking, JSON fixture checking, and future runtime-event checker work to `docs/runtime-event-checking-plan.md` first
- `docs/phase-3-1-sync-log.md` records the runtime-event checking plan synchronization as one responsibility unit split across multiple small commits
- `docs/phase-3-1-roadmap-note.md` records that Phase 3.1 is not yet a runtime-event checker implementation phase
- `ROADMAP.md` records the runtime-event checking rule before implementation
- `CHANGELOG.md` records the runtime-event checking plan as a conceptual milestone before checker implementation
- `docs/checker-coverage.md` records that current checkers do not validate `spec/runtime-event.schema.yaml` or `examples/adapter-input-event-minimal.json`
- `docs/example-index.md` records that `examples/runtime-event-to-pathway-minimal.yaml` is currently checked only as a pathway example and that runtime-event checks are not yet implemented

This synchronization does not unlock runtime-event checker implementation.

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
- runtime-event schema correctness proof
- JSON fixture correctness proof
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

1. keep service-specific connectors deferred
2. keep production conversion code deferred
3. keep runtime-event schema checking deferred until the schema and examples remain stable and `docs/runtime-event-checking-plan.md` preconditions are satisfied
4. keep JSON fixture checking deferred until the current event-to-pathway bridge remains readable and reviewable and `docs/runtime-event-checking-plan.md` preconditions are satisfied
5. do not add `scripts/check_runtime_events.py` or a runtime-event workflow until the checking plan preconditions are satisfied
6. keep Class E positive examples deferred
7. keep Lean expansion around adapter and runtime events deferred
8. maintain `docs/operation-index.md` when operation documents, snapshots, sync logs, roadmap notes, checker plans, session handoff rules, document usage phase rules, sync-log/roadmap-note role separation, or BEACON/snapshot role separation changes
9. use periodic operation review when commit granularity, reader paths, logs, roadmap notes, checker interpretation, document usage phase, BEACON/snapshot separation, sync-log/roadmap-note separation, session load, or deferred boundaries feel misaligned with actual practice
10. add only short ROADMAP or CHANGELOG references after the detailed state has a stable snapshot, sync log, roadmap note, checker plan, or operation document to point to
11. consider only a minimal, synthetic, non-production runtime fixture or runtime-checking stub after `docs/runtime-event-checking-plan.md` preconditions are satisfied; do not start production runtime integration

## Restart point

Restart from this file when continuing Phase 3.1.

Also read:

1. `BEACON.md`
2. `docs/repository-operation-model.md`
3. `docs/operation-index.md`
4. `docs/phase-3-1-sync-log.md`
5. `docs/phase-3-1-roadmap-note.md`
6. `docs/adapter-boundary.md`
7. `docs/runtime-event-checking-plan.md`
8. `docs/checker-coverage.md`
9. `docs/example-index.md`
10. `spec/runtime-event.schema.yaml`
11. `examples/adapter-input-event-minimal.json`
12. `examples/runtime-event-to-pathway-minimal.yaml`

Use `CHANGELOG.md` after these current-state documents only when a milestone, historical cause, serious inconsistency, or prior boundary decision needs investigation.

If continuing after a long or heavy session, use `docs/repository-operation-model.md` and `docs/operation-index.md` to confirm the session load and handoff policy before making broad changes.

The next direct implementation step should not be a production connector.

The next direct runtime step should not be production runtime integration. A minimal synthetic runtime fixture or bounded checker stub may be considered only after the runtime-event checking plan preconditions are satisfied.

The next direct checker step should not begin until `docs/runtime-event-checking-plan.md` preconditions are satisfied.
