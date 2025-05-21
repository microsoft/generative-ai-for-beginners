<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:41:37+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "fa"
}
-->
# راه‌اندازی محیط توسعه

ما این مخزن و دوره را با یک [container توسعه](https://containers.dev?WT.mc_id=academic-105485-koreyst) راه‌اندازی کرده‌ایم که دارای یک runtime جهانی است که می‌تواند از توسعه Python3، .NET، Node.js و Java پشتیبانی کند. پیکربندی مربوطه در فایل `devcontainer.json` که در پوشه `.devcontainer/` در ریشه این مخزن قرار دارد، تعریف شده است.

برای فعال‌سازی container توسعه، آن را در [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (برای یک runtime میزبان ابری) یا در [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (برای یک runtime میزبان دستگاه محلی) اجرا کنید. [این مستندات](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) را برای جزئیات بیشتر در مورد نحوه کار کردن containerهای توسعه در VS Code مطالعه کنید.

> [!TIP]  
> ما توصیه می‌کنیم از GitHub Codespaces برای شروع سریع با کمترین تلاش استفاده کنید. این سرویس یک [سهمیه استفاده رایگان سخاوتمندانه](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) برای حساب‌های شخصی ارائه می‌دهد. [زمان‌های توقف](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) را تنظیم کنید تا کداسپیس‌های غیرفعال را متوقف یا حذف کنید و از سهمیه خود بهینه استفاده کنید.

## ۱. اجرای تمرین‌ها

هر درس شامل تمرین‌های _اختیاری_ خواهد بود که ممکن است در یک یا چند زبان برنامه‌نویسی از جمله: Python، .NET/C#، Java و JavaScript/TypeScript ارائه شود. این بخش راهنمایی‌های کلی مربوط به اجرای این تمرین‌ها را ارائه می‌دهد.

### ۱.۱ تمرین‌های Python

تمرین‌های Python به صورت برنامه‌ها (فایل‌های `.py`) یا نوت‌بوک‌های Jupyter (فایل‌های `.ipynb`) ارائه می‌شوند.
- برای اجرای نوت‌بوک، آن را در Visual Studio Code باز کنید و سپس _Select Kernel_ (در بالا سمت راست) را کلیک کنید و گزینه پیش‌فرض Python 3 را انتخاب کنید. اکنون می‌توانید _Run All_ را برای اجرای نوت‌بوک انتخاب کنید.
- برای اجرای برنامه‌های Python از خط فرمان، دستورالعمل‌های خاص تمرین را دنبال کنید تا اطمینان حاصل کنید که فایل‌های صحیح را انتخاب کرده و آرگومان‌های لازم را ارائه می‌دهید.

## ۲. پیکربندی ارائه‌دهندگان

تمرین‌ها **ممکن است** برای کار با یک یا چند استقرار مدل زبان بزرگ (LLM) از طریق یک ارائه‌دهنده خدمات پشتیبانی‌شده مانند OpenAI، Azure یا Hugging Face تنظیم شوند. این‌ها یک _نقطه پایانی میزبانی‌شده_ (API) ارائه می‌دهند که می‌توانیم به صورت برنامه‌نویسی با اعتبارنامه‌های صحیح (کلید API یا token) به آن‌ها دسترسی پیدا کنیم. در این دوره، این ارائه‌دهندگان را مورد بحث قرار می‌دهیم:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) با مدل‌های متنوع از جمله سری اصلی GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) برای مدل‌های OpenAI با تمرکز بر آمادگی سازمانی
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) برای مدل‌های منبع‌باز و سرور استنتاج

**برای این تمرین‌ها نیاز به استفاده از حساب‌های خود دارید.** تمرین‌ها اختیاری هستند بنابراین می‌توانید یکی، همه یا هیچ‌کدام از ارائه‌دهندگان را بر اساس علاقه خود تنظیم کنید. برخی راهنمایی‌ها برای ثبت‌نام:

| ثبت‌نام | هزینه | کلید API | Playground | نظرات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروژه‌محور](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون کد، وب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | مدل‌های متعدد موجود |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [شروع سریع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [شروع سریع Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [باید از قبل برای دسترسی درخواست دهید](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://huggingface.co/pricing) | [توکن‌های دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat مدل‌های محدودی دارد](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

دستورالعمل‌های زیر را برای _پیکربندی_ این مخزن برای استفاده با ارائه‌دهندگان مختلف دنبال کنید. تمرین‌هایی که نیاز به یک ارائه‌دهنده خاص دارند، شامل یکی از این برچسب‌ها در نام فایل خود خواهند بود:
- `aoai` - نیاز به نقطه پایانی Azure OpenAI و کلید
- `oai` - نیاز به نقطه پایانی OpenAI و کلید
- `hf` - نیاز به توکن Hugging Face

شما می‌توانید یکی، هیچ‌کدام یا همه ارائه‌دهندگان را پیکربندی کنید. تمرین‌های مرتبط به سادگی در صورت نبود اعتبارنامه خطا خواهند داد.

### ۲.۱. ایجاد فایل `.env`

ما فرض می‌کنیم که شما راهنمایی‌های بالا را مطالعه کرده‌اید و با ارائه‌دهنده مربوطه ثبت‌نام کرده و اعتبارنامه‌های احراز هویت لازم (API_KEY یا token) را به دست آورده‌اید. در مورد Azure OpenAI، فرض می‌کنیم که شما همچنین یک استقرار معتبر از سرویس Azure OpenAI (نقطه پایانی) با حداقل یک مدل GPT برای تکمیل چت دارید.

گام بعدی پیکربندی **متغیرهای محیطی محلی** شما به صورت زیر است:

1. در پوشه ریشه به دنبال فایل `.env.copy` بگردید که باید محتوایی مانند زیر داشته باشد:

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

2. آن فایل را به `.env` با استفاده از دستور زیر کپی کنید. این فایل _gitignore-d_ شده است، بنابراین اطلاعات محرمانه ایمن می‌مانند.

   ```bash
   cp .env.copy .env
   ```

3. مقادیر را (جایگزین‌های سمت راست `=`) همان‌طور که در بخش بعدی توضیح داده شده است پر کنید.

3. (اختیاری) اگر از GitHub Codespaces استفاده می‌کنید، این گزینه را دارید که متغیرهای محیطی را به عنوان _secrets Codespaces_ مرتبط با این مخزن ذخیره کنید. در این صورت، نیازی به تنظیم یک فایل .env محلی نخواهید داشت. **اما توجه داشته باشید که این گزینه فقط در صورتی کار می‌کند که از GitHub Codespaces استفاده کنید.** اگر از Docker Desktop استفاده می‌کنید، همچنان باید فایل .env را تنظیم کنید.

### ۲.۲. پر کردن فایل `.env`

بیایید نگاهی سریع به نام متغیرها بیندازیم تا بفهمیم چه چیزی را نشان می‌دهند:

| متغیر  | توضیحات  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | این توکن دسترسی کاربری است که در پروفایل خود تنظیم کرده‌اید |
| OPENAI_API_KEY | این کلید مجوز برای استفاده از سرویس برای نقاط پایانی غیر Azure OpenAI است |
| AZURE_OPENAI_API_KEY | این کلید مجوز برای استفاده از آن سرویس است |
| AZURE_OPENAI_ENDPOINT | این نقطه پایانی مستقر برای یک منبع Azure OpenAI است |
| AZURE_OPENAI_DEPLOYMENT | این نقطه پایانی استقرار مدل _تولید متن_ است |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | این نقطه پایانی استقرار مدل _تعبیه متن_ است |
| | |

توجه: دو متغیر آخر Azure OpenAI یک مدل پیش‌فرض برای تکمیل چت (تولید متن) و جستجوی برداری (تعبیه) را نشان می‌دهند. دستورالعمل‌های تنظیم آن‌ها در تمرین‌های مربوطه تعریف خواهد شد.

### ۲.۳ پیکربندی Azure: از پورتال

مقادیر نقطه پایانی و کلید Azure OpenAI در [پورتال Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) یافت می‌شوند، بنابراین از آنجا شروع می‌کنیم.

1. به [پورتال Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بروید.
1. گزینه **کلیدها و نقطه پایانی** را در نوار کناری (منوی سمت چپ) کلیک کنید.
1. **نمایش کلیدها** را کلیک کنید - شما باید موارد زیر را ببینید: کلید ۱، کلید ۲ و نقطه پایانی.
1. از مقدار کلید ۱ برای AZURE_OPENAI_API_KEY استفاده کنید.
1. از مقدار نقطه پایانی برای AZURE_OPENAI_ENDPOINT استفاده کنید.

بعد، ما نیاز به نقاط پایانی برای مدل‌های خاصی که مستقر کرده‌ایم داریم.

1. گزینه **استقرار مدل‌ها** را در نوار کناری (منوی سمت چپ) برای منبع Azure OpenAI کلیک کنید.
1. در صفحه مقصد، **مدیریت استقرارها** را کلیک کنید.

این شما را به وب‌سایت Azure OpenAI Studio می‌برد، جایی که ما مقادیر دیگر را همان‌طور که در زیر توضیح داده شده است پیدا خواهیم کرد.

### ۲.۴ پیکربندی Azure: از Studio

1. به [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **از منبع خود** همان‌طور که در بالا توضیح داده شد بروید.
1. برگه **استقرارها** (نوار کناری، چپ) را برای مشاهده مدل‌های مستقر شده فعلی کلیک کنید.
1. اگر مدل مورد نظر شما مستقر نشده است، از **ایجاد استقرار جدید** برای استقرار آن استفاده کنید.
1. شما نیاز به یک مدل _تولید متن_ دارید - ما توصیه می‌کنیم: **gpt-35-turbo**
1. شما نیاز به یک مدل _تعبیه متن_ دارید - ما توصیه می‌کنیم **text-embedding-ada-002**

اکنون متغیرهای محیطی را برای منعکس کردن _نام استقرار_ استفاده شده به‌روزرسانی کنید. این معمولاً با نام مدل یکسان خواهد بود مگر اینکه آن را به‌طور خاص تغییر داده باشید. بنابراین، به عنوان مثال، ممکن است داشته باشید:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**فراموش نکنید که فایل .env را پس از اتمام ذخیره کنید.** اکنون می‌توانید فایل را ببندید و به دستورالعمل‌ها برای اجرای نوت‌بوک برگردید.

### ۲.۵ پیکربندی OpenAI: از پروفایل

کلید API OpenAI شما در حساب [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) شما قابل دسترسی است. اگر ندارید، می‌توانید برای یک حساب ثبت‌نام کنید و یک کلید API ایجاد کنید. هنگامی که کلید را دارید، می‌توانید از آن برای پر کردن متغیر `OPENAI_API_KEY` در فایل `.env` استفاده کنید.

### ۲.۶ پیکربندی Hugging Face: از پروفایل

توکن Hugging Face شما در پروفایل شما تحت [توکن‌های دسترسی](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) یافت می‌شود. این‌ها را به صورت عمومی منتشر یا به اشتراک نگذارید. در عوض، یک توکن جدید برای استفاده این پروژه ایجاد کنید و آن را در فایل `.env` تحت متغیر `HUGGING_FACE_API_KEY` کپی کنید. _توجه:_ این به‌طور فنی یک کلید API نیست اما برای احراز هویت استفاده می‌شود بنابراین ما این نام‌گذاری را برای سازگاری حفظ می‌کنیم.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.