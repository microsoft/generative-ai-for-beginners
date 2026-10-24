# سجل التغييرات

جميع التغييرات الهامة على منهج الذكاء الاصطناعي التوليدي للمبتدئين موثقة في هذا الملف.

التنسيق مستند إلى [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). وبما أن هذا منهج تعليمي بدلاً من حزمة برامج ذات إصدارات،
فالإدخالات منظمة حسب التاريخ.

## [2026-07-16] — التحقق من المحتوى + أصول صور الدرس 09

### تم التغيير

- **الدرس 10 (تطبيقات الذكاء الاصطناعي منخفضة الكود):** تم تحديث رابطين متقاعدين من `docs.microsoft.com/powerapps/...` Dataverse
  إلى `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` الحالي
  (تم التحقق منها مباشرًة).
- **الدرس 17 (وكلاء الذكاء الاصطناعي):** تم تحديث مثال نموذج قديم (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) واسم نشر عنصر نائب في نموذج إطار الوكيل
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **جذر `README.md`:** تمت إضافة معرّف تتبع `?WT.mc_id=academic-105485-koreyst` المفقود إلى
  رابط *Microsoft for Startups*.
- تم إعادة إنشاء أصول الصور للدرس 09 باستخدام نموذج `gpt-image`: `images/generated-image.png`،
  `images/sunlit_lounge.png`، `images/mask.png`، `images/sunlit_lounge_result.png`، و
  `images/startup.png` (زوج قبل/بعد مثال التحرير تم إنتاجه عبر مكالمة `client.images.edit` حقيقية مع قناع مولد).




  والروابط)؛ لا حاجة لأي تغييرات.
- تم تشغيل تحقق كامل من ملفات ماركداون الـ 41 في المستودع (باستثناء الترجمات) لفحص
  مسارات الوثائق المهجورة، `/en-us/` لغات Microsoft، أسماء المنتجات/النماذج القديمة، مفقودات معرّفات التتبع،
  والروابط/الصور النسبية المعطلة. كان الفارق القابل للتنفيذ الوحيد هو فجوة معرّف التتبع في *Microsoft for Startups*؛
  تم تأكيد أن كل الإشعارات الأخرى إيجابيات كاذبة (روابط الترجمة التلقائية،
  نماذج عنصر نائب تم التعليق عليها، وروابط الهيكلية لطرف ثالث `/en/`).






- **أُعيد كتابة الدرس 09 "بناء تطبيقات توليد الصور"** حول **`gpt-image`** الحالي
  عائلة النماذج (الافتراضي **`gpt-image-2`**؛ `gpt-image-1.5` / `gpt-image-1-mini` أيضًا GA)، لتحل محل
  محتوى DALL·E 2/3 القديم. التصحيحات الرئيسية:
  - نماذج `gpt-image` تعيد الصورة كـ **base64 (`b64_json`)**، وليس كعنوان URL. تم تحديث جميع العينات إلى
    `base64.b64decode(...)` بدلًا من تنزيل `url` مع `requests`.
  - تحديث إصدار واجهة برمجة تطبيقات الصورة إلى `2025-04-01-preview`.
  - استبدال القسم المزيف "temperature" (نماذج الصور لا تأخذ `temperature`) ومحتوى
    تعديلات الصور الخاص فقط بـ DALL·E-2 بـ قسم **تحرير الصور** (القناع/الترميم).
  - تحديث `README.md`، `python/aoai-app.py`، `python/oai-app.py`، `python/aoai-solution.py`، كلا
    دفاتر التعيين (`aoai-assignment.ipynb`، `oai-assignment.ipynb`)،
    `typescript/image-generation-app` (`main.ts`، `.env-sample`)، ودفتر `.dib` الخاص بـ .NET.

### تمت الإزالة

- حذف عينات `python/aoai-app-variation.py` و`python/oai-app-variation.py` المهجورة
  (`images.create_variation` خاص بـ DALL·E-2 وغير مدعوم من `gpt-image`).
- حذف ٤ أصول صور يتيمة مرتبطة بقسم مقارنة درجات الحرارة المحذوف
  (`v1-generated-image.png`، `v2-generated-image.png`، `v1-temp-generated-image.png`،
  `v2-temp-generated-image.png`).
- إسقاط الاعتماد غير الضروري `requests` من عينات بايثون ومتطلبات الدرس.

### تم التأكد منها

- تشغيل `aoai-app.py` من البداية للنهاية ضد نموذج `gpt-image-1.5` المنشور وتأكيد أن
  تدفق فك ترميز/حفظ base64 ينتج صورة PNG. تأكيد أن دفاتر الملاحظات صالحة JSON.

## [2026-07-14] — تحديث النموذج الافتراضي + توجيه نموذج الاستدلال

### تغييرات

- **النموذج الافتراضي للدردشة `gpt-4o-mini` → `gpt-5-mini`** عبر عينات التشغيل،
  المستندات، والتكوين في المنهج الدراسي. كان هذا مدفوعًا بحالة دورة حياة النموذج: على Microsoft Foundry،
  `gpt-4o-mini` (يتقاعد في 2026-10-01) وعائلة `gpt-4.1` بأكملها (`gpt-4.1`، `gpt-4.1-mini`،
  `gpt-4.1-nano`، يتقاعدون في 2026-10-14) **ستتوقف دعمها**، في حين أن **عائلة GPT-5
  (`gpt-5-mini`، `gpt-5`، `gpt-5-nano`) متاحة عمومًا** (يتقاعد في 2027-02-06). تم تحديث:
  - `.env.copy`، `00-course-setup/03-providers.md` (أوامر النشر الموصى بها و `az cognitiveservices`
    أوامر النشر)، وملفات README للدرسين 04، 06، 07، و 15.
  - عينات بايثون في الدرس 06 (`oai-app.py`، `oai-app-recipe.py`، `oai-history-bot.py`،
    `oai-study-buddy.py`، `githubmodels-app.py`) وبرامج الدرس 08.
  - عينات TypeScript / JavaScript في دروس 06، 07، و 11، ودفاتر ملاحظات `.dib` .NET
    للدروس 06 و07.
  - دفاتر الملاحظات الخاصة بالواجبات في دروس 04، 06، 07، و 11 (خلايا الكود)، بالإضافة إلى أمثلة `shared/python/api_utils.py`
    للسلاسل الوثائقية.
- **توجيهات معلمات نموذج الاستدلال (جديد).** `gpt-5-mini` هو نموذج *استدلال*: لا يدعم
  `temperature`/`top_p`، ويستخدم `max_completion_tokens` (اكتمالات الدردشة) /
  `max_output_tokens` (واجهة API للردود) بدلًا من `max_tokens`. وبناءً عليه:
  - أُزيل `temperature`/`top_p`/`max_tokens` من العينات التي أصبحت تستخدم `gpt-5-mini` افتراضيًا
    (`githubmodels-app.py`، `aoai-app-recipe.py`، `oai-app-recipe.py`، README درس 15 RAG).
  - أضيفت ملاحظة **"نماذج الاستدلال لا تستخدم `temperature`"** للدرس 06، توضح أن
    نماذج الاستدلال تتم توجيهها بـ **هندسة الموجهات + ضوابط الاستدلال** بدلاً من
    أزرار العينة، بينما `temperature`/`top_p` لا تزال صالحة على النماذج غير الاستدلالية
    (GPT-4.x، Mistral، Llama، Phi، النماذج المفتوحة).
- **`gpt-5-mini` غير مستخدم في درس تحضير التخصيص الدقيق (درس 18).** تدعم GPT-5 فقط
  التخصيص الدقيق التعزيزي (RFT)؛ ويركز درس 18 على التخصيص الدقيق الموجه (SFT) باستخدام `gpt-4.1-mini`،
  الذي يدعم SFT/DPO.
- **لعروض درجة الحرارة يتم استخدام نموذج Llama.** للحفاظ على تعليم `temperature` (الذي ترفضه نماذج الاستدلال)،
  يُستخدم نموذج `Llama-3.3-70B-Instruct` عبر نقطة نهاية نماذج Foundry. أُضيف متغير `AZURE_INFERENCE_CHAT_MODEL` جديد إلى `.env.copy`؛
  دفاتر الملاحظات `githubmodels` للدرس 04/06 و
  يقرأ عينة `06` `js-githubmodels` (الرجوع إلى `Llama-3.3-70B-Instruct`) ويحافظ على
  عروض `temperature`/`top_p`/`max_tokens` التجريبية الخاصة بهم.
- **تم تحديث عينات JS / .NET لـ GPT-5.** تمت إزالة `temperature`/`top_p`/`max_tokens` من عينات GPT-5
  (`06` `recipe-app` TypeScript، `06` `.dib` .NET - والتي ترفع أيضًا `MaxOutputTokenCount`
  حتى لا يتم اقتطاع مخرجات التفكير). تستخدم عينة `06` `js-githubmodels` الآن Llama للحفاظ على
  عرض درجة الحرارة الخاصة بها. تشير ملاحظات `.dib` إلى أن `Azure.AI.Inference` + نموذج Llama هو الطريق إلى
  عرض `Temperature` في .NET.
- تُركت `gpt-4o-mini` / `gpt-5-mini` في أماكنها حيث تظل دقيقة: مراجع ترميز الرموز `tiktoken`،
  قوائم توفر كتالوج النماذج، ونماذج الكلام في الدرس 02 (`gpt-4o-transcribe`).
- تحافظ عينات الدرس 20 (Mistral) و21 (Meta) على `temperature`/`max_tokens` لأنها تستهدف
  نماذج Mistral/Llama، التي تدعم تلك المعلمات.

## [2026-07-06] — تحديث تحديث المحتوى

تحديث شامل للحفاظ على دقة المناهج لعام 2026: واجهات برمجة تطبيقات حديثة، أسماء المنتجات
الحالية وأسماء النماذج، إرشادات مزود محدثة، وأدوات جديدة لتجربة المطور.

### تمت الإضافة

- قسم **إطار عمل وكيل مايكروسوفت** في الدرس `17-ai-agents` يغطي وكلاء الدردشة الفرديين،
  وأدوات / استدعاء الوظائف، وتكوين Azure OpenAI (Microsoft Foundry)، وتنسيق سير عمل الوكلاء المتعددين
  (`SequentialBuilder` / `ConcurrentBuilder`).
- تم توثيق **Foundry Local** كمزود غير متصل / على الجهاز (إلى جانب Ollama) في
  `00-course-setup/03-providers.md` والدرس `19-slm`.
- **سير عمل التكامل المستمر**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (مطبقة على وحدة `shared/` المُحافظة عليها،
    نصيحة على باقي المنهج)، فحص ESLint استشاري، ووظيفة pytest.
  - `.github/workflows/security.yml` — تحليل CodeQL (بايثون + جافا سكريبت/تايب سكريبت) و
    مراجعة التبعيات على طلبات السحب.
- **مجموعة الاختبار** تحت `tests/` — 41 اختبار pytest تغطي وحدة الأدوات المشتركة.
- **Azure OpenAI → مهارة ترحيل API الردود** تحت
  `.github/skills/azure-openai-to-responses/` المستخدم لتوجيه ترحيل API.

### تم التغيير

- **Chat Completions API → Responses API** عبر جميع عينات الدردشة في بايثون وتايب سكريبت
  (`client.responses.create(...)` → `response.output_text`)، بما في ذلك الدروس 04، 06، 07، 11،
  15، و18، بالإضافة إلى ملفات README الخاصة بها.
- **نماذج GitHub → نماذج Microsoft Foundry** في جميع النصوص والروابط والعينات. نماذج GitHub
  سيتم إيقافها في نهاية يوليو 2026؛ العينات الآن تشير إلى كتالوج نماذج Microsoft Foundry وتستخدم
  متغيرات البيئة `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **تم تحديث وثائق `.env.copy`، `AGENTS.md`، والمزود** لتعكس أن Azure OpenAI أصبحت الآن جزءًا
  من Microsoft Foundry، وتم رفع إصدار API الافتراضي إلى `2024-10-21`.
- **عينات TypeScript** (الدروس 06، 07، 08، 11) تم ترحيلها من SDK بيتا `@azure/openai` المهجور
  إلى حزمة `openai` (تستخدم تطبيقات الدردشة API الردود؛ تطبيق البحث يستخدم
  عميل التعابير).
- **دفاتر .NET** (`dotnet/*.dib`) تم توحيدها على `Azure.AI.OpenAI` **2.1.0**: الدروس 06 و07
  تستخدم API `ChatClient`، الدرس 08 يستخدم `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`)، و
  الدرس 09 يستخدم `ImageClient` (`GenerateImage`) مع `gpt-image-1`، مما يستبدل
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` القديمة من `1.0.0-beta.9`.
- **تحديث اسم المنتج**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (الدروس 14، 16، 17) و "Bing" → **Microsoft Copilot** (الدرس 12)، حيث تشير إلى
  المنتجات الحالية.
- **DevContainer** (`.devcontainer/`) الآن يشحن إضافات Pylance وBlack وRuff وESLint وPrettier وCopilot،
  ويفعل التنسيق عند الحفظ، ويثبت `ruff`، `black`، `mypy`، و`pytest` حتى يمكن
  إعادة تنفيذ فحوصات CI محليًا.
- **توليد الصور** (الدرس 09) يوصي بـ `gpt-image-1` لأزور (كتالوج أزور ألغى
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** تم تحديثه ليعكس العمل المكتمل (هجرة واجهة برمجة التطبيقات، CI،  
  DevContainer، الاختبارات) والحقائق الحالية (يتم إنتاج الترجمات تلقائيًا بواسطة  
  مترجم Azure Co-op؛ تم استبدال واجهة برمجة تطبيقات Assistants بواسطة واجهة برمجة تطبيقات Responses).  

### تم الإصلاح  

- **`shared/python/input_validation.py`** — الآن يُرجع `validate_text_input(allow_empty=True)`  
  سلسلة فارغة لإدخال يحتوي فقط على مسافات بدلاً من رفع خطأ "قصير جدًا" (متوافق مع حالة  
  `None`). تم العثور عليها وتغطيتها بواسطة مجموعة الاختبار الجديدة.  
- **عينات صور الدرس 09** — تم تصحيح أخطاء حقيقية: `InvalidRequestError` → `BadRequestError`،  
  `images.create` → `images.generate`، `Image.create_variation` → `client.images.create_variation`،  
  ومتغير ظلل وحدة `openai`.  
- **دفتر ملاحظات الدرس 15 RAG** — تم إصلاح إعداد العميل، واستبدال `DataFrame.append` المحذوفة  
  بـ `pd.concat`، وتحديث استخدام SDK القديم.  
- تم استبدال أسماء النماذج المتقادمة / المتوقفة (`gpt-3.5-turbo`، `gpt-35-turbo`) بـ `gpt-4o-mini`  
  في العينات النشطة؛ تم الحفاظ على مخرجات الضبط الدقيق التاريخية في الدرس 18 مع توضيحها  
  بدلاً من إعادة كتابتها.  

### تم التوقف / ملاحظات  

- **عينات نماذج Microsoft Foundry** التي تستخدم SDK `azure-ai-inference` / `@azure-rest/ai-inference`  
  (`client.complete()`) — عينات `githubmodels-*` و `js-githubmodels` والدروس 19، 20،  
  و21 — تبقى على واجهة برمجة تطبيقات استنتاج النموذج، التي **لا** تدعم واجهة برمجة تطبيقات Responses. تم  
  تركها عمدًا على ذلك SDK.  
- تم الاحتفاظ بـ `AzureOpenAI()` عمدًا حيثما كان مناسبًا (التضمينات وتوليد الصور)،  
  حيث إن تلك سير العمل ليست جزءًا من هجرة واجهة برمجة تطبيقات Responses.  
- يتم الحفاظ على مراجع `text-embedding-ada-002` حيث يعتمد عليها مؤشر تضمين محسوب مسبقًا.  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->