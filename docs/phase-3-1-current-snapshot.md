# Phase 3.1 Current Snapshot

This snapshot records the current Phase 3.1 position for the adapter boundary and runtime event bridge.

Phase 3.1 is the bridge from external logs, API events, workflow results, and runtime observations into draft Responsibility Pathway records.

It is not a production connector, production runtime, verification engine, certification tool, legal decision system, compliance engine, safety certification system, fairness certification tool, moral-resolution system, or AI final-responsibility transfer mechanism.

## Current artifacts

Current Phase 3.1 artifacts:

- `docs/adapter-boundary.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`
- `docs/repository-operation-model.md`

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

This means large documentation or reader-path updates should be split into small commits instead of replacing several long files at once.

The recommended order is:

1. create or update the primary artifact
2. observe or verify the bounded checker result when applicable
3. create a small current snapshot when the change crosses multiple documents
4. synchronize reader paths in README, README.ja, BEACON, ROADMAP, and CHANGELOG in separate small commits
5. synchronize example index and checker coverage in separate small commits
6. fetch the changed files after each commit
7. record observed green workflow status only after it has been observed

If a large full-file update is blocked or becomes risky, stop the full update and preserve the current state in a smaller snapshot file first.

This staged operation is a repository-maintenance practice. It does not certify the repository, examples, schemas, generated records, or future adapters.

## Current boundary

The current Phase 3.1 set does not provide:

- service-specific connectors
- production runtime integration
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

1. add `docs/repository-operation-model.md` to README, README.ja, BEACON, ROADMAP, and CHANGELOG reader paths as small commits
2. add this snapshot to ROADMAP and CHANGELOG through short references or companion notes
3. keep service-specific connectors deferred
4. keep conversion code deferred until the event schema and examples remain stable
5. keep Class E positive examples deferred
6. keep Lean expansion around adapter and runtime events deferred

## Restart point

Restart from this file when continuing Phase 3.1.

Also read `docs/repository-operation-model.md` before broad synchronization work.

The next direct implementation step should not be a production connector.

The next direct documentation step should be reader-path synchronization for the repository operation model and remaining Phase 3.1 roadmap/changelog references.
