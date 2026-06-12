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

end ResponsibilityPathway
