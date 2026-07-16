# Pregătirea datelor de transcriere

Scripturile de pregătire a datelor de transcriere descarcă transcrierile videoclipurilor YouTube și le pregătesc pentru utilizare cu exemplul Semantic Search with OpenAI Embeddings and Functions.

Scripturile de pregătire a datelor de transcriere au fost testate pe cele mai recente versiuni Windows 11, macOS Ventura și Ubuntu 22.04 (sau versiuni ulterioare).

## Creați resursele necesare Azure OpenAI Service

> [!IMPORTANT]
> Vă sugerăm să actualizați Azure CLI la cea mai recentă versiune pentru a asigura compatibilitatea cu OpenAI
> Consultați [Documentația](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Creați un grup de resurse

> [!NOTE]
> Pentru aceste instrucțiuni folosim grupul de resurse denumit "semantic-video-search" în East US.
> Puteți schimba numele grupului de resurse, dar când schimbați locația pentru resurse,
> verificați [tabelul disponibilității modelelor](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

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
   - `text-embedding-ada-002` versiunea `2` sau mai mare, denumit `text-embedding-ada-002`
   - `gpt-4o-mini` denumit `gpt-4o-mini`

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

## Software necesar

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) sau o versiune mai mare

## Variabile de mediu

Următoarele variabile de mediu sunt necesare pentru a rula scripturile de pregătire a datelor de transcriere YouTube.

### Pe Windows

Se recomandă adăugarea variabilelor în variabilele de mediu `user`.
`Start Windows` > `Editați variabilele de mediu ale sistemului` > `Variabile de mediu` > `Variabile utilizator` pentru [USER] > `Nou`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Puteți adăuga variabilele de mediu în profilul dvs. PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<cheia API pentru Azure OpenAI Service>"
$env:AZURE_OPENAI_ENDPOINT = "<endpoint-ul Azure OpenAI Service>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<numele implementării modelului Azure OpenAI Service>"
$env:GOOGLE_DEVELOPER_API_KEY = "<cheia API Google developer>"
``` -->

### Pe Linux și macOS

Se recomandă adăugarea următoarelor exporturi în fișierul `~/.bashrc` sau `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalați bibliotecile Python necesare

1. Instalați [clientul git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) dacă nu este deja instalat.
1. Dintr-o fereastră `Terminal`, clonați exemplul în folderul repo dorit.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigați la folderul `data_prep`.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->