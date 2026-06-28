# Connector Target Matrix

This document records candidate external connection targets for future Responsibility Pathway Engineering connector design.

It is a design-preview matrix only. It is not a connector implementation, production integration plan, API implementation, external service integration, conformance claim, certification claim, legal review, safety review, compliance review, fairness review, or AI final-responsibility transfer mechanism.

## Purpose

The purpose of this matrix is to clarify what kinds of external systems RPE may observe in the future and how their events might map to draft Responsibility Pathway records.

The matrix is intended to help decide:

- which external systems are worth modeling first;
- what events are observable;
- what RPE roles or evidence fields may be suggested;
- what the first safe synthetic example should look like;
- what must remain deferred before any implementation.

## Target matrix

| Target type | Example systems | Observable events | Candidate RPE mapping focus | First safe form | Deferred boundary |
| --- | --- | --- | --- | --- | --- |
| Workflow automation | GitHub Actions, GitLab CI, Azure DevOps pipelines | workflow run, job, step, actor, trigger, status, failure, retry | Evidence Log, Execution Actor, Stop/Failure signal, Human Return Point | synthetic repository-maintenance workflow event | no production connector |
| Agent tool protocol | MCP-style tools, agent SDK tools, hosted tools | tool listing, tool call, tool result, approval prompt, trace | AI Judgment Node, Evidence Log, Approval Gate, Stop Authority, missing context | synthetic tool-call trace | no live tool connection |
| API request logs | AI API logs, internal API gateway logs, application request logs | request metadata, response metadata, status, latency, error, actor or key reference | observed action, target, evidence pointer, uncertainty, missing context | redacted or synthetic request event | no real user data |
| Local service logs | FastAPI-style toy service, local test service | request lifecycle, handler, status, exception, rollback note | Execution Actor, affected object, Evidence Log, Repair Owner | local toy fixture | no production runtime |
| Cloud audit logs | AWS CloudTrail, Azure Activity Log, Google Cloud Audit Logs | actor, action, target resource, timestamp, source, region, status | Execution Actor, affected resource, authority signal, Evidence Log | synthetic audit event | no cloud connector |
| Ticketing workflow | Jira, ServiceNow, GitHub Issues, approval tickets | ticket creation, assignment, approval, rejection, escalation, closure | Decision Owner, Approval Gate, Repair Owner, Human Return Point | synthetic approval ticket | no enterprise integration |
| AI governance surface | model inventory, policy dashboard, use-case review, risk record | model entry, policy state, review status, exception, monitoring signal | review scope, non-claim preservation, Evidence Log, Decision Owner candidate | synthetic governance record | no governance certification claim |
| ERP document change | SAP, Salesforce, business document workflow | document creation, change, approval, release, reversal, correction | business Decision Owner, Approval Gate, Execution Actor, Repair Owner | synthetic business document event | no live ERP connection |
| Incident and support workflow | incident management, support escalation, runbook workflow | incident, severity, owner, escalation, mitigation, postmortem | Stop Authority, Repair Owner, Evidence Log, Human Return Point | synthetic incident note | no production support routing |

## Mapping discipline

A connector target should not be selected only because it is technically easy.

A target is useful for RPE when it can preserve at least some of the following:

- source event identity
- source system
- timestamp
- actor or system
- observed action
- affected target
- evidence pointer
- approval or review signal
- stop, failure, rollback, or repair signal
- missing context
- uncertainty
- excluded claims
- human or institutional return point

If a target cannot preserve enough context for review, it should remain a research note or negative example rather than becoming a connector target.

## First safe target candidates

The first connector-adjacent examples should remain synthetic and local.

Recommended safe order:

1. Synthetic workflow automation event.
2. Synthetic API request event.
3. Synthetic ticket or approval workflow event.
4. Synthetic cloud audit event.
5. Synthetic ERP document-change event.

This order favors readability and reviewability over production realism.

## Non-selection rule

Do not select a target for implementation when:

- it requires live credentials;
- it requires real user data;
- it requires personal data processing;
- it creates an external side effect;
- it requires production runtime integration;
- it implies connector correctness;
- it implies legal, safety, compliance, or fairness validation;
- it turns a draft pathway into an approved or final record.

## Relation to current documents

Related documents:

- `docs/adapter-boundary.md`
- `docs/api-future-shape.md`
- `docs/external-product-connection-survey.md`
- `docs/deferred-work-restart-conditions.md`
- `spec/runtime-event.schema.yaml`
- `examples/adapter-input-event-minimal.json`
- `examples/runtime-event-to-pathway-minimal.yaml`

## Next safe action

The next safe action is to connect this matrix from navigation documents only where it improves reader-path clarity.

Do not implement a connector from this matrix alone.

The human author or maintainer remains responsible for deciding whether any target should be modeled, expanded, connected, implemented, published, relied upon, reverted, repaired, or deferred.
