<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:14:18+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "bn"
}
-->
# মিস্ট্রাল মডেল দিয়ে তৈরি করা

## পরিচিতি

এই পাঠে আলোচনা করা হবে:
- বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ
- প্রতিটি মডেলের ব্যবহার-কেস এবং পরিস্থিতি বোঝা
- কোড নমুনা প্রতিটি মডেলের অনন্য বৈশিষ্ট্য প্রদর্শন করে

## মিস্ট্রাল মডেলসমূহ

এই পাঠে, আমরা ৩টি ভিন্ন মিস্ট্রাল মডেল অন্বেষণ করব: **মিস্ট্রাল লার্জ**, **মিস্ট্রাল স্মল** এবং **মিস্ট্রাল নেমো**।

প্রতিটি মডেল Github Model মার্কেটপ্লেসে বিনামূল্যে উপলব্ধ। এই নোটবুকের কোডটি এই মডেলগুলি ব্যবহার করে কোড চালাবে। এখানে আরও তথ্য রয়েছে Github Models ব্যবহার করে [AI মডেল দিয়ে প্রোটোটাইপ তৈরি করা](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)।

## মিস্ট্রাল লার্জ ২ (২৪০৭)

মিস্ট্রাল লার্জ ২ বর্তমানে মিস্ট্রালের প্রধান মডেল এবং এটি এন্টারপ্রাইজ ব্যবহারের জন্য ডিজাইন করা হয়েছে।

এই মডেলটি মূল মিস্ট্রাল লার্জের আপগ্রেড, যা অফার করে:
- বৃহত্তর প্রসঙ্গ উইন্ডো - ১২৮k বনাম ৩২k
- গণিত এবং কোডিং কাজের উপর উন্নত পারফরম্যান্স - ৭৬.৯% গড় সঠিকতা বনাম ৬০.৪%
- বহুভাষিক পারফরম্যান্স বৃদ্ধি - ভাষাগুলি অন্তর্ভুক্ত: ইংরেজি, ফরাসি, জার্মান, স্প্যানিশ, ইতালিয়ান, পর্তুগিজ, ডাচ, রাশিয়ান, চীনা, জাপানি, কোরিয়ান, আরবি এবং হিন্দি।

এই বৈশিষ্ট্যগুলির সাথে, মিস্ট্রাল লার্জ উজ্জ্বল:
- *রিট্রিভাল অগমেন্টেড জেনারেশন (RAG)* - বৃহত্তর প্রসঙ্গ উইন্ডোর কারণে
- *ফাংশন কলিং* - এই মডেলটির নেটিভ ফাংশন কলিং রয়েছে যা বাইরের টুল এবং API-এর সাথে সংহতকরণের অনুমতি দেয়। এই কলগুলি একসাথে বা ক্রমানুসারে একের পর এক করা যেতে পারে।
- *কোড জেনারেশন* - এই মডেলটি পাইথন, জাভা, টাইপস্ক্রিপ্ট এবং C++ জেনারেশনে উৎকৃষ্ট।

### RAG উদাহরণ ব্যবহার করে মিস্ট্রাল লার্জ ২

এই উদাহরণে, আমরা একটি পাঠ্য নথির উপর RAG প্যাটার্ন চালানোর জন্য মিস্ট্রাল লার্জ ২ ব্যবহার করছি। প্রশ্নটি কোরিয়ান ভাষায় লেখা এবং কলেজের আগে লেখকের কার্যকলাপ সম্পর্কে জানতে চায়।

এটি Cohere Embeddings Model ব্যবহার করে পাঠ্য নথির পাশাপাশি প্রশ্নের এমবেডিং তৈরি করে। এই নমুনার জন্য, এটি faiss পাইথন প্যাকেজকে ভেক্টর স্টোর হিসাবে ব্যবহার করে।

মিস্ট্রাল মডেলে পাঠানো প্রম্পটটিতে প্রশ্ন এবং প্রশ্নের সাথে মিলিত হওয়া চাঙ্কগুলি অন্তর্ভুক্ত রয়েছে। মডেলটি তখন একটি প্রাকৃতিক ভাষার উত্তর প্রদান করে।

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

মিস্ট্রাল স্মল মডেলটি মিস্ট্রাল পরিবারের মডেলগুলির মধ্যে একটি প্রিমিয়ার/এন্টারপ্রাইজ ক্যাটাগরিতে অন্তর্ভুক্ত। নামের মতোই, এই মডেলটি একটি ছোট ভাষার মডেল (SLM)। মিস্ট্রাল স্মল ব্যবহারের সুবিধাগুলি হল:
- মিস্ট্রাল LLMs যেমন মিস্ট্রাল লার্জ এবং NeMo এর তুলনায় খরচ সাশ্রয়ী - ৮০% মূল্য হ্রাস
- কম লেটেন্সি - মিস্ট্রালের LLMs এর তুলনায় দ্রুত প্রতিক্রিয়া
- নমনীয় - বিভিন্ন পরিবেশে কম সংস্থান প্রয়োজনীয়তার সাথে মোতায়েন করা যেতে পারে।

মিস্ট্রাল স্মল চমৎকার:
- পাঠ্য ভিত্তিক কাজ যেমন সারসংক্ষেপ, অনুভূতি বিশ্লেষণ এবং অনুবাদ
- অ্যাপ্লিকেশন যেখানে এর খরচ কার্যকারিতার কারণে ঘন ঘন অনুরোধ করা হয়
- কম লেটেন্সি কোড কাজ যেমন পর্যালোচনা এবং কোড পরামর্শ

## মিস্ট্রাল স্মল এবং মিস্ট্রাল লার্জের তুলনা

মিস্ট্রাল স্মল এবং লার্জের মধ্যে লেটেন্সির পার্থক্য দেখানোর জন্য, নিচের সেলগুলি চালান।

আপনি ৩-৫ সেকেন্ডের মধ্যে প্রতিক্রিয়ার সময়ের পার্থক্য দেখতে পাবেন। একই প্রম্পটের উপর প্রতিক্রিয়ার দৈর্ঘ্য এবং শৈলীও লক্ষ্য করুন।

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

## মিস্ট্রাল নেমো

এই পাঠে আলোচনা করা অন্য দুটি মডেলের তুলনায়, মিস্ট্রাল নেমো হল একমাত্র বিনামূল্যের মডেল যা Apache2 লাইসেন্স সহ উপলব্ধ।

এটি মিস্ট্রালের পূর্বের ওপেন সোর্স LLM, মিস্ট্রাল ৭B-এর আপগ্রেড হিসেবে দেখা হয়।

নেমো মডেলের কিছু অন্যান্য বৈশিষ্ট্য হল:

- *অধিক কার্যকর টোকেনাইজেশন:* এই মডেলটি সাধারণত ব্যবহৃত tiktoken-এর পরিবর্তে টেকেন টোকেনাইজার ব্যবহার করে। এটি আরও ভাষা এবং কোডের উপর ভাল পারফরম্যান্সের অনুমতি দেয়।

- *ফাইনটিউনিং:* বেস মডেলটি ফাইনটিউনিংয়ের জন্য উপলব্ধ। এটি সেই ব্যবহার-কেসগুলির জন্য আরও নমনীয়তা প্রদান করে যেখানে ফাইনটিউনিং প্রয়োজন হতে পারে।

- *নেটিভ ফাংশন কলিং* - মিস্ট্রাল লার্জের মতো, এই মডেলটি ফাংশন কলিংয়ে প্রশিক্ষিত হয়েছে। এটি এটিকে প্রথম ওপেন সোর্স মডেলগুলির মধ্যে একটি হিসাবে অনন্য করে তোলে।

### টোকেনাইজারগুলির তুলনা

এই নমুনায়, আমরা মিস্ট্রাল নেমো কীভাবে টোকেনাইজেশন পরিচালনা করে তা মিস্ট্রাল লার্জের সাথে তুলনা করে দেখব।

উভয় নমুনা একই প্রম্পট গ্রহণ করে কিন্তু আপনি দেখতে পাবেন যে নেমো মিস্ট্রাল লার্জের তুলনায় কম টোকেন ফেরত দেয়।

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

এই পাঠ সম্পন্ন করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন আপনার Generative AI জ্ঞান আরও উন্নত করতে!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাযথতার জন্য প্রচেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটি প্রামাণ্য সূত্র হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।