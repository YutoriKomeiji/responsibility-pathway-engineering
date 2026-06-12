# Responsibility Pathway Record Review

This document describes a simple way to review a Responsibility Pathway record after it has been created.

The goal is to make responsibility pathways easy for people, organizations, and AI-assisted tools to check without using unclear or inflated language.

## Purpose

A Responsibility Pathway record should be understandable after the fact.

A later reader should be able to ask:

- What happened?
- Who or what was involved?
- Was AI used as support?
- Where did responsibility return?
- Who could stop the pathway?
- What evidence was kept?
- Was repair needed?
- Was the pathway suspended, returned, or closed?
- What must not be claimed from this record?

This review process checks the structure of the record.

It does not decide whether the real-world decision was legally correct, safe, fair, compliant, morally resolved, certified, or production ready.

## Plain language terms

This repository uses plain terms wherever possible.

- Responsibility Pathway record: a record of a pathway, its participants, its return points, and its lifecycle state
- Review: checking the record after it is created
- Recheck: running the same review again later
- Review result: the output of the review
- Review tool: software that performs bounded structural checks
- Evidence record: a reference to information used for review
- Repair record: a record that a pathway was corrected or repaired
- Reopening condition: a condition under which a closed pathway can be reopened

The word Responsibility Pathway remains central. Other words should be easy for humans and AI tools to understand.

## What can be checked

A review can check whether the record preserves required structure.

It can check whether:

- the record has a pathway identifier
- the lifecycle state is present
- participating nodes are listed
- AI support nodes are marked as support nodes
- a human or institutional return point is present when AI support is involved
- final responsibility is not silently assigned to an AI support node under the current minimal model
- stop authority is recorded
- approval gates are recorded when used
- evidence records are present
- repair records are present when the pathway is marked repaired
- review or return conditions are present when the pathway is marked suspended
- returning pathways do not imply automatic continuation
- closed pathways preserve evidence records and reopening conditions
- excluded claims remain visible
- schema version and checker version are recorded where applicable

## What must not be claimed

A successful review does not mean:

- the underlying decision was legally valid
- the system was safe
- the process was compliant
- the outcome was fair
- moral accountability was fully resolved
- an institution certified the process
- the workflow was production ready
- all risks were eliminated
- human or institutional responsibility was replaced

The review says only that the record preserved the required responsibility-pathway structure under the current model.

## Minimum record fields

A minimal Responsibility Pathway record should preserve:

```text
pathway_id
schema_version
lifecycle_state
participating_nodes
ai_support_nodes
human_or_institutional_return_point
stop_authority
approval_gate
responsibility_owner
evidence_records
repair_record
suspension_condition
return_condition
closure_record
reopening_condition
excluded_claims
created_at
updated_at
review_tool_version
```

Not every field is required in every lifecycle state, but the record should make missing or non-applicable fields explicit.

## Review steps

A simple review should proceed in this order:

1. Confirm the record version.
2. Confirm the lifecycle state.
3. Confirm the participating nodes.
4. Check whether AI support is involved.
5. If AI support is involved, confirm the human or institutional return point.
6. Confirm that stop authority is recorded.
7. Confirm evidence records.
8. If the record is repaired, confirm the repair record.
9. If the record is suspended, confirm review or return conditions.
10. If the record is returning, confirm that it does not imply automatic continuation.
11. If the record is closed, confirm evidence records and reopening conditions.
12. Confirm excluded claims.
13. Produce a review result.

## Review result

A review result should be plain and limited.

Example:

```text
review_status: passed
review_scope: structural responsibility-pathway review
schema_version: 0.2.0
review_tool_version: example-checker-0.1
checked_items:
  - lifecycle state present
  - AI support node marked
  - human or institutional return point present
  - stop authority present
  - evidence records present
  - excluded claims present
not_claimed:
  - legal validity
  - safety certification
  - compliance certification
  - fairness certification
  - moral accountability resolution
  - production readiness
```

A minimal YAML fixture is available at `fixtures/review-results/record-review-result-minimal.yaml`.

That fixture is an output example only. It is not a pathway example, legal decision, safety decision, compliance decision, fairness decision, moral-resolution decision, certification, or production approval.

The review result should avoid broad wording.

Use:

```text
The record preserves the required responsibility-pathway structure under the current review rules.
```

Do not use:

```text
The system is safe.
The process is legally valid.
The organization is compliant.
The outcome is fair.
The issue is morally resolved.
```

## Rechecking later

A Responsibility Pathway record should be recheckable later.

A later reviewer should know:

- which schema version was used
- which review tool version was used
- which rules were applied
- which fields were checked
- which fields were not checked
- which claims were excluded

If the rules change, the record should not be silently treated as newly reviewed.

Instead, create a new review result with the new version information.

## Relationship to Lean

Lean is used for selected structural assumptions and theorem candidates.

A record review tool does not need to prove every real-world fact in Lean.

The practical relationship is:

```text
Responsibility Pathway definitions
→ schema-backed record
→ bounded review tool
→ review result
→ Lean-backed structural reference
```

The Lean layer helps keep the core assumptions explicit.

The review tool helps organizations check records in ordinary workflows.

Neither layer replaces responsible human or institutional judgment.

## Relationship to enterprise use

This document complements `docs/enterprise-implementation-profile.md`.

The enterprise implementation profile explains how organizations can connect RPE to workflow, evidence, checker, and governance layers.

This document explains how a specific Responsibility Pathway record can be reviewed or rechecked after it is created.

## Stop conditions

Stop the review and escalate to a responsible human or institution if:

- no human or institutional return point is present where one is required
- AI support is treated as the final responsibility holder under the current minimal model
- stop authority is missing
- evidence records are missing
- a repaired pathway has no repair record
- a suspended pathway has no review or return condition
- a returning pathway implies automatic continuation
- a closed pathway lacks evidence records or reopening conditions
- excluded claims are missing or weakened
- the review result is being used as legal, safety, compliance, fairness, or moral certification

## Responsibility boundary

Responsibility Pathway review helps preserve returnability.

It does not remove responsibility from people or institutions.

The organization using the record remains responsible for interpretation, review, governance, legal assessment, deployment, and public claims.
