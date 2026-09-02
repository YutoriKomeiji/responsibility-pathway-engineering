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
- contract/schema readback across every exposed adapter;
- deterministic negative/adversarial fixtures;
- stronger configuration identity and change detection;
- bounded formal assertions where the model and proof ceiling are explicit;
- environment-specific performance/reliability evidence;
- explicit reopening conditions when evidence, configuration, authority, or dependencies change.

Assured must not be interpreted as certification, production authorization, legal compliance, or proof of arbitrary external effects.

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
