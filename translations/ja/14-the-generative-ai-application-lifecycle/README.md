[![関数呼び出しとの統合](../../../translated_images/14-lesson-banner.png?WT.833a8de2ff3806528caaf839db4385f00ff7c9f92ccdd38d886f4d662fc72f2a.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# 生成的AIアプリケーションのライフサイクル

AIアプリケーションにとって重要な質問は、AI機能の関連性です。AIは急速に進化する分野であり、アプリケーションが常に関連性を持ち、信頼性が高く、堅牢であることを保証するためには、継続的に監視、評価、改善する必要があります。ここで、生成的AIライフサイクルが役立ちます。

生成的AIライフサイクルは、生成的AIアプリケーションの開発、展開、維持の段階をガイドするフレームワークです。目標を定義し、パフォーマンスを測定し、課題を特定し、解決策を実施するのに役立ちます。また、アプリケーションをドメインやステークホルダーの倫理的および法的基準に合わせるのにも役立ちます。生成的AIライフサイクルに従うことで、アプリケーションが常に価値を提供し、ユーザーを満足させることができます。

## はじめに

この章では、以下を学びます：

- MLOpsからLLMOpsへのパラダイムシフトを理解する
- LLMライフサイクル
- ライフサイクルのツール
- ライフサイクルの測定と評価

## MLOpsからLLMOpsへのパラダイムシフトを理解する

LLMは人工知能の新しいツールであり、アプリケーションの分析と生成タスクにおいて非常に強力です。しかし、この力はAIと従来の機械学習タスクの効率化にいくつかの影響を及ぼします。

これにより、このツールを動的に適応させるための新しいパラダイムが必要です。過去のAIアプリを「MLアプリ」とし、最新のAIアプリを「GenAIアプリ」または単に「AIアプリ」と分類できます。これは、当時の主流技術と手法を反映しています。このようにして、私たちの物語は多くの方法で変わります。次の比較を見てください。

![LLMOpsとMLOpsの比較](../../../translated_images/01-llmops-shift.png?WT.38bc3eca81f659d83b17070d0a766bc3a9f13284b92c307e296915db4e683fcf.ja.mc_id=academic-105485-koreys)

LLMOpsでは、アプリ開発者により焦点を当て、統合を重要なポイントとして使用し、「モデル・アズ・ア・サービス」を使用し、次のポイントでメトリクスを考えます。

- 品質：応答の品質
- 有害性：責任あるAI
- 誠実性：応答の根拠（意味が通じるか？正しいか？）
- コスト：ソリューションの予算
- 遅延：トークン応答の平均時間

## LLMライフサイクル

まず、ライフサイクルとその変更を理解するために、次のインフォグラフィックを見てみましょう。

![LLMOpsインフォグラフィック](../../../translated_images/02-llmops.png?WT.32553adc9de4d89bb1d6a2f1f99d985457158a3be863e8e5dddc5e3dd074558a.ja.mc_id=academic-105485-koreys)

ご覧の通り、これは通常のMLOpsのライフサイクルとは異なります。LLMは、プロンプト、品質を向上させるためのさまざまな手法（ファインチューニング、RAG、メタプロンプト）、責任あるAIに関する評価と責任、最後に新しい評価指標（品質、有害性、誠実性、コスト、遅延）など、多くの新しい要件があります。

たとえば、どのようにアイデアを出すかを見てみましょう。プロンプトエンジニアリングを使用して、さまざまなLLMで実験し、仮説が正しいかどうかをテストする可能性を探ります。

これは線形ではなく、統合されたループであり、反復的で包括的なサイクルです。

これらのステップをどのように探求することができるでしょうか？ライフサイクルをどのように構築するかについて詳しく見てみましょう。

![LLMOpsワークフロー](../../../translated_images/03-llm-stage-flows.png?WT.118920c8fd638f0879fe06c5e6eb9d91536e8b9c6bc56808ebed8706812f5391.ja.mc_id=academic-105485-koreys)

少し複雑に見えるかもしれませんが、まず3つの大きなステップに焦点を当てましょう。

1. アイデア出し/探索: 探索では、ビジネスニーズに応じて探索を行います。プロトタイピング、[PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)を作成し、仮説に対して十分に効率的かどうかをテストします。
2. 構築/拡張: 実装では、より大きなデータセットを評価し、ファインチューニングやRAGなどの手法を実装して、ソリューションの堅牢性を確認します。うまくいかない場合は、フローに新しいステップを追加したり、データを再構築したりすることで改善するかもしれません。フローとスケールをテストし、メトリクスを確認したら、次のステップに進む準備が整います。
3. 運用化: 統合では、モニタリングとアラートシステムをシステムに追加し、アプリケーションへの統合を行います。

その後、セキュリティ、コンプライアンス、ガバナンスに焦点を当てた管理の包括的なサイクルがあります。

おめでとうございます。これでAIアプリが準備完了し、運用可能です。実践的な経験を得るには、[Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)をご覧ください。

さて、どのようなツールを使用できるでしょうか？

## ライフサイクルのツール

ツールとして、Microsoftは[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)と[PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)を提供しており、サイクルを簡単に実装し、すぐに使えるようにします。

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)を使用すると、[AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)を利用できます。AI Studioは、モデル、サンプル、ツールを探索できるWebポータルであり、リソースの管理、UI開発フロー、コードファースト開発のためのSDK/CLIオプションを提供します。

![Azure AIの可能性](../../../translated_images/04-azure-ai-platform.png?WT.a39053c2efd7670298a79282658a9f5bf903dec5c1938b1a08cf45f1284e6ac0.ja.mc_id=academic-105485-koreys)

Azure AIを使用すると、複数のリソースを使用して、オペレーション、サービス、プロジェクト、ベクトル検索、データベースのニーズを管理できます。

![Azure AIを使用したLLMOps](../../../translated_images/05-llm-azure-ai-prompt.png?WT.9189130ce4f2e7c8667fc7c83c6b89236ce5c6361150f47104c27c105f04b487.ja.mc_id=academic-105485-koreys)

PromptFlowを使用して、概念実証(POC)から大規模アプリケーションまで構築します：

- VS Codeからビジュアルおよび機能的なツールを使用してアプリを設計および構築
- 簡単に質の高いAIのためにアプリをテストおよび微調整
- Azure AI Studioを使用してクラウドと統合および反復し、迅速な統合のためにプッシュおよびデプロイ

![PromptFlowを使用したLLMOps](../../../translated_images/06-llm-promptflow.png?WT.e479dfedaa5f6ef7d36a11edbff74ac5579c3121ba0be0ee32eb5fc3eb17bd77.ja.mc_id=academic-105485-koreys)

## 素晴らしい！学習を続けましょう！

素晴らしいですね。アプリケーションをどのように構築し、[Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)を使用して概念を活用する方法を学び、クラウドアドボカシーがこれらの概念をデモにどのように追加しているかを確認してください。詳細なコンテンツについては、[Igniteのブレークアウトセッション](https://www.youtube.com/watch?v=DdOylyrTOWg)をチェックしてください。

次に、Lesson 15を確認し、[Retrieval Augmented Generation and Vector Databases](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst)が生成的AIにどのように影響し、より魅力的なアプリケーションを作成するかを理解しましょう！

**免責事項**:  
この文書は、機械翻訳サービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。元の言語の文書が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当社は責任を負いません。