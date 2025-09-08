<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:58:03+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "bn"
}
-->
# Mistral মডেল দিয়ে নির্মাণ

## পরিচিতি

এই পাঠে আমরা আলোচনা করব:  
- বিভিন্ন Mistral মডেল অন্বেষণ  
- প্রতিটি মডেলের ব্যবহার ক্ষেত্র এবং পরিস্থিতি বোঝা  
- কোড নমুনা যা প্রতিটি মডেলের অনন্য বৈশিষ্ট্য প্রদর্শন করে।

## Mistral মডেলসমূহ

এই পাঠে, আমরা ৩টি ভিন্ন Mistral মডেল অন্বেষণ করব:  
**Mistral Large**, **Mistral Small** এবং **Mistral Nemo**।

এই মডেলগুলো Github Model মার্কেটপ্লেসে বিনামূল্যে পাওয়া যায়। এই নোটবুকে ব্যবহৃত কোডগুলো এই মডেলগুলো ব্যবহার করে চলবে। Github Models ব্যবহার করে [AI মডেল দিয়ে প্রোটোটাইপ তৈরি](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) করার আরও বিস্তারিত এখানে পাওয়া যাবে।

## Mistral Large 2 (2407)

Mistral Large 2 বর্তমানে Mistral এর প্রধান মডেল এবং এটি এন্টারপ্রাইজ ব্যবহারের জন্য ডিজাইন করা হয়েছে।

এই মডেলটি মূল Mistral Large এর আপগ্রেড সংস্করণ যা প্রদান করে:  
- বড় কনটেক্সট উইন্ডো - ১২৮কে বনাম ৩২কে  
- গণিত এবং কোডিং টাস্কে উন্নত পারফরম্যান্স - গড় সঠিকতা ৭৬.৯% বনাম ৬০.৪%  
- বহুভাষিক পারফরম্যান্স বৃদ্ধি - ভাষাগুলো হলো: ইংরেজি, ফরাসি, জার্মান, স্প্যানিশ, ইতালিয়ান, পর্তুগিজ, ডাচ, রাশিয়ান, চীনা, জাপানি, কোরিয়ান, আরবি এবং হিন্দি।

এই বৈশিষ্ট্যগুলোর মাধ্যমে Mistral Large বিশেষভাবে দক্ষ:  
- *Retrieval Augmented Generation (RAG)* - বড় কনটেক্সট উইন্ডোর কারণে  
- *Function Calling* - এই মডেলটি নেটিভ ফাংশন কলিং সমর্থন করে যা বাইরের টুল এবং API এর সাথে ইন্টিগ্রেশন সহজ করে। এই কলগুলো সমান্তরাল বা ধারাবাহিকভাবে করা যায়।  
- *Code Generation* - Python, Java, TypeScript এবং C++ কোড জেনারেশনে এই মডেলটি খুবই দক্ষ।

### Mistral Large 2 ব্যবহার করে RAG উদাহরণ

এই উদাহরণে, আমরা Mistral Large 2 ব্যবহার করে একটি টেক্সট ডকুমেন্টের উপর RAG প্যাটার্ন চালাচ্ছি। প্রশ্নটি কোরিয়ান ভাষায় লেখা এবং লেখকের কলেজের আগে কার্যকলাপ সম্পর্কে জানতে চায়।

এটি Cohere Embeddings Model ব্যবহার করে টেক্সট ডকুমেন্ট এবং প্রশ্নের এম্বেডিং তৈরি করে। এই নমুনায় faiss Python প্যাকেজ ভেক্টর স্টোর হিসেবে ব্যবহৃত হয়েছে।

Mistral মডেলে পাঠানো প্রম্পটে প্রশ্ন এবং প্রশ্নের সাথে মিল থাকা রিট্রিভড অংশগুলো অন্তর্ভুক্ত থাকে। মডেল তারপর একটি প্রাকৃতিক ভাষার উত্তর প্রদান করে।

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

Mistral Small হলো Mistral পরিবারের আরেকটি মডেল যা প্রিমিয়ার/এন্টারপ্রাইজ ক্যাটাগরির অন্তর্ভুক্ত। নাম অনুসারে, এটি একটি ছোট ভাষা মডেল (SLM)। Mistral Small ব্যবহারের সুবিধাগুলো হলো:  
- Mistral Large এবং NeMo এর মতো বড় LLM এর তুলনায় খরচ সাশ্রয়ী - ৮০% দাম কম  
- কম লেটেন্সি - Mistral এর বড় LLM গুলোর তুলনায় দ্রুত প্রতিক্রিয়া  
- নমনীয় - বিভিন্ন পরিবেশে কম রিসোর্সের প্রয়োজনীয়তা নিয়ে সহজে ডিপ্লয় করা যায়।

Mistral Small উপযুক্ত:  
- টেক্সট ভিত্তিক কাজ যেমন সারাংশ তৈরি, অনুভূতি বিশ্লেষণ এবং অনুবাদ  
- যেখানে ঘন ঘন অনুরোধ আসে, সেক্ষেত্রে খরচ সাশ্রয়ের জন্য  
- কম লেটেন্সি কোড কাজ যেমন রিভিউ এবং কোড সাজেশন

## Mistral Small এবং Mistral Large এর তুলনা

Mistral Small এবং Large এর লেটেন্সির পার্থক্য দেখানোর জন্য নিচের সেলগুলো চালান।

একই প্রম্পটের জন্য ৩-৫ সেকেন্ডের মধ্যে প্রতিক্রিয়ার সময়ের পার্থক্য দেখতে পাবেন। এছাড়াও প্রতিক্রিয়ার দৈর্ঘ্য এবং শৈলী লক্ষ্য করুন।

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

এই পাঠে আলোচিত অন্য দুই মডেলের তুলনায়, Mistral NeMo একমাত্র বিনামূল্যের মডেল যার Apache2 লাইসেন্স রয়েছে।

এটি Mistral এর আগের ওপেন সোর্স LLM, Mistral 7B এর আপগ্রেড হিসেবে বিবেচিত।

NeMo মডেলের কিছু অন্যান্য বৈশিষ্ট্য হলো:

- *আরও দক্ষ টোকেনাইজেশন:* এই মডেলটি tiktoken এর পরিবর্তে Tekken tokenizer ব্যবহার করে। এর ফলে আরও বেশি ভাষা এবং কোডে উন্নত পারফরম্যান্স পাওয়া যায়।

- *ফাইনটিউনিং:* বেস মডেলটি ফাইনটিউনিংয়ের জন্য উপলব্ধ। এটি এমন ব্যবহার ক্ষেত্রের জন্য বেশি নমনীয়তা দেয় যেখানে ফাইনটিউনিং প্রয়োজন হতে পারে।

- *নেটিভ ফাংশন কলিং* - Mistral Large এর মতো, এই মডেলটিও ফাংশন কলিং এর জন্য প্রশিক্ষিত। এটি এটিকে প্রথম ওপেন সোর্স মডেলগুলোর মধ্যে একটি হিসেবে বিশেষ করে তোলে।

### টোকেনাইজার তুলনা

এই নমুনায়, আমরা দেখব Mistral NeMo কিভাবে Mistral Large এর তুলনায় টোকেনাইজেশন পরিচালনা করে।

উভয় নমুনা একই প্রম্পট নেয়, কিন্তু আপনি দেখতে পাবেন NeMo তুলনামূলকভাবে কম টোকেন ফেরত দেয়।

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

## শেখা এখানেই শেষ নয়, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন এবং আপনার Generative AI জ্ঞানে আরও উন্নতি করুন!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।