# سجل التغييرات

جميع التغييرات الملحوظة على منهج الذكاء الاصطناعي التوليدي للمبتدئين موثقة في هذا الملف.

التنسيق مستند إلى [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). ونظرًا لأن هذا منهج تعليمي وليس حزمة برمجيات مُصنّفة بالإصدار، فإن الإدخالات مُجمعة حسب التاريخ.


## [2026-07-16] — التحقق من المحتوى + أصول الصور للدرس 09

### تم التغيير

- **الدرس 10 (تطبيقات الذكاء الاصطناعي منخفضة الكود):** تحديث رابطين تقاعدا في `docs.microsoft.com/powerapps/...` Dataverse
  إلى `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` الحالية
  (تم التحقق منها مباشرة).
- **الدرس 17 (وكلاء الذكاء الاصطناعي):** تحديث نموذج قديم (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) واسم نشر نائب في نموذج إطار الوكيل
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **جذر `README.md`:** إضافة معرف التتبع `?WT.mc_id=academic-105485-koreyst` المفقود إلى
  رابط *Microsoft for Startups*.
- **أصول صور الدرس 09** تم إعادة إنشائها باستخدام نموذج `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`، `images/mask.png`، `images/sunlit_lounge_result.png`، و
  `images/startup.png` (زوج الأمثلة قبل/بعد التعديل تم إنشاؤه من خلال مكالمة حقيقية
  لـ `client.images.edit` مع قناع مولد).

### تم التحقق منه

- تدقيق ملفات README لدروس 01، 03، 05، 12، 14، و16 — جميعها حالية (تسمية Microsoft Foundry الصحيحة
  والروابط)؛ لا توجد تغييرات مطلوبة.
- أُجري تحقق كامل من صحة ملفات الماركداون لجميع ملفات الماركداون الـ 41 في المستودع (باستثناء الترجمات) لـ
 مسارات المستندات المهجورة، `/en-us/` لغات مايكروسوفت المحلية، أسماء المنتجات/النماذج القديمة، معرفات التتبع المفقودة،
 والروابط/الصور النسبية المعطلة. الفجوة الوحيدة التي يمكن اتخاذ إجراء عليها كانت معرف التتبع الخاص بـ *مايكروسوفت للشركات الناشئة*؛
 أما جميع العلامات الأخرى فقد تم تأكيدها كإيجابيات كاذبة (روابط الترجمة المُنشأة تلقائياً،
 العناصر النائبة المعطلة بالتعليق، و`/en/` عناوين URL الهيكلية لجهات خارجية).

## [2026-07-15] — الدرس 09 (تطبيقات الصور) إعادة كتابة لنماذج صور GPT

### التغييرات

- **إعادة كتابة الدرس 09 "بناء تطبيقات توليد الصور"** حول النموذج الحالي **`gpt-image`**
  عائلة النماذج (افتراضي **`gpt-image-2`**؛ `gpt-image-1.5` / `gpt-image-1-mini` أيضًا GA)، تحل محل محتوى DALL·E 2/3 القديم.
  التصحيحات الرئيسية:
  - تعيد نماذج `gpt-image` الصورة كـ **base64 (`b64_json`)**، وليس كعنوان URL. تم تحديث جميع الأمثلة إلى
    `base64.b64decode(...)` بدلاً من تنزيل `url` باستخدام `requests`.
  - تمت ترقية إصدار واجهة برمجة تطبيقات الصورة إلى `2025-04-01-preview`.
  - تم استبدال القسم "المصطنع" لدرجة الحرارة (نماذج الصور لا تقبل `temperature`) ومحتوى
    **التغييرات** الخاصة بـ DALL·E-2 فقط بقسم **تحرير الصور** (القناع / التلوين).
  - تم تحديث `README.md`، `python/aoai-app.py`، `python/oai-app.py`، `python/aoai-solution.py`، وكلا
    دفتر ملاحظات التعيين (`aoai-assignment.ipynb`، `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`، `.env-sample`)، ودفتر ملاحظات .NET `.dib`.

### تم الحذف

- تم حذف عينات `python/aoai-app-variation.py` و `python/oai-app-variation.py` القديمة التي لم تعد مستخدمة
  (`images.create_variation` لـ DALL·E-2 فقط وغير مدعوم من `gpt-image`).
- تم حذف 4 أصول صور يتيمة مرتبطة بالقسم المحذوف لمقارنة درجة الحرارة
  (`v1-generated-image.png`، `v2-generated-image.png`، `v1-temp-generated-image.png`،
  `v2-temp-generated-image.png`).
- تم إسقاط اعتماد `requests` غير الضروري من عينات Python والمتطلبات في الدرس.

### تم التحقق منها

- تم تشغيل `aoai-app.py` من البداية إلى النهاية مقابل نموذج `gpt-image-1.5` منشور وتم التأكد من أن
  تدفق فك تشفير / حفظ base64 ينتج ملف PNG. تم التأكد من صحة دفاتر الملاحظات كـ JSON.

## [2026-07-14] — تحديث النموذج الافتراضي + توجيه نموذج الاستدلال

### تم التغيير

- **النموذج الافتراضي للدردشة `gpt-4o-mini` → `gpt-5-mini`** عبر عينات التشغيل والوثائق والتكوين في المنهج،
  وكان ذلك بناءً على حالة دورة حياة النموذج: على Microsoft Foundry،
  `gpt-4o-mini` (يتقاعد في 2026-10-01) وكل عائلة `gpt-4.1` (`gpt-4.1`، `gpt-4.1-mini`،
  `gpt-4.1-nano`، التي سيتوقف دعمها في 2026-10-14) يتم **إهمالها**، بينما عائلة **GPT-5
  (`gpt-5-mini`، `gpt-5`، `gpt-5-nano`) متاحة بشكل عام** (سيتوقف دعمها في 2027-02-06). تم التحديث:
  - `.env.copy`، `00-course-setup/03-providers.md` (نشر موصى به وأوامر `az cognitiveservices`
    للنشر)، وملفات README للدروس 04، 06، 07، و15.
  - عينات بايثون في الدرس 06 (`oai-app.py`، `oai-app-recipe.py`، `oai-history-bot.py`،
    `oai-study-buddy.py`، `githubmodels-app.py`) وسكريبتات الدرس 08.
  - عينات TypeScript / JavaScript في الدروس 06، 07، و11، ودفاتر `.dib` .NET لـ
    الدروس 06 و 07.
  - دفاتر التعيين في الدروس 04 و 06 و 07 و 11 (خلايا الكود)، بالإضافة إلى `shared/python/api_utils.py`
    أمثلة سلسلة التوثيق.
- **إرشادات معلمة نموذج التفكير (الجديد).** `gpt-5-mini` هو نموذج *تفكيري*: فهو **لا يدعم**
  `temperature`/`top_p`، ويستخدم `max_completion_tokens` (اكتمالات الدردشة) /
  `max_output_tokens` (واجهة برمجة التطبيقات للردود) بدلاً من `max_tokens`. وبناءً عليه:
  - تمت إزالة `temperature`/`top_p`/`max_tokens` من العينات التي تستخدم الآن `gpt-5-mini` كإعداد افتراضي
    (`githubmodels-app.py`، `aoai-app-recipe.py`، `oai-app-recipe.py`، الدرس 15 RAG README).
  - أضيفت ملاحظة **"نماذج التفكير لا تستخدم `temperature`"** إلى الدرس 06، توضح أن
    يتم توجيه نماذج الاستدلال باستخدام **هندسة المُحفزات + ضوابط الاستدلال** بدلاً من
    مقابض العينة، بينما يظل `temperature`/`top_p` صالحًا على النماذج غير الخاصة بالاستدلال
    (GPT-4.x، Mistral، Llama، Phi، النماذج المفتوحة).
- **`gpt-5-mini` غير مستخدم في درس التخصيص الدقيق (الدرس 18).** يدعم GPT-5 فقط
  التخصيص الدقيق بالتعزيز (RFT)؛ يستمر درس 18 الخاص بالتخصيص الدقيق الموجه (SFT)
  في استخدام `gpt-4.1-mini`، الذي يدعم SFT/DPO.
- **عروض درجة الحرارة تستخدم نموذج Llama.** للحفاظ على تعليم `temperature` (وهي نماذج التفكير
  الرفض)، يتم استخدام نموذج `Llama-3.3-70B-Instruct` عبر نقطة نهاية نماذج Foundry. تمت إضافة متغير جديد
  `AZURE_INFERENCE_CHAT_MODEL` إلى `.env.copy`؛ دفتر ملاحظات الدرس 04/06 `githubmodels` و
  عيّنة `06` `js-githubmodels` تقرأها (مع التراجع إلى `Llama-3.3-70B-Instruct`) وتحفظ
  عروض `temperature`/`top_p`/`max_tokens` الخاصة بها.
- **تم تحديث عينات JS / .NET لـ GPT-5.** تمت إزالة `temperature`/`top_p`/`max_tokens` من GPT-5
  عينات (`06` `recipe-app` TypeScript، `06` `.dib` .NET - التي تثير أيضًا `MaxOutputTokenCount`
  حتى لا يتم اقتطاع ناتج الاستدلال). يستخدم العينة `06` `js-githubmodels` الآن Llama للحفاظ على عرض درجة الحرارة الخاص بها.
  يشير `.dib` إلى أن `Azure.AI.Inference` + نموذج Llama هو الطريقة ل
  عرض `Temperature` في .NET.
- تُترك `gpt-4o-mini` / `gpt-5-mini` في مكانها حيث تبقى دقيقة: مراجع ترميز الرموز `tiktoken`،
  قوائم توفر كتالوج النماذج، ونماذج الكلام في الدرس 02 (`gpt-4o-transcribe`).
- تحفظ عينات الدرس 20 (Mistral) و 21 (Meta) `temperature`/`max_tokens` لأنها تستهدف
  نماذج Mistral/Llama التي تدعم هذه المعلمات.

## [2026-07-06] — تحديث تحديث المحتوى

تحديث واسع للحفاظ على دقة المنهج لعام 2026: واجهات برمجة تطبيقات حديثة، أسماء المنتجات الحالية وأسماء النماذج،
تحديثات توجيه المزود، وأدوات جديدة لتجربة المطور.

### تمت الإضافة

- قسم **Microsoft Agent Framework** في الدرس `17-ai-agents` يشمل وكلاء الدردشة الفردية،
الأدوات/استدعاء الوظائف، تكوين Azure OpenAI (Microsoft Foundry)، ووكلاء متعددين
  تنظيم سير العمل (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** موثق كمزود غير متصل / على الجهاز (جنباً إلى جنب مع Ollama) في
  `00-course-setup/03-providers.md` والدراسة `19-slm`.
- **سير عمل التكامل المستمر**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (مطبقة على وحدة `shared/` التي تتم صيانتها،
    ومرشد عبر بقية المنهج الدراسي)، تمرير ESLint استشاري، ووظيفة pytest.
  - `.github/workflows/security.yml` — تحليل CodeQL (بايثون + جافا سكريبت/تايب سكريبت) و
    مراجعة التبعيات على طلبات السحب.
- **مجموعة الاختبار** تحت `tests/` — 41 اختبار pytest تغطي وحدة الأدوات المشتركة.
- **Azure OpenAI → مهارة ترحيل API الاستجابات** تحت
  `.github/skills/azure-openai-to-responses/` المستخدمة لتوجيه ترحيل API.

### تم التغيير

- **واجهة برمجة تطبيقات إكمالات الدردشة → واجهة برمجة تطبيقات الردود** في جميع أمثلة الدردشة بـ Python وTypeScript
  (`client.responses.create(...)` → `response.output_text`)، بما في ذلك الدروس 04، 06، 07، 11،
  15، و 18، بالإضافة إلى ملفات README الخاصة بها.
- **نماذج GitHub → نماذج Microsoft Foundry** في جميع النصوص وروابط والعينات. نماذج GitHub
  ستتقاعد في نهاية يوليو 2026؛ العينات الآن تشير إلى كتالوج نماذج Microsoft Foundry وتستخدم
  متغيرات البيئة `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **تم تحديث `.env.copy`، `AGENTS.md`، ووثائق الموفر** لتعكس أن Azure OpenAI أصبحت الآن جزءًا
  من Microsoft Foundry، وتم رفع إصدار API الافتراضي إلى `2024-10-21`.
- **عينات TypeScript** (الدروس 06، 07، 08، 11) انتقلت من SDK بيتا المهجور `@azure/openai`
  إلى حزمة `openai` (تستخدم تطبيقات الدردشة واجهة برمجة تطبيقات الردود؛ يستخدم تطبيق البحث
  عميل التضمين).
- **دفاتر ملاحظات .NET** (`dotnet/*.dib`) تم توحيدها على إصدار `Azure.AI.OpenAI` **2.1.0**: الدروس 06 و07
  تستخدم واجهة برمجة تطبيقات `ChatClient`، الدرس 08 يستخدم `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`)، و
  الدرس 09 يستخدم `ImageClient` (`GenerateImage`) مع `gpt-image-1`، مستبدلاً النسخة القديمة
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` من `1.0.0-beta.9`.
- **تحديث اسم المنتج**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (الدروس 14، 16، 17) و"بينغ" → **Microsoft Copilot** (الدرس 12)، حيث يشير ذلك إلى
  المنتجات الحالية.
- **DevContainer** (`.devcontainer/`) الآن يشحن ملحقات Pylance وBlack وRuff وESLint وPrettier وCopilot،
  ويفعل التنسيق عند الحفظ، وينصب `ruff`، `black`، `mypy`، و`pytest` لكي
  يمكن تكرار فحوصات التكامل المستمر محليًا.
- **توليد الصور** (الدرس 09) يوصي بـ `gpt-image-1` لأزور (أزال كتالوج أزور
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** تم تحديثه ليعكس العمل المنجز (هجرة API، CI،
  DevContainer، الاختبارات) والحقائق الحالية (يتم إنتاج الترجمات تلقائيًا بواسطة
  Azure Co-op Translator؛ تم استبدال Assistants API بـ Responses API).

### تم الإصلاح

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` الآن يُرجع
  سلسلة فارغة لمدخلات تحتوي على فراغات فقط بدلاً من رفع خطأ "قصير جدًا" (متوافق مع
  `None` الحالة). تم العثور عليها وتغطيتها بواسطة مجموعة الاختبار الجديدة.
- **عينات صور الدرس 09** — تم تصحيح الأخطاء الحقيقية: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`، `Image.create_variation` → `client.images.create_variation`،
  ومتغير ظلل الوحدة `openai`.
- **دفتر ملاحظات الدرس 15 RAG** — تم إصلاح إعداد العميل، واستبدال `DataFrame.append` المحذوفة
  بـ `pd.concat`، وتحديث استخدام SDK القديم.
- أسماء النماذج المهجورة / المتقاعدة (`gpt-3.5-turbo`، `gpt-35-turbo`) تم استبدالها بـ `gpt-4o-mini`
  في العينات النشطة؛ تم الحفاظ على مخرجات الضبط الدقيق التاريخية في الدرس 18 وتوضيحها
  بدلاً من إعادة كتابتها.

### مهجورة / ملاحظات

- **عينات نماذج Microsoft Foundry** التي تستخدم `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — عينات `githubmodels-*` و`js-githubmodels` والدروس 19، 20،
  و21 — تبقى على واجهة برمجة تطبيقات استنتاج النموذج، التي **لا تدعم** واجهة برمجة تطبيقات الردود. هذه
  تُترك عمداً على ذلك SDK.
- `AzureOpenAI()` يُحتفظ به عمداً حيثما كان مناسباً (التضمينات وتوليد الصور)،
  حيث أن تلك سير العمل ليست جزءًا من ترحيل واجهة برمجة تطبيقات الردود.
- تُحتفظ إشارات `text-embedding-ada-002` حيث يعتمد فهرس التضمين المحسوب مسبقًا عليها.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->