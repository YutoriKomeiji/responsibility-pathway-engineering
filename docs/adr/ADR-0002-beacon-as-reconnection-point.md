# ADR-0002: BEACON as Reconnection Point

## Status

Accepted

## Context

The project is expected to be read across sessions, people, and AI systems. Future readers may not share the original conversation context.

A stable reconnection point is needed so that someone can re-enter the project without relying on hidden memory or prior session state.

## Decision

`BEACON.md` is adopted as the repository's reconnection point.

Its role is to answer:

- Where are we?
- What has already been established?
- What should be read first?
- What should not be assumed?
- What should happen next?

## Consequences

`BEACON.md` should be updated only at meaningful milestones, not after every small edit.

It should remain compact enough to function as an entry point.

The repository should not require private conversation history to be understandable.
