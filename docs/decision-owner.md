# Decision Owner

## Purpose

A Decision Owner is the entity responsible for a decision within a Responsibility Pathway.

The Decision Owner is not necessarily the actor that executes the action.

Separating decision ownership from execution helps preserve responsibility when AI agents, tools, workflows, or organizations participate in action.

## Minimal Definition

A Decision Owner is a human, organization, institution, or authorized role that holds responsibility for deciding whether a pathway transition should occur under stated assumptions and authority.

## Responsibilities

A Decision Owner should be identifiable for:

- the decision being made
- the authority used
- the assumptions accepted
- the evidence relied upon
- the risk accepted
- the affected parties considered
- the stop conditions recognized
- the repair path accepted

## Distinction from Execution Actor

The Execution Actor performs or triggers an action.

The Decision Owner authorizes or accepts responsibility for the decision that allows the action to occur.

An AI agent or tool may be an execution actor or recommendation source, but it is not the final human-responsible decision owner by default.

## Distinction from Approval Gate

An Approval Gate is the point where continuation is reviewed or permitted.

A Decision Owner is the entity that bears responsibility for the decision behind that permission.

They may be the same entity, but they do not have to be.

## Failure Modes

Decision ownership fails when:

- no owner is identified
- ownership is assigned only after failure
- the owner lacks actual authority
- the owner lacks information
- the owner cannot refuse
- execution occurs without owner visibility
- AI recommendation is treated as ownership transfer
- organizational responsibility is displaced onto an individual operator

## Boundary

Decision Owner is a modeling construct for preserving responsibility pathways.

It does not alone determine legal liability, employment responsibility, moral blame, or organizational fault.
