<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:18:36+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ur"
}
-->
# اس کورس کے ساتھ شروعات کریں

ہم آپ کے اس کورس کو شروع کرنے کے لئے بہت پرجوش ہیں اور دیکھنا چاہتے ہیں کہ آپ جنریٹیو AI کے ساتھ کیا بنانے کی تحریک لیتے ہیں!

آپ کی کامیابی کو یقینی بنانے کے لئے، یہ صفحہ سیٹ اپ کے مراحل، تکنیکی ضروریات، اور اگر ضرورت ہو تو مدد کہاں حاصل کی جا سکتی ہے، کے بارے میں بتاتا ہے۔

## سیٹ اپ کے مراحل

اس کورس کو شروع کرنے کے لئے، آپ کو درج ذیل مراحل مکمل کرنے کی ضرورت ہوگی۔

### 1. اس ریپو کو فورک کریں

اس پورے ریپو کو اپنے GitHub اکاؤنٹ میں [فورک کریں](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) تاکہ آپ کوڈ میں تبدیلیاں کر سکیں اور چیلنجز مکمل کر سکیں۔ آپ اس ریپو کو [سٹار (🌟) بھی کر سکتے ہیں](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تاکہ آپ کو یہ اور متعلقہ ریپوز آسانی سے مل سکیں۔

### 2. کوڈ اسپیس بنائیں

کوڈ کو چلانے کے دوران کسی بھی انحصار کے مسائل سے بچنے کے لئے، ہم اس کورس کو [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) میں چلانے کی سفارش کرتے ہیں۔

یہ آپ کے فورک کیے گئے ریپو ورژن میں `Code` آپشن کو منتخب کر کے اور **Codespaces** آپشن کو منتخب کر کے بنایا جا سکتا ہے۔

![کوڈ اسپیس بنانے کے لئے بٹن دکھانے والا ڈائیلاگ](../../../00-course-setup/images/who-will-pay.webp)

### 3. اپنے API کیز کو محفوظ کرنا

جب آپ کوئی ایپلیکیشن بناتے ہیں تو اپنے API کیز کو محفوظ اور محفوظ رکھنا ضروری ہے۔ ہم تجویز کرتے ہیں کہ کوئی بھی API کیز براہ راست اپنے کوڈ میں نہ رکھیں۔ ان تفصیلات کو عوامی ریپوزٹری میں جمع کرانا سیکیورٹی مسائل کا باعث بن سکتا ہے اور اگر کسی بدنیت فرد نے استعمال کیا تو غیر مطلوبہ اخراجات بھی ہو سکتے ہیں۔ یہاں Python کے لئے `.env` فائل بنانے اور `GITHUB_TOKEN` شامل کرنے کا مرحلہ وار گائیڈ ہے:

1. **اپنی پروجیکٹ ڈائریکٹری پر جائیں**: اپنی ٹرمینل یا کمانڈ پرامپٹ کھولیں اور اپنی پروجیکٹ کی روٹ ڈائریکٹری پر جائیں جہاں آپ `.env` فائل بنانا چاہتے ہیں۔

   ```bash
   cd path/to/your/project
   ```

2. **`.env` فائل بنائیں**: اپنی پسندیدہ ٹیکسٹ ایڈیٹر کا استعمال کرتے ہوئے ایک نئی فائل بنائیں جس کا نام `.env` ہو۔ اگر آپ کمانڈ لائن استعمال کر رہے ہیں تو `touch` (on Unix-based systems) or `echo` استعمال کر سکتے ہیں (ونڈوز پر):

   یونکس پر مبنی نظام:
   ```bash
   touch .env
   ```

   ونڈوز:
   ```cmd
   echo . > .env
   ```

3. **`.env` فائل میں ترمیم کریں**: `.env` فائل کو ٹیکسٹ ایڈیٹر (مثلاً، VS کوڈ، نوٹ پیڈ++، یا کوئی دوسرا ایڈیٹر) میں کھولیں۔ فائل میں مندرجہ ذیل لائن شامل کریں، `your_github_token_here` کو اپنے اصل GitHub ٹوکن سے تبدیل کریں:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **فائل کو محفوظ کریں**: تبدیلیوں کو محفوظ کریں اور ٹیکسٹ ایڈیٹر کو بند کریں۔

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` پیکج کو انسٹال کریں تاکہ `.env` فائل سے ماحول متغیرات کو آپ کی Python ایپلیکیشن میں لوڈ کیا جا سکے۔ آپ اسے `pip` کا استعمال کر کے انسٹال کر سکتے ہیں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنی Python اسکرپٹ میں ماحول متغیرات لوڈ کریں**: اپنی Python اسکرپٹ میں، `python-dotenv` پیکج کا استعمال کرتے ہوئے `.env` فائل سے ماحول متغیرات کو لوڈ کریں:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

یہی ہے! آپ نے کامیابی سے `.env` فائل بنائی، اپنا GitHub ٹوکن شامل کیا، اور اسے اپنی Python ایپلیکیشن میں لوڈ کیا۔

## اپنے کمپیوٹر پر مقامی طور پر کیسے چلائیں

اپنے کمپیوٹر پر کوڈ کو مقامی طور پر چلانے کے لئے، آپ کو [Python کا کچھ ورژن انسٹال](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) کرنا ہوگا۔

پھر ریپوزٹری کو استعمال کرنے کے لئے، آپ کو اسے کلون کرنا ہوگا:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

جب آپ کے پاس سب کچھ چیک آؤٹ ہو جائے، تو آپ شروع کر سکتے ہیں!

## اختیاری مراحل

### Miniconda انسٹال کرنا

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python، اور کچھ پیکجز انسٹال کرنے کے لئے ایک ہلکا وزن انسٹالر ہے۔ خود Conda ایک پیکج مینیجر ہے، جو مختلف Python [**ورچوئل ماحول**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکجز کے درمیان سیٹ اپ اور سوئچ کرنا آسان بناتا ہے۔ یہ ان پیکجز کو انسٹال کرنے کے لئے بھی کارآمد ہے جو `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` کے ذریعے دستیاب نہیں ہیں۔

اپنے ماحول فائل کو نیچے دی گئی سنیپٹ سے بھر دیں:

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

اگر آپ کو conda استعمال کرتے وقت غلطیاں ملتی ہیں تو آپ مندرجہ ذیل کمانڈ کا استعمال کرتے ہوئے Microsoft AI لائبریریوں کو دستی طور پر انسٹال کر سکتے ہیں۔

```
conda install -c microsoft azure-ai-ml
```

ماحول فائل انحصار کو وضاحت کرتی ہے جو ہمیں درکار ہیں۔ `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python کا تازہ ترین بڑا ورژن ہے۔

یہ کرنے کے بعد، آپ اپنے کمانڈ لائن/ٹرمینل میں نیچے دی گئی کمانڈز چلا کر اپنا Conda ماحول بنا سکتے ہیں۔

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر آپ کو کسی مسئلے کا سامنا ہو تو [Conda ماحول گائیڈ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) کا حوالہ دیں۔

### Python سپورٹ ایکسٹینشن کے ساتھ Visual Studio Code کا استعمال

ہم اس کورس کے لئے [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ایڈیٹر کے ساتھ [Python سپورٹ ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) انسٹال کرنے کی سفارش کرتے ہیں۔ تاہم، یہ زیادہ تر ایک سفارش ہے اور لازمی ضرورت نہیں ہے۔

> **نوٹ**: VS Code میں کورس ریپوزٹری کھول کر، آپ کے پاس پروجیکٹ کو ایک کنٹینر کے اندر سیٹ اپ کرنے کا آپشن ہوتا ہے۔ یہ کورس ریپوزٹری کے اندر موجود [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ڈائریکٹری کی وجہ سے ہے۔ اس پر مزید بعد میں بات کریں گے۔

> **نوٹ**: جب آپ ڈائریکٹری کو کلون اور کھولتے ہیں تو VS Code آپ کو Python سپورٹ ایکسٹینشن انسٹال کرنے کی تجویز دے گا۔

> **نوٹ**: اگر VS Code آپ کو ریپوزٹری کو کنٹینر میں دوبارہ کھولنے کی تجویز دیتا ہے، تو اس درخواست کو مسترد کریں تاکہ Python کا مقامی طور پر انسٹال شدہ ورژن استعمال کیا جا سکے۔

### براؤزر میں Jupyter کا استعمال

آپ [Jupyter ماحول](https://jupyter.org?WT.mc_id=academic-105485-koreyst) کو براؤزر میں ہی استعمال کر کے پروجیکٹ پر کام کر سکتے ہیں۔ کلاسک Jupyter اور [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) دونوں ہی آٹو کمپلیشن، کوڈ ہائی لائٹنگ وغیرہ جیسی خصوصیات کے ساتھ ایک خوشگوار ترقیاتی ماحول فراہم کرتے ہیں۔

مقامی طور پر Jupyter شروع کرنے کے لئے، ٹرمینل/کمانڈ لائن پر جائیں، کورس ڈائریکٹری پر جائیں، اور چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

یہ ایک Jupyter انسٹینس شروع کرے گا اور اس کا URL کمانڈ لائن ونڈو میں دکھایا جائے گا۔

جب آپ URL تک رسائی حاصل کریں گے، تو آپ کورس کا خاکہ دیکھ سکیں گے اور کسی بھی `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` فائل پر جا سکیں گے جہاں آپ کوڈ اور نتائج دیکھ سکتے ہیں۔

## پہلی بار Azure OpenAI سروس کا استعمال

اگر یہ آپ کا Azure OpenAI سروس کے ساتھ کام کرنے کا پہلا تجربہ ہے، تو براہ کرم اس گائیڈ کو فالو کریں کہ [Azure OpenAI سروس ریسورس کیسے بنائیں اور تعینات کریں۔](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## پہلی بار OpenAI API کا استعمال

اگر یہ آپ کا OpenAI API کے ساتھ کام کرنے کا پہلا تجربہ ہے، تو براہ کرم اس گائیڈ کو فالو کریں کہ [انٹرفیس کیسے بنائیں اور استعمال کریں۔](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## دوسرے سیکھنے والوں سے ملیں

ہم نے دوسرے سیکھنے والوں سے ملنے کے لئے اپنے سرکاری [AI کمیونٹی ڈسکارڈ سرور](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) میں چینلز بنائے ہیں۔ یہ ہم خیال انٹرپرینیورز، بلڈرز، طلباء، اور جنریٹیو AI میں مہارت حاصل کرنے کے خواہشمند کسی کے ساتھ نیٹ ورکنگ کرنے کا ایک بہترین طریقہ ہے۔

[![ڈسکارڈ چینل میں شامل ہوں](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

پروجیکٹ ٹیم بھی اس ڈسکارڈ سرور پر کسی بھی سیکھنے والے کی مدد کے لئے موجود ہوگی۔

## تعاون کریں

یہ کورس ایک اوپن سورس اقدام ہے۔ اگر آپ کو بہتری کے مواقع یا مسائل نظر آئیں، تو براہ کرم [پُل درخواست](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بنائیں یا [GitHub مسئلہ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) لاگ کریں۔

پروجیکٹ ٹیم تمام تعاون کو ٹریک کرے گی۔ اوپن سورس میں تعاون کرنا جنریٹیو AI میں اپنے کیریئر کی تعمیر کا ایک حیرت انگیز طریقہ ہے۔

زیادہ تر تعاون کے لئے آپ کو ایک Contributor License Agreement (CLA) سے اتفاق کرنے کی ضرورت ہوتی ہے، جس میں یہ اعلان ہوتا ہے کہ آپ کے پاس ہمیں آپ کے تعاون کے حقوق دینے کا حق ہے اور آپ واقعی ایسا کرتے ہیں۔ تفصیلات کے لئے، [CLA، Contributor License Agreement ویب سائٹ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔

اہم: جب اس ریپو میں متن کا ترجمہ کرتے ہیں، تو براہ کرم یقینی بنائیں کہ آپ مشینی ترجمہ استعمال نہیں کرتے ہیں۔ ہم کمیونٹی کے ذریعے ترجمے کی تصدیق کریں گے، لہذا براہ کرم صرف ان زبانوں میں ترجمہ کے لئے رضاکار بنیں جن میں آپ ماہر ہیں۔

جب آپ پُل درخواست جمع کراتے ہیں، تو ایک CLA-بوٹ خود بخود یہ طے کرے گا کہ آیا آپ کو CLA فراہم کرنے کی ضرورت ہے اور PR کو مناسب طریقے سے سجائے گا (مثلاً، لیبل، تبصرہ)۔ بس بوٹ کی فراہم کردہ ہدایات پر عمل کریں۔ آپ کو یہ ایک بار ہمارے CLA استعمال کرنے والے تمام ریپوزٹریز کے لئے کرنے کی ضرورت ہوگی۔

اس پروجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) کو اپنایا ہے۔ مزید معلومات کے لئے Code of Conduct FAQ پڑھیں یا کسی بھی اضافی سوالات یا تبصروں کے ساتھ [ای میل اوپن کوڈ](opencode@microsoft.com) سے رابطہ کریں۔

## شروع کریں

اب جب کہ آپ نے اس کورس کو مکمل کرنے کے لئے درکار مراحل مکمل کر لئے ہیں، تو آئیے [جنریٹیو AI اور LLMs کا تعارف](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) حاصل کر کے شروع کریں۔

**دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشاں ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غلط فہمیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں معتبر ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔