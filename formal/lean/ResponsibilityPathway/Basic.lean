/-
Responsibility Pathway Engineering - basic model primitives

Boundary:
This file defines only minimal structural primitives for early Phase 2 Lean
candidates. It is not a complete ontology of humans, institutions, AI systems,
organizations, workflows, or future artificial legal personhood regimes.
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
A safe AI node is structurally an AI node.
-/
theorem safe_ai_node_is_ai
    (id : String) :
    IsAI (safeAINode id) := by
  unfold IsAI
  simp [safeAINode]

/--
A safe AI node cannot hold final responsibility by construction.
This is a constructor-level sanity theorem, not a real-world legal claim.
-/
theorem safe_ai_node_cannot_hold_final_responsibility
    (id : String) :
    ¬ CanHoldFinalResponsibility (safeAINode id) := by
  unfold CanHoldFinalResponsibility
  simp [safeAINode]

/--
A human responsibility node has final-responsibility capacity by construction.
This is a structural model fact, not a finding that responsibility was actually
accepted in a real-world case.
-/
theorem human_responsibility_node_can_hold_final_responsibility
    (id : String) :
    CanHoldFinalResponsibility (humanResponsibilityNode id) := by
  unfold CanHoldFinalResponsibility
  simp [humanResponsibilityNode]

/--
An institutional responsibility node has final-responsibility capacity by
construction. This is a structural model fact, not a legal finding.
-/
theorem institutional_responsibility_node_can_hold_final_responsibility
    (id : String) :
    CanHoldFinalResponsibility (institutionalResponsibilityNode id) := by
  unfold CanHoldFinalResponsibility
  simp [institutionalResponsibilityNode]

/--
A human responsibility node is not an AI node.
-/
theorem human_responsibility_node_is_not_ai
    (id : String) :
    ¬ IsAI (humanResponsibilityNode id) := by
  unfold IsAI
  simp [humanResponsibilityNode]

end ResponsibilityPathway
