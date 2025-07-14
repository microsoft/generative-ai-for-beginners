<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:58:42+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "pa"
}
-->
# Mistral ਮਾਡਲਾਂ ਨਾਲ ਬਣਾਉਣਾ

## ਜਾਣ ਪਹਚਾਣ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਕਵਰ ਕਰਾਂਗੇ:  
- ਵੱਖ-ਵੱਖ Mistral ਮਾਡਲਾਂ ਦੀ ਖੋਜ  
- ਹਰ ਮਾਡਲ ਦੇ ਵਰਤੋਂ ਦੇ ਮਾਮਲੇ ਅਤੇ ਸਥਿਤੀਆਂ ਨੂੰ ਸਮਝਣਾ  
- ਕੋਡ ਦੇ ਉਦਾਹਰਣ ਜੋ ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਖੂਬੀਆਂ ਦਿਖਾਉਂਦੇ ਹਨ।  

## Mistral ਮਾਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ 3 ਵੱਖ-ਵੱਖ Mistral ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਕਰਾਂਗੇ:  
**Mistral Large**, **Mistral Small** ਅਤੇ **Mistral Nemo**।  

ਇਹਨਾਂ ਮਾਡਲਾਂ ਨੂੰ Github Model marketplace 'ਤੇ ਮੁਫ਼ਤ ਉਪਲਬਧ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਸ ਨੋਟਬੁੱਕ ਵਿੱਚ ਦਿੱਤਾ ਕੋਡ ਇਨ੍ਹਾਂ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਲਾਇਆ ਜਾਵੇਗਾ। Github ਮਾਡਲਾਂ ਨਾਲ [AI ਮਾਡਲਾਂ ਦੇ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਇੱਥੇ ਵੇਖੋ।  

## Mistral Large 2 (2407)  
Mistral Large 2 ਇਸ ਸਮੇਂ Mistral ਦਾ ਪ੍ਰਮੁੱਖ ਮਾਡਲ ਹੈ ਅਤੇ ਇਹ ਉਦਯੋਗਿਕ ਵਰਤੋਂ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ।  

ਇਹ ਮਾਡਲ ਮੂਲ Mistral Large ਦਾ ਅੱਪਗ੍ਰੇਡ ਹੈ ਜੋ ਇਹ ਖਾਸ ਗੁਣ ਦਿੰਦਾ ਹੈ:  
- ਵੱਡਾ Context Window - 128k ਬਨਾਮ 32k  
- ਗਣਿਤ ਅਤੇ ਕੋਡਿੰਗ ਟਾਸਕਾਂ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ - 76.9% ਔਸਤ ਸਹੀਤਾ ਬਨਾਮ 60.4%  
- ਵਧੀਆ ਬਹੁਭਾਸ਼ੀ ਪ੍ਰਦਰਸ਼ਨ - ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: ਅੰਗਰੇਜ਼ੀ, ਫਰਾਂਸੀਸੀ, ਜਰਮਨ, ਸਪੇਨੀ, ਇਟਾਲੀਅਨ, ਪੁਰਤਗਾਲੀ, ਡੱਚ, ਰੂਸੀ, ਚੀਨੀ, ਜਪਾਨੀ, ਕੋਰੀਆਈ, ਅਰਬੀ ਅਤੇ ਹਿੰਦੀ।  

ਇਨ੍ਹਾਂ ਖੂਬੀਆਂ ਨਾਲ, Mistral Large ਖਾਸ ਕਰਕੇ ਚੰਗਾ ਹੈ:  
- *Retrieval Augmented Generation (RAG)* - ਵੱਡੇ context window ਕਾਰਨ  
- *Function Calling* - ਇਸ ਮਾਡਲ ਵਿੱਚ ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਹੁੰਦੀ ਹੈ ਜੋ ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ APIs ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਇਹ ਕਾਲਾਂ ਇੱਕ ਸਮੇਂ ਜਾਂ ਲੜੀਵਾਰ ਤਰੀਕੇ ਨਾਲ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ।  
- *Code Generation* - ਇਹ ਮਾਡਲ Python, Java, TypeScript ਅਤੇ C++ ਕੋਡ ਬਣਾਉਣ ਵਿੱਚ ਮਹਾਰਤ ਰੱਖਦਾ ਹੈ।  

### Mistral Large 2 ਨਾਲ RAG ਉਦਾਹਰਣ  

ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ, ਅਸੀਂ Mistral Large 2 ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ 'ਤੇ RAG ਪੈਟਰਨ ਚਲਾ ਰਹੇ ਹਾਂ। ਸਵਾਲ ਕੋਰੀਆਈ ਵਿੱਚ ਲਿਖਿਆ ਗਿਆ ਹੈ ਅਤੇ ਲੇਖਕ ਦੀ ਕਾਲਜ ਤੋਂ ਪਹਿਲਾਂ ਦੀਆਂ ਗਤੀਵਿਧੀਆਂ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ।  

ਇਹ Cohere Embeddings Model ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਸਵਾਲ ਦੋਹਾਂ ਦੇ embeddings ਬਣਾਉਣ ਲਈ। ਇਸ ਨਮੂਨੇ ਵਿੱਚ faiss Python ਪੈਕੇਜ ਨੂੰ ਵੈਕਟਰ ਸਟੋਰ ਵਜੋਂ ਵਰਤਿਆ ਗਿਆ ਹੈ।  

Mistral ਮਾਡਲ ਨੂੰ ਭੇਜਿਆ ਗਿਆ ਪ੍ਰਾਂਪਟ ਸਵਾਲਾਂ ਅਤੇ ਉਹਨਾਂ ਚੰਕਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ ਜੋ ਸਵਾਲ ਨਾਲ ਮਿਲਦੇ-ਜੁਲਦੇ ਹਨ। ਮਾਡਲ ਫਿਰ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।  

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
Mistral Small Mistral ਪਰਿਵਾਰ ਦਾ ਇੱਕ ਹੋਰ ਮਾਡਲ ਹੈ ਜੋ ਪ੍ਰੀਮੀਅਰ/ਉਦਯੋਗਿਕ ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦਾ ਹੈ। ਨਾਮ ਤੋਂ ਹੀ ਪਤਾ ਲੱਗਦਾ ਹੈ ਕਿ ਇਹ ਇੱਕ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ। Mistral Small ਦੀ ਵਰਤੋਂ ਦੇ ਫਾਇਦੇ ਹਨ:  
- Mistral LLMs ਜਿਵੇਂ Mistral Large ਅਤੇ NeMo ਨਾਲੋਂ ਲਾਗਤ ਵਿੱਚ ਬਚਤ - 80% ਕੀਮਤ ਘਟਾਉਂਦਾ ਹੈ  
- ਘੱਟ ਲੇਟੈਂਸੀ - Mistral ਦੇ LLMs ਨਾਲੋਂ ਤੇਜ਼ ਜਵਾਬ  
- ਲਚਕੀਲਾ - ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਘੱਟ ਸਰੋਤਾਂ ਦੀ ਲੋੜ ਨਾਲ ਤੈਨਾਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।  

Mistral Small ਵਧੀਆ ਹੈ:  
- ਟੈਕਸਟ ਅਧਾਰਿਤ ਕੰਮਾਂ ਲਈ ਜਿਵੇਂ ਸੰਖੇਪ, ਭਾਵਨਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਅਨੁਵਾਦ  
- ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਜਿੱਥੇ ਬਾਰੰਬਾਰ ਬੇਨਤੀਆਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ ਕਿਉਂਕਿ ਇਹ ਲਾਗਤ-ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੈ  
- ਘੱਟ ਲੇਟੈਂਸੀ ਵਾਲੇ ਕੋਡ ਕੰਮ ਜਿਵੇਂ ਸਮੀਖਿਆ ਅਤੇ ਕੋਡ ਸੁਝਾਅ  

## Mistral Small ਅਤੇ Mistral Large ਦੀ ਤੁਲਨਾ  

Mistral Small ਅਤੇ Large ਵਿੱਚ ਲੇਟੈਂਸੀ ਦੇ ਫਰਕ ਨੂੰ ਵੇਖਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਸੈੱਲ ਚਲਾਓ।  

ਤੁਹਾਨੂੰ 3-5 ਸਕਿੰਟਾਂ ਦੇ ਜਵਾਬ ਸਮੇਂ ਵਿੱਚ ਫਰਕ ਦੇਖਣ ਨੂੰ ਮਿਲੇਗਾ। ਨਾਲ ਹੀ ਇੱਕੋ ਪ੍ਰਾਂਪਟ 'ਤੇ ਜਵਾਬ ਦੀ ਲੰਬਾਈ ਅਤੇ ਅੰਦਾਜ਼ ਨੂੰ ਵੀ ਨੋਟ ਕਰੋ।  

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

ਇਸ ਪਾਠ ਵਿੱਚ ਚਰਚਾ ਕੀਤੇ ਹੋਏ ਦੋ ਹੋਰ ਮਾਡਲਾਂ ਨਾਲੋਂ, Mistral NeMo ਇੱਕੋ ਮੁਫ਼ਤ ਮਾਡਲ ਹੈ ਜਿਸਦੇ ਕੋਲ Apache2 ਲਾਇਸੈਂਸ ਹੈ।  

ਇਹ Mistral ਦੇ ਪਹਿਲਾਂ ਦੇ ਖੁੱਲ੍ਹੇ ਸਰੋਤ LLM, Mistral 7B ਦਾ ਅੱਪਗ੍ਰੇਡ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ।  

NeMo ਮਾਡਲ ਦੀਆਂ ਕੁਝ ਹੋਰ ਖਾਸੀਅਤਾਂ ਹਨ:  

- *ਵਧੀਆ ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ:* ਇਹ ਮਾਡਲ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤੇ ਜਾਣ ਵਾਲੇ tiktoken ਦੀ ਥਾਂ Tekken tokenizer ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਇਸ ਨਾਲ ਵਧੇਰੇ ਭਾਸ਼ਾਵਾਂ ਅਤੇ ਕੋਡ 'ਤੇ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ ਹੁੰਦਾ ਹੈ।  

- *ਫਾਈਨਟਿਊਨਿੰਗ:* ਬੇਸ ਮਾਡਲ ਫਾਈਨਟਿਊਨਿੰਗ ਲਈ ਉਪਲਬਧ ਹੈ। ਇਸ ਨਾਲ ਉਹਨਾਂ ਵਰਤੋਂ ਦੇ ਮਾਮਲਿਆਂ ਲਈ ਜ਼ਿਆਦਾ ਲਚਕੀਲਾਪਨ ਮਿਲਦਾ ਹੈ ਜਿੱਥੇ ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ।  

- *ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ* - Mistral Large ਵਾਂਗ, ਇਸ ਮਾਡਲ ਨੂੰ ਵੀ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ 'ਤੇ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਇਸਨੂੰ ਪਹਿਲੇ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਵਿਲੱਖਣ ਬਣਾਉਂਦਾ ਹੈ।  

### ਟੋਕਨਾਈਜ਼ਰਾਂ ਦੀ ਤੁਲਨਾ  

ਇਸ ਨਮੂਨੇ ਵਿੱਚ, ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ Mistral NeMo ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਨੂੰ Mistral Large ਨਾਲੋਂ ਕਿਵੇਂ ਸੰਭਾਲਦਾ ਹੈ।  

ਦੋਹਾਂ ਨਮੂਨੇ ਇੱਕੋ ਪ੍ਰਾਂਪਟ ਲੈਂਦੇ ਹਨ ਪਰ ਤੁਸੀਂ ਦੇਖੋਗੇ ਕਿ NeMo ਵੱਲੋਂ ਵਾਪਸ ਘੱਟ ਟੋਕਨ ਮਿਲਦੇ ਹਨ ਬਨਾਮ Mistral Large।  

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

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ Generative AI ਦੀ ਜਾਣਕਾਰੀ ਨੂੰ ਹੋਰ ਉੱਚਾ ਕਰ ਸਕੋ!

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।