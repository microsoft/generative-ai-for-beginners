# ساخت با مدل‌های خانواده Meta

## مقدمه

این درس موارد زیر را پوشش می‌دهد:

- بررسی دو مدل اصلی خانواده Meta - Llama 3.1 و Llama 3.2
- درک کاربردها و سناریوهای هر مدل
- نمونه کد برای نشان دادن ویژگی‌های منحصربه‌فرد هر مدل


## خانواده مدل‌های Meta

در این درس، ما ۲ مدل از خانواده Meta یا "گله Llama" را بررسی خواهیم کرد - Llama 3.1 و Llama 3.2.

این مدل‌ها در نسخه‌های مختلف عرضه شده و در [کاتالوگ مدل‌های Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) در دسترس هستند.

> **توجه:** مدل‌های GitHub تا پایان ژوئیه ۲۰۲۶ بازنشسته خواهند شد. در اینجا جزئیات بیشتری در مورد استفاده از [مدل‌های Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) برای نمونه‌سازی با مدل‌های هوش مصنوعی آمده است.

نسخه‌های مدل‌ها:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*توجه: Llama 3 نیز در مدل‌های Microsoft Foundry موجود است اما در این درس پوشش داده نمی‌شود*

## Llama 3.1

با ۴۰۵ میلیارد پارامتر، Llama 3.1 در دسته مدل‌های منبع‌باز زبان قرار می‌گیرد.

این مدل به‌روزرسانی مدل قبلی Llama 3 است و امکانات زیر را ارائه می‌دهد:

- پنجره متنی بزرگ‌تر - ۱۲۸ هزار توکن در مقابل ۸ هزار توکن
- حداکثر توکن‌های خروجی بزرگ‌تر - ۴۰۹۶ در مقابل ۲۰۴۸
- پشتیبانی چندزبانه بهتر - به دلیل افزایش تعداد توکن‌های آموزش

این‌ها به Llama 3.1 اجازه می‌دهند در ساخت برنامه‌های GenAI کاربردهای پیچیده‌تری را مدیریت کند، شامل:
- فراخوانی تابع بومی - توانایی فراخوانی ابزارها و توابع خارجی خارج از روند LLM
- عملکرد بهتر در RAG - به علت پنجره متنی بزرگ‌تر
- تولید داده‌های مصنوعی - توانایی ایجاد داده‌های مؤثر برای کارهایی مانند تنظیم دقیق مدل

### فراخوانی تابع بومی

Llama 3.1 برای فراخوانی توابع یا ابزارها تنظیم دقیق شده تا مؤثرتر باشد. همچنین دو ابزار داخلی دارد که مدل بر اساس درخواست کاربر تشخیص می‌دهد باید استفاده شوند. این ابزارها عبارتند از:

- **Brave Search** - می‌توان از آن برای دریافت اطلاعات به‌روز مانند وضعیت هوا با انجام جستجوی وب استفاده کرد
- **Wolfram Alpha** - می‌توان برای محاسبات ریاضی پیچیده‌تر از آن استفاده کرد بنابراین نیاز به نوشتن توابع خودتان نیست

همچنین شما می‌توانید ابزارهای سفارشی خود را ایجاد کنید که LLM بتواند آنها را فراخوانی کند.

در نمونه کد زیر:

- ابزارهای در دسترس (brave_search, wolfram_alpha) را در درخواست سیستم تعریف می‌کنیم.
- درخواست کاربر را می‌فرستیم که درباره وضعیت هوا در یک شهر خاص سوال می‌کند.
- LLM با فراخوانی ابزار Brave Search پاسخ خواهد داد که شبیه این است `<|python_tag|>brave_search.call(query="Stockholm weather")`

*توجه: این مثال فقط فراخوانی ابزار را نشان می‌دهد، اگر می‌خواهید نتایج را دریافت کنید باید حساب رایگان در صفحه API Brave ایجاد کرده و خود تابع را تعریف کنید.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# این موارد را از صفحه «بررسی کلی» پروژه Microsoft Foundry خود دریافت کنید
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

علیرغم اینکه یک مدل LLM است، یکی از محدودیت‌های Llama 3.1 عدم چندرسانه‌ای بودن آن است. به عبارت دیگر، ناتوانی در استفاده از انواع ورودی مانند تصاویر به‌عنوان درخواست و ارائه پاسخ است. این قابلیت یکی از ویژگی‌های اصلی Llama 3.2 است. این ویژگی‌ها همچنین شامل موارد زیر است:

- چندرسانه‌ای بودن - توانایی ارزیابی همزمان درخواست‌های متنی و تصویری
- نسخه‌های اندازه کوچک تا متوسط (11B و 90B) - این ارائه گزینه‌های استقرار منعطف را فراهم می‌کند،
- نسخه‌های فقط متنی (1B و 3B) - این امکان مدل را برای استقرار روی دستگاه‌های لبه‌ای / موبایل با تأخیر کم فراهم می‌کند

پشتیبانی چندرسانه‌ای گامی بزرگ در دنیای مدل‌های منبع‌باز محسوب می‌شود. نمونه کد زیر هم یک تصویر و هم متن را به عنوان درخواست می‌گیرد تا تحلیلی از تصویر را توسط Llama 3.2 90B ارائه دهد.


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

# این موارد را از صفحه «نمای کلی» پروژه Microsoft Foundry خود بگیرید
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

## یادگیری اینجا پایان نمی‌یابد، مسیر را ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود را در حوزه هوش مصنوعی مولد ارتقا دهید!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->