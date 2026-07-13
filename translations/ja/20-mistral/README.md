# Mistralモデルでの構築

## はじめに

このレッスンでは以下について説明します:
- 異なるMistralモデルの探索
- 各モデルのユースケースやシナリオの理解
- 各モデルの特徴を示すコードサンプルの探索

## Mistralモデルについて

本レッスンでは、3つの異なるMistralモデルを探ります:
**Mistral Large**、**Mistral Small**、そして **Mistral Nemo** です。

これらのモデルはすべて [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) で無料で利用可能です。このノートブックのコードはこれらのモデルを使って実行されます。

> **注意:** GitHub Modelsは2026年7月末に廃止予定です。AIモデルのプロトタイピングに[Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst)を使う詳細はこちらをご覧ください。


## Mistral Large 2 (2407)
Mistral Large 2は現在Mistralの主力モデルであり企業利用を想定しています。

このモデルはオリジナルのMistral Largeのアップグレード版であり、
- より大きなコンテキストウィンドウ - 128k 対 32k
- 数学およびコーディングタスクの性能向上 - 76.9%の平均正答率 対 60.4%
- 多言語性能の向上 - 対応言語は英語、フランス語、ドイツ語、スペイン語、イタリア語、ポルトガル語、オランダ語、ロシア語、中国語、日本語、韓国語、アラビア語、ヒンディー語

これらの特徴により、Mistral Largeは以下の点で優れています:
- *Retrieval Augmented Generation (RAG)* - 大きなコンテキストウィンドウによる強化
- *Function Calling* - 外部ツールやAPIと統合可能なネイティブ関数呼び出しを搭載。これらの呼び出しは並列または逐次的に行えます。
- <em>コード生成</em> - Python、Java、TypeScript、C++の生成で優秀です。

### Mistral Large 2を使ったRAGの例

この例では、Mistral Large 2を用いてテキストドキュメントに対してRAGパターンを実行します。質問は韓国語で書かれており、著者の大学入学前の活動について尋ねています。

Cohere Embeddings Modelを使ってテキストドキュメントおよび質問の埋め込みを作成しています。このサンプルではfaiss Pythonパッケージをベクターストアに使用しています。

Mistralモデルに送られるプロンプトには質問と質問に似た検索済みチャンクの両方が含まれており、モデルは自然言語で応答を返します。

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

# Microsoft Foundry プロジェクトの「概要」ページからこれらを取得してください
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # 距離、インデックス
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small
Mistral SmallはMistralファミリーのプレミアム／エンタープライズカテゴリーに属する別のモデルです。名前が示す通り、小型の言語モデル（SLM）です。Mistral Smallを使うメリットは以下の通りです:
- Mistral LargeやNeMoなど他のMistralのLLMに比べコスト節約 - 80%の価格低下
- 低レイテンシー - MistralのLLMより高速な応答
- 柔軟性 - 必要なリソースの制約が少なく様々な環境に展開可能


Mistral Smallは以下に最適です:
- 要約、感情分析、翻訳などのテキストベースのタスク
- コスト効果が高いため、頻繁なリクエストがあるアプリケーション
- レビューやコード提案などの低レイテンシーなコードタスク

## Mistral SmallとMistral Largeの比較

Mistral SmallとLarge間のレイテンシーの違いを示すため、以下のセルを実行してください。

3〜5秒の応答時間の差が見られるはずです。 また、同じプロンプトでも応答の長さやスタイルの違いに注目してください。

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

今回のレッスンで扱う他の2つのモデルと比較して、Mistral NeMoは唯一のApache2ライセンスの無料モデルです。

これはMistralの以前のオープンソースLLM、Mistral 7Bのアップグレード版とみなされています。

NeMoモデルのその他の特徴は以下の通りです:

- *より効率的なトークナイゼーション:* このモデルはより一般的に使われるtiktokenではなくTekkenトークナイザーを使っています。これにより、より多くの言語やコードに対して優れた性能を発揮します。

- *ファインチューニング:* ベースモデルはファインチューニング可能で、必要に応じて利用ケースに合わせた調整が可能です。

- <em>ネイティブ関数呼び出し</em> - Mistral Largeと同様に、このモデルは関数呼び出しのトレーニングを受けています。これにより、最初期のオープンソースモデルの一つとして独特の存在となっています。


### トークナイザーの比較

このサンプルでは、Mistral NeMoがMistral Largeと比較してトークナイゼーションをどのように処理するかを見ていきます。

両方のサンプルは同じプロンプトを使用していますが、NeMoのほうがMistral Largeよりトークン数が少ないことが分かるはずです。

```bash
pip install mistral-common
```

```python 
# 必要なパッケージをインポートします：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistralトークナイザーをロードします

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# メッセージのリストをトークン化します
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# トークンの数をカウントします
print(len(tokens))
```

```python
# 必要なパッケージをインポートします：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistralのトークナイザーを読み込みます

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# メッセージのリストをトークン化します
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# トークンの数を数えます
print(len(tokens))
```

## 学びはここで終わりません、旅を続けましょう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めてください！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->