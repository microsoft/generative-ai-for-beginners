# Подготовка на данни за транскрипция

Скриптовете за подготовка на данни за транскрипция изтеглят транскрипти на видеоклипове от YouTube и ги подготвят за използване с примера Semantic Search с OpenAI Embeddings и функции.

Скриптовете за подготовка на данни за транскрипция са тествани на последните версии Windows 11, macOS Ventura и Ubuntu 22.04 (и по-нови).

## Създаване на необходимите ресурси в Azure OpenAI Service

> [!IMPORTANT]
> Препоръчваме да актуализирате Azure CLI до последната версия, за да осигурите съвместимост с OpenAI
> Вижте [Документация](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Създайте група ресурси

> [!NOTE]
> За тези инструкции използваме група ресурси с име "semantic-video-search" в East US.
> Можете да промените името на групата ресурси, но при смяна на местоположението на ресурсите,
> проверете [таблицата с наличност на моделите](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Създайте ресурс в Azure OpenAI Service.

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

1. Разположете следните модели:
   - `text-embedding-ada-002` версия `2` или по-нова, с име `text-embedding-ada-002`
   - `gpt-4o-mini` с име `gpt-4o-mini`

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

## Необходим софтуер

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или по-нова версия

## Променливи на средата

Следните променливи на средата са необходими за стартиране на скриптовете за подготовка на данни за транскрипция от YouTube.

### В Windows

Препоръчваме да добавите променливите към вашите потребителски променливи на средата.
`Старт на Windows` > `Редактиране на системните променливи на средата` > `Променливи на средата` > `Потребителски променливи` за [USER] > `Нова`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Можете да добавите променливите на средата към вашия PowerShell профил.

```powershell
$env:AZURE_OPENAI_API_KEY = "<вашият API ключ за Azure OpenAI Service>"
$env:AZURE_OPENAI_ENDPOINT = "<вашият краен URL за Azure OpenAI Service>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<името на разполагането на модела в Azure OpenAI Service>"
$env:GOOGLE_DEVELOPER_API_KEY = "<вашият API ключ за Google разработчик>"
``` -->

### В Linux и macOS

Препоръчваме да добавите следните експорти към файла си `~/.bashrc` или `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Инсталиране на необходимите Python библиотеки

1. Инсталирайте [git клиента](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), ако все още не е инсталиран.
1. Отворете прозорец на `Terminal` и клонирайте примера в предпочитаната папка на вашето хранилище.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Отидете в папката `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Създайте виртуална Python среда.

    В Windows:

    ```powershell
    python -m venv .venv
    ```

    В macOS и Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Активирайте виртуалната Python среда.

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

## Стартирайте скриптовете за подготовка на данни за транскрипция от YouTube

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
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->