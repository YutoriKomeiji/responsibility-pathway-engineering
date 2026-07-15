# External Kernel Roadmap

This roadmap moves RPE from specification-first artifacts toward portable components that drive Responsible AI requirements during AI operation.

## Target

Build reusable components that convert Responsible AI requirements into runtime controls for AI systems across multiple environments.

## Stage K0 — Foundation

- define the external responsibility kernel
- define a minimal requirement-pack shape
- define an AI action-request shape
- emit structured `allow`, `hold`, `deny`, `human_gate`, or `not_applicable` decisions
- preserve reason codes, evidence scope, and a human return point

Current seed:

- `docs/architecture/external-responsibility-kernel.md`
- `examples/external-kernel/minimal-requirement-pack.json`
- `examples/external-kernel/minimal-action-request.json`
- `scripts/run_external_kernel.py`

## Stage K1 — Stable interchange schemas

- publish versioned JSON Schemas for requirement packs, action requests, and gate decisions
- add positive and negative fixtures
- add structural validation in CI
- separate requirement source metadata from executable conditions
- record jurisdiction, framework version, owner, effective date, and review date

## Stage K2 — Requirement-pack compiler

- convert a bounded policy mapping into an executable requirement pack
- retain source clauses and human interpretation notes
- reject incomplete authority, scope, or ownership metadata
- produce a review diff rather than silently replacing policy interpretation

## Stage K3 — Runtime kernel library

- package the evaluator as a small vendor-neutral library and CLI
- support multiple packs and deterministic precedence
- add `allow`, `hold`, `deny`, and `human_gate` decision semantics
- add trace identifiers and repair/retry inputs
- keep final authority with configured human or institutional owners

## Stage K4 — Environment adapters

Build thin adapters around the stable kernel interface:

- MCP server and tool gateway
- OpenAI tool/function middleware
- Gemini function layer
- LangGraph node or middleware
- Semantic Kernel filter
- REST proxy
- GitHub Actions and CI adapter
- enterprise workflow adapters, including SAP-oriented integration patterns

Adapters should translate environment events into the common action-request format. They should not redefine requirement semantics independently.

## Stage K5 — Responsible AI requirement packs

Develop reviewable packs for:

- organizational AI policies
- data handling and external-send controls
- human oversight and escalation
- transparency and evidence-scope requirements
- incident, repair, and rollback paths
- selected mappings from public Responsible AI frameworks and laws

A law- or framework-derived pack must identify its source, version, jurisdiction, interpretation owner, effective scope, unresolved ambiguity, and required human review. A pack is an operational mapping, not a substitute for legal or regulatory judgment.

## Stage K6 — Conformance and interoperability research

Only after the interfaces and adapters have real implementation experience:

- compare decision behavior across adapters
- define compatibility levels
- test pack portability
- study trace interoperability
- consider conformance language only with explicit evidence and external review

## Near-term PR sequence

1. External kernel foundation and runnable synthetic example.
2. JSON Schemas and fixture validation workflow.
3. Repository-map generator and AI-readable generated catalog.
4. Multi-pack evaluator with deterministic precedence.
5. First adapter design and one local adapter prototype.
6. Requirement-pack source metadata and review workflow.

## Success measure

RPE progresses when a Responsible AI requirement can be represented, evaluated, traced, stopped, escalated, and returned to the correct human or institution through a portable interface—not when the repository merely adds more boundary prose.
