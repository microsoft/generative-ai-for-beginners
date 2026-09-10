# البدء في هذه الدورة

نحن متحمسون جدًا لبدء هذه الدورة ورؤية ما ستستلهم لبنائه باستخدام الذكاء الاصطناعي التوليدي!

لضمان نجاحك، توضح هذه الصفحة خطوات الإعداد والمتطلبات التقنية وأين يمكنك الحصول على المساعدة إذا لزم الأمر.

## خطوات الإعداد

لبدء أخذ هذه الدورة، ستحتاج إلى إكمال الخطوات التالية.

### 1. تفرع هذا المستودع

[انشئ تفرعًا لهذا المستودع بأكمله](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) إلى حسابك على GitHub لتتمكن من تغيير أي كود وإكمال التحديات. يمكنك أيضًا [تمييز (⭐) هذا المستودع](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) لتجده بسهولة مع المستودعات ذات الصلة.

### 2. إنشاء مساحة أكواد (codespace)

لتجنب أي مشاكل اعتماد عند تشغيل الكود، نوصي بتشغيل هذه الدورة في [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

في التفرع الخاص بك: **Code -> Codespaces -> جديد على main**

![Dialog showing buttons to create a codespace](../../../translated_images/ar/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 إضافة سر

1. ⚙️ أيقونة الترس -> لوحة الأوامر -> Codespaces: إدارة سر المستخدم -> أضف سرًا جديدًا.
2. اسم OPENAI_API_KEY، الصق مفتاحك، ثم احفظ.

### 3. ما التالي؟

| أريد أن…          | اذهب إلى…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| بدء الدرس 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| العمل دون اتصال بالإنترنت        | [`setup-local.md`](02-setup-local.md)                                   |
| إعداد موفر نموذج كبير | [`providers.md`](03-providers.md)                                        |
| لقاء متعلمين آخرين | [انضم إلى Discord الخاص بنا](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## استكشاف المشاكل وإصلاحها


| العرض                                    | الإصلاح                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| توقف بناء الحاوية لأكثر من 10 دقائق            | **Codespaces ➜ “إعادة بناء الحاوية”**                            |
| `python: command not found`               | الطرفية لم تُربط؛ انقر **+** ➜ *bash*                    |
| `401 Unauthorized` من OpenAI            | مفتاح `OPENAI_API_KEY` خاطئ أو منتهي الصلاحية                                |
| VS Code يعرض “Dev container mounting…”   | حدث تحديث صفحة المتصفح—أحيانًا تفقد Codespaces الاتصال   |
| فقدان نواة المفكرة                   | قائمة المفكرة ➜ **Kernel ▸ اختيار النواة ▸ Python 3**           |

   أنظمة تشغيل يونكس:

   ```bash
   touch .env
   ```

   ويندوز:

   ```cmd
   echo . > .env
   ```

3. **تحرير ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثل VS Code، Notepad++ أو أي محرر آخر). أضف السطور التالية إلى الملف، مع استبدال القيم النائبة بنقطة النهاية والمفتاح الفعليين من نماذج Microsoft Foundry (انظر [`providers.md`](03-providers.md) لمعرفة كيفية الحصول عليها):

   > **ملاحظة:** نماذج GitHub (ومتغير `GITHUB_TOKEN` الخاص بها) ستتوقف عن الاستخدام في نهاية يوليو 2026. يُرجى استخدام [نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) بدلاً منها.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **حفظ الملف**: احفظ التغييرات وأغلق محرر النصوص.

5. **تثبيت `python-dotenv`**: إذا لم تكن قد فعلت ذلك بعد، ستحتاج إلى تثبيت حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق Python الخاص بك. يمكنك تثبيتها باستخدام `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **تحميل متغيرات البيئة في برنامج Python الخاص بك**: في برنامج Python، استخدم حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # تحميل متغيرات البيئة من ملف .env
   load_dotenv()

   # الوصول إلى متغيرات نماذج Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

هذا كل شيء! لقد أنشأت بنجاح ملف `.env`، وأضفت بيانات اعتماد Microsoft Foundry Models، وقمت بتحميلها في تطبيق Python الخاص بك.

## كيفية التشغيل محليًا على جهاز الكمبيوتر الخاص بك

لتشغيل الكود محليًا على جهازك، تحتاج إلى تثبيت إصدار من [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

لاستخدام المستودع، تحتاج إلى نسخه (استنساخه):

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

بمجرد أن تتحقق من كل شيء، يمكنك البدء!

## خطوات اختيارية

### تثبيت Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، وPython، وبعض الحزم الإضافية.
Conda هو مدير حزم يسهل عليك إعداد والتبديل بين بيئات Python [الافتراضية](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) والحزم. كما أنه مفيد لتثبيت الحزم غير المتوفرة عبر `pip`.

يمكنك اتباع [دليل تثبيت MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) لإعداده.

بعد تثبيت Miniconda، تحتاج إلى نسخ [المستودع](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (إذا لم تكن قد فعلت ذلك بالفعل)

بعد ذلك، تحتاج إلى إنشاء بيئة افتراضية. للقيام بذلك باستخدام Conda، قم بإنشاء ملف بيئة جديد (environment.yml). إذا كنت تستخدم Codespaces، أنشئ الملف داخل دليل `.devcontainer`، أي `.devcontainer/environment.yml`.

ابدأ بملء ملف البيئة بالمقتطف أدناه:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

إذا واجهت أخطاء عند استخدام conda، يمكنك تثبيت مكتبات Microsoft AI يدويًا باستخدام الأمر التالي في الطرفية.

```
conda install -c microsoft azure-ai-ml
```

يحدد ملف البيئة الاعتمادات التي نحتاجها. `<environment-name>` يشير للاسم الذي ترغب باستخدامه لبيئة Conda الخاص بك، و`<python-version>` هو إصدار Python الذي تريد استخدامه، على سبيل المثال، `3` هو أحدث إصدار رئيسي من Python.

بعد ذلك، يمكنك متابعة إنشاء بيئة Conda بتنفيذ الأوامر التالية في سطر الأوامر/الطرفية

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # ينطبق مسار .devcontainer الفرعي فقط على إعدادات Codespace
conda activate ai4beg
```

راجع [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

### استخدام Visual Studio Code مع امتداد دعم Python

نوصي باستخدام محرر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) مع مثبت امتداد [دعم Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) لهذه الدورة. هذا مجرد توصية وليس شرطًا حتميًا.

> **ملاحظة**: بفتح مستودع الدورة في VS Code، لديك خيار إعداد المشروع ضمن حاوية. هذا بسبب وجود دليل [خاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) داخل مستودع الدورة. المزيد عن هذا لاحقًا.

> **ملاحظة**: بمجرد نسخ المستودع وفتحه في VS Code، سيقترح تلقائيًا تثبيت امتداد دعم Python.

> **ملاحظة**: إذا اقترح VS Code إعادة فتح المستودع داخل حاوية، رفض هذا الطلب لاستخدام نسخة Python المثبتة محليًا.

### استخدام Jupyter في المتصفح

يمكنك أيضًا العمل على المشروع باستخدام بيئة [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مباشرة من المتصفح. توفر كل من Jupyter الكلاسيكي و[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) بيئة تطوير ممتعة مع ميزات مثل الإكمال التلقائي، تمييز الكود، وغيرها.

لتشغيل Jupyter محليًا، توجه إلى الطرفية/سطر الأوامر، انتقل إلى دليل الدورة، ونفذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

هذا سيشغل مثيل Jupyter وسيتم عرض عنوان URL للوصول إليه ضمن نافذة سطر الأوامر.

بمجرد الوصول إلى العنوان، ستشاهد مسار الدورة ويمكنك التنقل إلى أي ملف `*.ipynb`، مثل `08-building-search-applications/python/oai-solution.ipynb`.

### التشغيل داخل حاوية

بديل لإعداد كل شيء على جهاز الكمبيوتر الخاص بك أو في Codespace هو استخدام [الحاويات](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). يسمح دليل `.devcontainer` الخاص في مستودع الدورة لـ VS Code بإعداد المشروع ضمن حاوية. خارج Codespaces، هذا يتطلب تثبيت Docker، وبصراحة، يتطلب بعض العمل، لذا نوصي به فقط لمن لديهم خبرة في العمل مع الحاويات.

إحدى أفضل الطرق للحفاظ على أمان مفاتيح API عند استخدام GitHub Codespaces هي باستخدام أسرار Codespace. يرجى متابعة دليل [إدارة أسرار Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) لمعرفة المزيد عن هذا.


## الدروس والمتطلبات التقنية

تحتوي الدورة على دروس "تعلم" تشرح مفاهيم الذكاء الاصطناعي التوليدي ودروس "بناء" مع أمثلة عملية بالكود باستخدام **Python** و**TypeScript** حيث أمكن.

للدروس البرمجية، نستخدم Azure OpenAI في Microsoft Foundry. ستحتاج إلى اشتراك Azure ومفتاح API. الوصول مفتوح - لا يتطلب تقديم طلب - لذا يمكنك [إنشاء مورد Microsoft Foundry ونشر نموذج](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) للحصول على نقطة النهاية والمفتاح.

كل درس برمجي يتضمن أيضًا ملف `README.md` حيث يمكنك عرض الكود والنتائج دون تشغيل أي شيء.

## استخدام خدمة Azure OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تعمل فيها مع خدمة Azure OpenAI، يرجى اتباع هذا الدليل حول كيفية [إنشاء ونشر مورد خدمة Azure OpenAI.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## استخدام واجهة برمجة تطبيقات OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تعمل فيها مع واجهة برمجة تطبيقات OpenAI، يرجى اتباع الدليل حول كيفية [إنشاء واستخدام الواجهة.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## لقاء متعلمين آخرين

أنشأنا قنوات في خادمنا الرسمي [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) للقاء متعلمين آخرين. هذه طريقة رائعة للتواصل مع رواد أعمال وبناة وطلاب يشاركونك الاهتمام ويريدون التقدم في مجال الذكاء الاصطناعي التوليدي.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

سيكون فريق المشروع أيضًا على هذا الخادم لمساعدة أي متعلمين.

## المساهمة

هذه الدورة هي مبادرة مفتوحة المصدر. إذا لاحظت مجالات للتحسين أو مشاكل، يرجى إنشاء [طلب سحب](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) أو تسجيل [مشكلة في GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

سيتابع فريق المشروع كل المساهمات. المساهمة في المصادر المفتوحة طريقة رائعة لبناء مسيرتك في الذكاء الاصطناعي التوليدي.

معظم المساهمات تتطلب موافقتك على اتفاقية ترخيص المساهم (CLA) التي تصرح فيها بأن لديك الحق وأنك تمنحنا حقوق استخدام مساهمتك. للتفاصيل، زر [موقع اتفاقية ترخيص المساهم (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

هام: عند ترجمة النص في هذا المستودع، يرجى التأكد من عدم استخدام الترجمة الآلية. سنقوم بالتحقق من الترجمات عبر المجتمع، لذا يرجى التطوع فقط لترجمات اللغات التي تجيدها.


عند تقديم طلب سحب، سيقوم روبوت CLA تلقائيًا بتحديد ما إذا كنت بحاجة إلى تقديم اتفاقية CLA وتزيين طلب السحب بشكل مناسب (مثل التسمية أو التعليق). ما عليك سوى اتباع التعليمات التي يقدمها الروبوت. ستحتاج إلى القيام بذلك مرة واحدة فقط عبر جميع المستودعات التي تستخدم CLA الخاص بنا.

لقد تبنى هذا المشروع [مدونة قواعد السلوك مفتوحة المصدر من مايكروسوفت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). لمزيد من المعلومات، اقرأ الأسئلة الشائعة حول مدونة قواعد السلوك أو تواصل مع [البريد الإلكتروني opencode](opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## لنبدأ

بعد أن أكملت الخطوات اللازمة لإتمام هذه الدورة، دعنا نبدأ بالحصول على [مقدمة في الذكاء الاصطناعي التوليدي ونماذج اللغة الكبيرة](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->