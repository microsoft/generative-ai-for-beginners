<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:08:41+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "mr"
}
-->
# ट्रान्सक्रिप्शन डेटा तयारी

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स YouTube व्हिडिओ ट्रान्सक्रिप्ट डाउनलोड करतात आणि Semantic Search with OpenAI Embeddings and Functions नमुन्यासाठी तयार करतात.

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स नवीनतम Windows 11, macOS Ventura आणि Ubuntu 22.04 (आणि त्याहून वर) वर तपासल्या आहेत.

## आवश्यक Azure OpenAI Service संसाधने तयार करा

> [!IMPORTANT]
> OpenAI सोबत सुसंगतता सुनिश्चित करण्यासाठी Azure CLI नवीनतम आवृत्तीवर अपडेट करण्याचा सल्ला देतो
> पाहा [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एक resource group तयार करा

> [!NOTE]
> या सूचनांसाठी आम्ही East US मधील "semantic-video-search" नावाचा resource group वापरत आहोत.
> तुम्ही resource group चे नाव बदलू शकता, पण संसाधनांसाठी स्थान बदलताना,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) तपासा.

```console
az group create --name semantic-video-search --location eastus
```

1. एक Azure OpenAI Service resource तयार करा.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. या अनुप्रयोगात वापरण्यासाठी endpoint आणि keys मिळवा

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. खालील मॉडेल्स तैनात करा:
   - `text-embedding-ada-002` आवृत्ती `2` किंवा त्याहून अधिक, नाव `text-embedding-ada-002`
   - `gpt-35-turbo` आवृत्ती `0613` किंवा त्याहून अधिक, नाव `gpt-35-turbo`

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

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) किंवा त्याहून अधिक

## पर्यावरण चल (Environment variables)

YouTube ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स चालवण्यासाठी खालील पर्यावरण चल आवश्यक आहेत.

### Windows वर

तुमच्या `user` पर्यावरण चलांमध्ये हे जोडण्याचा सल्ला दिला जातो.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux आणि macOS वर

तुमच्या `~/.bashrc` किंवा `~/.zshrc` फाईलमध्ये खालील exports जोडण्याचा सल्ला दिला जातो.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python लायब्ररी इन्स्टॉल करा

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) आधीपासून इन्स्टॉल नसेल तर इन्स्टॉल करा.
1. `Terminal` विंडोमधून, नमुना तुमच्या पसंतीच्या repo फोल्डरमध्ये क्लोन करा.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डरमध्ये जा.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python वर्चुअल एन्व्हायर्नमेंट तयार करा.

    Windows वर:

    ```powershell
    python -m venv .venv
    ```

    macOS आणि Linux वर:

    ```bash
    python3 -m venv .venv
    ```

1. Python वर्चुअल एन्व्हायर्नमेंट सक्रिय करा.

   Windows वर:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS आणि Linux वर:

   ```bash
   source .venv/bin/activate
   ```

1. आवश्यक लायब्ररी इन्स्टॉल करा.

   Windows वर:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS आणि Linux वर:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स चालवा

### Windows वर

```powershell
.\transcripts_prepare.ps1
```

### macOS आणि Linux वर

```bash
./transcripts_prepare.sh
```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.