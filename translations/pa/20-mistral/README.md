<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:55:11+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "pa"
}
-->
# Mistral ਮਾਡਲਾਂ ਨਾਲ ਇਮਾਰਤ

## ਪ੍ਰਸਤਾਵਨਾ

ਇਸ ਪਾਠ ਵਿੱਚ ਇਹ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:
- ਵੱਖ-ਵੱਖ Mistral ਮਾਡਲਾਂ ਦੀ ਖੋਜ
- ਹਰ ਮਾਡਲ ਲਈ ਵਰਤੋਂ-ਕੇਸ ਅਤੇ ਸਥਿਤੀਆਂ ਦੀ ਸਮਝ
- ਕੋਡ ਨਮੂਨੇ ਜੋ ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਂਦੇ ਹਨ।

## Mistral ਮਾਡਲਾਂ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ 3 ਵੱਖ-ਵੱਖ Mistral ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਕਰਾਂਗੇ: **Mistral Large**, **Mistral Small** ਅਤੇ **Mistral Nemo**।

ਇਨ੍ਹਾਂ ਵਿੱਚੋਂ ਹਰ ਇੱਕ ਮਾਡਲ Github Model ਮਾਰਕੀਟਪਲੇਸ 'ਤੇ ਮੁਫ਼ਤ ਉਪਲਬਧ ਹੈ। ਇਸ ਨੋਟਬੁੱਕ ਵਿੱਚ ਕੋਡ ਨੂੰ ਚਲਾਉਣ ਲਈ ਇਹ ਮਾਡਲ ਵਰਤੇ ਜਾਣਗੇ। [AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ਲਈ Github ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਬਾਰੇ ਹੋਰ ਵੇਰਵੇ ਇੱਥੇ ਹਨ।

## Mistral Large 2 (2407)

Mistral Large 2 ਮੌਜੂਦਾ Mistral ਦਾ ਪ੍ਰਮੁੱਖ ਮਾਡਲ ਹੈ ਅਤੇ ਇਹ ਉੱਦਮ ਵਰਤੋਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ।

ਮਾਡਲ ਮੂਲ Mistral Large ਦਾ ਅਪਗਰੇਡ ਹੈ ਜਿਸ ਵਿੱਚ ਇਹ ਸ਼ਾਮਲ ਹੈ:
- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਵਿਰੁੱਧ 32k
- ਗਣਿਤ ਅਤੇ ਕੋਡਿੰਗ ਟਾਸਕਾਂ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ - 76.9% ਔਸਤ ਸਹੀਤਾ ਵਿਰੁੱਧ 60.4%
- ਬਹੁਭਾਸ਼ੀ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਵਾਧਾ - ਭਾਸ਼ਾਵਾਂ ਸ਼ਾਮਲ ਹਨ: ਅੰਗਰੇਜ਼ੀ, ਫਰਾਂਸੀਸੀ, ਜਰਮਨ, ਸਪੇਨੀ, ਇਟਾਲਵੀ, ਪੁਰਤਗਾਲੀ, ਡੱਚ, ਰੂਸੀ, ਚੀਨੀ, ਜਾਪਾਨੀ, ਕੋਰੀਅਨ, ਅਰਬੀ, ਅਤੇ ਹਿੰਦੀ।

ਇਨ੍ਹਾਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ, Mistral Large ਸ਼ਾਨਦਾਰ ਹੈ:
- *Retrieval Augmented Generation (RAG)* - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਕਾਰਨ
- *Function Calling* - ਇਸ ਮਾਡਲ ਵਿੱਚ ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਹੈ ਜੋ ਬਾਹਰੀ ਟੂਲ ਅਤੇ API ਨਾਲ ਇਕੱਠਾ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਕਾਲਾਂ ਪੈਰਲਲ ਵਿੱਚ ਜਾਂ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਲਗਾਤਾਰ ਕ੍ਰਮ ਵਿੱਚ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।
- *Code Generation* - ਇਹ ਮਾਡਲ Python, Java, TypeScript ਅਤੇ C++ ਜਨਰੇਸ਼ਨ 'ਤੇ ਸ਼ਾਨਦਾਰ ਹੈ।

### Mistral Large 2 ਵਰਤ ਕੇ RAG ਉਦਾਹਰਨ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ Mistral Large 2 ਨੂੰ ਇੱਕ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ 'ਤੇ RAG ਪੈਟਰਨ ਚਲਾਉਣ ਲਈ ਵਰਤ ਰਹੇ ਹਾਂ। ਸਵਾਲ ਕੋਰੀਅਨ ਵਿੱਚ ਲਿਖਿਆ ਗਿਆ ਹੈ ਅਤੇ ਲੇਖਕ ਦੀਆਂ ਕਾਲਜ ਤੋਂ ਪਹਿਲਾਂ ਦੀਆਂ ਗਤੀਵਿਧੀਆਂ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ।

ਇਹ Cohere Embeddings Model ਨੂੰ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ ਦੇ ਨਾਲ ਨਾਲ ਸਵਾਲ ਦੀਆਂ ਐਮਬੈਡਿੰਗ ਬਣਾਉਣ ਲਈ ਵਰਤਦਾ ਹੈ। ਇਸ ਨਮੂਨੇ ਲਈ, ਇਹ faiss Python ਪੈਕੇਜ ਨੂੰ ਵੈਕਟਰ ਸਟੋਰ ਵਜੋਂ ਵਰਤਦਾ ਹੈ।

Mistral ਮਾਡਲ ਨੂੰ ਭੇਜਿਆ ਗਿਆ ਪ੍ਰੋੰਪਟ ਸਵਾਲਾਂ ਅਤੇ ਖੋਜੇ ਗਏ ਚੰਕਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਜੋ ਸਵਾਲ ਨਾਲ ਮਿਲਦੇ ਹਨ। ਮਾਡਲ ਫਿਰ ਇੱਕ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਜਵਾਬ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

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

Mistral Small Mistral ਮਾਡਲਾਂ ਦੇ ਪਰਿਵਾਰ ਵਿੱਚ ਇੱਕ ਹੋਰ ਮਾਡਲ ਹੈ ਜੋ ਪ੍ਰੀਮੀਅਰ/ਉੱਦਮ ਸ਼੍ਰੇਣੀ ਦੇ ਅੰਦਰ ਹੈ। ਜਿਵੇਂ ਕਿ ਨਾਮ ਤੋਂ ਸਪਸ਼ਟ ਹੈ, ਇਹ ਮਾਡਲ ਇੱਕ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ। Mistral Small ਦੀ ਵਰਤੋਂ ਦੇ ਫਾਇਦੇ ਇਹ ਹਨ ਕਿ ਇਹ:
- Mistral LLMs ਜਿਵੇਂ Mistral Large ਅਤੇ NeMo ਦੇ ਮੁਕਾਬਲੇ ਲਾਗਤ ਬਚਾਉਣ ਵਾਲਾ ਹੈ - 80% ਕੀਮਤ ਵਿੱਚ ਕਮੀ
- ਘੱਟ ਲੈਟੈਂਸੀ - Mistral ਦੇ LLMs ਦੇ ਮੁਕਾਬਲੇ ਤੇਜ਼ ਜਵਾਬ
- ਲਚਕਦਾਰ - ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਘੱਟ ਸਰੋਤਾਂ ਦੀ ਲੋੜ ਨਾਲ ਤੈਅ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

Mistral Small ਲਈ ਸ਼ਾਨਦਾਰ ਹੈ:
- ਪਾਠ ਅਧਾਰਤ ਟਾਸਕ ਜਿਵੇਂ ਸੰਖੇਪਕਰਨ, ਭਾਵਨਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਅਨੁਵਾਦ।
- ਐਪਲੀਕੇਸ਼ਨਾਂ ਜਿੱਥੇ ਇਸ ਦੀ ਲਾਗਤ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਕਾਰਨ ਵਾਰ-ਵਾਰ ਬੇਨਤੀਆਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ
- ਘੱਟ ਲੈਟੈਂਸੀ ਕੋਡ ਟਾਸਕ ਜਿਵੇਂ ਸਮੀਖਾ ਅਤੇ ਕੋਡ ਸੁਝਾਅ

## Mistral Small ਅਤੇ Mistral Large ਦੀ ਤੁਲਨਾ

Mistral Small ਅਤੇ Large ਵਿੱਚ ਲੈਟੈਂਸੀ ਵਿੱਚ ਅੰਤਰ ਦਿਖਾਉਣ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਸੈਲ ਚਲਾਓ।

ਤੁਹਾਨੂੰ 3-5 ਸਕਿੰਟ ਦੇ ਜਵਾਬ ਸਮਿਆਂ ਵਿੱਚ ਅੰਤਰ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਸੇ ਪ੍ਰੋੰਪਟ 'ਤੇ ਜਵਾਬ ਦੀ ਲੰਬਾਈ ਅਤੇ ਸ਼ੈਲੀ 'ਤੇ ਵੀ ਧਿਆਨ ਦਿਓ।

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

ਇਸ ਪਾਠ ਵਿੱਚ ਚਰਚਾ ਕੀਤੇ ਗਏ ਹੋਰ ਦੋ ਮਾਡਲਾਂ ਦੇ ਮੁਕਾਬਲੇ, Mistral NeMo ਇੱਕ Apache2 ਲਾਇਸੰਸ ਨਾਲ ਇਕਲੌਤਾ ਮੁਫ਼ਤ ਮਾਡਲ ਹੈ।

ਇਹ ਪਹਿਲੇ Mistral ਤੋਂ ਖੁੱਲ੍ਹੇ ਸਰੋਤ LLM, Mistral 7B ਲਈ ਅਪਗਰੇਡ ਵਜੋਂ ਦੇਖਿਆ ਜਾਂਦਾ ਹੈ।

NeMo ਮਾਡਲ ਦੀਆਂ ਕੁਝ ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ:

- *ਅਧਿਕ ਕੁਸ਼ਲ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ:* ਇਹ ਮਾਡਲ ਜ਼ਿਆਦਾਤਰ ਵਰਤੇ ਜਾਣ ਵਾਲੇ tiktoken ਦੇ ਥਾਂ Tekken tokenizer ਵਰਤਦਾ ਹੈ। ਇਸ ਨਾਲ ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਅਤੇ ਕੋਡ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ ਹੁੰਦਾ ਹੈ।

- *ਫਾਈਨਟਿਊਨਿੰਗ:* ਬੇਸ ਮਾਡਲ ਫਾਈਨਟਿਊਨਿੰਗ ਲਈ ਉਪਲਬਧ ਹੈ। ਇਸ ਨਾਲ ਵਰਤੋਂ-ਕੇਸਾਂ ਲਈ ਵਧੇਰੇ ਲਚਕਤਾ ਹੁੰਦੀ ਹੈ ਜਿੱਥੇ ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ।

- *ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - Mistral Large ਵਾਂਗ, ਇਸ ਮਾਡਲ ਨੂੰ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ 'ਤੇ ਪ੍ਰਸ਼ਿਕਸ਼ਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਸ ਨੂੰ ਪਹਿਲੇ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੈ।

### Tokenizers ਦੀ ਤੁਲਨਾ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ, ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ Mistral NeMo Mistral Large ਦੇ ਮੁਕਾਬਲੇ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਕਿਵੇਂ ਸੰਭਾਲਦਾ ਹੈ।

ਦੋਨੋ ਨਮੂਨੇ ਇੱਕੋ ਜਿਹੇ ਪ੍ਰੋੰਪਟ ਲੈਂਦੇ ਹਨ ਪਰ ਤੁਹਾਨੂੰ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ NeMo Mistral Large ਦੇ ਮੁਕਾਬਲੇ ਘੱਟ ਟੋਕਨ ਵਾਪਸ ਕਰਦਾ ਹੈ।

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

## ਸਿੱਖਣਾ ਇੱਥੇ ਨਹੀਂ ਰੁਕਦਾ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਹ ਪਾਠ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਜੋ ਤੁਹਾਡਾ Generative AI ਗਿਆਨ ਵਧਾਉਣਾ ਜਾਰੀ ਰੱਖ ਸਕੋ!

**ਛੁਟਕਾਰਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਵਿਧਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਗੰਭੀਰ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।