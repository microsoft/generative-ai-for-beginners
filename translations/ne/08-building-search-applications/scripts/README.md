# ट्रान्सक्रिप्शन डेटा तयारी

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरूले YouTube भिडियो ट्रान्सक्रिप्टहरू डाउनलोड गरी उनीहरूलाई Semantic Search with OpenAI Embeddings and Functions नमूनासँग प्रयोगको लागि तयार गर्छन्।

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरूलाई नवीनतम रिलिज Windows 11, macOS Ventura र Ubuntu 22.04 (वा माथि) मा परीक्षण गरिएको छ।

## आवश्यक Azure OpenAI सेवा स्रोतहरू सिर्जना गर्नुहोस्

> [!IMPORTANT]
> हामी तपाईंलाई Azure CLI लाई OpenAI सँगको अनुकूलताका लागि नवीनतम संस्करणमा अपडेट गर्न सल्लाह दिन्छौं
> हेर्नुहोस् [डोकुमेन्टेसन](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एउटा स्रोत समूह सिर्जना गर्नुहोस्

> [!NOTE]
> यी निर्देशनहरूका लागि हामीले "semantic-video-search" भन्ने स्रोत समूह East US मा प्रयोग गर्दैछौं।
> तपाईं स्रोत समूहको नाम परिवर्तन गर्न सक्नुहुन्छ, तर स्रोतहरूको स्थान परिवर्तन गर्दा,
> [स्रोत उपलब्धता तालिका](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) जाँच गर्नुहोस्।

```console
az group create --name semantic-video-search --location eastus
```

1. एउटा Azure OpenAI सेवा स्रोत सिर्जना गर्नुहोस्।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. यस अनुप्रयोगमा प्रयोगका लागि अन्त बिन्दु र कुञ्जीहरू प्राप्त गर्नुहोस्

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. तलका मोडेलहरू तैनाथ गर्नुहोस्:
   - `text-embedding-ada-002` संस्करण `2` वा माथि, नाम गरिएको `text-embedding-ada-002`
   - `gpt-5-mini` नाम गरिएको `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## आवश्यक सफ्टवेयर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) वा माथि

## वातावरण चरहरू

YouTube ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्टहरू चलाउनका लागि तलका वातावरण चरहरू आवश्यक छन्।

### Windows मा

तपाईंका `user` वातावरण चरहरूमा ती चरहरू थप्न सिफारिस गरिन्छ।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` को लागि [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- तपाईं यी वातावरण चरहरूलाई आफ्नो PowerShell प्रोफाइलमा पनि थप्न सक्नुहुन्छ।

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux र macOS मा

तपाईंका `~/.bashrc` वा `~/.zshrc` फाइलमा तलका एक्सपोर्टहरू थप्न सिफारिस गरिन्छ।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python पुस्तकालयहरू स्थापना गर्नुहोस्

1. यदि git क्लाइन्ट पहिले स्थापना भएको छैन भने, [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) स्थापना गर्नुहोस्।
1. `Terminal` विन्डोबाट नमूनालाई तपाईंको इच्छित रिपो फोल्डरमा क्लोन गर्नुहोस्।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डरमा जानुहोस्।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python भर्चुअल वातावरण सिर्जना गर्नुहोस्।

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->