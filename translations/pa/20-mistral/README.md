# ਮਿਸਟ੍ਰਲ ਮੋਡਲਾਂ ਨਾਲ ਬਿਲਡਿੰਗ

## ਜਾਣਪਛਾਣ

ਇਸ ਪਾਠ ਵਿੱਚ ਇਹ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:
- ਵੱਖ-ਵੱਖ ਮਿਸਟ੍ਰਲ ਮੋਡਲਾਂ ਦੀ ਖੋਜ
- ਹਰ ਮੋਡਲ ਲਈ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਤੇ ਸਿਹਤਾਂ ਨੂੰ ਸਮਝਣਾ
- ਕੋਡ ਨਮੂਨੇ ਜੋ ਹਰ ਮੋਡਲ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ ਦੀ ਖੋਜ

## ਮਿਸਟ੍ਰਲ ਮੋਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ 3 ਵੱਖਰੇ ਮਿਸਟ੍ਰਲ ਮੋਡਲਾਂ ਦੀ ਖੋਜ ਕਰਾਂਗੇ:
**ਮਿਸਟ੍ਰਲ ਲਾਰਜ**, **ਮਿਸਟ੍ਰਲ ਸਮਾਲ** ਅਤੇ **ਮਿਸਟ੍ਰਲ ਨੇਮੋ**।

ਇਹਨਾਂ ਸਾਰਿਆਂ ਮੋਡਲਾਂ ਨੂੰ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਮੁਫ਼ਤ ਉਪਲਬਧ ਹੈ। ਇਸ ਨੋਟਬੁੱਕ ਦਾ ਕੋਡ ਇਨ੍ਹਾਂ ਮੋਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰੇਗਾ।

> **ਨੋਟ:** GitHub ਮੋਡਲ 2026 ਦੀ ਜੁਲਾਈ ਦੇ ਅੰਤ ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਰਹੇ ਹਨ। ਇੱਥੇ ਵਧੇਰੇ ਵਿਸਥਾਰ ਹਨ ਕਿ ਕਿਵੇਂ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ਦੀ ਵਰਤੋਂ ਕਰਕੇ AI ਮੋਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।


## ਮਿਸਟ੍ਰਲ ਲਾਰਜ 2 (2407)
ਮਿਸਟ੍ਰਲ ਲਾਰਜ 2 ਇਸ ਵਕਤ ਮਿਸਟ੍ਰਲ ਦਾ ਫਲੈਗਸ਼ਿਪ ਮੋਡਲ ਹੈ ਅਤੇ ਇਹ ਉਦਯੋਗੀ ਵਰਤੋਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ।

ਇਹ ਮੋਡਲ ਮੂਲ ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਦਾ ਅਪਗ੍ਰੇਡ ਹੈ ਜਿਸ ਵਿੱਚ ਦਿੱਤੇ ਗਏ ਹਨ:
- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਬਨਾਮ 32k
- ਗਣਿਤ ਅਤੇ ਕੋਡਿੰਗ ਟਾਸਕਾਂ ‘ਤੇ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ - 76.9% ਦਰਸਾਏ ਦਰ ਨਾਲ 60.4% ਦੇ ਬਨਾਮ
- ਬਹੁਭਾਸ਼ੀ ਪ੍ਰਦਰਸ਼ਨ ਵਿਚ ਵਾਧਾ - ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: ਅੰਗਰੇਜ਼ੀ, ਫ੍ਰੈਂਚ, ਜਰਮਨ, ਸਪੇਨੀ, ਇਟਾਲੀਅਨ, ਪੁਤਰਗਾਲੀ, ਡਚ, ਰੂਸੀ, ਚੀਨੀ, ਜਪਾਨੀ, ਕੋਰੀਆਈ, ਅਰਬੀ ਅਤੇ ਹਿੰਦੀ।

ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ, ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਖਾਸ ਹੈ:
- *ਰੀਟਰੀਵਲ ਅਗਮੇਂਟਡ ਜਨਰੇਸ਼ਨ (RAG)* - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਕਾਰਨ
- *ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - ਇਸ ਮੋਡਲ ਵਿੱਚ ਜਾਂਚਤ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਹੈ ਜੋ ਬਾਹਰੀ ਉਪਕਰਣਾਂ ਅਤੇ ਏਪੀਆਈਜ਼ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਕਾਲਾਂ ਸੇਂਕੜੇ ਵਿਚ ਜਾਂ ਲੜੀਵਾਰ ਕ੍ਰਮ ਵਿੱਚ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।
- *ਕੋਡ ਜਨਰੇਸ਼ਨ* - ਇਹ ਮੋਡਲ ਪਾਈਥਨ, ਜਾਵਾ, ਟਾਈਪਸਕ੍ਰਿਪਟ ਅਤੇ C++ ਜਨਰੇਸ਼ਨ ਵਿੱਚ ਬੇਤਰ ਹੈ।

### ਮਿਸਟ੍ਰਲ ਲਾਰਜ 2 ਨਾਲ RAG ਉਦਾਹਰਨ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਮਿਸਟ੍ਰਲ ਲਾਰਜ 2 ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਲੇਖ ਦਸਤਾਵੇਜ਼ ‘ਤੇ RAG ਪੈਟਰਨ ਚਲਾ ਰਹੇ ਹਾਂ। ਸਵਾਲ ਕੋਰੀਆਈ ਵਿੱਚ ਲਿਖਿਆ ਗਿਆ ਹੈ ਅਤੇ ਲੇਖਕ ਦੀ ਕਾਲਜ ਤੋਂ ਪਿੱਛੇ ਦੀਆਂ ਗਤੀਵਿਧੀਆਂ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ।

ਇਹ ਕੋਹੀਰ ਐਮਬੈਡਿੰਗ ਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜਿਸ ਨਾਲ ਲੇਖ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਸਵਾਲ ਦੋਹਾਂ ਦੇ ਐਮਬੈਡਿੰਗ ਬਣਾਏ ਜਾਂਦੇ ਹਨ। ਇਸ ਨਮੂਨੇ ਲਈ ਇਹ ਫੈਸ ਪਾਈਥਨ ਪੈਕੇਜ ਦੀ ਵਰਤੋਂ ਇੱਕ ਵੈਕਟਰ ਸਟੋਰ ਵਜੋਂ ਕਰਦਾ ਹੈ।

ਮਿਸਟ੍ਰਲ ਮੋਡਲ ਨੂੰ ਭੇਜਿਆ ਗਿਆ ਪ੍ਰੰਪਟ ਸਵਾਲਾਂ ਅਤੇ ਉਹ ਚੰਕ ਜੋ ਸਵਾਲ ਨਾਲ ਮਿਲਦੇ ਜੁਲਦੇ ਹਨ, ਦੋਹਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਮੋਡਲ ਫਿਰ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਵਾਬ ਪੇਸ਼ ਕਰਦਾ ਹੈ।

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

# ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਦੇ "ਸਮਾਰੀ" ਪੇਜ ਤੋਂ ਲਓ
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ਦੂਰੀ, ਇੰਡੈਕਸ
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

## ਮਿਸਟ੍ਰਲ ਸਮਾਲ
ਮਿਸਟ੍ਰਲ ਸਮਾਲ ਮਿਸਟ੍ਰਲ ਪਰਿਵਾਰ ਦਾ ਇੱਕ ਹੋਰ ਮੋਡਲ ਹੈ ਜੋ ਪ੍ਰੀਮੀਅਰ/ਉਦਯੋਗ ਵਰਗ ਵਿੱਚ ਆਉਂਦਾ ਹੈ। ਨਾਮ ਦੇ ਅਨੁਸਾਰ, ਇਹ ਮੋਡਲ ਇੱਕ ਛੋਟਾ ਭਾਸ਼ਾਈ ਮਾਡਲ (SLM) ਹੈ। ਮਿਸਟ੍ਰਲ ਸਮਾਲ ਦੀ ਵਰਤੋਂ ਦੇ ਫਾਇਦੇ ਹਨ:
- ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਅਤੇ ਨੇਮੋ ਵਾਂਗ LLMs ਨਾਲੋਂ ਲਾਗਤ ਬਚਤ - 80% ਕੀਮਤ ਘਟਣਾ
- ਘੱਟ ਲੇਟੈਂਸੀ - ਮਿਸਟ੍ਰਲ ਦੇ LLMs ਨਾਲੋਂ ਤੇਜ਼ ਜਵਾਬ
- ਲਚਕੀਲਾ - ਵੱਖ-ਵੱਖ ਮਾਹੋਲਾਂ ਵਿੱਚ ਕੰਮ ਕਰਨ ਯੋਗ ਬਿਨਾਂ ਜ਼ਿਆਦਾ ਸਰੋਤਾਂ ਦੀ ਲੋੜ ਦੇ


ਮਿਸਟ੍ਰਲ ਸਮਾਲ ਵਧੀਆ ਹੈ:
- ਸਮਰਾਈ, ਭਾਵਨਾਤਮਕ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਅਨੁਵਾਦ ਵਰਗੇ ਪਾਠ ਅਧਾਰਿਤ ਕਾਰਜਾਂ ਲਈ
- ਵਹੀਨੀ ਅਰਜ਼ੀਆਂ ਜਿੱਥੇ ਬਹੁਤ ਸਾਰੀਆਂ ਬੇਨਤੀਆਂ ਆਉਂਦੀਆਂ ਹਨ, ਇਸਦੀ ਲਾਗਤ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਕਾਰਨ
- ਘੱਟ ਲੇਟੈਂਸੀ ਕੋਡ ਕਾਰਜ ਜਿਵੇਂ ਸਮੀਖਿਆ ਅਤੇ ਕੋਡ ਸਿਫਾਰਸ਼ਾਂ ਲਈ

## ਮਿਸਟ੍ਰਲ ਸਮਾਲ ਅਤੇ ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਦਾ ਤੁਲਨਾ

ਮਿਸਟ੍ਰਲ ਸਮਾਲ ਅਤੇ ਲਾਰਜ ਵਿਚ ਲੇਟੈਂਸੀ ਵਿੱਚ ਫਰਕ ਦਿਖਾਉਣ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਸੈੱਲ ਚਲਾਓ।

ਤੁਹਾਨੂੰ ਜਵਾਬ ਦੇ ਸਮੇਂ ਵਿੱਚ 3-5 ਸਕਿੰਟ ਦਾ ਫਰਕ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ। ਨਾਲ ਹੀ ਇੱਕੋ ਪ੍ਰੰਪਟ 'ਤੇ ਜਵਾਬ ਦੀ ਲੰਬਾਈ ਅਤੇ ਅੰਦਾਜ਼ ਦਾ ਵੀ ਧਿਆਨ ਕਰੋ।

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

## ਮਿਸਟ੍ਰਲ ਨੇਮੋ

ਇਸ ਪਾਠ ਵਿੱਚ ਚਰਚਾ ਕੀਤੇ ਹੋਰ ਦੋ ਮੋਡਲਾਂ ਦੇ ਮੁਕਾਬਲੇ, ਮਿਸਟ੍ਰਲ ਨੇਮੋ ਇੱਕੋ ਮੁਫ਼ਤ ਮੋਡਲ ਹੈ ਜੋ ਅਪਾਚੇ2 ਲਾਇਸੈਂਸ ਵਾਲਾ ਹੈ।

ਇਹ ਮਿਸਟ੍ਰਲ ਦੀ ਪਹਿਲਾਂ ਦੀ ਖੁੱਲੀ ਸਰੋਤ LLM, ਮਿਸਟ੍ਰਲ 7B ਦਾ ਅਪਗ੍ਰੇਡ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ।

ਨੇਮੋ ਮੋਡਲ ਦੀਆਂ ਕੁਝ ਹੋਰ ਖਾਸੀਅਤਾਂ ਹਨ:

- *ਵੱਧ ਪ੍ਰਭਾਵਸ਼ੀਲ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ:* ਇਹ ਮੋਡਲ ਟੇਕਨ ਟੋਕਨਾਈਜ਼ਰ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਜ਼ਿਆਦਾ ਪ੍ਰਚਲਿਤ tiktoken ਦੇ ਨਾਲੋਂ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਦਿੰਦਾ ਹੈ। ਇਸ ਨਾਲ ਵਧੇਰੇ ਭਾਸ਼ਾਵਾਂ ਅਤੇ ਕੋਡ ਤੇ ਬਿਹਤਰ ਨਤੀਜੇ ਮਿਲਦੇ ਹਨ।

- *ਫਾਈਨਟਯੂਨਿੰਗ:* ਬੇਸ ਮੋਡਲ ਫਾਈਨਟਯੂਨਿੰਗ ਲਈ ਉਪਲਬਧ ਹੈ। ਇਸ ਨਾਲ ਉਹਨਾਂ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ ਜ਼ਿਆਦਾ ਲਚਕੀਲਾਪਨ ਮਿਲਦਾ ਹੈ ਜਿੱਥੇ ਫਾਈਨਟਯੂਨਿੰਗ ਦੀ ਲੋੜ ਪੈਂਦੀ ਹੈ।

- *ਨੇਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਵਾਂਗ, ਇਸ ਮੋਡਲ ਨੂੰ ਵੀ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਲਈ ਟਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਸਨੂੰ ਖੁੱਲੇ ਸਰੋਤ ਵਾਲੇ ਪਹਿਲੇ ਮੋਡਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਵੱਖਰਾ ਬਣਾਉਂਦਾ ਹੈ।


### ਟੋਕਨਾਈਜ਼ਰਾਂ ਦੀ ਤੁਲਨਾ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ, ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ ਮਿਸਟ੍ਰਲ ਨੇਮੋ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਕਿਸ ਤਰ੍ਹਾਂ ਸੰਭਾਲਦਾ ਹੈ ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਨਾਲ ਤੁਲਨਾ ਵਿਚ।

ਦੋਹਾਂ ਨਮੂਨੇ ਇੱਕੋ ਪ੍ਰੰਪਟ ਲੈਂਦੇ ਹਨ ਪਰ ਤੁਸੀਂ ਦੇਖੋਗੇ ਕਿ ਨੇਮੋ ਮਿਸਟ੍ਰਲ ਲਾਰਜ ਦੇ ਮੁਕਾਬਲੇ ਘੱਟ ਟੋਕਨ ਵਾਪਸ ਕਰਦਾ ਹੈ।

```bash
pip install mistral-common
```

```python 
# ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਆਯਾਤ ਕਰੋ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ਮਿਸਟਰਾਲ ਟੋਕਨਾਇਜ਼ਰ ਲੋਡ ਕਰੋ

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰੋ
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

# ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਕਰੋ
print(len(tokens))
```

```python
# ਲੋੜੀਂਦੇ ਪੈਕੇਜ ਇੰਪੋਰਟ ਕਰੋ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ਮਿਸਟਰਾਲ ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰੋ

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ ਨੂੰ ਟੋਕਨਾਈਜ਼ ਕਰੋ
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

# ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਕਰੋ
print(len(tokens))
```

## ਸਿੱਖਣਾ ਇੱਥੇ ਖ਼ਤਮ ਨਹੀਂ ਹੁੰਦਾ, ਸਫ਼ਰ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [ਜਰਨਰੇਟਿਵ AI ਲਰਨਿੰਗ ਕਲੇਕਸ਼ਨ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਦੇਖੋ ਅਤੇ ਆਪਣੀ ਜਰਨਰੇਟਿਵ AI ਗਿਆਨ ਨੂੰ ਵਧਾਉਣ ਜਾਰੀ ਰੱਖੋ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->