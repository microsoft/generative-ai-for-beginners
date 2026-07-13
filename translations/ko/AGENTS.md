# AGENTS.md

## 프로젝트 개요

이 저장소에는 생성형 AI 기초와 애플리케이션 개발을 가르치는 총 21개의 강의 커리큘럼이 포함되어 있습니다. 이 과정은 초보자를 대상으로 하며 기본 개념부터 실전 준비 애플리케이션 구축까지 모두 다룹니다.

**핵심 기술:**
- Python 3.9+ 및 라이브러리: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript (Node.js 사용) 및 라이브러리: `openai` (Azure OpenAI v1 엔드포인트 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI 서비스, OpenAI API, Microsoft Foundry Models (GitHub Models는 2026년 7월 말에 종료 예정)
- 대화형 학습을 위한 주피터 노트북
- 일관된 개발 환경을 위한 Dev Containers

**저장소 구조:**
- 21개 번호가 지정된 강의 디렉토리(00-21), README, 코드 예제, 과제 포함
- 다중 구현: Python, TypeScript, 때때로 .NET 예제 포함
- 40개 이상의 언어 버전을 포함하는 번역 디렉토리
- `.env` 파일을 통한 중앙 구성 (템플릿으로 `.env.copy` 사용)

## 설정 명령어

### 초기 저장소 설정

```bash
# 저장소를 복제하세요
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 환경 템플릿을 복사하세요
cp .env.copy .env
# API 키와 엔드포인트로 .env 파일을 편집하세요
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
# 루트 수준 종속성 설치(문서화 도구용)
npm install

# 개별 수업 TypeScript 예제는 특정 수업으로 이동하세요:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container 설정 (권장)

저장소에는 GitHub Codespaces 또는 VS Code Dev Containers를 위한 `.devcontainer` 구성이 포함되어 있습니다:

1. GitHub Codespaces 또는 VS Code에서 Dev Containers 확장 기능과 함께 저장소 열기
2. Dev Container는 자동으로 다음을 수행합니다:
   - `requirements.txt`로부터 Python 종속성 설치
   - post-create 스크립트(`.devcontainer/post-create.sh`) 실행
   - Jupyter 커널 설정

## 개발 워크플로우

### 환경 변수

API 접근이 필요한 모든 강의는 `.env`에 정의된 환경 변수를 사용합니다:

- `OPENAI_API_KEY` - OpenAI API 용
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry의 Azure OpenAI 용 (Azure OpenAI 서비스는 현재 Microsoft Foundry 일부: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 엔드포인트 URL (Foundry 리소스 엔드포인트)
- `AZURE_OPENAI_DEPLOYMENT` - 채팅 완료 모델 배포 이름
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 임베딩 모델 배포 이름
- `AZURE_OPENAI_API_VERSION` - API 버전 (기본값: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face 모델용
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models 엔드포인트 (멀티 공급자 모델 카탈로그)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API 키 (`GITHUB_TOKEN`을 대체, 곧 종료 예정)

### Python 예제 실행

```bash
# 레슨 디렉토리로 이동
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

### 주피터 노트북 실행

```bash
# 저장소 루트에서 Jupyter 시작
jupyter notebook

# 또는 Jupyter 확장 기능이 있는 VS Code 사용
```

### 다양한 강의 유형 작업하기

- **"학습(Learn)" 강의**: README.md 문서 및 개념 중심
- **"구축(Build)" 강의**: Python 및 TypeScript로 된 작동하는 코드 예제 포함
- 각 강의는 이론, 코드 해설, 비디오 콘텐츠 링크가 포함된 README.md를 가짐

## 코드 스타일 지침

### Python

- 환경 변수 관리를 위해 `python-dotenv` 사용
- API 상호작용을 위해 `openai` 라이브러리 임포트
- 린팅을 위해 `pylint` 사용 (일부 예제는 간편히 `# pylint: disable=all` 포함)
- PEP 8 명명 규칙 준수
- API 자격 증명은 `.env` 파일에 보관, 코드 내에서는 절대 포함하지 않음

### TypeScript

- 환경 변수를 위해 `dotenv` 패키지 사용
- 각 앱에 대한 `tsconfig.json` 내 TypeScript 구성
- Azure OpenAI용 `openai` 패키지 사용 (클라이언트를 `/openai/v1/` 엔드포인트 지정 후 `client.responses.create` 호출); Microsoft Foundry Models용으로 `@azure-rest/ai-inference` 사용
- 자동 재시작이 가능한 개발용 `nodemon` 사용
- 실행 전 빌드: `npm run build` 다음에 `npm start`

### 일반 규칙

- 코드 예제는 간단하고 교육적 목적에 맞게 유지
- 주요 개념에 대한 주석 포함
- 각 강의의 코드는 자립적이고 실행 가능해야 함
- 일관된 명명법 사용: Azure OpenAI는 `aoai-` 접두어, OpenAI API는 `oai-` 접두어, Microsoft Foundry Models는 `githubmodels-` 접두어 (GitHub Models 배경 접두어 유지)

## 문서 작성 지침

### 마크다운 스타일

- 모든 URL은 `[text](../../url)` 형식으로 여백 없이 감싸야 함
- 상대 링크는 `./` 또는 `../`로 시작해야 함
- Microsoft 도메인의 모든 링크에는 추적 ID 포함: `?WT.mc_id=academic-105485-koreyst`
- URL에 국가별 로케일 포함 금지 (예: `/en-us/` 사용하지 않음)
- 이미지 파일은 `./images` 폴더에 설명적인 이름으로 저장
- 파일명은 영문자, 숫자, 대시만 사용

### 번역 지원

- 저장소는 GitHub Actions를 통한 40개 이상의 언어를 지원
- 번역 파일은 `translations/` 디렉토리에 저장
- 부분 번역 제출 금지
- 기계 번역만 제출 불가
- 번역된 이미지는 `translated_images/` 디렉토리 보관

## 테스트 및 검증

### 제출 전 점검

이 저장소는 GitHub Actions를 사용한 검증을 진행합니다. PR 제출 전:

1. **마크다운 링크 점검**:
   ```bash
   # validate-markdown.yml 워크플로우는 다음을 확인합니다:
   # - 깨진 상대 경로
   # - 경로에 누락된 추적 ID
   # - URL에 누락된 추적 ID
   # - 국가 로케일이 포함된 URL
   # - 깨진 외부 URL
   ```

2. **수동 테스트**:
   - Python 예제 테스트: venv 활성화 후 스크립트 실행
   - TypeScript 예제 테스트: `npm install`, `npm run build`, `npm start`
   - 환경 변수 올바르게 설정되었는지 확인
   - API 키가 코드 예제와 연동되는지 점검

3. **코드 예제**:
   - 오류 없이 모든 코드 실행 확인
   - 가능하면 Azure OpenAI와 OpenAI API 모두 테스트
   - 지원되는 경우 Microsoft Foundry Models로 예제 정상 작동 여부 확인

### 자동 테스트 없음

본 저장소는 교육 목적의 튜토리얼 및 예제 중심입니다. 단위 테스트나 통합 테스트는 없습니다. 검증 방식은 주로:
- 코드 예제의 수동 테스트
- Markdown 검증을 위한 GitHub Actions
- 교육 콘텐츠에 대한 커뮤니티 리뷰

## 풀 리퀘스트 가이드라인

### 제출 전

1. 가능하면 Python과 TypeScript 모두에서 코드 변경 테스트
2. Markdown 검증 실행 (PR 시 자동 트리거)
3. 모든 Microsoft URL에 추적 ID 포함 여부 확인
4. 상대 링크가 유효한지 점검
5. 이미지 참조가 올바른지 확인

### PR 제목 형식

- 설명적인 제목 사용: `[Lesson 06] Python 예제 오타 수정` 또는 `강의 08 README 업데이트`
- 관련 이슈 번호 포함 시: `Fixes #123`

### PR 설명

- 변경 사항과 이유 설명
- 관련 이슈 링크 포함
- 코드 변경 시 테스트한 예제 명시
- 번역 PR인 경우 전체 번역 파일 포함

### 기여 조건

- Microsoft CLA 서명 (첫 PR 시 자동 처리)
- 변경 전 개인 계정으로 저장소 Fork
- 하나의 논리적 변경마다 하나의 PR (무관한 수정 병합 금지)
- 가능하면 PR을 작고 집중되게 유지

## 일반 워크플로우

### 새 코드 예제 추가

1. 적절한 강의 디렉토리로 이동
2. `python/` 또는 `typescript/` 하위 디렉토리에 예제 생성
3. 명명 규칙 준수: `{provider}-{example-name}.{py|ts|js}`
4. 실제 API 자격 증명으로 테스트
5. 새로운 환경 변수가 있다면 강의 README에 문서화

### 문서 업데이트

1. 강의 디렉토리 내 README.md 편집
2. Markdown 지침 준수 (추적 ID, 상대 링크)
3. 번역은 GitHub Actions에서 처리 (수동 편집 금지)
4. 모든 링크 정상 작동 여부 확인

### Dev Containers 사용 작업

1. 저장소에 `.devcontainer/devcontainer.json` 포함
2. post-create 스크립트가 Python 종속성 자동 설치
3. Python 및 Jupyter 확장 사전 구성됨
4. 환경은 `mcr.microsoft.com/devcontainers/universal:2.11.2` 기반

## 배포 및 게시

본 저장소는 학습 목적이며 배포 과정은 없습니다. 커리큘럼 이용 방식은:

1. **GitHub 저장소**: 코드 및 문서 직접 접근
2. **GitHub Codespaces**: 사전 구성된 개발 환경 즉시 사용 가능
3. **Microsoft Learn**: 공식 학습 플랫폼으로 콘텐츠 유통 가능
4. **docsify**: Markdown 기반 문서 사이트 구축 (관련 파일 `docsifytopdf.js`, `package.json` 참조)

### 문서 사이트 빌드

```bash
# 문서에서 PDF 생성 (필요한 경우)
npm run convert
```

## 문제 해결

### 일반 문제

**Python Import 오류**:
- 가상 환경이 활성화되었는지 확인
- `pip install -r requirements.txt` 실행
- Python 버전이 3.9 이상인지 확인

**TypeScript 빌드 오류**:
- 해당 앱 디렉토리에서 `npm install` 실행
- Node.js 버전 호환성 확인
- 필요 시 `node_modules` 삭제 후 재설치

**API 인증 오류**:
- `.env` 파일이 존재하고 값이 올바른지 점검
- API 키가 유효하고 만료되지 않았는지 확인
- 지역에 맞는 올바른 엔드포인트 URL 사용 여부 확인

**환경 변수 누락**:
- `.env.copy`를 `.env`로 복사
- 작업 중인 강의에 필요한 모든 값 입력
- `.env` 수정 후 애플리케이션 재시작

## 추가 리소스

- [강의 설정 가이드](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [기여 가이드라인](./CONTRIBUTING.md)
- [행동 강령](./CODE_OF_CONDUCT.md)
- [보안 정책](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [고급 코드 샘플 모음](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 프로젝트별 노트

- 본 저장소는 <strong>교육용 저장소</strong>이며 실전 코드가 아닙니다
- 예제는 의도적으로 단순하며 개념 교육에 집중함
- 코드 품질과 교육적 명확성의 균형 유지
- 각 강의는 독립적이며 별도 완료 가능
- 저장소는 여러 API 제공자를 지원: Azure OpenAI, OpenAI, Microsoft Foundry Models, 그리고 Foundry Local, Ollama 같은 오프라인 제공자 포함
- 콘텐츠는 다중 언어 지원과 자동 번역 워크플로우 보유
- 질문 및 지원을 위한 활성 디스코드 커뮤니티 운영

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->