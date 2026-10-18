# Repository Principles

This repository serves as a primary archival source for Responsibility Pathway Engineering.

Articles, presentations, papers, implementations, examples, and formalizations should converge toward this repository as the canonical technical reference.

## Development Order

Observation
→ Definition
→ Specification
→ Formalization
→ Claim
→ Application

## Repository Philosophy

The purpose of this repository is not to own terminology.

Its purpose is to preserve, evolve, implement, and share a structural design framework through which responsibility can remain recoverable across humans and AI.

## From principle to executable evidence

The development order is a trace, not a waterfall or a license to invent new documents. For any changed responsibility-bearing behavior, identify:

1. the **observable problem** and credible simpler baseline;
2. the existing **authority and evidence boundary** from source documents;
3. the **versioned contract** (schema/API/routing semantics), including missing/ambiguous cases;
4. the **smallest corresponding code change**, preferably in the existing evaluator;
5. positive, negative and adversarial checks for that contract at the exact source revision;
6. the **reader's reproducible example** and the bounded claim its evidence supports.

Reference the current [ROADMAP](../ROADMAP.md) for layer owners, M2/M3 status and ordering. Do not equate a design, approved-looking template, green test, or synthetic demonstration with an external effect, an authorization grant, or validated adoption. A proposal can validly conclude that RPE adds no value beyond existing host controls for the stated scenario.

## Responsibility Boundary

Human authors remain responsible for definitions, claims, citations, and publication.
AI systems may assist drafting and implementation but are not responsible authors.