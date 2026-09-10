# انتخاب و پیکربندی ارائه‌دهنده LLM 🔑

تمرینات **ممکن است** برای کار با یک یا چند استقرار مدل زبان بزرگ (LLM) از طریق یک ارائه‌دهنده خدمات پشتیبانی شده مانند OpenAI، Azure یا Hugging Face تنظیم شوند. اینها یک _نقطه پایانی میزبانی شده_ (API) فراهم می‌کنند که ما می‌توانیم به صورت برنامه‌نویسی با اعتبارنامه‌های مناسب (کلید API یا توکن) به آن دسترسی پیدا کنیم. در این دوره، این ارائه‌دهندگان را بررسی می‌کنیم:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) با مدل‌های متنوع، از جمله سری اصلی GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) برای مدل‌های OpenAI با تمرکز بر آمادگی سازمانی
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) برای یک نقطه پایانی و کلید API واحد برای دسترسی به صدها مدل از OpenAI، Meta، Mistral، Cohere، Microsoft و موارد دیگر (جایگزین GitHub Models می‌شود که در پایان ژوئیه ۲۰۲۶ بازنشسته می‌شود)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) برای مدل‌های متن‌باز و سرور استنتاج
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) یا [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) اگر ترجیح می‌دهید مدل‌ها را کاملاً آفلاین روی دستگاه خود اجرا کنید، بدون نیاز به اشتراک ابری

**شما باید از حساب‌های خود برای این تمرینات استفاده کنید**. تمرینات اختیاری هستند، بنابراین می‌توانید بر اساس علاقه خود یکی، همه یا هیچ‌کدام از ارائه‌دهندگان را راه‌اندازی کنید. راهنمایی‌هایی برای ثبت‌نام:

| ثبت‌نام | هزینه | کلید API | محیط آزمایشی | توضیحات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [بر اساس پروژه](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون کدنویسی، وب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | مدل‌های متعدد موجود |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [شروع سریع SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [شروع سریع استودیو](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [باید از قبل درخواست دسترسی کرد](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [صفحه نمای کلی پروژه](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [محیط آزمایشی Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | لایه رایگان موجود؛ یک نقطه پایانی + کلید برای ارائه‌دهندگان مدل متعدد |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://huggingface.co/pricing) | [توکن‌های دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [گفتگوی Hugging](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [گفتگوی Hugging مدل‌های محدودی دارد](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | رایگان (روی دستگاه شما اجرا می‌شود) | نیاز نیست | [CLI/SDK محلی](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | کاملاً آفلاین، نقطه پایانی سازگار با OpenAI |
| | | | | |

دستورالعمل‌های زیر را برای _پیکربندی_ این مخزن برای استفاده با ارائه‌دهندگان مختلف دنبال کنید. تمریناتی که نیاز به ارائه‌دهنده خاصی دارند، یکی از این برچسب‌ها را در نام فایل خود خواهند داشت:

- `aoai` - نیاز به نقطه پایانی و کلید Azure OpenAI دارد
- `oai` - نیاز به نقطه پایانی و کلید OpenAI دارد
- `hf` - نیاز به توکن Hugging Face دارد
- `githubmodels` - نیاز به نقطه پایانی و کلید Microsoft Foundry Models دارد (GitHub Models در پایان ژوئیه ۲۰۲۶ بازنشسته می‌شود)

شما می‌توانید یکی، هیچ‌کدام یا همه ارائه‌دهندگان را پیکربندی کنید. تمرینات مرتبط به‌سادگی در صورت نبود اعتبارنامه‌ها به خطا برمی‌خورند.

## ایجاد فایل `.env`

فرض می‌کنیم که شما قبلاً راهنمایی‌های بالا را خوانده‌اید و در ارائه‌دهنده مربوطه ثبت‌نام کرده و اعتبارنامه‌های احراز هویت مورد نیاز (کلید API یا توکن) را دریافت کرده‌اید. در مورد Azure OpenAI، فرض می‌کنیم که همچنین یک استقرار معتبر از سرویس Azure OpenAI (نقطه پایانی) دارید که حداقل یک مدل GPT برای تکمیل چت مستقر شده است.

گام بعدی این است که **متغیرهای محیطی محلی** خود را به شکل زیر پیکربندی کنید:

1. در پوشه اصلی به دنبال فایلی با نام `.env.copy` بگردید که باید محتویات مشابه زیر داشته باشد:

   ```bash
   # ارائه‌دهنده OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## آزور OpenAI در Microsoft Foundry
   ## (خدمات آزور OpenAI اکنون بخشی از Microsoft Foundry است: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # پیش‌فرض تنظیم شده است! (نسخه پایدار فعلی GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## مدل‌های Microsoft Foundry (کاتالوگ مدل چند ارائه‌دهنده، جایگزین مدل‌های GitHub که تا پایان ژوئیه ۲۰۲۶ بازنشسته می‌شوند)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. آن فایل را با دستور زیر به `.env` کپی کنید. این فایل در _gitignore_ قرار دارد و اسرار را ایمن نگه می‌دارد.

   ```bash
   cp .env.copy .env
   ```

3. مقادیر را پر کنید (جایگزین‌های سمت راست علامت `=`) طبق توضیحات در بخش بعدی.

4. (اختیاری) اگر از GitHub Codespaces استفاده می‌کنید، می‌توانید متغیرهای محیطی را به عنوان _اسرار Codespaces_ مرتبط با این مخزن ذخیره کنید. در این صورت نیازی به راه‌اندازی فایل محلی .env نخواهید داشت. **اما توجه داشته باشید که این گزینه فقط در صورت استفاده از GitHub Codespaces کار می‌کند.** اگر به جای آن از Docker Desktop استفاده می‌کنید، همچنان باید فایل .env را تنظیم کنید.

## پر کردن فایل `.env`

بیایید نگاهی سریع به نام متغیرها بیندازیم تا بفهمیم هر کدام نماینده چه چیزی هستند:

| متغیر  | توضیح  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | این توکن دسترسی کاربری است که در پروفایل خود تنظیم کرده‌اید |
| OPENAI_API_KEY | این کلید مجوز استفاده از سرویس برای نقاط پایانی غیر Azure OpenAI است |
| AZURE_OPENAI_API_KEY | این کلید مجوز استفاده از سرویس Azure OpenAI است |
| AZURE_OPENAI_ENDPOINT | این نقطه پایانی مستقر شده برای منبع Azure OpenAI است |
| AZURE_OPENAI_DEPLOYMENT | این نقطه پایانی استقرار مدل _تولید متن_ است |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | این نقطه پایانی استقرار مدل _بردارهای متنی_ است |
| AZURE_INFERENCE_ENDPOINT | این نقطه پایانی پروژه Microsoft Foundry شما است، برای استفاده از Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | این کلید API پروژه Microsoft Foundry شما است |
| | |

توجه: دو متغیر آخر Azure OpenAI به ترتیب نمایانگر مدل پیش‌فرض برای تکمیل چت (تولید متن) و جستجوی برداری (بردارها) هستند. دستورالعمل تنظیم آن‌ها در تمرینات مربوطه تعریف خواهد شد.

## پیکربندی Azure OpenAI: از طریق پرتال

> **توجه:** سرویس Azure OpenAI اکنون بخشی از [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) است. منابع و استقرارها هنوز در پرتال Azure ظاهر می‌شوند، اما مدیریت روزمره مدل‌ها (استقرارها، محیط آزمایشی، نظارت) اکنون در پرتال Foundry انجام می‌شود به جای "استودیو Azure OpenAI" قدیمی.

مقادیر نقطه پایانی و کلید Azure OpenAI را در [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) خواهید یافت، پس از آنجا شروع کنیم.

1. به [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بروید
1. در نوار کناری (منوی سمت چپ) گزینه **Keys and Endpoint** را کلیک کنید.
1. روی **Show Keys** کلیک کنید - باید موارد زیر را مشاهده کنید: KEY 1، KEY 2 و Endpoint.
1. مقدار KEY 1 را برای AZURE_OPENAI_API_KEY استفاده کنید
1. مقدار Endpoint را برای AZURE_OPENAI_ENDPOINT استفاده کنید

در مرحله بعد، به نقطه‌های پایانی مدل‌های خاصی که مستقر کرده‌ایم نیاز داریم.

1. گزینه **Model deployments** را در نوار کناری (منوی سمت چپ) برای منبع Azure OpenAI کلیک کنید.
1. در صفحه مقصد، روی **Go to Microsoft Foundry portal** (یا **Manage Deployments**، بسته به نوع منبع شما) کلیک کنید

این شما را به پرتال Microsoft Foundry منتقل می‌کند، جایی که سایر مقادیر را طبق توضیحات زیر پیدا خواهیم کرد.

## پیکربندی Azure OpenAI: از طریق پرتال Microsoft Foundry

1. به [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **از منبع خود** مطابق توضیح بالا بروید.
1. تب **Deployments** را کلیک کنید (نوار کناری، سمت چپ) تا مدل‌های مستقر شده را مشاهده کنید.
1. اگر مدل مورد نظر شما مستقر نشده است، با استفاده از **Deploy model** آن را از [کتابخانه مدل‌ها](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) مستقر کنید.
1. شما به یک مدل _تولید متن_ نیاز خواهید داشت – پیشنهاد ما: **gpt-5-mini**
1. شما به یک مدل _بردار متنی_ نیاز خواهید داشت – پیشنهاد ما: **text-embedding-3-small**

اکنون متغیرهای محیطی را برای بازتاب _نام استقرار_ به‌روزرسانی کنید. این معمولاً همان نام مدل است مگر اینکه صریحاً آن را تغییر داده باشید. بنابراین، به عنوان مثال، ممکن است داشته باشید:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**فراموش نکنید که پس از پایان فایل .env را ذخیره کنید**. اکنون می‌توانید از فایل خارج شوید و به دستورالعمل‌های اجرای دفترچه بازگردید.

## پیکربندی OpenAI: از پروفایل

کلید API OpenAI شما را می‌توان در [حساب OpenAI شما](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) یافت. اگر حساب ندارید، می‌توانید ثبت‌نام کنید و یک کلید API بسازید. پس از دریافت کلید، می‌توانید آن را در متغیر `OPENAI_API_KEY` در فایل `.env` قرار دهید.

## پیکربندی Hugging Face: از پروفایل

توکن Hugging Face شما در پروفایل تحت بخش [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) یافت می‌شود. این توکن‌ها را به صورت عمومی منتشر نکنید یا به اشتراک نگذارید. در عوض، برای این پروژه یک توکن جدید بسازید و آن را در فایل `.env` زیر متغیر `HUGGING_FACE_API_KEY` کپی کنید. _توجه:_ این در واقع کلید API نیست اما برای احراز هویت استفاده می‌شود به همین دلیل نام‌گذاری را به این شکل حفظ کرده‌ایم.

## پیکربندی Microsoft Foundry Models: از طریق پرتال

> **توجه:** GitHub Models در پایان ژوئیه ۲۰۲۶ بازنشسته می‌شود. Microsoft Foundry Models جایگزین مستقیم آن است و همان تجربه کتابخانه مدل رایگان و SDK استنتاج Azure AI / OpenAI SDK را ارائه می‌دهد.

1. به [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) بروید و یک پروژه Foundry ایجاد یا باز کنید.
1. کتابخانه مدل را مرور کنید و یک مدل مستقر کنید، برای مثال `gpt-5-mini`.
1. در صفحه نمای کلی پروژه، **نقطه پایانی** و **کلید API** را کپی کنید.
1. مقدار نقطه پایانی را برای `AZURE_INFERENCE_ENDPOINT` و مقدار کلید را برای `AZURE_INFERENCE_CREDENTIAL` در فایل `.env` خود استفاده کنید.

## ارائه‌دهندگان آفلاین / محلی

اگر ترجیح می‌دهید اصلاً از اشتراک ابری استفاده نکنید، می‌توانید مدل‌های سازگار و باز را مستقیماً روی دستگاه خود اجرا کنید:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – اجرای دستگاه مایکروسافت. به طور خودکار بهترین ارائه‌دهنده اجرا (NPU، GPU یا CPU) را انتخاب می‌کند و یک نقطه پایانی سازگار با OpenAI ارائه می‌دهد، بنابراین می‌توانید اکثر کد نمونه در این دوره را با کمترین تغییرات مجدداً استفاده کنید. برای شروع، مستندات [Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) را ببینید یا با دستور `winget install Microsoft.FoundryLocal` (ویندوز) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) نصب کنید.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – جایگزین محبوب برای اجرای مدل‌های باز مانند Llama، Phi، Mistral و Gemma به صورت محلی.


برای مثال‌های عملی از هر دو گزینه، به [درس ۱۹: ساخت با SLM ها](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->