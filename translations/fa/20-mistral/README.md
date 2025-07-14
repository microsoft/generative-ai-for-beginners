<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:56:09+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fa"
}
-->
# ساخت با مدل‌های Mistral

## مقدمه

این درس شامل موارد زیر است:  
- بررسی مدل‌های مختلف Mistral  
- درک کاربردها و سناریوهای هر مدل  
- نمونه‌های کد که ویژگی‌های منحصر به فرد هر مدل را نشان می‌دهند.

## مدل‌های Mistral

در این درس، سه مدل مختلف Mistral را بررسی خواهیم کرد:  
**Mistral Large**، **Mistral Small** و **Mistral Nemo**.

هر یک از این مدل‌ها به صورت رایگان در بازار مدل‌های Github در دسترس هستند. کد این دفترچه از این مدل‌ها برای اجرای کد استفاده می‌کند. در اینجا جزئیات بیشتری درباره استفاده از مدل‌های Github برای [نمونه‌سازی با مدل‌های هوش مصنوعی](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آمده است.

## Mistral Large 2 (2407)  
Mistral Large 2 در حال حاضر مدل اصلی و پرچمدار Mistral است و برای استفاده سازمانی طراحی شده است.

این مدل ارتقاءیافته مدل اصلی Mistral Large است و ویژگی‌های زیر را ارائه می‌دهد:  
- پنجره متنی بزرگ‌تر - ۱۲۸ هزار در مقابل ۳۲ هزار  
- عملکرد بهتر در وظایف ریاضی و برنامه‌نویسی - دقت متوسط ۷۶.۹٪ در مقابل ۶۰.۴٪  
- بهبود عملکرد چندزبانه - زبان‌ها شامل: انگلیسی، فرانسوی، آلمانی، اسپانیایی، ایتالیایی، پرتغالی، هلندی، روسی، چینی، ژاپنی، کره‌ای، عربی و هندی.

با این ویژگی‌ها، Mistral Large در موارد زیر برجسته است:  
- *تولید تقویت‌شده با بازیابی (RAG)* - به دلیل پنجره متنی بزرگ‌تر  
- *فراخوانی توابع* - این مدل دارای فراخوانی توابع بومی است که امکان ادغام با ابزارها و APIهای خارجی را فراهم می‌کند. این فراخوانی‌ها می‌توانند به صورت موازی یا به ترتیب انجام شوند.  
- *تولید کد* - این مدل در تولید کدهای Python، Java، TypeScript و C++ عملکرد بسیار خوبی دارد.

### نمونه RAG با استفاده از Mistral Large 2

در این مثال، از Mistral Large 2 برای اجرای الگوی RAG روی یک سند متنی استفاده می‌کنیم. سوال به زبان کره‌ای نوشته شده و درباره فعالیت‌های نویسنده قبل از دانشگاه پرسیده است.

از مدل Embeddings شرکت Cohere برای ایجاد بردارهای متنی سند و سوال استفاده می‌شود. در این نمونه، از بسته Python به نام faiss به عنوان فروشگاه برداری استفاده شده است.

پرومپتی که به مدل Mistral ارسال می‌شود شامل سوالات و بخش‌های بازیابی شده‌ای است که به سوال شباهت دارند. سپس مدل پاسخ به زبان طبیعی ارائه می‌دهد.

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
Mistral Small مدل دیگری از خانواده مدل‌های Mistral است که در دسته مدل‌های پرمیوم/سازمانی قرار دارد. همانطور که از نامش پیداست، این مدل یک مدل زبان کوچک (SLM) است. مزایای استفاده از Mistral Small عبارتند از:  
- صرفه‌جویی در هزینه نسبت به مدل‌های بزرگ‌تر Mistral مانند Mistral Large و NeMo - کاهش قیمت تا ۸۰٪  
- تأخیر کم - پاسخ سریع‌تر نسبت به مدل‌های بزرگ Mistral  
- انعطاف‌پذیری - قابلیت استقرار در محیط‌های مختلف با محدودیت‌های کمتر در منابع مورد نیاز.

Mistral Small برای موارد زیر بسیار مناسب است:  
- وظایف متنی مانند خلاصه‌سازی، تحلیل احساسات و ترجمه  
- برنامه‌هایی که درخواست‌های مکرر دارند به دلیل صرفه‌جویی در هزینه  
- وظایف کد با تأخیر کم مانند بازبینی و پیشنهاد کد

## مقایسه Mistral Small و Mistral Large

برای مشاهده تفاوت در تأخیر بین Mistral Small و Large، سلول‌های زیر را اجرا کنید.

باید تفاوتی در زمان پاسخ بین ۳ تا ۵ ثانیه مشاهده کنید. همچنین به طول و سبک پاسخ‌ها در پرومپت یکسان توجه کنید.

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

در مقایسه با دو مدل دیگر که در این درس بررسی شدند، Mistral NeMo تنها مدل رایگان با مجوز Apache2 است.

این مدل به عنوان ارتقاء مدل متن‌باز قبلی Mistral، یعنی Mistral 7B، شناخته می‌شود.

برخی ویژگی‌های دیگر مدل NeMo عبارتند از:

- *توکن‌سازی بهینه‌تر:* این مدل از توکنایزر Tekken استفاده می‌کند که نسبت به توکنایزر رایج tiktoken عملکرد بهتری در زبان‌ها و کدهای مختلف دارد.

- *فاین‌تیونینگ:* مدل پایه برای فاین‌تیونینگ در دسترس است که امکان انعطاف بیشتر برای کاربردهایی که نیاز به فاین‌تیونینگ دارند را فراهم می‌کند.

- *فراخوانی توابع بومی* - مانند Mistral Large، این مدل نیز روی فراخوانی توابع آموزش دیده است. این ویژگی آن را به یکی از اولین مدل‌های متن‌باز با این قابلیت تبدیل کرده است.

### مقایسه توکنایزرها

در این نمونه، نحوه توکن‌سازی Mistral NeMo را در مقایسه با Mistral Large بررسی می‌کنیم.

هر دو نمونه از یک پرومپت یکسان استفاده می‌کنند اما باید ببینید که NeMo تعداد توکن‌های کمتری نسبت به Mistral Large برمی‌گرداند.

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

## یادگیری اینجا تمام نمی‌شود، سفر را ادامه دهید

پس از اتمام این درس، مجموعه [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود در زمینه هوش مصنوعی مولد را ارتقا دهید!

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.