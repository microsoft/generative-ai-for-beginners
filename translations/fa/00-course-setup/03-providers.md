# انتخاب و پیکربندی ارائه‌دهنده LLM 🔑

تمرین‌ها **ممکن است** به گونه‌ای تنظیم شوند که با یک یا چند استقرار مدل زبان بزرگ (LLM) از طریق یک ارائه‌دهنده سرویس پشتیبانی شده مانند OpenAI، Azure یا Hugging Face کار کنند. این‌ها یک _نقطه پایانی میزبانی شده_ (API) فراهم می‌کنند که ما می‌توانیم به صورت برنامه‌ای با مدارک درست (کلید API یا توکن) به آن دسترسی داشته باشیم. در این دوره، ما این ارائه‌دهندگان را بررسی می‌کنیم:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) با مدل‌های متنوع از جمله سری اصلی GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) برای مدل‌های OpenAI با تمرکز بر آمادگی سازمانی
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) برای یک نقطه پایانی و کلید API واحد برای دسترسی به صدها مدل از OpenAI، Meta، Mistral، Cohere، مایکروسافت و غیره (جایگزین GitHub Models که در پایان جولای ۲۰۲۶ بازنشسته می‌شود)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) برای مدل‌های متن‌باز و سرور استنتاج
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) یا [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) اگر ترجیح می‌دهید مدل‌ها را کاملاً به صورت آفلاین روی دستگاه خود اجرا کنید، بدون نیاز به اشتراک ابری

**برای این تمرین‌ها باید از حساب‌های خودتان استفاده کنید**. تمرین‌ها اختیاری هستند، بنابراین می‌توانید بر اساس علاقه‌مندی خود یک یا همه یا هیچ‌کدام از ارائه‌دهندگان را راه‌اندازی کنید. راهنمایی‌هایی برای ثبت نام:

| ثبت نام | هزینه | کلید API | محیط آزمایشی | توضیحات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [براساس پروژه](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون کد، وب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | مدل‌های متعدد موجود |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [شروع سریع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [شروع سریع استودیو](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [باید از قبل درخواست دسترسی بدهید](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [صفحه مرور پروژه](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [محیط آزمایشی Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ارائه رایگان در دسترس؛ یک نقطه پایانی + کلید برای چندین ارائه‌دهنده مدل |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت‌گذاری](https://huggingface.co/pricing) | [توکن‌های دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat مدل‌های محدودی دارد](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | رایگان (روی دستگاه شما اجرا می‌شود) | لازم نیست | [محلی CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | کاملاً آفلاین، نقطه پایانی سازگار با OpenAI |
| | | | | |

برای _پیکربندی_ این مخزن جهت استفاده با ارائه‌دهندگان مختلف، مراحل زیر را دنبال کنید. تمرین‌هایی که نیاز به ارائه‌دهنده خاصی دارند، یکی از این برچسب‌ها را در نام فایلشان خواهند داشت:

- `aoai` - نیاز به نقطه پایانی و کلید Azure OpenAI دارد
- `oai` - نیاز به نقطه پایانی و کلید OpenAI دارد
- `hf` - نیاز به توکن Hugging Face دارد
- `githubmodels` - نیاز به نقطه پایانی و کلید Microsoft Foundry Models دارد (GitHub Models در پایان جولای ۲۰۲۶ بازنشسته می‌شود)

می‌توانید هیچ، یک یا همه ارائه‌دهندگان را پیکربندی کنید. تمرین‌های مرتبط فقط در صورت نبود مدارک خطا می‌دهند.

## ایجاد فایل `.env`

فرض می‌کنیم که راهنمایی‌های بالا را خوانده‌اید، با ارائه‌دهنده مربوطه ثبت نام کرده‌اید و مدارک احراز هویت مورد نیاز (کلید API یا توکن) را به دست آورده‌اید. در مورد Azure OpenAI، فرض می‌کنیم که یک استقرار معتبر از سرویس Azure OpenAI (نقطه پایانی) با حداقل یک مدل GPT برای تکمیل چت دارید.

گام بعدی پیکربندی **متغیرهای محیطی محلی** شما به شرح زیر است:

1. در پوشه ریشه به دنبال فایل `.env.copy` بگردید که باید محتویاتی مشابه این داشته باشد:

   ```bash
   # ارائه‌دهنده OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI در Microsoft Foundry
   ## (خدمت Azure OpenAI اکنون بخشی از Microsoft Foundry است: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # پیش‌فرض تنظیم شده است! (نسخه پایدار فعلی API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## مدل‌های Microsoft Foundry (کاتالوگ مدل چند ارائه‌دهنده، جایگزین مدل‌های GitHub که تا پایان جولای ۲۰۲۶ بازنشسته می‌شوند)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. آن فایل را به `.env` با فرمان زیر کپی کنید. این فایل در _gitignore_ قرار دارد تا اسرار را امن نگه دارد.

   ```bash
   cp .env.copy .env
   ```

3. مقادیر را پر کنید (جایگزین جای‌گیرهای سمت راست `=` شوید) همانطور که در بخش بعدی توضیح داده شده.

4. (اختیاری) اگر از GitHub Codespaces استفاده می‌کنید، می‌توانید متغیرهای محیطی را به صورت _اسرار Codespaces_ متصل به این مخزن ذخیره کنید. در این صورت نیازی به راه‌اندازی فایل محلی .env ندارید. **با این حال، توجه داشته باشید این گزینه فقط در صورتی کاربرد دارد که شما از GitHub Codespaces استفاده کنید.** اگر به جای آن از Docker Desktop استفاده می‌کنید، هنوز باید فایل .env را راه‌اندازی کنید.

## پر کردن فایل `.env`

نگاهی سریع به نام متغیرها بیاندازیم تا بفهمیم هر کدام چه نمایندگی دارند:

| متغیر  | توضیحات  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | این همان توکن دسترسی کاربر است که در پروفایل خود تنظیم کرده‌اید |
| OPENAI_API_KEY | این کلید مجوز برای استفاده از سرویس برای نقطه‌های پایانی غیر Azure OpenAI است |
| AZURE_OPENAI_API_KEY | این کلید مجوز برای استفاده از آن سرویس است |
| AZURE_OPENAI_ENDPOINT | این نقطه پایانی مستقر شده برای منبع Azure OpenAI است |
| AZURE_OPENAI_DEPLOYMENT | این نقطه پایانی استقرار مدل تولید متن است |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | این نقطه پایانی استقرار مدل تعبیه‌های متنی است |
| AZURE_INFERENCE_ENDPOINT | این نقطه پایانی پروژه Microsoft Foundry شماست که برای مدل‌های Microsoft Foundry استفاده می‌شود |
| AZURE_INFERENCE_CREDENTIAL | این کلید API پروژه Microsoft Foundry شماست |
| | |

یادداشت: دو متغیر آخر Azure OpenAI نشان دهنده مدل پیش‌فرض برای تکمیل چت (تولید متن) و جستجوی برداری (embedding) به ترتیب هستند. راهنمایی‌های تنظیم آن‌ها در تمرین‌های مربوطه تعریف خواهد شد.

## پیکربندی Azure OpenAI: از طریق پرتال

> **توجه:** سرویس Azure OpenAI اکنون بخشی از [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) است. منابع و استقرارها هنوز در پرتال Azure نمایش داده می‌شوند، اما مدیریت روزمره مدل (استقرارها، محیط آزمایشی، نظارت) اکنون در پرتال Foundry انجام می‌شود و نه در محیط مستقل قدیمی "Azure OpenAI Studio".

مقادیر نقطه پایانی و کلید Azure OpenAI را می‌توانید در [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بیابید، پس از آنجا شروع می‌کنیم.

1. به [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) بروید
1. گزینه **Keys and Endpoint** را در نوار کناری (منوی سمت چپ) کلیک کنید.
1. روی **Show Keys** کلیک کنید - باید موارد زیر را ببینید: کلید ۱، کلید ۲ و نقطه پایانی.
1. مقدار کلید ۱ را برای AZURE_OPENAI_API_KEY استفاده کنید
1. مقدار نقطه پایانی را برای AZURE_OPENAI_ENDPOINT استفاده کنید

سپس، به نقطه‌های پایانی مدل‌های خاصی که مستقر کرده‌ایم نیاز داریم.

1. گزینه **Model deployments** را در نوار کناری (منوی سمت چپ) برای منبع Azure OpenAI کلیک کنید.
1. در صفحه مقصد، روی **Go to Microsoft Foundry portal** (یا **Manage Deployments** بستگی به نوع منبع شما دارد) کلیک کنید

این شما را به پرتال Microsoft Foundry می‌برد، جایی که مقادیر دیگر را به شرح زیر می‌یابیم.

## پیکربندی Azure OpenAI: از طریق پرتال Microsoft Foundry

1. به [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **از طریق منبع خود** همانطور که بالا توضیح داده شد بروید.
1. از تب **Deployments** (نوار کناری، سمت چپ) برای مشاهده مدل‌های مستقر شده فعلی استفاده کنید.
1. اگر مدل مورد نظر شما مستقر نشده است، از گزینه **Deploy model** برای استقرار آن از [فهرست مدل‌ها](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) استفاده کنید.
1. به یک مدل _تولید متن_ نیاز دارید - ما توصیه می‌کنیم: **gpt-4o-mini**
1. به یک مدل _تعبیه متنی_ نیاز دارید - ما توصیه می‌کنیم **text-embedding-3-small**

حالا متغیرهای محیطی را برای بازتاب _نام استقرار_ مورد استفاده به‌روزرسانی کنید. معمولاً این نام همان نام مدل است مگر اینکه صراحتاً تغییر داده باشید. بنابراین، به عنوان مثال، ممکن است داشته باشید:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**وقتی کار تمام شد، فراموش نکنید فایل .env را ذخیره کنید**. اکنون می‌توانید از فایل خارج شده و به دستورالعمل‌های اجرای دفترچه بازگردید.

## پیکربندی OpenAI: از طریق پروفایل

کلید API OpenAI شما را می‌توانید در حساب [OpenAI خود](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) بیابید. اگر کلیدی ندارید، می‌توانید ثبت نام کنید و یک کلید API ایجاد کنید. پس از داشتن کلید، می‌توانید متغیر `OPENAI_API_KEY` را در فایل `.env` پر کنید.

## پیکربندی Hugging Face: از طریق پروفایل

توکن Hugging Face شما را می‌توان در پروفایل تحت [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) یافت. این‌ها را به صورت عمومی منتشر یا به اشتراک نگذارید. در عوض، یک توکن جدید برای استفاده در این پروژه بسازید و آن را در فایل `.env` در متغیر `HUGGING_FACE_API_KEY` وارد کنید. _توجه:_ این از نظر فنی کلید API نیست ولی برای احراز هویت استفاده می‌شود، لذا نام متغیر را به این شکل نگه داشته‌ایم برای هماهنگی.

## پیکربندی Microsoft Foundry Models: از طریق پرتال

> **توجه:** GitHub Models در پایان جولای ۲۰۲۶ بازنشسته می‌شود. Microsoft Foundry Models جایگزین مستقیم است و تجربه مشابهی از فهرست مدل "رایگان برای امتحان" و SDK استنتاج Azure AI / OpenAI SDK را ارائه می‌کند.

1. به [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) بروید و یک پروژه Foundry بسازید (یا باز کنید).
1. در [فهرست مدل‌ها](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) مرور کرده و یک مدل مستقر کنید، مثلاً `gpt-4o-mini`.
1. در صفحه **مرور کلی** پروژه، **نقطه پایانی** و **کلید API** را کپی کنید.
1. مقدار نقطه پایانی را برای `AZURE_INFERENCE_ENDPOINT` و کلید را برای `AZURE_INFERENCE_CREDENTIAL` در فایل `.env` خود استفاده کنید.

## ارائه‌دهندگان آفلاین/محلی

اگر نمی‌خواهید اصلاً از اشتراک ابری استفاده کنید، می‌توانید مدل‌های سازگار متن‌باز را مستقیماً روی دستگاه خود اجرا کنید:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - زمان اجرای مایکروسافت روی دستگاه شما. به طور خودکار بهترین ارائه‌دهنده اجرا (NPU، GPU، یا CPU) را انتخاب می‌کند و یک نقطه پایانی سازگار با OpenAI ارائه می‌دهد، بنابراین می‌توانید بیشتر کد نمونه در این دوره را با حداقل تغییرات باز استفاده کنید. جهت شروع به [مستندات Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) مراجعه کنید، یا با `winget install Microsoft.FoundryLocal` (ویندوز) / `brew install microsoft/foundrylocal/foundrylocal` (مک‌او‌اس) نصب کنید.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - یک جایگزین محبوب برای اجرای مدل‌های باز مانند Llama، Phi، Mistral، و Gemma به صورت محلی.


برای مثال‌های عملی با استفاده از هر دو گزینه، به [درس ۱۹: ساخت با SLMها](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->