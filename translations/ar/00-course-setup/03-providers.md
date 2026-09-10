# اختيار وتكوين مزود نموذج اللغة الكبير 🔑

يمكن أيضًا إعداد المهام للعمل مع نشر نموذج أو أكثر من نماذج اللغة الكبيرة (LLM) من خلال مزود خدمة مدعوم مثل OpenAI أو Azure أو Hugging Face. توفر هذه نقطة نهاية مستضافة (API) يمكننا الوصول إليها برمجيًا باستخدام بيانات الاعتماد المناسبة (مفتاح API أو رمز توكن). في هذه الدورة، نناقش هؤلاء المزودين:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) مع نماذج متنوعة بما في ذلك سلسلة GPT الأساسية.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) لنماذج OpenAI مع التركيز على الجاهزية للمؤسسات
 - [نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) لنقطة نهاية واحدة ومفتاح API للوصول إلى مئات النماذج من OpenAI وMeta وMistral وCohere وMicrosoft والمزيد (تستبدل نماذج GitHub التي ستتوقف نهاية يوليو 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) للنماذج مفتوحة المصدر وخادم الاستدلال
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) أو [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) إذا كنت تفضل تشغيل النماذج بشكل كامل دون اتصال على جهازك الخاص، دون الحاجة لاشتراك في السحابة

**ستحتاج إلى استخدام حساباتك الخاصة لهذه التمارين**. المهام اختيارية لذا يمكنك اختيار إعداد واحد أو جميع المزودين أو لا شيء حسب اهتماماتك. بعض التوجيهات للتسجيل:

| التسجيل | التكلفة | مفتاح API | ساحة اللعب | التعليقات |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [التسعير](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [مفتاح يعتمد على المشروع](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [واجهة بدون كود، ويب](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | نماذج متعددة متاحة |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [التسعير](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [البدء السريع عبر SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [البدء السريع عبر الاستوديو](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [يجب التقديم مسبقًا للوصول](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [التسعير](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [صفحة نظرة عامة على المشروع](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [ساحة لعب Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | طبقة مجانية متاحة؛ نقطة نهاية واحدة + مفتاح للعديد من مزودي النماذج |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [التسعير](https://huggingface.co/pricing) | [رموز الوصول](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [محادثة Hugging](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [محادثة Hugging بها نماذج محدودة](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | مجاني (يعمل على جهازك) | غير مطلوب | [أوامر CLI/SDK محلية](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | نقطة نهاية متوافقة مع OpenAI تمامًا بدون اتصال |
| | | | | |

اتبع التعليمات أدناه لـ _تكوين_ هذا المستودع لاستخدامه مع المزودين المختلفين. ستحتوي المهام التي تتطلب مزودًا معينًا على واحدة من هذه العلامات في اسم الملف:

- `aoai` - يتطلب نقطة نهاية Azure OpenAI ومفتاح
- `oai` - يتطلب نقطة نهاية OpenAI ومفتاح
- `hf` - يتطلب رمز توكن Hugging Face
- `githubmodels` - يتطلب نقطة نهاية نماذج Microsoft Foundry ومفتاح (نماذج GitHub ستتوقف نهاية يوليو 2026)

يمكنك تكوين واحد، لا شيء، أو جميع المزودين. ستتسبب المهام ذات الصلة في ظهور خطأ في حالة عدم وجود بيانات اعتماد.

## إنشاء ملف `.env`

نفترض أنك قد قرأت التوجيه أعلاه وسجلت مع المزود المناسب، وحصلت على بيانات اعتماد المصادقة المطلوبة (API_KEY أو الرمز). في حالة Azure OpenAI، نفترض أيضًا أن لديك نشرًا صالحًا لخدمة Azure OpenAI (نقطة نهاية) مع نشر نموذج GPT واحد على الأقل لإكمال المحادثة.

الخطوة التالية هي تكوين **متغيرات البيئة المحلية** كما يلي:

1. ابحث في المجلد الجذر عن ملف `.env.copy` الذي يجب أن يحتوي على محتويات مثل هذه:

   ```bash
   # مزود OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI في Microsoft Foundry
   ## (خدمة Azure OpenAI أصبحت الآن جزءًا من Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # تم تعيين الافتراضي! (إصدار API المستقر الحالي)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## نماذج Microsoft Foundry (كتالوج نماذج متعدد المزودين، يحل محل نماذج GitHub التي تتوقف عن العمل في نهاية يوليو 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. انسخ هذا الملف إلى `.env` باستخدام الأمر أدناه. هذا الملف _مضاف إلى gitignore_ للحفاظ على السرية.

   ```bash
   cp .env.copy .env
   ```

3. املأ القيم (استبدل نائبات الرموز على الجانب الأيمن من `=`) كما هو موضح في القسم التالي.

4. (اختياري) إذا كنت تستخدم GitHub Codespaces، لديك خيار حفظ متغيرات البيئة كـ _أسرار Codespaces_ مرتبطة بهذا المستودع. في هذه الحالة، لن تحتاج إلى إعداد ملف .env محلي. **لكن، لاحظ أن هذا الخيار يعمل فقط إذا كنت تستخدم GitHub Codespaces.** ستحتاج إلى إعداد ملف .env إذا كنت تستخدم Docker Desktop بدلاً من ذلك.

## تعبئة ملف `.env`

لنلق نظرة سريعة على أسماء المتغيرات لفهم ما تمثله:

| المتغير  | الوصف  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | هذا هو رمز الوصول الذي قمت بإعداده في ملفك الشخصي |
| OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام الخدمة لنقاط نهاية OpenAI غير Azure |
| AZURE_OPENAI_API_KEY | هذا هو مفتاح التفويض لاستخدام تلك الخدمة |
| AZURE_OPENAI_ENDPOINT | هذه نقطة النهاية المنشورة لمورد Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | هذه نقطة نهاية نشر نموذج _توليد النص_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | هذه نقطة نهاية نشر نموذج _تضمين النصوص_ |
| AZURE_INFERENCE_ENDPOINT | هذه نقطة النهاية لمشروع Microsoft Foundry الخاص بك، تُستخدم لنماذج Microsoft Foundry |
| AZURE_INFERENCE_CREDENTIAL | هذا هو مفتاح API لمشروع Microsoft Foundry الخاص بك |
| | |

ملاحظة: يعكس المتغيران الأخيران في Azure OpenAI نموذجًا افتراضيًا لإكمال المحادثة (توليد النص) والبحث المتجه (التضمينات) على التوالي. ستُحدد التعليمات الخاصة بضبطها في التمارين ذات الصلة.

## تكوين Azure OpenAI: من البوابة الإلكترونية

> **ملاحظة:** خدمة Azure OpenAI أصبحت الآن جزءًا من [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). ما زالت الموارد والنشرات تظهر في بوابة Azure، لكن إدارة النماذج اليومية (النشرات، ساحة اللعب، المراقبة) تتم الآن في بوابة Foundry بدلاً من "استوديو Azure OpenAI" المستقل القديم.

ستجد قيم نقطة النهاية والمفتاح في [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) فلنبدأ من هناك.

1. اذهب إلى [بوابة Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. انقر على خيار **المفاتيح ونقطة النهاية** في الشريط الجانبي (القائمة على اليسار).
1. انقر على **عرض المفاتيح** - يجب أن ترى التالي: المفتاح 1، المفتاح 2 ونقطة النهاية.
1. استخدم قيمة المفتاح 1 لـ AZURE_OPENAI_API_KEY
1. استخدم قيمة نقطة النهاية لـ AZURE_OPENAI_ENDPOINT

بعد ذلك، نحتاج نقاط النهاية للنماذج المحددة التي نشرناها.

1. انقر على خيار **نشرات النماذج** في الشريط الجانبي (القائمة اليسرى) لمورد Azure OpenAI.
1. في الصفحة الوجهة، انقر على **الانتقال إلى بوابة Microsoft Foundry** (أو **إدارة النشرات**، حسب نوع المورد لديك)

سيأخذك هذا إلى بوابة Microsoft Foundry، حيث سنجد القيم الأخرى كما هو موضح أدناه.

## تكوين Azure OpenAI: من بوابة Microsoft Foundry

1. انتقل إلى [بوابة Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **من موردك** كما هو موضح أعلاه.
1. انقر على تبويب **النشرات** (الشريط الجانبي، اليسار) لعرض النماذج المنشورة حاليًا.
1. إذا لم يكن النموذج الذي تريده منشورًا، استخدم **نشر نموذج** لنشره من [كتالوج النماذج](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. ستحتاج إلى نموذج _توليد النص_ - نوصي بـ: **gpt-5-mini**
1. ستحتاج إلى نموذج _تضمين النصوص_ - نوصي بـ **text-embedding-3-small**

عيّن الآن متغيرات البيئة لتعكس _اسم النشر_ المستخدم. عادة ما يكون نفس اسم النموذج ما لم تقم بتغييره صراحة. على سبيل المثال، قد يكون لديك:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**لا تنسَ حفظ ملف .env عند الانتهاء**. يمكنك الخروج من الملف الآن والعودة إلى تعليمات تشغيل الدفتر.

## تكوين OpenAI: من ملف التعريف

يمكنك العثور على مفتاح API الخاص بـ OpenAI في [حساب OpenAI الخاص بك](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). إذا لم يكن لديك، يمكنك التسجيل للحصول على حساب وإنشاء مفتاح API. بمجرد حصولك على المفتاح، يمكنك استخدامه لتعبئة متغير `OPENAI_API_KEY` في ملف `.env`.

## تكوين Hugging Face: من ملف التعريف

يمكنك العثور على رمز توكن Hugging Face في ملفك الشخصي تحت [رموز الوصول](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). لا تقم بنشر هذه أو مشاركتها علنًا. بدلاً من ذلك، أنشئ رمز توكن جديد لهذا المشروع وانسخه إلى ملف `.env` تحت متغير `HUGGING_FACE_API_KEY`. _ملاحظة:_ هذه تقنيًا ليست مفتاح API لكنها تستخدم للمصادقة لذا نحتفظ بهذا التسمية للاتساق.

## تكوين نماذج Microsoft Foundry: من البوابة

> **ملاحظة:** نماذج GitHub ستتوقف نهاية يوليو 2026. نماذج Microsoft Foundry هي البديل المباشر، تقدم نفس كتالوج النماذج المجاني للتجربة وتجربة SDK استدلال Azure AI / OpenAI SDK.

1. اذهب إلى [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) وأنشئ (أو افتح) مشروع Foundry.
1. تصفح [كتالوج النماذج](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) وانشر نموذجًا، على سبيل المثال `gpt-5-mini`.
1. في صفحة **نظرة عامة** للمشروع، انسخ **نقطة النهاية** و **مفتاح API**.
1. استخدم قيمة نقطة النهاية لـ `AZURE_INFERENCE_ENDPOINT` وقيمة المفتاح لـ `AZURE_INFERENCE_CREDENTIAL` في ملف `.env` الخاص بك.

## المزودون المحليون / دون اتصال

إذا كنت تفضل عدم استخدام اشتراك سحابي على الإطلاق، يمكنك تشغيل نماذج مفتوحة متوافقة مباشرة على جهازك:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - وقت تشغيل مايكروسوفت على الجهاز. يختار تلقائيًا أفضل مزود تنفيذ (NPU، GPU، أو CPU) ويعرض نقطة نهاية متوافقة مع OpenAI، لذا يمكنك إعادة استخدام معظم الكود النموذجي في هذه الدورة مع تغييرات قليلة. انظر [وثائق Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) للبدء، أو قم بالتثبيت بواسطة `winget install Microsoft.FoundryLocal` (ويندوز) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - بديل شائع لتشغيل نماذج مفتوحة مثل Llama وPhi وMistral وGemma محليًا.


انظر [الدرس 19: البناء باستخدام SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) لأمثلة عملية باستخدام كلا الخيارين.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->