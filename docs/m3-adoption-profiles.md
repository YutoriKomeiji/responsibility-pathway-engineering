# RPE M3 Adoption Profiles — Experimental

Status: experimental M3 design/implementation contract. This document does not change the closed M2 public claim baseline.

## Why profiles exist

RPE should not require every adopter to integrate the entire Responsibility Pathway stack before receiving useful evaluation behavior. The adoption surface is therefore divided by **evidence and governance burden**, not by marketing tier.

All profiles preserve the same hard boundary:

- RPE evaluates; it does not dispatch the external action.
- RPE does not create legal or organizational authority.
- `authority_effect` remains `none`.
- `execution_effect` remains `none`.
- downstream authority/executor ownership remains explicit.
- a more advanced profile does not convert evaluation evidence into external-effect evidence.

## Thin

Use when the immediate need is to place one bounded responsibility gateway before an existing executor without rewriting the workflow around RPE.

Current experimental surface:

```python
from rpe_kernel import evaluate_gateway_request

result = evaluate_gateway_request(payload)
```

Equivalent reference adapters are being kept aligned across Python, REST, and MCP.

Required integration shape:

```text
existing proposal
  -> one RPE gateway evaluation
  -> control / transition metadata
  -> existing downstream authority + executor
```

Thin may include:

- the strict governed M2 envelope;
- optional declarative risk conditions;
- optional bounded constraints;
- optional descriptive route target;
- one machine-readable transition result.

Thin does **not** mean weak authority semantics. It means minimal integration topology.

## Governed

Use when Requirement Packs, governance records, applicability, compatibility, and source/pack binding must be checked before the M3 transition is derived.

The M3 one-call gateway always preserves the strict M2 governed evaluation as its baseline. M3 controls may narrow an M2 `allow`; they do not override M2 `human_gate`, `hold`, or `deny` into permission.

Governed adds reviewable inputs such as:

- admitted Requirement Packs;
- governance eligibility;
- pack/governance identity binding;
- applicability resolution;
- evidence requirements;
- Risk Condition Graph nodes and dependencies;
- explicit responsibility transition metadata.

## Assured

Assured is **not yet a completed M3 implementation profile**. It is the target profile for environments that require stronger review evidence around the same evaluation contract.

Candidate additional obligations include:

- independently reviewable provenance and evidence bindings;
- an explicit pre-action evidence fragment that downstream runtime layers can bind into a broader Responsibility Pathway Evidence Package;
- Security Context inputs with clear evidence ownership and no implicit authentication/Authority claim;
- contract/schema readback across every exposed adapter;
- deterministic negative/adversarial fixtures;
- stronger configuration identity and change detection;
- bounded formal assertions where the model and proof ceiling are explicit;
- environment-specific performance/reliability evidence;
- explicit reopening conditions when evidence, configuration, authority, or dependencies change.

Assured must not be interpreted as certification, production authorization, legal compliance, or proof of arbitrary external effects. RPE's Assured profile remains pre-action/evaluation scoped: downstream dispatch, effect verification, reconciliation, repair, resume, durable trajectory state, and final assurance-artifact assembly remain outside this layer.

## Profile promotion rule

A caller should move to a stronger profile because its **required evidence or governance obligations increased**, not because a package version number changed.

Conceptually:

```text
Thin
  + governance/source binding requirements
  -> Governed

Governed
  + stronger independent assurance obligations
  -> Assured
```

No profile silently inherits authority from another profile.

## Adapter rule

Python, REST, MCP, and future framework adapters should expose the same semantic boundary. Adapter convenience must not create a stronger authority or execution claim than the underlying gateway result.

A framework adapter is justified only when it reduces measured integration burden while preserving:

- the M2 governed baseline;
- M3 risk/control semantics;
- responsibility-transition metadata;
- fail-closed handling of unsupported/ambiguous inputs;
- downstream executor and authority ownership.

## Current implementation mapping

| Profile | Current branch evidence | Status |
|---|---|---|
| Thin | `evaluate_gateway_request`, `/v1/evaluate/transition`, MCP transition evaluation tool | implemented experimentally |
| Governed | strict M2 governed envelope + optional M3 risk graph / route / constraints | implemented experimentally |
| Assured | schema checks and adversarial continuity exist, but the full profile obligations are not closed | research / incremental implementation |

The table reports repository-level implementation state only. It does not establish production suitability or real-world risk reduction.


The [M3 integration/operator guide](m3-integration-operator-guide.md) offers a single first-use path from install through Python/REST/MCP I/O, host-side enforcement, failure semantics and evidence-limited expectations. This document retains ownership of the Thin/Governed/Assured profiles.

Quick first run on the experimental M3 Draft: `python scripts/try_m3.py` (or `--json` for a compact machine-readable outcome). This reuses the cross-surface and host-enforcement tests without granting execution authority or producing a real external effect.

## Reproduce the exact I/O across Python, REST and MCP

M3 guarded contract version: `0.2.0-exp`. The same evaluation request
can travel through any of the three installed reference surfaces:

```text
Caller policy + governed envelope + optional risk/guard conditions
  ├─ Python: evaluate_guarded_adapter_request(request)
  ├─ REST: POST /v1/evaluate/transition/guarded (application/json)
  └─ MCP stdio: tools/call rpe_evaluate_guarded_responsibility_transition
      → evaluation_result + guard_observations + risk_condition_result
        + transition_result + authority_effect:none + execution_effect:none
```

The following script **actually exercises all three I/O paths**, starting
a temporary loopback REST server and sending JSON-RPC through the MCP stdio
message handler. It asserts complete JSON-result equality for four inputs:

```bash
python scripts/demo_m3_cross_surface.py
python scripts/demo_m3_cross_surface.py --json
```

| Caller-supplied condition | Expected M3 action | Separate host obligation |
|---|---|---|
| Required approval present, no risk flag | `allow` | independently authorize and, if permitted, invoke an executor |
| Approval evidence absent | not `allow` | obtain/review missing evidence; no dispatch |
| Upstream mismatch observation triggered | `require_authority` | perform independent authority verification |
| Caller risk graph contains unknown field | `hold` | repair input; do not silently strip the field |

Machine-readable output includes the exact input, M2 decision, M3 control,
reason codes, unmet conditions and responsibility/effect boundary for each
case. The accepted evaluation response is **never itself authority** to run
an external tool. Authenticating evidence, enforcing decisions before
execution, retry controls, operational reliability, effect verification and
data residency remain responsibilities of the integrating host.

This demonstration uses a synthetic Requirement Pack and loopback transport
only; it measures adapter parity, **not** enterprise deployment security,
measured incident reduction or production-grade readiness.

## Host-side enforcement before any action

To illustrate how an integrating application **consumes** (but does not treat
as authority) an RPE M3 result, run:

```bash
python scripts/demo_m3_host_enforcement.py
```

This is a **synthetic in-process executor** that records a single effect to
an in-memory list; it does not call a bank, ERP, tool, network service or
release API. Six test cases show that host-level actor/target authorization
and RPE `allow` are both necessary to reach the simulated executor; missing
approval evidence, an upstream mismatch, wrong target, missing host grant and
untrusted actor do not dispatch. A seventh case rejects a forged
`authority_effect` result. This demonstrates one fail-closed integration
pattern, **not** independent authentication, authorization correctness,
remote enforcement, or guaranteed risk reduction.

A real deployment must bind an authenticated user/service to exact permitted
operations and target, prevent parallel bypass paths, acquire independent
approval evidence, verify effect in the external destination, and implement
durable retry/reconciliation/incident handling downstream.

## Problem-first implementation example: vendor bank-detail changes

A concrete enterprise risk is business-email compromise causing fraudulent
supplier-payment-detail changes. FBI recommends independently verifying account
changes; OWASP calls out excessive authority/autonomy for AI tools.

- FBI: https://www.fbi.gov/how-we-can-help-you/common-frauds-and-scams/business-email-compromise
- OWASP LLM06: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/

A runnable **synthetic integration preflight** uses the existing M3 guarded
adapter without creating a separate workflow engine:

```bash
python examples/business-controls/vendor_bank_change_preflight.py
python examples/business-controls/vendor_bank_change_preflight.py --self-test
```

To evaluate an external JSON case, use `--input path/to/case.json` with
exactly five fields:

```json
{
  "case_id": "illustrative-request-01",
  "vendor_ref": "non-sensitive-reference",
  "out_of_band_verified": false,
  "dual_control_approved": false,
  "account_mismatch": false
}
```

The application-facing outcomes distinguish:

- missing independent callback verification / dual-control evidence:
  M2 `human_gate` → M3 `require_evidence`;
- both signals present, no mismatch observed:
  M2 `allow` → M3 `allow` (still **no** execution authorization);
- signals present, upstream account mismatch observed:
  M2 `allow` → M3 `require_authority`.

**Implementation boundary:** These are synthetic, caller-supplied boolean
observations, not authenticated certificates. Do not populate them from the
vendor's email or an agent's assertion. A real implementation must source
them from independently controlled verification and approval workflows, enforce
the returned decision in its downstream ERP/payment executor, authenticate
users/tools, maintain auditable evidence, and verify the actual downstream
effect. RPE neither authenticates the upstream signals nor prevents a
privileged executor from ignoring its result. The embedded Requirement Pack is
a replaceable example, **not** an organization-approved payment policy or SAP
integration. No banking data, live SAP connection, payments, or external writes
are used.

This example supplies a problem/mitigation/integration starting point, not an
independent fraud-reduction, deployment, compliance, or commercial claim.
