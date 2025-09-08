<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T14:19:10+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ur"
}
-->
# مقامی سیٹ اپ 🖥️

**اس رہنمائی کو استعمال کریں اگر آپ سب کچھ اپنے لیپ ٹاپ پر چلانا چاہتے ہیں۔**  
آپ کے پاس دو راستے ہیں: **(A) نیٹو پائتھن + ورچوئل-انوائرنمنٹ** یا **(B) VS Code Dev Container with Docker**۔  
جو آسان لگے، وہی منتخب کریں—دونوں راستے ایک ہی سبق تک پہنچاتے ہیں۔

## 1.  لازمی چیزیں

| ٹول                | ورژن / نوٹس                                                                       |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (حاصل کریں <https://python.org>)                                           |
| **Git**            | تازہ ترین (Xcode / Git for Windows / Linux package manager کے ساتھ آتا ہے)         |
| **VS Code**        | اختیاری مگر تجویز کردہ <https://code.visualstudio.com>                            |
| **Docker Desktop** | *صرف* آپشن B کے لیے۔ مفت انسٹال: <https://docs.docker.com/desktop/>               |

> 💡 **ٹپ** – ٹرمینل میں ٹولز کی تصدیق کریں:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  آپشن A – نیٹو پائتھن (سب سے تیز)

### مرحلہ 1  اس ریپو کو کلون کریں

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### مرحلہ 2 ورچوئل انوائرنمنٹ بنائیں اور ایکٹیویٹ کریں

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ اب پرامپٹ (.venv) سے شروع ہونا چاہیے—اس کا مطلب ہے آپ انوائرنمنٹ کے اندر ہیں۔

### مرحلہ 3 ڈیپینڈنسیز انسٹال کریں

```bash
pip install -r requirements.txt
```

[API keys](../../../00-course-setup) والے سیکشن 3 پر جائیں

## 2. آپشن B – VS Code Dev Container (Docker)

ہم نے اس ریپوزٹری اور کورس کو ایک [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) کے ساتھ سیٹ اپ کیا ہے جس میں یونیورسل رن ٹائم ہے جو Python3, .NET, Node.js اور Java ڈویلپمنٹ کو سپورٹ کرتا ہے۔ متعلقہ کنفیگریشن `devcontainer.json` فائل میں ہے جو `.devcontainer/` فولڈر میں اس ریپوزٹری کی روٹ پر موجود ہے۔

>**یہ کیوں منتخب کریں؟**
>Codespaces جیسا بالکل ایک جیسا ماحول؛ کوئی ڈیپینڈنسی ڈرفٹ نہیں۔

### مرحلہ 0 اضافی چیزیں انسٹال کریں

Docker Desktop – تصدیق کریں ```docker --version``` کام کرتا ہے۔
VS Code Remote – Containers ایکسٹینشن (ID: ms-vscode-remote.remote-containers)۔

### مرحلہ 1 ریپو کو VS Code میں کھولیں

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code `.devcontainer/` کو پہچانتا ہے اور ایک پرامپٹ دکھاتا ہے۔

### مرحلہ 2 کنٹینر میں دوبارہ کھولیں

“Reopen in Container” پر کلک کریں۔ Docker امیج بناتا ہے (پہلی بار ≈ 3 منٹ)۔
جب ٹرمینل پرامپٹ آئے، آپ کنٹینر کے اندر ہیں۔

## 2.  آپشن C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ایک ہلکا پھلکا انسٹالر ہے جو [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python اور کچھ پیکجز انسٹال کرتا ہے۔
Conda بذات خود ایک پیکج مینیجر ہے، جو مختلف Python [**ورچوئل انوائرنمنٹس**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) اور پیکجز کو سیٹ اپ اور سوئچ کرنا آسان بناتا ہے۔ یہ ان پیکجز کو انسٹال کرنے میں بھی مددگار ہے جو `pip` سے دستیاب نہیں۔

### مرحلہ 0  Miniconda انسٹال کریں

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) کو فالو کریں۔

```bash
conda --version
```

### مرحلہ 1 ورچوئل انوائرنمنٹ بنائیں

نیا انوائرنمنٹ فائل (*environment.yml*) بنائیں۔ اگر آپ Codespaces استعمال کر رہے ہیں تو اسے `.devcontainer` ڈائریکٹری میں بنائیں، یعنی `.devcontainer/environment.yml`۔

### مرحلہ 2  انوائرنمنٹ فائل میں مواد ڈالیں

یہ اسنیپٹ اپنے `environment.yml` میں شامل کریں

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

### مرحلہ 3 اپنا Conda انوائرنمنٹ بنائیں

نیچے دیے گئے کمانڈز کمانڈ لائن/ٹرمینل میں چلائیں

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

اگر کوئی مسئلہ آئے تو [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) دیکھیں۔

## 2  آپشن D – کلاسک Jupyter / Jupyter Lab (اپنے براؤزر میں)

> **یہ کس کے لیے ہے؟**  
> ہر وہ شخص جو کلاسک Jupyter انٹرفیس پسند کرتا ہے یا نوٹ بکس VS Code کے بغیر چلانا چاہتا ہے۔  

### مرحلہ 1  یقینی بنائیں Jupyter انسٹال ہے

Jupyter کو مقامی طور پر چلانے کے لیے، ٹرمینل/کمانڈ لائن پر جائیں، کورس ڈائریکٹری میں جائیں، اور یہ کمانڈ چلائیں:

```bash
jupyter notebook
```

یا

```bash
jupyterhub
```

اس سے Jupyter انسٹینس شروع ہو جائے گا اور اس کا URL کمانڈ لائن ونڈو میں نظر آئے گا۔

جب آپ URL پر جائیں گے تو کورس آؤٹ لائن نظر آئے گی اور آپ کسی بھی `*.ipynb` فائل پر جا سکیں گے۔ مثلاً، `08-building-search-applications/python/oai-solution.ipynb`۔

## 3. اپنی API Keys شامل کریں

جب بھی کوئی ایپلیکیشن بنائیں، اپنی API keys کو محفوظ رکھنا بہت ضروری ہے۔ ہم تجویز کرتے ہیں کہ API keys کو براہ راست کوڈ میں نہ رکھیں۔ اگر یہ تفصیلات کسی پبلک ریپوزٹری میں چلی جائیں تو سیکیورٹی مسائل اور غیر ضروری اخراجات ہو سکتے ہیں۔
یہاں ایک مرحلہ وار رہنمائی ہے کہ Python کے لیے `.env` فائل کیسے بنائیں اور `GITHUB_TOKEN` کیسے شامل کریں:

1. **اپنے پروجیکٹ ڈائریکٹری میں جائیں**: ٹرمینل یا کمانڈ پرامپٹ کھولیں اور اس ڈائریکٹری میں جائیں جہاں آپ `.env` فائل بنانا چاہتے ہیں۔

   ```bash
   cd path/to/your/project
   ```

2. **`.env` فائل بنائیں**: اپنی پسندیدہ ٹیکسٹ ایڈیٹر سے نئی فائل بنائیں جس کا نام `.env` ہو۔ اگر کمانڈ لائن استعمال کر رہے ہیں تو `touch` (Unix-based systems پر) یا `echo` (Windows پر) استعمال کریں:

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` فائل ایڈٹ کریں**: `.env` فائل کو ٹیکسٹ ایڈیٹر میں کھولیں (جیسے VS Code، Notepad++ یا کوئی اور ایڈیٹر)۔ اس فائل میں یہ لائن شامل کریں، اور `your_github_token_here` کو اپنے اصل GitHub token سے بدل دیں:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **فائل کو محفوظ کریں**: تبدیلیاں محفوظ کریں اور ایڈیٹر بند کریں۔

5. **`python-dotenv` انسٹال کریں**: اگر پہلے انسٹال نہیں کیا تو `python-dotenv` پیکج انسٹال کریں تاکہ `.env` فائل سے انوائرنمنٹ ویریبلز Python ایپلیکیشن میں لوڈ ہو سکیں۔ `pip` سے انسٹال کریں:

   ```bash
   pip install python-dotenv
   ```

6. **Python اسکرپٹ میں انوائرنمنٹ ویریبلز لوڈ کریں**: اپنے Python اسکرپٹ میں `python-dotenv` پیکج استعمال کریں تاکہ `.env` فائل سے انوائرنمنٹ ویریبلز لوڈ ہو سکیں:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

بس! آپ نے کامیابی سے `.env` فائل بنائی، اپنا GitHub token شامل کیا، اور اسے Python ایپلیکیشن میں لوڈ کر لیا۔

🔐 کبھی بھی .env کو کمیٹ نہ کریں—یہ پہلے ہی .gitignore میں ہے۔
مکمل پرووائیڈر ہدایات [`providers.md`](03-providers.md) میں موجود ہیں۔

## 4. آگے کیا کرنا ہے؟

| میں چاہتا ہوں…         | جائیں…                                                                  |
|------------------------|-------------------------------------------------------------------------|
| سبق 1 شروع کریں        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM پرووائیڈر سیٹ اپ کریں | [`providers.md`](03-providers.md)                                       |
| دوسرے سیکھنے والوں سے ملیں | [ہمارے Discord میں شامل ہوں](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. مسائل اور حل

| مسئلہ                                      | حل                                                              |
|---------------------------------------------|-----------------------------------------------------------------|
| `python not found`                          | Python کو PATH میں شامل کریں یا انسٹال کے بعد ٹرمینل دوبارہ کھولیں|
| `pip` ونڈوز پر وہیلز نہیں بنا سکتا          | `pip install --upgrade pip setuptools wheel` پھر دوبارہ کوشش کریں|
| `ModuleNotFoundError: dotenv`               | `pip install -r requirements.txt` چلائیں (انوائرنمنٹ انسٹال نہیں ہوا)|
| Docker build fails *No space left*          | Docker Desktop ▸ *Settings* ▸ *Resources* → ڈسک سائز بڑھائیں    |
| VS Code بار بار دوبارہ کھولنے کا کہتا ہے     | شاید دونوں آپشنز ایکٹیو ہیں؛ ایک منتخب کریں (venv **یا** container)|
| OpenAI 401 / 429 errors                     | `OPENAI_API_KEY` ویلیو / ریکویسٹ ریٹ لمٹس چیک کریں              |
| Conda استعمال کرتے وقت ایررز                | Microsft AI لائبریریز انسٹال کریں: `conda install -c microsoft azure-ai-ml`|

---

**اعلانِ دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی بھرپور کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔