# البدء مع هذه الدورة

نحن متحمسون جدًا لبدء هذه الدورة ورؤية ما ستُلهم لبنائه باستخدام الذكاء الاصطناعي التوليدي!

لضمان نجاحك، توضح هذه الصفحة خطوات الإعداد والمتطلبات التقنية وأماكن الحصول على المساعدة إذا لزم الأمر.

## خطوات الإعداد

للبدء في أخذ هذه الدورة، ستحتاج إلى إكمال الخطوات التالية.

### 1. تفرع هذا المستودع

[قم بتفرع هذا المستودع بالكامل](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) إلى حساب GitHub الخاص بك لتتمكن من تغيير أي كود وإكمال التحديات. يمكنك أيضًا [وضع نجم (🌟) على هذا المستودع](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) لتسهيل العثور عليه وعلى المستودعات ذات الصلة.

### 2. إنشاء مساحة أكواد (Codespace)

لتجنب أي مشاكل في الاعتماديات عند تشغيل الكود، نوصي بتشغيل هذه الدورة في [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

في التفرع الخاص بك: **Code -> Codespaces -> New on main**

![صندوق حوار يُظهر أزرار لإنشاء مساحة أكواد](../../../translated_images/ar/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 إضافة سرية

1. ⚙️ أيقونة الترس -> Command Pallete -> Codespaces : إدارة السرية للمستخدم -> إضافة سر جديد.
2. اسمها OPENAI_API_KEY، الصق مفتاحك، ثم احفظ.

### 3. ما التالي؟

| أريد أن…          | اذهب إلى…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| ابدأ الدرس 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| العمل دون اتصال        | [`setup-local.md`](02-setup-local.md)                                   |
| إعداد مزود LLM | [`providers.md`](03-providers.md)                                        |
| لقاء متعلمين آخرين | [انضم إلى Discord الخاص بنا](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## حل المشاكل


| العَرَض                                   | الحل                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| توقف بناء الحاوية لأكثر من 10 دقائق            | **Codespaces ➜ “إعادة بناء الحاوية”**                            |
| `python: command not found`               | الطرفية لم تُرفق؛ انقر **+** ➜ *bash*                    |
| `401 Unauthorized` من OpenAI            | مفتاح `OPENAI_API_KEY` خاطئ أو منتهي الصلاحية                                |
| VS Code يعرض "جاري تركيب حاوية التطوير…"   | حدث تحديث لعلامة تبويب المتصفح - في بعض الأحيان تفقد Codespaces الاتصال   |
| ناقل النوتبوك مفقود                   | قائمة النوتبوك ➜ **Kernel ▸ اختيار ناقل ▸ Python 3**           |

   أنظمة يونكس:

   ```bash
   touch .env
   ```

   ويندوز:

   ```cmd
   echo . > .env
   ```

3. **تعديل ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثل VS Code أو Notepad++ أو أي محرر آخر). أضف الأسطر التالية إلى الملف، مستبدلًا عناصر العنونة بنقطة نهاية Microsoft Foundry Models ومفتاحك الفعلي (راجع [`providers.md`](03-providers.md) لمعرفة كيفية الحصول عليها):

   > **ملاحظة:** نماذج GitHub (ومتغير `GITHUB_TOKEN`) ستتوقف عن العمل بنهاية يوليو 2026. استخدم [نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) بدلاً من ذلك.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **احفظ الملف**: احفظ التغييرات وأغلق محرر النصوص.

5. **تثبيت `python-dotenv`**: إذا لم تكن قد قمت بذلك، ستحتاج إلى تثبيت حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق بايثون الخاص بك. يمكنك تثبيته باستخدام `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **تحميل متغيرات البيئة في سكريبت بايثون الخاص بك**: في سكريبت بايثون الخاص بك، استخدم حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env`:

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

هذا كل شيء! لقد أنشأت ملف `.env` بنجاح، وأضفت بيانات اعتماد Microsoft Foundry Models، وحملتها في تطبيق بايثون الخاص بك.

## كيفية التشغيل محليًا على جهاز الكمبيوتر الخاص بك

لتشغيل الكود محليًا على جهاز الكمبيوتر الخاص بك، ستحتاج إلى وجود بعض إصدارات [Python مثبتة](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

لاستخدام المستودع، تحتاج إلى نسخه (Clone):

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

بمجرد أن يكون كل شيء جاهزًا لديك، يمكنك البدء!

## خطوات اختيارية

### تثبيت Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف الوزن لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، وPython، وبعض الحزم.
Conda نفسه هو مدير حزم يسهل إعداد والتبديل بين بيئات Python [الافتراضية](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) والحزم. كما أنه مفيد لتثبيت الحزم غير المتوفرة عبر `pip`.

يمكنك اتباع [دليل تثبيت MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) لإعداده.

بعد تثبيت Miniconda، تحتاج إلى نسخ المستودع [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (إذا لم تكن قد قمت بذلك بالفعل)

بعد ذلك، تحتاج إلى إنشاء بيئة افتراضية. للقيام بذلك مع Conda، ابدأ بإنشاء ملف البيئة (_environment.yml_). إذا كنت تستخدم Codespaces، قم بإنشاء هذا داخل مجلد `.devcontainer`، هكذا `.devcontainer/environment.yml`.

قم بملء ملف البيئة بالمقتطف التالي:

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

إذا واجهت أخطاء باستخدام conda، يمكنك تثبيت مكتبات Microsoft AI يدويًا باستخدام الأمر التالي في الطرفية.

```
conda install -c microsoft azure-ai-ml
```

يحدد ملف البيئة التبعيات التي نحتاجها. يشير `<environment-name>` إلى الاسم الذي ترغب في استخدامه لبيئة Conda الخاصة بك، و `<python-version>` هو إصدار بايثون الذي تريد استخدامه، على سبيل المثال، `3` هو أحدث إصدار رئيسي من بايثون.

بعد ذلك، يمكنك إنشاء بيئة Conda بتشغيل الأوامر التالية في سطر الأوامر/الطرفية لديك

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # ينطبق مسار الفرعي .devcontainer فقط على إعدادات Codespace
conda activate ai4beg
```

ارجع إلى [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

### استخدام Visual Studio Code مع امتداد دعم Python

نوصي باستخدام محرر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) مع تثبيت [امتداد دعم Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) لهذه الدورة. هذه التوصية وليست مطلبًا نهائيًا.

> **ملاحظة**: عند فتح مستودع الدورة في VS Code، لديك خيار إعداد المشروع داخل حاوية. هذا بسبب مجلد [`.devcontainer` الخاص](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) الموجود في مستودع الدورة. المزيد عن هذا لاحقًا.

> **ملاحظة**: عند نسخ المستودع وفتحه في VS Code، سيقترح عليك تلقائيًا تثبيت امتداد دعم Python.

> **ملاحظة**: إذا اقترح VS Code إعادة فتح المستودع في حاوية، ارفض هذا الطلب لاستخدام إصدار Python المثبت محليًا.

### استخدام Jupyter في المتصفح

يمكنك أيضًا العمل على المشروع باستخدام بيئة [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مباشرة في متصفحك. توفر كل من Jupyter الكلاسيكي و [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) بيئة تطوير مريحة مع ميزات مثل الإكمال التلقائي، تمييز الكود، وغيرها.

لبدء Jupyter محليًا، توجه إلى الطرفية/سطر الأوامر، انتقل إلى دليل الدورة، ونفذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

سيبدأ هذا مثيل Jupyter وسيتم عرض عنوان URL للوصول إليه داخل نافذة سطر الأوامر.

بمجرد وصولك إلى عنوان URL، يجب أن ترى مخطط الدورة وأن تتمكن من التنقل إلى أي ملف `*.ipynb`، على سبيل المثال، `08-building-search-applications/python/oai-solution.ipynb`.

### التشغيل داخل حاوية

بديل لإعداد كل شيء على جهاز الكمبيوتر أو مساحة الأكواد الخاصة بك هو استخدام [حاوية](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). يتيح مجلد `.devcontainer` الخاص مستودع الدورة إمكانية VS Code لإعداد المشروع ضمن حاوية. خارج مساحة الأكواد، سيتطلب هذا تثبيت Docker، وبصراحة، يتطلب بعض العمل، لذا نوصي بذلك فقط لمن لديهم خبرة في العمل مع الحاويات.

إحدى أفضل الطرق لحفظ مفاتيح API الخاصة بك آمنة عند استخدام GitHub Codespaces هي استخدام الأسرار في مساحة الأكواد. يرجى اتباع دليل [إدارة الأسرار في Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) لمعرفة المزيد.


## الدروس والمتطلبات التقنية

تحتوي الدورة على 6 دروس مفاهيمية و6 دروس برمجية.

للدرورس البرمجية، نستخدم خدمة Azure OpenAI. ستحتاج إلى الوصول إلى خدمة Azure OpenAI ومفتاح API لتشغيل هذا الكود. يمكنك التقديم للحصول على الوصول من خلال [إكمال طلب هذا](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

أثناء انتظار معالجة طلبك، تتضمن كل درس برمجي أيضًا ملف `README.md` حيث يمكنك عرض الكود والمخرجات.

## استخدام خدمة Azure OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تعمل فيها مع خدمة Azure OpenAI، يرجى اتباع هذا الدليل حول كيفية [إنشاء ونشر مورد خدمة Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## استخدام API الخاص بـ OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تستخدم فيها واجهة برمجة تطبيقات OpenAI، يرجى اتباع الدليل حول كيفية [إنشاء واستخدام الواجهة.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## لقاء متعلمين آخرين

أنشأنا قنوات في خادم [مجتمع الذكاء الاصطناعي الرسمي على Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) للقاء متعلمين آخرين. هذه طريقة رائعة للتواصل مع رواد الأعمال، والبناة، والطلاب، وأي شخص يرغب في تطوير مهاراته في الذكاء الاصطناعي التوليدي.

[![انضم إلى قناة الديسكورد](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

سيكون فريق المشروع أيضًا على هذا الخادم لمساعدة أي متعلمين.

## المساهمة

هذه الدورة هي مبادرة مفتوحة المصدر. إذا رأيت مجالات للتحسين أو مشكلات، يرجى إنشاء [طلب سحب](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) أو تسجيل [مشكلة على GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

سيتابع فريق المشروع جميع المساهمات. المساهمة في المصدر المفتوح هي طريقة رائعة لبناء مسيرتك المهنية في الذكاء الاصطناعي التوليدي.

تتطلب معظم المساهمات منك الموافقة على اتفاقية ترخيص المساهم (CLA) التي تعلن أنك تملك الحق، وبالفعل تمنحنا الحقوق لاستخدام مساهمتك. للتفاصيل، قم بزيارة [موقع اتفاقية ترخيص المساهم](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

مهم: عند ترجمة النص في هذا المستودع، يرجى التأكد من عدم استخدام الترجمة الآلية. سنقوم بالتحقق من الترجمات من خلال المجتمع، لذا يرجى التطوع للترجمة فقط في اللغات التي تتقنها.

عند تقديم طلب سحب، سيقوم بوت CLA تلقائيًا بتحديد ما إذا كنت بحاجة لتوفير اتفاقية CLA وتزيين طلب السحب بشكل مناسب (مثل: علامة، تعليق). فقط اتبع التعليمات التي يقدمها البوت. ستحتاج إلى القيام بذلك مرة واحدة فقط عبر كل المستودعات التي تستخدم اتفاقيتنا.


اعتمد هذا المشروع [مدونة قواعد السلوك للمصدر المفتوح من مايكروسوفت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). للمزيد من المعلومات، اقرأ الأسئلة الشائعة حول مدونة قواعد السلوك أو تواصل عبر [البريد الإلكتروني opencode](opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## لنبدأ

الآن بعد أن أكملت الخطوات المطلوبة لإتمام هذه الدورة، لنبدأ بالحصول على [مقدمة في الذكاء الاصطناعي التوليدي والنماذج اللغوية الكبيرة](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->