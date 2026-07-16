# Responsibility Pathway Engineering

**AIシステムのための、実行可能なResponsible AI制御。**

責任経路工学（Responsibility Pathway Engineering / RPE）は、明示的に範囲を定めた要件のmappingを、実行時制御へ変換するための外部責任カーネルです。

```text
要件
  ↓
人間が範囲と解釈を定めたRequirement Pack
  ↓
AI Action Request
  ↓
RPE Kernel
  ↓
allow / hold / human_gate / deny
  ↓
理由コード・不足情報・人間への戻り先
```

## M1現在地 — Governed Reference Kernel

RPEは **M1 Governed Reference Kernel** のcheckpointへ到達しました。

実装済み:

- 1つのdeterministicなPython decision kernel
- applicability resolutionとmulti-pack evaluation
- Python、local REST、OpenAPI 3.1、MCP stdioのreference interface
- Requirement Packのlifecycleとmaintenance governance
- expiry、ambiguity、ownership、review、suspension、supersession、retirementの境界
- action request、gate decision、requirement pack、governance record、reason-code policyのversion baseline
- compatibility、unknown version、deprecation、migration規則
- schema、synthetic fixture、checker、CI guard

M1には外部Pack Loader、`evaluate_action()`内部でのGovernance強制、本番配備、自動的なsource解釈、Python runtimeの形式検証は含まれません。

## インストール

```bash
python -m pip install .
```

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

すべてのruntime interfaceは同じpackage APIへ委譲します。

| Interface | 入口 | 文書 |
|---|---|---|
| Python package | `evaluate_action` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| Local REST reference adapter | `rpe-rest` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| OpenAPI 3.1 | `GET /openapi.json` | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |
| MCP stdio reference adapter | `rpe-mcp` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |

Adapterは提案された行為を評価するだけです。行為の実行、merge、公開、本番承認、責任移転は行いません。

## Canonical runtime path

```text
Python / REST / MCP
        ↓
rpe_kernel.evaluate_action()
        ↓
Applicability Resolution
        ↓
Pack EvaluationとDecision Combination
```

Reference adapterはKernel semanticsを独自に再定義しません。詳細は [`docs/single-source-kernel.md`](docs/single-source-kernel.md) を参照してください。

## GovernanceとCompatibility

- [`docs/requirement-pack-governance.md`](docs/requirement-pack-governance.md)
- [`schemas/external-kernel/requirement-pack-governance.schema.json`](schemas/external-kernel/requirement-pack-governance.schema.json)
- [`docs/contract-compatibility-policy.md`](docs/contract-compatibility-policy.md)
- [`schemas/external-kernel/contract-versions.json`](schemas/external-kernel/contract-versions.json)

Packは、特定された人間が解釈・保守するoperational mappingです。Schema-validであることは、内容が正しい、最新、完全、または特定deploymentに適切であることを意味しません。

## 主要な入口

- Kernel: [`rpe_kernel/pipeline.py`](rpe_kernel/pipeline.py)
- Applicability: [`rpe_kernel/applicability.py`](rpe_kernel/applicability.py)
- Evaluation: [`rpe_kernel/evaluation.py`](rpe_kernel/evaluation.py)
- REST: [`rpe_kernel/http_api.py`](rpe_kernel/http_api.py)
- MCP: [`rpe_kernel/mcp_server.py`](rpe_kernel/mcp_server.py)
- OpenAPI: [`spec/openapi/rpe-kernel.openapi.json`](spec/openapi/rpe-kernel.openapi.json)
- Static catalog: [`site/index.html`](site/index.html)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- AI/Search Reader: [`READMEforAI.md`](READMEforAI.md)

## 次のMilestone

M2は **Governed Pack Integration** です。

1. runtime payloadでversionを明示する
2. runtime boundaryでGovernance eligibilityを扱う
3. boundedな外部Requirement Pack読込を追加する
4. stale、ownerless、ambiguous、suspended、incompatibleなPackを可視的に停止する
5. trace、evidence、repair、resume構造へ進む

## 責任境界

RPEは、承認された機械可読controlを執行・調停するreference kernelです。一般的なsource解釈engine、自動更新knowledge base、認証system、本番governance serviceではありません。

SchemaやcheckerのPASSは、明示されたcheckが通過したことだけを意味します。Source interpretation、現実の適用可能性、evidence sufficiency、deployment approval、execution authority、最終責任は、関係する人間または組織に残ります。

RPEはOpen Constructionとして、[Luminalia AI](docs/ai-assisted-construction-note.md) の支援を受けて開発されています。方向性、merge、公開、外部主張、本番採用、最終責任は人間maintainerに残ります。

## 著作者

著作者: **Akihisa Ono（小野昭久）**  
このリポジトリにおける所属表記: Independent

## License

[MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono（小野昭久）。
