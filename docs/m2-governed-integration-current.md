# RPE M2 Governed Integration — Current Status

Status: **bounded M2 governed-integration closure complete at repository level**.

This document records the current public implementation boundary after the governed-integration, responsibility-handoff, value-validation, and adversarial-closure work. The bounded M2 closure was read back on merged `main` with exact closure evidence in `docs/m2-r5-adversarial-closure-evidence.md`. Closure does not mean production-ready, compliant, certified, authorized for consequential execution, or complete with respect to post-M2 adaptive-routing/security/trajectory work.

## What is implemented now

### Explicit governed contracts

RPE has separate contract families for the strict governed evaluation surface. The governed result explicitly preserves:

- `authority_effect = none`;
- `decision_scope = evaluation_only`;
- evaluation decision and reason-code references;
- selected/rejected governed Pack references;
- evaluation evidence scope and Human Return;
- downstream responsibility obligations;
- nullable loader-observed transport provenance.

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

Unsupported governed contract combinations fail visibly before requirement evaluation. The governed request remains a closed JSON contract; loader transport observations are retained outside that request payload so loading does not silently migrate or relabel it.

### REST, MCP, and OpenAPI parity

The reference adapters preserve the legacy surfaces and add explicit governed surfaces:

- REST legacy: `POST /v1/evaluate`;
- REST governed: `POST /v1/evaluate/governed`;
- MCP legacy: `rpe_evaluate_action`;
- MCP governed: `rpe_evaluate_governed_action`.

The OpenAPI document represents governed admission, compatibility, governance, applicability, and evaluation stages together with the current responsibility-handoff fields. The OpenAPI snapshot is packaged with the Python distribution, and CI rejects repository/package/runtime drift.

The HTTP governed request does not accept caller-asserted transport provenance. Loader-observed provenance can appear in a shared governed result only when the bounded Python loader actually observed the input bytes.

### Bounded loader and transport provenance

RPE can load a governed evaluation envelope from:

- caller-provided UTF-8 JSON content; or
- an explicitly supplied local file.

The first loader intentionally does **not** perform network fetching, remote registry discovery, package installation, or source-trust establishment.

It applies a bounded payload size and stable loader failure codes. The loader now records the SHA-256 digest and byte length of the exact bytes it observes. The observation is held as non-JSON Python metadata so the governed request payload itself remains unchanged. When the loaded envelope is evaluated directly, the observation is preserved into the responsibility handoff.

Transport provenance is deliberately limited to:

- source kind (`caller_content` or `local_file`);
- SHA-256 digest;
- byte length;
- `observation_scope = transport_bytes_only`.

A local filesystem path is intentionally not carried into the governed payload or result. A digest match proves only which bytes were observed by the loader; it does not prove authorship, source authority, semantic correctness, governance eligibility, legal validity, current applicability, or external effect.

### Downstream responsibility obligations

RPE does not implement the downstream execution state machine. Instead, the governed handoff states the obligations that must remain visible after evaluation:

- dispatch requires separate downstream authority;
- an external-effect claim requires downstream effect verification;
- a receipt alone is not sufficient effect evidence;
- retry, repair, and resume require reauthorization;
- the authority owner is the downstream runtime or institution, not RPE;
- a residual-owner role remains visible, following Human Return when one exists.

These are handoff requirements, not execution capabilities or authority grants.

## Verification currently present

Current repository checks cover, among other things:

- governed admission positive and negative paths;
- legacy optional-M2 regression behavior;
- pack/governance binding failures;
- governance-date and ambiguity failures;
- bounded loader positive and negative paths;
- exact-byte digest and byte-length continuity from loader to handoff;
- rejection of caller-asserted transport provenance;
- absence of local-path leakage in the handoff;
- downstream obligation and no-authority invariants;
- REST legacy and governed routes;
- MCP legacy and governed tools;
- OpenAPI responsibility-handoff and repository/package/runtime parity;
- Python package API;
- single-source kernel delegation;
- repository security hygiene.

CI success is evidence that the declared repository checks passed. It is not production assurance, certification, legal review, source-trust proof, or proof of external effects.

## Responsibility boundary learned from later runtime work

M2 no longer treats post-evaluation execution state as something RPE should absorb wholesale.

RPE owns evaluation and responsibility-preserving handoff. It does **not** own the full post-execution state machine for dispatch, effect verification, retry/reconciliation, repair execution, or resume authorization.

The governed result therefore preserves information needed by downstream runtimes without manufacturing authority. In particular:

- evaluation evidence is not effect evidence;
- a receipt is not verified external effect;
- repair readiness is not repair authority;
- resume requires a separate authority-bearing transition in the system that owns execution;
- Human Return and residual responsibility must remain visible across failures.

These constraints remain permanent architecture boundaries after M2 closure and prevent RPE from turning into an operating system or execution controller.

## Not implemented / not claimed

The current governed-integration and responsibility-handoff baselines do not provide:

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

## M2 closure state

The declared M2 governed-integration scope is closed at repository level.

Closure evidence includes:

1. exact PR-head and merged-main readback;
2. focused governed-admission, compatibility, loader, handoff, REST, MCP, OpenAPI, value-demo, and adversarial checks;
3. explicit no-authority / evaluation-only handoff semantics;
4. selected negative checks for authority/evidence confusion, governance/binding failures, schema/runtime drift, and loader/provenance boundaries.

Post-M2 work is not “remaining M2” by default. Adaptive Responsibility Routing, conditional/trajectory risk, broader security architecture, NFR/adoption redesign, production deployment controls, and generalized runtime concerns require separately scoped owners and evidence.

## Provenance boundary

This public status document records public RPE implementation facts and public design abstractions only. It does not publish private project-control identifiers, private conversation state, private authoring-repository topology, or private persona/runtime configuration.

RPE is developed through Open Construction with Luminalia AI assistance. Direction, review, merge, publication claims, deployment decisions, and final responsibility remain with the human maintainer.
