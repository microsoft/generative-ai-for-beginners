# Mistralモデルを使ったビルディング

## はじめに

このレッスンでは以下をカバーします：
- さまざまなMistralモデルの探求
- 各モデルのユースケースとシナリオの理解
- 各モデルのユニークな機能を示すコードサンプル

## Mistralモデル

このレッスンでは、3つの異なるMistralモデルを探ります： **Mistral Large**、**Mistral Small**、そして**Mistral Nemo**。

これらのモデルはすべてGithub Modelマーケットプレイスで無料で利用可能です。このノートブックのコードでは、これらのモデルを使用してコードを実行します。Github Modelsを使用してAIモデルで[プロトタイプを作成する](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)方法についての詳細はこちらです。

## Mistral Large 2 (2407)

Mistral Large 2は現在Mistralのフラッグシップモデルで、エンタープライズ向けに設計されています。

このモデルは、オリジナルのMistral Largeを以下の点でアップグレードしています：
- より大きなコンテキストウィンドウ - 128k対32k
- 数学とコーディングタスクでのより良いパフォーマンス - 平均精度76.9%対60.4%
- 多言語パフォーマンスの向上 - 対応言語には、英語、フランス語、ドイツ語、スペイン語、イタリア語、ポルトガル語、オランダ語、ロシア語、中国語、日本語、韓国語、アラビア語、ヒンディー語が含まれます。

これらの機能により、Mistral Largeは以下で優れています：
- *Retrieval Augmented Generation (RAG)* - 大きなコンテキストウィンドウのおかげで
- *関数呼び出し* - このモデルはネイティブの関数呼び出しを備えており、外部ツールやAPIとの統合を可能にします。これらの呼び出しは、並行してまたは順次に行うことができます。
- *コード生成* - このモデルはPython、Java、TypeScript、C++の生成で優れています。

### Mistral Large 2を使用したRAGの例

この例では、Mistral Large 2を使用してテキストドキュメント上でRAGパターンを実行します。質問は韓国語で書かれており、大学入学前の著者の活動について尋ねています。

Cohere Embeddings Modelを使用してテキストドキュメントと質問の埋め込みを作成します。このサンプルでは、faiss Pythonパッケージをベクトルストアとして使用しています。

Mistralモデルに送信されるプロンプトには、質問と質問に類似した取得されたチャンクが含まれています。モデルは自然言語での応答を提供します。

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

Mistral Smallは、Mistralファミリーのモデルの中でプレミア/エンタープライズカテゴリーに属するもう一つのモデルです。名前が示すように、このモデルはSmall Language Model (SLM)です。Mistral Smallを使用する利点は以下の通りです：
- Mistral LargeやNeMoのようなMistral LLMと比較してコスト削減 - 価格が80%低下
- 低遅延 - MistralのLLMと比較して迅速な応答
- 柔軟性 - 必要なリソースに対する制限が少なく、さまざまな環境で展開可能

Mistral Smallは以下に最適です：
- 要約、感情分析、翻訳などのテキストベースのタスク
- コスト効果のために頻繁にリクエストが行われるアプリケーション
- レビューやコード提案のような低遅延のコードタスク

## Mistral SmallとMistral Largeの比較

Mistral SmallとLargeの間の遅延の違いを示すために、以下のセルを実行してください。

3〜5秒の応答時間の違いが見られるはずです。また、同じプロンプトに対する応答の長さとスタイルにも注目してください。

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

このレッスンで議論された他の2つのモデルと比較して、Mistral NeMoはApache2ライセンスを持つ唯一の無料モデルです。

これは、以前のオープンソースLLMであるMistral 7Bのアップグレードと見なされています。

NeMoモデルの他の特徴は以下の通りです：

- *より効率的なトークン化:* このモデルは、より一般的に使用されるtiktokenではなく、Tekkenトークナイザを使用しています。これにより、より多くの言語とコードでのパフォーマンスが向上します。

- *微調整:* ベースモデルは微調整が可能です。これにより、微調整が必要なユースケースに対してより柔軟に対応できます。

- *ネイティブ関数呼び出し* - Mistral Largeのように、このモデルは関数呼び出しで訓練されています。これにより、最初のオープンソースモデルの一つとしてユニークです。

### トークナイザの比較

このサンプルでは、Mistral NeMoがMistral Largeと比較してトークン化をどのように処理するかを見てみましょう。

両方のサンプルは同じプロンプトを取りますが、NeMoがMistral Largeに比べて少ないトークンを返すことがわかるはずです。

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

## 学びはここで終わりではありません、旅を続けましょう

このレッスンを完了した後は、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、Generative AIの知識をさらに向上させましょう！

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があります。原文はその言語で書かれた文書を権威ある情報源として考慮してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。