<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T09:42:15+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "ko"
}
-->
# 프롬프트 엔지니어링 기초

## 소개
이 모듈은 생성 AI 모델에서 효과적인 프롬프트를 작성하기 위한 필수 개념과 기술을 다룹니다. LLM에 프롬프트를 작성하는 방식도 중요합니다. 신중하게 작성된 프롬프트는 더 나은 품질의 응답을 얻을 수 있습니다. 하지만 _프롬프트_와 _프롬프트 엔지니어링_ 같은 용어는 정확히 무엇을 의미할까요? 그리고 LLM에 보내는 프롬프트 _입력_을 어떻게 개선할 수 있을까요? 이 장과 다음 장에서 이러한 질문에 답하려고 합니다.

_생성 AI_는 사용자 요청에 따라 새로운 콘텐츠(예: 텍스트, 이미지, 오디오, 코드 등)를 생성할 수 있습니다. 이는 자연어와 코드를 사용하여 훈련된 OpenAI의 GPT("Generative Pre-trained Transformer") 시리즈와 같은 _대규모 언어 모델_을 사용하여 달성됩니다.

사용자는 이제 기술적 전문 지식이나 훈련 없이도 채팅과 같은 친숙한 패러다임을 사용하여 이러한 모델과 상호작용할 수 있습니다. 모델은 _프롬프트 기반_입니다. 사용자는 텍스트 입력(프롬프트)을 보내고 AI 응답(완성)을 받습니다. 그런 다음 "AI와 채팅"을 반복하여 여러 번의 대화를 통해 프롬프트를 조정하여 응답이 기대에 부합하도록 할 수 있습니다.

"프롬프트"는 이제 생성 AI 앱의 주요 _프로그래밍 인터페이스_가 되어 모델에 무엇을 해야 하는지 지시하고 반환된 응답의 품질에 영향을 미칩니다. "프롬프트 엔지니어링"은 일관되고 품질 높은 응답을 대규모로 제공하기 위한 프롬프트의 _설계 및 최적화_에 중점을 둔 빠르게 성장하는 연구 분야입니다.

## 학습 목표

이 수업에서는 프롬프트 엔지니어링이 무엇인지, 왜 중요한지, 주어진 모델 및 애플리케이션 목표에 대해 더 효과적인 프롬프트를 작성하는 방법을 배웁니다. 프롬프트 엔지니어링의 핵심 개념과 모범 사례를 이해하고 이러한 개념이 실제 예제에 적용되는 대화형 주피터 노트북 "샌드박스" 환경에 대해 알아봅니다.

이 수업이 끝날 때까지 우리는 다음을 할 수 있습니다:

1. 프롬프트 엔지니어링이 무엇인지, 왜 중요한지 설명할 수 있습니다.
2. 프롬프트의 구성 요소와 그 사용 방법을 설명할 수 있습니다.
3. 프롬프트 엔지니어링의 모범 사례와 기술을 배울 수 있습니다.
4. 학습한 기술을 실제 예제에 적용하고, OpenAI 엔드포인트를 사용하여 적용할 수 있습니다.

## 주요 용어

프롬프트 엔지니어링: AI 모델이 원하는 출력을 생성하도록 입력을 설계하고 조정하는 실천.
토큰화: 텍스트를 모델이 이해하고 처리할 수 있는 작은 단위인 토큰으로 변환하는 과정.
명령 조정 LLM: 응답의 정확성과 관련성을 개선하기 위해 특정 명령으로 미세 조정된 대규모 언어 모델(LLM).

## 학습 샌드박스

프롬프트 엔지니어링은 현재 과학보다는 예술에 가깝습니다. 이를 개선하기 위한 최고의 방법은 _더 많이 연습하고_ 응용 도메인 전문 지식과 권장 기술 및 모델별 최적화를 결합한 시행착오 접근 방식을 채택하는 것입니다.

이 수업에 동반되는 주피터 노트북은 학습한 내용을 실습할 수 있는 _샌드박스_ 환경을 제공합니다. 연습을 실행하려면 다음이 필요합니다:

1. **Azure OpenAI API 키** - 배포된 LLM의 서비스 엔드포인트.
2. **Python 런타임** - 노트북을 실행할 수 있는 환경.
3. **로컬 환경 변수** - _지금 [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) 단계를 완료하여 준비_.

노트북에는 _시작_ 연습이 포함되어 있지만, 더 많은 예제나 아이디어를 시도해보고 프롬프트 설계에 대한 직관을 구축하기 위해 자신의 _Markdown_ (설명) 및 _Code_ (프롬프트 요청) 섹션을 추가하는 것이 좋습니다.

## 일러스트 가이드

이 수업에서 다루는 내용을 시작하기 전에 큰 그림을 보고 싶으신가요? 주요 주제를 이해하고 각 주제에 대해 생각할 주요 요점을 제공하는 이 일러스트 가이드를 확인하세요. 학습 로드맵은 핵심 개념과 문제를 이해하는 것부터 관련 프롬프트 엔지니어링 기술과 모범 사례를 통해 해결하는 것까지 안내합니다. 이 가이드의 "고급 기술" 섹션은 이 교육 과정의 _다음_ 장에서 다루는 내용을 참조합니다.

## 우리 스타트업

이제 _이 주제_가 [교육에 AI 혁신을 가져오는](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) 우리의 스타트업 미션과 어떻게 관련이 있는지 이야기해 보겠습니다. 우리는 _개인화된 학습_의 AI 기반 애플리케이션을 구축하고자 합니다. 따라서 우리의 애플리케이션의 다양한 사용자가 어떻게 프롬프트를 "설계"할 수 있을지 생각해 봅시다:

- **관리자**는 AI에게 _교육 과정 데이터를 분석하여 범위의 격차를 식별_하도록 요청할 수 있습니다. AI는 결과를 요약하거나 코드를 사용하여 시각화할 수 있습니다.
- **교육자**는 AI에게 _대상 청중과 주제에 맞는 수업 계획을 생성_하도록 요청할 수 있습니다. AI는 지정된 형식으로 개인화된 계획을 구축할 수 있습니다.
- **학생**은 AI에게 _어려운 과목을 지도_하도록 요청할 수 있습니다. AI는 이제 학생의 수준에 맞춘 수업, 힌트 및 예제로 학생을 안내할 수 있습니다.

이것은 빙산의 일각에 불과합니다. 교육 전문가가 큐레이팅한 오픈 소스 프롬프트 라이브러리인 [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)을 확인하여 가능성을 더 넓게 이해하세요! _샌드박스에서 이러한 프롬프트 중 일부를 실행하거나 OpenAI Playground를 사용하여 어떤 일이 발생하는지 확인해 보세요!_

## 프롬프트 엔지니어링이란?

우리는 이 수업을 **프롬프트 엔지니어링**을 주어진 애플리케이션 목표와 모델에 대해 일관되고 품질 높은 응답(완성)을 제공하기 위해 텍스트 입력(프롬프트)을 _설계하고 최적화_하는 과정으로 정의하며 시작했습니다. 이를 2단계 프로세스로 생각할 수 있습니다:

- 주어진 모델과 목표에 대한 초기 프롬프트 _설계_
- 응답의 품질을 개선하기 위한 프롬프트 _세부 조정_

이는 최적의 결과를 얻기 위해 사용자 직관과 노력이 필요한 시행착오 과정입니다. 그렇다면 왜 중요할까요? 이 질문에 답하기 위해 먼저 세 가지 개념을 이해해야 합니다:

- _토큰화_ = 모델이 프롬프트를 "보는" 방식
- _기본 LLM_ = 기본 모델이 프롬프트를 "처리"하는 방식
- _명령 조정 LLM_ = 모델이 "작업"을 볼 수 있는 방식

### 토큰화

LLM은 프롬프트를 _토큰의 시퀀스_로 보며, 다른 모델(또는 모델 버전)은 동일한 프롬프트를 다른 방식으로 토큰화할 수 있습니다. LLM은 토큰(원시 텍스트가 아님)으로 훈련되므로, 프롬프트가 토큰화되는 방식은 생성된 응답의 품질에 직접적인 영향을 미칩니다.

토큰화가 어떻게 작동하는지 직관을 얻기 위해 [OpenAI 토크나이저](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst)와 같은 도구를 사용해 보세요. 프롬프트를 복사하여 붙여넣고 토큰으로 변환되는 방식을 확인하며 공백 문자와 구두점이 처리되는 방식에 주목하세요. 이 예제는 이전 LLM(GPT-3)을 보여줍니다. 더 새로운 모델로 시도하면 다른 결과가 나올 수 있습니다.

### 개념: 기본 모델

프롬프트가 토큰화되면 ["기본 LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)(또는 기본 모델)의 주요 기능은 해당 시퀀스의 토큰을 예측하는 것입니다. LLM은 방대한 텍스트 데이터셋으로 훈련되었기 때문에 토큰 간의 통계적 관계를 잘 이해하고 예측할 수 있습니다. 그러나 프롬프트나 토큰의 _의미_를 이해하지 못하고, 단지 다음 예측으로 "완성"할 수 있는 패턴을 볼 뿐입니다. 사용자 개입이나 사전 설정된 조건에 의해 종료될 때까지 시퀀스를 계속 예측할 수 있습니다.

프롬프트 기반 완성이 어떻게 작동하는지 보고 싶으신가요? 위의 프롬프트를 Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)에 기본 설정으로 입력해 보세요. 시스템은 프롬프트를 정보 요청으로 처리하도록 구성되어 있으므로 이 컨텍스트를 만족시키는 완성을 볼 수 있습니다.

하지만 사용자가 특정 기준이나 작업 목표를 충족하는 것을 보고 싶다면 어떻게 할까요? 여기서 _명령 조정_ LLM이 등장합니다.

### 개념: 명령 조정 LLM

[명령 조정 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)은 기본 모델에서 시작하여 명령을 포함한 예제 또는 입력/출력 쌍(예: 여러 번의 "메시지")으로 미세 조정되어 AI가 해당 명령을 따르려고 시도하는 응답을 생성합니다.

이는 인간 피드백을 통한 강화 학습(RLHF)과 같은 기술을 사용하여 모델이 _명령을 따르고_ _피드백을 학습하도록_ 훈련하여 실제 애플리케이션에 더 적합하고 사용자 목표에 더 관련성이 높은 응답을 생성합니다.

한번 시도해 봅시다. 위의 프롬프트를 다시 방문하고 이제 _시스템 메시지_를 다음과 같이 제공하여 컨텍스트로 제공하세요:

> _제공된 콘텐츠를 2학년 학생에게 요약하세요. 결과를 3-5개의 핵심 사항으로 구성된 한 단락으로 유지하세요._

결과가 이제 원하는 목표와 형식을 반영하도록 조정된 것을 볼 수 있습니까? 교육자는 이제 이 응답을 해당 수업의 슬라이드에 직접 사용할 수 있습니다.

## 왜 프롬프트 엔지니어링이 필요한가?

이제 프롬프트가 LLM에 의해 처리되는 방식을 알았으니, 왜 프롬프트 엔지니어링이 필요한지 이야기해 봅시다. 그 이유는 현재 LLM이 _신뢰할 수 있고 일관된 완성_을 달성하기 어려운 여러 도전을 제기하기 때문입니다. 예를 들어:

1. **모델 응답은 확률적입니다.** _동일한 프롬프트_는 다른 모델이나 모델 버전에서 다른 응답을 생성할 가능성이 높습니다. 동일한 모델에서 다른 시간에 다른 결과를 생성할 수도 있습니다. _프롬프트 엔지니어링 기술은 더 나은 가드레일을 제공하여 이러한 변동을 최소화하는 데 도움을 줄 수 있습니다_.

2. **모델은 응답을 조작할 수 있습니다.** 모델은 _크지만 유한한_ 데이터셋으로 사전 훈련되었기 때문에 그 범위를 벗어난 개념에 대한 지식이 부족합니다. 결과적으로 부정확하거나 상상적이거나 알려진 사실과 직접적으로 모순되는 완성을 생성할 수 있습니다. _프롬프트 엔지니어링 기술은 AI에게 인용이나 추론을 요청하는 등의 방법으로 사용자가 이러한 조작을 식별하고 완화하도록 도울 수 있습니다_.

3. **모델 기능은 다양합니다.** 새로운 모델이나 모델 세대는 더 풍부한 기능을 제공하지만 비용과 복잡성에 있어 고유한 단점과 타협점을 가져옵니다. _프롬프트 엔지니어링은 차이를 추상화하고 모델별 요구 사항에 적응하는 모범 사례와 워크플로를 개발하여 확장 가능하고 원활한 방식으로 이러한 문제를 해결하는 데 도움을 줄 수 있습니다_.

OpenAI 또는 Azure OpenAI Playground에서 이를 실습해 봅시다:

- 동일한 프롬프트를 다른 LLM 배포판(OpenAI, Azure OpenAI, Hugging Face 등)에서 사용해 보세요. 변동을 보셨나요?
- 동일한 LLM 배포판(Azure OpenAI Playground 등)에서 동일한 프롬프트를 반복 사용해 보세요. 이러한 변동이 어떻게 달랐나요?

### 조작 예시

이 과정에서는 **"조작"**이라는 용어를 사용하여 LLM이 훈련의 제한이나 기타 제약으로 인해 때때로 사실적으로 부정확한 정보를 생성하는 현상을 참조합니다. 이는 인기 있는 기사나 연구 논문에서 _"환각"_으로 언급되기도 합니다. 그러나 기계 주도의 결과에 인간과 같은 특성을 부여하여 행동을 의인화하지 않도록 _"조작"_이라는 용어를 사용할 것을 강력히 권장합니다. 이는 용어 관점에서 [책임 있는 AI 가이드라인](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)을 강화하여 일부 맥락에서 공격적이거나 비포괄적인 것으로 간주될 수 있는 용어를 제거합니다.

조작이 어떻게 작동하는지 감을 잡고 싶으신가요? AI에게 존재하지 않는 주제에 대한 콘텐츠 생성을 지시하는 프롬프트를 생각해 보세요(훈련 데이터셋에 포함되지 않은 것을 보장하기 위해). 예를 들어, 저는 다음 프롬프트를 시도했습니다:

> **프롬프트:** 2076년 화성 전쟁에 대한 수업 계획을 생성하세요.

웹 검색을 통해 화성 전쟁에 대한 허구의 계정(예: TV 시리즈나 책)이 있었지만, 2076년에 대한 것은 없었습니다. 상식적으로도 2076년은 _미래_에 있으므로 실제 사건과 관련이 없다는 것을 알 수 있습니다.

다른 LLM 제공업체와 함께 이 프롬프트를 실행했을 때 어떤 일이 발생했는지 보겠습니다.

예상대로, 각 모델(또는 모델 버전)은 확률적 행동과 모델 기능 변동으로 인해 약간 다른 응답을 생성했습니다. 예를 들어, 한 모델은 8학년 청중을 대상으로 하고 다른 모델은 고등학생을 가정합니다. 그러나 세 모델 모두 비현실적인 사용자를 설득할 수 있는 응답을 생성했습니다.

프롬프트 엔지니어링 기술인 _메타프롬프팅_ 및 _온도 구성_은 모델 조작을 어느 정도 줄일 수 있습니다. 새로운 프롬프트 엔지니어링 _아키텍처_는 이러한 효과를 완화하거나 줄이기 위해 프롬프트 흐름에 새로운 도구와 기술을 원활하게 통합합니다.

## 사례 연구: GitHub Copilot

이 섹션을 마무리하면서 실제 솔루션에서 프롬프트 엔지니어링이 어떻게 사용되는지에 대한 감을 얻기 위해 하나의 사례 연구: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst)을 살펴보겠습니다.

GitHub Copilot은 "AI 페어 프로그래머"로, 텍스트 프롬프트를 코드 완성으로 변환하고 사용자 경험을 원활하게 하기 위해 개발 환경(예: Visual Studio Code)에 통합됩니다. 아래 블로그 시리즈에 문서화된 바와 같이, 초기 버전은 OpenAI Codex 모델을 기반으로 했으며, 엔지니어들은 코드 품질을 개선하기 위해 모델을 미세 조정하고 더 나은 프롬프트 엔지니어링 기술을 개발할 필요성을 빠르게 깨달았습니다. 7월에는 [Codex를 넘어선 향상된 AI 모델을 공개](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)하여 더 빠른 제안을 제공합니다.

그들의 학습 여정을 따라가려면 게시물을 순서대로 읽어보세요.

- **2023년 5월** | [GitHub Copilot은 코드를 더 잘 이해하고 있습니다](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023년 5월** | [GitHub 내부: GitHub Copilot 뒤의 LLM과 함께 작업하기](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-g
마침내 템플릿의 진정한 가치는 수직적 응용 분야를 위한 _프롬프트 라이브러리_ 를 생성하고 게시할 수 있는 능력에 있습니다. 여기서 프롬프트 템플릿은 이제 응용 프로그램에 특화된 맥락이나 예제를 반영하도록 _최적화_ 되어 대상 사용자에게 더 관련성 있고 정확한 응답을 제공합니다. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 저장소는 이러한 접근 방식의 훌륭한 예로, 교육 분야를 위한 프롬프트 라이브러리를 큐레이팅하고 수업 계획, 커리큘럼 디자인, 학생 지도와 같은 주요 목표에 중점을 둡니다.

## 콘텐츠 지원

프롬프트 구성은 지시사항(작업)과 대상(주요 콘텐츠)을 포함한다고 생각하면, _부차적인 콘텐츠_ 는 **어떤 방식으로든 출력을 영향을 미칠** 추가적인 맥락과 같습니다. 이는 모델이 원하는 사용자 목표나 기대에 맞춰 _반응을 맞춤화_ 하는 데 도움을 줄 수 있는 매개변수 조정, 형식 지시사항, 주제 분류 등일 수 있습니다.

예를 들어, 커리큘럼의 모든 사용 가능한 코스에 대한 광범위한 메타데이터(이름, 설명, 수준, 메타데이터 태그, 강사 등)를 가진 코스 카탈로그가 주어졌을 때:

- "2023년 가을 코스 카탈로그 요약"이라는 지시사항을 정의할 수 있습니다.
- 원하는 출력의 몇 가지 예를 제공하기 위해 주요 콘텐츠를 사용할 수 있습니다.
- 관심 있는 상위 5개의 "태그"를 식별하기 위해 부차적인 콘텐츠를 사용할 수 있습니다.

이제 모델은 몇 가지 예에서 보여준 형식으로 요약을 제공할 수 있지만, 결과에 여러 태그가 있는 경우 부차적인 콘텐츠에서 식별된 5개의 태그를 우선시할 수 있습니다.

---

<!--
레슨 템플릿:
이 단원은 핵심 개념 #1을 다루어야 합니다.
개념을 예제와 참고자료로 강화하세요.

개념 #3:
프롬프트 엔지니어링 기술.
프롬프트 엔지니어링의 기본 기술은 무엇인가요?
몇 가지 연습으로 설명하세요.
-->

## 프롬프트 모범 사례

이제 프롬프트를 어떻게 _구성_ 할 수 있는지 알았으니, 어떻게 _디자인_ 해야 모범 사례를 반영할 수 있을지 생각해볼 수 있습니다. 이를 두 부분으로 생각할 수 있습니다 - 올바른 _마인드셋_을 갖추고 올바른 _기술_을 적용하는 것입니다.

### 프롬프트 엔지니어링 마인드셋

프롬프트 엔지니어링은 시행착오 과정이므로 세 가지 넓은 지침 요소를 염두에 두세요:

1. **도메인 이해가 중요합니다.** 응답의 정확성과 관련성은 그 응용 프로그램이나 사용자가 운영하는 _도메인_의 함수입니다. 직관과 도메인 전문성을 적용하여 **기술을 맞춤화**하세요. 예를 들어, 시스템 프롬프트에서 _도메인 특화된 성격_을 정의하거나 사용자 프롬프트에서 _도메인 특화된 템플릿_을 사용하세요. 도메인 특화된 맥락을 반영하는 부차적인 콘텐츠를 제공하거나 _도메인 특화된 신호와 예제_를 사용하여 모델이 익숙한 사용 패턴으로 안내하도록 하세요.

2. **모델 이해가 중요합니다.** 우리는 모델이 본질적으로 확률적이라는 것을 알고 있습니다. 하지만 모델 구현은 그들이 사용하는 학습 데이터셋(사전 학습 지식), 제공하는 기능(API 또는 SDK 등) 및 최적화된 콘텐츠 유형(코드, 이미지, 텍스트 등)에 따라 다를 수 있습니다. 사용하는 모델의 강점과 한계를 이해하고 그 지식을 사용하여 _작업을 우선순위화_하거나 모델의 기능에 최적화된 _맞춤형 템플릿_을 구축하세요.

3. **반복 및 검증이 중요합니다.** 모델과 프롬프트 엔지니어링 기술은 빠르게 진화하고 있습니다. 도메인 전문가로서, _당신의_ 특정 응용 프로그램에 적용될 수 없는 다른 맥락이나 기준을 가질 수 있습니다. 프롬프트 엔지니어링 도구 및 기술을 사용하여 프롬프트 구성을 "빠르게 시작"한 다음 직관과 도메인 전문성을 사용하여 결과를 반복하고 검증하세요. 통찰력을 기록하고 다른 사람들이 더 빠른 반복을 위해 새로운 기준으로 사용할 수 있는 **지식 기반**(예: 프롬프트 라이브러리)을 만드세요.

## 모범 사례

이제 [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst)와 [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) 전문가들이 추천하는 일반적인 모범 사례를 살펴보겠습니다.

| 무엇                              | 왜                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 최신 모델 평가하기                | 새로운 모델 세대는 개선된 기능과 품질을 가질 가능성이 높지만 더 높은 비용이 발생할 수도 있습니다. 영향을 평가한 후 마이그레이션 결정을 내리세요.                                                                                            |
| 지시사항과 맥락 분리하기          | 모델/제공자가 지시사항, 주요 및 부차적인 콘텐츠를 더 명확하게 구분하기 위한 _구분자_를 정의하는지 확인하세요. 이는 모델이 토큰에 더 정확하게 가중치를 부여하는 데 도움이 될 수 있습니다.                                                   |
| 구체적이고 명확하게 하기          | 원하는 맥락, 결과, 길이, 형식, 스타일 등에 대해 더 많은 세부 정보를 제공하세요. 이는 응답의 품질과 일관성을 개선합니다. 재사용 가능한 템플릿에 레시피를 캡처하세요.                                                                           |
| 설명적이고 예시 사용하기          | 모델은 "보여주고 말하기" 접근 방식에 더 잘 반응할 수 있습니다. `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` 값을 사용하여 시작하세요. [학습 샌드박스 섹션](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals)으로 돌아가서 배우세요.

### 다음으로, Jupyter Notebook 열기

- 런타임 커널을 선택하세요. 옵션 1 또는 2를 사용하는 경우, dev 컨테이너에서 제공하는 기본 Python 3.10.x 커널을 선택하세요.

연습을 실행할 준비가 되었습니다. 여기에는 _옳고 그름_의 답이 없습니다 - 단지 시행착오를 통해 모델과 응용 분야에 대해 어떤 것이 효과적인지에 대한 직관을 키우는 것입니다.

_이러한 이유로 이 레슨에는 코드 솔루션 세그먼트가 없습니다. 대신 Notebook에는 "내 솔루션:"이라는 제목의 Markdown 셀이 있어 참조용으로 하나의 예시 출력을 보여줍니다._

 <!--
레슨 템플릿:
요약 및 자기 주도 학습을 위한 리소스로 섹션을 마무리하세요.
-->

## 지식 점검

다음 중 몇 가지 합리적인 모범 사례를 따르는 좋은 프롬프트는 무엇입니까?

1. 빨간 차의 이미지를 보여주세요
2. 빨간 차, Volvo 제조, XC90 모델, 절벽 옆에 주차된 해가 지는 이미지를 보여주세요
3. 빨간 차, Volvo 제조, XC90 모델의 이미지를 보여주세요

A: 2번이 가장 좋은 프롬프트입니다. "무엇"에 대한 세부 사항을 제공하고 구체적으로 설명하며(단순히 아무 차가 아닌 특정 제조 및 모델) 전체적인 설정을 설명합니다. 3번도 많은 설명을 포함하고 있어 다음으로 좋습니다.

## 🚀 도전

프롬프트: "Volvo 제조의 빨간 차 이미지를 보여주세요"라는 문장을 완성하는 "신호" 기술을 활용할 수 있는지 확인하세요. 그것은 무엇을 응답하고, 어떻게 개선할 수 있을까요?

## 훌륭한 작업! 학습 계속하기

다양한 프롬프트 엔지니어링 개념에 대해 더 알고 싶으신가요? 이 주제에 대한 다른 훌륭한 리소스를 찾기 위해 [지속적인 학습 페이지](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)로 이동하세요.

레슨 5로 이동하여 [고급 프롬프트 기술](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.