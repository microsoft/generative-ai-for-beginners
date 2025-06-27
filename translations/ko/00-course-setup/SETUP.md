<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:11:42+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ko"
}
-->
# 개발 환경 설정

이 저장소와 강의는 Python3, .NET, Node.js 및 Java 개발을 지원할 수 있는 Universal 런타임이 포함된 [개발 컨테이너](https://containers.dev?WT.mc_id=academic-105485-koreyst)로 설정되었습니다. 관련된 구성은 이 저장소의 루트에 있는 `.devcontainer/` 폴더에 위치한 `devcontainer.json` 파일에 정의되어 있습니다.

개발 컨테이너를 활성화하려면 [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)에서 실행하거나 (클라우드 호스팅 런타임용) [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)에서 실행하세요 (로컬 장치 호스팅 런타임용). VS Code 내에서 개발 컨테이너가 어떻게 작동하는지에 대한 자세한 내용은 [이 문서](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)를 참조하세요.

> [!TIP]  
> 최소한의 노력으로 빠르게 시작하려면 GitHub Codespaces를 사용하는 것을 추천합니다. 개인 계정에 대한 관대한 [무료 사용 할당량](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)을 제공합니다. [시간 초과](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)를 설정하여 비활성화된 codespaces를 중지하거나 삭제하여 할당량 사용을 극대화하세요.

## 1. 과제 실행

각 강의에는 Python, .NET/C#, Java 및 JavaScript/TypeScript를 포함하여 하나 이상의 프로그래밍 언어로 제공될 수 있는 _선택적_ 과제가 포함됩니다. 이 섹션에서는 이러한 과제를 실행하는 것과 관련된 일반적인 지침을 제공합니다.

### 1.1 Python 과제

Python 과제는 응용 프로그램(`.py` 파일) 또는 Jupyter 노트북(`.ipynb` 파일)으로 제공됩니다.
- 노트북을 실행하려면 Visual Studio Code에서 열고 _커널 선택_ (오른쪽 상단)을 클릭한 다음 표시된 기본 Python 3 옵션을 선택하세요. 이제 _모두 실행_하여 노트북을 실행할 수 있습니다.
- 명령줄에서 Python 응용 프로그램을 실행하려면 과제별 지침을 따라 올바른 파일을 선택하고 필요한 인수를 제공하세요.

## 2. 공급자 구성

과제는 OpenAI, Azure 또는 Hugging Face와 같은 지원되는 서비스 공급자를 통해 하나 이상의 대형 언어 모델(LLM) 배포에 대해 작동하도록 설정될 수 있습니다. 이러한 공급자는 올바른 자격 증명(API 키 또는 토큰)으로 프로그래밍 방식으로 액세스할 수 있는 _호스팅 엔드포인트_(API)를 제공합니다. 이 강의에서는 다음 공급자에 대해 논의합니다:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)와 다양한 모델을 포함하여 핵심 GPT 시리즈.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)로 기업 준비에 초점을 맞춘 OpenAI 모델.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)로 오픈 소스 모델 및 추론 서버.

**이 연습에서는 자신의 계정을 사용해야 합니다.** 과제는 선택 사항이므로 관심에 따라 하나, 모두 또는 아무것도 설정할 수 있습니다. 가입에 대한 몇 가지 지침:

| 가입 | 비용 | API 키 | 플레이그라운드 | 코멘트 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [가격](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [프로젝트 기반](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, 웹](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 여러 모델 사용 가능 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [가격](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [스튜디오 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [접근 권한을 위해 사전에 신청해야 함](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [가격](https://huggingface.co/pricing) | [액세스 토큰](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat은 제한된 모델을 가지고 있음](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

다양한 공급자와 함께 사용하기 위해 이 저장소를 _구성_하려면 아래 지침을 따르세요. 특정 공급자가 필요한 과제는 파일 이름에 다음 태그 중 하나를 포함합니다:
- `aoai` - Azure OpenAI 엔드포인트, 키 필요
- `oai` - OpenAI 엔드포인트, 키 필요
- `hf` - Hugging Face 토큰 필요

하나, 아무것도 또는 모든 공급자를 구성할 수 있습니다. 관련 과제는 자격 증명이 없으면 오류가 발생합니다.

### 2.1 `.env` 파일 생성

위의 지침을 읽고 관련 공급자에 가입하고 필요한 인증 자격 증명(API_KEY 또는 토큰)을 획득했다고 가정합니다. Azure OpenAI의 경우, 적어도 하나의 GPT 모델이 배포된 Azure OpenAI 서비스(엔드포인트)의 유효한 배포를 가지고 있다고 가정합니다.

다음 단계는 **로컬 환경 변수**를 다음과 같이 구성하는 것입니다:

1. 루트 폴더에서 다음과 같은 내용을 가진 `.env.copy` 파일을 찾으세요:

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

2. 아래 명령을 사용하여 `.env` 파일로 복사하세요. 이 파일은 _gitignore_되어 비밀을 안전하게 유지합니다.

   ```bash
   cp .env.copy .env
   ```

3. 다음 섹션에 설명된 대로 값을 채우세요 (오른쪽의 `=`를 대체).

3. (옵션) GitHub Codespaces를 사용하는 경우 이 저장소와 관련된 _Codespaces 비밀_로 환경 변수를 저장할 수 있습니다. 이 경우, 로컬 .env 파일을 설정할 필요가 없습니다. **그러나 이 옵션은 GitHub Codespaces를 사용할 때만 작동합니다.** 대신 Docker Desktop을 사용하는 경우 .env 파일을 설정해야 합니다.

### 2.2 `.env` 파일 채우기

변수 이름이 무엇을 나타내는지 이해하기 위해 빠르게 살펴보겠습니다:

| 변수  | 설명  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 프로필에서 설정한 사용자 액세스 토큰 |
| OPENAI_API_KEY | 비-Azure OpenAI 엔드포인트를 사용하기 위한 인증 키 |
| AZURE_OPENAI_API_KEY | 해당 서비스를 사용하기 위한 인증 키 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 리소스의 배포된 엔드포인트 |
| AZURE_OPENAI_DEPLOYMENT | _텍스트 생성_ 모델 배포 엔드포인트 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _텍스트 임베딩_ 모델 배포 엔드포인트 |
| | |

참고: 마지막 두 Azure OpenAI 변수는 채팅 완료(텍스트 생성) 및 벡터 검색(임베딩)에 대한 기본 모델을 반영합니다. 설정에 대한 지침은 관련 과제에서 정의됩니다.

### 2.3 Azure 구성: 포털에서

Azure OpenAI 엔드포인트 및 키 값은 [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있으므로 거기서 시작하겠습니다.

1. [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)로 이동하세요.
1. 사이드바(왼쪽 메뉴)에서 **키 및 엔드포인트** 옵션을 클릭하세요.
1. **키 표시**를 클릭하세요 - 다음을 볼 수 있습니다: KEY 1, KEY 2 및 엔드포인트.
1. AZURE_OPENAI_API_KEY에 KEY 1 값을 사용하세요.
1. AZURE_OPENAI_ENDPOINT에 엔드포인트 값을 사용하세요.

다음으로 배포한 특정 모델의 엔드포인트가 필요합니다.

1. Azure OpenAI 리소스의 사이드바(왼쪽 메뉴)에서 **모델 배포** 옵션을 클릭하세요.
1. 대상 페이지에서 **배포 관리**를 클릭하세요.

이 작업은 Azure OpenAI Studio 웹사이트로 안내하며, 아래에 설명된 다른 값을 찾을 수 있습니다.

### 2.4 Azure 구성: 스튜디오에서

1. 위에서 설명한 대로 **리소스에서** [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)로 이동하세요.
1. 현재 배포된 모델을 보기 위해 **배포** 탭(사이드바, 왼쪽)을 클릭하세요.
1. 원하는 모델이 배포되지 않은 경우 **새 배포 생성**을 사용하여 배포하세요.
1. _텍스트 생성_ 모델이 필요합니다 - **gpt-35-turbo**를 추천합니다.
1. _텍스트 임베딩_ 모델이 필요합니다 - **text-embedding-ada-002**를 추천합니다.

이제 환경 변수를 사용한 _배포 이름_을 반영하도록 업데이트하세요. 이는 일반적으로 모델 이름과 동일하며 명시적으로 변경하지 않은 경우입니다. 예를 들어 다음과 같을 수 있습니다:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**완료 후 .env 파일을 저장하는 것을 잊지 마세요**. 이제 파일을 종료하고 노트북 실행 지침으로 돌아갈 수 있습니다.

### 2.5 OpenAI 구성: 프로필에서

OpenAI API 키는 [OpenAI 계정](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 계정이 없으면 가입하고 API 키를 생성할 수 있습니다. 키를 얻은 후 `.env` 파일의 `OPENAI_API_KEY` 변수에 사용하세요.

### 2.6 Hugging Face 구성: 프로필에서

Hugging Face 토큰은 [액세스 토큰](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 아래 프로필에서 찾을 수 있습니다. 이를 공개적으로 게시하거나 공유하지 마세요. 대신 이 프로젝트 사용을 위해 새 토큰을 생성하고 `.env` 파일의 `HUGGING_FACE_API_KEY` 변수에 복사하세요. _참고:_ 이것은 기술적으로 API 키가 아니지만 인증에 사용되므로 일관성을 위해 그 명명 규칙을 유지하고 있습니다.

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역은 오류나 부정확성을 포함할 수 있습니다. 원본 문서는 그 언어로 된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.