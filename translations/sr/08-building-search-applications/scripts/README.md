# Припрема трансрипционих података

Скрипте за припрему трансрипционих података преузимају транскрипте YouTube видео снимака и припремају их за коришћење са примером Семантичке претраге са OpenAI уграђивањима и функцијама.

Скрипте за припрему трансрипционих података тестиране су на најновијим издањима Windows 11, macOS Ventura и Ubuntu 22.04 (и новијим).

## Креирање потребних ресурса Azure OpenAI сервиса

> [!IMPORTANT]
> Препоручујемо да ажурирате Azure CLI на најновију верзију ради обезбеђивања компатибилности са OpenAI
> Погледајте [Документацију](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Креирајте ресурсну групу

> [!NOTE]
> За ове инструкције користимо ресурсну групу под називом "semantic-video-search" у региону East US.
> Можете променити име ресурсне групе, али када мењате локацију ресурса,
> проверите [табелу доступности модела](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Креирајте Azure OpenAI Service ресурс.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Добијте крајњу тачку и кључеве за коришћење у овој апликацији

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Деплојујте следеће моделе:
   - `text-embedding-ada-002` верзија `2` или новија, под називом `text-embedding-ada-002`
   - `gpt-5-mini` под називом `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Потребан софтвер

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) или новији

## Променљиве окружења

Следеће променљиве окружења су потребне да би се покренуле скрипте за припрему трансрипционих података са YouTube.

### На Windows-у

Препоручујемо додавање променљивих у корисничке променљиве окружења (`user` environment variables).
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

Препоручујемо додавање следећих export команди у ваш `~/.bashrc` или `~/.zshrc` фајл.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Инсталирајте потребне Python библиотеке

1. Инсталирајте [git клијент](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) ако већ није инсталиран.
1. Из терминал прозора клонирајте пример у жељену фасциклу вашег репозиторијума.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Идите у фасциклу `data_prep`.

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

## Покрените скрипте за припрему YouTube трансрипционих података

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