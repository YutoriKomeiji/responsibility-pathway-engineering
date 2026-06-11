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
institutions, AI systems, organizations, or workflows.
-/
inductive NodeKind where
  | human
  | institution
  | ai
  deriving DecidableEq, Repr

/--
A node may participate in a pathway.

`canHoldFinalResponsibility` is modeled as an explicit structural field.
The first invariant below constrains this field for AI nodes.
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
Structural invariant: AI nodes cannot hold final responsibility.

This is a model assumption for Responsibility Pathway Engineering.
It does not make a legal, moral, safety, compliance, or production claim.
-/
def AIResponsibilityBoundary (node : Node) : Prop :=
  IsAI node -> ¬ CanHoldFinalResponsibility node

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
The first Phase 2 invariant candidate:
a node constructed as a safe AI node satisfies the AI responsibility boundary.
-/
theorem safe_ai_node_cannot_hold_final_responsibility
    (id : String) :
    AIResponsibilityBoundary (safeAINode id) := by
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
AI participates and whether a human or institutional return point is present.
-/
structure Pathway where
  id : String
  aiParticipates : Bool
  hasHumanOrInstitutionalReturnPoint : Bool
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
Structural invariant: if AI participates, the pathway must preserve a
human or institutional return point.

This is a structural returnability boundary, not a claim that the pathway is
safe, compliant, fair, legally valid, morally resolved, or operationally complete.
-/
def AIReturnPointBoundary (pathway : Pathway) : Prop :=
  HasAIParticipation pathway -> HasHumanOrInstitutionalReturnPoint pathway

/--
A constructor-level safe AI-assisted pathway includes a human or institutional
return point.
-/
def safeAIAssistedPathway (id : String) : Pathway :=
  {
    id := id,
    aiParticipates := true,
    hasHumanOrInstitutionalReturnPoint := true
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
    hasHumanOrInstitutionalReturnPoint := false
  }

theorem non_ai_pathway_satisfies_ai_return_point_boundary
    (id : String) :
    AIReturnPointBoundary (nonAIPathway id) := by
  intro hAI
  unfold HasAIParticipation at hAI
  simp [nonAIPathway] at hAI

end ResponsibilityPathway
