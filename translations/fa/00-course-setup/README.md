<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:36:46+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fa"
}
-->
# شروع به کار با این دوره

ما بسیار هیجان‌زده‌ایم که شما این دوره را آغاز کنید و ببینید چه چیزی شما را برای ساختن با هوش مصنوعی مولد الهام می‌بخشد!

برای اطمینان از موفقیت شما، این صفحه مراحل راه‌اندازی، نیازهای فنی و محلی برای دریافت کمک در صورت نیاز را توضیح می‌دهد.

## مراحل راه‌اندازی

برای شروع این دوره، باید مراحل زیر را تکمیل کنید.

### 1. این مخزن را فورک کنید

[این مخزن را فورک کنید](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) تا بتوانید هر کدی را در حساب GitHub خود تغییر دهید و چالش‌ها را تکمیل کنید. همچنین می‌توانید [این مخزن را ستاره‌دار کنید (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تا آن و مخازن مرتبط را راحت‌تر پیدا کنید.

### 2. ایجاد یک Codespace

برای جلوگیری از هر گونه مشکل وابستگی هنگام اجرای کد، توصیه می‌کنیم این دوره را در یک [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) اجرا کنید.

این کار با انتخاب گزینه `Code` در نسخه فورک شده شما از این مخزن و انتخاب گزینه **Codespaces** قابل انجام است.

![دیالوگ نشان‌دهنده دکمه‌هایی برای ایجاد یک codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. ذخیره کلیدهای API شما

حفظ امنیت و ایمنی کلیدهای API شما هنگام ساخت هر نوع برنامه‌ای مهم است. توصیه می‌کنیم هیچ کلید API را مستقیماً در کد خود ذخیره نکنید. وارد کردن این جزئیات در یک مخزن عمومی می‌تواند منجر به مشکلات امنیتی و حتی هزینه‌های ناخواسته شود اگر توسط یک فرد بد استفاده شود.
در اینجا یک راهنمای گام به گام در مورد چگونگی ایجاد یک فایل `.env` برای پایتون و افزودن `GITHUB_TOKEN` آمده است:

1. **به دایرکتوری پروژه خود بروید**: ترمینال یا کامند پرامپت خود را باز کنید و به دایرکتوری ریشه پروژه خود بروید، جایی که می‌خواهید فایل `.env` را ایجاد کنید.

   ```bash
   cd path/to/your/project
   ```

2. **ایجاد فایل `.env`**: از ویرایشگر متن مورد نظر خود برای ایجاد یک فایل جدید به نام `.env` استفاده کنید. اگر از خط فرمان استفاده می‌کنید، می‌توانید از `touch` (on Unix-based systems) or `echo` (در ویندوز) استفاده کنید:

   سیستم‌های مبتنی بر یونیکس:
   ```bash
   touch .env
   ```

   ویندوز:
   ```cmd
   echo . > .env
   ```

3. **ویرایش فایل `.env`**: فایل `.env` را در یک ویرایشگر متن باز کنید (مثلاً VS Code، Notepad++ یا هر ویرایشگر دیگری). خط زیر را به فایل اضافه کنید و `your_github_token_here` را با توکن واقعی GitHub خود جایگزین کنید:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ذخیره فایل**: تغییرات را ذخیره کنید و ویرایشگر متن را ببندید.

5. **نصب بسته `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` برای بارگذاری متغیرهای محیطی از فایل `.env` به برنامه پایتون خود. می‌توانید با استفاده از `pip` آن را نصب کنید:

   ```bash
   pip install python-dotenv
   ```

6. **بارگذاری متغیرهای محیطی در اسکریپت پایتون خود**: در اسکریپت پایتون خود، از بسته `python-dotenv` برای بارگذاری متغیرهای محیطی از فایل `.env` استفاده کنید:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

همین است! شما با موفقیت یک فایل `.env` ایجاد کرده‌اید، توکن GitHub خود را اضافه کرده‌اید و آن را به برنامه پایتون خود بارگذاری کرده‌اید.

## چگونه به صورت محلی بر روی کامپیوتر خود اجرا کنید

برای اجرای کد به صورت محلی بر روی کامپیوتر خود، باید نسخه‌ای از [پایتون نصب شده](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) داشته باشید.

سپس برای استفاده از مخزن، باید آن را کلون کنید:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

وقتی همه چیز را چک کردید، می‌توانید شروع کنید!

## مراحل اختیاری

### نصب Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و چند بسته دیگر است.
Conda خودش یک مدیر بسته است که راه‌اندازی و جابجایی بین [محیط‌های مجازی](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) مختلف پایتون و بسته‌ها را آسان می‌کند. همچنین برای نصب بسته‌هایی که از طریق `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` در دسترس نیستند، مفید است.

پیش بروید و فایل محیط خود را با قطعه زیر پر کنید:

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

اگر هنگام استفاده از conda خطاهایی دریافت می‌کنید، می‌توانید کتابخانه‌های AI مایکروسافت را با استفاده از دستور زیر در ترمینال به صورت دستی نصب کنید.

```
conda install -c microsoft azure-ai-ml
```

فایل محیط وابستگی‌هایی که نیاز داریم را مشخص می‌کند. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` آخرین نسخه اصلی پایتون است.

با انجام این کار، می‌توانید محیط Conda خود را با اجرای دستورات زیر در خط فرمان/ترمینال خود ایجاد کنید

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر با مشکلی مواجه شدید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

### استفاده از Visual Studio Code با افزونه پشتیبانی پایتون

ما توصیه می‌کنیم از ویرایشگر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) با افزونه پشتیبانی پایتون [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) برای این دوره استفاده کنید. این، با این حال، بیشتر یک توصیه است و نه یک الزام قطعی.

> **توجه**: با باز کردن مخزن دوره در VS Code، شما گزینه‌ای دارید که پروژه را درون یک کانتینر راه‌اندازی کنید. این به دلیل دایرکتوری [ویژه `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) موجود در مخزن دوره است. بیشتر در این باره بعداً.

> **توجه**: وقتی دایرکتوری را در VS Code کلون و باز می‌کنید، به طور خودکار به شما پیشنهاد می‌شود که یک افزونه پشتیبانی پایتون نصب کنید.

> **توجه**: اگر VS Code به شما پیشنهاد می‌دهد که مخزن را در یک کانتینر دوباره باز کنید، این درخواست را رد کنید تا از نسخه نصب شده محلی پایتون استفاده کنید.

### استفاده از Jupyter در مرورگر

شما همچنین می‌توانید با استفاده از محیط [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) به صورت مستقیم در مرورگر خود بر روی پروژه کار کنید. هر دو Jupyter کلاسیک و [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) محیط توسعه بسیار مناسبی با ویژگی‌هایی مانند تکمیل خودکار، برجسته‌سازی کد و غیره فراهم می‌کنند.

برای شروع Jupyter به صورت محلی، به ترمینال/خط فرمان بروید، به دایرکتوری دوره بروید و اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این یک نمونه Jupyter را شروع می‌کند و URL برای دسترسی به آن در پنجره خط فرمان نمایش داده خواهد شد.

وقتی به URL دسترسی پیدا کردید، باید طرح دوره را ببینید و بتوانید به هر فایل `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` بروید که در آن می‌توانید کد و خروجی‌ها را مشاهده کنید.

## استفاده از سرویس Azure OpenAI برای اولین بار

اگر این اولین باری است که با سرویس Azure OpenAI کار می‌کنید، لطفاً این راهنما را برای [ایجاد و استقرار یک منبع سرویس Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## استفاده از API OpenAI برای اولین بار

اگر این اولین باری است که با API OpenAI کار می‌کنید، لطفاً راهنما را برای [ایجاد و استفاده از رابط کاربری](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## ملاقات با دیگر یادگیرندگان

ما کانال‌هایی در سرور رسمی Discord جامعه AI خود ایجاد کرده‌ایم برای ملاقات با دیگر یادگیرندگان. این یک راه عالی برای شبکه‌سازی با دیگر کارآفرینان، سازندگان، دانشجویان و هر کسی است که به دنبال ارتقاء در هوش مصنوعی مولد است.

[![پیوستن به کانال دیسکورد](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

تیم پروژه نیز در این سرور Discord خواهد بود تا به هر یادگیرنده‌ای کمک کند.

## مشارکت

این دوره یک ابتکار منبع باز است. اگر مناطق بهبود یا مشکلاتی را مشاهده کردید، لطفاً یک [درخواست کشش](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ایجاد کنید یا یک [مشکل GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) را ثبت کنید.

تیم پروژه تمام مشارکت‌ها را دنبال خواهد کرد. مشارکت در منبع باز یک راه شگفت‌انگیز برای ساختن کارنامه خود در هوش مصنوعی مولد است.

بیشتر مشارکت‌ها نیاز به توافق‌نامه مجوز مشارکت‌کننده (CLA) دارند که اعلام می‌کند شما حق دارید و در واقع به ما حقوق استفاده از مشارکت شما را می‌دهید. برای جزئیات، به [وب‌سایت CLA، توافق‌نامه مجوز مشارکت‌کننده](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

مهم: هنگام ترجمه متن در این مخزن، لطفاً اطمینان حاصل کنید که از ترجمه ماشینی استفاده نمی‌کنید. ما ترجمه‌ها را از طریق جامعه تأیید خواهیم کرد، بنابراین لطفاً فقط برای ترجمه‌ها در زبان‌هایی که در آن‌ها مهارت دارید داوطلب شوید.

وقتی یک درخواست کشش ارسال می‌کنید، یک ربات CLA به طور خودکار تعیین می‌کند که آیا نیاز به ارائه CLA دارید و درخواست را به طور مناسب تزئین می‌کند (به عنوان مثال، برچسب، نظر). به سادگی دستورالعمل‌های ارائه شده توسط ربات را دنبال کنید. شما فقط باید این کار را یک بار در تمام مخازنی که از CLA ما استفاده می‌کنند انجام دهید.

این پروژه [کد رفتار منبع باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) را پذیرفته است. برای اطلاعات بیشتر، پرسش‌های متداول کد رفتار را بخوانید یا با [ایمیل opencode](opencode@microsoft.com) با هر سؤال یا نظری اضافی تماس بگیرید.

## بیایید شروع کنیم

اکنون که مراحل لازم برای تکمیل این دوره را انجام داده‌اید، بیایید با گرفتن [مقدمه‌ای بر هوش مصنوعی مولد و LLMها](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) شروع کنیم.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.