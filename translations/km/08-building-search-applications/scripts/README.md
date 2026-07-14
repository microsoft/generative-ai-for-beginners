# ព្រឹត្ដការណ៍ទិន្នន័យកិច្ចសម្ភាសន៍

ស្ក្រិបបញ្ចូលព្រឹត្ដការណ៍ទិន្នន័យកិច្ចសម្ភាសន៍ ទាញយកអត្ថបទវីដេអូ YouTube ហើយត្រៀមវា សម្រាប់ប្រើជាមួយ ស្វែងរកអារម្មណ៍ដោយការពិពណ៌នាដោយ OpenAI Embeddings និង Functions ឧទាហរណ៍។

ស្ក្រិបបញ្ចូលព្រឹត្ដការណ៍ទិន្នន័យកិច្ចសម្ភាសន៍ បានត្រូវបានសាកល្បងលើកំណែចុងក្រោយ Windows 11, macOS Ventura និង Ubuntu 22.04 (ឬលើស)។

## បង្កើតធនធាន Azure OpenAI Service ដែលត្រូវការ

> [!IMPORTANT]
> យើងសូមផ្តល់អនុសាសន៍ឲ្យអ្នកធ្វើបច្ចុប្បន្នភាព Azure CLI ទៅកំណែចុងក្រោយ ដើម្បីធានាការយោងគ្នាជាមួយ OpenAI
> មើល [អត្ថាធិប្បាយ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. បង្កើតក្រុមធនធាន

> [!NOTE]
> សម្រាប់ការណែនាំទាំងនេះ យើងកំពុងប្រើក្រុមធនធានឈ្មោះ "semantic-video-search" នៅតំបន់ East US។
> អ្នកអាចផ្លាស់ប្តូរឈ្មោះក្រុមធនធានបាន ប៉ុន្តេលើពេលផ្លាស់ទីកន្លែងសម្រាប់ធនធាន,
> សូមពិនិត្យតារាង [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)។

```console
az group create --name semantic-video-search --location eastus
```

1. បង្កើតធនធាន Azure OpenAI Service។

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ទទួលបានចំណុចចេញ និង key សម្រាប់ប្រើនៅកម្មវិធីនេះ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. បញ្ជូនមូលដ្ឋានម៉ូដែលដូចខាងក្រោម៖
   - `text-embedding-ada-002` កំណែ `2` ឬលើស កំណត់ឈ្មោះ `text-embedding-ada-002`
   - `gpt-4o-mini` កំណត់ឈ្មោះ `gpt-4o-mini`

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

## បច្ចេកវិជ្ជាដែលត្រូវការ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ឬលើស

## អថេរបរិស្ថាន

អថេរបរិស្ថានខាងក្រោមត្រូវការ ដើម្បីរត់ស្ក្រិបបញ្ចូលព្រឹត្ដការណ៍ទិន្នន័យកិច្ចសម្ភាសន៍ YouTube។

### លើ Windows

ណែនាំបន្ថែមអថេរទៅក្នុងអថេរបរិស្ថាន `user` របស់អ្នក។
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` សម្រាប់ [USER] > `New`។

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- អ្នកអាចបន្ថែមអថេរបរិស្ថានទៅក្នុងប្រវត្តិរូប PowerShell របស់អ្នក។

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### លើ Linux និង macOS

ណែនាំបន្ថែមការនាំចេញខាងក្រោមទៅក្នុងឯកសារ `~/.bashrc` ឬ `~/.zshrc` របស់អ្នក។

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ដំឡើងបណ្ណាល័យ Python ដែលត្រូវការ

1. ដំឡើង [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ប្រសិនបើមិនទាន់បានដំឡើង។
1. ពីបង្អួច `Terminal` ឆ្លងសម្លេងឧទាហរណ៍ទៅថត repo ដែលអ្នកចូលចិត្ត។

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. ចូលទៅថត `data_prep`។

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. បង្កើតបរិស្ថាន virtual Python។

    លើ Windows:

    ```powershell
    python -m venv .venv
    ```

    លើ macOS និង Linux:

    ```bash
    python3 -m venv .venv
    ```

1. បើកបរិស្ថាន virtual Python។

   លើ Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   លើ macOS និង Linux:

   ```bash
   source .venv/bin/activate
   ```

1. ដំឡើងបណ្ណាល័យដែលត្រូវការ។

   លើ Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   លើ macOS និង Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## រត់ស្ក្រិបបញ្ចូលព្រឹត្ដការណ៍ទិន្នន័យកិច្ចសម្ភាសន៍ YouTube

### លើ Windows

```powershell
.\transcripts_prepare.ps1
```

### លើ macOS និង Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->