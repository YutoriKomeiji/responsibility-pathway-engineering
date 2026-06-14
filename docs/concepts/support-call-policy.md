# Support-Call Policy Concept Mapping

This note maps the support-call policy idea to existing Responsibility Pathway Engineering concepts.

It is a concept mapping note only. It does not introduce schema fields, checker rules, examples, runtime connectors, workflows, or Lean theorems.

## Purpose

A support-call policy asks when an AI agent should continue alone and when it should seek support.

Support may include:

- human review
- user clarification
- expert input
- tool execution
- database query
- web search
- additional evidence
- stop-and-await behavior

In RPE, this question is not only an optimization problem. It is also a responsibility-pathway question: where does judgment return when the agent should not continue alone?

## Existing RPE concepts

### Decision Owner

The Decision Owner remains responsible for deciding whether the pathway can proceed, defer, stop, return, or repair.

A support-call policy may recommend that support be requested, but it does not replace the Decision Owner.

### Human Return Point

A support call may route the pathway back to a human or institution when the agent lacks context, authority, confidence, or permission to continue.

A Human Return Point records where that return is possible.

### Approval Gate

Some actions require approval before execution.

A support-call policy may identify that an Approval Gate should be activated, but it does not itself approve the action.

### Stop Authority

If support is required and unavailable, the pathway may need to stop.

A support-call policy can help identify stop-and-await conditions, but Stop Authority remains a separate pathway role.

### Evidence Log

Support calls should leave enough evidence to understand:

- what support was available
- what support was requested
- what support was skipped
- what support changed
- what uncertainty remained

The Evidence Log preserves this record.

### Repair Owner

If support was missed, delayed, or incorrectly skipped, repair may be needed.

The Repair Owner is responsible for reconnecting the pathway after failure, correction, rollback, or review.

### Action Class Matrix

Support-call policy interacts with action class.

Higher-impact or less reversible actions may require stronger support conditions, approval gates, or stop conditions.

However, this note does not modify the Action Class Matrix.

## Missed support

A missed-support event occurs when the pathway proceeds without support even though support would have materially improved the outcome.

In RPE, this is best treated as a structural review signal.

It may indicate that:

- the return point was missing
- the approval gate was not activated
- the stop condition was too weak
- the evidence record was insufficient
- the repair owner needs to review the pathway

A missed-support event does not automatically prove legal fault, safety failure, compliance failure, fairness failure, or production invalidity.

## Current boundary

This note does not create:

- a schema field
- a checker rule
- a runtime event field
- a workflow
- a connector
- a production policy
- a Lean theorem

It only maps a related support-seeking concept to existing RPE concepts.

## Future path

Before adding support-call policy to schemas or examples, the repository should have:

1. this concept mapping note,
2. a small boundary-only or negative example,
3. a clear target layer for the field or record,
4. a checker-design note if any checker behavior is proposed,
5. explicit restart conditions from `docs/deferred-work-restart-conditions.md`.

Until then, support-call policy remains a concept-level and related-work connection.
