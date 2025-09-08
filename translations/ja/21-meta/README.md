<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:07:33+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ja"
}
-->
# Metaファミリーモデルでの構築

## はじめに

このレッスンでは以下を扱います：

- Metaファミリーの主要モデルであるLlama 3.1とLlama 3.2の紹介
- 各モデルのユースケースや適用シナリオの理解
- 各モデルの特徴を示すコードサンプル

## Metaファミリーモデルについて

このレッスンでは、Metaファミリー、別名「Llama Herd」から2つのモデル、Llama 3.1とLlama 3.2を紹介します。

これらのモデルは複数のバリエーションがあり、GitHub Modelマーケットプレイスで利用可能です。GitHub Modelsを使った[AIモデルのプロトタイピング](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)についての詳細はこちらをご覧ください。

モデルのバリエーション：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注：Llama 3もGitHub Modelsで利用可能ですが、本レッスンでは扱いません*

## Llama 3.1

4050億パラメータを持つLlama 3.1は、オープンソースの大規模言語モデル（LLM）に分類されます。

このモデルは、以前のLlama 3から以下の点でアップグレードされています：

- より大きなコンテキストウィンドウ - 8kトークンから128kトークンへ
- 最大出力トークン数の増加 - 2048から4096へ
- トレーニングトークンの増加による多言語対応の強化

これにより、Llama 3.1はより複雑なユースケースに対応可能となり、以下のようなGenAIアプリケーションの構築に役立ちます：
- ネイティブ関数呼び出し - LLMのワークフロー外の外部ツールや関数を呼び出す機能
- RAG（Retrieval-Augmented Generation）性能の向上 - 大きなコンテキストウィンドウによる
- 合成データ生成 - ファインチューニングなどのタスクに有効なデータを作成可能

### ネイティブ関数呼び出し

Llama 3.1は関数やツールの呼び出しをより効果的に行えるようにファインチューニングされています。また、ユーザーのプロンプトに基づいて使用が必要と判断される2つの組み込みツールを備えています。これらのツールは：

- **Brave Search** - ウェブ検索を行い、天気などの最新情報を取得可能
- **Wolfram Alpha** - 複雑な数学計算に利用でき、自作関数を書く必要がありません

さらに、LLMが呼び出せるカスタムツールを作成することも可能です。

以下のコード例では：

- システムプロンプト内で利用可能なツール（brave_search、wolfram_alpha）を定義しています。
- 特定の都市の天気について尋ねるユーザープロンプトを送信します。
- LLMはBrave Searchツールを呼び出す形で応答し、`<|python_tag|>brave_search.call(query="Stockholm weather")`のように表示されます。

*注：この例はツール呼び出しのみを示しており、結果を取得するにはBrave APIページで無料アカウントを作成し、関数自体を定義する必要があります。*

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

Llama 3.1はLLMであるものの、マルチモーダル対応（画像など異なる種類の入力をプロンプトとして使い、応答を返す能力）には制限があります。この点がLlama 3.2の主な特徴の一つです。その他の特徴は：

- マルチモーダリティ - テキストと画像の両方のプロンプトを評価可能
- 小〜中規模のバリエーション（11Bと90B） - 柔軟な展開オプションを提供
- テキストのみのバリエーション（1Bと3B） - エッジやモバイルデバイスでの展開が可能で低遅延を実現

このマルチモーダル対応はオープンソースモデルの世界における大きな進歩です。以下のコード例では、画像とテキストの両方のプロンプトを使い、Llama 3.2 90Bから画像の解析結果を得ています。

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

## 学びはここで終わらない、旅を続けよう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めましょう！

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。