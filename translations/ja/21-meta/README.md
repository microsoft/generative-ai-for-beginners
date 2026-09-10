# Metaファミリーモデルでの構築 

## はじめに 

このレッスンでは以下を取り上げます： 

- 主なMetaファミリーモデル2種の探求 - Llama 3.1とLlama 3.2 
- 各モデルのユースケースとシナリオの理解 
- 各モデルのユニークな特徴を示すコードサンプル 


## Metaファミリーモデルについて 

このレッスンでは、Metaファミリーまたは「Llama Herd」から2つのモデル、Llama 3.1とLlama 3.2を探ります。

これらのモデルは様々なバリエーションがあり、[Microsoft Foundry Modelsカタログ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)で入手可能です。

> **注意:** GitHub Modelsは2026年7月末にサービス終了予定です。[Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst)を使ったAIモデルのプロトタイプ作成についての詳細はこちらをご覧ください。

モデルのバリエーション: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*注意: Llama 3もMicrosoft Foundry Modelsで利用可能ですが、このレッスンでは扱いません*

## Llama 3.1 

4050億パラメーターを持つLlama 3.1はオープンソースLLMのカテゴリに属します。 

このモデルは、初期リリースのLlama 3から以下の点でアップグレードされています： 

- より大きなコンテキストウィンドウ - 8kトークンから128kトークンへ 
- 最大出力トークン数増加 - 2048から4096へ 
- トレーニングトークンの増加により多言語対応が改善 

これによりLlama 3.1は次のようなGenAIアプリケーションの複雑なユースケースに対応可能です： 
- ネイティブ関数呼び出し - LLMワークフロー外の外部ツールや関数を呼び出す機能
- RAG性能の向上 - より広いコンテキストウィンドウによる 
- 合成データ生成 - ファインチューニングなどのタスク用に効果的なデータを作成する能力 

### ネイティブ関数呼び出し 

Llama 3.1は関数やツール呼び出しをより効果的に行うようにファインチューニングされています。また、モデルがユーザープロンプトに基づいて使用すべきと識別できる2つの組み込みツールがあります。これらのツールは： 

- **Brave Search** - ウェブ検索を行い、天気など最新情報を取得可能 
- **Wolfram Alpha** - 複雑な数式計算に利用でき、自分で関数を書く必要がない 

独自のカスタムツールを作成し、LLMが呼び出せるようにすることも可能です。 

以下のコード例では： 

- 利用可能なツール（brave_search、wolfram_alpha）をシステムプロンプトで定義しています。 
- 特定の都市の天気について問い合わせるユーザープロンプトを送信。 
- LLMはBrave Searchツールの呼び出しで応答し、`<|python_tag|>brave_search.call(query="Stockholm weather")`のようになります。 

*注意: この例はツール呼び出しのみ行います。結果を取得したい場合はBrave APIページで無料アカウントを作成し、関数本体を定義する必要があります。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# これらはMicrosoft Foundryプロジェクトの「概要」ページから取得します
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Llama 3.1はLLMながらマルチモーダリティの欠如という制限があります。つまり、画像など異なるタイプの入力をプロンプトとして使い、応答を返すことができません。この能力はLlama 3.2の主な特徴の一つです。その他の特徴は： 

- マルチモーダリティ - テキストと画像の両方のプロンプトを評価可能 
- 小から中サイズのバリエーション (11Bと90B) - 柔軟な展開オプションを提供 
- テキストのみバリエーション (1Bと3B) - エッジ/モバイルデバイスでの展開が可能で低遅延提供 

マルチモーダル対応はオープンソースモデルの世界で大きな進歩を示しています。以下のコード例は画像とテキストの両方のプロンプトを取り、Llama 3.2 90Bから画像の分析結果を得るものです。 


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

# これらはあなたのMicrosoft Foundryプロジェクトの「概要」ページから取得してください
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## 学びはここで終わらない、旅を続けよう

このレッスンが終わったら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)でジェネレーティブAIの知識をさらにレベルアップしましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->