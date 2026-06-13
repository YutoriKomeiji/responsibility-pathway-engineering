# Development Process

Responsibility Pathway Engineering is developed by operating it.

The project should not assume that its process is complete in advance. Operational lessons are part of the architecture when they are observed, understood, and recorded.

For the current repository-wide operation model, see `docs/repository-operation-model.md`.

That document defines staged update operation, snapshot roles, sync-log roles, roadmap-note roles, workflow observation policy, checker interpretation policy, long-file update policy, log organization policy, non-certifying operation boundaries, and restart rules.

## Process Loop

Build the project.
Observe the operation.
Improve the operation.
Record the improvement.

## Standard Work Cycle

1. Identify an observation or need.
2. Discuss and sketch the concept.
3. Add or update the primary artifact.
4. Fetch the changed artifact after writing.
5. Observe or run bounded checks when applicable.
6. Fix confirmed structural failures with the smallest possible change.
7. Add or update definitions, specifications, and examples only after the scope is clear.
8. Add Lean or other formalization only after the scope and assumptions are stable.
9. Use snapshots when a change spans multiple documents.
10. Use sync logs when reader-path or coverage synchronization spans multiple commits.
11. Use roadmap notes when `ROADMAP.md` would require a large or risky update.
12. Update BEACON, ROADMAP, or CHANGELOG only at meaningful milestones.

## Commit Discipline

- Prefer small commits.
- Prefer one concept or one synchronization purpose per commit.
- Fetch before changing an existing file.
- Fetch after writing a changed file.
- Do not mix unrelated documentation, specification, checker, example, and formalization changes.
- Do not record a workflow as green before it has been observed.
- Do not treat checker success as certification.
- Do not treat a draft theorem as a public guarantee.
- Do not treat an operational workaround as a stable rule until it has been observed, recorded, and connected to the operation model if it changes future work.

## Failure Handling

When a failure occurs:

1. Stop expanding the change.
2. Record what was observed.
3. Identify what is known and unknown.
4. Repair only the confirmed affected area.
5. Fetch the repaired file after writing.
6. Observe or rerun the bounded check when applicable.
7. Convert the lesson into documentation if it changes future operation.
8. Preserve the current state in a snapshot, sync log, or roadmap note if a long-file update becomes risky.

## Non-certifying process boundary

The development process preserves continuity, maintainability, and returnability.

It does not certify legal validity, safety, compliance, fairness, moral resolution, institutional approval, production readiness, connector correctness, adapter correctness, Lean theorem completeness, or AI final-responsibility transfer.
