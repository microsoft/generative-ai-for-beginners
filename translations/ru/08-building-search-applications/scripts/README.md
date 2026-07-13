# Подготовка данных транскрипции

Скрипты подготовки данных транскрипции загружают расшифровки видео с YouTube и подготавливают их для использования с примером Semantic Search с помощью OpenAI Embeddings и Functions.

Скрипты подготовки данных транскрипции были протестированы на последних выпусках Windows 11, macOS Ventura и Ubuntu 22.04 (и новее).

## Создание необходимых ресурсов Azure OpenAI Service

> [!IMPORTANT]
> Рекомендуем обновить Azure CLI до последней версии для обеспечения совместимости с OpenAI
> Смотрите [Документацию](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Создайте группу ресурсов

> [!NOTE]
> В этих инструкциях мы используем группу ресурсов с именем "semantic-video-search" в регионе East US.
> Вы можете изменить имя группы ресурсов, но при изменении местоположения ресурсов,
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
   - `text-embedding-ada-002` версии `2` или выше, с именем `text-embedding-ada-002`
   - `gpt-4o-mini` с именем `gpt-4o-mini`

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

## Необходимое программное обеспечение

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или выше

## Переменные окружения

Для запуска скриптов подготовки данных транскрипции YouTube требуются следующие переменные окружения.

### В Windows

Рекомендуется добавить переменные в переменные окружения пользователя `user`.
`Windows Start` > `Изменить системные переменные окружения` > `Переменные среды` > `Переменные пользователя` для [USER] > `Создать`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Вы можете добавить переменные окружения в профиль PowerShell.

```powershell
$env:AZURE_OPENAI_API_KEY = "<ваш ключ API Azure OpenAI Service>"
$env:AZURE_OPENAI_ENDPOINT = "<ваша конечная точка Azure OpenAI Service>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<имя развертывания модели Azure OpenAI Service>"
$env:GOOGLE_DEVELOPER_API_KEY = "<ваш ключ API разработчика Google>"
``` -->

### В Linux и macOS

Рекомендуется добавить следующие экспорты в ваш файл `~/.bashrc` или `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Установка необходимых библиотек Python

1. Установите [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), если он еще не установлен.
1. С окна `Terminal` клонируйте пример в предпочитаемую папку репозитория.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Перейдите в папку `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Создайте виртуальное окружение Python.

    В Windows:

    ```powershell
    python -m venv .venv
    ```

    В macOS и Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Активируйте виртуальное окружение Python.

   В Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   В macOS и Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Установите необходимые библиотеки.

   В Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   В macOS и Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Запуск скриптов подготовки данных транскрипции YouTube

### В Windows

```powershell
.\transcripts_prepare.ps1
```

### В macOS и Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->