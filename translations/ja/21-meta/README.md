<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:27:46+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ja"
}
-->
# メタファミリーモデルでの構築

## はじめに

このレッスンでは以下を取り上げます：

- メタファミリーモデルの主な2つ - Llama 3.1とLlama 3.2を探索
- 各モデルの使用例とシナリオの理解
- 各モデルの特徴を示すコードサンプル

## メタファミリーモデル

このレッスンでは、メタファミリーまたは「Llama Herd」から2つのモデル - Llama 3.1とLlama 3.2を探索します。

これらのモデルは異なるバリエーションがあり、GitHub Modelマーケットプレイスで利用可能です。GitHub Modelsを使用して[AIモデルでプロトタイプを作成](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)する方法についての詳細はこちらです。

モデルバリエーション：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注: Llama 3もGitHub Modelsで利用可能ですが、このレッスンでは取り上げません*

## Llama 3.1

4050億のパラメータを持つLlama 3.1は、オープンソースのLLMカテゴリに属します。

このモデルは、以前のリリースであるLlama 3をアップグレードし、以下を提供します：

- より大きなコンテキストウィンドウ - 128kトークン対8kトークン
- より大きな最大出力トークン - 4096対2048
- マルチリンガルサポートの向上 - トレーニングトークンの増加による

これにより、Llama 3.1はGenAIアプリケーションを構築する際により複雑なユースケースを扱うことができ、以下を含みます：
- ネイティブ関数呼び出し - LLMワークフロー外の外部ツールや関数を呼び出す能力
- RAGパフォーマンスの向上 - より大きなコンテキストウィンドウによる
- 合成データ生成 - 微調整などのタスクに効果的なデータを作成する能力

### ネイティブ関数呼び出し

Llama 3.1は、関数やツール呼び出しをより効果的に行うように微調整されています。また、モデルがユーザーからのプロンプトに基づいて使用する必要があると識別できる2つの組み込みツールがあります。これらのツールは：

- **Brave Search** - Web検索を行うことで天気などの最新情報を取得できます。
- **Wolfram Alpha** - より複雑な数学的計算に使用できるため、自分で関数を書く必要はありません。

また、LLMが呼び出せる独自のカスタムツールを作成することもできます。

以下のコード例では：

- システムプロンプトで利用可能なツール（brave_search、wolfram_alpha）を定義します。
- 特定の都市の天気について尋ねるユーザープロンプトを送信します。
- LLMはBrave Searchツールへのツール呼び出しで応答し、`<|python_tag|>brave_search.call(query="Stockholm weather")`のように見えます。

*注: この例ではツール呼び出しのみを行います。結果を取得したい場合は、Brave APIページで無料アカウントを作成し、関数自体を定義する必要があります。*

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

LLMであるにもかかわらず、Llama 3.1にはマルチモーダル性という制限があります。つまり、画像などの異なるタイプの入力をプロンプトとして使用し、応答を提供する能力です。この能力はLlama 3.2の主な特徴の一つです。これらの特徴には以下も含まれます：

- マルチモーダル性 - テキストと画像のプロンプトを評価する能力があります。
- 小から中サイズのバリエーション（11Bと90B） - 柔軟なデプロイメントオプションを提供します。
- テキストのみのバリエーション（1Bと3B） - モデルをエッジ/モバイルデバイスにデプロイし、低レイテンシーを提供します。

マルチモーダルサポートは、オープンソースモデルの世界で大きな進歩を表しています。以下のコード例では、画像とテキストプロンプトの両方を使用してLlama 3.2 90Bから画像の分析を取得します。

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

## 学びはここで終わりません、旅を続けましょう

このレッスンを完了した後、[Generative AI Learningコレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、Generative AIの知識をさらに向上させましょう！

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。元の言語での原文が信頼できる情報源とみなされるべきです。重要な情報については、プロの人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解については責任を負いません。