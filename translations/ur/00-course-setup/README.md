# اس کورس کے ساتھ شروع کرنا

ہم بہت پرجوش ہیں کہ آپ اس کورس کا آغاز کریں اور دیکھیں کہ آپ جنریٹو AI کے ساتھ کیا تخلیق کرنے کے لیے متاثر ہوتے ہیں!

آپ کی کامیابی کو یقینی بنانے کے لیے، یہ صفحہ سیٹ اپ کے مراحل، تکنیکی تقاضے، اور اگر ضرورت ہو تو مدد حاصل کرنے کے طریقے کا خاکہ پیش کرتا ہے۔

## سیٹ اپ کے مراحل

اس کورس کو شروع کرنے کے لیے، آپ کو درج ذیل مراحل مکمل کرنے کی ضرورت ہوگی۔

### 1. اس ریپو کو فورک کریں

[اس پورے ریپو کو فورک کریں](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) تاکہ آپ اپنے GitHub اکاؤنٹ پر کسی بھی کوڈ میں تبدیلی کر سکیں اور چیلنجز مکمل کر سکیں۔ آپ اسے آسانی سے تلاش کرنے کے لیے [اس ریپو کو اسٹار (🌟) بھی کر سکتے ہیں](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) اور متعلقہ ریپوز کو۔

### 2. کوڈ اسپیس بنائیں

کوڈ چلانے کے دوران کسی بھی انحصارات کے مسائل سے بچنے کے لیے، ہم اس کورس کو [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) میں چلانے کی سفارش کرتے ہیں۔

اپنے فورک میں: **Code -> Codespaces -> New on main**

![کوڈ اسپیس بنانے کے بٹن دکھانے والی ڈائیلاگ](../../../translated_images/ur/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 ایک سیکرٹ شامل کریں

1. ⚙️ گیئر آئیکن -> کمانڈ پیلیٹ -> Codespaces : Manage user secret -> Add a new secret.
2. نام OPENAI_API_KEY رکھیں، اپنی کی چسپاں کریں، اور محفوظ کریں۔

### 3. آگے کیا؟

| میں… کرنا چاہتا ہوں          | جائیں…                                                                  |
|-----------------------------|-------------------------------------------------------------------------|
| سبق 1 شروع کرنا              | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| آف لائن کام کرنا             | [`setup-local.md`](02-setup-local.md)                                   |
| ایل ایل ایم فراہم کنندہ سیٹ کرنا | [`providers.md`](03-providers.md)                                        |
| دوسرے سیکھنے والوں سے ملنا   | [ہمارے ڈسکارڈ میں شامل ہوں](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## مسئلہ حل کرنا


| نشانِ بیماری                           | حل                                                             |
|---------------------------------------|-----------------------------------------------------------------|
| کنٹینر بلڈ 10 منٹ سے زیادہ رک گیا    | **Codespaces ➜ "Rebuild Container”**                            |
| `python: command not found`            | ٹرمینل منسلک نہیں ہوا؛ **+** ➜ *bash* پر کلک کریں                |
| OpenAI سے `401 Unauthorized`           | غلط / معیاد ختم شدہ `OPENAI_API_KEY`                            |
| VS Code پر “Dev container mounting…” ظاہر ہو رہا ہے | براؤزر ٹیب کو ریفریش کریں—Codespaces کبھی کبھار کنکشن کھو دیتا ہے   |
| نوٹ بک کرنل غائب ہے                   | نوٹ بک مینو ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   یونکس پر مبنی سسٹمز کے لیے:

   ```bash
   touch .env
   ```

   ونڈوز:

   ```cmd
   echo . > .env
   ```

3. **`.env` فائل میں ترمیم کریں**: `.env` فائل کو کسی ٹیکسٹ ایڈیٹر (جیسے VS Code، Notepad++ یا کوئی اور ایڈیٹر) میں کھولیں۔ درج ذیل لائنیں فائل میں شامل کریں، اپنی Microsoft Foundry Models کے endpoint اور key کے حقیقی مقامات کے ساتھ (دیکھیں [`providers.md`](03-providers.md) کہ یہ کیسے حاصل کریں):

   > **نوٹ:** GitHub Models (اور اس کا `GITHUB_TOKEN` ویریبل) جولائی 2026 کے آخر میں ریٹائر ہو رہا ہے۔ اس کے بجائے [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) استعمال کریں۔

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **فائل محفوظ کریں**: تبدیلیوں کو محفوظ کریں اور ٹیکسٹ ایڈیٹر بند کریں۔

5. **`python-dotenv` انسٹال کریں**: اگر پہلے سے انسٹال نہیں کیا ہے تو، `.env` فائل سے ماحول کے ویریبلز کو اپنے Python ایپلیکیشن میں لوڈ کرنے کے لیے `python-dotenv` پیکج انسٹال کریں۔ آپ اسے `pip` کے ذریعے انسٹال کر سکتے ہیں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنے Python سکرپٹ میں ماحول کے ویریبلز لوڈ کریں**: اپنے Python سکرپٹ میں، `.env` فائل سے ماحول کے ویریبلز لوڈ کرنے کے لیے `python-dotenv` پیکج استعمال کریں:

   ```python
   from dotenv import load_dotenv
   import os

   # ماحول کی متغیرات .env فائل سے لوڈ کریں
   load_dotenv()

   # Microsoft Foundry Models کے متغیرات تک رسائی حاصل کریں
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

بس ہو گیا! آپ نے کامیابی کے ساتھ `.env` فائل بنائی ہے، اپنی Microsoft Foundry Models کی شناخت شامل کی ہے، اور انہیں اپنی Python ایپلیکیشن میں لوڈ کر لیا ہے۔

## اپنے کمپیوٹر پر لوکل طور پر چلانا کیسے ہے

کوڈ لوکل طور پر اپنے کمپیوٹر پر چلانے کے لیے، آپ کو [Python کا کوئی ورژن انسٹال شدہ](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ہونا چاہیے۔

پھر ریپوزٹری کو کلون کریں:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

جب سب کچھ تیار ہوجائے، تو آپ شروع کر سکتے ہیں!

## اختیاری مراحل

### Miniconda انسٹال کرنا

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ایک ہلکا پھلکا انسٹالر ہے جو [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python، اور چند دیگر پیکجز انسٹال کرتا ہے۔
Conda خود ایک پیکج مینیجر ہے، جو مختلف Python [**ورچوئل ماحول**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکجز کے درمیان آسانی سے سوئچ اور سیٹ اپ کرنے میں مدد دیتا ہے۔ یہ ان پیکجز کے انسٹالیشن کے لیے بھی مددگار ہے جو `pip` کے ذریعے دستیاب نہیں ہوتے۔

آپ [MiniConda انسٹالیشن گائیڈ](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) کی پیروی کر کے اسے سیٹ اپ کر سکتے ہیں۔

Miniconda انسٹال کرنے کے بعد، آپ کو ریپوزٹری کلون کرنی ہوگی (اگر پہلے سے نہیں کی)۔

اس کے بعد، آپ کو ایک ورچوئل ماحول بنانا ہوگا۔ Conda کے ساتھ ایسا کرنے کے لیے، ایک نیا environment فائل (_environment.yml_) بنائیں۔ اگر آپ Codespaces استعمال کر رہے ہیں، تو اسے `.devcontainer` ڈائریکٹری کے اندر بنائیں یعنی `.devcontainer/environment.yml`۔

نیچے دیا گیا کوڈ اپنے environment فائل میں شامل کریں:

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

اگر Conda استعمال کرتے ہوئے آپ کو مسائل آ رہے ہیں تو آپ ٹرمینل میں درج ذیل کمانڈ سے Microsoft AI Libraries دستی طور پر انسٹال کر سکتے ہیں۔

```
conda install -c microsoft azure-ai-ml
```

environment فائل وہ dependencies متعین کرتی ہے جن کی ہمیں ضرورت ہے۔ `<environment-name>` وہ نام ہے جو آپ اپنے Conda ماحول کے لیے استعمال کرنا چاہیں گے، اور `<python-version>` Python کا ورژن ہے جو آپ استعمال کرنا چاہیں گے، مثلاً `3` Python کا جدید ترین بڑا ورژن ہے۔

یہ سب کرنے کے بعد، آپ درج ذیل کمانڈز اپنے کمانڈ لائن/ٹرمینل میں چلائیں تاکہ اپنا Conda environment بنا سکیں۔

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer ذیلی راستہ صرف Codespace سیٹ اپس پر لاگو ہوتا ہے
conda activate ai4beg
```

اگر آپ کو کوئی مسئلہ ہوا تو [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) دیکھیں۔

### Python سپورٹ ایکسٹینشن کے ساتھ Visual Studio Code استعمال کرنا

ہم اس کورس کے لیے [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) ایڈیٹر کے ساتھ [Python سپورٹ ایکسٹینشن](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) انسٹال کرنے کی سفارش کرتے ہیں۔ یہ ایک سفارش ہے، ضروری شرط نہیں۔

> **نوٹ**: کورس ریپوزٹری کو VS Code میں کھول کر، آپ کو پروجیکٹ کو کنٹینر میں سیٹ اپ کرنے کا آپشن ملتا ہے۔ یہ اس لیے ہے کیونکہ کورس ریپوزٹری میں خاص `.devcontainer` ڈائریکٹری موجود ہے۔ اس بارے میں مزید آگے بات کریں گے۔

> **نوٹ**: جب آپ ریپوزٹری کلون کر کے VS Code میں کھولیں گے، تو آپ کو خود بخود Python سپورٹ ایکسٹینشن انسٹال کرنے کی تجویز دے گا۔

> **نوٹ**: اگر VS Code آپ کو ریپوزٹری کو کنٹینر میں دوبارہ کھولنے کا مشورہ دے، تو اس درخواست کو مسترد کریں تاکہ اپنی مقامی طور پر انسٹال Python ورژن استعمال کر سکیں۔

### براؤزر میں Jupyter کا استعمال

آپ اس پروجیکٹ پر اپنے براؤزر میں ہی [Jupyter ماحول](https://jupyter.org?WT.mc_id=academic-105485-koreyst) کے ذریعے کام کر سکتے ہیں۔ کلاسک Jupyter اور [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) دونوں ایک خوشگوار ترقیاتی ماحول فراہم کرتے ہیں جس میں آٹو کمپلیشن، کوڈ ہائلائٹنگ، وغیرہ شامل ہیں۔

لوکل طور پر Jupyter شروع کرنے کے لیے، ٹرمینل/کمانڈ لائن کو کھولیں، کورس ڈائریکٹری میں جائیں، اور یہ کمانڈ چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

اس سے ایک Jupyter انسٹینس شروع ہو گا اور اس تک رسائی کے لیے URL کمانڈ لائن ونڈو میں دکھایا جائے گا۔

جب آپ URL تک رسائی حاصل کریں گے، تو آپ کو کورس کا خاکہ دکھائی دے گا اور آپ کسی بھی `*.ipynb` فائل پر جا سکیں گے۔ مثال کے طور پر، `08-building-search-applications/python/oai-solution.ipynb`۔

### کنٹینر میں چلانا

اپنے کمپیوٹر یا Codespace پر سب کچھ سیٹ اپ کرنے کے متبادل کے طور پر، آپ [کنٹینر](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) استعمال کر سکتے ہیں۔ مخصوص `.devcontainer` فولڈر کورس ریپوزٹری میں VS Code کو کنٹینر میں پروجیکٹ سیٹ اپ کرنے کی اجازت دیتا ہے۔ Codespaces کے علاوہ، اس کے لیے Docker انسٹالیشن کی ضرورت ہوگی، اور سچ کہوں تو، اس میں کچھ محنت درکار ہوتی ہے، اس لیے ہم یہ صرف تجربہ کار کنٹینر صارفین کو مشورہ دیتے ہیں۔

GitHub Codespaces استعمال کرتے وقت اپنی API keys کو محفوظ رکھنے کے بہترین طریقوں میں سے ایک Codespace Secrets استعمال کرنا ہے۔ براہ کرم اس کے بارے میں مزید جاننے کے لیے [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) گائیڈ کی پیروی کریں۔


## اسباق اور تکنیکی تقاضے

اس کورس میں "Learn" سبق ہیں جو جنریٹو AI کے تصورات کی وضاحت کرتے ہیں اور "Build" سبق ہیں جن میں دونوں **Python** اور **TypeScript** میں ممکنہ طور پر عملی کوڈ کی مثالیں دی جاتی ہیں۔

کوڈنگ سبقوں کے لیے، ہم Microsoft Foundry میں Azure OpenAI استعمال کرتے ہیں۔ آپ کو ایک Azure سبسکرپشن اور API key کی ضرورت ہوگی۔ رسائی کھلی ہے - کوئی درخواست ضروری نہیں - اس لیے آپ [Microsoft Foundry resource بنا سکتے ہیں اور ماڈل ڈیپلائے کر سکتے ہیں](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) تاکہ اپنا endpoint اور key حاصل کر سکیں۔

ہر کوڈنگ سبق میں ایک `README.md` فائل بھی شامل ہوتی ہے جہاں آپ بغیر کچھ چلائے کوڈ اور نتائج دیکھ سکتے ہیں۔

## پہلی بار Azure OpenAI سروس استعمال کرنا

اگر آپ پہلی بار Azure OpenAI سروس کے ساتھ کام کر رہے ہیں، تو براہ کرم اس گائیڈ پر عمل کریں کہ [Azure OpenAI سروس resource کیسے بنائیں اور ڈیپلائے کریں](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)۔

## پہلی بار OpenAI API استعمال کرنا

اگر آپ پہلی بار OpenAI API کے ساتھ کام کر رہے ہیں، تو براہ کرم اس گائیڈ پر عمل کریں کہ [انٹرفیس کیسے بنائیں اور استعمال کریں](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)۔

## دوسرے سیکھنے والوں سے ملیں

ہم نے اپنے سرکاری [AI Community Discord سرور](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) میں دوسرے سیکھنے والوں سے ملنے کے لیے چینلز بنائے ہیں۔ یہ دوسرے ہم خیال کاروباری افراد، تخلیق کاروں، طلباء اور جنریٹو AI میں مہارت حاصل کرنے کے خواہشمند لوگوں کے ساتھ نیٹ ورکنگ کا ایک بہترین ذریعہ ہے۔

[![ڈسکارڈ چینل میں شامل ہوں](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

پروجیکٹ ٹیم بھی اس Discord سرور پر موجود ہوگی تاکہ کسی بھی سیکھنے والے کی مدد کر سکے۔

## تعاون کریں

یہ کورس ایک اوپن سورس پہل ہے۔ اگر آپ بہتری کے لیے کوئی جگہ یا مسائل دیکھتے ہیں، تو براہ کرم ایک [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) بنائیں یا [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) لاگ کریں۔

پروجیکٹ ٹیم تمام تعاون کو ٹریک کرے گی۔ اوپن سورس میں حصہ ڈالنا جنریٹو AI میں آپ کے کیریئر کو بنانے کا ایک شاندار طریقہ ہے۔

زیادہ تر تعاون کے لیے ضروری ہے کہ آپ ایک Contributor License Agreement (CLA) سے اتفاق کریں جس میں آپ یہ اعلان کرتے ہیں کہ آپ کو اپنے تعاون پر حقوق دینے کا اختیار ہے۔ تفصیلات کے لیے [CLA، Contributor License Agreement ویب سائٹ](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) دیکھیں۔

اہم: جب آپ اس ریپو میں متن کا ترجمہ کریں، تو براہ کرم یقینی بنائیں کہ آپ مشینی ترجمہ استعمال نہیں کرتے۔ ہم ترجمے کمیونٹی کے ذریعے تصدیق کریں گے، اس لیے براہ کرم صرف ان زبانوں میں ترجمے کے لیے رضاکار بنیں جن میں آپ ماہر ہوں۔


جب آپ پل ریکوئسٹ جمع کروائیں گے، تو ایک CLA-بوٹ خود بخود یہ طے کرے گا کہ آیا آپ کو CLA فراہم کرنے کی ضرورت ہے اور مناسب طریقے سے PR کو سجائے گا (مثلاً، لیبل، تبصرہ)۔ بس بوٹ کی فراہم کردہ ہدایات پر عمل کریں۔ آپ کو یہ کام ہمارے CLA استعمال کرنے والی تمام ریپوزٹریز میں صرف ایک بار کرنا ہوگا۔

اس پروجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) اپنایا ہے۔ مزید معلومات کے لیے کوڈ آف کنڈکٹ FAQ پڑھیں یا کسی اضافی سوالات یا تبصروں کے لیے [Email opencode](opencode@microsoft.com) سے رابطہ کریں۔

## آئیے شروع کرتے ہیں

اب جب کہ آپ نے اس کورس کو مکمل کرنے کے لیے ضروری مراحل پورے کر لیے ہیں، تو چلیں شروع کرتے ہیں [Generative AI اور LLMs کا تعارف](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) حاصل کر کے۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->