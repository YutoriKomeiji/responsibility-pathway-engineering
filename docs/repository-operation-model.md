# Repository Operation Model

This document describes how this repository should be operated as it grows.

The purpose is to preserve a readable Responsibility Pathway for repository changes themselves: claims should remain returnable to definitions, examples, schemas, checkers, snapshots, logs, assumptions, and excluded claims.

This document is an operation guide. It is not a certification process, legal review process, safety review process, compliance process, fairness review process, production approval process, or AI final-responsibility transfer mechanism.

## Operating principle

The repository should grow through small, reviewable changes.

Prefer:

- one primary artifact per commit when possible
- small synchronization commits after primary artifact commits
- fetch confirmation after each write
- observed workflow status recorded only after observation
- snapshots when changes span multiple documents
- sync logs when reader paths or coverage maps are synchronized over several commits
- roadmap notes when `ROADMAP.md` would require a large or risky update

Avoid:

- replacing several long files in a single update
- recording a workflow as green before observing it
- treating checker success as certification
- adding production connectors before boundaries, examples, and review requirements are stable
- expanding Lean around unstable examples or schemas
- introducing Class E positive examples before lower classes and stop boundaries remain stable

## Document roles

### `BEACON.md`

`BEACON.md` is the primary reconnection point.

Use it to record:

- current position
- read-first order
- restart point
- major observed workflow status
- current focus
- boundaries that must be preserved before continuing

Do not use it as a full detailed changelog.

### `ROADMAP.md`

`ROADMAP.md` records phase-level direction.

Use it to record:

- major phase status
- next low-risk work
- phase rules
- deferred work

When a roadmap update would require a large full-file replacement, create a short roadmap companion note first.

### `CHANGELOG.md`

`CHANGELOG.md` records conceptual milestones.

Use it for durable milestones that changed how the repository should be read or operated.

Do not use it for every individual code or documentation edit.

When changelog updates become large, preserve detailed synchronization state in a phase-specific sync log and add only a short changelog reference later.

### Current snapshots

Current snapshot files record the current restart position for a phase or subphase.

Examples:

- `docs/phase-2-current-snapshot.md`
- `docs/phase-2-5-current-snapshot.md`
- `docs/phase-3-1-current-snapshot.md`

Use a snapshot when:

- a phase crosses several documents
- the next maintainer needs a compact restart point
- long-file updates become risky
- workflow status and non-certifying interpretation need to be preserved together

Snapshots should include:

- current artifacts
- current status
- observed checks where applicable
- what the phase does not claim
- next low-risk work
- stop conditions
- restart point

### Sync logs

Sync logs record multi-commit synchronization work.

Example:

- `docs/phase-3-1-sync-log.md`

Use a sync log when:

- reader-path updates span several files
- coverage maps are updated in separate commits
- a long file update is deferred
- several commits together form one repository-maintenance operation

A sync log should record:

- primary artifacts added or changed
- observed check status
- reader paths synchronized
- coverage files synchronized
- current checker interpretation
- deferred work
- next safe synchronization step

A sync log is not a certification record.

### Roadmap notes

Roadmap notes are short companions to `ROADMAP.md`.

Example:

- `docs/phase-3-1-roadmap-note.md`

Use a roadmap note when:

- the roadmap position should be recorded
- `ROADMAP.md` is too long or risky to replace directly
- a phase needs a temporary planning bridge before main roadmap synchronization

A roadmap note should record:

- phase status
- current artifacts
- reached checkpoint
- roadmap interpretation
- next low-risk work
- stop conditions
- restart point

### Example index and checker coverage

`docs/example-index.md` explains how examples should be read.

`docs/checker-coverage.md` explains what current checkers do and do not check.

Update them after adding or changing examples.

Keep the distinction clear:

- example index: reading purpose and interpretation
- checker coverage: implemented structural checker behavior

## Staged update operation

For repository-wide synchronization, use staged update operation.

Recommended sequence:

1. add or update the primary artifact
2. fetch the primary artifact after writing
3. run or observe the bounded checker when applicable
4. fix structural checker failures with the smallest possible change
5. record observed workflow status only after observation
6. create or update a current snapshot when the change spans multiple documents
7. create or update a sync log when reader-path synchronization spans multiple commits
8. update example index and checker coverage as separate small commits
9. update README and README.ja as separate small commits
10. update BEACON as a reconnection commit
11. use a roadmap note before changing long roadmap sections
12. add short ROADMAP or CHANGELOG references only after the detailed state has a stable document to point to

If a long full-file update is blocked or risky, stop the full update and preserve current state in a smaller snapshot, sync log, or roadmap note first.

## Workflow observation policy

Only record a workflow result as observed green after the run has actually been observed.

When recording observed green status, include:

- workflow name
- run number or run id when available
- commit sha or short sha
- job name when available
- bounded interpretation

A green status means only that the relevant bounded repository-maintenance check passed for that repository state.

It does not mean:

- legal validity
- safety
- compliance
- fairness
- moral resolution
- institutional approval
- production readiness
- connector correctness
- adapter correctness
- AI final-responsibility transfer

## Checker interpretation policy

Checker documentation must distinguish between:

- what is actually checked now
- what is planned future checker work
- what is explicitly not claimed

For example, the current runtime-event bridge state distinguishes:

- `examples/runtime-event-to-pathway-minimal.yaml` is checked only as a pathway example
- `spec/runtime-event.schema.yaml` is not yet validated by the current checker
- `examples/adapter-input-event-minimal.json` is not yet checked by `scripts/check_examples.py`
- adapter mapping correctness is not yet checked
- service-specific connector behavior is not yet checked

## Long-file update policy

Treat the following files as long or high-risk files:

- `ROADMAP.md`
- `CHANGELOG.md`
- `BEACON.md`
- README files when they grow large
- large index or coverage documents

Before replacing a long file:

1. fetch the current file
2. identify the smallest section to update
3. prefer a companion note if the update is broad
4. avoid unrelated rewrites
5. fetch after update

If a full update is blocked, do not retry by sending larger content. Use staged operation instead.

## Log organization policy

Phase-specific logs may be stored either directly under `docs/` or under a future `docs/logs/` directory.

For the current repository state, avoid moving existing logs unless the link update is small and deliberate.

Recommended near-term approach:

- keep existing phase-specific logs in their current paths
- use new phase-specific logs only when a synchronization operation spans multiple commits
- do not create a single global log that absorbs all details

A future `docs/logs/` directory may be introduced when there are enough logs to justify moving them.

If logs are moved, update all links in README, README.ja, BEACON, snapshots, roadmap notes, and related docs in small commits.

## Non-certifying operation boundary

Repository operation practices preserve maintainability, traceability, and returnability.

They do not certify the repository, examples, schemas, checkers, generated records, adapters, connectors, workflows, Lean files, or public claims.

The human author or maintainer remains responsible for deciding whether a change should be made, published, relied upon, reverted, repaired, or deferred.

AI tools may assist drafting, organization, review, and implementation, but they do not assume final responsibility.

## Restart rule

When unsure where to restart:

1. read `BEACON.md`
2. read the current phase snapshot
3. read the relevant sync log or roadmap note
4. inspect the current example index and checker coverage
5. fetch the file before changing it
6. make one small change
7. fetch again after writing

Do not continue directly into production connectors, production conversion code, high-impact examples, or new formal claims unless the relevant boundary documents and examples are already stable.
