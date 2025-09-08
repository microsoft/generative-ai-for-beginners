<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T13:59:27+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ar"
}
-->
# الإعداد المحلي 🖥️

**استخدم هذا الدليل إذا كنت تفضل تشغيل كل شيء على جهازك المحمول.**  
أمامك خياران: **(A) بايثون محلي + بيئة افتراضية** أو **(B) حاوية تطوير VS Code مع Docker**.  
اختر ما يناسبك—كلاهما يؤدي لنفس الدروس.

## 1. المتطلبات الأساسية

| الأداة              | الإصدار / الملاحظات                                                                |
|--------------------|------------------------------------------------------------------------------------|
| **بايثون**         | 3.10 فما فوق (احصل عليه من <https://python.org>)                                   |
| **Git**            | الأحدث (يأتي مع Xcode / Git for Windows / مدير حزم لينكس)                          |
| **VS Code**        | اختياري لكن يُنصح به <https://code.visualstudio.com>                               |
| **Docker Desktop** | *فقط* للخيار B. تثبيت مجاني: <https://docs.docker.com/desktop/>                   |

> 💡 **نصيحة** – تحقق من الأدوات في الطرفية:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. الخيار A – بايثون محلي (الأسرع)

### الخطوة 1  استنساخ هذا المستودع

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### الخطوة 2 إنشاء وتفعيل بيئة افتراضية

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ يجب أن يبدأ السطر الآن بـ (.venv)—هذا يعني أنك داخل البيئة الافتراضية.

### الخطوة 3 تثبيت الاعتمادات

```bash
pip install -r requirements.txt
```

انتقل مباشرة إلى القسم 3 حول [مفاتيح API](../../../00-course-setup)

## 2. الخيار B – حاوية تطوير VS Code (Docker)

قمنا بإعداد هذا المستودع والدورة باستخدام [حاوية تطوير](https://containers.dev?WT.mc_id=academic-105485-koreyst) تحتوي على بيئة تشغيل شاملة تدعم بايثون 3، .NET، Node.js وجافا. تم تعريف الإعدادات ذات الصلة في ملف `devcontainer.json` الموجود في مجلد `.devcontainer/` في جذر المستودع.

>**لماذا تختار هذا الخيار؟**
>بيئة مطابقة تماماً لـ Codespaces؛ لا يوجد اختلاف في الاعتمادات.

### الخطوة 0 تثبيت الإضافات

Docker Desktop – تأكد أن ```docker --version``` يعمل.
VS Code Remote – إضافة الحاويات (ID: ms-vscode-remote.remote-containers).

### الخطوة 1 فتح المستودع في VS Code

ملف ▸ فتح مجلد…  → generative-ai-for-beginners

VS Code يكتشف .devcontainer/ ويظهر لك رسالة.

### الخطوة 2 إعادة الفتح داخل الحاوية

اضغط على “Reopen in Container”. سيقوم Docker ببناء الصورة (≈ 3 دقائق أول مرة).
عندما يظهر السطر في الطرفية، ستكون داخل الحاوية.

## 2. الخيار C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، بايثون، وبعض الحزم.
Conda نفسه هو مدير حزم، يسهل إعداد والتبديل بين [**البيئات الافتراضية**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) المختلفة وحزم بايثون. كما أنه مفيد لتثبيت الحزم غير المتوفرة عبر `pip`.

### الخطوة 0  تثبيت Miniconda

اتبع [دليل تثبيت MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) لإعداده.

```bash
conda --version
```

### الخطوة 1 إنشاء بيئة افتراضية

أنشئ ملف بيئة جديد (*environment.yml*). إذا كنت تستخدم Codespaces، أنشئه داخل مجلد `.devcontainer`، أي `.devcontainer/environment.yml`.

### الخطوة 2  تعبئة ملف البيئة

أضف المقطع التالي إلى ملف  `environment.yml`

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

### الخطوة 3 إنشاء بيئة Conda الخاصة بك

نفذ الأوامر التالية في الطرفية/سطر الأوامر

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

راجع [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

## 2 الخيار D – Jupyter الكلاسيكي / Jupyter Lab (في المتصفح)

> **لمن هذا الخيار؟**  
> لأي شخص يفضل واجهة Jupyter الكلاسيكية أو يريد تشغيل الدفاتر بدون VS Code.  

### الخطوة 1  التأكد من تثبيت Jupyter

لتشغيل Jupyter محلياً، انتقل للطرفية/سطر الأوامر، واذهب إلى مجلد الدورة، ونفذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

سيبدأ هذا جلسة Jupyter وسيظهر الرابط للوصول إليه في نافذة سطر الأوامر.

عند الدخول للرابط، سترى محتوى الدورة ويمكنك تصفح أي ملف `*.ipynb`. مثلاً، `08-building-search-applications/python/oai-solution.ipynb`.

## 3. إضافة مفاتيح API الخاصة بك

الحفاظ على أمان وسرية مفاتيح API أمر مهم عند بناء أي تطبيق. ننصح بعدم تخزين أي مفاتيح API مباشرة في الكود. رفع هذه التفاصيل إلى مستودع عام قد يؤدي لمشاكل أمنية وحتى تكاليف غير مرغوبة إذا استغلها شخص سيء.
إليك دليل خطوة بخطوة لإنشاء ملف `.env` لبايثون وإضافة `GITHUB_TOKEN`:

1. **انتقل إلى مجلد مشروعك**: افتح الطرفية أو موجه الأوامر واذهب إلى جذر مشروعك حيث تريد إنشاء ملف `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **أنشئ ملف `.env`**: استخدم محرر النصوص المفضل لديك لإنشاء ملف جديد باسم `.env`. إذا كنت تستخدم سطر الأوامر، يمكنك استخدام `touch` (على أنظمة يونكس) أو `echo` (على ويندوز):

   أنظمة يونكس:

   ```bash
   touch .env
   ```

   ويندوز:

   ```cmd
   echo . > .env
   ```

3. **تعديل ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثلاً VS Code، Notepad++، أو أي محرر آخر). أضف السطر التالي للملف، مع استبدال `your_github_token_here` برمز GitHub الخاص بك:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **احفظ الملف**: احفظ التغييرات وأغلق المحرر.

5. **تثبيت `python-dotenv`**: إذا لم تكن قد فعلت ذلك، ستحتاج لتثبيت حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق بايثون الخاص بك. يمكنك تثبيتها باستخدام `pip`:

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

هذا كل شيء! لقد أنشأت ملف `.env` بنجاح، وأضفت رمز GitHub الخاص بك، وحملته في تطبيق بايثون.

🔐 لا تقم أبداً برفع .env—فهو مضاف بالفعل إلى .gitignore.
تعليمات المزودين الكاملة موجودة في [`providers.md`](03-providers.md).

## 4. ماذا بعد؟

| أريد أن…            | اذهب إلى…                                                                  |
|---------------------|----------------------------------------------------------------------------|
| بدء الدرس الأول      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| إعداد مزود LLM      | [`providers.md`](03-providers.md)                                          |
| لقاء متعلمين آخرين   | [انضم إلى Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. استكشاف الأخطاء وإصلاحها

| العرض                                   | الحل                                                             |
|------------------------------------------|------------------------------------------------------------------|
| `python not found`                       | أضف بايثون إلى PATH أو أعد فتح الطرفية بعد التثبيت              |
| `pip` لا يستطيع بناء wheels (ويندوز)    | `pip install --upgrade pip setuptools wheel` ثم أعد المحاولة.    |
| `ModuleNotFoundError: dotenv`            | نفذ `pip install -r requirements.txt` (البيئة لم تُثبت).         |
| فشل بناء Docker *No space left*          | Docker Desktop ▸ *الإعدادات* ▸ *الموارد* → زيادة حجم القرص.      |
| VS Code يستمر في طلب إعادة الفتح         | قد يكون لديك كلا الخيارين نشطين؛ اختر واحداً (venv **أو** الحاوية)|
| أخطاء OpenAI 401 / 429                   | تحقق من قيمة `OPENAI_API_KEY` / حدود معدل الطلبات.              |
| أخطاء عند استخدام Conda                  | ثبت مكتبات Microsoft AI باستخدام `conda install -c microsoft azure-ai-ml`|

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُنصح بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.