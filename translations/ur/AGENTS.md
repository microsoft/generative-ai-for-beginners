<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:52:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ur"
}
-->
# AGENTS.md

## پروجیکٹ کا جائزہ

یہ ریپوزیٹری ایک جامع 21-سبق نصاب پر مشتمل ہے جو جنریٹو AI کی بنیادی باتیں اور ایپلیکیشن ڈیولپمنٹ سکھاتا ہے۔ یہ کورس ابتدائی افراد کے لیے ڈیزائن کیا گیا ہے اور بنیادی تصورات سے لے کر پروڈکشن کے لیے تیار ایپلیکیشنز بنانے تک سب کچھ شامل کرتا ہے۔

**اہم ٹیکنالوجیز:**
- Python 3.9+ کے ساتھ لائبریریاں: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript کے ساتھ Node.js اور لائبریریاں: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service، OpenAI API، اور GitHub Models
- انٹرایکٹو لرننگ کے لیے Jupyter Notebooks
- مستقل ڈیولپمنٹ ماحول کے لیے Dev Containers

**ریپوزیٹری کی ساخت:**
- 21 نمبر والے سبق کی ڈائریکٹریز (00-21) جن میں READMEs، کوڈ مثالیں، اور اسائنمنٹس شامل ہیں
- متعدد امپلیمنٹیشنز: Python، TypeScript، اور کبھی کبھار .NET مثالیں
- ترجمہ کی ڈائریکٹری 40+ زبانوں کے ورژنز کے ساتھ
- مرکزی کنفیگریشن `.env` فائل کے ذریعے (`.env.copy` کو ٹیمپلیٹ کے طور پر استعمال کریں)

## سیٹ اپ کمانڈز

### ابتدائی ریپوزیٹری سیٹ اپ

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python ماحول کی سیٹ اپ

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript سیٹ اپ

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container سیٹ اپ (تجویز کردہ)

ریپوزیٹری میں GitHub Codespaces یا VS Code Dev Containers کے لیے `.devcontainer` کنفیگریشن شامل ہے:

1. ریپوزیٹری کو GitHub Codespaces یا VS Code میں Dev Containers ایکسٹینشن کے ساتھ کھولیں
2. Dev Container خود بخود:
   - Python کی ضروریات `requirements.txt` سے انسٹال کرے گا
   - پوسٹ-کریٹ اسکرپٹ (`.devcontainer/post-create.sh`) چلائے گا
   - Jupyter kernel سیٹ اپ کرے گا

## ڈیولپمنٹ ورک فلو

### ماحول کے متغیرات

تمام سبق جو API تک رسائی کی ضرورت رکھتے ہیں، `.env` میں بیان کردہ ماحول کے متغیرات استعمال کرتے ہیں:

- `OPENAI_API_KEY` - OpenAI API کے لیے
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service کے لیے
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT` - چیٹ کمپلیشن ماڈل ڈیپلائمنٹ کا نام
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - ایمبیڈنگ ماڈل ڈیپلائمنٹ کا نام
- `AZURE_OPENAI_API_VERSION` - API ورژن (ڈیفالٹ: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face ماڈلز کے لیے
- `GITHUB_TOKEN` - GitHub Models کے لیے

### Python مثالیں چلانا

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript مثالیں چلانا

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks کے ساتھ کام کرنا

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### مختلف قسم کے اسباق کے ساتھ کام کرنا

- **"Learn" اسباق**: README.md دستاویزات اور تصورات پر توجہ مرکوز کریں
- **"Build" اسباق**: Python اور TypeScript میں کام کرنے والے کوڈ کی مثالیں شامل کریں
- ہر سبق میں README.md ہوتا ہے جس میں تھیوری، کوڈ واک تھرو، اور ویڈیو مواد کے لنکس شامل ہیں

## کوڈ اسٹائل گائیڈ لائنز

### Python

- ماحول کے متغیرات کے انتظام کے لیے `python-dotenv` استعمال کریں
- API تعاملات کے لیے `openai` لائبریری درآمد کریں
- لنٹنگ کے لیے `pylint` استعمال کریں (کچھ مثالوں میں سادگی کے لیے `# pylint: disable=all` شامل ہے)
- PEP 8 نام دینے کے اصولوں پر عمل کریں
- API کی اسناد کو `.env` فائل میں اسٹور کریں، کبھی کوڈ میں نہیں

### TypeScript

- ماحول کے متغیرات کے لیے `dotenv` پیکج استعمال کریں
- ہر ایپ کے لیے `tsconfig.json` میں TypeScript کنفیگریشن
- Azure سروسز کے لیے `@azure/openai` یا `@azure-rest/ai-inference` استعمال کریں
- آٹو ری لوڈ کے ساتھ ڈیولپمنٹ کے لیے `nodemon` استعمال کریں
- چلانے سے پہلے بلڈ کریں: `npm run build` پھر `npm start`

### عمومی اصول

- کوڈ کی مثالیں سادہ اور تعلیمی رکھیں
- کلیدی تصورات کی وضاحت کرنے والے تبصرے شامل کریں
- ہر سبق کا کوڈ خود مختار اور چلنے کے قابل ہونا چاہیے
- مستقل نام استعمال کریں: Azure OpenAI کے لیے `aoai-`، OpenAI API کے لیے `oai-`، GitHub Models کے لیے `githubmodels-`

## دستاویزات کے اصول

### Markdown اسٹائل

- تمام URLs کو `[text](../../url)` فارمیٹ میں لپیٹیں، اضافی اسپیس کے بغیر
- رشتہ دار لنکس `./` یا `../` سے شروع ہونے چاہئیں
- Microsoft ڈومینز کے تمام لنکس میں ٹریکنگ ID شامل ہونا چاہیے: `?WT.mc_id=academic-105485-koreyst`
- URLs میں ملک کے مخصوص لوکلز نہ ہوں (جیسے `/en-us/` سے گریز کریں)
- تصاویر `./images` فولڈر میں وضاحتی ناموں کے ساتھ اسٹور کریں
- فائل ناموں میں انگریزی حروف، نمبر، اور ڈیشز استعمال کریں

### ترجمہ کی حمایت

- ریپوزیٹری GitHub Actions کے ذریعے 40+ زبانوں کی حمایت کرتی ہے
- ترجمے `translations/` ڈائریکٹری میں اسٹور کیے جاتے ہیں
- جزوی ترجمے جمع نہ کریں
- مشین ترجمے قبول نہیں کیے جاتے
- ترجمہ شدہ تصاویر `translated_images/` ڈائریکٹری میں اسٹور کی جاتی ہیں

## ٹیسٹنگ اور ویلیڈیشن

### جمع کرانے سے پہلے چیک کریں

یہ ریپوزیٹری GitHub Actions کو ویلیڈیشن کے لیے استعمال کرتی ہے۔ PRs جمع کرانے سے پہلے:

1. **Markdown لنکس چیک کریں**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **دستی ٹیسٹنگ**:
   - Python مثالیں ٹیسٹ کریں: venv کو ایکٹیویٹ کریں اور اسکرپٹس چلائیں
   - TypeScript مثالیں ٹیسٹ کریں: `npm install`, `npm run build`, `npm start`
   - تصدیق کریں کہ ماحول کے متغیرات صحیح طریقے سے کنفیگر کیے گئے ہیں
   - چیک کریں کہ API کیز کوڈ کی مثالوں کے ساتھ کام کرتی ہیں

3. **کوڈ کی مثالیں**:
   - یقینی بنائیں کہ تمام کوڈ بغیر کسی غلطی کے چلتا ہے
   - Azure OpenAI اور OpenAI API دونوں کے ساتھ ٹیسٹ کریں جہاں قابل اطلاق ہو
   - تصدیق کریں کہ مثالیں GitHub Models کے ساتھ کام کرتی ہیں جہاں سپورٹ ہو

### کوئی خودکار ٹیسٹ نہیں

یہ ایک تعلیمی ریپوزیٹری ہے جو ٹیوٹوریلز اور مثالوں پر مرکوز ہے۔ کوئی یونٹ ٹیسٹ یا انٹیگریشن ٹیسٹ چلانے کے لیے نہیں ہیں۔ ویلیڈیشن بنیادی طور پر:
- کوڈ کی مثالوں کی دستی جانچ
- Markdown ویلیڈیشن کے لیے GitHub Actions
- تعلیمی مواد کا کمیونٹی جائزہ

## پل ریکویسٹ گائیڈ لائنز

### جمع کرانے سے پہلے

1. Python اور TypeScript دونوں میں کوڈ تبدیلیاں ٹیسٹ کریں جہاں قابل اطلاق ہو
2. Markdown ویلیڈیشن چلائیں (PR پر خود بخود ٹرگر ہوتا ہے)
3. Microsoft URLs پر ٹریکنگ IDs موجود ہونے کو یقینی بنائیں
4. چیک کریں کہ رشتہ دار لنکس درست ہیں
5. تصدیق کریں کہ تصاویر صحیح طریقے سے حوالہ دی گئی ہیں

### PR عنوان فارمیٹ

- وضاحتی عنوانات استعمال کریں: `[Lesson 06] Fix Python example typo` یا `Update README for lesson 08`
- مسئلہ نمبر کا حوالہ دیں جہاں قابل اطلاق ہو: `Fixes #123`

### PR تفصیل

- وضاحت کریں کہ کیا تبدیل کیا گیا اور کیوں
- متعلقہ مسائل کے لنکس دیں
- کوڈ تبدیلیوں کے لیے، وضاحت کریں کہ کون سی مثالیں ٹیسٹ کی گئیں
- ترجمہ PRs کے لیے، تمام فائلیں مکمل ترجمے کے ساتھ شامل کریں

### شراکت کی ضروریات

- Microsoft CLA پر دستخط کریں (پہلے PR پر خودکار)
- ریپوزیٹری کو اپنی اکاؤنٹ میں فورک کریں اور پھر تبدیلیاں کریں
- ایک PR فی منطقی تبدیلی (غیر متعلقہ اصلاحات کو نہ ملائیں)
- PRs کو مرکوز اور چھوٹا رکھیں جہاں ممکن ہو

## عمومی ورک فلو

### نئی کوڈ مثال شامل کرنا

1. متعلقہ سبق کی ڈائریکٹری پر جائیں
2. مثال `python/` یا `typescript/` سب ڈائریکٹری میں بنائیں
3. نام دینے کا اصول اپنائیں: `{provider}-{example-name}.{py|ts|js}`
4. حقیقی API اسناد کے ساتھ ٹیسٹ کریں
5. سبق README میں کسی نئے ماحول کے متغیرات کو دستاویز کریں

### دستاویزات کو اپ ڈیٹ کرنا

1. سبق کی ڈائریکٹری میں README.md کو ایڈٹ کریں
2. Markdown اصولوں پر عمل کریں (ٹریکنگ IDs، رشتہ دار لنکس)
3. ترجمے GitHub Actions کے ذریعے ہینڈل کیے جاتے ہیں (دستی طور پر ایڈٹ نہ کریں)
4. تمام لنکس کے درست ہونے کو ٹیسٹ کریں

### Dev Containers کے ساتھ کام کرنا

1. ریپوزیٹری میں `.devcontainer/devcontainer.json` شامل ہے
2. پوسٹ-کریٹ اسکرپٹ خود بخود Python کی ضروریات انسٹال کرتا ہے
3. Python اور Jupyter کے لیے ایکسٹینشنز پہلے سے کنفیگر ہیں
4. ماحول `mcr.microsoft.com/devcontainers/universal:2.11.2` پر مبنی ہے

## ڈیپلائمنٹ اور پبلشنگ

یہ ایک لرننگ ریپوزیٹری ہے - کوئی ڈیپلائمنٹ پروسیس نہیں ہے۔ نصاب استعمال کیا جاتا ہے:

1. **GitHub ریپوزیٹری**: کوڈ اور دستاویزات تک براہ راست رسائی
2. **GitHub Codespaces**: پہلے سے کنفیگر سیٹ اپ کے ساتھ فوری ڈیولپمنٹ ماحول
3. **Microsoft Learn**: مواد کو آفیشل لرننگ پلیٹ فارم پر سنڈیکیٹ کیا جا سکتا ہے
4. **docsify**: Markdown سے بنی دستاویزات کی سائٹ (دیکھیں `docsifytopdf.js` اور `package.json`)

### دستاویزات سائٹ بنانا

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## مسائل کا حل

### عام مسائل

**Python درآمد کی غلطیاں**:
- یقینی بنائیں کہ ورچوئل ماحول ایکٹیویٹ ہے
- `pip install -r requirements.txt` چلائیں
- Python ورژن 3.9+ چیک کریں

**TypeScript بلڈ کی غلطیاں**:
- مخصوص ایپ ڈائریکٹری میں `npm install` چلائیں
- Node.js ورژن مطابقت پذیر ہے چیک کریں
- `node_modules` کو صاف کریں اور دوبارہ انسٹال کریں اگر ضرورت ہو

**API تصدیق کی غلطیاں**:
- تصدیق کریں کہ `.env` فائل موجود ہے اور درست ویلیوز رکھتی ہے
- چیک کریں کہ API کیز درست ہیں اور ختم نہیں ہوئیں
- یقینی بنائیں کہ endpoint URLs آپ کے علاقے کے لیے درست ہیں

**ماحول کے متغیرات غائب ہیں**:
- `.env.copy` کو `.env` میں کاپی کریں
- سبق کے لیے تمام مطلوبہ ویلیوز بھریں جس پر آپ کام کر رہے ہیں
- `.env` کو اپ ڈیٹ کرنے کے بعد اپنی ایپلیکیشن کو دوبارہ شروع کریں

## اضافی وسائل

- [کورس سیٹ اپ گائیڈ](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [شراکت کی گائیڈ لائنز](./CONTRIBUTING.md)
- [کوڈ آف کنڈکٹ](./CODE_OF_CONDUCT.md)
- [سیکیورٹی پالیسی](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [ایڈوانسڈ کوڈ سیمپلز کا مجموعہ](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## پروجیکٹ کے مخصوص نوٹس

- یہ ایک **تعلیمی ریپوزیٹری** ہے جو لرننگ پر مرکوز ہے، پروڈکشن کوڈ پر نہیں
- مثالیں جان بوجھ کر سادہ اور تصورات سکھانے پر مرکوز ہیں
- کوڈ کا معیار تعلیمی وضاحت کے ساتھ متوازن ہے
- ہر سبق خود مختار ہے اور آزادانہ طور پر مکمل کیا جا سکتا ہے
- ریپوزیٹری متعدد API فراہم کنندگان کی حمایت کرتی ہے: Azure OpenAI، OpenAI، اور GitHub Models
- مواد کثیر لسانی ہے اور خودکار ترجمہ ورک فلو کے ساتھ ہے
- سوالات اور سپورٹ کے لیے Discord پر فعال کمیونٹی

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔