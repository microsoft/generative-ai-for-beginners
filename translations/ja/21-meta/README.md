# Metaファミリーモデルでの構築

## はじめに

このレッスンでは以下を扱います：

- Metaファミリーの主要な2つのモデル - Llama 3.1とLlama 3.2 の探求
- 各モデルのユースケースとシナリオの理解
- 各モデルの独自機能を示すコードサンプル


## Metaファミリーのモデル

このレッスンでは、Metaファミリー、または「Llama Herd」から2つのモデル - Llama 3.1 と Llama 3.2 を探ります。

これらのモデルはさまざまなバリエーションがあり、[Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)で利用可能です。

> **注意:** GitHub Modelsは2026年7月末に終了します。AIモデルのプロトタイピングに [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) を使用する詳細はこちらをご覧ください。

モデルバリエーション：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注意：Llama 3もMicrosoft Foundry Modelsで利用可能ですが、本レッスンでは扱いません*

## Llama 3.1

4050億パラメータで、Llama 3.1はオープンソースLLMカテゴリに属します。

このモデルは以前のリリースであるLlama 3のアップグレード版であり、以下の特徴を提供します：

- より大きなコンテキストウィンドウ - 128kトークン対8kトークン
- より大きな最大出力トークン数 - 4096対2048
- より良い多言語対応 - トレーニングトークンの増加による

これにより、Llama 3.1はGenAIアプリケーション構築時により複雑なユースケースに対応可能になります。例えば：
- ネイティブ関数呼び出し - LLMワークフロー外の外部ツールや関数を呼び出す能力
- より良いRAGパフォーマンス - より大きなコンテキストウィンドウによる
- 合成データ生成 - ファインチューニングなどのタスクのための効果的なデータを作成する能力

### ネイティブ関数呼び出し

Llama 3.1は関数やツールの呼び出しをより効果的に行うようファインチューニングされています。また、ユーザーのプロンプトに基づいて使用が必要と判断される2つの組み込みツールがあります。これらのツールは：

- **Brave Search** - Web検索を行い、天気などの最新情報を取得可能
- **Wolfram Alpha** - より複雑な数学的計算に使用でき、自作関数を書く必要がありません

また、LLMが呼び出せる独自のカスタムツールも作成できます。

以下のコード例では：

- システムプロンプト内で利用可能なツール（brave_search, wolfram_alpha）を定義しています。
- ある都市の天気について問い合わせるユーザープロンプトを送信します。
- LLMはBrave Searchツールの呼び出しで応答し、 `<|python_tag|>brave_search.call(query="Stockholm weather")` のようになります。

*注意：この例はツール呼び出しのみを行います。結果を得るには、Brave APIページで無料アカウントを作成し、関数自体を定義する必要があります。

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# これらは Microsoft Foundry プロジェクトの「概要」ページから取得してください
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

Llama 3.1はLLMであるものの、多様な入力（画像など）をプロンプトとして使用し応答を返すことができないという制限があります。この機能はLlama 3.2の主な特徴のひとつです。他の特徴には以下が含まれます：

- マルチモーダリティ - テキストおよび画像の両方のプロンプトを評価可能
- 小規模から中規模のバリエーション（11Bと90B） - 柔軟な展開オプションを提供
- テキストのみバリエーション（1Bと3B） - エッジ/モバイルデバイスへの展開や低レイテンシを実現

マルチモーダルサポートはオープンソースモデルの世界で大きな進歩を示します。以下のコード例では、画像とテキストのプロンプトの両方を使用して、Llama 3.2 90Bによる画像の分析を行います。


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

# これらはMicrosoft Foundryプロジェクトの「概要」ページから取得します
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

## 学習はここで終わらない、旅を続けよう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらにレベルアップしましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->