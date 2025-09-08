<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:13:16+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sr"
}
-->
# Припрема података за транскрипцију

Скрипте за припрему података за транскрипцију преузимају транскрипте YouTube видео снимака и припремају их за коришћење са примером Semantic Search са OpenAI уграђеним моделима и функцијама.

Скрипте за припрему података за транскрипцију тестиране су на најновијим верзијама Windows 11, macOS Ventura и Ubuntu 22.04 (и новијим).

## Креирање потребних ресурса у Azure OpenAI Service

> [!IMPORTANT]
> Препоручујемо да ажурирате Azure CLI на најновију верзију како бисте обезбедили компатибилност са OpenAI
> Погледајте [Документацију](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Креирајте resource group

> [!NOTE]
> За ове инструкције користимо resource group под именом "semantic-video-search" у East US региону.
> Можете променити име resource group-а, али ако мењате локацију ресурса,
> проверите [табелу доступности модела](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Креирајте Azure OpenAI Service ресурс.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Преузмите endpoint и кључеве за коришћење у овој апликацији

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Деплојујте следеће моделе:
   - `text-embedding-ada-002` верзија `2` или новија, под именом `text-embedding-ada-002`
   - `gpt-35-turbo` верзија `0613` или новија, под именом `gpt-35-turbo`

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

## Потребан софтвер

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или новији

## Променљиве окружења

За покретање скрипти за припрему YouTube транскрипција потребне су следеће променљиве окружења.

### На Windows-у

Препоручује се додавање променљивих у `user` променљиве окружења.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` за [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### На Linux-у и macOS-у

Препоручује се додавање следећих export наредби у ваш `~/.bashrc` или `~/.zshrc` фајл.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Инсталирање потребних Python библиотека

1. Инсталирајте [git клијент](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ако већ није инсталиран.
1. Из `Terminal` прозора, клонирајте пример у жељени фолдер за репозиторијум.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Идите у фолдер `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Креирајте Python виртуелно окружење.

    На Windows-у:

    ```powershell
    python -m venv .venv
    ```

    На macOS-у и Linux-у:

    ```bash
    python3 -m venv .venv
    ```

1. Активирајте Python виртуелно окружење.

   На Windows-у:

   ```powershell
   .venv\Scripts\activate
   ```

   На macOS-у и Linux-у:

   ```bash
   source .venv/bin/activate
   ```

1. Инсталирајте потребне библиотеке.

   На Windows-у:

   ```powershell
   pip install -r requirements.txt
   ```

   На macOS-у и Linux-у:

   ```bash
   pip3 install -r requirements.txt
   ```

## Покретање скрипти за припрему YouTube транскрипција

### На Windows-у

```powershell
.\transcripts_prepare.ps1
```

### На macOS-у и Linux-у

```bash
./transcripts_prepare.sh
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.