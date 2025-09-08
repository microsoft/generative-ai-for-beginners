<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T14:00:32+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ar"
}
-->
# البدء في هذه الدورة

نحن متحمسون جدًا لانضمامك إلى هذه الدورة وننتظر لنرى كيف ستلهمك لبناء مشاريع باستخدام الذكاء الاصطناعي التوليدي!

لضمان نجاحك، توضح هذه الصفحة خطوات الإعداد والمتطلبات التقنية وأماكن الحصول على المساعدة إذا احتجت إليها.

## خطوات الإعداد

لبدء هذه الدورة، عليك إكمال الخطوات التالية.

### 1. عمل Fork لهذا المستودع

[قم بعمل Fork لهذا المستودع بالكامل](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) إلى حسابك الخاص على GitHub حتى تتمكن من تعديل الكود وإكمال التحديات. يمكنك أيضًا [وضع نجمة (🌟) على هذا المستودع](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) لتسهيل العثور عليه وعلى المستودعات ذات الصلة.

### 2. إنشاء مساحة أكواد (Codespace)

لتجنب مشاكل الاعتمادية عند تشغيل الكود، ننصحك بتشغيل هذه الدورة في [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

في المستودع الخاص بك: **Code -> Codespaces -> New on main**

![مربع حوار يظهر أزرار لإنشاء مساحة أكواد](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 إضافة سر

1. ⚙️ أيقونة الترس -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. الاسم OPENAI_API_KEY، الصق مفتاحك، ثم احفظ.

### 3. ماذا بعد؟

| أريد أن...          | انتقل إلى…                                                                  |
|---------------------|----------------------------------------------------------------------------|
| بدء الدرس الأول      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| العمل بدون اتصال    | [`setup-local.md`](02-setup-local.md)                                      |
| إعداد مزود LLM      | [`providers.md`](providers.md)                                              |
| لقاء متعلمين آخرين  | [انضم إلى Discord الخاص بنا](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## استكشاف الأخطاء وإصلاحها

| العرض                                   | الحل                                                             |
|------------------------------------------|------------------------------------------------------------------|
| بناء الحاوية متوقف > 10 دقائق            | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`              | الطرفية لم تتصل؛ اضغط **+** ➜ *bash*                             |
| `401 Unauthorized` من OpenAI             | مفتاح `OPENAI_API_KEY` خاطئ أو منتهي الصلاحية                    |
| VS Code يظهر “Dev container mounting…”   | قم بتحديث علامة تبويب المتصفح—أحيانًا تفقد Codespaces الاتصال     |
| نواة الدفتر مفقودة                       | قائمة الدفتر ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   أنظمة يونكس:

   ```bash
   touch .env
   ```

   ويندوز:

   ```cmd
   echo . > .env
   ```

3. **تعديل ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثل VS Code أو Notepad++ أو أي محرر آخر). أضف السطر التالي إلى الملف، مع استبدال `your_github_token_here` برمز GitHub الخاص بك:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **حفظ الملف**: احفظ التغييرات وأغلق محرر النصوص.

5. **تثبيت `python-dotenv`**: إذا لم تكن قد فعلت ذلك بالفعل، ستحتاج لتثبيت حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق بايثون الخاص بك. يمكنك تثبيتها باستخدام `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **تحميل متغيرات البيئة في سكريبت بايثون الخاص بك**: في سكريبت بايثون، استخدم حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

هذا كل شيء! لقد أنشأت ملف `.env` بنجاح، وأضفت رمز GitHub الخاص بك، وقمت بتحميله في تطبيق بايثون الخاص بك.

## كيفية التشغيل محليًا على جهازك

لتشغيل الكود محليًا على جهازك، ستحتاج إلى تثبيت إصدار من [بايثون](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

لاستخدام المستودع، عليك استنساخه:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

بعد أن تقوم باستنساخ كل شيء، يمكنك البدء!

## خطوات اختيارية

### تثبيت Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، بايثون، وبعض الحزم.
Conda هو مدير حزم يسهل إعداد والتبديل بين [**البيئات الافتراضية**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) المختلفة وحزم بايثون. كما أنه مفيد لتثبيت الحزم غير المتوفرة عبر `pip`.

يمكنك اتباع [دليل تثبيت MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) لإعداده.

بعد تثبيت Miniconda، تحتاج لاستنساخ [المستودع](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (إذا لم تكن قد فعلت ذلك بالفعل).

بعد ذلك، تحتاج لإنشاء بيئة افتراضية. للقيام بذلك باستخدام Conda، أنشئ ملف بيئة جديد (_environment.yml_). إذا كنت تستخدم Codespaces، أنشئ هذا الملف داخل مجلد `.devcontainer`، أي `.devcontainer/environment.yml`.

قم بملء ملف البيئة بالمقطع التالي:

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

إذا واجهت أخطاء أثناء استخدام conda يمكنك تثبيت مكتبات Microsoft AI يدويًا باستخدام الأمر التالي في الطرفية.

```
conda install -c microsoft azure-ai-ml
```

ملف البيئة يحدد الاعتمادات التي نحتاجها. `<environment-name>` هو اسم البيئة التي ترغب في إنشائها، و `<python-version>` هو إصدار بايثون الذي تريده، مثلًا، `3` هو أحدث إصدار رئيسي.

بعد ذلك، يمكنك إنشاء بيئة Conda الخاصة بك بتشغيل الأوامر التالية في الطرفية:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

راجع [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

### استخدام Visual Studio Code مع إضافة دعم بايثون

ننصح باستخدام محرر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) مع إضافة [دعم بايثون](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) لهذه الدورة. هذا مجرد توصية وليس شرطًا أساسيًا.

> **Note**: عند فتح مستودع الدورة في VS Code، يمكنك إعداد المشروع داخل حاوية. هذا بسبب وجود [مجلد `.devcontainer` الخاص](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) داخل مستودع الدورة. سنتحدث عن هذا لاحقًا.

> **Note**: بعد استنساخ وفتح المجلد في VS Code، سيقترح عليك تلقائيًا تثبيت إضافة دعم بايثون.

> **Note**: إذا اقترح عليك VS Code إعادة فتح المستودع داخل حاوية، ارفض ذلك لتستخدم إصدار بايثون المثبت محليًا.

### استخدام Jupyter في المتصفح

يمكنك أيضًا العمل على المشروع باستخدام [بيئة Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مباشرة من المتصفح. كلا من Jupyter الكلاسيكي و [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) يوفران بيئة تطوير مريحة مع ميزات مثل الإكمال التلقائي وتلوين الكود وغيرها.

لتشغيل Jupyter محليًا، انتقل إلى الطرفية/سطر الأوامر، واذهب إلى مجلد الدورة، ونفذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

سيتم تشغيل Jupyter وستظهر لك عنوان URL للوصول إليه في نافذة الطرفية.

عند الوصول إلى الرابط، ستظهر لك هيكل الدورة ويمكنك التنقل إلى أي ملف `*.ipynb`. مثلًا، `08-building-search-applications/python/oai-solution.ipynb`.

### التشغيل داخل حاوية

بديل لإعداد كل شيء على جهازك أو في Codespace هو استخدام [حاوية](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). مجلد `.devcontainer` الخاص داخل مستودع الدورة يتيح لـ VS Code إعداد المشروع داخل حاوية. خارج Codespaces، سيتطلب ذلك تثبيت Docker، وقد يكون الأمر معقدًا بعض الشيء، لذا ننصح به فقط لمن لديهم خبرة في العمل مع الحاويات.

واحدة من أفضل الطرق للحفاظ على مفاتيح API الخاصة بك آمنة عند استخدام GitHub Codespaces هي استخدام أسرار Codespace. يرجى اتباع [دليل إدارة أسرار Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) لمعرفة المزيد.

## الدروس والمتطلبات التقنية

الدورة تحتوي على 6 دروس مفاهيمية و6 دروس برمجية.

بالنسبة للدروس البرمجية، نستخدم خدمة Azure OpenAI. ستحتاج إلى الوصول إلى خدمة Azure OpenAI ومفتاح API لتشغيل الكود. يمكنك التقديم للحصول على الوصول عبر [إكمال هذا النموذج](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

أثناء انتظار معالجة طلبك، كل درس برمجي يحتوي أيضًا على ملف `README.md` حيث يمكنك مشاهدة الكود والمخرجات.

## استخدام خدمة Azure OpenAI لأول مرة

إذا كانت هذه أول مرة تستخدم فيها خدمة Azure OpenAI، يرجى اتباع هذا الدليل حول كيفية [إنشاء ونشر مورد خدمة Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## استخدام واجهة OpenAI API لأول مرة

إذا كانت هذه أول مرة تستخدم فيها OpenAI API، يرجى اتباع الدليل حول كيفية [إنشاء واستخدام الواجهة.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## لقاء متعلمين آخرين

أنشأنا قنوات في [خادم Discord الرسمي لمجتمع الذكاء الاصطناعي](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) للقاء متعلمين آخرين. هذه طريقة رائعة للتواصل مع رواد أعمال وطلاب ومطورين مهتمين بالذكاء الاصطناعي التوليدي.

[![انضم إلى قناة Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

فريق المشروع سيكون أيضًا متواجدًا في هذا الخادم لمساعدة أي متعلم.

## المساهمة

هذه الدورة مبادرة مفتوحة المصدر. إذا وجدت نقاطًا للتحسين أو مشاكل، يرجى إنشاء [طلب سحب (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) أو تسجيل [مشكلة على GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

فريق المشروع سيتابع جميع المساهمات. المساهمة في المصادر المفتوحة طريقة رائعة لبناء مسيرتك في الذكاء الاصطناعي التوليدي.

معظم المساهمات تتطلب منك الموافقة على اتفاقية ترخيص المساهم (CLA) التي تؤكد أن لديك الحق في منحنا حقوق استخدام مساهمتك. للمزيد من التفاصيل، زر [موقع CLA، اتفاقية ترخيص المساهم](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

مهم: عند ترجمة النصوص في هذا المستودع، يرجى التأكد من عدم استخدام الترجمة الآلية. سنقوم بمراجعة الترجمات عبر المجتمع، لذا يرجى التطوع فقط للغات التي تتقنها.

عند إرسال طلب سحب، سيحدد روبوت CLA تلقائيًا ما إذا كنت بحاجة لتقديم CLA ويضيف العلامة المناسبة (مثل، تسمية أو تعليق). فقط اتبع التعليمات التي يقدمها الروبوت. ستحتاج للقيام بذلك مرة واحدة فقط عبر جميع المستودعات التي تستخدم CLA الخاص بنا.

هذا المشروع يتبع [مدونة قواعد السلوك لمصادر Microsoft المفتوحة](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). لمزيد من المعلومات اقرأ الأسئلة الشائعة حول مدونة قواعد السلوك أو تواصل مع [البريد الإلكتروني opencode](opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## هيا نبدأ
الآن بعد أن أنهيت الخطوات المطلوبة لإكمال هذه الدورة، دعنا نبدأ بالحصول على [مقدمة حول الذكاء الاصطناعي التوليدي ونماذج اللغة الكبيرة](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُنصح بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.