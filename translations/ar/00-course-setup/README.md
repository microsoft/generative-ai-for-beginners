# البدء مع هذا المقرر

نحن متحمسون جدًا لأن تبدأ هذا المقرر وترى ما الذي ستستلهمه للبناء باستخدام الذكاء الاصطناعي التوليدي!

لضمان نجاحك، توضح هذه الصفحة خطوات الإعداد والمتطلبات التقنية، وأين يمكنك الحصول على المساعدة إذا احتجت.

## خطوات الإعداد

لبدء هذا المقرر، ستحتاج إلى إكمال الخطوات التالية.

### 1. استنساخ هذا المستودع

[انسخ هذا المستودع بالكامل](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) إلى حسابك الخاص على GitHub لتستطيع تعديل أي كود وإكمال التحديات. يمكنك أيضًا [تمييز هذا المستودع بنجمة (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) لتسهيل العثور عليه وعلى المستودعات ذات الصلة.

### 2. إنشاء مساحة أكواد

لتجنب أي مشاكل في التبعيات عند تشغيل الكود، نوصي بتشغيل هذا المقرر في [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

في استنساخك: **Code -> Codespaces -> New on main**

![إظهار مربع حوار به أزرار لإنشاء مساحة أكواد](../../../translated_images/ar/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 إضافة سر

1. ⚙️ رمز الترس -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. سمِّه OPENAI_API_KEY، والصق مفتاحك، ثم احفظ.

### 3. وما الخطوة التالية؟

| أريد أن…           | اذهب إلى…                                                               |
|--------------------|-------------------------------------------------------------------------|
| بدء الدرس 1         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| العمل بدون اتصال   | [`setup-local.md`](02-setup-local.md)                                   |
| إعداد مزود LLM     | [`providers.md`](03-providers.md)                                        |
| لقاء متعلمين آخرين | [انضم إلى ديسكورد الخاص بنا](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## استكشاف الأخطاء وإصلاحها


| العَرَض                                  | الحل                                                               |
|-----------------------------------------|-------------------------------------------------------------------|
| بناء الحاوية متوقف لأكثر من 10 دقائق   | **Codespaces ➜ “Rebuild Container”**                              |
| `python: command not found`              | لم يكن الطرف متصلًا؛ اضغط **+** ➜ *bash*                          |
| `401 Unauthorized` من OpenAI             | مفتاح `OPENAI_API_KEY` خاطئ أو منتهي الصلاحية                      |
| VS Code يظهر “Dev container mounting…” | حدث تحديث لعلامة التبويب في المتصفح—أحيانًا تفقد Codespaces الاتصال |
| تفقد نواة دفتر الملاحظات                | قائمة الدفتر ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   أنظمة يونكس:

   ```bash
   touch .env
   ```

   ويندوز:

   ```cmd
   echo . > .env
   ```

3. **تحرير ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثلاً VS Code، Notepad++، أو أي محرر آخر). أضف السطر التالي للملف، مع استبدال `your_github_token_here` برمز GitHub الخاص بك:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **احفظ الملف**: احفظ التغييرات وأغلق محرر النصوص.

5. **تثبيت `python-dotenv`**: إذا لم تكن قد ثبّتَها من قبل، ستحتاج إلى تثبيت حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق Python الخاص بك. يمكنك تثبيتها باستخدام `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **تحميل متغيرات البيئة في سكريبت Python**: استخدم في سكريبت Python الخاص بك حزمة `python-dotenv` لتحميل المتغيرات من ملف `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # تحميل متغيرات البيئة من ملف .env
   load_dotenv()

   # الوصول إلى متغير GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

هذا كل شيء! لقد أنشأت بنجاح ملف `.env`، وأضفت مفتاح GitHub الخاص بك، وحمّلته في تطبيق Python الخاص بك.

## كيفية التشغيل محلياً على جهازك

لتشغيل الكود محليًا على جهازك، ستحتاج إلى وجود نسخة من [Python مثبتة](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

بعد ذلك، لاستخدام المستودع، تحتاج إلى نسخه:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

بمجرد حصولك على كل شيء جاهز، يمكنك البدء!

## خطوات اختيارية

### تثبيت Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst) وPython وبعض الحزم الأخرى.
Conda هو مدير حزم يسهل إعداد والتبديل بين [بيئات افتراضية](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) مختلفة من Python وحزمها. كما أنه مفيد لتثبيت الحزم غير المتوفرة عن طريق `pip`.

يمكنك متابعة [دليل تثبيت MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) لإعداده.

بعد تثبيت Miniconda، تحتاج إلى نسخ [المستودع](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (إذا لم تكن قد فعلت ذلك بعد)

بعدها تحتاج إلى إنشاء بيئة افتراضية. لفعل ذلك باستخدام Conda، قم بإنشاء ملف بيئة جديد (_environment.yml_). إذا كنت تستخدم Codespaces، أنشئ هذا داخل دليل `.devcontainer`، أي `.devcontainer/environment.yml`.

قم بملء ملف البيئة بالمقتطف أدناه:

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

يحدد ملف البيئة التبعيات التي نحتاجها. يشير `<environment-name>` إلى اسم البيئة التي تود استخدامها مع Conda، و`<python-version>` إلى نسخة Python التي تريد استخدامها، على سبيل المثال، `3` هي النسخة الكبيرة الأحدث من Python.

بعد ذلك، يمكنك إنشاء بيئة Conda الخاصة بك بتنفيذ الأوامر التالية في سطر الأوامر/الطرفية

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # مسار .devcontainer الفرعي ينطبق فقط على إعدادات Codespace
conda activate ai4beg
```

راجع [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

### استخدام Visual Studio Code مع امتداد دعم Python

نوصي باستخدام محرر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) مع [امتداد دعم Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) لهذا المقرر. هذا مجرد توصية وليس مطلبًا ضروريًا.

> **ملاحظة**: بفتح مستودع المقرر في VS Code، لديك خيار إعداد المشروع داخل حاوية. هذا بفضل دليل [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) الخاص داخل مستودع المقرر. سنشرح المزيد لاحقًا.

> **ملاحظة**: عند نسخ وفتح الدليل في VS Code، سيقترح تلقائيًا تثبيت امتداد دعم Python.

> **ملاحظة**: إذا اقترح VS Code إعادة فتح المستودع داخل حاوية، ارفض ذلك لاستخدام نسخة Python المثبتة محليًا.

### استخدام Jupyter في المتصفح

يمكنك أيضًا العمل على المشروع باستخدام بيئة [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مباشرةً ضمن المتصفح. توفر كل من Jupyter الكلاسيكي و[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) بيئة تطوير ممتعة مع ميزات مثل الإكمال التلقائي وتظليل الكود، وغيرها.

لتشغيل Jupyter محليًا، افتح الطرفية/سطر الأوامر، وانتقل إلى دليل المقرر، ونفذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

سيبدأ هذا نسخة Jupyter وسيُعرض عنوان URL للدخول إليه في نافذة سطر الأوامر.

بمجرد الوصول إلى عنوان URL، سترى مخطط المقرر ويمكنك التنقل إلى أي ملف `*.ipynb`. على سبيل المثال، `08-building-search-applications/python/oai-solution.ipynb`.

### التشغيل داخل حاوية

بديل لإعداد كل شيء على جهازك أو في مساحة أكواد هو استخدام [حاوية](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst). يتيح دليل `.devcontainer` الخاص بالمستودع إمكانية VS Code لإعداد المشروع داخل حاوية. خارج مساحات الأكواد، سيتطلب ذلك تثبيت Docker، وبصراحة، الأمر معقد قليلاً، لذا نوصي بذلك فقط لمن لديهم خبرة في العمل مع الحاويات.

واحدة من أفضل الطرق لحماية مفاتيح API الخاصة بك عند استخدام GitHub Codespaces هي باستخدام أسرار مساحات الأكواد. يرجى متابعة دليل [إدارة أسرار Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) لمعرفة المزيد حول هذا.

## الدروس والمتطلبات التقنية

المقرر يحتوي على 6 دروس مفاهيم و6 دروس ترميز.

لدروس الترميز، نستخدم خدمة Azure OpenAI. ستحتاج إلى الوصول إلى خدمة Azure OpenAI ومفتاح API لتشغيل هذا الكود. يمكنك التقديم للحصول على الوصول عبر [إتمام هذا الطلب](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

أثناء انتظار معالجة طلبك، يتضمن كل درس ترميز أيضًا ملف `README.md` حيث يمكنك عرض الكود والمخرجات.

## استخدام خدمة Azure OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تعمل فيها مع خدمة Azure OpenAI، يرجى اتباع هذا الدليل حول كيفية [إنشاء ونشر مورد خدمة Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## استخدام OpenAI API لأول مرة

إذا كانت هذه هي المرة الأولى التي تستخدم فيها OpenAI API، يرجى اتباع الدليل حول كيفية [إنشاء واستخدام الواجهة.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## لقاء المتعلمين الآخرين

أنشأنا قنوات في خادم [مجتمع الذكاء الاصطناعي الرسمي على ديسكورد](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) للقاء المتعلمين الآخرين. هذه طريقة رائعة للتشبيك مع رواد أعمال، منشئين، طلاب، وأي شخص يسعى للتطور في الذكاء الاصطناعي التوليدي.

[![انضم إلى قناة ديسكورد](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

فريق المشروع سيكون حاضرًا أيضًا على هذا الخادم لمساعدة أي متعلم.

## المساهمة

هذا المقرر هو مبادرة مفتوحة المصدر. إذا لاحظت مجالات للتحسين أو مشكلات، يرجى إنشاء [سحب طلب](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) أو تسجيل [مشكلة في GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

سيتعقب فريق المشروع كل المساهمات. المساهمة في مفتوح المصدر هي طريقة رائعة لبناء مسيرتك في الذكاء الاصطناعي التوليدي.

تتطلب معظم المساهمات موافقتك على اتفاقية ترخيص المساهم (CLA) التي تفيد بأن لديك الحق وأنك تمنحنا فعليًا الحقوق لاستخدام مساهمتك. للتفاصيل، قم بزيارة [موقع اتفاقية ترخيص المساهم (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

مهم: عند ترجمة النصوص في هذا المستودع، يرجى التأكد من عدم استخدام الترجمة الآلية. سنقوم بالتحقق من الترجمات عن طريق المجتمع، فالرجاء التطوع فقط لترجمات اللغات التي تجيدها.

عند تقديم طلب سحب، سيحدد CLA-bot تلقائيًا ما إذا كنت بحاجة إلى تقديم اتفاقية CLA ويزين طلب السحب بالملصق المناسب (مثلاً، تسمية، تعليق). فقط اتبع التعليمات التي يقدمها الروبوت. ستحتاج للقيام بذلك مرة واحدة فقط عبر كل المستودعات التي تستخدم اتفاقية CLA الخاصة بنا.

هذا المشروع اعتمد [مدونة السلوك المفتوحة لمايكروسوفت](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). للمزيد من المعلومات اقرأ أسئلة وأجوبة مدونة السلوك أو اتصل بـ [البريد الإلكتروني opencode](opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## هيا نبدأ!
الآن بعد أن أكملت الخطوات اللازمة لإتمام هذه الدورة، لنبدأ بالحصول على [مقدمة في الذكاء الاصطناعي التوليدي ونماذج اللغات الكبيرة](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحساسة، يُنصح بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->