<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T14:09:07+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "fa"
}
-->
# راه‌اندازی محلی 🖥️

**اگر دوست دارید همه چیز را روی لپ‌تاپ خودتان اجرا کنید، از این راهنما استفاده کنید.**  
دو مسیر پیش رو دارید: **(A) پایتون اصلی + محیط مجازی** یا **(B) Dev Container در VS Code با Docker**.  
هر کدام که برایتان راحت‌تر است را انتخاب کنید—هر دو به یک درس منتهی می‌شوند.

## ۱. پیش‌نیازها

| ابزار                | نسخه / توضیحات                                                                      |
|----------------------|-------------------------------------------------------------------------------------|
| **Python**           | ۳.۱۰ به بالا (از <https://python.org> دریافت کنید)                                  |
| **Git**              | آخرین نسخه (همراه با Xcode / Git for Windows / مدیر بسته لینوکس)                   |
| **VS Code**          | اختیاری اما توصیه می‌شود <https://code.visualstudio.com>                            |
| **Docker Desktop**   | *فقط* برای گزینه B. نصب رایگان: <https://docs.docker.com/desktop/>                 |

> 💡 **نکته** – ابزارها را در ترمینال بررسی کنید:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## ۲. گزینه A – پایتون اصلی (سریع‌ترین)

### گام ۱  کلون کردن این مخزن

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### گام ۲ ساخت و فعال‌سازی محیط مجازی

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ حالا باید ابتدای خط فرمان (.venv) باشد—یعنی داخل محیط مجازی هستید.

### گام ۳ نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

به بخش ۳ درباره [کلیدهای API](../../../00-course-setup) بروید

## ۲. گزینه B – Dev Container در VS Code (Docker)

ما این مخزن و دوره را با یک [کانتینر توسعه](https://containers.dev?WT.mc_id=academic-105485-koreyst) راه‌اندازی کردیم که محیطی جهانی برای پایتون ۳، .NET، Node.js و جاوا فراهم می‌کند. پیکربندی مربوطه در فایل `devcontainer.json` در پوشه `.devcontainer/` در ریشه این مخزن قرار دارد.

>**چرا این گزینه؟**
>محیط کاملاً مشابه Codespaces؛ بدون اختلاف وابستگی‌ها.

### گام ۰ نصب موارد اضافی

Docker Desktop – مطمئن شوید ```docker --version``` کار می‌کند.
افزونه VS Code Remote – Containers (شناسه: ms-vscode-remote.remote-containers).

### گام ۱ باز کردن مخزن در VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code پوشه .devcontainer/ را شناسایی می‌کند و یک پیام نمایش می‌دهد.

### گام ۲ باز کردن مجدد در کانتینر

روی “Reopen in Container” کلیک کنید. Docker ایمیج را می‌سازد (بار اول حدود ۳ دقیقه).
وقتی خط فرمان ظاهر شد، داخل کانتینر هستید.

## ۲. گزینه C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و چند بسته دیگر است.
خود Conda یک مدیر بسته است که راه‌اندازی و جابجایی بین [**محیط‌های مجازی**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) و بسته‌های مختلف پایتون را آسان می‌کند. همچنین برای نصب بسته‌هایی که با `pip` قابل نصب نیستند، مفید است.

### گام ۰  نصب Miniconda

طبق [راهنمای نصب MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) پیش بروید.

```bash
conda --version
```

### گام ۱ ساخت محیط مجازی

یک فایل محیط جدید (*environment.yml*) بسازید. اگر با Codespaces پیش می‌روید، این فایل را در پوشه `.devcontainer` بسازید، یعنی `.devcontainer/environment.yml`.

### گام ۲  پر کردن فایل محیط

کد زیر را به `environment.yml` اضافه کنید

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

### گام ۳ ساخت محیط Conda

دستورات زیر را در خط فرمان اجرا کنید

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر به مشکلی برخوردید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

## ۲. گزینه D – Jupyter کلاسیک / Jupyter Lab (در مرورگر شما)

> **مناسب چه کسانی است؟**  
> هر کسی که رابط کلاسیک Jupyter را دوست دارد یا می‌خواهد نوت‌بوک‌ها را بدون VS Code اجرا کند.  

### گام ۱  مطمئن شوید Jupyter نصب است

برای اجرای Jupyter به صورت محلی، ترمینال را باز کنید، به پوشه دوره بروید و اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این کار یک نمونه Jupyter را اجرا می‌کند و آدرس دسترسی در همان پنجره نمایش داده می‌شود.

پس از ورود به آدرس، باید فهرست دوره را ببینید و بتوانید به هر فایل `*.ipynb` بروید. مثلاً: `08-building-search-applications/python/oai-solution.ipynb`.

## ۳. افزودن کلیدهای API

حفظ امنیت کلیدهای API هنگام ساخت هر نوع برنامه‌ای بسیار مهم است. توصیه می‌کنیم هیچ کلید API را مستقیماً در کد خود ذخیره نکنید. قرار دادن این اطلاعات در مخزن عمومی می‌تواند باعث مشکلات امنیتی و حتی هزینه‌های ناخواسته شود اگر افراد سوءاستفاده‌گر از آن استفاده کنند.
در اینجا راهنمای گام‌به‌گام ساخت فایل `.env` برای پایتون و افزودن `GITHUB_TOKEN` آمده است:

۱. **رفتن به پوشه پروژه**: ترمینال یا Command Prompt را باز کنید و به پوشه اصلی پروژه بروید، جایی که می‌خواهید فایل `.env` را بسازید.

   ```bash
   cd path/to/your/project
   ```

۲. **ساخت فایل `.env`**: با ویرایشگر دلخواه یک فایل جدید به نام `.env` بسازید. اگر از خط فرمان استفاده می‌کنید، می‌توانید از `touch` (در سیستم‌های یونیکسی) یا `echo` (در ویندوز) استفاده کنید:

   سیستم‌های یونیکسی:

   ```bash
   touch .env
   ```

   ویندوز:

   ```cmd
   echo . > .env
   ```

۳. **ویرایش فایل `.env`**: فایل `.env` را با یک ویرایشگر متن (مثلاً VS Code، Notepad++ یا هر ویرایشگر دیگر) باز کنید. خط زیر را به فایل اضافه کنید و `your_github_token_here` را با توکن واقعی خود جایگزین کنید:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

۴. **ذخیره فایل**: تغییرات را ذخیره و ویرایشگر را ببندید.

۵. **نصب `python-dotenv`**: اگر قبلاً نصب نکرده‌اید، باید بسته `python-dotenv` را نصب کنید تا متغیرهای محیطی را از فایل `.env` به برنامه پایتون خود بارگذاری کنید. با `pip` نصب کنید:

   ```bash
   pip install python-dotenv
   ```

۶. **بارگذاری متغیرهای محیطی در اسکریپت پایتون**: در اسکریپت پایتون خود، با استفاده از بسته `python-dotenv` متغیرهای محیطی را از فایل `.env` بارگذاری کنید:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

همین! شما با موفقیت فایل `.env` را ساختید، توکن گیت‌هاب را اضافه کردید و آن را در برنامه پایتون خود بارگذاری کردید.

🔐 هرگز فایل .env را کامیت نکنید—در .gitignore قرار دارد.
راهنمای کامل ارائه‌دهندگان در [`providers.md`](03-providers.md) موجود است.

## ۴. مرحله بعد چیست؟

| می‌خواهم…            | برو به…                                                                  |
|----------------------|--------------------------------------------------------------------------|
| شروع درس ۱           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| راه‌اندازی ارائه‌دهنده LLM | [`providers.md`](03-providers.md)                                      |
| آشنایی با سایر یادگیرندگان | [به دیسکورد ما بپیوندید](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## ۵. رفع اشکال

| نشانه                                   | راه‌حل                                                            |
|------------------------------------------|-------------------------------------------------------------------|
| `python not found`                       | پایتون را به PATH اضافه کنید یا ترمینال را پس از نصب دوباره باز کنید |
| `pip` نمی‌تواند wheels بسازد (ویندوز)   | `pip install --upgrade pip setuptools wheel` را اجرا و دوباره تلاش کنید. |
| `ModuleNotFoundError: dotenv`            | `pip install -r requirements.txt` را اجرا کنید (محیط نصب نشده است). |
| خطای ساخت Docker *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → افزایش حجم دیسک.      |
| VS Code مدام درخواست باز کردن مجدد می‌دهد | ممکن است هر دو گزینه فعال باشند؛ یکی را انتخاب کنید (venv **یا** container)|
| خطاهای 401 / 429 OpenAI                  | مقدار `OPENAI_API_KEY` یا محدودیت نرخ درخواست را بررسی کنید.      |
| خطا هنگام استفاده از Conda               | کتابخانه‌های AI مایکروسافت را با `conda install -c microsoft azure-ai-ml` نصب کنید|

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادرستی باشند. نسخه اصلی سند به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.