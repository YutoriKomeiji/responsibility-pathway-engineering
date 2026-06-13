# Phase 3.1 Current Snapshot

This snapshot records the current Phase 3.1 position for the adapter boundary, runtime event bridge, and repository operation layer.

Phase 3.1 is the bridge from external logs, API events, workflow results, and runtime observations into draft Responsibility Pathway records.

It is not a production connector, production runtime, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Current artifacts

Current Phase 3.1 artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/phase-3-1-roadmap-note.md`
- `docs/repository-operation-model.md`
- `docs/operation-index.md`

Repository-wide reader-path and operation records now also include:

- `README.md`
- `README.ja.md`
- `BEACON.md`
- `CHANGELOG.md`

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

## Repository operation layer

Phase 3.1 now has an explicit repository-operation layer.

`docs/repository-operation-model.md` records:

- staged update operation
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

`CHANGELOG.md` now records the periodic operation review policy as a conceptual milestone.

## Commit granularity and operation review

The current repository operation rule is responsibility-unit based.

Prefer one commit per responsibility unit, not one commit per file, where the tooling permits. When the GitHub contents API requires per-file updates, treat the synchronized set as one responsibility unit in planning and reporting.

Use periodic operation review when:

- commit granularity feels too small or too large
- reader paths become long or scattered
- operation documents, snapshots, sync logs, or roadmap notes start multiplying
- checker interpretation and actual practice drift apart
- deferred boundaries need to be reconsidered
- observed workflow results need to remain bounded and non-certifying

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

If a large full-file update is blocked or becomes risky, stop the full update and preserve the current state in a smaller snapshot file first.

This staged operation is a repository-maintenance practice. It does not certify the repository, examples, schemas, generated records, operation documents, or future adapters.

## Current boundary

The current Phase 3.1 set does not provide:

- service-specific connectors
- production runtime integration
- production conversion code
- runtime-event schema validation by the checker
- JSON fixture validation by the checker
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
3. keep runtime-event schema checking deferred until the schema and examples remain stable
4. keep JSON fixture checking deferred until the current event-to-pathway bridge remains readable and reviewable
5. keep Class E positive examples deferred
6. keep Lean expansion around adapter and runtime events deferred
7. maintain `docs/operation-index.md` when operation documents, snapshots, sync logs, or roadmap notes change
8. use periodic operation review when commit granularity, reader paths, logs, roadmap notes, checker interpretation, or deferred boundaries feel misaligned with actual practice
9. add only short ROADMAP or CHANGELOG references after the detailed state has a stable snapshot, sync log, roadmap note, or operation document to point to

## Restart point

Restart from this file when continuing Phase 3.1.

Also read:

1. `BEACON.md`
2. `docs/repository-operation-model.md`
3. `docs/operation-index.md`
4. `docs/phase-3-1-sync-log.md`
5. `docs/phase-3-1-roadmap-note.md`
6. `docs/adapter-boundary.md`
7. `spec/runtime-event.schema.yaml`
8. `examples/adapter-input-event-minimal.json`
9. `examples/runtime-event-to-pathway-minimal.yaml`

The next direct implementation step should not be a production connector.

The next direct documentation step should be either a short ROADMAP reference update or a periodic operation review if the operation layer becomes misaligned with actual practice.
