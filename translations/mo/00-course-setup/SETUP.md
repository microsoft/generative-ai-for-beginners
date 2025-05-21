<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:42:57+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "mo"
}
-->
# إعداد بيئة التطوير الخاصة بك

قمنا بإعداد هذا المستودع والدورة باستخدام [حاوية تطوير](https://containers.dev?WT.mc_id=academic-105485-koreyst) تحتوي على بيئة تشغيل عالمية تدعم تطوير Python3 و .NET و Node.js و Java. يتم تعريف التكوين المرتبط في ملف `devcontainer.json` الموجود في مجلد `.devcontainer/` في جذر هذا المستودع.

لتفعيل حاوية التطوير، قم بتشغيلها في [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (لبيئة تشغيل مستضافة على السحابة) أو في [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (لبيئة تشغيل مستضافة على الجهاز المحلي). اقرأ [هذا المستند](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) للحصول على مزيد من التفاصيل حول كيفية عمل حاويات التطوير داخل VS Code.

> [!TIP]  
> نوصي باستخدام GitHub Codespaces للبدء السريع بأقل جهد. يوفر [حصة استخدام مجانية](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) سخية للحسابات الشخصية. قم بتكوين [الفترات الزمنية](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) لإيقاف أو حذف مساحات الأكواد غير النشطة لتعظيم استخدام حصتك.

## 1. تنفيذ التعيينات

كل درس سيكون لديه تعيينات _اختيارية_ قد تكون متاحة بلغة برمجة واحدة أو أكثر بما في ذلك: Python، .NET/C#، Java و JavaScript/TypeScript. يوفر هذا القسم إرشادات عامة تتعلق بتنفيذ هذه التعيينات.

### 1.1 تعيينات Python

تُقدم تعيينات Python إما كتطبيقات (ملفات `.py`) أو دفاتر Jupyter (ملفات `.ipynb`). 
- لتشغيل الدفتر، افتحه في Visual Studio Code ثم انقر على _Select Kernel_ (في أعلى اليمين) واختر خيار Python 3 الافتراضي المعروض. يمكنك الآن _Run All_ لتنفيذ الدفتر.
- لتشغيل تطبيقات Python من سطر الأوامر، اتبع التعليمات الخاصة بالتعيين لضمان اختيار الملفات الصحيحة وتوفير الوسيطات المطلوبة.

## 2. تكوين مقدمي الخدمات

قد يتم إعداد التعيينات أيضًا للعمل مع واحد أو أكثر من نماذج اللغة الكبيرة (LLM) من خلال مقدم خدمة مدعوم مثل OpenAI، Azure أو Hugging Face. توفر هذه نقطة نهاية مستضافة (API) يمكننا الوصول إليها برمجيًا مع الاعتمادات الصحيحة (مفتاح API أو رمز). في هذه الدورة، نناقش هؤلاء المزودين:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة بما في ذلك سلسلة GPT الأساسية.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع التركيز على جاهزية المؤسسات.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال.

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. التعيينات اختيارية لذا يمكنك اختيار إعداد واحد، جميعهم - أو لا شيء - من المزودين بناءً على اهتماماتك. بعض الإرشادات للتسجيل:

| التسجيل | التكلفة | مفتاح API | ملعب | التعليقات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [التسعير](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [قائم على المشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | تتوفر نماذج متعددة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [التسعير](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [البدء السريع لـ SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [البدء السريع للاستوديو](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [يجب التقديم مسبقًا للوصول](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [التسعير](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat لديها نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

اتبع الإرشادات أدناه لـ _تكوين_ هذا المستودع لاستخدامه مع مزودين مختلفين. التعيينات التي تتطلب مزودًا محددًا ستحتوي على واحدة من هذه العلامات في اسم الملف الخاص بها:
 - `aoai` - يتطلب نقطة نهاية Azure OpenAI، مفتاح
 - `oai` - يتطلب نقطة نهاية OpenAI، مفتاح
 - `hf` - يتطلب رمز Hugging Face

يمكنك تكوين واحد، لا شيء، أو جميع المزودين. التعيينات ذات الصلة ستفشل ببساطة في حالة عدم وجود الاعتمادات.

### 2.1. إنشاء ملف `.env`

نفترض أنك قد قرأت الإرشادات أعلاه وسجلت مع المزود ذي الصلة، وحصلت على الاعتمادات المطلوبة للمصادقة (API_KEY أو رمز). في حالة Azure OpenAI، نفترض أيضًا أن لديك نشر صالح لخدمة Azure OpenAI (نقطة نهاية) مع نشر نموذج GPT واحد على الأقل لإكمال الدردشة.

الخطوة التالية هي تكوين **المتغيرات البيئية المحلية** الخاصة بك كما يلي:

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

2. انسخ هذا الملف إلى `.env` باستخدام الأمر أدناه. هذا الملف يتم تجاهله في git، مما يحافظ على الأسرار بأمان.

   ```bash
   cp .env.copy .env
   ```

3. املأ القيم (استبدل العناصر النائبة على الجانب الأيمن من `=`) كما هو موضح في القسم التالي.

3. (اختياري) إذا كنت تستخدم GitHub Codespaces، لديك خيار حفظ المتغيرات البيئية كأسرار Codespaces المرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **ومع ذلك، لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستظل بحاجة إلى إعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

### 2.2. ملء ملف `.env`

لنلقِ نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير | الوصف |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز الوصول الذي قمت بإعداده في ملفك الشخصي |
| OPENAI_API_KEY | هذا هو مفتاح التصريح لاستخدام الخدمة لنقاط نهاية OpenAI غير Azure |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التصريح لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه هي نقطة النهاية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _توليد النص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _تضمين النص_ |
| | |

ملاحظة: تعكس آخر متغيرين من Azure OpenAI نموذجًا افتراضيًا لإكمال الدردشة (توليد النص) والبحث المتجه (التضمين) على التوالي. سيتم تحديد التعليمات لإعدادها في التعيينات ذات الصلة.

### 2.3 تكوين Azure: من البوابة

يمكن العثور على قيم نقطة النهاية والمفتاح لـ Azure OpenAI في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) لذا لنبدأ من هناك.

1. اذهب إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. انقر على خيار **المفاتيح ونقطة النهاية** في الشريط الجانبي (القائمة على اليسار).
1. انقر على **إظهار المفاتيح** - يجب أن ترى ما يلي: KEY 1، KEY 2 ونقطة النهاية.
1. استخدم قيمة KEY 1 لـ AZURE_OPENAI_API_KEY
1. استخدم قيمة نقطة النهاية لـ AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج إلى نقاط النهاية للنماذج المحددة التي قمنا بنشرها.

1. انقر على خيار **نشر النماذج** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.
1. في الصفحة الوجهة، انقر على **إدارة النشر**

سيأخذك هذا إلى موقع Azure OpenAI Studio، حيث سنجد القيم الأخرى كما هو موضح أدناه.

### 2.4 تكوين Azure: من الاستوديو

1. انتقل إلى [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **من المورد الخاص بك** كما هو موضح أعلاه.
1. انقر على علامة التبويب **النشر** (الشريط الجانبي، اليسار) لعرض النماذج المنشورة حاليًا.
1. إذا لم يتم نشر النموذج المطلوب، استخدم **إنشاء نشر جديد** لنشره.
1. ستحتاج إلى نموذج _توليد النص_ - نوصي بـ: **gpt-35-turbo**
1. ستحتاج إلى نموذج _تضمين النص_ - نوصي بـ **text-embedding-ada-002**

الآن قم بتحديث المتغيرات البيئية لتعكس _اسم النشر_ المستخدم. سيكون هذا عادة نفس اسم النموذج إلا إذا قمت بتغييره صراحة. لذا، كمثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**لا تنس حفظ ملف .env عند الانتهاء**. يمكنك الآن الخروج من الملف والعودة إلى التعليمات لتشغيل الدفتر.

### 2.5 تكوين OpenAI: من الملف الشخصي

يمكن العثور على مفتاح API الخاص بك لـ OpenAI في حسابك على [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك واحد، يمكنك التسجيل للحصول على حساب وإنشاء مفتاح API. بمجرد أن يكون لديك المفتاح، يمكنك استخدامه لملء المتغير `OPENAI_API_KEY` في ملف `.env`.

### 2.6 تكوين Hugging Face: من الملف الشخصي

يمكن العثور على رمز Hugging Face الخاص بك في ملفك الشخصي تحت [رموز الوصول](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تنشر أو تشارك هذه علنًا. بدلاً من ذلك، قم بإنشاء رمز جديد لاستخدام هذا المشروع وانسخه في ملف `.env` تحت المتغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذا ليس مفتاح API تقنيًا ولكنه يستخدم للمصادقة لذا نحافظ على تسمية تلك التسمية للتوافق.

I'm sorry, but I currently don't support translations to "mo." Could you please specify the language you are referring to?