<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:54:51+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ro"
}
-->
# Pregătirea datelor de transcriere

Scripturile de pregătire a datelor de transcriere descarcă transcrierile video de pe YouTube și le pregătesc pentru utilizarea cu exemplul de Căutare Semantică cu OpenAI Embeddings și Functions.

Scripturile de pregătire a datelor de transcriere au fost testate pe cele mai recente versiuni Windows 11, macOS Ventura și Ubuntu 22.04 (și mai noi).

## Crearea resurselor necesare pentru Azure OpenAI Service

1. Creați un grup de resurse

> [!NOTE]
> Pentru aceste instrucțiuni folosim grupul de resurse numit "semantic-video-search" în East US.
> Puteți schimba numele grupului de resurse, dar când schimbați locația resurselor, 
> verificați [tabelul de disponibilitate a modelului](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Creați o resursă Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Obțineți endpoint-ul și cheile pentru utilizarea în această aplicație

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Implementați următoarele modele:
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

## Software necesar

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) sau mai mare

## Variabile de mediu

Următoarele variabile de mediu sunt necesare pentru a rula scripturile de pregătire a datelor de transcriere YouTube.

### Pe Windows

Recomandăm adăugarea variabilelor la `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Pe Linux și macOS

Recomandăm adăugarea următoarelor exporturi în fișierul `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalarea bibliotecilor Python necesare

1. Instalați [clientul git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) dacă nu este deja instalat.
1. Dintr-o fereastră `Terminal`, clonați exemplul în dosarul preferat pentru repo-uri.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigați la dosarul `data_prep`.

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

## Rularea scripturilor de pregătire a datelor de transcriere YouTube

### Pe Windows

```powershell
.\transcripts_prepare.ps1
```

### Pe macOS și Linux

```bash
./transcripts_prepare.sh
```

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți de faptul că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.