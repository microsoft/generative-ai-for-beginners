<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:06:14+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fa"
}
-->
# ساختن با مدل‌های خانواده متا

## مقدمه

این درس شامل موارد زیر است:

- بررسی دو مدل اصلی خانواده متا - Llama 3.1 و Llama 3.2
- درک موارد استفاده و سناریوهای هر مدل
- نمونه کد برای نشان دادن ویژگی‌های منحصر به فرد هر مدل

## خانواده مدل‌های متا

در این درس، ما به بررسی 2 مدل از خانواده متا یا "گله لاما" - Llama 3.1 و Llama 3.2 خواهیم پرداخت.

این مدل‌ها در واریانت‌های مختلف عرضه می‌شوند و در بازار مدل GitHub در دسترس هستند. در اینجا جزئیات بیشتری درباره استفاده از مدل‌های GitHub برای [نمونه‌سازی با مدل‌های AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آورده شده است.

واریانت‌های مدل:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*توجه: Llama 3 نیز در مدل‌های GitHub موجود است اما در این درس پوشش داده نمی‌شود*

## Llama 3.1

با 405 میلیارد پارامتر، Llama 3.1 در دسته LLM های منبع باز قرار می‌گیرد.

این مدل ارتقاء‌یافته به نسخه قبلی Llama 3 با ارائه:

- پنجره متنی بزرگ‌تر - 128k توکن در مقابل 8k توکن
- حداکثر خروجی توکن بزرگ‌تر - 4096 در مقابل 2048
- پشتیبانی بهتر چندزبانه - به دلیل افزایش توکن‌های آموزشی

این ویژگی‌ها به Llama 3.1 امکان می‌دهند تا موارد استفاده پیچیده‌تری را در هنگام ساخت برنامه‌های GenAI مدیریت کند، از جمله:
- فراخوانی عملکرد بومی - توانایی فراخوانی ابزارها و عملکردهای خارجی خارج از جریان کار LLM
- عملکرد بهتر RAG - به دلیل پنجره متنی بزرگ‌تر
- تولید داده مصنوعی - توانایی ایجاد داده مؤثر برای وظایفی مانند تنظیم دقیق

### فراخوانی عملکرد بومی

Llama 3.1 به گونه‌ای تنظیم شده است که در فراخوانی عملکردها یا ابزارها مؤثرتر باشد. همچنین دو ابزار داخلی دارد که مدل می‌تواند بر اساس درخواست کاربر تشخیص دهد که نیاز به استفاده از آن‌ها است. این ابزارها عبارتند از:

- **Brave Search** - می‌تواند برای دریافت اطلاعات به‌روز مانند آب و هوا با انجام جستجوی وب استفاده شود
- **Wolfram Alpha** - می‌تواند برای محاسبات ریاضی پیچیده‌تر استفاده شود، بنابراین نیازی به نوشتن عملکردهای خودتان نیست.

شما همچنین می‌توانید ابزارهای سفارشی خود را ایجاد کنید که LLM می‌تواند آن‌ها را فراخوانی کند.

در مثال کد زیر:

- ما ابزارهای موجود (brave_search, wolfram_alpha) را در درخواست سیستم تعریف می‌کنیم.
- یک درخواست کاربر ارسال می‌کنیم که درباره آب و هوای یک شهر خاص می‌پرسد.
- LLM با یک فراخوانی ابزار به ابزار Brave Search پاسخ می‌دهد که به این شکل خواهد بود `<|python_tag|>brave_search.call(query="Stockholm weather")`

*توجه: این مثال فقط فراخوانی ابزار را انجام می‌دهد، اگر می‌خواهید نتایج را دریافت کنید، باید یک حساب کاربری رایگان در صفحه API Brave ایجاد کنید و خود عملکرد را تعریف کنید*

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

## Llama 3.2

با وجود اینکه LLM است، یکی از محدودیت‌های Llama 3.1 چندحالتی بودن است. یعنی، توانایی استفاده از انواع مختلف ورودی مانند تصاویر به عنوان درخواست و ارائه پاسخ‌ها. این توانایی یکی از ویژگی‌های اصلی Llama 3.2 است. این ویژگی‌ها همچنین شامل:

- چندحالتی - توانایی ارزیابی هر دو درخواست متنی و تصویری
- واریانت‌های کوچک تا متوسط (11B و 90B) - این امکان را برای گزینه‌های استقرار انعطاف‌پذیر فراهم می‌کند،
- واریانت‌های فقط متنی (1B و 3B) - این امکان را می‌دهد تا مدل بر روی دستگاه‌های لبه / موبایل مستقر شود و تأخیر کمی داشته باشد

پشتیبانی چندحالتی نمایانگر یک گام بزرگ در دنیای مدل‌های منبع باز است. مثال کد زیر هم یک تصویر و هم یک درخواست متنی را می‌گیرد تا تحلیل تصویر از Llama 3.2 90B را دریافت کند.

### پشتیبانی چندحالتی با Llama 3.2

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

## یادگیری در اینجا متوقف نمی‌شود، به سفر ادامه دهید

پس از تکمیل این درس، به [مجموعه یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما سر بزنید تا به ارتقاء دانش خود در زمینه هوش مصنوعی مولد ادامه دهید!

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌ها باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.