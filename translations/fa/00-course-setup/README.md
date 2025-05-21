<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:17:59+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fa"
}
-->
# شروع به کار با این دوره

ما بسیار هیجان‌زده‌ایم که شما این دوره را آغاز کنید و ببینید با هوش مصنوعی تولیدی چه چیزهایی می‌توانید بسازید!

برای اطمینان از موفقیت شما، این صفحه مراحل راه‌اندازی، الزامات فنی و جایی که در صورت نیاز می‌توانید کمک بگیرید را توضیح می‌دهد.

## مراحل راه‌اندازی

برای شروع این دوره، باید مراحل زیر را کامل کنید.

### 1. Fork این مخزن

[Fork کردن کل این مخزن](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) به حساب GitHub خودتان تا بتوانید هر کدی را تغییر دهید و چالش‌ها را کامل کنید. همچنین می‌توانید [ستاره‌دار کردن (🌟) این مخزن](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) را انجام دهید تا آن و مخازن مرتبط را راحت‌تر پیدا کنید.

### 2. ایجاد یک Codespace

برای جلوگیری از مشکلات وابستگی هنگام اجرای کد، توصیه می‌کنیم این دوره را در [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) اجرا کنید.

این می‌تواند با انتخاب گزینه `Code` در نسخه Fork شده این مخزن و انتخاب گزینه **Codespaces** ایجاد شود.

![دیالوگ نمایش دکمه‌ها برای ایجاد Codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. ذخیره کلیدهای API شما

نگه‌داری کلیدهای API شما ایمن و امن هنگام ساخت هر نوع برنامه‌ای مهم است. توصیه می‌کنیم کلیدهای API را مستقیماً در کد خود ذخیره نکنید. ارائه این جزئیات به یک مخزن عمومی می‌تواند منجر به مشکلات امنیتی و حتی هزینه‌های ناخواسته شود اگر توسط یک عامل بد استفاده شود.
در اینجا یک راهنمای مرحله به مرحله برای ایجاد یک فایل `.env` برای پایتون و افزودن `GITHUB_TOKEN` آورده شده است:

1. **پیمایش به دایرکتوری پروژه شما**: ترمینال یا خط فرمان خود را باز کنید و به دایرکتوری ریشه پروژه خود که می‌خواهید فایل `.env` را ایجاد کنید، بروید.

   ```bash
   cd path/to/your/project
   ```

2. **ایجاد فایل `.env`**: از ویرایشگر متن مورد نظر خود برای ایجاد یک فایل جدید با نام `.env` استفاده کنید. اگر از خط فرمان استفاده می‌کنید، می‌توانید از `touch` (on Unix-based systems) or `echo` (در ویندوز) استفاده کنید:

   سیستم‌های مبتنی بر یونیکس:
   ```bash
   touch .env
   ```

   ویندوز:
   ```cmd
   echo . > .env
   ```

3. **ویرایش فایل `.env`**: فایل `.env` را در یک ویرایشگر متن (مانند VS Code، Notepad++ یا هر ویرایشگر دیگر) باز کنید. خط زیر را به فایل اضافه کنید و `your_github_token_here` را با توکن واقعی GitHub خود جایگزین کنید:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ذخیره فایل**: تغییرات را ذخیره کنید و ویرایشگر متن را ببندید.

5. **نصب بسته `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` برای بارگذاری متغیرهای محیطی از فایل `.env` به برنامه پایتون خود. می‌توانید آن را با استفاده از `pip` نصب کنید:

   ```bash
   pip install python-dotenv
   ```

6. **بارگذاری متغیرهای محیطی در اسکریپت پایتون شما**: در اسکریپت پایتون خود، از بسته `python-dotenv` برای بارگذاری متغیرهای محیطی از فایل `.env` استفاده کنید:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

همین! شما با موفقیت یک فایل `.env` ایجاد کرده‌اید، توکن GitHub خود را اضافه کرده‌اید و آن را به برنامه پایتون خود بارگذاری کرده‌اید.

## چگونه محلی روی کامپیوتر خود اجرا کنید

برای اجرای کد به صورت محلی روی کامپیوتر خود، باید نسخه‌ای از [پایتون نصب شده](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) داشته باشید.

سپس برای استفاده از مخزن، باید آن را کلون کنید:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

وقتی همه چیز را بررسی کردید، می‌توانید شروع کنید!

## مراحل اختیاری 

### نصب Miniconda 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و همچنین چند بسته است.
خود Conda یک مدیر بسته است که تنظیم و تغییر بین محیط‌های [**مجازی پایتون**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) و بسته‌ها را آسان می‌کند. همچنین برای نصب بسته‌هایی که از طریق `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` در دسترس نیستند، مفید است.

پیش بروید و فایل محیط خود را با کد زیر پر کنید:

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

اگر متوجه شدید که هنگام استفاده از conda دچار خطا می‌شوید، می‌توانید کتابخانه‌های AI مایکروسافت را با استفاده از فرمان زیر در ترمینال به صورت دستی نصب کنید.

```
conda install -c microsoft azure-ai-ml
```

فایل محیط وابستگی‌هایی را که نیاز داریم مشخص می‌کند. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` آخرین نسخه اصلی پایتون است.

با انجام این کار، می‌توانید محیط Conda خود را با اجرای فرمان‌های زیر در خط فرمان/ترمینال خود ایجاد کنید

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر به مشکلی برخورد کردید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

### استفاده از Visual Studio Code با افزونه پشتیبانی پایتون

ما توصیه می‌کنیم از ویرایشگر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) با افزونه [پشتیبانی پایتون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) نصب شده برای این دوره استفاده کنید. این البته بیشتر یک توصیه است و نه یک الزام قطعی

> **توجه**: با باز کردن مخزن دوره در VS Code، گزینه‌ای برای تنظیم پروژه درون یک کانتینر دارید. این به دلیل دایرکتوری [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) موجود در مخزن دوره است. بیشتر در این مورد بعداً.

> **توجه**: هنگامی که دایرکتوری را کلون کرده و در VS Code باز می‌کنید، به طور خودکار پیشنهاد می‌دهد که یک افزونه پشتیبانی پایتون نصب کنید.

> **توجه**: اگر VS Code پیشنهاد می‌دهد مخزن را در یک کانتینر دوباره باز کنید، این درخواست را رد کنید تا از نسخه محلی نصب شده پایتون استفاده کنید.

### استفاده از Jupyter در مرورگر

شما همچنین می‌توانید روی پروژه با استفاده از محیط [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) درست در مرورگر خود کار کنید. هر دو Jupyter کلاسیک و [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) محیط توسعه بسیار خوبی با ویژگی‌هایی مانند تکمیل خودکار، برجسته‌سازی کد و غیره فراهم می‌کنند.

برای شروع Jupyter به صورت محلی، به ترمینال/خط فرمان بروید، به دایرکتوری دوره بروید و اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این یک نمونه Jupyter را شروع می‌کند و URL دسترسی به آن در پنجره خط فرمان نمایش داده می‌شود.

وقتی به URL دسترسی پیدا کردید، باید طرح دوره را ببینید و بتوانید به هر فایل `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` بروید که می‌توانید کد و خروجی‌ها را مشاهده کنید.

## استفاده از سرویس Azure OpenAI برای اولین بار

اگر این اولین بار است که با سرویس Azure OpenAI کار می‌کنید، لطفاً این راهنما را دنبال کنید که چگونه [یک منبع سرویس Azure OpenAI ایجاد و مستقر کنید.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## استفاده از API OpenAI برای اولین بار

اگر این اولین بار است که با API OpenAI کار می‌کنید، لطفاً راهنما را دنبال کنید که چگونه [رابط را ایجاد و استفاده کنید.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## ملاقات با سایر یادگیرندگان

ما کانال‌هایی در سرور رسمی Discord جامعه AI خودمان ایجاد کرده‌ایم برای ملاقات با سایر یادگیرندگان. این یک راه عالی برای شبکه‌سازی با سایر کارآفرینان، سازندگان، دانشجویان و هر کسی است که به دنبال ارتقاء در هوش مصنوعی تولیدی است.

[![پیوستن به کانال دیسکورد](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

تیم پروژه نیز در این سرور Discord حضور خواهد داشت تا به هر یادگیرنده‌ای کمک کند.

## مشارکت

این دوره یک ابتکار منبع باز است. اگر مناطقی برای بهبود یا مشکلاتی می‌بینید، لطفاً یک [درخواست Pull](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ایجاد کنید یا یک [مشکل GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ثبت کنید.

تیم پروژه همه مشارکت‌ها را دنبال خواهد کرد. مشارکت در منبع باز یک راه شگفت‌انگیز برای ساختن حرفه شما در هوش مصنوعی تولیدی است.

بیشتر مشارکت‌ها نیاز به توافقنامه مجوز مشارکت‌کننده (CLA) دارند که اعلام می‌کند شما حق دارید و واقعاً حقوق استفاده از مشارکت خود را به ما اعطا می‌کنید. برای جزئیات، به [وب‌سایت توافقنامه مجوز مشارکت‌کننده CLA](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

مهم: هنگام ترجمه متن در این مخزن، لطفاً اطمینان حاصل کنید که از ترجمه ماشینی استفاده نمی‌کنید. ما ترجمه‌ها را از طریق جامعه تأیید خواهیم کرد، بنابراین لطفاً فقط برای ترجمه‌ها در زبان‌هایی که در آنها مهارت دارید داوطلب شوید.

هنگامی که یک درخواست Pull ارسال می‌کنید، یک CLA-bot به طور خودکار تعیین می‌کند که آیا نیاز به ارائه CLA دارید و PR را به درستی تزئین می‌کند (مانند برچسب، نظر). به سادگی دستورالعمل‌های ارائه شده توسط ربات را دنبال کنید. شما فقط یک بار نیاز دارید این کار را در تمام مخازن با استفاده از CLA ما انجام دهید.

این پروژه [کد رفتار منبع باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) را پذیرفته است. برای اطلاعات بیشتر کد رفتار FAQ را بخوانید یا با [ایمیل opencode](opencode@microsoft.com) با هر سوال یا نظر اضافی تماس بگیرید.

## بیایید شروع کنیم

اکنون که مراحل لازم برای تکمیل این دوره را کامل کرده‌اید، بیایید با دریافت یک [معرفی به هوش مصنوعی تولیدی و LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) شروع کنیم.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای اشتباه ناشی از استفاده از این ترجمه نداریم.