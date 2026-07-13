# اختيار وتهيئة مزود نموذج لغوي كبير (LLM) 🔑

قد تُعد التعيينات للعمل مع نشر نموذج لغوي كبير واحد أو أكثر عبر مزود خدمة مدعوم مثل OpenAI أو Azure أو Hugging Face. توفر هذه نقطة نهاية مستضافة (API) يمكننا الوصول إليها برمجياً باستخدام بيانات الاعتماد الصحيحة (مفتاح API أو رمز). في هذا المساق، نناقش هؤلاء المزودين:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة تشمل سلسلة GPT الأساسية.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع التركيز على جهوزية المؤسسات
 - [نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) لنقطة نهاية واحدة ومفتاح API للوصول إلى مئات النماذج من OpenAI وMeta وMistral وCohere ومايكروسوفت وغيرهم (تحل محل نماذج GitHub التي ستتوقف نهاية يوليو 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) أو [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) إذا كنت تفضل تشغيل النماذج بالكامل دون اتصال على جهازك الخاص بدون اشتراك سحابي

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. التعيينات اختيارية لذا يمكنك اختيار إعداد واحد أو كلها - أو لا شيء - من المزودين بناءً على اهتماماتك. بعض الإرشادات للتسجيل:

| التسجيل | التكلفة | مفتاح API | الملعب | التعليقات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [التسعير](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [مفتاح حسب المشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | نماذج متعددة متاحة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [التسعير](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [بدء سريع SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [بدء سريع للاستوديو](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [يجب التقديم مسبقًا للوصول](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [التسعير](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [صفحة نظرة عامة على المشروع](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [ملعب Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | متوفر مستوى مجاني؛ نقطة نهاية واحدة + مفتاح لعدة مزودي نماذج |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [التسعير](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat يحتوي على نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | مجاني (يعمل على جهازك) | غير مطلوب | [CLI/SDK محلي](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | نقطة نهاية متوافقة مع OpenAI بدون اتصال بالكامل |
| | | | | |

اتبع الإرشادات أدناه لـ _تهيئة_ هذا المستودع للاستخدام مع مزودين مختلفين. التعيينات التي تتطلب مزودًا محددًا ستحتوي على واحدة من هذه العلامات في اسم الملف:

- `aoai` - يتطلب نقطة نهاية Azure OpenAI، ومفتاح
- `oai` - يتطلب نقطة نهاية OpenAI، ومفتاح
- `hf` - يتطلب رمز Hugging Face
- `githubmodels` - يتطلب نقطة نهاية Microsoft Foundry Models، ومفتاح (نماذج GitHub ستتوقف نهاية يوليو 2026)

يمكنك تهيئة واحد، أو لا شيء، أو كل المزودين. سيفشل التعيين المرتبط إذا كانت بيانات الاعتماد مفقودة.

## إنشاء ملف `.env`

نفترض أنك قد قرأت الإرشادات أعلاه وسجلت مع المزود المناسب، وحصلت على بيانات الاعتماد المطلوبة للمصادقة (API_KEY أو رمز). في حالة Azure OpenAI، نفترض أيضاً أن لديك نشرًا صالحًا لخدمة Azure OpenAI (نقطة نهاية) مع نشر نموذج GPT واحد على الأقل للدردشة.

الخطوة التالية هي تهيئة **متغيرات البيئة المحلية** كما يلي:

1. ابحث في المجلد الجذر عن ملف `.env.copy` الذي يجب أن يحتوي على محتويات مشابهة لهذه:

   ```bash
   # مزود OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## أزور OpenAI في Microsoft Foundry
   ## (خدمة أزور OpenAI الآن جزء من Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # الإعداد الافتراضي! (إصدار API العام المستقر الحالي)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## نماذج Microsoft Foundry (كتالوج نماذج متعدد المزودين، يستبدل نماذج GitHub التي ستتقاعد في نهاية يوليو 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. انسخ ذلك الملف إلى `.env` باستخدام الأمر أدناه. هذا الملف مضاف إلى _gitignore_ للحفاظ على السرية.

   ```bash
   cp .env.copy .env
   ```

3. املأ القيم (استبدل العناصر النائبة على الجانب الأيمن من `=`) كما هو موضح في القسم التالي.

4. (اختياري) إذا كنت تستخدم GitHub Codespaces، لديك خيار حفظ متغيرات البيئة كـ _أسرار Codespaces_ مرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **لكن لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستظل بحاجة إلى إعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

## تعبئة ملف `.env`

دعنا نلقي نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير | الوصف |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز وصول المستخدم الذي قمت بإعداده في ملف التعريف الخاص بك |
| OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام الخدمة لنقاط نهاية OpenAI غير Azure |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه هي نقطة النهاية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _توليد النصوص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه هي نقطة نهاية نشر نموذج _تضمين النصوص_ |
| AZURE_INFERENCE_ENDPOINT | هذه هي نقطة النهاية لمشروع Microsoft Foundry الخاص بك، المستخدمة لنماذج Microsoft Foundry |
| AZURE_INFERENCE_CREDENTIAL | هذا هو مفتاح API لمشروع Microsoft Foundry الخاص بك |
| | |

ملاحظة: المتغيران الأخيران لـ Azure OpenAI يعكسان نموذجًا افتراضيًا لإنهاء الدردشة (توليد النص) والبحث بالشبهات (التضمينات) على التوالي. سيتم تعريف تعليمات تعيينها في التعيينات ذات الصلة.

## تهيئة Azure OpenAI: من البوابة

> **ملاحظة:** خدمة Azure OpenAI أصبحت الآن جزءًا من [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). الموارد والنشرات لا تزال تظهر في بوابة Azure، لكن إدارة النماذج اليومية (النشر، الملعب، المراقبة) تتم الآن عبر بوابة Foundry بدلاً من استوديو Azure OpenAI المنفصل القديم.

ستجد قيم نقطة النهاية والمفتاح لخدمة Azure OpenAI في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) فلنبدأ من هناك.

1. اذهب إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. انقر على خيار **المفاتيح ونقطة النهاية** في الشريط الجانبي (القائمة على اليسار).
1. انقر على **عرض المفاتيح** - يجب أن ترى ما يلي: المفتاح 1، المفتاح 2، ونقطة النهاية.
1. استخدم قيمة المفتاح 1 للمتحول AZURE_OPENAI_API_KEY
1. استخدم قيمة نقطة النهاية للمتحول AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج إلى نقاط النهاية للنماذج المحددة التي نشرناها.

1. انقر على خيار **نشر النماذج** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.
1. في الصفحة المقصودة، انقر على **الذهاب إلى بوابة Microsoft Foundry** (أو **إدارة النشرات**، حسب نوع المورد الخاص بك)

سينقلك هذا إلى بوابة Microsoft Foundry، حيث سنجد القيم الأخرى كما هو موضح أدناه.

## تهيئة Azure OpenAI: من بوابة Microsoft Foundry

1. انتقل إلى [بوابة Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **من مورذك** كما هو موضح أعلاه.
1. انقر على تبويب **النشرات** (الشريط الجانبي الأيسر) لعرض النماذج المنشورة حاليا.
1. إذا لم يكن النموذج المرغوب منشرًا، استخدم **نشر نموذج** لنشره من [كتالوج النماذج](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. ستحتاج إلى نموذج _توليد نصوص_ - نوصي بـ: **gpt-4o-mini**
1. ستحتاج إلى نموذج _تضمين نصوص_ - نوصي بـ **text-embedding-3-small**

الآن حدث متغيرات البيئة لتعكس اسم _النشر_ المستخدم. سيكون هذا عادةً نفس اسم النموذج ما لم تقم بتغييره صراحةً. على سبيل المثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**لا تنس حفظ ملف .env عند الانتهاء**. يمكنك الآن الخروج من الملف والعودة إلى التعليمات لتشغيل المفكرة.

## تهيئة OpenAI: من الملف الشخصي

يمكنك العثور على مفتاح API الخاص بك من OpenAI في [حساب OpenAI الخاص بك](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك واحد، يمكنك التسجيل للحصول على حساب وإنشاء مفتاح API. بمجرد أن تحصل على المفتاح، يمكنك استخدامه لتعبئة متغير `OPENAI_API_KEY` في ملف `.env`.

## تهيئة Hugging Face: من الملف الشخصي

يمكنك العثور على رمز Hugging Face الخاص بك في ملف التعريف الخاص بك تحت [رموز الوصول](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تنشر أو تشارك هذه الرموز علنًا. بدلاً من ذلك، أنشئ رمزًا جديدًا لاستخدام هذا المشروع وانسخه في ملف `.env` تحت متغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذا من الناحية التقنية ليس مفتاح API لكنه يستخدم للمصادقة وبالتالي نحتفظ بالتسمية للحفاظ على الاتساق.

## تهيئة نماذج Microsoft Foundry: من البوابة

> **ملاحظة:** ستتوقف نماذج GitHub نهاية يوليو 2026. نماذج Microsoft Foundry هي البديل المباشر، حيث تقدم نفس كتالوج النماذج المجاني لتجربة SDK الاستدلال AI من Azure / OpenAI SDK.

1. اذهب إلى [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) وأنشئ (أو افتح) مشروع Foundry.
1. تصفح [كتالوج النماذج](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) وانشر نموذجًا، مثلاً `gpt-4o-mini`.
1. في صفحة **نظرة عامة** للمشروع، انسخ **نقطة النهاية** و**مفتاح API**.
1. استخدم قيمة نقطة النهاية لـ `AZURE_INFERENCE_ENDPOINT` وقيمة المفتاح لـ `AZURE_INFERENCE_CREDENTIAL` في ملف `.env` الخاص بك.

## المزودون دون اتصال / المحليون

إذا كنت تفضل عدم استخدام اشتراك سحابي على الإطلاق، يمكنك تشغيل نماذج مفتوحة متوافقة مباشرة على جهازك الخاص:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - بيئة تشغيل مايكروسوفت على الجهاز. تختار تلقائيًا أفضل مزود تنفيذ (NPU، GPU، أو CPU) وتوفر نقطة نهاية متوافقة مع OpenAI، لذا يمكنك إعادة استخدام معظم رمز العينة في هذا المساق مع تغييرات قليلة. راجع [وثائق Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) للبدء أو ثبت باستخدام `winget install Microsoft.FoundryLocal` (ويندوز) / `brew install microsoft/foundrylocal/foundrylocal` (ماك).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - بديل مشهور لتشغيل نماذج مفتوحة مثل Llama وPhi وMistral وGemma محليًا.


انظر [الدرس 19: البناء باستخدام SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) للحصول على أمثلة تطبيقية باستخدام كلا الخيارين.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->