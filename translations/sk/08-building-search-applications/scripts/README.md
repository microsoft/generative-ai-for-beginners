<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:12:40+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sk"
}
-->
# Príprava dát pre prepis

Skripty na prípravu dát pre prepis sťahujú prepisy videí z YouTube a pripravujú ich na použitie so vzorom Semantic Search s OpenAI Embeddings a Functions.

Skripty na prípravu dát pre prepis boli testované na najnovších verziách Windows 11, macOS Ventura a Ubuntu 22.04 (a novších).

## Vytvorenie potrebných zdrojov Azure OpenAI Service

> [!IMPORTANT]
> Odporúčame aktualizovať Azure CLI na najnovšiu verziu, aby bola zabezpečená kompatibilita s OpenAI
> Viac informácií nájdete v [dokumentácii](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvorte skupinu zdrojov

> [!NOTE]
> V týchto inštrukciách používame skupinu zdrojov s názvom "semantic-video-search" v regióne East US.
> Môžete zmeniť názov skupiny zdrojov, ale pri zmene lokality zdrojov
> skontrolujte [tabuľku dostupnosti modelov](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Vytvorte zdroj Azure OpenAI Service.

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
   - `gpt-35-turbo` verzia `0613` alebo vyššia, pomenovaný `gpt-35-turbo`

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

## Požadovaný softvér

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) alebo novší

## Premenné prostredia

Na spustenie skriptov na prípravu dát prepisu z YouTube sú potrebné nasledujúce premenné prostredia.

### Na Windows

Odporúčame pridať premenné do používateľských premenných prostredia.
`Windows Štart` > `Upraviť systémové premenné prostredia` > `Premenné prostredia` > `Používateľské premenné` pre [USER] > `Nové`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linux a macOS

Odporúčame pridať nasledujúce exporty do súboru `~/.bashrc` alebo `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Inštalácia potrebných Python knižníc

1. Nainštalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ak ešte nie je nainštalovaný.
1. V okne `Terminál` naklonujte vzorový projekt do preferovaného priečinka repozitára.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Prejdite do priečinka `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Vytvorte Python virtuálne prostredie.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS a Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivujte Python virtuálne prostredie.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS a Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Nainštalujte požadované knižnice.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS a Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Spustenie skriptov na prípravu dát prepisu z YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS a Linux

```bash
./transcripts_prepare.sh
```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.