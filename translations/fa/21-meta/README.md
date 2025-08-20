<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:06:24+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "fa"
}
-->
# ساخت با مدل‌های خانواده متا

## مقدمه

این درس شامل موارد زیر است:

- بررسی دو مدل اصلی خانواده متا - Llama 3.1 و Llama 3.2  
- درک کاربردها و سناریوهای هر مدل  
- نمونه کد برای نمایش ویژگی‌های منحصر به فرد هر مدل  

## خانواده مدل‌های متا

در این درس، دو مدل از خانواده متا یا "Llama Herd" را بررسی می‌کنیم - Llama 3.1 و Llama 3.2

این مدل‌ها در نسخه‌های مختلفی عرضه شده و در بازار مدل‌های گیت‌هاب در دسترس هستند. در اینجا جزئیات بیشتری درباره استفاده از مدل‌های گیت‌هاب برای [نمونه‌سازی با مدل‌های هوش مصنوعی](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آورده شده است.

نسخه‌های مدل:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*توجه: Llama 3 نیز در مدل‌های گیت‌هاب موجود است اما در این درس پوشش داده نمی‌شود*

## Llama 3.1

با ۴۰۵ میلیارد پارامتر، Llama 3.1 در دسته مدل‌های متن‌باز LLM قرار می‌گیرد.

این مدل نسبت به نسخه قبلی Llama 3 ارتقا یافته و امکانات زیر را ارائه می‌دهد:

- پنجره متنی بزرگ‌تر - ۱۲۸ هزار توکن در مقابل ۸ هزار توکن  
- حداکثر توکن خروجی بیشتر - ۴۰۹۶ در مقابل ۲۰۴۸  
- پشتیبانی بهتر چندزبانه - به دلیل افزایش تعداد توکن‌های آموزشی  

این ویژگی‌ها به Llama 3.1 امکان می‌دهد تا در ساخت برنامه‌های GenAI موارد پیچیده‌تری را مدیریت کند، از جمله:  
- فراخوانی توابع بومی - توانایی فراخوانی ابزارها و توابع خارجی خارج از جریان کاری LLM  
- عملکرد بهتر RAG - به دلیل پنجره متنی بزرگ‌تر  
- تولید داده‌های مصنوعی - توانایی ایجاد داده‌های مؤثر برای وظایفی مانند تنظیم دقیق  

### فراخوانی توابع بومی

Llama 3.1 به گونه‌ای تنظیم شده که در فراخوانی توابع یا ابزارها مؤثرتر باشد. همچنین دو ابزار داخلی دارد که مدل می‌تواند بر اساس درخواست کاربر تشخیص دهد که باید از آن‌ها استفاده کند. این ابزارها عبارتند از:

- **Brave Search** - می‌تواند برای دریافت اطلاعات به‌روز مانند وضعیت هوا با جستجوی وب استفاده شود  
- **Wolfram Alpha** - برای محاسبات ریاضی پیچیده‌تر کاربرد دارد و نیازی به نوشتن توابع خودتان نیست  

شما همچنین می‌توانید ابزارهای سفارشی خود را بسازید که LLM بتواند آن‌ها را فراخوانی کند.

در نمونه کد زیر:

- ابزارهای موجود (brave_search, wolfram_alpha) در پرامپت سیستم تعریف شده‌اند.  
- یک پرامپت کاربر ارسال می‌شود که درباره وضعیت هوا در یک شهر خاص سوال می‌کند.  
- LLM با فراخوانی ابزار Brave Search پاسخ می‌دهد که به این شکل خواهد بود `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*توجه: این مثال فقط فراخوانی ابزار را انجام می‌دهد، اگر می‌خواهید نتایج را دریافت کنید، باید یک حساب رایگان در صفحه API Brave ایجاد کرده و خود تابع را تعریف کنید*  

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

با وجود اینکه Llama 3.1 یک LLM است، یکی از محدودیت‌های آن چندرسانه‌ای بودن است؛ یعنی توانایی استفاده از انواع ورودی مانند تصاویر به عنوان پرامپت و ارائه پاسخ. این قابلیت یکی از ویژگی‌های اصلی Llama 3.2 است. ویژگی‌های دیگر شامل:

- چندرسانه‌ای بودن - توانایی ارزیابی همزمان پرامپت‌های متنی و تصویری  
- نسخه‌های کوچک تا متوسط (11B و 90B) - این امکان گزینه‌های استقرار انعطاف‌پذیر را فراهم می‌کند  
- نسخه‌های فقط متنی (1B و 3B) - این اجازه می‌دهد مدل روی دستگاه‌های لبه‌ای / موبایل مستقر شود و تأخیر کمی داشته باشد  

پشتیبانی چندرسانه‌ای گامی بزرگ در دنیای مدل‌های متن‌باز است. نمونه کد زیر هم تصویر و هم پرامپت متنی را می‌گیرد تا تحلیل تصویر را از Llama 3.2 90B دریافت کند.

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

## یادگیری اینجا متوقف نمی‌شود، سفر را ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود در زمینه هوش مصنوعی مولد را ارتقا دهید!

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.