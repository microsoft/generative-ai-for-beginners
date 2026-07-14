# Building wit Mistral Models 

## Introduction 

Dis lesson go cover: 
- Exploring di different Mistral Models 
- Understanding di use-cases and scenarios for each model 
- Exploring code samples wey show di unique features of each model. 

## Di Mistral Models 

For dis lesson, we go explore 3 different Mistral models: 
**Mistral Large**, **Mistral Small** and **Mistral Nemo**. 

Each of these models dey free for [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Di code for dis notebook go use these models to run di code.

> **Note:** GitHub Models dey retire by di end of July 2026. Here be more details on how to use [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) to prototype wit AI models. 


## Mistral Large 2 (2407)
Mistral Large 2 na di main model from Mistral now and e dey designed for enterprise use. 

Di model na upgrade from di og original Mistral Large by giving 
-  Bigger Context Window - 128k vs 32k 
-  Better performance on Math and Coding Tasks - 76.9% average accuracy vs 60.4% 
-  Increase multilingual performance - languages include: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi.

Wit these features, Mistral Large dey sharp for 
- *Retrieval Augmented Generation (RAG)* - because e get bigger context window
- *Function Calling* - dis model get native function calling wey allow am integrate wit outside tools and APIs. Dem fit make these calls either all at once or one after di oda like sequence. 
- *Code Generation* - dis model dey shine for Python, Java, TypeScript and C++ generation. 

### RAG Example wey use Mistral Large 2 

For dis example, we dey use Mistral Large 2 run one RAG pattern for one text document. Di question dey written for Korean and e dey ask about wetin di author dey do before college. 

E dey use Cohere Embeddings Model make embeddings of di text document plus di question. For dis sample, e use di faiss Python package as di vector store. 

Di prompt wey dem send to di Mistral model get both di questions and di chunks wey dem retrieve wey similar to di question. Di Model then go give natural language response. 

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

# Comot dis one for your Microsoft Foundry project "Overview" page
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
Mistral Small na another model for di Mistral family under di premier/enterprise category. Like di name talk, dis model na Small Language Model (SLM). Di advantages of using Mistral Small na: 
- E go save cost compared to Mistral LLMs like Mistral Large and NeMo - 80% price drop
- E get low latency - e respond faster compared to Mistral's LLMs
- E flexible - fit deploy for different environments wit less restriction on wetin e need. 


Mistral Small make sense for: 
- Text based tasks like summarization, sentiment analysis and translation. 
- Applications wey dem dey do frequent requests because e cheap 
- Low latency code tasks like code review and suggestions 

## Comparing Mistral Small and Mistral Large 

To see di difference for latency between Mistral Small and Large, run di cells wey dey below. 

You go see difference in response times around 3-5 seconds. Also note di response length and style for di same prompt.  

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

Compared to di oda two models wey we talk for dis lesson, Mistral NeMo na di only free model wey get Apache2 License. 

E dey viewed as upgrade to di earlier open source LLM from Mistral, Mistral 7B. 

Some oda features of di NeMo model be: 

- *More efficient tokenization:* Dis model dey use Tekken tokenizer instead of di more common tiktoken. Dis one make am perform well for more languages and code. 

- *Finetuning:* Di base model dey available for finetuning. Dis one make am flexible for use-cases wey need finetuning. 

- *Native Function Calling* - Like Mistral Large, dis model train on function calling. Dis one make am unique as e be one of di first open source models wey gatch train for dat. 


### Comparing Tokenizers 

For dis sample, we go see how Mistral NeMo handle tokenization compared to Mistral Large. 

Both samples take di same prompt but you go notice say NeMo return fewer tokens pass Mistral Large. 

```bash
pip install mistral-common
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

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize one list of messages
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

# Tokenize one list of messages
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

## Learning no stop here, continue di journey

After you finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) make you continue to level up your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->