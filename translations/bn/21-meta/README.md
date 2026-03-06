# মেটা ফ্যামিলি মডেল দিয়ে নির্মাণ

## পরিচিতি

এই পাঠে আলোচনা করা হবে:

- মেটা ফ্যামিলির দুটি প্রধান মডেল অনুসন্ধান - লামা 3.1 এবং লামা 3.2  
- প্রতিটি মডেলের ব্যবহার ক্ষেত্রে এবং পরিস্থিতি বোঝা  
- প্রতিটি মডেলের অনন্য বৈশিষ্ট্য প্রদর্শনের জন্য কোড নমুনা

## মেটা ফ্যামিলি অফ মডেলস

এই পাঠে, আমরা মেটা ফ্যামিলি বা "লামা হের্ড" থেকে ২টি মডেল তদন্ত করব - লামা 3.1 এবং লামা 3.2।

এই মডেলগুলো বিভিন্ন ভ্যারিয়েন্টে আসে এবং GitHub মডেল মার্কেটপ্লেসে উপলব্ধ। GitHub মডেল ব্যবহার করে [AI মডেল নিয়ে প্রোটোটাইপ করার](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) আরও বিস্তারিত এখানে রয়েছে।

মডেল ভ্যারিয়েন্টগুলি:  
- লামা 3.1 - ৭০B ইনস্ট্রাক্ট  
- লামা 3.1 - ৪০৫B ইনস্ট্রাক্ট  
- লামা 3.2 - ১১B ভিশন ইনস্ট্রাক্ট  
- লামা 3.2 - ৯০B ভিশন ইনস্ট্রাক্ট  

*নোট: লামা 3 GitHub মডেলে উপলব্ধ, কিন্তু এই পাঠে তার আলোচনা করা হবে না*

## লামা 3.1

৪০৫ বিলিয়ন প্যারামিটার সহ, লামা 3.1 ওপেন সোর্স LLM ক্যাটাগরির অন্তর্ভুক্ত।

এই মডেলটি আগের রিলিজ লামা 3 এর আপগ্রেড হিসেবে:

- বড় কনটেক্সট উইন্ডো - ১২৮k টোকেন বনাম ৮k টোকেন  
- বড় সর্বোচ্চ আউটপুট টোকেন - ৪০৯৬ বনাম ২০৪৮  
- উন্নত বহু-ভাষিক সমর্থন - প্রশিক্ষণ টোকেন বৃদ্ধির কারণে

এগুলো লামা 3.1 কে আরও জটিল ব্যবহার ক্ষেত্রে সক্ষম করে তোলে যখন GenAI অ্যাপ্লিকেশন তৈরি করা হয়, যেমন:  
- নেটিভ ফাংশন কলিং - LLM ওয়ার্কফ্লোর বাইরে বাহ্যিক টুল এবং ফাংশন কল করার ক্ষমতা  
- উন্নত RAG পারফরম্যান্স - বৃহত্তর কনটেক্সট উইন্ডোর কারণে  
- সিন্থেটিক ডেটা জেনারেশন - ফাইন-টিউনিংয়ের মতো কাজগুলোর জন্য কার্যকর তথ্য তৈরি করার ক্ষমতা  

### নেটিভ ফাংশন কলিং

লামা 3.1 কে আরও কার্যকর করে ফাংশন বা টুল কল করতে ফাইন-টিউন করা হয়েছে। এই মডেলে দুটি অন্তর্নির্মিত টুল আছে যা মডেল ব্যবহারকারীর প্রম্পট অনুসারে ব্যবহার করার দরকার শনাক্ত করতে পারে। এই টুলগুলো হল:

- **Brave Search** - ওয়েব সার্চ করে হালনাগাদ তথ্য যেমন আবহাওয়া পাওয়ার জন্য ব্যবহার করা যেতে পারে  
- **Wolfram Alpha** - জটিল গাণিতিক হিসাবের জন্য ব্যবহারযোগ্য, তাই নিজস্ব ফাংশন লেখার দরকার হয় না।

আপনি আপনার নিজস্ব কাস্টম টুলও তৈরি করতে পারেন যা LLM কল করতে পারবে।

নীচের কোড উদাহরণে:

- আমরা সিস্টেম প্রম্পটে উপলব্ধ টুলগুলোর (brave_search, wolfram_alpha) সংজ্ঞা দিয়েছি।  
- একটি ব্যবহারকারী প্রম্পট পাঠানো হয়েছে যা একটি নির্দিষ্ট শহরের আবহাওয়া সম্পর্কে জানার জন্য।  
- LLM একটি টুল কল হিসেবে Brave Search টুল ব্যবহার করে যা এমন দেখতে হবে `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*নোট: এই উদাহরণটি শুধুমাত্র টুল কল করে, যদি আপনি ফলাফল পেতে চান, তাহলে আপনাকে Brave API পৃষ্ঠায় একটি ফ্রি একাউন্ট তৈরি করে নিজেই ফাংশন সংজ্ঞায়িত করতে হবে।*

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

## লামা 3.2

যদিও এটি একটি LLM, লামা 3.1 এর একটি সীমাবদ্ধতা হল এর বহুমাধ্যমিকতা না থাকা। অর্থাৎ, ছবি ইত্যাদি বিভিন্ন ধরনের ইনপুটকে প্রম্পট হিসেবে ব্যবহার করার ক্ষমতা না থাকা এবং সাড়া দেওয়ার অক্ষমতা। এই ক্ষমতাটি লামা 3.2 এর প্রধান বৈশিষ্ট্যগুলোর একটি। এই বৈশিষ্ট্যগুলো অন্তর্ভুক্ত:

- বহুমাধ্যমিকতা - পাঠ্য এবং ছবি উভয় প্রম্পট মূল্যায়নের সক্ষমতা  
- ছোট থেকে মাঝারি সাইজের ভ্যারিয়েন্ট (১১B এবং ৯০B) - যা নমনীয় ডেপ্লয়মেন্ট বিকল্প প্রদান করে  
- শুধুমাত্র টেক্সট ভ্যারিয়েন্ট (১B এবং ৩B) - যা মডেলকে এজ/মোবাইল ডিভাইসে ডেপ্লয় করার এবং কম ল্যাটেন্সি প্রদানের সুযোগ দেয়

বহুমাধ্যমিক সমর্থন ওপেন সোর্স মডেলগুলোর ক্ষেত্রে একটি বড় অগ্রগতি। নীচের কোড উদাহরণটি লামা 3.2 ৯০B থেকে ছবি এবং টেক্সট দুটি প্রম্পট নিয়ে ছবির বিশ্লেষণ পেতে ব্যবহার করা হয়েছে।

### লামা 3.2 দিয়ে বহুমাধ্যমিক সমর্থন

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

## শিখন এখানেই থেমে নেই, সফর অবিরত রাখুন

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার জেনারেটিভ AI জ্ঞানে আরও উন্নতি করতে পারেন!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বছরান্তর**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথির স্থানীয় ভাষাটিকে কর্তৃত্বপূর্ণ সূত্র হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানুষের দ্বারা অনুবাদের সুপারিশ করা হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত যে কোনো ভুল বোঝাবুঝি বা ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->