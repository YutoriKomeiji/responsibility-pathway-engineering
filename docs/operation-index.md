# Operation Document Index

This index explains which operation-related document to read for each maintenance situation.

It is a navigation aid only. It is not a certification process, legal review process, safety review process, compliance process, production approval process, connector correctness proof, adapter correctness proof, or AI final-responsibility transfer mechanism.

## Primary reconnection path

Use this path when restarting work after a pause or when another maintainer, reviewer, or AI-assisted session needs to understand the current repository state.

1. `BEACON.md`
2. `docs/repository-operation-model.md`
3. the current phase snapshot
4. the relevant sync log or roadmap note
5. `docs/example-index.md`
6. `docs/checker-coverage.md`

`CHANGELOG.md` is not part of the primary construction-time reconnection path. Use it mainly for archival, investigative, historical, or retrospective milestone review.

## Usage phases

Use documents according to the phase of work.

| Work phase | Prefer reading | Use `CHANGELOG.md` when |
| --- | --- | --- |
| Active construction | `BEACON.md`, current snapshot, operation index, sync log, roadmap note, checker coverage, example index, primary artifact | a prior milestone or boundary change must be investigated |
| Restart or handoff | `BEACON.md`, current snapshot, operation index, sync log, roadmap note | the restart depends on historical cause tracing |
| Checker or example interpretation | `docs/checker-coverage.md`, `docs/example-index.md`, relevant schemas or examples | checking when a rule or coverage boundary changed |
| Phase planning | `ROADMAP.md`, roadmap note, current snapshot, operation index | confirming a past phase milestone |
| Audit, error investigation, or retrospective explanation | `CHANGELOG.md`, sync logs, snapshots, relevant commits and artifacts | this is the intended primary use |

If the purpose does not match the document, change the reading path or update path before continuing.

## BEACON and snapshot roles

`BEACON.md` and current snapshots are complementary but separate.

Use `BEACON.md` as the reconnection entrance:

- current focus
- read-first order
- restart pointer
- short boundary reminders
- compact continuity signal across sessions

Use the current phase snapshot as the detailed current-state record:

- current artifacts
- current synchronization state
- observed bounded checks
- detailed deferred boundaries
- next low-risk work
- stop conditions
- restart details

Do not let `BEACON.md` become a full snapshot or a second changelog.

Do not let a current snapshot replace the short reconnection role of `BEACON.md`.

When BEACON grows too large, preserve detailed state in the relevant snapshot, sync log, roadmap note, checker coverage, or example index, then keep BEACON focused on reconnection.

## Operation documents

| Document | Use when |
| --- | --- |
| `docs/repository-operation-model.md` | You need the current repository-wide operating model, document purpose and usage phase policy, staged update operation, synchronization unit operation, session load and handoff policy, commit granularity policy, periodic operation review policy, long-file update policy, workflow observation policy, sync-log and roadmap-note separation policy, or restart rule. |
| `docs/development-process.md` | You need the standard work cycle for concept, definition, specification, example, checker, or formalization work. |
| `docs/repository-governance.md` | You need the governance principles that preserve return paths from claims to definitions, specifications, formalization, and assumptions. |
| `BEACON.md` | You need the current reconnection entrance, compact read-first order, current focus, and restart pointer. |
| `ROADMAP.md` | You need phase-level direction, next low-risk work, phase rules, or deferred work. |
| `CHANGELOG.md` | You need archival milestones, serious error investigation support, historical cause tracing, or retrospective explanation of when and why a boundary or policy changed. |

## Periodic operation review

Use `docs/repository-operation-model.md` when operation itself needs review.

A periodic operation review is useful when:

- commit granularity feels too small or too large
- reader paths become long or scattered
- operation documents, snapshots, sync logs, or roadmap notes are multiplying
- BEACON starts carrying detailed snapshot history or changelog-like content
- sync logs and roadmap notes start duplicating each other
- active construction starts relying on `CHANGELOG.md` as a primary restart path
- a workflow result is recorded as observed green
- a checker failure changes future maintenance behavior
- a deferred implementation boundary is being reconsidered
- session load is becoming heavy or a session handoff needs a durable restart path
- Class E positive examples, production connectors, production conversion code, runtime-event schema checks, JSON fixture checks, or Lean expansion may need to be revisited

A periodic operation review may produce an operation-model update, operation-index update, snapshot update, sync-log entry, roadmap note, BEACON update, or short CHANGELOG milestone.

It must not be used as production approval, connector correctness proof, adapter correctness proof, legal review, safety review, compliance review, fairness review, Lean completeness proof, or AI final-responsibility transfer.

## Snapshot documents

Snapshots record current restart positions for phases or subphases.

| Document | Current role |
| --- | --- |
| `docs/phase-2-current-snapshot.md` | Current Phase 2 Lean restart point and scoped formalization status. |
| `docs/phase-2-5-current-snapshot.md` | Current Phase 2.5 enterprise and record-review restart point. |
| `docs/phase-3-1-current-snapshot.md` | Current Phase 3.1 adapter boundary, runtime-event bridge, runtime-event checking plan, repository operation, checker coverage, and example-index restart point. |

Use snapshots when a change spans multiple documents, when a long-file update becomes risky, when session handoff needs a durable restart path, when BEACON would otherwise need to carry detailed current-state history, or when the next maintainer needs a compact restart point.

## Sync logs and roadmap notes

Sync logs and roadmap notes are complementary but separate.

| Document | Current role |
| --- | --- |
| `docs/phase-3-1-sync-log.md` | Detailed synchronization record for multi-commit Phase 3.1 reader-path, coverage, checker-interpretation, and boundary synchronization. |
| `docs/phase-3-1-roadmap-note.md` | Short current-planning companion for Phase 3.1 near-term roadmap position, next low-risk work, phase rules, and stop conditions. |

Use sync logs to understand what changed across several commits, what was synchronized, what checker status or interpretation was current, and what work remained deferred after a synchronization unit.

Use roadmap notes to understand what should happen next, which phase rules matter now, what should remain deferred, and how to avoid changing a long `ROADMAP.md` section too early.

Do not use a roadmap note as a second changelog.

Do not use a sync log as a phase plan.

## Checker and example navigation

| Document | Use when |
| --- | --- |
| `docs/example-index.md` | You need to know how examples should be read, what each example is for, and which examples remain future work. |
| `docs/checker-coverage.md` | You need to know what current checkers actually check, what they do not check, and what is only planned future checker work. |
| `docs/runtime-event-checking-plan.md` | You need to know when runtime-event schema checking, JSON fixture checking, or future runtime-event checker work may be safely considered. |
| `docs/validator-boundary.md` | You need the non-certifying boundary for lightweight validation tools. |
| `docs/schema-cross-reference.md` | You need to understand how schema files relate to each other. |

## When to create a new operation document

Create a new operation document only when the repository gains a new repeatable maintenance pattern.

Prefer updating an existing operation document when the new rule is just a refinement of an existing policy.

Create a snapshot when the repository needs a restart point.

Create a sync log when several commits together form one synchronization operation.

Create a roadmap note when a roadmap update needs a short companion before a larger roadmap edit.

Do not create a single global log that absorbs all details.

## Log organization note

For the current repository state, phase-specific logs may remain directly under `docs/`.

A future `docs/logs/` directory may be introduced only when there are enough logs to justify moving them and the link updates are small and deliberate.

Until then, avoid moving existing logs.

## Non-certifying operation boundary

Operation documents preserve maintainability, traceability, and returnability.

They do not certify examples, schemas, checkers, generated records, adapters, connectors, workflows, Lean files, governance decisions, public claims, or repository states.

The human author or maintainer remains responsible for deciding whether a change should be made, published, relied upon, reverted, repaired, or deferred.
