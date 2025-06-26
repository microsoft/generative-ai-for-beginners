<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:52:30+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hi"
}
-->
# ट्रांसक्रिप्शन डेटा तैयारी

ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स YouTube वीडियो ट्रांसक्रिप्ट्स डाउनलोड करती हैं और उन्हें ओपनएआई एम्बेडिंग्स और फंक्शन्स के साथ सेमांटिक सर्च के नमूने के लिए उपयोग के लिए तैयार करती हैं।

ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स का परीक्षण नवीनतम रिलीज़ विंडोज 11, मैकओएस वेंचुरा और उबंटू 22.04 (और ऊपर) पर किया गया है।

## आवश्यक Azure OpenAI सेवा संसाधन बनाएं

> [!IMPORTANT]
> हम सुझाव देते हैं कि आप OpenAI के साथ संगतता सुनिश्चित करने के लिए Azure CLI को नवीनतम संस्करण में अपडेट करें
> देखें [प्रलेखन](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एक संसाधन समूह बनाएं

> [!NOTE]
> इन निर्देशों के लिए हम पूर्वी यूएस में "semantic-video-search" नामक संसाधन समूह का उपयोग कर रहे हैं।
> आप संसाधन समूह का नाम बदल सकते हैं, लेकिन संसाधनों के लिए स्थान बदलते समय, 
> [मॉडल उपलब्धता तालिका](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) की जाँच करें।

```console
az group create --name semantic-video-search --location eastus
```

1. एक Azure OpenAI सेवा संसाधन बनाएं।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. इस एप्लिकेशन में उपयोग के लिए एंडपॉइंट और कुंजियाँ प्राप्त करें

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. निम्नलिखित मॉडलों को परिनियोजित करें:
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

## आवश्यक सॉफ़्टवेयर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) या उससे अधिक

## पर्यावरणीय चर

YouTube ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स चलाने के लिए निम्नलिखित पर्यावरणीय चर आवश्यक हैं।

### विंडोज पर

सुझाव है कि इन चर को अपने `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` में जोड़ें।

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### लिनक्स और मैकओएस पर

सुझाव है कि निम्नलिखित एक्सपोर्ट्स को अपने `~/.bashrc` or `~/.zshrc` फ़ाइल में जोड़ें।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python पुस्तकालय स्थापित करें

1. [git क्लाइंट](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) स्थापित करें यदि यह पहले से स्थापित नहीं है।
1. `टर्मिनल` विंडो से, नमूने को अपनी पसंदीदा रिपो फ़ोल्डर में क्लोन करें।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फ़ोल्डर पर जाएं।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. एक Python वर्चुअल एनवायरनमेंट बनाएं।

    विंडोज पर:

    ```powershell
    python -m venv .venv
    ```

    मैकओएस और लिनक्स पर:

    ```bash
    python3 -m venv .venv
    ```

1. Python वर्चुअल एनवायरनमेंट को सक्रिय करें।

   विंडोज पर:

   ```powershell
   .venv\Scripts\activate
   ```

   मैकओएस और लिनक्स पर:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक पुस्तकालय स्थापित करें।

   विंडोज पर:

   ```powershell
   pip install -r requirements.txt
   ```

   मैकओएस और लिनक्स पर:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स चलाएं

### विंडोज पर

```powershell
.\transcripts_prepare.ps1
```

### मैकओएस और लिनक्स पर

```bash
./transcripts_prepare.sh
```

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। इसकी मूल भाषा में मूल दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।