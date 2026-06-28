# External Product Connection Survey

This note records an initial public-source survey of external AI products, agent frameworks, workflow tools, and governance surfaces for future Responsibility Pathway Engineering connector and API design.

This is a survey note only. It is not a product ranking, endorsement, certification result, conformance claim, production integration plan, connector implementation, runtime implementation, or AI final-responsibility transfer mechanism.

## Survey purpose

The purpose is to observe connection surfaces.

RPE needs to understand what current external systems expose or emphasize before choosing future connector targets.

The survey asks:

- What systems produce AI-involved events?
- What systems expose tool calls, workflow runs, approval states, or audit logs?
- What events could become draft Responsibility Pathway records?
- What must remain outside the connector until review boundaries are stable?

## Initial observation areas

| Area | Examples | RPE observation focus |
| --- | --- | --- |
| Agent SDK and tool protocols | OpenAI Agents SDK, Anthropic MCP, Google ADK | tool invocation, context access, approval, trace, transport, tool metadata |
| Workflow automation | GitHub Actions, n8n, Zapier-like automation | trigger, job, step, action, failure, retry, rollback, human review |
| Enterprise workflow | ServiceNow, Jira, Azure DevOps | ticket, assignment, approval, escalation, incident, audit trail |
| AI governance | ServiceNow AI Control Tower, cloud AI governance tools, model governance platforms | risk record, policy, model/use-case inventory, monitoring, review status |
| Cloud audit | AWS CloudTrail, Azure Activity Log, Google Cloud Audit Logs | actor, action, target, timestamp, authority, affected resource |
| ERP and business systems | SAP, Salesforce, ServiceNow workflows | business decision, document change, approval, execution, correction, repair |

## Initial public-source observations

### Agent protocols and tool surfaces

MCP-style tool connection has become a major reference point for AI systems connecting to external data, tools, and services.

For RPE, the important point is not only that a model or agent can call tools. The important point is whether the pathway from tool access to action, evidence, approval, stop, repair, and human return remains inspectable.

RPE should treat agent-tool interfaces as high-priority observation surfaces.

### Workflow automation surfaces

Workflow automation systems expose events that are naturally close to RPE concepts:

- workflow run
- job
- step
- actor
- trigger
- approval
- failure
- retry
- rollback
- artifact
- audit log

These surfaces are good candidates for early synthetic connector examples because they can be represented without claiming production readiness.

### Enterprise workflow and governance surfaces

Enterprise platforms often expose tickets, assignments, approvals, escalations, review states, and governance dashboards.

These are strong RPE targets because they already contain partial responsibility-pathway signals.

However, they should remain review-required. A ticket or approval state is not automatically a complete responsibility pathway.

### Cloud and audit logs

Cloud audit logs can provide actor, action, target, timestamp, source, and authority-related evidence.

They are useful for Evidence Log and Execution Actor signals, but they rarely provide complete Decision Owner, Approval Gate, Repair Owner, or Human Return Point information by themselves.

### ERP and business systems

ERP and business systems are high-value future targets because they contain real business decisions and document changes.

They should not be early production connectors. A safer path is to model synthetic or redacted business-event examples first.

## RPE differentiation

Most external products focus on enabling agents, tools, workflows, automation, governance dashboards, or audit trails.

RPE should focus on preserving the responsibility pathway around those events:

- where judgment arose
- where authority existed
- what evidence remained
- whether approval was required
- whether stop authority existed
- whether repair or rollback was possible
- where the case returned to a human or institution
- what remained missing or uncertain

This means RPE connectors should produce draft records for review, not final responsibility decisions.

## Suggested connector target matrix

A future connector-target matrix should include:

| Target type | First safe observation | Candidate RPE mapping | Deferred boundary |
| --- | --- | --- | --- |
| GitHub Actions | synthetic workflow run | Evidence Log, Execution Actor, Stop/Failure signal | no production connector |
| API request logs | redacted synthetic request event | actor, action, target, timestamp, missing context | no real user data |
| FastAPI-style service logs | local toy request lifecycle | Execution Actor, affected object, evidence pointer | no production runtime |
| Cloud audit logs | synthetic audit event | actor, authority, affected resource, evidence | no cloud connector |
| Ticketing workflow | synthetic approval ticket | Approval Gate, Decision Owner, Repair Owner | no enterprise integration |
| ERP document change | synthetic business document event | business decision, approval, correction, repair | no live ERP connection |

## Next safe repository action

The next safe action is to create or update a connector target matrix before implementing any connector.

Recommended next document:

- `docs/connector-target-matrix.md`

The matrix should remain design-level and synthetic-first.

## Boundary

This survey does not authorize:

- connecting to live external systems
- ingesting real logs
- processing personal data
- service-specific connector implementation
- production runtime integration
- automatic approval
- automatic execution
- certification claims
- conformance claims
- legal, safety, compliance, or fairness claims
- AI final-responsibility transfer

The human author or maintainer remains responsible for deciding whether any survey result should be used, revised, published, relied upon, reverted, repaired, or deferred.
