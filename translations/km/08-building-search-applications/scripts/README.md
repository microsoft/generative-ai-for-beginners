# ការរៀបចំទិន្នន័យបម្លែងសំឡេង

ស្គ្រីបរៀបចំទិន្នន័យបម្លែងសំឡេងទាញយកអត្ថបទវីដេអូ YouTube និងរៀបចំវាឱ្យប្រើជាមួយគំរូស្វែងរក Semantic ជាមួយ OpenAI Embeddings និង Functions ។

ស្គ្រីបរៀបចំទិន្នន័យបម្លែងសំឡេងត្រូវបានសាកល្បងនៅលើកំណែចុងក្រោយ Windows 11, macOS Ventura និង Ubuntu 22.04 (និងលើស).

## បង្កើតធនធាន Azure OpenAI Service ដែលត្រូវការ

> [!IMPORTANT]
> យើងផ្តល់អនុសាសន៍ឱ្យអ្នកធ្វើបច្ចុប្បន្នភាព Azure CLI ទៅកំណែចុងក្រោយដើម្បីធានាការភាពសមរម្យជាមួយ OpenAI
> មើល [ឯកសារណ៍](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. បង្កើតក្រុមធនធាន

> [!NOTE]
> សម្រាប់ការណែនាំទាំងនេះ យើងកំពុងប្រើក្រុមធនធានដែលមានឈ្មោះ "semantic-video-search" នៅ East US។
> អ្នកអាចប្ដូរឈ្មោះក្រុមធនធានបាន ប៉ុន្តេលើពេលប្ដូរទីតាំងសម្រាប់ធនធាន, 
> សូមពិនិត្ដតារាង [ការចូលប្រើម៉ូដែល](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)។

```console
az group create --name semantic-video-search --location eastus
```

1. បង្កើតធនធាន Azure OpenAI Service។

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ទទួលបានចំណុចចប់ និងកូនសោសម្រាប់ប្រើប្រាស់ក្នុងកម្មវិធីនេះ

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ចេញផ្សាយម៉ូដែលដូចតទៅ៖
   - `text-embedding-ada-002` កំណែ `2` ឬលើស, មានឈ្មោះ `text-embedding-ada-002`
   - `gpt-35-turbo` កំណែ `0613` ឬលើស, មានឈ្មោះ `gpt-35-turbo`

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

## កម្មវិធីដែលត្រូវការ

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ឬលើស

## បំណែងអថេរបរិស្ថាន

អថេរបរិស្ថានខាងក្រោមត្រូវការដើម្បីបញ្ជាររបៀបស្គ្រីបរៀបចំទិន្នន័យបម្លែងសំឡេង YouTube។

### នៅលើ Windows

ផ្តល់អនុសាសន៍បន្ថែមអថេរទៅអថេរបរិស្ថាន `user` របស់អ្នក។
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

### នៅលើ Linux និង macOS

ផ្តល់អនុសាសន៍បន្ថែមការនាំចេញខាងក្រោមទៅក្នុងឯកសារ `~/.bashrc` ឬ `~/.zshrc` របស់អ្នក។

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ដំឡើងបណ្ណាល័យ Python ដែលត្រូវការ

1. ដំឡើង [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ប្រសិនបើមិនទាន់ត្រូវបានដំឡើង។
1. ពីចំហៀង `Terminal`, បកចម្លងគំរូទៅកាន់ថត repo ដែលអ្នកចូលចិត្ត។

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. ធ្វើដំណើរទៅថត `data_prep` ។

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. បង្កើតបរិបទ Python virtual ។

    នៅលើ Windows:

    ```powershell
    python -m venv .venv
    ```

    នៅលើយ macOS និង Linux:

    ```bash
    python3 -m venv .venv
    ```

1. បើកបរិបទ Python virtual ។

   នៅលើ Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   នៅលើយ macOS និង Linux:

   ```bash
   source .venv/bin/activate
   ```

1. ដំឡើងបណ្ណាល័យដែលត្រូវការ។

   នៅលើ Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   នៅលើយ macOS និង Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## រត់ស្គ្រីបរៀបចំទិន្នន័យបម្លែងសំឡេង YouTube

### នៅលើ Windows

```powershell
.\transcripts_prepare.ps1
```

### នៅលើយ macOS និង Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្នុងខណៈដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬការបាត់បង់ភាពត្រឹមត្រូវខ្លះ។ ឯកសារដើមក្នុងភាសាម្ខាងគឺជាអ្នកផ្តល់ព័ត៌មានដែលមានអាជ្ញាធរមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សគឺជាជម្រើសដែលបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបញ្ចេញមតិមិនត្រឹមត្រូវដែលកើតមានអំពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->