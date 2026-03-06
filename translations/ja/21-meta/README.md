# Metaファミリーモデルでの構築

## はじめに

このレッスンで学ぶ内容:

- 主要な2つのMetaファミリーモデル - Llama 3.1 と Llama 3.2 の探索
- 各モデルのユースケースとシナリオの理解
- 各モデルの独自機能を示すコードサンプル

## Metaファミリーモデルについて

このレッスンでは、Metaファミリーまたは「Llama Herd」から2つのモデル、Llama 3.1 と Llama 3.2 を探ります。

これらのモデルは異なるバリアントで提供され、GitHubモデルマーケットプレイスで入手可能です。GitHub Modelsを使って[AIモデルでプロトタイピングする方法](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)の詳細はこちらです。

モデルバリアント:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct

*注意: Llama 3もGitHub Modelsで利用可能ですが、本レッスンでは扱いません*

## Llama 3.1

4050億パラメータを持つLlama 3.1は、オープンソースのLLMカテゴリに属します。

このモデルは初期リリースのLlama 3をアップグレードし、以下を提供します:

- より大きなコンテキストウィンドウ - 8kトークンから128kトークンへ
- より大きな最大出力トークン - 2048から4096へ
- 向上した多言語対応 - トレーニングトークン数の増加により

これにより、Llama 3.1はGenAIアプリケーション構築時により複雑なユースケースを扱うことが可能になります。例えば:  
- ネイティブ関数呼び出し - LLMワークフロー外の外部ツールや関数を呼び出す能力  
- より良いRAGパフォーマンス - より大きなコンテキストウィンドウによる  
- 合成データ生成 - 微調整のための効果的なデータ作成能力  

### ネイティブ関数呼び出し

Llama 3.1は関数やツール呼び出しをより効果的に行えるようにファインチューニングされています。また、モデルはユーザープロンプトに基づいて使用する必要のある2つの組み込みツールを識別できます。

これらのツールは:

- **Brave Search** - ウェブ検索を行い、天気などの最新情報を取得可能  
- **Wolfram Alpha** - 複雑な数学計算に利用できるため、自作関数は不要  

独自のカスタムツールも作成してLLMが呼び出せるようにできます。

以下のコード例では:

- システムプロンプト内に利用可能なツール（brave_search、wolfram_alpha）を定義します。  
- ある都市の天気を尋ねるユーザープロンプトを送信します。  
- LLMはBrave Searchツールへの呼び出しを `<|python_tag|>brave_search.call(query="Stockholm weather")` のように返します。

*注意: この例はツール呼び出しのみ行い、結果を取得したい場合はBrave APIページで無料アカウントを作成し、関数自体を定義する必要があります。*

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

LLMであるにもかかわらず、Llama 3.1の制約の一つはマルチモーダリティがないこと、つまり画像など異なるタイプの入力をプロンプトとして使い、応答を生成できない点です。この機能がLlama 3.2の主要な特徴の一つです。その他の特徴は:

- マルチモーダリティ - テキストと画像プロンプトの両方を評価可能  
- 小〜中サイズのバリエーション（11B と 90B） - 柔軟なデプロイオプションを提供  
- テキストのみのバリエーション（1B と 3B） - エッジ / モバイルデバイスでのデプロイが可能で低レイテンシを実現  

このマルチモーダルサポートはオープンソースモデルの世界における大きな進歩を示します。以下のコード例では、画像とテキストの両方のプロンプトを取り、Llama 3.2 90Bから画像の分析を得ます。

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

このレッスンを修了したら、ぜひ[Generative AI Learningコレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらにレベルアップしましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の翻訳者による人力翻訳を推奨します。本翻訳の利用に起因するいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->