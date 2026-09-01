# Responsibility Pathway Engineering

[![Value Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml)
[![Security Hygiene](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml)
[![Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml)

**Executable Responsible AI controls for AI systems.**

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for evaluating explicitly scoped machine-readable Responsible AI controls.

## What practical problem does this solve?

Many agent implementations can accidentally collapse **"the model proposed an action"** into **"the system may continue with that action."** RPE inserts a small, inspectable boundary between those two statements.

For an existing agent or automation, RPE can:

- turn a missing approval/evidence condition into a visible `human_gate` instead of implicit continuation;
- return stable machine-readable reason codes plus a Human Return / residual-owner role;
- preserve the distinction between evaluation evidence and verified external effect;
- sit in front of an existing execution stack without becoming the executor or requiring the whole application to become an RPE-specific runtime.

Run the synthetic before/after comparison:

```bash
python scripts/value_demo.py
```

See [`docs/why-rpe.md`](docs/why-rpe.md) for the concrete adoption-value boundary and what the demo does **not** prove.

```text
Responsible AI requirements
        ↓
human-scoped machine-readable Requirement Packs
        ↓
AI action request
        ↓
RPE external kernel
        ↓
allow / hold / human_gate / deny
        ↓
reason codes, governance state, applicability, evidence needs, and Human Return
```

RPE helps an AI application determine which stated requirements apply, whether a proposed action may continue under those stated controls, what is missing, and when responsibility must return to a human or institution.

## Long-term direction: human-reviewed normative controls

RPE aims to provide an open, inspectable engineering substrate through which human-reviewed interpretations of laws, public guidelines, standards, organizational policies, professional duties, and affected-party commitments can be translated into bounded machine-readable controls.

```text
official or otherwise authorized normative source
        ↓
human or institutional scoping, interpretation, review, and approval
        ↓
versioned Requirement Pack with source metadata and governance state
        ↓
RPE governed evaluation
        ↓
allow / hold / human_gate / deny, with reasons and a Human Return path
        ↓
separate assurance, legal review, execution authority, and operational responsibility
```

RPE does not transfer legal interpretation, approval authority, execution authority, or final responsibility to the kernel. It is not an automated compliance engine, legal-reasoning authority, self-updating regulatory database, certification body, or substitute for qualified legal, policy, safety, assurance, or operational governance review.

## Current position — M2 implementation in progress

RPE has moved beyond the M1-only implementation boundary. It is currently in **M2 implementation with the governed-integration baseline reached**.

Full M2 closure is **not yet claimed**.

Current public implementation status: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md).

Implemented now:

- deterministic applicability resolution and multi-pack evaluation;
- retained legacy/M1-compatible Python entry `evaluate_action()`;
- explicit strict governed Python entry `evaluate_governed_action()`;
- explicit governed contract families and runtime version handling;
- exact Requirement Pack/governance identity and version binding;
- strict governance eligibility and visible fail-closed outcomes;
- legacy and governed REST reference routes;
- legacy and governed MCP stdio tools;
- OpenAPI 3.1 governed admission/compatibility/governance/applicability/evaluation stages;
- packaged OpenAPI with repository/package/runtime drift checks;
- bounded caller-content and local-file governed-envelope loading;
- explicit rejection of network/registry loading in the first loader;
- responsibility-preserving governed handoff with `authority_effect = none` and `decision_scope = evaluation_only`;
- schemas, synthetic fixtures, deterministic regression checks, and CI guards.

## Two runtime entry modes

### Legacy / M1-compatible

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

This entry remains available for compatibility.

### Strict governed M2

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

The strict governed path is:

```text
governed envelope admission
        ↓
contract compatibility
        ↓
pack ↔ governance binding
        ↓
governance eligibility
        ↓
applicability resolution
        ↓
requirement evaluation
        ↓
decision combination
        ↓
responsibility-preserving handoff
```

Governed evaluation is explicit rather than an optional gate that callers can accidentally omit.

## Critical authority boundary

An RPE `allow` result is an **evaluation result**, not an execution authorization token.

RPE does not by itself:

- dispatch or execute an external action;
- approve deployment;
- verify that an external effect occurred;
- turn a receipt into verified effect evidence;
- grant repair authority because repair is possible;
- grant resume authority because a blocked path is ready to continue;
- transfer final responsibility to AI.

Evaluation evidence is not effect evidence. Repair readiness is not repair authority. Resume authority belongs to the runtime or institution that owns execution and requires a separate authority-bearing transition.

This boundary reflects implementation experience from downstream responsibility-path runtime work without turning RPE into an operating system or execution controller.

## Bounded loading

RPE currently accepts governed evaluation envelopes from:

- caller-provided UTF-8 JSON content; or
- explicitly supplied local files.

```python
from rpe_kernel import load_governed_envelope_content, load_governed_envelope_file
```

The first loader intentionally does not fetch URLs, discover remote registries, install packages, or establish source trust.

A readable file proves only that bytes were available. It does not prove source authority, semantic correctness, governance eligibility, legal validity, or current applicability.

## Install and reference interfaces

The current reference implementation is dependency-free Python 3.11+.

```bash
python -m pip install .
```

| Interface | Legacy entry | Strict governed entry | Documentation |
|---|---|---|---|
| Python package | `evaluate_action()` | `evaluate_governed_action()` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| Local REST | `POST /v1/evaluate` | `POST /v1/evaluate/governed` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| MCP stdio | `rpe_evaluate_action` | `rpe_evaluate_governed_action` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |
| OpenAPI 3.1 | documents both | documents both | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |

The adapters evaluate proposed actions only. They do not execute actions, approve deployment, publish releases, merge code, verify external effects, or transfer responsibility.

## Executable walkthrough and artifact catalog

For the shortest "why would I use this?" comparison:

```bash
python scripts/value_demo.py
```

For the broader bounded synthetic decision walkthrough:

```bash
python scripts/demo.py
```

The public static artifact catalog remains available at [`site/index.html`](site/index.html).

A demo pass or catalog entry is repository evidence only; it is not certification, production approval, legal review, real-world risk-reduction proof, or proof of external effect.

## Claim boundary and promotion path

RPE separates **evidence-limited milestone boundaries that can move** from **permanent responsibility boundaries that an engineering kernel should not cross by itself**. See [`docs/claim-boundary-promotion.md`](docs/claim-boundary-promotion.md).

The M1-only governed-integration boundary has moved: strict runtime governance, compatibility, binding, adapter parity, and bounded local/caller-content loading now have implementation and CI evidence.

That does **not** promote claims of:

- production readiness;
- legal or compliance correctness;
- certification or conformity;
- reviewed real-world normative mappings;
- execution authority;
- verified external effect;
- implementation-wide formal conformance;
- official-standard status.

Promotion is explicit and evidence-specific.

## Verification, assurance, and open governance

RPE connects to Verifiable AI and AI assurance through bounded, inspectable claims rather than a blanket safety declaration.

Formalization may prove properties of explicitly modeled responsibility pathways under stated assumptions. Such proofs do not automatically prove the complete Python runtime, source interpretation, legal validity, operational behavior, or production safety.

Public guidance can inform future human-reviewed Requirement Packs, but RPE does not automatically interpret law or guidance and does not claim that a schema-valid or loadable pack contains a correct legal or normative interpretation.

RPE is MIT-licensed and aims for open specifications, interoperability, independent verification, and multiple-implementation potential. It is not currently an official standard.

See [`docs/verification-assurance-and-open-governance.md`](docs/verification-assurance-and-open-governance.md).

## Main implementation artifacts

| Component | Start here |
|---|---|
| Why use RPE? | [`docs/why-rpe.md`](docs/why-rpe.md) |
| Current M2 status | [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md) |
| Kernel package | [`rpe_kernel/pipeline.py`](rpe_kernel/pipeline.py) |
| Bounded loader | [`rpe_kernel/loader.py`](rpe_kernel/loader.py) |
| Applicability resolver | [`rpe_kernel/applicability.py`](rpe_kernel/applicability.py) |
| Pack evaluator | [`rpe_kernel/evaluation.py`](rpe_kernel/evaluation.py) |
| Governance | [`rpe_kernel/governance.py`](rpe_kernel/governance.py) |
| Compatibility | [`rpe_kernel/compatibility.py`](rpe_kernel/compatibility.py) |
| REST adapter | [`rpe_kernel/http_api.py`](rpe_kernel/http_api.py) |
| MCP adapter | [`rpe_kernel/mcp_server.py`](rpe_kernel/mcp_server.py) |
| OpenAPI contract | [`spec/openapi/rpe-kernel.openapi.json`](spec/openapi/rpe-kernel.openapi.json) |
| Requirement-pack governance | [`docs/requirement-pack-governance.md`](docs/requirement-pack-governance.md) |
| Compatibility policy | [`docs/contract-compatibility-policy.md`](docs/contract-compatibility-policy.md) |
| Claim boundary | [`docs/claim-boundary-promotion.md`](docs/claim-boundary-promotion.md) |
| Project roadmap | [`ROADMAP.md`](ROADMAP.md) |
| Static artifact catalog | [`site/index.html`](site/index.html) |
| AI/search-reader entrance | [`READMEforAI.md`](READMEforAI.md) |
| Japanese entrance | [`README.ja.md`](README.ja.md) |

## Remaining M2 work

The next M2 work is not “add more execution machinery to RPE.” It is to make the evaluation-to-runtime responsibility handoff harder to misuse and prove a concrete adoption value rather than only internal correctness.

Priority areas:

1. adversarial validation of authority confusion, evidence confusion, stale/binding/governance failures, adapter drift, and loader-boundary violations;
2. prove one compact before/after adoption scenario where RPE changes an unsupported implicit continuation into a reasoned Human Return;
3. verify that repair/resume requirements remain requirements rather than authority grants;
4. synchronize claim review and M2 closure evidence.

See [`ROADMAP.md`](ROADMAP.md).

## Scope boundary

RPE is an evaluation and orchestration reference kernel for approved machine-readable controls. It is not a general legal reasoning engine, self-maintaining regulatory knowledge base, certification system, production governance service, official standard, execution controller, or proof that an AI system is lawful, safe, compliant, fair, or socially adequate.

A schema/checker/CI pass or loader success means only that the stated machine-readable checks passed. Source interpretation, real-world applicability, evidence sufficiency, deployment approval, execution authority, external-effect verification, and final responsibility remain with the relevant human or institution.

## Author and construction

Author: **Akihisa Ono (小野昭久)**  
Repository affiliation: Independent

RPE is developed through Open Construction with assistance from [Luminalia AI](docs/ai-assisted-construction-note.md). Human maintainer judgment remains responsible for direction, merge, publication, external claims, deployment decisions, and final responsibility.

- [Provenance](docs/provenance.md)
- [Authorship](AUTHORSHIP.md)
- [Open Construction](OPEN_CONSTRUCTION.md)
- [Citation metadata](CITATION.cff)

## License

Released under the [MIT License](LICENSE).

Copyright (c) 2026 Akihisa Ono (小野昭久). See [NOTICE.md](NOTICE.md) for attribution and AI-assistance notes.
