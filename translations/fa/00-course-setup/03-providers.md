<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T14:09:37+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "fa"
}
-->
# انتخاب و پیکربندی یک ارائه‌دهنده LLM 🔑

تمرین‌ها **ممکن است** طوری تنظیم شوند که با یک یا چند استقرار مدل زبانی بزرگ (LLM) از طریق یک ارائه‌دهنده سرویس پشتیبانی‌شده مثل OpenAI، Azure یا Hugging Face کار کنند. این سرویس‌ها یک _نقطه پایانی میزبانی‌شده_ (API) ارائه می‌دهند که می‌توانیم با داشتن اعتبارنامه مناسب (کلید API یا توکن) به صورت برنامه‌نویسی به آن دسترسی پیدا کنیم. در این دوره، این ارائه‌دهندگان را بررسی می‌کنیم:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) با مدل‌های متنوع از جمله سری اصلی GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) برای مدل‌های OpenAI با تمرکز بر آمادگی سازمانی
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) برای مدل‌های متن‌باز و سرور استنتاج

**برای این تمرین‌ها باید از حساب‌های شخصی خودتان استفاده کنید.** انجام تمرین‌ها اختیاری است، بنابراین می‌توانید بسته به علاقه‌تان یکی، همه یا هیچ‌کدام از ارائه‌دهندگان را راه‌اندازی کنید. راهنمایی‌هایی برای ثبت‌نام:

| ثبت‌نام | هزینه | کلید API | محیط آزمایشی | توضیحات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [بر اساس پروژه](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون کدنویسی، وب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | مدل‌های متعددی در دسترس است |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [شروع سریع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [شروع سریع Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [باید از قبل درخواست دسترسی بدهید](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://huggingface.co/pricing) | [توکن‌های دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat مدل‌های محدودی دارد](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

دستورالعمل‌های زیر را دنبال کنید تا این مخزن را برای استفاده با ارائه‌دهندگان مختلف _پیکربندی_ کنید. تمرین‌هایی که به یک ارائه‌دهنده خاص نیاز دارند، یکی از این برچسب‌ها را در نام فایل خود خواهند داشت:

- `aoai` - نیازمند نقطه پایانی و کلید Azure OpenAI
- `oai` - نیازمند نقطه پایانی و کلید OpenAI
- `hf` - نیازمند توکن Hugging Face

می‌توانید یکی، هیچ‌کدام یا همه ارائه‌دهندگان را پیکربندی کنید. تمرین‌های مرتبط در صورت نبود اعتبارنامه، با خطا مواجه خواهند شد.

## ساخت فایل `.env`

فرض می‌کنیم که راهنمای بالا را خوانده‌اید و در ارائه‌دهنده مربوطه ثبت‌نام کرده و اعتبارنامه‌های لازم (API_KEY یا توکن) را دریافت کرده‌اید. در مورد Azure OpenAI، فرض می‌کنیم که یک استقرار معتبر از سرویس Azure OpenAI (نقطه پایانی) با حداقل یک مدل GPT برای تکمیل چت دارید.

گام بعدی این است که **متغیرهای محیطی محلی** خود را به شکل زیر پیکربندی کنید:

1. در پوشه اصلی به دنبال فایلی به نام `.env.copy` بگردید که باید محتوایی شبیه زیر داشته باشد:

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

2. این فایل را با دستور زیر به `.env` کپی کنید. این فایل در _gitignore_ قرار دارد تا اطلاعات محرمانه محفوظ بماند.

   ```bash
   cp .env.copy .env
   ```

3. مقادیر را طبق توضیحات بخش بعدی (مقادیر سمت راست `=`) جایگزین کنید.

4. (اختیاری) اگر از GitHub Codespaces استفاده می‌کنید، می‌توانید متغیرهای محیطی را به عنوان _secrets_ مربوط به این مخزن ذخیره کنید. در این صورت، دیگر نیازی به ساخت فایل .env محلی ندارید. **اما توجه داشته باشید که این گزینه فقط در صورت استفاده از GitHub Codespaces کار می‌کند.** اگر از Docker Desktop استفاده می‌کنید، همچنان باید فایل .env را بسازید.

## مقداردهی فایل `.env`

بیایید نگاهی سریع به نام متغیرها بیندازیم تا بفهمیم هرکدام چه کاربردی دارند:

| متغیر  | توضیح  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | این توکن دسترسی کاربری است که در پروفایل خود تنظیم کرده‌اید |
| OPENAI_API_KEY | این کلید مجوز برای استفاده از سرویس در نقاط پایانی غیر Azure OpenAI است |
| AZURE_OPENAI_API_KEY | این کلید مجوز برای استفاده از آن سرویس است |
| AZURE_OPENAI_ENDPOINT | این نقطه پایانی استقرار برای منبع Azure OpenAI است |
| AZURE_OPENAI_DEPLOYMENT | این نقطه پایانی استقرار مدل _تولید متن_ است |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | این نقطه پایانی استقرار مدل _تعبیه متن_ است |
| | |

توجه: دو متغیر آخر Azure OpenAI به ترتیب مدل پیش‌فرض برای تکمیل چت (تولید متن) و جستجوی برداری (تعبیه‌ها) را نشان می‌دهند. دستورالعمل مقداردهی آن‌ها در تمرین‌های مربوطه ارائه خواهد شد.

## پیکربندی Azure: از طریق پورتال

مقادیر نقطه پایانی و کلید Azure OpenAI را می‌توانید در [پورتال Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پیدا کنید. مراحل زیر را دنبال کنید:

1. به [پورتال Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بروید
1. گزینه **Keys and Endpoint** را در نوار کناری (منوی سمت چپ) انتخاب کنید.
1. روی **Show Keys** کلیک کنید - باید موارد زیر را ببینید: KEY 1، KEY 2 و Endpoint.
1. مقدار KEY 1 را برای AZURE_OPENAI_API_KEY استفاده کنید
1. مقدار Endpoint را برای AZURE_OPENAI_ENDPOINT استفاده کنید

در مرحله بعد، باید نقاط پایانی مدل‌هایی که مستقر کرده‌ایم را پیدا کنیم.

1. گزینه **Model deployments** را در نوار کناری (منوی سمت چپ) برای منبع Azure OpenAI انتخاب کنید.
1. در صفحه مقصد، روی **Manage Deployments** کلیک کنید

این کار شما را به وب‌سایت Azure OpenAI Studio می‌برد، جایی که مقادیر دیگر را طبق توضیحات زیر پیدا خواهید کرد.

## پیکربندی Azure: از طریق Studio

1. به [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **از منبع خود** طبق توضیحات بالا بروید.
1. روی تب **Deployments** (نوار کناری، سمت چپ) کلیک کنید تا مدل‌های مستقرشده فعلی را ببینید.
1. اگر مدل مورد نظر شما مستقر نشده، از **Create new deployment** برای استقرار آن استفاده کنید.
1. به یک مدل _تولید متن_ نیاز دارید - ما **gpt-35-turbo** را پیشنهاد می‌کنیم
1. به یک مدل _تعبیه متن_ نیاز دارید - ما **text-embedding-ada-002** را پیشنهاد می‌کنیم

حالا متغیرهای محیطی را با توجه به _نام استقرار_ به‌روزرسانی کنید. معمولاً این نام با نام مدل یکسان است مگر اینکه خودتان آن را تغییر داده باشید. به عنوان مثال، ممکن است داشته باشید:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**فراموش نکنید که پس از اتمام، فایل .env را ذخیره کنید.** حالا می‌توانید از فایل خارج شوید و به دستورالعمل اجرای نوت‌بوک برگردید.

## پیکربندی OpenAI: از طریق پروفایل

کلید API خود را می‌توانید در [حساب OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) پیدا کنید. اگر کلید ندارید، می‌توانید ثبت‌نام کنید و یک کلید API بسازید. پس از دریافت کلید، آن را در متغیر `OPENAI_API_KEY` در فایل `.env` قرار دهید.

## پیکربندی Hugging Face: از طریق پروفایل

توکن Hugging Face شما در پروفایل‌تان زیر بخش [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) قابل مشاهده است. این توکن‌ها را به صورت عمومی منتشر یا به اشتراک نگذارید. برای این پروژه یک توکن جدید بسازید و آن را در فایل `.env` زیر متغیر `HUGGING_FACE_API_KEY` قرار دهید. _توجه:_ این در واقع یک کلید API نیست اما برای احراز هویت استفاده می‌شود، بنابراین برای یکدست بودن نام‌گذاری، همین نام را حفظ کرده‌ایم.

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادرستی باشند. نسخه اصلی سند به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.