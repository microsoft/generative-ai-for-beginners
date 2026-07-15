# Transkripcijos duomenų paruošimas

Transkripcijos duomenų paruošimo scenarijai atsisiunčia „YouTube“ vaizdo įrašų transkripcijas ir paruošia jas naudojimui su pavyzdžiu „Semantinė paieška su OpenAI įterpimais ir funkcijomis“.

Transkripcijos duomenų paruošimo scenarijai buvo išbandyti naujausiose „Windows 11“, „macOS Ventura“ ir „Ubuntu 22.04“ (ir naujesnėse) versijose.

## Sukurkite reikiamus Azure OpenAI paslaugos išteklius

> [!IMPORTANT]
> Rekomenduojame atnaujinti Azure CLI į naujausią versiją, kad užtikrintumėte suderinamumą su OpenAI
> Daugiau informacijos žr. [Dokumentacijoje](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Sukurkite išteklių grupę

> [!NOTE]
> Šioms instrukcijoms naudojame išteklių grupę pavadinimu „semantic-video-search“ East US regione.
> Galite pakeisti išteklių grupės pavadinimą, tačiau keičiant išteklių vietą,
> patikrinkite [modelių prieinamumo lentelę](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Sukurkite Azure OpenAI paslaugos išteklių.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Gaukite galutinį tašką ir raktus naudojimui šioje programoje

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Įdiekite šiuos modelius:
   - `text-embedding-ada-002` versiją `2` ar naujesnę, pavadintą `text-embedding-ada-002`
   - `gpt-4o-mini`, pavadintą `gpt-4o-mini`

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

## Reikalinga programinė įranga

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) arba naujesnė

## Aplinka kintamieji

Norint vykdyti YouTube transkripcijos duomenų paruošimo scenarijus, reikalingi šie aplinkos kintamieji.

### Windows sistemoje

Rekomenduojame pridėti kintamuosius prie savo `user` aplinkos kintamųjų.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Galite pridėti aplinkos kintamuosius prie savo PowerShell profilio.

```powershell
$env:AZURE_OPENAI_API_KEY = "<jūsų Azure OpenAI paslaugos API raktas>"
$env:AZURE_OPENAI_ENDPOINT = "<jūsų Azure OpenAI paslaugos galinis taškas>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<jūsų Azure OpenAI paslaugos modelio diegimo pavadinimas>"
$env:GOOGLE_DEVELOPER_API_KEY = "<jūsų Google kūrėjo API raktas>"
``` -->

### Linux ir macOS sistemose

Rekomenduojame pridėti šiuos eksportus į savo `~/.bashrc` arba `~/.zshrc` failą.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Įdiekite reikiamas Python bibliotekas

1. Įdiekite [git klientą](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jei jis dar nėra įdiegtas.
1. Iš `Terminal` lango nukopijuokite pavyzdį į savo pageidaujamą repo aplanką.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pereikite į `data_prep` aplanką.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Sukurkite Python virtualią aplinką.

    Windows sistemoje:

    ```powershell
    python -m venv .venv
    ```

    macOS ir Linux sistemose:

    ```bash
    python3 -m venv .venv
    ```

1. Aktyvinkite Python virtualią aplinką.

   Windows sistemoje:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ir Linux sistemose:

   ```bash
   source .venv/bin/activate
   ```

1. Įdiekite reikiamas bibliotekas.

   Windows sistemoje:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ir Linux sistemose:

   ```bash
   pip3 install -r requirements.txt
   ```

## Vykdykite YouTube transkripcijos duomenų paruošimo scenarijus

### Windows sistemoje

```powershell
.\transcripts_prepare.ps1
```

### macOS ir Linux sistemose

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->