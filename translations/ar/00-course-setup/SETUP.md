<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:22:10+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ar"
}
-->
# إعداد بيئة التطوير الخاصة بك

قمنا بإعداد هذا المستودع والدورة باستخدام [حاوية تطوير](https://containers.dev?WT.mc_id=academic-105485-koreyst) تحتوي على بيئة تشغيل شاملة تدعم تطوير Python3 و .NET و Node.js و Java. تم تعريف التهيئة ذات الصلة في ملف `devcontainer.json` الموجود في مجلد `.devcontainer/` في جذر هذا المستودع.

لتشغيل حاوية التطوير، افتحها في [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (لتشغيل مستضاف على السحابة) أو في [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (لتشغيل محلي على جهازك). اقرأ [هذه الوثائق](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) لمزيد من التفاصيل حول كيفية عمل حاويات التطوير داخل VS Code.

> [!TIP]  
> نوصي باستخدام GitHub Codespaces للبدء السريع بأقل جهد. فهو يوفر [حصة استخدام مجانية سخية](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) للحسابات الشخصية. قم بضبط [فترات التوقف](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) لإيقاف أو حذف الأكواد غير النشطة لتعظيم استخدام حصتك.

## 1. تنفيذ الواجبات

كل درس قد يحتوي على واجبات _اختيارية_ تُقدم بإحدى لغات البرمجة أو أكثر، مثل: Python، .NET/C#، Java و JavaScript/TypeScript. يقدم هذا القسم إرشادات عامة تتعلق بتنفيذ تلك الواجبات.

### 1.1 واجبات Python

تُقدم واجبات Python إما كتطبيقات (`.py` ملفات) أو دفاتر Jupyter (`.ipynb` ملفات).  
- لتشغيل الدفتر، افتحه في Visual Studio Code ثم انقر على _Select Kernel_ (في الأعلى يمين) واختر خيار Python 3 الافتراضي المعروض. يمكنك الآن النقر على _Run All_ لتنفيذ الدفتر.  
- لتشغيل تطبيقات Python من سطر الأوامر، اتبع التعليمات الخاصة بكل واجب لضمان اختيار الملفات الصحيحة وتوفير المعطيات المطلوبة.

## 2. تهيئة المزودين

قد يتم إعداد الواجبات للعمل مع نشرات نماذج اللغة الكبيرة (LLM) من خلال مزود خدمة مدعوم مثل OpenAI أو Azure أو Hugging Face. توفر هذه نقطة نهاية _مستضافة_ (API) يمكننا الوصول إليها برمجياً باستخدام بيانات الاعتماد الصحيحة (مفتاح API أو رمز). في هذه الدورة، نناقش المزودين التاليين:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة تشمل سلسلة GPT الأساسية.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع التركيز على الجاهزية المؤسسية  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. الواجبات اختيارية، لذا يمكنك اختيار إعداد مزود واحد أو جميعهم أو لا شيء حسب اهتماماتك. بعض الإرشادات للتسجيل:

| التسجيل | التكلفة | مفتاح API | بيئة تجريبية | تعليقات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [التسعير](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [مفتاح مشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | نماذج متعددة متاحة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [التسعير](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [بدء سريع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [بدء سريع Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [يجب التقديم مسبقاً للوصول](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [التسعير](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat يحتوي على نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

اتبع التعليمات أدناه لـ _تهيئة_ هذا المستودع للاستخدام مع المزودين المختلفين. الواجبات التي تتطلب مزوداً معيناً ستحتوي على أحد هذه العلامات في اسم الملف:  
 - `aoai` - يتطلب نقطة نهاية Azure OpenAI ومفتاح  
 - `oai` - يتطلب نقطة نهاية OpenAI ومفتاح  
 - `hf` - يتطلب رمز Hugging Face

يمكنك تهيئة مزود واحد أو لا شيء أو جميع المزودين. ستظهر أخطاء في الواجبات ذات الصلة إذا كانت بيانات الاعتماد مفقودة.

###  2.1. إنشاء ملف `.env`

نفترض أنك قد قرأت الإرشادات أعلاه وسجلت لدى المزود المناسب، وحصلت على بيانات الاعتماد المطلوبة (API_KEY أو الرمز). في حالة Azure OpenAI، نفترض أيضاً أن لديك نشراً صالحاً لخدمة Azure OpenAI (نقطة نهاية) مع نشر نموذج GPT واحد على الأقل لإكمال المحادثة.

الخطوة التالية هي تهيئة **متغيرات البيئة المحلية** كما يلي:

1. ابحث في المجلد الجذر عن ملف `.env.copy` الذي يجب أن يحتوي على محتويات مثل:

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

2. انسخ هذا الملف إلى `.env` باستخدام الأمر أدناه. هذا الملف _مُدرج في gitignore_، مما يحافظ على سرية المعلومات.

   ```bash
   cp .env.copy .env
   ```

3. املأ القيم (استبدل العناصر النائبة على يمين `=`) كما هو موضح في القسم التالي.

3. (اختياري) إذا كنت تستخدم GitHub Codespaces، يمكنك حفظ متغيرات البيئة كـ _أسرار Codespaces_ مرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **لكن لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستظل بحاجة إلى إعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

### 2.2. تعبئة ملف `.env`

لنلقِ نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير  | الوصف  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز وصول المستخدم الذي قمت بإعداده في ملفك الشخصي |
| OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام الخدمة لنقاط نهاية OpenAI غير Azure |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه هي نقطة النهاية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه هي نقطة نشر نموذج _توليد النصوص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه هي نقطة نشر نموذج _تضمين النصوص_ |
| | |

ملاحظة: المتغيران الأخيران في Azure OpenAI يعكسان نموذجاً افتراضياً لإكمال المحادثة (توليد النصوص) والبحث المتجه (التضمينات) على التوالي. سيتم تعريف التعليمات الخاصة بهما في الواجبات ذات الصلة.

### 2.3 تهيئة Azure: من البوابة

ستجد قيم نقطة النهاية والمفتاح الخاص بـ Azure OpenAI في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)، فلنبدأ من هناك.

1. اذهب إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. انقر على خيار **Keys and Endpoint** في الشريط الجانبي (القائمة على اليسار).  
1. انقر على **Show Keys** - يجب أن ترى التالي: KEY 1، KEY 2 ونقطة النهاية.  
1. استخدم قيمة KEY 1 لـ AZURE_OPENAI_API_KEY  
1. استخدم قيمة نقطة النهاية لـ AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج إلى نقاط النهاية للنماذج التي نشرناها.

1. انقر على خيار **Model deployments** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.  
1. في الصفحة الوجهة، انقر على **Manage Deployments**

سيأخذك هذا إلى موقع Azure OpenAI Studio، حيث سنجد القيم الأخرى كما هو موضح أدناه.

### 2.4 تهيئة Azure: من الاستوديو

1. انتقل إلى [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **من موردك** كما هو موضح أعلاه.  
1. انقر على تبويب **Deployments** (الشريط الجانبي، اليسار) لعرض النماذج المنشورة حالياً.  
1. إذا لم يكن النموذج المطلوب منشوراً، استخدم **Create new deployment** لنشره.  
1. ستحتاج إلى نموذج _توليد نصوص_ - نوصي بـ: **gpt-35-turbo**  
1. ستحتاج إلى نموذج _تضمين نصوص_ - نوصي بـ **text-embedding-ada-002**

الآن حدّث متغيرات البيئة لتعكس اسم _النشر_ المستخدم. عادةً ما يكون نفس اسم النموذج ما لم تقم بتغييره صراحةً. على سبيل المثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**لا تنس حفظ ملف .env عند الانتهاء**. يمكنك الآن الخروج من الملف والعودة إلى التعليمات لتشغيل الدفتر.

### 2.5 تهيئة OpenAI: من الملف الشخصي

يمكنك العثور على مفتاح API الخاص بـ OpenAI في حسابك على [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك حساب، يمكنك التسجيل وإنشاء مفتاح API. بمجرد حصولك على المفتاح، يمكنك استخدامه لملء متغير `OPENAI_API_KEY` في ملف `.env`.

### 2.6 تهيئة Hugging Face: من الملف الشخصي

يمكنك العثور على رمز Hugging Face الخاص بك في ملفك الشخصي تحت [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تنشر هذه الرموز أو تشاركها علناً. بدلاً من ذلك، أنشئ رمزاً جديداً لاستخدام هذا المشروع ونسخه إلى ملف `.env` تحت متغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذا ليس مفتاح API تقنياً لكنه يُستخدم للمصادقة، لذا نحتفظ بهذا التسمية للاتساق.

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.