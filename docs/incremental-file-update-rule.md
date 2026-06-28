# Incremental File Update Rule

This note records a repository maintenance rule for updating existing documentation files.

## Rule

Prefer incremental build-up over broad replacement.

Before updating an existing file:

1. fetch the relevant line range or section;
2. identify the target heading, list, table, or insertion point;
3. decide the smallest auditable addition or local replacement;
4. avoid broad restructuring unless the task explicitly requires it;
5. split large documentation changes into multiple small commits when the responsibility units are distinct;
6. verify the changed section after writing.

When a write tool requires a full replacement payload, the intended edit should still be designed as a narrow section-level change.

Do not use a whole-file rewrite as the default mental model for long navigation, overview, inventory, or synchronization documents.

Use a focused note only when a narrow responsibility unit should not force a risky broad rewrite, or when tool-side checks block an otherwise safe local edit.

## Write retry note

If a write attempt fails and no repository content changed, one smaller retry is allowed.

The retry should keep the same maintenance intent but reduce size or structure.

If the smaller retry also fails, stop that write path and use a safer later step.

Do not keep repeating the same failed shape.

## Boundary

This is an operation rule only.

It does not change repository schemas, examples, checkers, workflows, formalization files, or runtime behavior.
