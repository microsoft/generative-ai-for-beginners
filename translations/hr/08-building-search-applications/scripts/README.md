# Priprema podataka za transkripciju

Skripte za pripremu podataka za transkripciju preuzimaju transkripte videozapisa s YouTubea i pripremaju ih za korištenje s primjerom Semantičkog pretraživanja s OpenAI ugradnjama i funkcijama.

Skripte za pripremu podataka za transkripciju testirane su na najnovijim izdanjima Windows 11, macOS Ventura i Ubuntu 22.04 (i novijim).

## Stvaranje potrebnih resursa Azure OpenAI usluge

> [!IMPORTANT]
> Predlažemo da ažurirate Azure CLI na najnoviju verziju kako biste osigurali kompatibilnost s OpenAI
> Pogledajte [Dokumentaciju](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Stvorite grupu resursa

> [!NOTE]
> Za ove upute koristimo grupu resursa pod nazivom "semantic-video-search" u East US regiji.
> Možete promijeniti ime grupe resursa, ali prilikom promjene lokacije resursa,
> provjerite [tablicu dostupnosti modela](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Stvorite Azure OpenAI Service resurs.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Nabavite endpoint i ključeve za korištenje u ovoj aplikaciji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Postavite sljedeće modele:
   - `text-embedding-ada-002` verzija `2` ili veća, nazvani `text-embedding-ada-002`
   - `gpt-4o-mini` nazvan `gpt-4o-mini`

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

## Potreban softver

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ili noviji

## Varijable okoline

Sljedeće varijable okoline potrebne su za pokretanje skripti za pripremu podataka za transkripciju YouTubea.

### Na Windowsu

Preporučuje se dodavanje varijabli u vaše `user` varijable okoline.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` za [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Varijable okoline možete dodati i u svoj PowerShell profil.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Na Linuxu i macOS-u

Preporučuje se dodati sljedeće izvoze u vašu datoteku `~/.bashrc` ili `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalirajte potrebne Python knjižnice

1. Instalirajte [git klijent](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ako već nije instaliran.
1. U `Terminal` prozoru klonirajte primjer u željeni direktorij.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pređite u mapu `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Stvorite Python virtualno okruženje.

    Na Windowsu:

    ```powershell
    python -m venv .venv
    ```

    Na macOS-u i Linuxu:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivirajte Python virtualno okruženje.

   Na Windowsu:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS-u i Linuxu:

   ```bash
   source .venv/bin/activate
   ```

1. Instalirajte potrebne knjižnice.

   Na Windowsu:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS-u i Linuxu:

   ```bash
   pip3 install -r requirements.txt
   ```

## Pokrenite skripte za pripremu podataka transkripcije YouTubea

### Na Windowsu

```powershell
.\transcripts_prepare.ps1
```

### Na macOS-u i Linuxu

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->