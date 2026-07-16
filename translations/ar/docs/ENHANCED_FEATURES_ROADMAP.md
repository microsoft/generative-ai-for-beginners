# خارطة طريق الميزات المحسّنة والتحسينات

يحدد هذا الوثيقة التحسينات والتطويرات الموصى بها لمناهج الذكاء الاصطناعي التوليدي للمبتدئين، استنادًا إلى مراجعة شاملة للكود وتحليل أفضل ممارسات الصناعة.

## الملخص التنفيذي

تم تحليل قاعدة الشيفرة للأمان وجودة الكود وفعالية التعليم. توفر هذه الوثيقة توصيات للإصلاحات الفورية، والتحسينات القصيرة الأجل، والتعزيزات المستقبلية.

---

## 1. تحسينات الأمان (الأولوية: حرجة)

### 1.1 الإصلاحات الفورية (مكتملة)

| المشكلة | الملفات المتأثرة | الحالة |
|-------|----------------|--------|
| مفتاح سري مضمّن في الكود | `05-advanced-prompts/python/aoai-solution.py` | تم الإصلاح |
| عدم تحقق متغيرات البيئة | عدة ملفات JS/TS | تم الإصلاح |
| استدعاءات دوال غير آمنة | `11-integrating-with-function-calling/js-githubmodels/app.js` | تم الإصلاح |
| تسريبات مقبض الملف | `08-building-search-applications/scripts/` | تم الإصلاح |
| عدم وجود مهلات للطلبات | `09-building-image-applications/python/` | تم الإصلاح |

### 1.2 ميزات أمان إضافية موصى بها

1. **أمثلة على تحديد حدود المعدل**
   - إضافة كود مثال يوضح كيفية تنفيذ تحديد معدل لاستدعاءات API
   - توضيح أنماط التراجع الأُسّي

2. **تدوير مفاتيح API**
   - إضافة توثيق لأفضل الممارسات في تدوير مفاتيح API
   - تضمين أمثلة لاستخدام Azure Key Vault أو خدمات مشابهة

3. **تكامل أمان المحتوى**
   - إضافة أمثلة باستخدام Azure Content Safety API
   - توضيح أنماط التعديل على الإدخال/الإخراج

---

## 2. تحسينات جودة الكود

### 2.1 ملفات التكوين المضافة

| الملف | الغرض |
|------|---------|
| `.eslintrc.json` | قواعد تنسيق وتحليل JavaScript/TypeScript |
| `.prettierrc` | معايير تنسيق الكود |
| `pyproject.toml` | تكوين أدوات Python (Black, Ruff, mypy) |

### 2.2 إنشاء وحدات خدمات مشتركة

وحدة `shared/python/` الجديدة تحتوي على:
- `env_utils.py` - التعامل مع متغيرات البيئة
- `input_validation.py` - التحقق من صحة وتنقية المدخلات
- `api_utils.py` - أغلفة آمنة لطلبات API

### 2.3 تحسينات الكود الموصى بها

1. **تغطية باستخدام دلالات الأنواع (Type Hints)**
   - إضافة دلالات نوع لجميع ملفات Python
   - تفعيل وضع TypeScript الصارم في جميع مشاريع TS

2. **معايير التوثيق**
   - إضافة docstrings لكل دوال Python
   - إضافة تعليقات JSDoc لكل دوال JavaScript/TypeScript

3. **إطار الاختبار**
   - إضافة تهيئة pytest وأمثلة للاختبارات _(تم: تكوين pytest في `pyproject.toml`; أمثلة للاختبارات للوحدات المشتركة في [`tests/`](../../../tests) تعمل في CI)_
   - إضافة تهيئة Jest ل JavaScript/TypeScript

---

## 3. تحسينات تعليمية

### 3.1 مواضيع دروس جديدة

1. **الأمان في تطبيقات الذكاء الاصطناعي** (درس مقترح 22)
   - هجمات وتعاملات حقن المطالبات
   - إدارة مفاتيح API
   - تعديل المحتوى
   - تحديد حدود المعدل ومنع سوء الاستخدام

2. **نشر الإنتاج** (درس مقترح 23)
   - الحاويات باستخدام Docker
   - خطوط CI/CD
   - المراقبة والتسجيل
   - إدارة التكاليف

3. **تقنيات RAG المتقدمة** (درس مقترح 24)
   - البحث الهجين (الكلمات المفتاحية + الدلالي)
   - استراتيجيات إعادة الترتيب
   - RAG متعدد الوسائط
   - مقاييس التقييم

### 3.2 تحسينات في الدروس الحالية

| الدرس | التحسين الموصى به |
|--------|------------------------|
| 06 - توليد النص | إضافة أمثلة على الاستجابة المتدفقة |
| 07 - تطبيقات الدردشة | إضافة أنماط ذاكرة المحادثة |
| 08 - تطبيقات البحث | إضافة مقارنة قواعد البيانات المتجهة |
| 09 - توليد الصور | إضافة أمثلة تحرير/تنويع الصور |
| 11 - استدعاء الدوال | إضافة استدعاء دوال متوازٍ |
| 15 - RAG | إضافة مقارنة استراتيجيات التجزئة |
| 17 - وكلاء الذكاء الاصطناعي | إضافة تنسيق متعدد الوكلاء |

---

## 4. تحديث واجهات برمجة التطبيقات (API)

### 4.1 أنماط API المهجورة (الهجرة مكتملة)

تم ترحيل جميع عينات الدردشة بلغة Python وTypeScript من واجهة Chat Completions API إلى واجهة Responses API (`client.responses.create(...)` → `response.output_text`).

| النمط القديم | النمط الجديد | الحالة |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (الدردشة) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | مكتمل |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | مكتمل |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | حزمة `openai` `client.responses.create()` → `response.output_text` | مكتمل |
| `df.append()` (pandas) | `pd.concat()` | مكتمل |

> **ملاحظة:** عينات نماذج Microsoft Foundry التي تستخدم SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) لا زالت تستخدم Model Inference API وليس Responses API. يتم الاحتفاظ بـ `AzureOpenAI()` عمدًا حيث لا زال صالحًا (للتضمينات وتوليد الصور).

### 4.2 ميزات API جديدة للعرض

1. **مخرجات منظمة** (OpenAI)
   - وضع JSON
   - استدعاء الدوال مع مخططات صارمة

2. **قدرات الرؤية**
   - تحليل الصور مع GPT-4o (الرؤية)
   - مطالبات متعددة الوسائط

3. **أدوات مدمجة في Responses API** (تغني عن Assistants API القديم)
   - مفسر الشفرة
   - بحث في الملفات
   - بحث ويب وأدوات مخصصة

---

## 5. تحسينات البنية التحتية

### 5.1 تحسينات CI/CD

تم التنفيذ في [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): تطبيق قواعد التنسيق/التحليل ل Python (Ruff + Black) بشكل **إلزامي** على وحدة الخصائص المشتركة `shared/` ويعمل كتنبيه لبقية المنهج، بالإضافة إلى تمرير ESLint إرشادي ل JavaScript/TypeScript. النطاق التوضيحي كان:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 فحص الأمان

تم التنفيذ في [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): تحليل CodeQL لـ Python وJavaScript/TypeScript (على الدفع، وطلبات السحب، وجدولة أسبوعية) بالإضافة إلى مراجعة الاعتماديات على طلبات السحب. النطاق التوضيحي كان:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. تحسينات تجربة المطور

### 6.1 تحسينات DevContainer

تم التنفيذ في [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) و [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): الحاوية تتضمن الآن ملحقات Pylance، Black، Ruff، ESLint، Prettier، وCopilot، كما تفعّل التنسيق التلقائي عند الحفظ المرتبط بتكوين Black/Prettier الخاص بالمستودع، وتثبت أدوات المطور (`ruff`, `black`, `mypy`, `pytest`) بحيث يمكن تكرار [تدفق عمل جودة الكود](../../../.github/workflows/code-quality.yml) محليًا. صورة القاعدة `mcr.microsoft.com/devcontainers/universal` تضم Python وNode، لذلك لا تحتاج مزايا إضافية. النطاق التوضيحي كان:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 ملعب تفاعلي

النظر في الإضافة:
- دفاتر Jupyter مع مفاتيح API مملوءة مسبقًا (عبر البيئة)
- عروض Gradio/Streamlit للمتعلمين البصريين
- اختبارات تفاعلية لتقييم المعرفة

---

## 7. دعم متعدد اللغات

### 7.1 التغطية اللغوية الحالية

| التقنية | الدروس المشمولة | الحالة |
|------------|-----------------|--------|
| Python | الكل | مكتمل |
| TypeScript | 06-09، 11 | جزئي |
| JavaScript | 06-08، 11 | جزئي |
| .NET/C# | بعض | جزئي |

### 7.2 الإضافات الموصى بها

1. **Go** - نمو في أدوات AI/ML
2. **Rust** - التطبيقات الحساسة للأداء
3. **Java/Kotlin** - تطبيقات المؤسسات

---

## 8. تحسينات الأداء

### 8.1 تحسينات على مستوى الكود

1. **أنماط Async/Await**
   - إضافة أمثلة غير متزامنة للمعالجة الدُفعية
   - توضيح المكالمات المتزامنة لـ API

2. **استراتيجيات التخزين المؤقت**
   - إضافة أمثلة تخزين مؤقت للتضمينات
   - توضيح أنماط تخزين الاستجابة مؤقتًا

3. **تحسين التوكنز**
   - إضافة أمثلة استخدام tiktoken
   - توضيح تقنيات ضغط المطالبات

### 8.2 أمثلة تحسين التكلفة

إضافة أمثلة توضيحية:
- اختيار النموذج بناءً على تعقيد المهمة
- هندسة المطالبات لكفاءة التوكنز
- المعالجة الدُفعية للعمليات الكثيفة

---

## 9. سهولة الوصول والتمدد الدولي

### 9.1 حالة الترجمة الحالية

جميع الترجمات **مكتملة** وتُنتج تلقائيًا بواسطة [مترجم Azure Co-op](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst)، الذي ينتج ويحافظ على تزامن نسخ المنهج بأكثر من 50 لغة مع المصدر الإنجليزي. المحتوى المترجم موجود تحت `translations/` والصور المترجمة تحت `translated_images/`؛ القائمة الكاملة للغات المتاحة منشورة في أعلى README الخاص بالمستودع.

| الجانب | الحالة |
|--------|--------|
| تغطية الترجمة | مكتملة — أكثر من 50 لغة، كل الدروس |
| طريقة الترجمة | تلقائية عبر [مترجم Azure Co-op](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| الحفاظ على التزامن مع المصدر الإنجليزي | نعم — يُعاد توليدها تلقائيًا |

### 9.2 تحسينات سهولة الوصول

1. إضافة نص بديل لكل الصور
2. ضمان وجود تمييز نحوي صالح لأمثلة الشيفرة
3. إضافة نصوص فيديو لكل المحتوى الفيديوي
4. ضمان تباين الألوان حسب إرشادات WCAG

---

## 10. أولوية التنفيذ

### المرحلة 1: فورية (الأسبوع 1-2)
- [x] إصلاح قضايا الأمان الحرجة
- [x] إضافة تكوين جودة الكود
- [x] إنشاء أدوات مشتركة
- [x] توثيق إرشادات الأمان

### المرحلة 2: قصيرة الأجل (الأسبوع 3-4)
- [x] تحديث أنماط API المهجورة (من Chat Completions إلى Responses API، لـ Python + TypeScript)
- [ ] إضافة دلالات نوع لكل ملفات Python (تم للوحدة `shared/` المستدامة؛ عينات الدروس بسيطة)
- [x] إضافة تدفقات عمل CI/CD لجودة الكود
- [x] إنشاء تدفق عمل فحص الأمان

### المرحلة 3: متوسطة الأجل (الشهر 2-3)
- [ ] إضافة درس أمان جديد
- [ ] إضافة درس النشر في الإنتاج
- [x] تحسين إعداد DevContainer
- [ ] إضافة عروض تفاعلية

### المرحلة 4: طويلة الأجل (الشهر 4+)
- [ ] إضافة درس RAG متقدم
- [ ] توسيع تغطية اللغات
- [ ] إضافة مجموعة اختبارات شاملة
- [ ] إنشاء برنامج شهادات

---

## الخلاصة

توفر هذه الخارطة نهجًا منظمًا لتحسين منهج الذكاء الاصطناعي التوليدي للمبتدئين. من خلال معالجة مخاوف الأمان، تحديث APIs، وإضافة محتوى تعليمي، سيصبح المقرر أفضل تجهيزًا لإعداد الطلاب لتطوير تطبيقات الذكاء الاصطناعي في العالم الحقيقي.

للأسئلة أو المساهمات، يرجى فتح قضية في مستودع GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->