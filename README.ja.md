# Responsibility Pathway Engineering

**AIシステムのための、実行可能なResponsible AI制御。**

責任経路工学（Responsibility Pathway Engineering / RPE）は、明示的に範囲を定めた機械可読Responsible AI controlを評価するための、portableな外部責任kernelです。

```text
Responsible AI要件
        ↓
人間がscope/interpretationを定めたRequirement Pack
        ↓
AI Action Request
        ↓
RPE external kernel
        ↓
allow / hold / human_gate / deny
        ↓
reason code・governance・applicability・必要evidence・Human Return
```

RPEは、どの要件が適用されるか、明示されたcontrolの下で提案行為を継続できるか、何が不足しているか、どこで責任を人間・制度へ返すべきかを評価します。

## 長期方向：人間review済みの規範要求をbounded controlへ

RPEは、法令、公的ガイドライン、標準、組織規程、専門職上の義務、影響当事者とのcommitmentに対する**人間・制度によるreview済み解釈**を、限定された機械可読controlへ変換するための公開的・検査可能な工学基盤を目指します。

```text
公式または正当に承認された規範source
        ↓
人間・制度によるscope / interpretation / review / approval
        ↓
source metadataとgovernance stateを持つversioned Requirement Pack
        ↓
RPE governed evaluation
        ↓
allow / hold / human_gate / deny + reason + Human Return
        ↓
別系統のassurance / legal review / execution authority / operational responsibility
```

RPEはlegal interpretation、approval authority、execution authority、final responsibilityをkernelへ移しません。自動compliance engine、法的助言主体、自動更新regulatory database、認証機関、法務・政策・安全・assurance・運用統治の代替ではありません。

## 現在地 — M2実装中

RPEはM1-onlyの実装境界を越え、現在は **M2実装中 / governed-integration baseline到達** の状態です。

**M2全体のclosureはまだ主張しません。**

現在の公開実装状態: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md)

実装済み:

- deterministic applicability resolution / multi-pack evaluation
- legacy/M1-compatible Python entry `evaluate_action()`
- explicit strict governed Python entry `evaluate_governed_action()`
- governed contract familyとruntime version handling
- Requirement Pack / governance recordのidentity・version binding
- strict governance eligibilityとvisible fail-closed outcome
- legacy / governed REST reference route
- legacy / governed MCP stdio tool
- admission / compatibility / governance / applicability / evaluationを表現するOpenAPI 3.1
- repository / package / runtime OpenAPI drift check
- caller-content / local-fileに限定したbounded governed-envelope loader
- first loaderでのnetwork / registry loading明示拒否
- `authority_effect = none` / `decision_scope = evaluation_only` を保持するresponsibility handoff
- schema / synthetic fixture / deterministic regression / CI guard

## 二つのruntime entry

### Legacy / M1-compatible

```python
from rpe_kernel import evaluate_action

result = evaluate_action(action_request, requirement_packs)
```

互換性のため保持している入口です。

### Strict governed M2

```python
from rpe_kernel import evaluate_governed_action

result = evaluate_governed_action(governed_envelope)
```

Strict governed path:

```text
governed envelope admission
        ↓
contract compatibility
        ↓
Pack ↔ governance binding
        ↓
governance eligibility
        ↓
applicability resolution
        ↓
requirement evaluation
        ↓
decision combination
        ↓
responsibility-preserving handoff
```

M2 gateをoptional flagとして「付け忘れられる」形ではなく、strict governed entryとして明示的に分離しています。

## 重要なAuthority境界

RPEの`allow`は **evaluation result** であり、execution authorization tokenではありません。

RPE単体は次を行いません。

- external actionのdispatch / execution
- production deployment approval
- external effectが起きたことのverification
- receiptをverified effect evidenceへ昇格
- repair可能性からrepair authorityを生成
- blocked pathが再開可能になっただけでresume authorityを生成
- final responsibilityをAIへ移転

Evaluation evidenceはeffect evidenceではありません。Repair readinessはrepair authorityではありません。Resume authorityはexecutionを所有するruntime / institution側にあり、別のauthority-bearing transitionを必要とします。

この境界は後段runtimeで得られたimplementation experienceをRPEへ必要最小限反映したものであり、RPEをOSやexecution controllerへ変えるものではありません。

## Bounded loading

現在のloaderが受け入れるのは次だけです。

- caller-provided UTF-8 JSON content
- 明示指定されたlocal file

```python
from rpe_kernel import load_governed_envelope_content, load_governed_envelope_file
```

first loaderはURL fetch、remote registry discovery、package install、source trust establishmentを行いません。

fileが読めたことは、そのpathにbytesが存在したというtransport observationにすぎません。source authority、semantic correctness、governance eligibility、legal validity、current applicabilityは証明しません。

## Install / Reference Interface

```bash
python -m pip install .
```

| Interface | Legacy entry | Strict governed entry | 文書 |
|---|---|---|---|
| Python package | `evaluate_action()` | `evaluate_governed_action()` | [`docs/python-package-api.md`](docs/python-package-api.md) |
| Local REST | `POST /v1/evaluate` | `POST /v1/evaluate/governed` | [`docs/integrations/rest-api.md`](docs/integrations/rest-api.md) |
| MCP stdio | `rpe_evaluate_action` | `rpe_evaluate_governed_action` | [`docs/integrations/mcp-stdio.md`](docs/integrations/mcp-stdio.md) |
| OpenAPI 3.1 | 両方を記述 | 両方を記述 | [`docs/integrations/openapi.md`](docs/integrations/openapi.md) |

Adapterは提案行為を評価するだけです。行為のexecution、deployment approval、release publication、merge、external effect verification、責任移転は行いません。

## Claim boundary / Promotion

RPEは、**evidenceが揃えば前進できるmilestone boundary**と、**engineering kernel単体では越えるべきでないpermanent responsibility boundary**を分離します。

詳細: [`docs/claim-boundary-promotion.ja.md`](docs/claim-boundary-promotion.ja.md)

M1-onlyのgoverned-integration境界は前進しました。strict runtime governance、compatibility、binding、adapter parity、bounded local/caller-content loadingにはimplementation/CI evidenceがあります。

ただし次は自動昇格しません。

- production readiness
- legal / compliance correctness
- certification / conformity
- reviewed real-world normative mapping
- execution authority
- verified external effect
- implementation-wide formal conformance
- official-standard status

Promotionはevidenceごとに明示的に行います。

## 検証可能性・AI Assurance・公開Governance

RPEは、blanketな「安全」宣言ではなく、boundedでinspectableなclaimからVerifiable AI / AI Assuranceへ接続します。

Formalizationは、明示したmodelとassumptionの範囲でresponsibility pathwayのpropertyを証明対象にできます。ただし、そのproofだけでPython runtime全体、source interpretation、legal validity、operational behavior、production safetyを証明済みとは扱いません。

Public guidanceは将来のhuman-reviewed Requirement Packのsourceになり得ますが、RPEはlaw/guidanceを自動解釈せず、schema-validまたはload可能なPackが正しいlegal/normative interpretationを含むとは主張しません。

RPEはMIT Licenseで公開し、open specification、interoperability、independent verification、multiple implementation potentialを重視します。現時点でofficial standardではありません。

## 主要な入口

- Current M2 status: [`docs/m2-governed-integration-current.md`](docs/m2-governed-integration-current.md)
- Kernel: [`rpe_kernel/pipeline.py`](rpe_kernel/pipeline.py)
- Loader: [`rpe_kernel/loader.py`](rpe_kernel/loader.py)
- Applicability: [`rpe_kernel/applicability.py`](rpe_kernel/applicability.py)
- Evaluation: [`rpe_kernel/evaluation.py`](rpe_kernel/evaluation.py)
- Governance: [`rpe_kernel/governance.py`](rpe_kernel/governance.py)
- Compatibility: [`rpe_kernel/compatibility.py`](rpe_kernel/compatibility.py)
- REST: [`rpe_kernel/http_api.py`](rpe_kernel/http_api.py)
- MCP: [`rpe_kernel/mcp_server.py`](rpe_kernel/mcp_server.py)
- OpenAPI: [`spec/openapi/rpe-kernel.openapi.json`](spec/openapi/rpe-kernel.openapi.json)
- Claim boundary: [`docs/claim-boundary-promotion.ja.md`](docs/claim-boundary-promotion.ja.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- AI/Search Reader: [`READMEforAI.md`](READMEforAI.md)

## 残るM2 work

次のM2は「RPEへexecution machineryを増やす」工程ではありません。evaluationからdownstream runtimeへ渡すresponsibility handoffを、誤用しにくくする工程です。

優先:

1. uncertainty / effect / evidence handoff semantics
2. repair / resume **requirement** を明示しつつrepair/resume authorityをRPEへ持ち込まない
3. residual owner / Human Return continuity
4. authority confusion、evidence confusion、stale/binding/governance failure、adapter drift、loader boundary violationのadversarial validation
5. public claim syncとM2 closure evidence

詳細: [`ROADMAP.md`](ROADMAP.md)

## 責任境界

RPEは承認済みmachine-readable controlを評価・調停するreference kernelです。general legal reasoning engine、自動更新knowledge base、certification system、production governance service、official standard、execution controllerではありません。

Schema/checker/CI PASSやloader successが意味するのは、宣言されたmachine-readable checkが通ったことだけです。Source interpretation、real-world applicability、evidence sufficiency、deployment approval、execution authority、external-effect verification、final responsibilityは関係する人間・制度に残ります。

## Open Construction

RPEはOpen Constructionとして [Luminalia AI](docs/ai-assisted-construction-note.md) の支援を受けて開発されています。Direction、review、merge、publication claim、deployment decision、final responsibilityはhuman maintainerに残ります。

著作者: **Akihisa Ono（小野昭久）**  
Repository affiliation: Independent

## License

[MIT License](LICENSE) の下で公開されています。

Copyright (c) 2026 Akihisa Ono（小野昭久）。
