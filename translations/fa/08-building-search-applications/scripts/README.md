# آماده‌سازی داده‌های رونوشت

اسکریپت‌های آماده‌سازی داده‌های رونوشت ویدیوهای YouTube را دانلود کرده و برای استفاده با نمونه جستجوی معنایی با OpenAI Embeddings و توابع آماده می‌کنند.

اسکریپت‌های آماده‌سازی داده‌های رونوشت بر روی نسخه‌های جدید Windows 11، macOS Ventura و Ubuntu 22.04 (و بالاتر) آزمایش شده‌اند.

## ساخت منابع لازم برای سرویس Azure OpenAI

> [!IMPORTANT]
> پیشنهاد می‌کنیم Azure CLI را به آخرین نسخه به‌روزرسانی کنید تا با OpenAI سازگاری داشته باشد.
> مراجعه کنید به [مستندات](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ساخت یک گروه منبع

> [!NOTE]
> در این دستورالعمل‌ها از گروه منبعی به نام "semantic-video-search" در East US استفاده می‌کنیم.
> شما می‌توانید نام گروه منبع را تغییر دهید، اما هنگام تغییر مکان منابع، 
> جدول [در دسترس بودن مدل](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) را بررسی کنید.

```console
az group create --name semantic-video-search --location eastus
```

1. ساخت یک منبع سرویس Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. دریافت نقطه پایان و کلیدها برای استفاده در این برنامه

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. پیاده‌سازی مدل‌های زیر:
   - نسخه `2` یا بالاتر از `text-embedding-ada-002` با نام `text-embedding-ada-002`
   - مدل `gpt-4o-mini` با نام `gpt-4o-mini`

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

## نرم‌افزارهای مورد نیاز

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) یا بالاتر

## متغیرهای محیطی

متغیرهای محیطی زیر برای اجرای اسکریپت‌های آماده‌سازی داده‌های رونوشت YouTube مورد نیاز است.

### در ویندوز

پیشنهاد می‌شود متغیرها را به متغیرهای محیطی `user` خود اضافه کنید.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` برای [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- می‌توانید متغیرهای محیطی را به پروفایل PowerShell خود اضافه کنید.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### در لینوکس و macOS

پیشنهاد می‌شود اکسپورت‌های زیر را به فایل `~/.bashrc` یا `~/.zshrc` خود اضافه کنید.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## نصب کتابخانه‌های پایتون مورد نیاز

1. اگر نصب نیست، [کلاینت git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) را نصب کنید.
1. از پنجره `Terminal` نمونه را به پوشه ریپوی دلخواه خود کلون کنید.

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

## اجرای اسکریپت‌های آماده‌سازی داده‌های رونوشت یوتیوب

### در ویندوز

```powershell
.\transcripts_prepare.ps1
```

### در macOS و لینوکس

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->