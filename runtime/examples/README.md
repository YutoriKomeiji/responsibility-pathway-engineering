# Runtime examples scaffold

Status: runtime examples scaffold / Open Construction.

## Purpose

This directory is reserved for future runtime-adjacent examples.

The examples should show how a responsibility-path record may be placed near an execution request, automation step, tool-mediated workflow, or review gate while preserving human review and responsibility boundaries.

## Example principles

Runtime-adjacent examples should be:

- synthetic or local by default
- small enough to read manually
- copyable without setup friction
- explicit about approval gates
- explicit about stop authority
- explicit about repair ownership
- explicit about return points
- explicit about uncertainty and missing evidence
- explicit about excluded claims

## Not a runtime release

This directory does not mean that RPE provides a runtime release.

Examples in this directory must not claim:

- production readiness
- real-world execution authority
- hosted service availability
- connector availability
- package or SDK maturity
- safety validation
- compliance validation
- legal validity
- fairness validation
- certification
- AI final-responsibility transfer

## Candidate future examples

Possible future examples include:

- local command review record
- AI-assisted tool-call review record
- pre-execution approval gate record
- post-execution repair record
- automation stop-and-return record
- repository workflow responsibility record

Each future example should be introduced through a separate issue and reviewed before merge.

## Minimum acceptance for future examples

A future runtime-adjacent example should preserve:

- requester
- reviewer
- approval gate
- stop authority
- repair owner
- human return point
- evidence log
- uncertainty field
- excluded claims
- lifecycle state
- formalization scope

It should also remain clear that a responsibility-path record supports review; it does not replace human or institutional responsibility.
