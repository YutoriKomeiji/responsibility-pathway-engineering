# Requirement Pack Governance

This document defines the maintenance and lifecycle boundary for RPE Requirement Packs.

A Requirement Pack is not self-validating policy truth. It is a bounded operational mapping maintained by identified human or institutional owners.

## Lifecycle

```text
draft → reviewed → approved → active
                         ↘ suspended
                         ↘ superseded
                         ↘ retired
```

Allowed lifecycle states:

- `draft`: incomplete and not eligible for strict governed evaluation;
- `reviewed`: reviewed, but not yet approved for active use;
- `approved`: approved but not necessarily effective yet;
- `active`: candidate for bounded governed evaluation when all other eligibility conditions pass;
- `suspended`: temporarily ineligible pending review or correction;
- `superseded`: replaced by another identified pack version;
- `retired`: permanently withdrawn from use.

## Required governance record

Each governed pack identifies, at minimum:

- governance contract version;
- pack identifier and pack version;
- lifecycle state;
- maintenance owner;
- reviewer and approver;
- source authority, source version, jurisdiction, and effective scope;
- interpretation status and unresolved ambiguity;
- effective date, last-review date, and next-review due date;
- supersession relationship when applicable;
- Human Return role for governance failures.

## Strict governed eligibility

`rpe_kernel.evaluate_governed_action()` applies governance eligibility after contract compatibility and pack/governance binding, and before applicability/requirement evaluation.

The strict governed path rejects visible failure states including:

- non-active lifecycle state;
- missing maintenance owner, reviewer, or approver;
- malformed or missing review dates;
- future `last_reviewed` dates;
- invalid review-date ordering;
- expired review;
- not-yet-effective records;
- non-eligible interpretation state;
- non-empty unresolved ambiguity;
- suspended, superseded, or retired records;
- missing or mismatched pack/governance identity/version/source binding;
- missing required Human Return information.

A governance failure must not silently produce `allow`. The bounded default is a visible non-allow result, normally `human_gate`, with stable reason information and a Human Return route.

## Separation from compatibility and source trust

Governance eligibility is distinct from:

- contract compatibility;
- pack/governance binding;
- schema validity;
- local file readability;
- source authenticity/trust;
- legal or normative interpretation correctness;
- real-world applicability.

Passing one layer must not silently promote another.

The first bounded loader accepts caller-provided content and explicit local files only. Loading bytes does not establish governance eligibility or source authority; strict governed evaluation remains responsible for the runtime governance decision.

## Runtime authority boundary

Governance eligibility determines whether a pack may participate in RPE evaluation. It does not grant execution authority.

Even a fully eligible pack that contributes to an `allow` result leaves:

- `authority_effect = none`;
- `decision_scope = evaluation_only`.

Execution, external-effect verification, repair authority, resume authority, and final responsibility remain outside Requirement Pack governance.

## Reason-code boundary

Governance failures use the `RPE-PACK-GOV-*` namespace and related governed-admission/binding reason codes. Reason-code meanings are compatibility-sensitive and should not be silently repurposed.

## Change control

Changes to an active pack should produce a reviewable version change. Silent replacement is prohibited. Breaking interpretation changes require a new pack version and explicit supersession metadata.

A schema-valid, governance-eligible, or loadable Requirement Pack still does not prove that its source interpretation is legally correct, complete, current, fair, safe, or suitable for a deployment. Those remain separate human/institutional review responsibilities.
