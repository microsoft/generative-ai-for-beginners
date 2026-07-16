# Priprava podatkov za prepisovanje

Skripte za pripravo podatkov za prepisovanje prenesejo prepise videoposnetkov s YouTuba in jih pripravijo za uporabo s primerom semantičnega iskanja z OpenAI vdelavami in funkcijami.

Skripte za pripravo podatkov za prepisovanje so bile preizkušene na najnovejših različicah Windows 11, macOS Ventura in Ubuntu 22.04 (in novejših).

## Ustvarite zahtevane vire storitve Azure OpenAI

> [!IMPORTANT]
> Priporočamo, da posodobite Azure CLI na najnovejšo različico, da zagotovite združljivost z OpenAI
> Oglejte si [Dokumentacijo](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Ustvarite skupino virov

> [!NOTE]
> Za ta navodila uporabljamo skupino virov z imenom "semantic-video-search" v regiji East US.
> Ime skupine virov lahko spremenite, vendar pri spremembi lokacije virov,
> preverite [tabelo razpoložljivosti modelov](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Ustvarite vir storitve Azure OpenAI.

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
   - `text-embedding-ada-002` različica `2` ali novejša, z imenom `text-embedding-ada-002`
   - `gpt-4o-mini` z imenom `gpt-4o-mini`

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

## Potrebna programska oprema

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ali novejša

## Spremenljivke okolja

Za zagon skriptov za pripravo podatkov za prepisovanje YouTube so potrebne naslednje spremenljivke okolja.

### Na Windows

Priporočamo, da spremenljivke dodate v uporabniške spremenljivke okolja.
`Windows Start` > `Uredi sistemske spremenljivke okolja` > `Spremenljivke okolja` > `Uporabniške spremenljivke` za [USER] > `Novo`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Spremenljivke okolja lahko dodate v svoj PowerShell profil.

```powershell
$env:AZURE_OPENAI_API_KEY = "<vaš Azure OpenAI Service API ključ>"
$env:AZURE_OPENAI_ENDPOINT = "<vaša Azure OpenAI Service končna točka>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ime nameščanja modela Azure OpenAI Service>"
$env:GOOGLE_DEVELOPER_API_KEY = "<vaš Google razvijalski API ključ>"
``` -->

### Na Linux in macOS

Priporočamo, da dodate naslednje izvoze v datoteko `~/.bashrc` ali `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Namestite zahtevane Python knjižnice

1. Namestite [git odjemalca](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), če še ni nameščen.
1. V oknu `Terminal` klonirajte primer v svojo želeno mapo repozitorija.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pomaknite se v mapo `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Ustvarite virtualno Python okolje.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS in Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivirajte virtualno Python okolje.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS in Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Namestite zahtevane knjižnice.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS in Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Zaženite skripte za pripravo podatkov za prepisovanje YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS in Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->