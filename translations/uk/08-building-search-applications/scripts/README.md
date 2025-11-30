<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:14:00+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "uk"
}
-->
# Підготовка даних транскрипції

Скрипти підготовки даних транскрипції завантажують транскрипти відео з YouTube і готують їх для використання з прикладом Semantic Search з OpenAI Embeddings та Functions.

Скрипти підготовки даних транскрипції були протестовані на останніх версіях Windows 11, macOS Ventura та Ubuntu 22.04 (і новіших).

## Створення необхідних ресурсів Azure OpenAI Service

> [!IMPORTANT]
> Рекомендуємо оновити Azure CLI до останньої версії для забезпечення сумісності з OpenAI
> Дивіться [Документацію](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Створіть групу ресурсів

> [!NOTE]
> У цих інструкціях ми використовуємо групу ресурсів з назвою "semantic-video-search" у регіоні East US.
> Ви можете змінити назву групи ресурсів, але при зміні розташування ресурсів,
> перевірте [таблицю доступності моделей](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Створіть ресурс Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Отримайте endpoint та ключі для використання в цьому додатку

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Розгорніть наступні моделі:
   - `text-embedding-ada-002` версії `2` або вище, з назвою `text-embedding-ada-002`
   - `gpt-35-turbo` версії `0613` або вище, з назвою `gpt-35-turbo`

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

## Необхідне програмне забезпечення

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) або новіша версія

## Змінні середовища

Для запуску скриптів підготовки даних транскрипції YouTube потрібні наступні змінні середовища.

### У Windows

Рекомендується додати змінні до змінних середовища користувача.
`Пуск Windows` > `Змінити системні змінні середовища` > `Змінні середовища` > `Змінні користувача` для [USER] > `Створити`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### У Linux та macOS

Рекомендується додати наступні експорти у файл `~/.bashrc` або `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Встановлення необхідних бібліотек Python

1. Встановіть [git клієнт](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), якщо він ще не встановлений.
1. У вікні `Терміналу` склонуйте приклад у бажану папку репозиторію.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Перейдіть у папку `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Створіть віртуальне середовище Python.

    У Windows:

    ```powershell
    python -m venv .venv
    ```

    У macOS та Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Активуйте віртуальне середовище Python.

   У Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   У macOS та Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Встановіть необхідні бібліотеки.

   У Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   У macOS та Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Запуск скриптів підготовки даних транскрипції YouTube

### У Windows

```powershell
.\transcripts_prepare.ps1
```

### У macOS та Linux

```bash
./transcripts_prepare.sh
```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.