# মেটা ফ্যামিলি মডেল দিয়ে নির্মাণ 

## পরিচিতি 

এই পাঠে কভার করা হবে: 

- মেটার দুটি প্রধান ফ্যামিলি মডেল - লামা ৩.১ এবং লামা ৩.২ অন্বেষণ করা 
- প্রতিটি মডেলের ব্যবহারক্ষেত্র এবং পরিস্থিতি বোঝা 
- প্রতিটি মডেলের বিশেষ বৈশিষ্ট্য প্রদর্শনের জন্য কোড স্যাম্পল 


## মেটা ফ্যামিলির মডেলসমূহ 

এই পাঠে, আমরা মেটা ফ্যামিলি বা "লামা হের্ড" থেকে ২টি মডেল অন্বেষণ করবো - লামা ৩.১ এবং লামা ৩.২।

এই মডেলগুলো বিভিন্ন ভ্যারিয়েন্টে আসে এবং [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)-এ উপলব্ধ। 

> **নোট:** গিটহাব মডেলস  জুলাই ২০২৬ সালের শেষদিকে অবসর গ্রহণ করছে। AI মডেল দিয়ে প্রোটোটাইপ তৈরির জন্য [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ব্যবহারের আরও বিস্তারিত তথ্য এখানে পাওয়া যাবে।

মডেল ভ্যারিয়েন্টসমূহ: 
- লামা ৩.১ - ৭০B ইন্সট্রাক্ট 
- লামা ৩.১ - ৪০৫B ইন্সট্রাক্ট 
- লামা ৩.২ - ১১B ভিশন ইন্সট্রাক্ট 
- লামা ৩.২ - ৯০B ভিশন ইন্সট্রাক্ট 

*নোট: লামা ৩ মাইক্রোসফ্ট ফাউন্ড্রি মডেলসেও উপলব্ধ কিন্তু এই পাঠে আলোচনা করা হবে না*

## লামা ৩.১ 

৪০৫ বিলিয়ন প্যারামিটার সহ, লামা ৩.১ মুক্ত উৎস LLM ক্যাটাগরিতে পড়ে। 

মডেলটি আগের রিলিজ লামা ৩ এর একটি উন্নতি যা প্রস্তাব করে: 

- বড় কনটেক্সট উইন্ডো - ১২৮কে টোকেন বনাম ৮কে টোকেন 
- বড় সর্বোচ্চ আউটপুট টোকেন - ৪০৯৬ বনাম ২০৪৮ 
- উন্নত বহু-ভাষিক সমর্থন - প্রশিক্ষণ টোকেন বৃদ্ধির কারণে 

এগুলো লামা ৩.১ কে আরও জটিল ব্যবহারক্ষেত্রে উপযোগী করে তোলে যখন GenAI অ্যাপ্লিকেশন তৈরি করা হয়, যার মধ্যে রয়েছে: 
- নেটিভ ফাংশন কলিং - LLM ওয়ার্কফ্লো এর বাইরে বাইরের টুল এবং ফাংশন কল করার সক্ষমতা
- উন্নত RAG পারফরম্যান্স - উচ্চতর কনটেক্সট উইন্ডোর কারণে 
- সিন্থেটিক ডেটা জেনারেশন - যেমন ফাইন-টিউনিংয়ের জন্য কার্যকর ডেটা তৈরি করার ক্ষমতা 

### নেটিভ ফাংশন কলিং 

লামা ৩.১ বিশেষভাবে ফাইন-টিউন করা হয়েছে ফাংশন বা টুল কল করতে আরও কার্যকর হতে। এরbuilt-in দুটি টুল আছে যা মডেল ব্যবহারকারীর প্রম্পট অনুযায়ী ব্যবহারের প্রয়োজনীয়তা চিনতে পারে। এই টুলগুলো হলো: 

- **Brave Search** - ওয়েব অনুসন্ধান করে আবহাওয়ার মত সর্বশেষ তথ্য পাওয়ার জন্য ব্যবহার করা যায় 
- **Wolfram Alpha** - আরও জটিল গাণিতিক হিসাবের জন্য ব্যবহৃত, নিজের ফাংশন লেখার প্রয়োজন নেই। 

আপনি নিজের কাস্টম টুলও তৈরি করতে পারেন যা LLM কল করতে পারবে। 

নিচের কোড উদাহরণে: 

- সিস্টেম প্রম্পটে উপলব্ধ টুলগুলো (brave_search, wolfram_alpha) সংজ্ঞায়িত করা হয়েছে। 
- একটি ব্যবহারকারী প্রম্পট পাঠানো হয় যেটি নির্দিষ্ট শহরের আবহওয়ার ব্যাপারে জানতে চায়। 
- LLM একটি টুল কল করবে Brave Search টুলে যা এ রকম দেখাবে `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*নোট: এই উদাহরণ শুধুমাত্র টুল কল করে, ফলাফল পেতে হলে আপনাকে Brave API পৃষ্ঠায় একটি বিনামূল্যের অ্যাকাউন্ট তৈরি করে ফাংশন নিজেই সংজ্ঞায়িত করতে হবে।*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# আপনার Microsoft Foundry প্রকল্পের "ওভারভিউ" পৃষ্ঠাটি থেকে এগুলি পান
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

## লামা ৩.২ 

যদিও এটি একটি LLM, লামা ৩.১ এর একটি সীমাবদ্ধতা হলো এর মাল্টিমোডালিটি নেই। অর্থাৎ, ছবি বা অন্যান্য বিভিন্ন ধরনের ইনপুট প্রম্পট হিসেবে ব্যবহার করে প্রতিক্রিয়া দেওয়ার অসুবিধা। এই ক্ষমতা লামা ৩.২ এর প্রধান বৈশিষ্ট্যগুলোর একটি। অন্যান্য বৈশিষ্ট্যগুলো হলো: 

- মাল্টিমোডালিটি - টেক্সট এবং ইমেজ দুটো প্রম্পট মূল্যায়ন করার ক্ষমতা 
- ছোট থেকে মাঝারি আকারের ভ্যারিয়েশন(১১B এবং ৯০B) - নমনীয় ডিপ্লয়মেন্ট অপশন প্রদান করে, 
- শুধুমাত্র টেক্সট ভ্যারিয়েশন (১B এবং ৩B) - যা মডেলকে এজ / মোবাইল ডিভাইসে ডিপ্লয় করা ও কম বিলম্ব প্রদান করে 

মাল্টিমোডাল সাপোর্ট মুক্ত উৎস মডেলের দুনিয়ায় একটি বড় অগ্রগতি। নিচের কোড উদাহরণ লামা ৩.২ ৯০B থেকে একটি ছবি এবং টেক্সট প্রম্পট নিয়ে ছবির বিশ্লেষণ পাওয়ার জন্য। 


### লামা ৩.২ এর সাথে মাল্টিমোডাল সাপোর্ট

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

# আপনার Microsoft Foundry প্রকল্পের "ওভারভিউ" পেজ থেকে এগুলো নিন
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## শেখা এখানেই শেষ নয়, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার Generative AI জ্ঞান আরও উন্নত হয়!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->