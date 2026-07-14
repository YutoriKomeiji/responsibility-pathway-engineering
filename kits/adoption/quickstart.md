# RPE Adoption Kit Quickstart

This quickstart gives a short first-use path for one bounded AI-assisted work case.

Use it after reading:

- `kits/adoption/README.md`
- `kits/adoption/non-claims.md`

This file does not add a template, example, checklist, checker, workflow, or production process. It only explains the first safe path through the adoption kit.

## Before you start

Confirm these boundaries first:

- A draft record is not an approved record.
- A completed template is not certification.
- A checker pass is not validation.
- A filled example is not production evidence.
- A fork is not endorsement by the original repository.
- Final responsibility remains with the relevant human or institution.

Do not use this quickstart to approve legal, safety, compliance, fairness, medical, financial, disciplinary, or production decisions.

## Choose one bounded case

Start with a small case that can be inspected without external impact.

Good first cases:

- an internal document update
- an AI-assisted summary for review
- a draft note prepared with AI assistance
- a reversible planning aid
- a non-production workflow observation

Avoid first cases that involve:

- irreversible external action
- direct public communication
- safety-sensitive operation
- legal, medical, financial, or workplace disciplinary decision
- production runtime integration
- service-specific connector operation
- public claims of certification, conformance, approval, or standardization

## First-use steps

### 1. Name the work item

Write a short title for the work item.

Examples:

- Internal meeting summary draft
- AI-assisted policy note draft
- Draft customer FAQ review note
- Non-production workflow observation

Purpose in RPE:

- Give the responsibility path a stable reference point.

### 2. Identify the responsible human or institution

Write who remains responsible for reviewing, approving, publishing, acting on, or rejecting the work.

Do not list an AI tool as the final responsibility holder.

Purpose in RPE:

- Responsibility localization.

### 3. Describe where AI assisted

Record how AI was used.

Examples:

- drafted a first summary
- proposed wording
- reorganized notes
- suggested checklist items
- helped compare alternatives

Also record what AI did not decide.

Purpose in RPE:

- Boundary preservation between assistance and responsibility.

### 4. Record source material and evidence

List the sources, files, observations, or inputs used.

Also record which sources were not checked.

Purpose in RPE:

- Evidence route preservation.

### 5. Record missing context and uncertainty

Write what is still unknown.

Examples:

- source document not fully reviewed
- stakeholder has not confirmed
- legal or safety context not checked
- policy owner not identified
- output may omit edge cases

Purpose in RPE:

- Prevent formal-looking records from hiding uncertainty.

### 6. Identify the review gate

Write who reviews the draft before external use or reliance.

Examples:

- author review
- team lead review
- policy owner review
- legal review
- safety review
- compliance review

Only include a review gate if it actually exists.

Do not imply that this repository provides the review.

Purpose in RPE:

- Keep review separate from drafting.

### 7. Identify approval status

Record the current status clearly.

Use simple labels such as:

- draft
- under review
- approved by named human or institution
- rejected
- reopened
- blocked

Do not treat draft, review, approval, and validation as the same thing.

Purpose in RPE:

- Prevent status collapse.

### 8. Define the return path

Write where the result returns if it is challenged, disputed, harmful, incomplete, unclear, outdated, or unsupported.

Examples:

- return to author for correction
- return to reviewer for recheck
- reopen source evidence review
- escalate to policy owner
- stop before publication
- withdraw external use

Purpose in RPE:

- Return-path construction.

### 9. Apply non-claims before use

Before using, sharing, publishing, or relying on the record, reread `kits/adoption/non-claims.md`.

Ask:

- What could this record be mistaken as proving?
- What does it actually show?
- Who remains responsible?
- What review has not happened?
- What context remains missing?

Purpose in RPE:

- Non-claim preservation at the point of use.

### 10. Stop before external use if the path is unclear

Stop if any of these are unclear:

- responsible human or institution
- AI assistance boundary
- source evidence
- missing context
- review gate
- approval status
- return path
- excluded claims

Purpose in RPE:

- Human gate preservation.

## Minimal draft shape

Until a dedicated adoption-kit template exists, use this as a lightweight draft shape:

```text
work_item:
  title: ""
  scenario_boundary: ""
  status: "draft"

responsibility:
  responsible_human_or_institution: ""
  ai_is_final_responsibility_holder: false

ai_assistance:
  tool_or_model: ""
  assistance_type: ""
  not_decided_by_ai: ""

evidence:
  checked_sources: []
  unchecked_sources: []
  missing_context: []
  uncertainty: []

review:
  reviewer_or_gate: ""
  approval_status: "draft"
  approval_evidence: ""

return_path:
  if_challenged: ""
  if_harmful_or_incomplete: ""
  if_context_changes: ""

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

This shape is temporary quickstart material.

A future PR may add a dedicated template or a pointer to an existing source template.

## What should happen after using this quickstart

After using this quickstart, a reader should have:

- one draft responsibility-path record
- a visible human or institutional responsibility holder
- a visible AI assistance boundary
- visible evidence and missing context
- visible review and approval status
- a visible return, repair, dispute, or reopening path
- visible non-claims

The reader should not have:

- approval
- certification
- validation
- legal review
- safety review
- compliance review
- fairness review
- production readiness
- conformance evidence
- semantic responsibility proof
- AI final-responsibility transfer

## Next file to add

The next safe file should be a template pointer or local template copy under `kits/adoption/templates/`.

That step should decide whether to link to `templates/ai-assisted-work-responsibility-path.yaml` or copy a kit-local version with drift and source-reference notes.
