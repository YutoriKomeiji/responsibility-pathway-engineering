# 2026-06 Human-AI Review Workflow Example

This changelog fragment records the first small Phase 3 reference example milestone.

## Summary

`examples/human-ai-review-workflow-minimal.yaml` was added as the first small human-AI review workflow reference example.

It demonstrates a human-led review workflow where an AI summary assistant may summarize evidence and explain uncertainty, but responsibility returns to a human reviewer.

## Boundary preserved

The example preserves the following boundaries:

- the human reviewer is the decision owner
- the human reviewer is the responsibility owner
- the human reviewer is the approval gate
- the human reviewer is the stop authority
- the AI node may summarize evidence
- the AI node may explain uncertainty
- the AI node does not decide
- the AI node does not approve
- the AI node does not execute
- the AI node does not close
- the AI node does not assume final responsibility
- a human return point is preserved
- evidence records remain example-scoped
- unchecked items and not-claimed items remain visible

## Reader path updated

`docs/example-index.md` now includes the new example in the current example list, reading order, and naming convention.

## Observed bounded check

Master provided a GitHub Actions screenshot showing the bounded example checker run succeeded after this example was added.

Observed run:

- workflow run: `Check examples #9`
- branch: `main`
- observed commit: `d4e467a`
- total duration: about 9 seconds
- job: `Bounded structural example checks`
- job duration: about 6 seconds
- job result: success

This observation means the example passed the repository's bounded structural example checks for that repository state.

It does not mean the example is legally valid, safe, compliant, fair, morally resolved, institutionally certified, production ready, real-world validated, or eligible to transfer final responsibility to an AI node.

## Non-certifying interpretation

This milestone remains structural and non-certifying.

It does not claim legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, production readiness, real-world responsibility resolution, or AI final-responsibility transfer.
