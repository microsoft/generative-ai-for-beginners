# মিস্ট্রাল মডেল দিয়ে তৈরি করা 

## পরিচিতি 

এই পাঠে আলোচনা করা হবে: 
- বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ করা 
- প্রতিটি মডেলের ব্যবহারের ক্ষেত্র ও পরিস্থিতি বুঝে নেওয়া 
- এমন কোড স্যাম্পল অন্বেষণ যা প্রতিটি মডেলের বিশেষ বৈশিষ্ট্য দেখায়। 

## মিস্ট্রাল মডেলসমূহ 

এই পাঠে, আমরা ৩টি বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ করব: 
**মিস্ট্রাল লার্জ**, **মিস্ট্রাল স্মল** এবং **মিস্ট্রাল নেমো**। 

এই মডেলগুলো [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) এ বিনামূল্যে পাওয়া যায়। এই নোটবুকে ব্যবহৃত কোড এই মডেলগুলো ব্যবহারে রান করা হবে।

> **দ্রষ্টব্য:** GitHub Models জুলাই ২০২৬ এর শেষে বন্ধ হয়ে যাচ্ছে। AI মডেলগুলো প্রোটোটাইপ করার জন্য [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ব্যবহারের আরও বিশদ এখানে দেওয়া হয়েছে। 


## মিস্ট্রাল লার্জ ২ (২৪০৭)
মিস্ট্রাল লার্জ ২ বর্তমানে মিস্ট্রালের প্রধান মডেল এবং এটি এন্টারপ্রাইজ ব্যবহারের জন্য ডিজাইন করা হয়েছে। 

এই মডেলটি মূল মিস্ট্রাল লার্জের একটি উন্নতি, যা প্রদান করে 
- বড় কনটেক্সট উইন্ডো - ১২৮ক বনাম ৩২ক 
- গাণিতিক ও কোডিং কাজগুলিতে উন্নত পারফরম্যান্স - ৭৬.৯% গড় সঠিকতা বনাম ৬০.৪% 
- বহুভাষিক পারফরম্যান্স বৃদ্ধি - ভাষাসমূহের মধ্যে রয়েছে: ইংরেজি, ফরাসি, জার্মান, স্পেনিশ, ইতালিয়ান, পর্তুগিজ, ডাচ, রাশিয়ান, চীনা, জাপানি, কোরিয়ান, আরবি, এবং হিন্দি।

এই বৈশিষ্ট্যসহ, মিস্ট্রাল লার্জ উৎকৃষ্টভাবে সক্ষম 
- *রিট্রিভাল অগমেন্টেড জেনারেশন (RAG)* - বড় কনটেক্সট উইন্ডোর কারণে
- *ফাংশন কলিং* - এই মডেলটির নেটিভ ফাংশন কলিং রয়েছে যা বহির্গত টুল এবং API এর সাথে ইন্টিগ্রেশন সম্ভব করে। এই কলগুলো একসঙ্গে বা ধারাবাহিকভাবে করা যেতে পারে। 
- *কোড জেনারেশন* - এই মডেলটি পাইথন, জাভা, টাইপস্ক্রিপ্ট এবং সি++ জেনারেশনে উৎকৃষ্ট। 

### মিস্ট্রাল লার্জ ২ ব্যবহার করে RAG উদাহরণ 

এই উদাহরণে, আমরা একটি টেক্সট ডকুমেন্টের ওপর RAG প্যাটার্ন রান করতে মিস্ট্রাল লার্জ ২ ব্যবহার করছি। প্রশ্নটি কোরিয়ান ভাষায় লেখা হয়েছে এবং লেখকের কলেজের আগে করণীয় কার্যকলাপ সম্পর্কে জিজ্ঞাসা করছে। 

এটি কোহেরে এম্বেডিংস মডেল ব্যবহার করে টেক্সট ডকুমেন্ট এবং প্রশ্নের এম্বেডিং তৈরি করে। এই স্যাম্পলটিতে faiss পাইথন প্যাকেজ ভেক্টর স্টোর হিসেবে ব্যবহার করা হয়। 

মিস্ট্রাল মডেলে পাঠানো প্রম্পটে উভয়ই প্রশ্ন এবং প্রশ্নের সাথে সাদৃশ্যপূর্ণ পুনরুদ্ধারকৃত অংশ থাকে। মডেল তখন একটি প্রাকৃতিক ভাষার উত্তর প্রদান করে। 

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

# আপনার Microsoft Foundry প্রকল্পের "সংক্ষিপ্ত বিবরণ" পৃষ্ঠাটি থেকে এগুলি পান
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
মিস্ট্রাল স্মল হলো মিস্ট্রাল পরিবারের আরেকটি মডেল, প্রধানত প্রিমিয়ার/এন্টারপ্রাইজ ক্যাটাগরির অন্তর্গত। নাম অনুযায়ী, এটি একটি স্মল ল্যাঙ্গুয়েজ মডেল (SLM)। মিস্ট্রাল স্মল ব্যবহারের সুবিধাসমূহ হলো: 
- মিস্ট্রাল লার্জ ও নেমো এর মতো LLM তুলনায় খরচ সাশ্রয় - ৮০% দাম কম
- কম ল্যাটেন্সি - মিস্ট্রালের LLM এর তুলনায় দ্রুত প্রতিক্রিয়া
- নমনীয় - বিভিন্ন পরিবেশে কম রিসোর্সের প্রয়োজনীয়তা নিয়ে ডিপ্লয় করা যায়। 


মিস্ট্রাল স্মল ভালো কাজে লাগে: 
- টেক্সট ভিত্তিক কাজ যেমন সারাংশ তৈরি, অনুভূতি বিশ্লেষণ এবং অনুবাদ। 
- এমন অ্যাপ্লিকেশন যেখানে খরচ সাশ্রয়ী হওয়ার কারণে ঘন ঘন অনুরোধ করা হয় 
- কম ল্যাটেন্সির কোড কাজ যেমন পর্যালোচনা এবং কোড পরামর্শ দেওয়া 

## মিস্ট্রাল স্মল এবং মিস্ট্রাল লার্জের তুলনা 

মিস্ট্রাল স্মল এবং লার্জের মধ্যে ল্যাটেন্সির পার্থক্য দেখানোর জন্য নীচের সেলগুলো রান করুন। 

আপনাকে ৩-৫ সেকেন্ডের মধ্যে প্রতিক্রিয়ার সময়ে পার্থক্য দেখতে হবে। একই প্রম্পটের ওপর উত্তর দৈর্ঘ্য এবং ধরণও লক্ষ্য করুন।  

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

## মিস্ট্রাল নেমো

অন্য দুটো মডেলের তুলনায়, মিস্ট্রাল নেমো একমাত্র বিনামূল্যে মডেল যার অ্যাপাচি ২ লাইসেন্স রয়েছে। 

এটি মিস্ট্রালের পূর্ববর্তী ওপেন সোর্স LLM, মিস্ট্রাল ৭বি এর আপগ্রেড হিসেবে দেখা হয়। 

নেমো মডেলের আরও কিছু বৈশিষ্ট্য হলো: 

- *আরো দক্ষ টোকেনাইজেশন:* এই মডেল tiktoken এর পরিবর্তে Tekken টোকেনাইজার ব্যবহার করে। এর ফলে আরো ভাষা ও কোডে ভালো পারফরম্যান্স হয়। 

- *ফাইনটিউনিং:* বেস মডেলটি ফাইনটিউনিংয়ের জন্য পাওয়া যায়। এর ফলে ফাইনটিউনিং প্রয়োজনীয় ক্ষেত্রগুলোর জন্য আরো নমনীয়তা থাকে। 

- *নেটিভ ফাংশন কলিং* - মিস্ট্রাল লার্জের মতো, এই মডেলটিও ফাংশন কলিং অনুশীলন করেছে। এটি এটিকে প্রথম ওপেন সোর্স মডেলগুলোর একটি হিসেবে বিশেষ করে তোলে। 


### টোকেনাইজারগুলোর তুলনা 

এই স্যাম্পলে, আমরা মিস্ট্রাল নেমো কিভাবে টোকেনাইজেশন পরিচালনা করে মিস্ট্রাল লার্জের সাথে তুলনা করব। 

দুই স্যাম্পলই একই প্রম্পট নিচ্ছে কিন্তু আপনি দেখতে পারবেন নেমো মিস্ট্রালের তুলনায় কম টোকেন রিটার্ন করে। 

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

# বার্তাগুলির একটি তালিকা টোকেনাইজ করুন
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
# প্রয়োজনীয় প্যাকেজগুলি ইম্পোর্ট করুন:
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

# বার্তাগুলির একটি তালিকা টোকেনাইজ করুন
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

## শেখা এখানেই শেষ নয়, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পরে, আমাদের [জেনারেটিভ AI শেখার সংগ্রহ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন এবং আপনার জেনারেটিভ AI জ্ঞান উন্নত করুন!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->