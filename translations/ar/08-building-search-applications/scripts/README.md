# تحضير بيانات النسخ

تقوم سكربتات تحضير بيانات النسخ بتنزيل نصوص فيديوهات يوتيوب وتحضيرها للاستخدام مع نموذج البحث الدلالي باستخدام تضمينات OpenAI والوظائف.

تم اختبار سكربتات تحضير بيانات النسخ على أحدث إصدارات Windows 11 وmacOS Ventura وUbuntu 22.04 (وما فوق).

## إنشاء موارد خدمة Azure OpenAI المطلوبة

> [!IMPORTANT]
> نقترح عليك تحديث Azure CLI إلى أحدث إصدار لضمان التوافق مع OpenAI
> انظر [التوثيق](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

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
   - `text-embedding-ada-002` الإصدار `2` أو أعلى، المسمى `text-embedding-ada-002`
   - `gpt-4o-mini` المسمى `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## البرامج المطلوبة

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) أو أعلى

## متغيرات البيئة

متغيرات البيئة التالية مطلوبة لتشغيل سكربتات تحضير بيانات النسخ من YouTube.

### على ويندوز

يُنصح بإضافة المتغيرات إلى متغيرات بيئة `user`.
`قائمة ابدأ في ويندوز` > `تحرير متغيرات بيئة النظام` > `متغيرات البيئة` > `متغيرات المستخدم` لـ [USER] > `جديد`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- يمكنك إضافة متغيرات البيئة إلى ملف تعريف PowerShell الخاص بك.

```powershell
$env:AZURE_OPENAI_API_KEY = "<مفتاح API الخاص بخدمة Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<نقطة نهاية خدمة Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<اسم نشر نموذج خدمة Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<مفتاح API لمطور Google الخاص بك>"
``` -->

### على لينكس وmacOS

يُنصح بإضافة الصادرات التالية إلى ملف `~/.bashrc` أو `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## تثبيت مكتبات Python المطلوبة

1. قم بتثبيت [عميل git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) إذا لم يكن مثبتًا بالفعل.
1. من نافذة `Terminal`، انسخ النموذج إلى مجلد المستودع المفضل لديك.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. انتقل إلى مجلد `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. أنشئ بيئة Python افتراضية.

    على ويندوز:

    ```powershell
    python -m venv .venv
    ```

    على macOS وLinux:

    ```bash
    python3 -m venv .venv
    ```

1. فعّل بيئة Python الافتراضية.

   على ويندوز:

   ```powershell
   .venv\Scripts\activate
   ```

   على macOS وLinux:

   ```bash
   source .venv/bin/activate
   ```

1. ثبّت المكتبات المطلوبة.

   على ويندوز:

   ```powershell
   pip install -r requirements.txt
   ```

   على macOS وLinux:

   ```bash
   pip3 install -r requirements.txt
   ```

## تشغيل سكربتات تحضير بيانات نسخ YouTube

### على ويندوز

```powershell
.\transcripts_prepare.ps1
```

### على macOS وLinux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->