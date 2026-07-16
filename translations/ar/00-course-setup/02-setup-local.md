# الإعداد المحلي 🖥️

**استخدم هذا الدليل إذا كنت تفضل تشغيل كل شيء على حاسوبك المحمول الخاص.**   
لديك طريقان: **(أ) بايثون مدمج + بيئة افتراضية** أو **(ب) حاوية تطوير VS Code مع Docker**.  
اختر ما تشعر أنه أسهل — كلاهما يؤدي إلى نفس الدروس.

## 1. المتطلبات المسبقة

| الأداة               | الإصدار / الملاحظات                                                                  |
|--------------------|--------------------------------------------------------------------------------------|
| **بايثون**         | 3.10 + (احصل عليه من <https://python.org>)                                            |
| **جيّت**            | أحدث إصدار (يأتي مع Xcode / Git لنظام ويندوز / مدير الحزم على لينوكس)                   |
| **VS Code**        | اختياري لكنه موصى به <https://code.visualstudio.com>                             |
| **Docker Desktop** | *فقط* للخيار ب. تثبيت مجاني: <https://docs.docker.com/desktop/>                |

> 💡 **نصيحة** – تحقق من الأدوات في الطرفية:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. الخيار أ – بايثون مدمج (الأسرع)

### الخطوة 1 استنساخ هذا المستودع

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### الخطوة 2 إنشاء وتفعيل البيئة الافتراضية

```bash
python -m venv .venv          # اصنع واحدًا
source .venv/bin/activate     # ماك أو إس / لينكس
.\.venv\Scripts\activate      # ويندوز باورشيل
```

✅ يجب أن يبدأ الموجه الآن بـ (.venv) — هذا يعني أنك داخل البيئة.

### الخطوة 3 تثبيت التبعيات

```bash
pip install -r requirements.txt
```

تخط إلى القسم 3 حول [مفاتيح API](#3-أضف-مفاتيح-api-الخاصة-بك)

## 2. الخيار ب – حاوية تطوير VS Code (Docker)

أعددنا هذا المستودع والدورة بواسطة [حاوية تطوير](https://containers.dev?WT.mc_id=academic-105485-koreyst) التي تحتوي على بيئة تشغيل شاملة تدعم تطوير Python3, .NET, Node.js و Java. التكوين المتعلق معرفة في ملف `devcontainer.json` الموجود في مجلد `.devcontainer/` في جذر المستودع.

>**لماذا تختار هذا؟**
>بيئة مطابقة لـ Codespaces؛ لا انحراف في التبعيات.

### الخطوة 0 تثبيت الإضافات

Docker Desktop – تأكد من عمل الأمر ```docker --version```.
امتداد VS Code Remote – الحاويات (المعرّف: ms-vscode-remote.remote-containers).

### الخطوة 1 افتح المستودع في VS Code

ملف ▸ فتح مجلد…  → generative-ai-for-beginners

VS Code يكتشف .devcontainer/ ويظهر لك موجه.

### الخطوة 2 أعد الفتح داخل الحاوية

انقر على "إعادة الفتح داخل الحاوية". يقوم Docker ببناء الصورة (≈ 3 دقائق في المرة الأولى).
عند ظهور موجه الطرفية، تكون داخل الحاوية.

## 2. الخيار ج – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) هو مثبت خفيف لتثبيت [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)، بايثون، وبعض الحزم.
Conda نفسها هي مدير حزم يسهل إعداد والانتقال بين بيئات بايثون [**الافتراضية**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) والحزم. كما أنها مفيدة لتثبيت الحزم غير المتوفرة عبر `pip`.

### الخطوة 0 تثبيت Miniconda

اتبع [دليل تثبيت MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) لإعداده.

```bash
conda --version
```

### الخطوة 1 إنشاء بيئة افتراضية

أنشئ ملف بيئة جديد (*environment.yml*). إذا كنت تستخدم Codespaces، أنشئه داخل مجلد `.devcontainer` أي `.devcontainer/environment.yml`.

### الخطوة 2 ملء ملف البيئة الخاص بك

أضف المقتطف التالي إلى `environment.yml`

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

نفذ الأوامر أدناه في سطر الأوامر/الطرفية

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # ينطبق مسار فرعي .devcontainer فقط على إعدادات مساحة الرموز
conda activate ai4beg
```

راجع [دليل بيئات Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) إذا واجهت أي مشاكل.

## 2 الخيار د – Jupyter الكلاسيكي / Jupyter Lab (في متصفحك)

> **لمن هذا؟**  
> لأي شخص يحب واجهة Jupyter الكلاسيكية أو يرغب بتشغيل دفاتر الملاحظات بدون VS Code.  

### الخطوة 1 تأكد من تثبيت Jupyter

لبدء Jupyter محلياً، توجه إلى الطرفية/سطر الأوامر، انتقل إلى مجلد الدورة، ونفذ:

```bash
jupyter notebook
```

أو

```bash
jupyterhub
```

سيبدأ هذا جلسة Jupyter وسيُعرض رابط الوصول إليه داخل نافذة سطر الأوامر.

بمجرد وصولك للرابط، يجب أن ترى مخطط الدورة ويمكنك التنقل إلى أي ملف `*.ipynb`. على سبيل المثال، `08-building-search-applications/python/oai-solution.ipynb`.

## 3. أضف مفاتيح API الخاصة بك

من المهم الحفاظ على سرية وأمان مفاتيح API عند بناء أي نوع من التطبيقات. نوصي بعدم تخزين أي مفاتيح API مباشرة في شفرتك. إذا تم رفع هذه التفاصيل إلى مستودع عام، قد يؤدي ذلك إلى مشكلات أمنية وتكاليف غير مرغوب فيها في حال استخدامها من قبل جهة خبيثة.
إليك دليل خطوة بخطوة لإنشاء ملف `.env` لبايثون وإضافة بيانات اعتماد Microsoft Foundry Models الخاصة بك:

> **ملاحظة:** نماذج GitHub (ومتغير `GITHUB_TOKEN`) ستتوقف عن العمل في نهاية يوليو 2026. يستخدم هذا الدليل [نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) بدلاً من ذلك. تفضل العمل بالكامل دون اتصال؟ انظر [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **انتقل إلى مجلد مشروعك**: افتح الطرفية أو موجه الأوامر وانتقل إلى المجلد الجذري لمشروعك حيث تريد إنشاء ملف `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **إنشاء ملف `.env`**: استخدم محرر النصوص المفضل لديك لإنشاء ملف جديد باسم `.env`. إذا كنت تستخدم سطر الأوامر، يمكنك استخدام `touch` (في أنظمة يونكس) أو `echo` (في ويندوز):

   أنظمة يونكس:

   ```bash
   touch .env
   ```

   ويندوز:

   ```cmd
   echo . > .env
   ```

3. **تحرير ملف `.env`**: افتح ملف `.env` في محرر نصوص (مثل VS Code، Notepad++، أو أي محرر آخر). أضف الأسطر التالية إلى الملف، واستبدل عناصر النائب بنقطة نهاية مشروع Microsoft Foundry ورمز API الفعلي الخاص بك:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **حفظ الملف**: احفظ التغييرات وأغلق محرر النصوص.

5. **تثبيت `python-dotenv`**: إذا لم تكن قد فعلت ذلك، ستحتاج لتثبيت حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env` إلى تطبيق بايثون الخاص بك. يمكنك تثبيتها باستخدام `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **تحميل متغيرات البيئة في سكريبت بايثون الخاص بك**: في سكريبت بايثون، استخدم حزمة `python-dotenv` لتحميل متغيرات البيئة من ملف `.env`:

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

هذا كل شيء! لقد أنشأت بنجاح ملف `.env`، أضفت بيانات اعتماد Microsoft Foundry Models، وحملتها في تطبيق بايثون الخاص بك.

🔐 لا تُدرج ملف .env في الالتزامات — هو مُدرج بالفعل في .gitignore.
تعليمات المزود كاملة موجودة في [`providers.md`](03-providers.md).

## 4. ماذا بعد؟

| أريد أن…          | انتقل إلى…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| بدء الدرس 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| إعداد مزود LLM | [`providers.md`](03-providers.md)                                       |
| لقاء المتعلمين الآخرين | [انضم إلى ديسكورد](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. استكشاف الأخطاء وإصلاحها

| العرض                                   | الحل                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | أضف بايثون إلى PATH أو أعد فتح الطرفية بعد التثبيت            |
| `pip` لا يستطيع بناء العجلات (ويندوز)       | `pip install --upgrade pip setuptools wheel` ثم حاول مجددًا.        |
| `ModuleNotFoundError: dotenv`             | نفّذ `pip install -r requirements.txt` (البيئة لم تُثبت).   |
| فشل بناء Docker *No space left*        | Docker Desktop ▸ *الإعدادات* ▸ *الموارد* → زد حجم القرص. |
| VS Code يستمر بطلب إعادة الفتح         | قد يكون كلا الخيارين نشطا؛ اختر واحدًا (venv **أو** الحاوية)|
| أخطاء OpenAI 401 / 429                   | تحقق من قيمة `OPENAI_API_KEY` / حدود معدل الطلب.             |
| أخطاء استخدام Conda                        | ثبّت مكتبات AI من مايكروسوفت باستخدام `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->