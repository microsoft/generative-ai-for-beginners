<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:50:34+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "fa"
}
-->
# آماده‌سازی داده‌های رونویسی

اسکریپت‌های آماده‌سازی داده‌های رونویسی، رونویسی‌های ویدیوهای یوتیوب را دانلود کرده و آن‌ها را برای استفاده با نمونه جستجوی معنایی با تعبیه‌های OpenAI و توابع آماده می‌کنند.

اسکریپت‌های آماده‌سازی داده‌های رونویسی بر روی آخرین نسخه‌های ویندوز 11، macOS Ventura و اوبونتو 22.04 (و بالاتر) آزمایش شده‌اند.

## ایجاد منابع مورد نیاز سرویس Azure OpenAI

> [!IMPORTANT]
> پیشنهاد می‌کنیم Azure CLI را به آخرین نسخه به‌روزرسانی کنید تا سازگاری با OpenAI تضمین شود.
> به [مستندات](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) مراجعه کنید.

1. ایجاد یک گروه منابع

> [!NOTE]
> برای این دستورالعمل‌ها، ما از گروه منابعی با نام "semantic-video-search" در شرق ایالات متحده استفاده می‌کنیم.
> شما می‌توانید نام گروه منابع را تغییر دهید، اما هنگام تغییر مکان برای منابع، 
> جدول در دسترس بودن مدل را بررسی کنید. [جدول دسترس‌پذیری مدل](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. ایجاد یک منبع سرویس Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. دریافت نقطه پایانی و کلیدها برای استفاده در این برنامه

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. استقرار مدل‌های زیر:
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

## نرم‌افزار مورد نیاز

- [پایتون 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) یا بالاتر

## متغیرهای محیطی

متغیرهای محیطی زیر برای اجرای اسکریپت‌های آماده‌سازی داده‌های رونویسی یوتیوب لازم هستند.

### در ویندوز

توصیه می‌شود متغیرها را به `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` خود اضافه کنید.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### در لینوکس و macOS

توصیه می‌شود که صادرات زیر را به فایل `~/.bashrc` or `~/.zshrc` خود اضافه کنید.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## نصب کتابخانه‌های پایتون مورد نیاز

1. اگر کلاینت [git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) نصب نشده است، آن را نصب کنید.
1. از یک پنجره `ترمینال`، نمونه را به پوشه مخزن دلخواه خود کلون کنید.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. به پوشه `data_prep` بروید.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. یک محیط مجازی پایتون ایجاد کنید.

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
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.