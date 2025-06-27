<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T17:00:36+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sl"
}
-->
# Priprava podatkov za transkripcijo

Skripte za pripravo podatkov za transkripcijo prenesejo prepise YouTube videov in jih pripravijo za uporabo z vzorcem Semantičnega iskanja z OpenAI vdelavami in funkcijami.

Skripte za pripravo podatkov za transkripcijo so bile testirane na najnovejših izdajah Windows 11, macOS Ventura in Ubuntu 22.04 (in novejših).

## Ustvarite potrebne vire Azure OpenAI Service

> [!IMPORTANT]
> Priporočamo, da posodobite Azure CLI na najnovejšo različico, da zagotovite združljivost z OpenAI
> Glejte [Dokumentacijo](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Ustvarite skupino virov

> [!NOTE]
> Za ta navodila uporabljamo skupino virov z imenom "semantic-video-search" na vzhodu ZDA.
> Ime skupine virov lahko spremenite, vendar pri spreminjanju lokacije za vire 
> preverite [tabelo razpoložljivosti modelov](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Ustvarite vir Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Pridobite končno točko in ključe za uporabo v tej aplikaciji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Namestite naslednje modele:
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

## Potrebna programska oprema

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ali novejši

## Okoljske spremenljivke

Za izvajanje skriptov za pripravo podatkov za transkripcijo na YouTube so potrebne naslednje okoljske spremenljivke.

### Na Windows

Priporočamo dodajanje spremenljivk v `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linux in macOS

Priporočamo dodajanje naslednjih izvozenih vrednosti v datoteko `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Namestite potrebne Python knjižnice

1. Namestite [git odjemalec](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), če še ni nameščen.
2. V oknu `Terminal` klonirajte vzorec v želeno mapo repozitorija.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pomaknite se do mape `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Ustvarite Python virtualno okolje.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS in Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivirajte Python virtualno okolje.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS in Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Namestite potrebne knjižnice.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS in Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Zaženite skripte za pripravo podatkov za transkripcijo na YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS in Linux

```bash
./transcripts_prepare.sh
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Medtem ko si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.