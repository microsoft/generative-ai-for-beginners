# Mistral モデルでの構築

## はじめに

このレッスンでは以下を取り扱います：
- Mistral のさまざまなモデルの探求
- 各モデルの使用例やシナリオの理解
- 各モデルの特徴を示すコードサンプルの紹介

## Mistral モデル

このレッスンでは、3つの異なる Mistral モデルを探究します：
**Mistral Large**、**Mistral Small**、そして **Mistral Nemo**。

これらのモデルはすべて GitHub Model マーケットプレイスで無料で利用可能です。このノートブック内のコードはこれらのモデルを使って実行されます。GitHub モデルを使って[AIモデルでプロトタイピングする方法](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)についての詳細はこちらをご覧ください。

## Mistral Large 2 (2407)
Mistral Large 2 は現在、Mistral のフラッグシップモデルであり、エンタープライズ用途向けに設計されています。

このモデルは、オリジナルの Mistral Large のアップグレード版で、以下の点が強化されています：
- より大きなコンテキストウィンドウ - 128k 対 32k
- 数学やコーディングタスクでのパフォーマンス向上 - 平均精度 76.9% 対 60.4%
- 多言語性能の向上 - 対応言語は英語、フランス語、ドイツ語、スペイン語、イタリア語、ポルトガル語、オランダ語、ロシア語、中国語、日本語、韓国語、アラビア語、ヒンディー語を含みます。

これらの特長により、Mistral Large は以下に優れています：
- *検索強化型生成 (RAG)* - より大きなコンテキストウィンドウによる
- *関数呼び出し* - このモデルはネイティブの関数呼び出しをサポートし、外部ツールやAPIとの統合を可能にします。これらの呼び出しは並列または順次に行うことができます。
- *コード生成* - Python、Java、TypeScript、C++ の生成に優れています。

### Mistral Large 2 を使った RAG の例

この例では、テキストドキュメントに対して RAG パターンを実行するために Mistral Large 2 を使用しています。質問は韓国語で書かれており、著者が大学入学前にどのような活動をしていたかを尋ねています。

Cohere Embeddings モデルを使用してテキストドキュメントと質問の埋め込みを作成します。このサンプルでは faiss Python パッケージをベクトルストアとして使用しています。

Mistral モデルに送られるプロンプトには、質問と質問に類似した取得済みチャンクの両方が含まれています。モデルはそれに基づき自然言語で回答を提供します。

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
Mistral Small は Mistral ファミリーのプレミア／エンタープライズカテゴリに属するもう一つのモデルです。名前が示す通り、このモデルは小型言語モデル（SLM）です。Mistral Small を使う利点は以下の通りです：
- Mistral Large や NeMo といった Mistral の LLM と比べてコスト削減 - 80%の価格低減
- 低遅延 - Mistral の LLM と比べて応答が速い
- 柔軟性 - 必要なリソースに関する制限が少なく、さまざまな環境で展開可能

Mistral Small は以下の用途に適しています：
- 要約、感情分析、翻訳などのテキストベースのタスク
- コスト効率が高いため頻繁なリクエストがあるアプリケーション
- レビューやコード提案など低遅延が求められるコード系タスク

## Mistral Small と Mistral Large の比較

Mistral Small と Large の遅延差を示すために、以下のセルを実行してください。

同じプロンプトで応答時間に3-5秒の差が出るはずです。また応答の長さやスタイルの違いにも注目してください。

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

このレッスンで解説した他の2つのモデルと比較して、Mistral NeMo は唯一 Apache2 ライセンスで提供されている無料モデルです。

以前のオープンソース LLM である Mistral 7B のアップグレード版と位置付けられています。

NeMo モデルのその他の特長は以下の通りです：

- *より効率的なトークナイゼーション*：このモデルはより一般的に使われている tiktoken ではなく Tekken トークナイザーを使用しています。これにより、より多くの言語やコードのパフォーマンスが向上します。

- *ファインチューニング*：ベースモデルはファインチューニング可能です。必要に応じてファインチューニングが求められる用途に柔軟に対応できます。

- *ネイティブ関数呼び出し* - Mistral Large と同様にこのモデルも関数呼び出しに対応するように訓練されています。これはオープンソースモデルとしては初期の特徴の一つです。

### トークナイザの比較

このサンプルでは、Mistral NeMo が Mistral Large と比べてトークナイゼーションをどのように処理するかを見ていきます。

どちらのサンプルも同じプロンプトを使用していますが、NeMo のほうがトークン数が少なく返されるはずです。

```bash
pip install mistral-common
```

```python 
# 必要なパッケージをインポートする:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral トークナイザーを読み込む

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# メッセージのリストをトークン化する
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

# トークンの数をカウントする
print(len(tokens))
```

```python
# 必要なパッケージをインポートします:
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

# トークンの数をカウントします
print(len(tokens))
```

## 学習はここで終わらない、旅を続けよう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をチェックして、生成AIの知識をさらに深めてください！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本ドキュメントはAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記述された原文を正式な情報源としてご参照ください。重要な情報については、専門の人間翻訳を推奨いたします。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねますのでご了承ください。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->