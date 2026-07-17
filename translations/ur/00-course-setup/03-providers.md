# ایل ایل ایم فراہم کنندہ کا انتخاب اور ترتیب دینا 🔑

اسائنمنٹس **ممکن ہے** کہ ایک یا زیادہ بڑے زبان ماڈل (LLM) تعیناتیوں کے خلاف کام کرنے کے لیے ایک سپورٹڈ سروس فراہم کنندہ جیسے OpenAI، Azure یا Hugging Face کے ذریعے بھی سیٹ اپ کی جائیں۔ یہ ایک _میزبان اینڈپوائنٹ_ (API) فراہم کرتے ہیں جس تک ہم مناسب اسناد (API کی یا ٹوکن) کے ساتھ پروگراماتی طور پر رسائی حاصل کر سکتے ہیں۔ اس کورس میں، ہم ان فراہم کنندگان پر بات کرتے ہیں:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) متنوع ماڈلز کے ساتھ بشمول کور GPT سیریز۔
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ماڈلز کے لیے جو ادارہ جاتی تیاری پر توجہ مرکوز رکھتا ہے۔
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ایک واحد اینڈپوائنٹ اور API کی کے لیے، جو OpenAI، Meta، Mistral، Cohere، Microsoft اور مزید کئی ماڈلز تک رسائی فراہم کرتا ہے (GitHub Models کی جگہ لے رہا ہے، جو جولائی 2026 کے آخر میں بند ہو رہا ہے)۔
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) اوپن سورس ماڈلز اور انفیرنس سرور کے لیے۔
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) یا [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) اگر آپ ماڈلز کو مکمل طور پر آف لائن اپنے آلے پر چلانا چاہتے ہیں، بغیر کسی کلاؤڈ سبسکرپشن کے۔

**آپ کو ان مشقوں کے لیے اپنے اکاؤنٹس استعمال کرنے ہوں گے**۔ اسائنمنٹس اختیاری ہیں لہٰذا آپ اپنے مفادات کی بنیاد پر ایک، سب یا کوئی بھی فراہم کنندہ سیٹ اپ کرنے کا انتخاب کر سکتے ہیں۔ سائن اپ کے لیے کچھ رہنمائی:

| سائن اپ | قیمت | API کی | پلے گراؤنڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمتوں کا تعین](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ کی بنیاد پر](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [کوڈ کے بغیر، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب ہیں |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمتوں کا تعین](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK کوئیک اسٹارٹ](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [اسٹوڈیو کوئیک اسٹارٹ](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [رسائی کے لیے پیشگی درخواست ضروری](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [قیمتوں کا تعین](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [پروجیکٹ کا جائزہ صفحہ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry پلے گراؤنڈ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | مفت سطح دستیاب؛ ایک اینڈپوائنٹ + کئی ماڈل فراہم کنندگان کے لیے کی |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمتوں کا تعین](https://huggingface.co/pricing) | [رسائی کے ٹوکنز](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat محدود ماڈلز رکھتا ہے](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | مفت (آپ کے آلے پر چلتا ہے) | ضروری نہیں | [مقامی CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | مکمل طور پر آف لائن، OpenAI-مطابق اینڈپوائنٹ |
| | | | | |

نیچے دی گئی ہدایات کو فالو کریں تاکہ اس ریپوزیٹری کو مختلف فراہم کنندگان کے لیے _ترتیب دیا جا سکے۔ وہ اسائنمنٹس جو مخصوص فراہم کنندہ کی ضرورت رکھتے ہیں، ان کے فائل نام میں یہ ٹیگز شامل ہوں گے:

- `aoai` - Azure OpenAI اینڈپوائنٹ اور کی کی ضرورت ہے۔
- `oai` - OpenAI اینڈپوائنٹ اور کی کی ضرورت ہے۔
- `hf` - Hugging Face ٹوکن کی ضرورت ہے۔
- `githubmodels` - Microsoft Foundry Models اینڈپوائنٹ اور کی کی ضرورت ہے (GitHub ماڈلز جولائی 2026 کے آخر میں بند ہو رہا ہے)۔

آپ ایک، کوئی، یا تمام فراہم کنندگان کو ترتیب دے سکتے ہیں۔ متعلقہ اسائنمنٹس صرف اسناد کی کمی کی وجہ سے ایرر دکھائیں گے۔

## `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے اوپر دی گئی رہنمائی پڑھ لی ہے، متعلقہ فراہم کنندہ کے ساتھ سائن اپ کیا ہے، اور مطلوبہ تصدیقی اسناد (API_KEY یا ٹوکن) حاصل کر لی ہیں۔ Azure OpenAI کے معاملے میں، ہم فرض کرتے ہیں کہ آپ کے پاس Azure OpenAI سروس (اینڈپوائنٹ) کی ایک فعال تعیناتی ہے جس میں کم از کم ایک GPT ماڈل چیٹ کمپلیشن کے لیے تعینات ہے۔

اگلا مرحلہ ہے اپنے **مقامی ماحول کے متغیرات** کو درج ذیل طریقے سے سیٹ کرنا:

1. روٹ فولڈر میں `.env.copy` فائل دیکھیں جس میں درج ذیل مواد ہونا چاہیے:

   ```bash
   # اوپن اے آئی پرووائیڈر
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## مائیکروسافٹ فاؤنڈری میں آزور اوپن اے آئی
   ## (آزور اوپن اے آئی سروس اب مائیکروسافٹ فاؤنڈری کا حصہ ہے: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ڈیفالٹ مقرر ہے! (موجودہ مستحکم GA API ورژن)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## مائیکروسافٹ فاؤنڈری ماڈلز (کثیر فراہم کنندہ ماڈل کیٹلاگ، گٹ ہب ماڈلز کی جگہ، جو جولائی 2026 کے آخر میں بند ہو جائیں گے)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ہگزنگ فیس
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. اس فائل کو نیچے دیے گئے کمانڈ سے `.env` میں کاپی کریں۔ یہ فائل _gitignore-d_ ہے، راز محفوظ رکھنے کے لیے۔

   ```bash
   cp .env.copy .env
   ```

3. درج ذیل سیکشن میں بیان کیے گئے محل وقوع کی جگہ اقدار بھریں (یعنی `=` کے دائیں جانب موجود جگہوں پر)۔

4. (اختیاری) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ اس ریپوزیٹری کے ساتھ منسلک _Codespaces سیکرٹس_ کے طور پر ماحول کے متغیرات محفوظ کر سکتے ہیں۔ ایسی صورت میں، آپ کو مقامی `.env` فائل سیٹ اپ کرنے کی ضرورت نہیں ہوگی۔ **تاہم، یاد رکھیں کہ یہ آپشن صرف GitHub Codespaces استعمال کرنے پر کام کرتا ہے۔** اگر آپ Docker Desktop استعمال کرتے ہیں تو پھر بھی `.env` فائل سیٹ اپ کرنا پڑے گا۔

## `.env` فائل کو بھرنا

آئیں متغیرات کے ناموں پر ایک نظر ڈالتے ہیں تاکہ یہ سمجھ سکیں کہ وہ کیا ظاہر کرتے ہیں:

| متغیر | وضاحت |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ صارف کا رسائی ٹوکن ہے جو آپ نے اپنے پروفائل میں سیٹ اپ کیا ہے |
| OPENAI_API_KEY | یہ سروس کے استعمال کے لیے اجازت نامہ کلید ہے (غیر Azure OpenAI اینڈپوائنٹس کے لیے) |
| AZURE_OPENAI_API_KEY | یہ اس سروس کے استعمال کے لیے اجازت نامہ کلید ہے |
| AZURE_OPENAI_ENDPOINT | یہ Azure OpenAI ریسورس کے لیے تعینات اینڈپوائنٹ ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _متن جنریشن_ ماڈل کی تعیناتی کا اینڈپوائنٹ ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _متن ایمبیڈنگز_ ماڈل کی تعیناتی کا اینڈپوائنٹ ہے |
| AZURE_INFERENCE_ENDPOINT | یہ آپ کے Microsoft Foundry پروجیکٹ کا اینڈپوائنٹ ہے، جو Microsoft Foundry ماڈلز کے لیے استعمال ہوتا ہے |
| AZURE_INFERENCE_CREDENTIAL | یہ آپ کے Microsoft Foundry پروجیکٹ کے لیے API کی ہے |
| | |

نوٹ: آخری دونوں Azure OpenAI متغیرات بالترتیب چیٹ کمپلیشن (متن جنریشن) اور ویکٹر سرچ (ایمبیڈنگز) کے لیے ایک ڈیفالٹ ماڈل کی نمائندگی کرتے ہیں۔ انہیں سیٹ کرنے کی ہدایات متعلقہ اسائنمنٹس میں دی جائیں گی۔

## Azure OpenAI کو ترتیب دینا: پورٹل سے

> **نوٹ:** Azure OpenAI سروس اب [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) کا حصہ ہے۔ وسائل اور تعیناتیاں اب بھی Azure پورٹل میں نظر آتی ہیں، لیکن روزمرہ ماڈل مینجمنٹ (تعیناتیاں، پلے گراؤنڈ، مانیٹرنگ) اب پرانے "Azure OpenAI Studio" کی جگہ Foundry پورٹل میں ہوتی ہے۔

Azure OpenAI اینڈپوائنٹ اور کی کی اقدار آپ کو [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملیں گی، تو آئیے وہاں سے شروع کرتے ہیں۔

1. [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔
1. سائڈبار (بائیں مینو) میں **Keys and Endpoint** آپشن پر کلک کریں۔
1. **Show Keys** پر کلک کریں - آپ کو درج ذیل نظر آئے گا: KEY 1، KEY 2 اور Endpoint۔
1. `AZURE_OPENAI_API_KEY` کے لیے KEY 1 کی قیمت استعمال کریں۔
1. `AZURE_OPENAI_ENDPOINT` کے لیے Endpoint کی قیمت استعمال کریں۔

اگلے مرحلے میں، ہمیں مخصوص ماڈلز کی تعیناتیاں چاہیے ہوں گی۔

1. Azure OpenAI ریسورس کے لیے سائڈبار (بائیں مینو) میں **Model deployments** آپشن پر کلک کریں۔
1. منزل کے صفحے پر، **Go to Microsoft Foundry portal** (یا **Manage Deployments**) پر کلک کریں، آپ کے ریسورس کی قسم کے مطابق۔

یہ آپ کو Microsoft Foundry پورٹل پر لے جائے گا، جہاں ہم نیچے بیان کیے گئے دیگر اقدار تلاش کریں گے۔

## Azure OpenAI کو ترتیب دینا: Microsoft Foundry پورٹل سے

1. اوپر دیے گئے طریقے سے اپنے ریسورس سے [Microsoft Foundry پورٹل](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں۔
1. حالیہ تعینات ماڈلز دیکھنے کے لیے **Deployments** ٹیب (سائڈبار، بائیں) پر کلک کریں۔
1. اگر آپ کا مطلوبہ ماڈل تعینات نہیں ہے تو، [ماڈل کیٹلاگ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) سے اسے تعینات کرنے کے لیے **Deploy model** استعمال کریں۔
1. آپ کو ایک _متن جنریشن_ ماڈل درکار ہوگا - ہم تجویز کرتے ہیں: **gpt-5-mini**
1. آپ کو ایک _متن ایمبیڈنگ_ ماڈل درکار ہوگا - ہم تجویز کرتے ہیں **text-embedding-3-small**

اب ماحول کے متغیرات کو اپ ڈیٹ کریں تاکہ تعیناتی کا نام ظاہر ہو جو استعمال کیا گیا ہو۔ یہ عام طور پر ماڈل کے نام کے برابر ہوگا جب تک کہ آپ نے اسے واضح طور پر تبدیل نہ کیا ہو۔ مثال کے طور پر، آپ کے پاس ہو سکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**کام ختم ہونے پر .env فائل کو محفوظ کرنا نہ بھولیں۔** آپ اب فائل سے باہر نکل سکتے ہیں اور نوٹ بک چلانے کی ہدایات پر واپس جا سکتے ہیں۔

## OpenAI کو ترتیب دینا: پروفائل سے

آپ کی OpenAI API کی آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں مل سکتی ہے۔ اگر آپ کے پاس نہیں ہے تو، آپ اکاؤنٹ بنائیں اور API کی تخلیق کریں۔ کی ملنے کے بعد آپ اسے `.env` فائل میں `OPENAI_API_KEY` متغیر میں بھر سکتے ہیں۔

## Hugging Face کو ترتیب دینا: پروفائل سے

آپ کا Hugging Face ٹوکن آپ کے پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) کے تحت ملے گا۔ اسے عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس پروجیکٹ کے لیے نیا ٹوکن بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` متغیر میں کاپی کریں۔ _نوٹ:_ یہ تکنیکی طور پر API کی نہیں ہے لیکن توثیق کے لیے استعمال ہوتی ہے اس لیے ہم اس نام کو مستقل مزاجی کے لیے رکھتے ہیں۔

## Microsoft Foundry Models کو ترتیب دینا: پورٹل سے

> **نوٹ:** GitHub Models جولائی 2026 کے آخر میں بند ہو رہے ہیں۔ Microsoft Foundry Models براہ راست متبادل ہے، جو مفت آزمائش ماڈل کیٹلاگ اور Azure AI Inference SDK / OpenAI SDK کا ایک جیسا تجربہ فراہم کرتا ہے۔

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں اور Foundry پروجیکٹ بنائیں (یا کھولیں)۔
1. [ماڈل کیٹلاگ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) میں براؤز کریں اور ایک ماڈل تعینات کریں، مثلاً `gpt-5-mini`۔
1. پروجیکٹ کے **Overview** صفحے پر، **endpoint** اور **API key** کو کاپی کریں۔
1. اپنی `.env` فائل میں `AZURE_INFERENCE_ENDPOINT` کے لیے endpoint ویلیو اور `AZURE_INFERENCE_CREDENTIAL` کے لیے کی ویلیو استعمال کریں۔

## آف لائن / مقامی فراہم کنندگان

اگر آپ کلاؤڈ سبسکرپشن بالکل استعمال نہیں کرنا چاہتے، تو آپ کمپٹیبل اوپن ماڈلز براہ راست اپنے آلے پر چلا سکتے ہیں:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - مائیکروسافٹ کا آن-ڈیوائس رن ٹائم۔ یہ خود بخود بہترین ایکزیکیوٹر فراہم کنندہ کو منتخب کرتا ہے (NPU، GPU، یا CPU) اور OpenAI-مطابق اینڈپوائنٹ فراہم کرتا ہے، تاکہ آپ اس کورس کے نمونہ کوڈ کو معمولی تبدیلیوں کے ساتھ دوبارہ استعمال کر سکیں۔ شروع کرنے کے لیے [Foundry Local دستاویزات](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) دیکھیں یا `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) سے انسٹال کریں۔
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - اوپن ماڈلز جیسے Llama، Phi، Mistral، اور Gemma کو مقامی طور پر چلانے کے لیے ایک مقبول متبادل۔


عملی مثالوں کے لیے دونوں آپشنز استعمال کرتے ہوئے دیکھیں [سبق 19: SLMs کے ساتھ تعمیر](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->