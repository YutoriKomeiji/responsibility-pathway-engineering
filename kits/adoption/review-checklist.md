# RPE Adoption Kit Review Checklist

This checklist helps a reader inspect one bounded Responsibility Pathway Engineering (RPE) adoption-kit draft record.

Use it after reading:

- `kits/adoption/README.md`
- `kits/adoption/non-claims.md`
- `kits/adoption/quickstart.md`

The checklist is an inspection aid only.

It does not approve, certify, validate, assure, conform, legally review, safety review, compliance review, fairness review, production-approve, or prove any record, workflow, AI system, organization, fork, deployment, or external use.

A checked box means only that the reviewer observed the item in the draft record.

It does not mean the item is correct, sufficient, accepted, safe, lawful, fair, complete, production-ready, or externally endorsed.

## Intended use

Use this checklist when reviewing one small AI-assisted work record prepared with the adoption kit.

Good first uses include:

- internal meeting-summary draft review
- AI-assisted note review
- reversible planning record review
- non-production workflow observation
- internal documentation update review

Do not use this checklist as a shortcut for legal, safety, compliance, fairness, medical, financial, disciplinary, or production approval.

## Review status

Record the status before checking details.

```yaml
review_status:
  work_item_title: ""
  record_path_or_location: ""
  reviewer: ""
  review_date: "YYYY-MM-DD"
  checklist_status: "draft | in_review | blocked | completed_for_inspection"
  approval_status_of_record: "draft | under_review | approved_by_named_human_or_institution | rejected | reopened | blocked"
```

`completed_for_inspection` is not approval.

Approval, if any, must be separately recorded with a named human or institution.

## 1. Bounded scenario

Check whether the record describes one bounded case.

- [ ] The work item has a short title.
- [ ] The scenario boundary is visible.
- [ ] The case is small enough to inspect.
- [ ] The case is not treated as representative of all RPE use.
- [ ] The case is not presented as production readiness.
- [ ] The case does not rely on hidden external approval.

Stop or revise if:

- the scenario is too broad to inspect
- the record jumps from one example to a general claim
- the record is being used to approve external action without a local review gate

## 2. Responsibility holder

Check whether the responsible human or institution remains visible.

- [ ] A responsible human or institution is named.
- [ ] The responsible party is not an AI tool, model, agent, checker, template, or repository.
- [ ] The record says who reviews, approves, rejects, publishes, acts on, or reopens the work.
- [ ] If responsibility is shared, roles are separated.
- [ ] The record does not imply AI final-responsibility transfer.

Reviewer note:

```yaml
responsibility_holder_review:
  visible_responsibility_holder: true
  unclear_roles: []
  ai_as_final_holder_detected: false
```

Stop or revise if the responsible human or institution cannot be identified.

## 3. AI assistance boundary

Check whether AI assistance is described without turning into authority.

- [ ] The record says where AI assisted.
- [ ] The record says what AI did not decide.
- [ ] The record separates draft generation from review.
- [ ] The record separates suggestion from approval.
- [ ] The record does not treat model output as evidence by itself.
- [ ] The record does not treat AI fluency as correctness.

Examples of safe wording:

```text
AI drafted the first summary; the human reviewer remains responsible for review and approval.
```

```text
AI suggested checklist items; the reviewer selected, changed, or rejected them.
```

Unsafe patterns:

```text
AI approved the result.
```

```text
The model said this is compliant.
```

```text
The summary is reliable because AI generated it.
```

## 4. Evidence route

Check whether the record preserves where evidence came from.

- [ ] Checked sources are listed.
- [ ] Unchecked sources are listed separately.
- [ ] Missing context is visible.
- [ ] Assumptions are visible.
- [ ] Source relationship is clear when source links are used.
- [ ] A listed link or path is not treated as read content unless fetched or provided.
- [ ] Claims in the record point back to evidence or are marked as unsupported or tentative.

Reviewer note:

```yaml
evidence_route_review:
  checked_sources_visible: true
  unchecked_sources_visible: true
  missing_context_visible: true
  unsupported_claims: []
```

Stop or revise if evidence, unchecked sources, and missing context are collapsed into one field.

## 5. Source traversal honesty

Check whether the record avoids source traversal hallucination.

- [ ] The record distinguishes listed sources from read sources.
- [ ] The record distinguishes linked files from fetched files.
- [ ] The record does not summarize a linked file that was not fetched or provided.
- [ ] The record does not infer repository scope from a folder name alone.
- [ ] The record does not infer external source endorsement from a link.
- [ ] If current-page-only review is being performed, the record says so.

Suggested review phrase:

```text
This review is based only on the provided record and explicitly listed contents; linked files or sources were not treated as read unless their content was provided or fetched.
```

Stop or revise if the record claims knowledge of linked material that was not actually reviewed.

## 6. Review gate

Check whether review is separate from drafting.

- [ ] A review gate is named, if one exists.
- [ ] The record does not invent a review gate.
- [ ] The review gate is not confused with approval.
- [ ] The review gate is not confused with validation.
- [ ] The record says what happens if review has not happened yet.
- [ ] The repository itself is not treated as the reviewer.

Possible labels:

- no review yet
- author review only
- team review required
- policy owner review required
- legal review required
- safety review required
- compliance review required
- blocked until review

Only use review labels that match the actual local process.

## 7. Approval status

Check whether status is explicit.

- [ ] The record has an approval status.
- [ ] Draft, review, approval, validation, and certification are not collapsed.
- [ ] If approved, the approving human or institution is named.
- [ ] If not approved, the record says draft, under review, blocked, rejected, or reopened.
- [ ] Approval status is not inferred from checklist completion.
- [ ] Approval status is not inferred from checker results.

Stop or revise if the record uses vague status wording such as:

```text
looks good
```

```text
ready
```

```text
verified
```

without saying who approved what and within which boundary.

## 8. Return path

Check whether the record says where the work returns if challenged.

- [ ] There is a return path if the output is challenged.
- [ ] There is a return path if evidence is missing or outdated.
- [ ] There is a return path if harm, confusion, or unsupported use is found.
- [ ] There is a repair or reopening path.
- [ ] There is a stop-before-external-use path when needed.
- [ ] The return path points to a human, institution, review process, or named maintenance route.

Reviewer note:

```yaml
return_path_review:
  if_challenged: ""
  if_evidence_missing: ""
  if_harmful_or_incomplete: ""
  if_context_changes: ""
```

Stop or revise if the work can move forward but has nowhere to return.

## 9. Non-claims

Check whether excluded claims are visible before use.

The record should not be mistaken for:

- [ ] certification
- [ ] validation
- [ ] assurance
- [ ] conformity assessment
- [ ] legal review
- [ ] safety review
- [ ] compliance review
- [ ] fairness review
- [ ] production approval
- [ ] conformance evidence
- [ ] source endorsement
- [ ] institution-wide approval
- [ ] semantic responsibility proof
- [ ] runtime correctness proof
- [ ] adapter or connector correctness proof
- [ ] AI final-responsibility transfer

The boxes above are reminders of excluded claims.

They are not claims that the record has satisfied those domains.

## 10. Fork or reuse boundary

If the record, kit, or template will be copied, forked, or adapted, check local responsibility.

- [ ] The fork or reuse context is named.
- [ ] The local maintainer is responsible for local claims.
- [ ] Local policy, law, safety, compliance, or organizational process is not assumed from this repository.
- [ ] Examples are reviewed before being reused.
- [ ] Non-claims are preserved or made stricter.
- [ ] The original repository is not described as endorsing the fork.

Stop or revise if reuse would inherit claims without local review.

## 11. External use stop check

Before sharing, publishing, relying on, or acting externally, ask:

- [ ] Who remains responsible?
- [ ] Where did AI assist?
- [ ] What evidence was checked?
- [ ] What evidence was not checked?
- [ ] What context is missing?
- [ ] Who reviewed the record?
- [ ] Has anyone approved it?
- [ ] What does approval mean here?
- [ ] Where does the work return if challenged?
- [ ] What does this record explicitly not prove?

Stop before external use if any answer is unclear.

## Minimal review summary

A reviewer may summarize the inspection like this:

```yaml
rpe_adoption_review_summary:
  work_item_title: ""
  reviewed_record: ""
  responsibility_holder_visible: true
  ai_assistance_boundary_visible: true
  evidence_route_visible: true
  unchecked_sources_visible: true
  missing_context_visible: true
  review_gate_visible: true
  approval_status_visible: true
  return_path_visible: true
  non_claims_visible: true
  source_traversal_limitations_noted: true
  external_use_status: "not approved | blocked | local approval required | locally approved by named human or institution"
  reviewer_notes: []
```

This summary is a review note only.

It is not certification, validation, assurance, conformity evidence, approval, or proof.

## Human review remains required

This checklist can help a person notice whether required responsibility-path fields are present.

It cannot determine whether:

- the responsible party is legally sufficient
- evidence is complete
- source interpretation is correct
- missing context is acceptable
- a review gate is adequate
- an approval is valid
- a return path is socially or institutionally sufficient
- a workflow is safe, compliant, fair, lawful, or production-ready
- an AI reader actually fetched linked content
- a fork preserved the original boundary

Human or institutional review remains required.

## Stop conditions

Stop or revise if this checklist is used to:

- approve a record merely because boxes are checked
- replace local review
- replace legal, safety, compliance, or fairness review
- certify or validate an AI-assisted workflow
- imply production readiness
- treat checker output as proof
- treat linked files as read content
- hide unchecked sources or missing context
- hide who remains responsible
- transfer final responsibility to AI

## Next safe step

After this checklist, a later PR may add a short fork-localization note under:

```text
kits/adoption/notes/fork-localization-note.md
```

That note should explain how downstream maintainers can adapt the adoption kit without inheriting overclaims from the original repository.
