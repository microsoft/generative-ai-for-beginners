# 프롬프트 엔지니어링 기초

[![프롬프트 엔지니어링 기초](../../images/04-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/r2ItK3UMVTk?WT.mc_id=academic-105485-koreyst)

LLM에 프롬프트를 어떻게 작성하느냐는 중요합니다. 신중하게 구성된 프롬프트는 그렇지 않은 프롬프트보다 더 나은 결과를 낼 수 있습니다. 하지만 이러한 개념들, 프롬프트, 프롬프트 엔지니어링이 무엇이며, 내가 LLM에 보내는 내용을 어떻게 개선할 수 있을까요? 이 장과 다음 장에서 이와 같은 질문에 답하려고 합니다.

_생성형 AI_ 는 사용자의 요청에 반응하여 새로운 콘텐츠(예: 텍스트, 이미지, 오디오, 코드 등)를 만들어냅니다. 이를 위해 자연어 및 코드 사용에 대해 훈련된 _대형 언어 모델_ (LLMs)인 OpenAI의 GPT("Generative Pre-trained Transformer") 시리즈와 같은 모델을 활용합니다.

이제 사용자는 채팅과 같은 익숙한 패러다임을 사용하여 기술적 전문 지식이나 훈련없이 이러한 모델과 상호 작용할 수 있습니다. 이러한 모델들은 _프롬프트 기반_ 입니다. 사용자는 텍스트 입력(프롬프트)을 보내고 AI의 응답(완성)을 받아냅니다. 사용자는 이후 AI와 반복적으로 "대화"를 나누며, 여러 턴의 대화를 통해 원하는 응답이 나올 때까지 프롬프트를 정제할 수 있습니다.

이제 "프롬프트"는 생성형 AI 애플리케이션을 위한 주요 _프로그래밍 인터페이스_ 가 됩니다. 이는 모델에게 무엇을 할지 지시하고 반환된 응답의 질에 영향을 미칩니다. "프롬프트 엔지니어링"은 프롬프트의 _설계 및 최적화_ 에 중점을 두어 일관되고 질 높은 응답을 대규모로 제공하기 위한 연구 분야로 빠르게 성장하고 있습니다.

## 학습 목표

이 수업에서는 프롬프트 엔지니어링이 무엇인지, 왜 중요한지, 주어진 모델과 애플리케이션 목표에 맞는 보다 효과적인 프롬프트를 어떻게 만들 수 있는지를 배웁니다. 우리는 프롬프트 엔지니어링의 핵심 개념과 모범 사례를 이해하고, 실제 예시에 이러한 개념들이 적용되는 상호 작용하는 주피터 노트북 "sandbox" 환경에 대해 알아볼 것입니다.

이 수업을 마치면 다음을 할 수 있게 됩니다:

1. 프롬프트 엔지니어링이 무엇이며 왜 중요한지 설명할 수 있습니다.
2. 프롬프트의 구성 요소와 사용 방법을 기술할 수 있습니다.
3. 프롬프트 엔지니어링을 위한 모범 사례와 기술을 배울 수 있습니다.
4. 배운 기술을 OpenAI 엔드포인트를 사용하여 실제 예시에 적용할 수 있습니다.

## 샌드박스(Sandbox) 학습

프롬프트 엔지니어링은 현재 과학이라기보다는 예술에 가깝습니다. 직관력 향상시키는 가장 좋은 방법은 _더 많이 실습하고_ 애플리케이션 도메인 전문 지식과 권장 기술, 모델별 최적화를 결합하는 시행착오적 접근 방식을 채택하는 것입니다.

이 레슨과 함께 제공되는 주피터 노트북은 학습한 내용을 시험해 볼 수 있는 _sandbox_ 환경을 제공합니다 - 학습을 진행하면서 또는 마지막에 코드 챌린지의 일부로 사용할 수 있습니다. 연습문제를 실행하기 위해서는 다음이 필요합니다:

1. OpenAI API 키 - 배포된 LLM의 서비스 엔드포인트입니다.

2. 파이썬 런타임 - 노트북을 실행할 수 있는 환경입니다.

이 리포지토리는 파이썬 3 런타임이 포함된 _dev container_ 로 구성되어 있습니다. GitHub 코드스페이스나 로컬 Docker 데스크톱에서 리포지토리를 열면 런타임이 자동으로 활성화됩니다. 그런 다음 노트북을 열고 Python 3.x 커널을 선택해 노트북을 실행할 준비를 하세요.

기본 노트북은 OpenAI API 키 사용에 맞게 설정되어 있습니다. 폴더 루트의 `.env.copy` 파일을 `.env`로 복사하고 `OPENAI_API_KEY=` 줄에 API 키를 업데이트하면 준비가 완료됩니다.

노트북에는 _starter_ 연습 문제가 포함되어 있지만, 직접 _Markdown_ (설명) 과 _Code_ (프롬프트 요청) 섹션을 자유롭게 추가하고 더 많은 예제나 아이디어를 시도해보고 프롬프트 디자인에 대한 직관을 키우는 것이 좋습니다.

## Our Startup

이제, _이번 주제_ 가 [교육에 AI 혁신을 가져오기](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst)하는 우리 스타트업 미션과 어떻게 관련되는지에 대해 이야기해보겠습니다. 우리는 _맞춤 학습(personalized learning)_ 의 AI 기반 응용 프로그램을 구축하고 싶습니다. - 따라서 우리 애플리케이션의 다양한 사용자가 프롬프트를 어떻게 "디자인"할 수 있는지 생각해 봅시다:

- **관리자** 는 AI에게 _교육과정 데이터를 분석하여 커버리지의 공백을 식별하도록_ 요청할 수 있습니다. AI는 결과를 요약하거나 코드로 시각화할 수 있습니다.
- **교육자** 는 AI에게 _대상 교육생과 주제에 대한 수업 계획을 작성하도록_ 요청할 수 있습니다. AI는 지정된 형식으로 맞춤형 계획을 작성할 수 있습니다.
- **학생** 들은 AI에게 _어려운 과목을 가르쳐달라고_ 요청할 수 있습니다. AI는 이제 학생들의 수준에 맞춘 수업, 힌트 및 예시로 학생들을 안내할 수 있습니다.

이것은 빙산의 일각에 불과합니다. 교육 전문가들이 선별한 오픈소스 프롬프트 라이브러리인 [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - 을 확인하여 더 다양한 가능성을 살펴보세요! _샌드박스에서 몇 가지 프롬프트를 실행하거나 OpenAI Playground를 사용하여 어떤 일이 일어나는지 확인해 보세요!_  

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## 프롬프트 엔지니어링이란 무엇인가요?

우리는 이 수업을 특정 애플리케이션 목표와 모델에 대한 일관되고 질 좋은 응답(완성)을 내기 위해 텍스트 입력(프롬프트)의 _설계와 최적화_ 과정이라고 정의하는 **프롬프트 엔지니어링**으로 시작했습니다. 이를 2단계 과정으로 생각해볼 수 있습니다:

- 주어진 모델과 목표에 맞는 최초의 프롬프트 _설계하기_
- 반복적으로 프롬프트를 _정제하여_ 응답의 질을 높이기

이는 반드시 시행착오를 겪으며 사용자의 직관과 노력이 필요한 과정입니다. 그럼 왜 이것이 중요한가요? 그 질문에 답하기 위해서는 우선 세 가지 개념을 이해해야 합니다:

- _Tokenization_ = 모델이 프롬프트를 "어떻게 보는지"
- _Base LLMs_ = 기초 모델이 프롬프트를 "어떻게 처리하는지"
- _Instruction-Tuned LLMs_ = 모델이 이제 "작업"을 "어떻게 파악하는지"

### Tokenization

LLM은 프롬프트를 _토큰의 시퀀스_ 로 보며, 다른 모델(또는 모델의 버전)은 동일한 프롬프트를 다른 방식으로 토크나이징 할 수 있습니다. LLM은 토큰에 대해 훈련받기 때문에(원시 텍스트가 아니라), 프롬프트를 토크나이징하는 방식은 생성된 응답의 질에 직접적인 영향을 미칩니다.

토크나이제이션이 어떻게 작동하는지 직관적으로 이해하려면, 아래에 표시된 [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst)와 같은 도구를 사용해보세요. 여러분의 프롬프트를 복사하여 붙여넣고 - 그것이 어떻게 토큰으로 변환되는지 확인해보세요. 빈칸 문자와 구두점이 어떻게 처리되는지 주목하세요. 이 예시는 이전 버전의 LLM(GPT-3)을 보여주기 때문에, 새로운 모델로 시도하면 다른 결과가 나올 수 있습니다.

![Tokenization](../../images/04-tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

### 개념: 기초 모델(Foundation Models)

프롬프트가 토크나이징되면, ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (또는 기초 모델)의 주 기능은 해당 시퀀스에서 토큰을 예측하는 것입니다. LLM은 방대한 텍스트 데이터셋에 대해 훈련받기 때문에 토큰 간의 통계적 관계를 잘 파악하여 어느 정도의 확신을 가지고 예측을 할 수 있습니다. LLM은 프롬프트나 토큰의 _의미_ 를 이해하지 않습니다; 그저 다음 예측으로 "완성"할 수 있는 패턴을 보는 것뿐입니다. 사용자의 개입이나 사전에 설정된 조건에 의해 종료될 때까지 시퀀스 예측을 계속할 수 있습니다.

프롬프트 기반 완성이 어떻게 작동하는지 보고 싶으신가요? 위의 프롬프트를 Azure OpenAI Studio의 [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)에 기본 설정으로 입력해보세요. 시스템은 프롬프트를 정보 요청으로 처리하도록 설정되어 있기 때문에, 이 컨텍스트를 만족하는 완성/결과물(completion)을 볼 수 있습니다.

하지만 사용자가 특정 기준이나 작업 목표를 충족하는 특정한 것을 보고 싶다면 어떨까요? 이때 _지시학습으로 조정된(instruction-tuned)_ LLM이 등장합니다.

![Base LLM Chat Completion](../../images/04-playground-chat-base.png?WT.mc_id=academic-105485-koreyst)

### 개념: 지시학습으로 조정된 LLMs

[지시학습 튜닝된 LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst)은 기본 모델로 시작하여 사람이 이해하기 쉬운 지시사항을 포함한 예시나 입력/출력 쌍(예를 들어, 여러 턴의 "메시지")으로 정교하게 튜닝합니다 - 그리고 AI의 응답은 해당 지시사항을 따르려고 시도합니다.

이는 사람의 피드백을 통한 강화 학습(Reinforcement Learning with Human Feedback, RLHF)과 같은 기법을 사용하여 모델이 _지시사항을 따르고_ _피드백으로부터 배우도록_ 훈련하는데, 결과적으로 실용적인 애플리케이션에 더 적합하고 사용자의 목표에 더 관련 있는 응답을 생성하게 됩니다.

위의 프롬프트를 다시 살펴보고 이제 _system message_를 변경하여 다음 명령어를 컨텍스트로 제공하세요:

> _2학년 학생을 위해 제공된 콘텐츠를 요약합니다. 결과를 3~5개의 글머리 기호로 구성된 한 단락으로 유지하세요._

이제 원하는 목표와 형식을 반영하여 결과가 어떻게 조정되어 있는지 보셨나요? 이제 교육자는 이 응답을 해당 수업의 슬라이드에 직접 사용할 수 있습니다.

![Instruction Tuned LLM Chat Completion](../../images/04-playground-chat-instructions.png?WT.mc_id=academic-105485-koreyst)

## 왜 프롬프트 엔지니어링이 필요한가요?

이제 LLM들이 어떻게 프롬프트를 처리하는지 알았으니, _왜_ 프롬프트 엔지니어링이 필요한지 얘기해봅시다. 답은 현재 LLM들이 내포하는 여러 도전적인 과제들 때문인데, 이로 인해 노력 없이 프롬프트 구성과 최적화를 통해 _신뢰할 수 있고 일관된 완성들_ 을 달성하기 어려워졌습니다. 예를 들면:

1. **모델 응답은 확률적입니다.** _동일한 프롬프트_ 는 서로 다른 모델이나 모델 버전으로 실행했을 때 다른 결과를 낼 것이며, 심지어 _동일한 모델_ 이라도 다른 시간에는 다른 결과를 낼 수도 있습니다. _프롬프트 엔지니어링 기법은 더 나은 가이드라인을 제공하여 이런 변동성을 최소화하는데 도움을 줄 수 있습니다._

1. **모델이 응답을 조작할 수 있습니다.** 모델은 _크지만 한정된_ 데이터셋으로 사전 훈련되기 때문에 그 훈련 범위 밖의 개념에 대한 지식이 없습니다. 결과적으로, 부정확하거나 상상 속의 것, 혹은 알려진 사실과 직접적으로 모순되는 완성들을 생성할 수 있습니다. _프롬프트 엔지니어링 기법은 사용자가 이러한 조작을 식별하고 완화하는데 도움을 줄 수 있습니다. 예를 들어, 인용이나 이유를 AI에게 요청하도록 함으로써._

1. **모델의 능력은 다양합니다.** 새로운 모델이나 모델 세대는 더 풍부한 기능을 제공하지만, 비용과 복잡성 면에서 고유한 특징과 타협점을 가지게 됩니다. _프롬프트 엔지니어링은 최상의 실무 방식과 작업 흐름을 개발하는데 도움을 줄 수 있으며 차이를 추상화하고 모델별 요구사항에 맞춰 확장 가능하고 원활하게 적응할 수 있습니다._

OpenAI 또는 Azure OpenAI Playground에서 이를 실제로 적용해봅시다:

- 다른 LLM 배포(예: OpenAI, Azure OpenAI, Hugging Face)에 동일한 프롬프트를 사용해보세요 - 변화를 보셨나요?
- _동일한_ LLM 배포(예: Azure OpenAI playground)에서 동일한 프롬프트를 반복해서 사용해보세요 - 이러한 변화가 어떻게 달랐나요?

### 정보 조작 예시

이번 강의에서 우리는 LLMs이 훈련 과정의 한계나 기타 제약으로 인해 사실과 어긋나는 정보를 만들어내는 현상을 지칭하기 위해 **"정보 조작"** 이라는 용어를 사용합니다. 이것은 기사나 연구 논문에서 _"환각"_ 이라고도 불리기도 합니다. 그러나 우리는 기계가 주도하는 결과에 인간과 같은 특성을 부여함으로써 실수로 인류화하는 것을 피하기 위해 _"정보 조작"_ 이라는 용어를 사용하는 것을 강력히 권장합니다. 또한 이는 용어 사용 측면에서 [책임감 있는 AI 지침](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)을 강화하는 것이며, 특정 상황에서 불쾌하거나 포괄적이지 않은 것으로 간주될 수 있는 용어를 제거하는 데에도 도움이 됩니다.

정보 조작이 어떻게 작동하는지 궁금하신가요? 훈련 데이터셋에서 찾을 수 없는, 존재하지 않는 주제에 대한 내용을 생성하도록 AI에 지시하는 프롬프트를 생각해 보세요. 예를 들어, 저는 이런 프롬프트를 시도했습니다:
> **프롬프트:** 2076년 화성 전쟁에 대한 수업 계획을 작성하세요.

웹 검색을 통해 화성 전쟁에 대한 허구적인 묘사(예: TV 시리즈나 책)이 있음을 알 수 있겠지만, 2076년에는 없었습니다. 상식적으로 2076년은 _미래에 있기 때문에_ 실제 사건과 연관될 수 없지요.

그렇다면 이 프롬프트를 다양한 LLM 제공자들과 실행하면 어떻게 될까요?

> **응답 1**: OpenAI Playground (GPT-35)

![응답 1](../../images/04-fabrication-oai.png?WT.mc_id=academic-105485-koreyst)

**응답 2**: Azure OpenAI Playground (GPT-35)

![응답 2](../../images/04-fabrication-aoai.png?WT.mc_id=academic-105485-koreyst)

> **응답 3**: Hugging Face Chat Playground (LLama-2)

![응답 3](../../images/04-fabrication-huggingchat.png?WT.mc_id=academic-105485-koreyst)

예상대로, 각 모델(또는 모델 버전)은 확률적 행동과 모델 능력의 차이로 인해 약간 다른 응답을 생성합니다. 예를 들어, 한 모델은 8학년 대상을 목표로 하는 반면 다른 모델은 고등학생을 가정합니다. 하지만 모든 세 모델은 사건이 실제로 일어났다고 잘못된 정보를 가진 사용자를 속일 수 있는 응답을 생성했습니다.

_메타프롬프팅_ 및 _온도 설정_ 과 같은 프롬프트 엔지니어링 기술은 모델 정보 조작을 어느 정도 줄일 수 있습니다. 새로운 프롬프트 엔지니어링 _아키텍처_ 또한 새로운 도구와 기술을 프롬프트 흐름에 완벽하게 통합하여 이러한 효과를 완화하거나 줄이기도 합니다.

## 사례 연구: GitHub Copilot

이 섹션을 마무리하며 실제 솔루션에서 프롬프트 엔지니어링이 어떻게 사용되는지를 이해하기 위해 하나의 사례 연구를 살펴보겠습니다: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot은 여러분의 "AI 페어 프로그래머"로, 텍스트 프롬프트를 코드 완성으로 변환하며 개발 환경(예: Visual Studio Code)에 통합되어 원활한 사용자 경험을 제공합니다. 아래 블로그 시리즈에서 기술된 바와 같이, 초기 버전은 OpenAI Codex 모델을 기반으로 했으며, 엔지니어들은 모델을 미세 조정하고 더 나은 프롬프트 엔지니어링 기술을 개발할 필요성을 빠르게 깨달았습니다. 이를 통해 코드 품질을 향상시켰습니다. 7월에는 더 빠른 제안을 위해 [Codex를 넘어선 개선된 AI 모델을 선보였습니다](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst).

그들의 학습 여정을 따라가며 이러한 포스트들을 순서대로 읽어보세요.

- **2023년 5월** | [GitHub Copilot은 코드 이해를 더 잘하기 위해 개선되고 있습니다](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **2023년 5월** | [GitHub 내부: GitHub Copilot 뒤에 있는 LLM과의 작업](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023년 6월** | [GitHub Copilot을 위한 더 나은 프롬프트 작성 방법](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **2023년 7월** | [.. GitHub Copilot은 Codex를 넘어 개선된 AI 모델로 더 나아갑니다](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **2023년 7월** | [개발자를 위한 프롬프트 엔지니어링 및 LLM 가이드](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **2023년 9월** | [GitHub Copilot에서 얻은 교훈: 기업용 LLM 앱 구축 방법](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

또한, [이 글](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst)처럼 실제 애플리케이션 구동에 이러한 모델과 기술이 _적용되는_ 방법을 보여주는 글들을 [GitHub의 엔지니어링 블로그](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst)에서 더 많이 찾아볼 수 있습니다.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## 프롬프트 구성

프롬프트 엔지니어링의 중요성을 이해했으니, 이제 프롬프트가 어떻게 _구성_ 되는지 이해해보고 더 효과적인 프롬프트 설계를 위한 다양한 기술을 검증해보겠습니다.

### 기본 프롬프트

기본 프롬프트부터 시작해보겠습니다: 모델에 전달된 텍스트 입력으로 다른 맥락(context)이 없습니다. 예시 - 미국 국가의 첫 몇 단어를 OpenAI [완성 API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)에 보내면, 바로 다음 몇 줄로 응답을 _완성_ 하는데요, 이는 기본적인 예측 동작을 보여줍니다.

| 프롬프트 (입력) | 완성 (출력) |
|:---|:---|
| Oh say can you see | "The Star-Spangled Banner,"미국의 국가로 시작하는 가사 같네요. 전체 가사는 ... |

### 복잡한 프롬프트

이제 기본 프롬프트에 맥락(context)과 지시사항(instructions)을 추가해 보겠습니다. [채팅 완성 API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst)를 사용하면, _메세지_ 의 컬렉션으로 다음과 같이 복잡한 프롬프트를 구성할 수 있습니다.

- _사용자_ 입력과 _어시스턴트_ 응답을 반영하는 입력/출력 쌍.
- 어시스턴트의 행동이나 성격에 대한 맥락을 설정하는 시스템 메세지.

이제 요청은 아래와 같은 형태로, _토큰화_ 는 맥락과 대화에서 관련 정보를 효과적으로 포착하는 아래 형식이 되었습니다. 이제 시스템 맥락을 변경하면 사용자가 입력한 정보만큼이나 완성도에 영향을 미칠 수 있습니다.

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### 지시 프롬프트

위의 예에서 사용자 프롬프트는 정보 요청으로 해석될 수 있는 단순한 텍스트 쿼리였습니다. _지시_ 프롬프트를 사용하면 해당 텍스트를 사용하여 작업을 더 자세히 지정하여 AI에 더 나은 안내를 제공할 수 있습니다. 다음은 예시입니다:

| Prompt (Input) | Completion (Output) | Instruction Type |
|:---|:---|:---|
| 남북전쟁에 대한 설명을 작성하라 | _간단한 단락이 반환됨_ | 간단함 |
| 남북전쟁에 대한 설명을 작성하라. 주요 날짜와 사건을 제공하고 그 중요성을 설명하라 | _주요 사건 날짜와 설명이 포함된 단락이 반환됨_ | 복잡함 |
| 남북전쟁에 대한 설명을 1단락으로 작성하라. 주요 날짜와 그 중요성에 대한 3개의 요점을 제공하라. 주요 역사적 인물과 그들의 공헌에 대한 3개의 요점을 더 제공하라. 출력을 JSON 파일로 반환하라 | _JSON으로 포맷된 텍스트 박스에서 더 광범위한 세부사항이 반환되며, 필요에 따라 파일로 복사하여 검증할 수 있음_ | 복잡함. 포맷형태. |

## 주요 내용

위의 예시에서 프롬프트는 여
위의 예시에서는 프롬프트가 여전히 상당히 열린 상태이므로 LLM이 사전 학습된 데이터 세트의 어떤 부분이 관련성이 있는지 결정할 수 있습니다. _주요 내용_ 디자인 패턴을 사용하면 입력 텍스트가 두 부분으로 나뉩니다:

- 명령어 (동작)
- (행동에 영향을 미치는) 관련 콘텐츠

다음은 "이 내용을 2문장으로 요약하라"는 지시가 있는 예시입니다.

| 프롬프트 (입력) | 완성 (출력) |
|:---|:---|
| 목성은 태양으로부터 다섯 번째 행성이며 태양계에서 가장 큰 행성입니다. 목성은 태양의 질량의 천분의 일이지만, 태양계 내 다른 모든 행성의 질량을 합친 것의 두 배 반에 달합니다. 목성은 맨눈으로 볼 수 있는 가장 밝은 천체 중 하나이며, 기록된 역사 이전부터 고대 문명에 알려져 있습니다. 목성은 로마 신 목성의 이름을 따서 명명되었습니다. 지구에서 볼 때, 목성은 반사된 빛으로 가시적인 그림자를 만들 정도로 충분히 밝을 수 있으며[19], 평균적으로 달과 금성에 이어 밤하늘에서 세 번째로 밝은 천연 물체입니다.[20] <br/> **이것을 2문장으로 요약하라** | 태양으로부터 다섯 번째에 위치한 목성은 태양계에서 가장 크며 밤하늘에서 가장 밝은 천체 중 하나로 알려져 있습니다. 로마 신 목성의 이름을 딴 이 가스 거인은 태양계 내 다른 모든 행성의 질량을 합친 것보다 두 배 반 더 큰 질량을 가지고 있습니다. |

주요 내용 부분은 다양한 방식으로 더 효과적인 지시를 위해 사용될 수 있습니다:

- **예시** - 명시적인 지시로 모델에게 무엇을 할지 알려주는 대신, 무엇을 해야 하는지에 대한 예시를 제공하고 패턴을 추론하게 합니다.
- **큐** - 지시문 뒤에 완성을 유도하는 '큐'를 추가하여 모델을 더 관련성 있는 응답으로 안내합니다.
- **템플릿** - 이는 프롬프트에 대한 반복 가능한 '레시피'로, 특정 사용 사례에 대한 데이터로 사용자 지정할 수 있는 자리표시자(변수)가 포함됩니다.

이러한 방식을 실제로 적용해 보겠습니다.

### 예시 사용하기

이 접근법에서는 주요 내용을 사용하여 모델에 원하는 출력에 대한 몇 가지 예시를 "제공"하고, 원하는 출력에 대한 패턴을 추론하게 합니다. 제공된 예시의 수에 따라 제로-샷 프롬프팅, 원-샷 프롬프팅, 퓨-샷 프롬프팅 등이 있을 수 있습니다.

프롬프트는 이제 세 가지 구성 요소로 구성됩니다:

- 작업 설명
- 원하는 출력의 몇 가지 예시
- 새로운 예시의 시작 부분(묵시적 작업 설명이 됨)

| 학습 유형 | 프롬프트 (입력) | 완성 (출력) |
|:---|:---|:---|
| 제로-샷  | "The Sun is Shining". 스페인어로 번역하라  | "El Sol está brillando".|
| 원-샷 | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" => | "Es un día frío y ventoso". |
| 퓨-샷 | 선수가 베이스를 돌았다 => 야구  <br/> 선수가 에이스를 쳤다 => 테니스  <br/> 선수가 식스를 쳤다 => 크리켓  <br/> 선수가 슬램덩크를 했다 => | 농구 |

제로-샷 프롬프팅에서는 명시적인 지시("스페인어로 번역하라")가 필요했지만, 원-샷 프롬프팅 예시에서는 추론으로 이루어집니다. 퓨-샷 예시에서는 추가 지시 없이 더 많은 예시를 추가함으로써 모델이 더 정확한 추론을 할 수 있음을 보여줍니다.

### 프롬프트 큐

주요 내용을 사용하는 또 다른 기술은 예시 대신 _큐_를 제공하는 것입니다. 이 경우, 우리는 원하는 응답 형식을 반영하는 스니펫으로 시작하여 모델에 올바른 방향으로 힌트를 주고 있습니다. 모델은 그 큐를 "이어받아" 그 방식으로 계속합니다.

| 큐의 개수 | 프롬프트 (입력) | 완성 (출력) |
|:---|:---|:---|
| 0  | 목성은 태양으로부터 다섯 번째 행성이며 태양계에서 가장 큰 행성입니다. 목성은 태양의 질량의 천분의 일이지만, 태양계 내 다른 모든 행성의 질량을 합친 것의 두 배 반에 달합니다. 목성은 맨눈으로 볼 수 있는 가장 밝은 천체 중 하나이며, 기록된 역사 이전부터 고대 문명에 알려져 있습니다. <br/>**이것을 요약하시오.**  | 목성은 우리 태양계에서 가장 큰 행성이며 태양으로부터 다섯 번째에 위치합니다. 목성은 가스 거인으로, 태양의 질량의 1/1000에 불과하지만, 다른 모든 행성의 질량을 합친 것보다 무겁습니다. 고대 문명들은 오랜 시간 동안 목성을 알고 있었으며, 이는 밤하늘에서 쉽게 볼 수 있습니다..|
| 1 | 목성은 태양으로부터 다섯 번째 행성이며 태양계에서 가장 큰 행성입니다. 목성은 태양의 질량의 천분의 일이지만, 태양계 내 다른 모든 행성의 질량을 합친 것의 두 배 반에 달합니다. 목성은 맨눈으로 볼 수 있는 가장 밝은 천체 중 하나이며, 기록된 역사 이전부터 고대 문명에 알려져 있습니다. <br/>**이것을 요약하시오.** <br/> 우리가 목성에 대해 배운 것은 | 태양으로부터 다섯 번째에 위치한 목성은 태양계에서 가장 큰 행성입니다. 이는 가스 거인으로, 태양의 질량의 천분의 일이지만, 태양계의 다른 모든 행성들의 총 질량의 두 배 반에 해당합니다. 목성은 맨눈으로도 쉽게 볼 수 있으며, 고대부터 알려져 왔습니다. |
| 2 | 목성은 태양으로부터 다섯 번째 행성이며 태양계에서 가장 큰 행성입니다. 목성은 태양의 질량의 천분의 일이지만, 태양계 내 다른 모든 행성의 질량을 합친 것의 두 배 반에 달합니다. 목성은 맨눈으로 볼 수 있는 가장 밝은 천체 중 하나이며, 기록된 역사 이전부터 고대 문명에 알려져 있습니다. <br/>**이것을 요약하시오.** <br/> 우리가 배운 상위 3가지 사실: | 1. 목성은 태양으로부터 다섯 번째에 위치한 태양계에서 가장 큰 행성입니다. <br/> 2. 이는 가스 거인으로, 태양의 질량의 1/1000이지만...<br/> 3. 목성은 고대 시대부터 맨눈으로 볼 수 있으며...  |

### 프롬프트 템플릿

프롬프트 템플릿은 필요에 따라 저장하고 재사용할 수 있는 _미리 정의된 프롬프트 레시피_로, 대규모로 보다 일관된 사용자 경험을 제공할 수 있습니다. 가장 간단한 형태는 [OpenAI의 이 프롬프트](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst)와 같은 프롬프트 예시 모음으로, 대화형 프롬프트 구성 요소(사용자 및 시스템 메시지)와 API기반 요청 방식 모두 제공하여 재사용을 지원합니다.

[LangChain의 이 예시](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/?WT.mc_id=academic-105485-koreyst)와 같이 좀 더 복잡한 형태에서는 다양한 소스(사용자 입력, 시스템 맥락, 외부 데이터 소스 등)의 데이터로 대체하여 프롬프트를 동적으로 생성할 수 있는 _placeholder_ 가 포함되어 있습니다. 이를 통해 재사용 가능한 프롬프트 라이브러리를 생성하여 대규모로 일관된 사용자 경험을 **프로그래밍적으로** 제공할 수 있습니다.

마지막으로, 탬플릿의 진정한 가치는 수직적 애플리케이션 도메인을 위한 _프롬프트 라이브러리_ 를 만들고 공개하는 기능입니다. 이제 프롬프트 템플릿은 애플리케이션 별로 맥락이나 예시를 반영하여 타겟 사용자틍에게 보다 적절하고 정확한 응답을 제공할 수 있도록 _최적화_ 됩니다. [교육용 프롬프트](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) 저장소는 이러한 접근 방식의 좋은 예로, 수업 계획, 커리큘럼 설계, 학생 개인지도 등과 같은 주요 목표에 중점을 둔 교육용 프롬프트 라이브러리를 관리하고 있습니다.

## 보조 내용

프롬프트 구성을 명령어(작업)와 대상(기본 컨텐츠)이 있는 것으로 생각 한다면, _보조 콘텐츠_ 는 **어떤 방식으로든 출력에 영향**을 미치기 위해 제공하는 추가 맥락과 같은 겁니다. 이는 매개변수, 서식 지정 지시문, 주체 분류 등을 설정하여 모델이 원하는 사용자 목표나 기대에 맞게 응답을 '맞춤화'하는 데 도움이 될 수 있습니다.

예를 들어, 커리큘럼에서 사용 가능한 모든 코스의 광범위한 메타데이터(이름, 설명, 수준, 메타데이터 테그, 교수자 등)가 포함된 코스 카탈로그가 있다고 가정해 보겠습니다.

- "2023년 가을 학기 과정 카탈로그를 요약하라"는 지시문을 정의할 수 있습니다.
- 원하는 출력의 몇 가지 예시를 제공하기 위해 주요 내용을 사용할 수 있습니다.
- 관심 있는 상위 5개 "태그"를 식별하기 위해 보조 내용을 사용할 수 있습니다.

이제 모델은 몇 가지 예시에서 보여준 형식으로 요약을 제공할 수 있지만, 결과에 여러 태그를 가질 경우 보조 내용에서 식별된 5개 태그를 우선시할 수 있습니다.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Prompting Best Practices

Now that we know how prompts can be _constructed_, we can start thinking about how to _design_ them to reflect best practices. We can think about this in two parts - having the right _mindset_ and applying the right _techniques_.

### Prompt Engineering Mindset

Prompt Engineering is a trial-and-error process so keep three broad guiding factors in mind:

1. **Domain Understanding Matters.** Response accuracy and relevance is a function of the _domain_ in which that application or user operates. Apply your intuition and domain expertise to **customize techniques** further. For instance, define _domain-specific personalities_ in your system prompts, or use _domain-specific templates_ in your user prompts. Provide secondary content that reflects domain-specific contexts, or use _domain-specific cues and examples_ to guide the model towards familiar usage patterns.

2. **Model Understanding Matters.** We know models are stochastic by nature. But model implementations can also vary in terms of the training dataset they use (pre-trained knowledge), the capabilities they provide (e.g., via API or SDK) and the type of content they are optimized for (e.g, code vs. images vs. text). Understand the strengths and limitations of the model you are using, and use that knowledge to _prioritize tasks_ or build _customized templates_ that are optimized for the model's capabilities.

3. **Iteration & Validation Matters.** Models are evolving rapidly, and so are the techniques for prompt engineering. As a domain expert, you may have other context or criteria _your_ specific application, that may not apply to the broader community. Use prompt engineering tools & techniques to "jump start" prompt construction, then iterate and validate the results using your own intuition and domain expertise. Record your insights and create a **knowledge base** (e.g, prompt libraries) that can be used as a new baseline by others, for faster iterations in the future.

## Best Practices

Now let's look at common best practices that are recommended by [Open AI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) and [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) practitioners.

| What | Why |
|:---|:---|
| Evaluate the latest models. | New model generations are likely to have improved features and quality - but may also incur higher costs. Evaluate them for impact, then make migration decisions. |
| Separate instructions & context | Check if your model/provider defines _delimiters_ to distinguish instructions, primary and secondary content more clearly. This can help models assign weights more accurately to tokens. |
|Be specific and clear | Give more details about the desired context, outcome, length, format, style etc. This will improve both the quality and consistency of responses. Capture recipes in reusable templates. |
|Be descriptive, use examples |Models may respond better to a "show and tell" approach. Start with a `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies.|
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.|
|Double Down | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.|
| Order Matters | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.|
|Give the model an “out” | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses. |
| | |

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

- Copt the `.env.copy` file in repo root to `.env` and fill in the `OPENAI_API_KEY` value. You can find your API Key in your [OpenAI Dashboard](https://beta.openai.com/account/api-keys?WT.mc_id=academic-105485-koreyst).

### Next, open the Jupyter Notebook

- Select the runtime kernel. If using options 1 or 2, simply select the default Python 3.10.x kernel provided by the dev container.

You're all set to run the exercises. Note that there are no _right and wrong_ answers here - just exploring options by trial-and-error and building intuition for what works for a given model and application domain.

_For this reason there are no Code Solution segments in this lesson. Instead, the Notebook will have Markdown cells titled "My Solution:" that shows one example output for reference._

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Knowledge check

Which of the following is a good prompt following some reasonable best practices?

1. Show me an image of red car
2. Show me an image of red car of make Volvo and model XC90 parked by a cliff with the sun setting
3. Show me an image of red car of make Volvo and model XC90

A: 2, it's the best prompt as it provides details on "what" and goes into specifics (not just any car but a specific make and model) and it also describes the overall setting. 3 is next best as it also contains a lot of description.

## 🚀 Challenge

See if you can leverage the "cue" technique with the prompt: Complete the sentence "Show me an image of red car of make Volvo and ". What does it respond with, and how would you improve it?

## Great Work! Continue Your Learning

Want to learn more about different Prompt Engineering concepts? Go to the [contiuned learning page](../../../13-continued-learning/translations/ko-kr/README.md?WT.mc_id=academic-105485-koreyst) to find other great resources on this topic.

Head over to Lesson 5 where we will look at [advance prompting techniques](../../../05-advanced-prompts/translations/ko-kr/README.md?WT.mc_id=academic-105485-koreyst)!
