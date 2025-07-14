<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:07:03+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "fa"
}
-->
# آماده‌سازی داده‌های رونویسی

اسکریپت‌های آماده‌سازی داده‌های رونویسی، متن‌های ویدیوهای یوتیوب را دانلود کرده و برای استفاده در نمونه جستجوی معنایی با OpenAI Embeddings و Functions آماده می‌کنند.

این اسکریپت‌ها روی آخرین نسخه‌های ویندوز ۱۱، macOS Ventura و اوبونتو ۲۲.۰۴ (و بالاتر) تست شده‌اند.

## ایجاد منابع مورد نیاز سرویس Azure OpenAI

> [!IMPORTANT]
> پیشنهاد می‌کنیم Azure CLI را به آخرین نسخه به‌روزرسانی کنید تا از سازگاری با OpenAI اطمینان حاصل شود
> به [مستندات](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) مراجعه کنید

1. یک گروه منبع ایجاد کنید

> [!NOTE]
> در این دستورالعمل‌ها از گروه منبعی به نام "semantic-video-search" در منطقه East US استفاده می‌کنیم.
> می‌توانید نام گروه منبع را تغییر دهید، اما هنگام تغییر مکان منابع،
> جدول [دسترسی مدل‌ها](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) را بررسی کنید.

```console
az group create --name semantic-video-search --location eastus
```

1. یک منبع سرویس Azure OpenAI ایجاد کنید.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. نقطه پایان و کلیدهای لازم برای استفاده در این برنامه را دریافت کنید

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. مدل‌های زیر را مستقر کنید:
   - نسخه `2` یا بالاتر از `text-embedding-ada-002` با نام `text-embedding-ada-002`
   - نسخه `0613` یا بالاتر از `gpt-35-turbo` با نام `gpt-35-turbo`

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

## نرم‌افزارهای مورد نیاز

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) یا بالاتر

## متغیرهای محیطی

برای اجرای اسکریپت‌های آماده‌سازی داده‌های رونویسی یوتیوب، متغیرهای محیطی زیر لازم است.

### در ویندوز

توصیه می‌شود متغیرها را به متغیرهای محیطی `user` خود اضافه کنید.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` برای [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### در لینوکس و macOS

توصیه می‌شود موارد زیر را به فایل `~/.bashrc` یا `~/.zshrc` خود اضافه کنید.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## نصب کتابخانه‌های مورد نیاز پایتون

1. اگر کلاینت [git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) نصب نیست، آن را نصب کنید.
1. از پنجره `Terminal`، نمونه را در پوشه مخزن مورد نظر خود کلون کنید.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. به پوشه `data_prep` بروید.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. یک محیط مجازی پایتون بسازید.

    در ویندوز:

    ```powershell
    python -m venv .venv
    ```

    در macOS و لینوکس:

    ```bash
    python3 -m venv .venv
    ```

1. محیط مجازی پایتون را فعال کنید.

   در ویندوز:

   ```powershell
   .venv\Scripts\activate
   ```

   در macOS و لینوکس:

   ```bash
   source .venv/bin/activate
   ```

1. کتابخانه‌های مورد نیاز را نصب کنید.

   در ویندوز:

   ```powershell
   pip install -r requirements.txt
   ```

   در macOS و لینوکس:

   ```bash
   pip3 install -r requirements.txt
   ```

## اجرای اسکریپت‌های آماده‌سازی داده‌های رونویسی یوتیوب

### در ویندوز

```powershell
.\transcripts_prepare.ps1
```

### در macOS و لینوکس

```bash
./transcripts_prepare.sh
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.