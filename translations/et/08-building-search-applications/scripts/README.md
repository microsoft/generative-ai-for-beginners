# Transkriptsioonandmete ettevalmistus

Transkriptsioonandmete ettevalmistamise skriptid laadivad alla YouTube'i video transkriptsioonid ja valmistavad need ette kasutamiseks näidise Semantic Search with OpenAI Embeddings and Functions jaoks.

Transkriptsioonandmete ettevalmistamise skriptid on testitud Windows 11, macOS Ventura ja Ubuntu 22.04 (ja uuem) viimastel versioonidel.

## Nõutavate Azure OpenAI Service ressursside loomine

> [!IMPORTANT]
> Soovitame teil uuendada Azure CLI uusimale versioonile, et tagada ühilduvus OpenAI-ga
> Vaadake [Dokumentatsiooni](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Looge ressursside grupp

> [!NOTE]
> Nende juhiste puhul kasutame ressursside gruppi nimega "semantic-video-search" asukohaga East US.
> Saate muuta ressursside grupi nime, kuid kui muudate ressursside asukohta,
> kontrollige [mudeli saadavustabelit](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Looge Azure OpenAI Service ressurss.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Leidke selle rakenduse kasutamiseks vajalikud endpoint ja võtmed

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Paigaldage järgmised mudelid:
   - `text-embedding-ada-002` versioon `2` või uuem, nimega `text-embedding-ada-002`
   - `gpt-5-mini` nimega `gpt-5-mini`

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

## Nõutav tarkvara

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) või uuem

## Keskkonnamuutujad

Järgmistesse keskkonnamuutujatesse tuleb panna YouTube'i transkriptsioonandmete ettevalmistamise skriptide käivitamiseks.

### Windowsis

Soovitame lisada muutujad enda `user` keskkonnamuutujate hulka.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Võite lisada keskkonnamuutujad ka oma PowerShelli profiili.

```powershell
$env:AZURE_OPENAI_API_KEY = "<teie Azure OpenAI Service API võti>"
$env:AZURE_OPENAI_ENDPOINT = "<teie Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<teie Azure OpenAI Service mudeli paigaldamise nimi>"
$env:GOOGLE_DEVELOPER_API_KEY = "<teie Google arendaja API võti>"
``` -->

### Linuxis ja macOS-is

Soovitame lisada järgmised ekspordid oma `~/.bashrc` või `~/.zshrc` faili.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Nõutavate Python'i teekide paigaldamine

1. Paigaldage [git klient](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), kui see pole veel paigaldatud.
1. Avage `Terminali` aken ja kloonige näidis eelistatud kausta.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Minge kausta `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Looge Python'i virtuaalne keskkond.

    Windowsis:

    ```powershell
    python -m venv .venv
    ```

    macOS-is ja Linuxis:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiveerige Python'i virtuaalne keskkond.

   Windowsis:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS-is ja Linuxis:

   ```bash
   source .venv/bin/activate
   ```

1. Paigaldage nõutavad teegid.

   Windowsis:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS-is ja Linuxis:

   ```bash
   pip3 install -r requirements.txt
   ```

## Käivitage YouTube'i transkriptsioonandmete ettevalmistamise skriptid

### Windowsis

```powershell
.\transcripts_prepare.ps1
```

### macOS-is ja Linuxis

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->