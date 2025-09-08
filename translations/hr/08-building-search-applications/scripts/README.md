<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:13:27+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "hr"
}
-->
# Priprema podataka za transkripciju

Skripte za pripremu podataka za transkripciju preuzimaju transkripte YouTube videozapisa i pripremaju ih za korištenje s primjerom Semantic Search with OpenAI Embeddings and Functions.

Skripte za pripremu podataka za transkripciju testirane su na najnovijim verzijama Windows 11, macOS Ventura i Ubuntu 22.04 (i novijim).

## Kreiranje potrebnih Azure OpenAI Service resursa

> [!IMPORTANT]
> Preporučujemo da ažurirate Azure CLI na najnoviju verziju kako biste osigurali kompatibilnost s OpenAI
> Pogledajte [Dokumentaciju](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Kreirajte resource group

> [!NOTE]
> Za ove upute koristimo resource group pod nazivom "semantic-video-search" u regiji East US.
> Možete promijeniti naziv resource group, ali ako mijenjate lokaciju resursa,
> provjerite [tablicu dostupnosti modela](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Kreirajte Azure OpenAI Service resurs.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Dohvatite endpoint i ključeve za korištenje u ovoj aplikaciji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Postavite sljedeće modele:
   - `text-embedding-ada-002` verzija `2` ili novija, pod nazivom `text-embedding-ada-002`
   - `gpt-35-turbo` verzija `0613` ili novija, pod nazivom `gpt-35-turbo`

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

## Varijable okoline

Za pokretanje skripti za pripremu podataka za YouTube transkripciju potrebne su sljedeće varijable okoline.

### Na Windowsu

Preporučuje se dodavanje varijabli u `user` varijable okoline.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` za [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Na Linuxu i macOS-u

Preporučuje se dodavanje sljedećih export naredbi u vašu `~/.bashrc` ili `~/.zshrc` datoteku.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalacija potrebnih Python biblioteka

1. Instalirajte [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ako već nije instaliran.
1. Iz `Terminal` prozora klonirajte primjer u željeni repozitorij.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pređite u mapu `data_prep`.

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

## Pokretanje skripti za pripremu podataka za YouTube transkripciju

### Na Windowsu

```powershell
.\transcripts_prepare.ps1
```

### Na macOS-u i Linuxu

```bash
./transcripts_prepare.sh
```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.