# ट्रांसक्रिप्शन डेटा तैयारी

ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट YouTube वीडियो ट्रांसक्रिप्ट डाउनलोड करती हैं और उन्हें Semantic Search with OpenAI Embeddings and Functions नमूने के उपयोग के लिए तैयार करती हैं।

ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स को नवीनतम रिलीज़ Windows 11, macOS Ventura और Ubuntu 22.04 (और उससे ऊपर) पर परीक्षण किया गया है।

## आवश्यक Azure OpenAI सेवा संसाधन बनाएँ

> [!IMPORTANT]
> हम सुझाव देते हैं कि आप OpenAI के साथ संगतता सुनिश्चित करने के लिए Azure CLI को नवीनतम संस्करण में अपडेट करें
> देखें [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एक संसाधन समूह बनाएँ

> [!NOTE]
> इन निर्देशों के लिए हम East US में "semantic-video-search" नामक संसाधन समूह का उपयोग कर रहे हैं।
> आप संसाधन समूह का नाम बदल सकते हैं, लेकिन जब संसाधनों के स्थान को बदलते हैं,
> [मॉडल उपलब्धता तालिका](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) जांचें।

```console
az group create --name semantic-video-search --location eastus
```

1. एक Azure OpenAI सेवा संसाधन बनाएँ।

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. इस एप्लिकेशन में उपयोग के लिए एंडपॉइंट और कुंजी प्राप्त करें

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. निम्नलिखित मॉडल तैनात करें:
   - `text-embedding-ada-002` संस्करण `2` या उससे ऊपर, नामित `text-embedding-ada-002`
   - `gpt-5-mini` नामित `gpt-5-mini`

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

## आवश्यक सॉफ़्टवेयर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) या उससे ऊपर

## पर्यावरण चर (Environment variables)

YouTube ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट चलाने के लिए निम्नलिखित पर्यावरण चर आवश्यक हैं।

### विंडोज़ पर

चर को अपने `user` पर्यावरण चर में जोड़ने की सिफारिश की जाती है।
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] के लिए `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- आप अपने PowerShell प्रोफ़ाइल में पर्यावरण चर जोड़ सकते हैं।

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### लिनक्स और macOS पर

सिफारिश की जाती है कि निम्नलिखित एक्सपोर्ट्स को अपने `~/.bashrc` या `~/.zshrc` फ़ाइल में जोड़ें।

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python पुस्तकालय स्थापित करें

1. यदि git क्लाइंट इंस्टॉल नहीं है तो [git क्लाइंट](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) इंस्टॉल करें।
1. `Terminal` विंडो से, नमूना को अपनी पसंदीदा रिपॉ फ़ोल्डर में क्लोन करें।

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फ़ोल्डर में जाएँ।

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python वर्चुअल वातावरण बनाएँ।

    विंडोज़ पर:

    ```powershell
    python -m venv .venv
    ```

    macOS और लिनक्स पर:

    ```bash
    python3 -m venv .venv
    ```

1. Python वर्चुअल वातावरण सक्रिय करें।

   विंडोज़ पर:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS और लिनक्स पर:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक पुस्तकालय स्थापित करें।

   विंडोज़ पर:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS और लिनक्स पर:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रांसक्रिप्शन डेटा तैयारी स्क्रिप्ट्स चलाएँ

### विंडोज़ पर

```powershell
.\transcripts_prepare.ps1
```

### macOS और लिनक्स पर

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->