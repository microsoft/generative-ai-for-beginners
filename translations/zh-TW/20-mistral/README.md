# 使用 Mistral 模型進行構建

## 簡介

本課程將涵蓋：  
- 探索不同的 Mistral 模型  
- 了解每個模型的使用案例與場景  
- 探索展示每個模型獨特功能的程式碼範例。

## Mistral 模型

在本課程中，我們將探索 3 個不同的 Mistral 模型：  
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

這些模型均免費提供於 GitHub Model 市場中。本筆記本中的程式碼將使用這些模型來執行。關於如何使用 GitHub Models [進行 AI 模型原型設計](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多詳情，請參閱該連結。

## Mistral Large 2 (2407)  
Mistral Large 2 目前是 Mistral 的旗艦模型，專為企業級使用設計。

該模型是原始 Mistral Large 的升級版，提供  
- 更大的上下文窗口 — 128k 對比 32k  
- 在數學與程式編碼任務上的更佳表現 — 平均準確度 76.9% 對比 60.4%  
- 增強的多語言性能 — 支援語言包括：英文、法文、德文、西班牙文、義大利文、葡萄牙文、荷蘭文、俄文、中文、日文、韓文、阿拉伯文與印地語。

有了這些功能，Mistral Large 在以下方面表現優異  
- *檢索增強生成 (RAG)* — 得益於更大的上下文窗口  
- *函數呼叫* — 此模型具有原生函數呼叫能力，允許與外部工具及 API 整合。這些呼叫可平行執行，或以序列順序依次進行。  
- *程式碼生成* — 在 Python、Java、TypeScript 及 C++ 的生成方面表現出色。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 針對文字文件執行 RAG 模式。問題以韓文書寫，詢問作者大學前的活動。

它使用 Cohere Embeddings 模型來建立文字文件與問題的嵌入向量。範例中使用 faiss Python 套件作為向量庫。

送至 Mistral 模型的提示中包含問題與與問題相似的檢索段落。模型隨後提供自然語言回應。

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
Mistral Small 是 Mistral 家族中屬於頂級／企業類別的另一款模型。如其名所示，此模型為小型語言模型 (SLM)。使用 Mistral Small 的優勢包括：  
- 相較於 Mistral 大型 LLM（如 Mistral Large 與 NeMo）的成本節省 — 價格降低 80%  
- 低延遲 — 相較 Mistral 的大型 LLM 有更快的反應速度  
- 靈活性高 — 可於不同環境中部署，對所需資源限制較少。

Mistral Small 很適合：  
- 文字相關任務，如摘要、情感分析和翻譯。  
- 由於成本效益高，適用於頻繁請求的應用場景  
- 低延遲程式碼相關任務，如程式碼審查和建議。

## 比較 Mistral Small 與 Mistral Large

為展示 Mistral Small 與 Large 延遲的差異，請執行以下儲存格。

您會看到約 3-5 秒的反應時間差異。且請注意同一提示在回應長度與風格上也有所不同。

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

與本課程中討論的其他兩個模型相比，Mistral NeMo 是唯一擁有 Apache2 授權的免費模型。

它被視為早期 Mistral 開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點包括：

- *更高效的分詞器：* 此模型使用 Tekken 分詞器，取代較常用的 tiktoken。這提升了對多種語言與程式碼的表現。

- *微調能力：* 基底模型可用於微調。這讓其在需要微調的使用案例中具備更大靈活度。

- *原生函數呼叫* — 類似 Mistral Large，此模型經過函數呼叫訓練。這使其成為首批具備此功能的開源模型之一。

### 分詞器比較

在本範例中，我們將觀察 Mistral NeMo 相較於 Mistral Large 的分詞處理。

兩個範例均使用相同的提示，但您會發現 NeMo 返回的 token 數量少於 Mistral Large。

```bash
pip install mistral-common
```
  
```python 
# 匯入所需的套件：
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

# 計算標記數量
print(len(tokens))
```
  
```python
# 匯入所需的套件：
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

# 計算標記數量
print(len(tokens))
```
  
## 學習不止於此，繼續前進之旅

完成本課程後，請參考我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用本翻譯所引起的任何誤解或誤釋不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->