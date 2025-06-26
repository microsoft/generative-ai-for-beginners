<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:50:50+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ur"
}
-->
# نقل ڈیٹا کی تیاری

نقل ڈیٹا کی تیاری کے اسکرپٹس یوٹیوب ویڈیو نقل کو ڈاؤن لوڈ کرتے ہیں اور انہیں سیمینٹک سرچ ود اوپن اے آئی ایمبیڈنگز اور فنکشنز نمونے کے ساتھ استعمال کے لیے تیار کرتے ہیں۔

نقل ڈیٹا کی تیاری کے اسکرپٹس کو تازہ ترین ریلیزز ونڈوز 11، میک او ایس وینچورا اور اوبنٹو 22.04 (اور اس سے اوپر) پر جانچا گیا ہے۔

## ضروری Azure OpenAI سروس وسائل بنائیں

> [!IMPORTANT]
> ہم تجویز کرتے ہیں کہ آپ Azure CLI کو تازہ ترین ورژن میں اپ ڈیٹ کریں تاکہ OpenAI کے ساتھ مطابقت کو یقینی بنایا جا سکے
> [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) دیکھیں

1. ایک وسائل گروپ بنائیں

> [!NOTE]
> ان ہدایات کے لیے ہم مشرقی امریکہ میں "semantic-video-search" نامی وسائل گروپ استعمال کر رہے ہیں۔
> آپ وسائل گروپ کا نام تبدیل کر سکتے ہیں، لیکن جب وسائل کے مقام کو تبدیل کر رہے ہوں تو،
> [ماڈل دستیابی کا جدول](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) چیک کریں۔

```console
az group create --name semantic-video-search --location eastus
```

1. ایک Azure OpenAI سروس وسیلہ بنائیں۔

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. اس درخواست میں استعمال کے لیے اینڈ پوائنٹ اور چابیاں حاصل کریں

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. مندرجہ ذیل ماڈل تعینات کریں:
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

یوٹیوب نقل ڈیٹا کی تیاری کے اسکرپٹس چلانے کے لیے مندرجہ ذیل ماحول کے متغیرات کی ضرورت ہے۔

### ونڈوز پر

تجویز ہے کہ متغیرات کو آپ کے `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` میں شامل کریں۔

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### لینکس اور میک او ایس پر

تجویز ہے کہ مندرجہ ذیل ایکسپورٹس کو اپنے `~/.bashrc` or `~/.zshrc` فائل میں شامل کریں۔

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## مطلوبہ Python لائبریریاں انسٹال کریں

1. اگر پہلے سے انسٹال نہیں ہے تو [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) انسٹال کریں۔
1. ایک `Terminal` ونڈو سے، نمونے کو اپنے پسندیدہ ریپو فولڈر میں کلون کریں۔

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

## یوٹیوب نقل ڈیٹا کی تیاری کے اسکرپٹس چلائیں

### ونڈوز پر

```powershell
.\transcripts_prepare.ps1
```

### میک او ایس اور لینکس پر

```bash
./transcripts_prepare.sh
```

**دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غلطیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں معتبر ماخذ سمجھا جانا چاہئے۔ اہم معلومات کے لئے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔