# Припрема података транскрипције

Скрипте за припрему података транскрипције преузимају транскрипте видео снимака са YouTube-а и припремају их за коришћење са примером Семантичке претраге са OpenAI уграђивањима и функцијама.

Скрипте за припрему података транскрипције су тестиране на најновијим издањима Windows 11, macOS Ventura и Ubuntu 22.04 (и новије).

## Креирање потребних ресурса Azure OpenAI услуге

> [!IMPORTANT]
> Предлажемо да ажурирате Azure CLI на најновију верзију ради обезбеђења компатибилности са OpenAI
> Погледајте [Документацију](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Креирајте ресурсну групу

> [!NOTE]
> За ове инструкције користимо ресурсну групу под називом "semantic-video-search" у региону East US.
> Можете променити име ресурсне групе, али када мењате локацију ресурса,
> проверите [табелу доступности модела](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Креирајте Azure OpenAI сервис ресурс.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Набавите крајњу тачку и кључеве за коришћење у овој апликацији

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Деплотирајте следеће моделе:
   - `text-embedding-ada-002` верзија `2` или новија, под именом `text-embedding-ada-002`
   - `gpt-4o-mini` под именом `gpt-4o-mini`

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

## Потребан софтвер

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или новији

## Променљиве окружења

Следеће променљиве окружења су потребне за извршавање скрипти за припрему података транскрипције са YouTube-а.

### На Windows-у

Препоручује се додавање променљивих у `user` променљиве окружења.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` за [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Можете додати променљиве окружења у свој PowerShell профил.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### На Linux и macOS

Препоручује се да следеће export наредбе додате у свој `~/.bashrc` или `~/.zshrc` фајл.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Инсталирање потребних Python библиотека

1. Инсталирајте [git клијент](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ако већ није инсталиран.
1. Из `Terminal` прозора клонирајте пример у жељени фолдер свог репозиторијума.

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

    На macOS и Linux-у:

    ```bash
    python3 -m venv .venv
    ```

1. Активирајте Python виртуелно окружење.

   На Windows-у:

   ```powershell
   .venv\Scripts\activate
   ```

   На macOS и Linux-у:

   ```bash
   source .venv/bin/activate
   ```

1. Инсталирајте потребне библиотеке.

   На Windows-у:

   ```powershell
   pip install -r requirements.txt
   ```

   На macOS и Linux-у:

   ```bash
   pip3 install -r requirements.txt
   ```

## Покрените скрипте за припрему података транскрипције са YouTube-а

### На Windows-у

```powershell
.\transcripts_prepare.ps1
```

### На macOS и Linux-у

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->