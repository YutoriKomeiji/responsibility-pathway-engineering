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

**Status: implementation in progress; governed-integration baseline reached. Full M2 closure not yet claimed.**

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

Remaining M2 work is not to make this package an execution controller. It is to strengthen uncertainty/effect/evidence handoff semantics and responsibility continuity.

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

**Status: next M2 focus.**

RPE should preserve the information downstream runtimes need without taking ownership of the entire post-execution state machine.

Key constraints:

- evaluation evidence is not external-effect evidence;
- a receipt is not automatically verified effect;
- repair readiness is not repair authority;
- resume authority requires a separate authority-bearing transition in the execution-owning system;
- Human Return and residual responsibility must remain visible across failure paths.

Next implementation/testing should make these boundaries explicit and adversarially testable.

## Stage K9 — Production architecture research

**Status: deferred.**

Research authentication, authorization, transport security, persistence, retention, tenancy, secrets, rate limiting, observability, deployment, rollback, operational ownership, and incident response before making production claims.

## Stage K10 — Formalization and interoperability research

**Status: experimental and future-facing.**

Formal models may express selected responsibility-path invariants under stated assumptions. They do not automatically verify the Python runtime, source interpretation, organizational operation, or real-world outcome.

Broader interoperability or conformance language requires independent client/implementation evidence against declared interfaces and failure semantics.

## Near-term sequence

1. Merge/read back the M2 documentation synchronization slice.
2. Specify uncertainty/effect/evidence handoff semantics.
3. Specify repair/resume requirement semantics without authority inflation.
4. Preserve residual-owner and Human Return continuity.
5. Add adversarial tests for authority/evidence confusion, governance/binding failures, adapter drift, and loader-boundary violations.
6. Review claim boundaries and M2 closure evidence.
7. Add reviewed real-world mappings only with named interpretation/maintenance ownership.
8. Scope production work separately if deliberately authorized.

## Success measure

RPE progresses when an explicitly scoped Requirement Pack can be versioned, governed, checked for compatibility and applicability, evaluated, stopped, escalated, and handed off with responsibility information intact—without turning an evaluation result into execution authority or turning repository evidence into claims it cannot support.
