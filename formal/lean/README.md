# Lean Formalization

This directory contains formalization candidates for Responsibility Pathway Engineering.

## Purpose

The purpose of these files is to express selected structural properties in Lean.

Formalization is incremental and scope-limited.

## Current files

- `ResponsibilityPathway/Core.lean` - minimal node and pathway model with early responsibility-boundary invariant candidates

## Current invariant candidates

Current Phase 2 invariant candidates:

1. a node constructed as a safe AI node cannot hold final responsibility
2. a safely constructed AI-assisted pathway has a human or institutional return point

These are represented by:

- `NodeKind`
- `Node`
- `IsAI`
- `IsHumanOrInstitution`
- `CanHoldFinalResponsibility`
- `AIResponsibilityBoundary`
- `safe_ai_node_cannot_hold_final_responsibility`
- `Pathway`
- `HasAIParticipation`
- `HasHumanOrInstitutionalReturnPoint`
- `AIReturnPointBoundary`
- `safe_ai_assisted_pathway_has_return_point`

## Boundary

A Lean proof in this repository proves only the explicitly stated theorem under its stated assumptions.

It does not prove that any real-world AI system, organization, workflow, institution, or legal framework is safe, accountable, fair, lawful, compliant, morally resolved, complete, or production ready.

The current invariants do not make legal or moral claims. They state structural properties inside the minimal model.

## Strategy

Definitions first.
Invariants second.
Transitions third.
Examples fourth.
Extended theories later.

## Responsibility

The human author remains responsible for definitions and claims.
AI tools may assist implementation but are not responsible authors.
