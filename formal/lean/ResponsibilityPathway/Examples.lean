/-
Responsibility Pathway Engineering - constructor-level examples

Boundary:
These examples are model witnesses for early structural Lean candidates. They
are not real-world certification artifacts and do not claim legal validity,
safety, compliance, fairness, moral accountability resolution, production
readiness, or institutional certification.
-/

import ResponsibilityPathway.Lifecycle

namespace ResponsibilityPathway

/--
A constructor-level safe AI-assisted pathway includes a human or institutional
return point.
-/
def safeAIAssistedPathway (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := true,
    hasHumanOrInstitutionalReturnPoint := true,
    lifecycleRepaired := false,
    hasRepairRecord := false,
    lifecycleSuspended := false,
    hasReviewOrReturnCondition := false,
    lifecycleReturning := false,
    automaticContinuationAllowed := false,
    lifecycleClosed := false,
    hasEvidenceRecord := false,
    hasReopeningCondition := false
  }

/--
A pathway without AI participation does not require the AI-specific return-point
boundary.
-/
def nonAIPathway (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := false,
    hasHumanOrInstitutionalReturnPoint := false,
    lifecycleRepaired := false,
    hasRepairRecord := false,
    lifecycleSuspended := false,
    hasReviewOrReturnCondition := false,
    lifecycleReturning := false,
    automaticContinuationAllowed := false,
    lifecycleClosed := false,
    hasEvidenceRecord := false,
    hasReopeningCondition := false
  }

/--
A constructor-level repaired pathway includes a repair record.
-/
def repairedPathwayWithRecord (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := true,
    hasHumanOrInstitutionalReturnPoint := true,
    lifecycleRepaired := true,
    hasRepairRecord := true,
    lifecycleSuspended := false,
    hasReviewOrReturnCondition := false,
    lifecycleReturning := false,
    automaticContinuationAllowed := false,
    lifecycleClosed := false,
    hasEvidenceRecord := false,
    hasReopeningCondition := false
  }

/--
A constructor-level suspended pathway preserves review or return conditions.
-/
def suspendedPathwayWithReviewOrReturn (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := true,
    hasHumanOrInstitutionalReturnPoint := true,
    lifecycleRepaired := false,
    hasRepairRecord := false,
    lifecycleSuspended := true,
    hasReviewOrReturnCondition := true,
    lifecycleReturning := false,
    automaticContinuationAllowed := false,
    lifecycleClosed := false,
    hasEvidenceRecord := false,
    hasReopeningCondition := false
  }

/--
A constructor-level returning pathway does not allow automatic continuation.
-/
def returningPathwayWithoutAutomaticContinuation (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := true,
    hasHumanOrInstitutionalReturnPoint := true,
    lifecycleRepaired := false,
    hasRepairRecord := false,
    lifecycleSuspended := false,
    hasReviewOrReturnCondition := true,
    lifecycleReturning := true,
    automaticContinuationAllowed := false,
    lifecycleClosed := false,
    hasEvidenceRecord := false,
    hasReopeningCondition := false
  }

/--
A constructor-level closed pathway preserves evidence records and reopening
conditions.
-/
def closedPathwayWithEvidenceAndReopening (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := true,
    hasHumanOrInstitutionalReturnPoint := true,
    lifecycleRepaired := false,
    hasRepairRecord := false,
    lifecycleSuspended := false,
    hasReviewOrReturnCondition := false,
    lifecycleReturning := false,
    automaticContinuationAllowed := false,
    lifecycleClosed := true,
    hasEvidenceRecord := true,
    hasReopeningCondition := true
  }

/--
The safe AI-assisted example has AI participation by construction.
-/
theorem safe_ai_assisted_pathway_has_ai_participation
    (id : String) :
    HasAIParticipation (safeAIAssistedPathway id) := by
  unfold HasAIParticipation
  simp [safeAIAssistedPathway]

/--
The safe AI-assisted example has a human or institutional return point by
construction.
-/
theorem safe_ai_assisted_pathway_has_human_or_institutional_return_point
    (id : String) :
    HasHumanOrInstitutionalReturnPoint (safeAIAssistedPathway id) := by
  unfold HasHumanOrInstitutionalReturnPoint
  simp [safeAIAssistedPathway]

/--
The non-AI example has no AI participation by construction.
-/
theorem non_ai_pathway_has_no_ai_participation
    (id : String) :
    ¬ HasAIParticipation (nonAIPathway id) := by
  unfold HasAIParticipation
  simp [nonAIPathway]

/--
The repaired example is repaired and has a repair record by construction.
-/
theorem repaired_pathway_example_is_repaired_and_has_record
    (id : String) :
    IsRepairedPathway (repairedPathwayWithRecord id) ∧
      HasRepairRecord (repairedPathwayWithRecord id) := by
  constructor
  · unfold IsRepairedPathway
    simp [repairedPathwayWithRecord]
  · unfold HasRepairRecord
    simp [repairedPathwayWithRecord]

/--
The suspended example is suspended and preserves review or return conditions by
construction.
-/
theorem suspended_pathway_example_is_suspended_and_has_review_or_return
    (id : String) :
    IsSuspendedPathway (suspendedPathwayWithReviewOrReturn id) ∧
      HasReviewOrReturnCondition (suspendedPathwayWithReviewOrReturn id) := by
  constructor
  · unfold IsSuspendedPathway
    simp [suspendedPathwayWithReviewOrReturn]
  · unfold HasReviewOrReturnCondition
    simp [suspendedPathwayWithReviewOrReturn]

/--
The returning example is returning and does not allow automatic continuation by
construction.
-/
theorem returning_pathway_example_is_returning_without_automatic_continuation
    (id : String) :
    IsReturningPathway (returningPathwayWithoutAutomaticContinuation id) ∧
      ¬ AllowsAutomaticContinuation (returningPathwayWithoutAutomaticContinuation id) := by
  constructor
  · unfold IsReturningPathway
    simp [returningPathwayWithoutAutomaticContinuation]
  · unfold AllowsAutomaticContinuation
    simp [returningPathwayWithoutAutomaticContinuation]

/--
The closed example is closed and preserves evidence and reopening conditions by
construction.
-/
theorem closed_pathway_example_is_closed_with_evidence_and_reopening
    (id : String) :
    IsClosedPathway (closedPathwayWithEvidenceAndReopening id) ∧
      HasEvidenceRecord (closedPathwayWithEvidenceAndReopening id) ∧
        HasReopeningCondition (closedPathwayWithEvidenceAndReopening id) := by
  constructor
  · unfold IsClosedPathway
    simp [closedPathwayWithEvidenceAndReopening]
  · constructor
    · unfold HasEvidenceRecord
      simp [closedPathwayWithEvidenceAndReopening]
    · unfold HasReopeningCondition
      simp [closedPathwayWithEvidenceAndReopening]

end ResponsibilityPathway
