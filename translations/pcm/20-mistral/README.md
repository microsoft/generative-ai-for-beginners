# Building wit Mistral Models 

## Introduction 

Dis lesson go cover: 
- Exploring di different Mistral Models 
- Understanding di use-cases an scenarios for each model 
- Exploring code samples wey show di unique features of each model. 

## Di Mistral Models 

For dis lesson, we go explore 3 different Mistral models: 
**Mistral Large**, **Mistral Small** an **Mistral Nemo**. 

Each of dese models dey available free for di GitHub Model marketplace. Di code for dis notebook go dey use dese models to run di code. Here na more details on how to use GitHub Models to [prototype wit AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 


## Mistral Large 2 (2407)
Mistral Large 2 na di current flagship model from Mistral an e dey designed for enterprise use. 

Di model na upgrade to di original Mistral Large by offering 
-  Larger Context Window - 128k vs 32k 
-  Better performance on Math an Coding Tasks - 76.9% average accuracy vs 60.4% 
-  Increased multilingual performance - languages include: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, an Hindi.

Wit dese features, Mistral Large sabi wella for 
- *Retrieval Augmented Generation (RAG)* - because of di larger context window
- *Function Calling* - dis model get native function calling wey allow integration wit external tools an APIs. Dem calls fit be made both in parallel or one after di other in a sequential order. 
- *Code Generation* - dis model sabi well for Python, Java, TypeScript an C++ generation. 

### RAG Example wit Mistral Large 2 

For dis example, we dey use Mistral Large 2 run a RAG pattern over text document. Di question write for Korean an e dey ask about wetin di author do before college. 

E use Cohere Embeddings Model to create embeddings of di text document as well as di question. For dis sample, e use di faiss Python package as vector store. 

Di prompt wey dem send go di Mistral model get both di question an di retrieved chunks wey resemble di question. Di Model then go give natural language response. 

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
Mistral Small na another model for di Mistral family under di premier/enterprise category. As di name talk, dis model na Small Language Model (SLM). Di advantages of using Mistral Small na: 
- E dey save cost compared to Mistral LLMs like Mistral Large an NeMo - 80% price drop
- Low latency - e dey faster for response compared to Mistral's LLMs
- Flexible - fit deploy for different environments wit less restrictions on wetin resources e need. 


Mistral Small dey good for: 
- Text based tasks like summarization, sentiment analysis an translation. 
- Applications wey dem dey ask question many times because e dey cost effective 
- Low latency code tasks like review an code suggestions 

## Comparing Mistral Small an Mistral Large 

To show difference for latency between Mistral Small an Large, run di cells wey dey below. 

You go see difference for response times witin 3-5 seconds. Also check di response lengths an style on top di same prompt.  

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

Compared to di oda two models wey we talk about for dis lesson, Mistral NeMo na di only free model wey get Apache2 License. 

E dey seen as upgrade to di earlier open source LLM from Mistral, Mistral 7B. 

Some oda features of di NeMo model na: 

- *More efficient tokenization:* Dis model dey use di Tekken tokenizer over di more common tiktoken. Dis one dey allow better performance across more languages an code. 

- *Finetuning:* Di base model dey available for finetuning. Dis one go allow more flexibility for use-cases wey need finetuning. 

- *Native Function Calling* - Like Mistral Large, dis model don train on function calling. Dis one make am unique as e be one of di first open source models to do am. 


### Comparing Tokenizers 

For dis sample, we go look how Mistral NeMo dey handle tokenization compared to Mistral Large. 

Both samples go take di same prompt but you go see say NeMo dey return fewer tokens than Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Bring in di packages wey we need:
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

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Break list of messages into tokens
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

# Count how many tokens dey
print(len(tokens))
```

```python
# Bring in di packages wey we need:
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

# Tokenize list of messages dem
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

# Count how many tokens dey
print(len(tokens))
```

## Learning no stop for here, continue di journey

After you don finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to level up your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document dem don translate am wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg note say automated translation fit get mistakes or no too correct. The original document wey e dey for im own language na im be the correct source. If na serious matter, e better make human professional do the translation. We no go take responsibility if person no understand well or if person misunderstand because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->