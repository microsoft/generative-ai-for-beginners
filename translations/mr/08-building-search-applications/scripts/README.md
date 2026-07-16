# ट्रान्सक्रिप्शन डेटा तयारी

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स YouTube व्हिडिओ ट्रान्सक्रिप्ट्स डाउनलोड करतात आणि त्यांना Semantic Search with OpenAI Embeddings and Functions चा नमुना वापरण्यासाठी तयार करतात.

ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स नवीनतम Windows 11, macOS Ventura आणि Ubuntu 22.04 (आणि वरच्या) आवृत्त्यांवर तपासले गेले आहेत.

## आवश्यक Azure OpenAI Service संसाधने तयार करा

> [!IMPORTANT]
> OpenAI सह सुसंगतता सुनिश्चित करण्यासाठी आम्ही Azure CLI चे नवीनतम आवृत्तीमध्ये अद्यतन करण्याचा सल्ला देतो
> पहा [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. एक रिसोर्स ग्रुप तयार करा

> [!NOTE]
> या सूचना साठी आम्ही East US मध्ये "semantic-video-search" नावाचा रिसोर्स ग्रुप वापरत आहोत.
> तुम्ही रिसोर्स ग्रुप चे नाव बदलू शकता, पण संसाधनांच्या लोकेशन मध्ये बदल करताना,
> [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) तपासा.

```console
az group create --name semantic-video-search --location eastus
```

1. एक Azure OpenAI Service रिसोर्स तयार करा.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. या अनुप्रयोगात वापरण्यासाठी एन्डपॉईंट आणि कीज मिळवा

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. पुढील मॉडेल तैनात करा:
   - `text-embedding-ada-002` आवृत्ती `2` किंवा त्यापुढे, नाव `text-embedding-ada-002`
   - `gpt-4o-mini` नाव `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## आवश्यक सॉफ्टवेअर

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) किंवा त्यापुढे

## पर्यावरणीय चल (Environment variables)

YouTube ट्रान्सक्रिप्शन डेटा तयारी स्क्रिप्ट्स चालवण्यासाठी खालील पर्यावरणीय चल आवश्यक आहेत.

### Windows वर

आपले `user` पर्यावरणीय चल मध्ये पर्यावरणीय चल जोडण्याची शिफारस केली आहे.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- आपण आपल्या PowerShell प्रोफाइल मध्ये पर्यावरणीय चल जोडू शकता.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux आणि macOS वर

आपले `~/.bashrc` किंवा `~/.zshrc` फाइल मध्ये पुढील निर्यात जोडण्याची शिफारस केली आहे.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## आवश्यक Python लायब्ररी इंस्टॉल करा

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) आधीपासून स्थापित नसेल तर स्थापित करा.
1. `Terminal` विंडो मधून, नमुना आपल्या आवडत्या रेपो फोल्डर मध्ये क्लोन करा.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` फोल्डर मध्ये जा.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. एक Python वर्चुअल एन्व्हायर्नमेंट तयार करा.

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

1. आवश्यक लायब्ररी इंस्टॉल करा.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->