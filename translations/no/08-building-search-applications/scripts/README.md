# Forberedelse av transkripsjonsdata

Skriptene for forberedelse av transkripsjonsdata laster ned YouTube-video transkripsjoner og forbereder dem for bruk med eksemplet Semantisk søk med OpenAI-innbokser og funksjoner.

Skriptene for forberedelse av transkripsjonsdata er testet på nyeste utgaver av Windows 11, macOS Ventura og Ubuntu 22.04 (og nyere).

## Opprett nødvendige Azure OpenAI Service-ressurser

> [!IMPORTANT]
> Vi anbefaler at du oppdaterer Azure CLI til nyeste versjon for å sikre kompatibilitet med OpenAI
> Se [Dokumentasjon](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Opprett en ressursgruppe

> [!NOTE]
> For disse instruksjonene bruker vi ressursgruppen som heter "semantic-video-search" i East US.
> Du kan endre navnet på ressursgruppen, men når du endrer plasseringen for ressursene,
> sjekk [tabellen for modelltilgjengelighet](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Opprett en Azure OpenAI Service-ressurs.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hent endepunkt og nøkler for bruk i denne applikasjonen

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Distribuer følgende modeller:
   - `text-embedding-ada-002` versjon `2` eller nyere, med navn `text-embedding-ada-002`
   - `gpt-5-mini` med navn `gpt-5-mini`

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

## Nødvendig programvare

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) eller nyere

## Miljøvariabler

Følgende miljøvariabler er nødvendige for å kjøre skriptene for forberedelse av YouTube-transkripsjonsdata.

### På Windows

Anbefaler å legge til variablene i dine `user`-miljøvariabler.
`Windows Start` > `Rediger systemmiljøvariabler` > `Miljøvariabler` > `Brukervariabler` for [USER] > `Ny`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Du kan legge til miljøvariablene i din PowerShell-profil.

```powershell
$env:AZURE_OPENAI_API_KEY = "<din Azure OpenAI Service API-nøkkel>"
$env:AZURE_OPENAI_ENDPOINT = "<ditt Azure OpenAI Service endepunkt>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ditt Azure OpenAI Service modell distribusjonsnavn>"
$env:GOOGLE_DEVELOPER_API_KEY = "<din Google utvikler API-nøkkel>"
``` -->

### På Linux og macOS

Anbefaler å legge til følgende exports i din `~/.bashrc` eller `~/.zshrc`-fil.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installer nødvendige Python-biblioteker

1. Installer [git-klienten](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) om den ikke allerede er installert.
1. Fra et `Terminal`-vindu, klon eksemplet til din foretrukne repo-mappe.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Naviger til `data_prep`-mappen.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Opprett et Python virtuelt miljø.

    På Windows:

    ```powershell
    python -m venv .venv
    ```

    På macOS og Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktiver det virtuelle Python-miljøet.

   På Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   På macOS og Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installer nødvendige biblioteker.

   På Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   På macOS og Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Kjør skriptene for forberedelse av YouTube-transkripsjonsdata

### På Windows

```powershell
.\transcripts_prepare.ps1
```

### På macOS og Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->