<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T13:59:47+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ar"
}
-->
# اختيار وتهيئة مزود LLM 🔑

يمكن أيضًا إعداد الواجبات لتعمل مع واحد أو أكثر من عمليات نشر نماذج اللغة الكبيرة (LLM) من خلال مزود خدمة مدعوم مثل OpenAI أو Azure أو Hugging Face. هذه الخدمات توفر _نقطة نهاية مستضافة_ (API) يمكننا الوصول إليها برمجيًا باستخدام بيانات الاعتماد الصحيحة (مفتاح API أو رمز توكن). في هذا المقرر، سنناقش هذه المزودات:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة تشمل سلسلة GPT الأساسية.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع تركيز على جاهزية المؤسسات
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. الواجبات اختيارية، لذا يمكنك اختيار إعداد مزود واحد أو جميعها أو عدم إعداد أي منها حسب رغبتك. بعض الإرشادات للتسجيل:

| التسجيل | التكلفة | مفتاح API | Playground | ملاحظات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [الأسعار](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [حسب المشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | نماذج متعددة متوفرة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [الأسعار](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [دليل البدء السريع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [دليل البدء السريع Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [يجب التقديم مسبقًا للوصول](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [الأسعار](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat يحتوي على نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

اتبع التعليمات أدناه لـ _تهيئة_ هذا المستودع لاستخدامه مع مزودات مختلفة. الواجبات التي تتطلب مزودًا معينًا ستحتوي على أحد هذه الوسوم في اسم الملف:

- `aoai` - يتطلب نقطة نهاية Azure OpenAI ومفتاح
- `oai` - يتطلب نقطة نهاية OpenAI ومفتاح
- `hf` - يتطلب رمز Hugging Face

يمكنك تهيئة مزود واحد أو جميعها أو عدم تهيئة أي منها. الواجبات المتعلقة ستظهر خطأ في حال عدم وجود بيانات الاعتماد.

## إنشاء ملف `.env`

نفترض أنك قرأت الإرشادات أعلاه وسجلت مع المزود المناسب، وحصلت على بيانات الاعتماد المطلوبة (API_KEY أو رمز توكن). في حالة Azure OpenAI، نفترض أيضًا أن لديك عملية نشر صالحة لخدمة Azure OpenAI (نقطة نهاية) مع نشر نموذج GPT واحد على الأقل لإكمال المحادثة.

الخطوة التالية هي تهيئة **متغيرات البيئة المحلية** كما يلي:

1. ابحث في المجلد الجذري عن ملف باسم `.env.copy` يجب أن يحتوي على محتوى مثل هذا:

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

2. انسخ هذا الملف إلى `.env` باستخدام الأمر أدناه. هذا الملف _مستثنى من git_ للحفاظ على سرية البيانات.

   ```bash
   cp .env.copy .env
   ```

3. املأ القيم (استبدل العناصر النائبة على يمين `=`) كما هو موضح في القسم التالي.

4. (اختياري) إذا كنت تستخدم GitHub Codespaces، لديك خيار حفظ متغيرات البيئة كـ _أسرار Codespaces_ مرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **لكن لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستظل بحاجة لإعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

## تعبئة ملف `.env`

لنلقِ نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير  | الوصف  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز وصول المستخدم الذي قمت بإعداده في ملفك الشخصي |
| OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام الخدمة لنقاط نهاية OpenAI غير Azure |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه هي نقطة النهاية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _توليد النصوص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _تضمين النصوص_ |
| | |

ملاحظة: آخر متغيرين لـ Azure OpenAI يعكسان النموذج الافتراضي لإكمال المحادثة (توليد النصوص) والبحث المتجهي (التضمين) على التوالي. سيتم تحديد تعليمات إعدادها في الواجبات ذات الصلة.

## تهيئة Azure: من البوابة

ستجد قيم نقطة النهاية والمفتاح لـ Azure OpenAI في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) لذا لنبدأ من هناك.

1. انتقل إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. انقر على خيار **Keys and Endpoint** في الشريط الجانبي (القائمة على اليسار).
1. انقر على **Show Keys** - يجب أن ترى: KEY 1، KEY 2 ونقطة النهاية.
1. استخدم قيمة KEY 1 لـ AZURE_OPENAI_API_KEY
1. استخدم قيمة Endpoint لـ AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج إلى نقاط النهاية للنماذج التي قمنا بنشرها.

1. انقر على خيار **Model deployments** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.
1. في الصفحة المقصودة، انقر على **Manage Deployments**

سيأخذك هذا إلى موقع Azure OpenAI Studio، حيث سنجد القيم الأخرى كما هو موضح أدناه.

## تهيئة Azure: من الاستوديو

1. انتقل إلى [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **من موردك** كما هو موضح أعلاه.
1. انقر على تبويب **Deployments** (الشريط الجانبي، يسار) لعرض النماذج المنشورة حاليًا.
1. إذا لم يكن النموذج المطلوب منشورًا، استخدم **Create new deployment** لنشره.
1. ستحتاج إلى نموذج _توليد نصوص_ - نوصي بـ: **gpt-35-turbo**
1. ستحتاج إلى نموذج _تضمين نصوص_ - نوصي بـ **text-embedding-ada-002**

الآن قم بتحديث متغيرات البيئة لتعكس _اسم النشر_ المستخدم. غالبًا ما يكون هذا هو نفسه اسم النموذج إلا إذا قمت بتغييره صراحة. كمثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**لا تنس حفظ ملف .env عند الانتهاء**. يمكنك الآن إغلاق الملف والعودة إلى تعليمات تشغيل الدفتر.

## تهيئة OpenAI: من الملف الشخصي

يمكنك العثور على مفتاح OpenAI API الخاص بك في [حسابك على OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك واحد، يمكنك التسجيل وإنشاء مفتاح API. بعد حصولك على المفتاح، يمكنك استخدامه لتعبئة متغير `OPENAI_API_KEY` في ملف `.env`.

## تهيئة Hugging Face: من الملف الشخصي

يمكنك العثور على رمز Hugging Face الخاص بك في ملفك الشخصي تحت [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تقم بنشر هذه الرموز أو مشاركتها علنًا. بدلاً من ذلك، أنشئ رمزًا جديدًا لاستخدام هذا المشروع وادخله في ملف `.env` تحت متغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذا ليس مفتاح API تقنيًا، لكنه يُستخدم للمصادقة لذا أبقينا على نفس التسمية للاتساق.

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي والموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُنصح بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.