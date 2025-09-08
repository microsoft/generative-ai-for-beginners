<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T14:20:14+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ur"
}
-->
# اس کورس کے ساتھ شروعات کریں

ہمیں بہت خوشی ہے کہ آپ یہ کورس شروع کر رہے ہیں اور دیکھنا چاہتے ہیں کہ جنریٹیو اے آئی کے ساتھ آپ کیا تخلیق کرتے ہیں!

آپ کی کامیابی کو یقینی بنانے کے لیے، اس صفحے پر سیٹ اپ کے مراحل، تکنیکی ضروریات، اور مدد حاصل کرنے کے ذرائع بیان کیے گئے ہیں۔

## سیٹ اپ کے مراحل

اس کورس کو شروع کرنے کے لیے، آپ کو درج ذیل مراحل مکمل کرنے ہوں گے۔

### 1. اس ریپو کو فورک کریں

[اس پورے ریپو کو فورک کریں](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) اپنے GitHub اکاؤنٹ پر تاکہ آپ کوڈ میں تبدیلیاں کر سکیں اور چیلنجز مکمل کر سکیں۔ آپ اس ریپو کو [اسٹار (🌟) بھی کر سکتے ہیں](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) تاکہ اسے اور متعلقہ ریپوز کو آسانی سے تلاش کر سکیں۔

### 2. کوڈ اسپیس بنائیں

کوڈ چلانے کے دوران کسی بھی ڈیپینڈنسی کے مسئلے سے بچنے کے لیے، ہم تجویز کرتے ہیں کہ یہ کورس [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) میں چلائیں۔

اپنے فورک میں: **Code -> Codespaces -> New on main**

![کوڈ اسپیس بنانے کے بٹن دکھانے والا ڈائیلاگ](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 سیکرٹ شامل کریں

1. ⚙️ گیئر آئیکن -> کمانڈ پیلیٹ -> Codespaces : Manage user secret -> نیا سیکرٹ شامل کریں۔
2. نام رکھیں OPENAI_API_KEY، اپنی کی پیسٹ کریں، محفوظ کریں۔

### 3. آگے کیا کرنا ہے؟

| میں یہ کرنا چاہتا ہوں…      | یہاں جائیں                                                                  |
|-----------------------------|-----------------------------------------------------------------------------|
| سبق 1 شروع کریں             | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| آف لائن کام کریں            | [`setup-local.md`](02-setup-local.md)                                       |
| LLM فراہم کنندہ سیٹ اپ کریں | [`providers.md`](providers.md)                                              |
| دیگر سیکھنے والوں سے ملیں   | [ہمارے ڈسکارڈ میں شامل ہوں](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## مسائل اور ان کا حل

| مسئلہ                                      | حل                                                               |
|---------------------------------------------|------------------------------------------------------------------|
| کنٹینر بلڈ 10 منٹ سے زیادہ رک جائے          | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                 | ٹرمینل اٹیچ نہیں ہوا؛ **+** ➜ *bash* پر کلک کریں                 |
| OpenAI سے `401 Unauthorized`                | غلط یا ختم شدہ `OPENAI_API_KEY`                                  |
| VS Code میں “Dev container mounting…” آئے   | براؤزر ٹیب ریفریش کریں—Codespaces کبھی کبھار کنکشن کھو دیتا ہے  |
| نوٹ بک کرنل غائب ہے                        | نوٹ بک مینو ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   یونکس بیسڈ سسٹمز:

   ```bash
   touch .env
   ```

   ونڈوز:

   ```cmd
   echo . > .env
   ```

3. **`.env` فائل میں ترمیم کریں**: `.env` فائل کو کسی ٹیکسٹ ایڈیٹر (جیسے VS Code، Notepad++ یا کوئی اور ایڈیٹر) میں کھولیں۔ اس فائل میں درج ذیل لائن شامل کریں، `your_github_token_here` کو اپنے اصل GitHub ٹوکن سے بدل دیں:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **فائل محفوظ کریں**: تبدیلیاں محفوظ کریں اور ایڈیٹر بند کریں۔

5. **`python-dotenv` انسٹال کریں**: اگر آپ نے پہلے انسٹال نہیں کیا، تو آپ کو `python-dotenv` پیکیج انسٹال کرنا ہوگا تاکہ `.env` فائل سے ماحول کی ویریبلز اپنے Python ایپلیکیشن میں لوڈ کر سکیں۔ اسے `pip` سے انسٹال کریں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنے Python اسکرپٹ میں ماحول کی ویریبلز لوڈ کریں**: اپنے Python اسکرپٹ میں `python-dotenv` پیکیج استعمال کریں تاکہ `.env` فائل سے ماحول کی ویریبلز لوڈ کی جا سکیں:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

بس! آپ نے کامیابی سے `.env` فائل بنائی، اپنا GitHub ٹوکن شامل کیا، اور اسے اپنی Python ایپلیکیشن میں لوڈ کر لیا۔

## اپنے کمپیوٹر پر لوکل چلائیں

کوڈ کو اپنے کمپیوٹر پر لوکل چلانے کے لیے، آپ کو [Python کی کوئی ورژن انسٹال](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) کرنا ہوگی۔

اس کے بعد ریپوزٹری استعمال کرنے کے لیے، آپ کو اسے کلون کرنا ہوگا:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

جب سب کچھ چیک آؤٹ ہو جائے، تو آپ شروعات کر سکتے ہیں!

## اضافی مراحل

### Miniconda انسٹال کرنا

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ایک ہلکا پھلکا انسٹالر ہے جو [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python، اور کچھ پیکیجز انسٹال کرتا ہے۔
Conda بذات خود ایک پیکیج منیجر ہے، جو مختلف Python [**ورچوئل ماحول**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکیجز سیٹ اپ اور سوئچ کرنا آسان بناتا ہے۔ یہ ان پیکیجز کو انسٹال کرنے میں بھی مددگار ہے جو `pip` سے دستیاب نہیں۔

آپ [MiniConda انسٹالیشن گائیڈ](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) فالو کر کے اسے سیٹ اپ کر سکتے ہیں۔

Miniconda انسٹال ہونے کے بعد، آپ کو [ریپوزٹری](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) کلون کرنا ہوگی (اگر پہلے نہیں کی)۔

اس کے بعد، آپ کو ایک ورچوئل ماحول بنانا ہوگا۔ Conda کے ساتھ ایسا کرنے کے لیے، ایک نیا ماحول فائل (_environment.yml_) بنائیں۔ اگر آپ Codespaces استعمال کر رہے ہیں، تو یہ `.devcontainer` ڈائریکٹری میں بنائیں، یعنی `.devcontainer/environment.yml`۔

اپنے ماحول فائل کو نیچے دیے گئے اسنیپٹ سے مکمل کریں:

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

اگر آپ کو conda استعمال کرتے ہوئے ایرر آئے تو آپ مائیکروسافٹ اے آئی لائبریریز کو مندرجہ ذیل کمانڈ سے ٹرمینل میں دستی طور پر انسٹال کر سکتے ہیں۔

```
conda install -c microsoft azure-ai-ml
```

ماحول فائل میں وہ ڈیپینڈنسیز لکھی گئی ہیں جو ہمیں چاہیے۔ `<environment-name>` وہ نام ہے جو آپ اپنے Conda ماحول کے لیے رکھنا چاہتے ہیں، اور `<python-version>` وہ Python ورژن ہے جو آپ استعمال کرنا چاہتے ہیں، مثلاً `3` Python کا تازہ ترین میجر ورژن ہے۔

اب آپ اپنے Conda ماحول کو کمانڈ لائن/ٹرمینل میں نیچے دی گئی کمانڈز سے بنا سکتے ہیں

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر کوئی مسئلہ آئے تو [Conda ماحول گائیڈ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) دیکھیں۔

### Python سپورٹ ایکسٹینشن کے ساتھ Visual Studio Code استعمال کرنا

ہم تجویز کرتے ہیں کہ اس کورس کے لیے [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ایڈیٹر اور [Python سپورٹ ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) انسٹال کریں۔ یہ صرف ایک تجویز ہے، لازمی نہیں۔

> **نوٹ**: کورس ریپوزٹری کو VS Code میں کھولنے سے آپ کو پروجیکٹ کو کنٹینر میں سیٹ اپ کرنے کا آپشن ملتا ہے۔ یہ کورس ریپوزٹری میں موجود [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ڈائریکٹری کی وجہ سے ہے۔ اس پر بعد میں مزید بات ہوگی۔

> **نوٹ**: جب آپ ڈائریکٹری کو کلون اور VS Code میں کھولیں گے، تو یہ خودکار طور پر Python سپورٹ ایکسٹینشن انسٹال کرنے کی تجویز دے گا۔

> **نوٹ**: اگر VS Code آپ کو ریپوزٹری کو کنٹینر میں دوبارہ کھولنے کی تجویز دے، تو اس درخواست کو رد کریں تاکہ آپ لوکل انسٹال شدہ Python ورژن استعمال کر سکیں۔

### براؤزر میں Jupyter استعمال کرنا

آپ اس پروجیکٹ پر [Jupyter ماحول](https://jupyter.org?WT.mc_id=academic-105485-koreyst) میں بھی کام کر سکتے ہیں، براہ راست اپنے براؤزر میں۔ کلاسک Jupyter اور [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) دونوں میں آٹو کمپلیشن، کوڈ ہائی لائٹنگ وغیرہ جیسی سہولیات ہیں۔

Jupyter کو لوکل شروع کرنے کے لیے، ٹرمینل/کمانڈ لائن میں جائیں، کورس ڈائریکٹری پر جائیں، اور یہ کمانڈ چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

اس سے Jupyter انسٹینس شروع ہو جائے گا اور اس کا URL کمانڈ لائن ونڈو میں دکھایا جائے گا۔

جب آپ URL پر جائیں گے، تو آپ کو کورس آؤٹ لائن نظر آئے گی اور آپ کسی بھی `*.ipynb` فائل پر جا سکیں گے۔ مثلاً، `08-building-search-applications/python/oai-solution.ipynb`۔

### کنٹینر میں چلانا

اپنے کمپیوٹر یا Codespace پر سب کچھ سیٹ اپ کرنے کا متبادل یہ ہے کہ آپ [کنٹینر](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) استعمال کریں۔ کورس ریپوزٹری میں خاص `.devcontainer` فولڈر کی وجہ سے VS Code پروجیکٹ کو کنٹینر میں سیٹ اپ کر سکتا ہے۔ Codespaces کے علاوہ، اس کے لیے Docker انسٹال کرنا ہوگا، اور یہ کچھ محنت طلب ہے، اس لیے ہم یہ صرف ان لوگوں کو تجویز کرتے ہیں جنہیں کنٹینرز کے ساتھ کام کرنے کا تجربہ ہے۔

GitHub Codespaces استعمال کرتے ہوئے اپنے API کیز کو محفوظ رکھنے کے بہترین طریقوں میں سے ایک Codespace Secrets استعمال کرنا ہے۔ براہ کرم [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) گائیڈ فالو کریں۔

## اسباق اور تکنیکی ضروریات

کورس میں 6 تصوری اسباق اور 6 کوڈنگ اسباق ہیں۔

کوڈنگ اسباق کے لیے ہم Azure OpenAI Service استعمال کر رہے ہیں۔ اس کوڈ کو چلانے کے لیے آپ کو Azure OpenAI سروس تک رسائی اور API key چاہیے ہوگی۔ آپ [یہ درخواست مکمل کر کے](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) رسائی کے لیے اپلائی کر سکتے ہیں۔

جب تک آپ کی درخواست پراسیس ہو رہی ہے، ہر کوڈنگ سبق میں ایک `README.md` فائل بھی شامل ہے جس میں آپ کو کوڈ اور آؤٹ پٹس دیکھنے کو ملیں گے۔

## Azure OpenAI Service پہلی بار استعمال کرنا

اگر آپ پہلی بار Azure OpenAI سروس استعمال کر رہے ہیں، تو براہ کرم یہ گائیڈ فالو کریں کہ [Azure OpenAI Service ریسورس کیسے بنائیں اور ڈیپلائے کریں۔](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API پہلی بار استعمال کرنا

اگر آپ پہلی بار OpenAI API استعمال کر رہے ہیں، تو براہ کرم یہ گائیڈ فالو کریں کہ [انٹرفیس کیسے بنائیں اور استعمال کریں۔](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## دیگر سیکھنے والوں سے ملیں

ہم نے اپنے آفیشل [AI کمیونٹی ڈسکارڈ سرور](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) میں چینلز بنائے ہیں تاکہ آپ دیگر سیکھنے والوں سے مل سکیں۔ یہ ہم خیال کاروباری افراد، بلڈرز، طلبہ اور جنریٹیو اے آئی میں آگے بڑھنے کے خواہشمند افراد سے نیٹ ورکنگ کا بہترین طریقہ ہے۔

[![ڈسکارڈ چینل میں شامل ہوں](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

پروجیکٹ ٹیم بھی اس ڈسکارڈ سرور پر موجود ہوگی تاکہ سیکھنے والوں کی مدد کر سکے۔

## تعاون کریں

یہ کورس ایک اوپن سورس اقدام ہے۔ اگر آپ کو بہتری کی گنجائش یا کوئی مسئلہ نظر آئے تو براہ کرم [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بنائیں یا [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) لاگ کریں۔

پروجیکٹ ٹیم تمام تعاون کو ٹریک کرے گی۔ اوپن سورس میں تعاون کرنا جنریٹیو اے آئی میں اپنے کیریئر کو بنانے کا بہترین طریقہ ہے۔

زیادہ تر تعاون کے لیے آپ کو Contributor License Agreement (CLA) سے اتفاق کرنا ہوگا، جس میں آپ یہ اعلان کرتے ہیں کہ آپ کو تعاون کرنے کا حق ہے اور آپ ہمیں اس تعاون کو استعمال کرنے کی اجازت دیتے ہیں۔ تفصیلات کے لیے [CLA، Contributor License Agreement ویب سائٹ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) دیکھیں۔

اہم: اس ریپو میں ترجمہ کرتے وقت براہ کرم یقینی بنائیں کہ آپ مشین ترجمہ استعمال نہ کریں۔ ہم ترجمہ کو کمیونٹی کے ذریعے ویریفائی کریں گے، اس لیے صرف ان زبانوں میں ترجمہ کے لیے رضاکار بنیں جن میں آپ ماہر ہیں۔

جب آپ pull request جمع کرائیں گے، تو CLA-bot خودکار طور پر یہ طے کرے گا کہ آپ کو CLA فراہم کرنے کی ضرورت ہے یا نہیں اور PR کو مناسب طریقے سے لیبل یا کمنٹ کرے گا۔ بس bot کی ہدایات پر عمل کریں۔ آپ کو یہ صرف ایک بار کرنا ہوگا، تمام ریپوزٹریز میں جہاں ہمارا CLA استعمال ہوتا ہے۔

اس پروجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) کو اپنایا ہے۔ مزید معلومات کے لیے Code of Conduct FAQ پڑھیں یا [Email opencode](opencode@microsoft.com) پر رابطہ کریں اگر کوئی سوال یا تبصرہ ہو۔

## آئیے شروعات کریں
اب جب کہ آپ اس کورس کو مکمل کرنے کے لیے درکار تمام مراحل طے کر چکے ہیں، تو آئیے شروعات کرتے ہیں اور [جنریٹیو اے آئی اور ایل ایل ایمز کا تعارف](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) حاصل کرتے ہیں۔

---

**اعلانِ دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی بھرپور کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی صورت میں ہم ذمہ دار نہیں ہوں گے۔