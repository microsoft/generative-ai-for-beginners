# ਮਿਸਟਰਾਲ ਮਾਡਲਾਂ ਨਾਲ ਨਿਰਮਾਣ 

## ਜਾਣ ਪਹਚਾਣ 

ਇਸ ਪਾਠ ਵਿੱਚ ਕੁਝ ਇਨ੍ਹਾਂ ਚੀਜ਼ਾਂ ਨੂੰ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ: 
- ਵੱਖ-ਵੱਖ ਮਿਸਟਰਾਲ ਮਾਡਲਾਂ ਦੀ ਖੋਜ 
- ਹਰ ਮਾਡਲ ਦੇ ਇਸਤੇਮਾਲ ਮਾਮਲਿਆਂ ਅਤੇ ਸਥਿਤੀਆਂ ਨੂੰ ਸਮਝਣਾ 
- ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਰਸਾਉਂਦੇ ਕੋਡ ਨਮੂਨੇ ਦੀ ਖੋਜ। 

## ਮਿਸਟਰਾਲ ਮਾਡਲ 

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ 3 ਵੱਖ-ਵੱਖ ਮਿਸਟਰਾਲ ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਕਰਾਂਗੇ: 
**ਮਿਸਟਰਾਲ ਲਾਰਜ**, **ਮਿਸਟਰਾਲ ਸੌਂਘਾ** ਅਤੇ **ਮਿਸਟਰਾਲ ਨੇਮੋ**। 

ਇਹਨਾਂ ਵਿੱਚੋਂ ਹਰ ਇਕ ਮਾਡਲ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਮੁਫ਼ਤ ਉਪਲਬਧ ਹੈ। ਇਸ ਨੋਟਬੁੱਕ ਵਿੱਚ ਦਿੱਤਾ ਕੋਡ ਇਹਨਾਂ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। 

> **ਨੋਟ:** GitHub ਮਾਡਲ ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਤੇ ਮੁਕਦੇ ਹਨ। ਇੱਥੇ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ਦੀ ਵਰਤੋਂ ਨਾਲ AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ ਦੀ ਹੋਰ ਜਾਣਕਾਰੀ ਹੈ। 


## ਮਿਸਟਰਾਲ ਲਾਰਜ 2 (2407)
ਮਿਸਟਰਾਲ ਲਾਰਜ 2 ਇਸ ਵੇਲੇ ਮਿਸਟਰਾਲ ਤੋਂ ਫਲੈਗਸ਼ਿਪ ਮਾਡਲ ਹੈ ਅਤੇ ਇਹ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਵਰਤੇ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ। 

ਇਹ ਮਾਡਲ ਮੂਲ ਮਿਸਟਰਾਲ ਲਾਰਜ ਦੀ ਇੱਕ ਅੱਪਗਰੇਡ ਹੈ ਜਿਸ ਵਿੱਚ: 
- ਵੱਡਾ ਕਾਂਟੈਕਸਟ ਵਿਂਡੋ - 128k ਵਿਰੁੱਧ 32k 
- ਗਣਿਤ ਅਤੇ ਕੋਡਿੰਗ ਕੰਮਾਂ 'ਤੇ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ - 76.9% ਔਸਤ ਸਹੀਦਾਰੀ ਵਿਰੁੱਧ 60.4% 
- ਵਧੀਕ ਬਹੁਭਾਸ਼ੀ ਪ੍ਰਦਰਸ਼ਨ - ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: ਅੰਗ੍ਰੇਜ਼ੀ, ਫਰਾਂਸੀਸੀ, ਜਰਮਨ, ਸਪੇਨੀ, ਇਟਾਲੀਅਨ, ਪੁਰਤਗਾਲੀ, ਡੱਚ, ਰੂਸੀ, ਚੀਨੀ, ਜਪਾਨੀ, ਕੋਰੀਆਈ, ਅਰਬੀ ਅਤੇ ਹਿੰਦੀ। 

ਇਹਨਾਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ, ਮਿਸਟਰਾਲ ਲਾਰਜ ਸ਼ਾਨਦਾਰ ਹੈ: 
- *ਰੀਟਰੀਵਲ ਆਗਮੈਂਟਡ ਜਨਰੇਸ਼ਨ (RAG)* - ਵੱਡੇ ਕਾਂਟੈਕਸਟ ਵਿਂਡੋ ਕਾਰਨ 
- *ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - ਇਸ ਮਾਡਲ ਵਿੱਚ ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਹੈ ਜੋ ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ APIs ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਕਾਲਾਂ ਸੰਤੁਲਨਤ ਜਾਂ ਇੱਕ-ਦੂਜੇ ਦੀ ਪਿੱਛੇ ਕ੍ਰਮਵਾਰ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ। 
- *ਕੋਡ ਜਨਰੇਸ਼ਨ* - ਇਹ ਮਾਡਲ ਪਾਇਥਾਨ, ਜਾਵਾ, ਟਾਈਪਸਕ੍ਰਿਪਟ ਅਤੇ C++ ਜਨਰੇਸ਼ਨ 'ਚ ਸ਼ਾਨਦਾਰ ਹੈ। 

### ਮਿਸਟਰਾਲ ਲਾਰਜ 2 ਨਾਲ RAG ਉਦਾਹਰਨ 

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਮਿਸਟਰਾਲ ਲਾਰਜ 2 ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਇੱਕ ਟੈਕਸਟ ਡੌਕੂਮੈਂਟ 'ਤੇ RAG ਪੈਟਰਨ ਚਲਾਏਂਗੇ। ਸਵਾਲ ਕੋਰੀਆਈ ਵਿੱਚ ਲਿਖਿਆ ਗਿਆ ਹੈ ਅਤੇ ਲੇਖਕ ਦੀ ਕਾਲਜ ਤੋਂ ਪਹਿਲਾਂ ਦੀਆਂ ਗਤਿਵਿਧੀਆਂ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ। 

ਇਹ ਕੋਹੀਅਰ ਇੰਬੈਡਿੰਗ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਦੈ ਜਿਹੜਾ ਟੈਕਸਟ ਡੌਕੂਮੈਂਟ ਅਤੇ ਸਵਾਲ ਦੋਹਾਂ ਦੀਆਂ ਇੰਬੈਡਿੰਗ ਬਨਾਉਂਦਾ ਹੈ। ਇਸ ਨਮੂਨੇ ਲਈ, ਇਹ ਫੈਸ ਪਾਇਥਾਨ ਪੈਕੇਜ ਨੂੰ ਵੈਕਟਰ ਸਟੋਰ ਵਜੋਂ ਵਰਤਦਾ ਹੈ। 

ਮਿਸਟਰਾਲ ਮਾਡਲ ਨੂੰ ਭੇਜਿਆ ਗਿਆ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਸਵਾਲ ਅਤੇ ਪ੍ਰਾਪਤ ਚੰਕ ਦੋਹਾਂ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ ਜੋ ਸਵਾਲ ਦੇ ਸਮਾਨ ਹੁੰਦੇ ਹਨ। ਮਾਡਲ ਫਿਰ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਵਾਬ ਦਿੰਦਾ ਹੈ। 

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

# ਇਹਨਾਂ ਨੂੰ ਆਪਣੇ Microsoft Foundry ਪ੍ਰਾਜੈਕਟ ਦੇ "ਸਰਵੇਖਣ" ਪੰਨੇ ਤੋਂ ਪ੍ਰਾਪਤ ਕਰੋ
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ਦੂਰੀ, ਸੂਚਕ
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

## ਮਿਸਟਰਾਲ ਸੌਂਘਾ 
ਮਿਸਟਰਾਲ ਸੌਂਘਾ ਮਿਸਟਰਾਲ ਪਰਿਵਾਰ ਦਾ ਇੱਕ ਹੋਰ ਮਾਡਲ ਹੈ, ਜੋ ਪ੍ਰੀਮੀਅਰ/ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਹੈ। ਨਾਮ ਤੋਂ ਹੀ ਸਮਝ आता ਹੈ ਕਿ ਇਹ ਮਾਡਲ ਇੱਕ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ। ਮਿਸਟਰਾਲ ਸੌਂਘਾ ਦੀ ਵਰਤੋਂ ਦੇ ਫਾਇਦੇ ਹਨ: 
- ਮਿਸਟਰਾਲ LLMs ਜਿਵੇਂ ਕਿ ਮਿਸਟਰਾਲ ਲਾਰਜ ਅਤੇ ਨੇਮੋ ਨਾਲ ਤੁਲਨਾ ਵਿੱਚ ਲਾਗਤ ਬਚਤ - 80% ਕੀਮਤ ਘਟਾਉ 
- ਘੱਟ ਲੇਟੈਂਸੀ - ਮਿਸਟਰਾਲ ਦੇ LLMs ਨਾਲ ਤੁਲਨਾ ਵਿੱਚ ਤੇਜ਼ ਜਵਾਬ 
- ਲਚਕੀਲਾ - ਵੱਖ-ਵੱਖ ਮਾਹੌਲਾਂ ਵਿੱਚ ਘੱਟ ਸਰੋਤਾਂ ਦੀਆਂ ਪਾਬੰਦੀਆਂ ਨਾਲ ਤੈਅ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। 


ਮਿਸਟਰਾਲ ਸੌਂਘਾ ਲਈ ਵਧੀਆ ਹੈ: 
- ਟੈਕਸਟ ਅਧਾਰਿਤ ਕੰਮ ਜਿਵੇਂ ਕਿ ਸੰਖੇਪ ਬਣਾਉਣਾ, ਭਾਵਨਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਅਨੁਵਾਦ। 
- ਐਪਲੀਕੇਸ਼ਨ ਜਿੱਥੇ ਲਾਗਤ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਕਾਰਨ ਬਾਰੰਬਾਰ ਬੇਨਤੀਆਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ 
- ਘੱਟ ਲੇਟੈਂਸੀ ਕੋਡ ਕੰਮ ਜਿਵੇਂ ਸਮੀਖਿਆ ਅਤੇ ਕੋਡ ਸੁਝਾਵਾਂ 

## ਮਿਸਟਰਾਲ ਸੌਂਘਾ ਅਤੇ ਮਿਸਟਰਾਲ ਲਾਰਜ ਦੀ ਤੁਲਨਾ 

ਮਿਸਟਰਾਲ ਸੌਂਘਾ ਅਤੇ ਲਾਰਜ ਦੇ ਵਿਚਕਾਰ ਲੇਟੈਂਸੀ ਦੇ ਫਰਕ ਨੂੰ ਦਰਸਾਉਣ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਸੈੱਲ ਚਲਾਓ। 

ਤੁਹਾਨੂੰ ਜਵਾਬ ਦੇ ਸਮਿਆਂ ਵਿੱਚ 3-5 ਸਕਿੰਟ ਦਾ ਅੰਤਰ ਦੇਖਣ ਨੂੰ ਮਿਲੇਗਾ। ਇਹ ਵੀ ਧਿਆਨ ਦਿਓ ਕਿ ਇੱਕੋ ਹੀ ਪ੍ਰਾਂਪਟ ਤੇ ਜਵਾਬ ਦੀ ਲੰਬਾਈ ਅਤੇ ਅੰਦਾਜ਼ ਵੀ ਵੇਖੋ।  

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

## ਮਿਸਟਰਾਲ ਨੇਮੋ

ਇਸ ਪਾਠ ਵਿੱਚ ਚਰਚਾ ਕੀਤੇ ਹੋਰ ਦੋ ਮਾਡਲਾਂ ਨਾਲ ਤੁਲਨਾ ਕੀਤੀ ਜਾਵੇ ਤਾਂ, ਮਿਸਟਰਾਲ ਨੇਮੋ ਇਕਮਾਤਰ ਮੁਫ਼ਤ ਮਾਡਲ ਹੈ ਜਿਸ ਕੋਲ Apache2 ਲਾਇਸੈਂਸ ਹੈ। 

ਇਸ ਨੂੰ ਮਿਸਟਰਾਲ ਦੇ ਪਹਿਲਾਂ ਦੇ ਖੁੱਲ੍ਹੇ ਸਰੋਤ LLM, ਮਿਸਟਰਾਲ 7B ਦਾ ਅੱਪਗਰੇਡ ਸਮਝਿਆ ਜਾਂਦਾ ਹੈ। 

ਨੇਮੋ ਮਾਡਲ ਦੀਆਂ ਕੁਝ ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ: 

- *ਅਧਿਕ ਕਾਰੀਗਰ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ:* ਇਹ ਮਾਡਲ ਟਿਕਟੋਕਨ ਦੀ ਜਗ੍ਹਾ ਟੇੱਕਨ ਟੋਕਨਾਈਜ਼ਰ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਇਸ ਨਾਲ ਵੱਧ ਭਾਸ਼ਾਵਾਂ ਅਤੇ ਕੋਡ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ ਹਾਸਲ ਹੁੰਦਾ ਹੈ। 

- *ਫਾਈਨਟਿਊਨਿੰਗ:* ਆਧਾਰ ਮਾਡਲ ਫਾਈਨਟਿਊਨਿੰਗ ਲਈ ਉਪਲਬਧ ਹੈ। ਇਸ ਨਾਲ ਉਹਮਰੇਜ਼ ਇਹਨਾਂ ਮਾਮਲਿਆਂ ਵਿੱਚ ਜਿੱਥੇ ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਵਧੇਰੇ ਲਚਕੀਲਾਪਨ ਮਿਲਦਾ ਹੈ। 

- *ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - ਮਿਸਟਰਾਲ ਲਾਰਜ ਵਾਂਗ, ਇਸ ਮਾਡਲ ਨੂੰ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ 'ਤੇ ਟਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਇਸ ਨੂੰ ਪਹਿਲਾਂ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਵੱਖਰਾ ਬਣਾਉਂਦਾ ਹੈ। 


### ਟੋਕਨਾਈਜ਼ਰਾਂ ਦੀ ਤੁਲਨਾ 

ਇਸ ਨਮੂਨੇ ਵਿੱਚ, ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ ਮਿਸਟਰਾਲ ਨੇਮੋ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਮਿਸਟਰਾਲ ਲਾਰਜ ਨਾਲ ਕਿਵੇਂ ਨਿਭਾਉਂਦਾ ਹੈ। 

ਦੋਨੋਂ ਨਮੂਨੇ ਇੱਕੋ ਜਿਹਾ ਪ੍ਰਾਂਪਟ ਲੈਂਦੇ ਹਨ ਪਰ ਤੁਹਾਨੂੰ ਵੱਖਰਾ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਨੇਮੋ ਮਿਸਟਰਾਲ ਲਾਰਜ ਤੋਂ ਘੱਟ ਟੋਕਨ ਮੁੜਦਾ ਹੈ। 

```bash
pip install mistral-common
```

```python 
# ਜ਼ਰੂਰੀ ਪੈਕੇਜ ਆਮਦ ਕਰੋ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰੋ

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

# ਮਿਸ਼ਤਰਾਲ ਟੋਕਨਾਈਜ਼ਰ ਲੋਡ ਕਰੋ

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

## ਸਿੱਖਣਾ ਇੱਥੇ ਖਤਮ ਨਹੀਂ ਹੁੰਦਾ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਮੁਕੰਮਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਦਾ ਜਾਇਜ਼ਾ ਲਓ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਜਨਰੇਟਿਵ AI ਗਿਆਨ ਨੂੰ ਅੱਗੇ ਵਧਾ ਸਕੋ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->