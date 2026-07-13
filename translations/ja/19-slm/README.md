# ジェネレーティブAIのための小型言語モデル入門（初心者向け）
ジェネレーティブAIは、新しいコンテンツを生成できるシステムの作成に焦点を当てた人工知能の魅力的な分野です。このコンテンツは、テキストや画像から音楽、さらには仮想環境全体に至るまで多岐にわたります。ジェネレーティブAIの最もエキサイティングな応用の一つは、言語モデルの領域にあります。

## 小型言語モデルとは？

小型言語モデル（SLM）は、大型言語モデル（LLM）の縮小版であり、多くのLLMのアーキテクチャ原則や技術を活用しながら、計算量を大幅に削減したものを指します。

SLMは、人間のようなテキストを生成するよう設計された言語モデルの一種です。GPT-4のような大型モデルとは異なり、SLMはよりコンパクトで効率的であり、計算リソースが限られた環境において理想的です。サイズは小さいものの、様々なタスクを実行可能です。一般的に、SLMはLLMを圧縮または蒸留して構築され、元のモデルの機能性と言語能力の大部分を保持することを目指しています。モデルサイズの削減により複雑さが軽減され、メモリ使用量と計算要件の両方でSLMはより効率的になります。これらの最適化があっても、SLMは多岐にわたる自然言語処理（NLP）タスクを実行可能です：

- テキスト生成：一貫性があり文脈に適した文章や段落の作成。
- テキスト補完：与えられたプロンプトに基づいた文の予測および補完。
- 翻訳：ある言語のテキストを別の言語に変換。
- 要約：長い文章を短く分かりやすい要約に凝縮。

ただし、大型モデルと比較した場合、性能や理解の深さに若干のトレードオフがあります。

## 小型言語モデルはどのように機能するか？
SLMは大量のテキストデータで訓練されます。訓練中に言語のパターンや構造を学習し、文法的に正しくかつ文脈に適したテキストを生成できるようになります。訓練プロセスは以下を含みます：

- データ収集：様々なソースから大規模なテキストデータセットを集める。
- 前処理：訓練に適した状態にデータをクリーンアップし整理する。
- 訓練：機械学習アルゴリズムを用いてテキストの理解と生成をモデルに学習させる。
- ファインチューニング：特定のタスクでの性能向上のためにモデルを調整する。

SLMの開発は、モバイル端末やエッジコンピューティングプラットフォームのようなリソース制約のある環境で展開できるモデルのニーズ増加に合致しています。フルスケールのLLMはリソース消費が多いため実用的でない場合があります。効率性に注力することで、SLMは性能とアクセス可能性のバランスを取り、様々な分野での幅広い応用を可能にしています。

![slm](../../../translated_images/ja/slm.4058842744d0444a.webp)

## 学習目標

本レッスンでは、SLMの知識を紹介し、Microsoft Phi-3と組み合わせてテキストコンテンツ、ビジョン、MoEの異なるシナリオを学びます。

このレッスンの終了時には以下の質問に答えられることを目指します：

- SLMとは何か？
- SLMとLLMの違いは何か？
- Microsoft Phi-3/3.5ファミリーとは？
- Microsoft Phi-3/3.5ファミリーで推論を実行する方法は？

準備は良いですか？ 始めましょう。

## 大型言語モデル（LLM）と小型言語モデル（SLM）の違い

LLMとSLMは共に、確率的機械学習の基礎原則に基づき、アーキテクチャ設計、訓練方法、データ生成プロセス、モデル評価技術において類似したアプローチを採用しています。しかし、これら2種類のモデルにはいくつかの重要な違いがあります。

## 小型言語モデルの応用例

SLMは以下のような幅広い応用例があります：

- チャットボット：顧客サポートを提供し、ユーザーと対話形式で交流。
- コンテンツ作成：アイデアの生成や記事の草稿作成など作家を支援。
- 教育：学生の作文支援や新しい言語の学習を助ける。
- アクセシビリティ：テキスト読み上げシステムなど障害者用ツールの作成。

<strong>サイズ</strong>
  
LLMとSLMの主な違いはモデルの規模にあります。ChatGPT（GPT-4）のようなLLMは約1.76兆パラメーターを持つのに対し、オープンソースのSLM（例：Mistral 7B）は約70億のパラメーターで設計されています。この差異は主にモデルアーキテクチャと訓練プロセスの違いに起因します。例えば、ChatGPTはエンコーダー・デコーダー構造内で自己注意メカニズムを使用しますが、Mistral 7Bはスライディングウィンドウ注意を用いたデコーダー単独モデルで、より効率的な訓練が可能です。このアーキテクチャの違いはモデルの複雑さと性能に大きな影響を与えます。

<strong>理解度</strong>

SLMは特定ドメイン内での性能最適化が多いため、高度に専門化されていますが、多分野にわたる広範な文脈理解には制限があります。一方、LLMはより包括的に人間のような知能を模倣することを目指しています。広範で多様なデータセットで訓練されており、多様なドメインで高い適応性と汎用性を持つため、より広範な下流タスク（自然言語処理やプログラミングなど）に適しています。

<strong>計算資源</strong>

LLMの訓練と展開は計算リソースを大量に消費し、大規模なGPUクラスターを必要とします。例えば、ChatGPTのようなモデルをスクラッチから訓練するには、数千のGPUを長時間使用する必要があります。これに対し、SLMはパラメーター数が少ないため、計算リソース面でよりアクセスしやすく、Mistral 7Bのようなモデルは中程度のGPUを搭載したローカルマシンで訓練・実行可能ですが、数台のGPUで数時間の訓練は必要です。

<strong>バイアス</strong>

バイアスはLLMにおける既知の問題であり、主に訓練データの性質に起因します。これらのモデルはインターネットから取得した生の公開データを多く使用しており、特定のグループを過小評価または誤って表現することがあり、誤ったラベル付けや方言、地理的差異、文法規則による言語バイアスを含む可能性があります。さらに、LLMの複雑なアーキテクチャはバイアスを悪化させることがあり、細かなファインチューニングなしでは認識しづらいことがあります。対照的に、SLMはより制限されたドメイン固有のデータセットで訓練されるため、こうしたバイアスの影響は相対的に小さいものの、完全に免疫があるわけではありません。

<strong>推論</strong>

SLMの小型化は推論速度の大幅な向上をもたらし、広範な並列処理なしでローカルハードウェア上で効率的に出力生成が可能です。対してLLMはそのサイズと複雑さのため、許容可能な推論時間を実現するには大規模な並列計算資源がしばしば必要です。多数の同時ユーザーがいる場合、LLMの応答時間はさらに遅延します。

まとめると、LLMとSLMは機械学習に基づく共通基盤を持ちながら、モデルサイズ、リソース要件、文脈理解、バイアスへの感受性、推論速度において著しい違いがあります。これらの違いが使用用途の適合性を反映し、LLMはより多用途でリソース多用、SLMは特定ドメインに特化し計算負荷を軽減した効率を提供します。

***注：本レッスンでは例としてMicrosoft Phi-3 / 3.5を用いてSLMを紹介します。***

## Phi-3 / Phi-3.5 ファミリーの紹介

Phi-3 / 3.5 ファミリーは主にテキスト、ビジョン、エージェント（MoE）アプリケーションのシナリオを対象としています：

### Phi-3 / 3.5 インストラクト

主にテキスト生成、チャット補完、コンテンツ情報抽出などに使われます。

**Phi-3-mini**

3.8Bの言語モデルがMicrosoft Foundry、Hugging Face、Ollamaで利用可能です。Phi-3モデルは主要なベンチマークで同サイズまたはそれ以上のモデルを大きく上回る性能を示しています（下記ベンチマーク数値参照、数値が大きいほど良い）。Phi-3-miniは自身の2倍のサイズのモデルより優れており、Phi-3-smallおよびPhi-3-mediumはGPT-3.5を含むより大きなモデルに勝ります。

**Phi-3-small & medium**

7BパラメーターのPhi-3-smallは各種言語、推論、コーディング、数学ベンチマークでGPT-3.5Tを上回ります。

14BパラメーターのPhi-3-mediumはこの傾向を継続し、Gemini 1.0 Proを上回ります。

**Phi-3.5-mini**

Phi-3-miniのアップグレード版と考えられます。パラメーター数は変わりませんが、多言語対応能力が向上し（アラビア語、中国語、チェコ語、デンマーク語、オランダ語、英語、フィンランド語、フランス語、ドイツ語、ヘブライ語、ハンガリー語、イタリア語、日本語、韓国語、ノルウェー語、ポーランド語、ポルトガル語、ロシア語、スペイン語、スウェーデン語、タイ語、トルコ語、ウクライナ語を含む20以上の言語をサポート）長文コンテキスト対応も強化されました。

3.8BパラメーターのPhi-3.5-miniは同サイズの言語モデルを凌ぎ、2倍のサイズのモデルと同等の性能を持ちます。

### Phi-3 / 3.5 ビジョン

Phi-3/3.5のインストラクトモデルはPhiの理解力を表し、ビジョンはPhiに世界を認識する目を与えます。


**Phi-3-Vision**

4.2BパラメーターのPhi-3-visionはこの傾向を継続し、Claude-3 HaikuやGemini 1.0 Pro Vなどのより大きなモデルを一般的な視覚推論タスク、OCR、表や図の理解タスクで上回ります。


**Phi-3.5-Vision**

Phi-3.5-VisionもPhi-3-Visionのアップグレード版であり、複数画像サポートを追加しました。単なる画像認識だけでなく動画も認識可能になった改善版と考えられます。

Phi-3.5-visionはClaude-3.5 SonnetやGemini 1.5 Flashなどより大きなモデルをOCR、表やチャートの理解タスクで上回り、一般的な視覚知識推論タスクでも同等の性能を発揮します。複数フレーム入力、すなわち複数の入力画像に対する推論をサポートします。


### Phi-3.5-MoE

<strong><em>Mixture of Experts(MoE)</em></strong>は同じ計算予算で密結合モデルに比べて、遥かに少ない計算量でプレトレーニングできるモデル構造を可能にします。特に、MoEモデルはプレトレーニング時に密結合モデルと同等の品質をより速く達成できます。

Phi-3.5-MoEは16×3.8Bの専門家モジュールから構成されます。6.6BのアクティブパラメーターでPhi-3.5-MoEはより大きなモデルと同等の推論、言語理解、数学能力を実現します。

Phi-3/3.5ファミリーモデルは異なるシナリオに基づいて使用可能です。LLMとは異なり、Phi-3/3.5-miniやPhi-3/3.5-Visionはエッジデバイスに展開できます。


## Phi-3/3.5ファミリーモデルの利用方法

Phi-3/3.5を様々なシナリオで使いたいと考えています。次にこれらのシナリオに基づいてPhi-3/3.5を使います。

![phi3](../../../translated_images/ja/phi3.655208c3186ae381.webp)

### クラウドAPIによる推論

**Microsoft Foundry モデル**

> **注意:** GitHub Modelsは2026年7月末に廃止予定です。[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)がその後継となります。

Microsoft Foundry Modelsは最も直接的な方法で、Foundryモデルカタログから迅速にPhi-3/3.5-Instructモデルにアクセス可能です。Azure AI Inference SDK / OpenAI SDKと組み合わせてコード経由でAPI呼び出しが可能で、Playgroundを使って様々な効果をテストできます。

- デモ：Phi-3-miniとPhi-3.5-miniの中国語シナリオでの効果比較

![phi3](../../../translated_images/ja/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ja/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

ビジョンやMoEモデルを使いたい場合もMicrosoft Foundryを利用して呼び出せます。興味があればPhi-3 Cookbookを読み、Microsoft Foundry経由でPhi-3/3.5 Instruct、Vision、MoEを呼び出す方法を学んでください。[こちらのリンク](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

クラウドベースのMicrosoft Foundry Modelsカタログに加え、[NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)を使って関連呼び出しを行うことも可能です。NVIDIA NIMはPhi-3/3.5ファミリーのAPI呼び出しをサポートし、クラウド、データセンター、ワークステーションなど多様な環境で効率的なAIモデル展開を支援する加速推論マイクロサービス群です。

NVIDIA NIMの主な特徴は以下の通りです：

- **展開の容易さ:** NIMは単一コマンドでAIモデル展開を可能にし、既存のワークフローに統合しやすいです。

- **最適化されたパフォーマンス:** TensorRTやTensorRT-LLMなど、NVIDIAの事前最適化済み推論エンジンを活用して、低遅延かつ高スループットを実現します。
- **スケーラビリティ:** NIMはKubernetes上でのオートスケーリングをサポートし、変動するワークロードに効果的に対応します。
- **セキュリティと制御:** 組織は、自身の管理するインフラ上でNIMマイクロサービスをセルフホスティングすることで、データとアプリケーションの制御を維持できます。
- **標準的なAPI:** NIMは業界標準のAPIを提供し、チャットボットやAIアシスタントなどのAIアプリケーションの構築や統合を容易にします。

NIMはNVIDIA AI Enterpriseの一部であり、AIモデルの展開と運用を簡素化し、NVIDIA GPU上で効率的に動作させることを目指しています。

- デモ: NVIDIA NIMを使用してPhi-3.5-Vision-APIを呼び出す [[こちらをクリック](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5をローカルで実行する
Phi-3やGPT-3のような言語モデルに関連する推論とは、入力に基づいて応答や予測を生成するプロセスを指します。Phi-3にプロンプトや質問を提供すると、訓練されたニューラルネットワークを使って、訓練データ中のパターンや関係を分析し、最も可能性が高く関連性の高い応答を推論します。

**Hugging Face Transformer**
Hugging Face Transformersは、自然言語処理（NLP）やその他の機械学習タスク向けに設計された強力なライブラリです。以下はその主なポイントです：

1. **事前学習済みモデル:** テキスト分類、固有表現抽出、質問応答、要約、翻訳、テキスト生成など、さまざまなタスクに使える数千の事前学習済みモデルを提供しています。

2. **フレームワーク間互換性:** PyTorch、TensorFlow、JAXなど複数のディープラーニングフレームワークをサポートしており、あるフレームワークでトレーニングしたモデルを別のフレームワークで使用できます。

3. **マルチモーダル機能:** NLP以外にも、画像分類や物体検出などのコンピュータビジョン、音声認識や音声分類などのオーディオ処理をサポートしています。

4. **使いやすさ:** モデルのダウンロードやファインチューニングを簡単に行うAPIやツールを提供し、初心者から専門家まで幅広く利用可能です。

5. **コミュニティとリソース:** 活発なコミュニティと充実したドキュメント、チュートリアルやガイドがあり、利用開始や活用をサポートします。
[公式ドキュメント](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) や [GitHubリポジトリ](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)も参照してください。

これは最も一般的な方法ですが、GPUアクセラレーションが必要です。特にVisionやMoEなどのシナリオでは大量の計算を要し、量子化されていなければCPUでは非常に遅くなります。


- デモ: Transformerを使用してPhi-3.5-Instructを呼び出す [こちらをクリック](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- デモ: Transformerを使用してPhi-3.5-Visionを呼び出す [こちらをクリック](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- デモ: Transformerを使用してPhi-3.5-MoEを呼び出す [こちらをクリック](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)は、大規模言語モデル（LLM）をローカルマシンでより簡単に実行できるよう設計されたプラットフォームです。Llama 3.1、Phi 3、Mistral、Gemma 2など様々なモデルをサポートします。モデルの重み、構成、データを一つのパッケージにまとめて提供することで、ユーザーがカスタマイズやオリジナルモデル作成を容易に行えるようにしています。macOS、Linux、Windows対応で、クラウドサービスに依存せずにLLMを試したりデプロイしたりしたい場合に最適なツールです。Ollamaは最も直接的な方法で、以下のコマンドを実行するだけです。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)はマイクロソフトのオフライン・オンデバイス実行環境で、Phiのようなモデルを完全にローカルハードウェア上で実行可能にします。AzureのサブスクリプションやAPIキー、ネットワーク接続は不要です。利用可能な最適な実行プロバイダー（NPU、GPU、CPU）を自動的に選択し、OpenAI互換のエンドポイントを公開するため、既存の`openai`/Azure AI Inference SDKコードはわずかな変更で対応可能です。詳細は[Foundry Local ドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)を参照してください。

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

またはPythonでSDKを直接使用:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) はクロスプラットフォームの推論およびトレーニング用機械学習アクセラレータです。ONNX Runtime for Generative AI（GENAI）は、さまざまなプラットフォームで効率的に生成AIモデルを実行できる強力なツールです。

## ONNX Runtimeとは？
ONNX Runtimeは高性能な機械学習モデルの推論を可能にするオープンソースプロジェクトです。Open Neural Network Exchange（ONNX）フォーマットのモデルをサポートしており、これは機械学習モデル表現の標準です。ONNX Runtime推論により、顧客体験の高速化とコスト削減を実現し、PyTorchやTensorFlow/Kerasなどのディープラーニングフレームワークに加え、scikit-learn、LightGBM、XGBoostといった古典的機械学習ライブラリのモデルもサポートします。異なるハードウェア、ドライバ、OSに互換性があり、ハードウェアアクセラレータの活用とグラフ最適化や変換によって最適な性能を提供します。

## 生成AIとは？
生成AIは、訓練データに基づいてテキスト、画像、音楽などの新しいコンテンツを生成できるAIシステムを指します。例としてGPT-3のような言語モデルやStable Diffusionのような画像生成モデルがあります。ONNX Runtime for GenAIライブラリはONNXモデル向けの生成AIループを提供し、ONNX Runtimeによる推論、ロジット処理、探索とサンプリング、KVキャッシュ管理を含みます。

## ONNX Runtime for GENAI
ONNX Runtime for GENAIは、ONNX Runtimeの機能を拡張して生成AIモデルをサポートします。主な特徴は以下の通りです：

- **幅広いプラットフォームサポート:** Windows、Linux、macOS、Android、iOSなど様々なプラットフォームで動作します。
- **モデルサポート:** LLaMA、GPT-Neo、BLOOMなど多くの人気生成AIモデルをサポートします。
- **パフォーマンス最適化:** NVIDIA GPUやAMD GPUなど異なるハードウェアアクセラレータに対する最適化を含みます。
- **使いやすさ:** アプリケーションへ容易に統合できるAPIを提供し、最小限のコードでテキストや画像などのコンテンツ生成を可能にします。
- ユーザーは高レベルのgenerate()メソッドを呼び出すことも、ループ内でモデルの各イテレーションを実行しトークンを一つずつ生成し、オプションでループ内で生成パラメータを更新することも可能です。
- ONNX Runtimeは貪欲法/ビームサーチやTopP、TopKサンプリングのサポートもあり、トークン列の生成や繰り返しペナルティなどのロジット処理機能も内蔵しています。カスタムスコアリングも簡単に追加できます。

## はじめに
ONNX Runtime for GENAIの使用を開始するには、以下の手順に従ってください：

### ONNX Runtimeをインストール：
```Python
pip install onnxruntime
```
### 生成AI拡張機能をインストール：
```Python
pip install onnxruntime-genai
```

### モデルを実行：Pythonでの簡単な例：
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
### デモ: ONNX Runtime GenAIを使ってPhi-3.5-Visionを呼び出す


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

ONNX Runtime、Ollama、Foundry Localのリファレンスメソッドに加え、異なるメーカーが提供するモデル参考方法に基づく量子化モデルのリファレンスも補完可能です。例えばApple Metalを使ったApple MLXフレームワーク、NPUを用いたQualcomm QNN、CPU/GPU対応のIntel OpenVINOなどです。詳細は[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)からも入手できます。


## さらに

Phi-3/3.5ファミリーの基本は学びましたが、SLMについてより深く学ぶにはさらなる知識が必要です。答えはPhi-3 Cookbookにあります。詳細を知りたい場合は、ぜひ[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)をご覧ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->