# Kuandaa data za uandikishaji

Scripts za kuandaa data za uandikishaji hukamata manukuu ya video za YouTube na kuziandaa kwa matumizi na mfano wa Semantic Search with OpenAI Embeddings and Functions.

Scripts za kuandaa data za uandikishaji zimeshatumwa kwenye matoleo ya karibuni ya Windows 11, macOS Ventura na Ubuntu 22.04 (na juu yake).

## Tengeneza rasilimali zinazohitajika za Azure OpenAI Service

> [!IMPORTANT]
> Tunapendekeza upitie Azure CLI hadi toleo la karibuni ili kuhakikisha ulinganifu na OpenAI
> Angalia [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Tengeneza kundi la rasilimali

> [!NOTE]
> Kwa maagizo haya tunatumia kundi la rasilimali linaloitwa "semantic-video-search" katika East US.
> Unaweza kubadilisha jina la kundi la rasilimali, lakini unapobadilisha eneo la rasilimali, 
> angalia [jedwali la upatikanaji wa modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Tengeneza rasilimali ya Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Pata sehemu ya mwisho na funguo za matumizi katika programu hii

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Weka modeli zifuatazo:
   - toleo la `text-embedding-ada-002` lenye `2` au zaidi, liitwe `text-embedding-ada-002`
   - `gpt-4o-mini` liitwe `gpt-4o-mini`

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

## Programu zinazohitajika

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) au zaidi

## Mabadiliko ya mazingira

Mabadiliko ya mazingira yafuatayo yanahitajika kuendesha scripts za kuandaa data za uandikishaji za YouTube.

### Kwenye Windows

Tunapendekeza kuongeza mabadiliko haya kwenye mabadiliko ya mazingira ya `user`.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` kwa [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Unaweza kuongeza mabadiliko ya mazingira kwenye wasifu wako wa PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Kwenye Linux na macOS

Tunapendekeza kuongeza exports zifuatazo kwenye faili lako `~/.bashrc` au `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Sakinisha maktaba za Python zinazohitajika

1. Sakinisha [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ikiwa bado haisakinishwi.
1. Kutoka dirisha la `Terminal`, nakili mfano hadi folda yako ya depo unayoipenda.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Nenda kwenye folda ya `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Tengeneza mazingira ya virtual ya Python.

    Kwenye Windows:

    ```powershell
    python -m venv .venv
    ```

    Kwenye macOS na Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Washa mazingira ya virtual ya Python.

   Kwenye Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Kwenye macOS na Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Sakinisha maktaba zinazohitajika.

   Kwenye windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Kwenye macOS na Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Endesha scripts za kuandaa data za uandikishaji za YouTube

### Kwenye windows

```powershell
.\transcripts_prepare.ps1
```

### Kwenye macOS na Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->