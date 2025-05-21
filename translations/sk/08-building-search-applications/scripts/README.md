<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:54:34+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sk"
}
-->
# Príprava transkripčných dát

Skripty na prípravu transkripčných dát sťahujú prepisy videí z YouTube a pripravujú ich na použitie so vzorovým projektom Semantic Search s OpenAI Embeddings a Functions.

Skripty na prípravu transkripčných dát boli testované na najnovších verziách Windows 11, macOS Ventura a Ubuntu 22.04 (a vyšších).

## Vytvorenie potrebných zdrojov služby Azure OpenAI

> [!IMPORTANT]
> Odporúčame aktualizovať Azure CLI na najnovšiu verziu, aby bola zaistená kompatibilita s OpenAI.
> Pozrite si [Dokumentáciu](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Vytvorte skupinu zdrojov

> [!NOTE]
> Pre tieto pokyny používame skupinu zdrojov s názvom "semantic-video-search" v oblasti East US.
> Môžete zmeniť názov skupiny zdrojov, ale pri zmene umiestnenia zdrojov 
> skontrolujte [tabuľku dostupnosti modelov](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

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

## Požadovaný softvér

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) alebo novší

## Premenné prostredia

Nasledujúce premenné prostredia sú potrebné na spustenie skriptov na prípravu transkripčných dát z YouTube.

### Na Windows

Odporúčame pridať premenné do vášho `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linuxe a macOS

Odporúčame pridať nasledujúce exporty do vášho súboru `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Inštalácia potrebných Python knižníc

1. Nainštalujte [git klienta](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ak ešte nie je nainštalovaný.
1. Z `Terminal` okna klonujte vzorový projekt do preferovaného priečinka pre repozitáre.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Prejdite do priečinka `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Vytvorte virtuálne prostredie pre Python.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS a Linuxe:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivujte virtuálne prostredie pre Python.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS a Linuxe:

   ```bash
   source .venv/bin/activate
   ```

1. Nainštalujte potrebné knižnice.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS a Linuxe:

   ```bash
   pip3 install -r requirements.txt
   ```

## Spustenie skriptov na prípravu transkripčných dát z YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS a Linuxe

```bash
./transcripts_prepare.sh
```

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.