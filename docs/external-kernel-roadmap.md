# External Kernel Roadmap

This roadmap tracks RPE's portable external responsibility kernel and its interfaces.

## Target

Build reusable components that evaluate explicitly scoped Responsible AI requirement mappings during AI operation while preserving applicability, evidence scope, reason codes, maintenance ownership, and human-return routes.

RPE does not directly interpret the full complexity of law or policy. Real-world mappings require named human interpretation and maintenance ownership.

## Stage K0 — Foundation

**Status: implemented for the current synthetic reference scope.**

- external responsibility-kernel architecture;
- minimal requirement-pack and action-request shapes;
- structured `allow`, `hold`, `human_gate`, and `deny` decisions;
- reason codes and human-return routes.

## Stage K1 — Interchange schemas and compatibility

**Status: partially implemented.**

Implemented:

- JSON Schemas for requirement packs, action requests, and gate decisions;
- positive and negative fixtures;
- bounded validation workflows;
- source metadata fields.

Open:

- explicit request and result schema versions;
- pack lifecycle and schema versions;
- breaking-change, deprecation, and migration rules;
- reason-code compatibility rules.

## Stage K2 — Applicability and mapping boundary

**Status: minimal applicability resolution implemented.**

The current resolver uses a small fixed set of fields and deterministic equality checks. Requirement evaluation checks named context values. This is a bounded operational gate, not a general legal or policy reasoning engine.

Next:

- keep unknown applicability visible and human-returning;
- define conflict, exception, timing, and ambiguity boundaries before increasing condition complexity;
- require human-scoped and human-approved mappings for real-world use;
- preserve review diffs rather than silently replacing interpretation.

## Stage K3 — Requirement-pack governance

**Status: next priority.**

Define lifecycle states:

```text
draft → reviewed → approved → active → suspended / superseded / retired
```

Define and check:

- owner and reviewer;
- source authority, source version, and jurisdiction;
- effective scope and interpretation status;
- unresolved ambiguity;
- effective date, last review, and next review due;
- supersession and retirement relationships;
- failure behavior for expired, ownerless, ambiguous, or unreviewed packs.

External loading and reviewed real-world packs remain blocked until this governance boundary is explicit.

## Stage K4 — Runtime kernel package

**Status: implemented as a small Python reference API.**

Implemented:

- `rpe_kernel.evaluate_action()` package entry point;
- deterministic applicability and multi-pack evaluation;
- local package checker and CI;
- single-source delegation guard.

Next:

- explicit contract versioning;
- richer trace, repair, resume, and evidence references;
- release and migration policy beyond repository-local installation.

## Stage K5 — Reference adapters and SDK integrations

**Status: first bounded reference adapters implemented.**

Implemented:

- dependency-free local REST reference adapter;
- OpenAPI 3.1 contract served at `/openapi.json`;
- dependency-free MCP stdio reference adapter;
- one MCP tool: `rpe_evaluate_action`.

Current boundary:

- these are local reference interfaces, not production protocol stacks;
- they do not execute actions or provide production authentication, authorization, transport security, persistence, tenancy, deployment approval, or operational ownership.

Before adding an operational adapter:

- evaluate established SDKs and maintained protocol libraries;
- document protocol-version and dependency maintenance responsibility;
- keep the adapter thin;
- do not duplicate kernel semantics.

Future integration candidates include OpenAI, Gemini, Claude, LangGraph, LangChain, Semantic Kernel, AutoGen, CrewAI, GitHub Actions, and enterprise or SAP-oriented workflows.

## Stage K6 — External pack loading

**Status: blocked by governance and compatibility work.**

A bounded loader must preserve lifecycle, source, interpretation, ownership, version, and review-validity metadata. Invalid or stale governance state must fail visibly and must not silently produce `allow`.

Loading a pack is not evidence that the mapping is correct, current, complete, or approved for a deployment.

## Stage K7 — Reviewed requirement mappings

**Status: synthetic examples only.**

Candidate areas include organizational AI policies, data handling, external-send controls, human oversight, transparency, evidence scope, incident handling, repair, rollback, and selected public-framework mappings.

Each reviewed mapping needs named interpretation and maintenance ownership. A mapping is an operational artifact, not a substitute for professional or institutional judgment.

## Stage K8 — Trace, repair, and resume

**Status: candidate.**

Add explicit trace identifiers, evidence references, repair inputs, resume conditions, return-to-human ownership, and non-silent reopening rules.

## Stage K9 — Production architecture research

**Status: deferred.**

Research authentication, authorization, transport security, persistence, retention, tenancy, secrets, rate limiting, observability, deployment, rollback, operational ownership, and incident response before making production claims.

## Stage K10 — Formalization and interoperability research

**Status: experimental and future-facing.**

Lean currently expresses selected model-scoped structural invariants. It does not verify the Python runtime, source interpretation, organizational operation, or real-world outcome.

Do not use Lean as primary product evidence unless an explicit checked correspondence between formal definitions and runtime artifacts is established.

Interoperability or conformance language should be considered only after interfaces, governed packs, adapters, and traces have implementation experience and external review.

## Near-term PR sequence

1. Define pack lifecycle, ownership, expiry, supersession, and review-validity rules.
2. Define compatibility policy for pack, request, result, and reason-code versions.
3. Document reference adapters separately from future SDK-based operational adapters.
4. Add external pack loading only after governance failure modes are explicit.
5. Extend trace, repair, resume, and evidence-reference structures.
6. Add reviewed mappings only with named human interpretation and maintenance ownership.

## Success measure

RPE progresses when an explicitly scoped requirement mapping can be governed, checked for applicability, evaluated, traced, stopped, escalated, repaired, resumed, and returned to the correct human or institution through a maintainable interface—not when the repository merely adds interface count, condition complexity, formal terminology, or claims.