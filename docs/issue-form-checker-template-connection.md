# Issue Form Checker Template Connection

This note connects the AI-assisted work Issue Form route with its bounded checker.

## Connected files

- `.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml`
- `scripts/check_issue_form.py`
- `.github/workflows/check-issue-form.yml`
- `docs/issue-form-checker-note.md`
- `docs/checker-coverage.md`
- `templates/README.md`

## Local check

Run:

```bash
python -m pip install -r requirements.txt
python scripts/check_issue_form.py
```

## Observed workflow note

The observed manual GitHub Actions run for this route is recorded in `docs/issue-form-checker-note.md`.

That observation means only that the bounded Issue Form checker workflow completed successfully for the observed repository state. It is not evidence that any created issue body is correct, complete, legally valid, safe, compliant, fair, production ready, externally reviewed, socially accepted, certified, conformance-ready, or that AI assumes final responsibility.

## Meaning

The checker verifies selected structural signals in the Issue Form definition.

It helps keep the form aligned with RPE anchors such as returnability, non-final-AI boundary, and repair or reopening path.

## Boundary

A checker pass is a bounded structural maintenance signal only.
