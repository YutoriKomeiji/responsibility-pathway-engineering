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
- `docs/lean-evidence-approval-formalization-plan.md`
- `formal/lean/README.md`

## Current connection status

| Document | Current role | Current connection status | Next likely connection |
| --- | --- | --- | --- |
| `docs/social-connection-review-navigation.md` | focused reader path for social-connection review | connected from validation checklist, social exception cases, approval-transfer alignment, AI Judgment Node note, Evidence Log, task inventory, and operation index | keep aligned when review paths change |
| `docs/social-connection-exception-cases.md` | social-connection risk map | connected to review navigation and approval-transfer alignment | keep as review input; no schema or checker change yet |
| `docs/evidence-approval-transfer-alignment.md` | aligns approval skip, evidence, responsibility transfer, and social exceptions | connected to social exception cases, review navigation, Evidence Log, AI Judgment Node note, and Lean formalization planning path | consider Lean implementation only after separate implementation step |
| `docs/validation-checklist.md` | bounded review checklist | includes social connection review and review navigation | keep aligned when checklist scope changes |
| `docs/ai-judgment-node-task-control.md` | AI local judgment and approval-skip boundary | connected to approval-transfer alignment and social review navigation | keep task-control expansion deferred without design note |
| `docs/evidence-log.md` | evidence reconstruction and tamper-evident change handling | connected to approval-transfer alignment and social review navigation | use Lean formalization plan before formal theorem work |
| `docs/lean-evidence-approval-formalization-plan.md` | planning note for possible future Lean structural completeness work | connected from Lean README and this gap inventory | do not implement Lean module from plan alone |
| `formal/lean/README.md` | Lean4 adoption and evidentiary completeness boundary | connected to the Lean evidence approval formalization plan | keep theorem claims structural and assumption-scoped |
| `docs/current-task-inventory.md` | active and near-active task inventory | reflects social-connection cluster and Lean evidence approval planning | keep aligned when cluster status changes |
| `docs/operation-index.md` | operation navigation entrance | now includes social-connection review and gap-inventory pointers | avoid broad rewrites unless navigation changes again |

## Known gap candidates

### Operation index visibility

`docs/social-connection-review-navigation.md` and `docs/repository-pathway-gap-inventory.md` are now visible from `docs/operation-index.md`.

Future updates should remain small and focused because `docs/operation-index.md` is a large navigation file.

### Task inventory visibility

The social-connection cluster and Lean evidence-completeness candidates are now reflected in `docs/current-task-inventory.md`.

Future task-inventory updates should preserve the distinction between P1 review-navigation consolidation and P4 deferred schema, checker, workflow, runtime, connector, conformance, or Lean expansion.

### Lean formalization planning

Lean work should not jump directly from candidate list to theorem implementation.

`docs/lean-evidence-approval-formalization-plan.md` defines the current planning route for:

- evidence record completeness
- approval-skip rule preservation
- responsibility-transfer destination
- later return or dispute path
- correction or supersession record completeness

A separate implementation step is still required before adding Lean modules or theorem candidates.

### Review readiness connection

Before public or external review expansion, check whether external-review notes should reference the social-connection review path.

This should remain a navigation improvement, not a claim of social acceptance, legal validity, compliance, safety, or certification.

## Maintenance rule

Prefer small bidirectional links before large index rewrites.

When a large document is risky to update, add or update a focused navigation note first, then connect the large document later with the smallest viable pointer.

## Boundary

This inventory does not prove that the repository is complete or coherent.

It records current path risks and safe next connection points for future maintenance.
