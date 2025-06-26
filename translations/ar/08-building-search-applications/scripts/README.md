<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:50:23+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ar"
}
-->
# إعداد بيانات النسخ

تقوم سكربتات إعداد بيانات النسخ بتنزيل نصوص فيديوهات يوتيوب وتجهيزها للاستخدام مع البحث الدلالي باستخدام تضمينات ووظائف OpenAI.

تم اختبار سكربتات إعداد بيانات النسخ على أحدث الإصدارات من Windows 11 وmacOS Ventura وUbuntu 22.04 (وما فوقها).

## إنشاء الموارد المطلوبة لخدمة Azure OpenAI

> [!IMPORTANT]
> نقترح تحديث Azure CLI إلى أحدث إصدار لضمان التوافق مع OpenAI.
> انظر [التوثيق](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst).

1. إنشاء مجموعة موارد

> [!NOTE]
> لهذه التعليمات، نستخدم مجموعة الموارد المسماة "semantic-video-search" في شرق الولايات المتحدة.
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

1. الحصول على النقطة النهائية والمفاتيح لاستخدامها في هذا التطبيق.

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. نشر النماذج التالية:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) أو أعلى

## متغيرات البيئة

المتغيرات البيئية التالية مطلوبة لتشغيل سكربتات إعداد بيانات نسخ يوتيوب.

### على Windows

يوصى بإضافة المتغيرات إلى `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### على Linux وmacOS

يوصى بإضافة الصادرات التالية إلى ملف `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## تثبيت مكتبات بايثون المطلوبة

1. تثبيت [عميل git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) إذا لم يكن مثبتًا بالفعل.
1. من نافذة `Terminal`، قم باستنساخ العينة إلى مجلد الريبو المفضل لديك.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. انتقل إلى مجلد `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. إنشاء بيئة افتراضية لبايثون.

    على Windows:

    ```powershell
    python -m venv .venv
    ```

    على macOS وLinux:

    ```bash
    python3 -m venv .venv
    ```

1. تفعيل البيئة الافتراضية لبايثون.

   على Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   على macOS وLinux:

   ```bash
   source .venv/bin/activate
   ```

1. تثبيت المكتبات المطلوبة.

   على Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   على macOS وLinux:

   ```bash
   pip3 install -r requirements.txt
   ```

## تشغيل سكربتات إعداد بيانات نسخ يوتيوب

### على Windows

```powershell
.\transcripts_prepare.ps1
```

### على macOS وLinux

```bash
./transcripts_prepare.sh
```

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأم المصدر الموثوق. بالنسبة للمعلومات الحرجة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.