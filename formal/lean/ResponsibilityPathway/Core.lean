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
A human responsibility node is not an AI node.
-/
theorem human_responsibility_node_is_not_ai
    (id : String) :
    ¬ IsAI (humanResponsibilityNode id) := by
  unfold IsAI
  simp [humanResponsibilityNode]

end ResponsibilityPathway
