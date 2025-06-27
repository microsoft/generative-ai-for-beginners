<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:08:06+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ur"
}
-->
# اپنا ڈیولپمنٹ ماحول ترتیب دیں

ہم نے اس ریپوزٹری اور کورس کو ایک [ڈیولپمنٹ کنٹینر](https://containers.dev?WT.mc_id=academic-105485-koreyst) کے ساتھ ترتیب دیا ہے جس میں ایک یونیورسل رن ٹائم ہے جو Python3، .NET، Node.js اور Java ڈیولپمنٹ کی حمایت کرتا ہے۔ متعلقہ کنفیگریشن `devcontainer.json` فائل میں بیان کی گئی ہے جو اس ریپوزٹری کی روٹ پر `.devcontainer/` فولڈر میں واقع ہے۔

ڈیولپمنٹ کنٹینر کو فعال کرنے کے لیے، اسے [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (کلاؤڈ ہوسٹڈ رن ٹائم کے لیے) یا [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (مقامی ڈیوائس ہوسٹڈ رن ٹائم کے لیے) میں لانچ کریں۔ مزید تفصیلات کے لیے [یہ دستاویز](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) پڑھیں کہ کس طرح ڈیولپمنٹ کنٹینرز VS کوڈ میں کام کرتے ہیں۔

> [!TIP]  
> ہم تجویز کرتے ہیں کہ GitHub Codespaces کو تیز آغاز کے لیے استعمال کریں جس میں کم سے کم کوشش کی ضرورت ہو۔ یہ ذاتی اکاؤنٹس کے لیے ایک فراخ [مفت استعمال کوٹہ](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) فراہم کرتا ہے۔ [ٹائم آؤٹس](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) کو ترتیب دیں تاکہ غیر فعال کوڈ اسپیسز کو روکنے یا حذف کرنے سے آپ کے کوٹہ کے استعمال کو زیادہ سے زیادہ بنایا جا سکے۔

## 1. اسائنمنٹس کو چلانا

ہر سبق میں _اختیاری_ اسائنمنٹس ہوں گے جو ایک یا زیادہ پروگرامنگ زبانوں میں فراہم کیے جا سکتے ہیں، جن میں Python، .NET/C#, Java اور JavaScript/TypeScript شامل ہیں۔ یہ سیکشن ان اسائنمنٹس کو چلانے سے متعلق عمومی رہنمائی فراہم کرتا ہے۔

### 1.1 Python اسائنمنٹس

Python اسائنمنٹس ایپلی کیشنز (`.py` فائلیں) یا Jupyter نوٹ بکس (`.ipynb` فائلیں) کے طور پر فراہم کی جاتی ہیں۔
- نوٹ بک کو چلانے کے لیے، اسے Visual Studio Code میں کھولیں پھر _Select Kernel_ (اوپر دائیں طرف) پر کلک کریں اور دکھائی گئی ڈیفالٹ Python 3 آپشن کو منتخب کریں۔ آپ اب _Run All_ کر کے نوٹ بک کو چلا سکتے ہیں۔
- کمانڈ لائن سے Python ایپلی کیشنز چلانے کے لیے، اسائنمنٹ کے مخصوص ہدایات پر عمل کریں تاکہ آپ صحیح فائلوں کو منتخب کریں اور مطلوبہ دلائل فراہم کریں۔

## 2. فراہم کنندگان کو ترتیب دینا

اسائنمنٹس **ایک یا زیادہ بڑے زبان ماڈل (LLM) کی تعیناتیوں کے خلاف کام کرنے کے لیے** بھی ترتیب دی جا سکتی ہیں، جیسے کہ OpenAI، Azure یا Hugging Face جیسے سپورٹ شدہ سروس فراہم کنندگان کے ذریعے۔ یہ ایک _میزبان اینڈپوائنٹ_ (API) فراہم کرتے ہیں جس تک ہم صحیح اسناد (API کلید یا ٹوکن) کے ساتھ پروگرام کے ذریعے رسائی حاصل کر سکتے ہیں۔ اس کورس میں، ہم ان فراہم کنندگان پر بات کرتے ہیں:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مختلف ماڈلز کے ساتھ بشمول کور GPT سیریز۔
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ماڈلز کے لیے جو انٹرپرائز ریڈی نیس پر فوکس کرتے ہیں
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) اوپن سورس ماڈلز اور انفرینس سرور کے لیے

**آپ کو ان مشقوں کے لیے اپنے اکاؤنٹس کا استعمال کرنا ہوگا**۔ اسائنمنٹس اختیاری ہیں لہذا آپ اپنے دلچسپی کے مطابق ایک، سب - یا کوئی بھی فراہم کنندہ ترتیب دے سکتے ہیں۔ سائن اپ کے لیے کچھ رہنمائی:

| سائن اپ | لاگت | API کلید | پلے گراؤنڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ پر مبنی](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [کوڈ کے بغیر، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK فوری آغاز](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [اسٹوڈیو فوری آغاز](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [رسائی کے لیے پہلے سے درخواست دینی ہوگی](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمتیں](https://huggingface.co/pricing) | [رسائی ٹوکن](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat میں محدود ماڈلز ہیں](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

نیچے دی گئی ہدایات پر عمل کریں تاکہ مختلف فراہم کنندگان کے ساتھ استعمال کے لیے اس ریپوزٹری کو _ترتیب دیں_۔ اسائنمنٹس جنہیں کسی مخصوص فراہم کنندہ کی ضرورت ہوگی ان کے فائل نام میں ان میں سے ایک ٹیگ ہوگا:
 - `aoai` - Azure OpenAI اینڈپوائنٹ، کلید کی ضرورت ہے
 - `oai` - OpenAI اینڈپوائنٹ، کلید کی ضرورت ہے
 - `hf` - Hugging Face ٹوکن کی ضرورت ہے

آپ ایک، کوئی، یا تمام فراہم کنندگان کو ترتیب دے سکتے ہیں۔ متعلقہ اسائنمنٹس صرف اسناد کی کمی پر غلطی کریں گے۔

###  2.1. `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے اوپر دی گئی رہنمائی پڑھ لی ہے اور متعلقہ فراہم کنندہ کے ساتھ سائن اپ کر لیا ہے، اور مطلوبہ تصدیقی اسناد (API_KEY یا ٹوکن) حاصل کر لی ہیں۔ Azure OpenAI کے معاملے میں، ہم فرض کرتے ہیں کہ آپ کے پاس کم از کم ایک GPT ماڈل کے ساتھ Azure OpenAI سروس (اینڈپوائنٹ) کی ایک درست تعیناتی ہے۔

اگلا قدم یہ ہے کہ اپنے **مقامی ماحول کے متغیرات** کو درج ذیل طور پر ترتیب دیں:

1. روٹ فولڈر میں `.env.copy` فائل تلاش کریں جس کے مواد کچھ اس طرح ہونے چاہئیں:

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

2. اس فائل کو `.env` میں نیچے دیے گئے کمانڈ کا استعمال کرتے ہوئے کاپی کریں۔ یہ فائل _gitignore-d_ ہے، راز کو محفوظ رکھتے ہوئے۔

   ```bash
   cp .env.copy .env
   ```

3. اگلے سیکشن میں بیان کردہ طور پر اقدار کو بھریں (دائیں جانب `=` پر پلیس ہولڈرز کو تبدیل کریں)۔

3. (اختیار) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ کے پاس اس ریپوزٹری سے وابستہ _Codespaces راز_ کے طور پر ماحول کے متغیرات کو محفوظ کرنے کا اختیار ہے۔ اس صورت میں، آپ کو مقامی .env فائل ترتیب دینے کی ضرورت نہیں ہوگی۔ **تاہم، نوٹ کریں کہ یہ آپشن صرف اس صورت میں کام کرتا ہے جب آپ GitHub Codespaces استعمال کرتے ہیں۔** اگر آپ Docker Desktop استعمال کرتے ہیں تو آپ کو پھر بھی .env فائل ترتیب دینی ہوگی۔

### 2.2. `.env` فائل کو بھریں

آئیے متغیر ناموں پر ایک مختصر نظر ڈالیں تاکہ سمجھ سکیں کہ وہ کیا ظاہر کرتے ہیں:

| متغیر  | وضاحت  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ وہ صارف رسائی ٹوکن ہے جو آپ نے اپنے پروفائل میں ترتیب دیا ہے |
| OPENAI_API_KEY | یہ غیر-Azure OpenAI اینڈپوائنٹس کے لیے سروس استعمال کرنے کی اجازت کلید ہے |
| AZURE_OPENAI_API_KEY | یہ سروس استعمال کرنے کی اجازت کلید ہے |
| AZURE_OPENAI_ENDPOINT | یہ Azure OpenAI وسائل کے لیے تعینات اینڈپوائنٹ ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _متن کی تخلیق_ ماڈل تعیناتی اینڈپوائنٹ ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _متن کی ایمبیڈنگز_ ماڈل تعیناتی اینڈپوائنٹ ہے |
| | |

نوٹ: آخری دو Azure OpenAI متغیرات ایک ڈیفالٹ ماڈل کی عکاسی کرتے ہیں جو چیٹ مکمل کرنے (متن کی تخلیق) اور ویکٹر تلاش (ایمبیڈنگز) کے لیے ہیں۔ انہیں ترتیب دینے کے لیے ہدایات متعلقہ اسائنمنٹس میں بیان کی جائیں گی۔

### 2.3 Azure کو ترتیب دیں: پورٹل سے

Azure OpenAI اینڈپوائنٹ اور کلیدی اقدار [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملیں گی، لہذا آئیے وہاں سے شروع کرتے ہیں۔

1. [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں
1. سائڈبار (بائیں مینو) میں **Keys اور Endpoint** آپشن پر کلک کریں۔
1. **Show Keys** پر کلک کریں - آپ کو درج ذیل نظر آنا چاہئے: KEY 1، KEY 2 اور Endpoint۔
1. AZURE_OPENAI_API_KEY کے لیے KEY 1 قدر استعمال کریں
1. AZURE_OPENAI_ENDPOINT کے لیے Endpoint قدر استعمال کریں

اگلا، ہمیں ان مخصوص ماڈلز کے اینڈپوائنٹس کی ضرورت ہے جو ہم نے تعینات کیے ہیں۔

1. Azure OpenAI وسائل کے لیے سائڈبار (بائیں مینو) میں **ماڈل کی تعیناتی** آپشن پر کلک کریں۔
1. منزل والے صفحے پر، **Manage Deployments** پر کلک کریں

یہ آپ کو Azure OpenAI Studio ویب سائٹ پر لے جائے گا، جہاں ہم دیگر اقدار کو ذیل میں بیان کے مطابق پائیں گے۔

### 2.4 Azure کو ترتیب دیں: اسٹوڈیو سے

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) پر **اپنے وسائل سے** جیسا کہ اوپر بیان کیا گیا ہے، جائیں۔
1. موجودہ تعینات ماڈلز کو دیکھنے کے لیے **تعینات** ٹیب (سائڈبار، بائیں) پر کلک کریں۔
1. اگر آپ کا مطلوبہ ماڈل تعینات نہیں ہے، تو **نیا تعینات بنائیں** استعمال کریں تاکہ اسے تعینات کریں۔
1. آپ کو ایک _متن کی تخلیق_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں: **gpt-35-turbo**
1. آپ کو ایک _متن کی ایمبیڈنگ_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں **text-embedding-ada-002**

اب ماحول کے متغیرات کو تعینات نام کی عکاسی کرنے کے لیے اپ ڈیٹ کریں۔ یہ عام طور پر ماڈل نام کے جیسا ہی ہوگا جب تک آپ نے اسے صراحتاً تبدیل نہ کیا ہو۔ لہذا، مثال کے طور پر، آپ کے پاس ہو سکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**جب ہو جائے تو .env فائل کو محفوظ کرنا نہ بھولیں**۔ آپ اب فائل سے باہر نکل سکتے ہیں اور نوٹ بک چلانے کی ہدایات پر واپس جا سکتے ہیں۔

### 2.5 OpenAI کو ترتیب دیں: پروفائل سے

آپ کی OpenAI API کلید آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں مل سکتی ہے۔ اگر آپ کے پاس ایک نہیں ہے، تو آپ اکاؤنٹ کے لیے سائن اپ کر سکتے ہیں اور ایک API کلید بنا سکتے ہیں۔ ایک بار جب آپ کے پاس کلید ہو، تو آپ اسے `.env` فائل میں `OPENAI_API_KEY` متغیر کو بھریں۔

### 2.6 Hugging Face کو ترتیب دیں: پروفائل سے

آپ کا Hugging Face ٹوکن آپ کے پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) کے تحت مل سکتا ہے۔ انہیں عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس پروجیکٹ کے استعمال کے لیے ایک نیا ٹوکن بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` متغیر کے تحت کاپی کریں۔ _نوٹ:_ یہ تکنیکی طور پر ایک API کلید نہیں ہے لیکن تصدیق کے لیے استعمال ہوتی ہے لہذا ہم مستقل مزاجی کے لیے اس نامی کنونشن کو برقرار رکھ رہے ہیں۔

**دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔