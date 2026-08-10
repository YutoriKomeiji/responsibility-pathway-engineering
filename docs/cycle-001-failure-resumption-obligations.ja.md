<!--
Language: Japanese
Document-Type: Engineering obligation note
Status: Candidate
-->

# RP-CYCLE-001 — failure-to-resumption 工学義務

この文書は、RPOS Cycle 001 から返却された知見と Responsibility Pathway Runtime の既存実装レビューを、再利用可能な Engineering 層の義務として整理する。

これは法的責任、production authorization、compliance、組織責任、実装全体の正しさを定義するものではない。Cycle 001 で得られた限定的な証拠を、failure-to-resumption slice と互換性を主張する実装向けの工学制約へ変換する。

## 証拠クラス

Cycle 001 では、次の証拠を相互代替してはならない。

- formal/model evidence は形式化したモデルと仮定についてのみ述べる。
- executable tests はテストされた実装と環境についてのみ述べる。
- operational observation は観測された外部状態についてのみ述べる。
- evaluation、dependency、supply-chain evidence は判断材料にはなり得るが、それ自体は実行権限も外部効果の検証も生成しない。
- responsibility packet や完成した文書は情報を運ぶが、権限を生成しない。

## 必須工学性質

### 1. 不明な効果を明示的に保持する

dispatch 済み、または dispatch された可能性があるが外部効果が検証されていない操作について、実装は明示的な不確実状態を持たなければならない。

レイヤごとに名称は異なってよい。RPOS は `EFFECT_UNKNOWN`、RPR は `write_status_unknown` を用いる。互換性に必要なのは名前の統一ではなく、不確実性の意味保存である。

receipt、transport acknowledgement、local persistence、executor return のみを根拠として、verification contract を満たさないまま verified completion にしてはならない。

### 2. receipt と verified effect は代替不可

成功した dispatch receipt や local result を、意図した外部効果が実際に生じた証拠として扱ってはならない。

完了には、その操作で宣言された verification contract に適した証拠が必要である。検証が存在しない、失敗した、または検証自体が不確実な場合、pathway は unresolved のまま保持するか、明示的な repair/reconciliation 経路へ入らなければならない。

### 3. reconciliation は暗黙の redispatch をしてはならない

不確実な persisted attempt の reconciliation は、別途 authorization された execution transition が作られない限り、観測と分類のみでなければならない。

restart recovery は prior attempt identity を保持し、process restart を同じ外部 mutation の再dispatch許可として扱ってはならない。

### 4. repair readiness は authority restoration ではない

repair completion は `READY_TO_RESUME` 相当の状態を成立させてもよいが、その状態自体が execution authority を付与してはならない。

repair evidence が示すのは再検討可能な技術的・運用的準備状態であり、新しい attempt を実行してよいかどうかではない。

### 5. resume は明示的な authority-bearing transition

resume は configured resume authority による明示的な decision または operation として表現しなければならない。

resume を retry の省略形として実装したり、repair成功だけから自動推論したりしてはならない。

resume record は、可能な限り repaired prior attempt と authorized next attempt を識別できるべきである。

### 6. resumed execution は fresh attempt

再開後の mutation は failed/uncertain prior attempt と異なる execution-attempt identity を使用しなければならない。

operation-level idempotency でattempt間を関連づけてもよいが、evidence、failure、repair、reconciliation の履歴を監査可能に保つため attempt identity は分離する。

### 7. Human Return Point と Residual Owner は failure を越えて保持する

pathway definition または durable responsibility record は、failure、uncertainty、repair、restart、resumption を越えて Human Return Point と Residual Owner を保持しなければならない。

unresolved または不可逆な residual effect は明示的な residual owner に残る。実行が停止した、文書が生成された、automationが先へ進めない、といった理由で責任が消えたと推論してはならない。

### 8. authority effect を持たない evidence は state-neutral を維持する

evaluation result、dependency evidence、supply-chain evidence、diagnostics、handoff packet は、明示的な契約と必要なauthorityによるtransitionがない限り execution authority を変更してはならない。

informational evidence の既定の authority effect は none である。

### 9. path existence は liveness ではない

有効な recovery path が存在することは、実装、operator、organization が最終的にそのpathを完了することを意味しない。

test と formal model は reachability/path-existence claim と liveness/eventual-completion claim を区別しなければならない。

## Anti-patterns

次は Cycle 001 の Engineering 解釈と非互換である。

- `receipt == effect`
- `repair_complete == authorized`
- `resume == retry`
- resumed execution で failed attempt identity を再利用する
- prior outcome 不明を理由に restart 後自動redispatchする
- evaluator/dependency evidence を execution permission とみなす
- completed responsibility packet を authority transfer とみなす
- unresolved state で Residual Owner / Human Return Point を失う
- recovery reachability を eventual completion の証明として提示する

## 最小 trace 要件

互換実装は、少なくとも次の関係を durable evidence から再構成可能にすべきである。

1. pathway identity
2. prior execution attempt identity
3. uncertainty classification と reason
4. reconciliation で利用した observations
5. repair evidence と repair owner
6. repair後の readiness state
7. explicit resume authority と decision
8. fresh next-attempt identity
9. new attempt の verification evidence
10. unresolved/abort 時の Residual Owner と Human Return Point

これらは複数のevent/recordへ分散してよい。owning durable record が利用可能で追跡可能なら、すべてのeventへ重複格納する必要はない。

## Counterexample-oriented acceptance criteria

この Cycle 001 behavior を主張する実装は、最低限、次を限定的テストで示すべきである。

- acknowledgementだけではpathwayがcompleteしない
- uncertain attemptがredispatchなしでrestartを越えられる
- unresolved reconciliationはunresolvedのまま残る
- verified-not-applied reconciliationが明示的repair pathへ入る
- repair completionだけではresumeできない
- unauthorized resumeが拒否される
- authorized resumeにはfresh attempt identityが必要
- resumed attemptをprior failed attemptとは独立にverifyできる
- unresolved residualsをResidual Owner以外がcloseできない
- informational evidenceが暗黙にauthority stateを変えない

## 現在のcross-layer evidence

RPOS Cycle 001 は uncertainty、repair、readiness、explicit resume、fresh attempt、reconciliation、evidence-class separation、authority-neutral responsibility packets について限定的なLean/Python evidenceを提供した。

RPR Cycle 001 はpublic runtime既存実装をレビューし、restart/reconciliation と repair/explicit-resume/fresh-attempt を含む同等の限定的な実行挙動が既に存在すると判断した。そのため redundantなruntime behaviorを追加せず、`reviewed-no-code-change-required` としてreceiving issueをclosedした。

この文書は、それらを受けるRPE Engineering artifactである。将来のRPE/RPR変更では、後続cycleが新しい証拠とレビューにより明示的に改訂しない限り、これらの義務を保持する。
