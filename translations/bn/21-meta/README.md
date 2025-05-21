<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:08:42+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "bn"
}
-->
# মেটা ফ্যামিলি মডেল দিয়ে নির্মাণ

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- মেটা ফ্যামিলির দুটি প্রধান মডেল - Llama 3.1 এবং Llama 3.2 অনুসন্ধান করা
- প্রতিটি মডেলের ব্যবহারক্ষেত্র এবং পরিস্থিতি বোঝা
- প্রতিটি মডেলের বিশেষ বৈশিষ্ট্য প্রদর্শনের জন্য কোড উদাহরণ

## মেটা ফ্যামিলি মডেল

এই পাঠে আমরা মেটা ফ্যামিলি বা "Llama Herd" থেকে ২টি মডেল অনুসন্ধান করব - Llama 3.1 এবং Llama 3.2

এই মডেলগুলি বিভিন্ন ভ্যারিয়েন্টে আসে এবং GitHub Model মার্কেটপ্লেসে উপলব্ধ। GitHub Models ব্যবহার করে কিভাবে [AI মডেলের সাথে প্রোটোটাইপ তৈরি করবেন](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) তার আরও বিস্তারিত এখানে।

মডেল ভ্যারিয়েন্ট:
- Llama 3.1 - 70B ইনস্ট্রাক্ট
- Llama 3.1 - 405B ইনস্ট্রাক্ট
- Llama 3.2 - 11B ভিশন ইনস্ট্রাক্ট
- Llama 3.2 - 90B ভিশন ইনস্ট্রাক্ট

*দ্রষ্টব্য: Llama 3 GitHub Models এও উপলব্ধ কিন্তু এই পাঠে আলোচনা করা হবে না*

## Llama 3.1

৪০৫ বিলিয়ন প্যারামিটার সহ, Llama 3.1 ওপেন সোর্স LLM ক্যাটাগরিতে পড়ে।

এই মডেলটি পূর্ববর্তী রিলিজ Llama 3 এর আপগ্রেড, যা প্রদান করে:

- বৃহত্তর প্রসঙ্গ উইন্ডো - ১২৮কে টোকেন বনাম ৮কে টোকেন
- বৃহত্তর সর্বাধিক আউটপুট টোকেন - ৪০৯৬ বনাম ২০৪৮
- উন্নত বহুভাষিক সমর্থন - প্রশিক্ষণ টোকেনের বৃদ্ধির কারণে

এইগুলি Llama 3.1 কে জেনারেটিভ AI অ্যাপ্লিকেশন নির্মাণের সময় আরও জটিল ব্যবহারক্ষেত্র পরিচালনা করতে সক্ষম করে, যেমন:

- নেটিভ ফাংশন কলিং - LLM ওয়ার্কফ্লোর বাইরে বাহ্যিক সরঞ্জাম এবং ফাংশন কল করার ক্ষমতা
- উন্নত RAG পারফরম্যান্স - বৃহত্তর প্রসঙ্গ উইন্ডোর কারণে
- সিন্থেটিক ডেটা জেনারেশন - ফাইন-টিউনিং এর মতো কাজের জন্য কার্যকর ডেটা তৈরি করার ক্ষমতা

### নেটিভ ফাংশন কলিং

Llama 3.1 ফাংশন বা টুল কলিং আরও কার্যকর করতে ফাইন-টিউন করা হয়েছে। এটি দুটি বিল্ট-ইন টুলও রয়েছে যা মডেলটি ব্যবহারকারীর প্রম্পটের ভিত্তিতে ব্যবহার করা প্রয়োজন বলে চিহ্নিত করতে পারে। এই টুলগুলি হল:

- **ব্রেভ সার্চ** - ওয়েব সার্চ করে আবহাওয়ার মতো সর্বশেষ তথ্য পেতে ব্যবহার করা যেতে পারে
- **Wolfram Alpha** - আরও জটিল গাণিতিক গণনার জন্য ব্যবহার করা যেতে পারে তাই আপনার নিজস্ব ফাংশন লেখার প্রয়োজন নেই।

আপনি আপনার নিজস্ব কাস্টম টুলও তৈরি করতে পারেন যা LLM কল করতে পারে।

নিচের কোড উদাহরণে:

- আমরা সিস্টেম প্রম্পটে উপলব্ধ টুলগুলি (brave_search, wolfram_alpha) সংজ্ঞায়িত করি।
- একটি ব্যবহারকারী প্রম্পট পাঠান যা একটি নির্দিষ্ট শহরের আবহাওয়া সম্পর্কে জিজ্ঞাসা করে।
- LLM একটি টুল কলের সাথে Brave Search টুলে প্রতিক্রিয়া জানাবে যা এমন দেখাবে `<|python_tag|>brave_search.call(query="Stockholm weather")`

*দ্রষ্টব্য: এই উদাহরণটি শুধুমাত্র টুল কল করে, আপনি যদি ফলাফল পেতে চান, তাহলে আপনাকে Brave API পৃষ্ঠায় একটি বিনামূল্যে অ্যাকাউন্ট তৈরি করতে হবে এবং ফাংশনটি নিজেই সংজ্ঞায়িত করতে হবে*

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

একটি LLM হওয়া সত্ত্বেও, Llama 3.1 এর একটি সীমাবদ্ধতা হল মাল্টিমোডালিটি। অর্থাৎ, বিভিন্ন ধরনের ইনপুট যেমন ইমেজ প্রম্পট হিসেবে ব্যবহার করতে পারা এবং প্রতিক্রিয়া প্রদান করা। এই ক্ষমতা Llama 3.2 এর প্রধান বৈশিষ্ট্যগুলির মধ্যে একটি। এই বৈশিষ্ট্যগুলির মধ্যে রয়েছে:

- মাল্টিমোডালিটি - টেক্সট এবং ইমেজ প্রম্পট উভয়ই মূল্যায়ন করার ক্ষমতা রয়েছে
- ছোট থেকে মাঝারি আকারের ভ্যারিয়েশন (11B এবং 90B) - এটি নমনীয় ডিপ্লয়মেন্ট অপশন প্রদান করে
- শুধুমাত্র টেক্সট ভ্যারিয়েশন (1B এবং 3B) - এটি মডেলটিকে এজ / মোবাইল ডিভাইসে ডিপ্লয় করার অনুমতি দেয় এবং কম লেটেন্সি প্রদান করে

মাল্টিমোডাল সমর্থন ওপেন সোর্স মডেলের জগতে একটি বড় পদক্ষেপের প্রতিনিধিত্ব করে। নিচের কোড উদাহরণে Llama 3.2 90B থেকে একটি ইমেজের বিশ্লেষণ পেতে একটি ইমেজ এবং টেক্সট প্রম্পট উভয়ই নেওয়া হয়েছে।

### Llama 3.2 এর সাথে মাল্টিমোডাল সমর্থন

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

## শেখা এখানেই থেমে নেই, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পরে, আমাদের [Generative AI লার্নিং সংগ্রহ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন আপনার জেনারেটিভ AI জ্ঞান উন্নত করতে!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব নির্ভুলতার চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।