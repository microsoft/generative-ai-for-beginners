<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:08:52+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ne"
}
-->
# ट्रान्सक्रिप्शन डाटा तयारी

ट्रान्सक्रिप्शन डाटा तयारी स्क्रिप्टहरूले YouTube भिडियो ट्रान्सक्रिप्टहरू डाउनलोड गरी Semantic Search with OpenAI Embeddings and Functions नमूनासँग प्रयोगका लागि तयार पार्छन्।

ट्रान्सक्रिप्शन डाटा तयारी स्क्रिप्टहरूलाई Windows 11, macOS Ventura र Ubuntu 22.04 (र माथि) को नयाँ संस्करणहरूमा परीक्षण गरिएको छ।

## आवश्यक Azure OpenAI सेवा स्रोतहरू सिर्जना गर्नुहोस्

> [!IMPORTANT]
> हामी तपाईंलाई Azure CLI लाई सबैभन्दा नयाँ संस्करणमा अपडेट गर्न सल्लाह दिन्छौं ताकि OpenAI सँगको अनुकूलता सुनिश्चित होस्
> हेर्नुहोस् [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एउटा resource group सिर्जना गर्नुहोस्

> [!NOTE]
> यी निर्देशनहरूका लागि हामीले East US मा "semantic-video-search" नामक resource group प्रयोग गर्दैछौं।
> तपाईं resource group को नाम परिवर्तन गर्न सक्नुहुन्छ, तर स्रोतहरूको स्थान परिवर्तन गर्दा,
> कृपया [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) जाँच गर्नुहोस्।

```console
az group create --name semantic-video-search --location eastus
```

1. एउटा Azure OpenAI सेवा स्रोत सिर्जना गर्नुहोस्।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. यस एप्लिकेसनमा प्रयोगका लागि endpoint र keys प्राप्त गर्नुहोस्

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. तलका मोडेलहरू डिप्लोय गर्नुहोस्:
   - `text-embedding-ada-002` संस्करण `2` वा माथि, नाम `text-embedding-ada-002`
   - `gpt-35-turbo` संस्करण `0613` वा माथि, नाम `gpt-35-turbo`

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

## आवश्यक सफ्टवेयर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) वा माथि

## वातावरण चरहरू

YouTube ट्रान्सक्रिप्शन डाटा तयारी स्क्रिप्टहरू चलाउन तलका वातावरण चरहरू आवश्यक छन्।

### Windows मा

तपाईंको `user` वातावरण चरहरूमा यी चरहरू थप्न सिफारिस गरिन्छ।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] को लागि `User variables` > `New`।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux र macOS मा

तपाईंको `~/.bashrc` वा `~/.zshrc` फाइलमा तलका exports थप्न सिफारिस गरिन्छ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python लाइब्रेरीहरू स्थापना गर्नुहोस्

1. यदि git client पहिलेबाट स्थापना गरिएको छैन भने, [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) स्थापना गर्नुहोस्।
1. `Terminal` विन्डोबाट, नमूनालाई तपाईंको मनपर्ने repo फोल्डरमा क्लोन गर्नुहोस्।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डरमा जानुहोस्।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python virtual environment सिर्जना गर्नुहोस्।

    Windows मा:

    ```powershell
    python -m venv .venv
    ```

    macOS र Linux मा:

    ```bash
    python3 -m venv .venv
    ```

1. Python virtual environment सक्रिय गर्नुहोस्।

   Windows मा:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS र Linux मा:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक लाइब्रेरीहरू स्थापना गर्नुहोस्।

   Windows मा:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS र Linux मा:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रान्सक्रिप्शन डाटा तयारी स्क्रिप्टहरू चलाउनुहोस्

### Windows मा

```powershell
.\transcripts_prepare.ps1
```

### macOS र Linux मा

```bash
./transcripts_prepare.sh
```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।