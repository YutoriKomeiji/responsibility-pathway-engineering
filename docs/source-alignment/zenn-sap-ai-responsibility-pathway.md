# Source Alignment: sap-ai-responsibility-pathway.md

This note records a source-alignment review for the Zenn article on SAP / ERP and AI responsibility pathways.

It is based on the Markdown source in `YutoriKomeiji/zenn-content`, not on a Web-rendered page.

## Source article

- Source repository: `YutoriKomeiji/zenn-content`
- Source path: `articles/sap-ai-responsibility-pathway.md`
- Title: `SAP×AI時代の責任経路工学――ERP接続編`
- Published flag in frontmatter: `true`
- Review status: reviewed
- Review purpose: align the SAP / ERP article with the repository's bounded enterprise-system, evidence, stop, repair, and non-production example boundaries.

## Article-level role

The article frames SAP / ERP as a business platform where responsibility pathways are already embedded through approvals, authorities, evidence, documents, master data, accounting, purchasing, sales, inventory, manufacturing, HR, audit, operations, and repair.

It argues that connecting AI to SAP / ERP is not merely adding a convenience feature; it is connecting AI to enterprise responsibility pathways.

Current repository alignment:

- strongly aligned with enterprise AI-agent source notes
- strongly aligned with Action Class Matrix, Evidence Log, Stop Authority, Human Return Point, and Repair Owner
- supports future ERP-specific examples only with strong non-production boundaries

Repository change decision:

- no immediate schema change required
- high-value source for a future ERP/SAP example after generic examples stabilize

## Product-comparison boundary

The article explicitly states that it is not explaining SAP product features or implementation procedures and is not evaluating any specific vendor product.

Current repository alignment:

- supports non-product and non-vendor-evaluation boundaries
- supports keeping SAP / ERP examples illustrative rather than vendor-specific claims
- supports avoiding SAP capability, deployment, or certification claims

Repository change decision:

- no product comparison should be added
- if future SAP/ERP examples are added, they should be generic and synthetic unless explicitly scoped

## ERP as responsibility-pathway concentration

The article says ERP records who entered data, who approved, which document was created, which master data was used, and when accounting was affected. Therefore ERP holds responsibility pathways as documents, master data, approvals, authority, and logs.

Current repository alignment:

- strongly supports treating enterprise systems as responsibility-pathway carriers
- supports mapping AI actions to existing enterprise-process responsibility boundaries
- supports future examples involving documents, master data, approval, and audit traces

Repository change decision:

- no immediate definition change required
- possible future concept note: enterprise systems as responsibility-pathway carriers

## AI impact on ERP responsibility pathway

The article says AI can enter before business judgment, before approval, before execution, and sometimes close to execution itself. This lengthens and broadens responsibility pathways across AI proposals, human approval, SAP processing, BTP integration, AI Core jobs, and external services.

Current repository alignment:

- strongly aligned with AI support-node visibility
- supports not hiding AI under generic user responsibility or generic system execution
- supports linked Evidence Log across systems

Repository change decision:

- no immediate schema change required
- future ERP examples should separate AI proposal, human adoption, SAP document creation, BTP/AI execution, and external processing

## Joule / BTP / AI Core / Business Data Cloud boundary

The article discusses SAP Business AI, Joule, BTP, AI Core, Business Data Cloud, and external AI services as contexts where business data, process, approvals, and audit logs are close to AI.

It asks questions about contracts, billing, first response after failure, log connections, auditability of AI Core execution history, what business departments approve, IT responsibility, and vendor / external-service responsibility boundaries.

Current repository alignment:

- useful enterprise-system context
- must not become a claim about SAP product behavior, SAP compliance, or BTP/AI Core certification
- supports future examples involving cross-system trace IDs and contractual/billing boundaries as explicit assumptions

Repository change decision:

- no SAP product claim should be added
- no contractual or billing legal conclusion should be added
- future examples may include placeholders for external responsibility boundaries

## Data-path Evidence Log alignment

The article says that as AI reference data expands beyond SAP documents and master data into Business Data Cloud and external data platforms, the data pathway itself becomes part of Evidence Log. It asks what data was referenced, which point-in-time data was used, and how SAP-side evidence connects to external-data evidence.

Current repository alignment:

- strongly aligned with Context Log and Evidence Log concepts
- supports preserving data references rather than only AI outputs
- supports information-minimization and synthetic-example boundaries

Repository change decision:

- no immediate schema addition
- high-value source for future data-context evidence examples

## Master-data responsibility pathway

The article identifies master-data change as especially heavy in ERP contexts because customers, vendors, materials, prices, accounts, cost centers, authorities, and organizational structure affect downstream processing.

It says AI master-change proposals require clarity about whether AI only proposes or updates, which master record changes, downstream impact, before/after differences, business approval, IT/business/admin approval roles, rollback, history connection across SAP and AI, and repair responsibility after mistakes.

Current repository alignment:

- strongly aligned with Action Class Matrix and high-impact / irreversible boundaries
- strongly aligned with Human Return Point and Approval Gate
- strongly aligned with rollback and Repair Owner boundaries

Repository change decision:

- no immediate example addition
- master-data change is a high-value but high-risk future example; keep synthetic and heavily bounded

## Document-processing responsibility pathway

The article discusses purchase requests, invoice reading, incoming-payment clearing candidates, journal-entry proposals, and exception-handling proposals.

It says these must separate AI-generated candidates, human adoption judgment, SAP-registered documents, approval workflow, accounting effect, downstream processing, and correction / cancellation / reposting.

Current repository alignment:

- strongly aligned with the human-AI review workflow example
- supports future invoice-processing example only with explicit action-class and rollback boundaries
- supports separating proposal from execution and execution from accounting effect

Repository change decision:

- no immediate example addition
- possible future enterprise example after source-alignment phase is complete

## Approval workflow alignment

The article states that SAP / ERP approval workflows already exist, but AI changes the meaning of approval. If a human approves an AI-generated proposal, the approver must know whether they approved the AI proposal, the AI's evidence, the diff, the business impact, or downstream processing impact.

It says approval screens need generated content, referenced data, change diff, impact scope, uncertainty, alternatives, rollback availability, and post-approval execution effect.

Current repository alignment:

- strongly aligned with Human Return Point
- strongly aligned with Approval Log and Evidence Log
- supports not treating approval button as meaningful human return by itself

Repository change decision:

- no immediate checker change
- useful source for future approval-screen negative/positive examples

## SAP / BTP / AI log connection

The article states that multiple logs are insufficient unless connected. It proposes connections such as AI Request ID -> AI Proposal ID -> Approval ID -> SAP Document Number -> BTP Execution Log -> AI Core Job Log -> Stop / Repair Log.

Current repository alignment:

- strongly aligned with Evidence Log ID design
- supports future linked-ID examples
- supports cross-system traceability without claiming production audit readiness

Repository change decision:

- no immediate schema change
- possible future ERP-specific evidence-flow fixture after generic evidence-log fixture exists

## SAP-context Responsibility Pathway Layer mapping

The article maps RPL elements to SAP contexts:

- Decision Owner: business department / business owner
- Approval Gate: approval workflow, authority, change management
- Execution Actor: SAP, BTP, AI Core, external API, AI agent
- Stop Authority: business stop, job stop, permission stop, external integration stop
- Evidence Log: SAP change history, BTP logs, AI logs, approval logs
- Repair Owner: business repair, data correction, customer response, incident response
- Human Return Point: approval screen, diff review, exception handling, audit review

Current repository alignment:

- strongly aligned with current element vocabulary
- supports enterprise mapping examples
- must remain illustrative and not vendor-certified

Repository change decision:

- no immediate schema change
- high-value source for future `docs/enterprise-system-mapping.md`

## SAP / ERP staged adoption boundary

The article stages SAP / ERP AI connection by responsibility-pathway maturity:

- Level 0: no production connection
- Level 1: reference / summary only
- Level 2: document / master candidate generation
- Level 3: approved reversible operation
- Level 4: limited high-impact operation
- Level 5: production expansion

Current repository alignment:

- useful enterprise guidance
- not a formal maturity model or SAP readiness standard
- supports limiting examples by responsibility-pathway maturity

Repository change decision:

- no maturity model added
- future guidance should keep this staged model non-certifying

## Clean Core boundary

The article links Clean Core to responsibility pathways by arguing that custom AI extensions should not obscure which processing is standard, which is extension, and which decision is AI-derived. If responsibility pathways become untraceable, audit and repair become difficult.

Current repository alignment:

- useful SAP-context source
- must not become a SAP Clean Core certification or implementation prescription
- supports traceability and repairability as design concerns

Repository change decision:

- no Clean Core claim should be added to core spec
- keep as SAP-context guidance only

## ERP connection checklist alignment

The article provides a checklist across target area, master data, documents, approval, logs, stop, repair, contract, billing, SLA, and vendor boundaries.

Current repository alignment:

- strongly aligned with enterprise checklist note
- supports future SAP/ERP example boundaries
- must not become production-readiness certification

Repository change decision:

- no immediate example addition
- possible future ERP checklist boundary document after ISO/source reviews

## PoC-to-production boundary

The article states that SAP / ERP PoC and production differ significantly. Production adds real data, production authority, real transactions, accounting effects, audit, month-end close, customer response, incident response, billing, and SLA.

Current repository alignment:

- strongly aligned with reference-implementation boundary
- supports non-production synthetic examples
- supports refusal to claim production readiness

Repository change decision:

- no production claim should be added
- keep future ERP examples synthetic and bounded

## Claim-strength assessment

Compatible claims:

- ERP systems carry responsibility pathways through documents, master data, approvals, authority, and logs
- connecting AI to ERP connects AI to enterprise responsibility pathways
- AI proposal, human approval, ERP document creation, BTP/AI Core jobs, and external services must be distinguishable
- master-data and document processing require strong Evidence Log, Human Return Point, Stop Authority, and Repair Owner design
- SAP / BTP / AI logs must be linkable for responsibility-pathway reconstruction
- PoC success does not imply production responsibility-pathway readiness

Claims to keep bounded:

- SAP product evaluation
- SAP implementation procedure
- Clean Core certification or prescription
- production readiness
- compliance / audit / legal / safety certification
- vendor responsibility legal allocation
- contractual or billing conclusions

Repository interpretation:

This article is highly useful for future enterprise-system examples. It should not force immediate schema changes, but it strengthens the case for keeping enterprise examples synthetic, trace-ID oriented, and non-production.

## Repository alignment decision

Status: aligned with caution.

No immediate change is required to definitions, schemas, checkers, Lean assumptions, or Phase 3 examples.

This article supports the following future-example rule:

> ERP/SAP examples should separate AI proposal, human adoption, ERP execution, cross-system logs, stop authority, repair ownership, and organizational responsibility, while avoiding product, compliance, legal, audit, or production-readiness claims.

## Next action

Proceed to the next inventory target:

- `articles/iso42001-responsibility-pathway.md`

Keep review incremental. The ISO source review should determine how to discuss standards-adjacent material without turning the repository into a compliance framework.
