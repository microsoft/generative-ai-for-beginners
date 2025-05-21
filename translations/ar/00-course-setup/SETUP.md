<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:41:00+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ar"
}
-->
# إعداد بيئة التطوير الخاصة بك

قمنا بإعداد هذا المستودع والدورة باستخدام [حاوية التطوير](https://containers.dev?WT.mc_id=academic-105485-koreyst) التي تحتوي على بيئة تشغيل عالمية تدعم تطوير Python3 و .NET و Node.js و Java. يتم تعريف التكوين ذو الصلة في ملف `devcontainer.json` الموجود في مجلد `.devcontainer/` في جذر هذا المستودع.

لتفعيل حاوية التطوير، قم بتشغيلها في [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (لبيئة تشغيل مستضافة على السحابة) أو في [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (لبيئة تشغيل مستضافة على جهاز محلي). اقرأ [هذه الوثيقة](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) لمزيد من التفاصيل حول كيفية عمل حاويات التطوير داخل VS Code.

> [!TIP]  
> نوصي باستخدام GitHub Codespaces للبدء السريع بأقل جهد ممكن. يوفر [حصة استخدام مجانية سخية](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) للحسابات الشخصية. قم بتكوين [مهلات](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) لإيقاف أو حذف الأكواد غير النشطة لتعظيم استخدام حصتك.

## 1. تنفيذ المهام

كل درس سيكون له مهام _اختيارية_ قد تكون متوفرة في لغة برمجة واحدة أو أكثر بما في ذلك: Python و .NET/C# و Java و JavaScript/TypeScript. يوفر هذا القسم إرشادات عامة تتعلق بتنفيذ تلك المهام.

### 1.1 مهام Python

تُقدم مهام Python إما كتطبيقات (ملفات `.py`) أو دفاتر Jupyter (ملفات `.ipynb`).
- لتشغيل الدفتر، افتحه في Visual Studio Code ثم اضغط على _Select Kernel_ (في الأعلى يمين) واختر خيار Python 3 الافتراضي المعروض. يمكنك الآن الضغط على _Run All_ لتنفيذ الدفتر.
- لتشغيل تطبيقات Python من سطر الأوامر، اتبع تعليمات المهام المحددة لضمان اختيار الملفات الصحيحة وتوفير الحجج المطلوبة.

## 2. تكوين المزودين

يمكن إعداد المهام **أيضًا** للعمل مع واحدة أو أكثر من عمليات نشر نموذج اللغة الكبير (LLM) من خلال مزود خدمة مدعوم مثل OpenAI أو Azure أو Hugging Face. توفر هذه نقطة نهاية _مستضافة_ (API) يمكننا الوصول إليها برمجيًا باستخدام الاعتمادات الصحيحة (مفتاح API أو رمز). في هذه الدورة، نناقش هؤلاء المزودين:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة بما في ذلك سلسلة GPT الأساسية.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع التركيز على جاهزية المؤسسات.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال.

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. المهام اختيارية لذا يمكنك اختيار إعداد واحد، جميع - أو لا شيء - من المزودين بناءً على اهتماماتك. بعض الإرشادات للتسجيل:

| التسجيل | التكلفة | مفتاح API | الملعب | التعليقات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [التسعير](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [بناءً على المشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | نماذج متعددة متوفرة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [التسعير](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [البدء السريع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [البدء السريع في الاستوديو](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [يجب التقديم مسبقًا للحصول على الوصول](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [التسعير](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat يحتوي على نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

اتبع الإرشادات أدناه لتكوين هذا المستودع للاستخدام مع مختلف المزودين. المهام التي تتطلب مزودًا معينًا ستحتوي على أحد هذه العلامات في اسم الملف:
 - `aoai` - يتطلب نقطة نهاية Azure OpenAI، مفتاح
 - `oai` - يتطلب نقطة نهاية OpenAI، مفتاح
 - `hf` - يتطلب رمز Hugging Face

يمكنك تكوين واحد، لا شيء، أو جميع المزودين. ستظهر أخطاء في المهام ذات الصلة عند فقدان الاعتمادات.

### 2.1 إنشاء ملف `.env`

نفترض أنك قد قرأت بالفعل الإرشادات أعلاه وسجلت مع المزود المناسب، وحصلت على الاعتمادات المطلوبة (API_KEY أو رمز). في حالة Azure OpenAI، نفترض أيضًا أنك لديك عملية نشر صالحة لخدمة Azure OpenAI (نقطة نهاية) مع نموذج GPT واحد على الأقل منشور لإكمال الدردشة.

الخطوة التالية هي تكوين **متغيرات البيئة المحلية** كما يلي:

1. ابحث في المجلد الجذري عن ملف `.env.copy` الذي يجب أن يحتوي على محتويات مثل هذه:

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

2. انسخ هذا الملف إلى `.env` باستخدام الأمر أدناه. يتم تجاهل هذا الملف _gitignore-d_، مما يحافظ على الأسرار آمنة.

   ```bash
   cp .env.copy .env
   ```

3. قم بملء القيم (استبدل العناصر النائبة على الجانب الأيمن من `=`) كما هو موضح في القسم التالي.

3. (اختياري) إذا كنت تستخدم GitHub Codespaces، لديك الخيار لحفظ متغيرات البيئة كأسرار Codespaces مرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **لكن لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستظل بحاجة إلى إعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

### 2.2 ملء ملف `.env`

لنلقي نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير  | الوصف  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز الوصول الذي قمت بإعداده في ملفك الشخصي |
| OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام الخدمة لنقاط النهاية غير التابعة لـ Azure OpenAI |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه هي نقطة النهاية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _توليد النص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _تضمين النص_ |
| | |

ملاحظة: تعكس آخر متغيرين لـ Azure OpenAI نموذجًا افتراضيًا لإكمال الدردشة (توليد النص) والبحث عن المتجهات (التضمينات) على التوالي. سيتم تحديد تعليمات إعدادها في المهام ذات الصلة.

### 2.3 تكوين Azure: من البوابة

ستجد قيم نقطة النهاية ومفتاح Azure OpenAI في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) لذا دعونا نبدأ هناك.

1. اذهب إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. اضغط على خيار **Keys and Endpoint** في الشريط الجانبي (القائمة على اليسار).
1. اضغط على **Show Keys** - يجب أن ترى ما يلي: KEY 1، KEY 2 ونقطة النهاية.
1. استخدم قيمة KEY 1 لـ AZURE_OPENAI_API_KEY
1. استخدم قيمة نقطة النهاية لـ AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج إلى نقاط النهاية للنماذج المحددة التي قمنا بنشرها.

1. اضغط على خيار **Model deployments** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.
1. في الصفحة الوجهة، اضغط على **Manage Deployments**

سيأخذك هذا إلى موقع Azure OpenAI Studio، حيث سنجد القيم الأخرى كما هو موضح أدناه.

### 2.4 تكوين Azure: من الاستوديو

1. انتقل إلى [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **من موردك** كما هو موضح أعلاه.
1. اضغط على علامة التبويب **Deployments** (الشريط الجانبي، يسار) لعرض النماذج المنشورة حاليًا.
1. إذا لم يتم نشر النموذج المطلوب، استخدم **Create new deployment** لنشره.
1. ستحتاج إلى نموذج _توليد النص_ - نوصي بـ: **gpt-35-turbo**
1. ستحتاج إلى نموذج _تضمين النص_ - نوصي بـ **text-embedding-ada-002**

الآن قم بتحديث متغيرات البيئة لتعكس _اسم النشر_ المستخدم. سيكون هذا عادةً نفس اسم النموذج ما لم تقم بتغييره صراحةً. لذلك، كمثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**لا تنسى حفظ ملف .env عند الانتهاء**. يمكنك الآن الخروج من الملف والعودة إلى التعليمات لتشغيل الدفتر.

### 2.5 تكوين OpenAI: من الملف الشخصي

يمكن العثور على مفتاح API الخاص بـ OpenAI في [حسابك في OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك واحد، يمكنك التسجيل للحصول على حساب وإنشاء مفتاح API. بمجرد حصولك على المفتاح، يمكنك استخدامه لملء المتغير `OPENAI_API_KEY` في ملف `.env`.

### 2.6 تكوين Hugging Face: من الملف الشخصي

يمكن العثور على رمز Hugging Face في ملفك الشخصي تحت [رموز الوصول](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تقم بنشر أو مشاركة هذه الرموز علنًا. بدلاً من ذلك، قم بإنشاء رمز جديد لاستخدام هذا المشروع ونسخه إلى ملف `.env` تحت المتغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذا ليس مفتاح API تقنيًا ولكنه يستخدم للمصادقة لذا نحن نحافظ على تلك التسمية لأغراض التناسق.

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.