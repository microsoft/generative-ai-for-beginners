# LLM 공급자 선택 및 구성 🔑

과제는 OpenAI, Azure 또는 Hugging Face와 같은 지원되는 서비스 공급자를 통해 하나 이상의 대형 언어 모델(LLM) 배포에 대해 작동하도록 설정할 수도 있습니다. 이들은 올바른 자격 증명(API 키 또는 토큰)으로 프로그래밍 방식으로 액세스할 수 있는 _호스팅된 엔드포인트_(API)를 제공합니다. 이 과정에서는 다음 공급자에 대해 다룹니다:

 - 다양한 모델을 포함한 [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) (핵심 GPT 시리즈 포함)
 - 엔터프라이즈 준비에 중점을 둔 OpenAI 모델용 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)
 - 오픈 소스 모델 및 추론 서버용 [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)

**이 연습을 위해서는 본인의 계정을 사용해야 합니다**. 과제는 선택 사항이므로 관심에 따라 하나, 모두 또는 전혀 공급자를 설정하지 않을 수 있습니다. 가입에 대한 몇 가지 안내:

| 가입 | 비용 | API 키 | 플레이그라운드 | 비고 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [가격](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [프로젝트 기반](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [노코드, 웹](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 다양한 모델 사용 가능 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [가격](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [스튜디오 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [접근 권한 사전 신청 필요](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [가격](https://huggingface.co/pricing) | [액세스 토큰](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat은 제한된 모델 제공](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

아래 지침에 따라 이 저장소를 다양한 공급자와 함께 사용하도록 _구성_하세요. 특정 공급자가 필요한 과제는 파일 이름에 다음 태그 중 하나를 포함합니다:

- `aoai` - Azure OpenAI 엔드포인트, 키 필요
- `oai` - OpenAI 엔드포인트, 키 필요
- `hf` - Hugging Face 토큰 필요

하나, 전혀, 또는 모든 공급자를 구성할 수 있습니다. 관련 과제는 자격 증명이 없으면 오류가 발생합니다.

## `.env` 파일 생성

위 안내를 읽고 관련 공급자에 가입하여 필요한 인증 자격 증명(API_KEY 또는 토큰)을 이미 받았다고 가정합니다. Azure OpenAI의 경우, 최소 하나의 GPT 모델이 배포된 Azure OpenAI 서비스(엔드포인트)가 유효하게 배포되어 있다고 가정합니다.

다음 단계는 **로컬 환경 변수**를 다음과 같이 구성하는 것입니다:

1. 루트 폴더에서 `.env.copy` 파일을 찾으세요. 내용은 다음과 유사해야 합니다:

   ```bash
   # OpenAI 공급자
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # 기본값이 설정되었습니다!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## 허깅페이스
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 아래 명령어로 해당 파일을 `.env`로 복사하세요. 이 파일은 _gitignore_ 처리되어 비밀을 안전하게 유지합니다.

   ```bash
   cp .env.copy .env
   ```

3. 다음 섹션에 설명된 대로 값을 채우세요(`=` 오른쪽의 자리 표시자 교체).

4. (선택 사항) GitHub Codespaces를 사용하는 경우, 이 저장소와 연결된 _Codespaces 비밀_로 환경 변수를 저장할 수 있습니다. 이 경우 로컬 .env 파일을 설정할 필요가 없습니다. **단, 이 옵션은 GitHub Codespaces를 사용할 때만 작동합니다.** Docker Desktop을 사용하는 경우에는 여전히 .env 파일을 설정해야 합니다.

## `.env` 파일 채우기

변수 이름이 무엇을 나타내는지 빠르게 살펴보겠습니다:

| 변수  | 설명  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 프로필에서 설정한 사용자 액세스 토큰 |
| OPENAI_API_KEY | 비-Azure OpenAI 엔드포인트용 서비스 인증 키 |
| AZURE_OPENAI_API_KEY | 해당 서비스 인증 키 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 리소스의 배포된 엔드포인트 |
| AZURE_OPENAI_DEPLOYMENT | _텍스트 생성_ 모델 배포 엔드포인트 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _텍스트 임베딩_ 모델 배포 엔드포인트 |
| | |

참고: 마지막 두 Azure OpenAI 변수는 각각 채팅 완성(텍스트 생성) 및 벡터 검색(임베딩)에 대한 기본 모델을 반영합니다. 설정 방법은 관련 과제에서 정의됩니다.

## Azure 구성: 포털에서

Azure OpenAI 엔드포인트 및 키 값은 [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있으므로 여기서 시작합니다.

1. [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)로 이동합니다.
1. 사이드바(왼쪽 메뉴)에서 **키 및 엔드포인트** 옵션을 클릭합니다.
1. **키 표시**를 클릭하면 다음이 표시됩니다: KEY 1, KEY 2 및 엔드포인트.
1. AZURE_OPENAI_API_KEY에 KEY 1 값을 사용합니다.
1. AZURE_OPENAI_ENDPOINT에 엔드포인트 값을 사용합니다.

다음으로, 배포한 특정 모델의 엔드포인트가 필요합니다.

1. Azure OpenAI 리소스의 사이드바(왼쪽 메뉴)에서 **모델 배포** 옵션을 클릭합니다.
1. 대상 페이지에서 **배포 관리**를 클릭합니다.

이렇게 하면 Azure OpenAI Studio 웹사이트로 이동하며, 아래 설명된 다른 값을 찾을 수 있습니다.

## Azure 구성: 스튜디오에서

1. 위에서 설명한 대로 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **리소스에서** 이동합니다.
1. 현재 배포된 모델을 보려면 사이드바(왼쪽)에서 **배포** 탭을 클릭합니다.
1. 원하는 모델이 배포되어 있지 않으면 **새 배포 생성**을 사용해 배포하세요.
1. _텍스트 생성_ 모델이 필요합니다 - 권장: **gpt-35-turbo**
1. _텍스트 임베딩_ 모델이 필요합니다 - 권장: **text-embedding-ada-002**

이제 환경 변수를 _배포 이름_에 맞게 업데이트하세요. 일반적으로 모델 이름과 같지만 명시적으로 변경한 경우 다를 수 있습니다. 예를 들어 다음과 같을 수 있습니다:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**완료 후 .env 파일 저장을 잊지 마세요**. 이제 파일을 닫고 노트북 실행 지침으로 돌아가면 됩니다.

## OpenAI 구성: 프로필에서

OpenAI API 키는 [OpenAI 계정](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 계정이 없으면 가입 후 API 키를 생성할 수 있습니다. 키를 받으면 `.env` 파일의 `OPENAI_API_KEY` 변수에 입력하세요.

## Hugging Face 구성: 프로필에서

Hugging Face 토큰은 프로필의 [액세스 토큰](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다. 이를 공개적으로 게시하거나 공유하지 마세요. 대신 이 프로젝트 용도로 새 토큰을 생성하고 `.env` 파일의 `HUGGING_FACE_API_KEY` 변수에 복사하세요. _참고:_ 기술적으로 API 키는 아니지만 인증에 사용되므로 일관성을 위해 이 명명법을 유지합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->