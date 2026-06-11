# Lesson: Google Docs Small-Block Updates

## Date

2026-06

## Observation

Long-form Google Docs connector updates can create operational risk:

- partial insertion
- duplicated text
- wrong insertion location
- repair loops
- difficulty verifying large changes

## Lesson

Google Docs should be treated as an artifact-management and continuity layer, not as the primary writing environment for long-form structured drafts.

## Rule

When updating Google Docs through connector operations:

1. Prefer small confirmed blocks.
2. Verify after each update.
3. Use exact text anchors when possible.
4. Avoid raw index insertion unless the index has just been verified.
5. Move dense writing and code-like structure into files or repositories.

## Responsibility Pathway Impact

Small-block updates preserve a clearer pathway from intended change to applied change to verified result.

Large unverified insertions can break the responsibility pathway by making it unclear what changed, where it changed, and whether the change was intentional.
