<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:09:32+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "it"
}
-->
# Preparazione dati trascrizione

Gli script per la preparazione dei dati di trascrizione scaricano le trascrizioni dei video YouTube e le preparano per l'uso con l'esempio Semantic Search con OpenAI Embeddings e Functions.

Gli script per la preparazione dei dati di trascrizione sono stati testati sulle ultime versioni di Windows 11, macOS Ventura e Ubuntu 22.04 (e successive).

## Creare le risorse necessarie per Azure OpenAI Service

> [!IMPORTANT]
> Consigliamo di aggiornare l'Azure CLI all'ultima versione per garantire la compatibilità con OpenAI
> Consulta la [Documentazione](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Crea un gruppo di risorse

> [!NOTE]
> Per queste istruzioni utilizziamo il gruppo di risorse chiamato "semantic-video-search" in East US.
> Puoi cambiare il nome del gruppo di risorse, ma se modifichi la posizione delle risorse,
> verifica la [tabella di disponibilità dei modelli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Crea una risorsa Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Ottieni l'endpoint e le chiavi per l'uso in questa applicazione

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Distribuisci i seguenti modelli:
   - `text-embedding-ada-002` versione `2` o superiore, denominato `text-embedding-ada-002`
   - `gpt-35-turbo` versione `0613` o superiore, denominato `gpt-35-turbo`

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

## Software richiesto

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o superiore

## Variabili d'ambiente

Le seguenti variabili d'ambiente sono necessarie per eseguire gli script di preparazione dati trascrizione YouTube.

### Su Windows

Si consiglia di aggiungere le variabili alle variabili d'ambiente `utente`.
`Start di Windows` > `Modifica le variabili d'ambiente di sistema` > `Variabili d'ambiente` > `Variabili utente` per [USER] > `Nuova`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Su Linux e macOS

Si consiglia di aggiungere le seguenti esportazioni al file `~/.bashrc` o `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installare le librerie Python richieste

1. Installa il [client git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) se non è già installato.
1. Da una finestra `Terminale`, clona l'esempio nella cartella del tuo repository preferito.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Vai nella cartella `data_prep`.

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

1. Installa le librerie richieste.

   Su Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Su macOS e Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Eseguire gli script di preparazione dati trascrizione YouTube

### Su Windows

```powershell
.\transcripts_prepare.ps1
```

### Su macOS e Linux

```bash
./transcripts_prepare.sh
```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.