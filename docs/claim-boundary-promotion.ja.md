# Claim Boundary Promotion（主張境界の昇格）

RPEでは公開上の主張をevidence-governed stateとして扱います。現在のnon-claimを自動的に永久免責とはみなしません。

RPEは次を分離します。

1. 宣言したengineering / field evidenceが揃いreviewされれば前進できる **evidence-limited milestone boundary**
2. engineering kernel単体では越えるべきでない **permanent responsibility boundary**

## Current Evidence Boundary

RPEはM1-onlyの実装境界を越え、現在は **M2実装中 / governed-integration baseline到達** の状態です。

現時点のengineering evidenceが支えるもの:

- explicit strict governed contract
- governed contract-version check
- Packとgovernance recordのbinding
- runtime governance eligibility
- stale / ambiguous / ineligible / incompatibleな主要failure classのvisible stop
- legacy / governed Python・REST・MCP surface
- governed OpenAPI
- caller-content / local-fileに限定したbounded loader
- `authority_effect = none` / `decision_scope = evaluation_only` によるno-authority handoff
- これらに対するdeterministic regression / CI

ただし **M2全体のclosureはまだ主張しません**。残るengineering evidenceは、uncertainty / effect / evidence handoff、repair / resume責任境界、residual owner / Human Return continuity、adversarial validation、closure reviewです。

公開実装の現在地は [`m2-governed-integration-current.md`](m2-governed-integration-current.md) に記録します。

## Promotion Criteria

| 現在の境界 | 境界を前進させるevidence |
|---|---|
| M2 governed-integration baseline / M2全体は未closure | authority/effect/evidence混同、repair/resume境界、residual-owner/Human Return continuityに対するadversarial evidence、宣言したclosure criteria、同期済みpublic claim review |
| production deployment未主張 | deployment architecture、authentication/authorization boundary、operational monitoring、fault injection、upgrade/rollback、supported environment evidence |
| reviewed real-world normative mapping未主張 | source/version control、named human owner、applicability/interpretation record、conflict handling、review/approval state、expiry/supersession control、主張対象mappingごとのqualified independent review |
| implementation-wide formal conformance未主張 | formalization target、model-to-runtime correspondence/refinement relation、主張対象implementation surfaceの再現可能evidence |
| broader interoperability未主張 | 宣言したschema/interface/compatibility policy/failure semanticsに対する独立implementation/client evidence |

Engineering milestone完了だけでlegal、compliance、certification、production、operational authority claimへ自動昇格することはありません。

## Permanent Responsibility Boundaries

- RPEはlaw、policy、ethics、standard、affected-party mandateを自動解釈しません。
- RPE単体はdeployment approval、execution authority、certification、legal complianceを生成しません。
- schema-validまたはload可能なRequirement Packはsource interpretationの正しさ・最新性・完全性・適用可能性を証明しません。
- RPEの`allow`はevaluation resultであり、execution authorization tokenではありません。
- evaluation evidenceはexternal effectの発生を証明しません。
- receiptだけではverified effectを意味しません。
- repair readinessはrepair authorityを生成しません。
- resume authorityはexecutionを所有するruntime / institution側にあり、別のauthority-bearing transitionを必要とします。
- gate resultはexternal action、external system、business decisionそのものの正しさを生成しません。
- legal、policy、assurance、deployment、operational decisionの最終責任は責任主体である人間・制度に残ります。
- abstract modelへのformal proofだけでPython runtime全体、Pack interpretation、deployed system全体を証明済みと扱いません。

これらは未完了milestoneではなく責任境界です。

## Evidence Owner / Promotion State

RPE engineeringはkernel、schema、interface、compatibility、failure semantics、loader boundary、宣言したimplementation evidenceを担当します。Pack ownerとqualified reviewerはsource interpretation / mapping evidenceを担当します。Integrator/operatorはdeployment、execution authority、external effect、repair/resume、operational evidenceを担当します。Legal、certification、final authorizationは資格・権限を持つ人間／制度に残ります。

可能な範囲でevidence依存境界は `evidence_collecting` / `review_ready` / `promoted`、恒久境界は `permanently_out_of_scope` を使います。
