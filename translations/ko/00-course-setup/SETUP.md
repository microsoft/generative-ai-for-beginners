<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:25:27+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ko"
}
-->
# 개발 환경 설정하기

이 저장소와 강의는 Python3, .NET, Node.js, Java 개발을 지원하는 범용 런타임이 포함된 [개발 컨테이너](https://containers.dev?WT.mc_id=academic-105485-koreyst)로 구성되어 있습니다. 관련 설정은 이 저장소 루트의 `.devcontainer/` 폴더에 있는 `devcontainer.json` 파일에 정의되어 있습니다.

개발 컨테이너를 활성화하려면 [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)에서 실행하여 클라우드 호스팅 런타임을 사용하거나, [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)에서 실행하여 로컬 장치 호스팅 런타임을 사용할 수 있습니다. VS Code 내에서 개발 컨테이너가 어떻게 작동하는지에 대한 자세한 내용은 [이 문서](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)를 참고하세요.

> [!TIP]  
> 최소한의 노력으로 빠르게 시작하려면 GitHub Codespaces 사용을 권장합니다. 개인 계정에 대해 넉넉한 [무료 사용 한도](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)를 제공합니다. 비활성 codespaces를 중지하거나 삭제하도록 [타임아웃 설정](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)하여 할당량을 최대한 활용하세요.


## 1. 과제 실행하기

각 강의에는 Python, .NET/C#, Java, JavaScript/TypeScript 등 하나 이상의 프로그래밍 언어로 제공될 수 있는 _선택적_ 과제가 있습니다. 이 섹션에서는 과제 실행과 관련된 일반적인 안내를 제공합니다.

### 1.1 Python 과제

Python 과제는 애플리케이션(`.py` 파일) 또는 Jupyter 노트북(`.ipynb` 파일) 형태로 제공됩니다.  
- 노트북을 실행하려면 Visual Studio Code에서 열고 오른쪽 상단의 _Select Kernel_을 클릭한 후 기본 Python 3 옵션을 선택하세요. 이제 _Run All_을 클릭해 노트북을 실행할 수 있습니다.  
- 커맨드라인에서 Python 애플리케이션을 실행하려면 과제별 지침을 따라 올바른 파일을 선택하고 필요한 인자를 제공하세요.

## 2. 공급자 설정하기

과제는 OpenAI, Azure, Hugging Face 같은 지원되는 서비스 공급자를 통해 하나 이상의 대형 언어 모델(LLM) 배포와 연동되도록 설정될 수 있습니다. 이들은 적절한 인증 정보(API 키 또는 토큰)를 사용해 프로그래밍 방식으로 접근할 수 있는 _호스팅된 엔드포인트_(API)를 제공합니다. 이 강의에서는 다음 공급자들을 다룹니다:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - 핵심 GPT 시리즈를 포함한 다양한 모델 제공  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) - 엔터프라이즈 환경에 적합한 OpenAI 모델  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - 오픈소스 모델과 추론 서버 제공

**이 연습을 위해서는 각자 계정을 사용해야 합니다**. 과제는 선택 사항이므로 관심에 따라 한 개, 모두, 또는 전혀 설정하지 않아도 됩니다. 가입 관련 안내는 다음과 같습니다:

| 가입처 | 비용 | API 키 | 플레이그라운드 | 비고 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [가격](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [프로젝트 기반](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [코드 없이 웹에서](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 다양한 모델 제공 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [가격](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [스튜디오 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [사전 신청 필요](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [가격](https://huggingface.co/pricing) | [액세스 토큰](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat은 모델이 제한적](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

아래 지침에 따라 이 저장소를 다양한 공급자와 함께 사용할 수 있도록 _설정_하세요. 특정 공급자가 필요한 과제는 파일명에 다음 태그 중 하나가 포함되어 있습니다:
 - `aoai` - Azure OpenAI 엔드포인트 및 키 필요  
 - `oai` - OpenAI 엔드포인트 및 키 필요  
 - `hf` - Hugging Face 토큰 필요

공급자를 하나, 전혀, 또는 모두 설정할 수 있습니다. 관련 과제는 인증 정보가 없으면 오류가 발생합니다.

### 2.1 `.env` 파일 생성하기

위 안내를 읽고 관련 공급자에 가입하여 필요한 인증 정보(API_KEY 또는 토큰)를 이미 받았다고 가정합니다. Azure OpenAI의 경우, 적어도 하나의 GPT 모델이 배포된 Azure OpenAI 서비스(엔드포인트)를 유효하게 운영 중이어야 합니다.

다음 단계는 **로컬 환경 변수**를 다음과 같이 설정하는 것입니다:

1. 루트 폴더에서 `.env.copy` 파일을 찾아보세요. 내용은 다음과 비슷할 것입니다:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 아래 명령어로 `.env.copy` 파일을 `.env`로 복사하세요. 이 파일은 _gitignore_ 처리되어 비밀 정보를 안전하게 보호합니다.

   ```bash
   cp .env.copy .env
   ```

3. 다음 섹션에 설명된 대로 값을 채워 넣으세요(`=` 오른쪽의 플레이스홀더를 교체).

3. (선택 사항) GitHub Codespaces를 사용하는 경우, 환경 변수를 이 저장소와 연동된 _Codespaces 비밀_로 저장할 수 있습니다. 이 경우 로컬 `.env` 파일을 따로 설정할 필요가 없습니다. **단, 이 옵션은 GitHub Codespaces에서만 작동합니다.** Docker Desktop을 사용하는 경우에는 여전히 `.env` 파일 설정이 필요합니다.

### 2.2 `.env` 파일 내용 채우기

변수 이름이 무엇을 의미하는지 간단히 살펴보겠습니다:

| 변수명 | 설명 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 프로필에서 설정한 사용자 액세스 토큰 |
| OPENAI_API_KEY | 비-Azure OpenAI 엔드포인트용 서비스 인증 키 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 서비스 인증 키 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 리소스의 배포된 엔드포인트 |
| AZURE_OPENAI_DEPLOYMENT | _텍스트 생성_ 모델 배포 이름 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _텍스트 임베딩_ 모델 배포 이름 |
| | |

참고: 마지막 두 Azure OpenAI 변수는 각각 채팅 완성(텍스트 생성)과 벡터 검색(임베딩)에 사용되는 기본 모델을 나타냅니다. 설정 방법은 관련 과제에서 안내됩니다.

### 2.3 Azure 설정: 포털에서

Azure OpenAI 엔드포인트와 키 값은 [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있으니, 여기서부터 시작합니다.

1. [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에 접속하세요.  
2. 사이드바(왼쪽 메뉴)에서 **Keys and Endpoint** 옵션을 클릭하세요.  
3. **Show Keys**를 클릭하면 KEY 1, KEY 2, Endpoint가 표시됩니다.  
4. KEY 1 값을 `AZURE_OPENAI_API_KEY`에 사용하세요.  
5. Endpoint 값을 `AZURE_OPENAI_ENDPOINT`에 사용하세요.

다음으로, 배포한 특정 모델의 엔드포인트를 확인해야 합니다.

1. Azure OpenAI 리소스의 사이드바(왼쪽 메뉴)에서 **Model deployments** 옵션을 클릭하세요.  
2. 대상 페이지에서 **Manage Deployments**를 클릭하세요.

이후 Azure OpenAI Studio 웹사이트로 이동하며, 아래 설명대로 다른 값을 찾을 수 있습니다.

### 2.4 Azure 설정: 스튜디오에서

1. 위에서 설명한 대로 리소스에서 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)로 이동하세요.  
2. 사이드바(왼쪽)에서 **Deployments** 탭을 클릭해 현재 배포된 모델을 확인하세요.  
3. 원하는 모델이 배포되어 있지 않으면 **Create new deployment**를 사용해 배포하세요.  
4. _텍스트 생성_ 모델로는 **gpt-35-turbo**를 권장합니다.  
5. _텍스트 임베딩_ 모델로는 **text-embedding-ada-002**를 권장합니다.

이제 환경 변수에 _배포 이름_을 반영해 업데이트하세요. 보통 모델 이름과 같지만 직접 변경했다면 그 이름을 사용합니다. 예를 들어:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**설정 후 .env 파일을 꼭 저장하세요**. 파일을 닫고 노트북 실행 지침으로 돌아가면 됩니다.

### 2.5 OpenAI 설정: 프로필에서

OpenAI API 키는 [OpenAI 계정](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다. 계정이 없다면 가입 후 API 키를 생성하세요. 키를 받으면 `.env` 파일의 `OPENAI_API_KEY` 변수에 입력하면 됩니다.

### 2.6 Hugging Face 설정: 프로필에서

Hugging Face 토큰은 프로필 내 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다. 이 토큰을 공개적으로 게시하거나 공유하지 마세요. 대신 이 프로젝트 용도로 새 토큰을 생성한 후 `.env` 파일의 `HUGGING_FACE_API_KEY` 변수에 복사해 넣으세요. _참고:_ 기술적으로 API 키는 아니지만 인증에 사용되므로 일관성을 위해 이 명칭을 유지합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.