# اس کورس کے ساتھ شروعات

ہم بہت پرجوش ہیں کہ آپ اس کورس کا آغاز کریں اور دیکھیں کہ آپ پراڈکٹیو AI کے ساتھ کیا کچھ تخلیق کرنے کے لیے متحرک ہوتے ہیں!

آپ کی کامیابی کو یقینی بنانے کے لیے، یہ صفحہ سیٹ اپ کے مراحل، تکنیکی ضروریات، اور اگر ضرورت ہو تو مدد کہاں حاصل کریں کی وضاحت کرتا ہے۔

## سیٹ اپ کے مراحل

اس کورس کو شروع کرنے کے لیے، آپ کو مندرجہ ذیل مراحل مکمل کرنے ہوں گے۔

### 1. اس ریپو کو فورک کریں

[اس پورے ریپو کو فورک کریں](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) اپنے GitHub اکاؤنٹ پر تاکہ آپ کسی بھی کوڈ میں ترمیم کر سکیں اور چیلنجز مکمل کر سکیں۔ آپ اس ریپو کو [سٹار (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) بھی دے سکتے ہیں تاکہ اسے اور متعلقہ ریپوز کو آسانی سے تلاش کیا جا سکے۔

### 2. کوڈ اسپیس بنائیں

کوڈ چلانے میں کسی قسم کے انحصار کے مسائل سے بچنے کے لیے، ہم تجویز کرتے ہیں کہ اس کورس کو [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) میں چلائیں۔

اپنے فورک میں: **Code -> Codespaces -> New on main**

![ڈائیلاگ جو کوڈ اسپیس بنانے کے بٹن دکھا رہا ہے](../../../translated_images/ur/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ایک سیکرٹ شامل کریں

1. ⚙️ گیئر آئیکن -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.
2. نام OPENAI_API_KEY رکھیں، اپنی کلید چسپاں کریں، Save کریں۔

### 3. اگلا کیا؟

| میں کرنا چاہتا ہوں…      | جائیں…                                                                   |
|-------------------------|-------------------------------------------------------------------------|
| سبق 1 شروع کریں          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| آف لائن کام کرنا          | [`setup-local.md`](02-setup-local.md)                                     |
| LLM فراہم کنندہ سیٹ اپ کریں | [`providers.md`](03-providers.md)                                        |
| دوسرے طالب علموں سے ملاقات کریں| [ہمارے Discord میں شامل ہوں](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## مسائل کا حل


| علامت                                     | حل                                                               |
|-------------------------------------------|-----------------------------------------------------------------|
| کنٹینر بلڈ 10 منٹ سے زیادہ وقت لے رہا ہے | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | ٹرمینل منسلک نہیں ہوا؛ کلک کریں **+** ➜ *bash*                  |
| OpenAI سے `401 Unauthorized`               | غلط یا ختم شدہ `OPENAI_API_KEY`                                  |
| VS Code میں “Dev container mounting…” کی پیغام | براؤزر ٹیب کو ریفریش کریں—Codespaces بعض اوقات کنکشن کھو دیتا ہے |
| نوٹ بک کرنل غائب ہے                        | نوٹ بک مینو ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   یونیكس بیسڈ سسٹمز:

   ```bash
   touch .env
   ```

   ونڈوز:

   ```cmd
   echo . > .env
   ```

3. **`.env` فائل میں ترمیم کریں**: `.env` فائل کو کسی ٹیکسٹ ایڈیٹر (مثلاً VS Code، Notepad++، یا کوئی اور ایڈیٹر) میں کھولیں۔ فائل میں درج ذیل لائنیں شامل کریں، اور جگہ داروں کو اپنی اصل Microsoft Foundry Models اینڈپوائنٹ اور کلید سے تبدیل کریں (مزید معلومات کے لیے دیکھیں [`providers.md`](03-providers.md)):

   > **نوٹ:** GitHub ماڈلز (اور اس کا `GITHUB_TOKEN` متغیر) جولائی 2026 کے آخر میں بند ہو رہا ہے۔ اس کی جگہ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) استعمال کریں۔

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **فائل محفوظ کریں**: تبدیلیاں محفوظ کریں اور ٹیکسٹ ایڈیٹر بند کریں۔

5. **`python-dotenv` انسٹال کریں**: اگر آپ نے پہلے سے نہیں کیا ہے، تو آپ کو `python-dotenv` پیکیج انسٹال کرنا ہوگا تاکہ `.env` فائل سے ماحولیاتی متغیرات کو اپنے Python ایپلیکیشن میں لوڈ کر سکیں۔ آپ اسے `pip` کے ذریعے انسٹال کر سکتے ہیں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنے Python اسکرپٹ میں ماحولیاتی متغیرات لوڈ کریں**: اپنے Python اسکرپٹ میں، `python-dotenv` پیکیج استعمال کریں تاکہ `.env` فائل سے ماحولیاتی متغیرات لوڈ کیے جا سکیں:

   ```python
   from dotenv import load_dotenv
   import os

   # .env فائل سے ماحول کے متغیرات لوڈ کریں
   load_dotenv()

   # Microsoft Foundry Models کے متغیرات تک رسائی حاصل کریں
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

بس ہو گیا! آپ نے کامیابی سے `.env` فائل بنائی، اپنی Microsoft Foundry Models کی ساکھیں شامل کیں، اور انہیں اپنی Python ایپ میں لوڈ کر لیا۔

## اپنے کمپیوٹر پر مقامی طور پر کیسے چلائیں

اپنے کمپیوٹر پر کوڈ چلانے کے لیے، آپ کے پاس [Python کا کوئی ورژن انسٹال ہونا](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ضروری ہے۔

پھر ریپوزیٹری استعمال کرنے کے لیے، اسے کلون کریں:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

جب آپ کے پاس سب کچھ چیک آؤٹ ہو جائے، تو آپ شروع کر سکتے ہیں!

## اختیاری مراحل

### Miniconda انسٹال کرنا

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ایک ہلکا پھلکا انسٹالر ہے جو [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python، اور کچھ پیکیجز انسٹال کرنے کے لیے استعمال ہوتا ہے۔
Conda خود ایک پیکیج مینیجر ہے، جو مختلف Python [**ورچوئل ماحول**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکیجز کے درمیان آسانی سے سیٹ اپ اور تبدیلی کی سہولت دیتا ہے۔ یہ `pip` سے دستیاب نہ رہنے والے پیکیجز انسٹال کرنے میں بھی مددگار ثابت ہوتا ہے۔

آپ [MiniConda انسٹالیشن گائیڈ](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) کی پیروی کر کے اسے سیٹ اپ کر سکتے ہیں۔

Miniconda انسٹال کرنے کے بعد، آپ کو [ریپوزیٹری](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) کلون کرنی ہوگی (اگر آپ نے پہلے سے نہیں کی)۔

پھر، آپ کو ایک ورچوئل ماحول بنانا ہوگا۔ Conda کے ذریعے کرنے کے لیے، ایک نیا ماحول فائل (_environment.yml_) بنائیں۔ اگر آپ Codespaces استعمال کر رہے ہیں تو اسے `.devcontainer` ڈائریکٹری میں بنائیں، یعنی `.devcontainer/environment.yml`۔

اپنے ماحول کی فائل کو ذیل میں دیے گئے اسنیپٹ سے بھر دیں:

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

اگر آپ کو conda استعمال کرتے ہوئے غلطیاں مل رہی ہیں تو آپ ٹرمینل میں نیچے دی گئی کمانڈ کے ذریعے Microsoft AI لائبریریز دستی طور پر انسٹال کر سکتے ہیں۔

```
conda install -c microsoft azure-ai-ml
```

ماحول کی فائل میں وہ انحصارات بیان کیے گئے ہیں جن کی ہمیں ضرورت ہے۔ `<environment-name>` آپ کے Conda ماحول کے لیے منتخب کردہ نام ہے، اور `<python-version>` Python کا وہ ورژن ہے جو آپ استعمال کرنا چاہتے ہیں، مثلاً `3` Python کا تازہ ترین بڑا ورژن ہے۔

اس کے بعد، نیچے دی گئی کمانڈز اپنے کمانڈ لائن/ٹرمینل میں چلائیں تاکہ اپنا Conda ماحول بنا سکیں۔

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ضمنی راستہ صرف Codespace سیٹ اپس پر لاگو ہوتا ہے
conda activate ai4beg
```

اگر آپ کو کوئی مسئلہ ہو تو [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) دیکھیں۔

### Python سپورٹ ایکسٹینشن کے ساتھ Visual Studio Code کا استعمال

ہم سفارش کرتے ہیں کہ آپ اس کورس کے لیے [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ایڈیٹر کو [Python سپورٹ ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) کے ساتھ استعمال کریں۔ یہ سفارش ہے، پر لازمی شرط نہیں۔

> **نوٹ**: کورس ریپوزیٹری کو VS Code میں کھول کر، آپ کو یہ موقع ملتا ہے کہ پروجیکٹ کو ایک کنٹینر کے اندر سیٹ اپ کریں۔ اس کی وجہ یہ ہے کہ کورس ریپوزیٹری میں ایک خاص `.devcontainer` ڈائریکٹری موجود ہے۔ مزید معلومات بعد میں۔

> **نوٹ**: جب آپ ریپوزیٹری کو کلون کر کے VS Code میں کھولیں گے، تو یہ خود بخود Python سپورٹ ایکسٹینشن انسٹال کرنے کا مشورہ دے گا۔

> **نوٹ**: اگر VS Code آپ کو ریپوزیٹری کو کنٹینر میں دوبارہ کھولنے کا کہے تو اسے انکار کریں تاکہ آپ اپنے لوکل انسٹالڈ Python ورژن کو استعمال کر سکیں۔

### براؤزر میں Jupyter کا استعمال

آپ براؤزر میں ہی [Jupyter ماحول](https://jupyter.org?WT.mc_id=academic-105485-koreyst) کا استعمال کر کے اس پروجیکٹ پر کام کر سکتے ہیں۔ کلاسک Jupyter اور [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ایک خوشگوار ڈیویلپمنٹ ماحول دیتے ہیں جس میں خودکار تکمیل، کوڈ ہائی لائٹنگ وغیرہ جیسی خصوصیات شامل ہیں۔

Jupyter کو مقامی طور پر شروع کرنے کے لیے، ٹرمینل/کمانڈ لائن پر جائیں، کورس ڈائریکٹری پر نیویگیٹ کریں، اور یہ کمانڈ چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

اس سے Jupyter انسٹینس شروع ہو جائے گا اور کمانڈ لائن ونڈو میں اس تک رسائی کے لیے URL دکھایا جائے گا۔

URL تک پہنچنے کے بعد، آپ کورس کا خاکہ دیکھ سکیں گے اور کسی بھی `*.ipynb` فائل پر نیویگیٹ کر سکیں گے۔ مثال کے طور پر، `08-building-search-applications/python/oai-solution.ipynb`۔

### کنٹینر میں چلانا

اپنے کمپیوٹر یا Codespace پر سب کچھ سیٹ اپ کرنے کا متبادل طریقہ ایک [کنٹینر](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) کا استعمال ہے۔ کورس ریپوزیٹری کے اندر خاص `.devcontainer` فولڈر کی بدولت VS Code کے ذریعے پروجیکٹ کو کنٹینر کے اندر سیٹ اپ کرنا ممکن ہے۔ Codespaces کے باہر، اس کے لیے Docker انسٹال کرنا ضروری ہوگا، اور سچ کہوں تو یہ کافی محنت طلب عمل ہے، لہٰذا ہم اسے صرف ان لوگوں کے لیے تجویز کرتے ہیں جنہیں کنٹینرز کے ساتھ کام کرنے کا تجربہ ہے۔

GitHub Codespaces استعمال کرتے وقت اپنے API کیز محفوظ رکھنے کے بہترین طریقوں میں سے ایک Codespace Secrets کا استعمال ہے۔ براہ کرم اس بارے میں مزید جاننے کے لیے [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) گائیڈ کی پیروی کریں۔


## اسباق اور تکنیکی ضروریات

اس کورس میں 6 نظریاتی اسباق اور 6 کوڈنگ اسباق شامل ہیں۔

کوڈنگ اسباق کے لیے، ہم Azure OpenAI سروس استعمال کر رہے ہیں۔ آپ کو Azure OpenAI سروس تک رسائی اور API کلید کی ضرورت ہوگی تاکہ یہ کوڈ چلایا جا سکے۔ آپ [اس درخواست کو مکمل کر کے](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) رسائی کے لیے درخواست دے سکتے ہیں۔

جب تک آپ کی درخواست پروسیس ہو رہی ہے، ہر کوڈنگ سبق میں ایک `README.md` فائل بھی شامل ہے جہاں آپ کوڈ اور آؤٹ پٹ دیکھ سکتے ہیں۔

## پہلی بار Azure OpenAI سروس کا استعمال

اگر آپ پہلی بار Azure OpenAI سروس استعمال کر رہے ہیں، تو براہ کرم [Azure OpenAI سروس ریسورس بنائیں اور تعینات کریں](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) کی اس گائیڈ کی پیروی کریں۔

## پہلی بار OpenAI API کا استعمال

اگر آپ پہلی بار OpenAI API استعمال کر رہے ہیں، تو براہ کرم [انٹرفیس بنانے اور استعمال کرنے](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) کی گائیڈ کی پیروی کریں۔

## دیگر طالب علموں سے ملاقات کریں

ہم نے اپنے سرکاری [AI کمیونٹی Discord سرور](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) میں دیگر طالب علموں سے ملاقات کے لیے چینلز بنائے ہیں۔ یہ جیسے ذہن رکھنے والوں، تاجروں، بلڈرز، طلباء کے ساتھ نیٹ ورکنگ کے لیے ایک بہترین ذریعہ ہے جو Generative AI میں مہارت حاصل کرنا چاہتے ہیں۔

[![Discord چینل میں شامل ہوں](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

پروجیکٹ ٹیم بھی اس Discord سرور پر موجود رہے گی تاکہ کسی بھی طالب علم کی مدد کر سکے۔

## حصہ ڈالیں

یہ کورس ایک اوپن سورس اقدام ہے۔ اگر آپ بہتری یا مسائل دیکھیں، تو براہ کرم ایک [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بنائیں یا ایک [GitHub مسئلہ](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) درج کریں۔

پروجیکٹ ٹیم آپ کے تمام تعاون پر نظر رکھے گی۔ اوپن سورس میں تعاون کرنا Generative AI میں اپنے کیریئر کو ترقی دینے کا ایک شاندار طریقہ ہے۔

زیادہ تر تعاون کے لیے آپ کو ایک Contributor License Agreement (CLA) پر اتفاق کرنا ضروری ہوتا ہے جو اعلان کرتا ہے کہ آپ کو یہ حق حاصل ہے اور آپ واقعی ہمیں اپنے تعاون کے استعمال کے حقوق فراہم کرتے ہیں۔ تفصیلات کے لیے ملاحظہ کریں [CLA، Contributor License Agreement ویب سائٹ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)۔

اہم: اس ریپو میں ترجمہ کرتے وقت براہ کرم یقینی بنائیں کہ آپ مشین ترجمے کا استعمال نہیں کرتے۔ ہم کمیونٹی کے ذریعے ترجموں کی تصدیق کریں گے، لہٰذا براہ کرم صرف ایسی زبانوں کے لیے ترجمہ کی خدمت میں شامل ہوں جن میں آپ مہارت رکھتے ہوں۔

جب آپ ایک pull request بھیجیں گے، تو CLA-بوٹ خود بخود طے کرے گا کہ آیا آپ کو CLA فراہم کرنے کی ضرورت ہے اور PR کو مناسب طریقے سے ٹیگ کرے گا (جیسے لیبل، تبصرہ)۔ صرف بوٹ کی ہدایات پر عمل کریں۔ آپ کو یہ صرف ایک بار کرنا ہوگا تمام ریپوزز میں جہاں ہمارا CLA استعمال ہو رہا ہو۔


اس پراجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) کو اپنایا ہے۔ مزید معلومات کے لیے Code of Conduct FAQ پڑھیں یا کسی اضافی سوالات یا تبصروں کے لیے [Email opencode](opencode@microsoft.com) سے رابطہ کریں۔

## آئیے شروع کرتے ہیں

اب جب کہ آپ نے اس کورس کو مکمل کرنے کے لیے ضروری اقدامات مکمل کر لیے ہیں، تو آئیے ایک [Generative AI اور LLMs کا تعارف](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) حاصل کر کے شروع کرتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->