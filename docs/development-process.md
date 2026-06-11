# Development Process

Responsibility Pathway Engineering is developed by operating it.

The project should not assume that its process is complete in advance. Operational lessons are part of the architecture when they are observed, understood, and recorded.

## Process Loop

Build the project.
Observe the operation.
Improve the operation.
Record the improvement.

## Standard Work Cycle

1. Identify an observation or need.
2. Discuss and sketch the concept.
3. Add or update the definition.
4. Add or update the specification.
5. Add examples when the concept becomes concrete.
6. Add Lean or other formalization only after the scope is clear.
7. Update BEACON, ROADMAP, or CHANGELOG only at meaningful milestones.

## Commit Discipline

- Prefer small commits.
- Prefer one concept per commit.
- Do not mix unrelated documentation, specification, and formalization changes.
- Do not treat a draft theorem as a public guarantee.
- Do not treat an operational workaround as a stable rule until it has been observed and validated.

## Failure Handling

When a failure occurs:

1. Stop expanding the change.
2. Record what was observed.
3. Identify what is known and unknown.
4. Repair only the confirmed affected area.
5. Convert the lesson into documentation if it changes future operation.
