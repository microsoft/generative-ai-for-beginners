# 향상된 기능 및 개선 사항 로드맵

이 문서는 종합적인 코드 리뷰 및 업계 모범 사례 분석을 기반으로 Generative AI for Beginners 커리큘럼의 권장 향상 및 개선 사항을 개략적으로 설명합니다.

## 요약

코드베이스는 보안, 코드 품질 및 교육 효과성 측면에서 분석되었습니다. 이 문서는 즉각적인 수정, 단기 개선 사항 및 미래 향상에 대한 권장 사항을 제공합니다.

---

## 1. 보안 강화 (우선순위: 중요)

### 1.1 즉각적인 수정 (완료됨)

| 문제 | 영향 받는 파일 | 상태 |
|-------|----------------|--------|
| 하드코딩된 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 수정됨 |
| 누락된 env 유효성 검사 | 여러 JS/TS 파일 | 수정됨 |
| 안전하지 않은 함수 호출 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 수정됨 |
| 파일 핸들 누수 | `08-building-search-applications/scripts/` | 수정됨 |
| 누락된 요청 타임아웃 | `09-building-image-applications/python/` | 수정됨 |

### 1.2 권장 추가 보안 기능

1. **비율 제한 예제**
   - API 호출에 대한 비율 제한을 구현하는 예제 코드 추가
   - 지수 백오프 패턴 시연

2. **API 키 회전**
   - API 키 회전 모범 사례에 관한 문서 추가
   - Azure Key Vault 또는 유사 서비스 사용 예제 포함

3. **콘텐츠 안전 통합**
   - Azure Content Safety API 사용 예제 추가
   - 입력/출력 중재 패턴 시연

---

## 2. 코드 품질 개선

### 2.1 구성 파일 추가됨

| 파일 | 용도 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 린팅 규칙 |
| `.prettierrc` | 코드 포맷팅 표준 |
| `pyproject.toml` | Python 툴링 구성 (Black, Ruff, mypy) |

### 2.2 공유 유틸리티 생성됨

새로운 `shared/python/` 모듈 포함:
- `env_utils.py` - 환경 변수 처리
- `input_validation.py` - 입력 검증 및 정화
- `api_utils.py` - 안전한 API 요청 래퍼

### 2.3 권장 코드 개선 사항

1. **타입 힌트 적용 범위**
   - 모든 Python 파일에 타입 힌트 추가
   - 모든 TS 프로젝트에서 엄격한 TypeScript 모드 활성화

2. **문서화 표준**
   - 모든 Python 함수에 docstring 추가
   - 모든 JavaScript/TypeScript 함수에 JSDoc 주석 추가

3. **테스트 프레임워크**
   - pytest 구성 및 예제 테스트 추가
   - JavaScript/TypeScript용 Jest 구성 추가

---

## 3. 교육 향상

### 3.1 신규 강의 주제

1. **AI 애플리케이션 보안** (제안 강의 22)
   - 프롬프트 인젝션 공격 및 방어
   - API 키 관리
   - 콘텐츠 중재
   - 비율 제한 및 남용 방지

2. **프로덕션 배포** (제안 강의 23)
   - Docker를 이용한 컨테이너화
   - CI/CD 파이프라인
   - 모니터링 및 로깅
   - 비용 관리

3. **고급 RAG 기법** (제안 강의 24)
   - 하이브리드 검색 (키워드 + 의미)
   - 재순위 전략
   - 다중 모달 RAG
   - 평가 지표

### 3.2 기존 강의 개선

| 강의 | 권장 개선 사항 |
|--------|------------------------|
| 06 - 텍스트 생성 | 스트리밍 응답 예제 추가 |
| 07 - 챗 애플리케이션 | 대화 메모리 패턴 추가 |
| 08 - 검색 애플리케이션 | 벡터 데이터베이스 비교 추가 |
| 09 - 이미지 생성 | 이미지 편집/변형 예제 추가 |
| 11 - 함수 호출 | 병렬 함수 호출 추가 |
| 15 - RAG | 청킹 전략 비교 추가 |
| 17 - AI 에이전트 | 다중 에이전트 오케스트레이션 추가 |

---

## 4. API 현대화

### 4.1 업데이트가 필요한 사용 중단 API 패턴

| 이전 패턴 | 새 패턴 | 영향 받는 파일 |
|-------------|-------------|----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` 클라이언트 | `08-building-search-applications/` 내 여러 스크립트 |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | 여러 노트북 |
| `df.append()` (pandas) | `pd.concat()` | RAG 노트북 |

### 4.2 시연할 새 API 기능

1. **구조화된 출력** (OpenAI)
   - JSON 모드
   - 엄격한 스키마를 사용하는 함수 호출

2. **비전 기능**
   - GPT-4V를 통한 이미지 분석
   - 다중 모달 프롬프트

3. **어시스턴트 API**
   - 코드 해석기
   - 파일 검색
   - 사용자 정의 도구

---

## 5. 인프라 개선

### 5.1 CI/CD 개선사항

현재 워크플로우는 마크다운 검증 처리를 합니다. 권장 추가 사항:

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

## 6. 개발자 환경 개선

### 6.1 DevContainer 개선

`.devcontainer/devcontainer.json` 업데이트:

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

다음 항목 고려:
- 사전 입력된 API 키(환경 변수 사용)를 갖춘 Jupyter 노트북
- 시각 학습자를 위한 Gradio/Streamlit 데모
- 지식 평가용 인터랙티브 퀴즈

---

## 7. 다국어 지원

### 7.1 현재 언어 지원 현황

| 기술 | 포함된 강의 | 상태 |
|------------|-----------------|--------|
| Python | 전체 | 완성 |
| TypeScript | 06-09, 11 | 부분적 |
| JavaScript | 06-08, 11 | 부분적 |
| .NET/C# | 일부 | 부분적 |

### 7.2 권장 추가

1. **Go** - AI/ML 툴링 성장 중
2. **Rust** - 성능이 중요한 애플리케이션
3. **Java/Kotlin** - 엔터프라이즈 애플리케이션

---

## 8. 성능 최적화

### 8.1 코드 수준 최적화

1. **Async/Await 패턴**
   - 배치 처리용 비동기 예제 추가
   - 동시 API 호출 시연

2. **캐싱 전략**
   - 임베딩 캐싱 예제 추가
   - 응답 캐싱 패턴 시연

3. **토큰 최적화**
   - tiktoken 사용 예제 추가
   - 프롬프트 압축 기법 시연

### 8.2 비용 최적화 예제

다음 내용 시연 예제 추가:
- 작업 복잡도에 따른 모델 선택
- 토큰 효율성을 위한 프롬프트 엔지니어링
- 대량 작업을 위한 배치 처리

---

## 9. 접근성 및 국제화

### 9.1 현재 번역 상태

| 언어 | 상태 |
|----------|--------|
| 영어 | 완성 |
| 중국어 (간체) | 완성 |
| 일본어 | 완성 |
| 한국어 | 완성 |
| 스페인어 | 부분적 |
| 포르투갈어 | 부분적 |
| 터키어 | 부분적 |
| 폴란드어 | 부분적 |

### 9.2 접근성 개선

1. 모든 이미지에 대체 텍스트 추가
2. 코드 샘플에 적절한 구문 강조 적용
3. 모든 비디오 콘텐츠에 대해 자막 추가
4. WCAG 가이드라인에 맞는 색 대비 확보

---

## 10. 구현 우선순위

### 1단계: 즉시 (1-2주차)
- [x] 중요한 보안 이슈 수정
- [x] 코드 품질 구성 추가
- [x] 공유 유틸리티 생성
- [x] 보안 지침 문서화

### 2단계: 단기 (3-4주차)
- [ ] 사용 중단 API 패턴 업데이트
- [ ] 모든 Python 파일에 타입 힌트 추가
- [ ] 코드 품질용 CI/CD 워크플로우 추가
- [ ] 보안 스캐닝 워크플로우 생성

### 3단계: 중기 (2-3개월 차)
- [ ] 신규 보안 강의 추가
- [ ] 프로덕션 배포 강의 추가
- [ ] DevContainer 설정 개선
- [ ] 인터랙티브 데모 추가

### 4단계: 장기 (4개월 이후)
- [ ] 고급 RAG 강의 추가
- [ ] 언어 지원 확대
- [ ] 종합 테스트 스위트 추가
- [ ] 자격증 프로그램 생성

---

## 결론

이 로드맵은 Generative AI for Beginners 커리큘럼 개선을 위한 체계적인 접근 방식을 제공합니다. 보안 문제 해결, API 현대화 및 교육 콘텐츠 추가를 통해 수강생들이 실제 AI 애플리케이션 개발에 더 잘 대비할 수 있게 될 것입니다.

질문이나 기여 사항이 있으면 GitHub 저장소에서 이슈를 열어주시기 바랍니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에서는 오류나 부정확한 내용이 포함될 수 있음을 알려드립니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 사람 번역을 권장합니다. 이 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->