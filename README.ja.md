# Responsibility Pathway Engineering

[![Value Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-rpe-value-demo.yml)
[![Security Hygiene](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-repository-security.yml)
[![Demo](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml/badge.svg?branch=main)](https://github.com/YutoriKomeiji/responsibility-pathway-engineering/actions/workflows/check-demo.yml)

**AIエージェントが外部操作へ進む前に、「この条件で続行してよいか」を判定する実行可能なガバナンス評価レイヤーです。**

Responsibility Pathway Engineering（責任経路工学 / RPE）は、Pythonパッケージとして導入でき、Python API / REST / MCP stdio / OpenAPIから利用できます。適用要件、ガバナンス状態、承認、証拠条件、適用可能性、次の責任担当を評価し、外部操作へ進む前の判断を機械可読に返します。

このリポジトリは文書だけの設計案でも、独立したサンプル関数の寄せ集めでもありません。現在の`main`には、実行可能なパッケージ、サービス用entry point、schema、adapter、test、adversarial checker、CI、およびM2 governed integrationのclosure evidenceがあります。

## まず動かす

Python 3.11+が必要です。runtime packageには追加の外部runtime dependencyはありません。

```bash
git clone https://github.com/YutoriKomeiji/responsibility-pathway-engineering.git
cd responsibility-pathway-engineering
python -m pip install .
```

REST serviceを起動します。

```bash
rpe-rest --host 127.0.0.1 --port 8080
```

起動確認:

```bash
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/openapi.json
```

ガバナンス必須の評価endpointは次です。

```text
POST /v1/evaluate/governed
```

同じ評価kernelはPython APIとMCP stdioからも利用できます。

## 実際に何をするのか

RPEは「AIが提案した」と「実行系が続行してよい」の間に入ります。

```text
AI / 自動化が操作を提案
        ↓
request + Requirement Pack + governance情報をRPEへ渡す
        ↓
入力受付・contract compatibility
        ↓
Pack ↔ governance binding・governance eligibility
        ↓
applicability・requirement evaluation
        ↓
allow / hold / human_gate / deny
        ↓
reason code + 不足条件 + responsibility handoff
        ↓
後段のexecutor / runtime / 人間 / 組織
```

たとえば条件を満たさない場合、単なる失敗ではなく、機械可読な形で停止理由を返します。

```json
{
  "decision": "human_gate",
  "stage": "governance",
  "reason_codes": ["RPE-PACK-GOV-NOT-YET-EFFECTIVE"],
  "human_return": {"role": "governance_review_owner"}
}
```

実際のreasonは入力したgoverned envelopeと評価条件に依存します。

## 最短のbefore / after

```bash
python scripts/value_demo.py
```

同じsynthetic proposalを、naiveな続行とRPE経由の両方に通し、RPEを入れたときにobservable behaviorがどう変わるかを確認できます。

より広いwalkthrough:

```bash
python scripts/demo.py
```

価値主張と証拠範囲は [`docs/why-rpe.md`](docs/why-rpe.md) に記録しています。

## 現在実装されている入口

| Surface | Entry | 現在の状態 |
|---|---|---|
| Python | `evaluate_action()` | legacy / M1-compatible evaluation |
| Python | `evaluate_governed_action()` | strict governed M2 evaluation |
| REST | `POST /v1/evaluate` | 実行可能なlocal reference route |
| REST | `POST /v1/evaluate/governed` | 実行可能なgoverned route |
| MCP stdio | `rpe_evaluate_action` | 実行可能tool |
| MCP stdio | `rpe_evaluate_governed_action` | 実行可能governed tool |
| OpenAPI 3.1 | 両route | repository/package/runtime parityを検査 |
| Loader | caller JSON / 明示local file | bounded governed-envelope loading |

`pyproject.toml`にはCLI entry pointも定義されています。

```text
rpe-rest = rpe_kernel.http_api:main
rpe-mcp  = rpe_kernel.mcp_server:main
```

## 単純な`if`文と何が違うのか

strict governed pathでは、1個のbooleanへ潰さず、異なるfailure classを別々に扱います。

- contract version compatibility
- Requirement Pack / governanceのidentity・version binding
- source authority / source version / jurisdictionのbinding field
- governance lifecycle / date eligibility
- 複数Packのapplicability resolution
- requirement evaluationとdecision combination
- stable reason codeとHuman Return
- responsibility handoff metadata
- caller content / local fileのbounded provenance
- REST / MCP / OpenAPIのparity・drift check

さらに、misbinding、version drift、invalid governance、unknown applicability、schema mismatch、authority inflationなどを意図的に壊すnegative checkをCIで実行しています。

M2 closure evidence:

- [`docs/m2-r5-adversarial-closure-evidence.md`](docs/m2-r5-adversarial-closure-evidence.md)
- validated PR head: `ae2581ef3c68643687775e111fa8561b974fb2b8`
- merged-main closure anchor: `6edf1a0b501b7b25663ddc7fb942aa087c0db0f2`

現在の実装概要: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md)

## Python API

互換entry:

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

strict governed entry:

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

詳細: [`docs/python-package-api.md`](docs/python-package-api.md)

## REST / MCP / OpenAPI

- REST: [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md)
- MCP stdio: [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md)
- OpenAPI: [`docs/integrations/openapi.md`](docs/integrations/openapi.md)

これらは既存の実行stackの前段に置くための評価interfaceです。RPEはpolicy evaluationとaction executionを同じAuthorityへ潰さない設計になっています。

## Architecture boundary

ここから下は「何も実装されていない」という意味の免責ではなく、実装済み評価層と後段実行層を分離するためのarchitecture boundaryです。

RPEの`allow`は、

> 与えられたrequestが、今回評価したRPE条件を満たした

ことを意味します。

一方、それだけでは、

> 組織上の最終実行権限が与えられた / 外部操作が実行された / 意図したexternal effectまで確認された

ことを意味しません。

そのためgoverned resultは、

```json
{
  "authority_effect": "none",
  "decision_scope": "evaluation_only"
}
```

を保持し、別のdispatch authorityやeffect verificationが必要であることをhandoffとして返します。

この分離によって、RPEはexecutorへ変質せず、executorの前段へ挿入できます。

## 現在のscope

RPEが提供するのは上記のgoverned evaluation layerです。application authentication、TLS termination、tenancy、persistent operational state、external dispatch、retry orchestration、reconciliation、effect verificationなど、後段runtimeや組織が持つべき機能はRPEの評価kernelには統合していません。

同様に、RPEは与えられたmachine-readable controlを評価しますが、法的・組織的Authorityそのものを生成しません。

これらは「未実装なので何もできない」という説明ではありません。実装済みsurfaceと再現方法は上で明示しています。

## Verification

RPEでは、主張を具体的なcode、schema、checker、commit、failure caseへ結び付けます。

CI PASSはそのnamed checkがtested conditionで通った証拠です。形式化された性質がある場合も、明示したmodelとassumptionの範囲に限定します。それを自動的にlegal certification、production approval、external effect proofへ拡張しません。

- [`docs/verification-assurance-and-open-governance.md`](docs/verification-assurance-and-open-governance.md)
- [`docs/claim-boundary-promotion.ja.md`](docs/claim-boundary-promotion.ja.md)
- [`docs/support-maturity.md`](docs/support-maturity.md)

## 主要リンク

- [RPEを使う理由](docs/why-rpe.md)
- [M2 closure evidence](docs/m2-r5-adversarial-closure-evidence.md)
- [現在のM2実装状態](docs/m2-governed-integration-current.md)
- [Python API](docs/python-package-api.md)
- [Requirement Packガバナンス](docs/requirement-pack-governance.md)
- [互換性ポリシー](docs/contract-compatibility-policy.md)
- [ロードマップ](ROADMAP.md)
- [公開カタログ](site/index.html)
- [AI/Search Reader](READMEforAI.md)

## 開発とライセンス

著作者: **Akihisa Ono（小野昭久）**  
Repository affiliation: Independent

RPEはOpen Constructionとして [Luminalia AI](docs/ai-assisted-construction-note.md) の支援を受けて開発されています。方向性、レビュー、マージ、公開上の主張、デプロイ判断、最終責任は人間のメンテナーが担います。

[MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono（小野昭久）。
