# شروع کار با این دوره

ما بسیار هیجان‌زده‌ایم که شما این دوره را شروع کنید و ببینید با هوش مصنوعی مولد چه چیزهایی می‌توانید الهام‌بخش ساخت آنها باشید!

برای اطمینان از موفقیت شما، این صفحه مراحل راه‌اندازی، نیازمندی‌های فنی، و محل دریافت کمک در صورت نیاز را شرح می‌دهد.

## مراحل راه‌اندازی

برای شروع این دوره، باید مراحل زیر را کامل کنید.

### ۱. فورک کردن این مخزن

[این مخزن کامل را فورک کنید](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) به حساب GitHub خودتان تا بتوانید هر کدی را تغییر داده و چالش‌ها را کامل کنید. همچنین می‌توانید [📍این مخزن را به ستاره‌دارها اضافه کنید (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تا راحت‌تر آن و مخازن مرتبط را پیدا کنید.

### ۲. ایجاد کداسپیس

برای جلوگیری از هرگونه مشکل وابستگی هنگام اجرای کد، توصیه می‌کنیم این دوره را در [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) اجرا کنید.

در فورک خود: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/fa/who-will-pay.4c0609b1c7780f44.webp)

#### ۲.۱ اضافه کردن یک راز

1. ⚙️ آیکون چرخ‌دنده -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. نام را OPENAI_API_KEY بگذارید، کلید خود را بچسبانید، ذخیره کنید.

### ۳. مرحله بعدی چیست؟

| می‌خواهم…          | بروم به…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| شروع درس ۱          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| کار به صورت آفلاین | [`setup-local.md`](02-setup-local.md)                                   |
| راه‌اندازی ارائه‌دهنده LLM | [`providers.md`](03-providers.md)                                        |
| ملاقات با یادگیرندگان دیگر | [به Discord ما بپیوندید](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## عیب‌یابی


| علامت                                      | رفع مشکل                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| گیر کردن ساخت کانتینر بیش از ۱۰ دقیقه    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | ترمینال متصل نشده؛ روی **+** کلیک کنید ➜ *bash*                |
| `401 Unauthorized` از OpenAI              | کلید `OPENAI_API_KEY` اشتباه یا منقضی شده                        |
| VS Code پیام “Dev container mounting…” نشان می‌دهد | تب مرورگر را تازه کنید—گاهی اتصال Codespaces قطع می‌شود       |
| کرنل نوت‌بوک پیدا نمی‌شود                | منوی نوت‌بوک ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   سیستم‌های مبتنی بر یونیکس:

   ```bash
   touch .env
   ```

   ویندوز:

   ```cmd
   echo . > .env
   ```

۳. **فایل `.env` را ویرایش کنید**: فایل `.env` را در یک ویرایشگر متن (مثل VS Code، Notepad++ یا هر ویرایشگر دیگر) باز کنید. خط زیر را اضافه کنید، به جای `your_github_token_here`، توکن واقعی گیت‌هاب خود را وارد کنید:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

۴. **فایل را ذخیره کنید**: تغییرات را ذخیره کرده و ویرایشگر را ببندید.

۵. **نصب `python-dotenv`**: اگر قبلاً نصب نکرده‌اید، باید بسته `python-dotenv` را نصب کنید تا متغیرهای محیطی را از فایل `.env` به برنامه پایتون خود بارگذاری کنید. می‌توانید با دستور `pip` نصب کنید:

   ```bash
   pip install python-dotenv
   ```

۶. **بارگذاری متغیرهای محیطی در اسکریپت پایتون**: در اسکریپت پایتون خود، از بسته `python-dotenv` استفاده کنید تا متغیرهای محیطی را از فایل `.env` بارگذاری کنید:

   ```python
   from dotenv import load_dotenv
   import os

   # بارگیری متغیرهای محیطی از فایل .env
   load_dotenv()

   # دسترسی به متغیر GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

همین بود! شما با موفقیت یک فایل `.env` ایجاد کرده، توکن گیت‌هاب خود را اضافه و آن را در برنامه پایتون خود بارگذاری کردید.

## چگونه کد را به صورت محلی روی کامپیوتر خود اجرا کنیم

برای اجرای کد به صورت محلی روی کامپیوتر، باید نسخه‌ای از [پایتون را نصب داشته باشید](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

برای استفاده از مخزن، ابتدا باید آن را کلون کنید:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

وقتی همه چیز آماده شد، می‌توانید شروع کنید!

## مراحل اختیاری

### نصب Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) یک نصب‌کننده سبک برای نصب [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پایتون و چند بسته است.  
Conda خود یک مدیریت بسته است که راه‌اندازی و سوییچ بین محیط‌های [مجازی پایتون](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) و بسته‌ها را آسان می‌کند. همچنین برای نصب بسته‌هایی که در `pip` موجود نیستند، مفید است.

می‌توانید از [راهنمای نصب MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) دنبال کنید.

بعد از نصب Miniconda، باید مخزن را کلون کنید (اگر قبلاً نکرده‌اید) [مخزن](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)

سپس باید یک محیط مجازی بسازید. برای این کار با Conda یک فایل محیط جدید (_environment.yml_) بسازید. اگر با Codespaces دنبال می‌کنید، این فایل را داخل دایرکتوری `.devcontainer` بسازید، یعنی `.devcontainer/environment.yml`.

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

اگر هنگام استفاده از conda خطا دریافت کردید، می‌توانید به صورت دستی کتابخانه‌های هوش مصنوعی مایکروسافت را با دستور زیر نصب کنید:

```
conda install -c microsoft azure-ai-ml
```

فایل محیط، وابستگی‌های مورد نیاز را مشخص می‌کند. `<environment-name>` نام دلخواه شما برای محیط Conda است و `<python-version>` نسخه پایتونی که می‌خواهید استفاده کنید، مثلاً `3` جدیدترین نسخه اصلی پایتون است.

بعد از این کار، می‌توانید محیط Conda خود را با اجرای دستورات زیر در خط فرمان/ترمینال ایجاد کنید:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # مسیر فرعی .devcontainer فقط برای تنظیمات Codespace اعمال می‌شود
conda activate ai4beg
```

اگر به مشکلی برخوردید، به [راهنمای محیط‌های Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

### استفاده از Visual Studio Code با افزونه پشتیبانی پایتون

توصیه می‌کنیم از ویرایشگر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) به همراه [افزونه پشتیبانی پایتون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) برای این دوره استفاده کنید.  
با این حال، این صرفاً یک توصیه است و الزام قطعی نیست.

> **نکته**: با باز کردن مخزن دوره در VS Code، می‌توانید پروژه را داخل یک کانتینر تنظیم کنید. دلیل این امکان، وجود دایرکتوری خاص [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) در مخزن دوره است. بعداً بیشتر توضیح داده می‌شود.

> **نکته**: پس از کلون و باز کردن دایرکتوری در VS Code، به‌صورت خودکار پیشنهاد نصب افزونه پایتون را دریافت می‌کنید.

> **نکته**: اگر VS Code پیشنهاد داد مخزن را دوباره در یک کانتینر باز کنید، این درخواست را رد کنید تا از نسخه محلی پایتون استفاده کنید.

### استفاده از Jupyter در مرورگر

می‌توانید روی پروژه با محیط [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) درست در مرورگر خود کار کنید. هر دو Jupyter کلاسیک و [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) محیط توسعه خوشایندی با امکاناتی مانند کامل کردن خودکار، برجسته‌سازی کد و… فراهم می‌کنند.

برای اجرای لوکال Jupyter، به ترمینال/خط فرمان رفته، به پوشه دوره بروید و دستور زیر را اجرا کنید:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

این یک نمونه Jupyter راه‌اندازی می‌کند و آدرس URL دسترسی در پنجره خط فرمان نمایش داده می‌شود.

وقتی URL را باز کنید، باید ساختار دوره را ببینید و بتوانید به هر فایل `*.ipynb` هدایت شوید. برای مثال، `08-building-search-applications/python/oai-solution.ipynb`.

### اجرا در کانتینر

راه جایگزین برای راه‌اندازی همه چیز روی کامپیوتر یا Codespace استفاده از [کانتینر](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) است.  
پوشه خاص `.devcontainer` در مخزن دوره باعث می‌شود VS Code بتواند پروژه را داخل کانتینر راه‌اندازی کند.  
خارج از Codespaces، این کار نیاز به نصب Docker دارد و به‌طور کلی کمی پیچیده است، بنابراین تنها به کسانی که تجربه کار با کانتینرها را دارند توصیه می‌شود.

یکی از بهترین روش‌ها برای محافظت از کلیدهای API هنگام استفاده از GitHub Codespaces استفاده از رازهای Codespace است. لطفاً با راهنمای [مدیریت رازهای Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) بیشتر آشنا شوید.

## درس‌ها و نیازمندی‌های فنی

دوره شامل ۶ درس مفهومی و ۶ درس برنامه‌نویسی است.

برای درس‌های برنامه‌نویسی، از سرویس Azure OpenAI استفاده می‌کنیم. برای اجرای این کد به دسترسی سرویس Azure OpenAI و یک کلید API نیاز دارید. می‌توانید با [تکمیل این درخواست](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) برای دسترسی اقدام کنید.

در حالی که منتظر پردازش درخواست خود هستید، هر درس برنامه‌نویسی همچنین شامل یک فایل `README.md` است که کد و خروجی‌ها را می‌توانید مشاهده کنید.

## استفاده از سرویس Azure OpenAI برای اولین بار

اگر اولین بار است که با سرویس Azure OpenAI کار می‌کنید، لطفاً این راهنما را برای [ایجاد و راه‌اندازی منبع سرویس Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## استفاده از API OpenAI برای اولین بار

اگر اولین بار است که از API OpenAI استفاده می‌کنید، لطفاً این راهنما را برای [ایجاد و استفاده از رابط کاربری](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) دنبال کنید.

## ملاقات با یادگیرندگان دیگر

ما در سرور رسمی [Discord جامعه هوش مصنوعی](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) کانال‌هایی برای ملاقات با سایر یادگیرندگان ایجاد کرده‌ایم. این راهی عالی برای شبکه‌سازی با کارآفرینان، سازندگان، دانشجویان و هرکسی است که می‌خواهد در هوش مصنوعی مولد پیشرفت کند.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

تیم پروژه نیز در این سرور Discord حضور خواهد داشت تا به یادگیرندگان کمک کند.

## مشارکت

این دوره یک پروژه متن‌باز است. اگر نقاط بهبود یا مشکلی مشاهده کردید، لطفاً یک [درخواست پول ریکوئست](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بسازید یا یک [issue در گیت‌هاب ثبت کنید](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

تیم پروژه همه مشارکت‌ها را پیگیری خواهد کرد. مشارکت در متن‌باز یک راه شگفت‌انگیز برای ساختن مسیر شغلی شما در هوش مصنوعی مولد است.

اکثر مشارکت‌ها نیازمند موافقت با قرارداد مجوز مشارکت‌کننده (CLA) هستند که اعلام می‌کند شما حق دارید و در واقع به ما اجازه استفاده از مشارکتتان را می‌دهید. برای جزئیات، به وبسایت [CLA، قرارداد مجوز مشارکت‌کننده](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

مهم: هنگام ترجمه متن در این مخزن، لطفاً از ترجمه ماشینی استفاده نکنید. ما ترجمه‌ها را از طریق انجمن بررسی خواهیم کرد، بنابراین فقط داوطلب ترجمه در زبان‌هایی شوید که به آن مسلط هستید.

وقتی پول ریکوئست ارسال می‌کنید، یک ربات CLA به صورت خودکار بررسی می‌کند که آیا باید CLA ارائه دهید و PR را به شکل مناسب (برچسب، نظر) نشانه‌گذاری می‌کند. فقط کافیست دستورالعمل ربات را دنبال کنید. این کار فقط یک بار برای همه مخازنی که از CLA استفاده می‌کنند لازم است.

این پروژه از [کد رفتار متن‌باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) پیروی می‌کند. برای اطلاعات بیشتر FAQ کد رفتار را بخوانید یا به [ایمیل opencode](opencode@microsoft.com) برای هر سؤال یا نظر اضافی مراجعه کنید.

## بیایید شروع کنیم
حال که مراحل لازم برای تکمیل این دوره را به اتمام رسانده‌اید، بیایید با دریافت [معرفی به هوش مصنوعی مولد و مدل‌های زبان بزرگ](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) شروع کنیم.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم تا دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ‌گونه سوتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود، نمی‌باشیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->