# Phase 3.1 Snapshot Reduction Follow-up

This note records a follow-up created after the Phase 3.1 current snapshot was updated to include AI Judgment Node task-control boundary material.

The update kept the snapshot coherent, but it also confirms that `docs/phase-3-1-current-snapshot.md` is now carrying a large amount of detailed state.

Future maintenance should consider reducing the snapshot by moving narrow responsibility-unit details into focused connection notes and sync notes.

This note is a maintenance follow-up only. It is not a certification record, production approval, connector correctness proof, runtime correctness proof, legal review, safety review, compliance review, fairness review, Lean completeness proof, conformance evidence, or AI final-responsibility transfer mechanism.

## Reason

The AI Judgment Node synchronization added useful boundaries:

- AI local judgment can be pathway-relevant
- evaluator separation is not verification
- loop-like task control and goal-like stop conditions remain bounded task-control concepts
- future schema, checker, workflow, connector, runtime, conformance, or Lean work remains deferred

However, the current snapshot is a long-file restart artifact. Broad snapshot rewrites are harder to audit than focused connection notes.

## Recommended future action

When the next low-risk reader-path pass occurs, consider one of the following:

1. Keep the snapshot as the detailed state record, but avoid adding more narrow subsections.
2. Move narrow AI Judgment Node details primarily into:
   - `docs/ai-judgment-node-task-control.md`
   - `docs/phase-3-1-ai-judgment-node-connection.md`
   - `docs/phase-3-1-ai-judgment-node-sync-note.md`
3. Leave only a short pointer in the snapshot.
4. Keep `BEACON.md` short and avoid turning it into a second snapshot.

## Boundary

This follow-up does not require immediate correction.

It records a maintainability concern and a safe future cleanup path.

Do not use this note to start schema, checker, workflow, connector, runtime, conformance, or Lean expansion.