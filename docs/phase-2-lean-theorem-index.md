# Phase 2 Lean Theorem Index

This index groups the current Phase 2 Lean theorem candidates by role.

It is a navigation aid only. It does not add new formal claims and does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness.

## Build status

The repository has a minimal Lean build path:

- `lean-toolchain`
- `lakefile.lean`
- `.github/workflows/check-lean.yml`

The workflow installs Elan, runs `lake update`, and then runs `lake build`.

A passing build means only that the current Lean package builds.

## Module layout

- `formal/lean/ResponsibilityPathway/Basic.lean`
- `formal/lean/ResponsibilityPathway/Lifecycle.lean`
- `formal/lean/ResponsibilityPathway/Examples.lean`
- `formal/lean/ResponsibilityPathway/Invariants.lean`
- `formal/lean/ResponsibilityPathway/Core.lean`

`Core.lean` is the stable import entry point.

## Basic constructor sanity theorems

Defined in `formal/lean/ResponsibilityPathway/Basic.lean`.

These theorems check constructor-level facts about minimal node definitions.

- `safe_ai_node_is_ai`
- `safe_ai_node_cannot_hold_final_responsibility`
- `human_responsibility_node_can_hold_final_responsibility`
- `institutional_responsibility_node_can_hold_final_responsibility`
- `human_responsibility_node_is_not_ai`

Boundary:

- These are structural model facts only.
- They do not state that any real-world person or institution has actually accepted responsibility.
- They do not state a universal legal conclusion about AI systems.

## Example lifecycle sanity theorems

Defined in `formal/lean/ResponsibilityPathway/Examples.lean`.

These theorems check that constructor-level example pathways expose the intended lifecycle predicates.

- `safe_ai_assisted_pathway_has_ai_participation`
- `safe_ai_assisted_pathway_has_human_or_institutional_return_point`
- `non_ai_pathway_has_no_ai_participation`
- `repaired_pathway_example_is_repaired_and_has_record`
- `suspended_pathway_example_is_suspended_and_has_review_or_return`
- `returning_pathway_example_is_returning_without_automatic_continuation`
- `closed_pathway_example_is_closed_with_evidence_and_reopening`

Boundary:

- These are example-constructor checks only.
- They do not certify the corresponding lifecycle state in a real workflow.
- They do not prove operational completeness.

## Boundary predicates

Defined in `formal/lean/ResponsibilityPathway/Invariants.lean`.

These predicates name the current structural boundaries.

- `AIResponsibilityBoundary`
- `AIReturnPointBoundary`
- `RepairRecordBoundary`
- `SuspensionReviewReturnBoundary`
- `ReturningNoAutomaticContinuationBoundary`
- `ClosureEvidenceReopeningBoundary`

Boundary:

- These predicates define the current minimal model boundaries.
- They are not legal, moral, operational, compliance, fairness, safety, or certification standards.

## Positive invariant theorem candidates

Defined in `formal/lean/ResponsibilityPathway/Invariants.lean`.

These theorem candidates show that specific constructor-level examples satisfy the current boundary predicates.

- `safe_ai_node_cannot_hold_final_responsibility_under_current_assumptions`
- `safe_ai_assisted_pathway_has_return_point`
- `repaired_pathway_has_repair_record`
- `suspended_pathway_preserves_review_or_return_condition`
- `returning_pathway_does_not_allow_automatic_continuation`
- `closed_pathway_preserves_evidence_and_reopening_condition`

Boundary:

- These are scoped to the explicitly modeled assumptions and constructors.
- The AI final-responsibility theorem is scoped to the current minimal model where artificial legal personhood is not enabled.
- Future legal, institutional, national, international, or user/provider-agreement layers require explicit modeling.

## Vacuity / non-trigger theorem candidates

Defined in `formal/lean/ResponsibilityPathway/Invariants.lean`.

These theorem candidates show that boundary implications are not over-applied when their trigger condition is absent.

- `non_ai_pathway_satisfies_ai_return_point_boundary`
- `non_repaired_pathway_satisfies_repair_record_boundary`
- `non_suspended_pathway_satisfies_suspension_boundary`
- `non_returning_pathway_satisfies_returning_boundary`
- `non_closed_pathway_satisfies_closure_boundary`

Boundary:

- These are implication-shape checks.
- They do not say the non-trigger examples are complete, safe, compliant, fair, legally valid, morally resolved, or production ready.

## Recommended next theorem work

Low-risk next steps:

1. Keep current theorem names stable until the minimal build path remains green.
2. Add only small theorem candidates that preserve existing assumptions.
3. Prefer constructor-level sanity checks before generalized theory.
4. Avoid introducing real-world legal, safety, compliance, fairness, certification, or production-readiness claims.

Do not begin larger reference implementations until definitions, examples, checker boundaries, Lean assumptions, and excluded claims remain aligned.
