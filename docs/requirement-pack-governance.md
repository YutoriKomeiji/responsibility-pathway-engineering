# Requirement Pack Governance

This document defines the maintenance and lifecycle boundary for RPE requirement packs.

A requirement pack is not self-validating policy truth. It is a bounded operational mapping maintained by identified human or institutional owners.

## Lifecycle

```text
draft → reviewed → approved → active
                         ↘ suspended
                         ↘ superseded
                         ↘ retired
```

Allowed lifecycle states:

- `draft`: incomplete and not eligible for operational evaluation;
- `reviewed`: reviewed, but not yet approved for active use;
- `approved`: approved but not necessarily effective yet;
- `active`: eligible for bounded operational evaluation;
- `suspended`: temporarily ineligible pending review or correction;
- `superseded`: replaced by another identified pack version;
- `retired`: permanently withdrawn from use.

## Required governance record

Each governed pack must identify:

- pack identifier and pack version;
- lifecycle state;
- maintenance owner;
- reviewer and approver;
- source authority, source version, jurisdiction, and effective scope;
- interpretation status and unresolved ambiguity;
- effective date, last-review date, and next-review due date;
- supersession relationship when applicable;
- human-return role for governance failures.

## Eligibility rule

A pack is governance-eligible only when all of the following hold:

1. lifecycle state is `active`;
2. maintenance owner is present;
3. reviewer and approver are present;
4. last-review date and next-review due date are present;
5. next-review due date has not passed;
6. interpretation status is not `unreviewed`;
7. unresolved ambiguity is explicitly recorded;
8. a superseded, suspended, or retired pack is not selected.

A governance failure must not silently produce `allow`. The bounded default is `human_gate` with visible reason codes and a configured human-return role.

## Reason-code namespace

Governance checks use the `RPE-PACK-GOV-*` namespace. Initial codes include:

- `RPE-PACK-GOV-NOT-ACTIVE`
- `RPE-PACK-GOV-MISSING-MAINTENANCE-OWNER`
- `RPE-PACK-GOV-MISSING-REVIEWER`
- `RPE-PACK-GOV-MISSING-APPROVER`
- `RPE-PACK-GOV-MISSING-REVIEW-DATE`
- `RPE-PACK-GOV-MISSING-NEXT-REVIEW-DUE`
- `RPE-PACK-GOV-REVIEW-EXPIRED`
- `RPE-PACK-GOV-INTERPRETATION-UNREVIEWED`
- `RPE-PACK-GOV-SUPERSEDED`

## Separation from runtime semantics

The governance record determines whether a pack may enter evaluation. It does not determine whether the mapped requirements are legally correct, complete, current, fair, safe, or appropriate for a real-world case.

The current governance checker is a bounded repository and integration aid. It is not legal review, regulatory monitoring, certification, or proof that a pack should be used.

## Change control

Changes to an active pack should produce a reviewable version change. Silent replacement is prohibited. Breaking interpretation changes require a new pack version and explicit supersession metadata.

External pack loading remains blocked until governance and compatibility behavior are connected to the canonical kernel entry path and covered by deterministic tests.
