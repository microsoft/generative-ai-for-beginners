<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:55:48+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hr"
}
-->
# Priprema podataka za transkripciju

Skripte za pripremu podataka za transkripciju preuzimaju transkripte YouTube videozapisa i pripremaju ih za upotrebu s uzorkom Semantičkog pretraživanja uz OpenAI ugrađivanja i funkcije.

Skripte za pripremu podataka za transkripciju testirane su na najnovijim izdanjima Windows 11, macOS Ventura i Ubuntu 22.04 (i novijima).

## Kreirajte potrebne resurse Azure OpenAI usluge

> [!IMPORTANT]
> Preporučujemo da ažurirate Azure CLI na najnoviju verziju kako biste osigurali kompatibilnost s OpenAI
> Pogledajte [Dokumentaciju](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Kreirajte grupu resursa

> [!NOTE]
> Za ove upute koristimo grupu resursa nazvanu "semantic-video-search" u East US.
> Možete promijeniti naziv grupe resursa, ali prilikom promjene lokacije za resurse,
> provjerite [tablicu dostupnosti modela](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Kreirajte resurs Azure OpenAI usluge.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Dohvatite krajnju točku i ključeve za korištenje u ovoj aplikaciji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Implementirajte sljedeće modele:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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

## Potreban softver

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ili noviji

## Varijable okruženja

Sljedeće varijable okruženja potrebne su za pokretanje skripti za pripremu podataka za transkripciju YouTube-a.

### Na Windowsu

Preporučujemo dodavanje varijabli u vaše `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linuxu i macOS-u

Preporučujemo dodavanje sljedećih export naredbi u vašu `~/.bashrc` or `~/.zshrc` datoteku.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalirajte potrebne Python biblioteke

1. Instalirajte [git klijent](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ako već nije instaliran.
1. Iz `Terminal` prozora, klonirajte uzorak u željenu mapu repozitorija.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Idite do mape `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Kreirajte Python virtualno okruženje.

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

1. Instalirajte potrebne biblioteke.

   Na Windowsu:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS-u i Linuxu:

   ```bash
   pip3 install -r requirements.txt
   ```

## Pokrenite skripte za pripremu podataka za transkripciju YouTube-a

### Na Windowsu

```powershell
.\transcripts_prepare.ps1
```

### Na macOS-u i Linuxu

```bash
./transcripts_prepare.sh
```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo za točnost, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za bilo kakva nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.