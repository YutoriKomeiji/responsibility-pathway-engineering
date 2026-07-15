# Responsibility Pathway Engineering

**Executable Responsible AI controls for AI systems.**

Responsibility Pathway Engineering (RPE) is a portable external responsibility kernel and component toolkit for turning Responsible AI requirements into runtime controls.

RPE is designed to help AI applications answer four operational questions before or during action:

- Is this action allowed to proceed?
- Which requirements apply?
- What evidence or authority is missing?
- Should the system allow, hold, deny, or return the case to a human?

```text
Responsible AI requirements
        ↓
machine-readable requirement packs
        ↓
AI action request
        ↓
RPE external kernel
        ↓
allow / hold / human_gate / deny
        ↓
reason codes, evidence scope, and responsibility return
```

## Run the external kernel

The current reference implementation is dependency-free Python.

Evaluate one requirement pack:

```bash
python scripts/run_external_kernel.py \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-action-request.json
```

Evaluate multiple packs together:

```bash
python scripts/run_external_kernel_multi.py \
  examples/external-kernel/minimal-action-request.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-data-handling-pack.json
```

Expected combined behavior:

```text
publication requirement pack → human_gate
data-handling requirement pack → hold
combined decision → human_gate
```

The result preserves each pack's applicability, missing requirements, reason codes, source metadata, and human-return role instead of collapsing them into an opaque score.

## What is implemented

| Component | Purpose | Start here |
|---|---|---|
| External kernel | Evaluate one Responsible AI requirement pack against an AI action | [`scripts/run_external_kernel.py`](scripts/run_external_kernel.py) |
| Multi-pack evaluator | Combine multiple applicable requirement decisions with visible precedence | [`scripts/run_external_kernel_multi.py`](scripts/run_external_kernel_multi.py) |
| Requirement-pack schema | Define machine-readable controls and source provenance | [`schemas/external-kernel/requirement-pack.schema.json`](schemas/external-kernel/requirement-pack.schema.json) |
| Action-request schema | Define the AI action and its execution context | [`schemas/external-kernel/action-request.schema.json`](schemas/external-kernel/action-request.schema.json) |
| Gate-decision schema | Define structured allow, hold, human-gate, and deny results | [`schemas/external-kernel/gate-decision.schema.json`](schemas/external-kernel/gate-decision.schema.json) |
| Source metadata | Record authority, jurisdiction, source version, review owner, and interpretation status | [`docs/requirement-pack-source-metadata.md`](docs/requirement-pack-source-metadata.md) |
| Repository-map generator | Produce exact file URLs for AI/search readers | [`scripts/generate_repository_map.py`](scripts/generate_repository_map.py) |
| Responsibility-path tools | Record evidence, authority, stop, return, and repair paths | [`templates/ai-assisted-work-responsibility-path.yaml`](templates/ai-assisted-work-responsibility-path.yaml) |
| Formalization spine | Explore structural invariants in Lean 4 | [`formal/lean/README.md`](formal/lean/README.md) |

## Example decision

An AI requests external publication, but authority and human approval have not been confirmed:

```json
{
  "decision": "human_gate",
  "reason_codes": [
    "RPE-PUBLISH-MISSING-AUTHORITY-CONFIRMED",
    "RPE-PUBLISH-MISSING-HUMAN-APPROVAL-PRESENT"
  ],
  "missing_requirements": [
    "authority_confirmed",
    "human_approval_present"
  ],
  "human_return": {
    "role": "authorized_human_owner"
  }
}
```

RPE does not ask the model to merely "behave responsibly." It inserts explicit requirements, stop conditions, evidence expectations, and human-return routes into the action pathway.

## Intended integrations

The external kernel is vendor-neutral. Planned adapters and starter components include:

- MCP servers and tool gateways
- OpenAI tool and function-calling layers
- Gemini and Claude tool adapters
- LangGraph, LangChain, Semantic Kernel, AutoGen, and CrewAI middleware
- GitHub Actions and CI gates
- REST proxies and local CLI workflows
- enterprise and SAP-oriented workflow adapters

See [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md) for the implementation sequence.

## Requirement packs

A requirement pack converts a law mapping, standard, guideline, organizational policy, or synthetic test requirement into an executable control.

Each pack can carry:

- applicability conditions
- required context and evidence
- decision on missing requirements
- reason-code namespace
- human-return role
- source authority and URL
- jurisdiction and source version
- effective date and review owner
- review and interpretation status

The current packs are synthetic examples. Real law, standard, guideline, and organizational-policy mappings require source-specific review and maintenance.

## Project status

RPE is an active reference implementation under construction.

The repository already contains executable kernel paths, schemas, examples, validators, CI workflows, responsibility-record templates, reader tools, and formalization experiments. The next major work is applicability resolution, runtime packaging, adapters, richer requirement-pack tooling, and integration examples.

- [External-kernel architecture](docs/architecture/external-responsibility-kernel.md)
- [External-kernel roadmap](docs/external-kernel-roadmap.md)
- [Current project roadmap](ROADMAP.md)
- [Browser-friendly artifact catalog](https://yutorikomeiji.github.io/responsibility-pathway-engineering/)
- [AI/search-reader entrance](READMEforAI.md)

## Design principle

RPE preserves the ability to return from an AI action to:

- the requirement that affected it
- the evidence and uncertainty available at the time
- the authority required for execution
- the person or institution responsible for review
- the stop, repair, and reopening path

Responsibility boundaries are part of the implementation, not a substitute for implementation.

## Scope boundary

RPE provides executable control structures and traceable responsibility pathways. It does not by itself establish that a system is lawful, safe, compliant, fair, certified, socially adequate, or production-approved.

A schema-valid or passing result means that the stated machine-readable checks passed. Real-world applicability, source interpretation, evidence sufficiency, deployment approval, and final responsibility remain with the relevant human or institution.

## Author and construction

Author: **Akihisa Ono (小野昭久)**  
Repository affiliation: Independent

RPE is developed through Open Construction with assistance from [Luminalia AI](docs/ai-assisted-construction-note.md). Human maintainer judgment remains responsible for direction, merge, publication, external claims, and final decisions.

- [Provenance](docs/provenance.md)
- [Authorship](AUTHORSHIP.md)
- [Open Construction](OPEN_CONSTRUCTION.md)
- [Citation metadata](CITATION.cff)

## License

Released under the [MIT License](LICENSE).

Copyright (c) 2026 Akihisa Ono (小野昭久). See [NOTICE.md](NOTICE.md) for attribution and AI-assistance notes.
