<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:53:07+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ja"
}
-->
# Mistralモデルでの構築

## はじめに

このレッスンでは以下をカバーします:
- さまざまなMistralモデルの探索
- 各モデルのユースケースとシナリオの理解
- 各モデルのユニークな特徴を示すコードサンプル

## Mistralモデル

このレッスンでは、3つの異なるMistralモデルを探ります: **Mistral Large**、**Mistral Small**、**Mistral Nemo**。

これらのモデルはすべてGithub Modelマーケットプレイスで無料で利用可能です。このノートブックのコードはこれらのモデルを使用してコードを実行します。Github Modelsを使用してAIモデルで[プロトタイプを作成する](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)方法についての詳細はこちらです。

## Mistral Large 2 (2407)

Mistral Large 2は現在Mistralのフラッグシップモデルで、企業向けに設計されています。

このモデルは、元のMistral Largeをアップグレードし、以下を提供します:
- より大きなコンテキストウィンドウ - 128k vs 32k
- 数学とコーディングタスクでのより良いパフォーマンス - 平均精度76.9% vs 60.4%
- 多言語でのパフォーマンス向上 - 対応言語には英語、フランス語、ドイツ語、スペイン語、イタリア語、ポルトガル語、オランダ語、ロシア語、中国語、日本語、韓国語、アラビア語、ヒンディー語が含まれます。

これらの特徴により、Mistral Largeは以下に優れています:
- *情報検索を強化した生成 (RAG)* - より大きなコンテキストウィンドウによる
- *関数呼び出し* - このモデルはネイティブの関数呼び出しを持ち、外部ツールやAPIとの統合を可能にします。これらの呼び出しは並行して、または順次に行うことができます。
- *コード生成* - このモデルはPython、Java、TypeScript、C++の生成に優れています。

### Mistral Large 2を使用したRAGの例

この例では、Mistral Large 2を使用してテキストドキュメントにRAGパターンを実行します。質問は韓国語で書かれており、著者の大学入学前の活動について尋ねています。

Cohere Embeddings Modelを使用して、テキストドキュメントと質問の埋め込みを作成します。このサンプルでは、faiss Pythonパッケージをベクトルストアとして使用します。

Mistralモデルに送信されるプロンプトには、質問と質問に類似した取得されたチャンクの両方が含まれています。モデルは自然言語での応答を提供します。

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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

Mistral Smallは、Mistralファミリーのモデルの中でプレミア/企業カテゴリに属するもう一つのモデルです。その名の通り、このモデルは小型言語モデル (SLM) です。Mistral Smallを使用する利点は以下の通りです:
- Mistral LargeやNeMoのようなMistral LLMと比較してコスト削減 - 価格が80%低下
- 低レイテンシー - MistralのLLMと比較してより速い応答
- 柔軟性 - 必要なリソースに対する制限が少なく、さまざまな環境で展開可能

Mistral Smallは以下に最適です:
- 要約、感情分析、翻訳などのテキストベースのタスク
- コスト効果が高いため頻繁にリクエストが行われるアプリケーション
- レビューやコードの提案のような低レイテンシーコードタスク

## Mistral SmallとMistral Largeの比較

Mistral SmallとLargeのレイテンシーの違いを示すために、以下のセルを実行してください。

同じプロンプトで応答時間の違いが3-5秒あることがわかるはずです。また、応答の長さとスタイルも注意してください。

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

このレッスンで取り上げた他の2つのモデルと比較して、Mistral NeMoはApache2ライセンスを持つ唯一の無料モデルです。

以前のMistralのオープンソースLLMであるMistral 7Bのアップグレードと見なされています。

NeMoモデルのその他の特徴は以下の通りです:

- *より効率的なトークン化:* このモデルは、より一般的に使用されるtiktokenではなくTekkenトークナイザーを使用します。これにより、より多くの言語やコードに対してより良いパフォーマンスが得られます。

- *微調整:* ベースモデルは微調整可能です。これにより、微調整が必要なユースケースに対する柔軟性が向上します。

- *ネイティブ関数呼び出し* - Mistral Largeのように、このモデルは関数呼び出しをトレーニングされています。これにより、最初のオープンソースモデルの一つとしてユニークです。

### トークナイザーの比較

このサンプルでは、Mistral NeMoがMistral Largeと比較してトークン化をどのように処理するかを見てみます。

両方のサンプルは同じプロンプトを取りますが、NeMoがMistral Largeよりも少ないトークンを返すことがわかるはずです。

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## 学習はここで終わりません、旅を続けましょう

このレッスンを完了した後、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに向上させましょう！

**免責事項**：
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。元の言語での原文が信頼できる情報源とみなされるべきです。重要な情報については、プロの人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。