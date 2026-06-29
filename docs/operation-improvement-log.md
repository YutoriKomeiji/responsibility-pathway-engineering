# Operation Improvement Log

This log records repository-operation mistakes, recoveries, and durable improvements that should affect future maintenance behavior.

The purpose is not to blame a person or AI assistant. The purpose is to prevent recoverable operation problems from becoming recurring hidden patterns.

## Use this log when

Add an entry when an operation problem meets at least one of these conditions:

- the same tool-selection drift or operation mistake has repeated
- an error was avoided but the recovery path was unclear
- a long-file update was blocked, risky, or deferred
- a focused note or escape note was created and needs reconnection tracking
- a repository rule was created or updated because of an observed failure
- the fix changes how future maintainers or AI-assisted sessions should operate

Do not add an entry for every minor typo, harmless edit, or already-covered checker failure.

## Semi-automatic trigger rule

During AI-assisted repository maintenance, pause and consider an entry here when any of these phrases or situations appear in the work:

- "blocked"
- "drift"
- "recurrence"
- "again"
- "forgot"
- "unclear recovery path"
- "safe workaround"
- "escape note"
- "focused note"
- "long-file update"
- "tool discovery"
- "not sure where this was recorded"
- a safety check blocks an update
- a direct file update is abandoned and replaced with a different route
- an error is avoided but the future restart path is not obvious
- the maintainer notices that a past lesson was recorded but not naturally applied

This is a trigger to check the log, not an automatic requirement to write.

## Assistant-side maintenance trigger

`docs/assistant-pathway-maintenance-checklist.md` is the assistant-side checkpoint for detecting operation-path problems before the human maintainer notices them.

When that checklist finds repeated drift, unclear recovery path, forgotten prior lesson, long-file update block, focused-note reconnection gap, durable rule change, or future operation behavior change, use this log as the next place to decide whether a durable entry is needed.

The checklist should be run at natural responsibility-pathway points such as before a new responsibility unit, after blocked or redirected writes, after focused-note creation, after repeated tool-selection drift, before long-file updates, after operation-rule changes, before multi-commit summaries, and before heavy-session handoff.

This does not make logging automatic. It makes log consideration assistant-initiated rather than dependent on the human maintainer noticing the issue.

## Write timing rule

Write an entry at the earliest safe point after one of these happens:

1. the immediate recovery has succeeded,
2. the durable improvement file or rule is known,
3. the next check can be named, and
4. the entry can be written without interrupting a higher-risk repair.

If these are not yet true, record a temporary pointer in the focused note, sync log, snapshot, roadmap note, or gap inventory instead.

Do not wait until the same problem recurs if the current fix changes future operation behavior.

## Do not write when

Do not add an entry when:

- the event is a one-off typo or harmless wording repair
- the event is already fully covered by a checker failure note, workflow observation, or existing operation log entry
- the fix does not change future operation behavior
- the entry would be speculative before the actual recovery path is known
- writing the log would interrupt an urgent repair that still lacks a safe current state

## Entry format

Use short entries.

Recommended fields:

- Timestamp
- Trigger
- Observed problem
- Immediate recovery
- Durable improvement
- Improvement file(s)
- Next check
- Boundary

## Entries

### 2026-06-30 08:09 JST - Focused-note reconnection and recovery-path rule

- Trigger: A long `docs/operation-index.md` update was blocked after a focused connection note had been created to preserve the intended reader-path relation.
- Observed problem: The repository had rules for avoiding risky long-file updates, but the rule for reconnecting the escape or focused note back into the reader path was shallow.
- Immediate recovery: Created `docs/issue-body-warning-checker-operation-connection.md` to preserve the attempted connection between `docs/issue-body-warning-checker-plan.md`, `docs/checker-coverage.md`, and `docs/operation-index.md` without retrying a larger replacement.
- Durable improvement: Added `docs/focused-note-reconnection-rule.md` with a reconnection ladder, orphan-prevention checklist, deferred-navigation-pointer rule, and recovery-path requirement.
- Improvement file(s): `docs/focused-note-reconnection-rule.md`; `docs/issue-body-warning-checker-operation-connection.md`.
- Next check: Before creating or relying on any future focused note, check whether it has Level 0 self-containment, Level 1 local-pair connection, and either a Level 2 navigation pointer or a recorded deferred pointer.
- Boundary: This entry records repository-operation improvement only. It does not implement a checker, add a workflow, authorize live issue access, certify repository correctness, prove safety/compliance/fairness, or transfer final responsibility to AI.

### 2026-06-30 08:09 JST - Tool-discovery recurrence remains tolerable but should not ground writes

- Trigger: Tool-discovery calls recurred during known GitHub file work even though direct GitHub file tools were already available.
- Observed problem: The recurrence was harmless in content terms, but repeated discovery calls can obscure the responsibility path if they become the basis for writes or hide which fetched file, blob SHA, or line range grounded a change.
- Immediate recovery: Treat the recurrence as read-only operation drift when no repository content was changed, the discovery result was not used as write grounding, and the next operation returned to direct GitHub file read/write.
- Durable improvement: Keep using `docs/operation-tool-selection-guard.md` as the primary tool-selection rule and apply the recovery-path requirement in `docs/focused-note-reconnection-rule.md` when an error-avoidance step would otherwise lack a recovery path.
- Improvement file(s): `docs/operation-tool-selection-guard.md`; `docs/focused-note-reconnection-rule.md`.
- Next check: If the recurrence repeats inside the same responsibility unit, record whether it remained read-only and whether the write was grounded in a direct file fetch and current blob SHA.
- Boundary: This entry does not make tool discovery a preferred path. Direct GitHub file tools remain the preferred path for known repository files.
