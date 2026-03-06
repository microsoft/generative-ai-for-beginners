# ساخت با مدل‌های خانواده متا

## معرفی

این درس موارد زیر را پوشش می‌دهد:

- بررسی دو مدل اصلی خانواده متا - Llama 3.1 و Llama 3.2
- درک موارد استفاده و سناریوهای هر مدل
- نمونه کد برای نمایش ویژگی‌های منحصربه‌فرد هر مدل

## خانواده مدل‌های متا

در این درس، دو مدل از خانواده متا یا "Llama Herd" را بررسی خواهیم کرد - Llama 3.1 و Llama 3.2.

این مدل‌ها در انواع مختلف عرضه شده‌اند و در بازار مدل‌های GitHub در دسترس هستند. در اینجا جزئیات بیشتری در مورد استفاده از مدل‌های GitHub برای [نمونه‌سازی با مدل‌های هوش مصنوعی](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) آورده شده است.

انواع مدل:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*توجه: Llama 3 نیز در مدل‌های GitHub موجود است اما در این درس پوشش داده نمی‌شود*

## Llama 3.1

با ۴۰۵ میلیارد پارامتر، Llama 3.1 در دسته مدل‌های زبانی بزرگ متن‌باز قرار می‌گیرد.

این مدل ارتقاءیافته نسخه قبلی Llama 3 است و امکانات زیر را ارائه می‌دهد:

- پنجره زمینه بزرگتر - ۱۲۸ هزار توکن در مقابل ۸ هزار توکن
- حداکثر توکن خروجی بیشتر - ۴۰۹۶ در مقابل ۲۰۴۸
- پشتیبانی بهتر چندزبانه - به دلیل افزایش توکن‌های آموزش

این موارد به Llama 3.1 امکان می‌دهد تا موارد استفاده پیچیده‌تری را هنگام ساخت برنامه‌های AI تولیدی مدیریت کند، از جمله:
- فراخوانی توابع بومی - توانایی فراخوانی ابزارها و توابع خارجی خارج از جریان کار مدل زبانی
- عملکرد بهتر RAG - به دلیل پنجره زمینه بزرگتر
- تولید داده‌های مصنوعی - توانایی ایجاد داده‌های مؤثر برای وظایفی مانند تنظیم دقیق

### فراخوانی توابع بومی

Llama 3.1 به طوری که در فراخوانی توابع یا ابزارها مؤثرتر باشد، بهینه شده است. همچنین دو ابزار داخلی دارد که مدل می‌تواند تشخیص دهد بر اساس پرسش کاربر باید از آنها استفاده کند. این ابزارها عبارت‌اند از:

- **Brave Search** - برای به‌دست آوردن اطلاعات به‌روز مانند وضعیت هوا با انجام جستجوی وب استفاده می‌شود
- **Wolfram Alpha** - برای انجام محاسبات ریاضی پیچیده‌تر که نوشتن توابع خودتان را لازم نمی‌کند

شما همچنین می‌توانید ابزارهای سفارشی خود را بسازید که مدل زبانی بتواند آنها را فراخوانی کند.

در نمونه کد زیر:

- ابزارهای موجود (brave_search، wolfram_alpha) در پروامپت سیستم تعریف شده‌اند.
- یک پروامپت کاربر ارسال شده که درباره آب و هوا در یک شهر خاص سؤال می‌کند.
- مدل زبانی پاسخ را با فراخوانی ابزار Brave Search ارائه می‌دهد که به این صورت خواهد بود `<|python_tag|>brave_search.call(query="Stockholm weather")`

*توجه: این مثال تنها فراخوانی ابزار را انجام می‌دهد، اگر می‌خواهید نتایج را دریافت کنید، باید یک حساب رایگان در صفحه Brave API بسازید و خود تابع را تعریف کنید.

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

با اینکه یک مدل زبانی بزرگ است، یکی از محدودیت‌های Llama 3.1 عدم چندرسانه‌ای بودن آن است. یعنی توانایی استفاده از انواع ورودی‌های متفاوت مانند تصاویر به عنوان پروامپت و ارائه پاسخ. این توانایی یکی از ویژگی‌های اصلی Llama 3.2 است. این ویژگی‌ها همچنین شامل:

- چندرسانه‌ای بودن - توانایی ارزیابی هر دو پروامپت متن و تصویر
- تغییرات اندازه کوچک تا متوسط (11B و 90B) - که گزینه‌های پیاده‌سازی انعطاف‌پذیر را فراهم می‌کند،
- تنوع‌های تنها متنی (۱B و ۳B) - که به مدل امکان پیاده‌سازی روی دستگاه‌های لبه‌ای / موبایل را می‌دهد و تأخیر کمی دارد

پشتیبانی چندرسانه‌ای گامی بزرگ در دنیای مدل‌های متن‌باز است. نمونه کد زیر هر دو پروامپت تصویر و متن را می‌گیرد تا تحلیلی از تصویر توسط Llama 3.2 90B ارائه دهد.

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

## یادگیری اینجا متوقف نمی‌شود، سفر خود را ادامه دهید

پس از تکمیل این درس، مجموعه [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود در هوش مصنوعی تولیدی را افزایش دهید!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیح مهم**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. با اینکه ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->