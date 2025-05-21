<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:47:02+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ur"
}
-->
# ٹرانسکرپشن ڈیٹا کی تیاری

ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس یوٹیوب ویڈیو ٹرانسکرپٹس کو ڈاؤنلوڈ کرتے ہیں اور انہیں سیمینٹک سرچ کے ساتھ اوپن اے آئی ایمبیڈنگز اور فنکشنز کے نمونے کے استعمال کے لیے تیار کرتے ہیں۔

ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس کو ونڈوز 11، میک او ایس وینٹورا اور اوبنٹو 22.04 (اور اس سے اوپر) کے تازہ ترین ریلیز پر آزمایا گیا ہے۔

## مطلوبہ Azure OpenAI سروس وسائل بنائیں

> [!IMPORTANT]
> ہم تجویز کرتے ہیں کہ آپ Azure CLI کو تازہ ترین ورژن پر اپ ڈیٹ کریں تاکہ OpenAI کے ساتھ مطابقت کو یقینی بنایا جا سکے۔
> [دستاویزات](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) دیکھیں۔

1. ایک وسائل گروپ بنائیں

> [!NOTE]
> ان ہدایات کے لیے ہم مشرقی امریکہ میں "semantic-video-search" نامی وسائل گروپ استعمال کر رہے ہیں۔
> آپ وسائل گروپ کا نام تبدیل کر سکتے ہیں، لیکن جب وسائل کے لیے مقام تبدیل کر رہے ہوں، 
> تو [ماڈل کی دستیابی کی جدول](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) چیک کریں۔

```console
az group create --name semantic-video-search --location eastus
```

1. ایک Azure OpenAI سروس وسائل بنائیں۔

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. اس ایپلیکیشن میں استعمال کے لیے اینڈ پوائنٹ اور چابیاں حاصل کریں

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. درج ذیل ماڈلز کو ڈیپلوئے کریں:
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

## مطلوبہ سافٹ ویئر

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) یا اس سے زیادہ

## ماحول کے متغیرات

یوٹیوب ٹرانسکرپشن ڈیٹا کی تیاری کے اسکرپٹس کو چلانے کے لیے درج ذیل ماحول کے متغیرات کی ضرورت ہے۔

### ونڈوز پر

متغیرات کو اپنے `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` میں شامل کرنے کی سفارش کریں۔

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### لینکس اور میک او ایس پر

آپ کے `~/.bashrc` or `~/.zshrc` فائل میں درج ذیل ایکسپورٹس شامل کرنے کی سفارش کریں۔

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## مطلوبہ Python لائبریریاں انسٹال کریں

1. اگر یہ پہلے سے انسٹال نہیں ہے تو [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) انسٹال کریں۔
1. `Terminal` ونڈو سے، نمونہ کو اپنے پسندیدہ ریپو فولڈر میں کلون کریں۔

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` فولڈر پر جائیں۔

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. ایک Python ورچوئل ماحول بنائیں۔

    ونڈوز پر:

    ```powershell
    python -m venv .venv
    ```

    میک او ایس اور لینکس پر:

    ```bash
    python3 -m venv .venv
    ```

1. Python ورچوئل ماحول کو فعال کریں۔

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

**دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں معتبر ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔