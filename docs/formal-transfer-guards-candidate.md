# Transfer guard Lean candidate (design-time, not production enforcement)

This module introduces a **non-vacuous Boolean decision model** with independently supplied host claims: verified authority, verified delegation, receiver eligibility, evidence access, evidence freshness, and external-effect uncertainty.

`transferPermitted` returns true only with all five positive facts and no unknown effect. The Lean theorems include soundness of a true decision, blocking unknown effects, missing delegation, and stale evidence; concrete positive/negative decision witnesses are also compiled.

The model is intentionally *stricter* than classifying an unresolved route, and does not convert RPR/RPOS names into authority. It models facts as Boolean inputs; **it does not verify a signature, a wall clock, the provenance of claims, or the execution path of the current Python RPE gateway**. No claim of end-to-end RPE ↔ Lean refinement is made.

The immediate product value is to make the proposed routing-handoff gate explicit and falsifiable in Lean. Next evidence needed: a versioned schema/cross-language fixture demonstrating that Python's implementation uses the same decision function for concrete cases, including replay and restart, without editing the active M3 PR. Failure cases should remain observable, not hidden by extra implication-only proofs.

`Core.lean` imports this module so `lake build` compiles it. This is a draft PR candidate and must pass exact-head CI; it is not a merged or released RPE guarantee.
