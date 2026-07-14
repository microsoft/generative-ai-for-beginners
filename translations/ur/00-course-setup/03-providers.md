# ایک LLM فراہم کنندہ کا انتخاب اور ترتیب دینا 🔑

اسائنمنٹس کو ایک یا زیادہ بڑے زبان ماڈل (LLM) تعینات کردہ سے متصل بھی کیا جا سکتا ہے، جنہیں OpenAI، Azure یا Hugging Face جیسے معاون سروس فراہم کنندہ کے ذریعے پیش کیا جاتا ہے۔ یہ ایک _میزبان اینڈپوائنٹ_ (API) فراہم کرتے ہیں جسے ہم مناسب اسناد (API کلید یا ٹوکن) کے ساتھ پروگراماتی طور پر استعمال کر سکتے ہیں۔ اس کورس میں، ہم ان فراہم کنندگان پر بات کرتے ہیں:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مختلف ماڈلز کے ساتھ بشمول بنیادی GPT سیریز۔
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ماڈلز کے لیے بزنس تیاری پر توجہ کے ساتھ
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ایک واحد اینڈپوائنٹ اور API کلید کے ذریعے سینکڑوں ماڈلز تک رسائی کے لیے، مثلاً OpenAI، Meta، Mistral، Cohere، Microsoft اور دیگر (GitHub Models کا متبادل، جو جولائی 2026 کے آخر میں بند ہو رہے ہیں)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) اوپن سورس ماڈلز اور inference سرور کے لیے
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) یا [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) اگر آپ ماڈلز کو مکمل طور پر آف لائن اپنے آلے پر چلانا چاہتے ہیں، بغیر کسی کلاؤڈ سبسکرپشن کے

**ان مشقوں کے لیے آپ کو اپنے ذاتی اکاؤنٹس کی ضرورت ہوگی**۔ اسائنمنٹس اختیاری ہیں لہٰذا آپ اپنی دلچسپیوں کی بنیاد پر ایک، تمام یا کوئی بھی فراہم کنندہ ترتیب دے سکتے ہیں۔ سائن اپ کے متعلق کچھ رہنمائی:

| سائن اپ | قیمت | API کلید | پلے گراونڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ پر مبنی](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [نو-کوڈ، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK کوئیک سٹارٹ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [اسٹوڈیو کوئیک سٹارٹ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [پہلے سے درخواست ضرور کریں](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [قیمتیں](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [پروجیکٹ کا جائزہ صفحہ](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry پلے گراونڈ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | مفت سطح دستیاب؛ ایک اینڈپوائنٹ + کلید کئی ماڈل فراہم کنندگان کے لیے |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمتیں](https://huggingface.co/pricing) | [رسائی ٹوکنز](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat محدود ماڈلز رکھتا ہے](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | مفت (آپ کے آلے پر چلتا ہے) | ضروری نہیں | [Local CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | مکمل طور پر آف لائن، OpenAI کے ساتھ ہم آہنگ اینڈپوائنٹ |
| | | | | |

نیچے دی گئی ہدایات کے مطابق اس ریپوزٹری کو مختلف فراہم کنندگان کے لیے _ترتیب_ دیں۔ مخصوص فراہم کنندہ کی ضرورت والے اسائنمنٹس کی فائل کے نام میں ان میں سے کوئی ایک ٹیگ ہوگا:

- `aoai` - Azure OpenAI اینڈپوائنٹ، کلید کی ضرورت ہوتی ہے
- `oai` - OpenAI اینڈپوائنٹ، کلید کی ضرورت ہوتی ہے
- `hf` - Hugging Face ٹوکن کی ضرورت ہوتی ہے
- `githubmodels` - Microsoft Foundry Models اینڈپوائنٹ، کلید کی ضرورت ہوتی ہے (GitHub Models جولائی 2026 کے آخر میں بند ہو رہا ہے)

آپ ایک، کوئی یا تمام فراہم کنندگان کو ترتیب دے سکتے ہیں۔ متعلقہ اسائنمنٹس لاگت کی کمی پر سیدها ایرر ظاہر کریں گے۔

## `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے پہلے سے مذکورہ بالا رہنمائی پڑھ لی ہے، متعلقہ فراہم کنندہ کے ساتھ سائن اپ کر لیا ہے، اور مطلوبہ تصدیقی اسناد (API_KEY یا ٹوکن) حاصل کر لی ہیں۔ Azure OpenAI کے معاملے میں، ہم فرض کرتے ہیں کہ آپ کے پاس Azure OpenAI سروس (اینڈپوائنٹ) کی ایک فعال تعیناتی ہے جس میں کم از کم ایک GPT ماڈل چیٹ کمپلیشن کے لیے تعینات ہے۔

اگلا قدم یہ ہے کہ آپ اپنے **لوکل ماحول کے متغیرات** درج ذیل طریقے سے ترتیب دیں:

1. روٹ فولڈر میں `.env.copy` فائل تلاش کریں جس میں ترتیب کچھ اس طرح ہونا چاہیے:

   ```bash
   # اوپن اے آئی فراہم کنندہ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## مائیکروسافٹ فاؤنڈری میں ایزور اوپن اے آئی
   ## (ایزور اوپن اے آئی سروس اب مائیکروسافٹ فاؤنڈری کا حصہ ہے: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ڈیفالٹ مقرر ہے! (موجودہ مستحکم GA API ورژن)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## مائیکروسافٹ فاؤنڈری ماڈلز (کثیر فراہم کنندہ ماڈل کیٹلاگ، GitHub ماڈلز کی جگہ، جو جولائی 2026 کے آخر میں بند ہو جائے گا)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ہگنگ فیس
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. اس فائل کو نیچے دیے گئے کمانڈ سے `.env` میں کاپی کریں۔ یہ فائل _gitignore-d_ ہے، رازوں کو محفوظ رکھتی ہے۔

   ```bash
   cp .env.copy .env
   ```

3. اقدار پر کریں (دائیں جانب `=` کے بعد موجود جگہ کو تبدیل کریں) جیسا کہ اگلے سیکشن میں بتایا گیا ہے۔

4. (اختیاری) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ کے پاس یہ اختیار ہوتا ہے کہ ماحول کے متغیرات کو اس ریپوزٹری سے وابستہ _Codespaces secrets_ کے طور پر محفوظ کریں۔ اس صورت میں، آپ کو لوکل `.env` فائل بنانے کی ضرورت نہیں ہوگی۔ **لیکن یاد رکھیں کہ یہ اختیار صرف تب کام کرتا ہے جب آپ GitHub Codespaces استعمال کریں۔** اگر آپ Docker Desktop استعمال کرتے ہیں تو پھر بھی آپ کو `.env` فائل بنانی ہوگی۔

## `.env` فائل بھرنا

آئیے متغیرات کے ناموں پر نظر ڈالتے ہیں تاکہ یہ سمجھ سکیں کہ وہ کیا ظاہر کرتے ہیں:

| متغیر | وضاحت |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ وہ یوزر ایکسیس ٹوکن ہے جو آپ نے اپنے پروفائل میں ترتیب دیا ہے |
| OPENAI_API_KEY | یہ وہ اجازت نامہ کلید ہے جو نان-Azure OpenAI اینڈپوائنٹس کے لیے سروس استعمال کرنے کے لیے ہے |
| AZURE_OPENAI_API_KEY | یہ اس سروس کے لیے اجازت نامہ کلید ہے |
| AZURE_OPENAI_ENDPOINT | یہ Azure OpenAI ریسورس کے لیے تعینات اینڈپوائنٹ ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _ٹیکسٹ جنریشن_ ماڈل تعیناتی اینڈپوائنٹ ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _ٹیکسٹ ایمبیڈنگز_ ماڈل تعیناتی اینڈپوائنٹ ہے |
| AZURE_INFERENCE_ENDPOINT | یہ آپ کے Microsoft Foundry پروجیکٹ کے لیے اینڈپوائنٹ ہے، جو Microsoft Foundry Models کے لیے استعمال ہوتا ہے |
| AZURE_INFERENCE_CREDENTIAL | یہ آپ کے Microsoft Foundry پروجیکٹ کی API کلید ہے |
| | |

نوٹ: آخری دو Azure OpenAI متغیرات ایک ڈیفالٹ ماڈل کی نمائندگی کرتے ہیں جو چیٹ کمپلیشن (ٹیکسٹ جنریشن) اور ویکٹر سرچ (ایمبیڈنگز) کے لیے ہیں۔ انہیں ترتیب دینے کی ہدایات متعلقہ اسائنمنٹس میں دی جائیں گی۔

## Azure OpenAI کو ترتیب دینا: پورٹل سے

> **نوٹ:** Azure OpenAI سروس اب [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) کا حصہ ہے۔ وسائل اور تعیناتیاں Azure پورٹل میں نظر آتی ہیں، لیکن روزمرہ کا ماڈل انتظام (deployments، playground، مانیٹرنگ) اب Foundry پورٹل میں ہوتا ہے بجائے پرانے آزاد "Azure OpenAI Studio" کے۔

Azure OpenAI اینڈپوائنٹ اور کلید کی مقدار [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملے گی، تو چلیں وہاں سے شروع کرتے ہیں۔

1. [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں
1. سائیڈبار (بائیں مینو) میں **Keys and Endpoint** آپشن پر کلک کریں۔
1. **Show Keys** پر کلک کریں - آپ کو درج ذیل نظر آئے گا: KEY 1، KEY 2 اور Endpoint۔
1. AZURE_OPENAI_API_KEY کے لیے KEY 1 کا استعمال کریں
1. AZURE_OPENAI_ENDPOINT کے لیے Endpoint کی قدروقیمت استعمال کریں

اب، ہمیں ان مخصوص ماڈلز کے اینڈپوائنٹس کی ضرورت ہے جو ہم نے تعینات کیے ہیں۔

1. Azure OpenAI ریسورس کے لیے سائیڈبار (بائیں مینو) میں **Model deployments** آپشن پر کلک کریں۔
1. منزل صفحہ میں، **Go to Microsoft Foundry portal** (یا **Manage Deployments**) پر کلک کریں، آپ کے ریسورس کی قسم کے مطابق۔

یہ آپ کو Microsoft Foundry پورٹل پر لے جائے گا، جہاں ہم دیگر مطلوبہ اقدار تلاش کریں گے جیسا کہ نیچے بیان کیا گیا ہے۔

## Azure OpenAI کو ترتیب دینا: Microsoft Foundry پورٹل سے

1. اوپر بیان کے مطابق **اپنے ریسورس سے** [Microsoft Foundry پورٹل](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔
1. تعینات ماڈلز دیکھنے کے لیے **Deployments** ٹیب (سائیڈبار، بائیں) پر کلک کریں۔
1. اگر آپ کا مطلوب ماڈل تعینات نہیں ہے، تو [ماڈل کاتلاگ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) سے **Deploy model** کا استعمال کرتے ہوئے اسے تعینات کریں۔
1. آپ کو ایک _ٹیکسٹ جنریشن_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں: **gpt-4o-mini**
1. آپ کو ایک _ٹیکسٹ ایمبیڈنگ_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں **text-embedding-3-small**

اب ماحول کے متغیرات کو _Deployment name_ کی عکاسی کرنے کے لیے اپ ڈیٹ کریں۔ عام طور پر یہ ماڈل کے نام کے برابر ہوگا جب تک کہ آپ نے اسے واضح طور پر تبدیل نہ کیا ہو۔ مثال کے طور پر، آپ کے پاس ہو سکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**کام ختم ہونے پر .env فائل کو محفوظ کرنا مت بھولیے**۔ اب آپ فائل سے باہر نکل سکتے ہیں اور نوٹ بک چلانے کی ہدایات پر واپس جا سکتے ہیں۔

## OpenAI کو ترتیب دینا: پروفائل سے

آپ کی OpenAI API کلید آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں مل سکتی ہے۔ اگر آپ کے پاس کلید نہیں ہے، تو آپ اکاؤنٹ بنا کر API کلید پیدا کر سکتے ہیں۔ کلید ملنے کے بعد، آپ اسے `.env` فائل میں `OPENAI_API_KEY` متغیر کو بھرنے کے لیے استعمال کر سکتے ہیں۔

## Hugging Face کو ترتیب دینا: پروفائل سے

آپ کا Hugging Face ٹوکن آپ کے پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) سیکشن میں ملے گا۔ انہیں عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس کے بجائے، اس پروجیکٹ کے استعمال کے لیے ایک نیا ٹوکن بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` متغیر میں نقل کریں۔ _نوٹ:_ یہ تکنیکی طور پر API کلید نہیں ہے لیکن توثیق کے لیے استعمال ہوتا ہے، لہٰذا ہم تسلسل کے لیے یہی نام استعمال کر رہے ہیں۔

## Microsoft Foundry Models کو ترتیب دینا: پورٹل سے

> **نوٹ:** GitHub Models جولائی 2026 کے آخر میں بند ہو رہے ہیں۔ Microsoft Foundry Models اس کا براہ راست متبادل ہے، جو وہی مفت ماڈل کاتلاگ اور Azure AI Inference SDK / OpenAI SDK تجربہ فراہم کرتا ہے۔

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں اور ایک Foundry پروجیکٹ بنائیں (یا کھولیں)۔
1. [ماڈل کاتلاگ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) کو براؤز کریں اور ایک ماڈل تعینات کریں، مثلاً `gpt-4o-mini`۔
1. پروجیکٹ کے **Overview** صفحہ پر، **endpoint** اور **API کلید** کو کاپی کریں۔
1. اپنی `.env` فائل میں `AZURE_INFERENCE_ENDPOINT` کے لیے اینڈپوائنٹ، اور `AZURE_INFERENCE_CREDENTIAL` کے لیے کلید کی مقدار استعمال کریں۔

## آف لائن / مقامی فراہم کنندگان

اگر آپ کلاؤڈ سبسکرپشن استعمال نہیں کرنا چاہتے تو آپ ہم آہنگ اوپن ماڈلز کو براہ راست اپنے آلے پر چلا سکتے ہیں:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - مائیکروسافٹ کا آن- ڈیوائس رن ٹائم۔ یہ خود بخود بہترین ایگزیکیوٹر (NPU، GPU، یا CPU) منتخب کرتا ہے اور OpenAI کے موافق اینڈپوائنٹ فراہم کرتا ہے، تو آپ اس کورس کے زیادہ تر سیمپل کوڈ کو معمولی تبدیلیوں کے ساتھ دوبارہ استعمال کر سکتے ہیں۔ شروع کرنے کے لیے [Foundry Local دستاویزات](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) دیکھیں، یا `winget install Microsoft.FoundryLocal` (ونڈوز) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) سے انسٹال کریں۔
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - اوپن ماڈلز جیسے Llama، Phi، Mistral، اور Gemma کو مقامی طور پر چلانے کے لیے ایک مقبول متبادل۔


عملی مثالوں کے لیے دونوں اختیارات استعمال کرتے ہوئے دیکھیں [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->