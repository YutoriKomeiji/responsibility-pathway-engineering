# Quickstart: review one responsibility path

Status: Open Construction / reviewer-facing quickstart.

This guide helps a first-time reviewer inspect one Responsibility Pathway record without reading the full repository first.

## Choose the entry that matches your task

**Try the current executable M2 kernel:** install the package using `python -m pip install .` and run `python scripts/value_demo.py` from the repository root. The demo compares a naive continuation with strict `evaluate_governed_action()` on the same synthetic, missing-approval request. It **never executes the proposed external send**. For integration, read [the value explanation](why-rpe.md), [current M2 implementation](m2-governed-integration-current.md), and [Python API](python-package-api.md). The REST and MCP service surfaces are described in the repository README.

**Review the historical record-format example:** follow the YAML example below. `scripts/check_examples.py` checks bounded document structure; it does **not** exercise the M2 governed evaluator. Do not treat a passing YAML checker as evidence that M2 governance, REST/MCP behavior, approval rules, or external effects have been validated.

**AI reader:** choose one task explicitly: `structure_review` or `governed_evaluation`. Do not silently substitute the structural example checker for the executable evaluation kernel. Record the observed entry point, input provenance, exact result and whether the action was only evaluated or actually executed (this guide never executes it). `allow` means an evaluation outcome, not newly granted dispatch Authority.

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

In this deliberately human-owned example, the record shows a human return point for an eligible human-held decision. This is an example-specific route, **not a universal rule** for every incomplete or blocked action. Current route-first design may instead require bounded continuation, reconciliation hold, neutral hold or stop, depending on existing Authority, receiver eligibility and effect uncertainty. See [Responsibility Routing contract](responsibility-routing-contract-v0.1.md).

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
