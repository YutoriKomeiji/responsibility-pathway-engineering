# External Responsibility Kernel

Responsibility Pathway Engineering (RPE) is intended to become a portable component toolkit that turns Responsible AI requirements into executable controls around AI systems.

## Core idea

RPE does not ask an AI system to be responsible by instruction alone. It converts requirements from laws, governance frameworks, organizational policies, and project rules into machine-readable checks that can drive runtime behavior.

```text
Responsible AI requirement
        -> machine-readable requirement pack
        -> AI action request
        -> allow | hold | deny | human_gate
        -> reason codes, evidence scope, and responsibility return
```

## Kernel boundary

The external kernel sits between an AI system and actions that may affect tools, data, people, organizations, or public environments.

It may:

- inspect an action request
- check required authority and evidence fields
- evaluate explicit stop and escalation conditions
- return a structured gate decision
- identify the human or institutional return point
- produce a trace that downstream adapters can preserve

It does not become the legal, moral, institutional, or final responsibility holder.

## Portable component layers

1. **Requirement packs** — machine-readable Responsible AI requirements.
2. **Gate evaluator** — evaluates an action request against one or more packs.
3. **Human-return controller** — routes unresolved or authority-sensitive cases to a named human or institution.
4. **Evidence-scope checker** — distinguishes available, missing, and unfetched evidence.
5. **Trace adapter** — emits reviewable decisions and reason codes.
6. **Environment adapters** — connect the kernel to agent frameworks, tool gateways, workflow engines, CI, and enterprise systems.

## First reference slice

The first local reference slice in this repository is deliberately small:

- one synthetic requirement pack
- one synthetic action request
- one dependency-free Python evaluator
- one structured decision output

The slice demonstrates how an AI action can be held for human review when authority is missing. It is a reference implementation seed, not a production enforcement system.

## Design direction

Future work should add compatible adapters rather than hard-code one vendor. Candidate environments include MCP servers, OpenAI tool gateways, Gemini function layers, LangGraph, Semantic Kernel, CI workflows, REST proxies, and enterprise workflow systems.

The stable interface should remain centered on:

- action
- actor
- target
- authority
- evidence scope
- applicable requirements
- stop conditions
- decision
- reason codes
- human return point
- trace metadata
