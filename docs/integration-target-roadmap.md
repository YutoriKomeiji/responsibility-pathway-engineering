# RPE Integration Target Roadmap

## Product objective

RPE should be installable around AI systems as a portable external responsibility kernel.

The core remains framework-neutral. Product adapters translate framework events into RPE action requests and translate RPE gate decisions back into native allow, hold, human-return, or deny behavior.

```text
AI application or agent framework
        ↓
RPE adapter
        ↓
RPE core kernel
        ↓
requirement packs + applicability + evidence + authority
        ↓
allow / hold / human_gate / deny
        ↓
adapter-enforced runtime behavior and trace
```

## Selection principles

Prioritize a target when it:

- has a clear interception point before tool execution or external action
- can carry structured action, actor, target, authority, evidence, and context
- can enforce or faithfully return a gate decision
- is widely reusable across products
- can be demonstrated locally with synthetic fixtures
- does not require production credentials for the first implementation

## Tier 0 — framework-neutral product core

Build these before coupling RPE to one vendor:

1. importable Python core package
2. stable action-request and gate-decision contracts
3. requirement-pack loader and validator
4. applicability resolver
5. multi-pack evaluator
6. trace and repair record
7. CLI
8. local REST boundary

## Tier 1 — first public adapters

### 1. MCP server and gateway

Purpose:

- expose RPE evaluation as an MCP tool
- wrap selected tool calls with pre-execution gating
- return human-gate requirements and reason codes to the host

Why first:

MCP provides a reusable boundary across multiple assistants, IDEs, agents, and tool environments.

### 2. LangGraph adapter

Purpose:

- provide an RPE gate node
- route `allow`, `hold`, `human_gate`, and `deny` into separate graph edges
- preserve pack decisions and trace data in graph state

### 3. LangChain middleware or runnable wrapper

Purpose:

- evaluate tool or action requests before invocation
- expose RPE decisions through standard callbacks or middleware boundaries

### 4. GitHub Actions gate

Purpose:

- evaluate repository actions and deployment-like requests in CI
- emit structured decision artifacts
- demonstrate non-interactive policy enforcement

### 5. REST and webhook adapter

Purpose:

- support language-neutral and product-neutral integration
- accept action requests and return gate decisions through a small local service

## Tier 2 — model and agent ecosystem adapters

- OpenAI tool and function-calling layer
- Gemini tool adapter
- Claude tool adapter
- Microsoft Semantic Kernel filter or middleware
- AutoGen tool or message gate
- CrewAI task or tool gate

Each adapter should map native context into the same RPE core contracts rather than reimplementing policy logic.

## Tier 3 — evidence and operational systems

- OpenTelemetry trace export
- GitHub Issues and pull-request approval flows
- Jira and ServiceNow human-return tickets
- cloud audit-log importers
- SIEM and GRC event adapters

These targets strengthen evidence, escalation, repair, and audit integration after runtime gating is stable.

## Tier 4 — enterprise workflow adapters

- SAP business-object and approval workflow adapter
- Salesforce workflow adapter
- Azure DevOps and GitLab CI adapters
- organization-specific governance and policy-pack registries

SAP is strategically important for enterprise use, but should build on stable core contracts and earlier public adapters.

## Adapter contract

Every adapter should document:

- native event or interception point
- mapping into the RPE action request
- available authority and evidence signals
- how each RPE decision is enforced or returned
- human-return destination
- trace and repair behavior
- unsupported context and failure mode

## Near-term implementation sequence

1. Applicability Resolver
2. importable Python core package
3. local REST API
4. MCP server prototype
5. LangGraph gate node
6. GitHub Actions gate example
7. LangChain wrapper
8. OpenTelemetry trace export
9. first model-specific tool adapter
10. SAP-oriented synthetic workflow adapter
