# AI-assisted work minimal example

Status: Open Construction / bounded example guide.

Example file:

- [`examples/ai-assisted-work-minimal.yaml`](../../examples/ai-assisted-work-minimal.yaml)

## Purpose

This guide introduces a small copyable example for recording AI-assisted internal work.

The example preserves:

- source reference
- human instruction
- AI draft or summary
- human review status
- approval state
- uncertainty
- evidence log
- human return point
- repair or reopening owner

## Scenario shape

```text
Human reviewer -> AI assistant -> Human reviewer
```

The AI assistant may draft, summarize, structure, or explain uncertainty.

The AI assistant does not decide, approve, execute, stop, repair, close, or become the final responsibility holder.

## First things to inspect

1. `roles.decision_owner` points to the human reviewer.
2. `roles.approval_gate` points to the human reviewer.
3. `roles.stop_authority` points to the human reviewer.
4. `ai_participation.assumes_final_responsibility` is `false`.
5. `responsibility_boundary.ai_final_responsibility_allowed` is `false`.
6. `return_points` preserves a human return point.
7. `formalization_scope.excluded_claims` keeps stronger claims out of scope.

## Boundary

This example is synthetic, local, manually readable, and non-certifying.

A checker pass, if any, should be read only as a bounded structural maintenance signal.

## Suggested next use

This file can become the first target for a reviewer-facing quickstart in RPE Issue #9.
