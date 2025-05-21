<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:54:17+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "cs"
}
-->
# Příprava dat pro přepis

Skripty pro přípravu dat pro přepis stahují přepisy videí z YouTube a připravují je pro použití se vzorovým příkladem Sémantického vyhledávání s OpenAI Embeddings a Functions.

Skripty pro přípravu dat pro přepis byly testovány na nejnovějších verzích Windows 11, macOS Ventura a Ubuntu 22.04 (a vyšších).

## Vytvoření potřebných prostředků Azure OpenAI Service

> [!IMPORTANT]
> Doporučujeme aktualizovat Azure CLI na nejnovější verzi, aby byla zajištěna kompatibilita s OpenAI
> Viz [Dokumentace](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvořte skupinu prostředků

> [!NOTE]
> Pro tyto instrukce používáme skupinu prostředků s názvem "semantic-video-search" ve východní části USA.
> Můžete změnit název skupiny prostředků, ale při změně umístění pro prostředky
> zkontrolujte [tabulku dostupnosti modelů](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Vytvořte prostředek Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Získejte koncový bod a klíče pro použití v této aplikaci

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Nasadit následující modely:
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

## Potřebný software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) nebo novější

## Proměnné prostředí

Pro spuštění skriptů pro přípravu dat pro přepis z YouTube jsou vyžadovány následující proměnné prostředí.

### Na Windows

Doporučujeme přidat proměnné do `uživatelských` environment variables.
`Windows Start` > `Upravit systémové proměnné prostředí` > `Proměnné prostředí` > `Uživatelské proměnné` for [USER] > `Nový`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linux a macOS

Doporučujeme přidat následující exporty do vašeho souboru `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalace potřebných Python knihoven

1. Nainstalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), pokud již není nainstalován.
1. Z okna `Terminálu` naklonujte vzorek do vámi preferované složky pro repozitáře.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Přejděte do složky `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Vytvořte virtuální prostředí pro Python.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS a Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivujte virtuální prostředí pro Python.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS a Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Nainstalujte potřebné knihovny.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS a Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Spuštění skriptů pro přípravu dat pro přepis z YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS a Linux

```bash
./transcripts_prepare.sh
```

**Zřeknutí se odpovědnosti**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé v důsledku použití tohoto překladu.