# Zenn Article Title Source Check

This note records the source-check rule for future Zenn article title planning.

It is a planning and navigation note only. It is not a Zenn article draft, publication record, external review result, certification, conformance claim, standardization claim, production approval, API implementation, connector implementation, or AI final-responsibility transfer mechanism.

## Rule

Before proposing or drafting a new Zenn article title for Responsibility Pathway Engineering, check the dedicated Zenn content repository and the existing RPE source-alignment inventory.

Primary repository to check:

- `YutoriKomeiji/zenn-content`
- `articles/`

Primary RPE-side records to check:

- `docs/source-alignment/zenn-article-inventory.md`
- `docs/source-alignment/zenn-source-alignment-synthesis.md`

Do not rely on memory alone when choosing titles, article scope, or publication sequence.

## Current exclusion

The latest article should be excluded from immediate title-planning reuse unless the maintainer explicitly reopens it.

Current latest article identified from the dedicated Zenn content repository:

- `articles/responsibility-pathway-boundary.md`
- title: `「責任」と「経路」は一般語でも、「責任経路」はそれだけでは片づかない`

## Existing explicit-title articles checked

The following existing Zenn articles were checked directly from `YutoriKomeiji/zenn-content/articles/` and should be treated as occupied title / scope territory when planning the next article:

| Path | Current title |
| --- | --- |
| `articles/what-is-responsibility-pathway.md` | `責任経路とは何か――責任経路工学の定義と境界` |
| `articles/responsibility-pathway-engineering.md` | `責任を固定するだけでは足りない――責任経路工学という設計対象` |
| `articles/why-responsibility-pathway-engineering.md` | `なぜ「責任経路工学」だったのか` |
| `articles/responsible-ai-to-responsibility-pathway.md` | `責任あるAIから、責任を扱えるAIへ――AIエージェント時代に必要な責任経路という補助線` |
| `articles/fixed-responsibility-to-pathway.md` | `責任固定から責任経路設計へ――AIガバナンスに必要な「固定後」の設計` |
| `articles/ai-responsibility-node.md` | `AI責任ノード――AIエージェントを責任経路で管理する` |
| `articles/human-return-point.md` | `Human Return Point――HITLと人間監督の再設計` |
| `articles/evidence-log-design.md` | `Evidence Log設計――責任経路を後から再構成するための監査ログ` |
| `articles/stop-authority-design.md` | `Stop Authority設計――AIエージェントの停止権限` |
| `articles/enterprise-agent-checklist.md` | `企業AIエージェント導入チェックリスト――責任経路編` |
| `articles/sap-ai-responsibility-pathway.md` | `SAP×AI時代の責任経路工学――ERP接続編` |
| `articles/iso42001-responsibility-pathway.md` | `ISO/IEC 42001時代の責任経路工学――AIマネジメントシステムを実装粒度へ落とす` |
| `articles/self-application-responsibility.md` | `責任を語る主体も、責任経路の外側には立てない` |

## Existing RPE-side source alignment

The existing RPE article inventory records additional hash / legacy filename candidates and marks the inventoried candidates as aligned.

Do not ignore those hash-named articles when choosing future article scope.

The current synthesis indicates that all inventoried explicit-title candidates and hash / legacy candidates were aligned at the time of that review.

## Title planning implication

Near-term article planning should avoid duplicating these existing article scopes.

Safer next title directions are likely to be operational updates or repository-publication topics, such as:

- how to read the GitHub repository;
- what has changed since the earlier Zenn series;
- why the repository is specification-first;
- what is ready for external review and what is not;
- how API / connector future-shape remains separate from implementation;
- how Zenn publication handoff works between this repository and `YutoriKomeiji/zenn-content`.

## Boundary

This note does not select a final title, authorize publication, or move article text into the Zenn content repository.

The human author or maintainer remains responsible for deciding whether any article title, scope, draft, migration, publication, revision, retraction, repair, or deferral should occur.
