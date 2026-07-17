# Przygotowanie danych transkrypcji

Skrypty do przygotowania danych transkrypcyjnych pobierają transkrypcje z filmów YouTube i przygotowują je do użycia z przykładem Semantic Search z OpenAI Embeddings i Functions.

Skrypty do przygotowania danych transkrypcyjnych były testowane na najnowszych wersjach Windows 11, macOS Ventura oraz Ubuntu 22.04 (i wyższych).

## Utwórz wymagane zasoby usługi Azure OpenAI

> [!IMPORTANT]
> Zalecamy zaktualizowanie Azure CLI do najnowszej wersji, aby zapewnić kompatybilność z OpenAI
> Zobacz [Dokumentację](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Utwórz grupę zasobów

> [!NOTE]
> W tych instrukcjach używamy grupy zasobów o nazwie "semantic-video-search" w regionie East US.
> Możesz zmienić nazwę grupy zasobów, ale zmieniając lokalizację zasobów, 
> sprawdź [tabelę dostępności modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Utwórz zasób usługi Azure OpenAI.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Pobierz punkt końcowy i klucze do użycia w tej aplikacji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Wdróż następujące modele:
   - `text-embedding-ada-002` w wersji `2` lub wyższej, nazwany `text-embedding-ada-002`
   - `gpt-5-mini` nazwany `gpt-5-mini`

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

## Wymagane oprogramowanie

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) lub nowszy

## Zmienne środowiskowe

Do uruchomienia skryptów przygotowujących dane transkrypcji YouTube wymagane są następujące zmienne środowiskowe.

### Na Windows

Zalecamy dodanie zmiennych do zmiennych środowiskowych `user`.
`Start Windows` > `Edytuj zmienne środowiskowe systemu` > `Zmienne środowiskowe` > `Zmienne użytkownika` dla [USER] > `Nowa`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Możesz dodać zmienne środowiskowe do swojego profilu PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<twój klucz API usługi Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<twój punkt końcowy usługi Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<twoja nazwa wdrożenia modelu usługi Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<twój klucz API developera Google>"
``` -->

### Na Linux i macOS

Zalecamy dodanie poniższych eksportów do pliku `~/.bashrc` lub `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalacja wymaganych bibliotek Pythona

1. Zainstaluj [klient git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jeśli nie jest jeszcze zainstalowany.
1. Z okna `Terminal` sklonuj przykład do preferowanego folderu repozytorium.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Przejdź do folderu `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Utwórz wirtualne środowisko Pythona.

    Na Windows:

    ```powershell
    python -m venv .venv
    ```

    Na macOS i Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktywuj wirtualne środowisko Pythona.

   Na Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Na macOS i Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Zainstaluj wymagane biblioteki.

   Na Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Na macOS i Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Uruchom skrypty przygotowujące dane transkrypcji YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS i Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->