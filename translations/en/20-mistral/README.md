<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:54:58+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "en"
}
-->
# Building with Mistral Models 

## Introduction 

This lesson will cover: 
- Exploring the different Mistral Models 
- Understanding the use cases and scenarios for each model 
- Code samples demonstrating the unique features of each model. 

## The Mistral Models 

In this lesson, we will explore 3 different Mistral models: 
**Mistral Large**, **Mistral Small**, and **Mistral NeMo**. 

Each of these models is available for free on the Github Model marketplace. The code in this notebook will use these models to run the examples. Here are more details on using Github Models to [prototype with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 


## Mistral Large 2 (2407)
Mistral Large 2 is currently the flagship model from Mistral and is designed for enterprise use. 

This model is an upgrade to the original Mistral Large, offering 
-  Larger Context Window - 128k vs 32k 
-  Better performance on Math and Coding Tasks - 76.9% average accuracy vs 60.4% 
-  Improved multilingual capabilities - supporting English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, and Hindi.

With these features, Mistral Large excels at 
- *Retrieval Augmented Generation (RAG)* - thanks to the larger context window
- *Function Calling* - this model supports native function calling, enabling integration with external tools and APIs. These calls can be made either in parallel or sequentially. 
- *Code Generation* - this model performs especially well with Python, Java, TypeScript, and C++ code generation. 

### RAG Example using Mistral Large 2 

In this example, we use Mistral Large 2 to perform a RAG pattern over a text document. The question is written in Korean and asks about the author's activities before college. 

It uses the Cohere Embeddings Model to create embeddings for both the text document and the question. For this example, the faiss Python package is used as a vector store. 

The prompt sent to the Mistral model includes both the question and the retrieved chunks that are similar to the question. The model then generates a natural language response. 

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
Mistral Small is another model in the Mistral family, positioned under the premier/enterprise category. As the name suggests, this is a Small Language Model (SLM). The benefits of using Mistral Small include: 
- Cost savings compared to larger Mistral LLMs like Mistral Large and NeMo - up to 80% cheaper
- Low latency - faster response times compared to Mistral's larger LLMs
- Flexibility - can be deployed across various environments with fewer resource requirements. 


Mistral Small is ideal for: 
- Text-based tasks such as summarization, sentiment analysis, and translation. 
- Applications with frequent requests due to its cost efficiency 
- Low latency code tasks like code review and suggestions 

## Comparing Mistral Small and Mistral Large 

To see the difference in latency between Mistral Small and Large, run the cells below. 

You should notice a difference in response times of about 3-5 seconds. Also, observe the differences in response length and style for the same prompt.  

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

Compared to the other two models discussed in this lesson, Mistral NeMo is the only free model with an Apache2 License. 

It is considered an upgrade to the earlier open source LLM from Mistral, Mistral 7B. 

Some other features of the NeMo model include: 

- *More efficient tokenization:* This model uses the Tekken tokenizer instead of the more commonly used tiktoken. This results in better performance across more languages and code. 

- *Finetuning:* The base model is available for finetuning, providing more flexibility for use cases that require customization. 

- *Native Function Calling* - Like Mistral Large, this model has been trained on function calling, making it one of the first open source models to support this feature. 


### Comparing Tokenizers 

In this example, we compare how Mistral NeMo handles tokenization versus Mistral Large. 

Both samples use the same prompt, but you should see that NeMo returns fewer tokens compared to Mistral Large. 

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

## Learning does not stop here, continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to keep advancing your Generative AI skills!

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.