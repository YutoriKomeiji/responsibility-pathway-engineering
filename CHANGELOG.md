# CHANGELOG

This changelog records conceptual milestones rather than individual code edits.

## 2026-06

### ROADMAP synchronized with Lean theorem index

- ROADMAP now records constructor-level sanity theorem coverage for Basic and Examples modules
- ROADMAP now references `docs/phase-2-lean-theorem-index.md` as the theorem-role guide before further theorem expansion
- Next low-risk Phase 2 work now includes using the theorem-role index before adding or renaming Lean theorem candidates

### BEACON synchronized with Lean theorem index

- BEACON now records `docs/phase-2-lean-theorem-index.md` as part of the Phase 2 Lean reconnection path
- Current Focus now says to use the theorem-role index before adding or renaming Lean theorem candidates
- Restart Point now includes theorem-role stability as a condition before adding further theorem candidates

### Lean theorem index linked from README files

- README and README.ja now include `docs/phase-2-lean-theorem-index.md` in the Phase 2 Lean reader path
- `formal/lean/README.md` now links to the theorem-role index near the split-plan link
- This completes the previously deferred README synchronization for the theorem index

### Phase 2 Lean theorem index added

- `docs/phase-2-lean-theorem-index.md` added as a navigation aid for current Lean theorem roles
- The index groups Basic constructor sanity theorems, Example lifecycle sanity theorems, boundary predicates, positive invariant theorem candidates, and vacuity/non-trigger theorem candidates
- The index adds no new formal claims and remains non-certifying

### Phase 2 example lifecycle sanity theorems added

- `formal/lean/ResponsibilityPathway/Examples.lean` updated with constructor-level sanity theorems for lifecycle examples
- Added checks for AI participation and return-point fields in the safe AI-assisted example
- Added checks for non-AI participation, repaired/record, suspended/review-or-return, returning/no-automatic-continuation, and closed/evidence/reopening constructor examples
- These are structural model facts only; they do not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Phase 2 basic node sanity theorems added

- `formal/lean/ResponsibilityPathway/Basic.lean` updated with constructor-level sanity theorems for basic node definitions
- Added theorem candidates showing that a safe AI node is an AI node and cannot hold final responsibility by construction
- Added theorem candidates showing that human and institutional responsibility nodes can hold final responsibility by construction
- These are structural model facts only; they do not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Lean workflow generates Lake manifest before build

- `.github/workflows/check-lean.yml` updated after the first workflow attempt reported `No lake-manifest.json found`
- The workflow now installs Elan directly, prints Lean/Lake versions, runs `lake update`, and then runs `lake build`
- This avoids requiring a precommitted `lake-manifest.json` for the current dependency-free minimal Lean package

### Lean workflow inputs made explicit

- `.github/workflows/check-lean.yml` updated to use explicit `leanprover/lean-action@v1` inputs
- `auto-config` is set to `false`
- `build`, `test`, `lint`, and `use-mathlib-cache` are set explicitly as string inputs
- This keeps the minimal Lean CI focused on `lake build` only

### Phase 2 minimal Lean build path added

- `lean-toolchain` added and pinned to `leanprover/lean4:v4.30.0`
- `lakefile.lean` added as a minimal Lake package using `formal/lean` as the Lean source directory
- `.github/workflows/check-lean.yml` added as a minimal Lean build workflow using `leanprover/lean-action@v1`
- README, README.ja, ROADMAP, BEACON, and `formal/lean/README.md` updated to reflect the minimal Lean build path
- The workflow checks only the Lean package build; it does not certify legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Phase 2 Lean core split documented across entry files

- README and README.ja now state that the Phase 2 Lean spine is split into small modules while `Core.lean` remains the stable entry point
- ROADMAP now records the Lean core split as completed and lists minimal Lean toolchain/build verification as the next low-risk Phase 2 work
- BEACON now records the split module layout, the current restart point, and the fact that Lean build verification is not yet established
- Current GitHub Actions automation remains limited to the bounded Python example checker

### Phase 2 Lean core split into small modules

- `formal/lean/ResponsibilityPathway/Core.lean` reduced to a stable import entry point
- New split modules added: `Basic.lean`, `Lifecycle.lean`, `Examples.lean`, and `Invariants.lean`
- The existing six Phase 2 invariant candidates were preserved while separating model primitives, lifecycle predicates, constructor examples, and theorem candidates
- `docs/phase-2-lean-split-plan.md` records the split rationale, order, stop conditions, and non-goals
- `formal/lean/README.md` updated to describe the split module layout
- No new legal, safety, compliance, fairness, moral accountability, certification, or production-readiness claims were introduced

### Phase 2 minimal Lean lifecycle invariant set introduced

- `formal/lean/ResponsibilityPathway/Core.lean` now contains a minimal node/pathway model and six scoped lifecycle-invariant candidates
- The current invariant set covers AI final-responsibility boundary, AI return-point boundary, repair-record boundary, suspension review/return boundary, returning no-automatic-continuation boundary, and closure evidence/reopening boundary
- The AI final-responsibility boundary is explicitly assumption-scoped to the current minimal model where no artificial legal-personhood layer is assumed
- Future legal, institutional, national, international, or user/provider-agreement personhood layers remain open for explicit modeling rather than silent assumption
- README, README.ja, ROADMAP, and BEACON updated to reflect the current Phase 2 Lean status
- The formalization remains structural, assumption-bound, and non-certifying; it does not claim legal validity, safety, compliance, fairness, moral accountability resolution, institutional certification, or production readiness

### Phase 2 closure evidence-reopening invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with closed-pathway structural fields
- `IsClosedPathway`, `HasEvidenceRecord`, `HasReopeningCondition`, and `ClosureEvidenceReopeningBoundary` predicates added
- Sixth invariant candidate added: a safely constructed closed pathway preserves evidence and reopening-condition records
- Non-closed pathway implication case added to show the closure-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current closure evidence/reopening invariant candidate and boundary note

### Phase 2 returning no-automatic-continuation invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with returning-pathway structural fields
- `IsReturningPathway`, `AllowsAutomaticContinuation`, and `ReturningNoAutomaticContinuationBoundary` predicates added
- Fifth invariant candidate added: a safely constructed returning pathway does not allow automatic continuation
- Non-returning pathway implication case added to show the returning-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current returning no-automatic-continuation invariant candidate and boundary note

### Phase 2 suspension review-return invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with suspended-pathway structural fields
- `IsSuspendedPathway`, `HasReviewOrReturnCondition`, and `SuspensionReviewReturnBoundary` predicates added
- Fourth invariant candidate added: a safely constructed suspended pathway preserves review or return conditions
- Non-suspended pathway implication case added to show the suspension-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current suspension review/return invariant candidate and boundary note

### Phase 2 repair-record invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with repaired-pathway structural fields
- `IsRepairedPathway`, `HasRepairRecord`, and `RepairRecordBoundary` predicates added
- Third invariant candidate added: a safely constructed repaired pathway has a repair record
- Non-repaired pathway implication case added to show the repair-specific boundary is not over-applied
- `formal/lean/README.md` updated with the current repair-record invariant candidate and boundary note

### Phase 2 AI responsibility invariant assumption boundary clarified

- `formal/lean/ResponsibilityPathway/Core.lean` updated with `ModelAssumptions` and `NoArtificialLegalPersonhood`
- The AI final-responsibility invariant is now scoped to the current minimal model where no artificial legal-personhood layer is assumed
- The theorem name was updated to `safe_ai_node_cannot_hold_final_responsibility_under_current_assumptions`
- The formalization now explicitly leaves room for future legal, institutional, national, international, or user/provider-agreement models that may introduce artificial legal-personhood layers
- `formal/lean/README.md` updated to clarify that the invariant is not a universal claim about all possible future legal or institutional regimes

### Phase 2 AI return-point invariant established

- `formal/lean/ResponsibilityPathway/Core.lean` updated with a minimal `Pathway` model
- `HasAIParticipation`, `HasHumanOrInstitutionalReturnPoint`, and `AIReturnPointBoundary` predicates added
- Second invariant candidate added: a safely constructed AI-assisted pathway has a human or institutional return point
