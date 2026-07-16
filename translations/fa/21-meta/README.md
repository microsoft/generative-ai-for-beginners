# ساخت با مدل‌های خانواده متا

## مقدمه

این درس شامل موارد زیر است:

- بررسی دو مدل اصلی خانواده متا - Llama 3.1 و Llama 3.2
- درک موارد استفاده و سناریوهای هر مدل
- نمونه کد برای نمایش ویژگی‌های منحصر به فرد هر مدل


## خانواده مدل‌های متا

در این درس، ما ۲ مدل از خانواده متا یا "گله لاما" را بررسی خواهیم کرد - Llama 3.1 و Llama 3.2.

این مدل‌ها در انواع مختلف عرضه می‌شوند و در [کتالوگ مدل‌های Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) قابل دسترسی هستند.

> **توجه:** GitHub Models در پایان ژوئیه ۲۰۲۶ بازنشسته خواهد شد. در اینجا جزئیات بیشتری درباره استفاده از [مدل‌های Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) برای نمونه‌سازی با مدل‌های هوش مصنوعی وجود دارد.

انواع مدل‌ها:
- Llama 3.1 - 70 میلیارد پارامتر Instruct
- Llama 3.1 - 405 میلیارد پارامتر Instruct
- Llama 3.2 - 11 میلیارد پارامتر Vision Instruct
- Llama 3.2 - 90 میلیارد پارامتر Vision Instruct

*توجه: Llama 3 نیز در مدل‌های Microsoft Foundry موجود است اما در این درس پوشش داده نمی‌شود*

## Llama 3.1

با ۴۰۵ میلیارد پارامتر، Llama 3.1 در دسته مدل‌های زبان بزرگ متن‌باز قرار می‌گیرد.

این مدل نسبت به نسخه قبلی Llama 3 ارتقا یافته است و ارائه می‌دهد:

- پنجره زمینه بزرگ‌تر - ۱۲۸ هزار توکن در مقابل ۸ هزار توکن
- حداکثر خروجی توکن بیشتر - ۴۰۹۶ در مقابل ۲۰۴۸
- پشتیبانی چندزبانه بهتر - به دلیل افزایش توکن‌های آموزشی

این موارد به Llama 3.1 امکان می‌دهد که موارد استفاده پیچیده‌تری در ساخت برنامه‌های GenAI مانند:
- فراخوانی توابع بومی - توانایی فراخوانی ابزارها و توابع خارجی خارج از جریان کاری LLM
- عملکرد بهتر RAG - به دلیل پنجره زمینه بزرگ‌تر
- تولید داده‌های مصنوعی - توانایی ایجاد داده‌های موثر برای وظایفی مانند تنظیم دقیق

### فراخوانی توابع بومی

Llama 3.1 برای فراخوانی مؤثرتر توابع یا ابزارها بهینه‌سازی شده است. همچنین دو ابزار داخلی دارد که مدل می‌تواند بر اساس راهنمایی کاربر تشخیص دهد که باید از آنها استفاده کند. این ابزارها عبارتند از:

- **Brave Search** - می‌تواند برای دریافت اطلاعات به‌روز مانند وضعیت هوا با انجام جستجوی وب استفاده شود
- **Wolfram Alpha** - می‌تواند برای محاسبات ریاضی پیچیده‌تر استفاده شود تا نیازی به نوشتن توابع خودتان نباشد.

همچنین می‌توانید ابزارهای سفارشی خود را ایجاد کنید که LLM بتواند فراخوانی کند.

در مثال کد زیر:

- ابزارهای موجود (brave_search، wolfram_alpha) را در پیام سیستم تعریف می‌کنیم.
- یک ورودی کاربر ارسال می‌شود که درباره آب و هوا در یک شهر سوال می‌کند.
- LLM با یک فراخوانی ابزار به ابزار Brave Search پاسخ می‌دهد که اینگونه به نظر می‌رسد `<|python_tag|>brave_search.call(query="Stockholm weather")`

*توجه: این مثال فقط فراخوانی ابزار را انجام می‌دهد، اگر می‌خواهید نتایج را بگیرید، باید یک حساب کاربری رایگان در صفحه API Brave ایجاد کرده و خود تابع را تعریف کنید.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# این‌ها را از صفحه "بررسی اجمالی" پروژه Microsoft Foundry خود دریافت کنید
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

با وجود اینکه Llama 3.1 یک LLM است، یکی از محدودیت‌های آن عدم پشتیبانی چندرسانه‌ای است. یعنی ناتوانی در استفاده از انواع ورودی مانند تصاویر به عنوان ورودی و ارائه پاسخ. این ویژگی یکی از قابلیت‌های اصلی Llama 3.2 است. این ویژگی‌ها همچنین شامل:

- چندرسانه‌ای بودن - قابلیت ارزیابی همزمان ورودی‌های متنی و تصویری
- انواع اندازه کوچک تا متوسط (۱۱ میلیارد و ۹۰ میلیارد) - که گزینه‌های استقرار انعطاف‌پذیر را فراهم می‌کند،
- انواع فقط متنی (۱ میلیارد و ۳ میلیارد) - که امکان استقرار مدل روی دستگاه‌های لبه/موبایل و فراهم کردن تأخیر کم را می‌دهد

پشتیبانی چندرسانه‌ای گام بزرگی در دنیای مدل‌های متن‌باز است. مثال کد زیر با استفاده از تصویر و ورودی متنی، تحلیل تصویری از Llama 3.2 90B می‌گیرد.


### پشتیبانی چندرسانه‌ای با Llama 3.2

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

# این موارد را از صفحه "نمای کلی" پروژه Microsoft Foundry خود دریافت کنید
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

## یادگیری اینجا متوقف نمی‌شود، سفر را ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود در زمینه هوش مصنوعی مولد را ارتقاء دهید!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->