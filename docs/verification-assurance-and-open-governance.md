# Verification, Assurance, and Open Governance Scope

This document records the current RPE position on formal verification, AI assurance, public governance guidance, licensing, interoperability, and non-exclusive responsibility infrastructure.

## Verifiable AI and Lean 4

RPE uses **verifiable AI** in a bounded sense: assumptions, requirement mappings, decision rules, stop conditions, reason codes, and human-return routes should be inspectable and capable of being checked again.

Planned Lean 4 work may prove properties of an explicitly formalized responsibility-path model, for example:

- deterministic decisions for the same modeled inputs;
- absence of `allow` when modeled mandatory evidence is missing;
- preservation of stronger `deny` or `human_gate` decisions during combination;
- existence of a human-return route when modeled approval is required;
- rejection of forbidden state transitions;
- preservation of stated invariants across modeled transitions.

Such results would prove that the **formalized responsibility path follows the formalized rules under the stated assumptions**.

They would not, by themselves, prove the correctness of the complete Python runtime, external services, dependencies, input data, human operations, requirement-pack interpretation, legal conclusions, social adequacy, or production deployment.

The boundary exists because Lean 4 proves propositions expressed in the Lean model. Extending confidence to the deployed system additionally requires evidence that the formal model corresponds to the Python implementation and that runtime inputs and external conditions satisfy the model assumptions.

## AI assurance

RPE treats AI assurance as an evidence-building activity, not as a declaration that an AI system is simply “safe.”

The relevant assurance surface includes:

- explicit requirements and their source metadata;
- applicability records;
- decision traces and reason codes;
- missing-evidence records;
- governance ownership and review state;
- human-return routes;
- stated verification results and their proof boundaries;
- repair and resume records as those structures are implemented.

RPE does not currently issue certification, compliance findings, deployment approval, or a general safety guarantee.

## AI alignment boundary

RPE does not claim to solve model-internal value alignment, objective selection, or the full AI alignment problem.

Its role is external and operational: connect a proposed AI-assisted action to explicit requirements, stop conditions, evidence expectations, and a route back to a responsible human or institution.

## Public guidance and requirement packs

Public laws, standards, and guidelines are not executed directly by the kernel. Identified humans must establish the source, scope, interpretation, review status, and maintenance responsibility of an operational Requirement Pack.

The Japanese Ministry of Internal Affairs and Communications and Ministry of Economy, Trade and Industry **AI Guidelines for Business Ver. 1.2** (31 March 2026) may be used as an official governance reference when future mappings are prepared.

RPE does not currently claim:

- official implementation of that guideline;
- conformity or compliance with the guideline;
- automated interpretation of the guideline;
- reviewed real-world Requirement Packs derived from the guideline;
- government adoption or endorsement of RPE.

Future work may document source-linked correspondences and human-reviewed mappings without converting non-binding guidance into an invented legal obligation.

Official source:

- <https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html>
- <https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf>

## Open implementation and standardization

RPE is released under the MIT License so that organizations, public bodies, researchers, and developers can inspect, reuse, compare, and improve the implementation.

RPE is not currently an official standard. The direction is to provide open specifications, interoperable structures, multiple-implementation potential, and independent verification surfaces that could inform future standardization discussions.

## Responsibility proof must not become responsibility monopoly

Intellectual-property protection for individual products, algorithms, and implementation techniques is distinct from exclusive control over the common foundations used to demonstrate responsibility.

If responsibility pathways, evidence formats, stop conditions, human-return protocols, or recognition authority become dependent on exclusive patents or closed specifications, foreseeable structural risks include:

- loss of interoperability;
- vendor or certification-body lock-in;
- unequal access to responsibility evidence because of cost;
- reduced independent verification;
- concentration of authority over who may be recognized as sufficiently responsible.

RPE does not reject patent or intellectual-property systems as a whole. It favors open specifications, interoperability, independent verification, and the possibility of multiple implementations for the shared foundations of responsibility evidence.

**A mechanism for demonstrating responsibility must not become a mechanism for monopolizing responsibility.**
