<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:11:35+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fa"
}
-->
# ساختن با مدل‌های Mistral

## مقدمه

این درس شامل موارد زیر خواهد بود:
- بررسی مدل‌های مختلف Mistral
- درک موارد استفاده و سناریوهای هر مدل
- نمونه‌های کد که ویژگی‌های منحصر به فرد هر مدل را نشان می‌دهند.

## مدل‌های Mistral

در این درس، ما به بررسی ۳ مدل مختلف Mistral خواهیم پرداخت: **Mistral Large**، **Mistral Small** و **Mistral Nemo**.

هر یک از این مدل‌ها به صورت رایگان در بازار مدل‌های Github در دسترس هستند. کد موجود در این دفترچه یادداشت از این مدل‌ها برای اجرای کد استفاده خواهد کرد. در اینجا جزئیات بیشتری درباره استفاده از مدل‌های Github برای [نمونه‌سازی با مدل‌های AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آمده است.

## Mistral Large 2 (2407)
Mistral Large 2 در حال حاضر مدل اصلی Mistral است و برای استفاده در سازمان‌ها طراحی شده است.

این مدل ارتقاء یافته مدل اصلی Mistral Large است که ارائه می‌دهد:
- پنجره متن بزرگتر - ۱۲۸k در مقابل ۳۲k
- عملکرد بهتر در وظایف ریاضی و کدنویسی - دقت متوسط ۷۶.۹٪ در مقابل ۶۰.۴٪
- افزایش عملکرد چندزبانه - زبان‌ها شامل: انگلیسی، فرانسوی، آلمانی، اسپانیایی، ایتالیایی، پرتغالی، هلندی، روسی، چینی، ژاپنی، کره‌ای، عربی و هندی هستند.

با این ویژگی‌ها، Mistral Large در موارد زیر برتری دارد:
- *تولید افزایش‌یافته بازیابی (RAG)* - به دلیل پنجره متن بزرگتر
- *فراخوانی توابع* - این مدل دارای فراخوانی توابع بومی است که امکان ادغام با ابزارها و APIهای خارجی را فراهم می‌کند. این فراخوانی‌ها می‌توانند هم به صورت موازی و هم یکی پس از دیگری در یک ترتیب متوالی انجام شوند.
- *تولید کد* - این مدل در تولید Python، Java، TypeScript و C++ برتری دارد.

### مثال RAG با استفاده از Mistral Large 2

در این مثال، ما از Mistral Large 2 برای اجرای یک الگوی RAG بر روی یک سند متنی استفاده می‌کنیم. سؤال به زبان کره‌ای نوشته شده و درباره فعالیت‌های نویسنده قبل از دانشگاه می‌پرسد.

این مدل از مدل Embeddings Cohere برای ایجاد تعبیه‌های سند متنی و همچنین سؤال استفاده می‌کند. برای این نمونه، از بسته Python faiss به عنوان یک ذخیره‌سازی برداری استفاده می‌شود.

پیشنهاد ارسال شده به مدل Mistral شامل هم سؤال‌ها و هم قطعات بازیابی شده مشابه سؤال است. سپس مدل پاسخ به زبان طبیعی ارائه می‌دهد.

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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
Mistral Small مدل دیگری در خانواده مدل‌های Mistral تحت دسته‌بندی اصلی/سازمانی است. همانطور که از نامش پیداست، این مدل یک مدل زبان کوچک (SLM) است. مزایای استفاده از Mistral Small این است که:
- صرفه‌جویی در هزینه در مقایسه با LLMهای Mistral مانند Mistral Large و NeMo - کاهش قیمت ۸۰٪
- تأخیر کم - پاسخ سریع‌تر در مقایسه با LLMهای Mistral
- انعطاف‌پذیر - می‌تواند در محیط‌های مختلف با محدودیت کمتر در منابع مورد نیاز مستقر شود.

Mistral Small برای موارد زیر عالی است:
- وظایف مبتنی بر متن مانند خلاصه‌سازی، تحلیل احساسات و ترجمه.
- برنامه‌هایی که به دلیل صرفه‌جویی در هزینه، درخواست‌های مکرر دارند.
- وظایف کدنویسی با تأخیر کم مانند بررسی و پیشنهادات کد.

## مقایسه Mistral Small و Mistral Large

برای نشان دادن تفاوت‌های تأخیر بین Mistral Small و Large، سلول‌های زیر را اجرا کنید.

باید تفاوتی در زمان پاسخ بین ۳-۵ ثانیه مشاهده کنید. همچنین طول و سبک پاسخ‌ها بر روی همان پیشنهاد را یادداشت کنید.

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

## Mistral NeMo

در مقایسه با دو مدل دیگر مورد بحث در این درس، Mistral NeMo تنها مدل رایگان با مجوز Apache2 است.

این مدل به عنوان ارتقاء به LLM منبع باز قبلی Mistral، Mistral 7B، در نظر گرفته می‌شود.

برخی از ویژگی‌های دیگر مدل NeMo عبارتند از:

- *رمزگذاری کارآمدتر:* این مدل از رمزگذار Tekken به جای رمزگذار معمولی tiktoken استفاده می‌کند. این امکان عملکرد بهتر بر روی زبان‌ها و کدهای بیشتر را فراهم می‌کند.

- *تنظیم دقیق:* مدل پایه برای تنظیم دقیق در دسترس است. این امکان انعطاف‌پذیری بیشتری برای موارد استفاده‌ای که ممکن است تنظیم دقیق نیاز باشد، فراهم می‌کند.

- *فراخوانی توابع بومی* - مانند Mistral Large، این مدل بر روی فراخوانی توابع آموزش دیده است. این مدل به عنوان یکی از اولین مدل‌های منبع باز که این کار را انجام می‌دهد، منحصر به فرد است.

### مقایسه رمزگذارها

در این نمونه، ما به نحوه مدیریت رمزگذاری Mistral NeMo در مقایسه با Mistral Large نگاه خواهیم کرد.

هر دو نمونه همان پیشنهاد را می‌گیرند اما باید ببینید که NeMo تعداد کمتری از توکن‌ها را نسبت به Mistral Large بازمی‌گرداند.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## یادگیری اینجا متوقف نمی‌شود، ادامه مسیر

پس از تکمیل این درس، مجموعه [یادگیری AI تولیدی](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا به ارتقاء دانش AI تولیدی خود ادامه دهید!

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم یا سوء تفسیر ناشی از استفاده از این ترجمه نداریم.