<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:07:50+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ja"
}
-->
# Metaファミリーモデルでの構築

## はじめに

このレッスンでは以下をカバーします：

- 主なMetaファミリーモデル2つ、Llama 3.1とLlama 3.2の探索
- 各モデルのユースケースとシナリオの理解
- 各モデルのユニークな特徴を示すコードサンプル

## Metaファミリーのモデル

このレッスンでは、Metaファミリーまたは「Llama Herd」からLlama 3.1とLlama 3.2の2つのモデルを探ります。

これらのモデルはさまざまなバリアントがあり、GitHub Modelマーケットプレイスで利用可能です。GitHub Modelsを使用して[AIモデルでプロトタイプを作成する](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)方法の詳細はこちらをご覧ください。

モデルバリアント：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注：Llama 3もGitHub Modelsで利用可能ですが、このレッスンでは取り上げません*

## Llama 3.1

4050億パラメータを持つLlama 3.1は、オープンソースLLMカテゴリに属します。

このモデルは以前のリリースであるLlama 3のアップグレード版であり、以下を提供します：

- より大きなコンテキストウィンドウ - 128kトークン対8kトークン
- より大きな最大出力トークン - 4096対2048
- より良い多言語サポート - トレーニングトークンの増加による

これにより、Llama 3.1はGenAIアプリケーションの構築時により複雑なユースケースを処理できるようになります：
- ネイティブ関数呼び出し - LLMワークフロー外の外部ツールや関数を呼び出す能力
- より良いRAGパフォーマンス - より高いコンテキストウィンドウのおかげ
- 合成データ生成 - 微調整などのタスクに効果的なデータを作成する能力

### ネイティブ関数呼び出し

Llama 3.1は、関数やツールの呼び出しをより効果的に行うように微調整されています。また、ユーザーのプロンプトに基づいて使用が必要と認識される2つの組み込みツールを持っています。これらのツールは：

- **Brave Search** - 天気のような最新情報を得るためにウェブ検索を行うことができる
- **Wolfram Alpha** - より複雑な数学的計算を行うために使用でき、独自の関数を書く必要がありません。

LLMが呼び出すカスタムツールを作成することもできます。

以下のコード例では：

- 利用可能なツール（brave_search、wolfram_alpha）をシステムプロンプトで定義します。
- 特定の都市の天気について尋ねるユーザープロンプトを送信します。
- LLMはBrave Searchツールへのツール呼び出しで応答し、それは次のようになります`<|python_tag|>brave_search.call(query="Stockholm weather")`

*注：この例ではツール呼び出しのみを行います。結果を得たい場合は、Brave APIページで無料アカウントを作成し、関数自体を定義する必要があります*

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

LLMであるにもかかわらず、Llama 3.1にはマルチモダリティという制限があります。つまり、画像などの異なるタイプの入力をプロンプトとして使用し、応答を提供する能力です。この能力はLlama 3.2の主な特徴の一つです。これらの特徴には以下も含まれます：

- マルチモダリティ - テキストと画像プロンプトの両方を評価する能力
- 小から中サイズのバリエーション（11Bと90B） - 柔軟なデプロイメントオプションを提供
- テキストのみのバリエーション（1Bと3B） - モデルをエッジ/モバイルデバイスにデプロイし、低遅延を提供

マルチモーダルサポートはオープンソースモデルの世界における大きな進歩を表しています。以下のコード例は、Llama 3.2 90Bから画像の分析を得るために画像とテキストプロンプトの両方を取ります。

### Llama 3.2によるマルチモーダルサポート

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

## 学習はここで止まりません。旅を続けましょう

このレッスンを完了した後は、[Generative AI Learningコレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、Generative AIの知識をさらに深めていきましょう！

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご注意ください。元の文書がその言語での権威ある情報源とみなされるべきです。重要な情報については、プロの人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解については責任を負いません。