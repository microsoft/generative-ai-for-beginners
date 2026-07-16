# ساخت با مدل‌های میسترال

## مقدمه

این درس شامل موارد زیر است:
- بررسی مدل‌های مختلف میسترال
- درک کاربردها و سناریوهای هر مدل
- بررسی نمونه‌های کد که ویژگی‌های منحصر به فرد هر مدل را نشان می‌دهند.

## مدل‌های میسترال

در این درس، ما سه مدل مختلف میسترال را بررسی خواهیم کرد:
**میسترال بزرگ**، **میسترال کوچک** و **میسترال نِمو**.

هر یک از این مدل‌ها به صورت رایگان در [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) در دسترس هستند. کد این نت‌بوک از این مدل‌ها برای اجرای کد استفاده خواهد کرد.

> **توجه:** GitHub Models در پایان ژوئیه ۲۰۲۶ بازنشسته خواهد شد. جزئیات بیشتری درباره استفاده از [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) برای نمونه‌سازی با مدل‌های هوش مصنوعی در اینجا موجود است.


## میسترال بزرگ ۲ (2407)
میسترال بزرگ ۲ در حال حاضر مدل پرچمدار از میسترال است و برای استفاده سازمانی طراحی شده است.

این مدل یک ارتقاء نسبت به مدل میسترال بزرگ اصلی است که ارائه می‌دهد:
- پنجره زمینه بزرگ‌تر - ۱۲۸k در برابر ۳۲k
- عملکرد بهتر در وظایف ریاضی و برنامه‌نویسی - دقت متوسط ۷۶.۹٪ در برابر ۶۰.۴٪
- عملکرد چندزبانه بهبود یافته - زبان‌ها شامل: انگلیسی، فرانسوی، آلمانی، اسپانیایی، ایتالیایی، پرتغالی، هلندی، روسی، چینی، ژاپنی، کره‌ای، عربی و هندی.

با این ویژگی‌ها، میسترال بزرگ در موارد زیر برجسته است:
- *تولید تقویت‌شده بازیابی (RAG)* - به دلیل پنجره زمینه بزرگ‌تر
- *فراخوانی تابع* - این مدل دارای فراخوانی تابع بومی است که امکان ادغام با ابزارها و APIهای خارجی را فراهم می‌کند. این فراخوانی‌ها می‌توانند به صورت موازی یا به ترتیب انجام شوند.
- *تولید کد* - این مدل در تولید کدهای پایتون، جاوا، تایپ‌اسکریپت و ++C عملکرد خوبی دارد.

### مثال RAG با استفاده از میسترال بزرگ ۲

در این مثال، از میسترال بزرگ ۲ برای اجرای الگوی RAG روی یک سند متنی استفاده می‌کنیم. پرسش به زبان کره‌ای نوشته شده و درباره فعالیت‌های نویسنده قبل از دانشگاه است.

از مدل تعبیه‌های Cohere برای ایجاد تعبیه از سند متنی و پرسش استفاده می‌کند. برای این نمونه، از بسته پایتون faiss به عنوان فروشگاه برداری استفاده می‌شود.

پیشنهادی که به مدل میسترال ارسال می‌شود، شامل پرسش‌ها و بخش‌های بازیابی شده‌ای است که شبیه پرسش هستند. سپس مدل پاسخ به زبان طبیعی ارائه می‌دهد.

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

# اینها را از صفحه "نمای کلی" پروژه Microsoft Foundry خود دریافت کنید
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

## میسترال کوچک
میسترال کوچک مدل دیگری از خانواده میسترال در دسته بندی پریمیوم/سازمانی است. همانطور که از نامش پیداست، این مدل یک مدل زبان کوچک (SLM) است. مزایای استفاده از میسترال کوچک عبارت‌اند از:
- صرفه‌جویی در هزینه نسبت به مدل‌های بزرگ میسترال مانند میسترال بزرگ و نِمو - کاهش قیمت ۸۰٪
- تأخیر کم - پاسخ سریع‌تر نسبت به مدل‌های بزرگ میسترال
- انعطاف‌پذیری - قابل استقرار در محیط‌های مختلف با محدودیت‌های کمتر در منابع مورد نیاز.


میسترال کوچک برای موارد زیر عالی است:
- وظایف متنی مانند خلاصه‌سازی، تحلیل احساسات و ترجمه.
- کاربردهایی که درخواست‌های مکرر به علت صرفه‌جویی در هزینه دارد
- وظایف کد با تأخیر کم مانند بازبینی و پیشنهاد کد

## مقایسه میسترال کوچک و میسترال بزرگ

برای نشان دادن تفاوت در تأخیر بین میسترال کوچک و بزرگ، سلول‌های زیر را اجرا کنید.

باید تفاوتی در زمان پاسخ بین ۳ تا ۵ ثانیه مشاهده کنید. همچنین طول و سبک پاسخ‌ها روی همان پرسش را توجه نمایید.

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

## میسترال نِمو

در مقایسه با دو مدل دیگر که در این درس بحث شدند، میسترال نِمو تنها مدل رایگان با مجوز Apache2 است.

این مدل به عنوان ارتقاء مدل LLM منبع باز قبلی میسترال، میسترال 7B، شناخته می‌شود.

برخی از ویژگی‌های دیگر مدل نِمو عبارت‌اند از:

- *نشانه‌گذاری مؤثرتر:* این مدل از توکنایزر Tekken استفاده می‌کند که نسبت به tiktoken شایع‌تر است. این امکان عملکرد بهتر روی زبان‌ها و کدهای بیشتر را فراهم می‌کند.

- *فاین‌تونیگ:* مدل پایه برای فاین‌تونیگ در دسترس است. این امکان انعطاف‌پذیری بیشتری برای مواردی که نیاز به فاین‌تونیگ دارند فراهم می‌کند.

- *فراخوانی تابع بومی* - مانند میسترال بزرگ، این مدل نیز برای فراخوانی تابع آموزش دیده است. این ویژگی آن را به یکی از اولین مدل‌های منبع باز تبدیل کرده است که این قابلیت را دارد.


### مقایسه توکنایزرها

در این نمونه، نگاهی می‌اندازیم به نحوه توکن‌سازی مدل میسترال نِمو در مقایسه با میسترال بزرگ.

هر دو نمونه همان پرسش را می‌گیرند اما باید ببینید که نِمو توکن‌های کمتری نسبت به میسترال بزرگ بازمی‌گرداند.

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

# بارگذاری توکنیزر میسترال

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

# توکنایز کردن یک لیست از پیام‌ها
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

## یادگیری اینجا متوقف نمی‌شود، مسیر را ادامه دهید

پس از اتمام این درس، مجموعه [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود را در زمینه هوش مصنوعی مولد ارتقا دهید!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->