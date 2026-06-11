# Lean Formalization

This directory contains formalization candidates for Responsibility Pathway Engineering.

## Purpose

The purpose of these files is to express selected structural properties in Lean.

Formalization is incremental and scope-limited.

## Current files

- `ResponsibilityPathway/Core.lean` - minimal node and pathway model with early responsibility-boundary invariant candidates

## Current invariant candidates

Current Phase 2 invariant candidates:

1. under current minimal assumptions, a node constructed as a safe AI node cannot hold final responsibility
2. a safely constructed AI-assisted pathway has a human or institutional return point
3. a safely constructed repaired pathway has a repair record
4. a safely constructed suspended pathway preserves review or return conditions

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
- `AIReturnPointBoundary`
- `RepairRecordBoundary`
- `SuspensionReviewReturnBoundary`
- `safe_ai_assisted_pathway_has_return_point`
- `repaired_pathway_has_repair_record`
- `suspended_pathway_preserves_review_or_return_condition`

## Boundary

A Lean proof in this repository proves only the explicitly stated theorem under its stated assumptions.

It does not prove that any real-world AI system, organization, workflow, institution, or legal framework is safe, accountable, fair, lawful, compliant, morally resolved, complete, or production ready.

The current AI final-responsibility invariant is scoped to the current minimal model, where no artificial legal-personhood layer is assumed.

It is not a universal claim that future law, future institutions, states, international agreements, or users could never grant some form of legal or institutional personhood to AI systems.

If such a layer is introduced in a future model, the AI final-responsibility invariant must be revisited instead of treated as absolute.

The repair-record invariant does not mean real-world repair is complete, harm is eliminated, legal liability is resolved, moral responsibility is resolved, or closure is justified. It only states that a pathway declared repaired in the minimal model must preserve a repair-record signal.

The suspension review/return invariant does not mean suspension is justified, safe, compliant, fair, legally valid, morally resolved, or operationally complete. It only states that a pathway declared suspended in the minimal model must preserve a review-or-return condition.

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
