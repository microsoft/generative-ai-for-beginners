<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:37:58+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ur"
}
-->
# اس کورس کا آغاز

ہم اس کورس کے آغاز کے لیے بہت پرجوش ہیں اور دیکھنا چاہتے ہیں کہ آپ جنریٹیو اے آئی کے ساتھ کیا تخلیق کرنے کی تحریک پاتے ہیں!

آپ کی کامیابی کو یقینی بنانے کے لیے، یہ صفحہ سیٹ اپ کے مراحل، تکنیکی ضروریات، اور ضرورت پڑنے پر مدد کہاں سے حاصل کی جا سکتی ہے، کی وضاحت کرتا ہے۔

## سیٹ اپ کے مراحل

اس کورس کو شروع کرنے کے لیے، آپ کو مندرجہ ذیل مراحل مکمل کرنے کی ضرورت ہوگی۔

### 1. اس ریپو کو فورک کریں

[اس پورے ریپو کو فورک کریں](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) اپنے GitHub اکاؤنٹ پر تاکہ آپ کوڈ میں تبدیلی کر سکیں اور چیلنجز مکمل کر سکیں۔ آپ اس ریپو کو [اسٹار (🌟) بھی دے سکتے ہیں](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تاکہ اسے اور متعلقہ ریپوز کو آسانی سے تلاش کیا جا سکے۔

### 2. کوڈ اسپیس بنائیں

کسی بھی ڈپینڈنسی کے مسائل سے بچنے کے لیے جب کوڈ چلایا جائے، ہم تجویز کرتے ہیں کہ اس کورس کو [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) میں چلائیں۔

یہ آپ کے فورک کیے گئے ریپو کے `Code` آپشن کو منتخب کرکے اور **Codespaces** آپشن کو منتخب کرکے بنایا جا سکتا ہے۔

![کوڈ اسپیس بنانے کے لیے بٹن دکھانے والا ڈائیلاگ](../../../00-course-setup/images/who-will-pay.webp)

### 3. اپنے API کیز کو محفوظ کریں

کسی بھی قسم کی ایپلیکیشن بناتے وقت اپنے API کیز کو محفوظ اور محفوظ رکھنا اہم ہے۔ ہم تجویز کرتے ہیں کہ کسی بھی API کیز کو براہ راست آپ کے کوڈ میں نہ رکھیں۔ ان تفصیلات کو کسی عوامی ریپوزیٹری میں جمع کرانے سے سیکیورٹی مسائل اور یہاں تک کہ ناپسندیدہ اخراجات بھی ہو سکتے ہیں اگر کسی برے کردار کے ذریعہ استعمال کیا جائے۔
یہاں ایک مرحلہ وار گائیڈ ہے کہ کس طرح Python کے لیے `.env` فائل بنائی جائے اور `GITHUB_TOKEN` شامل کی جائے:

1. **اپنے پروجیکٹ ڈائریکٹری پر جائیں**: اپنا ٹرمینل یا کمانڈ پرامپٹ کھولیں اور اپنے پروجیکٹ کی روٹ ڈائریکٹری میں جائیں جہاں آپ `.env` فائل بنانا چاہتے ہیں۔

   ```bash
   cd path/to/your/project
   ```

2. **`.env` فائل بنائیں**: اپنے پسندیدہ ٹیکسٹ ایڈیٹر کا استعمال کرکے ایک نئی فائل بنائیں جس کا نام `.env` ہو۔ اگر آپ کمانڈ لائن استعمال کر رہے ہیں، تو آپ `touch` (on Unix-based systems) or `echo` استعمال کر سکتے ہیں (ونڈوز پر):

   یونکس پر مبنی سسٹمز:
   ```bash
   touch .env
   ```

   ونڈوز:
   ```cmd
   echo . > .env
   ```

3. **`.env` فائل میں ترمیم کریں**: `.env` فائل کو کسی ٹیکسٹ ایڈیٹر (مثلاً، VS کوڈ، نوٹ پیڈ++، یا کسی دوسرے ایڈیٹر) میں کھولیں۔ فائل میں مندرجہ ذیل لائن شامل کریں، `your_github_token_here` کو اپنے اصل GitHub ٹوکن سے تبدیل کریں:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **فائل کو محفوظ کریں**: تبدیلیوں کو محفوظ کریں اور ٹیکسٹ ایڈیٹر کو بند کریں۔

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` پیکج انسٹال کریں تاکہ `.env` فائل سے اپنے Python ایپلیکیشن میں ماحول کے متغیرات کو لوڈ کیا جا سکے۔ آپ اسے `pip` کا استعمال کرکے انسٹال کر سکتے ہیں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنی Python اسکرپٹ میں ماحول کے متغیرات کو لوڈ کریں**: اپنی Python اسکرپٹ میں، `.env` فائل سے ماحول کے متغیرات کو لوڈ کرنے کے لیے `python-dotenv` پیکج کا استعمال کریں:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

یہی ہے! آپ نے کامیابی کے ساتھ ایک `.env` فائل بنائی، اپنا GitHub ٹوکن شامل کیا، اور اسے اپنی Python ایپلیکیشن میں لوڈ کیا۔

## اپنے کمپیوٹر پر مقامی طور پر کیسے چلائیں

اپنے کمپیوٹر پر کوڈ کو مقامی طور پر چلانے کے لیے، آپ کو [Python کا کچھ ورژن انسٹال](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) کرنا ہوگا۔

پھر ریپوزیٹری کو استعمال کرنے کے لیے، آپ کو اسے کلون کرنے کی ضرورت ہے:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ایک بار جب آپ کے پاس سب کچھ چیک ہو جائے، تو آپ شروع کر سکتے ہیں!

## اختیاری مراحل 

### Miniconda انسٹال کرنا

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python، اور کچھ پیکجز کو انسٹال کرنے کے لیے ایک ہلکا پھلکا انسٹالر ہے۔
خود Conda ایک پیکج مینیجر ہے، جو مختلف Python [**ورچوئل ماحول**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکجز کے درمیان سیٹ اپ اور سوئچ کرنا آسان بناتا ہے۔ یہ ان پیکجز کو انسٹال کرنے کے لیے بھی کارآمد ہے جو `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` کے ذریعے دستیاب نہیں ہیں۔

اپنے ماحول کی فائل کو نیچے دیے گئے اقتباس سے بھریں:

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

اگر آپ کو conda استعمال کرتے ہوئے غلطیاں ملتی ہیں تو آپ مندرجہ ذیل کمانڈ کو ٹرمینل میں استعمال کرتے ہوئے Microsoft AI لائبریریوں کو دستی طور پر انسٹال کر سکتے ہیں۔

```
conda install -c microsoft azure-ai-ml
```

ماحول کی فائل ان انحصار کو بیان کرتی ہے جن کی ہمیں ضرورت ہے۔ `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python کا تازہ ترین بڑا ورژن ہے۔

یہ سب ہو جانے کے بعد، آپ کمانڈ لائن/ٹرمینل میں نیچے دی گئی کمانڈز چلا کر اپنا Conda ماحول بنا سکتے ہیں

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر آپ کو کوئی مسئلہ پیش آئے تو [Conda ماحولیات کی گائیڈ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) کا حوالہ دیں۔

### Python سپورٹ ایکسٹینشن کے ساتھ Visual Studio Code کا استعمال

ہم اس کورس کے لیے [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ایڈیٹر کے ساتھ [Python سپورٹ ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) انسٹال کرنے کی سفارش کرتے ہیں۔ تاہم، یہ زیادہ تر ایک سفارش ہے اور قطعی ضرورت نہیں ہے۔

> **نوٹ**: VS کوڈ میں کورس ریپوزیٹری کو کھول کر، آپ کے پاس پروجیکٹ کو ایک کنٹینر کے اندر سیٹ اپ کرنے کا آپشن ہے۔ یہ کورس ریپوزیٹری کے اندر پائی جانے والی [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ڈائریکٹری کی وجہ سے ہے۔ اس پر مزید بعد میں بات کریں گے۔

> **نوٹ**: ایک بار جب آپ ڈائریکٹری کو کلون اور VS کوڈ میں کھولتے ہیں، تو یہ خود بخود آپ کو Python سپورٹ ایکسٹینشن انسٹال کرنے کی تجویز دے گا۔

> **نوٹ**: اگر VS کوڈ آپ کو کنٹینر میں ریپوزیٹری کو دوبارہ کھولنے کی تجویز دیتا ہے، تو اس درخواست کو مسترد کریں تاکہ Python کے مقامی طور پر انسٹال شدہ ورژن کا استعمال کیا جا سکے۔

### براؤزر میں Jupyter کا استعمال

آپ اپنے براؤزر کے اندر [Jupyter ماحول](https://jupyter.org?WT.mc_id=academic-105485-koreyst) کا استعمال کرتے ہوئے پروجیکٹ پر بھی کام کر سکتے ہیں۔ کلاسیکی Jupyter اور [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) دونوں ایک خوشگوار ترقیاتی ماحول فراہم کرتے ہیں جس میں آٹو کمپلیشن، کوڈ ہائی لائٹنگ وغیرہ جیسی خصوصیات شامل ہیں۔

مقامی طور پر Jupyter شروع کرنے کے لیے، ٹرمینل/کمانڈ لائن پر جائیں، کورس ڈائریکٹری میں جائیں، اور عمل کریں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

یہ ایک Jupyter انسٹینس کو شروع کرے گا اور اسے تک رسائی کے لیے URL کمانڈ لائن ونڈو میں دکھایا جائے گا۔

ایک بار جب آپ URL تک رسائی حاصل کر لیتے ہیں، تو آپ کو کورس کا خاکہ نظر آنا چاہیے اور کسی بھی `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` فائل پر جا سکیں گے جہاں آپ کوڈ اور آؤٹ پٹس دیکھ سکتے ہیں۔

## Azure OpenAI سروس کا پہلی بار استعمال

اگر یہ آپ کا پہلی بار Azure OpenAI سروس کے ساتھ کام کرنا ہے، تو براہ کرم اس گائیڈ پر عمل کریں کہ کس طرح [Azure OpenAI سروس کا ریسورس بنائیں اور تعینات کریں۔](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## پہلی بار OpenAI API کا استعمال

اگر یہ آپ کا پہلی بار OpenAI API کے ساتھ کام کرنا ہے، تو براہ کرم اس گائیڈ پر عمل کریں کہ کس طرح [انٹرفیس بنائیں اور استعمال کریں۔](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## دوسرے سیکھنے والوں سے ملاقات کریں

ہم نے دوسرے سیکھنے والوں سے ملنے کے لیے اپنے سرکاری [AI کمیونٹی ڈسکارڈ سرور](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) میں چینلز بنائے ہیں۔ یہ ہم خیال کاروباری افراد، تخلیق کاروں، طلباء، اور کسی بھی ایسے شخص کے ساتھ نیٹ ورک کرنے کا ایک بہترین طریقہ ہے جو جنریٹیو اے آئی میں اپنی مہارت کو بڑھانا چاہتا ہے۔

[![ڈسکارڈ چینل میں شامل ہوں](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

پروجیکٹ ٹیم بھی اس ڈسکارڈ سرور پر سیکھنے والوں کی مدد کے لیے موجود ہوگی۔

## تعاون کریں

یہ کورس ایک اوپن سورس اقدام ہے۔ اگر آپ کو بہتری کے علاقے یا مسائل نظر آتے ہیں، تو براہ کرم ایک [پُل ریکویسٹ](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بنائیں یا ایک [GitHub مسئلہ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) لاگ کریں۔

پروجیکٹ ٹیم تمام تعاون کو ٹریک کرے گی۔ اوپن سورس میں تعاون کرنا جنریٹیو اے آئی میں اپنے کیریئر کی تعمیر کا ایک شاندار طریقہ ہے۔

زیادہ تر تعاون کے لیے آپ کو ایک تعاون کنندہ لائسنس معاہدہ (CLA) سے اتفاق کرنے کی ضرورت ہوتی ہے جس میں یہ اعلان کیا جاتا ہے کہ آپ کو حق حاصل ہے اور آپ واقعی ہمیں آپ کے تعاون کو استعمال کرنے کے حقوق دیتے ہیں۔ تفصیلات کے لیے، [CLA، تعاون کنندہ لائسنس معاہدہ ویب سائٹ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔

اہم: اس ریپو میں متن کا ترجمہ کرتے وقت، براہ کرم یقینی بنائیں کہ آپ مشین ترجمہ استعمال نہیں کرتے ہیں۔ ہم کمیونٹی کے ذریعے تراجم کی تصدیق کریں گے، لہذا براہ کرم صرف ان زبانوں کے تراجم کے لیے رضاکارانہ طور پر کام کریں جہاں آپ ماہر ہیں۔

جب آپ ایک پُل ریکویسٹ جمع کراتے ہیں، تو ایک CLA-bot خود بخود یہ تعین کرے گا کہ آیا آپ کو CLA فراہم کرنے کی ضرورت ہے اور PR کو مناسب طریقے سے سجائے گا (مثلاً، لیبل، تبصرہ)۔ بس بوٹ کی طرف سے فراہم کردہ ہدایات پر عمل کریں۔ آپ کو یہ ہمارے CLA استعمال کرنے والی تمام ریپوزیٹریز میں ایک بار کرنا ہوگا۔

اس پروجیکٹ نے [Microsoft اوپن سورس ضابطہ اخلاق](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) کو اپنایا ہے۔ مزید معلومات کے لیے ضابطہ اخلاق FAQ پڑھیں یا [ای میل اوپن کوڈ](opencode@microsoft.com) سے کسی بھی اضافی سوالات یا تبصروں کے ساتھ رابطہ کریں۔

## شروع کریں

اب جب کہ آپ نے اس کورس کو مکمل کرنے کے لیے ضروری مراحل مکمل کر لیے ہیں، آئیے [جنریٹیو اے آئی اور LLMs کا تعارف](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) حاصل کرکے شروع کریں۔

**دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔