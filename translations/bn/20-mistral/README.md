# মিস্ট্রাল মডেল দিয়ে নির্মাণ 

## পরিচিতি 

এই পাঠে আমরা আলোচনা করব: 
- বিভিন্ন মিস্ট্রাল মডেল অন্বেষণ করা 
- প্রতিটি মডেলের ব্যবহারের ক্ষেত্র এবং পরিস্থিতি বোঝা 
- প্রতিটি মডেলের অনন্য বৈশিষ্ট্য প্রদর্শন করে কোড নমুনা অন্বেষণ করা। 

## মিস্ট্রাল মডেলসমূহ 

এই পাঠে, আমরা ৩টি ভিন্ন মিস্ট্রাল মডেল অন্বেষণ করব: 
**মিস্ট্রাল লার্জ**, **মিস্ট্রাল স্মল** এবং **মিস্ট্রাল নেমো**। 

এই মডেলগুলো [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) এ বিনামূল্যে পাওয়া যায়। এই নোটবুকের কোড এই মডেলগুলো ব্যবহার করে চলবে।

> **দ্রষ্টব্য:** GitHub Models জুলাই ২০২৬ এর শেষে বন্ধ হয়ে যাচ্ছে। AI মডেল নিয়ে প্রোটোটাইপ করতে [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ব্যবহার করার আরও বিস্তারিত এখানে দেওয়া হয়েছে। 


## মিস্ট্রাল লার্জ ২ (২৪০৭)
মিস্ট্রাল লার্জ ২ বর্তমানে মিস্ট্রালের প্রধান মডেল এবং এটি এন্টারপ্রাইজ ব্যবহারের জন্য ডিজাইন করা হয়েছে। 

মডেলটি মূল মিস্ট্রাল লার্জের একটি আপগ্রেড যা দেয় 
- বড় কনটেক্সট উইন্ডো - ১২৮কে বনাম ৩২কে 
- গণিত এবং কোডিং টাস্কে উন্নত পারফর্মেন্স - গড় যথার্থতা ৭৬.৯% বনাম ৬০.৪% 
- বৃদ্ধি প্রাপ্ত বহু ভাষাভিত্তিক পারফর্মেন্স - ভাষাগুলো হলো: ইংরেজি, ফরাসি, জার্মান, স্প্যানিশ, ইতালিয়ান, পর্তুগিজ, ডাচ, রুশ, চীনা, জাপানি, কোরিয়ান, আরবি, এবং হিন্দি।

এই বৈশিষ্ট্যগুলোর সঙ্গে, মিস্ট্রাল লার্জ বিশেষভাবে দক্ষ 
- *রিট্রিভাল অগমেন্টেড জেনারেশন (RAG)* - বড় কনটেক্সট উইন্ডোর কারণে
- *ফাংশন কলিং* - এই মডেলটিতে নেটিভ ফাংশন কলিং রয়েছে যা বাহ্যিক টুল এবং API এর সাথে ইন্টিগ্রেশন সক্ষম করে। এই কলগুলো একযোগে বা ক্রমানুসারে করা যেতে পারে। 
- *কোড জেনারেশন* - এই মডেল পাইথন, জাভা, টাইপস্ক্রিপ্ট এবং C++ জেনারেশনে পারদর্শী। 

### মিস্ট্রাল লার্জ ২ ব্যবহার করে RAG উদাহরণ 

এই উদাহরণে, আমরা একটি টেক্সট ডকুমেন্টে RAG প্যাটার্ন চালাতে মিস্ট্রাল লার্জ ২ ব্যবহার করছি। প্রশ্নটি কোরিয়ান ভাষায় লেখা হয়েছে এবং লেখকের কলেজের পূর্ববর্তী কার্যক্রম সম্পর্কে জানতে চায়। 

এটি প্রশ্ন এবং টেক্সট ডকুমেন্ট উভয়ের এমবেডিংস তৈরির জন্য Cohere এমবেডিংস মডেল ব্যবহার করে। এই নমুনার জন্য faiss পাইথন প্যাকেজটি ভেক্টর স্টোর হিসেবে ব্যবহৃত হয়েছে। 

মিস্ট্রাল মডেলে পাঠানো প্রম্পটে প্রশ্ন এবং প্রশ্নের সাথে সাদৃশ্যপূর্ণ রিট্রিভড চাঙ্ক উভয়ই অন্তর্ভুক্ত থাকে। মডেলটি তারপর প্রাকৃতিক ভাষায় উত্তর প্রদান করে। 

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

# এগুলো আপনার Microsoft Foundry প্রকল্পের "অভারভিউ" পেজ থেকে নিন
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
মিস্ট্রাল স্মল মিস্ট্রাল পরিবারের আরেকটি মডেল যা প্রিমিয়ার/এন্টারপ্রাইজ ক্যাটাগরির অন্তর্ভুক্ত। নাম অনুযায়ী, এটি একটি স্মল ভাষা মডেল (SLM)। মিস্ট্রাল স্মল ব্যবহারের সুবিধাসমূহ হলো: 
- মিস্ট্রাল লার্জ এবং NeMo মত LLM এর তুলনায় খরচ সাশ্রয় - ৮০% দাম কম
- কম বিলম্বতা - মিস্ট্রালের অন্যান্য LLM এর তুলনায় দ্রুত প্রতিক্রিয়া
- নমনীয়তা - কম সম্পদের প্রয়োজনীয়তা নিয়ে বিভিন্ন পরিবেশে ডিপ্লয় করা যায়। 


মিস্ট্রাল স্মল উপযুক্ত: 
- টেক্সট ভিত্তিক কাজ যেমন সারাংশ তৈরি, অনুভূতি বিশ্লেষণ এবং অনুবাদ। 
- যেখানে প্রায়ই অনুরোধ করা হয়, তেমন অ্যাপ্লিকেশন, খরচ কার্যকারিতার জন্য 
- কম বিলম্বতার কোড টাস্ক যেমন রিভিউ এবং কোড সুপারিশ 

## মিস্ট্রাল স্মল এবং মিস্ট্রাল লার্জের তুলনা 

মিস্ট্রাল স্মল ও লার্জের মধ্যে বিলম্বতার পার্থক্য দেখাতে নিচের সেলগুলো চালান। 

একই প্রম্পটের ওপর প্রতিক্রিয়া সময়ে ৩-৫ সেকেন্ডের পার্থক্য দেখতে পাবেন। পাশাপাশি প্রতিক্রিয়ার দৈর্ঘ্য ও শৈলীর পার্থক্যও লক্ষ্য করুন।  

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

এই পাঠে আলোচনা করা অন্য দুই মডেলের তুলনায়, মিস্ট্রাল নেমো একমাত্র Apache2 লাইসেন্স সহ বিনামূল্যে মডেল। 

এটি পূর্ববর্তী মিস্ট্রাল ওপেন সোর্স LLM, মিস্ট্রাল ৭বি এর একটি আপগ্রেড হিসেবে বিবেচিত। 

নেমো মডেলের আরো কিছু বৈশিষ্ট্য হলো: 

- *আরও দক্ষ টোকেনাইজেশন:* এই মডেলটি অধিক ব্যবহৃত tiktoken এর পরিবর্তে Tekken টোকেনাইজার ব্যবহার করে। এতে বেশি ভাষা এবং কোডে ভালো পারফর্মেন্স পাওয়া যায়। 

- *ফাইনটিউনিং:* বেস মডেলটি ফাইনটিউনিংয়ের জন্য উপলব্ধ। এটি এমন ব্যবহার ক্ষেত্রে আরও নমনীয়তা দেয় যেখানে ফাইনটিউনিং প্রয়োজন হতে পারে। 

- *নেটিভ ফাংশন কলিং* - মিস্ট্রাল লার্জের মতো, এই মডেলটিও ফাংশন কলিং প্রশিক্ষিত। এই বৈশিষ্ট্যটি এটিকে প্রথম কিছু ওপেন সোর্স মডেলের মধ্যে একটি করে তোলে। 


### টোকেনাইজার তুলনা 

এই নমুনায়, আমরা দেখব মিস্ট্রাল নেমো কীভাবে টোকেনাইজেশন পরিচালনা করে মিস্ট্রাল লার্জের তুলনায়। 

উভয় নমুনাই একই প্রম্পট নেয় কিন্তু দেখবেন নেমো মিস্ট্রাল লার্জের তুলনায় কম টোকেন ফেরত দেয়। 

```bash
pip install mistral-common
```

```python 
# প্রয়োজনীয় প্যাকেজগুলি আমদানি করুন:
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

```python
# প্রয়োজনীয় প্যাকেজগুলি আমদানি করুন:
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

## শেখা এখানে থেমে যায় না, যাত্রা চালিয়ে যান

এই পাঠ সম্পন্ন করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনি আপনার জেনারেটিভ AI জ্ঞান আরও উন্নত করতে পারেন!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->