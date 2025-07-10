<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:22:34+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fa"
}
-->
# راه‌اندازی محیط توسعه خود

ما این مخزن و دوره را با استفاده از [کانتینر توسعه](https://containers.dev?WT.mc_id=academic-105485-koreyst) راه‌اندازی کرده‌ایم که یک محیط اجرایی یونیورسال دارد و می‌تواند از توسعه Python3، .NET، Node.js و Java پشتیبانی کند. پیکربندی مرتبط در فایل `devcontainer.json` قرار دارد که در پوشه `.devcontainer/` در ریشه این مخزن واقع شده است.

برای فعال‌سازی کانتینر توسعه، آن را در [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (برای اجرای ابری) یا در [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (برای اجرای محلی روی دستگاه خودتان) اجرا کنید. برای اطلاعات بیشتر درباره نحوه کار کانتینرهای توسعه در VS Code، [این مستندات](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) را مطالعه کنید.

> [!TIP]  
> توصیه می‌کنیم برای شروع سریع و با کمترین دردسر از GitHub Codespaces استفاده کنید. این سرویس برای حساب‌های شخصی، [سهمیه استفاده رایگان](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) مناسبی ارائه می‌دهد. همچنین می‌توانید [زمان‌بندی توقف یا حذف کد‌اسپیس‌های غیرفعال](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) را تنظیم کنید تا استفاده بهینه‌تری از سهمیه خود داشته باشید.

## ۱. اجرای تمرین‌ها

هر درس شامل تمرین‌های _اختیاری_ است که ممکن است به یک یا چند زبان برنامه‌نویسی از جمله Python، .NET/C#، Java و JavaScript/TypeScript ارائه شوند. این بخش راهنمایی کلی برای اجرای این تمرین‌ها ارائه می‌دهد.

### ۱.۱ تمرین‌های Python

تمرین‌های Python یا به صورت برنامه‌های کاربردی (`.py` فایل‌ها) یا دفترچه‌های Jupyter (`.ipynb` فایل‌ها) ارائه می‌شوند.  
- برای اجرای دفترچه، آن را در Visual Studio Code باز کنید، سپس روی _Select Kernel_ (بالای سمت راست) کلیک کرده و گزینه پیش‌فرض Python 3 را انتخاب کنید. حالا می‌توانید با کلیک روی _Run All_ کل دفترچه را اجرا کنید.  
- برای اجرای برنامه‌های Python از خط فرمان، دستورالعمل‌های خاص هر تمرین را دنبال کنید تا مطمئن شوید فایل‌های درست را انتخاب کرده و آرگومان‌های لازم را وارد می‌کنید.

## ۲. پیکربندی ارائه‌دهندگان

تمرین‌ها **ممکن است** به گونه‌ای تنظیم شده باشند که با یک یا چند استقرار مدل زبان بزرگ (LLM) از طریق ارائه‌دهنده خدمات پشتیبانی شده مانند OpenAI، Azure یا Hugging Face کار کنند. این ارائه‌دهندگان یک _نقطه انتهایی میزبانی شده_ (API) فراهم می‌کنند که می‌توانیم با استفاده از اعتبارنامه‌های مناسب (کلید API یا توکن) به صورت برنامه‌نویسی به آن دسترسی داشته باشیم. در این دوره، این ارائه‌دهندگان را بررسی می‌کنیم:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) با مدل‌های متنوع از جمله سری اصلی GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) برای مدل‌های OpenAI با تمرکز بر آمادگی سازمانی
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) برای مدل‌های متن‌باز و سرور استنتاج

**برای این تمرین‌ها باید از حساب‌های خودتان استفاده کنید**. تمرین‌ها اختیاری هستند، بنابراین می‌توانید بر اساس علاقه‌تان یکی، همه یا هیچ‌کدام از ارائه‌دهندگان را راه‌اندازی کنید. راهنمایی‌هایی برای ثبت‌نام:

| ثبت‌نام | هزینه | کلید API | محیط آزمایشی | توضیحات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [بر اساس پروژه](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون کد، وب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | مدل‌های متنوع موجود |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [شروع سریع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [شروع سریع استودیو](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [باید از قبل درخواست دسترسی دهید](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://huggingface.co/pricing) | [توکن‌های دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat مدل‌های محدودی دارد](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

دستورالعمل‌های زیر را برای _پیکربندی_ این مخزن جهت استفاده با ارائه‌دهندگان مختلف دنبال کنید. تمرین‌هایی که نیاز به ارائه‌دهنده خاصی دارند، یکی از این برچسب‌ها را در نام فایل خود خواهند داشت:  
 - `aoai` - نیاز به نقطه انتهایی و کلید Azure OpenAI دارد  
 - `oai` - نیاز به نقطه انتهایی و کلید OpenAI دارد  
 - `hf` - نیاز به توکن Hugging Face دارد  

شما می‌توانید یکی، هیچ‌کدام یا همه ارائه‌دهندگان را پیکربندی کنید. تمرین‌های مرتبط در صورت نبود اعتبارنامه‌ها خطا خواهند داد.

### ۲.۱. ایجاد فایل `.env`

فرض می‌کنیم که راهنمایی‌های بالا را خوانده‌اید، با ارائه‌دهنده مربوطه ثبت‌نام کرده‌اید و اعتبارنامه‌های لازم (API_KEY یا توکن) را دریافت کرده‌اید. در مورد Azure OpenAI، فرض می‌کنیم که یک استقرار معتبر از سرویس Azure OpenAI (نقطه انتهایی) دارید که حداقل یک مدل GPT برای تکمیل چت روی آن مستقر شده است.

گام بعدی پیکربندی **متغیرهای محیطی محلی** شما به صورت زیر است:

1. در پوشه ریشه به دنبال فایل `.env.copy` بگردید که باید محتوایی شبیه به این داشته باشد:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. آن فایل را با دستور زیر به `.env` کپی کنید. این فایل در `.gitignore` قرار دارد تا اسرار محفوظ بمانند.

   ```bash
   cp .env.copy .env
   ```

3. مقادیر را پر کنید (جایگزین مقادیر سمت راست `=`) طبق توضیحات بخش بعدی.

3. (اختیاری) اگر از GitHub Codespaces استفاده می‌کنید، می‌توانید متغیرهای محیطی را به عنوان _اسرار Codespaces_ مرتبط با این مخزن ذخیره کنید. در این صورت نیازی به راه‌اندازی فایل محلی .env ندارید. **اما توجه داشته باشید که این گزینه فقط در صورت استفاده از GitHub Codespaces کار می‌کند.** اگر از Docker Desktop استفاده می‌کنید، همچنان باید فایل .env را تنظیم کنید.

### ۲.۲. پر کردن فایل `.env`

بیایید نگاهی سریع به نام متغیرها بیندازیم تا بفهمیم هر کدام چه معنایی دارند:

| متغیر | توضیح |
| :--- | :--- |
| HUGGING_FACE_API_KEY | این توکن دسترسی کاربری است که در پروفایل خود تنظیم کرده‌اید |
| OPENAI_API_KEY | کلید مجوز برای استفاده از سرویس در نقاط انتهایی غیر Azure OpenAI |
| AZURE_OPENAI_API_KEY | کلید مجوز برای استفاده از سرویس Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | نقطه انتهایی مستقر شده برای منبع Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | نقطه انتهایی استقرار مدل _تولید متن_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | نقطه انتهایی استقرار مدل _بردارهای متنی_ |
| | |

توجه: دو متغیر آخر Azure OpenAI به ترتیب مدل پیش‌فرض برای تکمیل چت (تولید متن) و جستجوی برداری (بردارها) را نشان می‌دهند. دستورالعمل‌های تنظیم آن‌ها در تمرین‌های مرتبط ارائه خواهد شد.

### ۲.۳. پیکربندی Azure: از طریق پرتال

مقادیر نقطه انتهایی و کلید Azure OpenAI را می‌توانید در [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پیدا کنید، پس از آنجا شروع می‌کنیم.

1. به [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بروید  
1. در نوار کناری (منوی سمت چپ) گزینه **Keys and Endpoint** را کلیک کنید  
1. روی **Show Keys** کلیک کنید - باید موارد زیر را ببینید: KEY 1، KEY 2 و Endpoint  
1. مقدار KEY 1 را برای AZURE_OPENAI_API_KEY استفاده کنید  
1. مقدار Endpoint را برای AZURE_OPENAI_ENDPOINT استفاده کنید  

حالا به نقاط انتهایی مدل‌های خاصی که مستقر کرده‌ایم نیاز داریم.

1. در نوار کناری (منوی سمت چپ) گزینه **Model deployments** را برای منبع Azure OpenAI انتخاب کنید  
1. در صفحه مقصد، روی **Manage Deployments** کلیک کنید  

این شما را به وب‌سایت Azure OpenAI Studio می‌برد، جایی که مقادیر دیگر را طبق توضیحات زیر پیدا می‌کنیم.

### ۲.۴. پیکربندی Azure: از طریق استودیو

1. به [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **از طریق منبع خود** که در بالا توضیح داده شد، بروید  
1. تب **Deployments** (نوار کناری، سمت چپ) را برای مشاهده مدل‌های مستقر شده باز کنید  
1. اگر مدل مورد نظر شما مستقر نشده است، از گزینه **Create new deployment** برای استقرار آن استفاده کنید  
1. شما به یک مدل _تولید متن_ نیاز دارید - توصیه ما: **gpt-35-turbo**  
1. شما به یک مدل _بردار متنی_ نیاز دارید - توصیه ما: **text-embedding-ada-002**  

حالا متغیرهای محیطی را به گونه‌ای به‌روزرسانی کنید که نام _استقرار_ استفاده شده را نشان دهند. معمولاً این نام همان نام مدل است مگر اینکه آن را صراحتاً تغییر داده باشید. به عنوان مثال، ممکن است داشته باشید:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**فراموش نکنید پس از اتمام، فایل .env را ذخیره کنید**. حالا می‌توانید از فایل خارج شده و به دستورالعمل‌های اجرای دفترچه بازگردید.

### ۲.۵. پیکربندی OpenAI: از طریق پروفایل

کلید API OpenAI خود را می‌توانید در [حساب OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) خود پیدا کنید. اگر حساب ندارید، می‌توانید ثبت‌نام کرده و یک کلید API ایجاد کنید. پس از دریافت کلید، می‌توانید آن را در متغیر `OPENAI_API_KEY` در فایل `.env` وارد کنید.

### ۲.۶. پیکربندی Hugging Face: از طریق پروفایل

توکن Hugging Face خود را می‌توانید در پروفایل خود در بخش [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) پیدا کنید. این توکن‌ها را به صورت عمومی منتشر یا به اشتراک نگذارید. به جای آن، یک توکن جدید برای استفاده در این پروژه ایجاد کرده و آن را در فایل `.env` در متغیر `HUGGING_FACE_API_KEY` وارد کنید. _توجه:_ این از نظر فنی کلید API نیست اما برای احراز هویت استفاده می‌شود، بنابراین برای حفظ یکپارچگی نام‌گذاری، از همین نام استفاده می‌کنیم.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.