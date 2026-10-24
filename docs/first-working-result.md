# From problem to first working result

This page helps a new developer choose **one useful entry point** without learning the entire Responsibility Pathway family up front.

## Choose your starting point

| Your immediate problem | Start here | What you can try now |
|---|---|---|
| An agent proposes an action, but approval or evidence is missing | **RPE** (this repository) | Compare a naive continuation with governed evaluation using `python scripts/value_demo.py` |
| A write might have happened even though an HTTP call timed out | [RPR](https://github.com/YutoriKomeiji/responsibility-pathway-runtime) | Follow the runtime's uncertainty/readback/recovery quick start |
| You need durable operating state for authorization, dispatch, uncertain effects and recovery | [RPOS](https://github.com/YutoriKomeiji/responsibility-pathway-os) | Run its SQLite-backed CLI and documented integration scenarios |
| You need to turn a responsibility concern into reviewable design obligations | [RPD](https://github.com/YutoriKomeiji/responsibility-pathway-design) | Inspect the worked ERP design-transformation case |
| You need the conceptual model and current manuscript evidence | [RPM](https://github.com/YutoriKomeiji/responsibility-pathway-model) | Check access and the current manuscript/submission status; the repository may not be publicly accessible |

Each entry stands on its own where documented. You do **not** need to install the entire stack to run RPE's first demo.

## Try the smallest RPE value demonstration

Requirements: Git, Python 3.11+.

```bash
git clone https://github.com/YutoriKomeiji/responsibility-pathway-engineering.git
cd responsibility-pathway-engineering
python -m pip install .
python scripts/value_demo.py
```

This demo uses a **synthetic proposal** about sending externally, with the required human approval absent. It compares two simulated continuation decisions:

1. Naive continuation: the proposal alone would be enough to proceed.
2. Governed evaluation: RPE returns `human_gate`, a stable reason code and an explicit owner route.

Both paths report `executed: false`; **no actual external message is sent**. The demo checks its own expected values and reports why RPE changed the proposed continuation. A demo assertion failure is a finding to report, not a reason to claim a different outcome.

To go further, inspect [Why RPE?](why-rpe.md), the [Python API](python-package-api.md), [REST](integrations/rest-api.md) and [MCP stdio](integrations/mcp-stdio.md). The current released/default-branch M2 evaluation is distinct from experimental M3 work in draft pull requests.

## Integrate only the boundary you need

```text
existing agent or automation
          |
          v
  proposed consequential action
          |
          v
 RPE evaluates the supplied requirements and governance
          |
          +--> non-allow: stop, ask for evidence or return to the named owner
          |
          +--> allow: host independently checks real execution authority
                         |
                         v
                    existing executor
```

RPE returns an **evaluation**, not a credential, organization-level authorization, or verified real-world effect. Your host must enforce the result and its own authority before dispatch; the executor or runtime owns readback, reconciliation and recovery.

## Use, modify, verify and contribute

The individually developed reference implementation is published for use and extension within its [MIT license](../LICENSE). You may adapt it in a fork without contributing upstream. Contributions and independent evaluations are also welcome:

- Found an environment that does not install or run? Open an [Issue](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/issues) with Python version, OS, command, actual output and expected output (redact secrets).
- Added a useful integration or simplified the setup? Share a PR following [CONTRIBUTING](../CONTRIBUTING.md).
- Able to verify integration, operational, performance or threat scenarios not covered by the current CI? Share reproducible cases, assumptions, observed results and residual unknowns.
- Found a security-sensitive weakness? Follow [SECURITY](../SECURITY.md), not a public exploit report.

Current repository CI verifies named code paths and examples; it is not a claim of field deployment, certification, or universal security. Those unverified settings are **opportunities for practical validation**, not a blanket bar on using and improving the documented functionality.
