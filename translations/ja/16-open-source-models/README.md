<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T13:41:54+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "ja"
}
-->
[![Open Source Models](../../../translated_images/ja/16-lesson-banner.6b56555e8404fda1.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## はじめに

オープンソースのLLMの世界は刺激的で常に進化しています。このレッスンではオープンソースモデルについて詳しく解説します。プロプライエタリモデルとオープンソースモデルの比較に関する情報をお探しの場合は、[「さまざまなLLMの探索と比較」レッスン](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)をご覧ください。このレッスンではファインチューニングのトピックも扱いますが、より詳細な説明は[「LLMのファインチューニング」レッスン](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst)にあります。

## 学習目標

- オープンソースモデルの理解を深める
- オープンソースモデルを使う利点を理解する
- Hugging FaceやAzure AI Studioで利用可能なオープンモデルを探る

## オープンソースモデルとは？

オープンソースソフトウェアはさまざまな分野で技術の成長に重要な役割を果たしてきました。Open Source Initiative（OSI）は、ソフトウェアがオープンソースと分類されるための[10の基準](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)を定めています。ソースコードはOSI承認のライセンスの下で公開されなければなりません。

LLMの開発はソフトウェア開発と似た要素を持ちますが、プロセスは完全に同じではありません。このため、LLMの文脈でのオープンソースの定義についてコミュニティ内で多くの議論がなされています。伝統的なオープンソースの定義に沿うモデルであるためには、以下の情報が公開されている必要があります：

- モデルのトレーニングに使用されたデータセット
- トレーニングの一部としての完全なモデル重み
- 評価コード
- ファインチューニングコード
- 完全なモデル重みとトレーニングメトリクス

現在、この基準を満たすモデルはごくわずかです。[Allen Institute for Artificial Intelligence (AllenAI) が作成したOLMoモデル](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst)はこのカテゴリに該当します。

本レッスンでは、執筆時点で上記の基準に完全に合致しない可能性があるため、今後「オープンモデル」と呼びます。

## オープンモデルの利点

**高度なカスタマイズ性** - オープンモデルは詳細なトレーニング情報と共に公開されているため、研究者や開発者はモデルの内部を修正できます。これにより、特定のタスクや研究分野に特化した高度に専門化されたモデルを作成できます。例としてはコード生成、数学的演算、生物学などがあります。

**コスト** - これらのモデルの使用および展開にかかるトークンあたりのコストは、プロプライエタリモデルよりも低くなっています。生成AIアプリケーションを構築する際には、これらのモデルを使った場合のパフォーマンスと価格のバランスを検討することが重要です。

![Model Cost](../../../translated_images/ja/model-price.3f5a3e4d32ae00b4.png)
出典: Artificial Analysis

**柔軟性** - オープンモデルを使うことで、異なるモデルを使い分けたり組み合わせたりする柔軟性が得られます。例として、[HuggingChatアシスタント](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)では、ユーザーがUI上で直接使用するモデルを選択できます：

![Choose Model](../../../translated_images/ja/choose-model.f095d15bbac92214.png)

## さまざまなオープンモデルの紹介

### Llama 2

[Metaが開発したLlama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst)はチャットベースのアプリケーションに最適化されたオープンモデルです。これは大量の対話データと人間のフィードバックを用いたファインチューニング手法によるもので、この方法によりモデルは人間の期待により沿った結果を出し、より良いユーザー体験を提供します。

Llamaのファインチューニング版の例としては、日本語に特化した[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)や、ベースモデルを強化した[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)があります。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)は高性能と効率性に重点を置いたオープンモデルです。Mixture-of-Expertsアプローチを採用しており、専門化された複数のエキスパートモデルを組み合わせ、入力に応じて特定のモデルを選択して使用します。これにより、モデルは専門分野の入力のみを処理するため計算効率が向上します。

Mistralのファインチューニング版の例には、医療分野に特化した[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)や、数学計算を行う[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)があります。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst)はTechnology Innovation Institute（**TII**）によって作成されたLLMです。Falcon-40Bは400億パラメータでトレーニングされており、GPT-3よりも少ない計算リソースで優れた性能を示しています。これはFlashAttentionアルゴリズムとマルチクエリアテンションの使用により、推論時のメモリ要件を削減できるためです。この推論時間の短縮により、Falcon-40Bはチャットアプリケーションに適しています。

Falconのファインチューニング版の例には、オープンモデルを基にしたアシスタントである[OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)や、ベースモデルより高性能な[GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)があります。

## モデルの選び方

オープンモデルの選択に正解はありません。まずはAzure AI Studioのタスク別フィルター機能を使うのが良い出発点です。これによりモデルがどのようなタスクにトレーニングされているかを理解できます。Hugging Faceも特定の指標に基づくLLMリーダーボードを維持しています。

異なるタイプのLLMを比較したい場合は、[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst)も優れたリソースです：

![Model Quality](../../../translated_images/ja/model-quality.aaae1c22e00f7ee1.png)
出典: Artificial Analysis

特定のユースケースに取り組む場合は、同じ分野に特化したファインチューニング版を探すのが効果的です。複数のオープンモデルを試して、自分やユーザーの期待にどのように応えるかを評価するのも良い方法です。

## 次のステップ

オープンモデルの最大の利点は、すぐに使い始められることです。ここで紹介したモデルを含むHugging Faceコレクションを特徴とする[Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)をぜひご覧ください。

## 学びはここで終わらない、旅を続けよう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)で生成AIの知識をさらに深めていきましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->