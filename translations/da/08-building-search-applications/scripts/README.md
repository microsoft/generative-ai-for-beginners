# Transskriptionsdataforberedelse

Transskriptionsdataforberedelsesskripterne downloader YouTube-video-transskriptioner og forbereder dem til brug med eksemplet Semantic Search with OpenAI Embeddings and Functions.

Transskriptionsdataforberedelsesskripterne er testet på de nyeste versioner af Windows 11, macOS Ventura og Ubuntu 22.04 (og nyere).

## Opret nødvendige Azure OpenAI Service-ressourcer

> [!IMPORTANT]
> Vi anbefaler, at du opdaterer Azure CLI til den nyeste version for at sikre kompatibilitet med OpenAI
> Se [Dokumentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Opret en ressourcegruppe

> [!NOTE]
> Til disse instruktioner bruger vi ressourcegruppen med navnet "semantic-video-search" i East US.
> Du kan ændre navnet på ressourcegruppen, men når du ændrer placeringen af ressourcerne,
> se tabellet over [modeltilgængelighed](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Opret en Azure OpenAI Service-ressource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Hent endpoint og nøgler til brug i denne applikation

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Deployér følgende modeller:
   - `text-embedding-ada-002` version `2` eller højere, navngivet `text-embedding-ada-002`
   - `gpt-5-mini` navngivet `gpt-5-mini`

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

## Nødvendig software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) eller nyere

## Miljøvariabler

Følgende miljøvariabler er nødvendige for at køre YouTube-transskriptionsdataforberedelsesskripterne.

### På Windows

Vi anbefaler at tilføje variablerne til dine `user` miljøvariabler.
`Windows Start` > `Rediger systemets miljøvariabler` > `Miljøvariabler` > `Brugervariabler` for [USER] > `Ny`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Du kan tilføje miljøvariablerne til din PowerShell-profil.

```powershell
$env:AZURE_OPENAI_API_KEY = "<din Azure OpenAI Service API-nøgle>"
$env:AZURE_OPENAI_ENDPOINT = "<dit Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<dit Azure OpenAI Service model-deploymentsnavn>"
$env:GOOGLE_DEVELOPER_API_KEY = "<din Google developer API-nøgle>"
``` -->

### På Linux og macOS

Vi anbefaler at tilføje følgende exports til din `~/.bashrc` eller `~/.zshrc` fil.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installer de nødvendige Python-biblioteker

1. Installer [git-klienten](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), hvis den ikke allerede er installeret.
1. Fra et `Terminal`-vindue, klon eksemplet til din foretrukne repo-mappe.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Naviger til `data_prep` mappen.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Opret et Python virtuelt miljø.

    På Windows:

    ```powershell
    python -m venv .venv
    ```

    På macOS og Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivér det Python virtuelle miljø.

   På Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   På macOS og Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installer de nødvendige biblioteker.

   På Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   På macOS og Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Kør YouTube-transskriptionsdataforberedelsesskripterne

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
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->