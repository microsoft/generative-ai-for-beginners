# Príprava dát pre prepis

Skripty na prípravu dát pre prepis sťahujú prepisy videí z YouTube a pripravujú ich na použitie so vzorcom Semantic Search with OpenAI Embeddings and Functions.

Skripty na prípravu dát pre prepis boli testované na najnovších verziách Windows 11, macOS Ventura a Ubuntu 22.04 (a vyššie).

## Vytvorenie požadovaných zdrojov služby Azure OpenAI Service

> [!IMPORTANT]
> Odporúčame aktualizovať Azure CLI na najnovšiu verziu, aby bola zabezpečená kompatibilita s OpenAI
> Pozrite si [Dokumentáciu](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvorte skupinu zdrojov

> [!NOTE]
> Pre tieto pokyny používame skupinu zdrojov s názvom "semantic-video-search" v regióne East US.
> Môžete zmeniť názov skupiny zdrojov, ale pri zmene lokácie zdrojov,
> skontrolujte [tabuľku dostupnosti modelov](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Vytvorte zdroj služby Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Získajte endpoint a kľúče na použitie v tejto aplikácii

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Nasadzujte nasledujúce modely:
   - `text-embedding-ada-002` verzia `2` alebo vyššia, pomenovaný `text-embedding-ada-002`
   - `gpt-5-mini` pomenovaný `gpt-5-mini`

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

## Potrebný softvér

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) alebo vyšší

## Premenné prostredia

Na spustenie skriptov na prípravu dát pre prepis YouTube sú potrebné nasledujúce premenné prostredia.

### Vo Windows

Odporúča sa pridať premenné do vašich používateľských premenných prostredia.
`Windows Štart` > `Upraviť premenné systému` > `Premenné prostredia` > `Používateľské premenné` pre [USER] > `Nové`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Môžete pridať premenné prostredia do vášho PowerShell profilu.

```powershell
$env:AZURE_OPENAI_API_KEY = "<váš Azure OpenAI Service API kľúč>"
$env:AZURE_OPENAI_ENDPOINT = "<váš Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<váš názov nasadenia modelu Azure OpenAI Service>"
$env:GOOGLE_DEVELOPER_API_KEY = "<váš Google developer API kľúč>"
``` -->

### V Linuxe a macOS

Odporúča sa pridať nasledujúce exporty do súboru `~/.bashrc` alebo `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Inštalácia požadovaných Python knižníc

1. Nainštalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ak ešte nie je nainštalovaný.
1. Z terminálu sklonujte vzorový projekt do vášho preferovaného priečinka.

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

## Spustenie skriptov na prípravu dát pre prepis YouTube

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