# اس کورس کے ساتھ شروعات

ہم بہت پرجوش ہیں کہ آپ اس کورس کو شروع کریں اور دیکھیں کہ آپ جنریٹیو AI کے ساتھ کیا تخلیق کرنے کی تحریک حاصل کرتے ہیں!

آپ کی کامیابی کو یقینی بنانے کے لیے، یہ صفحہ سیٹ اپ کے مراحل، تکنیکی ضروریات، اور مدد کہاں ملے گی اگر ضرورت ہو، کی وضاحت کرتا ہے۔

## سیٹ اپ کے مراحل

اس کورس کو شروع کرنے کے لیے، آپ کو درج ذیل مراحل مکمل کرنے ہوں گے۔

### 1. اس ریپو کو فورک کریں

[اس پورے ریپو کو فورک کریں](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) تاکہ آپ اپنے GitHub اکاؤنٹ پر کوڈ میں تبدیلی کر سکیں اور چیلنج مکمل کر سکیں۔ آپ اسے اور متعلقہ ریپوز کو آسانی سے تلاش کرنے کے لیے [اس ریپو کو اسٹار (🌟) بھی کر سکتے ہیں](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)۔

### 2. کوڈ اسپیس بنائیں

کوڈ چلانے میں کسی بھی انحصار کے مسائل سے بچنے کے لیے، ہم تجویز کرتے ہیں کہ آپ یہ کورس [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) میں چلائیں۔

اپنے فورک میں: **Code -> Codespaces -> New on main**

![ڈائیلاگ جو کوڈ اسپیس بنانے کے بٹن دکھا رہا ہے](../../../translated_images/ur/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ایک سیکرٹ شامل کریں

1. ⚙️ گئر آئیکن -> کمانڈ پیلیٹ -> Codespaces : Manage user secret -> Add a new secret۔
2. نام OPENAI_API_KEY رکھیں، اپنی کلید چسپاں کریں، Save کریں۔

### 3. آگے کیا کرنا ہے؟

| میں چاہتا ہوں کہ…       | جائیں…                                                                |
|-------------------------|----------------------------------------------------------------------|
| سبق 1 شروع کریں         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| آف لائن کام کریں        | [`setup-local.md`](02-setup-local.md)                                 |
| LLM فراہم کنندہ سیٹ اپ کریں | [`providers.md`](03-providers.md)                                    |
| دیگر سیکھنے والوں سے ملیں | [ہمارے Discord میں شامل ہوں](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## مسئلہ حل کرنے کی ہدایات

| علامت                                  | حل                                                              |
|---------------------------------------|-----------------------------------------------------------------|
| کنٹینر بلڈ 10 منٹ سے زیادہ رکا رہا ہو | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`            | ٹرمینل جڑا نہیں؛ **+** پر کلک کریں ➜ *bash*                     |
| OpenAI سے `401 Unauthorized`           | غلط یا معیاد ختم شدہ `OPENAI_API_KEY`                          |
| VS Code “Dev container mounting…” دکھائے | براؤزر ٹیب کو ریفریش کریں—Codespaces کبھی کبھار کنکشن کھو دیتا ہے |
| نوٹ بک کرنل غائب ہے                    | نوٹ بک مینو ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   یونکس بیسڈ سسٹمز:

   ```bash
   touch .env
   ```

   ونڈوز:

   ```cmd
   echo . > .env
   ```

3. **`.env` فائل میں ترمیم کریں**: `.env` فائل کو کسی ٹیکسٹ ایڈیٹر (جیسے VS Code، Notepad++، یا کوئی اور ایڈیٹر) میں کھولیں۔ فائل میں درج ذیل لائن شامل کریں، اپنے حقیقی GitHub ٹوکن کے ساتھ `your_github_token_here` کو تبدیل کرتے ہوئے:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **فائل کو محفوظ کریں**: تبدیلیاں محفوظ کریں اور ٹیکسٹ ایڈیٹر بند کریں۔

5. **`python-dotenv` انسٹال کریں**: اگر آپ نے ابھی تک یہ نہیں کیا، تو آپ کو `python-dotenv` پیکج انسٹال کرنا ہوگا تاکہ `.env` فائل سے ماحول کے متغیرات آپ کے پائتھن ایپ میں لوڈ ہوں۔ آپ اسے `pip` کے ذریعے انسٹال کر سکتے ہیں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنے پائتھن اسکرپٹ میں ماحول کے متغیرات لوڈ کریں**: اپنے پائتھن اسکرپٹ میں، `python-dotenv` پیکج استعمال کریں تاکہ `.env` فائل سے ماحول کے متغیرات لوڈ کر سکیں:

   ```python
   from dotenv import load_dotenv
   import os

   # فائل .env سے ماحول کے متغیرات کو لوڈ کریں
   load_dotenv()

   # متغیر GITHUB_TOKEN تک رسائی حاصل کریں
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

یہی ہے! آپ نے کامیابی کے ساتھ `.env` فائل بنالی ہے، اپنا GitHub ٹوکن شامل کیا ہے، اور اسے اپنے پائتھن ایپلیکیشن میں لوڈ کیا ہے۔

## اپنے کمپیوٹر پر مقامی طور پر چلانے کا طریقہ

اپنے کمپیوٹر پر کوڈ چلانے کے لیے، آپ کے پاس [پائتھن کی کوئی نہ کوئی ورژن انسٹال ہونا ضروری ہے](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)۔

پھر اس ریپوزٹری کو استعمال کرنے کے لیے، آپ کو اسے کلون کرنا ہوگا:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ایک بار جب آپ نے سب کچھ چیک آؤٹ کر لیا تو، آپ شروع کر سکتے ہیں!

## اختیاری مراحل

### Miniconda انسٹال کرنا

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ایک ہلکا پھلکا انسٹالر ہے جو [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پائتھن، اور کچھ پیکجز انسٹال کرنے کے لیے استعمال ہوتا ہے۔
Conda خود ایک پیکج مینیجر ہے، جو مختلف پائتھن [**ورچوئل ماحول**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکجز کو سیٹ اپ اور سوئچ کرنا آسان بناتا ہے۔ یہ `pip` کے ذریعے دستیاب نہ ہونے والے پیکجز انسٹال کرنے میں بھی مددگار ہے۔

آپ [MiniConda انسٹالیشن گائیڈ](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) کی پیروی کر کے اسے سیٹ اپ کر سکتے ہیں۔

Miniconda انسٹال ہونے کے بعد، آپ کو ریپوزٹری کو کلون کرنا ہوگا (اگر پہلے نہیں کیا ہے)۔

اس کے بعد، آپ کو ورچوئل ماحول بنانا ہوگا۔ Conda کے ساتھ یہ کرنے کے لیے، ایک نیا ماحول فائل (_environment.yml_) بنائیں۔ اگر آپ Codespaces استعمال کر رہے ہیں تو اسے `.devcontainer` ڈائریکٹری میں بنائیں، یعنی `.devcontainer/environment.yml`۔

نیچے دی گئی کوڈ کاپی کر کے اپنے ماحول کی فائل میں شامل کریں:

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

اگر آپ کو conda استعمال کرتے ہوئے غلطیاں آرہی ہوں، تو آپ مائیکروسافٹ AI لائبریریاں دستی طور پر مندرجہ ذیل کمانڈ کے ذریعے انسٹال کر سکتے ہیں:

```
conda install -c microsoft azure-ai-ml
```

ماحول کی فائل میں وہ انحصارات بیان کیے گئے ہیں جن کی ہمیں ضرورت ہے۔ `<environment-name>` سے مراد وہ نام ہے جو آپ اپنے Conda ماحول کے لیے رکھنا چاہتے ہیں، اور `<python-version>` پائتھن کا وہ ورژن ہے جو آپ استعمال کرنا چاہتے ہیں، مثلاً `3` پائتھن کا جدید بڑا ورژن ہے۔

یہ سب ہو جانے کے بعد، آپ نیچے دی گئی کمانڈز اپنے کمانڈ لائن/ٹرمینل میں چلا کر اپنا Conda ماحول بنا سکتے ہیں:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ذیلی راستہ صرف Codespace سیٹ اپس پر لاگو ہوتا ہے
conda activate ai4beg
```

اگر آپ کو کوئی مسئلہ پیش آئے تو [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ملاحظہ کریں۔

### Visual Studio Code کے ساتھ Python سپورٹ ایکسٹینشن کا استعمال

ہم اس کورس کے لیے [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ایڈیٹر کو [Python سپورٹ ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) کے ساتھ استعمال کرنے کی سفارش کرتے ہیں۔ تاہم، یہ صرف ایک سفارش ہے اور لازمی شرط نہیں۔

> **نوٹ**: کورس ریپوزٹری کو VS Code میں کھول کر، آپ کو پروجیکٹ کو کنٹینر کے اندر سیٹ اپ کرنے کا اختیار ملتا ہے۔ یہ اس لیے ممکن ہے کیونکہ کورس ریپوزٹری میں ایک [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) فولڈر موجود ہے۔ اس بارے میں مزید بعد میں بات ہوگی۔

> **نوٹ**: جب آپ ریپوزٹری کو کلون کر کے VS Code میں کھولیں گے، تو یہ خود بخود آپ کو Python سپورٹ ایکسٹینشن انسٹال کرنے کا مشورہ دے گا۔

> **نوٹ**: اگر VS Code آپ کو ریپوزٹری کو کنٹینر میں دوبارہ کھولنے کا مشورہ دے، تو اسے مسترد کریں تاکہ آپ لوکل انسٹال شدہ Python ورژن استعمال کر سکیں۔

### براؤزر میں Jupyter کا استعمال

آپ اس پروجیکٹ پر اپنے براؤزر میں [Jupyter ماحول](https://jupyter.org?WT.mc_id=academic-105485-koreyst) کا استعمال کرتے ہوئے بھی کام کر سکتے ہیں۔ کلاسک Jupyter اور [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) دونوں ایک خوشگوار ترقیاتی ماحول فراہم کرتے ہیں، جس میں خودکار تکمیل، کوڈ ہائی لائٹنگ، وغیرہ جیسی خصوصیات شامل ہیں۔

مقامی طور پر Jupyter شروع کرنے کے لیے، ٹرمینل/کمانڈ لائن میں جائیں، کورس ڈائریکٹری پر نیویگیٹ کریں، اور درج ذیل چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

یہ Jupyter کا ایک انسٹنس شروع کرے گا اور اسے رسائی کے لیے URL کمانڈ لائن ونڈو میں دکھایا جائے گا۔

جب آپ URL تک پہنچیں گے، تو آپ کورس کا خاکہ دیکھ سکیں گے اور کسی بھی `*.ipynb` فائل پر نیویگیٹ کر سکیں گے، مثلاً `08-building-search-applications/python/oai-solution.ipynb`۔

### کنٹینر میں چلانا

اپنے کمپیوٹر یا Codespace پر ہر چیز سیٹ اپ کرنے کا ایک متبادل طریقہ [کنٹینر](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) کا استعمال ہے۔ کورس ریپوزٹری میں خاص `.devcontainer` فولڈر VS Code کو پروجیکٹ کو کنٹینر کے اندر سیٹ اپ کرنے کے قابل بناتا ہے۔ Codespaces کے باہر، اس کے لیے Docker انسٹال کرنا ہوگا، اور صاف گوئی سے کہیں تو یہ کچھ فنی تجربہ طلب کرتا ہے، اس لیے ہم اس کی سفارش صرف ان لوگوں کو کرتے ہیں جنہیں کنٹینرز کے ساتھ کام کرنے کا تجربہ ہو۔

GitHub Codespaces استعمال کرتے وقت اپنی API کیز کو محفوظ رکھنے کا ایک بہترین طریقہ Codespace Secrets کا استعمال ہے۔ اس کے بارے میں مزید جاننے کے لیے براہ کرم [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) گائیڈ پر عمل کریں۔

## اسباق اور تکنیکی ضروریات

کورس میں 6 تصوراتی اسباق اور 6 کوڈنگ اسباق شامل ہیں۔

کوڈنگ اسباق کے لیے، ہم Azure OpenAI Service استعمال کر رہے ہیں۔ آپ کو Azure OpenAI سروس تک رسائی اور API کلید کی ضرورت ہوگی تاکہ یہ کوڈ چلایا جا سکے۔ آپ [اس درخواست کو مکمل کر کے](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) رسائی کے لیے درخواست دے سکتے ہیں۔

جب آپ کی درخواست پر کارروائی ہو رہی ہو، تو ہر کوڈنگ سبق کے ساتھ ایک `README.md` فائل بھی ہوتی ہے جہاں آپ کوڈ اور نتائج دیکھ سکتے ہیں۔

## Azure OpenAI Service کا پہلی بار استعمال

اگر آپ پہلی بار Azure OpenAI سروس استعمال کر رہے ہیں، تو براہ کرم اس گائیڈ پر عمل کریں کہ کیسے [Azure OpenAI Service ریسورس بنائیں اور تعینات کریں۔](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API کا پہلی بار استعمال

اگر یہ آپ کا پہلا بار ہے کہ آپ OpenAI API استعمال کر رہے ہیں، تو براہ کرم یہ گائیڈ دیکھیں کہ کیسے [انٹرفیس بنائیں اور استعمال کریں۔](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## دیگر سیکھنے والوں سے ملاقات

ہم نے اپنے سرکاری [AI کمیونٹی Discord سرور](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) میں چیلنز بنائے ہیں تاکہ دیگر سیکھنے والوں سے مل سکیں۔ یہ دوسرے مماثل سوچ کے کاروباریوں، بنانے والوں، طلباء، اور ہر اُس شخص کے ساتھ نیٹ ورک بنانے کا ایک بہترین طریقہ ہے جو جنریٹیو AI میں مہارت حاصل کرنا چاہتا ہے۔

[![Discord چینل میں شامل ہوں](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

پروجیکٹ ٹیم بھی اس Discord سرور پر موجود ہوگی تاکہ کسی بھی سیکھنے والے کی مدد کر سکے۔

## حصہ ڈالیں

یہ کورس ایک اوپن سورس اقدام ہے۔ اگر آپ بہتری یا مسائل دیکھتے ہیں، تو براہ کرم ایک [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بنائیں یا [GitHub مسئلہ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) رپورٹ کریں۔

پروجیکٹ ٹیم تمام شراکتوں کو ٹریک کرے گی۔ اوپن سورس میں حصہ ڈالنا جنریٹیو AI میں اپنا کیریئر بنانے کا ایک شاندار طریقہ ہے۔

زیادہ تر شراکتوں کے لیے آپ کو ایک Contributor License Agreement (CLA) سے اتفاق کرنا ہوگا جو اعلان کرے کہ آپ کے پاس اس شراکت کو استعمال کرنے کے حقوق ہیں۔ تفصیلات کے لیے [CLA, Contributor License Agreement ویب سائٹ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) دیکھیں۔

اہم: جب آپ اس ریپو کے متن کا ترجمہ کریں، تو براہ کرم یقینی بنائیں کہ آپ مشین ترجمہ استعمال نہ کریں۔ ہم ترجموں کی تصدیق کمیونٹی کے ذریعے کریں گے، لہٰذا براہ کرم صرف وہ زبانیں منتخب کریں جن میں آپ ماہر ہیں۔

جب آپ پل ریکوئسٹ جمع کرائیں گے، تو CLA-بوٹ خود بخود فیصلہ کرے گا کہ آیا آپ کو CLA فراہم کرنا ہوگا اور PR کو مناسب طریقے سے ٹیگ کرے گا (مثلاً لیبل، تبصرہ)۔ بس بوٹ کی ہدایات پر عمل کریں۔ آپ کو یہ تمام ریپوزٹریز میں صرف ایک بار کرنا ہوگا جو ہمارے CLA کا استعمال کرتی ہیں۔

اس منصوبے نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) اپنایا ہے۔ مزید معلومات کے لیے Code of Conduct FAQ پڑھیں یا اضافی سوالات یا تبصروں کے لیے [Email opencode](opencode@microsoft.com) سے رابطہ کریں۔

## چلیں شروع کریں!
اب جب کہ آپ نے اس کورس کو مکمل کرنے کے لیے ضروری اقدامات مکمل کر لیے ہیں، آئیے ایک [تعارف جنریٹیو اے آئی اور ایل ایل ایمز کا](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) حاصل کرنے سے شروع کرتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**خبردار**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم یہ بات ذہن میں رکھیں کہ خودکار تراجم میں غلطیاں یا بے ترتیبی ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں مستند سورس سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا بدفہمی کی صورت میں ہم ذمہ دار نہیں ہوں گے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->