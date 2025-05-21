<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:48:46+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ne"
}
-->
# ट्रान्सक्रिप्शन डेटा तयारी

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरूले युट्युब भिडियो ट्रान्सक्रिप्टहरू डाउनलोड गर्छन् र तिनीहरूलाई सेमान्टिक सर्च विथ ओपनएआई एम्बेडिङ्स र फङ्सनहरू नमूनासँग प्रयोग गर्नका लागि तयार पार्छन्।

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरूले पछिल्लो संस्करणहरूमा परीक्षण गरिएका छन्: Windows 11, macOS Ventura र Ubuntu 22.04 (र माथि)।

## आवश्यक Azure OpenAI सेवा स्रोतहरू बनाउनुहोस्

> [!IMPORTANT]
> हामी सुझाव दिन्छौं कि तपाईंले OpenAI सँगको अनुकूलता सुनिश्चित गर्नको लागि Azure CLI लाई पछिल्लो संस्करणमा अद्यावधिक गर्नुहोस्
> [डकुमेन्टेशन](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) हेर्नुहोस्

1. एक स्रोत समूह बनाउनुहोस्

> [!NOTE]
> यी निर्देशनहरूका लागि हामी East US मा "semantic-video-search" नामको स्रोत समूह प्रयोग गर्दैछौं।
> तपाईं स्रोत समूहको नाम परिवर्तन गर्न सक्नुहुन्छ, तर स्रोतहरूको स्थान परिवर्तन गर्दा, 
> [मोडेल उपलब्धता तालिका](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) जाँच गर्नुहोस्।

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI सेवा स्रोत बनाउनुहोस्।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. यस अनुप्रयोगमा प्रयोगका लागि अन्तिम बिन्दु र कुञ्जीहरू प्राप्त गर्नुहोस्

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. निम्न मोडेलहरू तैनाथ गर्नुहोस्:
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

## आवश्यक सफ्टवेयर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) वा उच्च संस्करण

## वातावरणीय भेरिएबलहरू

YouTube ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरू चलाउन निम्न वातावरणीय भेरिएबलहरू आवश्यक छन्।

### Windows मा

तपाईंको `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` मा भेरिएबलहरू थप्न सिफारिस गरिन्छ।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux र macOS मा

तपाईंको `~/.bashrc` or `~/.zshrc` फाइलमा निम्न निर्यातहरू थप्न सिफारिस गरिन्छ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python पुस्तकालयहरू स्थापना गर्नुहोस्

1. [git क्लाइन्ट](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) स्थापना गर्नुहोस् यदि यो पहिले नै स्थापना गरिएको छैन भने।
1. `Terminal` विन्डोबाट, नमूनालाई तपाईंको मनपर्ने रिपो फोल्डरमा क्लोन गर्नुहोस्।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डरमा जानुहोस्।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python भर्चुअल वातावरण बनाउनुहोस्।

    Windows मा:

    ```powershell
    python -m venv .venv
    ```

    macOS र Linux मा:

    ```bash
    python3 -m venv .venv
    ```

1. Python भर्चुअल वातावरण सक्रिय गर्नुहोस्।

   Windows मा:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS र Linux मा:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक पुस्तकालयहरू स्थापना गर्नुहोस्।

   Windows मा:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS र Linux मा:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरू चलाउनुहोस्

### Windows मा

```powershell
.\transcripts_prepare.ps1
```

### macOS र Linux मा

```bash
./transcripts_prepare.sh
```

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। यसको मूल भाषा मा रहेको दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुनेछैनौं।