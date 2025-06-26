<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:15:19+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "pa"
}
-->
# ਮਿਸਟਰਾਲ ਮਾਡਲ ਨਾਲ ਨਿਰਮਾਣ

## ਪਰੇਚਾ

ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:
- ਵੱਖ-ਵੱਖ ਮਿਸਟਰਾਲ ਮਾਡਲਾਂ ਦੀ ਖੋਜ
- ਹਰ ਮਾਡਲ ਲਈ ਉਪਯੋਗ ਕੇਸਾਂ ਅਤੇ ਦ੍ਰਿਸ਼ਾਂ ਦੀ ਸਮਝ
- ਕੋਡ ਨਮੂਨੇ ਜੋ ਹਰ ਮਾਡਲ ਦੀ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਂਦੇ ਹਨ।

## ਮਿਸਟਰਾਲ ਮਾਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ 3 ਵੱਖ-ਵੱਖ ਮਿਸਟਰਾਲ ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਕਰਾਂਗੇ: **ਮਿਸਟਰਾਲ ਲਾਰਜ**, **ਮਿਸਟਰਾਲ ਸਮਾਲ** ਅਤੇ **ਮਿਸਟਰਾਲ ਨੇਮੋ**।

ਇਹਨਾਂ ਵਿੱਚੋਂ ਹਰ ਮਾਡਲ Github ਮਾਡਲ ਮਾਰਕੀਟਪਲੇਸ 'ਤੇ ਮੁਫਤ ਉਪਲਬਧ ਹੈ। ਇਸ ਨੋਟਬੁੱਕ ਵਿੱਚ ਕੋਡ ਚਲਾਉਣ ਲਈ ਇਹ ਮਾਡਲ ਵਰਤੇ ਜਾਣਗੇ। ਇੱਥੇ Github ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਬਾਰੇ ਹੋਰ ਵੇਰਵੇ ਹਨ [AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ ਲਈ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)।

## ਮਿਸਟਰਾਲ ਲਾਰਜ 2 (2407)

ਮਿਸਟਰਾਲ ਲਾਰਜ 2 ਇਸ ਸਮੇਂ ਮਿਸਟਰਾਲ ਦਾ ਮੁੱਖ ਮਾਡਲ ਹੈ ਅਤੇ ਇਹ ਕਾਰੋਬਾਰੀ ਵਰਤੋਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ।

ਇਹ ਮਾਡਲ ਮੂਲ ਮਿਸਟਰਾਲ ਲਾਰਜ ਦਾ ਅਪਗ੍ਰੇਡ ਹੈ ਜੋ ਪੇਸ਼ ਕਰਦਾ ਹੈ
- ਵੱਡਾ ਸੰਦਰਭ ਖਿੜਕੀ - 128k ਵਿਰੁੱਧ 32k
- ਗਣਿਤ ਅਤੇ ਕੋਡਿੰਗ ਕਿਰਿਆਵਾਂ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ - 76.9% ਸਧਾਰਣ ਸਹੀਤਾ ਵਿਰੁੱਧ 60.4%
- ਵਧੀਆ ਬਹੁਭਾਸ਼ਾਈ ਪ੍ਰਦਰਸ਼ਨ - ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: ਅੰਗਰੇਜ਼ੀ, ਫ੍ਰੈਂਚ, ਜਰਮਨ, ਸਪੇਨੀ, ਇਟਾਲਵੀ, ਪੁਰਤਗਾਲੀ, ਡੱਚ, ਰੂਸੀ, ਚੀਨੀ, ਜਪਾਨੀ, ਕੋਰੀਅਨ, ਅਰਬੀ ਅਤੇ ਹਿੰਦੀ।

ਇਨ੍ਹਾਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ, ਮਿਸਟਰਾਲ ਲਾਰਜ ਵਿੱਚ ਸ਼ਾਨਦਾਰ ਹੈ
- *ਰੀਟ੍ਰੀਵਲ ਆਗਮੈਂਟਡ ਜਨਰੇਸ਼ਨ (RAG)* - ਵੱਡੇ ਸੰਦਰਭ ਖਿੜਕੀ ਦੇ ਕਾਰਨ
- *ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - ਇਸ ਮਾਡਲ ਵਿੱਚ ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਹੈ ਜੋ ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ APIਜ਼ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਕਾਲਾਂ ਦੋਵੇਂ ਇੱਕਸਾਰ ਜਾਂ ਇੱਕ ਦੇ ਬਾਅਦ ਇੱਕ ਕ੍ਰਮਵਾਰ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।
- *ਕੋਡ ਜਨਰੇਸ਼ਨ* - ਇਹ ਮਾਡਲ ਪਾਇਥਨ, ਜਾਵਾ, ਟਾਈਪਸਕ੍ਰਿਪਟ ਅਤੇ C++ ਜਨਰੇਸ਼ਨ 'ਤੇ ਸ਼ਾਨਦਾਰ ਹੈ।

### RAG ਉਦਾਹਰਨ ਮਿਸਟਰਾਲ ਲਾਰਜ 2 ਦੀ ਵਰਤੋਂ ਕਰਕੇ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਮਿਸਟਰਾਲ ਲਾਰਜ 2 ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇੱਕ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ 'ਤੇ RAG ਪੈਟਰਨ ਚਲਾਉਂਦੇ ਹਾਂ। ਸਵਾਲ ਕੋਰੀਅਨ ਵਿੱਚ ਲਿਖਿਆ ਗਿਆ ਹੈ ਅਤੇ ਲੇਖਕ ਦੀਆਂ ਕਾਲਜ ਤੋਂ ਪਹਿਲਾਂ ਦੀਆਂ ਗਤੀਵਿਧੀਆਂ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ।

ਇਹ Cohere Embeddings ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਸਵਾਲ ਦੇ ਐਮਬੈਡਿੰਗ ਬਣ ਸਕਣ। ਇਸ ਨਮੂਨੇ ਲਈ, ਇਹ faiss ਪਾਇਥਨ ਪੈਕੇਜ ਨੂੰ ਵੈਕਟਰ ਸਟੋਰ ਵਜੋਂ ਵਰਤਦਾ ਹੈ।

ਮਿਸਟਰਾਲ ਮਾਡਲ ਨੂੰ ਭੇਜੇ ਗਏ ਪ੍ਰੰਪਟ ਵਿੱਚ ਸਵਾਲਾਂ ਅਤੇ ਪ੍ਰਾਪਤ ਕੀਤੇ ਗਏ ਟੁਕੜੇ ਜੋ ਸਵਾਲ ਨਾਲ ਮਿਲਦੇ ਹਨ, ਦੋਵੇਂ ਸ਼ਾਮਲ ਹਨ। ਮਾਡਲ ਫਿਰ ਇੱਕ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

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

## ਮਿਸਟਰਾਲ ਸਮਾਲ

ਮਿਸਟਰਾਲ ਸਮਾਲ ਮਿਸਟਰਾਲ ਮਾਡਲਾਂ ਦੇ ਪਰਿਵਾਰ ਵਿੱਚ ਇੱਕ ਹੋਰ ਮਾਡਲ ਹੈ ਜੋ ਪ੍ਰੀਮੀਅਰ/ਇੰਟਰਪ੍ਰਾਈਜ਼ ਸ਼੍ਰੇਣੀ ਹੇਠ ਆਉਂਦਾ ਹੈ। ਜਿਵੇਂ ਕਿ ਨਾਮ ਤੋਂ ਪਤਾ ਲੱਗਦਾ ਹੈ, ਇਹ ਮਾਡਲ ਇੱਕ ਛੋਟੀ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ। ਮਿਸਟਰਾਲ ਸਮਾਲ ਦੀ ਵਰਤੋਂ ਦੇ ਫਾਇਦੇ ਇਹ ਹਨ ਕਿ ਇਹ:
- ਮਿਸਟਰਾਲ LLMs ਜਿਵੇਂ ਕਿ ਮਿਸਟਰਾਲ ਲਾਰਜ ਅਤੇ NeMo ਦੇ ਮੁਕਾਬਲੇ ਲਾਗਤ ਬਚਤ - 80% ਕੀਮਤ ਘਟਾਓ
- ਘੱਟ ਵਿਲੰਬ - ਮਿਸਟਰਾਲ ਦੇ LLMs ਦੇ ਮੁਕਾਬਲੇ ਤੇਜ਼ ਜਵਾਬ
- ਲਚਕਦਾਰ - ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਘੱਟ ਸੰਸਾਧਨਾਂ ਦੀ ਲੋੜ ਨਾਲ ਤੈਨਾਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

ਮਿਸਟਰਾਲ ਸਮਾਲ ਲਈ ਸ਼ਾਨਦਾਰ ਹੈ:
- ਟੈਕਸਟ ਅਧਾਰਤ ਕੰਮ ਜਿਵੇਂ ਕਿ ਸੰਖੇਪਣ, ਭਾਵਨਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਅਨੁਵਾਦ।
- ਐਪਲੀਕੇਸ਼ਨ ਜਿੱਥੇ ਇਸ ਦੀ ਲਾਗਤ ਪ੍ਰਭਾਵੀਤਾ ਦੇ ਕਾਰਨ ਅਕਸਰ ਬੇਨਤੀਆਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ
- ਘੱਟ ਵਿਲੰਬ ਕੋਡ ਕੰਮ ਜਿਵੇਂ ਕਿ ਸਮੀਖਿਆ ਅਤੇ ਕੋਡ ਸੁਝਾਅ

## ਮਿਸਟਰਾਲ ਸਮਾਲ ਅਤੇ ਮਿਸਟਰਾਲ ਲਾਰਜ ਦੀ ਤੁਲਨਾ

ਮਿਸਟਰਾਲ ਸਮਾਲ ਅਤੇ ਲਾਰਜ ਵਿਚਕਾਰ ਵਿਲੰਬ ਵਿੱਚ ਅੰਤਰ ਦਿਖਾਉਣ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਸੈੱਲ ਚਲਾਓ।

ਤੁਸੀਂ 3-5 ਸਕਿੰਟ ਦੇ ਵਿਚਕਾਰ ਜਵਾਬ ਦੇ ਸਮਿਆਂ ਵਿੱਚ ਅੰਤਰ ਦੇਖ ਸਕਦੇ ਹੋ। ਇਹ ਵੀ ਨੋਟ ਕਰੋ ਕਿ ਇੱਕੋ ਜਿਹੇ ਪ੍ਰੰਪਟ ਤੇ ਜਵਾਬ ਦੀ ਲੰਬਾਈ ਅਤੇ ਸ਼ੈਲੀ।

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

## ਮਿਸਟਰਾਲ ਨੇਮੋ

ਇਸ ਪਾਠ ਵਿੱਚ ਚਰਚਾ ਕੀਤੇ ਹੋਰ ਦੋ ਮਾਡਲਾਂ ਦੇ ਮੁਕਾਬਲੇ, ਮਿਸਟਰਾਲ ਨੇਮੋ ਹੀ ਇੱਕ ਮੁਫਤ ਮਾਡਲ ਹੈ ਜਿਸ ਵਿੱਚ ਅਪਾਚੇ 2 ਲਾਇਸੈਂਸ ਹੈ।

ਇਸਨੂੰ ਮਿਸਟਰਾਲ ਦੇ ਪਹਿਲਾਂ ਦੇ ਖੁੱਲੇ ਸਰੋਤ LLM, ਮਿਸਟਰਾਲ 7B ਦੇ ਅਪਗ੍ਰੇਡ ਵਜੋਂ ਦੇਖਿਆ ਜਾਂਦਾ ਹੈ।

ਨੇਮੋ ਮਾਡਲ ਦੀਆਂ ਕੁਝ ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ:

- *ਵਧੇਰੇ ਕੁਸ਼ਲ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ:* ਇਹ ਮਾਡਲ ਟਿਕਟੋਕਨ ਨਾਲੋਂ ਟੇਕਨ ਟੋਕਨਾਈਜ਼ਰ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਇਸ ਨਾਲ ਵੱਧ ਭਾਸ਼ਾਵਾਂ ਅਤੇ ਕੋਡ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ ਹੁੰਦਾ ਹੈ।

- *ਫਾਈਨਟਿਊਨਿੰਗ:* ਬੇਸ ਮਾਡਲ ਫਾਈਨਟਿਊਨਿੰਗ ਲਈ ਉਪਲਬਧ ਹੈ। ਇਹ ਉਪਯੋਗ ਕੇਸਾਂ ਲਈ ਵਧੇਰੇ ਲਚਕਦਾਰਤਾ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜਿੱਥੇ ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਲੋੜ ਪੈ ਸਕਦੀ ਹੈ।

- *ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - ਮਿਸਟਰਾਲ ਲਾਰਜ ਵਾਂਗ, ਇਸ ਮਾਡਲ ਨੂੰ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ 'ਤੇ ਸਿਖਲਾਇਆ ਗਿਆ ਹੈ। ਇਸ ਨਾਲ ਇਹ ਖਾਸ ਬਣ ਜਾਂਦਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਪਹਿਲਾਂ ਦੇ ਖੁੱਲੇ ਸਰੋਤ ਮਾਡਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ ਜੋ ਇਹ ਕਰਦਾ ਹੈ।

### ਟੋਕਨਾਈਜ਼ਰ ਦੀ ਤੁਲਨਾ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ, ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ ਮਿਸਟਰਾਲ ਨੇਮੋ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਮਿਸਟਰਾਲ ਲਾਰਜ ਦੇ ਮੁਕਾਬਲੇ ਕਿਵੇਂ ਹੈਂਡਲ ਕਰਦਾ ਹੈ।

ਦੋਵੇਂ ਨਮੂਨੇ ਇੱਕੋ ਜਿਹੇ ਪ੍ਰੰਪਟ ਲੈਂਦੇ ਹਨ ਪਰ ਤੁਹਾਨੂੰ ਵੇਖਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਨੇਮੋ ਵਾਪਸ ਘੱਟ ਟੋਕਨ ਵਾਪਸ ਕਰਦਾ ਹੈ ਵਿਰੁੱਧ ਮਿਸਟਰਾਲ ਲਾਰਜ।

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

## ਸਿੱਖਿਆ ਇੱਥੇ ਨਹੀਂ ਰੁਕਦੀ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਹ ਪਾਠ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [ਜਨਰੇਟਿਵ AI ਸਿੱਖਣ ਸੰਗ੍ਰਹਿ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਜੋ ਆਪਣੀ ਜਨਰੇਟਿਵ AI ਗਿਆਨ ਨੂੰ ਅੱਗੇ ਵਧਾਇਆ ਜਾ ਸਕੇ!

**ਅਸਵੀਕਾਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਨੂੰ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਸਚੇਤ ਰਹੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਨਿਯਮਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।