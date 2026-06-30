# Templates

This directory contains copyable starting points for Responsibility Pathway Engineering records and adoption surfaces.

These templates are lightweight adoption artifacts. They are not certification records, conformance evidence, production approval, legal review, safety review, compliance review, fairness review, social acceptance proof, or AI final-responsibility transfer mechanisms.

## RPE distinction

These templates should not be treated as generic AI-use disclosure forms.

They are intended to preserve whether judgment, evidence, review, repair, and responsibility can return to a human or institution when AI-assisted work is wrong, unclear, incomplete, unsupported, harmful, or disputed.

See `docs/issue-form-rpe-originality-note.md` for the RPE-specific design anchors: returnability, non-final-AI boundary, and repair / dispute / reopening path.

## Current templates

- `ai-assisted-work-responsibility-path.yaml` - a first under-construction copyable YAML template for recording AI-assisted work responsibility paths.
- `.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml` - a GitHub Issue Form for the same kind of record inside GitHub issue workflows.

## Guides and demos

- `docs/issue-form-user-guide.md` - English user guide for the GitHub Issue Form.
- `docs/issue-form-demo-ai-assisted-work.md` - English filled example for an AI-assisted PR review scenario.
- `docs/issue-form-user-guide.ja.md` - Japanese user guide for the GitHub Issue Form.
- `docs/issue-form-demo-ai-assisted-work.ja.md` - Japanese filled example for an AI-assisted PR review scenario.

## How to use

Use either route:

1. Copy `templates/ai-assisted-work-responsibility-path.yaml` into your own repository, issue, review process, or documentation workflow.
2. Use the GitHub Issue Form when the responsibility-path record should live as a repository issue.

Keep the non-claim boundary visible when adapting a template.

## Evidence and time-order guidance

When recording evidence, preserve time-order reviewability where possible.

Use:

- `observed_at` for when the evidence, source, log, message, test result, or review signal was observed,
- `recorded_at` for when it was written into the responsibility-path record,
- `timezone` for the time zone used by the timestamps.

These fields help later readers understand whether evidence existed before or after a decision, review, repair, dispute, or reopening step.

They do not prove that the evidence is true, complete, legally sufficient, safe, compliant, fair, production-ready, externally reviewed, certified, conformance-ready, or responsibility-resolving.

## Construction status

Current templates should be treated as `under-construction` unless a later index or release note marks them otherwise.

Use `docs/repository-construction-status-labels.md` to interpret construction labels.

## Recommended first template

Start with:

`templates/ai-assisted-work-responsibility-path.yaml`

Use it when AI assistance was involved and you need to preserve:

- source reference
- actor or requester
- AI assistance boundary
- human or institutional review
- evidence, evidence timestamps, and missing context
- responsibility return point
- repair, dispute, or reopening path
- non-claims

## Boundary

A copied template or issue form can help preserve reviewability.

It does not prove correctness, legality, safety, compliance, fairness, production readiness, conformance, or final responsibility assignment.
