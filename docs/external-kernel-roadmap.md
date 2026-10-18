# External Kernel Roadmap

This roadmap tracks RPE's portable external responsibility kernel and its interfaces.

## Target

Build reusable components that evaluate explicitly scoped Responsible AI requirement mappings while preserving applicability, governance state, compatibility, evidence scope, reason codes, maintenance ownership, and Human Return routes.

RPE does not directly interpret the full complexity of law or policy. Real-world mappings require named human interpretation and maintenance ownership.

## Current milestone position

### M1 — Governed Reference Kernel

**Status: reached and retained as the compatibility baseline.**

M1 established the shared deterministic kernel, Python/REST/OpenAPI/MCP reference interfaces, requirement-pack governance model, contract-family version baselines, compatibility policy, and explicit scope boundaries.

### M2 — Governed Pack Integration

**Status: bounded M2 governed-integration closure completed, with exact-head adversarial and post-merge evidence.** This does not certify production operation, legal mapping, external effect, or real-world safety. See [`m2-r5-adversarial-closure-evidence.md`](m2-r5-adversarial-closure-evidence.md).

Current public implementation status: [`m2-governed-integration-current.md`](m2-governed-integration-current.md).

## Stage K0 — Foundation

**Status: implemented for the current synthetic reference scope.**

- external responsibility-kernel architecture;
- bounded Requirement Pack and Action Request shapes;
- structured `allow`, `hold`, `human_gate`, and `deny` decisions;
- reason codes and Human Return routes.

## Stage K1 — Interchange schemas and compatibility

**Status: governed baseline implemented.**

Implemented:

- JSON Schemas for legacy and governed contract families;
- positive and negative fixtures;
- source metadata and governance fields;
- independent contract-family semantic versions;
- additive versus breaking change rules;
- unknown-version behavior;
- reason-code stability;
- deprecation/migration rules;
- packaged contract-version snapshot consumed by runtime compatibility;
- CI checks for repository/package version drift.

Open:

- migration fixtures for future real breaking changes;
- release support-window policy beyond the current reference distribution.

## Stage K2 — Applicability and mapping boundary

**Status: minimal applicability resolution implemented.**

The resolver uses bounded deterministic checks. It is an operational gate, not a general legal or policy reasoning engine.

Next:

- keep unknown applicability visible and Human Returning;
- define conflict/exception/timing/ambiguity boundaries before increasing condition complexity;
- require human-scoped and human-approved mappings for real-world use;
- preserve review diffs rather than silently replacing interpretation.

## Stage K3 — Requirement Pack governance

**Status: strict governed runtime integration implemented.**

The explicit governed path checks:

- lifecycle and ownership;
- reviewer/approver presence;
- source authority/version/jurisdiction binding;
- interpretation status and unresolved ambiguity;
- effective/review/expiry dates;
- suspension/supersession/retirement;
- exact pack/governance identity/version binding;
- Human Return information.

Governance eligibility is distinct from legal correctness, source trust, schema validity, and execution authority.

## Stage K4 — Runtime kernel package

**Status: legacy and strict governed entries implemented.**

Implemented:

- `rpe_kernel.evaluate_action()` for legacy/M1-compatible use;
- `rpe_kernel.evaluate_governed_action()` for strict governed evaluation;
- explicit admission → compatibility → binding → governance → applicability → evaluation order;
- responsibility handoff with `authority_effect = none` and `decision_scope = evaluation_only`;
- deterministic regression and CI coverage.

The completed bounded M2 contract preserves evaluation/effect distinctions and downstream responsibility obligations. Further route generalization, cumulative exposure, and integrity observations are M3 experiments, not unfinished M2 or execution authority.

## Stage K5 — Reference adapters and SDK integrations

**Status: bounded legacy and governed reference adapters implemented.**

Implemented:

- local REST reference adapter;
- legacy `POST /v1/evaluate`;
- governed `POST /v1/evaluate/governed`;
- OpenAPI 3.1 served at `/openapi.json`;
- packaged OpenAPI snapshot with repository/package/runtime parity checks;
- MCP stdio reference adapter;
- legacy MCP tool `rpe_evaluate_action`;
- governed MCP tool `rpe_evaluate_governed_action`.

Current boundary:

- reference interfaces only, not production protocol stacks;
- no action execution, production authentication/authorization, transport security, persistence, tenancy, deployment approval, effect verification, or operational ownership.

Future operational integrations must remain thin over the same semantic kernel and require separate dependency/security/maintenance review.

## Stage K6 — Bounded loading

**Status: first bounded loader implemented.**

Implemented:

- caller-provided UTF-8 JSON content;
- explicitly supplied local files;
- bounded payload size;
- stable loader failure codes;
- rejection of network/remote-registry source forms;
- downstream use of strict governed evaluation.

Loading bytes is not trust establishment. Local file existence does not prove source authority, interpretation correctness, governance eligibility, or current applicability.

Network fetching, remote registry trust, source discovery, and automatic updates remain out of scope unless deliberately reopened.

## Stage K7 — Reviewed requirement mappings

**Status: synthetic/reference mappings only by default.**

Candidate areas include organizational AI policies, data handling, external-send controls, human oversight, transparency, evidence scope, incident handling, and selected public-framework mappings.

Each claimed reviewed mapping needs named interpretation and maintenance ownership, source/version control, review/approval state, ambiguity handling, expiry/supersession rules, and appropriate independent review.

## Stage K8 — Responsibility handoff, uncertainty, repair, and resume boundary

**Status: bounded M2 responsibility-handoff obligations implemented and adversarially checked; downstream runtime semantics remain separately owned.**

RPE should preserve the information downstream runtimes need without taking ownership of the entire post-execution state machine.

Key constraints:

- evaluation evidence is not external-effect evidence;
- a receipt is not automatically verified effect;
- repair readiness is not repair authority;
- resume authority requires a separate authority-bearing transition in the execution-owning system;
- Human Return and residual responsibility must remain visible across failure paths.

M2 closure includes selected negative checks for these boundaries. Post-M2 generalized routing and conditional risk are pursued as non-released experimental M3 work in [draft PR #127](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/pull/127), without claiming dispatch, readback, durable retry, or resume authority.

## Stage K9 — Production architecture research

**Status: deferred.**

Research authentication, authorization, transport security, persistence, retention, tenancy, secrets, rate limiting, observability, deployment, rollback, operational ownership, and incident response before making production claims.

## Stage K10 — Formalization and interoperability research

**Status: experimental and future-facing.**

Formal models may express selected responsibility-path invariants under stated assumptions. They do not automatically verify the Python runtime, source interpretation, organizational operation, or real-world outcome.

Broader interoperability or conformance language requires independent client/implementation evidence against declared interfaces and failure semantics.

## Near-term sequence

1. Preserve closed M2 runtime and exact-head evidence on current `main`. Verify new work does not silently reclassify its public capabilities.
2. Assess the existing M3 draft PR #127 against the [current top-down quality order](../ROADMAP.md): route eligibility, explicit control semantics, input trust, versioned adapters, and existing adversarial checks. A branch-local bounded slice is not a release.
3. Reuse current schemas, fixture families, Python/REST/MCP adapters and negative tests. Add a narrowly scoped implementation change only after a concrete missing obligation or counterexample is confirmed.
4. Independently assess first-use and adoption value against a credible no-RPE alternative. Existing synthetic demos and green CI do not show integration cost, field effectiveness, or external adoption.
5. Keep durable trajectory state, policy truth, execution/effect reconciliation, production NFRs, and independent human-return effectiveness with their current owners.
6. Introduce real-world Requirement Pack mappings only with named human interpretation and maintenance ownership. Any production/release/standards claim requires separate applicable review and evidence.

**Historical note:** the former near-term sequence referred to unclosed M2 R3–R5 work. That sequence was completed within its declared bounded scope and must not be reused as the current plan.

## Success measure

RPE progresses when an explicitly scoped Requirement Pack can be versioned, governed, checked for compatibility and applicability, evaluated, stopped, escalated, and handed off with responsibility information intact—without turning an evaluation result into execution authority or turning repository evidence into claims it cannot support.
