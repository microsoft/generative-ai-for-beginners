<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:46:18+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ru"
}
-->
# Подготовка данных для транскрипции

Скрипты подготовки данных для транскрипции загружают транскрипции видео с YouTube и подготавливают их для использования с примером семантического поиска с OpenAI Embeddings и Functions.

Скрипты подготовки данных для транскрипции были протестированы на последних версиях Windows 11, macOS Ventura и Ubuntu 22.04 (и выше).

## Создание необходимых ресурсов Azure OpenAI Service

> [!IMPORTANT]
> Мы рекомендуем обновить Azure CLI до последней версии для обеспечения совместимости с OpenAI
> См. [документацию](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Создайте группу ресурсов

> [!NOTE]
> В этих инструкциях мы используем группу ресурсов с именем "semantic-video-search" в регионе East US.
> Вы можете изменить имя группы ресурсов, но при изменении местоположения ресурсов
> проверьте [таблицу доступности моделей](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Создайте ресурс Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Получите конечную точку и ключи для использования в этом приложении

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Разверните следующие модели:
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

## Необходимое программное обеспечение

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или выше

## Переменные окружения

Следующие переменные окружения необходимы для запуска скриптов подготовки данных для транскрипции YouTube.

### На Windows

Рекомендуется добавить переменные в `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### На Linux и macOS

Рекомендуется добавить следующие экспорты в файл `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Установка необходимых библиотек Python

1. Установите [git клиент](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), если он еще не установлен.
1. Из окна `Terminal` клонируйте пример в предпочитаемую папку репозитория.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Перейдите в папку `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Создайте виртуальное окружение Python.

    На Windows:

    ```powershell
    python -m venv .venv
    ```

    На macOS и Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Активируйте виртуальное окружение Python.

   На Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   На macOS и Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Установите необходимые библиотеки.

   На Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   На macOS и Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Запуск скриптов подготовки данных для транскрипции YouTube

### На Windows

```powershell
.\transcripts_prepare.ps1
```

### На macOS и Linux

```bash
./transcripts_prepare.sh
```

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Мы стремимся к точности, однако, пожалуйста, учтите, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке должен считаться авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за недопонимание или неправильное толкование, возникшее в результате использования этого перевода.