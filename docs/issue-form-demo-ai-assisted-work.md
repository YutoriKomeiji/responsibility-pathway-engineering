# AI-assisted Work Responsibility Issue Form Demo

This demo shows a simple filled example for the GitHub Issue Form.

It is a demo only. It is not certification, legal review, safety review, compliance review, fairness review, production approval, conformance evidence, social acceptance proof, or AI final-responsibility transfer.

## RPE focus

This demo is not only showing that AI was used.

It shows where the work can return if the AI-assisted review is wrong, unclear, incomplete, unsupported, or disputed.

The important fields are the AI assistance boundary, evidence log, missing context, responsibility return point, and repair / reopening path.

See `docs/issue-form-rpe-originality-note.md` for the RPE-specific design anchors.

## Scenario

A maintainer uses AI to summarize a pull request and highlight possible review risks.

The AI helps with summarization and review support. The maintainer remains responsible for review judgment.

## Example issue title

AI-assisted work responsibility path: PR review summary for documentation update

## Example filled fields

### Source reference

Pull request: `#42`

### Work context

A documentation pull request updates the project README and adds a new usage section.

Requester: contributor

Responsible person or team: repository maintainer

Affected area: public documentation

Expected outcome: clearer reader path without expanding certification or production-readiness claims

### AI assistance role

review_support

### AI assistance boundary

The AI summarized the pull request, identified possible ambiguity in the new usage section, and suggested review questions.

The AI did not approve the pull request, decide correctness, decide legal validity, decide safety, decide compliance, or become the final responsibility holder.

### Human or institutional review

Reviewer: repository maintainer

Review status: pending

Approval gate: maintainer review before merge

### Approval skip or transfer, if any

No approval skip occurred.

### Evidence log

- PR diff
- README before and after the change
- related issue discussion
- local markdown preview

### Missing context or uncertainty

- The new wording may sound stronger than intended.
- The usage section may need a clearer non-claim boundary.

### Responsibility return point

Return to the repository maintainer if the merged wording creates confusion, overclaiming, or unclear responsibility boundaries.

### Repair, dispute, or reopening path

Open a follow-up issue or revert/patch the README section if the wording misleads readers.

### Non-claim boundary

This issue does not certify correctness, legal validity, safety, compliance, fairness, production readiness, conformance, or final responsibility assignment.

The AI-assisted review is a support record only.

## What this demonstrates

This example shows how an issue can preserve:

- what AI helped with
- what AI did not decide
- what evidence was reviewed
- who must review or approve
- where the path returns if the result is wrong
- how the record can be repaired or reopened
