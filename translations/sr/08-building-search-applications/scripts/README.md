<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:59:58+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "sr"
}
-->
# Припрема података за транскрипцију

Скрипте за припрему података за транскрипцију преузимају транскрипте са YouTube видеа и припремају их за коришћење са примером Семантичке претраге помоћу OpenAI Embeddings и Functions.

Скрипте за припрему података за транскрипцију су тестиране на најновијим издањима Windows 11, macOS Ventura и Ubuntu 22.04 (и новијим).

## Креирање потребних ресурса за Azure OpenAI Service

> [!IMPORTANT]
> Препоручујемо да ажурирате Azure CLI на најновију верзију како бисте обезбедили компатибилност са OpenAI
> Погледајте [документацију](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Креирајте ресурсну групу

> [!NOTE]
> За ова упутства користимо ресурсну групу под именом "semantic-video-search" у East US.
> Можете променити име ресурсне групе, али када мењате локацију за ресурсе,
> проверите [табелу доступности модела](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Креирајте ресурс за Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Преузмите крајњу тачку и кључеве за коришћење у овој апликацији

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Дистрибуирајте следеће моделе:
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

## Потребан софтвер

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или новији

## Енвиронмент променљиве

Следеће енвиронмент променљиве су потребне за покретање скрипти за припрему података за транскрипцију са YouTube-а.

### На Windows-у

Препоручујемо додавање променљивих у ваш `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### На Linux и macOS

Препоручујемо додавање следећих извозних команди у ваш `~/.bashrc` or `~/.zshrc` фајл.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Инсталирајте потребне Python библиотеке

1. Инсталирајте [git клијент](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ако већ није инсталиран.
1. Из `Terminal` прозора, клонирајте пример у жељени фолдер репоа.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Идите у `data_prep` фолдер.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Креирајте Python виртуелно окружење.

    На Windows-у:

    ```powershell
    python -m venv .venv
    ```

    На macOS и Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Активирајте Python виртуелно окружење.

   На Windows-у:

   ```powershell
   .venv\Scripts\activate
   ```

   На macOS и Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Инсталирајте потребне библиотеке.

   На Windows-у:

   ```powershell
   pip install -r requirements.txt
   ```

   На macOS и Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Покрените скрипте за припрему података за транскрипцију са YouTube-а

### На Windows-у

```powershell
.\transcripts_prepare.ps1
```

### На macOS и Linux

```bash
./transcripts_prepare.sh
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење вештачком интелигенцијом [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неразумевања или погрешна тумачења настала коришћењем овог превода.