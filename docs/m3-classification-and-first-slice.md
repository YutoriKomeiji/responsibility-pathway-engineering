# RPE M3 — classification and first vertical slice

Status: **M3 working branch / non-canonical until reviewed and merged**  
Owner: Linear `DAN-65`

M2 remains the public governed-integration baseline. M3 is additive and must not silently turn RPE into an executor, router, or durable runtime.

## First vertical slice

```text
existing M2 governed evaluation result
        ↓
M3 transition evaluation
        ↓
control action + route descriptor + constraints + unmet conditions
        ↓
separate executor / runtime / institution
```

### Adopt now

- generalized responsibility route-target vocabulary;
- additive adaptive-control vocabulary;
- pure `evaluate_transition()` transformation over an existing RPE result;
- explicit `authority_effect: none` and `execution_effect: none`;
- deterministic fail-closed handling for invalid route targets and unsupported decisions;
- evidence-missing handling through `require_evidence`;
- deterministic checker and CI;
- downstream executor ownership remains explicit.

### Research / prototype

- Risk Condition Graph / contextual exposure;
- autonomy envelopes and cumulative budgets;
- trust/responsibility taint propagation;
- relationship/path integrity;
- goal/incentive boundary;
- execution-configuration identity;
- Human Gate quality;
- least-restrictive-route optimization.

No novelty claim is made for these concepts at this stage.

### Assign elsewhere

- authority grant/delegation/expiry/revocation/resume authority → `DAN-9`;
- long-horizon trajectory invariants → `DAN-28`;
- durable dispatch/effect/retry/reconciliation/repair/resume state → RPR / RPOS;
- legal/organizational authority → integrating institution.

### Defer

Observability/NFR targets, framework adapters, full Thin/Governed/Assured packaging, and collective multi-agent controls follow after the gateway contract is stable enough to measure.

### Reject for RPE itself

RPE must not become the external-action executor, a durable workflow engine, a source of legal authority, an external-effect verifier by assertion, or a stateful retry/recovery runtime.

## First-slice rules

1. `allow` with no requested route → `allow`.
2. `allow` with a valid requested route → `route`.
3. `human_gate` with missing evidence → `require_evidence`.
4. other `human_gate` outcomes → `handoff`.
5. `deny` → `deny`.
6. `hold` → `hold`.
7. unsupported decisions → fail closed as `hold`.
8. invalid route targets → fail closed as `hold`.

Every experimental result must preserve:

```text
authority_effect = none
execution_effect = none
downstream_executor_required = true
```

A route descriptor is metadata about a responsibility transition. It is not a dispatch instruction.
