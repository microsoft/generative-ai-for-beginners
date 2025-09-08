<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-08-25T12:46:52+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "lt"
}
-->
# Transkripcijos duomenų paruošimas

Transkripcijos duomenų paruošimo scenarijai atsisiunčia „YouTube“ vaizdo įrašų transkripcijas ir paruošia jas naudoti su pavyzdžiu „Semantinė paieška su OpenAI Embeddings ir Functions“.

Transkripcijos duomenų paruošimo scenarijai buvo išbandyti su naujausiomis Windows 11, macOS Ventura ir Ubuntu 22.04 (ir naujesnėmis) versijomis.

## Sukurkite reikalingus Azure OpenAI Service išteklius

> [!IMPORTANT]
> Rekomenduojame atnaujinti Azure CLI į naujausią versiją, kad būtų užtikrintas suderinamumas su OpenAI
> Žiūrėkite [dokumentaciją](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Sukurkite išteklių grupę

> [!NOTE]
> Šiose instrukcijose naudojame išteklių grupę „semantic-video-search“ Rytų JAV regione.
> Galite pakeisti išteklių grupės pavadinimą, tačiau jei keičiate išteklių vietą,
> patikrinkite [modelių prieinamumo lentelę](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Sukurkite Azure OpenAI Service išteklių.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Gaukite galinį tašką ir raktus, reikalingus šiai programai

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Įdiekite šiuos modelius:
   - `text-embedding-ada-002` versija `2` arba naujesnė, pavadinta `text-embedding-ada-002`
   - `gpt-35-turbo` versija `0613` arba naujesnė, pavadinta `gpt-35-turbo`

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

## Reikalinga programinė įranga

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) arba naujesnė

## Aplinkos kintamieji

Toliau nurodyti aplinkos kintamieji yra būtini norint paleisti „YouTube“ transkripcijos duomenų paruošimo scenarijus.

### Windows sistemoje

Rekomenduojame kintamuosius pridėti prie savo `user` aplinkos kintamųjų.
`Windows Start` > `Redaguoti sistemos aplinkos kintamuosius` > `Aplinkos kintamieji` > `Vartotojo kintamieji` [USER] > `Naujas`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux ir macOS sistemose

Rekomenduojame šiuos eksportus pridėti į savo `~/.bashrc` arba `~/.zshrc` failą.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Įdiekite reikiamas Python bibliotekas

1. Įdiekite [git klientą](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jei jis dar neįdiegtas.
1. Atidarykite `Terminal` langą ir nukopijuokite pavyzdį į norimą repo aplanką.

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

1. Aktyvuokite Python virtualią aplinką.

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

## Paleiskite „YouTube“ transkripcijos duomenų paruošimo scenarijus

### Windows sistemoje

```powershell
.\transcripts_prepare.ps1
```

### macOS ir Linux sistemose

```bash
./transcripts_prepare.sh
```

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.