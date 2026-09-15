# Responsibility Routing engineering contract v0.1

Status: OPEN CONSTRUCTION / ENGINEERING CONTRACT DRAFT

This document translates recent RPR hardening into reusable RPE obligations without treating product-specific implementation details as universal requirements.

## Engineering invariant set

1. **Fail-closed is not automatically Human Gate.** A failure or uncertainty condition may resolve to hold, reconciliation, bounded continuation, deny, or Human Return depending on Authority and delegation.
2. **Human Return is a bounded route subtype.** Use it only when the next required decision genuinely belongs to a human or institution and the target is eligible to receive it.
3. **Evidence transfer does not grant Authority.** Moving logs, provenance, state, or evaluation output between components must not mutate Authority unless an explicit authorized transition says so.
4. **Capability does not imply receiver eligibility.** Eligibility must be established from Authority, delegation scope, evidence access, timing, role, and any other declared prerequisites.
5. **Route selection does not create Authority.** A router may select among already-valid routes; it must not manufacture a permission by selecting a destination.
6. **Recovered state does not recover approval.** Restart/checkpoint recovery must separately verify whether approval/resume Authority is still valid.
7. **Uncertain external effects remain unresolved.** A lost response after a potentially consequential write must not be silently converted into success, failure, or retry permission.

## Candidate route outcomes

Machine-readable implementations should be able to represent at least the semantic equivalents of:

- `CONTINUE_AUTONOMOUSLY`
- `AI_RESOLVE_WITHIN_DELEGATION`
- `HOLD_NEUTRAL`
- `HOLD_FOR_RECONCILIATION`
- `BOUNDED_HUMAN_RETURN`
- `STOP_AND_PRESERVE_RESIDUE`

Exact enum names may differ by product or schema. The semantic distinctions are the contract.

## Minimum handoff / route envelope

A route or handoff record should carry, where applicable:

- route identity;
- source holder;
- candidate receiver;
- required Authority class;
- delegation scope;
- receiver eligibility state and evidence;
- unresolved payload;
- external-effect uncertainty state;
- allowed next actions;
- forbidden next actions;
- reevaluation / readback condition;
- expiry / timing constraint;
- residual owner;
- evidence/provenance references;
- explicit marker that Authority was not inferred from evidence, capability, tool success, or state recovery.

## Assurance lifecycle contract

Engineering repositories and generated surfaces should distinguish:

- released/published artifact;
- current repository source;
- historical frozen evidence;
- migration records;
- authoring/control records.

Regression checks should prevent current-facing documentation from silently presenting historical/migration/control state as current. Frozen historical evidence must not be rewritten merely to match a newer product version.

## Validation discipline

- Exact-head evidence supports the exact evaluated head, not arbitrary later source.
- Post-merge/readback is required before declaring a transition closed where merge itself changes the evaluated surface.
- Cross-runtime probes are bounded compatibility evidence only for the tested boundary.
- Formal/kernel acceptance supports encoded invariants under stated assumptions; it does not establish real-world correctness, organizational Authority, legal validity, or deployment safety.

## Falsification boundary

If an existing host/application already preserves the same responsibility contract across ambiguous effects, readback, repair/resume, routing, restart, and Authority boundaries, an additional RP mechanism may provide little or no value. RPE should allow that result instead of forcing adoption.

## Compatibility principle

Existing Human Return / return-point schemas and examples should migrate additively. Do not destructively rename or erase working public interfaces before compatibility aliases, migration notes, and downstream consumers are understood.
