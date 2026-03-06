# 使用 Mistral 模型構建

## 介紹

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 理解每個模型的使用案例和場景
- 探索展示每個模型獨特功能的代碼範例。

## Mistral 模型

在本課程中，我們將探索 3 個不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

這些模型皆可在 GitHub Model 市場免費獲取。本筆記本中的代碼將使用這些模型來運行。以下是使用 GitHub 模型進行 [AI 模型原型設計](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多詳細說明。

## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗艦模型，設計用於企業用途。

該模型是原始 Mistral Large 的升級版，提供了
- 較大的上下文窗口 - 128k 對比 32k
- 在數學和編程任務上的更佳表現 - 平均準確率 76.9% 對比 60.4%
- 提升的多語言性能 - 支持語言包括：英語、法語、德語、西班牙語、意大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語和印地語。

憑藉這些功能，Mistral Large 在以下方面表現優異
- *檢索增強生成（RAG）* - 由於更大的上下文窗口
- *函數調用* - 該模型具備原生函數調用，允許與外部工具和 API 集成。這些調用可以並行執行，也可以按順序逐個執行。
- *代碼生成* - 此模型在 Python、Java、TypeScript 及 C++ 生成方面表現出色。

### 使用 Mistral Large 2 的 RAG 範例

在本例中，我們使用 Mistral Large 2 對文本文件執行 RAG 模式。問題用韓語書寫，詢問作者大學前的活動。

它使用 Cohere Embeddings 模型為文本文件和問題創建嵌入。在此範例中，使用 faiss Python 套件作為向量存儲。

發送給 Mistral 模型的提示包含問題以及與問題相似的檢索片段。模型隨後給出自然語言回答。

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # 距離，索引
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
Mistral Small 是 Mistral 家族中另一款屬於高級/企業類別的模型。顧名思義，此模型是一款小型語言模型（SLM）。使用 Mistral Small 的優點是：
- 相較於 Mistral 的大型語言模型（如 Mistral Large 和 NeMo）節省成本 - 價格下降 80%
- 低延遲 - 回應速度快於 Mistral 的大型語言模型
- 靈活性高 - 可在不同環境中部署，對所需資源的限制較少。

Mistral Small 非常適合：
- 基於文本的任務，如摘要、情感分析和翻譯。
- 由於成本效益高，適合頻繁請求的應用。
- 低延遲的代碼任務，如代碼審查和代碼建議。

## 比較 Mistral Small 與 Mistral Large

要展示 Mistral Small 和 Large 之間的延遲差異，請運行以下單元格。

您應該會看到相同提示下回應時間有 3-5 秒的差異，也請注意回應長度和風格的不同。

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

與本課程中討論的其他兩款模型相比，Mistral NeMo 是唯一擁有 Apache2 授權的免費模型。

它被視為 Mistral 先前開源大型語言模型 Mistral 7B 的升級版本。

NeMo 模型的其他特點包括：

- *更高效的標記化器（tokenization）：* 此模型使用 Tekken 標記化器，勝過更常用的 tiktoken。這使其在多語言和代碼處理上表現更佳。

- *微調功能（Finetuning）：* 基礎模型可供微調，這為需要微調的使用案例提供更多靈活性。

- *原生函數調用* - 與 Mistral Large 一樣，該模型已接受函數調用訓練。這使其成為首批具有此功能的開源模型之一。

### 標記化器比較

在本範例中，我們將比較 Mistral NeMo 和 Mistral Large 的標記化處理。

兩個範例均採用相同提示，但你應該會看到 NeMo 產生的標記數少於 Mistral Large。

```bash
pip install mistral-common
```

```python 
# 匯入所需套件：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 載入 Mistral 分詞器

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# 對訊息列表進行分詞
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

# 計算分詞數量
print(len(tokens))
```

```python
# 導入所需套件：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 載入 Mistral 分詞器

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 對訊息列表進行分詞
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

# 計算分詞數量
print(len(tokens))
```

## 學習不止於此，繼續前行

完成本課程後，請查看我們的 [生成式 AI 學習集錦](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件以其原語言版本為準。對於重要資訊，建議採用專業人工翻譯。我們不對使用本翻譯所引致的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->