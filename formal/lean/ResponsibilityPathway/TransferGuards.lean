/-
A bounded, executable decision model for responsibility transfer.
Model inputs are claims from an external verifier, not proof that external
credentials, delegation or timestamps are genuine.
-/
namespace ResponsibilityPathway

structure TransferFacts where
  authorityVerified : Bool
  delegationVerified : Bool
  receiverEligible : Bool
  evidenceAccessible : Bool
  evidenceCurrent : Bool
  effectUnknown : Bool
  deriving Repr, DecidableEq

/-- A transfer is permitted only if every positive fact is established and
    the external effect is not unknown. No Authority is granted by this model. -/
def transferPermitted (f : TransferFacts) : Bool :=
  f.authorityVerified &&
  f.delegationVerified &&
  f.receiverEligible &&
  f.evidenceAccessible &&
  f.evidenceCurrent &&
  !f.effectUnknown

/-- A true decision entails the complete modeled guard conjunction. -/
theorem transfer_sound (f : TransferFacts) (h : transferPermitted f = true) :
    f.authorityVerified = true ∧
    f.delegationVerified = true ∧
    f.receiverEligible = true ∧
    f.evidenceAccessible = true ∧
    f.evidenceCurrent = true ∧
    f.effectUnknown = false := by
  cases f with
  | mk a d r e c u =>
    cases a <;> cases d <;> cases r <;> cases e <;> cases c <;> cases u <;>
      simp_all [transferPermitted]

/-- Unknown external effects cannot be promoted to transfer permission. -/
theorem unknown_effect_blocks_transfer (f : TransferFacts)
    (h : f.effectUnknown = true) : transferPermitted f = false := by
  simp [transferPermitted, h]

/-- Expired evidence blocks transfer even if other checks are positive. -/
theorem stale_evidence_blocks_transfer (f : TransferFacts)
    (h : f.evidenceCurrent = false) : transferPermitted f = false := by
  simp [transferPermitted, h]

/-- Lack of delegation blocks transfer regardless of receiver capability. -/
theorem missing_delegation_blocks_transfer (f : TransferFacts)
    (h : f.delegationVerified = false) : transferPermitted f = false := by
  simp [transferPermitted, h]

/-- Positive and negative concrete witnesses to avoid purely vacuous claims. -/
example : transferPermitted ⟨true, true, true, true, true, false⟩ = true := by decide
example : transferPermitted ⟨true, true, true, true, true, true⟩ = false := by decide
example : transferPermitted ⟨true, false, true, true, true, false⟩ = false := by decide

end ResponsibilityPathway
