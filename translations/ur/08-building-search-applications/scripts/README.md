<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:07:13+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ur"
}
-->
# ٹرانسکرپشن ڈیٹا کی تیاری

ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس یوٹیوب ویڈیو کے ٹرانسکرپٹس ڈاؤن لوڈ کرتے ہیں اور انہیں Semantic Search with OpenAI Embeddings and Functions کے نمونے کے ساتھ استعمال کے لیے تیار کرتے ہیں۔

ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس کو تازہ ترین ریلیزز Windows 11، macOS Ventura اور Ubuntu 22.04 (اور اس سے اوپر) پر آزمایا گیا ہے۔

## مطلوبہ Azure OpenAI سروس کے وسائل بنائیں

> [!IMPORTANT]
> ہم تجویز کرتے ہیں کہ آپ Azure CLI کو تازہ ترین ورژن میں اپ ڈیٹ کریں تاکہ OpenAI کے ساتھ مطابقت یقینی بنائی جا سکے
> دیکھیں [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. ایک resource group بنائیں

> [!NOTE]
> ان ہدایات کے لیے ہم "semantic-video-search" نامی resource group استعمال کر رہے ہیں جو East US میں ہے۔
> آپ resource group کا نام تبدیل کر سکتے ہیں، لیکن جب وسائل کی جگہ تبدیل کریں، 
> تو [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) چیک کریں۔

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

1. درج ذیل ماڈلز کو تعینات کریں:
   - `text-embedding-ada-002` ورژن `2` یا اس سے زیادہ، جس کا نام `text-embedding-ada-002` ہو
   - `gpt-35-turbo` ورژن `0613` یا اس سے زیادہ، جس کا نام `gpt-35-turbo` ہو

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

## مطلوبہ سافٹ ویئر

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) یا اس سے زیادہ

## ماحول کے متغیرات

یوٹیوب ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس چلانے کے لیے درج ذیل ماحول کے متغیرات ضروری ہیں۔

### ونڈوز پر

تجویز ہے کہ آپ متغیرات کو اپنے `user` ماحول کے متغیرات میں شامل کریں۔
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] کے لیے `User variables` > `New`۔

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### لینکس اور میک او ایس پر

تجویز ہے کہ درج ذیل exports کو اپنے `~/.bashrc` یا `~/.zshrc` فائل میں شامل کریں۔

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## مطلوبہ Python لائبریریاں انسٹال کریں

1. اگر پہلے سے انسٹال نہیں ہے تو [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) انسٹال کریں۔
1. `Terminal` ونڈو سے، نمونہ کو اپنی پسندیدہ repo فولڈر میں clone کریں۔

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` فولڈر میں جائیں۔

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python کا virtual environment بنائیں۔

    ونڈوز پر:

    ```powershell
    python -m venv .venv
    ```

    میک او ایس اور لینکس پر:

    ```bash
    python3 -m venv .venv
    ```

1. Python virtual environment کو فعال کریں۔

   ونڈوز پر:

   ```powershell
   .venv\Scripts\activate
   ```

   میک او ایس اور لینکس پر:

   ```bash
   source .venv/bin/activate
   ```

1. مطلوبہ لائبریریاں انسٹال کریں۔

   ونڈوز پر:

   ```powershell
   pip install -r requirements.txt
   ```

   میک او ایس اور لینکس پر:

   ```bash
   pip3 install -r requirements.txt
   ```

## یوٹیوب ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس چلائیں

### ونڈوز پر

```powershell
.\transcripts_prepare.ps1
```

### میک او ایس اور لینکس پر

```bash
./transcripts_prepare.sh
```

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔