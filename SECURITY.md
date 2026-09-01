# Security Policy

RPE is actively developed and usable within documented boundaries. Security limitations are treated as engineering work, not as a reason to discourage all use.

## Supported security posture

The maintainer accepts security reports for the current `main` line and the latest intentionally published release/tag when one exists.

RPE currently provides a bounded responsibility-evaluation kernel and reference adapters. It does **not** currently provide a complete production authentication, authorization, tenant-isolation, secret-management, network-security, or deployment-security layer.

Those missing platform controls are known boundaries, not evidence that every RPE integration is forbidden. Integrators must supply deployment-specific controls appropriate to their environment.

## Report a vulnerability

Please do not put secrets, private exploit details, credentials, private logs, or sensitive operational data in a public issue.

Prefer GitHub Private Vulnerability Reporting when enabled for this repository. If private reporting is unavailable, contact the maintainer through a non-public channel listed on the maintainer GitHub profile and include enough information to reproduce the issue safely.

Useful reports include:

- affected commit/version;
- affected interface or adapter;
- minimal reproduction;
- expected versus observed responsibility/authority behavior;
- whether external effect, privilege, confidential data, or integrity is at risk;
- any known workaround or containment step.

Ordinary bugs, documentation gaps, integration failures, and non-sensitive adversarial examples may be filed as public issues.

## Threat families under active attention

RPE security work is broader than prompt filtering. Current and planned threat-model work includes:

- direct and indirect prompt/content injection;
- multi-stage injection across tools, memory, agents, and systems;
- relationship injection / relation misbinding;
- memory or persistence poisoning;
- goal hijacking;
- inter-agent trust escalation;
- authority laundering and scope escalation;
- Requirement Pack / policy / adapter supply-chain compromise;
- recovery-path injection;
- trajectory and cumulative-risk escalation;
- resource and economic abuse;
- provenance and evidence confusion.

Not all of these are fully implemented defenses today. They are explicit research and engineering targets.

## Security invariants

RPE should preserve these distinctions even when a model or upstream context is wrong:

- content is not authority;
- capability is not authority;
- identity is not established by self-assertion alone;
- delegation is not transitive by default;
- trust does not automatically reset at agent/system boundaries;
- evaluation evidence is not external-effect evidence;
- an `allow` evaluation is not execution authorization;
- repair/resume requirements are not repair/resume authority;
- unknown lineage or effect remains unknown until independently resolved.

## Fix lifecycle

Where feasible, a confirmed security defect should produce:

1. a minimal reproduction;
2. impact classification;
3. a fix or containment change;
4. regression/adversarial coverage;
5. release or migration guidance when users must act;
6. a public advisory when disclosure is appropriate.

RPE does not claim perfect prevention of prompt injection, malicious intent, arbitrary multi-agent emergence, or all future attack classes. The engineering target is to prevent untrusted or compromised inputs from silently acquiring authority or effect whenever the architecture can enforce that separation.
