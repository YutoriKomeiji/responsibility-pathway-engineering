const shelves = [
  {
    name: "Reader path map",
    what: "責任経路、最初に見る場所、次に作れるページを視覚的に示す装飾付きマップ。",
    start: "reader-path/",
    boundary: "導線補助であり、認証・検証・本番承認ではありません。"
  },
  {
    name: "Templates",
    what: "AI支援作業の責任経路を記録するためのコピー可能なテンプレート。",
    start: "../../templates/ai-assisted-work-responsibility-path.yaml",
    boundary: "テンプレートであり、認証や本番承認ではありません。"
  },
  {
    name: "Examples",
    what: "責任主体、AI境界、証拠、人間への戻り先、修復経路を埋めた例。",
    start: "../../examples/ai-assisted-work-minimal.yaml",
    boundary: "説明・レビュー用であり、法的・安全・遵法・公平性・本番性の証明ではありません。"
  },
  {
    name: "Reviewer quickstart",
    what: "リポジトリ全体を読む前に、1つの責任経路を短時間で確認するための導線。",
    start: "../../docs/quickstart-review-one-path.md",
    boundary: "点検ガイドであり、承認・認証ではありません。"
  },
  {
    name: "Python scripts",
    what: "examples、review results、runtime-event fixtures向けの限定的な構造checker。",
    start: "../../scripts/check_examples.py",
    boundary: "checkerの通過は限定的な構造シグナルにすぎません。"
  },
  {
    name: "GitHub Actions",
    what: "現在のLeanとchecker surfaceを継続的に確認するworkflow。",
    start: "../../.github/workflows/check-lean.yml",
    boundary: "workflow greenは安全・遵法・公平・合法・本番Readyを意味しません。"
  },
  {
    name: "Lean4",
    what: "構造定義、例、invariant候補のための最小formalization spine。",
    start: "../../formal/lean/README.md",
    boundary: "明示された仮定のもとで、明示された性質だけを示します。"
  },
  {
    name: "Future starters",
    what: "Python、GitHub Actions、TypeScript、CLI、JSON Schema、API-event利用に向けた将来starter。",
    start: "../../README.ja.md#artifact-catalog--成果物カタログ",
    boundary: "starterであり、SDK・runtime・service・最終責任機構ではありません。"
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
  ["人間のdecision ownerが明示されている", "decision_owner: human_reviewer_001"],
  ["approval gateが明示されている", "approval_gate: human_reviewer_001"],
  ["stop authorityが明示されている", "stop_authority: human_reviewer_001"],
  ["repair ownerが明示されている", "repair_owner: human_reviewer_001"],
  ["人間へのreturn pointがある", "human_return_point: return_point_001"],
  ["AIへの最終責任移転がブロックされている", "ai_final_responsibility_allowed: false"],
  ["AIは最終責任を引き受けない", "assumes_final_responsibility: false"],
  ["強い主張が除外されている", "excluded_claims:"],
  ["production readinessが除外されている", "production_readiness"]
];

function renderShelves() {
  const container = document.querySelector("#shelves");
  container.innerHTML = shelves.map((shelf) => `
    <article class="card">
      <span class="tag">${shelf.name}</span>
      <h3>${shelf.name}</h3>
      <p>${shelf.what}</p>
      <p><a href="${shelf.start}">ここから見る</a></p>
      <p><strong>境界:</strong> ${shelf.boundary}</p>
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
    document.querySelector("#copyExample").textContent = "YAMLをコピーしました";
  } catch (error) {
    document.querySelector("#copyExample").textContent = "コピーできません";
  }
}

renderShelves();
renderExample();
runBrowserCheck();
document.querySelector("#copyExample").addEventListener("click", copyExample);
