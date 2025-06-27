<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:06:57+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ar"
}
-->
# إعداد بيئة التطوير الخاصة بك

قمنا بإعداد هذا المستودع والدورة باستخدام [حاوية تطوير](https://containers.dev?WT.mc_id=academic-105485-koreyst) تحتوي على بيئة تشغيل عالمية تدعم تطوير Python3، .NET، Node.js وJava. يتم تعريف التكوين المرتبط في ملف `devcontainer.json` الموجود في مجلد `.devcontainer/` في جذر هذا المستودع.

لتفعيل حاوية التطوير، قم بتشغيلها في [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (لبيئة تشغيل مستضافة في السحابة) أو في [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (لبيئة تشغيل مستضافة على جهاز محلي). اقرأ [هذه الوثائق](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) لمزيد من التفاصيل حول كيفية عمل حاويات التطوير داخل VS Code.

> [!TIP]  
> نوصي باستخدام GitHub Codespaces لبدء سريع مع جهد قليل. يوفر [حصة استخدام مجانية سخية](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) للحسابات الشخصية. قم بتكوين [فترات التوقف](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) لإيقاف أو حذف المساحات غير النشطة لتعظيم استخدام حصتك.

## 1. تنفيذ المهام

كل درس سيكون لديه مهام _اختيارية_ قد تُقدم بلغة برمجة واحدة أو أكثر بما في ذلك: Python، .NET/C#، Java وJavaScript/TypeScript. يوفر هذا القسم إرشادات عامة متعلقة بتنفيذ تلك المهام.

### 1.1 مهام Python

تُقدم مهام Python إما كتطبيقات (ملفات `.py`) أو دفاتر Jupyter (ملفات `.ipynb`).
- لتشغيل الدفتر، افتحه في Visual Studio Code ثم انقر على _اختيار Kernel_ (في الأعلى يمينًا) واختر خيار Python 3 الافتراضي المعروض. يمكنك الآن _تشغيل الكل_ لتنفيذ الدفتر.
- لتشغيل تطبيقات Python من سطر الأوامر، اتبع تعليمات المهام المحددة لضمان اختيار الملفات الصحيحة وتقديم الحجج المطلوبة.

## 2. تكوين مقدمي الخدمات

قد يتم إعداد المهام للعمل ضد نشر نموذج لغة كبير (LLM) واحد أو أكثر من خلال مقدم خدمة مدعوم مثل OpenAI، Azure أو Hugging Face. هذه توفر _نقطة نهاية مستضافة_ (API) يمكننا الوصول إليها برمجيًا مع بيانات الاعتماد الصحيحة (مفتاح API أو رمز). في هذه الدورة، نناقش هؤلاء المقدمي الخدمات:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة بما في ذلك سلسلة GPT الأساسية.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع التركيز على جاهزية المؤسسات.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال.

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. المهام اختيارية لذلك يمكنك اختيار إعداد واحد، الكل - أو لا شيء - من المقدمي الخدمات بناءً على اهتماماتك. بعض الإرشادات للتسجيل:

| التسجيل | التكلفة | مفتاح API | الملعب | التعليقات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [التسعير](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [قائم على المشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | نماذج متعددة متاحة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [التسعير](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [بداية سريعة SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [بداية سريعة Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [يجب التقديم مسبقًا للحصول على الوصول](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [التسعير](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat لديه نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

اتبع التعليمات أدناه لتكوين هذا المستودع للاستخدام مع مقدمي الخدمات المختلفين. المهام التي تتطلب مقدم خدمة محدد ستحتوي على أحد هذه العلامات في اسم الملف:
- `aoai` - يتطلب نقطة نهاية Azure OpenAI، مفتاح
- `oai` - يتطلب نقطة نهاية OpenAI، مفتاح
- `hf` - يتطلب رمز Hugging Face

يمكنك تكوين واحد، لا شيء، أو جميع مقدمي الخدمات. ستظهر الأخطاء في المهام المرتبطة بسبب فقدان بيانات الاعتماد.

### 2.1. إنشاء ملف `.env`

نفترض أنك قد قرأت الإرشادات أعلاه وقمت بالتسجيل مع مقدم الخدمة المناسب، وحصلت على بيانات الاعتماد المطلوبة (API_KEY أو رمز). في حالة Azure OpenAI، نفترض أيضًا أن لديك نشر صالح لخدمة Azure OpenAI (نقطة نهاية) مع نموذج GPT واحد على الأقل منشور لإكمال الدردشة.

الخطوة التالية هي تكوين **المتغيرات البيئية المحلية** كما يلي:

1. ابحث في المجلد الجذر عن ملف `.env.copy` الذي يجب أن يحتوي على محتويات مثل هذه:

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

2. انسخ هذا الملف إلى `.env` باستخدام الأمر أدناه. هذا الملف مُحذوف من gitignore، مما يحافظ على الأسرار آمنة.

   ```bash
   cp .env.copy .env
   ```

3. املأ القيم (استبدل العناصر النائبة على الجانب الأيمن من `=`) كما هو موضح في القسم التالي.

3. (اختياري) إذا كنت تستخدم GitHub Codespaces، لديك الخيار لحفظ المتغيرات البيئية كأسرار Codespaces مرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **ومع ذلك، لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستحتاج إلى إعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

### 2.2. تعبئة ملف `.env`

لنلقي نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير  | الوصف  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز الوصول الذي قمت بإعداده في ملفك الشخصي |
| OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام الخدمة لنقاط النهاية غير Azure OpenAI |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه هي النقطة النهائية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _توليد النص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _التضمين النصي_ |
| | |

ملاحظة: المتغيران الأخيران لـ Azure OpenAI يعكسان نموذجًا افتراضيًا لإكمال الدردشة (توليد النص) والبحث عن المتجهات (التضمين) على التوالي. سيتم تحديد تعليمات إعدادهم في المهام ذات الصلة.

### 2.3 تكوين Azure: من البوابة

يمكن العثور على قيم النقطة النهائية والمفتاح لـ Azure OpenAI في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) لذا لنبدأ من هناك.

1. اذهب إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. انقر على خيار **المفاتيح والنقطة النهائية** في الشريط الجانبي (القائمة في اليسار).
1. انقر على **إظهار المفاتيح** - يجب أن ترى ما يلي: المفتاح 1، المفتاح 2 والنقطة النهائية.
1. استخدم قيمة المفتاح 1 لـ AZURE_OPENAI_API_KEY
1. استخدم قيمة النقطة النهائية لـ AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج إلى النقاط النهائية للنماذج المحددة التي قمنا بنشرها.

1. انقر على خيار **نشر النماذج** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.
1. في صفحة الوجهة، انقر على **إدارة النشر**

سيأخذك هذا إلى موقع Azure OpenAI Studio، حيث سنجد القيم الأخرى كما هو موضح أدناه.

### 2.4 تكوين Azure: من الاستوديو

1. انتقل إلى [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **من المورد الخاص بك** كما هو موضح أعلاه.
1. انقر على علامة تبويب **النشر** (الشريط الجانبي، اليسار) لعرض النماذج المنشورة حاليًا.
1. إذا لم يتم نشر النموذج المطلوب، استخدم **إنشاء نشر جديد** لنشره.
1. ستحتاج إلى نموذج _توليد النص_ - نوصي بـ: **gpt-35-turbo**
1. ستحتاج إلى نموذج _التضمين النصي_ - نوصي بـ **text-embedding-ada-002**

الآن قم بتحديث المتغيرات البيئية لتعكس اسم النشر المستخدم. سيكون هذا عادةً نفس اسم النموذج ما لم تقم بتغييره صراحةً. لذا، كمثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**لا تنسى حفظ ملف .env عند الانتهاء**. يمكنك الآن الخروج من الملف والعودة إلى التعليمات لتشغيل الدفتر.

### 2.5 تكوين OpenAI: من الملف الشخصي

يمكن العثور على مفتاح API الخاص بك لـ OpenAI في حسابك على [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك واحد، يمكنك التسجيل للحصول على حساب وإنشاء مفتاح API. بمجرد حصولك على المفتاح، يمكنك استخدامه لملء المتغير `OPENAI_API_KEY` في ملف `.env`.

### 2.6 تكوين Hugging Face: من الملف الشخصي

يمكن العثور على رمز Hugging Face الخاص بك في ملفك الشخصي تحت [رموز الوصول](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تقم بنشر أو مشاركة هذه بشكل علني. بدلاً من ذلك، قم بإنشاء رمز جديد لاستخدام هذا المشروع ونسخه إلى ملف `.env` تحت المتغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذا ليس مفتاح API تقنيًا ولكنه يستخدم للمصادقة لذلك نحن نحافظ على تلك التسمية لأجل الاتساق.

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأم هي المصدر الموثوق. بالنسبة للمعلومات الهامة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.