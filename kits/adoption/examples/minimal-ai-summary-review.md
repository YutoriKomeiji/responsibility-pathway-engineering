# Minimal AI Summary Review Example

This is a minimal filled example for the RPE Adoption Kit.

It shows one bounded, non-production AI-assisted work case: an internal meeting-summary draft prepared with AI assistance and reviewed by a human before any external use.

This example is illustrative only.

It does not approve, certify, validate, assure, or prove any real workflow, output, person, organization, AI system, checker result, fork, or downstream use.

## Read first

Before using this example, read:

1. `kits/adoption/README.md`
2. `kits/adoption/non-claims.md`
3. `kits/adoption/quickstart.md`
4. `kits/adoption/templates/ai-assisted-work-responsibility-path.md`

This example should be read after the non-claims and quickstart, not before them.

## Scenario boundary

The scenario is intentionally small:

- an internal meeting-summary draft
- prepared with AI assistance
- checked against local meeting notes by a human
- not sent outside the team
- not used for legal, safety, compliance, fairness, medical, financial, disciplinary, or production decisions
- not treated as an approved record

The scenario is not:

- a public statement
- a customer communication
- a policy approval
- a legal or compliance record
- a safety case
- a conformity assessment
- a TEVV result
- an assurance case
- a production workflow
- a model evaluation
- a cryptographic proof

## Filled minimal record

```yaml
work_item:
  title: "Internal meeting summary draft"
  scenario_boundary: "Non-production internal review of a short meeting-summary draft."
  status: "draft"

responsibility:
  responsible_human_or_institution: "Meeting note owner"
  ai_is_final_responsibility_holder: false

ai_assistance:
  tool_or_model: "AI drafting assistant"
  assistance_type: "Drafted a first summary from local notes supplied by the user."
  not_decided_by_ai: "AI did not approve the summary, decide what happened in the meeting, identify final action owners, or authorize external use."

evidence:
  checked_sources:
    - "Local meeting notes supplied by the note owner"
  unchecked_sources:
    - "Original audio recording, if any"
    - "Chat logs or side-channel discussion not included in the notes"
  missing_context:
    - "Whether all attendees agree with the action-item wording"
    - "Whether any sensitive or private details should be removed"
  uncertainty:
    - "The draft may omit discussion context not present in the local notes"
    - "The draft may misstate action ownership if the notes were incomplete"

review:
  reviewer_or_gate: "Meeting note owner review before sharing beyond the immediate drafting context"
  approval_status: "draft"
  approval_evidence: "No approval evidence recorded in this example"

return_path:
  if_challenged: "Return to the note owner and re-check against source notes"
  if_harmful_or_incomplete: "Withdraw draft use and reopen the meeting-note review"
  if_context_changes: "Update the draft or mark it outdated before reuse"

non_claims:
  not_certification: true
  not_validation: true
  not_legal_review: true
  not_safety_review: true
  not_compliance_review: true
  not_fairness_review: true
  not_production_approval: true
  not_conformance_evidence: true
  not_ai_final_responsibility_transfer: true
```

## What this example demonstrates

This example demonstrates a small responsibility-path shape:

- the work item is named
- the scenario boundary is limited
- the human responsibility holder is visible
- AI assistance is described
- AI non-decision is described
- checked and unchecked sources are separated
- missing context is recorded
- uncertainty is visible
- review is separate from approval
- approval status remains `draft`
- return paths are explicit
- non-claims are visible

## What should happen if this were used

A reader using this pattern should be able to produce one draft responsibility-path record for one bounded AI-assisted work case.

Before any external use, the reader should still ask:

- Who remains responsible?
- What did AI assist with?
- What did AI not decide?
- What evidence was checked?
- What evidence was not checked?
- What context is missing?
- Who reviews the draft?
- What is the current approval status?
- Where does the result return if challenged, harmful, incomplete, unsupported, or outdated?
- What claims are explicitly excluded?

If any answer is unclear, the record should stop before external use.

## What this example does not demonstrate

This example does not demonstrate:

- certification
- validation
- assurance
- conformity assessment
- TEVV
- legal review
- safety review
- compliance review
- fairness review
- production readiness
- model correctness
- runtime correctness
- adapter correctness
- connector correctness
- cryptographic verifiability
- semantic responsibility proof
- complete provenance
- complete traceability
- institutional approval
- AI final-responsibility transfer

## RPE function

Inside Responsibility Pathway Engineering, this example supports **first-case record demonstration**.

Its role is to make the adoption kit concrete without turning the example into proof.

It supports:

- responsibility localization
- AI assistance boundary preservation
- evidence route visibility
- missing-context visibility
- review and approval separation
- return-path construction
- non-claim preservation

## Fork note

A fork maintainer may adapt this example to a local context.

When adapting it, the maintainer should replace the fictional scenario with a real local boundary and remove any unsupported implication that review, approval, assurance, compliance, safety, fairness, or production readiness has occurred.

The original repository does not endorse downstream adaptations merely because this example was copied.

## Next file to add

The next safe file should be `kits/adoption/review-checklist.md`.

That checklist should help a reader review one draft responsibility-path record before external use while preserving non-claims and human or institutional responsibility holders.
