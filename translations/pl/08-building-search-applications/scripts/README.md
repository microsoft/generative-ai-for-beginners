<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:54:41+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "pl"
}
-->
# Przygotowanie danych transkrypcji

Skrypty przygotowujące dane transkrypcji pobierają transkrypcje wideo z YouTube i przygotowują je do użycia w przykładzie Wyszukiwania Semantycznego z OpenAI Embeddings i Functions.

Skrypty przygotowujące dane transkrypcji zostały przetestowane na najnowszych wersjach Windows 11, macOS Ventura i Ubuntu 22.04 (i wyżej).

## Utwórz wymagane zasoby Azure OpenAI Service

> [!IMPORTANT]
> Sugerujemy zaktualizowanie Azure CLI do najnowszej wersji, aby zapewnić kompatybilność z OpenAI
> Zobacz [Dokumentację](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Utwórz grupę zasobów

> [!NOTE]
> Dla tych instrukcji używamy grupy zasobów o nazwie "semantic-video-search" w regionie East US.
> Możesz zmienić nazwę grupy zasobów, ale przy zmianie lokalizacji dla zasobów,
> sprawdź [tabelę dostępności modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Utwórz zasób Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Uzyskaj punkt końcowy i klucze do użycia w tej aplikacji

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Wdróż następujące modele:
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

## Wymagane oprogramowanie

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) lub nowszy

## Zmienne środowiskowe

Następujące zmienne środowiskowe są wymagane do uruchomienia skryptów przygotowujących dane transkrypcji z YouTube.

### Na Windows

Zaleca się dodanie zmiennych do `user` environment variables.
`Windows Start` > `Edytuj zmienne środowiskowe systemu` > `Zmienne środowiskowe` > `Zmienne użytkownika` for [USER] > `Nowy`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Na Linux i macOS

Zaleca się dodanie następujących eksportów do pliku `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Zainstaluj wymagane biblioteki Pythona

1. Zainstaluj [klienta git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), jeśli nie jest jeszcze zainstalowany.
1. W oknie `Terminal` sklonuj przykład do preferowanego folderu repozytorium.

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
Ten dokument został przetłumaczony przy użyciu usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.