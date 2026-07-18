# Maandalizi ya data ya uandishi wa maandishi

Skripti za maandalizi ya data ya uandishi wa maandishi hupakua maandishi ya video za YouTube na kuziandaa kwa matumizi na mfano wa Semantic Search with OpenAI Embeddings and Functions.

Skripti za maandalizi ya data ya uandishi wa maandishi zimejaribiwa kwenye matoleo ya hivi karibuni ya Windows 11, macOS Ventura na Ubuntu 22.04 (na juu zaidi).

## Tengeneza rasilimali za huduma ya Azure OpenAI zinazohitajika

> [!IMPORTANT]
> Tunapendekeza uusasishe Azure CLI hadi toleo la hivi karibuni ili kuhakikisha ulinganifu na OpenAI
> Tazama [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Tengeneza kundi la rasilimali

> [!NOTE]
> Kwa maelekezo haya tunatumia kundi la rasilimali linaloitwa "semantic-video-search" kusini mwa Mashariki ya Marekani.
> Unaweza kubadilisha jina la kundi la rasilimali, lakini unapotoboa eneo la rasilimali, 
> angalia [jedwali la upatikanaji wa modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Tengeneza rasimali ya huduma ya Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Pata kiunganishi na funguo kwa matumizi katika programu hii

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Sambaza modeli zifuatazo:
   - toleo la `text-embedding-ada-002` `2` au zaidi, jina `text-embedding-ada-002`
   - `gpt-5-mini` jina `gpt-5-mini`

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

## Programu zinazohitajika

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) au zaidi

## Mabadiliko ya mazingira

Mabadiliko ya mazingira yafuatayo yanahitajika kuendesha skripti za maandalizi ya data ya uandishi wa maandishi wa YouTube.

### Kwenye Windows

Tunapendekeza kuongeza mabadiliko kwenye mabadiliko ya mazingira ya `user`.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` kwa [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Unaweza kuongeza mabadiliko ya mazingira kwenye wasifu wako wa PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<funguo yako ya API ya Huduma ya Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<kiunganishi chako cha Huduma ya Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<jina la usambazaji wa modeli ya Huduma ya Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<funguo yako ya API ya mtengenezaji wa Google>"
``` -->

### Kwenye Linux na macOS

Tunapendekeza kuongeza amri zifuatazo kwenye faili yako ya `~/.bashrc` au `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Sakinisha maktaba za Python zinazohitajika

1. Sakinisha [klenti ya git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst ikiwa bado haijasakinishwa.
1. Kutoka kwenye dirisha la `Terminal`, nakili mfano katika folda ya repo unayopendelea.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Nenda kwenye folda ya `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Tengeneza mazingira ya dhihirisho ya Python.

    Kwenye Windows:

    ```powershell
    python -m venv .venv
    ```

    Kwenye macOS na Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Washa mazingira ya dhihirisho ya Python.

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

## Endesha skripti za maandalizi ya data ya uandishi wa maandishi wa YouTube

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