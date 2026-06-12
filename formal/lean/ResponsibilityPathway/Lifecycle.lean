/-
Responsibility Pathway Engineering - minimal lifecycle model

Boundary:
This file defines only a minimal structural lifecycle model for early Phase 2
Lean candidates. It does not claim operational completeness, legal validity,
safety, compliance, fairness, moral accountability resolution, production
readiness, or institutional certification.
-/

import ResponsibilityPathway.Basic

namespace ResponsibilityPathway

/--
A minimal pathway model for early structural invariants.

This is intentionally not a complete graph model. It records only whether
AI participates, whether a human or institutional return point is present,
whether the pathway is declared repaired, whether a repair record is present,
whether the pathway is declared suspended, whether review or return conditions
are preserved, whether the pathway is declared returning, whether automatic
continuation is allowed, whether the pathway is declared closed, whether
evidence is preserved, and whether reopening conditions are preserved.
-/
structure Pathway where
  id : String
  aiParticipates : Bool
  hasHumanOrInstitutionalReturnPoint : Bool
  lifecycleRepaired : Bool
  hasRepairRecord : Bool
  lifecycleSuspended : Bool
  hasReviewOrReturnCondition : Bool
  lifecycleReturning : Bool
  automaticContinuationAllowed : Bool
  lifecycleClosed : Bool
  hasEvidenceRecord : Bool
  hasReopeningCondition : Bool
  deriving Repr

/--
Predicate: AI participates in the pathway.
-/
def HasAIParticipation (pathway : Pathway) : Prop :=
  pathway.aiParticipates = true

/--
Predicate: the pathway has a human or institutional return point.
-/
def HasHumanOrInstitutionalReturnPoint (pathway : Pathway) : Prop :=
  pathway.hasHumanOrInstitutionalReturnPoint = true

/--
Predicate: the pathway is declared as repaired inside the minimal model.
-/
def IsRepairedPathway (pathway : Pathway) : Prop :=
  pathway.lifecycleRepaired = true

/--
Predicate: the pathway references at least one repair record inside the
minimal model.
-/
def HasRepairRecord (pathway : Pathway) : Prop :=
  pathway.hasRepairRecord = true

/--
Predicate: the pathway is declared as suspended inside the minimal model.
-/
def IsSuspendedPathway (pathway : Pathway) : Prop :=
  pathway.lifecycleSuspended = true

/--
Predicate: the pathway preserves at least one review or return condition inside
the minimal model.
-/
def HasReviewOrReturnCondition (pathway : Pathway) : Prop :=
  pathway.hasReviewOrReturnCondition = true

/--
Predicate: the pathway is declared as returning inside the minimal model.
-/
def IsReturningPathway (pathway : Pathway) : Prop :=
  pathway.lifecycleReturning = true

/--
Predicate: the pathway allows automatic continuation inside the minimal model.
-/
def AllowsAutomaticContinuation (pathway : Pathway) : Prop :=
  pathway.automaticContinuationAllowed = true

/--
Predicate: the pathway is declared as closed inside the minimal model.
-/
def IsClosedPathway (pathway : Pathway) : Prop :=
  pathway.lifecycleClosed = true

/--
Predicate: the pathway preserves evidence records inside the minimal model.
-/
def HasEvidenceRecord (pathway : Pathway) : Prop :=
  pathway.hasEvidenceRecord = true

/--
Predicate: the pathway preserves reopening conditions inside the minimal model.
-/
def HasReopeningCondition (pathway : Pathway) : Prop :=
  pathway.hasReopeningCondition = true

end ResponsibilityPathway
