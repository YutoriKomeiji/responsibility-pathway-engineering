# Document Redundancy Review Follow-up Selection

This note selects the next safe direction after the initial document-redundancy findings pass.

It follows:

- `docs/document-redundancy-review-plan.md`
- `docs/document-redundancy-review-initial-pass-sync-note.md`
- the nine focused findings notes listed by the initial pass

## Current state

The initial findings pass is complete for all currently listed candidate review groups.

The first pass created reviewable classifications and operation-index pointers.

The next step is selection, not automatic consolidation.

## Selection rule

Choose a follow-up only when it satisfies all of these conditions:

1. It improves restartability, reader-path clarity, or boundary clarity.
2. It can be reviewed as one small responsibility unit.
3. It does not require broad rewrites of `README.md`, `README.ja.md`, `BEACON.md`, `ROADMAP.md`, or `CHANGELOG.md`.
4. It does not merge, delete, rename, or archive focused notes before a replacement path is clear.
5. It does not expand checker, schema, workflow, runtime, connector, Lean, conformance, external-review, certification, or standardization claims.
6. It can be verified by a small fetch after the change.

## Candidate follow-up classes

| Follow-up class | Use when | Risk level |
| --- | --- | --- |
| short pointer | a focused note exists but is hard to find | low |
| status clarification | a note may be read as current when it is historical, transitional, or planning-only | low |
| boundary clarification | a note could be read as certification, approval, standardization, or implementation | low |
| index-line improvement | an index entry exists but the route is unclear or overbroad | low |
| source-document rewrite | a broad document actively misleads readers | higher; defer unless necessary |
| merge / delete / rename | a replacement path is already clear and stable | deferred |

## Recommended next follow-up

Recommended next follow-up: choose one low-risk pointer or status clarification from the findings notes, rather than editing a broad source document.

The safest first target is an index-line or pointer-level improvement because it improves reader paths without changing project claims.

Suggested first selection:

- review `docs/operation-index.md` and the newly added redundancy-review findings pointers
- check whether `docs/document-redundancy-review-initial-pass-sync-note.md` needs a short pointer from `docs/operation-index.md`
- if yes, add one operation-index row for the initial-pass sync note

Rationale:

- the sync note is now the best restart point after the initial pass
- it helps future sessions avoid automatic consolidation
- it does not require changing README, BEACON, ROADMAP, CHANGELOG, checker behavior, schemas, workflows, runtime files, connectors, Lean files, or public claims

## First selected follow-up status

Status: completed with a recovery path.

Completed follow-up work:

- `docs/operation-index.md` now points to `docs/document-redundancy-review-initial-pass-sync-note.md`.
- `docs/operation-index.md` now points to this selection note.
- `docs/document-redundancy-review-task-inventory-connection.md` was added as a focused connection note after a broad direct update to `docs/current-task-inventory.md` was unnecessary or unsafe.
- `docs/operation-index.md` now points to `docs/document-redundancy-review-task-inventory-connection.md`.

Recovery interpretation:

The intended task-inventory connection was preserved through a focused connection note instead of a broad inventory rewrite.

This keeps the post-initial-pass route reachable while preserving the rule that broad files should not be rewritten unless a reader-path failure requires it.

Next follow-up state:

- choose one additional low-risk follow-up from the nine findings notes
- prefer pointer, status clarification, boundary clarification, or index-line improvement
- do not start automatic consolidation

## Explicit non-selection

Do not select these as the immediate next follow-up:

- merging the nine findings notes
- deleting old focused notes
- renaming document groups
- rewriting README or README.ja
- expanding BEACON into a detailed redundancy-review summary
- adding standardization, certification, conformance, external-review, or public maturity claims
- implementing checker, schema, workflow, runtime, connector, or Lean changes

## Restart pointer

When this selection note is read later:

1. confirm the initial-pass sync note is still current
2. confirm `docs/operation-index.md` has a pointer to the sync note if needed
3. choose only one low-risk follow-up at a time
4. fetch after the change
5. stop before broad rewrites unless a specific reader-path failure is found

## Boundary

This note selects a safe next direction only.

It does not execute broad consolidation, merge files, delete files, rename files, certify the repository, complete external review, approve public maturity claims, standardize RPE, or change any checker, schema, workflow, runtime, connector, Lean, README, BEACON, ROADMAP, or CHANGELOG behavior.
