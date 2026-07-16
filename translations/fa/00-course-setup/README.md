# شروع کار با این دوره

ما بسیار هیجان‌زده‌ایم که شما این دوره را شروع کنید و ببینید با هوش مصنوعی مولد چه چیزهایی می‌توانید بسازید!

برای اطمینان از موفقیت شما، این صفحه مراحل راه‌اندازی، نیازمندی‌های فنی و محل دریافت کمک در صورت نیاز را شرح می‌دهد.

## مراحل راه‌اندازی

برای شروع این دوره، باید مراحل زیر را تکمیل کنید.

### 1. فورک کردن این مخزن

[این مخزن کامل را فورک کنید](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) به حساب گیت‌هاب خودتان تا بتوانید هر کدی را تغییر دهید و چالش‌ها را کامل کنید. همچنین می‌توانید [با گرفتن ستاره (🌟) این مخزن](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) آن را و مخازن مرتبط راحت‌تر پیدا کنید.

### 2. ساخت یک کدسپیس

برای جلوگیری از هرگونه مشکل وابستگی هنگام اجرای کد، توصیه می‌کنیم این دوره را در [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) اجرا کنید.

در فورک خود: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/fa/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 افزودن یک راز (secret)

1. ⚙️ آیکون تنظیمات -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. نام OPENAI_API_KEY، کلید خود را جایگذاری کنید، ذخیره کنید.

### 3. بعدی چیست؟

| من می‌خواهم…          | بروم به…                                                              |
|---------------------|-------------------------------------------------------------------------|
| شروع درس 1          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| کار آفلاین         | [`setup-local.md`](02-setup-local.md)                                   |
| راه‌اندازی ارائه‌دهنده LLM | [`providers.md`](03-providers.md)                                        |
| ملاقات با دیگر یادگیرندگان | [به دیسکورد ما بپیوندید](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## رفع اشکال


| نشانه                                     | راه‌حل                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| گیر کردن ساخت کانتینر بیش از ۱۰ دقیقه    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | ترمینال متصل نشده؛ روی **+** کلیک کنید ➜ *bash*                     |
| `401 Unauthorized` از OpenAI              | `OPENAI_API_KEY` اشتباه یا منقضی شده                              |
| ویژوال کد نمایش می‌دهد “Dev container mounting…” | تب مرورگر را تازه کنید — گاهی Codespaces اتصال خود را از دست می‌دهد   |
| کرنل نوت‌بوک گم شده                      | منوی نوت‌بوک ➜ **Kernel ▸ انتخاب کرنل ▸ Python 3**                    |

   سیستم‌های مبتنی بر یونیکس:

   ```bash
   touch .env
   ```

   ویندوز:

   ```cmd
   echo . > .env
   ```

3. **ویرایش فایل `.env`**: فایل `.env` را در ویرایشگر متنی باز کنید (مثلاً VS Code، Notepad++ یا هر ویرایشگر دیگر). خطوط زیر را اضافه کنید، با جایگزینی متغیرهای جایگزین شده با نقطه پایان و کلید Microsoft Foundry Models خود (برای نحوه دریافت آنها به [`providers.md`](03-providers.md) مراجعه کنید):

   > **توضیح:** GitHub Models (و متغیر `GITHUB_TOKEN`) تا پایان جولای ۲۰۲۶ بازنشسته می‌شود. به جای آن از [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) استفاده کنید.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

۴. **ذخیره فایل**: تغییرات را ذخیره کرده و ویرایشگر متن را ببندید.

5. **نصب `python-dotenv`**: اگر قبلاً این کار را نکرده‌اید، باید پکیج `python-dotenv` را نصب کنید تا متغیرهای محیطی را از فایل `.env` در اپلیکیشن پایتون خود بارگذاری کنید. می‌توانید با دستور `pip` آن را نصب کنید:

   ```bash
   pip install python-dotenv
   ```

۶. **بارگذاری متغیرهای محیطی در اسکریپت پایتون**: در اسکریپت پایتون خود از پکیج `python-dotenv` برای بارگذاری متغیرهای محیطی از فایل `.env` استفاده کنید:

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

تمام شد! شما با موفقیت فایل `.env` را ایجاد کرده، مجوزهای Microsoft Foundry Models را اضافه و آنها را در اپلیکیشن پایتون خود بارگذاری کرده‌اید.

## نحوه اجرای محلی روی کامپیوتر خودتان

برای اجرای کد روی کامپیوتر خود، باید یک نسخه از [پایتون نصب شده داشته باشید](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

سپس برای استفاده از مخزن، باید آن را کلون کنید:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

پس از بررسی همه چیز، می‌توانید شروع کنید!

## مراحل اختیاری

### نصب Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و چند بسته است.
خود Conda یک مدیر بسته است که راه‌اندازی و تغییر بین [محیط‌های مجازی](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) پایتون و بسته‌ها را آسان می‌کند. همچنین برای نصب بسته‌های غیر قابل دسترس از طریق `pip` مفید است.

می‌توانید از [راهنمای نصب MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) برای نصب استفاده کنید.

بعد از نصب Miniconda، باید مخزن را کلون کنید (اگر قبلاً نکرده‌اید) [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst).

سپس باید یک محیط مجازی ایجاد کنید. برای این کار با Conda، یک فایل محیط جدید (_environment.yml_) بسازید. اگر با Codespaces همراه هستید، این را در دایرکتوری `.devcontainer` ایجاد کنید، یعنی `.devcontainer/environment.yml`.

محتویات نمونه را در فایل محیط خود قرار دهید:

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

اگر هنگام استفاده از conda خطا دریافت کردید، می‌توانید کتابخانه‌های AI مایکروسافت را دستی با دستور زیر در ترمینال نصب کنید.

```
conda install -c microsoft azure-ai-ml
```

فایل محیط وابستگی‌هایی که نیاز داریم را مشخص می‌کند. `<environment-name>` نام دلخواه محیط Conda و `<python-version>` نسخه پایتون مورد نظر است، برای مثال، `3` آخرین نسخه اصلی پایتون است.

پس از آن می‌توانید محیط Conda خود را با اجرای دستورات زیر در خط فرمان یا ترمینال ایجاد کنید:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # مسیر فرعی .devcontainer فقط برای تنظیمات Codespace اعمال می‌شود
conda activate ai4beg
```

اگر مشکلی داشتید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

### استفاده از Visual Studio Code به همراه افزونه پایتون

توصیه می‌شود از [ویرایشگر Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) به همراه [افزونه پشتیبانی پایتون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) برای این دوره استفاده کنید. این تنها یک توصیه است و الزام قطعی نیست.

> **تذکر:** با باز کردن مخزن دوره در VS Code، گزینه راه‌اندازی پروژه در یک کانتینر وجود دارد. دلیل آن وجود دایرکتوری ویژه [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) در مخزن است. بعداً بیشتر توضیح داده می‌شود.

> **تذکر:** پس از کلون و باز کردن دایرکتوری در VS Code، به صورت خودکار افزونه پشتیبانی پایتون را نصب پیشنهاد می‌کند.

> **تذکر:** اگر VS Code پیشنهاد داد مخزن را دوباره در یک کانتینر باز کنید، درخواست را رد کنید تا از نسخه محلی پایتون استفاده کنید.

### استفاده از Jupyter در مرورگر

همچنین می‌توانید پروژه را با استفاده از محیط [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) در مرورگر خود کار کنید. هم Jupyter کلاسیک و هم [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) محیط توسعه خوبی با امکاناتی مانند تکمیل خودکار، برجسته‌سازی کد و غیره ارائه می‌دهند.

برای شروع Jupyter به صورت محلی، وارد ترمینال/خط فرمان شده، به دایرکتوری دوره بروید و اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این یک نمونه Jupyter را راه‌اندازی کرده و URL دسترسی آن در پنجره خط فرمان نشان داده می‌شود.

پس از دسترسی به URL، باید طرح کلی دوره را ببینید و بتوانید به هر فایل `*.ipynb` هدایت شوید. مثلاً `08-building-search-applications/python/oai-solution.ipynb`.

### اجرای داخل کانتینر

جایگزین راه‌اندازی همه چیز روی کامپیوتر یا Codespace استفاده از [کانتینر](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) است. دایرکتوری ویژه `.devcontainer` داخل مخزن امکان راه‌اندازی پروژه داخل کانتینر را برای VS Code فراهم می‌کند. خارج از Codespaces، نیاز به نصب Docker دارد و نسبتاً کمی کار بر است، بنابراین این روش فقط برای افرادی که تجربه کار با کانتینرها دارند توصیه می‌شود.

یکی از بهترین روش‌ها برای حفظ امنیت کلیدهای API در GitHub Codespaces، استفاده از Secrets کدسپیس است. لطفاً برای اطلاعات بیشتر راهنمای [مدیریت رازهای Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) را دنبال کنید.


## درس‌ها و نیازمندی‌های فنی

این دوره شامل ۶ درس مفهومی و ۶ درس کدنویسی است.

برای درس‌های کدنویسی، ما از سرویس Azure OpenAI استفاده می‌کنیم. برای اجرای این کد به سرویس Azure OpenAI و کلید API نیاز دارید. می‌توانید با [پر کردن این درخواست](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) به آن دسترسی پیدا کنید.

در حالی که منتظر پردازش درخواست خود هستید، هر درس کدنویسی همچنین شامل یک فایل `README.md` است که می‌توانید کد و خروجی‌ها را مشاهده کنید.

## استفاده اولیه از سرویس Azure OpenAI

اگر برای اولین بار با سرویس Azure OpenAI کار می‌کنید، لطفاً این راهنما را برای [ایجاد و استقرار منبع سرویس Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## استفاده اولیه از API OpenAI

اگر برای اولین بار با API OpenAI کار می‌کنید، لطفاً راهنما را درباره [ایجاد و استفاده از رابط کاربری](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## ملاقات با دیگر یادگیرندگان

ما در سرور رسمی دیسکورد [AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) کانال‌هایی برای ملاقات با دیگر یادگیرندگان ایجاد کرده‌ایم. این روش عالی برای شبکه‌سازی با دیگر کارآفرینان، سازندگان، دانشجویان و هر کسی است که می‌خواهد در هوش مصنوعی مولد پیشرفت کند.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

تیم پروژه نیز در این سرور دیسکورد حضور دارد تا به یادگیرندگان کمک کند.

## مشارکت

این دوره یک پروژه متن‌باز است. اگر نقاط بهبود یا مشکلاتی دیدید، لطفاً یک [درخواست کشش (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ایجاد کنید یا یک [مسئله GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ثبت نمایید.

تیم پروژه همه مشارکت‌ها را پیگیری خواهد کرد. مشارکت در متن‌باز راهی عالی برای ساختن حرفه خود در هوش مصنوعی مولد است.

بیشتر مشارکت‌ها نیازمند موافقت با قرارداد مجوز مشارکت‌کننده (CLA) است که اعلام می‌کند شما حق دارید و واقعاً این حقوق را به ما اعطا می‌کنید تا از مشارکت شما استفاده کنیم. برای جزئیات به وب‌سایت [CLA، قرارداد مجوز مشارکت‌کننده](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

مهم: هنگام ترجمه متن در این مخزن، لطفاً از ترجمه ماشینی استفاده نکنید. ما ترجمه‌ها را از طریق جامعه بررسی خواهیم کرد، بنابراین لطفاً فقط در زبان‌هایی که تخصص دارید برای ترجمه داوطلب شوید.

هنگام ارسال درخواست کشش، یک ربات CLA-bot به‌طور خودکار تعیین می‌کند که آیا نیاز به ارائه CLA دارید و درخواست را به نحوی مناسب علامت‌گذاری می‌کند (مثلاً برچسب، نظر). فقط کافی است دستورالعمل‌های ارائه ‌شده توسط ربات را دنبال کنید. این تنها یک بار در همه مخازنی که از CLA ما استفاده می‌کنند لازم است.


این پروژه، [کد رفتاری منبع‌باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) را پذیرفته است. برای اطلاعات بیشتر، به سوالات متداول کد رفتار مراجعه کنید یا با [ایمیل opencode](opencode@microsoft.com) تماس بگیرید تا سوالات یا نظرات اضافی خود را مطرح کنید.

## بیایید شروع کنیم

اکنون که مراحل لازم برای تکمیل این دوره را پشت سر گذاشتید، بیایید با یک [معرفی به هوش مصنوعی تولیدی و مدل‌های زبانی بزرگ](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) شروع کنیم.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->