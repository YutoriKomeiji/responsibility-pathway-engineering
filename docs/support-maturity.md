# Support and Maturity by Surface

RPE is not described by one repository-wide maturity label. Different surfaces have different support expectations.

| Surface | Current posture | Notes |
|---|---|---|
| Legacy Python `evaluate_action()` | Supported | Retained for compatibility; bounded semantics documented. |
| Governed Python `evaluate_governed_action()` | Supported reference | Intended for real bounded integrations; M2 closure/adversarial evidence is still being completed. |
| Requirement Pack + governance contracts | Supported reference | Versioned and CI-checked; real-world normative interpretation remains integrator/human-owned. |
| Local/caller-content loader | Supported reference | Bounded to documented content/file loading; no remote trust establishment. |
| REST adapter | Supported reference | Local/reference integration surface, not a complete production service stack. |
| MCP stdio adapter | Supported reference | Reference tool boundary; production peer identity/transport controls remain integrator-owned. |
| OpenAPI contract | Supported reference | Repository/package/runtime parity is checked. |
| Synthetic value/demo scenarios | Supported examples | Reproducible repository evidence, not proof of external effect or universal risk reduction. |
| AI -> AI generalized responsibility routing | Research / planned | Not yet implemented as a general handoff model. |
| SaaS/legacy adapters | Planned / preview target | Architecture direction only until concrete adapters are implemented and tested. |
| Trajectory/cumulative-risk engine | Research | Connected to future long-horizon assurance work; not yet a supported runtime feature. |
| Trust / responsibility taint propagation | Research | Candidate security architecture. |
| Relationship-injection defense | Research | Explicit threat-model target, not a complete current defense. |
| Production authentication/authorization/tenancy/secrets | Not included | Must be supplied by an integrating production environment unless a future scoped RPE surface implements them. |
| Automatic legal/compliance determination | Unsupported | RPE does not create legal interpretation or certification authority. |
| Execution/repair/resume authority issuance | Unsupported by RPE core | These authority-bearing transitions belong to the responsible runtime/institutional layer. |

## How to read this table

- **Supported** — normal use is intended within documented boundaries; defects are accepted and should be repaired.
- **Supported reference** — intended as a usable reference implementation; deployment-specific hardening may remain external.
- **Preview / planned target** — early integration direction; interface may change.
- **Research** — investigative; no stable integration contract yet.
- **Not included** — not provided by the current surface; another layer may provide it.
- **Unsupported** — deliberately outside the responsibility/authority the RPE core should create.

`Not guaranteed` does not automatically mean `forbidden`. Use the documented surface posture, risk conditions, and integration boundary rather than a single alpha/non-alpha label.
