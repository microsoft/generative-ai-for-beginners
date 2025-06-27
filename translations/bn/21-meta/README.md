<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:28:34+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "bn"
}
-->
# মেটা ফ্যামিলি মডেলের সাথে নির্মাণ

## ভূমিকা

এই পাঠে আলোচনা করা হবে:

- দুটি প্রধান মেটা ফ্যামিলি মডেল - ল্লামা ৩.১ এবং ল্লামা ৩.২ অন্বেষণ করা
- প্রতিটি মডেলের ব্যবহারের ক্ষেত্র এবং পরিস্থিতি বোঝা
- প্রতিটি মডেলের বিশেষ বৈশিষ্ট্য প্রদর্শনের জন্য কোড নমুনা

## মেটা ফ্যামিলি মডেল

এই পাঠে, আমরা মেটা ফ্যামিলি বা "ল্লামা হের্ড" থেকে দুটি মডেল অন্বেষণ করব - ল্লামা ৩.১ এবং ল্লামা ৩.২

এই মডেলগুলি বিভিন্ন বৈচিত্র্যে আসে এবং GitHub মডেল মার্কেটপ্লেসে পাওয়া যায়। AI মডেল দিয়ে [প্রোটোটাইপ তৈরি করার জন্য GitHub মডেল ব্যবহার করার](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) আরও বিস্তারিত এখানে রয়েছে।

মডেল বৈচিত্র্য:
- ল্লামা ৩.১ - ৭০বি ইনস্ট্রাক্ট
- ল্লামা ৩.১ - ৪০৫বি ইনস্ট্রাক্ট
- ল্লামা ৩.২ - ১১বি ভিশন ইনস্ট্রাক্ট
- ল্লামা ৩.২ - ৯০বি ভিশন ইনস্ট্রাক্ট

*দ্রষ্টব্য: ল্লামা ৩ GitHub মডেলে পাওয়া যায় কিন্তু এই পাঠে আলোচনা করা হবে না*

## ল্লামা ৩.১

৪০৫ বিলিয়ন প্যারামিটার সহ, ল্লামা ৩.১ ওপেন সোর্স LLM বিভাগে অন্তর্ভুক্ত।

এই মডেলটি পূর্ববর্তী ল্লামা ৩ রিলিজের একটি আপগ্রেড যা প্রদান করে:

- বড় প্রসঙ্গ উইন্ডো - ১২৮কে টোকেন বনাম ৮কে টোকেন
- বড় সর্বাধিক আউটপুট টোকেন - ৪০৯৬ বনাম ২০৪৮
- উন্নত বহু ভাষার সমর্থন - প্রশিক্ষণ টোকেনের বৃদ্ধির কারণে

এগুলি ল্লামা ৩.১ কে জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করার সময় আরও জটিল ব্যবহারের ক্ষেত্রে পরিচালনা করতে সক্ষম করে, যার মধ্যে রয়েছে:
- নেটিভ ফাংশন কলিং - LLM ওয়ার্কফ্লোর বাইরে বাহ্যিক টুল এবং ফাংশন কল করার ক্ষমতা
- উন্নত RAG কর্মক্ষমতা - উচ্চ প্রসঙ্গ উইন্ডোর কারণে
- সিন্থেটিক ডেটা জেনারেশন - ফাইন-টিউনিংয়ের মতো কাজের জন্য কার্যকর ডেটা তৈরি করার ক্ষমতা

### নেটিভ ফাংশন কলিং

ল্লামা ৩.১ ফাংশন বা টুল কলিংয়ে আরও কার্যকর হওয়ার জন্য ফাইন-টিউন করা হয়েছে। এটি দুটি বিল্ট-ইন টুলও রয়েছে যা মডেলটি ব্যবহারকারীর প্রম্পটের উপর ভিত্তি করে ব্যবহারের প্রয়োজনীয়তা চিহ্নিত করতে পারে। এই টুলগুলি হল:

- **ব্রেভ সার্চ** - ওয়েব সার্চ করে আবহাওয়ার মতো আপ-টু-ডেট তথ্য পেতে ব্যবহার করা যেতে পারে
- **ওলফ্রাম আলফা** - আরও জটিল গাণিতিক গণনার জন্য ব্যবহার করা যেতে পারে তাই নিজস্ব ফাংশন লেখার প্রয়োজন নেই।

আপনি আপনার নিজস্ব কাস্টম টুলও তৈরি করতে পারেন যা LLM কল করতে পারে।

নীচের কোড উদাহরণে:

- আমরা সিস্টেম প্রম্পটে উপলব্ধ টুল (ব্রেভ_সার্চ, ওলফ্রাম_আলফা) সংজ্ঞায়িত করি।
- একটি ব্যবহারকারী প্রম্পট পাঠান যা একটি নির্দিষ্ট শহরের আবহাওয়া সম্পর্কে জানতে চায়।
- LLM ব্রেভ সার্চ টুলে একটি টুল কল দিয়ে প্রতিক্রিয়া জানাবে যা এইরকম দেখাবে `<|python_tag|>brave_search.call(query="Stockholm weather")`

*দ্রষ্টব্য: এই উদাহরণটি শুধুমাত্র টুল কল করে, আপনি যদি ফলাফল পেতে চান, তাহলে আপনাকে ব্রেভ API পৃষ্ঠায় একটি বিনামূল্যে অ্যাকাউন্ট তৈরি করতে হবে এবং ফাংশনটি নিজেই সংজ্ঞায়িত করতে হবে*

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

## ল্লামা ৩.২

একটি LLM হওয়া সত্ত্বেও, ল্লামা ৩.১ এর একটি সীমাবদ্ধতা হল মাল্টিমোডালিটি। অর্থাৎ, চিত্রের মতো বিভিন্ন ধরণের ইনপুট প্রম্পট হিসাবে ব্যবহার করা এবং প্রতিক্রিয়া প্রদান করা। এই ক্ষমতা হল ল্লামা ৩.২ এর প্রধান বৈশিষ্ট্যগুলির মধ্যে একটি। এই বৈশিষ্ট্যগুলির মধ্যে আরও রয়েছে:

- মাল্টিমোডালিটি - পাঠ্য এবং চিত্র প্রম্পট উভয়ই মূল্যায়ন করার ক্ষমতা রয়েছে
- ছোট থেকে মাঝারি আকারের বৈচিত্র্য (১১বি এবং ৯০বি) - এটি নমনীয় স্থাপনার বিকল্প প্রদান করে
- শুধুমাত্র পাঠ্য বৈচিত্র্য (১বি এবং ৩বি) - এটি মডেলকে এজ / মোবাইল ডিভাইসে স্থাপন করার অনুমতি দেয় এবং কম লেটেন্সি প্রদান করে

মাল্টিমোডাল সমর্থন ওপেন সোর্স মডেলের জগতে একটি বড় পদক্ষেপের প্রতিনিধিত্ব করে। নীচের কোড উদাহরণে একটি চিত্র এবং পাঠ্য প্রম্পট উভয়ই ব্যবহার করা হয়েছে ল্লামা ৩.২ ৯০বি থেকে চিত্রের একটি বিশ্লেষণ পেতে।

### ল্লামা ৩.২ এর সাথে মাল্টিমোডাল সমর্থন

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

## শেখা এখানেই থেমে থাকে না, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [জেনারেটিভ AI শেখার সংগ্রহ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন আপনার জেনারেটিভ AI জ্ঞানকে আরও উন্নত করতে!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় প্রামাণিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।