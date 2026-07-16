# 전사 데이터 준비

전사 데이터 준비 스크립트는 YouTube 비디오 전사본을 다운로드하고 이를 OpenAI 임베딩 및 함수가 포함된 시맨틱 검색 샘플과 함께 사용할 수 있도록 준비합니다.

전사 데이터 준비 스크립트는 최신 릴리스인 Windows 11, macOS Ventura, Ubuntu 22.04(이상)에서 테스트되었습니다.

## 필요한 Azure OpenAI 서비스 리소스 생성

> [!IMPORTANT]
> 호환성을 보장하기 위해 Azure CLI를 최신 버전으로 업데이트할 것을 권장합니다.
> 자세한 내용은 [문서](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)를 참조하세요.

1. 리소스 그룹 생성

> [!NOTE]
> 이 지침에서는 "semantic-video-search"라는 이름의 East US 지역 리소스 그룹을 사용합니다.
> 리소스 그룹 이름을 변경할 수 있지만, 리소스 위치를 변경할 경우 
> [모델 가용성 표](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)를 확인하세요.

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI 서비스 리소스를 생성하세요.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 이 애플리케이션에서 사용할 엔드포인트 및 키를 가져오세요.

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 다음 모델을 배포하세요:
   - `text-embedding-ada-002` 버전 `2` 이상, 이름 `text-embedding-ada-002`
   - `gpt-5-mini` 이름 `gpt-5-mini`

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

## 필수 소프트웨어

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 이상

## 환경 변수

다음 환경 변수들은 YouTube 전사 데이터 준비 스크립트를 실행하는 데 필요합니다.

### Windows에서

변수들을 `사용자` 환경 변수에 추가하는 것을 권장합니다.
`Windows 시작` > `시스템 환경 변수 편집` > `환경 변수` > [USER]의 `사용자 변수` > `새로 만들기`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- PowerShell 프로필에 환경 변수를 추가할 수도 있습니다.

```powershell
$env:AZURE_OPENAI_API_KEY = "<당신의 Azure OpenAI 서비스 API 키>"
$env:AZURE_OPENAI_ENDPOINT = "<당신의 Azure OpenAI 서비스 엔드포인트>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<당신의 Azure OpenAI 서비스 모델 배포 이름>"
$env:GOOGLE_DEVELOPER_API_KEY = "<당신의 Google 개발자 API 키>"
``` -->

### Linux 및 macOS에서

다음 export 문들을 `~/.bashrc` 또는 `~/.zshrc` 파일에 추가하는 것을 권장합니다.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 필요한 Python 라이브러리 설치

1. 설치되어 있지 않다면 [git 클라이언트](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)를 설치하세요.
1. `터미널` 창에서, 샘플을 원하는 저장소 폴더에 클론하세요.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` 폴더로 이동하세요.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python 가상 환경을 만드세요.

    Windows에서:

    ```powershell
    python -m venv .venv
    ```

    macOS 및 Linux에서:

    ```bash
    python3 -m venv .venv
    ```

1. Python 가상 환경을 활성화하세요.

   Windows에서:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS 및 Linux에서:

   ```bash
   source .venv/bin/activate
   ```

1. 필요한 라이브러리를 설치하세요.

   Windows에서:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS 및 Linux에서:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube 전사 데이터 준비 스크립트 실행

### Windows에서

```powershell
.\transcripts_prepare.ps1
```

### macOS 및 Linux에서

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->