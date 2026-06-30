# Document Redundancy Review Plan

This note records a low-risk plan for reviewing possible overlap, duplication, and navigation sprawl across repository documents.

## Purpose

The repository now has many documents under `docs/`.

This is useful for preserving small responsibility units, but it also creates a risk that:

- similar boundaries are repeated in multiple files
- focused notes become hard to find
- operation rules overlap without clear priority
- navigation indexes grow too large
- old restart paths remain after newer focused notes exist
- broad files and focused notes duplicate each other

This plan defines how to review that risk without immediately merging, deleting, or rewriting documents.

## Review status

This is a planning note only.

It does not merge files.

It does not delete files.

It does not rename files.

It does not change checker, schema, workflow, runtime, connector, Lean, README, BEACON, ROADMAP, or CHANGELOG behavior.

## Candidate review groups

Initial review should group documents by role rather than by filename alone.

Possible groups:

- operation rules and guards
- operation logs and improvement logs
- focused connection notes
- checker coverage and checker plans
- example indexes and example notes
- phase snapshots and sync logs
- roadmap notes and deferred-work notes
- public-entry and publication-readiness notes
- standardization and external-review notes

## Findings notes

Current findings notes:

- `docs/document-redundancy-review-findings-operation-rules.md` records first low-risk findings for the operation-rules and operation-guards document group.
- `docs/document-redundancy-review-findings-checker-plans.md` records low-risk findings for the checker coverage and checker-plan document group.
- `docs/document-redundancy-review-findings-operation-logs.md` records low-risk findings for the operation-log, improvement-log, sync-log, and workflow-observation document group.

A findings note should not be treated as a merge, deletion, rename, archive, or broad navigation rewrite. It records classification and next safe review steps only.

## Review questions

For each group, ask:

- Which document is the authoritative current reader path?
- Which document is only historical, transitional, or local to one synchronization unit?
- Are two files repeating the same boundary statement without adding a distinct role?
- Is a focused note safely reconnected or still orphan-like?
- Is a long navigation file carrying details that should live in a focused note or sync log?
- Is a focused note carrying broad navigation content that should be a short pointer elsewhere?
- Does any document claim current behavior when it only records planned future work?
- Does any entry need to move from a temporary note into a current snapshot, sync log, roadmap note, or operation index?

## Safe review sequence

Use a staged review sequence:

1. Search for candidate overlap terms such as `blocked`, `drift`, `reconnection`, `focused note`, `warning-only`, `workflow`, `not current checker behavior`, and `AI final-responsibility transfer`.
2. Read only the candidate group being reviewed.
3. Classify each document as authoritative, companion, historical, transitional, or gap-tracking.
4. Record findings in a review note before changing broad navigation files.
5. Prefer short pointers over full content duplication.
6. Do not delete or merge files until a current replacement path is clear.
7. If a duplicate boundary is harmless and helps local readability, leave it unless it misdirects readers.

## Possible outputs

A redundancy review may produce:

- a short findings note
- an operation-index pointer
- a repository-pathway-gap-inventory entry
- a current snapshot update
- a sync-log entry
- a focused-note reconnection update
- a small operation-model rule update

A redundancy review should not start by rewriting `README.md`, `BEACON.md`, `ROADMAP.md`, `CHANGELOG.md`, or a large index file unless stale broad navigation would actively mislead readers.

## Boundary

This is a repository-maintenance review plan only.

It is not a content deletion plan, consolidation mandate, certification process, conformance process, legal review, safety review, compliance review, fairness review, production approval, connector correctness proof, adapter correctness proof, runtime correctness proof, Lean completeness proof, or AI final-responsibility transfer mechanism.
