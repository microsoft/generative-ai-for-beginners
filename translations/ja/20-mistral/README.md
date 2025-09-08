<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:57:20+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ja"
}
-->
# Mistralモデルでの構築

## はじめに

このレッスンでは以下を扱います：
- さまざまなMistralモデルの紹介
- 各モデルのユースケースや適用シナリオの理解
- 各モデルの特徴を示すコードサンプル

## Mistralモデルについて

このレッスンでは、3つの異なるMistralモデルを紹介します：
**Mistral Large**、**Mistral Small**、そして**Mistral Nemo**です。

これらのモデルはすべてGithub Modelマーケットプレイスで無料で利用可能です。このノートブックのコードはこれらのモデルを使って実行されます。Github Modelsを使った[AIモデルのプロトタイピング](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)についての詳細もご覧ください。

## Mistral Large 2 (2407)
Mistral Large 2は現在Mistralのフラッグシップモデルで、企業向けに設計されています。

このモデルは元のMistral Largeのアップグレード版で、以下の特徴があります：
- より大きなコンテキストウィンドウ - 128k 対 32k
- 数学やコーディングタスクでの性能向上 - 平均正答率76.9% 対 60.4%
- 多言語対応の強化 - 対応言語は英語、フランス語、ドイツ語、スペイン語、イタリア語、ポルトガル語、オランダ語、ロシア語、中国語、日本語、韓国語、アラビア語、ヒンディー語

これらの特徴により、Mistral Largeは以下の分野で優れています：
- *Retrieval Augmented Generation (RAG)* - 大きなコンテキストウィンドウが活かされます
- *Function Calling* - ネイティブの関数呼び出し機能を持ち、外部ツールやAPIとの統合が可能です。これらの呼び出しは並列または順次に実行できます。
- *コード生成* - Python、Java、TypeScript、C++のコード生成に優れています。

### Mistral Large 2を使ったRAGの例

この例では、Mistral Large 2を使ってテキストドキュメントに対してRAGパターンを実行します。質問は韓国語で書かれており、著者の大学入学前の活動について尋ねています。

Cohere Embeddings Modelを使ってテキストドキュメントと質問の埋め込みを作成しています。このサンプルではfaissのPythonパッケージをベクトルストアとして使用しています。

Mistralモデルに送られるプロンプトには、質問と質問に類似した取得済みのチャンクが含まれています。モデルはそれに基づいて自然言語で回答を返します。

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
Mistral SmallはMistralファミリーの中でプレミアム／エンタープライズカテゴリに属するもう一つのモデルです。名前の通り、小型の言語モデル（SLM）です。Mistral Smallを使う利点は以下の通りです：
- Mistral LargeやNeMoなどのMistralのLLMに比べてコスト削減が可能 - 価格は約80%ダウン
- 低レイテンシー - MistralのLLMよりも高速な応答
- 柔軟性 - 必要なリソースの制約が少なく、さまざまな環境に展開可能

Mistral Smallは以下の用途に最適です：
- 要約、感情分析、翻訳などのテキストベースのタスク
- 頻繁にリクエストが発生するアプリケーションにおいてコスト効率が良い
- レビューやコード提案などの低レイテンシーが求められるコード関連タスク

## Mistral SmallとMistral Largeの比較

Mistral SmallとLargeのレイテンシーの違いを示すために、以下のセルを実行してください。

同じプロンプトに対して3〜5秒の応答時間の差が見られるはずです。また、応答の長さやスタイルの違いにも注目してください。

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

このレッスンで紹介した他の2つのモデルと比べて、Mistral NeMoは唯一Apache2ライセンスの無料モデルです。

Mistralの以前のオープンソースLLMであるMistral 7Bのアップグレード版と見なされています。

NeMoモデルのその他の特徴は以下の通りです：

- *より効率的なトークナイゼーション*：このモデルは一般的に使われるtiktokenではなくTekkenトークナイザーを使用しています。これにより、より多くの言語やコードでの性能が向上しています。

- *ファインチューニング*：ベースモデルはファインチューニング可能で、ファインチューニングが必要なユースケースに柔軟に対応できます。

- *ネイティブ関数呼び出し* - Mistral Largeと同様に、このモデルは関数呼び出しのトレーニングを受けています。これにより、オープンソースモデルとしては初期の段階でこの機能を持つユニークな存在となっています。

### トークナイザーの比較

このサンプルでは、Mistral NeMoがMistral Largeと比べてどのようにトークナイゼーションを処理するかを見ていきます。

両方のサンプルは同じプロンプトを使いますが、NeMoの方が返すトークン数が少ないことがわかるはずです。

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

## 学びはここで終わらない、旅を続けよう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めていきましょう！

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。