# Source Alignment: ai-responsibility-node.md

This note records a source-alignment review for the Zenn article on AI responsibility nodes.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/ai-responsibility-node.md`
- Title: `AI責任ノード――AIエージェントを責任経路で管理する`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align the public `AI責任ノード` framing with the repository's bounded AI support node and AI final-responsibility boundary.

## Article-level role

The article frames AI not as a final responsibility subject, not as a moral or legal person, and not as a static invisible tool. Instead, it treats AI as an operating unit on a responsibility pathway that should be identified, controlled, and recorded.

Current repository alignment:

- strongly aligned with AI support node modeling
- strongly aligned with the Phase 3 human-AI review workflow example
- strongly aligned with AI final-responsibility exclusion under the current minimal model
- supports making AI participation visible without assigning final responsibility to AI

Repository change decision:

- no immediate schema or Lean change required
- use caution before importing the phrase `AI responsibility node` into public repo-facing summaries because it can be misread as assigning responsibility to AI

## Responsibility boundary

The article explicitly states that AI responsibility nodes are not a concept for making AI bear responsibility. They are units for identifying, controlling, and recording how AI acted on a responsibility pathway.

Current repository alignment:

- directly supports `ai_participation.assumes_final_responsibility: false`
- directly supports the boundary that AI may participate as a node but final responsibility returns to humans, organizations, or institutions
- supports the repository's current wording that AI should not be personified as final responsibility holder

Repository change decision:

- preserve this article as source support for AI participation visibility
- do not rename current schema nodes without further design review

## Record-keeping and human oversight bridge

The article connects record-keeping and human oversight by asking, for each AI operating unit:

- which AI acted
- in what context
- with what authority
- which human understood, intervened, or could stop it
- which logs allow later reconstruction

Current repository alignment:

- strongly aligned with Evidence Log
- strongly aligned with Human Return Point
- strongly aligned with Stop Authority
- supports the review-result boundary between recorded facts and responsibility resolution

Repository change decision:

- no immediate checker change required
- useful source for future AI support-node example expansion

## Agent infrastructure boundary

The article compares AI responsibility nodes with agent identity, tool boundary, execution trace, memory, checkpoints, and human-in-the-loop infrastructure.

It distinguishes the goals:

- agent infrastructure keeps agents running, preserving state and execution history
- Responsibility Pathway Engineering preserves who accepts, stops, repairs, and returns responsibility after AI action

Current repository alignment:

- supports keeping RPE distinct from ordinary agent-runtime logging
- supports Phase 3 boundary against turning the repo into a large agent framework
- supports using reference examples only as small structural examples

Repository change decision:

- no runtime implementation change required
- if future examples use agent infrastructure terms, keep them illustrative and non-production

## Tool vs. god boundary

The article criticizes both extremes: treating AI as a mere tool and treating AI mainly through future ASI fear. It argues that today's organizational AI-agent risks appear in mail sending, file updates, API calls, master-data changes, customer-response drafts, approval UI, log design, and stop authority.

Current repository alignment:

- supports practical Phase 3 examples grounded in bounded workflows
- supports current human-AI review workflow example
- supports future examples for file update, API call, email draft, or ERP-like action classes

Repository change decision:

- no immediate new example yet
- useful source for choosing future examples after source alignment stabilizes

## AI as operating unit on responsibility pathway

The article defines the relevant operating unit as something that acts on human or organizational judgment, approval, execution, stopping, or repair pathways and changes that flow.

It states that AI is not human, not a corporation, and not a moral responsibility subject, but it acts on responsibility pathways and therefore should not be erased from them.

Current repository alignment:

- strongly supports AI support-node visibility
- strongly supports recording AI influence on human judgment environments
- supports not collapsing AI action into generic user responsibility or generic system execution

Repository change decision:

- no immediate schema change required
- possible future documentation note: AI involvement should be visible without becoming final responsibility ownership

## Legal and contract boundary

The article says legal, contractual, and regulatory questions matter, but responsibility-boundary discussions require prior identification of where AI acted, under what authority, and in which judgment, approval, or execution context.

Current repository alignment:

- supports the repository's pre-legal structural role
- supports non-certifying legal boundary language
- supports using RPE records as structural inputs, not legal decisions

Repository change decision:

- no legal claim should be added
- keep legal/contractual references as downstream context only

## AI Responsibility Capacity / ARC relation

The article links AI responsibility nodes to AI responsibility pathway device and AI Responsibility Capacity / ARC. It says:

- AI responsibility node: implementation/audit identification unit
- AI responsibility pathway device: AI-side support device for returning responsibility pathways to humans, organizations, and institutions
- ARC: viewpoint for evaluating support capability

Current repository alignment:

- related to existing `ai_participation` and AI support-node capability modeling
- may become useful for a bounded capability-profile note
- must not imply AI personhood, legal capacity, moral capacity, certification, or final responsibility

Repository change decision:

- do not add ARC to schema yet
- if revisited later, create `docs/ai-responsibility-capacity-boundary.md` first

## Implementation component alignment

The article maps AI responsibility nodes to multiple RPE parts:

- Responsibility Pathway Layer
- Action Class Matrix
- Evidence Log
- External Oversight Pathway
- Stop Authority
- Human Return Point
- Repair Owner
- Decision Owner

Current repository alignment:

- strongly aligned with current element vocabulary
- introduces `External Oversight Pathway`, which is not yet a core schema object in the repository
- supports future discussion of external oversight only as a bounded extension

Repository change decision:

- no immediate schema change
- record `External Oversight Pathway` as a possible future source-alignment concept, not a current committed element

## Enterprise example alignment

The article gives an invoice-processing example in which AI reads invoices, compares purchase information, proposes payment candidates, a human approves, and ERP performs voucher processing.

It models the AI node with:

- target business process
- action class
- reference scope
- proposal content
- Human Return Point
- Evidence Log
- Stop Authority
- Repair Owner

Current repository alignment:

- high-value source for future enterprise reference example design
- closely related to SAP/ERP implementation context
- must remain illustrative and non-production

Repository change decision:

- no immediate example addition
- possible future Phase 3 candidate only after source alignment and checker boundaries remain stable

## Claim-strength assessment

Compatible claims:

- AI should not be treated as final responsibility holder under current assumptions
- AI should not be erased as a mere invisible tool if it affects judgment, approval, execution, stopping, repair, or evidence
- AI participation can be identified, controlled, and recorded structurally
- AI nodes must be connected to Decision Owner, Human Return Point, Stop Authority, Evidence Log, and Repair Owner
- legal and contractual responsibility questions require prior structural reconstruction of AI action context

Claims to keep bounded:

- `AI責任ノード` as a term, because it can be misread as assigning responsibility to AI
- AI responsibility pathway device
- ARC
- External Oversight Pathway
- enterprise invoice-processing implementations
- comparisons with corporate personhood

Repository interpretation:

The article supports the repository's middle path: do not make AI a final responsibility subject, but do not hide AI participation inside generic human or system responsibility either.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-example rule:

> AI nodes should be visible as support or operating units in the pathway, but final decision, repair, closure, and responsibility ownership must remain routed to humans, organizations, or institutions.

## Next action

Proceed to the next inventory target:

- `articles/human-return-point.md`

Keep review incremental. Do not import ARC, External Oversight Pathway, or enterprise invoice examples into the main specification before additional source alignment and boundary documents are prepared.
