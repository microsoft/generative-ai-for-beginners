<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:56:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ko"
}
-->
# AGENTS.md

## 프로젝트 개요

이 저장소는 생성형 AI의 기본 개념과 애플리케이션 개발을 가르치는 21개의 레슨 커리큘럼을 포함하고 있습니다. 이 과정은 초보자를 대상으로 하며, 기본 개념부터 실무 애플리케이션 구축까지 다룹니다.

**주요 기술:**
- Python 3.9+ 및 라이브러리: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript 및 Node.js 라이브러리: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI 서비스, OpenAI API, GitHub 모델
- 대화형 학습을 위한 Jupyter 노트북
- 일관된 개발 환경을 위한 Dev 컨테이너

**저장소 구조:**
- 21개의 번호가 매겨진 레슨 디렉토리(00-21)에는 README, 코드 예제, 과제가 포함됨
- Python, TypeScript, 때로는 .NET 예제를 포함한 여러 구현
- 40개 이상의 언어 버전을 포함한 번역 디렉토리
- `.env` 파일을 통한 중앙 집중식 구성 (`.env.copy`를 템플릿으로 사용)

## 설정 명령어

### 초기 저장소 설정

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python 환경 설정

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript 설정

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev 컨테이너 설정 (권장)

이 저장소는 GitHub Codespaces 또는 VS Code Dev 컨테이너를 위한 `.devcontainer` 구성을 포함합니다:

1. GitHub Codespaces 또는 VS Code에서 저장소를 엽니다 (Dev 컨테이너 확장 사용)
2. Dev 컨테이너는 자동으로 다음을 수행합니다:
   - `requirements.txt`에서 Python 종속성 설치
   - 포스트 생성 스크립트 실행 (`.devcontainer/post-create.sh`)
   - Jupyter 커널 설정

## 개발 워크플로우

### 환경 변수

API 액세스가 필요한 모든 레슨은 `.env`에 정의된 환경 변수를 사용합니다:

- `OPENAI_API_KEY` - OpenAI API용
- `AZURE_OPENAI_API_KEY` - Azure OpenAI 서비스용
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 엔드포인트 URL
- `AZURE_OPENAI_DEPLOYMENT` - 채팅 완료 모델 배포 이름
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 임베딩 모델 배포 이름
- `AZURE_OPENAI_API_VERSION` - API 버전 (기본값: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face 모델용
- `GITHUB_TOKEN` - GitHub 모델용

### Python 예제 실행

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript 예제 실행

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter 노트북 실행

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### 다양한 레슨 유형 작업

- **"Learn" 레슨**: README.md 문서와 개념에 중점
- **"Build" 레슨**: Python 및 TypeScript의 작동 코드 예제 포함
- 각 레슨에는 이론, 코드 워크스루, 비디오 콘텐츠 링크가 포함된 README.md가 있음

## 코드 스타일 가이드라인

### Python

- 환경 변수 관리를 위해 `python-dotenv` 사용
- API 상호작용을 위해 `openai` 라이브러리 가져오기
- 린팅을 위해 `pylint` 사용 (`# pylint: disable=all`을 포함한 간단한 예제 있음)
- PEP 8 명명 규칙 준수
- API 자격 증명은 코드에 저장하지 않고 `.env` 파일에 저장

### TypeScript

- 환경 변수를 위해 `dotenv` 패키지 사용
- 각 앱에 대한 `tsconfig.json`으로 TypeScript 구성
- Azure 서비스를 위해 `@azure/openai` 또는 `@azure-rest/ai-inference` 사용
- 자동 재로드를 위해 `nodemon` 사용
- 실행 전에 빌드: `npm run build` 후 `npm start`

### 일반 규칙

- 코드 예제를 간단하고 교육적으로 유지
- 주요 개념을 설명하는 주석 포함
- 각 레슨의 코드는 독립적이고 실행 가능해야 함
- 일관된 명명 사용: Azure OpenAI는 `aoai-`, OpenAI API는 `oai-`, GitHub 모델은 `githubmodels-` 접두사 사용

## 문서화 가이드라인

### Markdown 스타일

- 모든 URL은 `[텍스트](../../url)` 형식으로 감싸야 하며, 추가 공백 없음
- 상대 링크는 `./` 또는 `../`로 시작해야 함
- Microsoft 도메인 링크에는 추적 ID 포함: `?WT.mc_id=academic-105485-koreyst`
- URL에 국가별 로케일 포함 금지 (예: `/en-us/` 사용 금지)
- 이미지는 `./images` 폴더에 설명적인 이름으로 저장
- 파일 이름에는 영어 문자, 숫자, 대시만 사용

### 번역 지원

- 저장소는 GitHub Actions를 통해 40개 이상의 언어를 지원
- 번역은 `translations/` 디렉토리에 저장
- 부분 번역 제출 금지
- 기계 번역은 허용되지 않음
- 번역된 이미지는 `translated_images/` 디렉토리에 저장

## 테스트 및 검증

### 제출 전 확인

이 저장소는 GitHub Actions를 사용하여 검증을 수행합니다. PR 제출 전에:

1. **Markdown 링크 확인**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **수동 테스트**:
   - Python 예제 테스트: 가상 환경 활성화 후 스크립트 실행
   - TypeScript 예제 테스트: `npm install`, `npm run build`, `npm start`
   - 환경 변수가 올바르게 구성되었는지 확인
   - API 키가 코드 예제와 작동하는지 확인

3. **코드 예제**:
   - 모든 코드가 오류 없이 실행되는지 확인
   - Azure OpenAI 및 OpenAI API 모두에서 테스트
   - GitHub 모델이 지원되는 경우 예제가 작동하는지 확인

### 자동화된 테스트 없음

이 저장소는 튜토리얼과 예제에 중점을 둔 교육용 저장소입니다. 실행할 단위 테스트나 통합 테스트는 없습니다. 검증은 주로 다음을 포함합니다:
- 코드 예제의 수동 테스트
- Markdown 검증을 위한 GitHub Actions
- 교육 콘텐츠에 대한 커뮤니티 리뷰

## Pull Request 가이드라인

### 제출 전

1. Python 및 TypeScript에서 코드 변경 사항 테스트
2. Markdown 검증 실행 (PR에서 자동으로 트리거됨)
3. 모든 Microsoft URL에 추적 ID가 포함되었는지 확인
4. 상대 링크가 유효한지 확인
5. 이미지가 올바르게 참조되었는지 확인

### PR 제목 형식

- 설명적인 제목 사용: `[Lesson 06] Fix Python example typo` 또는 `Update README for lesson 08`
- 관련된 이슈 번호 참조: `Fixes #123`

### PR 설명

- 변경된 내용과 이유 설명
- 관련된 이슈 링크
- 코드 변경 사항의 경우 테스트된 예제 명시
- 번역 PR의 경우 전체 번역 파일 포함

### 기여 요구사항

- Microsoft CLA 서명 (첫 PR에서 자동으로 처리됨)
- 변경 사항을 만들기 전에 저장소를 계정에 포크
- 논리적 변경 사항당 하나의 PR (관련 없는 수정 사항 결합 금지)
- PR은 가능하면 집중적이고 작게 유지

## 일반 워크플로우

### 새로운 코드 예제 추가

1. 적절한 레슨 디렉토리로 이동
2. `python/` 또는 `typescript/` 하위 디렉토리에 예제 생성
3. 명명 규칙 준수: `{provider}-{example-name}.{py|ts|js}`
4. 실제 API 자격 증명으로 테스트
5. 레슨 README에 새로운 환경 변수를 문서화

### 문서 업데이트

1. 레슨 디렉토리의 README.md 편집
2. Markdown 가이드라인 준수 (추적 ID, 상대 링크)
3. 번역 업데이트는 GitHub Actions에서 처리 (수동 편집 금지)
4. 모든 링크가 유효한지 테스트

### Dev 컨테이너 작업

1. 저장소는 `.devcontainer/devcontainer.json`을 포함
2. 포스트 생성 스크립트가 Python 종속성을 자동으로 설치
3. Python 및 Jupyter 확장이 미리 구성됨
4. 환경은 `mcr.microsoft.com/devcontainers/universal:2.11.2`를 기반으로 함

## 배포 및 게시

이 저장소는 학습용으로 사용되며 배포 프로세스는 없습니다. 커리큘럼은 다음을 통해 소비됩니다:

1. **GitHub 저장소**: 코드와 문서에 직접 액세스
2. **GitHub Codespaces**: 사전 구성된 설정으로 즉시 개발 환경 제공
3. **Microsoft Learn**: 공식 학습 플랫폼에 콘텐츠가 배포될 수 있음
4. **docsify**: Markdown에서 생성된 문서 사이트 (`docsifytopdf.js` 및 `package.json` 참조)

### 문서 사이트 빌드

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## 문제 해결

### 일반적인 문제

**Python 가져오기 오류**:
- 가상 환경이 활성화되었는지 확인
- `pip install -r requirements.txt` 실행
- Python 버전이 3.9+인지 확인

**TypeScript 빌드 오류**:
- 특정 앱 디렉토리에서 `npm install` 실행
- Node.js 버전이 호환되는지 확인
- `node_modules`를 지우고 다시 설치

**API 인증 오류**:
- `.env` 파일이 존재하고 올바른 값이 있는지 확인
- API 키가 유효하고 만료되지 않았는지 확인
- 엔드포인트 URL이 지역에 맞는지 확인

**환경 변수 누락**:
- `.env.copy`를 `.env`로 복사
- 작업 중인 레슨에 필요한 모든 값을 채움
- `.env` 업데이트 후 애플리케이션 재시작

## 추가 자료

- [코스 설정 가이드](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [기여 가이드라인](./CONTRIBUTING.md)
- [행동 강령](./CODE_OF_CONDUCT.md)
- [보안 정책](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [고급 코드 샘플 모음](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 프로젝트 관련 참고 사항

- 이 저장소는 **교육용 저장소**로 학습에 중점을 두며, 프로덕션 코드가 아님
- 예제는 의도적으로 간단하며 개념 교육에 초점
- 코드 품질은 교육적 명확성과 균형을 이룸
- 각 레슨은 독립적이며 개별적으로 완료 가능
- 저장소는 여러 API 제공자를 지원: Azure OpenAI, OpenAI, GitHub 모델
- 콘텐츠는 다국어로 제공되며 자동 번역 워크플로우 포함
- 질문 및 지원을 위한 Discord 커뮤니티 활성화

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.