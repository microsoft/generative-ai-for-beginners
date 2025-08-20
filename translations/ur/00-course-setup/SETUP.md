<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:23:03+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ur"
}
-->
# اپنا ڈیولپمنٹ ماحول سیٹ اپ کریں

ہم نے اس ریپوزیٹری اور کورس کو ایک [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) کے ساتھ سیٹ اپ کیا ہے جس میں ایک یونیورسل رن ٹائم شامل ہے جو Python3، .NET، Node.js اور Java کی ڈیولپمنٹ کو سپورٹ کرتا ہے۔ متعلقہ کنفیگریشن `devcontainer.json` فائل میں دی گئی ہے جو اس ریپوزیٹری کی جڑ میں موجود `.devcontainer/` فولڈر میں ہے۔

dev container کو فعال کرنے کے لیے، اسے [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (کلاؤڈ ہوسٹڈ رن ٹائم کے لیے) یا [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (لوکل ڈیوائس پر رن ٹائم کے لیے) میں لانچ کریں۔ VS Code میں dev containers کے کام کرنے کے طریقہ کار کے بارے میں مزید جاننے کے لیے [یہ دستاویزات](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) پڑھیں۔  

> [!TIP]  
> ہم GitHub Codespaces استعمال کرنے کی سفارش کرتے ہیں کیونکہ یہ کم محنت میں جلد آغاز کے لیے بہترین ہے۔ یہ ذاتی اکاؤنٹس کے لیے ایک فراخدلانہ [مفت استعمال کوٹہ](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) فراہم کرتا ہے۔ اپنے کوٹہ کے استعمال کو زیادہ سے زیادہ کرنے کے لیے غیر فعال codespaces کو روکنے یا حذف کرنے کے لیے [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) کو ترتیب دیں۔


## 1. اسائنمنٹس کو چلانا

ہر سبق میں _اختیاری_ اسائنمنٹس ہو سکتے ہیں جو ایک یا زیادہ پروگرامنگ زبانوں میں دیے جا سکتے ہیں، جن میں شامل ہیں: Python، .NET/C#، Java اور JavaScript/TypeScript۔ یہ سیکشن ان اسائنمنٹس کو چلانے کے حوالے سے عمومی رہنمائی فراہم کرتا ہے۔

### 1.1 Python اسائنمنٹس

Python اسائنمنٹس یا تو ایپلیکیشنز (`.py` فائلیں) کی صورت میں دیے جاتے ہیں یا Jupyter notebooks (`.ipynb` فائلیں) کی شکل میں۔  
- نوٹ بک چلانے کے لیے، اسے Visual Studio Code میں کھولیں، پھر اوپر دائیں جانب _Select Kernel_ پر کلک کریں اور دکھائے گئے ڈیفالٹ Python 3 آپشن کو منتخب کریں۔ اب آپ _Run All_ کر کے نوٹ بک کو چلا سکتے ہیں۔  
- کمانڈ لائن سے Python ایپلیکیشنز چلانے کے لیے، اسائنمنٹ کی مخصوص ہدایات پر عمل کریں تاکہ درست فائلیں منتخب کریں اور مطلوبہ دلائل فراہم کریں۔

## 2. پرووائیڈرز کی کنفیگریشن

اسائنمنٹس **ممکن ہے** کہ ایک یا زیادہ Large Language Model (LLM) ڈپلائمنٹس کے خلاف کام کرنے کے لیے سیٹ اپ کیے گئے ہوں، جو OpenAI، Azure یا Hugging Face جیسے سپورٹڈ سروس پرووائیڈرز کے ذریعے فراہم کیے جاتے ہیں۔ یہ ایک _hosted endpoint_ (API) فراہم کرتے ہیں جس تک ہم مناسب اسناد (API key یا token) کے ساتھ پروگرام کے ذریعے رسائی حاصل کر سکتے ہیں۔ اس کورس میں ہم ان پرووائیڈرز پر بات کرتے ہیں:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مختلف ماڈلز کے ساتھ، جن میں کور GPT سیریز شامل ہے۔  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ماڈلز کے لیے، جس میں انٹرپرائز تیاری پر توجہ دی گئی ہے۔  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) اوپن سورس ماڈلز اور inference سرور کے لیے۔

**ان مشقوں کے لیے آپ کو اپنے ذاتی اکاؤنٹس استعمال کرنے ہوں گے**۔ اسائنمنٹس اختیاری ہیں، لہٰذا آپ اپنی دلچسپی کے مطابق ایک، تمام یا کوئی بھی پرووائیڈر سیٹ اپ کر سکتے ہیں۔ سائن اپ کے لیے کچھ رہنمائی:

| سائن اپ | قیمت | API کی | پلے گراؤنڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ کی بنیاد پر](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [نو-کوڈ، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب ہیں |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [رسائی کے لیے پہلے درخواست دینا ضروری ہے](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمتیں](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat میں محدود ماڈلز ہیں](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

اس ریپوزیٹری کو مختلف پرووائیڈرز کے ساتھ استعمال کے لیے _configure_ کرنے کے لیے نیچے دی گئی ہدایات پر عمل کریں۔ جو اسائنمنٹس کسی مخصوص پرووائیڈر کی ضرورت رکھتے ہیں ان کی فائل نیم میں درج ذیل ٹیگز میں سے کوئی ایک شامل ہوگا:  
 - `aoai` - Azure OpenAI endpoint، key کی ضرورت ہے  
 - `oai` - OpenAI endpoint، key کی ضرورت ہے  
 - `hf` - Hugging Face token کی ضرورت ہے  

آپ ایک، کوئی یا تمام پرووائیڈرز کو کنفیگر کر سکتے ہیں۔ متعلقہ اسائنمنٹس اسناد کی کمی پر ایرر دے دیں گے۔

###  2.1. `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے اوپر دی گئی رہنمائی پڑھ لی ہے، متعلقہ پرووائیڈر کے ساتھ سائن اپ کر لیا ہے، اور مطلوبہ تصدیقی اسناد (API_KEY یا token) حاصل کر لی ہیں۔ Azure OpenAI کے معاملے میں، ہم فرض کرتے ہیں کہ آپ کے پاس Azure OpenAI سروس (endpoint) کی ایک درست ڈپلائمنٹ ہے جس میں کم از کم ایک GPT ماڈل چیٹ کمپلیشن کے لیے تعینات ہے۔

اگلا قدم آپ کے **لوکل ماحول کے متغیرات** کو درج ذیل طریقے سے ترتیب دینا ہے:


1. جڑ فولڈر میں `.env.copy` فائل تلاش کریں جس میں مندرجہ ذیل مواد ہونا چاہیے:

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

2. اس فائل کو نیچے دیے گئے کمانڈ سے `.env` میں کاپی کریں۔ یہ فائل _gitignore-d_ ہے، جو رازوں کو محفوظ رکھتی ہے۔

   ```bash
   cp .env.copy .env
   ```

3. اقدار کو پر کریں (دائیں جانب `=` کے بعد موجود پلیس ہولڈرز کو تبدیل کریں) جیسا کہ اگلے سیکشن میں بیان کیا گیا ہے۔

3. (اختیاری) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ کے پاس ماحول کے متغیرات کو اس ریپوزیٹری سے منسلک _Codespaces secrets_ کے طور پر محفوظ کرنے کا اختیار ہے۔ اس صورت میں، آپ کو لوکل .env فائل سیٹ اپ کرنے کی ضرورت نہیں ہوگی۔ **تاہم، نوٹ کریں کہ یہ آپشن صرف GitHub Codespaces استعمال کرنے پر کام کرتا ہے۔** اگر آپ Docker Desktop استعمال کرتے ہیں تو پھر بھی .env فائل سیٹ اپ کرنا ضروری ہے۔


### 2.2. `.env` فائل کو بھرنا

آئیے متغیرات کے ناموں پر ایک نظر ڈالیں تاکہ سمجھ سکیں کہ وہ کیا ظاہر کرتے ہیں:

| متغیر  | وضاحت  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ وہ یوزر ایکسیس ٹوکن ہے جو آپ نے اپنے پروفائل میں سیٹ کیا ہے |
| OPENAI_API_KEY | یہ غیر Azure OpenAI endpoints کے لیے سروس استعمال کرنے کی اجازت دینے والی کلید ہے |
| AZURE_OPENAI_API_KEY | یہ اس سروس کے لیے اجازت دینے والی کلید ہے |
| AZURE_OPENAI_ENDPOINT | یہ Azure OpenAI ریسورس کے لیے تعینات کردہ endpoint ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _text generation_ ماڈل کی ڈپلائمنٹ endpoint ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _text embeddings_ ماڈل کی ڈپلائمنٹ endpoint ہے |
| | |

نوٹ: آخری دو Azure OpenAI متغیرات چیٹ کمپلیشن (ٹیکسٹ جنریشن) اور ویکٹر سرچ (ایمبیڈنگز) کے لیے ڈیفالٹ ماڈل کی نمائندگی کرتے ہیں۔ انہیں سیٹ کرنے کی ہدایات متعلقہ اسائنمنٹس میں دی جائیں گی۔


### 2.3 Azure کی کنفیگریشن: پورٹل سے

Azure OpenAI endpoint اور key کی قدریں [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملیں گی، تو آئیے وہاں سے شروع کرتے ہیں۔

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں  
1. سائڈبار (بائیں مینو) میں **Keys and Endpoint** آپشن پر کلک کریں۔  
1. **Show Keys** پر کلک کریں - آپ کو درج ذیل نظر آئے گا: KEY 1، KEY 2 اور Endpoint۔  
1. AZURE_OPENAI_API_KEY کے لیے KEY 1 کی ویلیو استعمال کریں۔  
1. AZURE_OPENAI_ENDPOINT کے لیے Endpoint کی ویلیو استعمال کریں۔  

اب ہمیں ان مخصوص ماڈلز کے endpoints کی ضرورت ہے جو ہم نے تعینات کیے ہیں۔

1. Azure OpenAI ریسورس کے لیے سائڈبار (بائیں مینو) میں **Model deployments** آپشن پر کلک کریں۔  
1. منزل کے صفحے پر، **Manage Deployments** پر کلک کریں۔  

یہ آپ کو Azure OpenAI Studio ویب سائٹ پر لے جائے گا، جہاں ہم نیچے بیان کردہ دیگر اقدار تلاش کریں گے۔

### 2.4 Azure کی کنفیگریشن: اسٹوڈیو سے

1. اوپر بیان کردہ طریقے سے اپنے ریسورس سے [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔  
1. موجودہ تعینات ماڈلز دیکھنے کے لیے سائڈبار (بائیں) میں **Deployments** ٹیب پر کلک کریں۔  
1. اگر آپ کا مطلوبہ ماڈل تعینات نہیں ہے، تو اسے تعینات کرنے کے لیے **Create new deployment** استعمال کریں۔  
1. آپ کو ایک _text-generation_ ماڈل کی ضرورت ہوگی - ہم سفارش کرتے ہیں: **gpt-35-turbo**  
1. آپ کو ایک _text-embedding_ ماڈل کی ضرورت ہوگی - ہم سفارش کرتے ہیں: **text-embedding-ada-002**  

اب ماحول کے متغیرات کو اپ ڈیٹ کریں تاکہ وہ استعمال شدہ _Deployment name_ کی عکاسی کریں۔ یہ عام طور پر ماڈل کے نام کے برابر ہوتا ہے جب تک کہ آپ نے اسے واضح طور پر تبدیل نہ کیا ہو۔ مثال کے طور پر، آپ کے پاس ہو سکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**کام مکمل ہونے پر .env فائل کو محفوظ کرنا نہ بھولیں**۔ اب آپ فائل سے باہر نکل سکتے ہیں اور نوٹ بک چلانے کی ہدایات پر واپس جا سکتے ہیں۔

### 2.5 OpenAI کی کنفیگریشن: پروفائل سے

آپ کی OpenAI API key آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں مل سکتی ہے۔ اگر آپ کے پاس نہیں ہے، تو آپ اکاؤنٹ بنا کر API key تخلیق کر سکتے ہیں۔ کلید حاصل کرنے کے بعد، آپ اسے `.env` فائل میں `OPENAI_API_KEY` متغیر میں بھر سکتے ہیں۔

### 2.6 Hugging Face کی کنفیگریشن: پروفائل سے

آپ کا Hugging Face ٹوکن آپ کے پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) کے تحت ملے گا۔ انہیں عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس کے بجائے، اس پروجیکٹ کے استعمال کے لیے نیا ٹوکن بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` متغیر کے تحت کاپی کریں۔ _نوٹ:_ یہ تکنیکی طور پر API key نہیں ہے لیکن تصدیق کے لیے استعمال ہوتا ہے، اس لیے ہم تسلسل کے لیے اسی نام کا استعمال کر رہے ہیں۔

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔