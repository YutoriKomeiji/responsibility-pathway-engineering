# Phase 3.1 AI Judgment Node Connection

This focused connection note links Phase 3.1 Adapter Boundary and Runtime Event Bridge work to `docs/ai-judgment-node-task-control.md` without rewriting the full Phase 3.1 current snapshot.

It is a reader-path note only. It is not a schema change, checker change, workflow change, runtime connector, production runtime, conformance model, legal decision system, safety certification, compliance certification, fairness certification, Lean formalization, or AI final-responsibility transfer mechanism.

## Connection reason

Phase 3.1 already records runtime observations, adapter boundaries, minimal synthetic runtime fixtures, bounded runtime-event checker behavior, workflow observations, and future event-to-pathway relation checker planning.

The AI Judgment Node note adds a boundary needed for task-control discussions: an AI system may act as a local judgment node inside a Responsibility Pathway even when a human or institution remains the final responsible party.

This matters for loop-like or goal-like AI task-control mechanisms where an AI system may judge whether to continue, stop, retry, escalate, re-observe, select evidence, or choose a next action.

## Phase 3.1 interpretation

For Phase 3.1, an AI local judgment should be treated as pathway-relevant when it affects:

- continuation or stop behavior
- retry or re-observation timing
- escalation or human-return behavior
- evidence selection
- action selection
- downstream execution allowance

This does not imply that the AI node holds final responsibility.

It also does not imply that evaluator separation establishes verification, semantic correctness, safety, legality, compliance, fairness, connector correctness, runtime correctness, conformance, or production readiness.

## Boundary for future work

Future runtime-event, adapter-boundary, or relation-checker work may use the AI Judgment Node concept only after a separate design note or restart-condition review.

Any future record shape should distinguish at least:

- visible evidence
- missing or unobserved evidence
- judging node
- selected option or stop/continue result
- downstream action or no-action status
- human or institutional return point
- audit or repair path

This note does not authorize implementation of autonomous task control, production connectors, automatic approval, automatic execution, schema expansion, checker expansion, workflow expansion, conformance checks, or Lean expansion.

## Reader path

When AI local judgment, task-control loops, stop conditions, or evaluator separation matter, read:

1. `docs/ai-judgment-node-task-control.md`
2. `docs/ai-agent-operation-patterns.md`
3. `docs/phase-3-1-current-snapshot.md`
4. `docs/current-task-inventory.md`
5. `docs/responsibility-pathway-availability.md` when the pathway is narrowed, incomplete, noisy, or temporarily broken

## Current status

This connection note preserves the concept boundary for Phase 3.1 review.

It does not change Phase 3.1 implementation scope.