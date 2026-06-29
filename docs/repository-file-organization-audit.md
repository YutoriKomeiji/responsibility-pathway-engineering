# Repository File Organization Audit

This note tracks possible file sprawl, role overlap, and cleanup candidates in the Responsibility Pathway Engineering repository.

It is an organization audit only. It does not delete files, deprecate files, rewrite history, certify completeness, approve publication, authorize implementation, or change schema, checker, workflow, runtime, connector, conformance, Lean, legal, safety, compliance, fairness, social-acceptance, or production boundaries.

## Purpose

Use this audit before deleting, merging, renaming, or deprecating repository documents.

The repository intentionally uses focused notes to avoid risky long-file rewrites. Over time, that can create too many nearby notes. This audit keeps cleanup review explicit without losing restart paths.

## Classification

When reviewing a file, classify it as one of:

- active entrance
- active focused note
- current snapshot or sync record
- historical reference
- duplicate or overlap candidate
- merge candidate
- deprecation candidate
- delete candidate
- unknown until inspected

Deletion should be the last option.

Prefer preserving a short redirect or deprecation note when a file has been used as a reader path, restart path, sync record, or public-facing reference.

## Initial cleanup questions

Ask these before cleanup:

- Does another document now cover the same role more clearly?
- Is the file still linked from operation index, task inventory, roadmap, progress map, README, BEACON, or a focused reader path?
- Is the file a historical synchronization record that should remain archived?
- Would removing it break restartability or reader trust?
- Can the file be merged into a broader index without losing boundary language?
- Can the file remain but be marked as historical reference?

## Current high-risk overlap zones

Potential overlap zones to inspect later:

- Phase 3.1 current snapshot, sync log, roadmap notes, and focused sync notes
- AI Judgment Node connection notes and sync notes
- progress-map connection notes and progress map
- Zenn readiness plan, readiness connection, Level 2 readiness note, cadence note, and article-scope notes
- external-review readiness checklist and external-review package note
- social-connection review navigation, social exception cases, approval-transfer alignment, and gap inventory
- runtime-event workflow status, workflow observation notes, and checker connection notes

These are not delete decisions. They are inspection zones.

## Safe cleanup order

1. Inventory likely overlaps.
2. Confirm whether each file is active, historical, or deferred.
3. Preserve alternate routes before removing or deprecating a route.
4. Prefer small deprecation notes over deletion for public or restart-facing files.
5. Update operation index, current task inventory, progress map, roadmap, and gap inventory after any cleanup.

## Current no-delete rule

Do not delete files during active Level 2 publication readiness work unless the file is clearly accidental, unreferenced, and not part of a restart or reader path.

Until Level 2 is stable, prefer classification and connection over deletion.

## Next safe action

Connect this audit from the operation or task navigation path when file organization becomes part of the active maintenance work.
