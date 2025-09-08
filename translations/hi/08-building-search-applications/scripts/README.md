<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:08:21+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hi"
}
-->
# ट्रांसक्रिप्शन डेटा तैयारी

ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स YouTube वीडियो ट्रांसक्रिप्ट डाउनलोड करती हैं और उन्हें Semantic Search with OpenAI Embeddings and Functions नमूने के लिए तैयार करती हैं।

ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स को नवीनतम रिलीज़ Windows 11, macOS Ventura और Ubuntu 22.04 (और उससे ऊपर) पर परीक्षण किया गया है।

## आवश्यक Azure OpenAI Service संसाधन बनाएं

> [!IMPORTANT]
> हम सुझाव देते हैं कि आप Azure CLI को नवीनतम संस्करण में अपडेट करें ताकि OpenAI के साथ संगतता सुनिश्चित हो सके
> देखें [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एक resource group बनाएं

> [!NOTE]
> इन निर्देशों के लिए हम East US में "semantic-video-search" नामक resource group का उपयोग कर रहे हैं।
> आप resource group का नाम बदल सकते हैं, लेकिन जब संसाधनों के लिए स्थान बदलें, 
> तो [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) जांचें।

```console
az group create --name semantic-video-search --location eastus
```

1. एक Azure OpenAI Service resource बनाएं।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. इस एप्लिकेशन में उपयोग के लिए endpoint और keys प्राप्त करें

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. निम्नलिखित मॉडल तैनात करें:
   - `text-embedding-ada-002` संस्करण `2` या उससे ऊपर, नामित `text-embedding-ada-002`
   - `gpt-35-turbo` संस्करण `0613` या उससे ऊपर, नामित `gpt-35-turbo`

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

## आवश्यक सॉफ़्टवेयर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) या उससे ऊपर

## पर्यावरण चर

YouTube ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स चलाने के लिए निम्नलिखित पर्यावरण चर आवश्यक हैं।

### Windows पर

सुझाव है कि आप इन चर को अपने `user` पर्यावरण चर में जोड़ें।  
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux और macOS पर

सुझाव है कि आप निम्नलिखित exports को अपने `~/.bashrc` या `~/.zshrc` फ़ाइल में जोड़ें।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python लाइब्रेरी इंस्टॉल करें

1. यदि git client पहले से इंस्टॉल नहीं है तो [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) इंस्टॉल करें।  
1. एक `Terminal` विंडो से, नमूना को अपनी पसंदीदा repo फ़ोल्डर में clone करें।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फ़ोल्डर में जाएं।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. एक Python वर्चुअल एनवायरनमेंट बनाएं।

    Windows पर:

    ```powershell
    python -m venv .venv
    ```

    macOS और Linux पर:

    ```bash
    python3 -m venv .venv
    ```

1. Python वर्चुअल एनवायरनमेंट सक्रिय करें।

   Windows पर:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS और Linux पर:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक लाइब्रेरी इंस्टॉल करें।

   Windows पर:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS और Linux पर:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स चलाएं

### Windows पर

```powershell
.\transcripts_prepare.ps1
```

### macOS और Linux पर

```bash
./transcripts_prepare.sh
```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।