<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:54:09+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "bn"
}
-->
# মিস্ট্রাল মডেল নিয়ে কাজ করা

## ভূমিকা

এই পাঠে আলোচনা করা হবে:
- বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ করা
- প্রতিটি মডেলের ব্যবহার ক্ষেত্র এবং পরিস্থিতি বোঝা
- কোড উদাহরণগুলি প্রতিটি মডেলের বিশেষ বৈশিষ্ট্য প্রদর্শন করে

## মিস্ট্রাল মডেলগুলি

এই পাঠে, আমরা ৩টি ভিন্ন মিস্ট্রাল মডেল অন্বেষণ করব: **মিস্ট্রাল লার্জ**, **মিস্ট্রাল স্মল** এবং **মিস্ট্রাল নিমো**।

এই মডেলগুলি Github Model মার্কেটপ্লেসে বিনামূল্যে পাওয়া যায়। এই নোটবুকে কোড চালানোর জন্য আমরা এই মডেলগুলি ব্যবহার করব। Github Models ব্যবহার করে [AI মডেল দিয়ে প্রোটোটাইপ তৈরি করা](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) সম্পর্কে আরও বিস্তারিত এখানে রয়েছে।

## মিস্ট্রাল লার্জ ২ (2407)
মিস্ট্রাল লার্জ ২ বর্তমানে মিস্ট্রালের ফ্ল্যাগশিপ মডেল এবং এন্টারপ্রাইজ ব্যবহারের জন্য ডিজাইন করা হয়েছে।

মডেলটি মূল মিস্ট্রাল লার্জের একটি উন্নত সংস্করণ, যা প্রদান করে:
- বড় কনটেক্সট উইন্ডো - 128k বনাম 32k
- গণিত এবং কোডিং কাজের উপর ভালো পারফরম্যান্স - 76.9% গড় সঠিকতা বনাম 60.4%
- বহু ভাষায় উন্নত পারফরম্যান্স - ভাষার মধ্যে অন্তর্ভুক্ত: ইংরেজি, ফরাসি, জার্মান, স্প্যানিশ, ইতালীয়, পর্তুগিজ, ডাচ, রাশিয়ান, চীনা, জাপানি, কোরিয়ান, আরবি, এবং হিন্দি।

এই বৈশিষ্ট্যগুলির সাথে, মিস্ট্রাল লার্জ উৎকৃষ্ট:
- *রিট্রিভাল অগমেন্টেড জেনারেশন (RAG)* - বড় কনটেক্সট উইন্ডোর কারণে
- *ফাংশন কলিং* - এই মডেলটি নেটিভ ফাংশন কলিং সমর্থন করে যা বাহ্যিক টুল এবং API এর সাথে ইন্টিগ্রেশন করতে দেয়। এই কলগুলি সমান্তরাল বা ধারাবাহিকভাবে একের পর এক করা যেতে পারে।
- *কোড জেনারেশন* - এই মডেলটি পাইথন, জাভা, টাইপস্ক্রিপ্ট এবং C++ জেনারেশনে উৎকৃষ্ট।

### মিস্ট্রাল লার্জ ২ ব্যবহার করে RAG উদাহরণ

এই উদাহরণে, আমরা একটি টেক্সট ডকুমেন্টে RAG প্যাটার্ন চালানোর জন্য মিস্ট্রাল লার্জ ২ ব্যবহার করছি। প্রশ্নটি কোরিয়ানে লেখা এবং কলেজের আগে লেখকের কর্মকাণ্ড সম্পর্কে জানতে চায়।

এটি Cohere Embeddings Model ব্যবহার করে টেক্সট ডকুমেন্ট এবং প্রশ্নের এম্বেডিং তৈরি করে। এই নমুনার জন্য, এটি faiss পাইথন প্যাকেজ ব্যবহার করে একটি ভেক্টর স্টোর হিসেবে।

মিস্ট্রাল মডেলে পাঠানো প্রম্পটে প্রশ্ন এবং প্রশ্নের সাথে সাদৃশ্যপূর্ণ উদ্ধার করা অংশগুলি অন্তর্ভুক্ত থাকে। তারপর মডেলটি একটি প্রাকৃতিক ভাষায় উত্তর প্রদান করে।

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

## মিস্ট্রাল স্মল
মিস্ট্রাল স্মল মিস্ট্রাল মডেল পরিবারের একটি মডেল যা প্রিমিয়ার/এন্টারপ্রাইজ শ্রেণীতে অন্তর্ভুক্ত। নাম অনুসারে, এই মডেলটি একটি ছোট ভাষার মডেল (SLM)। মিস্ট্রাল স্মল ব্যবহারের সুবিধাগুলি হল:
- মিস্ট্রাল LLMs যেমন মিস্ট্রাল লার্জ এবং NeMo এর তুলনায় খরচ সাশ্রয়ী - 80% মূল্য হ্রাস
- কম লেটেন্সি - মিস্ট্রালের LLMs এর তুলনায় দ্রুত প্রতিক্রিয়া
- নমনীয় - কম সংস্থান প্রয়োজনের সীমাবদ্ধতা সহ বিভিন্ন পরিবেশে স্থাপন করা যেতে পারে।

মিস্ট্রাল স্মল উৎকৃষ্ট:
- টেক্সট ভিত্তিক কাজ যেমন সারসংক্ষেপ, অনুভূতি বিশ্লেষণ এবং অনুবাদ।
- এমন অ্যাপ্লিকেশন যেখানে তার খরচ কার্যকারিতা কারণে ঘন ঘন অনুরোধ করা হয়
- কম লেটেন্সি কোড কাজ যেমন পর্যালোচনা এবং কোড সুপারিশ

## মিস্ট্রাল স্মল এবং মিস্ট্রাল লার্জ তুলনা করা

মিস্ট্রাল স্মল এবং লার্জের মধ্যে লেটেন্সির পার্থক্য দেখাতে, নিচের কোষগুলি চালান।

আপনার ৩-৫ সেকেন্ডের মধ্যে প্রতিক্রিয়া সময়ের পার্থক্য দেখতে হবে। একই প্রম্পটে প্রতিক্রিয়ার দৈর্ঘ্য এবং শৈলীও লক্ষ্য করুন।

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

## মিস্ট্রাল নিমো

এই পাঠে আলোচিত অন্য দুটি মডেলের তুলনায়, মিস্ট্রাল নিমো একমাত্র বিনামূল্যে মডেল যা Apache2 লাইসেন্স সহ আসে।

এটি মিস্ট্রালের পূর্বের ওপেন সোর্স LLM, মিস্ট্রাল 7B এর একটি উন্নত সংস্করণ হিসেবে দেখা হয়।

নিমো মডেলের কিছু অন্যান্য বৈশিষ্ট্য হল:

- *অধিক কার্যকর টোকেনাইজেশন:* এই মডেলটি সাধারণত ব্যবহৃত tiktoken এর পরিবর্তে Tekken টোকেনাইজার ব্যবহার করে। এটি অধিক ভাষা এবং কোডের উপর ভালো পারফরম্যান্স দেয়।

- *ফাইনটিউনিং:* বেস মডেলটি ফাইনটিউনিং এর জন্য উপলব্ধ। এটি এমন ব্যবহার ক্ষেত্রে যেখানে ফাইনটিউনিং প্রয়োজন হতে পারে তার জন্য অধিক নমনীয়তা দেয়।

- *নেটিভ ফাংশন কলিং* - মিস্ট্রাল লার্জের মতো, এই মডেলটি ফাংশন কলিংয়ে প্রশিক্ষিত হয়েছে। এটি প্রথম ওপেন সোর্স মডেলগুলির মধ্যে একটি যা এটি করতে সক্ষম।

### টোকেনাইজার তুলনা

এই নমুনায়, আমরা দেখব কিভাবে মিস্ট্রাল নিমো টোকেনাইজেশন পরিচালনা করে মিস্ট্রাল লার্জের তুলনায়।

উভয় নমুনা একই প্রম্পট নেয় কিন্তু আপনি দেখতে পাবেন যে নিমো কম টোকেন ফেরত দেয় মিস্ট্রাল লার্জের তুলনায়।

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

## শেখা এখানেই থেমে থাকে না, যাত্রা চালিয়ে যান

এই পাঠ সম্পন্ন করার পর, আমাদের [জেনারেটিভ AI লার্নিং সংগ্রহ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন আপনার জেনারেটিভ AI জ্ঞান আরও উন্নত করতে!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিকেই নির্ভরযোগ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে উদ্ভূত কোন ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।