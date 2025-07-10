<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:12:29+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "cs"
}
-->
# Příprava dat pro přepis

Skripty pro přípravu dat přepisu stahují přepisy videí z YouTube a připravují je pro použití se vzorcem Semantic Search s OpenAI Embeddings a Functions.

Skripty pro přípravu dat přepisu byly testovány na nejnovějších verzích Windows 11, macOS Ventura a Ubuntu 22.04 (a novějších).

## Vytvoření požadovaných zdrojů Azure OpenAI Service

> [!IMPORTANT]
> Doporučujeme aktualizovat Azure CLI na nejnovější verzi, aby byla zajištěna kompatibilita s OpenAI
> Viz [Dokumentace](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvořte skupinu zdrojů

> [!NOTE]
> Pro tyto pokyny používáme skupinu zdrojů s názvem "semantic-video-search" v regionu East US.
> Název skupiny zdrojů můžete změnit, ale při změně umístění zdrojů 
> zkontrolujte [tabulku dostupnosti modelů](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Vytvořte zdroj Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Získejte endpoint a klíče pro použití v této aplikaci

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Nasadte následující modely:
   - `text-embedding-ada-002` verze `2` nebo vyšší, pojmenovaný `text-embedding-ada-002`
   - `gpt-35-turbo` verze `0613` nebo vyšší, pojmenovaný `gpt-35-turbo`

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

## Požadovaný software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) nebo novější

## Proměnné prostředí

Pro spuštění skriptů pro přípravu dat přepisu z YouTube jsou vyžadovány následující proměnné prostředí.

### Na Windows

Doporučujeme přidat proměnné do uživatelských proměnných prostředí.
`Windows Start` > `Upravit systémové proměnné prostředí` > `Proměnné prostředí` > `Uživatelské proměnné` pro [USER] > `Nová`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Na Linuxu a macOS

Doporučujeme přidat následující exporty do souboru `~/.bashrc` nebo `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalace požadovaných Python knihoven

1. Nainstalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), pokud ještě není nainstalován.
1. V okně `Terminálu` naklonujte vzorový projekt do vámi preferované složky repozitáře.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Přejděte do složky `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Vytvořte Python virtuální prostředí.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS a Linuxu:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivujte Python virtuální prostředí.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS a Linuxu:

   ```bash
   source .venv/bin/activate
   ```

1. Nainstalujte požadované knihovny.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS a Linuxu:

   ```bash
   pip3 install -r requirements.txt
   ```

## Spuštění skriptů pro přípravu dat přepisu z YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS a Linuxu

```bash
./transcripts_prepare.sh
```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.