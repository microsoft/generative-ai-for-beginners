# Preparazione dati trascrizione

Gli script per la preparazione dei dati di trascrizione scaricano le trascrizioni video di YouTube e le preparano per l'utilizzo con l'esempio di Ricerca Semantica con OpenAI Embeddings e Functions.

Gli script per la preparazione dei dati di trascrizione sono stati testati sulle ultime versioni di Windows 11, macOS Ventura e Ubuntu 22.04 (e successive).

## Creare le risorse necessarie di Azure OpenAI Service

> [!IMPORTANT]
> Si consiglia di aggiornare l'Azure CLI all'ultima versione per garantire la compatibilità con OpenAI
> Vedi [Documentazione](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Creare un gruppo di risorse

> [!NOTE]
> Per queste istruzioni stiamo usando il gruppo di risorse chiamato "semantic-video-search" in East US.
> Puoi cambiare il nome del gruppo di risorse, ma cambiando posizione per le risorse,
> consulta la [tabella di disponibilità dei modelli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Creare una risorsa Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Ottenere l'endpoint e le chiavi per l'uso in questa applicazione

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Distribuire i seguenti modelli:
   - `text-embedding-ada-002` versione `2` o superiore, denominato `text-embedding-ada-002`
   - `gpt-5-mini` denominato `gpt-5-mini`

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

## Software richiesto

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o superiore

## Variabili ambiente

Le seguenti variabili ambiente sono richieste per eseguire gli script di preparazione dati trascrizione di YouTube.

### Su Windows

Si consiglia di aggiungere le variabili alle variabili ambiente dell'utente.
`Windows Start` > `Modifica le variabili di ambiente di sistema` > `Variabili d'ambiente` > `Variabili utente` per [USER] > `Nuova`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Puoi aggiungere le variabili ambiente al tuo profilo PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<la tua chiave API di Azure OpenAI Service>"
$env:AZURE_OPENAI_ENDPOINT = "<il tuo endpoint di Azure OpenAI Service>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<il nome del deployment modello di Azure OpenAI Service>"
$env:GOOGLE_DEVELOPER_API_KEY = "<la tua chiave API sviluppatore Google>"
``` -->

### Su Linux e macOS

Si consiglia di aggiungere le seguenti export nel file `~/.bashrc` o `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installare le librerie Python richieste

1. Installare il [client git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) se non è già installato.
1. Da una finestra `Terminal`, clonare il sample nella cartella repo preferita.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigare nella cartella `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Creare un ambiente virtuale Python.

    Su Windows:

    ```powershell
    python -m venv .venv
    ```

    Su macOS e Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Attivare l'ambiente virtuale Python.

   Su Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Su macOS e Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installare le librerie richieste.

   Su Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Su macOS e Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Eseguire gli script di preparazione dati trascrizione di YouTube

### Su Windows

```powershell
.\transcripts_prepare.ps1
```

### Su macOS e Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->