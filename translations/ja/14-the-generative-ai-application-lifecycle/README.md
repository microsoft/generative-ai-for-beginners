[![function callingとの統合](../../../translated_images/ja/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# ジェネレーティブ AI アプリケーションのライフサイクル

すべての AI アプリケーションにとって重要な問いは、AI が急速に進化する分野であるため、AI 機能の関連性です。アプリケーションを関連性があり信頼性が高く堅牢な状態に保つためには、それを継続的に監視、評価、改善していく必要があります。そこでジェネレーティブ AI のライフサイクルが登場します。

ジェネレーティブ AI のライフサイクルは、ジェネレーティブ AI アプリケーションを開発、展開、維持する各段階を案内するフレームワークです。目的を定義し、パフォーマンスを測定し、課題を特定し、解決策を実行するのに役立ちます。また、アプリケーションをドメインやステークホルダーの倫理的・法的基準に合わせる手助けもします。ジェネレーティブ AI のライフサイクルに従うことで、常に価値を提供しユーザーを満足させるアプリケーションを保証できます。

## はじめに

この章では、次のことを学びます：

- MLOps から LLMOps へのパラダイムシフトの理解
- LLM ライフサイクル
- ライフサイクルツール
- ライフサイクルのメトリフィケーションと評価

## MLOps から LLMOps へのパラダイムシフトの理解

LLM は人工知能の新たな道具であり、分析や生成タスクにおいて非常に強力ですが、この力は AI や従来の機械学習タスクの合理化に影響を及ぼします。

これにより、動的かつ正しいインセンティブに基づいてこのツールを適応させる新しいパラダイムが必要です。古い AI アプリは「ML アプリ」と分類でき、新しい AI アプリは「GenAI アプリ」や単に「AI アプリ」と呼び、その時代の主流技術と手法を反映します。この変化は多方面にわたり、次の比較を参照してください。

![LLMOps 対 MLOps 比較](../../../translated_images/ja/01-llmops-shift.29bc933cb3bb0080.webp)

LLMOps では、アプリ開発者により焦点を当て、統合を重要ポイントとし、「Models-as-a-Service」を利用、そして以下のメトリクスを考慮しています。

- 品質：応答の質
- 有害性：責任ある AI
- 正直さ：応答の根拠（筋が通っているか？正しいか？）
- コスト：解決策の予算
- レイテンシー：トークン応答の平均時間

## LLM ライフサイクル

まず、ライフサイクルとその変更点を理解するために、次のインフォグラフィックをご覧ください。

![LLMOps インフォグラフィック](../../../translated_images/ja/02-llmops.70a942ead05a7645.webp)

ご覧の通り、これは通常の MLOps ライフサイクルとは異なります。LLM は多くの新しい要件があり、プロンプト、品質向上のための様々な技術（ファインチューニング、RAG、メタプロンプト）、責任ある AI に関連する異なる評価と責任、最後に新しい評価指標（品質、有害性、正直さ、コスト、レイテンシー）があります。

たとえば、私たちがどのようにアイデアを出すか見てみましょう。プロンプトエンジニアリングを使って様々な LLM を試し、その仮説が正しいか探ります。

これは線形ではなく、統合されたループであり、反復的で包括的なサイクルであることに注意してください。

これらのステップをどのように探求できるか、ライフサイクルの構築方法を詳しく見てみましょう。

![LLMOps ワークフロー](../../../translated_images/ja/03-llm-stage-flows.3a1e1c401235a6cf.webp)

少し複雑に見えますが、まずは大きな3つのステップに注目しましょう。

1. アイデア出し/探索：ビジネスニーズに応じて探求します。プロトタイプ作成、[PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) の作成、仮説の検証に十分かテストします。
1. 構築/強化：実装。大規模データセット向けに評価を始め、ファインチューニングや RAG などの技術を実装してソリューションの堅牢性を確認します。うまくいかない場合は再実装、フローに新ステップ追加、データ構造の見直しが助けになります。フローとスケールをテストし、メトリクスを確認したら次のステップへ。
1. 運用化：統合。監視およびアラートシステムを追加し、システム展開とアプリケーション統合を行います。

その後、管理の全体的なサイクルがあり、セキュリティ、コンプライアンス、ガバナンスに注力します。

おめでとうございます。これで AI アプリが準備完了、運用可能です。実践体験として、[Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) をご覧ください。

では、どんなツールが使えるでしょうか？

## ライフサイクルツール

ツールとして、Microsoft は [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) と [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) を提供し、ライフサイクルを実装しやすくしています。

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) では、[Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) を利用できます。Microsoft Foundry（旧 Azure AI Studio）はモデル、サンプル、ツールの探索、リソース管理、UI開発フローの利用、SDK/CLI を使ったコード中心の開発を可能にするウェブポータルです。

![Azure AI の可能性](../../../translated_images/ja/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI は、運用、サービス、プロジェクト、ベクター検索、データベース管理など複数のリソースを活用できます。

![Azure AI と LLMOps](../../../translated_images/ja/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

PromptFlow を使い、概念実証(POC)から大規模アプリケーションを構築：

- VS Code からビジュアルかつ機能的なツールでアプリを設計・構築
- 品質の高い AI のためにアプリを簡単にテスト・ファインチューニング
- Microsoft Foundry を活用し、クラウド連携、プッシュ、展開で高速統合と反復が可能

![PromptFlow と LLMOps](../../../translated_images/ja/06-llm-promptflow.a183eba07a3a7fdf.webp)

## 素晴らしい！学習を続けましょう！

素晴らしいです。次は [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) を使ってアプリ構造を学び、Cloud Advocacy がデモでどのようにこれらの概念を取り入れているかを確認しましょう。さらに詳しくは [Ignite ブレイクアウトセッション！](https://www.youtube.com/watch?v=DdOylyrTOWg)


続いて、ジェネレーティブ AI に影響を与える [Retrieval Augmented Generation とベクターデータベース](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) について理解を深め、より魅力的なアプリケーション作成を目指しましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->