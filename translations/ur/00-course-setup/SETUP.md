<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:42:17+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ur"
}
-->
# اپنا ڈویلپمنٹ ماحول سیٹ اپ کریں

ہم نے اس ریپوزیٹری اور کورس کو [ڈویلپمنٹ کنٹینر](https://containers.dev?WT.mc_id=academic-105485-koreyst) کے ساتھ سیٹ اپ کیا ہے جس میں یونیورسل رن ٹائم ہے جو Python3، .NET، Node.js اور Java ڈویلپمنٹ کو سپورٹ کر سکتا ہے۔ متعلقہ کنفیگریشن `devcontainer.json` فائل میں بیان کی گئی ہے جو اس ریپوزیٹری کے روٹ پر `.devcontainer/` فولڈر میں واقع ہے۔

ڈویلپمنٹ کنٹینر کو فعال کرنے کے لیے، اسے [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (کلاؤڈ پر مبنی رن ٹائم کے لیے) یا [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (لوکل ڈیوائس پر مبنی رن ٹائم کے لیے) میں لانچ کریں۔ VS Code میں ڈویلپمنٹ کنٹینرز کے کام کرنے کے طریقے پر مزید تفصیلات کے لیے [یہ دستاویز](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) پڑھیں۔

> [!TIP]  
> ہم کم سے کم کوشش کے ساتھ جلدی شروع کرنے کے لیے GitHub Codespaces استعمال کرنے کی سفارش کرتے ہیں۔ یہ ذاتی اکاؤنٹس کے لیے فراخ [مفت استعمال کوٹہ](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) فراہم کرتا ہے۔ اپنے کوٹہ کے استعمال کو زیادہ سے زیادہ کرنے کے لیے غیر فعال کوڈ اسپیسز کو روکنے یا حذف کرنے کے لیے [ٹائم آؤٹس](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) کو ترتیب دیں۔

## 1. اسائنمنٹس کو چلانا

ہر سبق میں _اختیاری_ اسائنمنٹس ہوں گے جو ایک یا زیادہ پروگرامنگ زبانوں میں فراہم کیے جا سکتے ہیں جن میں شامل ہیں: Python، .NET/C#، Java اور JavaScript/TypeScript۔ یہ سیکشن ان اسائنمنٹس کو چلانے سے متعلق عمومی رہنمائی فراہم کرتا ہے۔

### 1.1 Python اسائنمنٹس

Python اسائنمنٹس یا تو ایپلی کیشنز (`.py` فائلیں) یا Jupyter نوٹ بکس (`.ipynb` فائلیں) کے طور پر فراہم کی جاتی ہیں۔
- نوٹ بک چلانے کے لیے، اسے Visual Studio Code میں کھولیں پھر _Select Kernel_ (اوپر دائیں جانب) پر کلک کریں اور دکھائی جانے والی ڈیفالٹ Python 3 آپشن کو منتخب کریں۔ اب آپ نوٹ بک کو چلانے کے لیے _Run All_ کر سکتے ہیں۔
- کمانڈ لائن سے Python ایپلی کیشنز چلانے کے لیے، اسائنمنٹ کی مخصوص ہدایات پر عمل کریں تاکہ یہ یقینی بنایا جا سکے کہ آپ صحیح فائلوں کو منتخب کریں اور مطلوبہ دلائل فراہم کریں۔

## 2. فراہم کنندگان کو ترتیب دینا

اسائنمنٹس **ممکنہ طور پر** ایک یا زیادہ بڑے زبان ماڈل (LLM) تعیناتیوں کے خلاف کام کرنے کے لیے ایک معاون سروس فراہم کنندہ جیسے OpenAI، Azure یا Hugging Face کے ذریعے سیٹ اپ کی جا سکتی ہیں۔ یہ ایک _ہوسٹڈ اینڈ پوائنٹ_ (API) فراہم کرتے ہیں جسے ہم صحیح اسناد (API کلید یا ٹوکن) کے ساتھ پروگرام کے ذریعے رسائی حاصل کر سکتے ہیں۔ اس کورس میں، ہم ان فراہم کنندگان پر بات کرتے ہیں:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مختلف ماڈلز کے ساتھ، جن میں کور GPT سیریز شامل ہے۔
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ماڈلز کے لیے جو انٹرپرائز تیاری پر مرکوز ہیں۔
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) اوپن سورس ماڈلز اور انفرنس سرور کے لیے۔

**آپ کو ان مشقوں کے لیے اپنے اکاؤنٹس استعمال کرنے کی ضرورت ہوگی**۔ اسائنمنٹس اختیاری ہیں لہذا آپ اپنی دلچسپیوں کی بنیاد پر ایک، سب - یا کوئی بھی فراہم کنندہ سیٹ اپ کرنے کا انتخاب کر سکتے ہیں۔ سائن اپ کے لیے کچھ رہنمائی:

| سائن اپ | لاگت | API کلید | پلے گراؤنڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمت](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ پر مبنی](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [نو کوڈ، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب ہیں |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمت](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK کوئیک اسٹارٹ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [اسٹوڈیو کوئیک اسٹارٹ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [رسائی کے لیے پیشگی درخواست دینی ہوگی](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمت](https://huggingface.co/pricing) | [رسائی ٹوکن](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat کے پاس محدود ماڈلز ہیں](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

نیچے دی گئی ہدایات پر عمل کریں تاکہ مختلف فراہم کنندگان کے ساتھ استعمال کے لیے اس ریپوزیٹری کو _ترتیب_ دیں۔ اسائنمنٹس جنہیں کسی مخصوص فراہم کنندہ کی ضرورت ہوتی ہے ان کے فائل نام میں ان میں سے کوئی ایک ٹیگ شامل ہوگا:
- `aoai` - Azure OpenAI اینڈ پوائنٹ، کلید کی ضرورت ہے
- `oai` - OpenAI اینڈ پوائنٹ، کلید کی ضرورت ہے
- `hf` - Hugging Face ٹوکن کی ضرورت ہے

آپ ایک، کوئی بھی، یا تمام فراہم کنندگان کو ترتیب دے سکتے ہیں۔ متعلقہ اسائنمنٹس صرف اسناد کی کمی پر غلطی کریں گے۔

### 2.1. `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے پہلے ہی اوپر دی گئی رہنمائی کو پڑھ لیا ہے اور متعلقہ فراہم کنندہ کے ساتھ سائن اپ کیا ہے، اور مطلوبہ تصدیقی اسناد (API_KEY یا ٹوکن) حاصل کر لی ہیں۔ Azure OpenAI کے معاملے میں، ہم فرض کرتے ہیں کہ آپ کے پاس کم از کم ایک GPT ماڈل کے ساتھ Azure OpenAI سروس (اینڈ پوائنٹ) کی ایک درست تعیناتی بھی ہے جو چیٹ کمپلیشن کے لیے تعینات ہے۔

اگلا مرحلہ آپ کے **مقامی ماحول کے متغیرات** کو درج ذیل کے طور پر ترتیب دینا ہے:

1. روٹ فولڈر میں `.env.copy` فائل تلاش کریں جس کے مواد کچھ اس طرح ہوں:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ذیل کے کمانڈ کا استعمال کرتے ہوئے اس فائل کو `.env` میں کاپی کریں۔ یہ فائل _gitignore-d_ ہے، جو رازوں کو محفوظ رکھتی ہے۔

   ```bash
   cp .env.copy .env
   ```

3. اگلے سیکشن میں بیان کردہ کے مطابق اقدار کو بھریں (پلیس ہولڈرز کو `=` کے دائیں جانب تبدیل کریں)۔

3. (آپشن) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ کے پاس اس ریپوزیٹری کے ساتھ وابستہ _Codespaces secrets_ کے طور پر ماحول کے متغیرات کو محفوظ کرنے کا اختیار ہوتا ہے۔ اس صورت میں، آپ کو مقامی .env فائل ترتیب دینے کی ضرورت نہیں ہوگی۔ **تاہم، نوٹ کریں کہ یہ آپشن صرف اس صورت میں کام کرتا ہے جب آپ GitHub Codespaces استعمال کرتے ہیں۔** آپ کو پھر بھی Docker Desktop استعمال کرنے کی صورت میں .env فائل ترتیب دینی ہوگی۔

### 2.2. `.env` فائل کو بھرنا

متغیر ناموں کو سمجھنے کے لیے ایک مختصر نظر ڈالیں کہ وہ کیا نمائندگی کرتے ہیں:

| متغیر | وضاحت |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ آپ کے پروفائل میں سیٹ اپ کردہ صارف رسائی ٹوکن ہے |
| OPENAI_API_KEY | غیر Azure OpenAI اینڈ پوائنٹس کے لیے سروس استعمال کرنے کی اجازت کلید ہے |
| AZURE_OPENAI_API_KEY | اس سروس کو استعمال کرنے کی اجازت کلید ہے |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI وسائل کے لیے تعینات اینڈ پوائنٹ ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _ٹیکسٹ جنریشن_ ماڈل تعیناتی اینڈ پوائنٹ ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _ٹیکسٹ ایمبیڈنگز_ ماڈل تعیناتی اینڈ پوائنٹ ہے |
| | |

نوٹ: آخری دو Azure OpenAI متغیرات بالترتیب چیٹ کمپلیشن (ٹیکسٹ جنریشن) اور وییکٹر سرچ (ایمبیڈنگز) کے لیے ایک ڈیفالٹ ماڈل کی عکاسی کرتے ہیں۔ ان کو ترتیب دینے کے لیے ہدایات متعلقہ اسائنمنٹس میں بیان کی جائیں گی۔

### 2.3 Azure کو ترتیب دیں: پورٹل سے

Azure OpenAI اینڈ پوائنٹ اور کلیدی اقدار [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملیں گی، تو آئیے وہاں سے شروع کریں۔

1. [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔
1. سائڈبار (بائیں مینو) میں **Keys and Endpoint** آپشن پر کلک کریں۔
1. **Show Keys** پر کلک کریں - آپ کو درج ذیل نظر آنا چاہیے: KEY 1، KEY 2 اور اینڈ پوائنٹ۔
1. AZURE_OPENAI_API_KEY کے لیے KEY 1 قدر استعمال کریں۔
1. AZURE_OPENAI_ENDPOINT کے لیے اینڈ پوائنٹ قدر استعمال کریں۔

اگلا، ہمیں ان مخصوص ماڈلز کے لیے اینڈ پوائنٹس کی ضرورت ہے جنہیں ہم نے تعینات کیا ہے۔

1. Azure OpenAI وسائل کے لیے سائڈبار (بائیں مینو) میں **Model deployments** آپشن پر کلک کریں۔
1. منزل کے صفحے پر، **Manage Deployments** پر کلک کریں۔

یہ آپ کو Azure OpenAI اسٹوڈیو ویب سائٹ پر لے جائے گا، جہاں ہم نیچے بیان کردہ دیگر اقدار کو تلاش کریں گے۔

### 2.4 Azure کو ترتیب دیں: اسٹوڈیو سے

1. [Azure OpenAI اسٹوڈیو](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) پر **اپنے وسائل سے** نیویگیٹ کریں جیسا کہ اوپر بیان کیا گیا ہے۔
1. موجودہ تعینات شدہ ماڈلز کو دیکھنے کے لیے **Deployments** ٹیب (سائڈبار، بائیں) پر کلک کریں۔
1. اگر آپ کا مطلوبہ ماڈل تعینات نہیں ہے، تو اسے تعینات کرنے کے لیے **Create new deployment** استعمال کریں۔
1. آپ کو ایک _ٹیکسٹ جنریشن_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں: **gpt-35-turbo**
1. آپ کو ایک _ٹیکسٹ ایمبیڈنگ_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں **text-embedding-ada-002**

اب ماحول کے متغیرات کو تعیناتی نام کی عکاسی کرنے کے لیے اپ ڈیٹ کریں۔ یہ عام طور پر ماڈل نام کے برابر ہوگا جب تک کہ آپ نے اسے واضح طور پر تبدیل نہ کیا ہو۔ لہذا، مثال کے طور پر، آپ کے پاس ہوسکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**جب مکمل ہو جائے تو .env فائل کو محفوظ کرنا نہ بھولیں**۔ آپ اب فائل سے باہر نکل سکتے ہیں اور نوٹ بک کو چلانے کی ہدایات پر واپس جا سکتے ہیں۔

### 2.5 OpenAI کو ترتیب دیں: پروفائل سے

آپ کی OpenAI API کلید آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں مل سکتی ہے۔ اگر آپ کے پاس نہیں ہے، تو آپ ایک اکاؤنٹ کے لیے سائن اپ کر سکتے ہیں اور ایک API کلید بنا سکتے ہیں۔ کلید حاصل کرنے کے بعد، آپ اسے `.env` فائل میں `OPENAI_API_KEY` متغیر کو بھرنے کے لیے استعمال کر سکتے ہیں۔

### 2.6 Hugging Face کو ترتیب دیں: پروفائل سے

آپ کا Hugging Face ٹوکن آپ کے پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) کے تحت مل سکتا ہے۔ انہیں عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس منصوبے کے استعمال کے لیے ایک نیا ٹوکن بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` متغیر کے تحت کاپی کریں۔ _نوٹ:_ یہ تکنیکی طور پر ایک API کلید نہیں ہے لیکن تصدیق کے لیے استعمال ہوتا ہے لہذا ہم مستقل مزاجی کے لیے وہ نام رکھنے کا کنونشن استعمال کر رہے ہیں۔

**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔