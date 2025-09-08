<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:12:51+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ro"
}
-->
# Pregătirea datelor de transcriere

Scripturile pentru pregătirea datelor de transcriere descarcă transcrierile videoclipurilor YouTube și le pregătesc pentru utilizare cu exemplul Semantic Search cu OpenAI Embeddings și Functions.

Scripturile pentru pregătirea datelor de transcriere au fost testate pe cele mai recente versiuni Windows 11, macOS Ventura și Ubuntu 22.04 (și versiuni ulterioare).

## Crearea resurselor necesare pentru Azure OpenAI Service

> [!IMPORTANT]
> Vă recomandăm să actualizați Azure CLI la cea mai recentă versiune pentru a asigura compatibilitatea cu OpenAI
> Consultați [Documentația](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Creați un grup de resurse

> [!NOTE]
> Pentru aceste instrucțiuni folosim grupul de resurse numit "semantic-video-search" în East US.
> Puteți schimba numele grupului de resurse, dar dacă schimbați locația resurselor,
> verificați [tabelul de disponibilitate a modelelor](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Creați o resursă Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obțineți endpoint-ul și cheile pentru utilizare în această aplicație

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Implementați următoarele modele:
   - `text-embedding-ada-002` versiunea `2` sau mai mare, denumit `text-embedding-ada-002`
   - `gpt-35-turbo` versiunea `0613` sau mai mare, denumit `gpt-35-turbo`

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

## Software necesar

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) sau o versiune superioară

## Variabile de mediu

Următoarele variabile de mediu sunt necesare pentru a rula scripturile de pregătire a datelor de transcriere YouTube.

### Pe Windows

Recomandăm adăugarea variabilelor în variabilele de mediu ale utilizatorului.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` pentru [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Pe Linux și macOS

Recomandăm adăugarea următoarelor exporturi în fișierul `~/.bashrc` sau `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalarea bibliotecilor Python necesare

1. Instalați [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) dacă nu este deja instalat.
1. Dintr-o fereastră `Terminal`, clonați exemplul în folderul preferat pentru repo.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigați în folderul `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Creați un mediu virtual Python.

    Pe Windows:

    ```powershell
    python -m venv .venv
    ```

    Pe macOS și Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Activați mediul virtual Python.

   Pe Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Pe macOS și Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Instalați bibliotecile necesare.

   Pe Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Pe macOS și Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Rulați scripturile de pregătire a datelor de transcriere YouTube

### Pe Windows

```powershell
.\transcripts_prepare.ps1
```

### Pe macOS și Linux

```bash
./transcripts_prepare.sh
```

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.