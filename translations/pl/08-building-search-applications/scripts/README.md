<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:09:42+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "pl"
}
-->
# Przygotowanie danych transkrypcji

Skrypty do przygotowania danych transkrypcji pobierają transkrypcje filmów z YouTube i przygotowują je do użycia z przykładem Semantic Search z OpenAI Embeddings i Functions.

Skrypty do przygotowania danych transkrypcji zostały przetestowane na najnowszych wersjach Windows 11, macOS Ventura oraz Ubuntu 22.04 (i nowszych).

## Utwórz wymagane zasoby Azure OpenAI Service

> [!IMPORTANT]
> Zalecamy zaktualizowanie Azure CLI do najnowszej wersji, aby zapewnić kompatybilność z OpenAI
> Zobacz [Dokumentację](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Utwórz grupę zasobów

> [!NOTE]
> W tych instrukcjach używamy grupy zasobów o nazwie "semantic-video-search" w regionie East US.
> Możesz zmienić nazwę grupy zasobów, ale przy zmianie lokalizacji zasobów,
> sprawdź [tabelę dostępności modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Utwórz zasób Azure OpenAI Service.

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
   - `text-embedding-ada-002` w wersji `2` lub wyższej, o nazwie `text-embedding-ada-002`
   - `gpt-35-turbo` w wersji `0613` lub wyższej, o nazwie `gpt-35-turbo`

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

## Wymagane oprogramowanie

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) lub nowszy

## Zmienne środowiskowe

Do uruchomienia skryptów przygotowujących dane transkrypcji z YouTube wymagane są następujące zmienne środowiskowe.

### Na Windows

Zalecamy dodanie zmiennych do zmiennych środowiskowych użytkownika.
`Start Windows` > `Edytuj zmienne środowiskowe systemu` > `Zmienne środowiskowe` > `Zmienne użytkownika` dla [USER] > `Nowa`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linux i macOS

Zalecamy dodanie poniższych poleceń export do pliku `~/.bashrc` lub `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalacja wymaganych bibliotek Pythona

1. Zainstaluj [klienta git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jeśli nie jest jeszcze zainstalowany.
1. W oknie `Terminal` sklonuj przykład do wybranego folderu repozytorium.

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

## Uruchom skrypty przygotowujące dane transkrypcji z YouTube

### Na Windows

```powershell
.\transcripts_prepare.ps1
```

### Na macOS i Linux

```bash
./transcripts_prepare.sh
```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.