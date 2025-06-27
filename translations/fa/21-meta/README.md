<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:26:18+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fa"
}
-->
# ساخت با مدل‌های خانواده متا

## مقدمه

این درس شامل موارد زیر خواهد بود:

- بررسی دو مدل اصلی خانواده متا - لاما 3.1 و لاما 3.2
- درک موارد استفاده و سناریوها برای هر مدل
- نمونه کد برای نشان دادن ویژگی‌های منحصر به فرد هر مدل

## خانواده مدل‌های متا

در این درس، دو مدل از خانواده متا یا "گله لاما" - لاما 3.1 و لاما 3.2 - را بررسی خواهیم کرد.

این مدل‌ها در انواع مختلف ارائه می‌شوند و در بازار مدل GitHub موجود هستند. جزئیات بیشتر در مورد استفاده از مدل‌های GitHub برای [پروتوتایپ‌سازی با مدل‌های هوش مصنوعی](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) را می‌توانید مشاهده کنید.

انواع مدل‌ها:
- لاما 3.1 - 70B دستورالعمل
- لاما 3.1 - 405B دستورالعمل
- لاما 3.2 - 11B دستورالعمل بینایی
- لاما 3.2 - 90B دستورالعمل بینایی

*توجه: لاما 3 نیز در مدل‌های GitHub موجود است اما در این درس پوشش داده نخواهد شد*

## لاما 3.1

با 405 میلیارد پارامتر، لاما 3.1 در دسته‌بندی LLM منبع باز قرار می‌گیرد.

این مدل نسبت به نسخه قبلی لاما 3 ارتقا یافته است و ارائه می‌دهد:

- پنجره متن بزرگتر - 128k توکن در مقابل 8k توکن
- توکن‌های خروجی حداکثر بزرگتر - 4096 در مقابل 2048
- پشتیبانی چندزبانه بهتر - به دلیل افزایش در توکن‌های آموزشی

این ویژگی‌ها به لاما 3.1 امکان می‌دهد تا موارد استفاده پیچیده‌تری را هنگام ساخت برنامه‌های GenAI مدیریت کند، از جمله:
- فراخوانی تابع بومی - توانایی فراخوانی ابزارها و توابع خارجی خارج از جریان کاری LLM
- عملکرد RAG بهتر - به دلیل پنجره متن بزرگتر
- تولید داده مصنوعی - توانایی ایجاد داده‌های مؤثر برای وظایفی مانند تنظیم دقیق

### فراخوانی تابع بومی

لاما 3.1 برای انجام فراخوانی‌های تابع یا ابزار به شکل مؤثرتر تنظیم شده است. همچنین دارای دو ابزار داخلی است که مدل می‌تواند بر اساس درخواست کاربر تشخیص دهد که باید استفاده شود. این ابزارها عبارتند از:

- **جستجوی شجاع** - می‌توان از آن برای دریافت اطلاعات به‌روز مانند آب‌وهوا با انجام جستجوی وب استفاده کرد
- **ولفرام آلفا** - می‌توان از آن برای محاسبات ریاضی پیچیده‌تر استفاده کرد، بنابراین نیازی به نوشتن توابع خود نیست.

شما همچنین می‌توانید ابزارهای سفارشی خود را ایجاد کنید که LLM بتواند آنها را فراخوانی کند.

در مثال کد زیر:

- ابزارهای موجود (brave_search، wolfram_alpha) را در درخواست سیستم تعریف می‌کنیم.
- درخواست کاربری ارسال می‌کنیم که درباره آب‌وهوای یک شهر خاص سوال می‌کند.
- LLM با یک فراخوانی ابزار به ابزار جستجوی شجاع پاسخ خواهد داد که به این شکل خواهد بود `<|python_tag|>brave_search.call(query="Stockholm weather")`

*توجه: این مثال فقط فراخوانی ابزار را انجام می‌دهد، اگر می‌خواهید نتایج را دریافت کنید، باید یک حساب رایگان در صفحه API شجاع ایجاد کنید و خود تابع را تعریف کنید*

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

## لاما 3.2

علیرغم اینکه یک LLM است، یکی از محدودیت‌هایی که لاما 3.1 دارد، چندحالتی بودن است. یعنی توانایی استفاده از انواع مختلف ورودی مانند تصاویر به عنوان درخواست و ارائه پاسخ‌ها. این توانایی یکی از ویژگی‌های اصلی لاما 3.2 است. این ویژگی‌ها همچنین شامل:

- چندحالتی بودن - توانایی ارزیابی درخواست‌های متنی و تصویری
- تنوع اندازه کوچک تا متوسط (11B و 90B) - این گزینه‌های استقرار انعطاف‌پذیر را فراهم می‌کند،
- تنوع فقط متنی (1B و 3B) - این امکان را فراهم می‌کند که مدل روی دستگاه‌های لبه / موبایل مستقر شود و تاخیر کم را فراهم کند

پشتیبانی چندحالتی نمایانگر یک قدم بزرگ در دنیای مدل‌های منبع باز است. مثال کد زیر هم یک تصویر و هم درخواست متنی را برای دریافت تحلیل تصویر از لاما 3.2 90B دریافت می‌کند.

### پشتیبانی چندحالتی با لاما 3.2

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

پس از تکمیل این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا به ارتقاء دانش خود در زمینه هوش مصنوعی مولد ادامه دهید!

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال هرگونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.