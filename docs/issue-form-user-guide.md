# AI-assisted Work Responsibility Issue Form User Guide

This guide explains how to use the GitHub Issue Form for AI-assisted work responsibility paths.

It is a usage guide only. It is not certification, legal review, safety review, compliance review, fairness review, production approval, conformance evidence, social acceptance proof, or AI final-responsibility transfer.

## RPE distinction

This form is not only an AI-use disclosure form.

Its RPE-specific purpose is to preserve where judgment, evidence, review, repair, and responsibility can return when AI-assisted work is wrong, unclear, incomplete, unsupported, or disputed.

See `docs/issue-form-rpe-originality-note.md` for the design anchors.

## What it is for

Use the issue form when AI assistance was involved in work and the repository should preserve a responsibility path as an issue.

Typical uses:

- AI-assisted pull request review
- AI-assisted issue triage
- AI-assisted drafting of documentation or specifications
- AI-assisted log summarization
- AI-assisted incident note preparation
- AI-assisted decision support that still requires human or institutional review

## What it records

The issue form records:

- source reference
- work context
- AI assistance role
- AI assistance boundary
- human or institutional review
- approval skip or transfer, if any
- evidence log
- missing context or uncertainty
- responsibility return point
- repair, dispute, or reopening path
- non-claim boundary

## How to use it

1. Open a new GitHub issue.
2. Select `AI-assisted work responsibility path`.
3. Fill in each field with short, concrete information.
4. Link the issue from the related pull request, document, incident note, or review thread.
5. Update the issue if review status, evidence, uncertainty, or return point changes.

## Practical effect

The form helps make AI-assisted work reviewable.

It helps future readers answer:

- What did AI assist with?
- What did AI not decide?
- What evidence was used?
- Who reviewed or still needs to review the work?
- Where does the responsibility path return if something is wrong?
- How can the work be repaired, disputed, or reopened?

## When not to use it

Do not use this form as a substitute for legal review, safety review, compliance review, security review, production approval, external review, or formal certification.

Do not use it to claim that AI became the final responsibility holder.

## Relation to the YAML template

Use `templates/ai-assisted-work-responsibility-path.yaml` when you want a copyable file-based record.

Use `.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml` when you want the record to live as a GitHub issue.

Both are lightweight, under-construction, and non-certifying.
