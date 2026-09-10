# 自習学習のためのリソース

このレッスンは、用語やチュートリアルの参照として OpenAI と Microsoft Foundry の主要なリソースを使用して作成されました。以下は、ご自身の自習学習に役立つ非網羅的なリストです。以下のすべてのリンクは、現在サポートされている資料にリンクしています。

## 1. 主要なリソース

| タイトル/リンク | 説明 |
| :--- | :--- |
| [Fine-tuning with OpenAI Models](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | ファインチューニングは、プロンプトに収まる数よりもはるかに多くの例でトレーニングすることで、少数ショット学習を改善し、コスト削減、応答品質の向上、低レイテンシー要求を可能にします。**OpenAI のファインチューニング概要を確認してください。** |
| [When to use Microsoft Foundry fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | ファインチューニングとは何か（概念）、なぜ検討すべきか、どのデータを使用するか、品質の測定方法を理解し、SFT、DPO、RFT のいずれが適切かを学びます。 |
| [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry におけるポータル、OpenAI / Foundry Python SDK、REST API を使用したファインチューニングのエンドツーエンドの<strong>手順（プロセス）</strong>。データ準備、トレーニング、チェックポイント、デプロイを含みます。 |
| [Continuous fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | すでにファインチューニングされたモデルをベースモデルとして選択し、新しいトレーニング例のセットで<strong>さらにファインチューニング</strong>を繰り返すプロセス。 |
| [Fine-tuning with tool (function) calling](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | ツール呼び出しの例を用いたファインチューニングにより、より正確で一貫性があり、同様のフォーマットの応答を、より少ないプロンプトトークンで実現して出力を改善します。 |
| [Fine-tuning models: Microsoft Foundry guidance](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | ファインチューニング可能なモデル、対応する手法（SFT / DPO / RFT）、利用可能なリージョンを確認できます。 |
| [Fine-tuning overview: techniques and modalities](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | 3つのトレーニング手法（SFT、DPO、RFT）と、2つのモダリティ（サーバーレス対マネージドコンピューティング）を比較し、ベースモデルの選び方や開始方法のガイダンスを提供します。 |
| **Tutorial**: [Fine-tune a model in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | サンプルデータセットの作成、ファインチューニングの準備、`gpt-4.1-mini`などの現在サポートされているモデルでファインチューニングジョブを実行し、Azure にファインチューニング済みモデルをデプロイします。 |
| **Tutorial**: [Fine-tune models with serverless API deployments](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry のローコード、UIベースのワークフローを使用して、Phi、Llama、Mistral などのオープン及びパートナーモデルをデータセットに合わせてカスタマイズします。 |
| **Tutorial**: [Fine-tune Hugging Face models on Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks と Hugging Face Trainer を使用して、単一GPU上で `transformers` ライブラリのHugging Faceモデルをファインチューニングします。 |
| **Training**: [Fine-tune a foundation model with Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning モデルカタログには多くのオープンソースモデルがあり、これらをファインチューニングできます。[Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst)の一部です。 |
| **Tutorial**: [Azure OpenAI fine-tuning with Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | W&B を使って Azure 上のファインチューニング実行を追跡・分析します。OpenAIのファインチューニングガイドに Azure 固有のステップと実験追跡を追加した内容です。 |

## 2. 二次的なリソース

このセクションでは、レッスンでカバーできなかった追加で探索する価値のあるリソースを紹介しています。このトピックに関するご自身の専門知識を深めるために活用してください。

| タイトル/リンク | 説明 |
| :--- | :--- |
| **OpenAI Cookbook**: [チャットモデル用ファインチューニングのためのデータ準備と解析](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | ファインチューニング前にチャットデータセットを前処理・解析します：フォーマットエラーのチェック、基本統計の取得、トークン数（と費用）推定。[OpenAIファインチューニングガイド](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)と併用推奨。 |
| **OpenAI Cookbook**: [Qdrant を用いた検索強化生成（RAG）のファインチューニング](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | OpenAIモデルをRAG向けにファインチューニングする包括的な例。Qdrant と少数ショット学習を統合し、性能向上と誤情報の削減を図ります。 |
| **OpenAI Cookbook**: [Weights & Biases を使った GPT ファインチューニング](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | W&B を利用してモデルのトレーニングとファインチューニングを追跡します。まず[OpenAI ファインチューニング](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst)ガイドを読んでからCookbookの演習に挑戦しましょう。 |
| **Hugging Face チュートリアル**: [Hugging Face TRLを使ったLLMのファインチューニング](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL、Transformers、datasetsを用いてオープンLLMをファインチューニング：ユースケース定義、開発環境設定、データセット準備、ファインチューニング、評価、デプロイ。 |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | 多くのモデルタイプをファインチューニングできる Hugging Face のノーコード/ローコードライブラリ。自身のクラウド、Hugging Face Spaces、またはローカルでGUI、CLI、YAML設定を使って実行可能。 |
| **Unsloth**: [LLMファインチューニングガイド](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | ローカルLLMファインチューニングと強化学習を簡素化するオープンソースフレームワーク。使いやすい[ノートブック](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)付き。 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->