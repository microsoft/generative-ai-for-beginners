# 생성형 AI 애플리케이션 생애주기

모든 AI 애플리케이션에 중요한 질문은 AI 기능의 적절성입니다. AI는 빠르게 발전하는 분야이므로, 애플리케이션이 지속적으로 관련성, 신뢰성 및 강건성을 유지하도록 하기 위해서는 모니터링, 평가 및 개선이 계속 필요합니다. 이러한 과정에서 생성형 AI 생애주기가 중요한 역할을 합니다.

생성형 AI 생애주기는 생성형 AI 애플리케이션을 개발, 배포 및 유지 관리하는 단계를 안내하는 프레임워크입니다. 이를 통해 목표를 설정하고, 성능을 측정하며, 도전에 대응하고, 해결책을 구현할 수 있습니다. 또한, 도메인 및 이해 관계자의 윤리적 및 법적 기준에 애플리케이션을 일치시킬 수 있도록 도와줍니다. 생성형 AI 생애주기를 따르면 애플리케이션이 항상 가치를 제공하고 사용자 만족도를 충족시킬 수 있습니다.

## 소개

이 장에서는 다음을 이해할 것입니다:

- MLOps에서 LLMOps로의 패러다임 전환
- LLM 수명 주기
- 수명 주기 도구
- 수명 주기 측정 및 평가

## MLOps에서 LLMOps로의 패러다임 전환 이해하기

LLM은 인공지능 무기고의 새로운 도구로서, 응용 프로그램의 분석 및 생성 작업에 있어서 매우 강력합니다. 그러나 이 강력함은 AI와 고전적인 머신 러닝 작업을 간소화하는 방식에 몇 가지 영향을 미칩니다.

이와 함께, 우리는 동적으로 이 도구를 적응시키기 위한 새로운 패러다임이 필요합니다. 적절한 인센티브로 말이죠. 이전의 AI 애플리케이션은 "ML 애플리케이션"으로, 새로운 AI 애플리케이션은 "GenAI 애플리케이션" 또는 단순히 "AI 애플리케이션"으로 분류할 수 있는데, 이는 당시에 사용된 주류 기술과 기법을 반영합니다. 이는 여러 방식으로 우리 내러티브를 변화시킵니다. 다음 비교를 살펴보세요.

![LLMOps vs. MLOps 비교](../../images/01-llmops-shift.png?WT.mc_id=academic-105485-koreys)

LLMOps에서는 앱 개발자에 더욱 초점을 맞추고, 통합을 주요 포인트로 사용하며 "서비스로서의 모델(Models-as-a-Service)"을 사용하고 지표를 다음과 같이 생각합니다.

- 품질: 응답 품질
- 해악: 책임 있는 AI
- 정직성: 응답의 타당성 (의미가 있는가? 정확한가?)
- 비용: 솔루션 예산
- 지연 시간: 평균 토큰 응답 시간

## LLM 라이프사이클

먼저, 라이프사이클과 그 변화를 이해하기 위해 다음 인포그래픽을 참고하세요.

![LLMOps infographic](../../images/02-llmops.png?WT.mc_id=academic-105485-koreys)

보시다시피, 이것은 일반적인 MLOps 라이프사이클과 다릅니다. LLM은 프롬프트 엔지니어링, 품질 향상을 위한 다양한 기법 (Fine-Tuning, RAG, Meta-Prompts), 책임 있는 AI와의 평가 및 책임 등 여러 새로운 요구 사항이 있습니다. 마지막으로, 새로운 평가 지표 (품질, 해악, 정직성, 비용 및 지연)가 있습니다.

예를 들어, 우리는 다양한 LLM을 사용하여 가설이 맞는지 테스트하기 위해 프롬프트 엔지니어링을 사용하여 아이디어를 구상합니다.

이는 선형적이지 않으며, 통합된 루프, 반복적이며 전반적인 주기로 이루어집니다.

이 단계를 탐색하려면 어떻게 해야 할까요? 라이프사이클을 구축하는 방법에 대해 자세히 살펴보겠습니다.

![LLMOps Workflow](../../images/03-llm-stage-flows.png?WT.mc_id=academic-105485-koreys)

이것은 약간 복잡해 보일 수 있습니다. 먼저 세 가지 큰 단계에 집중해 보겠습니다.

1. 아이디어 구상/탐색: 탐색 단계입니다. 여기에서 비즈니스 요구에 따라 탐색할 수 있습니다. 프로토타이핑, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 생성 및 가설이 충분히 효율적인지 테스트합니다.
1. 구축/증강: 구현 단계입니다. 이제 더 큰 데이터 세트를 평가하고 Fine-Tuning 및 RAG와 같은 기법을 사용하여 솔루션의 견고성을 확인합니다. 해결되지 않으면, 흐름에 새로운 단계를 추가하거나 데이터를 재구조화하는 등의 재구현이 도움이 될 수 있습니다. 흐름과 확장을 테스트하여 작동하고 지표가 만족스러우면 다음 단계로 넘어갈 준비가 된 것입니다.
1. 운영화: 통합 단계입니다. 이제 모니터링 및 경고 시스템을 시스템에 추가하고 애플리케이션에 배포하고 통합합니다.

그런 다음 보안, 컴플라이언스 및 거버넌스를 중심으로 관리 주기가 있습니다.

축하합니다, 이제 AI 애플리케이션이 준비되어 운영 가능합니다. 실습 경험을 원한다면, [Contoso Chat 데모](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)를 참조하세요.

이제 어떤 도구를 사용할 수 있을까요?

## 라이프사이클 도구

도구에 관해서는, Microsoft는 [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)과 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 제공하여 사용자가 쉽게 주기를 구현하고 실행할 수 있도록 합니다.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)은 [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)를 사용할 수 있게 합니다. AI Studio는 다양한 모델, 샘플, 도구 등을 탐색할 수 있는 웹 포털입니다. 자원을 관리하고, UI 개발 흐름과 코드-중심 개발을 위한 SDK/CLI 옵션을 포함합니다.

![Azure AI 가능성](../../images/04-azure-ai-platform.png?WT.mc_id=academic-105485-koreys)

Azure AI는 여러 자원을 사용하여 운영, 서비스, 프로젝트, 벡터 검색 및 데이터베이스 필요를 관리할 수 있게 합니다.

![LLMOps with Azure AI](../../images/05-llm-azure-ai-prompt.png?WT.mc_id=academic-105485-koreys)

PromptFlow와 함께 개념 증명(Proof-of-Concept, POC)에서 대규모 애플리케이션까지 구축:

- VS Code에서 시각적이고 기능적인 도구를 사용하여 앱을 설계하고 빌드
- 품질 높은 AI를 위해 앱을 쉽게 테스트하고 조정
- 클라우드와 통합하고 반복하기 위해 Azure AI Studio를 사용하고, 신속한 통합을 위해 Push 및 Deploy

![LLMOps with PromptFlow](../../images/06-llm-promptflow.png?WT.mc_id=academic-105485-koreys)

## 훌륭합니다! 학습을 계속하세요!

놀랍습니다! 이제 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)을 통해 애플리케이션을 구조화하여 개념을 사용하는 방법을 배우고, Cloud Advocacy가 이러한 개념을 데모에 추가하는 방식을 확인하세요. 더 많은 콘텐츠를 보려면 [Ignite 분과 세션](https://www.youtube.com/watch?v=DdOylyrTOWg)을 확인하세요!

이제 Lesson 15를 확인하여 [Retrieval Augmented Generation 및 벡터 데이터베이스](../../../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst)가 생성 AI에 미치는 영향과 보다 흥미로운 애플리케이션을 만드는 방법을 이해하세요!
