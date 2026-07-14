# Príprava dát pre prepis

Skripty na prípravu dát pre prepis sťahujú tabuľky titulkov videí z YouTube a pripravujú ich na použitie so vzorovým príkladom Semantického vyhľadávania s OpenAI Embeddings a Funkciami.

Skripty na prípravu dát pre prepis boli testované na najnovších verziách Windows 11, macOS Ventura a Ubuntu 22.04 (a novších).

## Vytvorenie požadovaných zdrojov služby Azure OpenAI

> [!IMPORTANT]
> Odporúčame aktualizovať Azure CLI na najnovšiu verziu, aby bola zabezpečená kompatibilita s OpenAI
> Viac informácií nájdete v [dokumentácii](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvorte skupinu zdrojov

> [!NOTE]
> V týchto inštrukciách používame skupinu zdrojov s názvom "semantic-video-search" v regióne East US.
> Môžete zmeniť názov skupiny zdrojov, ale pri zmene umiestnenia zdrojov
> si skontrolujte [tabuľku dostupnosti modelov](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Vytvorte zdroj služby Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Získajte koncový bod a kľúče na použitie v tejto aplikácii

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Nasadte nasledujúce modely:
   - `text-embedding-ada-002` verzia `2` alebo vyššia, s názvom `text-embedding-ada-002`
   - `gpt-4o-mini` s názvom `gpt-4o-mini`

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

## Požadovaný softvér

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) alebo novší

## Premenné prostredia

Na spustenie skriptov na prípravu dát prepisu YouTube sú potrebné nasledujúce premenné prostredia.

### Vo Windows

Odporúčame pridať premenné do používateľských premenných prostredia.
`Windows Štart` > `Upraviť systémové premenné prostredia` > `Premenné prostredia` > `Používateľské premenné` pre [USER] > `Nové`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Premenné prostredia môžete pridať do svojho profilu PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<váš API kľúč služby Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<váš koncový bod služby Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<názov nasadenia modelu služby Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<váš Google API kľúč pre vývojárov>"
``` -->

### Na Linuxe a macOS

Odporúčame pridať nasledujúce exporty do súboru `~/.bashrc` alebo `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Inštalácia požadovaných Python knižníc

1. Nainštalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ak ešte nie je nainštalovaný.
1. V okne `Terminálu` sklonujte vzorový príklad do preferovaného priečinka.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Prejdite do priečinka `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Vytvorte virtuálne prostredie Pythonu.

    Vo Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS a Linuxe:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivujte virtuálne prostredie Pythonu.

   Vo Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS a Linuxe:

   ```bash
   source .venv/bin/activate
   ```

1. Nainštalujte požadované knižnice.

   Vo Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS a Linuxe:

   ```bash
   pip3 install -r requirements.txt
   ```

## Spustenie skriptov na prípravu dát prepisu YouTube

### Vo Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS a Linuxe

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->