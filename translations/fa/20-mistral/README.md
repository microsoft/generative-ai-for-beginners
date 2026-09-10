# ساخت با مدل‌های میسترال

## مقدمه

این درس شامل موارد زیر است:
- بررسی مدل‌های مختلف میسترال
- درک موارد استفاده و سناریوهای هر مدل
- بررسی نمونه‌های کدی که ویژگی‌های منحصر به فرد هر مدل را نشان می‌دهد.

## مدل‌های میسترال

در این درس، سه مدل مختلف میسترال را بررسی خواهیم کرد:
**Mistral Large**، **Mistral Small** و **Mistral Nemo**.

هر یک از این مدل‌ها به صورت رایگان در [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) در دسترس است. کد در این دفترچه از این مدل‌ها برای اجرای کد استفاده خواهد کرد.

> **توجه:** GitHub Models تا پایان ژوئیه ۲۰۲۶ بازنشسته می‌شود. در اینجا جزئیات بیشتری درباره استفاده از [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) برای نمونه‌سازی اولیه با مدل‌های هوش مصنوعی آورده شده است.


## Mistral Large 2 (2407)
میسترال بزرگ ۲ در حال حاضر مدل شاخص میسترال است و برای استفاده سازمانی طراحی شده است.

این مدل ارتقاء یافته مدل اصلی Mistral Large است و ویژگی‌های زیر را ارائه می‌دهد:
- پنجره متنی بزرگ‌تر - ۱۲۸k در مقابل ۳۲k
- عملکرد بهتر در وظایف ریاضی و برنامه‌نویسی - دقت میانگین ۷۶.۹٪ در مقابل ۶۰.۴٪
- عملکرد چندزبانه افزایش یافته - زبان‌ها شامل: انگلیسی، فرانسوی، آلمانی، اسپانیایی، ایتالیایی، پرتغالی، هلندی، روسی، چینی، ژاپنی، کره‌ای، عربی و هندی.

با این ویژگی‌ها، میسترال بزرگ در موارد زیر برجسته است:
- *تولید تقویت‌شده با بازیابی (RAG)* - به دلیل پنجره متن بزرگ‌تر
- *فراخوانی توابع* - این مدل دارای فراخوانی توابع بومی است که امکان ادغام با ابزارها و APIهای خارجی را فراهم می‌کند. این فراخوانی‌ها می‌توانند به صورت همزمان یا یکی پس از دیگری به ترتیب انجام شوند.
- *تولید کد* - این مدل در تولید پایتون، جاوا، تایپ‌اسکریپت و ++C برجسته است.

### نمونه RAG با استفاده از Mistral Large 2

در این مثال، از Mistral Large 2 برای اجرای الگوی RAG روی یک سند متنی استفاده می‌شود. سؤال به زبان کره‌ای نوشته شده و درباره فعالیت‌های نویسنده قبل از دانشگاه پرسیده است.

از مدل Embeddings Cohere برای ایجاد بردارهایی از سند متنی و همچنین سؤال استفاده می‌کند. برای این نمونه، از بسته Python faiss به عنوان مخزن بردار استفاده شده است.

پرامپتی که به مدل میسترال ارسال می‌شود شامل هم سؤال‌ها و هم بخش‌های بازیابی‌شده شبیه به سؤال است. سپس مدل پاسخ به زبان طبیعی ارائه می‌دهد.

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

# این موارد را از صفحه «مرور کلی» پروژه Microsoft Foundry خود بگیرید
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # فاصله، شاخص
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

## Mistral Small
Mistral Small مدل دیگری از خانواده مدل‌های میسترال در دسته بندی پرمیوم/سازمانی است. همانطور که نام آن نشان می‌دهد، این مدل یک مدل زبان کوچک (SLM) است. مزایای استفاده از Mistral Small عبارتند از:
- صرفه‌جویی در هزینه نسبت به مدل‌های LLM میسترال مانند Mistral Large و NeMo - کاهش قیمت ۸۰٪
- تأخیر کم - پاسخ سریع‌تر نسبت به مدل‌های LLM میسترال
- انعطاف‌پذیر - امکان استقرار در محیط‌های مختلف با محدودیت‌های کمتر در منابع مورد نیاز.


Mistral Small برای موارد زیر عالی است:
- وظایف مبتنی بر متن مانند خلاصه‌سازی، تحلیل احساسات و ترجمه.
- کاربردهایی که درخواست‌های مکرر دارند به دلیل به صرفه بودن هزینه
- وظایف کد با تأخیر کم مانند بررسی و پیشنهاد کد

## مقایسه Mistral Small و Mistral Large

برای نشان دادن تفاوت‌های تأخیر بین Mistral Small و Large، سلول‌های زیر را اجرا کنید.

شما باید تفاوتی در زمان پاسخ‌دهی بین ۳ تا ۵ ثانیه مشاهده کنید. همچنین به طول و سبک پاسخ‌ها برای همان پرامپت توجه کنید.

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

## Mistral NeMo

در مقایسه با دو مدل دیگر که در این درس بررسی شدند، Mistral NeMo تنها مدل رایگانی است که دارای مجوز Apache2 است.

این مدل به عنوان ارتقاء مدل منبع باز قبلی میسترال، Mistral 7B، دیده می‌شود.

برخی ویژگی‌های دیگر مدل NeMo عبارتند از:

- *توکن‌سازی کارآمدتر:* این مدل از توکنایزر Tekken به جای tiktoken رایج‌تر استفاده می‌کند. این باعث عملکرد بهتر در زبان‌ها و کدهای بیشتر می‌شود.

- *تنظیم دقیق:* مدل پایه برای تنظیم دقیق در دسترس است. این امکان انعطاف بیشتر برای موارد استفاده‌ای که نیاز به تنظیم دقیق دارند را فراهم می‌کند.

- *فراخوانی توابع بومی* - مانند Mistral Large، این مدل برای فراخوانی توابع آموزش دیده است. این ویژگی آن را به یکی از اولین مدل‌های منبع باز با این قابلیت تبدیل می‌کند.


### مقایسه توکنایزرها

در این نمونه، نحوه توکن‌سازی Mistral NeMo را در مقایسه با Mistral Large بررسی خواهیم کرد.

هر دو نمونه همان پرامپت را می‌گیرند اما باید ببینید که NeMo تعداد توکن‌های کمتری نسبت به Mistral Large برمی‌گرداند.

```bash
pip install mistral-common
```

```python 
# وارد کردن بسته‌های مورد نیاز:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# بارگذاری توکنایزر میسترال

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# توکنیزه کردن یک لیست از پیام‌ها
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

# شمارش تعداد توکن‌ها
print(len(tokens))
```

```python
# وارد کردن بسته‌های مورد نیاز:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# بارگذاری توکنایزر میسترال

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# توکنیزه کردن یک لیست پیام‌ها
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

# شمارش تعداد توکن‌ها
print(len(tokens))
```

## یادگیری اینجا متوقف نمی‌شود، سفر را ادامه دهید

پس از اتمام این درس، مجموعه [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را برای ادامه ارتقای دانش خود در زمینه هوش مصنوعی مولد بررسی کنید!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->