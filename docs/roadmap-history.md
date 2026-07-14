# Roadmap History

This note preserves the reason why `ROADMAP.md` was compacted.

The previous `ROADMAP.md` had accumulated milestone history, workflow observations, phase notes, reader-path synchronization records, and planning details. That made it useful as a historical trace, but difficult to maintain as a current roadmap.

The current policy is:

- keep `ROADMAP.md` short and current
- keep detailed current-state records in phase snapshots and focused roadmap notes
- keep detailed synchronization records in sync logs
- keep historical cause tracing in `CHANGELOG.md` and git history
- avoid duplicating long historical logs inside the active roadmap

## Where to find older roadmap detail

Use git history for the pre-compaction roadmap content.

The last long-roadmap state before compaction was on `main` before this replacement PR.

Relevant companion notes include:

- `docs/phase-3-1-roadmap-note.md`
- `docs/phase-3-1-current-snapshot.md`
- `docs/phase-3-1-sync-log.md`
- `docs/progress-map.md`
- `docs/current-task-inventory.md`
- `docs/operation-index.md`
- `CHANGELOG.md`

## Replacement rule

When a planning file becomes too long to update safely or review clearly, prefer one of the following:

1. replace the active file with a compact current version
2. move detailed current state into a focused snapshot or companion note
3. preserve historical detail through git history, changelog milestones, or a short history note

Do not keep expanding an active roadmap until it becomes a second changelog or sync log.

## Boundary

This history note is a maintenance aid only.

It is not a certification record, external review finding, conformance record, production approval, standardization claim, legal review, safety review, compliance review, fairness review, runtime correctness proof, connector correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.
