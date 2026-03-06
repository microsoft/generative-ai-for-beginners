# মিস্ট্রাল মডেল দিয়ে নির্মাণ

## পরিচিতি

এই পাঠে আলোচনা করা হবে:  
- বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ  
- প্রতিটি মডেলের ব্যবহার ক্ষেত্র এবং পরিস্থিতি বোঝা  
- প্রতিটি মডেলের অনন্য বৈশিষ্ট্য দেখানো কোড নমুনা অন্বেষণ করা।

## মিস্ট্রাল মডেলসমূহ

এই পাঠে, আমরা ৩টি বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ করব:  
**মিস্ট্রাল লার্জ**, **মিস্ট্রাল স্মল** এবং **মিস্ট্রাল নেমো**।

এই মডেল প্রতিটি GitHub মডেল মার্কেটপ্লেসে বিনামূল্যে উপলব্ধ। এই নোটবুকে থাকা কোড গুলো এই মডেলগুলো ব্যবহার করে কোড চালাবে। GitHub মডেল ব্যবহার করে [AI মডেল দিয়ে প্রোটটাইপ তৈরির](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) বিস্তারিত জানতে এখানে ক্লিক করুন।

## মিস্ট্রাল লার্জ ২ (2407)  
মিস্ট্রাল লার্জ ২ বর্তমানে মিস্ট্রালের প্রধান মডেল এবং এন্টারপ্রাইজ ব্যবহারের জন্য ডিজাইন করা হয়েছে।

এই মডেলটি মূল মিস্ট্রাল লার্জের আপগ্রেড, যা প্রদান করে  
- বড় প্রসঙ্গ জানালা - ১২৮ক বনাম ৩২ক  
- গণিত এবং কোডিং কাজের উন্নত কর্মক্ষমতা - গড় সঠিকতা ৭৬.৯% বনাম ৬০.৪%  
- বৃদ্ধি পাওয়া বহু ভাষার কর্মদক্ষতা - ইংরেজি, ফ্রেঞ্চ, জার্মান, স্প্যানিশ, ইতালিয়ান, পর্তুগিজ, ডাচ, রাশিয়ান, চীনা, জাপানি, কোরিয়ান, আরবি, এবং হিন্দি ভাষাসমূহ অন্তর্ভুক্ত।

এই বৈশিষ্ট্যগুলো দিয়ে মিস্ট্রাল লার্জ দক্ষ হয়  
- *রিট্রিভাল অগমেন্টেড জেনারেশন (RAG)* - বড় প্রসঙ্গ জানালার জন্য  
- *ফাংশন কলিং* - এই মডেলটি নেটিভ ফাংশন কলিং থাকে যা বাহ্যিক টুল এবং API এর সঙ্গে একতা ঘটাতে দেয়। এই কলগুলো সমান্তরালে বা একটার পর একটা ধারাবাহিক ক্রমে করা যায়।  
- *কোড জেনারেশন* - এই মডেল পাইথন, জাভা, টাইপস্ক্রিপ্ট এবং সি++ জেনারেশনে অসাধারণ।

### মিস্ট্রাল লার্জ ২ ব্যবহার করে RAG উদাহরণ

এই উদাহরণে, আমরা একটি টেক্সট ডকুমেন্টে RAG প্যাটার্ন চালানোর জন্য মিস্ট্রাল লার্জ ২ ব্যবহার করছি। প্রশ্নটি কোরিয়ান ভাষায় লেখা এবং লেখকের কলেজের আগে করা কার্যক্রম সম্পর্কে জানতে চায়।

এটি Cohere Embeddings মডেল ব্যবহার করে টেক্সট ডকুমেন্ট এবং প্রশ্নের এম্বেডিং তৈরি করে। এই নমুনায় faiss পাইথন প্যাকেজ ভেক্টর স্টোর হিসেবে ব্যবহৃত হয়।

মডেলকে প্রেরিত প্রম্পটে প্রশ্ন এবং প্রশ্নের সঙ্গে সাদৃশ্যপূর্ণ পুনরুদ্ধৃত অংশগুলো উভয়ই অন্তর্ভুক্ত থাকে। মডেল তারপরে একটি স্বাভাবিক ভাষার উত্তর প্রদান করে।

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # দূরত্ব, সূচক
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
মিস্ট্রাল স্মল হল মিস্ট্রালের মডেল পরিবারের আরেকটি মডেল যা প্রিমিয়ার/এন্টারপ্রাইজ ক্যাটাগরির আওতায়। নামানুসারে, এটি একটি ছোট ভাষার মডেল (SLM)। মিস্ট্রাল স্মল ব্যবহারের সুবিধাগুলো হল:  
- মিস্ট্রাল লার্জ এবং নেমোর মতো মডেলের তুলনায় খরচ সাশ্রয় - ৮০% মূল্য হ্রাস  
- কম প্রয়োজনীয় বিলম্ব - মিস্ট্রালের LLM গুলোর চেয়ে দ্রুত সাড়া  
- নমনীয় - কম রিসোর্সের ওপর কম সীমাবদ্ধতা নিয়ে বিভিন্ন পরিবেশে স্থাপনযোগ্য।  

মিস্ট্রাল স্মল ভালো যখন:  
- সারাংশ তৈরি, অনুভূতি বিশ্লেষণ এবং অনুবাদের মতো টেক্সট ভিত্তিক কাজ  
- যেখানে অতি ঘনঘন অনুরোধ করা হয়, এর খরচ কার্যকারিতার কারণে  
- কোড রিভিউ এবং কোড প্রস্তাবনার মতো কম বিলম্বের কাজ

## মিস্ট্রাল স্মল ও মিস্ট্রাল লার্জ তুলনা

মিস্ট্রাল স্মল ও লার্জের বিলম্বের পার্থক্য দেখানোর জন্য নিচের সেলগুলো চালান।

একই প্রম্পটের জন্য সাড়া সময়ের মধ্যে ৩-৫ সেকেন্ড পার্থক্য দেখা যাবে। এছাড়াও সাড়া দৈর্ঘ্য এবং স্টাইলের পার্থক্য লক্ষ করুন।

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

এই পাঠে আলোচিত অন্য দুই মডেলের তুলনায়, মিস্ট্রাল নেমো একমাত্র বিনামূল্যের মডেল যা Apache2 লাইসেন্সভুক্ত।

এটি মিস্ট্রালের পূর্ববর্তী ওপেন সোর্স LLM, মিস্ট্রাল ৭বি এর আপগ্রেড হিসেবে দেখা হয়।

নেমো মডেলের কিছু বৈশিষ্ট্য হলো:

- *অধিক কার্যকর টোকেনাইজেশন:* এই মডেলটি tiktoken এর পরিবর্তে Tekken টোকেনাইজার ব্যবহার করে। যা আরও বেশি ভাষা এবং কোডের ক্ষেত্রে উন্নত কর্মদক্ষতা দেয়।

- *ফাইনটিউনিং:* বেস মডেলটি ফাইনটিউনিং এর জন্য উপলব্ধ। এটি ব্যবহার ক্ষেত্র অনুযায়ী ফাইনটিউনিং করার জন্য অধিক নমনীয়তা দেয়।

- *নেটিভ ফাংশন কলিং* - মিস্ট্রাল লার্জের মতো, এই মডেলও ফাংশন কলিং এ প্রশিক্ষিত। এটি প্রথম ওপেন সোর্স মডেলগুলোর মধ্যে একটি যা এটি করে।

### টোকেনাইজার তুলনা

এই নমুনায়, আমরা দেখব মিস্ট্রাল নেমো কিভাবে টোকেনাইজেশন পরিচালনা করে মিস্ট্রাল লার্জের তুলনায়।

উভয় নমুনাই একই প্রম্পট নেওয়া হলেও দেখা যাবে নেমো মডেলটি মিস্ট্রাল লার্জের তুলনায় কম টোকেন ফিরিয়ে দেয়।

```bash
pip install mistral-common
```
  
```python 
# প্রয়োজনীয় প্যাকেজ আমদানি করুন:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# মিস্ট্রাল টোকেনাইজার লোড করুন

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# মেসেজের একটি তালিকা টোকেনাইজ করুন
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

# টোকেনের সংখ্যা গণনা করুন
print(len(tokens))
```
  
```python
# প্রয়োজনীয় প্যাকেজ ইম্পোর্ট করুন:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# মিস্ট্রাল টোকেনাইজার লোড করুন

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# একটি বার্তার তালিকা টোকেনাইজ করুন
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

# টোকেনের সংখ্যা গণনা করুন
print(len(tokens))
```
  

## শেখানো এখানেই থামে না, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [জেনারেটিভ AI লার্নিং সংগ্রহ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার জেনারেটিভ AI জ্ঞানের স্তর বৃদ্ধি অব্যাহত থাকে!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ডিসক্লেইমার**:  
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসত্যতা থাকতে পারে। মূল ডকুমেন্টটি এর নিজস্ব ভাষায় সর্বোচ্চ কর্তৃপক্ষের উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ নেওয়া পরামর্শযোগ্য। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->