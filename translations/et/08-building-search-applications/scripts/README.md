# Transkriptsiooniandmete ettevalmistus

Transkriptsiooniandmete ettevalmistamise skriptid laadivad alla YouTube'i video transkriptsioonid ja valmistavad need ette kasutamiseks näites Semantic Search with OpenAI Embeddings and Functions.

Transkriptsiooniandmete ettevalmistamise skripte on testitud uusimate versioonidega Windows 11, macOS Ventura ja Ubuntu 22.04 (ja uuemad).

## Vajalikud Azure OpenAI Service ressursid

> [!IMPORTANT]
> Soovitame värskendada Azure CLI uusimale versioonile, et tagada ühilduvus OpenAI-ga
> Vaata [Dokumentatsiooni](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Loo ressursigrupp

> [!NOTE]
> Nendes juhistes kasutame ressursigruppi nimega "semantic-video-search" East US piirkonnas.
> Saad muuta ressursigrupi nime, kuid kui ressursi asukohta muudad,
> kontrolli [mudeli saadavuse tabelit](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Loo Azure OpenAI Service ressurss.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hangi selle rakenduse kasutamiseks lõpp-punkt ja võtmed

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Paigalda järgmised mudelid:
   - `text-embedding-ada-002` versioon `2` või uuem, nimega `text-embedding-ada-002`
   - `gpt-4o-mini` nimega `gpt-4o-mini`

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

## Vajalik tarkvara

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) või uuem

## Keskkonnamuutujad

Järgmised keskkonnamuutujad on vajalikud YouTube'i transkriptsiooniandmete ettevalmistamise skriptide käivitamiseks.

### Windowsis

Soovitame lisada muutujad oma `user` keskkonnamuutujate hulka.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Saad lisada keskkonnamuutujad oma PowerShell profiili.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linuxis ja macOS-is

Soovitame lisada järgmised ekspordikäsklused oma `~/.bashrc` või `~/.zshrc` faili.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Vajalikud Python'i teegid

1. Paigalda [git klient](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), kui see pole veel installitud.
1. Terminalis klooni näidis eelistatud repokataloogi.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Liigu kataloogi `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Loo Python virtuaalne keskkond.

    Windowsis:

    ```powershell
    python -m venv .venv
    ```

    macOS-is ja Linuxis:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiveeri Python virtuaalne keskkond.

   Windowsis:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS-is ja Linuxis:

   ```bash
   source .venv/bin/activate
   ```

1. Paigalda vajalikud teegid.

   Windowsis:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS-is ja Linuxis:

   ```bash
   pip3 install -r requirements.txt
   ```

## Käivita YouTube'i transkriptsiooniandmete ettevalmistamise skriptid

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