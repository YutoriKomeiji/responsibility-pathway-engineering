# Assistant Pathway Maintenance Checklist

This checklist defines when an AI-assisted repository session should pause and inspect the repository operation path without waiting for the human maintainer to notice a problem.

## Purpose

Operation lessons are easy to record and easy to forget.

This checklist turns selected operation lessons into assistant-side maintenance checkpoints.

The goal is to preserve repository responsibility pathways during the work itself, not only after the human maintainer notices a recurrence.

## When to run this checklist

Run this checklist at these natural points during AI-assisted repository work:

1. before starting a new responsibility unit,
2. after a write is blocked or redirected,
3. after creating a focused note, companion note, connection note, or escape note,
4. after repeated tool-selection drift,
5. before updating a long or high-risk navigation file,
6. after adding or changing an operation rule,
7. before summarizing a multi-commit work unit,
8. before ending or handing off a heavy session,
9. when document count, reader-path length, or boundary repetition appears to be increasing.

This checklist is not a background process. It is an in-session maintenance checkpoint.

## Quick checks

Ask these questions before continuing broad work:

- What is the current responsibility unit?
- Which file is the primary artifact?
- Which file or line range grounds the next write?
- Did any error get avoided without a recovery path?
- Did any focused note get created without reconnection?
- Did a tool-discovery or read-surface drift occur?
- If a long-file update was blocked, where is the attempted path recorded?
- Is the next safe step named?
- Is the relevant improvement recorded in `docs/operation-improvement-log.md` or intentionally deferred?
- Is there a boundary statement saying what the current action does not implement, authorize, validate, certify, or prove?
- Are docs multiplying, overlapping, or repeating boundaries enough to require `docs/document-redundancy-review-plan.md` before more files are added?

## Maintenance actions

If a check fails, use the smallest safe maintenance action:

- fetch the relevant file again,
- create or update a focused connection note,
- add a temporary pointer in a sync log, snapshot, roadmap note, or gap inventory,
- add an entry to `docs/operation-improvement-log.md`,
- consult `docs/document-redundancy-review-plan.md` before adding more docs when overlap or navigation sprawl is the problem,
- update `docs/focused-note-reconnection-rule.md` only if the rule itself is missing,
- stop broad work until the recovery path is named.

## Log trigger relation

Use `docs/operation-improvement-log.md` when the maintenance check discovers:

- repeated drift,
- unclear recovery path,
- forgotten prior lesson,
- long-file update block,
- focused-note reconnection gap,
- document sprawl or boundary repetition that changes future operation behavior,
- durable rule change,
- future operation behavior change.

If the durable improvement is not yet known, do not force a log entry. Record a temporary pointer in the current focused note, sync log, snapshot, roadmap note, or gap inventory.

## Assistant-side responsibility boundary

AI assistance may notice operation drift, propose a maintenance step, draft a focused note, update an operation rule, or remind the maintainer of a missing recovery path.

AI assistance must not treat this checklist as automatic permission to implement schemas, checkers, workflows, connectors, production runtime behavior, public certification language, conformance language, legal conclusions, safety conclusions, compliance conclusions, fairness conclusions, or AI final-responsibility transfer.

The human maintainer remains responsible for deciding whether a maintenance action should be made, published, reverted, repaired, or deferred.
