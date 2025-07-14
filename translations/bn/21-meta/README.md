<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:08:08+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "bn"
}
-->
# Building With the Meta Family Models 

## পরিচিতি 

এই পাঠে আলোচনা করা হবে: 

- মেটা ফ্যামিলির দুইটি প্রধান মডেল - Llama 3.1 এবং Llama 3.2 এর পরিচিতি  
- প্রতিটি মডেলের ব্যবহার ক্ষেত্র এবং পরিস্থিতি বোঝা  
- প্রতিটি মডেলের বিশেষ বৈশিষ্ট্য দেখানোর জন্য কোড উদাহরণ  

## মেটা ফ্যামিলির মডেলসমূহ 

এই পাঠে, আমরা মেটা ফ্যামিলির বা "Llama Herd" এর ২টি মডেল অন্বেষণ করব - Llama 3.1 এবং Llama 3.2 

এই মডেলগুলো বিভিন্ন ভ্যারিয়েন্টে আসে এবং GitHub Model মার্কেটপ্লেসে পাওয়া যায়। GitHub Models ব্যবহার করে [AI মডেল দিয়ে প্রোটোটাইপ তৈরি](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) করার আরও বিস্তারিত এখানে দেওয়া হয়েছে। 

মডেল ভ্যারিয়েন্টসমূহ:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Note: Llama 3 GitHub Models এ পাওয়া যায়, তবে এই পাঠে তা আলোচনা করা হবে না*  

## Llama 3.1 

৪০৫ বিলিয়ন প্যারামিটার সহ, Llama 3.1 ওপেন সোর্স LLM ক্যাটাগরিতে পড়ে। 

এই মডেলটি আগের Llama 3 রিলিজের একটি আপগ্রেড যা দেয়: 

- বড় কনটেক্সট উইন্ডো - ১২৮কে টোকেন বনাম ৮কে টোকেন  
- বড় সর্বোচ্চ আউটপুট টোকেন - ৪০৯৬ বনাম ২০৪৮  
- উন্নত বহুভাষিক সমর্থন - প্রশিক্ষণ টোকেন বৃদ্ধির কারণে  

এগুলো Llama 3.1 কে আরও জটিল ব্যবহার ক্ষেত্র সামলাতে সক্ষম করে যখন GenAI অ্যাপ্লিকেশন তৈরি করা হয়, যেমন:  
- নেটিভ ফাংশন কলিং - LLM ওয়ার্কফ্লোর বাইরে বাহ্যিক টুল এবং ফাংশন কল করার ক্ষমতা  
- উন্নত RAG পারফরম্যান্স - বড় কনটেক্সট উইন্ডোর কারণে  
- সিন্থেটিক ডেটা জেনারেশন - ফাইন-টিউনিংয়ের মতো কাজের জন্য কার্যকর ডেটা তৈরি করার ক্ষমতা  

### নেটিভ ফাংশন কলিং 

Llama 3.1 ফাইন-টিউন করা হয়েছে ফাংশন বা টুল কল করার ক্ষেত্রে আরও কার্যকর হতে। এতে দুটি বিল্ট-ইন টুল রয়েছে যেগুলো মডেল ব্যবহারকারীর প্রম্পট অনুযায়ী ব্যবহার করার প্রয়োজনীয়তা চিনতে পারে। এই টুলগুলো হল: 

- **Brave Search** - ওয়েব সার্চ করে আপডেটেড তথ্য যেমন আবহাওয়া পাওয়ার জন্য ব্যবহার করা যায়  
- **Wolfram Alpha** - জটিল গাণিতিক হিসাবের জন্য ব্যবহার করা যায়, নিজের ফাংশন লেখার প্রয়োজন নেই  

আপনি নিজের কাস্টম টুলও তৈরি করতে পারেন যা LLM কল করতে পারবে।  

নিচের কোড উদাহরণে: 

- আমরা সিস্টেম প্রম্পটে উপলব্ধ টুলগুলো (brave_search, wolfram_alpha) সংজ্ঞায়িত করেছি।  
- ব্যবহারকারীর প্রম্পট পাঠিয়েছি যা একটি নির্দিষ্ট শহরের আবহাওয়া সম্পর্কে জানতে চায়।  
- LLM একটি টুল কল হিসেবে Brave Search টুলকে কল করবে, যা দেখতে এরকম হবে `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Note: এই উদাহরণ শুধুমাত্র টুল কল করে, ফলাফল পেতে চাইলে আপনাকে Brave API পেজে একটি ফ্রি অ্যাকাউন্ট তৈরি করে ফাংশনটি নিজে সংজ্ঞায়িত করতে হবে*  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2 

যদিও এটি একটি LLM, Llama 3.1 এর একটি সীমাবদ্ধতা হলো মাল্টিমোডালিটি। অর্থাৎ, বিভিন্ন ধরনের ইনপুট যেমন ছবি প্রম্পট হিসেবে ব্যবহার করা এবং সাড়া দেওয়ার ক্ষমতা। এই ক্ষমতাই Llama 3.2 এর প্রধান বৈশিষ্ট্যগুলোর একটি। অন্যান্য বৈশিষ্ট্যগুলো হলো: 

- মাল্টিমোডালিটি - টেক্সট এবং ছবি উভয় প্রম্পট মূল্যায়ন করার ক্ষমতা  
- ছোট থেকে মাঝারি আকারের ভ্যারিয়েন্ট (11B এবং 90B) - নমনীয় ডিপ্লয়মেন্ট অপশন প্রদান করে  
- শুধুমাত্র টেক্সট ভ্যারিয়েন্ট (1B এবং 3B) - এজ/মোবাইল ডিভাইসে ডিপ্লয়মেন্টের সুবিধা এবং কম লেটেন্সি প্রদান করে  

মাল্টিমোডাল সমর্থন ওপেন সোর্স মডেলগুলোর জগতে একটি বড় অগ্রগতি। নিচের কোড উদাহরণে একটি ছবি এবং টেক্সট প্রম্পট ব্যবহার করে Llama 3.2 90B থেকে ছবির বিশ্লেষণ নেওয়া হয়েছে।  

### Llama 3.2 এর মাল্টিমোডাল সমর্থন

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## শেখা এখানেই শেষ নয়, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন এবং আপনার Generative AI জ্ঞানে আরও উন্নতি করুন!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।