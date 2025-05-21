<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:55:04+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "bg"
}
-->
# Подготовка на данни за транскрипция

Скриптовете за подготовка на данни за транскрипция изтеглят транскрипции на видеоклипове от YouTube и ги подготвят за използване с Пример за семантично търсене с OpenAI Embeddings и Functions.

Скриптовете за подготовка на данни за транскрипция са тествани на последните версии на Windows 11, macOS Ventura и Ubuntu 22.04 (и по-нови).

## Създаване на необходимите ресурси на Azure OpenAI Service

> [!IMPORTANT]
> Препоръчваме да актуализирате Azure CLI до последната версия, за да осигурите съвместимост с OpenAI
> Вижте [Документация](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Създайте ресурсна група

> [!NOTE]
> За тези инструкции използваме ресурсната група с име "semantic-video-search" в East US.
> Можете да промените името на ресурсната група, но когато променяте местоположението на ресурсите,
> проверете [таблицата за наличност на модели](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Създайте ресурс на Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Получете крайна точка и ключове за използване в това приложение

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Разгърнете следните модели:
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

## Необходим софтуер

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или по-нова версия

## Променливи на средата

Следните променливи на средата са необходими за изпълнение на скриптовете за подготовка на данни за транскрипция от YouTube.

### В Windows

Препоръчваме да добавите променливите към вашия `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### В Linux и macOS

Препоръчваме да добавите следните експорти към вашия файл `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Инсталиране на необходимите Python библиотеки

1. Инсталирайте [git клиента](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ако не е инсталиран.
1. Отворете `Terminal` и клонирайте примера в предпочитаната от вас папка за репо.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Навигирайте до папката `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Създайте виртуална среда за Python.

    В Windows:

    ```powershell
    python -m venv .venv
    ```

    В macOS и Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Активирайте виртуалната среда за Python.

   В Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   В macOS и Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Инсталирайте необходимите библиотеки.

   В Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   В macOS и Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Изпълнение на скриптовете за подготовка на данни за транскрипция от YouTube

### В Windows

```powershell
.\transcripts_prepare.ps1
```

### В macOS и Linux

```bash
./transcripts_prepare.sh
```

**Отказ от отговорност**: 
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Докато се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, произтичащи от използването на този превод.