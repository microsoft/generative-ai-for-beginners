# LLM 공급자 선택 및 구성 🔑

과제는 OpenAI, Azure 또는 Hugging Face와 같은 지원되는 서비스 공급자를 통해 하나 이상의 대규모 언어 모델(LLM) 배포판을 대상으로 작동하도록 설정할 수도 있습니다. 이들은 적절한 자격 증명(API 키 또는 토큰)으로 프로그래밍 방식으로 액세스할 수 있는 _호스팅된 엔드포인트_(API)를 제공합니다. 이 과정에서는 다음 공급자에 대해 다룹니다:

 - 다양한 모델을 포함한 핵심 GPT 시리즈를 제공하는 [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst).
 - 엔터프라이즈 준비에 중점을 둔 OpenAI 모델을 위한 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst).
 - OpenAI, Meta, Mistral, Cohere, Microsoft 등 수백 개 모델에 하나의 엔드포인트와 API 키로 접근할 수 있는 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) (2026년 7월 말 종료 예정인 GitHub Models를 대체).
 - 오픈 소스 모델과 추론 서버를 위한 [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst).
 - 클라우드 구독 없이 자체 장치에서 완전히 오프라인으로 모델을 실행하려는 경우 [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 또는 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst).

**이 연습 문제는 본인 계정을 사용해야 합니다**. 과제는 선택 사항이므로 관심에 따라 하나, 모두 또는 전혀 설정하지 않을 수 있습니다. 가입 관련 안내:

| 가입 | 비용 | API 키 | 플레이그라운드 | 코멘트 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [가격](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [프로젝트 기반](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [노코드, 웹](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 다양한 모델 사용 가능 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [가격](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 퀵스타트](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [스튜디오 퀵스타트](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [접근 권한 사전 신청 필요](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [가격](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [프로젝트 개요 페이지](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 플레이그라운드](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 무료 티어 사용 가능; 다수 모델 공급자용 단일 엔드포인트 + 키 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [가격](https://huggingface.co/pricing) | [액세스 토큰](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat은 제한된 모델만 지원](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 무료 (장치에서 실행) | 필요 없음 | [로컬 CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 완전 오프라인, OpenAI 호환 엔드포인트 |
| | | | | |

다음 지침에 따라 이 리포지토리를 다양한 공급자와 함께 _구성_하십시오. 특정 공급자가 필요한 과제는 파일명에 아래 태그 중 하나를 포함합니다:

- `aoai` - Azure OpenAI 엔드포인트, 키 필요
- `oai` - OpenAI 엔드포인트, 키 필요
- `hf` - Hugging Face 토큰 필요
- `githubmodels` - Microsoft Foundry Models 엔드포인트, 키 필요 (GitHub Models는 2026년 7월 말 종료 예정)

하나, 전혀 또는 모두의 공급자를 구성할 수 있습니다. 관련 과제는 자격 증명이 없으면 오류가 발생합니다.

## `.env` 파일 생성

위 안내를 참고해 적절한 공급자에 가입하고 필요한 인증 자격 증명(API_KEY 또는 토큰)을 획득했다고 가정합니다. Azure OpenAI의 경우, 최소 하나 이상의 GPT 모델이 배포된 Azure OpenAI 서비스(엔드포인트)의 올바른 배포판도 있다고 가정합니다.

다음 단계는 <strong>로컬 환경 변수</strong>를 아래와 같이 구성하는 것입니다:

1. 루트 폴더에서 `.env.copy` 파일을 찾아 그 내용이 다음과 유사한지 확인합니다:

   ```bash
   # OpenAI 제공자
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry의 Azure OpenAI
   ## (Azure OpenAI 서비스는 이제 Microsoft Foundry의 일부입니다: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # 기본값이 설정되었습니다! (현재 안정적인 GA API 버전)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 모델 (다중 제공자 모델 카탈로그, 2026년 7월 말에 종료되는 GitHub 모델을 대체)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## 허깅 페이스
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 아래 명령어로 해당 파일을 `.env`로 복사하십시오. 이 파일은 _gitignore_ 되어 있어 비밀을 안전하게 보호합니다.

   ```bash
   cp .env.copy .env
   ```

3. 다음 섹션에서 설명하는 대로 값(= 오른쪽의 자리 표시자)을 채웁니다.

4. (선택 사항) GitHub Codespaces를 사용하는 경우, 환경 변수를 이 리포지토리와 연관된 _Codespaces 비밀_로 저장할 수 있습니다. 이 경우 로컬 .env 파일 설정이 필요 없습니다. **단, 이 옵션은 GitHub Codespaces를 사용하는 경우에만 작동합니다.** Docker Desktop을 사용하는 경우 .env 파일 설정이 여전히 필요합니다.

## `.env` 파일 내용 채우기

변수 이름이 의미하는 바를 간단히 살펴보겠습니다:

| 변수명  | 설명  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 프로필에서 설정한 사용자 액세스 토큰 |
| OPENAI_API_KEY | 비 Azure OpenAI 엔드포인트 서비스용 인증 키 |
| AZURE_OPENAI_API_KEY | 해당 서비스용 인증 키 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 리소스의 배포된 엔드포인트 |
| AZURE_OPENAI_DEPLOYMENT | _텍스트 생성_ 모델 배포 엔드포인트 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _텍스트 임베딩_ 모델 배포 엔드포인트 |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry 프로젝트용 엔드포인트 (Microsoft Foundry Models 용) |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry 프로젝트의 API 키 |
| | |

참고: 마지막 두 개의 Azure OpenAI 변수는 각각 챗 생성(텍스트 생성)과 벡터 검색(임베딩)에 대한 기본 모델을 나타냅니다. 구성 방법은 관련 과제에서 설명됩니다.

## Azure OpenAI 구성: 포털에서

> **참고:** Azure OpenAI 서비스는 현재 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)의 일부입니다. 리소스와 배포 판은 여전히 Azure 포털에서 확인 가능하지만, 일상적인 모델 관리(배포, 플레이그라운드, 모니터링)는 기존 독립형 "Azure OpenAI Studio" 대신 Foundry 포털에서 이루어집니다.

Azure OpenAI 엔드포인트와 키 값은 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있으니, 그곳에서 시작합시다.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)로 이동
1. 사이드바(왼쪽 메뉴)에서 **Keys and Endpoint** 옵션 클릭
1. **키 표시(Show Keys)** 클릭 - KEY 1, KEY 2 및 엔드포인트 항목이 표시됩니다.
1. KEY 1 값을 AZURE_OPENAI_API_KEY에 사용
1. 엔드포인트 값을 AZURE_OPENAI_ENDPOINT에 사용

다음으로, 배포한 특정 모델의 엔드포인트가 필요합니다.

1. Azure OpenAI 리소스의 사이드바(왼쪽 메뉴)에서 **Model deployments** 옵션 클릭
1. 대상 페이지에서 **Microsoft Foundry 포털로 이동** (또는 리소스 유형에 따라 **배포 관리** 클릭)

이 작업으로 Microsoft Foundry 포털에 접근하게 되며, 아래 설명된 다른 값을 찾을 수 있습니다.

## Azure OpenAI 구성: Microsoft Foundry 포털에서

1. 앞서 설명한 대로 [Microsoft Foundry 포털](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)로 이동(리소스에서)
1. 배포된 모델을 확인하려면 사이드바 왼쪽의 **Deployments** 탭 클릭
1. 원하는 모델이 배포되지 않았다면, [모델 카탈로그](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)에서 <strong>모델 배포</strong>를 통해 배포
1. _텍스트 생성_ 모델이 필요하며, 추천 모델은 **gpt-4o-mini**
1. _텍스트 임베딩_ 모델이 필요하며, 추천 모델은 **text-embedding-3-small**

이제 환경 변수를 해당 _배포 이름_으로 업데이트하십시오. 보통 모델명과 동일하지만 명시적으로 변경한 경우 다를 수 있습니다. 예를 들어:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**작업 완료 후 .env 파일 저장을 잊지 마십시오**. 파일을 종료하고 노트북 실행 지침으로 돌아가십시오.

## OpenAI 구성: 프로필에서

OpenAI API 키는 [OpenAI 계정](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 계정이 없다면 가입 후 API 키를 생성할 수 있습니다. 키가 있으면 `.env` 파일 내 `OPENAI_API_KEY` 변수에 입력하세요.

## Hugging Face 구성: 프로필에서

Hugging Face 토큰은 프로필 아래의 [액세스 토큰](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 이를 공개적으로 게시하거나 공유하지 마십시오. 대신 프로젝트 사용을 위해 새 토큰을 생성한 후 `.env` 파일의 `HUGGING_FACE_API_KEY` 변수에 복사하세요. _참고:_ 엄밀히 말하면 API 키는 아니지만 인증에 사용되므로 명명 규칙을 일관성 있게 유지합니다.

## Microsoft Foundry Models 구성: 포털에서

> **참고:** GitHub Models는 2026년 7월 말 종료 예정입니다. Microsoft Foundry Models가 직접적인 대체 수단이며, 동일한 무료 체험 모델 카탈로그와 Azure AI 추론 SDK / OpenAI SDK 경험을 제공합니다.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)로 이동해 Foundry 프로젝트 생성 또는 열기
1. [모델 카탈로그](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 탐색 후 예를 들어 `gpt-4o-mini` 모델 배포
1. 프로젝트의 <strong>개요</strong> 페이지에서 <strong>엔드포인트</strong> 및 **API 키** 복사
1. `.env` 파일 내 `AZURE_INFERENCE_ENDPOINT` 변수에 엔드포인트 값, `AZURE_INFERENCE_CREDENTIAL` 변수에 키 값 입력

## 오프라인 / 로컬 공급자

클라우드 구독 없이 호환 가능한 오픈 모델을 직접 장치에서 실행하고자 하는 경우:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft의 장치 내 런타임입니다. 최적 실행 공급자(NPU, GPU, CPU)를 자동으로 선택하며 OpenAI 호환 엔드포인트를 제공합니다. 이 과제의 대부분 샘플 코드를 최소한의 변경으로 재사용할 수 있습니다. 시작하려면 [Foundry Local 문서](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 참고 또는 `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS)로 설치하세요.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral, Gemma 등 오픈 모델을 로컬에서 실행할 수 있는 인기 대안입니다.


두 옵션을 모두 사용한 실습 예제는 [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)를 참조하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->