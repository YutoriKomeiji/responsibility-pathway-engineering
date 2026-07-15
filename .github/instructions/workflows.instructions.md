---
applyTo: ".github/workflows/**/*.yml,.github/workflows/**/*.yaml"
---

# GitHub Actions instructions

- Use the minimum required `permissions` block; default to `contents: read`.
- Prefer deterministic local checks that can also be run outside GitHub Actions.
- Give steps names that identify the actual contract being checked.
- Keep workflows non-deploying and non-publishing unless the maintainer explicitly approves that behavior.
- Do not add automatic commits, branch updates, releases, Pages publication, external messages, or secret-dependent steps without explicit approval.
- Before changing README commands or links, inspect workflows for exact `grep` or path contracts.
- Pin only to established major action versions already consistent with the repository unless an upgrade is part of the task.
- Make failure output actionable and preserve the distinction between structural validation and real-world approval.
