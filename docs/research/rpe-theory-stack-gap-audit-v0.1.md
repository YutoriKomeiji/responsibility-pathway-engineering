# RPE Theory Stack Gap Audit v0.1

**Status:** Internal research audit. Not a claim that Responsibility Pathway Engineering is a completed discipline.

## Audit question

Does the current RPE repository contain a sufficiently complete theory stack connecting Responsibility Pathway Model (RPM) analysis to repeatable engineering design, implementation, verification, operation, and revision?

## Executive finding

The repository already contains important structural ingredients:

- bounded definitions and claim-strength controls;
- lifecycle states;
- AI responsibility and return-point boundaries;
- suspension, return, repair, closure, evidence, and reopening invariants;
- schemas, examples, validators, and formal Lean artifacts;
- security and repository-governance applications.

However, the middle of the theory stack remains underdeveloped. The repository says what a structurally acceptable pathway should preserve, but it does not yet fully specify how an analyst converts RPM findings into design requirements, how competing pathway designs are selected, how implementation conformance is established, or how operational evidence feeds redesign.

The principal missing layer is therefore **Responsibility Pathway Design Theory**.

---

## 1. Proposed theory stack

The research program should distinguish seven layers.

### T0. Responsibility theory

Questions:

- What kinds of responsibility are in scope?
- How do answerability, obligation, blame, liability, repair, compensation, and stewardship differ?
- What is the role of remaining reversibility and broader response capacity?

Primary home: RPM conceptual theory and external normative scholarship.

### T1. Responsibility pathway theory

Questions:

- What constitutes a responsibility-bearing transition?
- What makes a pathway continuous or discontinuous?
- How do authority, knowledge, action, evidence, intervention, contestation, recovery, and residual ownership connect?

Primary home: RPM.

### T2. Responsibility Pathway Model

Questions:

- How are actors, states, transitions, options, evidence, and residuals represented?
- What coding and comparison procedures are reproducible?

Primary home: RPM analytical schema.

### T3. Responsibility Pathway Design Theory

Questions:

- How are detected discontinuities transformed into design requirements?
- Which intervention pattern should be chosen and why?
- How are trade-offs among speed, cost, privacy, security, autonomy, resilience, and recoverability handled?
- How are affected-party access and institutional authority built into the design?

Primary home: currently missing as a coherent theory layer; should bridge RPM and RPE.

### T4. Responsibility Pathway Engineering

Questions:

- How are pathway requirements implemented through architecture, workflow, roles, controls, records, interfaces, and operational procedures?
- How are artifacts versioned, reviewed, tested, deployed, observed, and repaired?

Primary home: RPE.

### T5. Responsibility Pathway Assurance

Questions:

- What evidence supports conformance to a specified pathway design?
- Which properties can be formally verified, tested, inspected, or audited?
- What remains unverified or institution-dependent?

Primary home: RPE plus external assurance and safety literature.

### T6. Institutional operation and evolution

Questions:

- How do pathways behave under real incentives, power asymmetry, staff turnover, policy change, emergencies, and adversarial compliance?
- How are failed premises detected and designs revised?

Primary home: RPE operational research and empirical studies.

---

## 2. Existing strengths

### 2.1 Structural boundaries

Current formal work defines useful minimum boundaries:

- AI participation requires a human or institutional return point.
- repaired pathways require repair records;
- suspended pathways preserve review or return conditions;
- returning pathways do not automatically continue;
- closed pathways preserve evidence and reopening conditions.

These are valuable candidate invariants, but they are mainly necessary structural conditions, not a complete design theory.

### 2.2 Strong non-certification discipline

The repository consistently states that formal theorems and validators do not prove legal validity, moral resolution, real-world safety, fairness, compliance, or production readiness. This is an important scholarly strength and should remain explicit.

### 2.3 Lifecycle orientation

RPE already treats responsibility as extending across suspension, return, repair, closure, and reopening rather than ending at execution or logging. This gives the engineering program a strong temporal foundation.

### 2.4 Evidence is necessary but insufficient

The repository distinguishes evidence chains from responsibility pathways and recognizes premise failure, human return, repair ownership, and residual responsibility. This supports a broader engineering theory than observability alone.

---

## 3. Missing or incomplete theory modules

## G1. Diagnostic-to-design transformation theory — Critical

RPM can identify a discontinuity, but RPE does not yet define a systematic transformation:

```text
RPM finding
  -> design objective
  -> requirement
  -> candidate intervention patterns
  -> trade-off analysis
  -> selected design
  -> implementation artifact
  -> verification evidence
  -> operational feedback
```

Required output:

- a transformation rule set;
- requirement templates;
- traceability from finding to intervention;
- rejection reasons for non-selected designs.

## G2. Design objective theory — Critical

RPE needs explicit objectives beyond generic pathway preservation. Candidate objectives include:

- preserve meaningful response options;
- minimize unjustified reversibility loss;
- keep intervention authority aligned with intervention capacity;
- maintain evidence continuity;
- make contestation accessible and effective;
- assign and resource recovery obligations;
- prevent unresolved residuals from becoming ownerless;
- avoid responsibility theatre and blame transfer.

These objectives can conflict. RPE therefore needs a non-scalar, multi-objective design model rather than one universal score.

## G3. Design-pattern theory — Critical

The repository contains examples and controls, but not a stabilized pattern language. Candidate pattern families include:

- scoped authorization;
- dual-key or multi-party approval;
- time-bounded delegation;
- reversible staging;
- canary execution;
- intervention checkpoint;
- accountable human or institutional return;
- contestation hold;
- evidence-preserving rollback;
- compensatory recovery;
- residual stewardship;
- premise-expiry and reevaluation.

Each pattern needs applicability, prerequisites, benefits, costs, failure modes, and anti-patterns.

## G4. Composition theory — Major

Real systems contain branching, concurrent, nested, and cross-organizational pathways. RPE lacks a mature theory for:

- composing local pathways;
- preserving invariants across organizational boundaries;
- handling conflicting authorities;
- merging or splitting residual obligations;
- reasoning about multi-agent delegation;
- ensuring end-to-end properties when components satisfy only local properties.

## G5. Trade-off and proportionality theory — Major

Maximal reversibility is neither always possible nor always desirable. RPE must explain when irreversibility is justified and how design burden should be proportionate to:

- severity and distribution of possible impact;
- time sensitivity;
- reversibility decay;
- affected-party vulnerability;
- uncertainty;
- scale and propagation speed;
- cost of intervention;
- security and privacy exposure.

This must not become an unvalidated universal score.

## G6. Verification and validation theory — Major

Current formal invariants show constructor-level structural properties. RPE still needs to distinguish:

- schema validity;
- design conformance;
- implementation conformance;
- operational effectiveness;
- institutional legitimacy;
- affected-party recognition of recovery;
- external legal or regulatory compliance.

Only the first three may be substantially machine-checkable. The others require empirical or institutional evidence.

## G7. Failure and anti-pattern theory — Major

RPE should formally catalogue:

- nominal return points without authority;
- approval without intelligible scope;
- logs without intervention rights;
- rollback without stakeholder recovery;
- contestation without reversal power;
- residual ownership without resources;
- emergency procedures that erase evidence;
- responsibility theatre;
- responsibility dumping onto low-power operators;
- premise persistence after invalidation.

## G8. Institutional and incentive theory — Major

Engineering controls operate within organizations. RPE needs explicit treatment of:

- incentives to hide or delay pathway failures;
- separation of duties and conflicts of interest;
- budget and resource ownership;
- regulator and third-party participation;
- labor and professional authority;
- cross-border and contractual boundaries;
- organizational learning and memory.

## G9. Economics and operational burden — Moderate

A pathway design can be theoretically strong and operationally unusable. RPE should track:

- analysis and implementation cost;
- latency introduced by controls;
- review fatigue;
- false-positive interruption;
- documentation burden;
- maintenance and retraining cost;
- cost distribution among institutions and affected parties.

## G10. Theory of change and adoption — Moderate

To reach academies, research institutes, firms, and international organizations, RPE needs a theory of how pathway artifacts alter practice:

- who adopts them;
- what decisions they influence;
- what evidence changes behavior;
- what organizational conditions permit adoption;
- how local adaptations preserve core properties.

---

## 4. Proposed core RPE design principles

These are candidate principles, not validated standards.

1. **Pathway traceability** — Every material design control should trace to a responsibility-pathway finding or declared preventive objective.
2. **Authority-capacity alignment** — An actor assigned intervention or recovery responsibility must have corresponding authority, information, resources, and time.
3. **Response-option preservation** — Designs should preserve meaningful response options where proportionate and document intentional option removal.
4. **No automatic recovery equivalence** — Technical restoration does not imply completed responsibility recovery.
5. **Contestability by design** — Affected parties or legitimate representatives require intelligible, accessible, and effective routes to challenge outcomes.
6. **Residual stewardship** — Irreducible impact must remain visible and institutionally owned rather than disappearing at closure.
7. **Evidence with actionability** — Evidence is useful only when connected to actors able and obligated to act.
8. **Premise expiry** — Assumptions and authority conditions require review triggers and expiry conditions.
9. **Emergency precedence** — Immediate containment and human support may precede exhaustive pathway analysis, while preserving essential evidence.
10. **Anti-theatre** — Documentation without actual authority, capacity, remedy, or review power does not satisfy pathway design.
11. **Proportionality** — Design burden should reflect impact, uncertainty, scale, vulnerability, and reversibility decay.
12. **Revision openness** — Closure preserves evidence, reopening conditions, and institutional capacity to revise the pathway.

---

## 5. Proposed engineering lifecycle

```text
1. Scope responsibility-bearing transitions
2. Apply RPM analysis
3. Identify discontinuities and response-option loss
4. Establish affected parties and institutional boundaries
5. Derive design objectives
6. Generate candidate pathway interventions
7. Compare trade-offs and failure modes
8. Select and document pathway design
9. Implement controls, records, roles, and interfaces
10. Verify structural and implementation conformance
11. Exercise through simulation, tabletop, or controlled tests
12. Operate and collect evidence
13. Detect premise failure and pathway degradation
14. Contain, return, repair, compensate, or steward residue
15. Review, reopen, and redesign
```

This lifecycle should become the central bridge between RPM and RPE.

---

## 6. International scholarly positioning needs

RPE should be positioned as complementary to, and tested against, mature work in:

- systems safety and control theory;
- resilience engineering;
- software and requirements engineering;
- safety and assurance cases;
- human factors and meaningful human control;
- organizational accountability;
- contestability, remedy, and redress;
- AI lifecycle governance and risk management;
- formal methods and runtime assurance;
- incident management and post-incident learning;
- responsible innovation and technology governance;
- public administration and institutional design.

The research program should avoid presenting national or corporate governance frameworks as globally universal. Comparative work should include multiple legal, organizational, and cultural contexts and explicitly separate structural claims from jurisdiction-specific requirements.

---

## 7. Recommended paper sequence

### Paper A — RPM conceptual-method paper

Defines and evaluates the analytical model.

### Paper B — Responsibility Pathway Design Theory

Defines diagnostic-to-design transformation, objectives, patterns, trade-offs, composition, and anti-patterns.

### Paper C — RPE method and reference lifecycle

Defines repeatable engineering activities, artifacts, roles, assurance boundaries, and operational feedback.

### Paper D — Formal structural properties

Presents scoped formalization and explicitly limited invariant proofs.

### Paper E — Comparative empirical evaluation

Tests RPM/RPE against mature integrated governance and engineering baselines across domains and regions.

This separation is preferable to forcing RPM, design theory, RPE methodology, formal verification, and empirical validation into one paper.

---

## 8. Immediate actions

1. Create a Responsibility Pathway Design Theory draft.
2. Define finding-to-requirement transformation rules.
3. Build an initial pattern and anti-pattern catalogue.
4. Map current Lean invariants to design principles and clarify which principles are not formalized.
5. Add composition and proportionality research questions.
6. Build one worked example from RPM diagnosis through RPE redesign and re-evaluation.
7. Conduct a literature pass across systems safety, requirements engineering, assurance cases, resilience, and institutional accountability.
8. Preserve an explicit distinction among structural conformance, operational effectiveness, normative justification, and legal compliance.

## Audit conclusion

RPE theory is not absent. Its structural kernel, lifecycle orientation, bounded formalization, and claim discipline are substantial. The missing element is a coherent theory of **design transformation and selection** between RPM diagnosis and RPE implementation. Filling that layer will make the overall progression academically clearer:

```text
Responsibility
  -> Responsibility Pathway
  -> RPM analysis
  -> Responsibility Pathway Design Theory
  -> RPE implementation
  -> Responsibility Pathway Assurance
  -> Institutional operation and revision
```

No part of this audit authorizes claims that RPE is validated, complete, universally applicable, legally sufficient, or superior to existing disciplines.