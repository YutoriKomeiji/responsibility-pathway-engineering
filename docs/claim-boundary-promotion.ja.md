# Claim Boundary Promotion（主張境界の昇格）

RPEでは公開上の主張をevidence-governed stateとして扱います。現在のnon-claimを自動的に永久免責とはみなしません。

RPEは次を分離します。

1. 宣言したengineering / field evidenceが揃いreviewされれば前進できる **evidence-limited milestone boundary**
2. engineering kernel単体では越えるべきでない **permanent responsibility boundary**

## Current Evidence Boundary

RPEは現在 **M1 Governed Reference Kernel** です。M1 evidenceが支えるのは、deterministic reference kernel、applicability resolution、multi-pack evaluation、reference interface、lifecycle/maintenance governance、compatibility rule、schema、fixture、checker、CI guardです。

M1にはまだ、external pack loading、`evaluate_action()`内部でのgovernance enforcement、本番deployment control、review済み実世界Requirement Mapping、implementation-wide formal conformanceは含まれません。

## Promotion Criteria

| 現在の境界 | 境界を前進させるevidence |
|---|---|
| M1のみ / governed external pack integration未実装 | bounded external pack loading、runtime governance eligibility、stale/ownerless/ambiguous/suspended/incompatibleを可視的に止める処理、trace/evidence/repair/resume behaviorに関するM2実装・test |
| production deployment未主張 | deployment architecture、authentication/authorization boundary、operational monitoring、fault injection、upgrade/rollback、supported environment evidence |
| reviewed real-world normative mapping未主張 | source/version control、named human owner、applicability/interpretation record、conflict handling、review/approval state、expiry/supersession control、主張対象mappingごとのqualified independent review |
| implementation-wide formal conformance未主張 | formalization target、model-to-runtime correspondence/refinement relation、主張対象implementation surfaceの再現可能evidence |
| broader interoperability未主張 | 宣言したschema/interface/compatibility policy/failure semanticsに対する独立implementation/client evidence |

Milestone完了だけでlegal、compliance、certification、production、operational authority claimへ自動昇格することはありません。

## Permanent Responsibility Boundaries

- RPEはlaw、policy、ethics、standard、affected-party mandateを自動解釈しません。
- RPE単体はdeployment approval、execution authority、certification、legal complianceを生成しません。
- schema-validなRequirement Packはsource interpretationの正しさ・最新性・完全性・適用可能性を証明しません。
- gate resultはexternal action、external system、business decisionそのものの正しさを生成しません。
- legal、policy、assurance、deployment、operational decisionの最終責任は責任主体である人間・制度に残ります。
- abstract modelへのformal proofだけでPython runtime全体、Pack interpretation、deployed system全体を証明済みと扱いません。

これらは未完了milestoneではなく責任境界です。

## Evidence Owner / Promotion State

RPE engineeringはkernel、schema、interface、compatibility、failure semantics、宣言したimplementation evidenceを担当します。Pack ownerとqualified reviewerはsource interpretation / mapping evidenceを担当します。Integrator/operatorはdeployment / operational evidenceを担当します。Legal、certification、final authorizationは資格・権限を持つ人間／制度に残ります。

可能な範囲でevidence依存境界は `evidence_collecting` / `review_ready` / `promoted`、恒久境界は `permanently_out_of_scope` を使います。
