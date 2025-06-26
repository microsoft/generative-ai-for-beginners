<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:07:31+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fa"
}
-->
# تنظیم محیط توسعه خود

ما این مخزن و دوره را با یک [کانتینر توسعه](https://containers.dev?WT.mc_id=academic-105485-koreyst) راه‌اندازی کرده‌ایم که دارای یک زمان اجرا جهانی است که می‌تواند از توسعه Python3، .NET، Node.js و Java پشتیبانی کند. پیکربندی مربوطه در فایل `devcontainer.json` واقع در پوشه `.devcontainer/` در ریشه این مخزن تعریف شده است.

برای فعال‌سازی کانتینر توسعه، آن را در [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (برای زمان اجرا میزبانی شده در ابر) یا در [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (برای زمان اجرا میزبانی شده در دستگاه محلی) راه‌اندازی کنید. [این مستندات](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) را بخوانید تا جزئیات بیشتری درباره نحوه کار کانتینرهای توسعه در VS Code بدانید.

> [!TIP]  
> ما توصیه می‌کنیم از GitHub Codespaces برای شروع سریع و با حداقل تلاش استفاده کنید. این سرویس یک [سهمیه استفاده رایگان سخاوتمندانه](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) برای حساب‌های شخصی ارائه می‌دهد. [تنظیمات زمان‌بندی](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) را برای توقف یا حذف کدهای غیرفعال تنظیم کنید تا استفاده از سهمیه خود را به حداکثر برسانید.

## 1. اجرای تکالیف

هر درس شامل تکالیف _اختیاری_ خواهد بود که ممکن است به یکی یا چند زبان برنامه‌نویسی از جمله: Python، .NET/C#، Java و JavaScript/TypeScript ارائه شود. این بخش راهنمایی‌های کلی مربوط به اجرای این تکالیف را ارائه می‌دهد.

### 1.1 تکالیف Python

تکالیف Python به صورت برنامه‌ها (`.py` فایل‌ها) یا دفترچه‌های Jupyter (`.ipynb` فایل‌ها) ارائه می‌شوند.
- برای اجرای دفترچه، آن را در Visual Studio Code باز کرده و سپس روی _انتخاب هسته_ (در بالا سمت راست) کلیک کنید و گزینه پیش‌فرض Python 3 نمایش داده شده را انتخاب کنید. اکنون می‌توانید _اجرای همه_ را برای اجرای دفترچه انتخاب کنید.
- برای اجرای برنامه‌های Python از خط فرمان، دستورالعمل‌های خاص تکلیف را دنبال کنید تا مطمئن شوید فایل‌های صحیح را انتخاب کرده و آرگومان‌های مورد نیاز را فراهم کرده‌اید.

## 2. پیکربندی ارائه‌دهندگان

تکالیف **ممکن است** همچنین برای کار با یک یا چند استقرار مدل زبان بزرگ (LLM) از طریق یک ارائه‌دهنده خدمات پشتیبانی شده مانند OpenAI، Azure یا Hugging Face تنظیم شوند. این ارائه‌دهندگان یک _نقطه پایانی میزبانی شده_ (API) ارائه می‌دهند که می‌توانیم با اعتبارنامه‌های مناسب (کلید API یا توکن) به صورت برنامه‌ریزی شده به آن دسترسی پیدا کنیم. در این دوره، این ارائه‌دهندگان را مورد بحث قرار می‌دهیم:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) با مدل‌های متنوع از جمله سری اصلی GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) برای مدل‌های OpenAI با تمرکز بر آمادگی سازمانی.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) برای مدل‌های متن‌باز و سرور استنتاج.

**شما باید از حساب‌های خود برای این تمرین‌ها استفاده کنید**. تکالیف اختیاری هستند بنابراین می‌توانید یکی، همه - یا هیچ‌یک - از ارائه‌دهندگان را بر اساس علاقه خود تنظیم کنید. برخی راهنمایی‌ها برای ثبت‌نام:

| ثبت‌نام | هزینه | کلید API | محیط آزمایش | توضیحات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [بر اساس پروژه](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون کد، وب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | مدل‌های متعدد موجود |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [شروع سریع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [شروع سریع استودیو](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [باید از قبل برای دسترسی درخواست دهید](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://huggingface.co/pricing) | [توکن‌های دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [چت Hugging](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [چت Hugging مدل‌های محدودی دارد](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

دستورالعمل‌های زیر را دنبال کنید تا این مخزن را برای استفاده با ارائه‌دهندگان مختلف پیکربندی کنید. تکالیفی که به یک ارائه‌دهنده خاص نیاز دارند یکی از این برچسب‌ها را در نام فایل خود خواهند داشت:
- `aoai` - نیاز به نقطه پایانی Azure OpenAI و کلید دارد
- `oai` - نیاز به نقطه پایانی OpenAI و کلید دارد
- `hf` - نیاز به توکن Hugging Face دارد

شما می‌توانید یکی، هیچ‌یک یا همه ارائه‌دهندگان را پیکربندی کنید. تکالیف مرتبط به سادگی بر روی اعتبارنامه‌های گم‌شده خطا خواهند داد.

### 2.1. ایجاد فایل `.env`

فرض می‌کنیم که شما قبلاً راهنمایی‌های بالا را خوانده‌اید و با ارائه‌دهنده مربوطه ثبت‌نام کرده‌اید و اعتبارنامه‌های احراز هویت مورد نیاز (API_KEY یا توکن) را دریافت کرده‌اید. در مورد Azure OpenAI، فرض می‌کنیم که شما همچنین یک استقرار معتبر از سرویس Azure OpenAI (نقطه پایانی) با حداقل یک مدل GPT مستقر برای تکمیل چت دارید.

مرحله بعدی پیکربندی **متغیرهای محیط محلی** شما به شرح زیر است:

1. در پوشه ریشه به دنبال فایل `.env.copy` بگردید که باید محتوایی مانند این داشته باشد:

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

2. آن فایل را با استفاده از دستور زیر به `.env` کپی کنید. این فایل _gitignore-d_ شده است، بنابراین اسرار را امن نگه می‌دارد.

   ```bash
   cp .env.copy .env
   ```

3. مقادیر را پر کنید (جایگزین placeholders در سمت راست `=`) همان‌طور که در بخش بعدی توضیح داده شده است.

3. (اختیاری) اگر از GitHub Codespaces استفاده می‌کنید، گزینه‌ای دارید که متغیرهای محیطی را به عنوان _اسرار Codespaces_ مرتبط با این مخزن ذخیره کنید. در این صورت، نیازی به تنظیم فایل .env محلی نخواهید داشت. **با این حال، توجه داشته باشید که این گزینه فقط در صورتی کار می‌کند که از GitHub Codespaces استفاده کنید.** اگر از Docker Desktop استفاده می‌کنید، همچنان باید فایل .env را تنظیم کنید.

### 2.2. پر کردن فایل `.env`

بیایید نگاهی سریع به نام‌های متغیر بیندازیم تا بفهمیم چه چیزی را نمایندگی می‌کنند:

| متغیر | توضیحات |
| :--- | :--- |
| HUGGING_FACE_API_KEY | این توکن دسترسی کاربری است که در پروفایل خود تنظیم کرده‌اید |
| OPENAI_API_KEY | این کلید احراز هویت برای استفاده از سرویس برای نقاط پایانی غیر Azure OpenAI است |
| AZURE_OPENAI_API_KEY | این کلید احراز هویت برای استفاده از آن سرویس است |
| AZURE_OPENAI_ENDPOINT | این نقطه پایانی مستقر برای یک منبع Azure OpenAI است |
| AZURE_OPENAI_DEPLOYMENT | این نقطه پایانی استقرار مدل _تولید متن_ است |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | این نقطه پایانی استقرار مدل _تعبیه‌های متن_ است |
| | |

توجه: دو متغیر آخر Azure OpenAI نشان‌دهنده یک مدل پیش‌فرض برای تکمیل چت (تولید متن) و جستجوی برداری (تعبیه‌ها) هستند. دستورالعمل‌ها برای تنظیم آن‌ها در تکالیف مربوطه تعریف خواهد شد.

### 2.3 پیکربندی Azure: از پورتال

مقادیر نقطه پایانی و کلید Azure OpenAI در [پورتال Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) یافت می‌شود، بنابراین از آنجا شروع کنیم.

1. به [پورتال Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بروید.
1. گزینه **کلیدها و نقطه پایانی** را در نوار کناری (منو در سمت چپ) کلیک کنید.
1. روی **نمایش کلیدها** کلیک کنید - باید موارد زیر را ببینید: کلید 1، کلید 2 و نقطه پایانی.
1. از مقدار کلید 1 برای AZURE_OPENAI_API_KEY استفاده کنید.
1. از مقدار نقطه پایانی برای AZURE_OPENAI_ENDPOINT استفاده کنید.

بعد، باید نقاط پایانی برای مدل‌های خاصی که مستقر کرده‌ایم را پیدا کنیم.

1. گزینه **استقرار مدل‌ها** را در نوار کناری (منو سمت چپ) برای منبع Azure OpenAI کلیک کنید.
1. در صفحه مقصد، روی **مدیریت استقرارها** کلیک کنید.

این شما را به وب‌سایت Azure OpenAI Studio می‌برد، جایی که ما بقیه مقادیر را همان‌طور که در زیر توضیح داده شده است پیدا خواهیم کرد.

### 2.4 پیکربندی Azure: از استودیو

1. از [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **از منبع خود** همان‌طور که در بالا توضیح داده شد، پیمایش کنید.
1. برای مشاهده مدل‌های مستقر شده فعلی، روی برگه **استقرارها** (نوار کناری، سمت چپ) کلیک کنید.
1. اگر مدل مورد نظر شما مستقر نشده است، از **ایجاد استقرار جدید** برای استقرار آن استفاده کنید.
1. شما به یک مدل _تولید متن_ نیاز خواهید داشت - ما توصیه می‌کنیم: **gpt-35-turbo**
1. شما به یک مدل _تعبیه متن_ نیاز خواهید داشت - ما توصیه می‌کنیم **text-embedding-ada-002**

اکنون متغیرهای محیطی را به نام استقرار _استفاده شده_ به‌روز کنید. این معمولاً همان نام مدل خواهد بود مگر اینکه آن را به‌طور صریح تغییر داده باشید. بنابراین، به عنوان مثال، ممکن است داشته باشید:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**فراموش نکنید که فایل .env را پس از پایان ذخیره کنید**. اکنون می‌توانید فایل را ببندید و به دستورالعمل‌های اجرای دفترچه بازگردید.

### 2.5 پیکربندی OpenAI: از پروفایل

کلید API OpenAI شما در حساب [OpenAI شما](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) قابل یافتن است. اگر کلید ندارید، می‌توانید برای یک حساب ثبت‌نام کرده و یک کلید API ایجاد کنید. هنگامی که کلید را دارید، می‌توانید از آن برای پر کردن متغیر `OPENAI_API_KEY` در فایل `.env` استفاده کنید.

### 2.6 پیکربندی Hugging Face: از پروفایل

توکن Hugging Face شما در پروفایل شما تحت [توکن‌های دسترسی](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) قابل یافتن است. این‌ها را به صورت عمومی منتشر یا به اشتراک نگذارید. در عوض، یک توکن جدید برای استفاده در این پروژه ایجاد کنید و آن را در فایل `.env` تحت متغیر `HUGGING_FACE_API_KEY` کپی کنید. _توجه:_ این به‌طور فنی یک کلید API نیست اما برای احراز هویت استفاده می‌شود بنابراین ما برای سازگاری از نام‌گذاری آن استفاده می‌کنیم.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال هرگونه سوءتفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه نداریم.