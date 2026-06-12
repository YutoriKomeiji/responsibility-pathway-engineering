# Lean Formalization

This directory contains formalization candidates for Responsibility Pathway Engineering.

## Purpose

The purpose of these files is to express selected structural properties in Lean.

Formalization is incremental and scope-limited.

## Current files

The Phase 2 Lean spine is split into small modules:

- `ResponsibilityPathway/Basic.lean` - minimal node kinds, model assumptions, node predicates, and constructor-level responsibility nodes
- `ResponsibilityPathway/Lifecycle.lean` - minimal pathway structure and lifecycle predicates
- `ResponsibilityPathway/Examples.lean` - constructor-level example pathways used as model witnesses
- `ResponsibilityPathway/Invariants.lean` - scoped boundary predicates and current theorem candidates
- `ResponsibilityPathway/Core.lean` - stable entry point that imports the split modules

The split plan is recorded in `../../docs/phase-2-lean-split-plan.md`.

## Build path

The repository now includes a minimal Lean build path:

- `../../lean-toolchain`
- `../../lakefile.lean`
- `../../.github/workflows/check-lean.yml`

From the repository root, run:

```bash
lake build
```

The GitHub Actions workflow installs Elan, runs `lake update`, and then runs `lake build` for the minimal Lean package.

A passing build only checks the Lean package. It does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness.

## Basic sanity theorems

Current constructor-level sanity theorems in `ResponsibilityPathway/Basic.lean`:

- `safe_ai_node_is_ai`
- `safe_ai_node_cannot_hold_final_responsibility`
- `human_responsibility_node_can_hold_final_responsibility`
- `institutional_responsibility_node_can_hold_final_responsibility`
- `human_responsibility_node_is_not_ai`

These theorems check the current constructor definitions only. They are not real-world certification claims.

## Example lifecycle sanity theorems

Current constructor-level sanity theorems in `ResponsibilityPathway/Examples.lean`:

- `safe_ai_assisted_pathway_has_ai_participation`
- `safe_ai_assisted_pathway_has_human_or_institutional_return_point`
- `non_ai_pathway_has_no_ai_participation`
- `repaired_pathway_example_is_repaired_and_has_record`
- `suspended_pathway_example_is_suspended_and_has_review_or_return`
- `returning_pathway_example_is_returning_without_automatic_continuation`
- `closed_pathway_example_is_closed_with_evidence_and_reopening`

These theorems check only that the constructor-level examples expose the intended lifecycle predicates. They are not real-world certification claims.

## Current invariant candidates

Current Phase 2 invariant candidates:

1. under current minimal assumptions, a node constructed as a safe AI node cannot hold final responsibility
2. a safely constructed AI-assisted pathway has a human or institutional return point
3. a safely constructed repaired pathway has a repair record
4. a safely constructed suspended pathway preserves review or return conditions
5. a safely constructed returning pathway does not allow automatic continuation
6. a safely constructed closed pathway preserves evidence and reopening-condition records

These are represented by:

- `NodeKind`
- `ModelAssumptions`
- `NoArtificialLegalPersonhood`
- `Node`
- `IsAI`
- `IsHumanOrInstitution`
- `CanHoldFinalResponsibility`
- `AIResponsibilityBoundary`
- `currentMinimalAssumptions`
- `safe_ai_node_cannot_hold_final_responsibility_under_current_assumptions`
- `Pathway`
- `HasAIParticipation`
- `HasHumanOrInstitutionalReturnPoint`
- `IsRepairedPathway`
- `HasRepairRecord`
- `IsSuspendedPathway`
- `HasReviewOrReturnCondition`
- `IsReturningPathway`
- `AllowsAutomaticContinuation`
- `IsClosedPathway`
- `HasEvidenceRecord`
- `HasReopeningCondition`
- `AIReturnPointBoundary`
- `RepairRecordBoundary`
- `SuspensionReviewReturnBoundary`
- `ReturningNoAutomaticContinuationBoundary`
- `ClosureEvidenceReopeningBoundary`
- `safe_ai_assisted_pathway_has_return_point`
- `repaired_pathway_has_repair_record`
- `suspended_pathway_preserves_review_or_return_condition`
- `returning_pathway_does_not_allow_automatic_continuation`
- `closed_pathway_preserves_evidence_and_reopening_condition`

## Boundary

A Lean proof in this repository proves only the explicitly stated theorem under its stated assumptions.

It does not prove that any real-world AI system, organization, workflow, institution, or legal framework is safe, accountable, fair, lawful, compliant, morally resolved, complete, or production ready.

The current AI final-responsibility invariant is scoped to the current minimal model, where no artificial legal-personhood layer is assumed.

It is not a universal claim that future law, future institutions, states, international agreements, or users could never grant some form of legal or institutional personhood to AI systems.

If such a layer is introduced in a future model, the AI final-responsibility invariant must be revisited instead of treated as absolute.

The repair-record invariant does not mean real-world repair is complete, harm is eliminated, legal liability is resolved, moral responsibility is resolved, or closure is justified. It only states that a pathway declared repaired in the minimal model must preserve a repair-record signal.

The suspension review/return invariant does not mean suspension is justified, safe, compliant, fair, legally valid, morally resolved, or operationally complete. It only states that a pathway declared suspended in the minimal model must preserve a review-or-return condition.

The returning no-automatic-continuation invariant does not mean return is justified, authorized, safe, compliant, fair, legally valid, morally resolved, or operationally complete. It only states that a pathway declared returning in the minimal model must not be treated as automatically continuing.

The closure evidence/reopening invariant does not mean closure is justified, legally valid, morally resolved, safe, compliant, fair, permanent, or operationally complete. It only states that a pathway declared closed in the minimal model must preserve evidence records and reopening-condition records.

The current invariants do not make legal or moral claims. They state structural properties inside the minimal model.

## Strategy

Definitions first.
Invariants second.
Transitions third.
Examples fourth.
Extended theories later.

## Responsibility

The human author remains responsible for definitions and claims.
AI tools may assist implementation but are not responsible authors.
