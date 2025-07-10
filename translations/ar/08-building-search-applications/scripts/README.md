<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:06:54+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ar"
}
-->
# تحضير بيانات النسخ

تقوم سكريبتات تحضير بيانات النسخ بتنزيل نصوص فيديوهات YouTube وتجهيزها للاستخدام مع نموذج البحث الدلالي باستخدام OpenAI Embeddings والوظائف.

تم اختبار سكريبتات تحضير بيانات النسخ على أحدث إصدارات Windows 11 وmacOS Ventura وUbuntu 22.04 (وأعلى).

## إنشاء الموارد المطلوبة لخدمة Azure OpenAI

> [!IMPORTANT]
> ننصح بتحديث Azure CLI إلى أحدث إصدار لضمان التوافق مع OpenAI
> راجع [التوثيق](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. إنشاء مجموعة موارد

> [!NOTE]
> في هذه التعليمات نستخدم مجموعة الموارد المسماة "semantic-video-search" في منطقة East US.
> يمكنك تغيير اسم مجموعة الموارد، ولكن عند تغيير موقع الموارد،
> تحقق من [جدول توفر النماذج](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. إنشاء مورد لخدمة Azure OpenAI.

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
   - `text-embedding-ada-002` إصدار `2` أو أعلى، باسم `text-embedding-ada-002`
   - `gpt-35-turbo` إصدار `0613` أو أعلى، باسم `gpt-35-turbo`

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
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## البرامج المطلوبة

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) أو أحدث

## متغيرات البيئة

المتغيرات البيئية التالية مطلوبة لتشغيل سكريبتات تحضير بيانات نسخ YouTube.

### على ويندوز

ننصح بإضافة المتغيرات إلى متغيرات بيئة `user`.
`ابدأ ويندوز` > `تحرير متغيرات بيئة النظام` > `متغيرات البيئة` > `متغيرات المستخدم` لـ [USER] > `جديد`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### على لينكس وmacOS

ننصح بإضافة الصادرات التالية إلى ملف `~/.bashrc` أو `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## تثبيت مكتبات Python المطلوبة

1. قم بتثبيت [عميل git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) إذا لم يكن مثبتًا بالفعل.
1. من نافذة `Terminal`، انسخ العينة إلى مجلد المستودع المفضل لديك.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. انتقل إلى مجلد `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. أنشئ بيئة افتراضية لـ Python.

    على ويندوز:

    ```powershell
    python -m venv .venv
    ```

    على macOS ولينكس:

    ```bash
    python3 -m venv .venv
    ```

1. فعّل البيئة الافتراضية لـ Python.

   على ويندوز:

   ```powershell
   .venv\Scripts\activate
   ```

   على macOS ولينكس:

   ```bash
   source .venv/bin/activate
   ```

1. ثبّت المكتبات المطلوبة.

   على ويندوز:

   ```powershell
   pip install -r requirements.txt
   ```

   على macOS ولينكس:

   ```bash
   pip3 install -r requirements.txt
   ```

## تشغيل سكريبتات تحضير بيانات نسخ YouTube

### على ويندوز

```powershell
.\transcripts_prepare.ps1
```

### على macOS ولينكس

```bash
./transcripts_prepare.sh
```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.