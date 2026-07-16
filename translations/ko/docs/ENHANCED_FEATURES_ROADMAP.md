# 향상된 기능 및 개선 로드맵

이 문서는 종합적인 코드 리뷰 및 업계 모범 사례 분석을 기반으로 Generative AI for Beginners 커리큘럼에 권장되는 향상 및 개선 사항을 개요합니다.

## 요약

코드베이스는 보안, 코드 품질, 교육 효과성 측면에서 분석되었습니다. 이 문서는 즉각적인 수정, 단기 개선 및 향후 향상에 대한 권장 사항을 제공합니다.

---

## 1. 보안 강화 (우선순위: 중요)

### 1.1 즉각적인 수정 (완료됨)

| 문제 | 영향을 받는 파일 | 상태 |
|-------|----------------|--------|
| 하드코딩된 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 수정됨 |
| 환경 변수 검증 누락 | 여러 JS/TS 파일 | 수정됨 |
| 안전하지 않은 함수 호출 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 수정됨 |
| 파일 핸들 누수 | `08-building-search-applications/scripts/` | 수정됨 |
| 요청 타임아웃 누락 | `09-building-image-applications/python/` | 수정됨 |

### 1.2 추가 권장 보안 기능

1. **율 제한 예제**
   - API 호출에 대한 율 제한 구현 예제 코드 추가
   - 지수 백오프 패턴 시연

2. **API 키 교체**
   - API 키 교체 모범 사례 문서 추가
   - Azure Key Vault 또는 유사 서비스 사용 예제 포함

3. **콘텐츠 안전 통합**
   - Azure Content Safety API 사용 예제 추가
   - 입력/출력 검열 패턴 시연

---

## 2. 코드 품질 개선

### 2.1 구성 파일 추가

| 파일 | 용도 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 린트 규칙 |
| `.prettierrc` | 코드 포매팅 표준 |
| `pyproject.toml` | Python 도구 설정 (Black, Ruff, mypy) |

### 2.2 공유 유틸리티 생성

새로운 `shared/python/` 모듈 제공:
- `env_utils.py` - 환경 변수 처리
- `input_validation.py` - 입력 검증 및 정화
- `api_utils.py` - 안전한 API 요청 래퍼

### 2.3 권장 코드 개선 사항

1. **타입 힌트 적용 범위**
   - 모든 Python 파일에 타입 힌트 추가
   - 모든 TS 프로젝트에서 엄격한 TypeScript 모드 활성화

2. **문서화 표준**
   - 모든 Python 함수에 도큐스트링 추가
   - 모든 JavaScript/TypeScript 함수에 JSDoc 주석 추가

3. **테스트 프레임워크**
   - pytest 구성과 예제 테스트 추가 _(완료: `pyproject.toml` 내 pytest 구성; [`tests/`](../../../tests) 에서 공유 유틸리티 예제 테스트가 CI에서 실행)_
   - JavaScript/TypeScript용 Jest 구성 추가

---

## 3. 교육 개선

### 3.1 신규 강의 주제

1. **AI 애플리케이션 보안** (제안 강의 22)
   - 프롬프트 인젝션 공격 및 방어
   - API 키 관리
   - 콘텐츠 검열
   - 율 제한 및 악용 방지

2. **프로덕션 배포** (제안 강의 23)
   - Docker를 이용한 컨테이너화
   - CI/CD 파이프라인
   - 모니터링 및 로깅
   - 비용 관리

3. **고급 RAG 기법** (제안 강의 24)
   - 하이브리드 검색 (키워드 + 의미론적)
   - 재순위 전략
   - 다중 모달 RAG
   - 평가 지표

### 3.2 기존 강의 개선

| 강의 | 권장 개선 사항 |
|--------|------------------------|
| 06 - 텍스트 생성 | 스트리밍 응답 예제 추가 |
| 07 - 채팅 애플리케이션 | 대화 메모리 패턴 추가 |
| 08 - 검색 애플리케이션 | 벡터 데이터베이스 비교 추가 |
| 09 - 이미지 생성 | 이미지 편집/변형 예제 추가 |
| 11 - 함수 호출 | 병렬 함수 호출 추가 |
| 15 - RAG | 청킹 전략 비교 추가 |
| 17 - AI 에이전트 | 다중 에이전트 오케스트레이션 추가 |

---

## 4. API 현대화

### 4.1 사용 중단된 API 패턴 (마이그레이션 완료)

모든 Python 및 TypeScript <strong>채팅</strong> 샘플은 Chat Completions API에서 **Responses API** (`client.responses.create(...)` → `response.output_text`)로 마이그레이션되었습니다.

| 이전 패턴 | 새 패턴 | 상태 |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (채팅) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | 완료 |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | 완료 |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` 패키지 `client.responses.create()` → `response.output_text` | 완료 |
| `df.append()` (pandas) | `pd.concat()` | 완료 |

> **참고:** `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`)를 사용하는 Microsoft Foundry Models 샘플은 Responses API를 지원하지 않는 Model Inference API에 남아 있습니다. `AzureOpenAI()`는 임베딩 및 이미지 생성에 유효한 곳에 의도적으로 유지됩니다.

### 4.2 시연할 새로운 API 기능들

1. **구조화된 출력** (OpenAI)
   - JSON 모드
   - 엄격한 스키마를 이용한 함수 호출

2. **비전 기능**
   - GPT-4o (비전) 이미지 분석
   - 다중 모달 프롬프트

3. **Responses API 내장 도구들** (종전 Assistants API 대체)
   - 코드 인터프리터
   - 파일 검색
   - 웹 검색 및 맞춤 도구

---

## 5. 인프라 개선

### 5.1 CI/CD 강화

[`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml)에서 구현: Python 린팅/포매팅(Ruff + Black)이 유지되는 `shared/` 유틸리티 모듈에서는 <strong>강제</strong>되며 커리큘럼 나머지 부분에서는 <strong>권고</strong>로 수행되는 것과, JavaScript/TypeScript용 권고 ESLint 패스가 포함되었습니다. 예시 기준은 다음과 같았습니다:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 보안 스캐닝

[`.github/workflows/security.yml`](../../../.github/workflows/security.yml)에서 구현: Python과 JavaScript/TypeScript 대상 CodeQL 분석 (푸시, 풀 리퀘스트, 주 단위 일정에서 수행)과 풀 리퀘스트 의존성 리뷰가 포함됩니다. 예시 기준은 다음과 같았습니다:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. 개발자 경험 개선

### 6.1 DevContainer 개선

[`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json)과 [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh)에서 구현: 컨테이너가 이제 Pylance, Black 포매터, Ruff, ESLint, Prettier, Copilot 확장 기능을 포함하며, 포맷 온 세이브(Black/Prettier 설정과 연결됨)를 활성화하고, 개발 도구(`ruff`, `black`, `mypy`, `pytest`)를 설치하여 [code-quality 워크플로우](../../../.github/workflows/code-quality.yml)를 로컬에서 재현할 수 있도록 합니다. `mcr.microsoft.com/devcontainers/universal` 기본 이미지에는 Python과 Node가 이미 번들로 포함되어 있어 추가 기능이 필요 없습니다. 예시 기준은 다음과 같았습니다:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 인터랙티브 플레이그라운드

다음을 고려해보세요:
- API 키가 미리 채워진 Jupyter 노트북 (환경 변수 통해)
- 시각 학습자를 위한 Gradio/Streamlit 데모
- 지식 평가를 위한 인터랙티브 퀴즈

---

## 7. 다국어 지원

### 7.1 현재 지원 언어 범위

| 기술 | 지원 강의 | 상태 |
|------------|-----------------|--------|
| Python | 전체 | 완료 |
| TypeScript | 06-09, 11 | 일부 완료 |
| JavaScript | 06-08, 11 | 일부 완료 |
| .NET/C# | 일부 | 일부 완료 |

### 7.2 추천 추가 언어

1. **Go** - AI/ML 도구에서 성장 중
2. **Rust** - 성능 중요 애플리케이션
3. **Java/Kotlin** - 엔터프라이즈 애플리케이션

---

## 8. 성능 최적화

### 8.1 코드 레벨 최적화

1. **Async/Await 패턴**
   - 배치 처리용 async 예제 추가
   - 동시 API 호출 시연

2. **캐싱 전략**
   - 임베딩 캐싱 예제 추가
   - 응답 캐싱 패턴 시연

3. **토큰 최적화**
   - tiktoken 사용 예제 추가
   - 프롬프트 압축 기법 시연

### 8.2 비용 최적화 예제

다음 예제를 추가하세요:
- 작업 복잡도 기반 모델 선택
- 토큰 효율성을 위한 프롬프트 엔지니어링
- 대량 작업을 위한 배치 처리

---

## 9. 접근성 및 국제화

### 9.1 현재 번역 상태

모든 번역은 <strong>완료</strong>되었으며 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst)에 의해 자동 생성됩니다. 이 도구는 50개 이상의 언어 판본을 영어 원본과 동기화하여 유지합니다. 번역된 콘텐츠는 `translations/`에, 현지화된 이미지는 `translated_images/`에 있습니다; 지원 가능한 모든 언어 목록은 리포지터리 README 상단에 게시되어 있습니다.

| 항목 | 상태 |
|--------|--------|
| 번역 범위 | 완료 — 50개 이상 언어, 모든 강의 |
| 번역 방법 | [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst)를 통한 자동화 |
| 영어 원본과 동기화 유지 | 예 — 자동 재생성 |

### 9.2 접근성 개선

1. 모든 이미지에 대체 텍스트 추가
2. 코드 샘플에 적절한 구문 강조 적용
3. 모든 동영상 콘텐츠에 비디오 대본 추가
4. WCAG 가이드라인에 맞는 색 대비 보장

---

## 10. 구현 우선순위

### 1단계: 즉시 (1-2주)
- [x] 중요 보안 문제 수정
- [x] 코드 품질 설정 추가
- [x] 공유 유틸리티 생성
- [x] 보안 가이드라인 문서화

### 2단계: 단기 (3-4주)
- [x] 사용 중단 API 패턴 업데이트 (Chat Completions → Responses API, Python + TypeScript)
- [ ] 모든 Python 파일에 타입 힌트 추가 (`shared/` 모듈은 완료; 강의 샘플은 단순하게 유지)
- [x] 코드 품질용 CI/CD 워크플로우 추가
- [x] 보안 스캐닝 워크플로우 생성

### 3단계: 중기 (2-3개월)
- [ ] 신규 보안 강의 추가
- [ ] 프로덕션 배포 강의 추가
- [x] DevContainer 설정 개선
- [ ] 인터랙티브 데모 추가

### 4단계: 장기 (4개월 이상)
- [ ] 고급 RAG 강의 추가
- [ ] 언어 커버리지 확장
- [ ] 통합 테스트 스위트 추가
- [ ] 인증 프로그램 생성

---

## 결론

이 로드맵은 Generative AI for Beginners 커리큘럼 개선을 위한 체계적인 접근법을 제공합니다. 보안 문제 해결, API 현대화, 교육 콘텐츠 추가를 통해 학생들이 실제 AI 애플리케이션 개발을 더 잘 준비할 수 있도록 합니다.

질문이나 기여가 있으시면 GitHub 리포지터리에 이슈를 열어 주십시오.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->