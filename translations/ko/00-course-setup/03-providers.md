# LLM 공급자 선택 및 구성 🔑

과제는 **경우에 따라** OpenAI, Azure, Hugging Face와 같은 지원되는 서비스 공급자를 통해 하나 이상의 대형 언어 모델(LLM) 배포판에 대해 작동하도록 설정할 수도 있습니다. 이들은 적절한 자격 증명(API 키 또는 토큰)으로 프로그래밍 방식으로 접근할 수 있는 _호스팅 엔드포인트_(API)를 제공합니다. 이 과정에서는 다음 공급자들을 다룹니다:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) - 핵심 GPT 시리즈를 포함한 다양한 모델 제공
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) - 기업용 준비에 중점 둔 OpenAI 모델
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) - OpenAI, Meta, Mistral, Cohere, Microsoft 등의 수백 모델에 단일 엔드포인트와 API 키로 접근 (2026년 7월 말 종료 예정인 GitHub Models를 대체)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) - 오픈소스 모델 및 추론 서버
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 또는 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) - 클라우드 구독 없이 직접 기기에서 완전 오프라인으로 모델을 실행하고자 할 경우

**이 연습 문제들에서는 반드시 직접 계정을 사용해야 합니다**. 과제는 선택사항이므로 관심에 따라 한 개, 모두 또는 아무 공급자도 설정하지 않아도 됩니다. 가입에 대한 몇 가지 안내:

| 가입 | 비용 | API 키 | 플레이그라운드 | 비고 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [가격](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [프로젝트 기반](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [노코드, 웹](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 다양한 모델 사용 가능 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [가격](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 빠른 시작](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [스튜디오 빠른 시작](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [접근 권한 사전 신청 필요](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [가격](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [프로젝트 개요 페이지](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 플레이그라운드](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 무료 등급 사용 가능; 다수 모델 공급자에 대해 단일 엔드포인트와 키 제공 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [가격](https://huggingface.co/pricing) | [접근 토큰](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat은 제한된 모델 제공](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 무료 (기기에서 실행) | 불필요 | [로컬 CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 완전 오프라인, OpenAI 호환 엔드포인트 |
| | | | | |

아래 지침을 따라 이 저장소를 다양한 공급자용으로 _구성_ 하세요. 특정 공급자를 필요로 하는 과제는 파일명에 다음 중 하나의 태그가 포함되어 있습니다:

- `aoai` - Azure OpenAI 엔드포인트 및 키 필요
- `oai` - OpenAI 엔드포인트 및 키 필요
- `hf` - Hugging Face 토큰 필요
- `githubmodels` - Microsoft Foundry Models 엔드포인트 및 키 필요 (GitHub Models는 2026년 7월 말 종료 예정)

하나, 전부 또는 전혀 공급자를 구성하지 않아도 됩니다. 관련 과제에서 자격 증명이 없으면 오류가 발생할 뿐입니다.

## `.env` 파일 생성

위 지침을 이미 읽고 관련 공급자에 가입하여 필요한 인증 자격증명(API_KEY 또는 토큰)을 얻었다고 가정합니다. Azure OpenAI의 경우 적어도 하나의 GPT 모델이 배포된 Azure OpenAI 서비스(엔드포인트)를 유효하게 운영 중일 것으로 가정합니다.

다음 단계는 다음과 같이 <strong>로컬 환경 변수</strong>를 구성하는 것입니다:

1. 최상위 폴더에 `.env.copy` 파일이 있는지 확인합니다. 내용은 다음과 비슷해야 합니다:

   ```bash
   # OpenAI 제공자
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry의 Azure OpenAI
   ## (Azure OpenAI 서비스는 현재 Microsoft Foundry의 일부입니다: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # 기본값이 설정되었습니다! (현재 안정적인 GA API 버전)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 모델 (다중 제공자 모델 카탈로그, 2026년 7월 말에 종료되는 GitHub 모델을 대체)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## 허깅페이스
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 아래 명령어로 `.env.copy` 파일을 `.env`로 복사합니다. 이 파일은 _gitignore 설정_이 되어 있어 비밀을 안전하게 유지합니다.

   ```bash
   cp .env.copy .env
   ```

3. 다음 섹션에서 설명하는 대로 값을 채우세요(등호 오른쪽 자리 표시자 교체).

4. (선택 사항) GitHub Codespaces를 사용하는 경우, 이 저장소와 연결된 _Codespaces secrets_ 로 환경 변수를 저장할 수 있습니다. 이렇게 하면 로컬 `.env` 파일을 설정할 필요가 없습니다. **단, 이 옵션은 GitHub Codespaces를 사용할 때만 작동합니다.** Docker Desktop을 사용할 경우 `.env` 파일 설정이 여전히 필요합니다.

## `.env` 파일 값 채우기

변수 이름이 의미하는 바를 빠르게 살펴보겠습니다:

| 변수명  | 설명  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 프로필에서 설정한 사용자 접근 토큰 |
| OPENAI_API_KEY | 비-Azure OpenAI 엔드포인트용 서비스 사용 인증 키 |
| AZURE_OPENAI_API_KEY | 해당 서비스 사용 인증 키 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 리소스에 배포된 엔드포인트 |
| AZURE_OPENAI_DEPLOYMENT | _텍스트 생성_ 모델 배포 엔드포인트 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _텍스트 임베딩_ 모델 배포 엔드포인트 |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry 프로젝트용 엔드포인트, Microsoft Foundry Models 사용 |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry 프로젝트용 API 키 |
| | |

참고: 마지막 두 Azure OpenAI 변수는 각각 채팅 완성(텍스트 생성)과 벡터 검색(임베딩)용 기본 모델을 반영합니다. 설정 지침은 관련 과제에 정의됩니다.

## Azure OpenAI 구성: 포털에서

> **참고:** Azure OpenAI 서비스는 현재 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)의 일부입니다. 리소스와 배포는 Azure 포털에 여전히 표시되지만, 일상적인 모델 관리(배포, 플레이그라운드, 모니터링)는 기존 독립형 "Azure OpenAI Studio" 대신 Foundry 포털에서 이루어집니다.

Azure OpenAI 엔드포인트 및 키 값은 [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있으니 시작해봅시다.

1. [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)로 이동합니다.
1. 사이드바(왼쪽 메뉴)에서 **키 및 엔드포인트** 옵션을 클릭합니다.
1. <strong>키 표시</strong>를 클릭하면 KEY 1, KEY 2 및 엔드포인트가 보입니다.
1. KEY 1 값을 AZURE_OPENAI_API_KEY에 사용합니다.
1. 엔드포인트 값을 AZURE_OPENAI_ENDPOINT에 사용합니다.

다음으로, 배포한 특정 모델의 엔드포인트가 필요합니다.

1. Azure OpenAI 리소스의 사이드바(왼쪽 메뉴)에서 **모델 배포** 옵션을 클릭합니다.
1. 대상 페이지에서 **Microsoft Foundry 포털로 이동** (또는 리소스 유형에 따라 **배포 관리**)을 클릭합니다.

그러면 Microsoft Foundry 포털로 이동하며, 아래에 설명된 다른 값을 확인할 수 있습니다.

## Azure OpenAI 구성: Microsoft Foundry 포털에서

1. 위에서 설명한 대로 [Microsoft Foundry 포털](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)로 이동합니다.
1. 사이드바(왼쪽)의 <strong>배포</strong> 탭을 클릭해 현재 배포된 모델을 확인합니다.
1. 원하는 모델이 배포되지 않았다면, [모델 카탈로그](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)에서 배포를 위해 <strong>모델 배포</strong>를 사용하세요.
1. _텍스트 생성_ 모델이 필요합니다 - 권장: **gpt-5-mini**
1. _텍스트 임베딩_ 모델이 필요합니다 - 권장: **text-embedding-3-small**

이제 환경 변수를 배포 이름에 맞게 업데이트합니다. 일반적으로 배포 이름은 모델 이름과 동일합니다(명시적으로 변경하지 않는 한). 예를 들어 다음과 같이 설정할 수 있습니다:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**설정을 완료한 후 .env 파일 저장을 잊지 마세요**. 이제 파일을 닫고 노트북 실행 지침으로 돌아가세요.

## OpenAI 구성: 프로필에서

OpenAI API 키는 [OpenAI 계정](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 계정이 없으면 가입 후 API 키를 생성할 수 있습니다. 키를 받으면 `.env` 파일의 `OPENAI_API_KEY` 변수에 입력하세요.

## Hugging Face 구성: 프로필에서

Hugging Face 토큰은 프로필 내 [접근 토큰](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 이 토큰을 공개적으로 게시하거나 공유하지 마세요. 대신 이 프로젝트용 새 토큰을 만들어 `.env` 파일의 `HUGGING_FACE_API_KEY` 변수에 복사하세요. _참고:_ 기술적으로 API 키는 아니지만 인증에 사용되므로 통일성을 위해 이 명칭을 유지합니다.

## Microsoft Foundry Models 구성: 포털에서

> **참고:** GitHub Models는 2026년 7월 말 종료 예정입니다. Microsoft Foundry Models는 동일한 무료 체험 모델 카탈로그와 Azure AI 추론 SDK / OpenAI SDK 경험을 제공하는 직접 대체입니다.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)로 이동해 Foundry 프로젝트를 생성하거나 엽니다.
1. [모델 카탈로그](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)를 탐색하며 예를 들어 `gpt-5-mini`를 배포하세요.
1. 프로젝트 <strong>개요</strong> 페이지에서 <strong>엔드포인트</strong>와 <strong>API 키</strong>를 복사합니다.
1. `.env` 파일에서 엔드포인트를 `AZURE_INFERENCE_ENDPOINT`에, 키를 `AZURE_INFERENCE_CREDENTIAL`에 입력합니다.

## 오프라인 / 로컬 공급자

클라우드 구독을 전혀 사용하지 않고 싶다면, 호환되는 오픈 모델을 직접 기기에서 실행할 수 있습니다:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft의 기기 내 런타임입니다. 최적의 실행 공급자(NPU, GPU 또는 CPU)를 자동 선택하고 OpenAI 호환 엔드포인트를 노출하므로, 이 과정 내 대부분 샘플 코드를 최소한의 변경으로 재사용할 수 있습니다. 시작하려면 [Foundry Local 문서](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)를 참고하거나 `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS)로 설치하세요.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma 같은 오픈 모델을 로컬에서 실행하는 인기 대안입니다.


두 옵션을 모두 사용하는 실습 예제는 [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)을 참조하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->