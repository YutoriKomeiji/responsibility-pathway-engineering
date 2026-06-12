# Source Alignment: evidence-log-design.md

This note records a source-alignment review for the Zenn article on Evidence Log design.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/evidence-log-design.md`
- Title: `Evidence Log設計――責任経路を後から再構成するための監査ログ`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align the public Evidence Log definition with the repository's bounded evidence, checker, review-result, and non-certifying boundaries.

## Article-level role

The article frames Evidence Log as a responsibility-pathway reconstruction layer, not as a generic event log, audit product, or legal-evidence determination.

Current repository alignment:

- strongly aligned with existing Evidence Log vocabulary
- strongly aligned with review-result boundaries
- strongly aligned with validator-boundary language that passing checks or preserving logs is not certification
- strongly aligned with the Phase 3 human-AI review workflow example

Repository change decision:

- no immediate schema change required
- high-value source for future evidence-record and repair-record examples

## Event log boundary

The article states that ordinary event logs record what happened, but responsibility-pathway reconstruction requires relations among request, context, proposal, approval, execution, stopping, and repair.

Current repository alignment:

- supports treating Evidence Log as connected pathway evidence, not a mere chronological trace
- supports not treating logs as responsibility completion
- supports review-result fields that preserve checked, not-checked, and not-claimed boundaries

Repository change decision:

- no immediate checker change required
- possible future checker idea: examples that claim Evidence Log should connect event IDs across request, proposal, approval, execution, stop, and repair records

## Legal-evidence boundary

The article explicitly says it is not comparing log products and is not making final judgments about legal evidentiary value.

Current repository alignment:

- directly aligned with non-legal and non-certifying boundaries
- supports keeping Evidence Log as a structural reconstruction concept
- supports avoiding claims of legal proof, compliance certification, safety certification, or production audit readiness

Repository change decision:

- no legal or compliance claim should be added
- keep Evidence Log language bounded to reconstruction and structural traceability

## Evidence Log definition

The article defines Evidence Log as evidence for reconstructing AI-agent judgment, approval, execution, stopping, and repair as a responsibility pathway.

It says the purpose is not only blame or accusation. Evidence Log supports reconstructing what happened, verifying why a judgment occurred, checking whether approval was substantive, locating stop points, identifying repair responsibility, connecting recurrence prevention, returning to organizational learning, and preserving external oversight / policy-update context.

Current repository alignment:

- strongly aligned with current Evidence Log definition direction
- supports Human Return Point and Stop Authority connections
- supports repair and organizational-learning concepts without turning them into certification

Repository change decision:

- no immediate definition rewrite required
- preserve as source support for future public explanation of Evidence Log

## Log type alignment

The article separates Evidence Log into multiple log types:

- Request Log
- Context Log
- Proposal Log
- Approval Log
- Execution Log
- Stop Log
- Repair Log

Current repository alignment:

- strongly aligned with existing concept vocabulary
- supports future examples that separate AI proposal from execution
- supports future examples that distinguish approval record from meaningful human return
- supports future examples that separate stop record and repair record

Repository change decision:

- no immediate schema split required
- possible future minimal example: `examples/evidence-log-minimal.yaml` or `examples/evidence-record-flow.yaml`

## Approval Log alignment

The article states that approval logs must include who approved, what they saw, whether differences, impact scope, and risk were shown, and whether refusal was possible. A bare approval button is insufficient.

Current repository alignment:

- strongly aligned with Human Return Point article
- supports not treating nominal approval as responsibility return
- supports future review-result fields for visible evidence, missing information, and refusal/stop options

Repository change decision:

- no immediate change required
- useful source for future Human Return Point examples

## Stop Log alignment

The article states that Stop Log records where the process was stopped or why it was not stopped. It includes stop conditions, who held Stop Authority, whether the system suggested stopping, whether humans could stop, why execution continued, and who the process returned to after stopping.

Current repository alignment:

- strongly aligned with Stop Authority concept
- supports future suspension and return examples
- supports recording unused stop authority as evidence, not merely executed stops

Repository change decision:

- no immediate schema change
- high-value source for the next Stop Authority alignment note

## Repair Log alignment

The article says Repair Log records who repaired what after failure, and that without repair logs an incident may appear closed while the responsibility pathway remains open. It records repair target, repair actor, repair content, recurrence prevention, customer response, and organizational reporting.

Current repository alignment:

- strongly aligned with Repair Owner as a repeated cross-article concept
- supports future cross-article Repair Owner alignment note
- supports lifecycle examples in which execution is not the end of the pathway

Repository change decision:

- do not create a standalone Repair Owner source note yet
- after Stop Authority review, consider a cross-article Repair Owner note

## ID design alignment

The article states that it is not enough to separate log types; logs must be connectable as the same responsibility pathway. It proposes IDs such as:

- case_id
- request_id
- proposal_id
- approval_id
- execution_id
- external_trace_id
- stop_id
- repair_id

Current repository alignment:

- strongly aligned with traceability requirements
- supports future example/checker design for connected IDs
- supports avoiding isolated logs that cannot reconstruct pathway context

Repository change decision:

- no immediate schema change
- possible future small example can test linked IDs as structural fields

## Data minimization boundary

The article warns that Evidence Log must balance reconstruction with information minimization. Unlimited full storage of personal information, confidential information, contract information, customer data, and security information can create new risks.

Current repository alignment:

- supports non-production bounded examples
- supports privacy and confidentiality caution without making compliance claims
- supports keeping examples synthetic and minimal

Repository change decision:

- no immediate privacy/compliance schema change
- future examples should avoid real personal or confidential data

## Minimal schema alignment

The article proposes a minimal EvidenceLogEntry sketch including event_id, timestamp, action_class, request_owner, decision_owner, approval_gate, execution_actor, stop_authority, human_return_point, evidence_type, context/proposal/approval/execution/stop/repair refs, affected_scope, reversibility, risk_level, and status.

Current repository alignment:

- compatible with existing element vocabulary
- useful source for a future bounded Evidence Log example
- should not be copied into main schema without further design review

Repository change decision:

- no immediate schema replacement
- possible future: add a dedicated minimal evidence-log fixture only after checker scope is defined

## Failure-pattern alignment

The article lists common failures such as AI output only being saved, approval reasons missing, approver-visible information unknown, execution actor unknown, context missing, rollback missing, stop decisions missing, repair owner unknown, logs unreadable to humans, and logs disconnected from responsibility units.

Current repository alignment:

- strongly supports review-result boundary and unchecked items
- supports future negative fixtures
- supports human-readable evidence and pathway linkage requirements

Repository change decision:

- no immediate negative fixture required
- high-value candidate for later checker tests

## External-context boundary

The article references EU AI Act record-keeping and human oversight, NIST AI RMF, ISO/IEC 42001, and an OpenAI social-responsibility-principles news article as external context.

Current repository alignment:

- useful background for governance and audit discussions
- must not be imported as compliance, legal evidence, safety, audit, or standards certification

Repository change decision:

- keep external references contextual
- no compliance claim should be added

## Claim-strength assessment

Compatible claims:

- logs are necessary but not sufficient
- Evidence Log is for responsibility-pathway reconstruction
- event logs and Evidence Logs are different
- evidence must connect request, context, proposal, approval, execution, stop, and repair
- approval logs must preserve what humans saw and whether refusal was possible
- stop and repair logs are distinct and necessary
- logs must be linkable by IDs
- reconstruction must be balanced with data minimization

Claims to keep bounded:

- legal evidentiary value
- audit readiness
- compliance or standards certification
- safety certification
- production logging architecture
- personal or confidential data retention choices

Repository interpretation:

Evidence Log is a core source-aligned concept, but must remain bounded: evidence preservation helps reconstruction; it does not complete or certify responsibility.

## Repository alignment decision

Status: aligned.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-example rule:

> An Evidence Log claim should show connected request, context, proposal, approval, execution, stop, and repair evidence, while also preserving explicit not-checked items and information-minimization boundaries.

## Next action

Proceed to the next inventory target:

- `articles/stop-authority-design.md`

Keep review incremental. Stop Authority should be reviewed before adding an example that claims complete human return or evidence reconstruction.
