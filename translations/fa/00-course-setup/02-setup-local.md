# راه‌اندازی محلی 🖥️

**اگر ترجیح می‌دهید همه چیز را روی لپ‌تاپ خود اجرا کنید، از این راهنما استفاده کنید.**  
شما دو مسیر دارید: **(A) پایتون بومی + virtual-env** یا **(B) کانتینر توسعه در VS Code با داکر**.  
هر کدام که برایتان آسان‌تر است انتخاب کنید—هر دو به درس‌های یکسانی منجر می‌شوند.

## 1. پیش‌نیازها

| ابزار                | نسخه / یادداشت‌ها                                                                       |
|----------------------|-----------------------------------------------------------------------------------------|
| **پایتون**           | 3.10 + (از <https://python.org> دریافت کنید)                                           |
| **گیت**              | آخرین نسخه (همراه با Xcode / گیت برای ویندوز / مدیر بسته لینوکس)                       |
| **VS Code**          | اختیاری اما توصیه شده <https://code.visualstudio.com>                                |
| **Docker Desktop**   | *فقط* برای گزینه B. نصب رایگان: <https://docs.docker.com/desktop/>                   |

> 💡 **نکته** – ابزارها را در ترمینال بررسی کنید:  
> `python --version`، `git --version`، `docker --version`، `code --version`  

## 2. گزینه A – پایتون بومی (سریع‌ترین)

### گام 1 کلون کردن این مخزن

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### گام 2 ساخت و فعال‌سازی محیط مجازی

```bash
python -m venv .venv          # بساز
source .venv/bin/activate     # مک‌اواس / لینوکس
.\.venv\Scripts\activate      # ویندوز پاورشل
```

✅ اکنون پرامپت باید با (.venv) شروع شود — یعنی داخل محیط مجازی هستید.

### گام 3 نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

به بخش 3 درباره [کلیدهای API](#3-کلیدهای-api-خود-را-اضافه-کنید) بروید

## 2. گزینه B – کانتینر توسعه VS Code (داکر)

این مخزن و دوره را با یک <a href="https://containers.dev?WT.mc_id=academic-105485-koreyst">کانتینر توسعه</a> راه‌اندازی کردیم که یک محیط اجرایی جهانی دارد که از پایتون ۳، .NET، Node.js و جاوا پشتیبانی می‌کند. تنظیمات مرتبط در فایل `devcontainer.json` در پوشه `.devcontainer/` در ریشه این مخزن تعریف شده است.

>**چرا این را انتخاب کنیم؟**
>محیطی مشابه Codespaces؛ بدون انحراف وابستگی.

### گام 0 نصب موارد اضافی

Docker Desktop – تأیید کنید که ```docker --version``` کار می‌کند.
افزونه VS Code Remote – Containers (شناسه: ms-vscode-remote.remote-containers).

### گام 1 باز کردن مخزن در VS Code

فایل ▸ باز کردن پوشه…  → generative-ai-for-beginners

VS Code پوشه .devcontainer/ را شناسایی کرده و یک اعلان باز می‌کند.

### گام 2 دوباره باز کردن در کانتینر

روی «بازکردن دوباره در کانتینر» کلیک کنید. داکر تصویر را می‌سازد (≈ ۳ دقیقه در بار اول).
وقتی پرامپت ترمینال ظاهر شد، داخل کانتینر هستید.

## 2. گزینه C – Miniconda

<a href="https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst">Miniconda</a> یک نصب‌کننده سبک برای نصب <a href="https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst">Conda</a>، پایتون و چند بسته دیگر است.
Conda خود مدیر بسته‌ای است که کار راه‌اندازی و تعویض بین مختلف [محیط‌های مجازی](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) پایتون و بسته‌ها را آسان می‌کند. همچنین برای نصب بسته‌هایی که با `pip` در دسترس نیستند مفید است.

### گام 0 نصب Miniconda

راهنمای <a href="https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst">نصب MiniConda</a> را دنبال کنید تا آن را راه‌اندازی کنید.

```bash
conda --version
```

### گام 1 ساخت یک محیط مجازی

یک فایل محیط جدید (*environment.yml*) ایجاد کنید. اگر در Codespaces هستید، این فایل را در دایرکتوری `.devcontainer` بسازید، یعنی `.devcontainer/environment.yml`.

### گام 2 پر کردن فایل محیط‌تان

قطعه زیر را به `environment.yml` اضافه کنید

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### گام 3 ساخت محیط Conda

دستورات زیر را در خط فرمان/ترمینال خود اجرا کنید

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer زیرمسیر فقط برای تنظیمات Codespace اعمال می‌شود
conda activate ai4beg
```

اگر مشکلی پیش آمد به راهنمای <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst">محیط‌های Conda</a> مراجعه کنید.

## 2 گزینه D – Jupyter کلاسیک / Jupyter Lab (در مرورگر شما)

> **این گزینه برای کیست؟**  
> هر کسی که رابط کلاسیک Jupyter را دوست دارد یا می‌خواهد نوت‌بوک‌ها را بدون VS Code اجرا کند.  

### گام 1 اطمینان از نصب Jupyter

برای اجرای Jupyter به صورت محلی، به ترمینال/خط فرمان بروید، به دایرکتوری دوره مراجعه کنید و دستور زیر را اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این باعث راه‌اندازی یک نمونه Jupyter می‌شود و آدرس URL دسترسی به آن در پنجره خط فرمان ظاهر خواهد شد.

وقتی به URL دسترسی پیدا کردید، باید طرح کلی دوره را ببینید و بتوانید به هر فایل `*.ipynb` وارد شوید. مثلاً `08-building-search-applications/python/oai-solution.ipynb`.

## 3. کلیدهای API خود را اضافه کنید

حفظ امنیت و محافظت کلیدهای API هنگام ساخت هر نوع برنامه‌ای مهم است. پیشنهاد می‌کنیم کلیدهای API را مستقیماً در کد خود ذخیره نکنید. قرار دادن این اطلاعات در مخزن عمومی ممکن است منجر به مشکلات امنیتی و حتی هزینه‌های ناخواسته در صورت استفاده توسط افراد سوءاستفاده‌گر شود.
در اینجا راهنمای گام‌به‌گام برای ایجاد فایل `.env` در پایتون و افزودن اعتبارنامه‌های Microsoft Foundry Models ارائه شده است:

> **توجه:** مدل‌های GitHub (و متغیر `GITHUB_TOKEN` آن) تا پایان جولای ۲۰۲۶ بازنشسته می‌شوند. این راهنما از <a href="https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst">Microsoft Foundry Models</a> استفاده می‌کند. ترجیح می‌دهید کاملاً آفلاین کار کنید؟ به <a href="https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst">Foundry Local</a> مراجعه کنید.

۱. **رفتن به دایرکتوری پروژه**: ترمینال یا خط فرمان خود را باز کنید و به ریشه دایرکتوری پروژه که می‌خواهید فایل `.env` را ایجاد کنید، بروید.

   ```bash
   cd path/to/your/project
   ```

۲. **ایجاد فایل `.env`**: از ویرایشگر متن مورد علاقه خود برای ایجاد یک فایل جدید به نام `.env` استفاده کنید. اگر از خط فرمان استفاده می‌کنید، می‌توانید از `touch` (در سیستم‌های مبتنی بر یونیکس) یا `echo` (در ویندوز) استفاده کنید:

   سیستم‌های مبتنی بر یونیکس:

   ```bash
   touch .env
   ```

   ویندوز:

   ```cmd
   echo . > .env
   ```

۳. **ویرایش فایل `.env`**: فایل `.env` را در یک ویرایشگر متن (مثلاً VS Code، Notepad++ یا هر ویرایشگر دیگری) باز کنید. خطوط زیر را به فایل اضافه کنید و مقادیر جایگزین را با نقطه پایانی پروژه و کلید API واقعی Microsoft Foundry خود جایگزین کنید:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

۴. **ذخیره فایل**: تغییرات را ذخیره کرده و ویرایشگر متن را ببندید.

۵. **نصب `python-dotenv`**: اگر قبلاً نصب نکرده‌اید، باید بسته `python-dotenv` را نصب کنید تا متغیرهای محیطی از فایل `.env` در برنامه پایتون شما بارگذاری شوند. می‌توانید آن را با `pip` نصب کنید:

   ```bash
   pip install python-dotenv
   ```

۶. **بارگذاری متغیرهای محیطی در اسکریپت پایتون خود**: در اسکریپت پایتون خود، از بسته `python-dotenv` استفاده کنید تا متغیرهای محیطی را از فایل `.env` بارگذاری کنید:

   ```python
   from dotenv import load_dotenv
   import os

   # بارگذاری متغیرهای محیطی از فایل .env
   load_dotenv()

   # دسترسی به متغیرهای مدل‌های Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

همین بود! شما با موفقیت فایل `.env` ایجاد کرده‌اید، اعتبارنامه‌های Microsoft Foundry Models خود را اضافه کرده‌اید و آن‌ها را در برنامه پایتون خود بارگذاری کرده‌اید.

🔐 هرگز فایل .env را کامیت نکنید — این فایل در .gitignore قرار دارد.
دستورالعمل‌های کامل ارائه‌دهنده در [`providers.md`](03-providers.md) موجود است.

## 4. قدم بعدی چیست؟

| می‌خواهم…           | بروم به…                                                                |
|---------------------|-------------------------------------------------------------------------|
| شروع درس ۱          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| راه‌اندازی یک ارائه‌دهنده LLM | [`providers.md`](03-providers.md)                                       |
| ملاقات با دیگر یادگیرندگان | [عضویت در Discord ما](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. رفع اشکال

| نشانه                                     | راه‌حل                                                            |
|--------------------------------------------|------------------------------------------------------------------|
| `python not found` (پایتون پیدا نشد)        | پایتون را به PATH اضافه کنید یا پس از نصب ترمینال را دوباره باز کنید.    |
| `pip` نمی‌تواند wheel بسازد (ویندوز)        | دستور `pip install --upgrade pip setuptools wheel` را اجرا کرده و دوباره تلاش کنید. |
| `ModuleNotFoundError: dotenv` (ماژول dotenv پیدا نشد) | دستور `pip install -r requirements.txt` را اجرا کنید (محیط نصب نشده بود). |
| ساخت داکر خطا می‌دهد *No space left*         | در Docker Desktop ▸ *Settings* ▸ *Resources* → اندازه دیسک را افزایش دهید. |
| VS Code مدام پیشنهاد بازکردن مجدد می‌دهد       | ممکن است هر دو گزینه فعال باشند؛ یکی را انتخاب کنید (venv **یا** کانتینر).  |
| خطاهای ۴۰۱ / ۴۲۹ OpenAI                     | مقدار `OPENAI_API_KEY` و نرخ درخواست‌ها را بررسی کنید.            |
| خطا در استفاده از Conda                      | کتابخانه‌های هوش مصنوعی مایکروسافت را با دستور `conda install -c microsoft azure-ai-ml` نصب کنید. |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->