# RPE M2 Governed Integration — Current Status

Status: **implementation in progress; governed-integration baseline reached**.

This document records the current public implementation boundary after the R3A–R3D sequence. It supersedes the implementation-status assumptions in the older M2 entry plan. It does not declare M2 fully closed, production-ready, compliant, certified, or authorized for consequential execution.

## What is implemented now

### Explicit governed contracts

RPE has separate contract families for the strict governed evaluation surface. The governed result explicitly preserves:

- `authority_effect = none`;
- `decision_scope = evaluation_only`.

An RPE `allow` remains an evaluation result. It is not an execution authorization token.

### Strict governed Python entry

`rpe_kernel.evaluate_governed_action()` provides the explicit M2 governed entry.

Its bounded order is:

```text
governed envelope admission
→ contract compatibility
→ pack/governance binding
→ governance eligibility
→ applicability resolution
→ requirement evaluation
→ decision combination
→ responsibility handoff
```

The historical `evaluate_action()` entry remains available for legacy/M1-compatible use. The two entry modes are intentionally distinct rather than relying on optional flags that can silently omit M2 gates.

### Governance normalization

The strict governed path rejects visible governance failures including unsupported interpretation states, unresolved ambiguity, malformed or future review dates, invalid review ordering, expired review, not-yet-effective records, missing required ownership/review information, and pack/governance binding mismatch.

Loading or schema validity does not establish that a source interpretation is legally, normatively, or operationally correct.

### Contract-version handling

Runtime compatibility uses the packaged contract-version snapshot rather than a separate hard-coded version table. Repository and packaged contract snapshots are checked for drift.

Unsupported governed contract combinations fail visibly before requirement evaluation.

### REST, MCP, and OpenAPI parity

The reference adapters preserve the legacy surfaces and add explicit governed surfaces:

- REST legacy: `POST /v1/evaluate`;
- REST governed: `POST /v1/evaluate/governed`;
- MCP legacy: `rpe_evaluate_action`;
- MCP governed: `rpe_evaluate_governed_action`.

The OpenAPI document represents governed admission, compatibility, governance, applicability, and evaluation stages. The OpenAPI snapshot is packaged with the Python distribution, and CI rejects repository/package drift.

### Bounded loader

RPE can load a governed evaluation envelope from:

- caller-provided UTF-8 JSON content; or
- an explicitly supplied local file.

The first loader intentionally does **not** perform network fetching, remote registry discovery, package installation, or source-trust establishment.

It applies a bounded payload size and stable loader failure codes. Reading a local file is only a transport observation; file existence does not prove source authority, semantic correctness, governance eligibility, or current validity.

## Verification currently present

Current repository checks cover, among other things:

- governed admission positive and negative paths;
- legacy optional-M2 regression behavior;
- pack/governance binding failures;
- governance-date and ambiguity failures;
- bounded loader positive and negative paths;
- REST legacy and governed routes;
- MCP legacy and governed tools;
- OpenAPI repository/package/runtime parity;
- Python package API;
- single-source kernel delegation;
- repository security hygiene.

CI success is evidence that the declared repository checks passed. It is not production assurance, certification, legal review, or proof of external effects.

## Responsibility boundary learned from later runtime work

M2 no longer treats post-evaluation execution state as something RPE should absorb wholesale.

RPE owns evaluation and responsibility-preserving handoff. It does **not** own the full post-execution state machine for dispatch, effect verification, retry/reconciliation, repair execution, or resume authorization.

The governed result therefore preserves information needed by downstream runtimes without manufacturing authority. In particular:

- evaluation evidence is not effect evidence;
- a receipt is not verified external effect;
- repair readiness is not repair authority;
- resume requires a separate authority-bearing transition in the system that owns execution;
- Human Return and residual responsibility must remain visible across failures.

These constraints guide the remaining M2 work without turning RPE into an operating system or execution controller.

## Not implemented / not claimed

The current governed-integration baseline does not provide:

- network or registry-based Requirement Pack loading;
- automatic source discovery or self-updating regulation;
- production authentication, authorization, persistence, tenancy, secrets, rate limiting, or deployment controls;
- execution, dispatch, publish, merge, payment, or other consequential action authority;
- external-effect verification;
- automatic retry/reconciliation;
- repair or resume execution authority;
- reviewed real-world legal/guideline mappings by default;
- legal/compliance/certification claims;
- proof that a schema-valid pack contains a correct interpretation;
- proof that a Python decision caused or verified a real-world effect.

## Remaining M2 work

The next M2 slices should focus on the boundary between evaluation and downstream runtime responsibility rather than importing an entire execution state machine into RPE.

Priority areas:

1. make uncertainty/effect/evidence handoff semantics explicit and adversarially test them;
2. preserve repair and resume **requirements** without granting repair/resume authority;
3. strengthen residual-owner and Human Return continuity in failure paths;
4. test authority-confusion, evidence-confusion, stale-governance, binding, adapter, and loader adversarial cases;
5. synchronize claim boundaries and close M2 only when the declared engineering evidence is complete.

## Provenance boundary

This public status document records public RPE implementation facts and public design abstractions only. It does not publish private project-control identifiers, private conversation state, private authoring-repository topology, or private persona/runtime configuration.

RPE is developed through Open Construction with Luminalia AI assistance. Direction, review, merge, publication claims, deployment decisions, and final responsibility remain with the human maintainer.
