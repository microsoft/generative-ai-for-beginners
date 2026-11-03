# Building with Mistral Models 

## Introduction 

This lesson will cover: 
- Exploring the different Mistral Models 
- Understanding the use-cases and scenarios for each model 
- Exploring code samples that show the unique features of each model. 

## The Mistral Models 

In this lesson, we will explore 3 different Mistral models: 
**Mistral Large**, **Mistral Small** and **Mistral Nemo**. 

Mistral Large and Mistral Small are available on [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) and are billed pay-as-you-go to your Azure subscription. Mistral NeMo is no longer offered on Foundry, so this lesson only uses its tokenizer, which runs locally without an API call.

> **Note:** GitHub Models was retired at the end of July 2026, so this lesson uses Microsoft Foundry Models. Here are more details on using [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) to prototype with AI models. 


## Mistral Large 3
Mistral Large 3 is currently the flagship model from Mistral and is designed for enterprise use. On Microsoft Foundry it is available with the model ID `Mistral-Large-3`.

> **Note:** Earlier versions of this lesson used Mistral Large 2 (`Mistral-large-2407`). That model and its successor `Mistral-large-2411` have been retired from Microsoft Foundry, so the samples now use Mistral Large 3.

Compared to earlier Mistral Large versions, the model offers
-  Larger Context Window - up to 256k tokens
-  Open weights under the Apache 2.0 License, using a sparse Mixture-of-Experts (MoE) architecture
-  Strong multilingual performance - languages include: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi.

With these features, Mistral Large excels at 
- *Retrieval Augmented Generation (RAG)* - due to the larger context window
- *Function Calling* - this model has native function calling which allows integration with external tools and APIs. These calls can be made both in parallel or one after another in a sequential order. 
- *Code Generation* - this model excels on Python, Java, TypeScript and C++ generation. 

### RAG Example using Mistral Large 3 

In this example, we are using Mistral Large 3 to run a RAG pattern over a text document. The question is written in Korean and asks about the author's activities before college. 

It uses the Cohere Embed v4 model (`embed-v-4-0`) to create embeddings of the text document as well as the question. For this sample, it uses the faiss Python package as a vector store. 

The samples call Microsoft Foundry Models with the `openai` Python package (`pip install openai`) through the Foundry resource's OpenAI-compatible `/openai/v1/` endpoint. 

The prompt sent to the Mistral model includes both the questions and the retrieved chunks that are similar to the question. The Model then provides a natural language response. 

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from openai import OpenAI

# Get these from your Microsoft Foundry project's "Overview" page
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-Large-3"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

# The openai SDK uses the Foundry resource's OpenAI-compatible /openai/v1/ route.
# This works whether your endpoint is the resource URL, ends in /models, or is a project endpoint.
# e.g. https://<resource>.services.ai.azure.com/models -> https://<resource>.services.ai.azure.com/openai/v1/
resource_url = endpoint.split("/api/projects")[0].split("/models")[0].split("/openai")[0].rstrip("/")
base_url = f"{resource_url}/openai/v1/"

client = OpenAI(
    base_url=base_url,
    api_key=token,
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "embed-v-4-0" # Cohere Embed v4

# The same client is used to create embeddings
embed_response = client.embeddings.create(
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

question_embedding = client.embeddings.create(
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


chat_response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small 
Mistral Small is another model in the Mistral family of models under the premier/enterprise category. As the name implies, this model is a Small Language Model (SLM). The advantages of using Mistral Small are that it is: 
- Cost Saving compared to Mistral LLMs like Mistral Large and NeMo - 80% price drop
- Low latency - faster response compared to Mistral's LLMs
- Flexible - can be deployed across different environments with less restrictions on required resources. 


Mistral Small is great for: 
- Text based tasks such as summarization, sentiment analysis and translation. 
- Applications where frequent requests are made due to its cost effectiveness 
- Low latency code tasks like review and code suggestions 

> **Note:** The original `Mistral-small` model has been retired from Microsoft Foundry. The samples use `mistral-small-2503` (Mistral Small 3.1). Models are retired over time, so check the [Foundry model retirement schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule?WT.mc_id=academic-105485-koreyst) and use the newest Mistral Small available in your Foundry catalog if this one has been retired.

## Comparing Mistral Small and Mistral Large 

To show differences in latency between Mistral Small and Large, run the below cells. 

You should see a difference in response times between 3-5 seconds. Also note the response lengths and style over the same prompt.  

```python 

import os 
from openai import OpenAI

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "mistral-small-2503"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

# Point the openai SDK at the Foundry resource's /openai/v1/ route
# e.g. https://<resource>.services.ai.azure.com/models -> https://<resource>.services.ai.azure.com/openai/v1/
resource_url = endpoint.split("/api/projects")[0].split("/models")[0].split("/openai")[0].rstrip("/")
base_url = f"{resource_url}/openai/v1/"

client = OpenAI(
    base_url=base_url,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Can you write a Python function to the fizz buzz test?"},
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
from openai import OpenAI

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-Large-3"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

# Point the openai SDK at the Foundry resource's /openai/v1/ route
# e.g. https://<resource>.services.ai.azure.com/models -> https://<resource>.services.ai.azure.com/openai/v1/
resource_url = endpoint.split("/api/projects")[0].split("/models")[0].split("/openai")[0].rstrip("/")
base_url = f"{resource_url}/openai/v1/"

client = OpenAI(
    base_url=base_url,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Can you write a Python function to the fizz buzz test?"},
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

Mistral NeMo is an open model released under the Apache 2.0 License. 

It is viewed as an upgrade to the earlier open source LLM from Mistral, Mistral 7B. 

Some other features of the NeMo model are: 

- *More efficient tokenization:* This model uses the Tekken tokenizer over the more commonly used tiktoken. This allows for better performance over more languages and code. 

- *Finetuning:* The base model is available for finetuning. This allows for more flexibility for use-cases where finetuning may be needed. 

- *Native Function Calling* - Like Mistral Large, this model has been trained on function calling. This makes it unique as being one of the first open source models to do so. 


### Comparing Tokenizers 

In this sample, we will look at how Mistral NeMo handles tokenization compared to Mistral Large. 

Both samples take the same prompt but you should see that NeMo returns fewer tokens than Mistral Large. 

> **Note:** Mistral NeMo is no longer offered in the Microsoft Foundry model catalog. The tokenizer samples below run locally with the `mistral-common` package, so they don't need a model deployment or API key.

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

model_name = "open-mistral-nemo"

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

# Count the number of tokens
print(len(tokens))
```

## Learning does not stop here, continue the journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!
