# Repository Operation Model

This document describes how this repository should be operated as it grows.

The purpose is to preserve a readable Responsibility Pathway for repository changes themselves: claims should remain returnable to definitions, examples, schemas, checkers, snapshots, logs, assumptions, and excluded claims.

This document is an operation guide. It is not a certification process, legal review process, safety review process, compliance process, fairness review process, production approval process, or AI final-responsibility transfer mechanism.

For a short navigation index of operation-related documents, see `docs/operation-index.md`.

## Operating principle

The repository should grow through small, reviewable changes.

Prefer:

- one primary artifact per commit when possible
- one responsibility unit per commit
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

### `docs/operation-index.md`

`docs/operation-index.md` is the navigation index for operation-related documents.

Use it when:

- you are unsure which operation document to read first
- operation documents, snapshots, sync logs, and roadmap notes are growing
- a future maintainer needs a compact map of repository-maintenance documents
- reader-path updates risk becoming scattered across several files

The operation index should stay short and navigational. It should not replace this operation model, current snapshots, sync logs, roadmap notes, BEACON, ROADMAP, or CHANGELOG.

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

## Synchronization unit operation

A synchronization unit may be larger than one file when several documents must be aligned around the same repository state.

Use a synchronization unit when one conceptual change needs coordinated updates across navigation, snapshots, roadmap notes, changelog milestones, checker coverage, and example interpretation.

For example, the Phase 3.1 runtime-event checking plan synchronization is one responsibility unit even though it is split across several small commits:

- primary plan document
- operation index
- current snapshot
- roadmap
- changelog
- checker coverage
- example index
- sync log
- roadmap note

For a synchronization unit:

1. keep the conceptual purpose stable across all commits
2. update high-risk or long files in small commits
3. preserve detailed state in a sync log or snapshot before changing broad reader paths
4. fetch after every write
5. report the group as one responsibility unit in summaries
6. keep deferred boundaries explicit until an implementation boundary is deliberately reopened

A synchronization unit is not a permission to mix unrelated changes.

Do not combine schema behavior changes, checker behavior changes, workflow changes, Lean formalization changes, public-claim changes, and reader-path synchronization in one unit unless they truly share the same reason, risk profile, and review path.

This staged operation is a repository-maintenance practice. It does not certify the repository, examples, schemas, generated records, operation documents, checker plans, or future adapters.

## Commit granularity policy

Prefer one commit per responsibility unit, not necessarily one commit per file.

A responsibility unit is a coherent change whose files share the same reason, risk profile, and review path.

Use one commit when multiple files are changed for the same synchronization purpose, such as:

- README and README.ja receiving the same reader-path update
- repository-governance and development-process receiving the same operation-model reference
- example-index and checker-coverage receiving the same example coverage update when the checker interpretation is unchanged
- snapshot and sync-log updates that record the same observed checkpoint

Use separate commits when changes affect different responsibility layers, such as:

- schema changes
- example additions
- checker behavior changes
- workflow changes
- Lean formalization changes
- reader-path synchronization
- observed workflow status records
- failure repair commits
- public-claim or citation changes

Use smaller commits when:

- a file is long or high-risk
- a checker failure is being repaired
- the change may alter interpretation of responsibility, authority, approval, execution, stop, repair, or excluded claims
- the update crosses from documentation into schema, checker, workflow, example, or Lean behavior

Use a larger single commit only when the files are small, the purpose is single, the risk is low, and the change remains easy to review and revert.

Commit granularity is a maintainability practice. It is not certification and does not make a repository state legally valid, safe, compliant, fair, morally resolved, production ready, connector-correct, adapter-correct, or AI-responsibility-transferring.

## Periodic operation review policy

Operation should be reviewed while operating.

Use periodic operation review when the repository has gained enough new commits, documents, examples, schemas, checker behavior, workflow results, or reader-path changes that the current operation may no longer match actual practice.

A periodic operation review should ask:

- Are commits too small, too large, or still aligned with responsibility units?
- Are reader paths still readable, or have they become too long or scattered?
- Are operation documents, snapshots, sync logs, and roadmap notes still easy to find?
- Are sync logs recording useful synchronization work, or are they becoming a second changelog?
- Are roadmap notes still temporary companions, or should their content be moved into `ROADMAP.md`?
- Are long-file updates still being handled safely?
- Are checker results still described only as bounded repository-maintenance signals?
- Are deferred items still correctly deferred, or has any boundary become stable enough to revisit?
- Are Class E positive examples, production connectors, production conversion code, runtime-event schema checks, JSON fixture checks, or Lean expansion still correctly blocked?
- Are AI-assistance boundaries and human-maintainer responsibility still explicit?

Review cadence should be practical rather than calendar-fixed.

Prefer a review when one of these triggers occurs:

- a new phase or subphase starts
- a phase snapshot is created or substantially updated
- several reader-path files are synchronized
- operation documents gain a new policy
- commit granularity feels too small or too large
- logs or roadmap notes start to multiply
- a checker failure changes future maintenance behavior
- a workflow result is recorded as observed green
- a deferred implementation boundary is being reconsidered

A periodic operation review may produce:

- a small operation-model update
- an operation-index update
- a current snapshot update
- a sync-log entry
- a roadmap note
- a short CHANGELOG milestone when the operating model changes how the repository should be read or maintained

Do not use periodic operation review to approve production readiness, connector correctness, adapter correctness, legal validity, safety, compliance, fairness, moral resolution, Lean completeness, or AI final-responsibility transfer.

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
2. read `docs/operation-index.md` when you need the operation-document map
3. read the current phase snapshot
4. read the relevant sync log or roadmap note
5. inspect the current example index and checker coverage
6. fetch the file before changing it
7. make one small change
8. fetch again after writing

Do not continue directly into production connectors, production conversion code, high-impact examples, or new formal claims unless the relevant boundary documents and examples are already stable.
