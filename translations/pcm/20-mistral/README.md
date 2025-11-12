<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-11-12T08:54:14+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "pcm"
}
-->
# How to Build wit Mistral Models

## Introduction

Dis lesson go cover:
- How to sabi di different Mistral Models
- Di kain work wey each model fit do and di situations wey dem dey useful
- Code samples wey go show di special features of each model.

## Di Mistral Models

For dis lesson, we go look three different Mistral models:
**Mistral Large**, **Mistral Small**, and **Mistral Nemo**.

All dis models dey free for Github Model marketplace. Di code wey dey dis notebook go use dis models to run di code. You fit find more info about how to use Github Models to [prototype wit AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 na di main model wey Mistral get now and dem design am for big companies.

Dis model na upgrade to di original Mistral Large and e dey offer:
- Bigger Context Window - 128k instead of 32k
- Better performance for Math and Coding Tasks - 76.9% average accuracy instead of 60.4%
- Better performance for plenty languages - di languages include: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi.

Wit all dis features, Mistral Large dey good for:
- *Retrieval Augmented Generation (RAG)* - because e get bigger context window
- *Function Calling* - dis model sabi call functions wey fit connect wit external tools and APIs. Di calls fit happen at di same time or one after di other.
- *Code Generation* - dis model sabi generate code for Python, Java, TypeScript, and C++.

### RAG Example wit Mistral Large 2

For dis example, we dey use Mistral Large 2 to run RAG pattern for one text document. Di question dey write for Korean and e dey ask about wetin di author do before e enter college.

E dey use Cohere Embeddings Model to create embeddings for di text document and di question. For dis sample, e dey use di faiss Python package as vector store.

Di prompt wey dem send to di Mistral model get di question and di chunks wey resemble di question. Di model go then give natural language answer.

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

Mistral Small na another model for di Mistral family of models wey dey under di premier/enterprise category. As di name talk, dis model na Small Language Model (SLM). Di benefits of using Mistral Small na:
- E dey save money compared to Mistral LLMs like Mistral Large and NeMo - 80% price drop
- E dey fast - e dey respond quicker compared to Mistral's LLMs
- E dey flexible - e fit work for different environments wit less wahala for resources.

Mistral Small dey good for:
- Text-based work like summarization, sentiment analysis, and translation.
- Apps wey dey make plenty requests because e dey cheap.
- Low latency code work like review and code suggestions.

## How Mistral Small and Mistral Large take compare

To show di difference for latency between Mistral Small and Large, run di cells wey dey below.

You go see di difference for response time wey dey between 3-5 seconds. Also check di response length and style for di same prompt.

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

Compared to di other two models wey we don talk about for dis lesson, Mistral NeMo na di only free model wey get Apache2 License.

People dey see am as upgrade to di earlier open-source LLM from Mistral, Mistral 7B.

Some other features wey NeMo model get na:

- *Better tokenization:* Dis model dey use Tekken tokenizer instead of di common tiktoken. Dis one dey make am perform better for plenty languages and code.

- *Finetuning:* Di base model dey available for finetuning. Dis one dey make am flexible for situations wey need finetuning.

- *Native Function Calling* - Like Mistral Large, dis model don train for function calling. Dis one make am special as e be one of di first open-source models wey sabi do dis.

### How Tokenizers take compare

For dis sample, we go look how Mistral NeMo dey handle tokenization compared to Mistral Large.

Both samples go use di same prompt but you go see say NeMo go return less tokens compared to Mistral Large.

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


## Learning no dey finish here, continue di Journey

After you don finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more about Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make sure say e correct, abeg make you sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->