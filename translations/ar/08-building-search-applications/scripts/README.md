# إعداد بيانات التفريغ النصي

تقوم سكريبتات إعداد بيانات التفريغ النصي بتنزيل نصوص فيديوهات يوتيوب وتحضيرها للاستخدام مع نموذج البحث الدلالي مع تضمينات OpenAI والوظائف.

تم اختبار سكريبتات إعداد بيانات التفريغ النصي على أحدث إصدارات Windows 11 وmacOS Ventura وUbuntu 22.04 (والأعلى).

## إنشاء الموارد المطلوبة لخدمة Azure OpenAI

> [!IMPORTANT]
> نقترح تحديث واجهة سطر أوامر Azure إلى أحدث إصدار لضمان التوافق مع OpenAI
> راجع [التوثيق](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. إنشاء مجموعة موارد

> [!NOTE]
> في هذه التعليمات نستخدم مجموعة الموارد المسماة "semantic-video-search" في شرق الولايات المتحدة.
> يمكنك تغيير اسم مجموعة الموارد، ولكن عند تغيير موقع الموارد، 
> تحقق من [جدول توفر النماذج](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. إنشاء مورد خدمة Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. الحصول على نقطة النهاية والمفاتيح لاستخدامها في هذا التطبيق

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. نشر النماذج التالية:
   - الإصدار `2` أو أعلى من `text-embedding-ada-002`، المسمى `text-embedding-ada-002`
   - `gpt-5-mini` المسمى `gpt-5-mini`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## البرامج المطلوبة

- [بايثون 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) أو أعلى

## متغيرات البيئة

المتغيرات البيئية التالية مطلوبة لتشغيل سكريبتات إعداد بيانات تفريغ يوتيوب.

### على ويندوز

يُوصى بإضافة المتغيرات إلى متغيرات بيئة المستخدم الخاصة بك.
`بدء ويندوز` > `تحرير متغيرات نظام البيئة` > `متغيرات البيئة` > `متغيرات المستخدم` لـ [USER] > `جديد`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- يمكنك إضافة متغيرات البيئة إلى ملف التعريف PowerShell الخاص بك.

```powershell
$env:AZURE_OPENAI_API_KEY = "<مفتاح API لخدمة Azure OpenAI الخاص بك>"
$env:AZURE_OPENAI_ENDPOINT = "<نقطة نهاية خدمة Azure OpenAI الخاصة بك>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<اسم نشر نموذج خدمة Azure OpenAI الخاص بك>"
$env:GOOGLE_DEVELOPER_API_KEY = "<مفتاح API لمطور جوجل الخاص بك>"
``` -->

### على لينكس وmacOS

يُوصى بإضافة الصادرات التالية إلى ملف `~/.bashrc` أو `~/.zshrc` الخاص بك.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## تثبيت مكتبات بايثون المطلوبة

1. قم بتثبيت [عميل git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) إذا لم يكن مثبتاً مسبقاً.
1. من نافذة `الطرفية`، انسخ العينة إلى مجلد المستودع المفضل لديك.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. انتقل إلى مجلد `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. أنشئ بيئة افتراضية لبايثون.

    على ويندوز:

    ```powershell
    python -m venv .venv
    ```

    على macOS ولينكس:

    ```bash
    python3 -m venv .venv
    ```

1. فعّل البيئة الافتراضية لبايثون.

   على ويندوز:

   ```powershell
   .venv\Scripts\activate
   ```

   على macOS ولينكس:

   ```bash
   source .venv/bin/activate
   ```

1. ثبت المكتبات المطلوبة.

   على ويندوز:

   ```powershell
   pip install -r requirements.txt
   ```

   على macOS ولينكس:

   ```bash
   pip3 install -r requirements.txt
   ```

## تشغيل سكريبتات إعداد بيانات التفريغ النصي ليوتيوب

### على ويندوز

```powershell
.\transcripts_prepare.ps1
```

### على macOS ولينكس

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->