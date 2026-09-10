# Building wit Mistral Models 

## Introduction 

Dis leksson go cover: 
- Exploring di diferent Mistral Models 
- Understanding di use-cases and scenarios for each model 
- Exploring code samples wey dey show di unique features of each model. 

## Di Mistral Models 

For dis leksson, we go explore 3 diferent Mistral models: 
**Mistral Large**, **Mistral Small** and **Mistral Nemo**. 

Each of dem models dey free for [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Di code for dis notebook go use dis models to run di code.

> **Note:** GitHub Models go stop for end of July 2026. Here na more details about how to use [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) to prototype wit AI models. 


## Mistral Large 2 (2407)
Mistral Large 2 na di main model from Mistral and e dey designed for enterprise use. 

Di model na upgrade to di original Mistral Large by offering 
-  Bigger Context Window - 128k vs 32k 
-  Better performance for Math and Coding Tasks - 76.9% average accuracy vs 60.4% 
-  Better multilingual performance - languages include: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi.

With dis features, Mistral Large dey perform well for 
- *Retrieval Augmented Generation (RAG)* - because e get bigger context window
- *Function Calling* - dis model get native function calling wey allow e to connect wit external tools and APIs. Dem calls fit happen both for parallel or one after di oda for sequential order. 
- *Code Generation* - dis model dey strong for Python, Java, TypeScript and C++ generation. 

### RAG Example wit Mistral Large 2 

For dis example, we dey use Mistral Large 2 to run RAG pattern on top text document. Di question dey written for Korean and e dey ask about wetin di author dey do before college. 

E use Cohere Embeddings Model to create embeddings of di text document and di question. For dis sample, e use di faiss Python package as vector store. 

Di prompt wey dem send go Mistral model get both di questions and di retrieved chunks wey dey similar to di question. Di Model then go give natural language response. 

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

# Collect dem from your Microsoft Foundry project "Overview" page
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
Mistral Small na another model for Mistral family of models under di premier/enterprise category. As di name talk, dis model na Small Language Model (SLM). Di advantages of using Mistral Small na: 
- Cost Saving compared to Mistral LLMs like Mistral Large and NeMo - 80% price drop
- Low latency - faster response compared to Mistral's LLMs
- Flexible - fit deploy for different environments wit less restrictions on needed resources. 


Mistral Small good for: 
- Text based tasks like summarization, sentiment analysis and translation. 
- Applications wey dem dey make frequent requests because e cheap 
- Low latency code tasks like review and code suggestions 

## Comparing Mistral Small and Mistral Large 

To show difference in latency between Mistral Small and Large, run di cells wey dey below. 

You go see difference for response times between 3-5 seconds. Make you also note di response lengths and style for di same prompt.  

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

Compared to di oda two models wey we discuss for dis leksson, Mistral NeMo na di only free model wey get Apache2 License. 

E dey seen as upgrade to di earlier open source LLM from Mistral, Mistral 7B. 

Some other features of di NeMo model na: 

- *More efficient tokenization:* Dis model dey use di Tekken tokenizer instead of di more common tiktoken. Dis one allow better performance for more languages and code. 

- *Finetuning:* Di base model dey available for finetuning. Dis one give more flexibility for use-cases wey need finetuning. 

- *Native Function Calling* - Like Mistral Large, dis model don train on function calling. Dis one make am unique as one of di first open source models wey do am. 


### Comparing Tokenizers 

For dis sample, we go look how Mistral NeMo handle tokenization compared to Mistral Large. 

Both samples use the same prompt but you go see say NeMo go return fewer tokens than Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Import di package wey you need:
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

# Tokenize di list of messages
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
# Import di packages wey you need:
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

# Tokenize wan list of messages
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

## Learning no stop here, make you continue di journey

After you finish dis leksson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to dey level up your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->