---
applyTo: "scripts/**/*.py,src/**/*.py,tests/**/*.py"
---

# Python implementation instructions

- Prefer Python 3.12-compatible, dependency-light code for reference components.
- Keep domain logic separate from CLI argument parsing and file I/O.
- Use deterministic output ordering and stable reason codes.
- Validate required input shape explicitly and fail with actionable messages.
- Preserve per-pack decisions and provenance; do not collapse responsibility routes into an unexplained score.
- Add executable checks or tests for success, hold, human-gate, deny, non-applicable, and malformed-input paths when relevant.
- Avoid network calls, live credentials, external side effects, and production data in repository checks.
- Use type hints and small functions where they improve reviewability.
- A script must not merge, publish, approve, or execute the requested downstream AI action.
