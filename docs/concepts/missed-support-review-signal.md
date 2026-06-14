# Missed-Support Review Signal

This note defines missed support as a Responsibility Pathway review signal.

It is a concept note only. It does not introduce schema fields, checker rules, runtime fields, connector behavior, production policy, or Lean theorems.

## Definition

A missed-support review signal records that a pathway appears to have continued or nearly continued without support that should have been requested.

Support may include:

- human review
- user clarification
- expert input
- approval gate activation
- stop authority review
- tool use
- evidence gathering
- repair-owner review

The signal is about pathway structure, not automatic fault determination.

## Why it matters

A responsibility pathway is weakened when an AI support node continues without returning to the right human, institution, approval gate, stop authority, evidence source, or repair owner.

A missed-support signal helps reviewers ask:

- Was support available?
- Was support required?
- Was support requested?
- Was support skipped?
- Did skipping support change the pathway?
- Did the pathway preserve enough evidence to review the skip?
- Who can stop, return, or repair the pathway now?

## Relation to support-call policy

A support-call policy asks when an agent should seek support.

A missed-support review signal records that the support-call boundary may have failed.

In RPE terms:

- support-call policy is the decision or recommendation boundary;
- missed support is a review signal after that boundary may have been crossed;
- neither replaces the human or institutional decision owner.

## Existing RPE concept connections

### Decision Owner

The Decision Owner decides whether the pathway may proceed, return, stop, repair, defer, or close.

A missed-support signal returns the pathway to the Decision Owner for review.

### Human Return Point

If the agent should have sought human review, the Human Return Point records where the pathway should have returned.

A missed-support signal may indicate that the Human Return Point was missing, unclear, skipped, or not activated.

### Approval Gate

If the action required approval, a missed-support signal may indicate that the Approval Gate was bypassed or under-specified.

The signal does not approve or reject the action by itself.

### Stop Authority

If support was required but unavailable, the pathway may need to stop.

A missed-support signal may trigger stop-and-return review.

### Evidence Log

A missed-support signal should be accompanied by evidence that can reconstruct:

- what was proposed
- what support was available
- what support was required
- what support was skipped
- what uncertainty remained
- what return or repair path exists

### Repair Owner

If missed support affected the pathway, the Repair Owner may need to record correction, rejection, rollback, revision, or continuation conditions.

## What the signal is not

A missed-support review signal is not:

- legal liability determination
- moral blame assignment
- safety certification result
- compliance determination
- fairness determination
- production-readiness result
- runtime correctness proof
- connector correctness proof
- semantic correctness proof
- AI final-responsibility transfer

It is a structural signal for review.

## Minimal example

The current minimal example is:

- `examples/missed-support-boundary-minimal.yaml`

Focused status is recorded in:

- `docs/examples/missed-support-current-status.md`

The example models repository maintenance only.

It is synthetic, local, boundary-only, non-production, and non-certifying.

## Current checker boundary

The current bounded example checker can check the file as a pathway example with `lifecycle_state: returning`.

The checker does not enforce missed-support correctness or support-call semantics.

Therefore, a green workflow only means that the current bounded structural example checks completed without failures.

## Future path

Possible future work may include:

1. a schema-design note for support-call or missed-support fields;
2. additional boundary-only examples;
3. optional structural checker design;
4. runtime-event support-call observation fields;
5. formal theorem-role notes.

All future work remains deferred until `docs/deferred-work-restart-conditions.md` restart conditions are satisfied.
