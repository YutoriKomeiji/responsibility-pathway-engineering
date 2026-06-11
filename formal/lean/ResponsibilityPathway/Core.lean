/-
Responsibility Pathway Engineering - Core Lean candidates

This file contains small structural formalization candidates.

Boundary:
A theorem in this file proves only the explicitly stated proposition under
its explicitly modeled assumptions. It does not prove real-world safety,
legal validity, compliance, fairness, moral accountability resolution,
production readiness, or institutional certification.
-/

namespace ResponsibilityPathway

/--
A minimal node kind for early structural invariants.

This is intentionally small. It is not a complete ontology of humans,
institutions, AI systems, organizations, workflows, or future artificial legal
personhood regimes.
-/
inductive NodeKind where
  | human
  | institution
  | ai
  deriving DecidableEq, Repr

/--
Explicit model assumptions for early Phase 2 invariants.

`artificialLegalPersonhoodEnabled = false` means this minimal RPE model does
not include a future legal or institutional layer that grants AI systems
personhood, legal capacity, assets, representation, enforceable duties, or
final responsibility capacity comparable to a legal person.

If such a layer is introduced in a future model, the invariants below must be
revisited rather than treated as universal claims.
-/
structure ModelAssumptions where
  artificialLegalPersonhoodEnabled : Bool
  deriving Repr

/--
Predicate: the current minimal model does not assume artificial legal
personhood for AI systems.
-/
def NoArtificialLegalPersonhood (assumptions : ModelAssumptions) : Prop :=
  assumptions.artificialLegalPersonhoodEnabled = false

/--
A node may participate in a pathway.

`canHoldFinalResponsibility` is modeled as an explicit structural field.
In the current minimal model, AI nodes are constrained only when artificial
legal personhood is not enabled.
-/
structure Node where
  id : String
  kind : NodeKind
  canHoldFinalResponsibility : Bool
  deriving Repr

/--
Predicate: a node is an AI node.
-/
def IsAI (node : Node) : Prop :=
  node.kind = NodeKind.ai

/--
Predicate: a node is a human or institutional node.
-/
def IsHumanOrInstitution (node : Node) : Prop :=
  node.kind = NodeKind.human ∨ node.kind = NodeKind.institution

/--
Predicate: a node is structurally allowed to hold final responsibility.
-/
def CanHoldFinalResponsibility (node : Node) : Prop :=
  node.canHoldFinalResponsibility = true

/--
Structural invariant under current minimal-model assumptions:
if no artificial legal personhood layer is assumed, AI nodes cannot hold final
responsibility in this model.

This is not a universal claim about future law, future institutions, or future
international agreements. It is a scoped model boundary.
-/
def AIResponsibilityBoundary
    (assumptions : ModelAssumptions)
    (node : Node) : Prop :=
  NoArtificialLegalPersonhood assumptions ->
    IsAI node ->
      ¬ CanHoldFinalResponsibility node

/--
A constructor-level current minimal assumption set.
-/
def currentMinimalAssumptions : ModelAssumptions :=
  {
    artificialLegalPersonhoodEnabled := false
  }

/--
A constructor-level safe AI node sets `canHoldFinalResponsibility` to false.
-/
def safeAINode (id : String) : Node :=
  {
    id := id,
    kind := NodeKind.ai,
    canHoldFinalResponsibility := false
  }

/--
The first Phase 2 invariant candidate, now explicitly scoped:
under current minimal assumptions, a node constructed as a safe AI node
satisfies the AI responsibility boundary.
-/
theorem safe_ai_node_cannot_hold_final_responsibility_under_current_assumptions
    (id : String) :
    AIResponsibilityBoundary currentMinimalAssumptions (safeAINode id) := by
  intro hNoPersonhood
  intro hAI
  unfold CanHoldFinalResponsibility
  simp [safeAINode]

/--
A human node may be modeled with final-responsibility capacity.
This is a structural permission, not a claim that any real-world human has
actually accepted legal or moral responsibility in a particular case.
-/
def humanResponsibilityNode (id : String) : Node :=
  {
    id := id,
    kind := NodeKind.human,
    canHoldFinalResponsibility := true
  }

/--
An institutional node may be modeled with final-responsibility capacity.
This is a structural permission inside the model, not a legal finding.
-/
def institutionalResponsibilityNode (id : String) : Node :=
  {
    id := id,
    kind := NodeKind.institution,
    canHoldFinalResponsibility := true
  }

/--
A human responsibility node is not an AI node.
-/
theorem human_responsibility_node_is_not_ai
    (id : String) :
    ¬ IsAI (humanResponsibilityNode id) := by
  unfold IsAI
  simp [humanResponsibilityNode]

/--
A minimal pathway model for early structural invariants.

This is intentionally not a complete graph model. It records only whether
AI participates, whether a human or institutional return point is present,
whether the pathway is declared repaired, whether a repair record is present,
whether the pathway is declared suspended, and whether review or return
conditions are preserved.
-/
structure Pathway where
  id : String
  aiParticipates : Bool
  hasHumanOrInstitutionalReturnPoint : Bool
  lifecycleRepaired : Bool
  hasRepairRecord : Bool
  lifecycleSuspended : Bool
  hasReviewOrReturnCondition : Bool
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
Structural invariant: if AI participates, the pathway must preserve a
human or institutional return point.

This remains useful even if future legal-personhood layers are modeled,
because returnability and auditability are separate from personhood status.
It is still only a structural returnability boundary, not a claim that the
pathway is safe, compliant, fair, legally valid, morally resolved, or
operationally complete.
-/
def AIReturnPointBoundary (pathway : Pathway) : Prop :=
  HasAIParticipation pathway -> HasHumanOrInstitutionalReturnPoint pathway

/--
Structural invariant: if a pathway is declared repaired, the minimal model
requires a repair record.

This does not mean real-world repair is complete, harm is eliminated,
legal liability is resolved, moral responsibility is resolved, or closure is
justified. It only requires structural traceability for the repaired state.
-/
def RepairRecordBoundary (pathway : Pathway) : Prop :=
  IsRepairedPathway pathway -> HasRepairRecord pathway

/--
Structural invariant: if a pathway is declared suspended, the minimal model
requires preserved review or return conditions.

This does not mean suspension is justified, safe, compliant, fair, legally
valid, morally resolved, or operationally complete. It only requires that a
suspended state does not erase the path back to review or return.
-/
def SuspensionReviewReturnBoundary (pathway : Pathway) : Prop :=
  IsSuspendedPathway pathway -> HasReviewOrReturnCondition pathway

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
    hasReviewOrReturnCondition := false
  }

/--
The second Phase 2 invariant candidate:
a safely constructed AI-assisted pathway satisfies the AI return-point boundary.
-/
theorem safe_ai_assisted_pathway_has_return_point
    (id : String) :
    AIReturnPointBoundary (safeAIAssistedPathway id) := by
  intro hAI
  unfold HasHumanOrInstitutionalReturnPoint
  simp [safeAIAssistedPathway]

/--
A pathway without AI participation does not require this AI-specific boundary.
This theorem only states the implication form of the boundary is satisfied
vacuously in the constructor-level non-AI case.
-/
def nonAIPathway (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := false,
    hasHumanOrInstitutionalReturnPoint := false,
    lifecycleRepaired := false,
    hasRepairRecord := false,
    lifecycleSuspended := false,
    hasReviewOrReturnCondition := false
  }

theorem non_ai_pathway_satisfies_ai_return_point_boundary
    (id : String) :
    AIReturnPointBoundary (nonAIPathway id) := by
  intro hAI
  unfold HasAIParticipation at hAI
  simp [nonAIPathway] at hAI

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
    hasReviewOrReturnCondition := false
  }

/--
The third Phase 2 invariant candidate:
a safely constructed repaired pathway satisfies the repair-record boundary.
-/
theorem repaired_pathway_has_repair_record
    (id : String) :
    RepairRecordBoundary (repairedPathwayWithRecord id) := by
  intro hRepaired
  unfold HasRepairRecord
  simp [repairedPathwayWithRecord]

/--
A pathway that is not declared repaired does not require a repair record under
this repair-specific boundary. This theorem only states the implication form
is satisfied vacuously in the constructor-level non-repaired case.
-/
theorem non_repaired_pathway_satisfies_repair_record_boundary
    (id : String) :
    RepairRecordBoundary (safeAIAssistedPathway id) := by
  intro hRepaired
  unfold IsRepairedPathway at hRepaired
  simp [safeAIAssistedPathway] at hRepaired

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
    hasReviewOrReturnCondition := true
  }

/--
The fourth Phase 2 invariant candidate:
a safely constructed suspended pathway satisfies the suspension review/return
boundary.
-/
theorem suspended_pathway_preserves_review_or_return_condition
    (id : String) :
    SuspensionReviewReturnBoundary (suspendedPathwayWithReviewOrReturn id) := by
  intro hSuspended
  unfold HasReviewOrReturnCondition
  simp [suspendedPathwayWithReviewOrReturn]

/--
A pathway that is not declared suspended does not require review or return
conditions under this suspension-specific boundary. This theorem only states
the implication form is satisfied vacuously in the constructor-level
non-suspended case.
-/
theorem non_suspended_pathway_satisfies_suspension_boundary
    (id : String) :
    SuspensionReviewReturnBoundary (safeAIAssistedPathway id) := by
  intro hSuspended
  unfold IsSuspendedPathway at hSuspended
  simp [safeAIAssistedPathway] at hSuspended

end ResponsibilityPathway
