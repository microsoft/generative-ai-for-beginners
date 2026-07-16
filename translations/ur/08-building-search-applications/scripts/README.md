# نقل تحریر ڈیٹا کی تیاری

نقل تحریر کے ڈیٹا کی تیاری کے اسکرپٹس یوٹیوب ویڈیو کے نقل تحریر ڈاؤن لوڈ کرتے ہیں اور انہیں Semantic Search with OpenAI Embeddings and Functions کے نمونہ کے ساتھ استعمال کے لیے تیار کرتے ہیں۔

نقل تحریر کے ڈیٹا کی تیاری کے اسکرپٹس کو تازہ ترین ریلیزز Windows 11، macOS Ventura اور Ubuntu 22.04 (اور اس سے اوپر) پر آزمایا گیا ہے۔

## ضروری Azure OpenAI سروس کے وسائل بنائیں

> [!IMPORTANT]
> ہم تجویز کرتے ہیں کہ آپ Azure CLI کو جدید ترین ورژن میں اپ ڈیٹ کریں تاکہ OpenAI کے ساتھ مطابقت کو یقینی بنایا جا سکے
> دیکھیں [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ایک resource group بنائیں

> [!NOTE]
> ان ہدایات کے لیے ہم "semantic-video-search" نامی resource group استعمال کر رہے ہیں جو East US میں ہے۔
> آپ resource group کا نام تبدیل کر سکتے ہیں، لیکن جب وسائل کے لیے مقام تبدیل کریں، 
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) چیک کریں۔

```console
az group create --name semantic-video-search --location eastus
```

1. ایک Azure OpenAI Service resource بنائیں۔

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. اس ایپلیکیشن میں استعمال کے لیے endpoint اور keys حاصل کریں

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. درج ذیل ماڈلز کو ڈیپلائے کریں:
   - `text-embedding-ada-002` ورژن `2` یا اس سے زیادہ، نام `text-embedding-ada-002`
   - `gpt-4o-mini` نام `gpt-4o-mini`

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

## ضروری سافٹ ویئر

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) یا اس سے زیادہ

## ماحول کے تغیرات

یوٹیوب نقل تحریر ڈیٹا کی تیاری کے اسکرپٹس چلانے کے لیے درج ذیل ماحول متغیرات ضروری ہیں۔

### Windows پر

صارف کے ماحول متغیرات میں یہ متغیرات شامل کرنے کی سفارش کی جاتی ہے۔
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` برائے [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- آپ اپنے PowerShell پروفائل میں ماحول متغیرات بھی شامل کر سکتے ہیں۔

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux اور macOS پر

ان ایکسپورٹس کو اپنی `~/.bashrc` یا `~/.zshrc` فائل میں شامل کرنے کی سفارش کی جاتی ہے۔

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ضروری Python لائبریریاں انسٹال کریں

1. اگر git کلائنٹ انسٹال نہیں ہے تو اسے انسٹال کریں [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)۔
1. `Terminal` ونڈو سے، نمونہ کو اپنی پسند کی repository فولڈر میں کلون کریں۔

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` فولڈر میں جائیں۔

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python ورچوئل ماحول بنائیں۔

    Windows پر:

    ```powershell
    python -m venv .venv
    ```

    macOS اور Linux پر:

    ```bash
    python3 -m venv .venv
    ```

1. Python ورچوئل ماحول کو فعال کریں۔

   Windows پر:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS اور Linux پر:

   ```bash
   source .venv/bin/activate
   ```

1. ضروری لائبریریاں انسٹال کریں۔

   Windows پر:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS اور Linux پر:

   ```bash
   pip3 install -r requirements.txt
   ```

## یوٹیوب نقل تحریر ڈیٹا کی تیاری کے اسکرپٹس چلائیں

### Windows پر

```powershell
.\transcripts_prepare.ps1
```

### macOS اور Linux پر

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->