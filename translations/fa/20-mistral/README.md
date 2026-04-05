# ساخت با مدل‌های میسترال

## مقدمه

این درس شامل موارد زیر است:  
- بررسی انواع مدل‌های میسترال  
- درک کاربردها و سناریوهای هر مدل  
- بررسی نمونه کدهایی که ویژگی‌های منحصر به فرد هر مدل را نشان می‌دهد.

## مدل‌های میسترال

در این درس، ما سه مدل مختلف میسترال را بررسی می‌کنیم:  
**میسترال بزرگ**، **میسترال کوچک** و **میسترال نِمو**.

هر یک از این مدل‌ها به‌صورت رایگان در بازار مدل گیت‌هاب در دسترس هستند. کد این دفترچه از این مدل‌ها برای اجرای کد استفاده می‌کند. در اینجا جزئیات بیشتری درباره استفاده از مدل‌های گیت‌هاب برای [نمونه‌سازی با مدل‌های هوش مصنوعی](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آمده است.

## میسترال بزرگ 2 (2407)  
میسترال بزرگ 2 در حال حاضر مدل شاخص میسترال است و برای استفاده سازمانی طراحی شده است.

این مدل یک ارتقاء نسبت به میسترال بزرگ اصلی است که ارائه می‌دهد:  
- پنجره متن زمینه بزرگ‌تر - ۱۲۸ هزار در مقابل ۳۲ هزار  
- عملکرد بهتر در مسائل ریاضی و برنامه‌نویسی - دقت متوسط ۷۶.۹٪ در مقابل ۶۰.۴٪  
- عملکرد چندزبانه افزایش یافته – زبان‌ها شامل: انگلیسی، فرانسوی، آلمانی، اسپانیایی، ایتالیایی، پرتغالی، هلندی، روسی، چینی، ژاپنی، کره‌ای، عربی و هندی هستند.

با این ویژگی‌ها، میسترال بزرگ در موارد زیر برجسته است:  
- *تولید افزایشی بازیابی‌شده (RAG)* – به دلیل پنجره متنی بزرگ‌تر  
- *صدا زدن توابع* – این مدل دارای قابلیت بومی برای صدا زدن توابع است که اجازه یکپارچه‌سازی با ابزارها و APIهای خارجی را می‌دهد. این صداها هم به صورت موازی و هم به صورت ترتیبی قابل انجام هستند.  
- *تولید کد* – این مدل در تولید کدهای پایتون، جاوا، تایپ‌اسکریپت و C++ عملکرد خوبی دارد.

### نمونه RAG با استفاده از میسترال بزرگ 2

در این مثال، ما از میسترال بزرگ 2 برای اجرای الگوی RAG روی یک سند متنی استفاده می‌کنیم. سوال به زبان کره‌ای نوشته شده و درباره فعالیت‌های نویسنده قبل از دانشگاه می‌پرسد.

از مدل embedings کوهیر برای ایجاد embeddingهای سند متنی و سوال استفاده می‌کند. برای این نمونه از بسته پایتون faiss به عنوان ذخیره‌ساز برداری استفاده شده است.

پیام ارسالی به مدل میسترال شامل سوالات و بخش‌های بازیابی شده مشابه با سوال است. مدل سپس پاسخ به زبان طبیعی ارائه می‌دهد.

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # فاصله، اندیس
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
میسترال کوچک مدل دیگری از خانواده مدل‌های میسترال است که در دسته سازمانی و پرمیر قرار دارد. همانطور که از نامش پیداست، این مدل یک مدل زبان کوچک (SLM) است. مزایای استفاده از میسترال کوچک عبارتند از:  
- صرفه‌جویی در هزینه نسبت به مدل‌های بزرگ میسترال مانند میسترال بزرگ و NeMo - کاهش قیمت ۸۰٪  
- تأخیر پایین - پاسخ سریع‌تر نسبت به مدل‌های بزرگ میسترال  
- انعطاف‌پذیری – قابلیت استقرار در محیط‌های مختلف با محدودیت‌های منابع کمتر.

میسترال کوچک برای موارد زیر عالی است:  
- وظایف متنی مانند خلاصه‌سازی، تحلیل احساسات و ترجمه.  
- برنامه‌هایی که درخواست‌های مکرر دارند به دلیل صرفه‌جویی در هزینه  
- وظایف کدی با تأخیر پایین مانند بازبینی و پیشنهاد کد

## مقایسه میسترال کوچک و میسترال بزرگ

برای مشاهده تفاوت‌های تأخیر بین میسترال کوچک و بزرگ، سلول‌های زیر را اجرا کنید.

باید تفاوتی در زمان پاسخ بین ۳ تا ۵ ثانیه مشاهده کنید. همچنین به طول پاسخ‌ها و سبک آنها در همان پیام دقت کنید.

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

در مقایسه با دو مدل دیگر که در این درس بررسی شدند، میسترال نِمو تنها مدل رایگان با مجوز Apache2 است.

این مدل به عنوان یک ارتقاء به مدل متن‌باز قبلی میسترال، میسترال 7B، شناخته می‌شود.

برخی ویژگی‌های دیگر مدل نِمو عبارتند از:

- *توکنیزه کردن کارآمدتر:* این مدل از توکنیزر Tekken استفاده می‌کند که برتری نسبت به توکنیزر رایج‌تر tiktoken دارد. این امر عملکرد بهتری بر روی زبان‌ها و کدهای بیشتر فراهم می‌کند.

- *تنظیم دقیق (Finetuning):* مدل پایه برای تنظیم دقیق در دسترس است. این امکان انعطاف بیشتر برای موارد استفاده فراهم می‌کند که نیاز به تنظیم دقیق دارند.

- *صدازدن توابع به صورت بومی* - مانند میسترال بزرگ، این مدل نیز برای صدازدن توابع آموزش دیده است. این امر آن را به یکی از اولین مدل‌های متن‌باز با چنین قابلیتی تبدیل می‌کند.

### مقایسه توکنیزرها

در این نمونه، نگاه می‌کنیم که چگونه میسترال نِمو توکنیزه کردن را در مقایسه با میسترال بزرگ انجام می‌دهد.

هر دو نمونه همان پیام را می‌گیرند اما باید ببینید که نِمو توکن‌های کمتری نسبت به میسترال بزرگ برمی‌گرداند.

```bash
pip install mistral-common
```
  
```python 
# وارد کردن بسته‌های لازم:
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

# شمردن تعداد توکن‌ها
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

# توکنیزه کردن لیستی از پیام‌ها
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
  
## یادگیری اینجا تمام نمی‌شود، سفر را ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود در زمینه هوش مصنوعی مولد را افزایش دهید!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیح**:  
این سند با استفاده از سرویس ترجمه مبتنی بر هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید منبع معتبر تلقی شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->