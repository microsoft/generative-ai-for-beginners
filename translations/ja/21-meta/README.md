# Metaファミリーモデルを使った構築

## はじめに

このレッスンでは以下をカバーします：

- 主要な2つのMetaファミリーモデル - Llama 3.1とLlama 3.2の探求
- 各モデルのユースケースとシナリオの理解
- 各モデルのユニークな特徴を示すコードサンプル

## Metaファミリーのモデル

このレッスンでは、Metaファミリー、または「Llama Herd」から2つのモデル - Llama 3.1とLlama 3.2を探ります。

これらのモデルは異なるバリアントで提供されており、Github Modelマーケットプレイスで入手可能です。Github Modelsを使用して[AIモデルでプロトタイプを作成する](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)方法についての詳細はこちらをご覧ください。

モデルのバリアント：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注意: Llama 3もGithub Modelsで利用可能ですが、このレッスンでは取り上げません。*

## Llama 3.1

4050億のパラメータを持つLlama 3.1は、オープンソースのLLMカテゴリに属します。

このモデルは、以前のリリースであるLlama 3のアップグレード版で、以下を提供します：

- より大きなコンテキストウィンドウ - 128kトークン対8kトークン
- より大きな最大出力トークン - 4096対2048
- 多言語サポートの向上 - トレーニングトークンの増加による

これにより、Llama 3.1はGenAIアプリケーションの構築時により複雑なユースケースを処理できるようになります。具体的には：
- ネイティブ機能呼び出し - LLMワークフロー外の外部ツールや機能を呼び出す能力
- RAGパフォーマンスの向上 - より高いコンテキストウィンドウによる
- 合成データ生成 - 微調整などのタスクに効果的なデータを作成する能力

### ネイティブ機能呼び出し

Llama 3.1は、機能やツールの呼び出しをより効果的に行うように微調整されています。また、ユーザーからのプロンプトに基づいて使用が必要と判断される2つの組み込みツールがあります。これらのツールは：

- **Brave Search** - ウェブ検索を行うことで天気などの最新情報を取得するのに使用できます
- **Wolfram Alpha** - より複雑な数学的計算に使用できるため、独自の関数を書く必要がありません

また、LLMが呼び出すことができる独自のカスタムツールを作成することもできます。

以下のコード例では：

- システムプロンプトで利用可能なツール（brave_search、wolfram_alpha）を定義します。
- 特定の都市の天気について尋ねるユーザープロンプトを送信します。
- LLMはBrave Searchツールへのツール呼び出しで応答します。それは次のように見えるでしょう `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意: この例はツール呼び出しのみを行います。結果を取得したい場合は、Brave APIページで無料アカウントを作成し、関数自体を定義する必要があります。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

LLMであるにもかかわらず、Llama 3.1にはマルチモーダル対応の制限があります。つまり、画像などの異なる種類の入力をプロンプトとして使用し、応答を提供する能力です。この能力はLlama 3.2の主要な特徴の一つです。これらの特徴には以下も含まれます：

- マルチモーダル対応 - テキストと画像のプロンプトの両方を評価する能力
- 小規模から中規模のバリエーション（11Bと90B） - 柔軟なデプロイメントオプションを提供
- テキストのみのバリエーション（1Bと3B） - エッジ/モバイルデバイスでモデルをデプロイし、低レイテンシーを提供

マルチモーダル対応は、オープンソースモデルの世界における大きな進歩を表しています。以下のコード例では、Llama 3.2 90Bから画像の分析を得るために、画像とテキストプロンプトの両方を取ります。

### Llama 3.2によるマルチモーダル対応

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## 学習はここで終わりません、旅を続けましょう

このレッスンを完了した後は、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、Generative AIの知識をさらに深めましょう！

**免責事項**:  
この文書は機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めていますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご注意ください。元の言語の文書を権威ある情報源と見なすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。