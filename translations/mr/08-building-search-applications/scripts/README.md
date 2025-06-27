<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:53:05+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "mr"
}
-->
# लिप्यंतरण डेटा तयारी

लिप्यंतरण डेटा तयारी स्क्रिप्ट्स YouTube व्हिडिओ ट्रान्सक्रिप्ट्स डाउनलोड करतात आणि त्यांना OpenAI Embeddings आणि Functions च्या नमुन्यासह सेमॅंटिक शोधासाठी तयार करतात.

लिप्यंतरण डेटा तयारी स्क्रिप्ट्सची चाचणी Windows 11, macOS Ventura आणि Ubuntu 22.04 (आणि त्यापुढील) नवीनतम आवृत्त्यांवर करण्यात आली आहे.

## आवश्यक Azure OpenAI सेवा संसाधने तयार करा

> [!IMPORTANT]
> OpenAI सोबत सुसंगतता सुनिश्चित करण्यासाठी Azure CLI नवीनतम आवृत्तीत अद्ययावत करण्याची आम्ही शिफारस करतो.
> [दस्तऐवज](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) पहा

1. एक संसाधन गट तयार करा

> [!NOTE]
> या सूचनांसाठी आम्ही East US मध्ये "semantic-video-search" नावाचा संसाधन गट वापरत आहोत.
> तुम्ही संसाधन गटाचे नाव बदलू शकता, परंतु संसाधनांसाठी स्थान बदलताना,
> [मॉडेल उपलब्धता तक्ता](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) तपासा.

```console
az group create --name semantic-video-search --location eastus
```

1. एक Azure OpenAI सेवा संसाधन तयार करा.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. या अनुप्रयोगात वापरण्यासाठी एंडपॉइंट आणि कीज मिळवा

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. खालील मॉडेल्स तैनात करा:
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

## आवश्यक सॉफ्टवेअर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) किंवा त्यापेक्षा जास्त

## पर्यावरणीय चल

YouTube लिप्यंतरण डेटा तयारी स्क्रिप्ट्स चालवण्यासाठी खालील पर्यावरणीय चल आवश्यक आहेत.

### Windows वर

तुमच्या `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New` मध्ये चल जोडण्याची शिफारस करा.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux आणि macOS वर

तुमच्या `~/.bashrc` or `~/.zshrc` फाईलमध्ये खालील निर्यात जोडण्याची शिफारस करा.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python लायब्ररी स्थापित करा

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) स्थापित करा जर ते आधीपासून स्थापित नसेल.
1. `Terminal` विंडोमधून, नमुना तुमच्या पसंतीच्या रिपो फोल्डरमध्ये क्लोन करा.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डरमध्ये जा.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. एक Python वर्चुअल वातावरण तयार करा.

    Windows वर:

    ```powershell
    python -m venv .venv
    ```

    macOS आणि Linux वर:

    ```bash
    python3 -m venv .venv
    ```

1. Python वर्चुअल वातावरण सक्रिय करा.

   Windows वर:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS आणि Linux वर:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक लायब्ररी स्थापित करा.

   Windows वर:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS आणि Linux वर:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube लिप्यंतरण डेटा तयारी स्क्रिप्ट्स चालवा

### Windows वर

```powershell
.\transcripts_prepare.ps1
```

### macOS आणि Linux वर

```bash
./transcripts_prepare.sh
```

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अशुद्धता असू शकतात. मूळ भाषेतील दस्तऐवज हा प्रमाणित स्रोत मानला जावा. महत्त्वपूर्ण माहितीसाठी, व्यावसायिक मानव भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.