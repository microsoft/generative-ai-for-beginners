<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:36:16+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ar"
}
-->
# بدء استخدام هذه الدورة

نحن متحمسون جدًا لبدء هذه الدورة ومعرفة ما الذي ستستلهمه لبنائه باستخدام الذكاء الاصطناعي التوليدي!

لضمان نجاحك، تحدد هذه الصفحة خطوات الإعداد والمتطلبات التقنية وأين يمكنك الحصول على المساعدة إذا لزم الأمر.

## خطوات الإعداد

لبدء هذه الدورة، ستحتاج إلى إكمال الخطوات التالية.

### 1. نسخ هذا المستودع

[قم بنسخ المستودع بالكامل](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) إلى حساب GitHub الخاص بك لتتمكن من تغيير أي كود وإكمال التحديات. يمكنك أيضًا [تفضيل (🌟) هذا المستودع](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) لتسهيل العثور عليه وعلى المستودعات ذات الصلة.

### 2. إنشاء مساحة عمل

لتجنب أي مشاكل في التبعيات عند تشغيل الكود، نوصي بتشغيل هذه الدورة في [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

يمكن إنشاؤها عن طريق تحديد خيار `Code` على النسخة المنسوخة من هذا المستودع واختيار خيار **Codespaces**.

![حوار يظهر الأزرار لإنشاء مساحة عمل](../../../00-course-setup/images/who-will-pay.webp)

### 3. تخزين مفاتيح API الخاصة بك

الحفاظ على مفاتيح API الخاصة بك آمنة ومأمونة أمر مهم عند بناء أي نوع من التطبيقات. نوصي بعدم تخزين أي مفاتيح API مباشرة في الكود الخاص بك. يمكن أن يؤدي التزام هذه التفاصيل في مستودع عام إلى مشاكل أمنية وحتى تكاليف غير مرغوب فيها إذا استخدمها شخص سيء.
إليك دليل خطوة بخطوة حول كيفية إنشاء ملف `.env` لـ Python وإضافة `GITHUB_TOKEN`:

1. **التنقل إلى دليل مشروعك**: افتح الطرفية أو موجه الأوامر وانتقل إلى الدليل الجذري لمشروعك حيث تريد إنشاء ملف `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **إنشاء ملف `.env`**: استخدم محرر النصوص المفضل لديك لإنشاء ملف جديد باسم `.env`. إذا كنت تستخدم سطر الأوامر، يمكنك استخدام `touch` (on Unix-based systems) or `echo` (على ويندوز):

   أنظمة Unix:
   ```bash
   touch .env
   ```

   ويندوز:
   ```cmd
   echo . > .env
   ```

3. **تعديل ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثل VS Code أو Notepad++ أو أي محرر آخر). أضف السطر التالي إلى الملف، واستبدل `your_github_token_here` برمز GitHub الفعلي الخاص بك:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **حفظ الملف**: احفظ التغييرات وأغلق محرر النصوص.

5. **تثبيت حزمة `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق Python الخاص بك. يمكنك تثبيتها باستخدام `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **تحميل متغيرات البيئة في سكريبت Python الخاص بك**: في سكريبت Python الخاص بك، استخدم حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

هذا هو! لقد نجحت في إنشاء ملف `.env`، وأضفت رمز GitHub الخاص بك، وحملته في تطبيق Python الخاص بك.

## كيفية التشغيل محليًا على جهاز الكمبيوتر الخاص بك

لتشغيل الكود محليًا على جهاز الكمبيوتر الخاص بك، ستحتاج إلى تثبيت بعض إصدارات [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

ثم لاستخدام المستودع، تحتاج إلى نسخه:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

بمجرد أن تكون كل شيء جاهزًا، يمكنك البدء!

## خطوات اختيارية

### تثبيت Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، Python، وكذلك بعض الحزم.
Conda نفسها هي مدير حزم، مما يسهل إعداد وتبديل بين بيئات Python [**الافتراضية**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) والحزم. كما أنها مفيدة لتثبيت الحزم التي لا تتوفر عبر `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

قم بملء ملف البيئة الخاص بك بالقطعة أدناه:

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

إذا وجدت أنك تواجه أخطاء باستخدام conda يمكنك تثبيت مكتبات Microsoft AI يدويًا باستخدام الأمر التالي في الطرفية.

```
conda install -c microsoft azure-ai-ml
```

ملف البيئة يحدد التبعيات التي نحتاجها. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` هو أحدث إصدار رئيسي من Python.

مع ذلك، يمكنك المضي قدمًا وإنشاء بيئة Conda الخاصة بك عن طريق تشغيل الأوامر أدناه في سطر الأوامر/الطرفية

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ارجع إلى [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

### استخدام Visual Studio Code مع امتداد دعم Python

نوصي باستخدام محرر [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) مع تثبيت امتداد [دعم Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) لهذه الدورة. ومع ذلك، هذا أكثر من توصية وليس متطلبًا محددًا.

> **ملاحظة**: من خلال فتح مستودع الدورة في VS Code، لديك الخيار لإعداد المشروع داخل حاوية. هذا بسبب [الدليل الخاص `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) الموجود داخل مستودع الدورة. المزيد عن هذا لاحقًا.

> **ملاحظة**: بمجرد نسخ وفتح الدليل في VS Code، سيقترح تلقائيًا تثبيت امتداد دعم Python.

> **ملاحظة**: إذا اقترح VS Code إعادة فتح المستودع في حاوية، رفض هذا الطلب لاستخدام الإصدار المثبت محليًا من Python.

### استخدام Jupyter في المتصفح

يمكنك أيضًا العمل على المشروع باستخدام [بيئة Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) مباشرة داخل متصفحك. يوفر كل من Jupyter الكلاسيكي و[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) بيئة تطوير ممتعة مع ميزات مثل الإكمال التلقائي، تمييز الكود، إلخ.

لبدء Jupyter محليًا، توجه إلى الطرفية/سطر الأوامر، انتقل إلى دليل الدورة، وقم بتنفيذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

سيبدأ هذا مثيل Jupyter وسيتم عرض عنوان URL للوصول إليه داخل نافذة سطر الأوامر.

بمجرد الوصول إلى عنوان URL، يجب أن ترى مخطط الدورة وأن تكون قادرًا على التنقل إلى أي ملف `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` حيث يمكنك عرض الكود والمخرجات.

## استخدام خدمة Azure OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تعمل فيها مع خدمة Azure OpenAI، يرجى اتباع هذا الدليل حول كيفية [إنشاء ونشر مورد خدمة Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## استخدام واجهة برمجة التطبيقات OpenAI لأول مرة

إذا كانت هذه هي المرة الأولى التي تعمل فيها مع واجهة برمجة التطبيقات OpenAI، يرجى اتباع الدليل حول كيفية [إنشاء واستخدام الواجهة.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## لقاء المتعلمين الآخرين

لقد أنشأنا قنوات في خادم Discord الرسمي الخاص بمجتمع الذكاء الاصطناعي [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) للقاء المتعلمين الآخرين. هذه طريقة رائعة للتواصل مع رواد الأعمال والمطورين والطلاب الآخرين الذين يتطلعون إلى تحسين مهاراتهم في الذكاء الاصطناعي التوليدي.

[![انضم إلى قناة Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

سيكون فريق المشروع أيضًا في هذا الخادم Discord لمساعدة أي متعلمين.

## المساهمة

هذه الدورة هي مبادرة مفتوحة المصدر. إذا رأيت مناطق للتحسين أو مشاكل، يرجى إنشاء [طلب سحب](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) أو تسجيل [مشكلة GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

سيقوم فريق المشروع بتتبع جميع المساهمات. المساهمة في المصادر المفتوحة هي طريقة رائعة لبناء حياتك المهنية في الذكاء الاصطناعي التوليدي.

تتطلب معظم المساهمات منك الموافقة على اتفاقية ترخيص المساهم (CLA) التي تعلن أنك لديك الحق في وتقوم فعليًا بمنحنا الحقوق لاستخدام مساهمتك. للحصول على التفاصيل، قم بزيارة [موقع اتفاقية ترخيص المساهم CLA](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

مهم: عند ترجمة النص في هذا المستودع، يرجى التأكد من عدم استخدام الترجمة الآلية. سنقوم بالتحقق من الترجمات عبر المجتمع، لذا يرجى التطوع للترجمات فقط في اللغات التي تكون فيها محترفًا.

عند تقديم طلب سحب، سيقوم CLA-bot تلقائيًا بتحديد ما إذا كنت بحاجة إلى تقديم CLA وتزيين PR بشكل مناسب (مثل التصنيف، التعليق). ببساطة اتبع التعليمات المقدمة من البوت. ستحتاج فقط إلى القيام بذلك مرة واحدة عبر جميع المستودعات التي تستخدم CLA الخاص بنا.

لقد تبنى هذا المشروع [مدونة قواعد السلوك المفتوحة المصدر من Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). لمزيد من المعلومات، اقرأ الأسئلة الشائعة حول مدونة قواعد السلوك أو اتصل بـ [بريد إلكتروني opencode](opencode@microsoft.com) مع أي أسئلة أو تعليقات إضافية.

## لنبدأ

الآن بعد أن أكملت الخطوات اللازمة لإكمال هذه الدورة، دعنا نبدأ بالحصول على [مقدمة إلى الذكاء الاصطناعي التوليدي وLLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.