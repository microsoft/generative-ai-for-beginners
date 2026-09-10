# মেটা পরিবারের মডেল দিয়ে নির্মাণ 

## পরিচয় 

এই পাঠে নিম্নলিখিত বিষয়গুলি কভার করা হবে: 

- দুইটি প্রধান মেটা পরিবারের মডেল অন্বেষণ করা - Llama 3.1 এবং Llama 3.2 
- প্রতিটি মডেলের ব্যবহারের ক্ষেত্র এবং পরিস্থিতি বোঝা 
- প্রতিটি মডেলের অনন্য বৈশিষ্ট্য প্রদর্শনের জন্য কোড নমুনা 


## মেটা পরিবারের মডেলসমূহ 

এই পাঠে, আমরা মেটা পরিবার বা "Llama Herd"-এর ২টি মডেল অন্বেষণ করব - Llama 3.1 এবং Llama 3.2।

এই মডেলগুলি বিভিন্ন বৈচিত্র্যে আসে এবং [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) এ উপলব্ধ।

> ** লক্ষ্যণীয়:** GitHub Models জুলাই ২০২৬ এর শেষের দিকে বন্ধ হয়ে যাচ্ছে। AI মডেল দিয়ে প্রোটোটাইপ তৈরির জন্য [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ব্যবহারের আরও বিস্তারিত এখানে পাওয়া যাবে।

মডেলের বৈচিত্র্যসমূহ: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*টীকাঃ Llama 3 মাইক্রোসফট ফাউন্ড্রি মডেলস-এও উপলব্ধ কিন্তু এই পাঠে কভার করা হবে না*

## Llama 3.1 

৪০৫ বিলিয়ন প্যারামিটার সহ, Llama 3.1 ওপেন সোর্স LLM বিভাগে পড়ে। 

মডেলটি পূর্বের Llama 3 রিলিজের আপগ্রেড যা প্রদান করে: 

- বড় কনটেক্সট উইন্ডো - ৮ক থেকে ১২৮কে টোকেন 
- বেশি সর্বোচ্চ আউটপুট টোকেন - ২০৪৮ থেকে ৪০৯৬ 
- উন্নত বহুভাষিক সহায়তা - প্রশিক্ষণ টোকেন বৃদ্ধির কারণে 

এরা Llama 3.1-কে জেনারেটিভ AI অ্যাপ্লিকেশন নির্মাণে আরও জটিল ব্যবহারের ক্ষেত্রে সক্ষম করে যেমন: 
- নেটিভ ফাংশন কলিং - LLM ওয়ার্কফ্লোর বাইরে বাহ্যিক টুল এবং ফাংশন কল করার ক্ষমতা 
- ভালো RAG পারফরম্যান্স - উচ্চতর কনটেক্সট উইন্ডোর কারণে 
- সিন্থেটিক ডেটা জেনারেশন - যেসকল কাজে যেমন ফাইন-টিউনিং এর জন্য কার্যকর ডেটা তৈরি করার ক্ষমতা 

### নেটিভ ফাংশন কলিং 

Llama 3.1 ফাংশন বা টুল কল করার ক্ষেত্রে আরও কার্যকর হতে ফাইন-টিউন করা হয়েছে। এতে দুটি বিল্ট-ইন টুল রয়েছে যা মডেল ব্যবহারকারীর প্রম্পট অনুযায়ী ব্যবহার করার জন্য সনাক্ত করতে পারে। এই টুলগুলি হল: 

- **Brave Search** - ওয়েব সার্চ করে আবহাওয়া মতো আপ-টু-ডেট তথ্য পাওয়ার জন্য ব্যবহার করা যেতে পারে 
- **Wolfram Alpha** - জটিল গাণিতিক হিসাবের জন্য ব্যবহার করা যায়, তাই নিজস্ব ফাংশন লেখার প্রয়োজন নেই। 

আপনি আপনার নিজের কাস্টম টুলও তৈরি করতে পারেন যা LLM কল করতে পারে। 

নিচের কোড উদাহরণে: 

- আমরা সিস্টেম প্রম্পটে উপলব্ধ টুলগুলি (brave_search, wolfram_alpha) সংজ্ঞায়িত করেছি। 
- এমন একটি ইউজার প্রম্পট পাঠানো হয়েছে যা একটি শহরের আবহাওয়া সম্পর্কে জিজ্ঞাসা করে। 
- LLM Brave Search টুলের একটি টুল কল দিয়ে প্রতিক্রিয়া দেবে যা এরকম দেখাবে `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*টীকাঃ এই উদাহরণ শুধুমাত্র টুল কল করে, যদি আপনি ফলাফল পেতে চান তবে Brave API পেজে একটি ফ্রি অ্যাকাউন্ট তৈরি করে ফাংশন নিজেই সংজ্ঞায়িত করতে হবে।*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# এগুলো আপনার Microsoft Foundry প্রকল্পের "ওভারভিউ" পৃষ্ঠাটি থেকে নিন
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

## Llama 3.2 

Llama 3.1 একটি LLM হলেও, এর একটি সীমাবদ্ধতা হল এর মাল্টিমোডালিটির অভাব, অর্থাৎ বিভিন্ন ধরনের ইনপুট যেমন ছবি প্রম্পট হিসেবে ব্যবহার করা এবং প্রতিক্রিয়া প্রদান করার অক্ষমতা। এই ক্ষমতা Llama 3.2-এর প্রধান বৈশিষ্ট্যগুলোর একটি। এই বৈশিষ্ট্যগুলোর মধ্যে রয়েছে: 

- মাল্টিমোডালিটি - পাঠ্য ও ছবি উভয় প্রম্পট মূল্যায়ন করার ক্ষমতা 
- ছোট থেকে মাঝারি আকারের বৈচিত্র্য (১১বি এবং ৯০বি) - যা নমনীয় স্থাপন বিকল্প প্রদান করে, 
- শুধুমাত্র পাঠ্য বৈচিত্র্য (১বি এবং ৩বি) - মডেলকে এজ/মোবাইল ডিভাইসে স্থাপন এবং কম বিলম্ব সক্ষম করে 

মাল্টিমোডাল সাপোর্ট ওপেন সোর্স মডেলের জগতে একটি বড় পদক্ষেপ। নিচের কোড উদাহরণে Llama 3.2 90B থেকে ছবি ও পাঠ্য প্রম্পট দিয়ে ছবির বিশ্লেষণ নেওয়া হয়েছে। 


### Llama 3.2 এর মাল্টিমোডাল সাপোর্ট

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

# এগুলো আপনার Microsoft Foundry প্রকল্পের "সংক্ষিপ্ত বিবরণ" পৃষ্ঠার থেকে পান।
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

## শেখা এখানেই থেমে থাকে না, যাত্রা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন এবং আপনার Generative AI জ্ঞানে আরও উন্নতি করুন!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->