[![함수 호출과 통합](../../../translated_images/ko/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 생성형 AI 애플리케이션 라이프사이클

모든 AI 애플리케이션에 있어 중요한 질문은 AI 기능의 적절성입니다. AI는 빠르게 발전하는 분야이기 때문에 애플리케이션이 관련성 있고 신뢰할 수 있으며 견고하게 유지되도록 지속적으로 모니터링, 평가 및 개선해야 합니다. 여기서 생성형 AI 라이프사이클이 역할을 합니다.

생성형 AI 라이프사이클은 생성형 AI 애플리케이션을 개발, 배포 및 유지하는 단계를 안내하는 프레임워크입니다. 이 라이프사이클은 목표를 정의하고 성능을 측정하며 문제를 식별하고 해결책을 구현하도록 도와줍니다. 또한 애플리케이션을 도메인 및 이해관계자의 윤리적, 법적 기준과 정렬하도록 돕습니다. 생성형 AI 라이프사이클을 따르면 애플리케이션이 항상 가치를 제공하고 사용자 만족을 보장할 수 있습니다.

## 소개

이 장에서는 다음 내용을 다룹니다:

- MLOps에서 LLMOps로의 패러다임 전환 이해
- LLM 라이프사이클
- 라이프사이클 도구
- 라이프사이클 측정 및 평가

## MLOps에서 LLMOps로의 패러다임 전환 이해

LLM은 인공지능 무기고에서 새로운 도구입니다. 애플리케이션의 분석 및 생성 작업에서 매우 강력하지만, 이 힘은 AI 및 기존 머신러닝 작업을 간소화하는 방식에 일부 영향을 미칩니다.

이에 따라 우리는 이 도구를 역동적으로 올바른 인센티브와 함께 적응시킬 새로운 패러다임이 필요합니다. 이전 AI 앱은 "ML 앱"으로, 최신 AI 앱은 주류 기술과 기법을 반영하여 "GenAI 앱" 또는 단순히 "AI 앱"으로 분류할 수 있습니다. 이는 우리의 서사를 여러 면에서 전환시킵니다. 다음 비교를 살펴보십시오.

![LLMOps vs. MLOps 비교](../../../translated_images/ko/01-llmops-shift.29bc933cb3bb0080.webp)

LLMOps에서는 앱 개발자에 좀 더 집중하며, 통합을 핵심 요소로 활용하고 "서비스형 모델"을 사용하며 다음 지표에 고민합니다.

- 품질: 응답 품질
- 해악: 책임 있는 AI
- 정직성: 응답의 근거 (말이 되는가? 정확한가?)
- 비용: 솔루션 예산
- 대기 시간: 토큰 응답 평균 시간

## LLM 라이프사이클

먼저, 라이프사이클과 변경 사항을 이해하기 위해 다음 인포그래픽을 확인해 보겠습니다.

![LLMOps 인포그래픽](../../../translated_images/ko/02-llmops.70a942ead05a7645.webp)

보시다시피, 이는 일반적인 MLOps 라이프사이클과 다릅니다. LLM은 프롬프트, 품질 향상을 위한 다양한 기법(파인튜닝, RAG, 메타 프롬프트), 책임 있는 AI에 따른 평가 및 책임, 최종적으로 새로운 평가 지표(품질, 해악, 정직성, 비용, 대기 시간) 등 다양한 새로운 요구사항을 가집니다.

예를 들어, 아이디어 구상 방식을 살펴보십시오. 다양한 LLM을 실험하는 프롬프트 엔지니어링을 통해 가설이 맞는지 탐구하는 방식입니다.

이것은 선형이 아니라 통합되고 반복적이며 전체 주기를 포괄하는 구조임을 주의하세요.

이 단계를 어떻게 탐색할 수 있을까요? 라이프사이클 구축에 대해 자세히 살펴보겠습니다.

![LLMOps 워크플로우](../../../translated_images/ko/03-llm-stage-flows.3a1e1c401235a6cf.webp)

다소 복잡해 보일 수 있으니, 우선 세 가지 주요 단계에 집중해 봅시다.

1. 아이디어 구상/탐색: 비즈니스 요구에 맞게 자유롭게 탐색합니다. 프로토타이핑, [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)를 만들고 가설에 충분히 효과적인지 테스트합니다.
1. 구축/보강: 구현 단계로, 더 큰 데이터셋을 평가하고 파인튜닝, RAG 같은 기법을 적용해 솔루션의 견고성을 확인합니다. 문제가 있으면 흐름에 새 단계를 추가하거나 데이터를 재구조화해 재구현할 수 있습니다. 테스트와 확장 후 지표가 충족되면 다음 단계로 진행합니다.
1. 운영화: 통합 단계로, 모니터링 및 알림 시스템을 추가하고 애플리케이션 배포 및 통합을 진행합니다.

이후 보안, 규정 준수, 거버넌스를 중점으로 관리의 포괄적 주기가 이어집니다.

축하합니다, 이제 AI 앱이 준비되어 운영할 수 있습니다. 직접 체험해 보려면 [Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)를 참고하세요.

그럼, 어떤 도구를 사용할 수 있을까요?

## 라이프사이클 도구

도구로써, Microsoft는 [Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst)과 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)를 제공하여 라이프사이클 구현을 용이하게 하고 즉시 활용할 수 있도록 합니다.

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst)는 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)를 사용할 수 있도록 합니다. Microsoft Foundry(이전 Azure AI Studio)는 모델, 샘플, 도구를 탐색하고, 자원 관리하며, UI 개발 흐름과 SDK/CLI 옵션을 활용하여 코드 우선 개발을 지원하는 웹 포털입니다.

![Azure AI 가능성](../../../translated_images/ko/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI는 여러 자원을 활용하여 운영, 서비스, 프로젝트, 벡터 검색 및 데이터베이스 요구를 관리할 수 있도록 합니다.

![Azure AI와 함께하는 LLMOps](../../../translated_images/ko/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Proof-of-Concept(POC)부터 대규모 애플리케이션까지 PromptFlow와 함께 구축하기:

- VS Code에서 시각적 및 기능 도구로 앱 설계 및 구축
- 쉽고 빠른 품질 AI 테스트 및 파인튜닝
- Microsoft Foundry를 사용해 클라우드와 통합 및 반복, 빠른 통합을 위한 Push 및 배포

![PromptFlow와 함께하는 LLMOps](../../../translated_images/ko/06-llm-promptflow.a183eba07a3a7fdf.webp)

## 훌륭합니다! 학습을 계속하세요!

멋집니다, 이제 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)으로 애플리케이션 구조와 개념이 어떻게 응용되는지 배우고 Cloud Advocacy가 데모에 어떻게 개념을 적용하는지 확인하세요. 더 많은 콘텐츠는 [Ignite breakout session!](https://www.youtube.com/watch?v=DdOylyrTOWg)에서 확인하세요.


이제 15강을 확인하여 [Retrieval Augmented Generation과 벡터 데이터베이스](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst)가 생성형 AI에 미치는 영향과 더 매력적인 애플리케이션을 만드는 방법을 이해해 보세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->