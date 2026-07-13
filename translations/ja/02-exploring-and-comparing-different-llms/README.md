# さまざまなLLMの探索と比較

[![さまざまなLLMの探索と比較](../../../translated_images/ja/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _ビデオを見るには上の画像をクリックしてください_

前のレッスンで、生成AIがどのように技術の風景を変えているか、Large Language Models (LLM) がどのように機能し、私たちのようなスタートアップがそれらをユースケースに適用して成長できるかを見てきました。この章では、さまざまな種類の大規模言語モデル（LLM）を比較し、その長所と短所を理解します。

次のステップは、スタートアップの旅の中で現在のLLMの状況を探り、どれが私たちのユースケースに適しているかを理解することです。

## はじめに

このレッスンでは以下を扱います：

- 現在の状況におけるさまざまなタイプのLLM。
- Azureでのユースケース向けのさまざまなモデルのテスト、反復、比較。
- LLMのデプロイ方法。

## 学習目標

このレッスンを完了すると、以下ができるようになります：

- ユースケースに適したモデルを選択する。
- モデルの性能をテスト、反復、改善する方法を理解する。
- ビジネスがモデルをどのようにデプロイするかを知る。

## さまざまな種類のLLMを理解する

LLMは、アーキテクチャ、トレーニングデータ、ユースケースに基づいて複数の分類があります。これらの違いを理解することで、スタートアップがシナリオに適したモデルを選択し、テスト、反復、性能向上の方法を理解できます。

多くの種類のLLMモデルが存在し、モデルの選択は用途、データ、支払える費用などに依存します。

テキスト、音声、ビデオ、画像生成など、何に使うかによってもモデルを選択します。

- <strong>音声認識</strong>。Whisperスタイルのモデルはまだ汎用の音声認識モデルとして有用ですが、プロダクションでは`gpt-4o-transcribe`、`gpt-4o-mini-transcribe`、およびダイアリゼーション変種などの新しい音声テキスト変換モデルも使われます。言語対応範囲、ダイアリゼーション、リアルタイム対応、遅延、コストをユースケースに合わせて評価してください。詳細は[OpenAI音声テキスト変換ドキュメント](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst)をご覧ください。

- <strong>画像生成</strong>。DALL-EやMidjourneyはよく知られた画像生成オプションですが、現在のOpenAI画像APIは`gpt-image-2`のようなGPT画像モデルを中心としており、Stable Diffusion、Imagen、Flux、そのほかのモデルファミリーもよく使われます。プロンプト遵守率、編集サポート、スタイル制御、安全性要件、ライセンスを比較してください。詳細は[OpenAI画像生成ガイド](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst)および本カリキュラムの第9章を参照してください。

- <strong>テキスト生成</strong>。テキストモデルには最先端モデル、推論モデル、小型で低遅延のモデル、オープンウェイトのモデルがあります。現在の例としてOpenAI GPT-5.xモデル、Anthropic Claude 4.xモデル、Google Gemini 3.xモデル、Meta Llama 4モデル、Mistralモデルがあります。リリース日や価格だけで選ばず、タスク品質、遅延、コンテキストウィンドウ、ツール利用、安全性挙動、地域利用可能性、総コストを比較してください。[Microsoft Foundry model catalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst)はAzureで利用可能なモデル比較に役立ちます。

- <strong>マルチモーダル</strong>。現在の多くのモデルはテキスト以外も処理可能です。画像、音声、ビデオ入力を受け付けるもの、ツール呼び出し可能なもの、画像音声ビデオ生成に特化したものがあります。例えばOpenAIの現行モデルはテキストと画像入力をサポートし、Geminiモデルはバリアントによりテキスト・コード・画像・音声・ビデオ入力をサポートし、Llama 4 ScoutやMaverickはオープンウェイトでネイティブなマルチモーダルモデルです。ワークフロー構築前には必ず各モデルカードで入出力モダリティを確認してください。

モデル選択は基本的な能力を得ることを意味しますが、それだけでは不十分なこともあります。しばしば企業固有のデータをLLMに与える必要があります。アプローチはいくつかあり、それについては今後のセクションで説明します。

### ファウンデーションモデルとLLMの違い

ファウンデーションモデルは[スタンフォードの研究者が造語し](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)、以下のような特徴を持つAIモデルとして定義されます：

- <strong>教師なし学習または自己教師あり学習で訓練される</strong>ため、ラベルなしのマルチモーダルデータを使い、トレーニングに人間の注釈は必要としません。
- <strong>非常に大規模なモデル</strong>であり、数十億パラメーターの非常に深いニューラルネットワークを用います。
- <strong>通常は「基礎」として他モデルの土台となることを意図している</strong>ため、ファインチューニングによって他のモデルのベースとして使えます。

![ファウンデーションモデルとLLMの違い](../../../translated_images/ja/FoundationModel.e4859dbb7a825c94.webp)

画像出典：[Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

これをさらに明確にするために、ChatGPTを歴史的な例として見てみましょう。初期のChatGPTはGPT-3.5をファウンデーションモデルとして使い、OpenAIはチャット特化データとアライメント技術で調整し、チャットボットのような会話シナリオで優れた性能を持つ調整済みモデルを作りました。現在のAIサービスは通常いくつかのモデルバリアントを使い分けているため、サービス名とモデル名は必ずしも一致しません。

![ファウンデーションモデル](../../../translated_images/ja/Multimodal.2c389c6439e0fc51.webp)

画像出典：[2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### オープンウェイト/オープンソースと独自モデルの違い

LLMのもう一つの分類方法は、オープンウェイト、オープンソース、独自かどうかです。

オープンソースおよびオープンウェイトモデルはモデルアーティファクトを検査、ダウンロード、カスタマイズ可能にしますが、ライセンス形態は異なります。完全にオープンソースの場合もあれば、使用制限のあるオープンウェイトモデルもあります。企業が展開制御、データの所在、コスト、カスタマイズを重視する際に有用です。ただし本番利用にはライセンス条件、サービス費用、メンテナンス、安全性アップデート、評価品質を確認する必要があります。例には[Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst)、一部の[Mistralモデル](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst)、[Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst)上の多くのモデルがあります。

独自モデルはプロバイダーが所有しホストしています。これらは管理された本番利用向けに最適化されており、強力なサポート、安全システム、ツール統合、スケールを提供可能です。ただし通常、顧客はモデルの重みを検査・修正できません。プライバシー、保持、コンプライアンス、許容使用に関してはプロバイダーの規約を確認する必要があります。例には[OpenAIモデル](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)、[Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst)、[Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst)があります。

### 埋め込み、画像生成、テキストおよびコード生成の違い

LLMは出力の種類によっても分類できます。

埋め込みは、テキストを数値形式（埋め込み）に変換するモデル群です。埋め込みは入力テキストの数値的な表現であり、単語や文の関係性を機械が理解しやすくし、分類やクラスタリングなど数値データで性能が良い他モデルの入力として使えます。埋め込みモデルは転移学習にも使われ、豊富なデータがある別タスク向けにモデルを訓練後、その重み（埋め込み）を他の下流タスクに再利用します。例として[OpenAIの埋め込み](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)があります。

![埋め込み](../../../translated_images/ja/Embedding.c3708fe988ccf760.webp)

画像生成モデルは画像を生成するモデルです。これらは画像編集、合成、変換に使われます。一般的に[LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)などの大規模画像データセットで訓練されており、新規画像生成や、修復、超解像、着色技術による既存画像編集が可能です。例として[GPT画像モデル](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst)、[Stable Diffusionモデル](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst)、Imagenモデルがあります。

![画像生成](../../../translated_images/ja/Image.349c080266a763fd.webp)

テキストおよびコード生成モデルはテキストやコードを生成します。テキスト生成モデルは要約、翻訳、質問応答に使われます。多くの場合[BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst)のような大容量テキストデータセットで訓練されており、新規テキスト生成や質問応答に使われます。コード生成モデルは[CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)のようにGitHubなどの大規模コードデータセットで訓練され、新コード生成や既存のコードのバグ修正に使われます。

![テキストおよびコード生成](../../../translated_images/ja/Text.a8c0cf139e5cc2a0.webp)

### エンコーダ-デコーダとデコーダのみ

LLMのアーキテクチャの違いを話すために、例え話をしましょう。

あなたの上司が学生向けクイズを書くタスクを出しました。2人の同僚がいます。1人はコンテンツ作成を担当し、もう1人はレビュー担当です。

コンテンツ作成者はデコーダーのみモデルのようなもので、トピックを見て、既に書かれた内容を見て、その文脈に基づきコンテンツ生成を続けます。魅力的で情報豊かな文章生成に優れていますが、分類や検索、情報のエンコードには必ずしも最適とは限りません。デコーダーのみモデルの例にはGPTやLlamaモデルがあります。

レビュー担当はエンコーダーのみモデルのようで、コースや回答を見てそれらの関係性や文脈を把握しますが、コンテンツ生成は得意ではありません。エンコーダーのみモデルの例はBERTです。

作成とレビューの両方をできる人がいると想像してください。これがエンコーダー-デコーダーモデルです。例にはBARTやT5があります。

### サービスとモデルの違い

サービスはクラウドサービスプロバイダーが提供する製品で、モデル、データ、その他のコンポーネントの組み合わせです。モデルはサービスの中核であり、通常はファウンデーションモデルなどのLLMです。

サービスは本番利用向けに最適化されており、多くの場合GUIで使いやすいです。ただし無料でないことが多く、サブスクリプションや従量課金が必要で、サービス所有者の設備・資源を利用し費用を最適化しスケールを容易にします。例として [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst) があり、従量課金制で利用量に応じて料金がかかります。Azure OpenAI Serviceはエンタープライズ向けのセキュリティと責任あるAIフレームワークをモデル機能の上に提供します。

モデルはニューラルネットワークのアーティファクト、パラメーター、重み、アーキテクチャ、トークナイザー、構成を指します。ローカルまたはプライベート環境でモデルを動かすには適切なハードウェア、サービング基盤、モニタリング、および互換性のあるオープンソースまたはオープンウェイトライセンスか商用ライセンスが必要です。Llama 4やMistralなどのオープンウェイトモデルはセルフホスト可能ですが、計算資源と運用の専門知識が必要です。

## Azureでの異なるモデルのテストと反復による性能理解方法


チームが現在のLLMの状況を調査し、シナリオに適した候補モデルを特定したら、次のステップはそれらを実際のデータとワークロードでテストすることです。これは実験と測定を繰り返す反復プロセスです。
前節で述べたほとんどのモデル（OpenAIモデル、Llama 4やMistralのようなオープンウェイトモデル、およびHugging Faceモデル）は、[Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst)で利用可能です。

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst)（旧称Azure AI Studio/Azure AI Foundry）は、AIアプリケーションやエージェントを構築するための統一されたAzureプラットフォームです。実験・評価から展開、監視、ガバナンスまでのライフサイクル管理を支援します。Microsoft Foundryのモデルカタログでは、ユーザーは以下のことができます：

- Azureやパートナー、コミュニティ提供者によるモデルを含む、興味のあるファウンデーションモデルをカタログで検索できます。タスク、提供者、ライセンス、展開オプション、名前でフィルター可能です。

![Model catalog](../../../translated_images/ja/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- 意図された使用法やトレーニングデータの詳細説明、コードサンプル、内部評価ライブラリによる評価結果を含むモデルカードをレビューできます。

![Model card](../../../translated_images/ja/ModelCard.598051692c6e400d.webp)

- [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst)ペインを通じて、業界で利用可能なモデルやデータセットのベンチマークを比較し、ビジネスシナリオに最適なものを評価できます。

![Model benchmarks](../../../translated_images/ja/ModelBenchmarks.254cb20fbd06c03a.webp)

- 対応するモデルをカスタムトレーニングデータでファインチューニングし、Microsoft Foundryの実験・追跡機能を活用して特定のワークロードでのパフォーマンスを向上させます。

![Model fine-tuning](../../../translated_images/ja/FineTuning.aac48f07142e36fd.webp)

- 元の事前学習済みモデルまたはファインチューニング済みモデルをマネージドコンピューティングやサーバーレス展開オプションを使ってリモートリアルタイム推論エンドポイントにデプロイし、アプリケーションで利用可能にします。

![Model deployment](../../../translated_images/ja/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> カタログ内のすべてのモデルが現在ファインチューニングおよび/または従量課金型展開に対応しているわけではありません。モデルカードでモデルの能力と制限の詳細を確認してください。

## LLMの成果を向上させる

スタートアップチームで様々な種類のLLMと、異なるモデルを比較・評価しパフォーマンスを向上させ、推論エンドポイントに展開できるクラウドプラットフォーム（Microsoft Foundry）を探ってきました。

では、事前学習済みモデルの使用ではなく、いつファインチューニングを検討すべきでしょうか？特定のワークロードでモデル性能を改善する他の方法はあるでしょうか？

ビジネスがLLMから必要な結果を得るためには、いくつかのアプローチがあります。運用環境にLLMを展開する際、異なる訓練度のモデルを選択できます。複雑さ、コスト、品質に応じたさまざまな方法を紹介します：

- <strong>コンテキストを用いたプロンプトエンジニアリング</strong>。要求に必要な回答を得るために十分なコンテキストをプロンプトで提供する方法です。

- **Retrieval Augmented Generation (RAG)**。データベースやWebエンドポイントに存在するデータを、プロンプトの際に含めるために、関連データを取得してユーザーのプロンプトの一部とする方法です。

- <strong>ファインチューニング済みモデル</strong>。自社データでモデルをさらに訓練することで、ニーズにより正確に応答するようにしますが、コストがかかる場合があります。

![LLMs deployment](../../../translated_images/ja/Deploy.18b2d27412ec8c02.webp)

画像出典：[Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### コンテキストを用いたプロンプトエンジニアリング

事前学習済みLLMは、短いプロンプト（完成文や質問など）を使った「ゼロショット」学習でも汎用的な自然言語タスクに非常によく対応します。

しかし、ユーザーが詳細な要求や例（コンテキスト）を使ってクエリをフレーミングできれば、それだけ回答の精度やユーザー期待に近い結果となります。例が1つなら「ワンショット」学習、複数なら「数ショット」学習と言います。
コンテキストを用いたプロンプトエンジニアリングは、最もコスト効果の高い開始方法です。

### Retrieval Augmented Generation (RAG)

LLMは訓練に用いたデータのみで回答を生成できるという制限があります。訓練後の事実や非公開情報（企業データなど）には対応できません。
これは、文書のチャンクとして外部データをプロンプトへ補強し、プロンプト長制限を考慮しつつ記憶を拡張するRAGで克服できます。これには、[Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)のようなベクトルデータベースツールが、定義済みの様々なデータソースから有用なチャンクを検索してプロンプトコンテキストに追加することをサポートします。

十分なデータや時間、リソースがなくファインチューニングできない場合でも、特定のワークロードでのパフォーマンス向上や、幻覚・旧式や非対応回答のリスク軽減に役立つ手法です。

### ファインチューニング済みモデル

ファインチューニングは、転移学習を活用してモデルを下流タスクや特定の問題に「適応」させるプロセスです。数ショット学習やRAGとは異なり、新しいモデルが生成され、重みとバイアスが更新されます。単一の入力（プロンプト）とそれに対応する出力（補完）からなる訓練例セットが必要です。
以下の場合に推奨されます：

- <strong>小さなタスク特化モデルの利用</strong>。大規模な先端モデルを繰り返しプロンプトする代わりに、小型モデルをファインチューニングし、よりコスト効果が高く高速なソリューションとします。

- <strong>遅延の考慮</strong>。特定のユースケースで待機時間が重要で、非常に長いプロンプトの使用や学習すべき例の数がプロンプト長制限に合わない場合。

- <strong>安定した動作の適応</strong>。多数の高品質な例があり、モデルにタスクパターン、出力フォーマット、トーン、ドメイン固有スタイルを一貫して従わせたい場合。頻繁に変わる新事実やプライベート知識が問題の場合は、ファインチューニング単独ではなくRAGを用います。

### 訓練済みモデル

LLMをゼロからトレーニングするのは間違いなく最も難しく複雑な方法であり、大量のデータ、高度なスキルを持つリソース、適切な計算能力が必要です。この選択肢は、ビジネスがドメイン特化のユースケースと大量のドメイン中心データを有する場合に限って検討すべきです。

## 知識チェック

LLMの補完結果を改善するための良いアプローチは何でしょうか？

1. コンテキストを用いたプロンプトエンジニアリング
1. RAG
1. ファインチューニング済みモデル

A: いずれも効果的です。迅速な改善のためにはコンテキストを用いたプロンプトエンジニアリングから始め、モデルに最新の事実やプライベートビジネスデータが必要な場合はRAGを利用します。十分な高品質例があり、タスク・フォーマット・トーン・ドメインパターンにモデルを一貫従属させたい時はファインチューニングを選びます。

## 🚀 チャレンジ

ご自身のビジネスで[いかにRAGを活用できるか](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)について更に読み進めてみてください。

## 素晴らしい！学習を続けましょう

このレッスンを修了したら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識レベルアップを続けましょう！

続けてレッスン3では、[責任ある生成AIの活用方法](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)を学びます！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->