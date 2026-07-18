# Mistralモデルを使った構築

## はじめに

このレッスンでは以下をカバーします：
- さまざまなMistralモデルの探索
- 各モデルのユースケースやシナリオの理解
- 各モデルの固有の特徴を示すコードサンプルの探索

## Mistralモデル

このレッスンでは、3つの異なるMistralモデルを探ります：
**Mistral Large**、**Mistral Small**、および **Mistral Nemo**。

これらのモデルはすべて [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) で無料で利用可能です。このノートブックのコードはこれらのモデルを使って実行します。

> **注意：** GitHub Modelsは2026年7月末で廃止されます。AIモデルのプロトタイピングに[Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst)を使う方法の詳細はこちらをご覧ください。


## Mistral Large 2 (2407)
Mistral Large 2は現在Mistralのフラッグシップモデルであり、企業向けに設計されています。

このモデルはオリジナルのMistral Largeのアップグレード版で以下の特徴があります：
- より大きなコンテキストウィンドウ - 32kから128kへ
- 数学やコーディングタスクでのパフォーマンス向上 - 平均精度76.9% 対 60.4%
- 多言語対応の向上 - 対応言語：英語、フランス語、ドイツ語、スペイン語、イタリア語、ポルトガル語、オランダ語、ロシア語、中国語、日本語、韓国語、アラビア語、ヒンディー語

これらの特徴により、Mistral Largeは以下に優れています：
- *Retrieval Augmented Generation (RAG)* - より大きなコンテキストウィンドウのため
- <em>関数呼び出し</em> - このモデルはネイティブの関数呼び出しをサポートし、外部ツールやAPIとの統合が可能です。これらの呼び出しは並列または順次行うことができます。
- <em>コード生成</em> - Python、Java、TypeScript、C++の生成に優れています。

### Mistral Large 2を使ったRAGの例

この例では、Mistral Large 2を使ってテキストドキュメントに対してRAGパターンを実行します。質問は韓国語で書かれ、「大学前の著者の活動」について尋ねています。

Cohere Embeddingsモデルを使ってテキストドキュメントと質問の埋め込みを作成しています。このサンプルでは、faiss Pythonパッケージをベクトルストアとして使用しています。

Mistralモデルに送られるプロンプトには質問と、質問に類似した取得済みチャンクの両方が含まれています。モデルはそれらをもとに自然言語で応答を生成します。

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

# これらはMicrosoft Foundryプロジェクトの「概要」ページから取得します
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
Mistral SmallはMistralファミリーの中でもプレミアム／エンタープライズカテゴリーに属する別のモデルです。名前が示す通り、小型の言語モデル（SLM）です。Mistral Smallを使う利点は：
- Mistral LargeやNeMoのようなMistralの大規模言語モデルに比べてコスト削減 - 価格が約80%ダウン
- 低遅延 - Mistralの大規模言語モデルより高速な応答
- 柔軟性 - 必要なリソースの制限が少なく、異なる環境に展開可能


Mistral Smallは以下に最適です：
- 要約、感情分析、翻訳といったテキストベースのタスク
- コスト効率の良さから頻繁にリクエストがあるアプリケーション
- レビューやコード提案など低遅延を要するコード関連タスク

## Mistral SmallとMistral Largeの比較

Mistral SmallとLargeの遅延差を示すため、以下のセルを実行してください。

応答時間に3〜5秒の差が見られるはずです。同じプロンプトに対する応答の長さやスタイルの違いにも注目してください。

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

このレッスンで紹介した他の2つのモデルに比べ、Mistral NeMoは唯一Apache2ライセンスの無料モデルです。

以前のオープンソースLLMであるMistral 7Bのアップグレード版と見なされています。

NeMoモデルのその他の特徴は：

- <em>より効率的なトークナイゼーション</em>：このモデルはより一般的なtiktokenではなくTekkenトークナイザーを使用しています。これにより、より多くの言語やコードでの性能が向上します。

- <em>ファインチューニング</em>：ベースモデルはファインチューニング可能です。これにより、ファインチューニングが必要なユースケースへの柔軟性が高まります。

- <em>ネイティブ関数呼び出し</em> - Mistral Largeと同様にこのモデルは関数呼び出しのトレーニングがされています。これはオープンソースモデルとしては初期の例のひとつとしてユニークです。


### トークナイザーの比較

このサンプルでは、Mistral NeMoがMistral Largeと比べてどのようにトークナイゼーションを処理するかを見ていきます。

両方のサンプルは同じプロンプトを使用しますが、NeMoはMistral Largeよりも少ないトークン数を返すことが分かるはずです。

```bash
pip install mistral-common
```

```python 
# 必要なパッケージをインポートする：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistralトークナイザーを読み込む

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

# トークンの数を数える
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

# Mistralトークナイザーを読み込みます

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# メッセージのリストをトークナイズします
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

## 学習はここで終わりません、旅を続けましょう

このレッスンを終えたら、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をチェックして、ジェネレーティブAIの知識をさらに深めましょう！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->