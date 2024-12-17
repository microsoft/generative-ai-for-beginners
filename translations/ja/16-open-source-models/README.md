[![Open Source Models](../../../translated_images/16-lesson-banner.png?WT.a9a13a59f0350adb5846e88fb3aba98cd4c6cb3297e78cb7100938f45b7dac47.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## はじめに

オープンソースLLMの世界は刺激的で絶えず進化しています。このレッスンでは、オープンソースモデルについて詳しく見ていきます。独自モデルとオープンソースモデルの比較に関する情報をお探しの場合は、「[異なるLLMの探索と比較](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)」のレッスンをご覧ください。このレッスンでは、微調整のトピックも取り上げますが、より詳細な説明は「[LLMの微調整](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst)」のレッスンで確認できます。

## 学習目標

- オープンソースモデルの理解を深める
- オープンソースモデルを使うことの利点を理解する
- Hugging FaceやAzure AI Studioで利用可能なオープンモデルを探索する

## オープンソースモデルとは？

オープンソースソフトウェアは、さまざまな分野での技術の成長において重要な役割を果たしてきました。オープンソースイニシアティブ（OSI）は、ソフトウェアをオープンソースとして分類するための[10の基準](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)を定義しています。ソースコードは、OSIが承認したライセンスの下でオープンに共有される必要があります。

LLMの開発はソフトウェアの開発と似た要素を持っていますが、プロセスはまったく同じではありません。これにより、LLMの文脈でのオープンソースの定義について、コミュニティ内で多くの議論が生まれました。モデルが伝統的なオープンソースの定義に沿うためには、以下の情報が公開されている必要があります：

- モデルのトレーニングに使用されたデータセット。
- トレーニングの一部としての完全なモデルの重み。
- 評価コード。
- 微調整コード。
- 完全なモデルの重みとトレーニングメトリクス。

現在、この基準を満たすモデルはごくわずかです。 [Allen Institute for Artificial Intelligence (AllenAI) によって作成されたOLMoモデル](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst)は、このカテゴリーに該当します。

このレッスンでは、上記の基準を満たしていない可能性があるため、今後「オープンモデル」と呼ぶことにします。

## オープンモデルの利点

**高いカスタマイズ性** - オープンモデルは詳細なトレーニング情報と共にリリースされるため、研究者や開発者はモデルの内部を変更できます。これにより、特定のタスクや研究分野に特化したモデルを微調整して作成することが可能になります。例としては、コード生成、数学的操作、生物学などがあります。

**コスト** - これらのモデルを使用およびデプロイする際のトークンあたりのコストは、独自モデルよりも低くなります。生成AIアプリケーションを構築する際には、これらのモデルを使用する際のパフォーマンスと価格のバランスを検討する必要があります。

![Model Cost](../../../translated_images/model-price.png?WT.473bad4fe5bdb7014798275047130c0949da1e4a3d6f379037bedf68ef1d5e42.ja.mc_id=academic-105485-koreyst)
出典: Artificial Analysis

**柔軟性** - オープンモデルを使用することで、異なるモデルを使用したり、組み合わせたりする柔軟性が得られます。例えば、[HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)では、ユーザーがユーザーインターフェースで使用するモデルを直接選択できます：

![Choose Model](../../../translated_images/choose-model.png?WT.50da8a7caba083003bcf9f71017d17715f032acff67359c11c9886597ca3efdc.ja.mc_id=academic-105485-koreyst)

## 異なるオープンモデルの探索

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst)は、Metaによって開発されたチャットベースのアプリケーションに最適化されたオープンモデルです。これは、大量の対話と人間のフィードバックを含む微調整方法によるものです。この方法により、モデルは人間の期待に合った結果をより多く生成し、より良いユーザー体験を提供します。

Llamaの微調整版の例としては、日本語に特化した[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)や、ベースモデルの強化版である[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)があります。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)は、高性能と効率性に重点を置いたオープンモデルです。Mixture-of-Expertsアプローチを使用しており、特定の入力に応じて選択される専門家モデルのグループを1つのシステムに組み合わせています。これにより、計算がより効果的になり、モデルは専門としている入力のみを処理します。

Mistralの微調整版の例としては、医療分野に焦点を当てた[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)や、数学的計算を行う[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)があります。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst)は、技術革新研究所（**TII**）によって作成されたLLMです。Falcon-40Bは400億のパラメータでトレーニングされており、より少ない計算予算でGPT-3よりも優れた性能を示しています。これは、FlashAttentionアルゴリズムとマルチクエリ注意を使用して、推論時のメモリ要件を削減できるためです。この推論時間の短縮により、Falcon-40Bはチャットアプリケーションに適しています。

Falconの微調整版の例としては、オープンモデルに基づいて構築されたアシスタントである[OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)や、ベースモデルよりも高性能を発揮する[GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)があります。

## 選び方

オープンモデルを選ぶための唯一の答えはありません。良い出発点は、Azure AI Studioのタスク別フィルタ機能を使用することです。これにより、モデルがどのようなタスクに対してトレーニングされているかを理解することができます。Hugging Faceも、特定のメトリクスに基づいて最高のパフォーマンスを示すモデルを表示するLLMリーダーボードを維持しています。

異なるタイプのLLMを比較する際には、[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst)も優れたリソースです：

![Model Quality](../../../translated_images/model-quality.png?WT.bffdb0b01a3f3205153df83585941f90a153017f607dbcfad9cde5369764f203.ja.mc_id=academic-105485-koreyst)
出典: Artificial Analysis

特定のユースケースに取り組む場合、同じ分野に焦点を当てた微調整版を検索することが効果的です。複数のオープンモデルを試して、あなたやユーザーの期待にどのように応えるかを確認することも良い実践です。

## 次のステップ

オープンモデルの最も良い点は、すぐに作業を開始できることです。[Azure AI Studioモデルカタログ](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)をチェックして、ここで紹介したモデルを含む特定のHugging Faceコレクションを見てみましょう。

## 学習はここで終わりません、旅を続けましょう

このレッスンを完了した後は、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めましょう！

**免責事項**:  
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文の言語で書かれたオリジナルの文書を権威ある情報源とみなしてください。重要な情報については、プロの人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。