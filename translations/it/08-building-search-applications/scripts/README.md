<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:54:28+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "it"
}
-->
# Preparazione dati di trascrizione

Gli script di preparazione dei dati di trascrizione scaricano le trascrizioni dei video di YouTube e le preparano per l'uso con il campione di Ricerca Semantica con OpenAI Embeddings e Funzioni.

Gli script di preparazione dei dati di trascrizione sono stati testati sulle ultime versioni di Windows 11, macOS Ventura e Ubuntu 22.04 (e successive).

## Creare le risorse necessarie per il servizio Azure OpenAI

> [!IMPORTANT]
> Consigliamo di aggiornare l'Azure CLI all'ultima versione per garantire la compatibilità con OpenAI
> Vedi [Documentazione](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Creare un gruppo di risorse

> [!NOTE]
> Per queste istruzioni utilizziamo il gruppo di risorse denominato "semantic-video-search" in East US.
> Puoi cambiare il nome del gruppo di risorse, ma quando cambi la posizione delle risorse, 
> controlla la [tabella di disponibilità dei modelli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Creare una risorsa del servizio Azure OpenAI.

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

## Software necessario

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o superiore

## Variabili d'ambiente

Le seguenti variabili d'ambiente sono necessarie per eseguire gli script di preparazione dei dati di trascrizione di YouTube.

### Su Windows

Si consiglia di aggiungere le variabili al tuo `user` environment variables.
`Windows Start` > `Modifica le variabili di sistema` > `Variabili d'ambiente` > `Variabili utente` for [USER] > `Nuovo`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Su Linux e macOS

Si consiglia di aggiungere i seguenti export al tuo file `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installare le librerie Python necessarie

1. Installa il [client git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) se non è già installato.
1. Da una finestra `Terminal`, clona il campione nella tua cartella repo preferita.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Naviga nella cartella `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Crea un ambiente virtuale Python.

    Su Windows:

    ```powershell
    python -m venv .venv
    ```

    Su macOS e Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Attiva l'ambiente virtuale Python.

   Su Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Su macOS e Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installa le librerie necessarie.

   Su Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Su macOS e Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Eseguire gli script di preparazione dei dati di trascrizione di YouTube

### Su Windows

```powershell
.\transcripts_prepare.ps1
```

### Su macOS e Linux

```bash
./transcripts_prepare.sh
```

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.