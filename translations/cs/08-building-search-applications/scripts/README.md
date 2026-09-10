# Příprava dat přepisů

Skripty pro přípravu dat přepisů stahují přepisy videí z YouTube a připravují je k použití se vzorkem Semantic Search s OpenAI Embeddings a Functions.

Skripty pro přípravu dat přepisů byly testovány na nejnovějších verzích Windows 11, macOS Ventura a Ubuntu 22.04 (a novějších).

## Vytvoření požadovaných zdrojů služby Azure OpenAI

> [!IMPORTANT]
> Doporučujeme aktualizovat Azure CLI na nejnovější verzi pro zajištění kompatibility s OpenAI
> Viz [Dokumentace](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvořte skupinu zdrojů

> [!NOTE]
> Pro tyto instrukce používáme skupinu zdrojů s názvem "semantic-video-search" ve východních USA.
> Název skupiny zdrojů můžete změnit, ale pokud změníte umístění zdrojů,
> zkontrolujte [tabulku dostupnosti modelů](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Vytvořte zdroj služby Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Získejte koncový bod a klíče k použití v této aplikaci

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Nasazujte následující modely:
   - `text-embedding-ada-002` verze `2` nebo vyšší, pojmenovaný `text-embedding-ada-002`
   - `gpt-5-mini` pojmenovaný `gpt-5-mini`

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

## Požadovaný software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) nebo vyšší

## Proměnné prostředí

Pro spuštění skriptů pro přípravu dat přepisů z YouTube jsou vyžadovány následující proměnné prostředí.

### Na Windows

Doporučujeme přidat proměnné do uživatelských proměnných prostředí.
`Windows Start` > `Upravit systémové proměnné prostředí` > `Proměnné prostředí` > `Uživatelské proměnné` pro [USER] > `Nová`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Proměnné prostředí můžete přidat do svého PowerShell profilu.

```powershell
$env:AZURE_OPENAI_API_KEY = "<váš API klíč služby Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<váš koncový bod služby Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<název nasazení modelu služby Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<váš API klíč pro Google vývojáře>"
``` -->

### Na Linuxu a macOS

Doporučujeme přidat následující exporty do svého souboru `~/.bashrc` nebo `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalace požadovaných Python knihoven

1. Nainstalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), pokud není již nainstalován.
1. Z okna `Terminálu` klonujte příklad do požadované složky repozitáře.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Přejděte do složky `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Vytvořte virtuální prostředí Python.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS a Linuxu:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivujte virtuální prostředí Python.

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

## Spuštění skriptů pro přípravu dat přepisů z YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS a Linuxu

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->