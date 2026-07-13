# Quickstart: review one responsibility path

Status: Open Construction / reviewer-facing quickstart.

This guide helps a first-time reviewer inspect one Responsibility Pathway record without reading the full repository first.

Start with:

- `examples/ai-assisted-work-minimal.yaml`
- `docs/examples/ai-assisted-work-minimal.md`
- `scripts/check_examples.py`
- `docs/checker-coverage.md`

## 1. Open the example

Read `examples/ai-assisted-work-minimal.yaml` first.

The scenario is:

```text
Human reviewer -> AI assistant -> Human reviewer
```

The AI assistant may draft, summarize, structure, or explain uncertainty.

The AI assistant does not decide, approve, execute, stop, repair, close, or become the final responsibility holder.

## 2. Check the core responsibility holders

Look for these fields:

```yaml
roles:
  decision_owner: human_reviewer_001
  approval_gate: human_reviewer_001
  stop_authority: human_reviewer_001
  repair_owner: human_reviewer_001
```

The important question is not only what the AI produced.

The important question is where judgment, approval, stop authority, repair, and return remain reachable.

## 3. Check the AI boundary

Look for these fields:

```yaml
ai_participation:
  assumes_final_responsibility: false

responsibility_boundary:
  ai_final_responsibility_allowed: false
```

This is the first boundary a reviewer should confirm.

## 4. Check evidence and uncertainty

Look for:

- `evidence_logs`
- `source_reference`
- `human_instruction`
- `ai_draft_or_summary`
- `approval_state`
- `uncertainty`

A useful record does not have to be complete at first.

It should make missing context and uncertainty visible enough for a human or institution to review later.

## 5. Check the human return point

Look for `return_points`.

The record should show where the pathway returns if the output is disputed, incomplete, unclear, unsupported, or outside scope.

## 6. Run the bounded checker

From the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/check_examples.py
```

The checker performs bounded structural checks only.

A passing result does not mean certified, safe, compliant, fair, legally valid, morally resolved, institutionally approved, production ready, or AI-final-responsibility transferred.

## 7. Review result

After reading the example, a reviewer can answer:

- Is the human decision owner explicit?
- Is approval authority explicit?
- Is stop authority explicit?
- Is AI final responsibility blocked?
- Is evidence visible?
- Is uncertainty visible?
- Is a human return point visible?
- Is repair or reopening ownership visible?
- Are stronger claims excluded?

If the answer is unclear, open an Issue or suggest a small PR.

## Boundary

This quickstart is an inspection guide.

It is not certification, legal review, safety review, compliance review, fairness review, production approval, institutional endorsement, or AI final-responsibility transfer.
