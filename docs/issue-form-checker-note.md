# Issue Form Checker Note

This note explains the bounded checker for the AI-assisted work GitHub Issue Form.

It is a maintenance note only. It is not certification, legal review, safety review, compliance review, fairness review, production approval, conformance evidence, social acceptance proof, or AI final-responsibility transfer.

## Checker

- Script: `scripts/check_issue_form.py`
- Default target: `.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml`
- Workflow: `.github/workflows/check-issue-form.yml`

## Purpose

The checker verifies that the Issue Form definition preserves selected Responsibility Pathway Engineering structural signals.

It helps prevent the form from drifting into a generic AI-use disclosure form.

## What it checks

The checker currently checks that the form definition contains:

- expected top-level GitHub Issue Form keys
- source reference field
- work context field
- AI assistance role field
- AI assistance boundary field
- human or institutional review field
- evidence log field
- responsibility return point field
- repair / reopening field
- non-claim checkbox field
- required non-claim checkbox options
- non-final-AI responsibility boundary text
- selected non-claim boundary keywords

## What it does not check

The checker does not validate the actual content of a created issue.

It does not judge whether a user wrote a good return point, strong evidence, sufficient review, valid repair path, or acceptable decision.

It does not verify URLs, tests, reviewers, approvals, legal validity, safety, compliance, fairness, production readiness, social acceptance, conformance, or final responsibility assignment.

## Meaning of PASS

PASS means only that the Issue Form definition contains selected RPE structural fields and non-claim boundary signals.

PASS does not mean that any filled issue is correct, complete, safe, compliant, legally valid, fair, production ready, externally reviewed, socially accepted, or certified.

## How to run locally

```bash
python -m pip install -r requirements.txt
python scripts/check_issue_form.py
```

## GitHub Actions

The workflow `.github/workflows/check-issue-form.yml` runs the checker when the Issue Form, checker script, or dependency file changes.

The workflow declares read-only repository permissions:

```yaml
permissions:
  contents: read
```

This keeps the checker aligned with the repository security hygiene rule.

## RPE relation

The checker supports the RPE anchors described in `docs/issue-form-rpe-originality-note.md`:

- returnability
- non-final-AI boundary
- repair / dispute / reopening path

The checker is intentionally bounded. It preserves structure before deeper semantic checking is introduced.
