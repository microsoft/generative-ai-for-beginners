# 初心者のための生成AIにおける小型言語モデル入門
生成AIは、新しいコンテンツを生成できるシステムの構築に焦点を当てた人工知能の魅力的な分野です。このコンテンツは、テキストや画像から音楽、さらには仮想環境全体にまで及びます。生成AIの最もエキサイティングな応用の一つは、言語モデルの領域にあります。

## 小型言語モデルとは何か？

小型言語モデル（SLM）は、大型言語モデル（LLM）の縮小版であり、LLMの多くの構造原理や技術を活用しながら、計算負荷を大幅に軽減しています。

SLMは、人間のようなテキストを生成することを目的とした言語モデルのサブセットです。GPT-4などの大型モデルとは異なり、SLMはよりコンパクトで効率的であり、計算資源が限られた環境に最適です。サイズは小さいものの、多様なタスクをこなせます。通常、SLMはLLMを圧縮または蒸留することによって構築され、元のモデルの機能や言語能力の多くを保持することを目指しています。このモデルサイズの縮小により、メモリ使用と計算要求の両面で効率性が向上しています。これらの最適化にもかかわらず、SLMは以下の幅広い自然言語処理（NLP）タスクを実行できます：

- テキスト生成：一貫性のある文や段落を文脈に沿って作成する。
- テキスト補完：与えられたプロンプトに基づき文を予測し補完する。
- 翻訳：ある言語のテキストを別の言語に変換する。
- 要約：長文を短く分かりやすい要約にまとめる。

ただし、大型モデルと比べると性能や理解の深さにはいくつかのトレードオフがあります。 

## 小型言語モデルはどのように機能するのか？
SLMは大量のテキストデータで訓練されます。訓練中に言語のパターンや構造を学習し、文法的に正しく文脈的にも適切なテキストを生成できるようになります。訓練プロセスは以下を含みます：

- データ収集：さまざまなソースから大規模なテキストデータセットを集める。
- 前処理：データを整理し訓練に適した形にする。
- 訓練：機械学習アルゴリズムを用いてテキストの理解と生成を学習させる。
- 微調整：特定のタスクでの性能を向上させるためにモデルを調整する。

SLMの開発は、モバイル端末やエッジコンピューティングプラットフォームのようなリソース制約のある環境での展開ニーズの高まりに応えています。フルスケールのLLMはこれらの環境では実用的でない場合が多いため、効率性に焦点を当てることで、SLMは性能とアクセスしやすさのバランスを取り、さまざまな分野での広範な応用を可能にしています。

![slm](../../../translated_images/ja/slm.4058842744d0444a.webp)

## 学習目標

このレッスンでは、SLMの知識を紹介し、Microsoft Phi-3と組み合わせてテキストコンテンツ、ビジョン、MoEの異なるシナリオを学びます。

レッスンの終了時には、以下の質問に答えられるようになることを目指します：

- SLMとは何か？
- SLMとLLMの違いは何か？
- Microsoft Phi-3 / 3.5ファミリーとは何か？
- Microsoft Phi-3 / 3.5ファミリーでの推論の実行方法は？

準備はいいですか？さっそく始めましょう。

## 大型言語モデル（LLM）と小型言語モデル（SLM）の違い

LLMとSLMはどちらも確率的機械学習の基本原理に基づいて構築されており、アーキテクチャ設計、訓練方法論、データ生成プロセス、モデル評価技術において類似のアプローチを取ります。しかし、いくつかの重要な要素がこれら二つのモデルタイプを区別しています。

## 小型言語モデルの応用

SLMは以下のような幅広い応用分野を持ちます：

- チャットボット：顧客サポートやユーザーとの対話を提供。
- コンテンツ作成：執筆者を支援し、アイデア生成や記事の草稿作成を補助。
- 教育：学生の作文支援や新しい言語学習の助けに。
- アクセシビリティ：テキスト読み上げシステムなど障害者支援ツールの作成。

<strong>サイズ</strong>
  
LLMとSLMの主な違いはモデルの規模にあります。ChatGPT (GPT-4) のようなLLMは推定で1.76兆のパラメータを持つ一方、オープンソースのSLMであるMistral 7Bは約70億パラメータと大幅に少ない数に設計されています。この違いは主にモデルのアーキテクチャと訓練プロセスの違いによるものです。例えば、ChatGPTはエンコーダ-デコーダ形式における自己注意機構を利用するのに対し、Mistral 7Bはデコーダのみのモデル内で効率的な訓練を可能にするスライディングウィンドウ注意を使用しています。このアーキテクチャの違いはモデルの複雑さと性能に大きく影響します。

<strong>理解力</strong>

SLMは特定のドメインに最適化されることが多く、高度に専門化されていますが、複数の分野にまたがる広範な文脈理解能力は限定的になる可能性があります。一方、LLMはより包括的なレベルで人間のような知能を模倣しようと設計されています。多様で大規模なデータセットで訓練され、多様な分野で良好な性能を発揮し、より高い適応性と汎用性を提供します。そのため、LLMは自然言語処理やプログラミングなど、より広範な下流タスクに向いています。

<strong>計算</strong>

LLMの訓練と展開はリソース集約的であり、大規模なGPUクラスターなどの高度な計算インフラを必要とします。例えば、ChatGPTのようなモデルをゼロから訓練するには、何千ものGPUを長期間使用することが求められます。一方、パラメータ数が少ないSLMはより限られた計算資源でもアクセスが容易です。Mistral 7Bのようなモデルは中程度のGPU能力を持つローカルマシンで訓練及び実行が可能ですが、訓練には複数GPUにまたがる数時間が必要です。

<strong>バイアス</strong>

バイアスはLLMにおける既知の問題であり、主に訓練データの性質によります。これらのモデルはインターネットから得られた生のオープンデータに依存することが多く、特定のグループが過小評価または誤って表現されていたり、誤ったラベル付けがされていたり、方言、地理的変異、文法規則に影響された言語的バイアスを反映している可能性があります。加えて、LLMの複雑なアーキテクチャはバイアスを気づかれにくい形で悪化させることがあります。一方、SLMはより制約されたドメイン固有のデータセットで訓練されるため、こうしたバイアスには本質的に弱いですが、完全に免疫があるわけではありません。

<strong>推論</strong>

SLMの小さいサイズは推論速度で大きな利点をもたらし、ローカルハードウェア上で広範な並列処理を必要とせず効率的に出力を生成できます。一方、LLMはその大きさと複雑さのため、許容できる推論時間を得るにはかなりの並列計算資源を必要とします。複数の同時ユーザーが存在すると、スケールアウトされた環境ではLLMの応答時間はさらに遅くなります。

要約すると、LLMとSLMはどちらも機械学習に基づく基盤を共有していますが、モデルサイズ、リソース要件、文脈理解度、バイアス耐性、推論速度の面で大きく異なります。これらの違いは使用ケースごとの適合性を反映しており、LLMはより多用途でリソースを多く消費する一方、SLMは計算負荷を抑えつつ特定ドメインでの効率を提供します。

***注意：本レッスンではMicrosoft Phi-3 / 3.5を例にSLMを紹介します。***

## Phi-3 / Phi-3.5 ファミリーの紹介

Phi-3 / 3.5 ファミリーは主にテキスト、ビジョン、およびAgent（MoE）アプリケーションシナリオを対象としています：

### Phi-3 / 3.5 Instruct

主にテキスト生成、チャット補完、コンテンツ情報抽出などに利用されます。

**Phi-3-mini**

3.8Bパラメータの言語モデルはMicrosoft Foundry、Hugging Face、およびOllamaで利用可能です。Phi-3モデルはキーとなるベンチマークにおいて、同サイズまたはそれ以上のサイズの言語モデルを大きく上回る性能を発揮します（以下のベンチマーク数値参照、数値が高いほど良い）。Phi-3-miniは自モデルの2倍のサイズのモデルに勝り、Phi-3-smallおよびPhi-3-mediumはGPT-3.5を含むより大きなモデルに対しても優れた性能を示します。

**Phi-3-small & medium**

7BパラメータのPhi-3-smallは、さまざまな言語、推論、コーディング、数学のベンチマークでGPT-3.5Tを上回ります。

14BパラメータのPhi-3-mediumもこの傾向を継続し、Gemini 1.0 Proを上回ります。

**Phi-3.5-mini**

Phi-3-miniのアップグレード版と考えられます。パラメータ数は変わりませんが、20以上の言語（アラビア語、中国語、チェコ語、デンマーク語、オランダ語、英語、フィンランド語、フランス語、ドイツ語、ヘブライ語、ハンガリー語、イタリア語、日本語、韓国語、ノルウェー語、ポーランド語、ポルトガル語、ロシア語、スペイン語、スウェーデン語、タイ語、トルコ語、ウクライナ語）に対応し、長い文脈へのサポートを強化しています。

3.8BパラメータのPhi-3.5-miniは同サイズの言語モデルを上回り、2倍のサイズのモデルと同等の性能を示します。

### Phi-3 / 3.5 Vision

Phi-3/3.5のInstructモデルをPhiの理解力とすると、VisionはPhiに世界を理解する目を与えるものです。


**Phi-3-Vision**

4.2BパラメータしかないPhi-3-Visionは、この流れを継続し、Claude-3 HaikuやGemini 1.0 Pro Vなどより大きなモデルを一般的な視覚的推論タスク、OCR、表や図の理解タスクで上回ります。


**Phi-3.5-Vision**

Phi-3.5-VisionはPhi-3-Visionのアップグレード版で、複数画像のサポートを追加しました。単に画像を見るだけでなく動画も扱える視覚の改良版と考えられます。

Phi-3.5-Visionは、OCR、表やチャートの理解タスクでClaude-3.5 SonnetやGemini 1.5 Flashのような大型モデルを上回り、一般的な視覚知識推論タスクでも同等の性能を発揮します。複数フレーム入力をサポートし、複数の入力画像に対する推論を行います。


### Phi-3.5-MoE

<strong><em>Mixture of Experts(MoE)</em></strong>により、モデルははるかに少ない計算量で事前訓練が可能になり、同じ計算予算でモデルやデータセットの規模を劇的に拡大できます。特に、MoEモデルは密なモデルと同等の品質を事前訓練中により速く達成できます。

Phi-3.5-MoEは16x3.8Bの専門家モジュールで構成され、6.6Bのアクティブパラメータしか持たず、それでもより大きなモデルと同等の推論力、言語理解、数学能力を達成します。

Phi-3/3.5ファミリーのモデルはシナリオに応じて活用できます。LLMとは異なり、Phi-3/3.5-miniやPhi-3/3.5-Visionはエッジデバイス上に展開可能です。


## Phi-3/3.5ファミリーモデルの使い方

Phi-3/3.5をさまざまなシナリオで使用することを目指します。次にシナリオ別にPhi-3/3.5の利用法を説明します。

![phi3](../../../translated_images/ja/phi3.655208c3186ae381.webp)

### クラウドAPIによる推論

**Microsoft Foundry モデル**

> **注意:** GitHub Models は2026年7月末にサービス終了予定です。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) へ移行が推奨されます。

Microsoft Foundry Modelsは最も手軽な方法で、Foundryモデルカタログを通じてPhi-3/3.5-Instructモデルに迅速にアクセス可能です。Azure AI Inference SDK / OpenAI SDKと組み合わせることでコードからAPIを呼び出し、Phi-3/3.5-Instructを利用できます。Playgroundからも様々な効果を試せます。

- デモ：中国語シナリオにおけるPhi-3-miniとPhi-3.5-miniの効果比較

![phi3](../../../translated_images/ja/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ja/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

もしVisionやMoEモデルを使いたい場合も、Microsoft Foundryで呼び出しが可能です。興味がある方はPhi-3 Cookbookを参照し、Microsoft Foundry経由でのPhi-3/3.5 Instruct、Vision、MoE呼び出し方法をご確認ください。[こちらのリンク](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

クラウドベースのMicrosoft Foundry Modelsカタログに加え、[NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)を使って関連呼び出しを行うことも可能です。NVIDIA NIM (NVIDIA Inference Microservices)は、クラウド、データセンター、ワークステーションなどの多様な環境でAIモデルを効率的に展開するために設計された加速推論マイクロサービスのセットです。

主なNVIDIA NIMの特徴は以下のとおりです：

- **展開の容易さ:** NIMは一つのコマンドでAIモデルを展開でき、既存のワークフローへの統合が容易です。

- **最適化されたパフォーマンス:** TensorRTやTensorRT-LLMなど、NVIDIAの事前最適化済み推論エンジンを活用し、低レイテンシと高スループットを実現します。
- **スケーラビリティ:** NIMはKubernetesのオートスケーリングをサポートしており、変動するワークロードに効果的に対応できます。
- **セキュリティと管理:** 組織はNIMマイクロサービスを自社管理のインフラ上でセルフホスティングすることで、データやアプリケーションの管理を維持できます。
- **標準API:** NIMは業界標準のAPIを提供し、チャットボット、AIアシスタントなどのAIアプリケーションの構築や統合を容易にします。

NIMはNVIDIA AI Enterpriseの一部であり、AIモデルの展開と運用を簡素化し、NVIDIA GPU上で効率的に動作することを目指しています。

- デモ: NVIDIA NIMを使用してPhi-3.5-Vision-APIを呼び出す [[このリンクをクリック](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5をローカルで実行する
Phi-3やGPT-3などの言語モデルに関する推論とは、入力に基づいて応答や予測を生成するプロセスを指します。Phi-3にプロンプトや質問を与えると、訓練済みのニューラルネットワークを使って、訓練データ内のパターンや関係性を分析し、最も可能性が高く関連性のある応答を推測します。

**Hugging Face Transformer**
Hugging Face Transformersは、自然言語処理（NLP）やその他の機械学習タスク用に設計された強力なライブラリです。主なポイントは以下の通りです：

1. <strong>事前学習済みモデル</strong>: テキスト分類、固有表現抽出、質問応答、要約、翻訳、テキスト生成など、多様なタスクに使える数千の事前学習済みモデルを提供します。

2. <strong>フレームワーク間の互換性</strong>: PyTorch、TensorFlow、JAXなど複数のディープラーニングフレームワークをサポートし、あるフレームワークでモデルを訓練し他のフレームワークで利用可能です。

3. <strong>マルチモーダル機能</strong>: NLPに加え、画像分類や物体検出などのコンピュータビジョンタスク、音声認識や音声分類などの音声処理タスクもサポートしています。

4. <strong>使いやすさ</strong>: モデルのダウンロードやファインチューニングを簡単に行えるAPIやツールを提供しており、初心者から専門家まで利用しやすい設計です。

5. <strong>コミュニティとリソース</strong>: 活発なコミュニティと豊富なドキュメント、チュートリアル、ガイドがあり、利用開始や最大活用を支援します。
[公式ドキュメント](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) または [GitHubリポジトリ](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst) を参照してください。

これは最も一般的な方法ですが、GPUアクセラレーションが必要です。特にVisionやMoEなどのシナリオは多くの計算を必要とし、量子化されていなければCPUでは非常に遅くなります。


- デモ: Transformerを使用してPhi-3.5-Instructを呼び出す [このリンクをクリック](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- デモ: Transformerを使用してPhi-3.5-Visionを呼び出す [このリンクをクリック](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- デモ: Transformerを使用してPhi-3.5-MoEを呼び出す [このリンクをクリック](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) は、大規模言語モデル（LLM）をローカルマシン上で簡単に動かせるように設計されたプラットフォームです。Llama 3.1、Phi 3、Mistral、Gemma 2など様々なモデルをサポートしています。モデルの重み、設定、データをひとつのパッケージにまとめて提供し、ユーザーがカスタマイズやモデル作成をしやすくしています。macOS、Linux、Windows向けに提供されており、クラウドに依存せずにLLMを試したり展開したりするのに最適なツールです。Ollamaは最も直接的な方法であり、以下のコマンドを実行するだけです。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) は、Phiのようなモデルを完全に自分のハードウェアでオフラインかつオンデバイスで動かすためのMicrosoftのランタイムです。Azureサブスクリプション、APIキー、ネットワーク接続は不要です。利用可能な最適な実行プロバイダー（NPU、GPU、CPU）を自動的に選択し、OpenAI互換のエンドポイントを提供するため、既存の`openai`/Azure AI Inference SDKコードを最小限の変更で利用できます。始めるには[Foundry Localドキュメント](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)をご覧ください。

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

またはPythonで直接SDKを使用できます：

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) はクロスプラットフォームの推論・学習用機械学習アクセラレータです。ONNX Runtime for Generative AI (GENAI)は、多様なプラットフォームで生成系AIモデルを効率的に実行する強力なツールです。

## ONNX Runtimeとは？
ONNX Runtimeは、高性能な機械学習モデルの推論を可能にするオープンソースプロジェクトです。Open Neural Network Exchange(ONNX)フォーマットのモデルをサポートします。ONNX Runtimeの推論により、高速なユーザー体験と低コストを実現でき、PyTorchやTensorFlow/Kerasのディープラーニングフレームワークから、scikit-learn、LightGBM、XGBoostなどの古典的機械学習ライブラリのモデルまで対応しています。ONNX Runtimeは多様なハードウェア、ドライバー、OSに対応し、グラフ最適化や変換に加え、ハードウェアアクセラレータを活用することで最適なパフォーマンスを提供します。

## 生成系AIとは？
生成系AIとは、学習したデータに基づいてテキスト、画像、音楽などの新しいコンテンツを生成できるAIシステムを指します。GPT-3のような言語モデルやStable Diffusionのような画像生成モデルが例です。ONNX Runtime for GenAIライブラリは、ONNXモデルの生成系AIループを提供し、ONNX Runtimeによる推論、ロジット処理、探索とサンプリング、KVキャッシュ管理などを行います。

## ONNX Runtime for GENAI
ONNX Runtime for GENAIは、生成系AIモデルをサポートするためにONNX Runtimeの機能を拡張したものです。主な特徴は以下の通りです：

- **幅広いプラットフォーム対応:** Windows、Linux、macOS、Android、iOSを含むさまざまなプラットフォームで動作します。
- **モデル対応:** LLaMA、GPT-Neo、BLOOMなどの人気の生成系AIモデルをサポートします。
- **パフォーマンス最適化:** NVIDIA GPU、AMD GPUなどの異なるハードウェアアクセラレータ向けの最適化が含まれています。
- **使いやすさ:** アプリケーションへの統合が簡単なAPIを提供し、最小限のコードでテキスト、画像、その他のコンテンツを生成できます。
- ユーザーは高レベルのgenerate()メソッドを呼び出すか、1トークンずつ生成しながらループ内でモデルの各イテレーションを実行し、必要に応じて生成パラメータを更新できます。
- ONNX Runtimeは貪欲探索やビームサーチ、TopP、TopKサンプリング、繰り返しペナルティなどのロジット処理もサポートしており、カスタムスコアリングを簡単に追加できます。

## はじめに
ONNX Runtime for GENAIの利用を始めるには、以下の手順を参考にしてください：

### ONNX Runtimeのインストール：
```Python
pip install onnxruntime
```
### 生成系AI拡張のインストール：
```Python
pip install onnxruntime-genai
```

### モデルの実行：Pythonの簡単な例はこちら
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### デモ: ONNX Runtime GenAIでPhi-3.5-Visionを呼び出す


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


<strong>その他</strong>

ONNX Runtime、Ollama、Foundry Localの参照方法に加え、各社が提供するモデル参照方法を基に量子化モデルのリファレンスも完成させることができます。例えばAppleのMetalを用いたApple MLXフレームワーク、QualcommのNPUを使うQNN、IntelのOpenVINOによるCPU/GPU対応などです。詳しくは[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)をご覧ください。


## その他の情報

Phi-3/3.5ファミリーの基本を学びましたが、SLMについてより深く学ぶにはさらに知識が必要です。答えはPhi-3 Cookbookにあります。詳細を知りたい方はぜひ[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)をご訪問ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->