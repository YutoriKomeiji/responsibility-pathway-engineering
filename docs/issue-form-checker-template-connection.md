# Issue Form Checker Template Connection

This note connects the AI-assisted work Issue Form route with its bounded checker.

## Connected files

- `.github/ISSUE_TEMPLATE/ai-assisted-work-responsibility-path.yml`
- `templates/ai-assisted-work-responsibility-path.yaml`
- `scripts/check_issue_form.py`
- `.github/workflows/check-issue-form.yml`
- `docs/issue-form-checker-note.md`
- `docs/checker-coverage.md`
- `docs/issue-body-warning-checker-plan.md`
- `templates/README.md`

## Local check

Run:

```bash
python -m pip install -r requirements.txt
python scripts/check_issue_form.py
```

## Evidence timestamp guidance

The template and Issue Form evidence-log guidance now include `observed_at`, `recorded_at`, and `timezone` so maintainers can preserve time-order reviewability when evidence, decisions, reviews, repairs, disputes, or reopening steps need to be checked later.

This is current template and form guidance, not current filled-issue validation.

`docs/checker-coverage.md` records that the current Issue Form checker does not enforce timestamp fields inside created issue bodies.

`docs/issue-body-warning-checker-plan.md` records possible future warning-only signals for missing or weak evidence timestamp fields.

## Observed workflow note

The observed manual GitHub Actions run for this route is recorded in `docs/issue-form-checker-note.md`.

That observation means only that the bounded Issue Form checker workflow completed successfully for the observed repository state. It is not evidence that any created issue body is correct, complete, time-ordered, legally valid, safe, compliant, fair, production ready, externally reviewed, socially accepted, certified, conformance-ready, or that AI assumes final responsibility.

## Meaning

The checker verifies selected structural signals in the Issue Form definition.

It helps keep the form aligned with RPE anchors such as returnability, non-final-AI boundary, and repair or reopening path.

## Boundary

A checker pass is a bounded structural maintenance signal only.
