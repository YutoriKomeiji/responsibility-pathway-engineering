# RPE Tool Proposal Template

This template is for small, searchable Responsibility Pathway Engineering tool proposals.

Use it when publishing an experimental RPE tool, template, checker, browser aid, formal fragment, or paper-to-RPE prototype.

The purpose is to make the proposal discoverable through accurate area terms, related keywords, and source links while preserving non-claims.

This template does not certify, validate, assure, conform, approve, or prove any tool, record, AI system, workflow, organization, paper interpretation, or downstream use.

## Proposal title

```text
RPE Tool Proposal: <short searchable title>
```

Good title pattern:

```text
RPE Tool Proposal: Traceability helper for AI-assisted review records
```

Avoid titles that imply certification, assurance, validation, conformance, or solved responsible AI.

## Short summary

```text
This prototype explores whether <artifact type> can make <responsibility-path concern> easier to inspect in <bounded scenario>. It is not certification, validation, assurance, conformity assessment, legal review, safety review, compliance review, fairness review, production approval, or AI final-responsibility transfer.
```

## Discovery metadata

```yaml
discovery:
  area_terms:
    - "Responsible AI"
    - "traceability"
  related_keywords:
    - "responsibility holder"
    - "AI-assisted work record"
    - "review gate"
    - "return path"
  source_links:
    - url: ""
      title: ""
      source_type: "paper"
      date_checked: "YYYY-MM-DD"
      relationship_note: "Used as context for a responsibility-path concern; not an endorsement."
  rpe_problem_statement: ""
  rpe_tool_angle: ""
  implementation_surface: "YAML | Python | JavaScript | Lean4 | Markdown | mixed"
  tool_status: "prototype"
  feedback_requested: true
  non_claims:
    - "not certification"
    - "not validation"
    - "not assurance"
    - "not conformity assessment"
    - "not legal review"
    - "not safety review"
    - "not compliance review"
    - "not fairness review"
    - "not production approval"
    - "not AI final-responsibility transfer"
```

The metadata block is for discovery and review.

It is not evidence that the proposal satisfies the listed area terms or source requirements.

## Area terms

List broad terms that genuinely match the proposal.

Examples:

- Responsible AI
- Explainable AI
- Safe AI
- Verified AI
- AI verification
- TEVV
- AI assurance
- conformity assessment
- provenance
- traceability
- record-keeping
- cryptographic verifiability

Only include a term when the proposal directly maps to a responsibility-path concern associated with that term.

Do not add keywords only for search traffic.

## Related keywords

List more specific phrases that match the actual tool contents.

Examples:

- responsibility holder
- human oversight
- review gate
- approval status
- evidence route
- missing context
- source provenance
- traceable decision path
- accountable workflow
- audit trail
- tamper-evident record
- signed manifest
- model output review
- AI-assisted work record
- disputed output return path

## Source links

Use this section when the proposal is inspired by a paper, technical report, standard, guidance document, public incident write-up, benchmark, framework, or project documentation.

```text
Source:
- Title:
- URL:
- Source type:
- Date checked:
- Relationship to this proposal:
```

Relationship note examples:

```text
This source is used as public context for a responsibility-path concern. It does not endorse this tool proposal.
```

```text
This proposal extracts one RPE angle from the source. It does not claim to represent the authors' intent.
```

```text
This source discusses a broader problem. This prototype only explores one bounded responsibility-path artifact.
```

## Observed problem

Describe the problem in responsibility-path terms.

Good examples:

- The output may be reused without a visible human responsibility holder.
- The evidence route behind an AI-assisted review is hard to inspect.
- A checker result may be mistaken for approval.
- A generated artifact may hide unchecked sources.
- A disputed output may have no visible return path.

Avoid:

- This solves Responsible AI.
- This proves explainability.
- This verifies safety.
- This satisfies TEVV.
- This performs conformity assessment.

## RPE translation

Map the observed problem into RPE fields.

```yaml
rpe_translation:
  responsibility_holder: ""
  ai_assistance_boundary: ""
  evidence_route: ""
  unchecked_sources: []
  missing_context: []
  review_gate: ""
  approval_status: "draft | under review | approved externally | rejected | reopened | blocked"
  return_path: ""
  non_claims: []
```

## Tool made

Describe the actual artifact.

```text
Tool made:
- Artifact path:
- Language or format:
- Bounded function:
- Input:
- Output:
- Human review expected:
```

Examples:

```text
Tool made:
- Artifact path: tools/discovery/example-checker.py
- Language or format: Python
- Bounded function: checks whether selected local RPE records contain required fields
- Input: local YAML files
- Output: missing-field report
- Human review expected: yes
```

```text
Tool made:
- Artifact path: docs/tool-proposals/example.md
- Language or format: Markdown and YAML
- Bounded function: shows one paper-to-RPE responsibility-path mapping
- Input: public source link and local proposal metadata
- Output: reviewable tool proposal
- Human review expected: yes
```

## What it may help with

Describe bounded usefulness.

Examples:

- make responsibility-path assumptions visible
- help a reviewer notice missing context
- preserve source-link relationship notes
- keep unchecked sources visible
- separate draft, review, approval, validation, and assurance
- show where a disputed result should return
- make a small prototype easier to discuss publicly

## What it does not prove

Include this section in every tool proposal.

```text
This proposal does not prove, certify, validate, assure, conform, approve, or guarantee anything about the relevant AI system, workflow, organization, record, paper interpretation, model behavior, runtime behavior, legal status, safety status, compliance status, fairness status, production readiness, or downstream use.
```

Also state as applicable:

- It does not replace human or institutional judgment.
- It does not perform legal review.
- It does not perform safety review.
- It does not perform compliance review.
- It does not perform fairness review.
- It does not provide conformity assessment.
- It does not provide TEVV.
- It does not create an accepted assurance case.
- It does not represent source-author endorsement.
- It does not transfer final responsibility to AI.

## How to try it

Explain the smallest safe trial path.

```text
1. Read the non-claims.
2. Inspect the source relationship note.
3. Run or copy the artifact only on a bounded, non-production case.
4. Treat output as draft review material.
5. Have a human or institution decide whether it is useful.
6. Stop before external reliance if the responsibility holder, review gate, approval status, evidence route, missing context, or return path is unclear.
```

## Feedback request

Ask for feedback as design input, not as validation.

Good questions:

- Does this match a real responsibility-path pain point?
- Are the area terms accurate?
- Are the source links relevant?
- Is the source relationship note clear?
- Which field is missing?
- Which boundary is too weak?
- Would this help a reviewer inspect a draft?
- Where would this fail in a real organization?

Feedback is not endorsement, validation, certification, assurance, conformity, acceptance, or approval.

## Public post stub

Optional public wording:

```text
I tried making a small RPE tool proposal for <area term>.

The idea is not to prove that an AI system is responsible, safe, explainable, verified, assured, or conformant.

The idea is narrower: take one responsibility-path concern from <source or topic>, turn it into an inspectable artifact, and ask whether the shape is useful.

Prototype: <artifact path or link>
Source context: <URL>
Non-claims: <short boundary>

If this touches a real pain point, feedback is welcome.
```

## Stop conditions

Stop or revise if the proposal:

- uses area terms that the artifact does not actually address
- cites a source as endorsement without evidence
- implies author intent without confirmation
- implies standards or regulatory compliance
- claims certification, validation, assurance, conformity, legal review, safety review, compliance review, fairness review, or production readiness
- hides uncertainty
- hides missing context
- treats visibility as proof
- treats feedback as acceptance
- treats a checker, YAML file, browser aid, or Lean4 fragment as sufficient by itself
- transfers final responsibility to AI

## Next safe step

After this template, the next safe step is one filled tool proposal example.

The first example should use a bounded, non-production responsibility-path concern and should include accurate keywords, a source relationship note, non-claims, and feedback questions.
