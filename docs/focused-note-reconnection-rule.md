# Focused Note Reconnection Rule

This note defines how a focused note, companion note, connection note, or escape note should be reconnected after it is created because a long or high-risk file update was blocked, risky, or deliberately deferred.

## Purpose

Focused notes are useful when the repository needs to preserve a current state without rewriting a long navigation file, roadmap, snapshot, or changelog.

However, a focused note must not become an orphan.

This rule defines a minimal reconnection ladder.

## When this rule applies

Use this rule when a new focused note is created because:

- a long file update was blocked
- a long file update would be risky
- a broad synchronization update is not yet stable
- a current state needs to be preserved before touching a larger navigation surface
- a planning note needs a small operation bridge before implementation is reopened

## Reconnection ladder

After creating a focused note, reconnect it using the smallest safe ladder that fits the note's role.

### Level 0 - Self-contained note

The focused note must name:

- the primary artifact or plan it connects
- the broader navigation file it is related to
- the current status
- what it does not implement, authorize, certify, validate, or prove

Level 0 is required for every focused note.

### Level 1 - Local pair connection

Connect the focused note to the closest already-relevant document when that document is small or safe to update.

Examples:

- a checker plan connects to `docs/checker-coverage.md`
- an example note connects to `docs/example-index.md`
- an operation note connects to a focused operation connection note
- a publication note connects to the nearest Zenn readiness connection note

Level 1 should usually be done before touching broad navigation files.

### Level 2 - Navigation pointer

Add a short pointer from the relevant navigation surface when the edit is small and safe.

Possible targets include:

- `docs/operation-index.md`
- the current phase snapshot
- the relevant sync log
- the relevant roadmap note
- `docs/repository-pathway-gap-inventory.md` when the note is intentionally not yet in the primary reader path

If a navigation pointer update is blocked, do not retry with a larger replacement. Preserve the attempted connection in a focused connection note and treat the navigation pointer as deferred.

### Level 3 - Broad reconnection

Only after the focused note's role is stable, consider broad reader-path updates such as:

- `BEACON.md`
- `README.md`
- `README.ja.md`
- `ROADMAP.md`
- `CHANGELOG.md`

Use broad reconnection only when stale broad navigation would mislead maintainers, reviewers, or public readers.

## Orphan prevention checklist

A focused note is not considered safely reconnected unless at least one of the following is true:

- it is linked from the primary artifact it explains
- it is linked from the closest coverage, example, operation, or readiness document
- it is linked from a current snapshot, sync log, roadmap note, or operation index
- it is listed in a gap inventory as intentionally not yet connected

If none of these is true, the note is an orphan and should be connected or explicitly recorded as a gap.

## Deferred navigation pointer

When a broad or long navigation update is blocked or deferred, record:

- the attempted target
- why the direct update was not completed
- where the focused note is temporarily connected
- what the next safe reconnection step is

This record may live in the focused note itself, a connection note, a sync log, or the repository pathway gap inventory.

## Boundary

This is an operation rule only.

It does not authorize implementation, schema expansion, checker expansion, workflow expansion, production runtime integration, connector work, public certification language, conformance language, legal review, safety review, compliance review, fairness review, or AI final-responsibility transfer.
