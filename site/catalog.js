const shelves = [
  {
    name: "Reader path map",
    what: "A decorated first-reader map showing the responsibility pathway, start points, and next pages to build.",
    start: "reader-path/",
    boundary: "Navigation aid only; not certification, validation, or production approval."
  },
  {
    name: "Boundary glossary",
    what: "A decorated glossary explaining excluded readings such as certification, validation, production readiness, legal review, and AI final responsibility.",
    start: "boundary-glossary/",
    boundary: "Terminology aid only; not legal advice, safety review, compliance review, fairness review, certification, or production approval."
  },
  {
    name: "Templates",
    what: "Copyable responsibility-path record templates for AI-assisted work.",
    start: "../templates/ai-assisted-work-responsibility-path.yaml",
    boundary: "Template only; not certification or production approval."
  },
  {
    name: "Examples",
    what: "Filled examples showing responsibility holders, AI boundaries, evidence, return points, and repair paths.",
    start: "../examples/ai-assisted-work-minimal.yaml",
    boundary: "Illustrative and reviewable; not legal, safety, compliance, fairness, or production proof."
  },
  {
    name: "Reviewer quickstart",
    what: "A short path for reviewing one responsibility path without reading the whole repo.",
    start: "../docs/quickstart-review-one-path.md",
    boundary: "Inspection guide only; not endorsement or certification."
  },
  {
    name: "Python scripts",
    what: "Bounded local structural checkers for examples, review results, and runtime-event fixtures.",
    start: "../scripts/check_examples.py",
    boundary: "Checker pass is a bounded structural signal only."
  },
  {
    name: "GitHub Actions",
    what: "Workflow-backed checks for the current Lean and checker surfaces.",
    start: "../.github/workflows/check-lean.yml",
    boundary: "Green workflow does not mean safe, compliant, fair, lawful, or production ready."
  },
  {
    name: "Lean4",
    what: "Minimal formalization spine for structural definitions, examples, and invariant candidates.",
    start: "../formal/lean/README.md",
    boundary: "Proves only stated properties under stated assumptions."
  },
  {
    name: "Future starters",
    what: "Planned environment starters for Python, GitHub Actions, TypeScript, CLI, JSON Schema, and API-event use.",
    start: "../README.md#artifact-catalog",
    boundary: "Starter only; not SDK, runtime, service, or final responsibility mechanism."
  }
];

const exampleYaml = `id: ai_assisted_work_minimal_001
version: 0.1.0
lifecycle_state: originating

nodes:
  - id: human_reviewer_001
    type: Human
    authority_scope:
      can_decide: true
      can_approve: true
      can_execute: false
      can_stop: true
      can_repair: true
      can_close: true
    human_responsibility_capacity: true

  - id: ai_assistant_001
    type: AIAgent
    authority_scope:
      can_decide: false
      can_approve: false
      can_execute: false
      can_stop: false
      can_repair: false
      can_close: false
    human_responsibility_capacity: false
    ai_participation:
      may_generate: true
      may_summarize: true
      may_recommend: true
      may_execute_under_authority: false
      assumes_final_responsibility: false

edges:
  - from: human_reviewer_001
    to: ai_assistant_001
    relation_type: delegated_support
  - from: ai_assistant_001
    to: human_reviewer_001
    relation_type: return_to_authority

roles:
  decision_owner: human_reviewer_001
  approval_gate: human_reviewer_001
  stop_authority: human_reviewer_001
  repair_owner: human_reviewer_001
  human_return_point: return_point_001

return_points:
  - id: return_point_001
    type: HumanReturnPoint
    target_node: human_reviewer_001

responsibility_boundary:
  human_author_required: true
  ai_final_responsibility_allowed: false
  legal_or_moral_claims_out_of_scope: true

formalization_scope:
  excluded_claims:
    - legal_liability
    - moral_blame
    - compliance
    - safety
    - fairness
    - production_readiness`;

const checkItems = [
  ["Human decision owner is explicit", "decision_owner: human_reviewer_001"],
  ["Approval gate is explicit", "approval_gate: human_reviewer_001"],
  ["Stop authority is explicit", "stop_authority: human_reviewer_001"],
  ["Repair owner is explicit", "repair_owner: human_reviewer_001"],
  ["Human return point exists", "human_return_point: return_point_001"],
  ["AI final responsibility is blocked", "ai_final_responsibility_allowed: false"],
  ["AI does not assume final responsibility", "assumes_final_responsibility: false"],
  ["Stronger claims are excluded", "excluded_claims:"],
  ["Production readiness is excluded", "production_readiness"]
];

function renderShelves() {
  const container = document.querySelector("#shelves");
  container.innerHTML = shelves.map((shelf) => `
    <article class="card">
      <span class="tag">${shelf.name}</span>
      <h3>${shelf.name}</h3>
      <p>${shelf.what}</p>
      <p><a href="${shelf.start}">Start here</a></p>
      <p><strong>Boundary:</strong> ${shelf.boundary}</p>
    </article>
  `).join("");
}

function renderExample() {
  const example = document.querySelector("#exampleText");
  example.textContent = exampleYaml;
}

function runBrowserCheck() {
  const checks = document.querySelector("#checks");
  checks.innerHTML = checkItems.map(([label, needle]) => {
    const ok = exampleYaml.includes(needle);
    return `<li><span class="${ok ? "ok" : "warn"}">${ok ? "OK" : "CHECK"}</span> ${label}</li>`;
  }).join("");
}

async function copyExample() {
  try {
    await navigator.clipboard.writeText(exampleYaml);
    document.querySelector("#copyExample").textContent = "Copied YAML";
  } catch (error) {
    document.querySelector("#copyExample").textContent = "Copy unavailable";
  }
}

renderShelves();
renderExample();
runBrowserCheck();
document.querySelector("#copyExample").addEventListener("click", copyExample);
