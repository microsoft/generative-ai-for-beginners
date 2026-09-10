# ट्रान्सक्रिप्शन डेटा तयार करणे

ट्रान्सक्रिप्शन डेटा तयार करण्याच्या स्क्रिप्ट्स YouTube व्हिडिओ ट्रान्सक्रिप्ट डाउनलोड करतात आणि त्यांना Semantic Search with OpenAI Embeddings and Functions उदाहरणासह वापरण्यासाठी तयार करतात.

ट्रान्सक्रिप्शन डेटा तयार करण्याच्या स्क्रिप्ट्स नवीनतम प्रकाशनांवर Windows 11, macOS Ventura आणि Ubuntu 22.04 (आणि त्यापुढे) यावर तपासल्या गेल्या आहेत.

## आवश्यक Azure OpenAI सेवा साधने तयार करा

> [!IMPORTANT]
> आम्ही Azure CLI चे नवीनतम आवृत्तीमध्ये अद्यतन करण्याचा सल्ला देतो जेणेकरून OpenAI शी सुसंगतता सुनिश्चित करता येईल
> पहा [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एक रिसोर्स ग्रुप तयार करा

> [!NOTE]
> या सूचनांसाठी आम्ही East US मधील "semantic-video-search" नावाचा रिसोर्स ग्रुप वापरत आहोत.
> तुम्ही रिसोर्स ग्रुपचे नाव बदलू शकता, पण रिसोर्सेससाठी स्थान बदलताना,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) तपासा.

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI सेवा रिसोर्स तयार करा.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. या ॲप्लिकेशनसाठी वापरासाठी एंडपॉइंट आणि की प्राप्त करा

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. पुढील मॉडेल्स तैनात करा:
   - `text-embedding-ada-002` आवृत्ती `2` किंवा त्यापुढे, नाव `text-embedding-ada-002`
   - `gpt-5-mini` नाव `gpt-5-mini`

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

## आवश्यक सॉफ्टवेअर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) किंवा त्यापुढे

## पर्यावरणीय बदल (Environment variables)

पुढील पर्यावरणीय बदल YouTube ट्रान्सक्रिप्शन डेटा तयार करण्याच्या स्क्रिप्ट्स चालवण्यासाठी आवश्यक आहेत.

### Windows वर

शिफारस केली जाते की या बदलांना तुमच्या `user` पर्यावरणीय बदलांत जोडा.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `[USER]` साठी `User variables` > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- तुम्ही Environment variables तुमच्या PowerShell प्रोफाइलमध्ये जोडू शकता.

```powershell
$env:AZURE_OPENAI_API_KEY = "<तुमची Azure OpenAI सेवा API की>"
$env:AZURE_OPENAI_ENDPOINT = "<तुमचा Azure OpenAI सेवा एंडपॉइंट>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<तुमच्या Azure OpenAI सेवा मॉडेल डिप्लॉयमेंटचे नाव>"
$env:GOOGLE_DEVELOPER_API_KEY = "<तुमच्या Google डेव्हलपर API की>"
``` -->

### Linux आणि macOS वर

शिफारस केली जाते की पुढील एक्सपोर्ट्स तुमच्या `~/.bashrc` किंवा `~/.zshrc` फाईलमध्ये जोडा.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python लायब्ररी इंस्टॉल करा

1. जर git client स्थापित नसेल तर याला [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) इन्स्टॉल करा.
1. `Terminal` विंडोमधून, सॅम्पल तुमच्या पसंतीच्या रिपॉ फोल्डरमध्ये क्लोन करा.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डरमध्ये जा.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python वर्चुअल वातावरण तयार करा.

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

1. आवश्यक लायब्ररी इंस्टॉल करा.

   Windows वर:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS आणि Linux वर:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube ट्रान्सक्रिप्शन डेटा तयार करण्याच्या स्क्रिप्ट्स चालवा

### Windows वर

```powershell
.\transcripts_prepare.ps1
```

### macOS आणि Linux वर

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->