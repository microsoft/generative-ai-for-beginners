<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T15:14:33+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ko"
}
-->
# LLM 공급자 선택 및 설정 🔑

과제는 OpenAI, Azure, Hugging Face와 같은 지원되는 서비스 공급자를 통해 하나 이상의 대형 언어 모델(LLM) 배포와 연동되도록 설정할 수 있습니다. 이들 서비스는 _호스팅된 엔드포인트_ (API)를 제공하며, 적절한 인증 정보(API 키 또는 토큰)로 프로그래밍 방식으로 접근할 수 있습니다. 이 과정에서는 다음과 같은 공급자들을 다룹니다:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst): GPT 시리즈를 포함한 다양한 모델 제공
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst): 엔터프라이즈 환경에 적합한 OpenAI 모델 제공
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst): 오픈소스 모델 및 추론 서버 제공

**이 실습을 위해서는 각자 계정을 사용해야 합니다.** 과제는 선택 사항이므로, 관심에 따라 하나, 모두, 또는 아무 공급자도 설정하지 않아도 됩니다. 가입 관련 안내는 다음과 같습니다:

| 가입 | 비용 | API 키 | 플레이그라운드 | 비고 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [가격](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [프로젝트 기반](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [노코드, 웹](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 다양한 모델 제공 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [가격](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 빠른 시작](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [사전 신청 필요](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [가격](https://huggingface.co/pricing) | [액세스 토큰](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat은 모델이 제한적임](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

아래 안내에 따라 이 저장소를 다양한 공급자와 함께 사용할 수 있도록 _설정_하세요. 특정 공급자가 필요한 과제는 파일명에 다음과 같은 태그가 포함되어 있습니다:

- `aoai` - Azure OpenAI 엔드포인트 및 키 필요
- `oai` - OpenAI 엔드포인트 및 키 필요
- `hf` - Hugging Face 토큰 필요

공급자를 하나도, 일부만, 또는 모두 설정할 수 있습니다. 관련 과제는 인증 정보가 없으면 오류가 발생합니다.

## `.env` 파일 생성

위 안내를 이미 읽고 관련 공급자에 가입하여 필요한 인증 정보(API_KEY 또는 토큰)를 받았다고 가정합니다. Azure OpenAI의 경우, 최소 하나의 GPT 모델이 배포된 Azure OpenAI 서비스(엔드포인트)가 있어야 합니다.

다음 단계는 **로컬 환경 변수**를 다음과 같이 설정하는 것입니다:

1. 루트 폴더에서 `.env.copy` 파일을 찾으세요. 내용은 다음과 비슷할 것입니다:

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

2. 아래 명령어로 해당 파일을 `.env`로 복사하세요. 이 파일은 _gitignore_ 처리되어 비밀 정보가 안전하게 보호됩니다.

   ```bash
   cp .env.copy .env
   ```

3. 다음 섹션에 설명된 대로 값을 채워주세요(`=` 오른쪽의 플레이스홀더를 실제 값으로 교체).

4. (선택) GitHub Codespaces를 사용하는 경우, 환경 변수를 이 저장소에 연결된 _Codespaces secrets_로 저장할 수 있습니다. 이 경우 로컬 .env 파일을 따로 설정할 필요가 없습니다. **단, 이 옵션은 GitHub Codespaces를 사용할 때만 적용됩니다.** Docker Desktop을 사용하는 경우에는 .env 파일을 반드시 설정해야 합니다.

## `.env` 파일 값 채우기

변수명이 의미하는 바를 간단히 살펴보겠습니다:

| 변수명  | 설명  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 프로필에서 설정한 사용자 액세스 토큰 |
| OPENAI_API_KEY | Azure가 아닌 OpenAI 엔드포인트용 서비스 인증 키 |
| AZURE_OPENAI_API_KEY | 해당 서비스용 인증 키 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 리소스의 배포된 엔드포인트 |
| AZURE_OPENAI_DEPLOYMENT | _텍스트 생성_ 모델 배포 엔드포인트 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _텍스트 임베딩_ 모델 배포 엔드포인트 |
| | |

참고: 마지막 두 Azure OpenAI 변수는 각각 채팅 완성(텍스트 생성)과 벡터 검색(임베딩)에 사용할 기본 모델을 나타냅니다. 값 설정 방법은 관련 과제에서 안내됩니다.

## Azure 설정: 포털에서

Azure OpenAI 엔드포인트와 키 값은 [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다.

1. [Azure 포털](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)에 접속하세요.
1. 왼쪽 메뉴에서 **Keys and Endpoint** 옵션을 클릭하세요.
1. **Show Keys**를 클릭하면 KEY 1, KEY 2, Endpoint가 표시됩니다.
1. AZURE_OPENAI_API_KEY에는 KEY 1 값을 사용하세요.
1. AZURE_OPENAI_ENDPOINT에는 Endpoint 값을 사용하세요.

다음으로, 배포한 특정 모델의 엔드포인트가 필요합니다.

1. Azure OpenAI 리소스의 왼쪽 메뉴에서 **Model deployments** 옵션을 클릭하세요.
1. 해당 페이지에서 **Manage Deployments**를 클릭하세요.

이제 Azure OpenAI Studio 웹사이트로 이동하여 아래에 설명된 다른 값을 찾을 수 있습니다.

## Azure 설정: 스튜디오에서

1. 위에서 설명한 대로 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)로 **리소스에서 이동**하세요.
1. 왼쪽 사이드바의 **Deployments** 탭을 클릭하여 현재 배포된 모델을 확인하세요.
1. 원하는 모델이 배포되어 있지 않다면 **Create new deployment**로 새로 배포하세요.
1. _텍스트 생성_ 모델이 필요합니다 - **gpt-35-turbo**를 추천합니다.
1. _텍스트 임베딩_ 모델이 필요합니다 - **text-embedding-ada-002**를 추천합니다.

이제 환경 변수에 _배포 이름_을 반영하여 값을 업데이트하세요. 별도로 변경하지 않았다면 모델명과 동일합니다. 예를 들어 다음과 같이 설정할 수 있습니다:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**작업이 끝나면 .env 파일 저장을 잊지 마세요.** 이제 파일을 닫고 노트북 실행 안내로 돌아가면 됩니다.

## OpenAI 설정: 프로필에서

OpenAI API 키는 [OpenAI 계정](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다. 계정이 없다면 가입 후 API 키를 생성하세요. 키를 받으면 `.env` 파일의 `OPENAI_API_KEY` 변수에 입력하면 됩니다.

## Hugging Face 설정: 프로필에서

Hugging Face 토큰은 프로필의 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다. 이 토큰을 공개적으로 게시하거나 공유하지 마세요. 이 프로젝트용으로 새 토큰을 생성한 뒤, `.env` 파일의 `HUGGING_FACE_API_KEY` 변수에 복사하세요. _참고:_ 기술적으로는 API 키가 아니지만 인증에 사용되므로 명칭을 통일했습니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.