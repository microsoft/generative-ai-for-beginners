# ការរៀបចំទិន្នន័យ​បម្លែងអត្ថបទ

ស្ក្រិបបម្លែងទិន្នន័យ​បម្លែង​អត្ថបទ​ទាញយក​អត្ថបទ​វីដេអូ YouTube ហើយរៀបចំ​វាសម្រាប់​ប្រើប្រាស់ជាមួយ​ការ​ស្វែងរក​សមដ្ឋាន​ជាមួយ OpenAI Embeddings និង Functions គំរូ។

ស្ក្រិបបម្លែងទិន្នន័យ​បម្លែង​អត្ថបទ​ត្រូវ​បានសាកល្បងលើកំណែ​បច្ចុប្បន្ន​បំផុត Windows 11, macOS Ventura និង Ubuntu 22.04 (និងខាងលើ)។

## បង្កើតធនធានសរុប Azure OpenAI Service ត្រូវការ

> [!IMPORTANT]
> យើង​ប្រ Ángelថាអ្នក​គួរអាប់ដេត Azure CLI ទៅកំណែ​បច្ចុប្បន្ន​បំផុត​ដើម្បីធានា​ការចងក្រង​ជាមួយ OpenAI
> មើល [ឯកសារ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. បង្កើតក្រុមធនធាន

> [!NOTE]
> សម្រាប់ការណែនាំ​ទាំងនេះយើងកំពុងប្រើ​ក្រុមធនធាន​ឈ្មោះ "semantic-video-search" នៅ East US។
> អ្នកអាចប្ដូរឈ្មោះក្រុមធនធានបាន ប៉ុន្តេលពេលប្ដូរទីតាំងសម្រាប់ធនធាន,
> សូមពិនិត្យ [តារាងប្រើបានម៉ូដែល](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)។

```console
az group create --name semantic-video-search --location eastus
```

1. បង្កើតធនធាន Azure OpenAI Service។

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ទទួលអាសយដ្ឋានចុងក្រោយ និងកូនសោសម្រាប់ប្រើប្រាស់ក្នុងកម្មវិធីនេះ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ចាក់បញ្ចូលម៉ូដែលដូចខាងក្រោម៖
   - `text-embedding-ada-002` កំណែ `2` ឬច្រើនជាងនេះ, ឈ្មោះ `text-embedding-ada-002`
   - `gpt-5-mini` ឈ្មោះ `gpt-5-mini`

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

## កម្មវិធីត្រូវការ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ឬច្រើនជាងនេះ

## អថេរ​បរិស្ថាន

អថេរ​បរិស្ថាន​ខាងក្រោម​ត្រូវការ​ដើម្បី​រត់​ស្ក្រិប​បម្លែង​អត្ថបទ YouTube។

### នៅលើ Windows

ណែនាំឲ្យបន្ថែមអថេរ​ទៅអថេរក្នុង​បរិស្ធាន `user` របស់អ្នក។
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` សម្រាប់ [USER] > `New`។

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- អ្នកអាចបន្ថែមអថេរបរិស្ថានទៅប្រវត្តិ PowerShell របស់អ្នក។

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### នៅលើ Linux និង macOS

ណែនាំឲ្យបន្ថែមការនាំចេញខាងក្រោមទៅឯកសារ `~/.bashrc` ឬ `~/.zshrc` របស់អ្នក។

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ដំឡើងបណ្ណាល័យ Python ត្រូវការ

1. ដំឡើង [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ប្រសិនបើវាមិនត្រូវបានដំឡើងរួច។
1. ពី​បង្អួច `Terminal` ចម្លងគំរូទៅថតភ្ជាប់ repo ដែលអ្នកចូលចិត្ត។

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. ចូលទៅថត `data_prep`។

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. បង្កើតបរិស្ថាន Python ភាគច្រើន។

    នៅលើ Windows:

    ```powershell
    python -m venv .venv
    ```

    នៅលើ macOS និង Linux:

    ```bash
    python3 -m venv .venv
    ```

1. បើកបរិស្ថាន Python ភាគច្រើន។

   នៅលើ Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   នៅលើ macOS និង Linux:

   ```bash
   source .venv/bin/activate
   ```

1. ដំឡើងបណ្ណាល័យ​ត្រូវការ។

   នៅលើ Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   នៅលើ macOS និង Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## រត់ស្ក្រិបបម្លែងអត្ថបទ YouTube

### នៅលើ Windows

```powershell
.\transcripts_prepare.ps1
```

### នៅលើ macOS និង Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->