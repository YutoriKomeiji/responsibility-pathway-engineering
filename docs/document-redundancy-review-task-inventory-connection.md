# Document Redundancy Review Task Inventory Connection

This note records a low-risk connection between the current task inventory and the document-redundancy review post-initial-pass route.

It exists because `docs/current-task-inventory.md` is a long planning file, and a direct broad rewrite should be avoided unless necessary.

## Connection

When choosing the next task after the initial document-redundancy findings pass, use this route:

1. `docs/current-task-inventory.md`
2. `docs/document-redundancy-review-plan.md`
3. `docs/document-redundancy-review-initial-pass-sync-note.md`
4. `docs/document-redundancy-review-follow-up-selection.md`
5. the relevant focused findings note for the selected group

## Current state

The initial document-redundancy findings pass is complete for all currently listed candidate review groups.

A follow-up selection note exists to keep the next step as selection from findings notes, not automatic consolidation.

The operation index already contains pointers to:

- `docs/document-redundancy-review-initial-pass-sync-note.md`
- `docs/document-redundancy-review-follow-up-selection.md`
- the nine focused findings notes

## Task-inventory interpretation

For task selection purposes, the document-redundancy route should be treated as a P0/P1 maintenance path:

- P0 when restartability or boundary clarity is at risk
- P1 when selecting one low-risk pointer, status clarification, boundary clarification, or index-line improvement

It should not be treated as permission for automatic merge, deletion, rename, broad rewrite, certification, external-review completion, standardization, conformance, checker expansion, schema expansion, workflow expansion, runtime expansion, connector expansion, Lean expansion, or public maturity claims.

## Why this note exists instead of a broad inventory rewrite

`docs/current-task-inventory.md` is a long cross-phase planning file.

A full rewrite just to add one document-redundancy pointer would be higher-risk than a focused connection note.

This note preserves the connection without forcing a broad inventory replacement.

## Possible later follow-up

If a future maintainer is already editing `docs/current-task-inventory.md` for another small, reviewable reason, they may add a short pointer to:

- `docs/document-redundancy-review-follow-up-selection.md`
- this connection note

That future update should remain a small responsibility unit and should not rewrite unrelated task-inventory sections.

## Boundary

This connection note does not update `docs/current-task-inventory.md` directly.

It does not merge, delete, rename, archive, certify, approve, standardize, validate, externally review, or change any checker, schema, workflow, runtime, connector, Lean, README, BEACON, ROADMAP, CHANGELOG, or public claim.
