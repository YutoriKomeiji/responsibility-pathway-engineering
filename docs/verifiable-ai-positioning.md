# Verifiable AI positioning

Status: public positioning note / Open Construction.

## Core position

RPE is complementary to Verifiable AI, but it is not the same layer.

Verifiable AI usually asks whether an AI output, inference trace, reasoning process, or agent execution can be verified.

RPE asks a different question:

> Can the responsibility pathway around an AI-assisted action remain reviewable, bounded, returnable, and repairable?

Suggested public phrase:

> Verifiable Responsibility Pathway

## Why this matters

An AI answer can be checked without resolving responsibility.

An inference trace can be inspected without showing who requested the action.

A tool call can be authorized without preserving why a human accepted, rejected, stopped, repaired, or reopened the action.

A model output can be logically consistent while the surrounding workflow still has missing evidence, skipped approval, unclear authority, lost uncertainty, hidden delegation, or no visible return path.

RPE is built for that surrounding layer.

## Relationship to Verifiable AI

RPE should be described as adjacent to, and compatible with, Verifiable AI work.

| Verifiable AI focus | RPE focus |
| --- | --- |
| Was this model, inference, reasoning chain, or agent execution verified? | Was the responsibility path around the action preserved? |
| Can the computational result be trusted under stated assumptions? | Can the human and institutional review path be inspected under stated boundaries? |
| Does a proof, trace, solver result, or authorization artifact support the action? | Who requested, reviewed, approved, stopped, repaired, reopened, or accepted responsibility for the action? |
| What does the AI system claim or execute? | What does the workflow explicitly not claim, not prove, and not authorize? |

## RPE claim boundary

RPE does not claim to prove:

- model correctness
- inference correctness
- reasoning correctness
- cryptographic proof soundness
- browser rendering correctness
- legal validity
- safety validity
- compliance validity
- fairness validity
- production readiness
- certification
- conformance
- runtime correctness
- connector correctness
- AI final-responsibility transfer

RPE can instead provide reviewable records for:

- source preservation
- evidence preservation
- missing evidence
- uncertainty
- human instruction
- human review status
- approval gates
- stop authority
- repair ownership
- return points
- excluded claims
- lifecycle state
- bounded checker results
- formalization scope

## Strategic message

The strongest message is not:

> RPE verifies AI.

The stronger and safer message is:

> RPE makes the responsibility pathway around AI-assisted work reviewable.

Or, more compactly:

> Verifiable AI checks the machine-side claim. RPE preserves the human-side responsibility path.

## Open Construction use

This positioning should guide future README, article, catalog, example, checker, and formalization language.

When referencing Verifiable AI, keep the phrase bounded:

- complementary to Verifiable AI
- responsibility-path layer
- reviewable responsibility boundary
- evidence and return path preservation
- bounded structural checks
- assumption-scoped formalization

Avoid language that implies:

- RPE proves AI correctness
- RPE certifies AI output
- RPE replaces safety review
- RPE replaces legal review
- RPE replaces compliance review
- RPE grants production approval
- RPE transfers final responsibility to AI

## Source context for future reviewers

Recent Verifiable AI work includes lightweight proof or trace approaches for inference, formal or solver-guided verification of LLM reasoning, and proof-derived authorization or evidence-chain approaches for agentic execution.

RPE should not compete by overstating the same claims. RPE should occupy the responsibility-pathway layer that remains necessary even when computational or authorization artifacts exist.

## Next reader path

Use this note when preparing:

- public README language
- HTML catalog language
- Zenn or article framing
- external review package notes
- checker boundary explanations
- future examples involving AI agents or tool-mediated execution
