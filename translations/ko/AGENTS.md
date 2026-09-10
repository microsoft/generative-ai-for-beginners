# AGENTS.md

## 프로젝트 개요

이 저장소에는 생성 AI 기본 원리와 애플리케이션 개발을 가르치는 21개의 수업으로 구성된 포괄적인 커리큘럼이 포함되어 있습니다. 이 과정은 초보자를 대상으로 하며 기본 개념부터 프로덕션 준비 애플리케이션 구축까지 모두 다룹니다.

**핵심 기술:**
- 라이브러리와 함께 Python 3.9+: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- Node.js와 라이브러리와 함께 TypeScript/JavaScript: `openai` (v1 엔드포인트 및 응답 API를 통한 Azure OpenAI), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI 서비스, OpenAI API, Microsoft Foundry Models (GitHub Models는 2026년 7월 말에 종료 예정)
- 대화형 학습을 위한 Jupyter 노트북
- 일관된 개발 환경을 위한 개발 컨테이너

**저장소 구조:**
- README, 코드 예제, 과제가 포함된 번호가 매겨진 21개 수업 디렉터리 (00-21)
- Python, TypeScript 그리고 때때로 .NET 예제의 다중 구현
- 40개 이상의 언어 버전을 포함한 번역 디렉터리
- `.env` 파일을 통한 중앙 집중식 구성 (`.env.copy`를 템플릿으로 사용)

## 설정 명령

### 초기 저장소 설정

```bash
# 저장소를 복제하세요
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 환경 템플릿을 복사하세요
cp .env.copy .env
# .env 파일을 API 키와 엔드포인트로 수정하세요
```

### Python 환경 설정

```bash
# 가상 환경 생성
python3 -m venv venv

# 가상 환경 활성화
# macOS/Linux에서:
source venv/bin/activate
# Windows에서:
venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### Node.js/TypeScript 설정

```bash
# 루트 수준 의존성 설치 (문서 도구용)
npm install

# 개별 수업 TypeScript 예제를 보려면 특정 수업으로 이동하세요:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### 개발 컨테이너 설정 (권장)

이 저장소는 GitHub Codespaces 또는 VS Code Dev Containers용 `.devcontainer` 구성을 포함합니다:

1. 저장소를 GitHub Codespaces 또는 Dev Containers 확장 기능이 있는 VS Code에서 엽니다
2. 개발 컨테이너가 자동으로 다음을 수행합니다:
   - `requirements.txt`에서 Python 종속성 설치
   - post-create 스크립트 실행 (`.devcontainer/post-create.sh`)
   - Jupyter 커널 설정

## 개발 워크플로우

### 환경 변수

API 접근이 필요한 모든 수업은 `.env`에 정의된 환경 변수를 사용합니다:

- `OPENAI_API_KEY` - OpenAI API용
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry 내 Azure OpenAI용 (Azure OpenAI 서비스는 현재 Microsoft Foundry의 일부: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 엔드포인트 URL (Foundry 리소스 엔드포인트)
- `AZURE_OPENAI_DEPLOYMENT` - 채팅 완성 모델 배포 이름 (과정 기본값: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 임베딩 모델 배포 이름 (과정 기본값: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API 버전 (기본값: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face 모델용
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models 엔드포인트 (멀티 제공자 모델 카탈로그)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API 키 (`GITHUB_TOKEN` 종료 대체)
- `AZURE_INFERENCE_CHAT_MODEL` - 비추론 모델 (예: `Llama-3.3-70B-Instruct`)으로, `temperature` 예제에서 사용. 추론 모델은 샘플링 제어를 지원하지 않음

### 모델 규칙 (중요)

- **기본 채팅 모델은 `gpt-5-mini`<strong> - 현재 사용 중이고 폐기되지 않은 </strong>추론(reasoning)** 모델입니다. 2026년 기준으로 이전의 온도 제어 가능한 "미니" 모델(`gpt-4o-mini`, `gpt-4.1-mini`)은 <em>폐기</em> 중이라 커리큘럼은 GPT-5 가족으로 표준화합니다.
- **추론 모델은 `temperature`와 `top_p`를 거부**하며, `max_output_tokens` (Responses API) / `max_completion_tokens` (챗 완성) 을 `max_tokens` 대신 사용합니다. `gpt-5-mini`를 호출하는 샘플에 `temperature`/`top_p`/`max_tokens`를 추가하지 마세요.
- **`temperature`를 보여주기 위해** Microsoft Foundry Models 엔드포인트(`AZURE_INFERENCE_CHAT_MODEL`)로 **Llama** 모델(`Llama-3.3-70B-Instruct`)을 사용합니다. 추론 모델은 샘플링 조절 대신 프롬프트 엔지니어링과 추론 제어를 사용해 조절하세요.
- <strong>미세 조정(lesson 18)</strong>에서는 `gpt-4.1-mini`를 유지합니다: GPT-5는 강화 학습 미세 조정(RFT)만 지원하고, 여기서 보여주는 감독 학습 미세 조정(SFT)은 지원하지 않습니다.
- 20강(Mistral)과 21강(Meta)은 Mistral/Llama 모델 대상으로 `temperature`/`max_tokens`를 유지합니다.

### Python 예제 실행

```bash
# 수업 디렉토리로 이동
cd 06-text-generation-apps/python

# 파이썬 스크립트를 실행하세요
python aoai-app.py
```

### TypeScript 예제 실행

```bash
# TypeScript 앱 디렉토리로 이동
cd 06-text-generation-apps/typescript/recipe-app

# TypeScript 코드 빌드
npm run build

# 애플리케이션 실행
npm start
```

### Jupyter 노트북 실행

```bash
# 저장소 루트에서 Jupyter 시작
jupyter notebook

# 또는 Jupyter 확장 기능이 있는 VS Code 사용
```

### 다양한 수업 유형 작업

- **"Learn" 수업**: README.md 문서와 개념에 집중
- **"Build" 수업**: Python과 TypeScript 작업 코드 예제 포함
- 각 수업은 이론, 코드 설명, 동영상 링크가 포함된 README.md가 있음

## 코드 스타일 가이드

### Python

- 환경 변수 관리를 위해 `python-dotenv` 사용
- API 상호작용에 `openai` 라이브러리 임포트
- Linting에 `pylint` 사용 (일부 예제는 단순화를 위해 `# pylint: disable=all` 포함)
- PEP 8 명명 규칙 준수
- API 자격 증명은 코드에 저장하지 말고 `.env` 파일에 보관

### TypeScript

- 환경 변수에 `dotenv` 패키지 사용
- 각 앱별 `tsconfig.json`에 TypeScript 구성
- Azure OpenAI용으로 `openai` 패키지 사용 (`/openai/v1/` 엔드포인트 지정 후 `client.responses.create` 호출); Microsoft Foundry Models용으로 `@azure-rest/ai-inference` 사용
- 자동 재시작 개발용 `nodemon` 사용
- 실행 전 빌드: `npm run build` 후 `npm start`

### 일반 규칙

- 코드 예제를 단순하고 교육적으로 유지
- 핵심 개념 설명 주석 포함
- 각 수업 코드는 독립 실행 가능해야 함
- 일관된 명명법 사용: Azure OpenAI는 `aoai-` 접두어, OpenAI API는 `oai-`, Microsoft Foundry Models는 `githubmodels-` (GitHub Models 시대에서 유래한 접두어 유지)

## 문서 작성 지침

### 마크다운 스타일

- 모든 URL은 `[text](../../url)` 형식으로 작성, 추가 공백 금지
- 상대 링크는 `./` 또는 `../`로 시작
- Microsoft 도메인 링크는 모두 추적 ID 포함: `?WT.mc_id=academic-105485-koreyst`
- 국가별 로케일 포함 URL 금지 (예: `/en-us/` 사용 지양)
- 이미지는 `./images` 폴더에 설명적 이름으로 저장
- 파일 이름에 영문자, 숫자, 대시 사용

### 번역 지원

- 저장소는 40개 이상의 언어를 자동 GitHub Actions로 지원
- 번역은 `translations/` 디렉터리에 저장
- 부분 번역 제출 금지
- 기계 번역 불가
- 번역된 이미지는 `translated_images/` 디렉터리에 저장

## 테스트 및 검증

### 제출 전 확인

이 저장소는 검증에 GitHub Actions를 사용합니다. PR 제출 전:

1. **마크다운 링크 확인**:
   ```bash
   # validate-markdown.yml 워크플로는 다음을 검사합니다:
   # - 깨진 상대 경로
   # - 경로에 누락된 추적 ID
   # - URL에 누락된 추적 ID
   # - 국가 로케일이 포함된 URL
   # - 깨진 외부 URL
   ```

2. **수동 테스트**:
   - Python 예제 테스트: 가상 환경 활성화 후 스크립트 실행
   - TypeScript 예제 테스트: `npm install`, `npm run build`, `npm start`
   - 환경 변수 올바르게 구성되었는지 확인
   - 코드 예제와 함께 API 키 동작 확인

3. **코드 예제**:
   - 모든 코드가 오류 없이 실행되는지 확인
   - 해당 시 Azure OpenAI와 OpenAI API 모두에서 테스트
   - Microsoft Foundry Models 지원 시 예제 동작 확인

### 자동화된 테스트 없음

이 저장소는 튜토리얼과 예제 중심의 교육용입니다. 단위 테스트나 통합 테스트는 없습니다. 검증 방법은 주로:
- 코드 예제의 수동 테스트
- 마크다운 검증을 위한 GitHub Actions
- 교육 콘텐츠에 대한 커뮤니티 검토

## 풀 리퀘스트 가이드라인

### 제출 전

1. 적용 가능한 경우 Python과 TypeScript 모두에서 코드 변경 테스트
2. 마크다운 검증 실행 (PR 시 자동 실행)
3. 모든 Microsoft URL에 추적 ID 포함 확인
4. 상대 링크가 유효한지 확인
5. 이미지가 제대로 참조되고 있는지 확인

### PR 제목 형식

- 설명적인 제목 사용: `[Lesson 06] Python 예제 오타 수정` 또는 `lesson 08 README 업데이트`
- 해당 시 이슈 번호 참조: `Fixes #123`

### PR 설명

- 변경 내용과 이유 설명
- 관련 이슈 링크 포함
- 코드 변경 시 테스트한 예제 명시
- 번역 PR의 경우 완전한 번역을 위해 모든 파일 포함

### 기여 요건

- Microsoft CLA 서명 (첫 PR 시 자동)
- 변경 전 저장소를 내 계정으로 포크
- 논리적 변경당 하나의 PR 제출 (무관한 수정 병합 금지)
- 가능하면 PR은 집중되고 작게 유지

## 일반 워크플로우

### 새 코드 예제 추가

1. 적절한 수업 디렉터리로 이동
2. `python/` 또는 `typescript/` 하위 디렉터리에 예제 생성
3. 명명 규칙 준수: `{provider}-{example-name}.{py|ts|js}`
4. 실제 API 자격 증명으로 테스트
5. 새로운 환경 변수는 수업 README에 문서화

### 문서 업데이트

1. 수업 디렉터리의 README.md 편집
2. 마크다운 가이드라인(추적 ID, 상대 링크) 준수
3. 번역은 GitHub Actions가 처리 (수동 편집 금지)
4. 모든 링크 유효성 테스트

### 개발 컨테이너 작업

1. 저장소에 `.devcontainer/devcontainer.json` 포함
2. 포스트 생성 스크립트가 Python 종속성 자동 설치
3. Python과 Jupyter 확장 사전 구성
4. 환경이 `mcr.microsoft.com/devcontainers/universal:2.11.2` 기준

## 배포 및 게시

이 저장소는 학습용 - 배포 과정은 없습니다. 커리큘럼은 다음을 통해 활용됩니다:

1. **GitHub 저장소**: 코드와 문서 직접 접근
2. **GitHub Codespaces**: 사전 설정된 즉각적 개발 환경
3. **Microsoft Learn**: 공식 학습 플랫폼에 콘텐츠가 배포될 수 있음
4. **docsify**: 마크다운에서 빌드된 문서 사이트 (`docsifytopdf.js` 및 `package.json` 참고)

### 문서 사이트 빌드

```bash
# 문서에서 PDF 생성 (필요한 경우)
npm run convert
```

## 문제 해결

### 일반 문제

**Python 임포트 오류**:
- 가상 환경이 활성화되어 있는지 확인
- `pip install -r requirements.txt` 실행
- Python 버전이 3.9 이상인지 확인

**TypeScript 빌드 오류**:
- 해당 앱 디렉터리에서 `npm install` 실행
- Node.js 버전이 호환되는지 확인
- 필요 시 `node_modules` 삭제 후 재설치

**API 인증 오류**:
- `.env` 파일이 존재하고 올바른 값인지 확인
- API 키가 유효하고 만료되지 않았는지 확인
- 지역에 맞는 엔드포인트 URL 사용 확인

**환경 변수 누락**:
- `.env.copy`를 `.env`로 복사
- 작업 중인 수업에 필요한 모든 값 입력
- `.env` 업데이트 후 애플리케이션 재시작

## 추가 자료

- [과정 설정 가이드](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [기여 지침](./CONTRIBUTING.md)
- [행동 강령](./CODE_OF_CONDUCT.md)
- [보안 정책](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [고급 코드 샘플 모음](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 프로젝트 관련 참고 사항

- 이 저장소는 <strong>교육용 저장소</strong>로, 학습에 중점을 두고 있으며 프로덕션 코드는 아님
- 예제는 의도적으로 단순하며 개념 교육에 집중
- 코드 품질과 교육적 명확성의 균형 유지
- 각 수업은 독립적으로 완성할 수 있음
- 저장소는 Azure OpenAI, OpenAI, Microsoft Foundry Models 및 Foundry Local과 Ollama 같은 오프라인 제공자를 모두 지원
- 콘텐츠는 다국어 및 자동화된 번역 워크플로우 지원
- 질문과 지원을 위한 활발한 Discord 커뮤니티 운영

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->