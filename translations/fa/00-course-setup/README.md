# شروع کار با این دوره

ما بسیار هیجان‌زده هستیم که شما این دوره را شروع کنید و ببینید که با هوش مصنوعی مولد چه چیزهایی می‌خواهید بسازید!

برای اطمینان از موفقیت شما، این صفحه مراحل راه‌اندازی، نیازهای فنی و محل دریافت کمک در صورت نیاز را بیان می‌کند.

## مراحل راه‌اندازی

برای شروع این دوره، باید مراحل زیر را کامل کنید.

### 1. فورک کردن این مخزن

[کل این مخزن را فورک کنید](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) به حساب کاربری GitHub خودتان تا بتوانید هر کد را تغییر دهید و چالش‌ها را کامل کنید. همچنین می‌توانید این مخزن را [ستاره (🌟) بدهید](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تا پیدا کردن آن و مخازن مرتبط راحت‌تر باشد.

### 2. ساخت یک کداسپیس

برای جلوگیری از هرگونه مشکل وابستگی هنگام اجرای کد، توصیه می‌کنیم این دوره را در [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) اجرا کنید.

در فورک شما: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/fa/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 اضافه کردن یک راز

1. ⚙️ آیکون چرخ‌دنده -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. نام را OPENAI_API_KEY بگذارید، کلید خود را الصاق کنید، ذخیره کنید.

### 3. بعدی چیست؟

| من می‌خواهم…          | بروم به…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| شروع درس 1           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| کار به صورت آفلاین  | [`setup-local.md`](02-setup-local.md)                                   |
| راه‌اندازی ارائه‌دهنده LLM | [`providers.md`](03-providers.md)                                        |
| دیدار با سایر یادگیرندگان | [عضویت در Discord ما](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## رفع اشکال


| نشانه                                    | راه‌حل                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| ساخت کانتینر بیش از ۱۰ دقیقه طول کشید      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | ترمینال وصل نشده؛ روی **+** کلیک کنید ➜ *bash*                    |
| `401 Unauthorized` از OpenAI              | کلید `OPENAI_API_KEY` اشتباه یا منقضی شده                         |
| VS Code نمایش می‌دهد “Dev container mounting…” | تب مرورگر را رفرش کنید— گاهی اتصال Codespaces قطع می‌شود          |
| کرنل نوت‌بوک گم شده                      | منوی نوت‌بوک ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   سیستم‌های مبتنی بر یونیکس:

   ```bash
   touch .env
   ```

   ویندوز:

   ```cmd
   echo . > .env
   ```

3. **فایل `.env` را ویرایش کنید**: فایل `.env` را در ویرایشگر متن باز کنید (مثلاً VS Code، Notepad++ یا هر ویرایشگر دیگری). خطوط زیر را اضافه کنید و مقادیر واقعی نقطه انتهایی و کلید Microsoft Foundry Models خود را جایگزین کلیدهای نگهدارنده کنید (برای اطلاعات بیشتر به [`providers.md`](03-providers.md) مراجعه کنید):

   > **توجه:** مدل‌های GitHub (و متغیر `GITHUB_TOKEN` مربوطه) تا پایان جولای ۲۰۲۶ بازنشسته می‌شوند. به جای آن از [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) استفاده کنید.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **فایل را ذخیره کنید**: تغییرات را ذخیره کرده و ویرایشگر متن را ببندید.

5. **نصب `python-dotenv`**: اگر هنوز نصب نکرده‌اید، باید بسته `python-dotenv` را نصب کنید تا متغیرهای محیطی از فایل `.env` در برنامه پایتون شما بارگذاری شود. می‌توانید با `pip` آن را نصب کنید:

   ```bash
   pip install python-dotenv
   ```

6. **بارگذاری متغیرهای محیطی در اسکریپت پایتون شما**: در اسکریپت پایتون خود از بسته `python-dotenv` برای بارگذاری متغیرهای محیطی فایل `.env` استفاده کنید:

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

تمام شد! شما با موفقیت یک فایل `.env` ایجاد کرده، اطلاعات Microsoft Foundry Models خود را اضافه کرده و آنها را در برنامه پایتون خود بارگذاری کرده‌اید.

## چگونه به صورت محلی روی کامپیوتر خود اجرا کنیم

برای اجرای کد به صورت محلی روی کامپیوترتان، باید نسخه‌ای از [پایتون نصب شده](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) داشته باشید.

سپس برای استفاده از مخزن، باید آن را کلون کنید:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

پس از اینکه همه چیز را دریافت کردید، می‌توانید شروع کنید!

## مراحل اختیاری

### نصب Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و چند بسته است.
خود Conda یک مدیر بسته است که تنظیم و جابجایی بین محیط‌های مجازی پایتون و بسته‌ها را آسان می‌کند. همچنین برای نصب بسته‌هایی که با `pip` در دسترس نیستند، مفید است.

می‌توانید با دنبال کردن [راهنمای نصب MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) آن را راه‌اندازی کنید.

پس از نصب Miniconda، باید [مخزن](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) را کلون کنید (اگر قبلاً کلون نکردید)

سپس باید یک محیط مجازی بسازید. برای این کار با Conda، یک فایل محیط جدید (_environment.yml_) بسازید. اگر در Codespaces همراهی می‌کنید، این فایل را در پوشه `.devcontainer` بسازید، یعنی `.devcontainer/environment.yml`.

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

اگر هنگام استفاده از conda خطا دریافت می‌کنید، می‌توانید به صورت دستی کتابخانه‌های Microsoft AI را با دستور زیر در ترمینال نصب کنید.

```
conda install -c microsoft azure-ai-ml
```

فایل محیط وابستگی‌هایی را که نیاز داریم مشخص می‌کند. `<environment-name>` نام محیط Conda شما و `<python-version>` نسخه پایتونی است که می‌خواهید استفاده کنید، مثلاً `3` جدیدترین نسخه اصلی پایتون است.

پس از آن، می‌توانید محیط Conda خود را با اجرای دستورات زیر در خط فرمان/ترمینال بسازید

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # مسیر فرعی .devcontainer فقط برای تنظیمات Codespace اعمال می‌شود
conda activate ai4beg
```

اگر مشکلی داشتید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

### استفاده از Visual Studio Code با افزونه پشتیبانی پایتون

توصیه می‌کنیم از ویرایشگر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) همراه با [افزونه پشتیبانی پایتون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) برای این دوره استفاده کنید. با این حال، این فقط یک توصیه است و الزام قطعی نیست.

> **توجه**: با باز کردن مخزن دوره در VS Code، می‌توانید پروژه را داخل یک کانتینر راه‌اندازی کنید. این به خاطر پوشه خاص [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) داخل مخزن دوره است. بعداً بیشتر در مورد آن توضیح می‌دهیم.

> **توجه**: پس از کلون و باز کردن دایرکتوری در VS Code، به صورت خودکار نصب افزونه پشتیبانی پایتون را پیشنهاد می‌دهد.

> **توجه**: اگر VS Code پیشنهاد داد مخزن را دوباره در یک کانتینر باز کنید، این درخواست را رد کنید تا از نسخه محلی پایتون استفاده کنید.

### استفاده از Jupyter در مرورگر

همچنین می‌توانید پروژه را با استفاده از محیط [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مستقیم در مرورگر اجرا کنید. هم Jupyter کلاسیک و هم [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) محیط توسعه دلچسبی با ویژگی‌های تکمیل خودکار، برجسته‌سازی کد و ... ارائه می‌دهند.

برای شروع Jupyter به صورت محلی، به ترمینال/خط فرمان بروید، به دایرکتوری دوره بروید و فرمان زیر را اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این یک نمونه Jupyter راه‌اندازی می‌کند و URL دسترسی را در پنجره خط فرمان نشان می‌دهد.

وقتی URL را باز کنید، باید طرح کلی دوره را ببینید و بتوانید به هر فایل `*.ipynb` ناوبری کنید. مثلاً `08-building-search-applications/python/oai-solution.ipynb`.

### اجرای داخل کانتینر

راه دیگر راه‌اندازی همه چیز روی کامپیوتر یا Codespace استفاده از [کانتینر](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) است. پوشه خاص `.devcontainer` در مخزن دوره امکان راه‌اندازی پروژه داخل کانتینر توسط VS Code را فراهم می‌کند. خارج از Codespaces، این نیاز به نصب Docker دارد و کمی کار می‌برد، پس فقط به کسانی که تجربه کار با کانتینر دارند توصیه می‌شود.

یکی از بهترین روش‌ها برای امن نگه داشتن کلیدهای API هنگام استفاده از GitHub Codespaces، استفاده از رازهای Codespace است. لطفاً راهنمای [مدیریت رازهای Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) را دنبال کنید.


## درس‌ها و نیازهای فنی

دوره دارای درس‌های "یادگیری" است که مفاهیم هوش مصنوعی مولد را توضیح می‌دهد و درس‌های "ساخت" با مثال‌های کدنویسی عملی در هر دو زبان **Python** و **TypeScript** در صورت امکان.

برای درس‌های برنامه‌نویسی از Azure OpenAI در Microsoft Foundry استفاده می‌کنیم. شما نیاز به اشتراک Azure و کلید API دارید. دسترسی آزاد است - نیازی به درخواست ندارد - بنابراین می‌توانید [یک منبع Microsoft Foundry ایجاد کرده و مدل را مستقر کنید](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) و نقطه انتهایی و کلید خود را دریافت کنید.

هر درس برنامه‌نویسی همچنین یک فایل `README.md` دارد که می‌توانید کد و خروجی‌ها را بدون اجرای چیزی مشاهده کنید.

## اولین بار استفاده از سرویس Azure OpenAI

اگر این اولین بار است که با سرویس Azure OpenAI کار می‌کنید، لطفاً این راهنما را برای [ایجاد و استقرار یک منبع Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## اولین بار استفاده از API OpenAI

اگر اولین بار است که با API OpenAI کار می‌کنید، لطفاً راهنمای [ایجاد و استفاده از رابط کاربری](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) را دنبال کنید.

## دیدار با سایر یادگیرندگان

ما کانال‌هایی در سرور رسمی [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) ایجاد کرده‌ایم تا با سایر یادگیرندگان ملاقات کنید. این روش خوبی برای شبکه‌سازی با دیگر کارآفرینان، سازندگان، دانشجویان و هر کسی است که می‌خواهد در حوزه هوش مصنوعی مولد پیشرفت کند.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

تیم پروژه نیز در این سرور Discord حضور خواهد داشت تا به هر یادگیرنده‌ای کمک کند.

## مشارکت

این دوره یک پروژه متن‌باز است. اگر بهبود یا مشکلی دیدید، لطفاً یک [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ایجاد یا یک [issue در GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) گزارش کنید.

تیم پروژه تمام مشارکت‌ها را دنبال خواهد کرد. مشارکت در متن‌باز راه شگفت‌انگیزی برای ساختن حرفه شما در هوش مصنوعی مولد است.

اکثر مشارکت‌ها مستلزم توافق با قرارداد مجوز مشارکت‌کننده (CLA) است که شما حق دارید و واقعاً به ما حقوق استفاده از مشارکتتان را می‌دهید. برای اطلاعات بیشتر به وب‌سایت [CLA، قرارداد مجوز مشارکت‌کننده](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

مهم: هنگام ترجمه متن در این مخزن، لطفاً مطمئن شوید که از ترجمه ماشینی استفاده نمی‌کنید. ما ترجمه‌ها را توسط جامعه بررسی می‌کنیم، بنابراین فقط برای زبان‌هایی که مسلط هستید داوطلب ترجمه شوید.


وقتی یک درخواست کشش ارسال می‌کنید، ربات CLA به‌طور خودکار تعیین می‌کند که آیا نیاز به ارائه CLA دارید و PR را به‌طور مناسب تزیین می‌کند (مثلاً برچسب، نظر). به سادگی دستورالعمل‌های ارائه شده توسط ربات را دنبال کنید. شما فقط یکبار در تمام مخازنی که از CLA ما استفاده می‌کنند، باید این کار را انجام دهید.

این پروژه [کد رفتار منبع باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) را پذیرفته است. برای اطلاعات بیشتر، به پرسش‌های متداول کد رفتار مراجعه کنید یا با [ایمیل opencode](opencode@microsoft.com) برای سوالات یا نظرات اضافی تماس بگیرید.

## بیایید شروع کنیم

اکنون که مراحل لازم برای تکمیل این دوره را طی کرده‌اید، بیایید با [معرفی به هوش مصنوعی مولد و LLMها](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) شروع کنیم.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->