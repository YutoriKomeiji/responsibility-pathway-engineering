# External Kernel Roadmap

This roadmap tracks RPE's portable external responsibility kernel and its interfaces.

## Target

Build reusable components that convert Responsible AI requirements into runtime controls across multiple AI environments while preserving applicability, evidence scope, reason codes, and human-return ownership.

## Stage K0 — Foundation

**Status: implemented for the current synthetic reference scope.**

- external responsibility-kernel architecture
- minimal requirement-pack and action-request shapes
- structured `allow`, `hold`, `human_gate`, and `deny` decisions
- reason codes and human-return routes

Primary files:

- `docs/architecture/external-responsibility-kernel.md`
- `examples/external-kernel/`
- `scripts/run_external_kernel.py`
- `scripts/run_external_kernel_multi.py`

## Stage K1 — Stable interchange schemas

**Status: partially implemented; compatibility policy remains open.**

Implemented:

- JSON Schemas for requirement packs, action requests, and gate decisions
- positive and negative fixtures
- bounded validation workflows
- source metadata for authority, jurisdiction, version, owner, effective date, and review status

Next:

- explicit request and result schema-version policy
- breaking-change and deprecation rules
- reason-code compatibility rules

## Stage K2 — Applicability and requirement-pack tooling

**Status: applicability resolution implemented; compiler and external loading remain open.**

Implemented:

- deterministic applicability resolution
- visible `applicable`, `not_applicable`, and `unknown` handling
- human return when applicability is unknown or no pack is applicable

Next:

- bounded external pack loader
- reviewable compiler or mapping assistant
- validation of authority, scope, ownership, and interpretation metadata
- review diffs rather than silent policy replacement

## Stage K3 — Runtime kernel package

**Status: implemented as a small Python package reference API.**

Implemented:

- `rpe_kernel.evaluate_action()` package entry point
- multi-pack evaluation and deterministic precedence
- applicability, evaluation, and combination modules
- local package checker and CI

Next:

- explicit contract versioning
- richer trace, repair, resume, and evidence references
- packaging and release policy beyond repository-local installation

## Stage K4 — Environment adapters

**Status: first bounded adapters implemented.**

Implemented:

- local REST adapter: `rpe-rest`
- OpenAPI 3.1 contract served at `/openapi.json`
- MCP stdio adapter: `rpe-mcp`
- one MCP tool: `rpe_evaluate_action`
- single-source guard that keeps REST and MCP delegated to `evaluate_action()`

Current boundary:

- local reference interfaces only
- no production authentication, authorization, TLS termination, rate limiting, persistence, tenancy isolation, deployment approval, or automatic execution

Future adapter candidates:

- OpenAI tool/function middleware
- Gemini and Claude tool layers
- LangGraph, LangChain, Semantic Kernel, AutoGen, and CrewAI integration examples
- GitHub Actions and CI gates
- enterprise and SAP-oriented workflow adapters

Every adapter must translate environment events into the common request contract and must not redefine kernel semantics independently.

## Stage K5 — Reviewed requirement packs

**Status: synthetic examples only.**

Candidate areas:

- organizational AI policies
- data handling and external-send controls
- human oversight and escalation
- transparency and evidence-scope requirements
- incident, repair, rollback, and resume paths
- selected mappings from public Responsible AI frameworks and laws

A real-world pack must identify its source, version, jurisdiction, interpretation owner, effective scope, unresolved ambiguity, and required human review. A pack is an operational mapping, not a substitute for legal or regulatory judgment.

## Stage K6 — Production architecture research

**Status: deferred until local contracts have implementation experience.**

Research areas:

- authentication and authorization
- persistence, retention, and tenancy
- secrets and transport security
- rate limiting and abuse handling
- observability and audit traces
- deployment, rollback, and incident ownership

No production claim should be made from the current local adapters.

## Stage K7 — Conformance and interoperability research

**Status: future research.**

Only after interfaces, packs, and adapters have real implementation experience:

- compare behavior across adapters
- define compatibility levels
- test pack portability
- study trace interoperability
- consider conformance language only with explicit evidence and external review

## Near-term PR sequence

1. Define request/result schema-version and compatibility policy.
2. Add a bounded external requirement-pack loader and checker.
3. Add one integration example without duplicating kernel semantics.
4. Extend trace, repair, resume, and evidence-reference structures.
5. Add reviewed requirement packs only with named human interpretation ownership.
6. Revisit production architecture after the local contracts stabilize.

## Success measure

RPE progresses when a requirement can be represented, checked for applicability, evaluated, traced, stopped, escalated, repaired, resumed, and returned to the correct human or institution through a portable interface—not when the repository merely adds more prose or interface count.
