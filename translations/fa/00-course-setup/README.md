<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T14:10:20+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fa"
}
-->
# شروع کار با این دوره

خیلی خوشحالیم که می‌خواهید این دوره را شروع کنید و ببینید با هوش مصنوعی مولد چه چیزهایی می‌توانید بسازید!

برای اینکه موفق باشید، این صفحه مراحل راه‌اندازی، نیازمندی‌های فنی و راه‌های دریافت کمک را توضیح می‌دهد.

## مراحل راه‌اندازی

برای شروع این دوره، باید مراحل زیر را انجام دهید.

### ۱. فورک کردن این مخزن

[کل این مخزن را فورک کنید](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) تا بتوانید کدها را تغییر دهید و چالش‌ها را کامل کنید. همچنین می‌توانید [این مخزن را ستاره‌دار (🌟) کنید](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تا راحت‌تر آن را پیدا کنید.

### ۲. ساختن یک codespace

برای جلوگیری از مشکلات وابستگی هنگام اجرای کد، توصیه می‌کنیم این دوره را در [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) اجرا کنید.

در فورک خودتان: **Code -> Codespaces -> New on main**

![دیالوگ نمایش دکمه‌های ساخت codespace](../../../00-course-setup/images/who-will-pay.webp)

#### ۲.۱ افزودن یک secret

۱. آیکون ⚙️ -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
۲. نام OPENAI_API_KEY را وارد کنید، کلید خود را بچسبانید و ذخیره کنید.

### ۳. بعدی چه کاری انجام دهم؟

| می‌خواهم...           | برو به...                                                                |
|----------------------|--------------------------------------------------------------------------|
| شروع درس اول         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| کار آفلاین           | [`setup-local.md`](02-setup-local.md)                                    |
| راه‌اندازی ارائه‌دهنده LLM | [`providers.md`](providers.md)                                   |
| آشنایی با سایر یادگیرندگان | [به دیسکورد ما بپیوندید](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## رفع اشکال

| نشانه مشکل                              | راه‌حل                                                          |
|-----------------------------------------|-----------------------------------------------------------------|
| ساخت کانتینر بیش از ۱۰ دقیقه طول کشید   | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`             | ترمینال وصل نشده؛ روی **+** ➜ *bash* کلیک کنید                  |
| `401 Unauthorized` از OpenAI            | `OPENAI_API_KEY` اشتباه یا منقضی شده                            |
| VS Code پیام “Dev container mounting…”  | تب مرورگر را رفرش کنید—گاهی Codespaces ارتباط را از دست می‌دهد |
| کرنل نوت‌بوک پیدا نمی‌شود               | منوی نوت‌بوک ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   سیستم‌های مبتنی بر یونیکس:

   ```bash
   touch .env
   ```

   ویندوز:

   ```cmd
   echo . > .env
   ```

۳. **ویرایش فایل `.env`**: فایل `.env` را با یک ویرایشگر متن (مثل VS Code، Notepad++ یا هر ویرایشگر دیگر) باز کنید. خط زیر را به فایل اضافه کنید و `your_github_token_here` را با توکن واقعی خود جایگزین کنید:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

۴. **ذخیره فایل**: تغییرات را ذخیره کنید و ویرایشگر را ببندید.

۵. **نصب `python-dotenv`**: اگر قبلاً نصب نکرده‌اید، باید بسته `python-dotenv` را نصب کنید تا متغیرهای محیطی را از فایل `.env` در برنامه پایتون خود بارگذاری کنید. با دستور زیر نصب کنید:

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

تمام شد! شما با موفقیت فایل `.env` را ساختید، توکن گیت‌هاب خود را اضافه کردید و آن را در برنامه پایتون خود بارگذاری کردید.

## نحوه اجرای محلی روی کامپیوتر

برای اجرای کدها به صورت محلی روی کامپیوتر خود، باید [پایتون](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) را نصب کرده باشید.

برای استفاده از مخزن، باید آن را کلون کنید:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

وقتی همه چیز را دریافت کردید، می‌توانید شروع کنید!

## مراحل اختیاری

### نصب Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و چند بسته دیگر است.
خود Conda یک مدیر بسته است که راه‌اندازی و جابجایی بین [محیط‌های مجازی](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) و بسته‌های مختلف پایتون را آسان می‌کند. همچنین برای نصب بسته‌هایی که با `pip` قابل نصب نیستند، کاربرد دارد.

می‌توانید راهنمای نصب [MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) را دنبال کنید.

بعد از نصب Miniconda، باید [مخزن را کلون کنید](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (اگر قبلاً این کار را نکرده‌اید)

سپس باید یک محیط مجازی بسازید. برای این کار با Conda، یک فایل محیط جدید (_environment.yml_) بسازید. اگر با Codespaces کار می‌کنید، این فایل را در پوشه `.devcontainer` بسازید، یعنی `.devcontainer/environment.yml`.

فایل محیط خود را با قطعه کد زیر پر کنید:

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

اگر با استفاده از conda دچار خطا شدید، می‌توانید کتابخانه‌های هوش مصنوعی مایکروسافت را با دستور زیر به صورت دستی نصب کنید.

```
conda install -c microsoft azure-ai-ml
```

فایل محیط وابستگی‌های مورد نیاز را مشخص می‌کند. `<environment-name>` نامی است که برای محیط Conda خود انتخاب می‌کنید و `<python-version>` نسخه پایتون مورد نظر شماست، مثلاً `3` آخرین نسخه اصلی پایتون است.

حالا می‌توانید محیط Conda خود را با اجرای دستورات زیر در خط فرمان/ترمینال بسازید

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر با مشکلی مواجه شدید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

### استفاده از Visual Studio Code با افزونه پشتیبانی پایتون

توصیه می‌کنیم برای این دوره از [ویرایشگر Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) با [افزونه پشتیبانی پایتون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) استفاده کنید. البته این فقط یک توصیه است و الزام نیست.

> **Note**: با باز کردن مخزن دوره در VS Code، می‌توانید پروژه را داخل یک کانتینر راه‌اندازی کنید. این به خاطر پوشه [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) است که در مخزن دوره وجود دارد. بعداً بیشتر توضیح داده می‌شود.

> **Note**: وقتی مخزن را کلون و در VS Code باز کنید، به طور خودکار پیشنهاد نصب افزونه پشتیبانی پایتون را دریافت خواهید کرد.

> **Note**: اگر VS Code پیشنهاد داد مخزن را در کانتینر باز کنید، این درخواست را رد کنید تا از نسخه محلی پایتون استفاده کنید.

### استفاده از Jupyter در مرورگر

می‌توانید پروژه را با [محیط Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مستقیماً در مرورگر خود انجام دهید. هم Jupyter کلاسیک و هم [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) محیط توسعه خوبی با امکاناتی مثل تکمیل خودکار و برجسته‌سازی کد دارند.

برای شروع Jupyter به صورت محلی، به ترمینال/خط فرمان بروید، به پوشه دوره بروید و دستور زیر را اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این کار یک نمونه Jupyter را اجرا می‌کند و آدرس URL برای دسترسی به آن در پنجره خط فرمان نمایش داده می‌شود.

بعد از ورود به URL، باید ساختار دوره را ببینید و بتوانید به هر فایل `*.ipynb` بروید. مثلاً `08-building-search-applications/python/oai-solution.ipynb`.

### اجرا در کانتینر

یک راه جایگزین برای راه‌اندازی همه چیز روی کامپیوتر یا Codespace، استفاده از [کانتینر](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) است. پوشه خاص `.devcontainer` در مخزن دوره این امکان را می‌دهد که VS Code پروژه را داخل یک کانتینر راه‌اندازی کند. خارج از Codespaces، این کار نیاز به نصب Docker دارد و کمی پیچیده است، پس این روش را فقط به کسانی که با کانتینرها تجربه دارند توصیه می‌کنیم.

یکی از بهترین راه‌ها برای امن نگه داشتن کلیدهای API هنگام استفاده از GitHub Codespaces، استفاده از Codespace Secrets است. لطفاً راهنمای [مدیریت secrets در Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) را مطالعه کنید.

## درس‌ها و نیازمندی‌های فنی

این دوره شامل ۶ درس مفهومی و ۶ درس کدنویسی است.

برای درس‌های کدنویسی، از سرویس Azure OpenAI استفاده می‌کنیم. برای اجرای کدها باید به سرویس Azure OpenAI و یک کلید API دسترسی داشته باشید. می‌توانید با [تکمیل این فرم](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) درخواست دسترسی بدهید.

تا زمانی که درخواست شما بررسی شود، هر درس کدنویسی یک فایل `README.md` دارد که می‌توانید کد و خروجی‌ها را مشاهده کنید.

## استفاده از سرویس Azure OpenAI برای اولین بار

اگر اولین بار است که با سرویس Azure OpenAI کار می‌کنید، لطفاً راهنمای [ساخت و راه‌اندازی منبع Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) را دنبال کنید.

## استفاده از API OpenAI برای اولین بار

اگر اولین بار است که با API OpenAI کار می‌کنید، لطفاً راهنمای [ساخت و استفاده از رابط کاربری](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) را دنبال کنید.

## آشنایی با سایر یادگیرندگان

در سرور رسمی [دیسکورد جامعه هوش مصنوعی](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) کانال‌هایی برای آشنایی با سایر یادگیرندگان ساخته‌ایم. این راه خوبی برای شبکه‌سازی با کارآفرینان، سازندگان، دانشجویان و هر کسی است که می‌خواهد در هوش مصنوعی مولد پیشرفت کند.

[![به کانال دیسکورد بپیوندید](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

تیم پروژه نیز در این سرور دیسکورد حضور دارد تا به یادگیرندگان کمک کند.

## مشارکت

این دوره یک پروژه متن‌باز است. اگر جایی برای بهبود یا مشکلی دیدید، لطفاً یک [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بسازید یا یک [issue در گیت‌هاب](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ثبت کنید.

تیم پروژه همه مشارکت‌ها را دنبال می‌کند. مشارکت در متن‌باز راه فوق‌العاده‌ای برای ساختن مسیر حرفه‌ای در هوش مصنوعی مولد است.

بیشتر مشارکت‌ها نیاز به توافق‌نامه مجوز مشارکت‌کننده (CLA) دارند که اعلام می‌کند شما حق و اجازه استفاده از مشارکت خود را به ما می‌دهید. برای جزئیات بیشتر به [سایت CLA](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

مهم: هنگام ترجمه متن‌های این مخزن، لطفاً از ترجمه ماشینی استفاده نکنید. ترجمه‌ها توسط جامعه بررسی می‌شوند، پس فقط در زبان‌هایی داوطلب شوید که در آن‌ها مهارت دارید.

وقتی pull request ارسال کنید، یک ربات CLA به طور خودکار بررسی می‌کند که آیا باید CLA را ارائه دهید و PR را برچسب‌گذاری یا کامنت‌گذاری می‌کند. فقط کافی است دستورالعمل‌های ربات را دنبال کنید. این کار را فقط یک بار برای همه مخازن با CLA انجام می‌دهید.

این پروژه [قانون‌نامه متن‌باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) را پذیرفته است. برای اطلاعات بیشتر قانون‌نامه را بخوانید یا با [ایمیل opencode](opencode@microsoft.com) سوال یا نظر خود را مطرح کنید.

## بیایید شروع کنیم
حالا که مراحل لازم برای گذراندن این دوره را پشت سر گذاشته‌اید، بیایید با هم با [معرفی هوش مصنوعی مولد و مدل‌های زبانی بزرگ (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) شروع کنیم.

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادرستی باشند. نسخه اصلی سند به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.