<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:52:30+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fa"
}
-->
# AGENTS.md

## نمای کلی پروژه

این مخزن شامل یک برنامه درسی جامع ۲۱ درس برای آموزش اصول هوش مصنوعی تولیدی و توسعه برنامه‌ها است. این دوره برای مبتدیان طراحی شده و همه چیز را از مفاهیم پایه تا ساخت برنامه‌های آماده تولید پوشش می‌دهد.

**فناوری‌های کلیدی:**
- Python 3.9+ با کتابخانه‌ها: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript با Node.js و کتابخانه‌ها: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- سرویس Azure OpenAI، OpenAI API و مدل‌های GitHub
- Jupyter Notebooks برای یادگیری تعاملی
- Dev Containers برای محیط توسعه یکپارچه

**ساختار مخزن:**
- ۲۱ پوشه درس شماره‌گذاری شده (۰۰-۲۱) شامل فایل‌های README، مثال‌های کد و تکالیف
- پیاده‌سازی‌های متعدد: Python، TypeScript و گاهی مثال‌های .NET
- پوشه ترجمه‌ها با نسخه‌های بیش از ۴۰ زبان
- پیکربندی متمرکز از طریق فایل `.env` (از `.env.copy` به عنوان قالب استفاده کنید)

## دستورات راه‌اندازی

### راه‌اندازی اولیه مخزن

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### راه‌اندازی محیط Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### راه‌اندازی Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### راه‌اندازی Dev Container (توصیه‌شده)

این مخزن شامل پیکربندی `.devcontainer` برای GitHub Codespaces یا Dev Containers در VS Code است:

1. مخزن را در GitHub Codespaces یا VS Code با افزونه Dev Containers باز کنید
2. Dev Container به طور خودکار:
   - وابستگی‌های Python را از `requirements.txt` نصب می‌کند
   - اسکریپت پس از ایجاد (`.devcontainer/post-create.sh`) را اجرا می‌کند
   - کرنل Jupyter را تنظیم می‌کند

## جریان کاری توسعه

### متغیرهای محیطی

تمام درس‌هایی که نیاز به دسترسی API دارند از متغیرهای محیطی تعریف‌شده در `.env` استفاده می‌کنند:

- `OPENAI_API_KEY` - برای OpenAI API
- `AZURE_OPENAI_API_KEY` - برای سرویس Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL نقطه پایانی Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - نام استقرار مدل تکمیل چت
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - نام استقرار مدل Embeddings
- `AZURE_OPENAI_API_VERSION` - نسخه API (پیش‌فرض: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - برای مدل‌های Hugging Face
- `GITHUB_TOKEN` - برای مدل‌های GitHub

### اجرای مثال‌های Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### اجرای مثال‌های TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### اجرای Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### کار با انواع مختلف درس‌ها

- **درس‌های "یادگیری"**: تمرکز بر مستندات README.md و مفاهیم
- **درس‌های "ساخت"**: شامل مثال‌های کد عملی در Python و TypeScript
- هر درس دارای README.md با نظریه، مرور کد و لینک‌های محتوای ویدیویی است

## دستورالعمل‌های سبک کدنویسی

### Python

- از `python-dotenv` برای مدیریت متغیرهای محیطی استفاده کنید
- کتابخانه `openai` را برای تعاملات API وارد کنید
- از `pylint` برای بررسی کد استفاده کنید (برخی مثال‌ها شامل `# pylint: disable=all` برای سادگی هستند)
- از کنوانسیون‌های نام‌گذاری PEP 8 پیروی کنید
- اعتبارنامه‌های API را در فایل `.env` ذخیره کنید، نه در کد

### TypeScript

- از بسته `dotenv` برای متغیرهای محیطی استفاده کنید
- پیکربندی TypeScript در `tsconfig.json` برای هر برنامه
- از `@azure/openai` یا `@azure-rest/ai-inference` برای خدمات Azure استفاده کنید
- از `nodemon` برای توسعه با بارگذاری خودکار استفاده کنید
- قبل از اجرا بسازید: `npm run build` سپس `npm start`

### کنوانسیون‌های عمومی

- مثال‌های کد را ساده و آموزشی نگه دارید
- شامل توضیحات در مورد مفاهیم کلیدی باشید
- کد هر درس باید مستقل و قابل اجرا باشد
- از نام‌گذاری یکسان استفاده کنید: پیشوند `aoai-` برای Azure OpenAI، `oai-` برای OpenAI API، `githubmodels-` برای مدل‌های GitHub

## دستورالعمل‌های مستندسازی

### سبک Markdown

- تمام URL‌ها باید در قالب `[متن](../../url)` با هیچ فاصله اضافی قرار گیرند
- لینک‌های نسبی باید با `./` یا `../` شروع شوند
- تمام لینک‌ها به دامنه‌های Microsoft باید شامل شناسه ردیابی باشند: `?WT.mc_id=academic-105485-koreyst`
- از لوکال‌های خاص کشور در URL‌ها اجتناب کنید (از `/en-us/` خودداری کنید)
- تصاویر در پوشه `./images` با نام‌های توصیفی ذخیره شوند
- از کاراکترهای انگلیسی، اعداد و خط تیره در نام فایل‌ها استفاده کنید

### پشتیبانی ترجمه

- مخزن از بیش از ۴۰ زبان از طریق GitHub Actions خودکار پشتیبانی می‌کند
- ترجمه‌ها در پوشه `translations/` ذخیره می‌شوند
- ترجمه‌های ناقص ارسال نکنید
- ترجمه‌های ماشینی پذیرفته نمی‌شوند
- تصاویر ترجمه‌شده در پوشه `translated_images/` ذخیره می‌شوند

## آزمایش و اعتبارسنجی

### بررسی‌های پیش از ارسال

این مخزن از GitHub Actions برای اعتبارسنجی استفاده می‌کند. قبل از ارسال PR‌ها:

1. **بررسی لینک‌های Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **آزمایش دستی**:
   - مثال‌های Python را آزمایش کنید: venv را فعال کنید و اسکریپت‌ها را اجرا کنید
   - مثال‌های TypeScript را آزمایش کنید: `npm install`, `npm run build`, `npm start`
   - اطمینان حاصل کنید که متغیرهای محیطی به درستی پیکربندی شده‌اند
   - بررسی کنید که کلیدهای API با مثال‌های کد کار می‌کنند

3. **مثال‌های کد**:
   - اطمینان حاصل کنید که تمام کد بدون خطا اجرا می‌شود
   - با هر دو Azure OpenAI و OpenAI API در صورت امکان آزمایش کنید
   - بررسی کنید که مثال‌ها با مدل‌های GitHub در صورت پشتیبانی کار می‌کنند

### بدون آزمایش‌های خودکار

این یک مخزن آموزشی است که بر آموزش و مثال‌ها تمرکز دارد. هیچ آزمایش واحد یا یکپارچه‌ای برای اجرا وجود ندارد. اعتبارسنجی عمدتاً شامل موارد زیر است:
- آزمایش دستی مثال‌های کد
- GitHub Actions برای اعتبارسنجی Markdown
- بررسی محتوای آموزشی توسط جامعه

## دستورالعمل‌های درخواست کشش (Pull Request)

### قبل از ارسال

1. تغییرات کد را در هر دو Python و TypeScript در صورت امکان آزمایش کنید
2. اعتبارسنجی Markdown را اجرا کنید (به طور خودکار در PR فعال می‌شود)
3. اطمینان حاصل کنید که شناسه‌های ردیابی در تمام URL‌های Microsoft وجود دارند
4. بررسی کنید که لینک‌های نسبی معتبر هستند
5. اطمینان حاصل کنید که تصاویر به درستی ارجاع داده شده‌اند

### قالب عنوان PR

- از عناوین توصیفی استفاده کنید: `[درس ۰۶] اصلاح خطای تایپی مثال Python` یا `به‌روزرسانی README برای درس ۰۸`
- در صورت امکان به شماره‌های مسئله اشاره کنید: `Fixes #123`

### توضیحات PR

- توضیح دهید که چه چیزی تغییر کرده و چرا
- لینک به مسائل مرتبط
- برای تغییرات کد، مشخص کنید که کدام مثال‌ها آزمایش شده‌اند
- برای PR‌های ترجمه، تمام فایل‌ها را برای یک ترجمه کامل شامل کنید

### الزامات مشارکت

- امضای Microsoft CLA (به طور خودکار در اولین PR)
- مخزن را به حساب خود فورک کنید قبل از ایجاد تغییرات
- یک PR برای هر تغییر منطقی (تغییرات غیرمرتبط را ترکیب نکنید)
- PR‌ها را متمرکز و کوچک نگه دارید در صورت امکان

## جریان‌های کاری رایج

### افزودن یک مثال کد جدید

1. به پوشه درس مربوطه بروید
2. مثال را در زیرپوشه `python/` یا `typescript/` ایجاد کنید
3. از کنوانسیون نام‌گذاری پیروی کنید: `{provider}-{example-name}.{py|ts|js}`
4. با اعتبارنامه‌های واقعی API آزمایش کنید
5. هر متغیر محیطی جدید را در README درس مستند کنید

### به‌روزرسانی مستندات

1. فایل README.md را در پوشه درس ویرایش کنید
2. از دستورالعمل‌های Markdown پیروی کنید (شناسه‌های ردیابی، لینک‌های نسبی)
3. به‌روزرسانی ترجمه‌ها توسط GitHub Actions مدیریت می‌شود (به صورت دستی ویرایش نکنید)
4. تمام لینک‌ها را بررسی کنید که معتبر باشند

### کار با Dev Containers

1. مخزن شامل فایل `.devcontainer/devcontainer.json` است
2. اسکریپت پس از ایجاد به طور خودکار وابستگی‌های Python را نصب می‌کند
3. افزونه‌ها برای Python و Jupyter از پیش پیکربندی شده‌اند
4. محیط بر اساس `mcr.microsoft.com/devcontainers/universal:2.11.2` است

## استقرار و انتشار

این یک مخزن آموزشی است - هیچ فرآیند استقراری وجود ندارد. برنامه درسی توسط موارد زیر مصرف می‌شود:

1. **مخزن GitHub**: دسترسی مستقیم به کد و مستندات
2. **GitHub Codespaces**: محیط توسعه فوری با تنظیمات از پیش پیکربندی‌شده
3. **Microsoft Learn**: محتوا ممکن است به پلتفرم یادگیری رسمی منتقل شود
4. **docsify**: سایت مستندات ساخته‌شده از Markdown (به `docsifytopdf.js` و `package.json` مراجعه کنید)

### ساخت سایت مستندات

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## رفع اشکال

### مشکلات رایج

**خطاهای وارد کردن Python**:
- اطمینان حاصل کنید که محیط مجازی فعال است
- دستور `pip install -r requirements.txt` را اجرا کنید
- بررسی کنید که نسخه Python 3.9+ باشد

**خطاهای ساخت TypeScript**:
- دستور `npm install` را در پوشه برنامه خاص اجرا کنید
- بررسی کنید که نسخه Node.js سازگار باشد
- پوشه `node_modules` را پاک کنید و دوباره نصب کنید در صورت نیاز

**خطاهای احراز هویت API**:
- بررسی کنید که فایل `.env` وجود دارد و مقادیر صحیح دارد
- اطمینان حاصل کنید که کلیدهای API معتبر و منقضی نشده‌اند
- بررسی کنید که URL‌های نقطه پایانی برای منطقه شما صحیح هستند

**متغیرهای محیطی گم‌شده**:
- فایل `.env.copy` را به `.env` کپی کنید
- تمام مقادیر مورد نیاز برای درسی که روی آن کار می‌کنید را پر کنید
- پس از به‌روزرسانی `.env` برنامه خود را مجدداً راه‌اندازی کنید

## منابع اضافی

- [راهنمای راه‌اندازی دوره](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [دستورالعمل‌های مشارکت](./CONTRIBUTING.md)
- [قوانین رفتاری](./CODE_OF_CONDUCT.md)
- [سیاست امنیتی](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [مجموعه نمونه‌های کد پیشرفته](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## یادداشت‌های خاص پروژه

- این یک **مخزن آموزشی** است که بر یادگیری تمرکز دارد، نه کد تولیدی
- مثال‌ها به طور عمدی ساده و متمرکز بر آموزش مفاهیم هستند
- کیفیت کد با وضوح آموزشی متعادل شده است
- هر درس مستقل است و می‌توان آن را به طور جداگانه تکمیل کرد
- مخزن از چندین ارائه‌دهنده API پشتیبانی می‌کند: Azure OpenAI، OpenAI و مدل‌های GitHub
- محتوا چندزبانه است و دارای جریان‌های کاری ترجمه خودکار است
- جامعه فعال در Discord برای سوالات و پشتیبانی

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.