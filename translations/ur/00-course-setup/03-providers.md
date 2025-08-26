<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T14:19:35+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ur"
}
-->
# ایل ایل ایم فراہم کنندہ کا انتخاب اور ترتیب دینا 🔑

اسائنمنٹس کو اس طرح بھی ترتیب دیا جا سکتا ہے کہ وہ ایک یا ایک سے زیادہ بڑے لینگویج ماڈل (LLM) ڈیپلائمنٹس کے ساتھ کام کریں، جو کہ کسی سپورٹڈ سروس فراہم کنندہ جیسے OpenAI، Azure یا Hugging Face کے ذریعے دستیاب ہوں۔ یہ ایک _ہوسٹڈ اینڈ پوائنٹ_ (API) فراہم کرتے ہیں جس تک ہم درست اسناد (API key یا token) کے ساتھ پروگرام کے ذریعے رسائی حاصل کر سکتے ہیں۔ اس کورس میں ہم ان فراہم کنندگان پر بات کریں گے:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) جس میں مختلف ماڈلز شامل ہیں، خاص طور پر GPT سیریز۔
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) جو کہ OpenAI ماڈلز کو انٹرپرائز سطح پر فراہم کرتا ہے
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) جو کہ اوپن سورس ماڈلز اور انفیرنس سرور کے لیے ہے

**ان مشقوں کے لیے آپ کو اپنے اکاؤنٹس استعمال کرنا ہوں گے۔** اسائنمنٹس اختیاری ہیں، اس لیے آپ اپنی دلچسپی کے مطابق ایک، سب یا کوئی بھی فراہم کنندہ سیٹ اپ کر سکتے ہیں۔ سائن اپ کے لیے کچھ رہنمائی:

| سائن اپ | قیمت | API Key | پلے گراؤنڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ کی بنیاد پر](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [نو کوڈ، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب ہیں |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [رسائی کے لیے پہلے درخواست دینا ضروری ہے](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمتیں](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat میں ماڈلز محدود ہیں](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

مختلف فراہم کنندگان کے ساتھ اس ریپوزٹری کو استعمال کرنے کے لیے نیچے دی گئی ہدایات پر عمل کریں۔ جن اسائنمنٹس کو کسی خاص فراہم کنندہ کی ضرورت ہو گی، ان کی فائل کے نام میں یہ ٹیگز ہوں گے:

- `aoai` - Azure OpenAI اینڈ پوائنٹ اور key درکار ہے
- `oai` - OpenAI اینڈ پوائنٹ اور key درکار ہے
- `hf` - Hugging Face token درکار ہے

آپ ایک، کوئی یا سب فراہم کنندگان کو ترتیب دے سکتے ہیں۔ متعلقہ اسائنمنٹس اسناد نہ ہونے پر ایرر دیں گی۔

## `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے اوپر دی گئی رہنمائی پڑھ لی ہے، متعلقہ فراہم کنندہ کے ساتھ سائن اپ کر لیا ہے، اور مطلوبہ تصدیقی اسناد (API_KEY یا token) حاصل کر لی ہیں۔ Azure OpenAI کے معاملے میں، ہم یہ بھی فرض کرتے ہیں کہ آپ کے پاس Azure OpenAI Service (اینڈ پوائنٹ) کی درست ڈیپلائمنٹ ہے، جس میں کم از کم ایک GPT ماڈل چیٹ کمپلیشن کے لیے ڈیپلائے ہے۔

اگلا مرحلہ یہ ہے کہ اپنے **لوکل انوائرمنٹ ویریبلز** کو اس طرح ترتیب دیں:

1. روٹ فولڈر میں `.env.copy` فائل دیکھیں، جس میں کچھ اس طرح کا مواد ہونا چاہیے:

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

2. اس فائل کو نیچے دیے گئے کمانڈ کے ذریعے `.env` میں کاپی کریں۔ یہ فائل _gitignore_ کی گئی ہے، اس لیے راز محفوظ رہتے ہیں۔

   ```bash
   cp .env.copy .env
   ```

3. اگلے حصے میں بیان کردہ طریقے کے مطابق ویلیوز بھریں (placeholder کو `=` کے دائیں طرف تبدیل کریں)۔

4. (اختیاری) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ کے پاس انوائرمنٹ ویریبلز کو _Codespaces secrets_ کے طور پر اس ریپوزٹری کے ساتھ محفوظ کرنے کا آپشن ہے۔ اس صورت میں، آپ کو لوکل .env فائل سیٹ اپ کرنے کی ضرورت نہیں ہو گی۔ **تاہم، یہ آپشن صرف GitHub Codespaces کے ساتھ کام کرتا ہے۔** اگر آپ Docker Desktop استعمال کرتے ہیں تو پھر بھی .env فائل سیٹ اپ کرنا ہو گی۔

## `.env` فائل کو مکمل کریں

آئیے ویریبل ناموں پر ایک نظر ڈالتے ہیں تاکہ سمجھ سکیں کہ یہ کس چیز کی نمائندگی کرتے ہیں:

| ویریبل  | وضاحت  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ وہ یوزر ایکسیس ٹوکن ہے جو آپ نے اپنے پروفائل میں سیٹ اپ کیا ہے |
| OPENAI_API_KEY | یہ سروس استعمال کرنے کے لیے اجازت نامہ ہے، غیر Azure OpenAI اینڈ پوائنٹس کے لیے |
| AZURE_OPENAI_API_KEY | یہ اس سروس کے لیے اجازت نامہ ہے |
| AZURE_OPENAI_ENDPOINT | یہ Azure OpenAI ریسورس کے لیے ڈیپلائے اینڈ پوائنٹ ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _ٹیکسٹ جنریشن_ ماڈل ڈیپلائمنٹ اینڈ پوائنٹ ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _ٹیکسٹ ایمبیڈنگز_ ماڈل ڈیپلائمنٹ اینڈ پوائنٹ ہے |
| | |

نوٹ: آخری دو Azure OpenAI ویریبلز چیٹ کمپلیشن (ٹیکسٹ جنریشن) اور ویکٹر سرچ (ایمبیڈنگز) کے لیے ڈیفالٹ ماڈل کی نمائندگی کرتے ہیں۔ انہیں سیٹ کرنے کی ہدایات متعلقہ اسائنمنٹس میں دی جائیں گی۔

## Azure کی ترتیب: پورٹل سے

Azure OpenAI اینڈ پوائنٹ اور key کی ویلیوز آپ کو [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملیں گی، تو آئیے وہیں سے شروع کرتے ہیں۔

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں
1. سائیڈبار (بائیں مینو) میں **Keys and Endpoint** آپشن پر کلک کریں۔
1. **Show Keys** پر کلک کریں - آپ کو KEY 1، KEY 2 اور Endpoint نظر آئیں گے۔
1. AZURE_OPENAI_API_KEY کے لیے KEY 1 ویلیو استعمال کریں
1. AZURE_OPENAI_ENDPOINT کے لیے Endpoint ویلیو استعمال کریں

اب ہمیں ان ماڈلز کے اینڈ پوائنٹس چاہیے جو ہم نے ڈیپلائے کیے ہیں۔

1. Azure OpenAI ریسورس کے لیے سائیڈبار (بائیں مینو) میں **Model deployments** آپشن پر کلک کریں۔
1. منزل والے صفحے پر **Manage Deployments** پر کلک کریں

اس سے آپ Azure OpenAI Studio ویب سائٹ پر پہنچ جائیں گے، جہاں باقی ویلیوز ملیں گی، جیسا کہ نیچے بیان کیا گیا ہے۔

## Azure کی ترتیب: اسٹوڈیو سے

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) پر **اپنے ریسورس** سے جائیں، جیسا کہ اوپر بیان کیا گیا۔
1. سائیڈبار (بائیں) میں **Deployments** ٹیب پر کلک کریں تاکہ موجودہ ڈیپلائے ماڈلز دیکھ سکیں۔
1. اگر مطلوبہ ماڈل ڈیپلائے نہیں ہے، تو **Create new deployment** استعمال کریں۔
1. آپ کو ایک _ٹیکسٹ جنریشن_ ماڈل چاہیے - ہم **gpt-35-turbo** تجویز کرتے ہیں
1. آپ کو ایک _ٹیکسٹ ایمبیڈنگ_ ماڈل چاہیے - ہم **text-embedding-ada-002** تجویز کرتے ہیں

اب انوائرمنٹ ویریبلز کو اس _Deployment name_ کے مطابق اپ ڈیٹ کریں جو آپ نے استعمال کیا ہے۔ یہ عموماً ماڈل کے نام جیسا ہی ہوتا ہے، جب تک آپ نے اسے خاص طور پر تبدیل نہ کیا ہو۔ مثال کے طور پر، آپ کے پاس یہ ہو سکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**جب کام مکمل ہو جائے تو .env فائل کو محفوظ کرنا نہ بھولیں۔** اب آپ فائل سے باہر نکل سکتے ہیں اور نوٹ بک چلانے کی ہدایات پر واپس جا سکتے ہیں۔

## OpenAI کی ترتیب: پروفائل سے

آپ کی OpenAI API key آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں ملے گی۔ اگر آپ کے پاس نہیں ہے تو اکاؤنٹ بنا کر API key حاصل کریں۔ جب key مل جائے تو اسے `.env` فائل میں `OPENAI_API_KEY` ویریبل میں ڈال دیں۔

## Hugging Face کی ترتیب: پروفائل سے

آپ کا Hugging Face token آپ کے پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) کے تحت ملے گا۔ انہیں عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس پروجیکٹ کے لیے نیا token بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` ویریبل کے تحت ڈال دیں۔ _نوٹ:_ یہ تکنیکی طور پر API key نہیں ہے، لیکن تصدیق کے لیے استعمال ہوتا ہے، اس لیے ہم نام میں تسلسل کے لیے یہی کنونشن رکھ رہے ہیں۔

---

**اعلانِ دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی بھرپور کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی صورت میں ہم ذمہ دار نہیں ہوں گے۔