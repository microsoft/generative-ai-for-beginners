<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:46:11+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "fa"
}
-->
# ساخت مدل‌های Mistral

## مقدمه

این درس شامل موارد زیر خواهد بود:
- بررسی مدل‌های مختلف Mistral
- درک موارد استفاده و سناریوهای هر مدل
- نمونه‌های کد که ویژگی‌های منحصر به فرد هر مدل را نشان می‌دهند.

## مدل‌های Mistral

در این درس، ۳ مدل مختلف Mistral را بررسی خواهیم کرد: **Mistral Large**، **Mistral Small** و **Mistral Nemo**.

هر یک از این مدل‌ها به صورت رایگان در بازار مدل‌های Github در دسترس هستند. کد موجود در این دفترچه یادداشت از این مدل‌ها برای اجرای کد استفاده خواهد کرد. در اینجا جزئیات بیشتری درباره استفاده از مدل‌های Github برای [نمونه‌سازی با مدل‌های هوش مصنوعی](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آورده شده است.

## Mistral Large 2 (2407)
Mistral Large 2 در حال حاضر مدل پرچمدار Mistral است و برای استفاده سازمانی طراحی شده است.

این مدل یک ارتقا به مدل اصلی Mistral Large است که ارائه می‌دهد:
- پنجره متنی بزرگتر - ۱۲۸k در مقابل ۳۲k
- عملکرد بهتر در وظایف ریاضی و کدنویسی - دقت متوسط ۷۶.۹٪ در مقابل ۶۰.۴٪
- افزایش عملکرد چندزبانه - زبان‌ها شامل: انگلیسی، فرانسوی، آلمانی، اسپانیایی، ایتالیایی، پرتغالی، هلندی، روسی، چینی، ژاپنی، کره‌ای، عربی و هندی.

با این ویژگی‌ها، Mistral Large در موارد زیر برتری دارد:
- *تولید مبتنی بر بازیابی (RAG)* - به دلیل پنجره متنی بزرگتر
- *فراخوانی تابع* - این مدل دارای فراخوانی تابع بومی است که اجازه می‌دهد با ابزارها و API‌های خارجی ادغام شود. این فراخوانی‌ها می‌توانند به صورت موازی یا به ترتیب یکی پس از دیگری انجام شوند.
- *تولید کد* - این مدل در تولید Python، Java، TypeScript و C++ برتری دارد.

### مثال RAG با استفاده از Mistral Large 2

در این مثال، ما از Mistral Large 2 برای اجرای یک الگوی RAG بر روی یک سند متنی استفاده می‌کنیم. سوال به زبان کره‌ای نوشته شده و درباره فعالیت‌های نویسنده قبل از دانشگاه می‌پرسد.

این مدل از مدل Cohere Embeddings برای ایجاد جاسازی‌های سند متنی و همچنین سوال استفاده می‌کند. برای این نمونه، از بسته Python به نام faiss به عنوان یک فروشگاه برداری استفاده می‌کند.

پرسش ارسالی به مدل Mistral شامل سوالات و قطعات بازیابی شده مشابه سوال است. مدل سپس یک پاسخ به زبان طبیعی ارائه می‌دهد.

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
Mistral Small مدل دیگری در خانواده مدل‌های Mistral در دسته برتر/سازمانی است. همانطور که از نامش پیداست، این مدل یک مدل زبان کوچک (SLM) است. مزایای استفاده از Mistral Small عبارتند از:
- صرفه‌جویی در هزینه در مقایسه با LLMهای Mistral مانند Mistral Large و NeMo - کاهش قیمت ۸۰٪
- تأخیر کم - پاسخ سریعتر در مقایسه با LLMهای Mistral
- انعطاف‌پذیری - می‌تواند در محیط‌های مختلف با محدودیت‌های کمتر بر منابع مورد نیاز مستقر شود.

Mistral Small برای موارد زیر عالی است:
- وظایف مبتنی بر متن مانند خلاصه‌سازی، تحلیل احساسات و ترجمه.
- برنامه‌هایی که درخواست‌های مکرر دارند به دلیل مقرون به صرفه بودن
- وظایف کد با تأخیر کم مانند بررسی و پیشنهادات کد

## مقایسه Mistral Small و Mistral Large

برای نشان دادن تفاوت‌های تأخیر بین Mistral Small و Large، سلول‌های زیر را اجرا کنید.

باید تفاوتی در زمان‌های پاسخ بین ۳-۵ ثانیه مشاهده کنید. همچنین به طول و سبک پاسخ‌ها بر اساس همان درخواست توجه کنید.

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

به عنوان یک ارتقا به LLM منبع باز قبلی Mistral، یعنی Mistral 7B، در نظر گرفته می‌شود.

برخی دیگر از ویژگی‌های مدل NeMo عبارتند از:

- *رمزگذاری کارآمدتر:* این مدل از رمزگذار Tekken به جای tiktoken که معمولاً استفاده می‌شود، استفاده می‌کند. این امر به عملکرد بهتر در زبان‌ها و کدهای بیشتر کمک می‌کند.

- *تنظیم دقیق:* مدل پایه برای تنظیم دقیق در دسترس است. این امر انعطاف‌پذیری بیشتری برای موارد استفاده‌ای که ممکن است نیاز به تنظیم دقیق داشته باشند، فراهم می‌کند.

- *فراخوانی تابع بومی* - مانند Mistral Large، این مدل برای فراخوانی تابع آموزش دیده است. این امر آن را منحصر به فرد می‌کند به عنوان یکی از اولین مدل‌های منبع باز که این کار را انجام می‌دهد.

### مقایسه رمزگذارها

در این نمونه، ما بررسی خواهیم کرد که Mistral NeMo چگونه در مقایسه با Mistral Large رمزگذاری را انجام می‌دهد.

هر دو نمونه از همان درخواست استفاده می‌کنند اما باید مشاهده کنید که NeMo تعداد کمتری رمز را در مقایسه با Mistral Large برمی‌گرداند.

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

## یادگیری در اینجا متوقف نمی‌شود، سفر را ادامه دهید

پس از تکمیل این درس، مجموعه یادگیری [Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا به ارتقای دانش خود در زمینه هوش مصنوعی مولد ادامه دهید!

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.