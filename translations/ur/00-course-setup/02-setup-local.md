# لوکل سیٹ اپ 🖥️

**اس گائیڈ کو اس صورت میں استعمال کریں اگر آپ سب کچھ اپنے لیپ ٹاپ پر چلانا پسند کرتے ہیں۔**  
آپ کے پاس دو راستے ہیں: **(A) مقامی پائتھن + ورچوئل-انویئرنمنٹ** یا **(B) VS کوڈ ڈیو کنٹینر ڈوکر کے ساتھ**۔  
جو بھی آسان لگے منتخب کریں—دونوں ہی ایک ہی دروس پر لے جاتے ہیں۔

## 1.   ضروریات

| آلہ               | ورژن / نوٹس                                                                     |
|--------------------|--------------------------------------------------------------------------------|
| **پائتھن**          | 3.10 + (حاصل کریں <https://python.org> سے)                                    |
| **گٹ**             | تازہ ترین (Xcode / Git for Windows / Linux پیکج منیجر کے ساتھ آتا ہے)          |
| **VS کوڈ**          | اختیاری مگر تجویز کردہ <https://code.visualstudio.com>                        |
| **ڈوکر ڈیسک ٹاپ**   | صرف آپشن B کے لیے۔ مفت تنصیب: <https://docs.docker.com/desktop/>              |

> 💡 **مشورہ** – ٹرمینل میں آلات کی تصدیق کریں:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  آپشن A – مقامی پائتھن (سب سے تیز)

### مرحلہ 1  اس ریپو کو کلون کریں

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### مرحلہ 2  ورچوئل انویئرنمنٹ بنائیں اور فعال کریں

```bash
python -m venv .venv          # ایک بنائیں
source .venv/bin/activate     # میک او ایس / لینکس
.\.venv\Scripts\activate      # ونڈوز پاور شیل
```

✅ پرامپٹ اب (.venv) سے شروع ہونا چاہئے—اس کا مطلب ہے کہ آپ انویئرنمنٹ کے اندر ہیں۔

### مرحلہ 3  انحصار انسٹال کریں

```bash
pip install -r requirements.txt
```

سیکشن 3 [API کیز](#3-اپنی-api-کیز-شامل-کریں) پر جائیں

## 2. آپشن B – VS کوڈ ڈیو کنٹینر (ڈوکر)

ہم نے اس ریپوزیٹری اور کورس کو [ڈیولپمنٹ کنٹینر](https://containers.dev?WT.mc_id=academic-105485-koreyst) کے ساتھ سیٹ اپ کیا ہے جس میں یونیورسل رن ٹائم ہے جو Python3، .NET، Node.js اور Java کی ترقی کو سپورٹ کرتا ہے۔ متعلقہ کنفیگریشن `devcontainer.json` فائل میں مقرر ہے جو اس ریپوزیٹری کے روٹ میں `.devcontainer/` فولڈر میں واقع ہے۔

>**کیوں یہ منتخب کریں؟**
>Codespaces جیسا ماحول؛ کوئی انحصار کی تبدیلی نہیں۔

### مرحلہ 0 اضافی انسٹال کریں

ڈوکر ڈیسک ٹاپ – تصدیق کریں کہ ```docker --version``` کام کرتا ہے۔
VS کوڈ ریموٹ – کنٹینرز ایکسٹینشن (آئی ڈی: ms-vscode-remote.remote-containers)۔

### مرحلہ 1 ریپو کو VS کوڈ میں کھولیں

فائل ▸ فولڈر کھولیں… → generative-ai-for-beginners

VS کوڈ `.devcontainer/` کو پہچانتا ہے اور پرامپٹ دکھاتا ہے۔

### مرحلہ 2 کنٹینر میں دوبارہ کھولیں

"Reopen in Container" پر کلک کریں۔ ڈوکر امیج بنائے گا (تقریباً 3 منٹ پہلی بار)۔
جب ٹرمینل پرامپٹ آئے گا، تو آپ کنٹینر کے اندر ہیں۔

## 2.  آپشن C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ایک ہلکا پھلکا انسٹالر ہے جو [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، پائتھن، اور چند پیکجز انسٹال کرنے کے لیے ہے۔
Conda خود ایک پیکج مینیجر ہے، جو مختلف پائتھن [**ورچوئل انویئرنمنٹز**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکجز کو آسانی سے سیٹ اپ اور تبدیل کرنے میں مدد دیتا ہے۔ یہ ان پیکجز کی تنصیب میں بھی کام آتا ہے جو `pip` کے ذریعے دستیاب نہیں ہیں۔

### مرحلہ 0  Miniconda انسٹال کریں

[MiniConda انسٹالیشن گائیڈ](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) پر عمل کریں۔

```bash
conda --version
```

### مرحلہ 1  ورچوئل انویئرنمنٹ بنائیں

نئی انویئرنمنٹ فائل بنائیں (*environment.yml*)۔ اگر آپ Codespaces استعمال کر رہے ہیں تو یہ `.devcontainer` ڈائرکٹری میں بنائیں، یعنی `.devcontainer/environment.yml`۔

### مرحلہ 2  اپنی انویئرنمنٹ فائل میں مواد ڈالیں

درج ذیل حصہ اپنی `environment.yml` میں شامل کریں

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

### مرحلہ 3  اپنی Conda انویئرنمنٹ بنائیں

نیچے دیے گئے کمانڈ لائن/ٹرمینل میں کمانڈز چلائیں

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer کا ذیلی راستہ صرف Codespace کے ترتیبات پر لاگو ہوتا ہے۔
conda activate ai4beg
```

اگر کوئی مسئلہ ہو تو [Conda انویئرنمنٹز گائیڈ](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) دیکھیں۔

## 2  آپشن D – کلاسک جیوپیٹر / جیوپیٹر لیب (آپ کے براؤزر میں)

> **یہ کس کے لیے ہے؟**  
> جو کوئی کلاسک جیوپیٹر انٹرفیس پسند کرتا ہے یا VS کوڈ کے بغیر نوٹ بکس چلانا چاہتا ہے۔  

### مرحلہ 1  یقینی بنائیں کہ جیوپیٹر انسٹال ہے

جیوپیٹر لوکل چلانے کے لیے، ٹرمینل/کمانڈ لائن کھولیں، کورس ڈائریکٹری میں جائیں، اور درج ذیل کمانڈ چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

یہ جیوپیٹر انسٹینس شروع کرے گا اور اسے کون تک رسائی حاصل ہوگی اس کا URL کمانڈ لائن ونڈو میں دکھایا جائے گا۔

جب آپ URL تک رسائی حاصل کریں، تو آپ کورس کا خاکہ دیکھ سکیں گے اور کسی بھی `*.ipynb` فائل کو نیویگیٹ کر سکیں گے۔ مثلاً، `08-building-search-applications/python/oai-solution.ipynb`۔

## 3. اپنی API کیز شامل کریں

اپنی API کیز کو محفوظ رکھنا کسی بھی قسم کی ایپلیکیشن بناتے وقت اہم ہے۔ ہم تجویز کرتے ہیں کہ API کیز کو براہ راست اپنے کوڈ میں محفوظ نہ کریں۔ ان تفصیلات کو پبلک ریپوزیٹری میں ڈالنے سے سیکیورٹی مسائل اور غیر مطلوبہ اخراجات ہو سکتے ہیں اگر کوئی برائی کرنے والا اسے استعمال کرے۔
یہاں ایک مرحلہ وار گائیڈ ہے کہ پائتھن کے لیے `.env` فائل کیسے بنائیں اور Microsoft Foundry Models کے اسناد کیسے شامل کریں:

> **نوٹ:** GitHub Models (اور اس کا `GITHUB_TOKEN` ویری ایبل) جولائی 2026 کے آخر میں بند ہو رہا ہے۔ یہ گائیڈ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) استعمال کرتا ہے۔ مکمل طور پر آف لائن کام کرنا چاہتے ہیں؟ دیکھیں [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)۔

1. **اپنے پروجیکٹ ڈائریکٹری پر جائیں:** اپنا ٹرمینل یا کمانڈ پرامپٹ کھولیں اور اس فولڈر میں جائیں جہاں آپ `.env` فائل بنانا چاہتے ہیں۔

   ```bash
   cd path/to/your/project
   ```

2. **`.env` فائل بنائیں:** اپنا پسندیدہ ٹیکسٹ ایڈیٹر استعمال کرکے نیا `.env` نام کی فائل بنائیں۔ اگر کمانڈ لائن استعمال کر رہے ہیں، تو Unix سسٹمز پر `touch` یا Windows پر `echo` استعمال کریں:

   یونکس طرز کے سسٹمز:

   ```bash
   touch .env
   ```

   ونڈوز:

   ```cmd
   echo . > .env
   ```

3. **`.env` فائل کو ترمیم کریں:** `.env` فائل کو کسی ٹیکسٹ ایڈیٹر میں کھولیں (جیسے VS کوڈ، Notepad++ یا کوئی اور ایڈیٹر). فائل میں درج ذیل لائنیں شامل کریں، اپنے Microsoft Foundry پروجیکٹ اینڈپوائنٹ اور API کی کے اصل مقامات کے ساتھ:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **فائل محفوظ کریں:** تبدیلیاں محفوظ کریں اور ٹیکسٹ ایڈیٹر بند کریں۔

5. **`python-dotenv` انسٹال کریں:** اگر آپ نے پہلے نہیں کیا، تو `.env` فائل سے ماحولیاتی متغیرات کو اپنے پائتھن ایپلیکیشن میں لوڈ کرنے کے لیے `python-dotenv` پیکج انسٹال کریں۔ آپ اسے `pip` سے انسٹال کر سکتے ہیں:

   ```bash
   pip install python-dotenv
   ```

6. **اپنے پائتھن اسکرپٹ میں ماحولیاتی متغیرات لوڈ کریں:** اپنے پائتھن اسکرپٹ میں، `python-dotenv` پیکج کا استعمال کرتے ہوئے ماحولیاتی متغیرات `.env` فائل سے لوڈ کریں:

   ```python
   from dotenv import load_dotenv
   import os

   # .env فائل سے ماحولیاتی متغیرات لوڈ کریں
   load_dotenv()

   # مائیکروسافٹ فانڈری ماڈلز کے متغیرات تک رسائی حاصل کریں
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

بس یہی! آپ نے کامیابی سے `.env` فائل بنائی، اپنے Microsoft Foundry Models کی اسناد شامل کیں، اور انہیں اپنے پائتھن ایپلیکیشن میں لوڈ کیا۔

🔐 کبھی بھی .env کو commit نہ کریں—یہ پہلے سے .gitignore میں ہے۔
مکمل فراہم کنندہ کی ہدایات [`providers.md`](03-providers.md) میں موجود ہیں۔

## 4. اگلا کیا؟

| میں کرنا چاہتا ہوں… | جائیں…                                                                   |
|--------------------|-------------------------------------------------------------------------|
| سبق 1 شروع کریں    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| LLM پرووائیڈر سیٹ اپ کریں | [`providers.md`](03-providers.md)                                          |
| دوسرے سیکھنے والوں سے ملیں | [ہماری Discord میں شامل ہوں](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. دشواریوں کا ازالہ

| علامت                                   | حل                                                           |
|----------------------------------------|--------------------------------------------------------------|
| `python not found`                     | Python کو PATH میں شامل کریں یا انسٹال کے بعد ٹرمینل دوبارہ کھولیں  |
| `pip` پہ وہیلز نہیں بن پا رہیں (ونڈوز) | `pip install --upgrade pip setuptools wheel` پھر دوبارہ کوشش کریں۔     |
| `ModuleNotFoundError: dotenv`          | `pip install -r requirements.txt` چلائیں (env انسٹال نہیں تھا).          |
| ڈوکر بلڈ ناکام – *No space left*       | ڈوکر ڈیسک ٹاپ ▸ *Settings* ▸ *Resources* → ڈسک سائز بڑھائیں۔            |
| VS کوڈ بار بار ری اوپن کا پوچھتا ہے    | ہو سکتا ہے کہ دونوں آپشنز فعال ہوں؛ ایک کو منتخب کریں (venv **یا** کنٹینر) |
| OpenAI 401 / 429 کی غلطیاں             | `OPENAI_API_KEY` ویلیو / درخواست کی حدوں کی جانچ کریں۔                   |
| Conda استعمال کرتے ہوئے غلطیاں        | Microsoft AI لائبریریاں انسٹال کریں `conda install -c microsoft azure-ai-ml`  |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->