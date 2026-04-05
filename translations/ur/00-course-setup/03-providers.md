# LLM فراہم کنندہ کا انتخاب اور ترتیب دینا 🔑

اسائنمنٹس **ممکنہ طور پر** ایک یا زیادہ بڑے زبان کے ماڈل (LLM) کی تعیناتیوں کے خلاف کام کرنے کے لیے ایک معاون سروس فراہم کنندہ جیسے OpenAI، Azure یا Hugging Face کے ذریعے ترتیب دی جا سکتی ہیں۔ یہ ایک _میزبان اینڈپوائنٹ_ (API) فراہم کرتے ہیں جس تک ہم مناسب اسناد (API کلید یا ٹوکن) کے ساتھ پروگراماتی طور پر رسائی حاصل کر سکتے ہیں۔ اس کورس میں، ہم ان فراہم کنندگان پر بات کرتے ہیں:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مختلف ماڈلز کے ساتھ بشمول بنیادی GPT سیریز۔
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ماڈلز کے لیے کاروباری تیاری پر توجہ کے ساتھ
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) اوپن سورس ماڈلز اور انفرنس سرور کے لیے

**آپ کو ان مشقوں کے لیے اپنے ذاتی اکاؤنٹس استعمال کرنے ہوں گے**۔ اسائنمنٹس اختیاری ہیں لہٰذا آپ اپنی دلچسپیوں کی بنیاد پر ایک، تمام یا کوئی بھی فراہم کنندہ ترتیب دے سکتے ہیں۔ سائن اپ کے لیے کچھ رہنمائی:

| سائن اپ | لاگت | API کلید | پلے گراؤنڈ | تبصرے |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [پروجیکٹ کی بنیاد پر](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [نو-کوڈ، ویب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | متعدد ماڈلز دستیاب |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [قیمتیں](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK کوئیک اسٹارٹ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [اسٹوڈیو کوئیک اسٹارٹ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [رسائی کے لیے پہلے درخواست دینا ضروری](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [قیمتیں](https://huggingface.co/pricing) | [رسائی کے ٹوکن](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat میں محدود ماڈلز ہیں](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

نیچے دی گئی ہدایات پر عمل کریں تاکہ اس ریپوزیٹری کو مختلف فراہم کنندگان کے ساتھ استعمال کے لیے _ترتیب_ دیا جا سکے۔ وہ اسائنمنٹس جنہیں کسی مخصوص فراہم کنندہ کی ضرورت ہو گی، ان کے فائل نام میں درج ذیل ٹیگز ہوں گے:

- `aoai` - Azure OpenAI اینڈپوائنٹ، کلید کی ضرورت ہے
- `oai` - OpenAI اینڈپوائنٹ، کلید کی ضرورت ہے
- `hf` - Hugging Face ٹوکن کی ضرورت ہے

آپ ایک، کوئی یا تمام فراہم کنندگان کو ترتیب دے سکتے ہیں۔ متعلقہ اسائنمنٹس اسناد کی کمی پر صرف ایرر دیں گے۔

## `.env` فائل بنائیں

ہم فرض کرتے ہیں کہ آپ نے اوپر دی گئی رہنمائی پڑھ لی ہے اور متعلقہ فراہم کنندہ کے ساتھ سائن اپ کر کے مطلوبہ توثیقی اسناد (API_KEY یا ٹوکن) حاصل کر لی ہیں۔ Azure OpenAI کی صورت میں، ہم فرض کرتے ہیں کہ آپ کے پاس Azure OpenAI سروس (اینڈپوائنٹ) کی ایک درست تعیناتی ہے جس میں کم از کم ایک GPT ماڈل چیٹ کمپلیشن کے لیے تعینات ہے۔

اگلا قدم آپ کے **مقامی ماحول کے متغیرات** کو درج ذیل طریقے سے ترتیب دینا ہے:

1. روٹ فولڈر میں `.env.copy` فائل تلاش کریں جس میں مندرجہ ذیل مواد ہونا چاہیے:

   ```bash
   # اوپن اے آئی فراہم کنندہ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## ایزور اوپن اے آئی
   AZURE_OPENAI_API_VERSION='2024-02-01' # ڈیفالٹ سیٹ ہے!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## ہگنگ فیس
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. اس فائل کو نیچے دیے گئے کمانڈ سے `.env` میں کاپی کریں۔ یہ فائل _gitignore-d_ ہے، رازوں کو محفوظ رکھتی ہے۔

   ```bash
   cp .env.copy .env
   ```

3. اقدار کو پر کریں (دائیں جانب `=` کے بعد موجود جگہوں کو تبدیل کریں) جیسا کہ اگلے سیکشن میں بیان کیا گیا ہے۔

4. (اختیاری) اگر آپ GitHub Codespaces استعمال کرتے ہیں، تو آپ کے پاس ماحول کے متغیرات کو اس ریپوزیٹری سے منسلک _Codespaces secrets_ کے طور پر محفوظ کرنے کا اختیار ہے۔ ایسی صورت میں، آپ کو مقامی .env فائل ترتیب دینے کی ضرورت نہیں ہوگی۔ **تاہم، نوٹ کریں کہ یہ اختیار صرف GitHub Codespaces استعمال کرنے پر کام کرتا ہے۔** اگر آپ Docker Desktop استعمال کرتے ہیں تو پھر بھی .env فائل ترتیب دینی ہوگی۔

## `.env` فائل کو بھرنا

آئیے متغیرات کے ناموں پر ایک نظر ڈالیں تاکہ سمجھ سکیں کہ وہ کیا ظاہر کرتے ہیں:

| متغیر  | وضاحت  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | یہ وہ صارف رسائی ٹوکن ہے جو آپ نے اپنی پروفائل میں ترتیب دیا ہے |
| OPENAI_API_KEY | یہ غیر Azure OpenAI اینڈپوائنٹس کے لیے سروس استعمال کرنے کی اجازت کی کلید ہے |
| AZURE_OPENAI_API_KEY | یہ اس سروس کے استعمال کی اجازت کی کلید ہے |
| AZURE_OPENAI_ENDPOINT | یہ Azure OpenAI وسائل کے لیے تعینات کردہ اینڈپوائنٹ ہے |
| AZURE_OPENAI_DEPLOYMENT | یہ _متن کی تخلیق_ ماڈل کی تعیناتی کا اینڈپوائنٹ ہے |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | یہ _متن کے ایمبیڈنگز_ ماڈل کی تعیناتی کا اینڈپوائنٹ ہے |
| | |

نوٹ: آخری دو Azure OpenAI متغیرات بالترتیب چیٹ کمپلیشن (متن کی تخلیق) اور ویکٹر سرچ (ایمبیڈنگز) کے لیے ایک ڈیفالٹ ماڈل کی عکاسی کرتے ہیں۔ انہیں ترتیب دینے کی ہدایات متعلقہ اسائنمنٹس میں دی جائیں گی۔

## Azure کی ترتیب: پورٹل سے

Azure OpenAI اینڈپوائنٹ اور کلید کی قدریں [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) میں ملیں گی، تو آئیے وہاں سے شروع کرتے ہیں۔

1. [Azure پورٹل](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں
1. سائڈبار (بائیں مینو) میں **Keys and Endpoint** آپشن پر کلک کریں۔
1. **Show Keys** پر کلک کریں - آپ کو درج ذیل نظر آئے گا: KEY 1، KEY 2 اور Endpoint۔
1. AZURE_OPENAI_API_KEY کے لیے KEY 1 کی قدر استعمال کریں
1. AZURE_OPENAI_ENDPOINT کے لیے Endpoint کی قدر استعمال کریں

اب ہمیں ان مخصوص ماڈلز کے اینڈپوائنٹس کی ضرورت ہے جو ہم نے تعینات کیے ہیں۔

1. Azure OpenAI وسائل کے لیے سائڈبار (بائیں مینو) میں **Model deployments** آپشن پر کلک کریں۔
1. منزل کے صفحے پر، **Manage Deployments** پر کلک کریں

یہ آپ کو Azure OpenAI اسٹوڈیو ویب سائٹ پر لے جائے گا، جہاں ہم نیچے بیان کردہ دیگر قدریں تلاش کریں گے۔

## Azure کی ترتیب: اسٹوڈیو سے

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) پر جائیں **اپنے وسائل سے** جیسا کہ اوپر بیان کیا گیا ہے۔
1. موجودہ تعینات ماڈلز دیکھنے کے لیے **Deployments** ٹیب (سائڈبار، بائیں) پر کلک کریں۔
1. اگر آپ کا مطلوبہ ماڈل تعینات نہیں ہے، تو اسے تعینات کرنے کے لیے **Create new deployment** استعمال کریں۔
1. آپ کو ایک _متن کی تخلیق_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں: **gpt-35-turbo**
1. آپ کو ایک _متن کے ایمبیڈنگ_ ماڈل کی ضرورت ہوگی - ہم تجویز کرتے ہیں **text-embedding-ada-002**

اب ماحول کے متغیرات کو اپ ڈیٹ کریں تاکہ استعمال شدہ _Deployment name_ کی عکاسی ہو۔ یہ عام طور پر ماڈل کے نام کے برابر ہوتا ہے جب تک کہ آپ نے اسے واضح طور پر تبدیل نہ کیا ہو۔ مثال کے طور پر، آپ کے پاس ہو سکتا ہے:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**کام مکمل ہونے پر .env فائل کو محفوظ کرنا نہ بھولیں**۔ اب آپ فائل سے باہر نکل سکتے ہیں اور نوٹ بک چلانے کی ہدایات پر واپس جا سکتے ہیں۔

## OpenAI کی ترتیب: پروفائل سے

آپ کی OpenAI API کلید آپ کے [OpenAI اکاؤنٹ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) میں مل سکتی ہے۔ اگر آپ کے پاس کلید نہیں ہے، تو آپ اکاؤنٹ کے لیے سائن اپ کر کے API کلید بنا سکتے ہیں۔ کلید حاصل کرنے کے بعد، آپ اسے `.env` فائل میں `OPENAI_API_KEY` متغیر کو بھرنے کے لیے استعمال کر سکتے ہیں۔

## Hugging Face کی ترتیب: پروفائل سے

آپ کا Hugging Face ٹوکن آپ کی پروفائل میں [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) کے تحت مل سکتا ہے۔ انہیں عوامی طور پر پوسٹ یا شیئر نہ کریں۔ اس کے بجائے، اس پروجیکٹ کے استعمال کے لیے نیا ٹوکن بنائیں اور اسے `.env` فائل میں `HUGGING_FACE_API_KEY` متغیر کے تحت کاپی کریں۔ _نوٹ:_ یہ تکنیکی طور پر API کلید نہیں ہے لیکن توثیق کے لیے استعمال ہوتا ہے، اس لیے ہم تسلسل کے لیے اسی نام کا استعمال کر رہے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->