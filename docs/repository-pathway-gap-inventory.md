# Repository Pathway Gap Inventory

This note tracks possible structure breaks and reader-path gaps in the Responsibility Pathway Engineering repository.

It is a maintenance inventory only.

It does not introduce schema changes, checker changes, workflow changes, runtime behavior, connector behavior, Lean formalization, legal decision logic, compliance certification, safety certification, social acceptance certification, or production authorization.

## Purpose

Use this inventory to avoid losing important documents after new concepts, review notes, or boundary notes are added.

A document is considered at risk of pathway gap when:

- it is important but hard to discover from nearby documents
- it introduces a review concept without a return path to the main review flow
- it is cited only one way when bidirectional navigation would help
- it affects claims, boundaries, or review readiness but is absent from task or operation navigation
- it should remain deferred but lacks a clear restart condition

## Current social-connection cluster

The current social-connection cluster includes:

- `docs/social-connection-review-navigation.md`
- `docs/social-connection-exception-cases.md`
- `docs/evidence-approval-transfer-alignment.md`
- `docs/validation-checklist.md`
- `docs/ai-judgment-node-task-control.md`
- `docs/evidence-log.md`
- `formal/lean/README.md`

## Current connection status

| Document | Current role | Current connection status | Next likely connection |
| --- | --- | --- | --- |
| `docs/social-connection-review-navigation.md` | focused reader path for social-connection review | connected from validation checklist, social exception cases, approval-transfer alignment, AI Judgment Node note, and Evidence Log | add to task inventory and operation index when safe |
| `docs/social-connection-exception-cases.md` | social-connection risk map | connected to review navigation and approval-transfer alignment | keep as review input; no schema or checker change yet |
| `docs/evidence-approval-transfer-alignment.md` | aligns approval skip, evidence, responsibility transfer, and social exceptions | connected to social exception cases and review navigation | consider Lean formalization plan later |
| `docs/validation-checklist.md` | bounded review checklist | includes social connection review and review navigation | may need operation-index pointer later |
| `docs/ai-judgment-node-task-control.md` | AI local judgment and approval-skip boundary | connected to approval-transfer alignment and social review navigation | may need task-inventory pointer if not already present |
| `docs/evidence-log.md` | evidence reconstruction and tamper-evident change handling | connected to approval-transfer alignment and social review navigation | consider Lean evidence completeness plan later |
| `formal/lean/README.md` | Lean4 adoption and evidentiary completeness boundary | names evidence and approval-transfer candidates | requires separate formalization plan before Lean module work |

## Known gap candidates

### Operation index visibility

`docs/social-connection-review-navigation.md` is not yet clearly visible from `docs/operation-index.md`.

Because `docs/operation-index.md` is a large navigation file, update it only with a small, focused change after this inventory is stable.

### Task inventory visibility

The social-connection cluster and Lean evidence-completeness candidates should be reflected in `docs/current-task-inventory.md` before deeper implementation or formalization work.

### Lean formalization planning

Lean work should not jump directly from candidate list to theorem implementation.

A separate plan should define the minimal model terms for:

- evidence record completeness
- approval-skip rule preservation
- responsibility-transfer destination
- later return or dispute path
- correction or supersession record completeness

### Review readiness connection

Before public or external review expansion, check whether external-review notes should reference the social-connection review path.

This should remain a navigation improvement, not a claim of social acceptance, legal validity, compliance, safety, or certification.

## Maintenance rule

Prefer small bidirectional links before large index rewrites.

When a large document is risky to update, add or update a focused navigation note first, then connect the large document later with the smallest viable pointer.

## Boundary

This inventory does not prove that the repository is complete or coherent.

It records current path risks and safe next connection points for future maintenance.
