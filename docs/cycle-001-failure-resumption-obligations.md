<!--
Language: English
Document-Type: Engineering obligation note
Status: Candidate
-->

# RP-CYCLE-001 — Failure-to-resumption engineering obligations

This note captures the bounded engineering obligations returned by RPOS Cycle 001 and reviewed against existing Responsibility Pathway Runtime behavior.

It does not define legal responsibility, production authorization, compliance, organizational accountability, or blanket implementation correctness. It translates the Cycle 001 evidence into reusable engineering constraints for implementations that claim compatibility with this failure-to-resumption slice.

## Evidence classes

Cycle 001 combines distinct evidence classes that must not be substituted for one another:

- formal/model evidence can establish only properties of the formalized model and stated assumptions;
- executable tests can establish only the tested implementation behavior and environment;
- operational observation can establish only the observed external condition;
- evaluation, dependency, or supply-chain evidence can inform decisions but does not itself authorize execution or verify an external effect;
- a responsibility packet or completed document carries information but does not generate authority.

## Required engineering properties

### 1. Uncertain effect must remain explicit

An implementation MUST have an explicit representation for a dispatched or possibly dispatched action whose externally relevant effect has not been verified.

Layer-specific vocabulary may differ. RPOS uses `EFFECT_UNKNOWN`; RPR uses `write_status_unknown`. Compatibility requires preservation of the uncertainty semantics, not cosmetic state-name synchronization.

The implementation MUST NOT convert receipt, transport acknowledgement, local persistence, or executor return into verified completion unless the verification contract for that action is satisfied.

### 2. Receipt and verified effect are non-substitutable

A dispatch receipt or successful local result MUST NOT be treated as proof that the intended external effect occurred.

Completion requires evidence appropriate to the declared verification contract. If verification is absent, fails, or is itself uncertain, the pathway MUST remain unresolved or enter an explicit repair/reconciliation path.

### 3. Reconciliation must not silently redispatch

Reconciliation of an uncertain persisted attempt MUST be observation/classification work unless a separately authorized execution transition is created.

Restart recovery MUST preserve the prior attempt identity and MUST NOT treat process restart as permission to dispatch the same external mutation again.

### 4. Repair readiness is not restored authority

Repair completion MAY establish a `READY_TO_RESUME`-equivalent condition, but that condition MUST NOT itself grant execution authority.

Repair evidence answers whether the pathway is technically or operationally ready for reconsideration. It does not answer whether a new attempt is authorized.

### 5. Resume is an explicit authority-bearing transition

Resume MUST be represented as an explicit decision or operation governed by the configured resume authority.

An implementation MUST NOT encode resume as retry shorthand or infer it solely from successful repair.

The resume record SHOULD identify the repaired prior attempt and the authorized next attempt.

### 6. A resumed execution is a fresh attempt

A resumed mutation MUST use a distinct execution-attempt identity from the failed or uncertain prior attempt.

Idempotency relationships MAY link attempts at the operation level, but attempt identity MUST remain distinct so that evidence, failure, repair, and reconciliation histories remain auditable.

### 7. Human Return Point and Residual Owner must survive failure

The pathway definition or durable responsibility record MUST preserve a Human Return Point and Residual Owner across failure, uncertainty, repair, restart, and resumption.

Unresolved or non-reversible residual effects MUST remain assigned to an explicit residual owner. A system MUST NOT infer that responsibility disappears because execution stopped, a document was produced, or automation cannot proceed.

### 8. Evidence with no authority effect must remain state-neutral

Evaluation results, dependency evidence, supply-chain evidence, diagnostics, and prepared handoff packets MUST NOT change execution authority unless an explicit contract defines such a transition and the required authority performs it.

The default authority effect of informational evidence is none.

### 9. Path existence is not liveness

Demonstrating that a valid recovery path exists does not establish that an implementation, operator, or organization will eventually complete that path.

Tests and formal models MUST distinguish reachability/path-existence claims from liveness/eventual-completion claims.

## Anti-patterns

The following are incompatible with the Cycle 001 engineering interpretation:

- `receipt == effect`;
- `repair_complete == authorized`;
- `resume == retry`;
- reusing the failed attempt identity for a resumed execution;
- redispatching automatically after restart because the previous outcome is unknown;
- treating evaluator or dependency evidence as execution permission;
- treating a completed responsibility packet as authority transfer;
- dropping Residual Owner or Human Return Point when the pathway enters an unresolved state;
- presenting recovery reachability as proof of eventual completion.

## Minimum trace expectations

A compatible implementation SHOULD make the following relationships reconstructable from durable evidence:

1. pathway identity;
2. prior execution attempt identity;
3. uncertainty classification and reason;
4. observations used during reconciliation;
5. repair evidence and repair owner;
6. readiness state after repair;
7. explicit resume authority and decision;
8. fresh next-attempt identity;
9. verification evidence for the new attempt;
10. Residual Owner and Human Return Point if the pathway remains unresolved or aborts.

These relationships may be stored across multiple events or records; they do not need to be duplicated in every event if the owning durable record remains available and traceable.

## Counterexample-oriented acceptance criteria

At minimum, an implementation claiming this Cycle 001 behavior SHOULD demonstrate bounded tests showing that:

- an acknowledgement without verified effect does not complete the pathway;
- an uncertain attempt can survive restart without redispatch;
- unresolved reconciliation remains unresolved;
- verified-not-applied reconciliation enters an explicit repair path;
- repair completion alone cannot resume execution;
- an unauthorized resume is rejected;
- an authorized resume requires a fresh attempt identity;
- a resumed attempt can be verified independently of the prior failed attempt;
- unresolved residuals cannot be closed by an actor other than the Residual Owner;
- informational evidence cannot silently change authority state.

## Current cross-layer evidence

RPOS Cycle 001 supplied bounded Lean and Python evidence for uncertainty, repair, readiness, explicit resume, fresh attempt, reconciliation, evidence-class separation, and authority-neutral responsibility packets.

RPR Cycle 001 reviewed the existing public runtime and found equivalent bounded executable behavior already present, including restart/reconciliation and repair/explicit-resume/fresh-attempt paths. RPR therefore closed its Cycle 001 receiving issue as `reviewed-no-code-change-required` rather than adding redundant runtime behavior.

This engineering note is the RPE receiving artifact for those findings. Future RPE or RPR changes should preserve these obligations unless a later cycle explicitly revises them with new evidence and review.
