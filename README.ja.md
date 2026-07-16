# Responsibility Pathway Engineering

**AIシステムのための、実行可能なResponsible AI制御。**

責任経路工学（Responsibility Pathway Engineering / RPE）は、Responsible AI要件を実行時制御へ変換するための、持ち運び可能な外部責任カーネルとコンポーネント群です。

```text
Responsible AI要件
        ↓
機械可読なRequirement Pack
        ↓
AI Action Request
        ↓
RPE外部カーネル
        ↓
allow / hold / human_gate / deny
        ↓
理由コード・適用判定・不足情報・人間への戻り先
```

RPEは、どの要件が適用されるか、行為を継続できるか、何が不足しているか、どこで人間または組織へ責任を戻すべきかを、構造化された結果として返します。

## インストールと基本呼び出し

現在のreference implementationは、Python 3.11以上で動作する依存なしの小さなpackageです。

```bash
python -m pip install .
```

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

すべてのruntime interfaceは、この同じpackage APIへ委譲します。

| Interface | 起動・入口 | 文書 |
|---|---|---|
| Python package | `from rpe_kernel import evaluate_action` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| Local REST adapter | `rpe-rest` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| OpenAPI 3.1 contract | `GET /openapi.json` | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |
| MCP stdio adapter | `rpe-mcp` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |

REST adapterは次の経路を公開します。

```text
GET  /health
GET  /openapi.json
POST /v1/evaluate
```

MCP adapterは、次の1つのbounded toolを公開します。

```text
rpe_evaluate_action
```

RESTとMCPは、提案された行為を評価するだけです。行為の実行、merge、公開、本番承認、責任移転は行いません。

## 実行例

単一Pack:

```bash
python scripts/run_external_kernel.py \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-action-request.json
```

複数Pack:

```bash
python scripts/run_external_kernel_multi.py \
  examples/external-kernel/minimal-action-request.json \
  examples/external-kernel/minimal-requirement-pack.json \
  examples/external-kernel/minimal-data-handling-pack.json
```

原初の15秒demo:

```bash
python scripts/demo.py
```

## 現在実装されているもの

- Requirement PackのApplicability Resolution
- deterministicなMulti-Pack Evaluation
- `allow`、`hold`、`human_gate`、`deny`の構造化Decision
- import可能なPython package API
- local REST adapter
- REST自身が返すOpenAPI 3.1 contract
- bounded MCP stdio adapter
- source metadata、理由コード、不足要件、人間への戻り先
- schema、synthetic fixture、checker、GitHub Actions
- RESTとMCPによるKernel semanticsの再実装を防ぐsingle-source guard

Canonical runtime pathは次です。

```text
Python / REST / MCP
        ↓
rpe_kernel.evaluate_action()
        ↓
Applicability Resolution
        ↓
Pack EvaluationとDecision Combination
```

実装ドリフト防止規則は [`docs/single-source-kernel.md`](docs/single-source-kernel.md) を参照してください。

## 主要な入口

| 対象 | ファイル |
|---|---|
| Kernel package | [`rpe_kernel/pipeline.py`](rpe_kernel/pipeline.py) |
| Applicability Resolver | [`rpe_kernel/applicability.py`](rpe_kernel/applicability.py) |
| Pack Evaluator | [`rpe_kernel/evaluation.py`](rpe_kernel/evaluation.py) |
| REST Adapter | [`rpe_kernel/http_api.py`](rpe_kernel/http_api.py) |
| MCP Adapter | [`rpe_kernel/mcp_server.py`](rpe_kernel/mcp_server.py) |
| OpenAPI Contract | [`spec/openapi/rpe-kernel.openapi.json`](spec/openapi/rpe-kernel.openapi.json) |
| Architecture | [`docs/architecture/external-responsibility-kernel.md`](docs/architecture/external-responsibility-kernel.md) |
| Product Roadmap | [`docs/external-kernel-roadmap.md`](docs/external-kernel-roadmap.md) |
| Project Roadmap | [`ROADMAP.md`](ROADMAP.md) |
| AI/Search Reader入口 | [`READMEforAI.md`](READMEforAI.md) |

## Requirement Pack

Requirement Packは、法令mapping、standard、guideline、組織policy、またはsynthetic test requirementを、実行可能なcontrolへ変換します。

Packには、適用条件、必要context、decision behavior、reason-code namespace、人間への戻り先、source authority、jurisdiction、version、effective date、review owner、interpretation statusを記録できます。

同梱されるPackはsynthetic exampleです。実際の法令・standard・policy由来Packには、source-specificな人間reviewと継続的maintenanceが必要です。

## 現在の方向

Kernel packageと最初のportable interfaceは実装済みです。次の主な作業は以下です。

1. request/result contractとschema-version policyの安定化
2. 外部Requirement Packのboundedな読込・validation
3. Kernel semanticsを複製しないintegration example
4. trace、repair、resume、evidence処理の強化
5. authentication、authorization、tenancy、persistence、deployment controlなど本番境界の研究

## 構築と責任境界

RPEはOpen Constructionとして、[Luminalia AI](docs/ai-assisted-construction-note.md) の支援を受けて開発されています。

AIは草案、実装、検査を支援しますが、方向性、merge、公開、外部主張、本番採用、最終責任は人間maintainerに残ります。

RPEは、法的正しさ、安全性、遵法性、公平性、認証、社会的妥当性、本番承認を単独で成立させるものではありません。

schemaやcheckerのPASSは、明示された機械可読checkが通過したことだけを意味します。現実の適用可能性、source interpretation、evidence sufficiency、deployment approval、execution authority、最終責任は、関係する人間または組織に残ります。

## 著作者

著作者: **Akihisa Ono（小野昭久）**  
このリポジトリにおける所属表記: Independent

- [Provenance](docs/provenance.md)
- [Authorship](AUTHORSHIP.md)
- [Open Construction](OPEN_CONSTRUCTION.md)
- [Citation metadata](CITATION.cff)

## License

[MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono（小野昭久）。帰属とAI支援の表示は [NOTICE.md](NOTICE.md) を参照してください。
