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

## Operation documents

| Document | Use when |
| --- | --- |
| `docs/repository-operation-model.md` | You need the current repository-wide operating model, staged update operation, commit granularity policy, long-file update policy, workflow observation policy, or restart rule. |
| `docs/development-process.md` | You need the standard work cycle for concept, definition, specification, example, checker, or formalization work. |
| `docs/repository-governance.md` | You need the governance principles that preserve return paths from claims to definitions, specifications, formalization, and assumptions. |
| `BEACON.md` | You need the current reconnection point, read-first order, current focus, and restart point. |
| `ROADMAP.md` | You need phase-level direction, next low-risk work, phase rules, or deferred work. |
| `CHANGELOG.md` | You need durable conceptual milestones rather than detailed per-commit history. |

## Snapshot documents

Snapshots record current restart positions for phases or subphases.

| Document | Current role |
| --- | --- |
| `docs/phase-2-current-snapshot.md` | Current Phase 2 Lean restart point and scoped formalization status. |
| `docs/phase-2-5-current-snapshot.md` | Current Phase 2.5 enterprise and record-review restart point. |
| `docs/phase-3-1-current-snapshot.md` | Current Phase 3.1 adapter boundary and runtime-event bridge restart point. |

Use snapshots when a change spans multiple documents, when a long-file update becomes risky, or when the next maintainer needs a compact restart point.

## Sync logs and roadmap notes

Sync logs record multi-commit synchronization work.

Roadmap notes are short companions to `ROADMAP.md` when direct roadmap edits would be large or risky.

| Document | Current role |
| --- | --- |
| `docs/phase-3-1-sync-log.md` | Records staged synchronization work for Phase 3.1 Adapter Boundary and Runtime Event Bridge. |
| `docs/phase-3-1-roadmap-note.md` | Records the short roadmap companion for Phase 3.1. |

Use sync logs when reader-path updates, coverage updates, or long-file deferrals span multiple commits.

Use roadmap notes when the roadmap position should be recorded before changing long roadmap sections.

## Checker and example navigation

| Document | Use when |
| --- | --- |
| `docs/example-index.md` | You need to know how examples should be read, what each example is for, and which examples remain future work. |
| `docs/checker-coverage.md` | You need to know what current checkers actually check, what they do not check, and what is only planned future checker work. |
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
