# Phase 2 Lean Split Plan

This note records a low-risk split plan for the current Phase 2 Lean formalization.

The goal is not to expand the theory yet. The goal is to keep the current minimal model readable, traceable, and assumption-explicit before adding more invariant candidates.

## Current state

The current Lean formalization is concentrated in:

- `formal/lean/ResponsibilityPathway/Core.lean`

That file currently contains:

- minimal node-kind definitions
- explicit model assumptions
- minimal node definitions and responsibility-capacity predicates
- AI final-responsibility boundary candidate
- minimal pathway structure
- lifecycle predicates
- lifecycle boundary predicates
- constructor-level example pathways
- theorem candidates for the current six Phase 2 lifecycle invariants

This is acceptable for an early Phase 2 spine, but it should be split before the file becomes a mixed ontology, lifecycle, examples, and theorem accumulator.

## Proposed split

A future low-risk split may use the following modules:

```text
formal/lean/ResponsibilityPathway/Basic.lean
formal/lean/ResponsibilityPathway/Lifecycle.lean
formal/lean/ResponsibilityPathway/Invariants.lean
formal/lean/ResponsibilityPathway/Examples.lean
formal/lean/ResponsibilityPathway/Core.lean
```

### `Basic.lean`

Purpose: keep the smallest stable model primitives.

Candidate contents:

- `namespace ResponsibilityPathway`
- `NodeKind`
- `ModelAssumptions`
- `NoArtificialLegalPersonhood`
- `Node`
- `IsAI`
- `IsHumanOrInstitution`
- `CanHoldFinalResponsibility`
- `currentMinimalAssumptions`
- `safeAINode`
- `humanResponsibilityNode`
- `institutionalResponsibilityNode`

Boundary:

- Do not turn this into a complete ontology.
- Do not model legal personhood layers silently.
- Keep artificial legal-personhood assumptions explicit.

### `Lifecycle.lean`

Purpose: keep the minimal pathway and lifecycle-state predicates.

Candidate contents:

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

Boundary:

- Keep this as a minimal structural lifecycle model.
- Do not claim operational completeness.
- Do not encode production workflow semantics yet.

### `Invariants.lean`

Purpose: keep named boundary predicates and theorem candidates.

Candidate contents:

- `AIResponsibilityBoundary`
- `AIReturnPointBoundary`
- `RepairRecordBoundary`
- `SuspensionReviewReturnBoundary`
- `ReturningNoAutomaticContinuationBoundary`
- `ClosureEvidenceReopeningBoundary`
- current theorem candidates proving the six constructor-level invariant cases
- vacuity/non-trigger cases where useful

Boundary:

- Every theorem must remain scoped to explicitly modeled assumptions.
- The AI final-responsibility invariant must remain assumption-scoped, not universal.
- No theorem should be described as proving legal validity, safety, compliance, fairness, moral accountability resolution, certification, or production readiness.

### `Examples.lean`

Purpose: keep constructor-level examples and safe/non-trigger cases.

Candidate contents:

- `safeAIAssistedPathway`
- `nonAIPathway`
- `repairedPathwayWithRecord`
- `suspendedPathwayWithReviewOrReturn`
- `returningPathwayWithoutAutomaticContinuation`
- `closedPathwayWithEvidenceAndReopening`

Boundary:

- Examples are model witnesses, not real-world certification artifacts.
- Example names should remain clear and lifecycle-specific.

### `Core.lean`

Purpose: preserve a stable import surface.

Candidate future content:

```lean
import ResponsibilityPathway.Basic
import ResponsibilityPathway.Lifecycle
import ResponsibilityPathway.Examples
import ResponsibilityPathway.Invariants
```

Boundary:

- `Core.lean` should remain a small public entry point.
- Existing documentation may continue to point to `Core.lean` while detailed definitions live in split modules.

## Split order

Recommended order:

1. Create `Basic.lean` and move node/model assumptions first.
2. Create `Lifecycle.lean` and move `Pathway` plus lifecycle predicates.
3. Create `Examples.lean` and move constructor-level example pathways.
4. Create `Invariants.lean` and move boundary predicates plus theorem candidates.
5. Reduce `Core.lean` to imports only.
6. Update `formal/lean/README.md` after the split is completed.

## Stop conditions

Stop before splitting if:

- imports cannot be checked locally or in CI
- theorem names need unnecessary churn
- module boundaries force non-minimal new abstractions
- the split would introduce claims beyond the current minimal model

Stop after splitting if:

- the existing six invariant candidates are preserved
- documentation still states the non-certifying boundary clearly
- `Core.lean` remains a stable import surface

## Non-goals

This split does not introduce:

- a complete responsibility ontology
- a production checker
- legal validity claims
- safety or compliance certification
- fairness certification
- moral accountability resolution
- artificial legal-personhood modeling
- institutional certification
- real-world deployment readiness

## Current recommendation

The next implementation step should be a mechanical split only.

Do not add new lifecycle states or new theorem families during the split. Preserve the current six invariant candidates first, then consider additional formalization work in a later commit.
