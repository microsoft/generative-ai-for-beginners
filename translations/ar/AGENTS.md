<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:51:56+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ar"
}
-->
# AGENTS.md

## نظرة عامة على المشروع

يحتوي هذا المستودع على منهج شامل مكون من 21 درسًا لتعليم أساسيات الذكاء الاصطناعي التوليدي وتطوير التطبيقات. تم تصميم الدورة للمبتدئين وتغطي كل شيء بدءًا من المفاهيم الأساسية وصولًا إلى بناء تطبيقات جاهزة للإنتاج.

**التقنيات الرئيسية:**
- Python 3.9+ مع المكتبات: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript مع Node.js والمكتبات: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- خدمة Azure OpenAI، واجهة برمجة تطبيقات OpenAI، ونماذج GitHub
- دفاتر Jupyter للتعلم التفاعلي
- حاويات التطوير لتوفير بيئة تطوير متسقة

**هيكل المستودع:**
- 21 دليلًا مرقمًا للدروس (00-21) تحتوي على ملفات README، أمثلة على الأكواد، والواجبات
- تطبيقات متعددة: Python، TypeScript، وأحيانًا أمثلة .NET
- دليل الترجمات يحتوي على أكثر من 40 نسخة لغوية
- إعداد مركزي عبر ملف `.env` (استخدم `.env.copy` كقالب)

## أوامر الإعداد

### إعداد المستودع الأولي

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### إعداد بيئة Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### إعداد Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### إعداد حاوية التطوير (موصى به)

يتضمن المستودع إعداد `.devcontainer` لـ GitHub Codespaces أو VS Code Dev Containers:

1. افتح المستودع في GitHub Codespaces أو VS Code مع امتداد Dev Containers
2. ستقوم حاوية التطوير تلقائيًا بـ:
   - تثبيت تبعيات Python من `requirements.txt`
   - تشغيل سكربت ما بعد الإنشاء (`.devcontainer/post-create.sh`)
   - إعداد نواة Jupyter

## سير العمل التطويري

### متغيرات البيئة

تستخدم جميع الدروس التي تتطلب الوصول إلى واجهات برمجة التطبيقات متغيرات البيئة المحددة في `.env`:

- `OPENAI_API_KEY` - لواجهة برمجة تطبيقات OpenAI
- `AZURE_OPENAI_API_KEY` - لخدمة Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - عنوان URL لنقطة نهاية Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - اسم نشر نموذج إكمال المحادثة
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - اسم نشر نموذج التضمين
- `AZURE_OPENAI_API_VERSION` - إصدار واجهة برمجة التطبيقات (الافتراضي: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - لنماذج Hugging Face
- `GITHUB_TOKEN` - لنماذج GitHub

### تشغيل أمثلة Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### تشغيل أمثلة TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### تشغيل دفاتر Jupyter

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### العمل مع أنواع الدروس المختلفة

- **دروس "التعلم"**: تركز على وثائق README.md والمفاهيم
- **دروس "البناء"**: تتضمن أمثلة عملية على الأكواد بـ Python وTypeScript
- يحتوي كل درس على README.md يتضمن النظرية، استعراض الأكواد، وروابط لمحتوى الفيديو

## إرشادات أسلوب الأكواد

### Python

- استخدم `python-dotenv` لإدارة متغيرات البيئة
- استورد مكتبة `openai` للتفاعل مع واجهة برمجة التطبيقات
- استخدم `pylint` للتحقق من الأكواد (تتضمن بعض الأمثلة `# pylint: disable=all` للتبسيط)
- اتبع اتفاقيات التسمية في PEP 8
- قم بتخزين بيانات اعتماد واجهة برمجة التطبيقات في ملف `.env`، وليس في الكود

### TypeScript

- استخدم حزمة `dotenv` لمتغيرات البيئة
- إعداد TypeScript في `tsconfig.json` لكل تطبيق
- استخدم `@azure/openai` أو `@azure-rest/ai-inference` لخدمات Azure
- استخدم `nodemon` للتطوير مع إعادة التحميل التلقائي
- قم بالبناء قبل التشغيل: `npm run build` ثم `npm start`

### الاتفاقيات العامة

- حافظ على بساطة الأمثلة التعليمية
- قم بتضمين تعليقات تشرح المفاهيم الرئيسية
- يجب أن تكون أكواد كل درس مكتفية ذاتيًا وقابلة للتشغيل
- استخدم تسمية متسقة: `aoai-` لخدمة Azure OpenAI، `oai-` لواجهة برمجة تطبيقات OpenAI، `githubmodels-` لنماذج GitHub

## إرشادات التوثيق

### أسلوب Markdown

- يجب أن تكون جميع الروابط مغلفة بصيغة `[النص](../../الرابط)` بدون مسافات إضافية
- يجب أن تبدأ الروابط النسبية بـ `./` أو `../`
- يجب أن تتضمن جميع الروابط إلى نطاقات Microsoft معرف التتبع: `?WT.mc_id=academic-105485-koreyst`
- لا تستخدم المواقع المحلية الخاصة بالدول في الروابط (تجنب `/en-us/`)
- يتم تخزين الصور في مجلد `./images` بأسماء وصفية
- استخدم الأحرف الإنجليزية، الأرقام، والشرطات في أسماء الملفات

### دعم الترجمة

- يدعم المستودع أكثر من 40 لغة عبر إجراءات GitHub الآلية
- يتم تخزين الترجمات في دليل `translations/`
- لا تقبل الترجمات الجزئية
- لا يتم قبول الترجمات الآلية
- يتم تخزين الصور المترجمة في دليل `translated_images/`

## الاختبار والتحقق

### الفحوصات قبل الإرسال

يستخدم هذا المستودع إجراءات GitHub للتحقق. قبل إرسال طلبات السحب:

1. **التحقق من روابط Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **الاختبار اليدوي**:
   - اختبار أمثلة Python: قم بتنشيط البيئة الافتراضية وتشغيل السكربتات
   - اختبار أمثلة TypeScript: `npm install`، `npm run build`، `npm start`
   - تحقق من أن متغيرات البيئة تم تكوينها بشكل صحيح
   - تأكد من أن مفاتيح واجهة برمجة التطبيقات تعمل مع أمثلة الأكواد

3. **أمثلة الأكواد**:
   - تأكد من أن جميع الأكواد تعمل بدون أخطاء
   - اختبر مع كل من Azure OpenAI وواجهة برمجة تطبيقات OpenAI عند الاقتضاء
   - تحقق من أن الأمثلة تعمل مع نماذج GitHub حيثما كان ذلك مدعومًا

### لا توجد اختبارات آلية

هذا مستودع تعليمي يركز على الشروحات والأمثلة. لا توجد اختبارات وحدات أو اختبارات تكامل للتشغيل. التحقق يعتمد بشكل أساسي على:
- الاختبار اليدوي لأمثلة الأكواد
- إجراءات GitHub للتحقق من Markdown
- مراجعة المجتمع للمحتوى التعليمي

## إرشادات طلبات السحب

### قبل الإرسال

1. اختبر تغييرات الأكواد في كل من Python وTypeScript عند الاقتضاء
2. قم بتشغيل التحقق من Markdown (يتم تشغيله تلقائيًا عند تقديم الطلب)
3. تأكد من وجود معرفات التتبع على جميع روابط Microsoft
4. تحقق من صحة الروابط النسبية
5. تأكد من أن الصور تم الإشارة إليها بشكل صحيح

### تنسيق عنوان الطلب

- استخدم عناوين وصفية: `[الدرس 06] إصلاح خطأ في مثال Python` أو `تحديث README للدرس 08`
- أشر إلى أرقام القضايا عند الاقتضاء: `Fixes #123`

### وصف الطلب

- اشرح ما تم تغييره ولماذا
- أضف روابط إلى القضايا ذات الصلة
- بالنسبة لتغييرات الأكواد، حدد أي أمثلة تم اختبارها
- بالنسبة لطلبات الترجمة، قم بتضمين جميع الملفات للحصول على ترجمة كاملة

### متطلبات المساهمة

- توقيع اتفاقية Microsoft CLA (تلقائي عند أول طلب سحب)
- قم بتفريغ المستودع إلى حسابك قبل إجراء التغييرات
- طلب سحب واحد لكل تغيير منطقي (لا تجمع إصلاحات غير ذات صلة)
- حافظ على تركيز الطلبات وصغر حجمها قدر الإمكان

## سير العمل الشائع

### إضافة مثال كود جديد

1. انتقل إلى دليل الدرس المناسب
2. قم بإنشاء المثال في دليل `python/` أو `typescript/`
3. اتبع اتفاقية التسمية: `{provider}-{example-name}.{py|ts|js}`
4. اختبر باستخدام بيانات اعتماد واجهة برمجة التطبيقات الفعلية
5. قم بتوثيق أي متغيرات بيئة جديدة في README الخاص بالدرس

### تحديث التوثيق

1. قم بتحرير README.md في دليل الدرس
2. اتبع إرشادات Markdown (معرفات التتبع، الروابط النسبية)
3. يتم تحديث الترجمات بواسطة إجراءات GitHub (لا تقم بتحريرها يدويًا)
4. تحقق من صحة جميع الروابط

### العمل مع حاويات التطوير

1. يتضمن المستودع `.devcontainer/devcontainer.json`
2. يقوم سكربت ما بعد الإنشاء بتثبيت تبعيات Python تلقائيًا
3. يتم تكوين الإضافات لـ Python وJupyter مسبقًا
4. البيئة تعتمد على `mcr.microsoft.com/devcontainers/universal:2.11.2`

## النشر والنشر

هذا مستودع تعليمي - لا توجد عملية نشر. يتم استهلاك المنهج من خلال:

1. **مستودع GitHub**: الوصول المباشر إلى الأكواد والتوثيق
2. **GitHub Codespaces**: بيئة تطوير فورية مع إعداد مسبق
3. **Microsoft Learn**: قد يتم نشر المحتوى على منصة التعلم الرسمية
4. **docsify**: موقع توثيق مبني من Markdown (راجع `docsifytopdf.js` و`package.json`)

### بناء موقع التوثيق

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

**أخطاء استيراد Python**:
- تأكد من تنشيط البيئة الافتراضية
- قم بتشغيل `pip install -r requirements.txt`
- تحقق من أن إصدار Python هو 3.9+

**أخطاء بناء TypeScript**:
- قم بتشغيل `npm install` في دليل التطبيق المحدد
- تحقق من أن إصدار Node.js متوافق
- قم بمسح `node_modules` وأعد التثبيت إذا لزم الأمر

**أخطاء مصادقة واجهة برمجة التطبيقات**:
- تحقق من وجود ملف `.env` وقيمه الصحيحة
- تحقق من أن مفاتيح واجهة برمجة التطبيقات صالحة ولم تنتهِ صلاحيتها
- تأكد من صحة عناوين URL لنقاط النهاية لمنطقتك

**متغيرات البيئة المفقودة**:
- انسخ `.env.copy` إلى `.env`
- املأ جميع القيم المطلوبة للدرس الذي تعمل عليه
- أعد تشغيل التطبيق بعد تحديث `.env`

## موارد إضافية

- [دليل إعداد الدورة](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [إرشادات المساهمة](./CONTRIBUTING.md)
- [مدونة قواعد السلوك](./CODE_OF_CONDUCT.md)
- [سياسة الأمان](./SECURITY.md)
- [Discord الخاص بـ Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [مجموعة من أمثلة الأكواد المتقدمة](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## ملاحظات خاصة بالمشروع

- هذا مستودع **تعليمي** يركز على التعلم وليس الأكواد الإنتاجية
- الأمثلة بسيطة عمدًا وتركز على تعليم المفاهيم
- جودة الأكواد متوازنة مع وضوح التعليم
- كل درس مكتفٍ ذاتيًا ويمكن إكماله بشكل مستقل
- يدعم المستودع مزودي واجهات برمجة التطبيقات المتعددة: Azure OpenAI، OpenAI، ونماذج GitHub
- المحتوى متعدد اللغات مع إجراءات ترجمة آلية
- مجتمع نشط على Discord للأسئلة والدعم

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.