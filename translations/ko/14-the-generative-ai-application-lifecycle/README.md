<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T13:48:33+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "ko"
}
-->
[![함수 호출과 통합하기](../../../translated_images/ko/14-lesson-banner.066d74a31727ac12.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 생성형 AI 애플리케이션 수명 주기

모든 AI 애플리케이션에 중요한 질문은 AI 기능의 적합성입니다. AI는 빠르게 진화하는 분야이므로, 애플리케이션이 관련성 있고 신뢰할 수 있으며 견고하게 유지되도록 지속적으로 모니터링, 평가 및 개선해야 합니다. 바로 이 점에서 생성형 AI 수명 주기가 필요합니다.

생성형 AI 수명 주기는 생성형 AI 애플리케이션을 개발, 배포 및 유지 관리하는 단계를 안내하는 프레임워크입니다. 목표를 정의하고, 성과를 측정하며, 문제를 식별하고, 해결책을 구현하는 데 도움을 줍니다. 또한 도메인과 이해관계자의 윤리적 및 법적 기준에 애플리케이션을 맞추는 데도 도움을 줍니다. 생성형 AI 수명 주기를 따르면 애플리케이션이 항상 가치를 제공하고 사용자를 만족시키는지 보장할 수 있습니다.

## 소개

이 장에서 여러분은:

- MLOps에서 LLMOps로의 패러다임 전환 이해
- LLM 수명 주기
- 수명 주기 도구
- 수명 주기 측정 및 평가

## MLOps에서 LLMOps로의 패러다임 전환 이해

LLM은 인공지능 무기고의 새로운 도구로, 애플리케이션의 분석 및 생성 작업에서 매우 강력합니다. 하지만 이 강력함은 AI와 기존 머신러닝 작업을 간소화하는 방식에 몇 가지 영향을 미칩니다.

이에 따라 이 도구를 동적으로 적응시키고 올바른 인센티브를 부여하기 위한 새로운 패러다임이 필요합니다. 이전 AI 앱은 "ML 앱"으로, 최신 AI 앱은 "GenAI 앱" 또는 단순히 "AI 앱"으로 분류할 수 있으며, 이는 당시 주류 기술과 기법을 반영합니다. 이는 여러 면에서 우리의 내러티브를 변화시킵니다. 다음 비교를 살펴보세요.

![LLMOps vs. MLOps 비교](../../../translated_images/ko/01-llmops-shift.29bc933cb3bb0080.png)

LLMOps에서는 앱 개발자에 더 집중하며, 통합을 핵심 포인트로 사용하고, "서비스로서의 모델"을 활용하며 다음과 같은 지표를 고려합니다.

- 품질: 응답 품질
- 해악: 책임 있는 AI
- 정직성: 응답 근거 (말이 되는가? 정확한가?)
- 비용: 솔루션 예산
- 지연 시간: 토큰 응답 평균 시간

## LLM 수명 주기

먼저 수명 주기와 변경 사항을 이해하기 위해 다음 인포그래픽을 참고하세요.

![LLMOps 인포그래픽](../../../translated_images/ko/02-llmops.70a942ead05a7645.png)

보시다시피, 이는 일반적인 MLOps 수명 주기와 다릅니다. LLM은 프롬프트, 품질 향상을 위한 다양한 기법(파인튜닝, RAG, 메타 프롬프트), 책임 있는 AI에 따른 평가 및 책임, 그리고 새로운 평가 지표(품질, 해악, 정직성, 비용, 지연 시간) 등 많은 새로운 요구사항이 있습니다.

예를 들어, 아이디어를 구상하는 방식을 살펴보세요. 다양한 LLM을 실험하는 프롬프트 엔지니어링을 사용하여 가설이 맞는지 테스트할 가능성을 탐색합니다.

이는 선형적이지 않고 통합된 루프, 반복적이며 포괄적인 사이클임을 주목하세요.

이 단계를 어떻게 탐색할 수 있을까요? 수명 주기를 구축하는 방법을 자세히 살펴봅시다.

![LLMOps 워크플로우](../../../translated_images/ko/03-llm-stage-flows.3a1e1c401235a6cf.png)

조금 복잡해 보일 수 있으니, 먼저 세 가지 큰 단계에 집중해 봅시다.

1. 아이디어 구상/탐색: 탐색 단계로, 비즈니스 요구에 따라 탐색합니다. 프로토타입을 만들고 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)를 생성하여 가설에 충분히 효율적인지 테스트합니다.
1. 구축/확장: 구현 단계로, 이제 더 큰 데이터셋을 평가하고 파인튜닝, RAG 같은 기법을 적용하여 솔루션의 견고성을 확인합니다. 견고하지 않으면, 흐름에 새 단계를 추가하거나 데이터를 재구성하는 등 재구현할 수 있습니다. 흐름과 규모를 테스트하고 지표를 확인한 후, 준비가 되면 다음 단계로 넘어갑니다.
1. 운영화: 통합 단계로, 이제 모니터링 및 알림 시스템을 추가하고, 배포 및 애플리케이션 통합을 진행합니다.

그다음으로 보안, 규정 준수 및 거버넌스에 중점을 둔 관리의 포괄적 사이클이 있습니다.

축하합니다, 이제 AI 앱이 준비되어 운영할 수 있습니다. 실습 경험을 원한다면 [Contoso Chat 데모](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)를 확인해 보세요.

그럼, 어떤 도구를 사용할 수 있을까요?

## 수명 주기 도구

도구로는 Microsoft가 제공하는 [Azure AI 플랫폼](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)과 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)가 있어 수명 주기 구현을 쉽게 하고 준비할 수 있게 도와줍니다.

[Azure AI 플랫폼](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)은 [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)를 사용할 수 있게 합니다. AI Studio는 모델, 샘플, 도구를 탐색하고, 리소스를 관리하며, UI 개발 흐름과 코드 우선 개발을 위한 SDK/CLI 옵션을 제공하는 웹 포털입니다.

![Azure AI 가능성](../../../translated_images/ko/04-azure-ai-platform.80203baf03a12fa8.png)

Azure AI는 여러 리소스를 사용하여 운영, 서비스, 프로젝트, 벡터 검색 및 데이터베이스 요구를 관리할 수 있게 합니다.

![Azure AI와 함께하는 LLMOps](../../../translated_images/ko/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.png)

Proof-of-Concept(POC)부터 대규모 애플리케이션까지 PromptFlow로 구축하세요:

- VS Code에서 시각적 및 기능적 도구로 앱 설계 및 구축
- 품질 높은 AI를 위해 앱을 테스트하고 파인튜닝
- Azure AI Studio를 사용해 클라우드와 통합, 반복, 빠른 통합을 위한 푸시 및 배포

![PromptFlow와 함께하는 LLMOps](../../../translated_images/ko/06-llm-promptflow.a183eba07a3a7fdf.png)

## 훌륭합니다! 학습을 계속하세요!

멋집니다, 이제 [Contoso Chat 앱](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)에서 개념을 어떻게 구조화하는지 배우고, 클라우드 어드보커시가 데모에 어떻게 이 개념들을 적용하는지 확인하세요. 더 많은 콘텐츠는 [Ignite 브레이크아웃 세션!](https://www.youtube.com/watch?v=DdOylyrTOWg)을 참고하세요.

이제 15과를 확인하여 [검색 증강 생성 및 벡터 데이터베이스](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst)가 생성형 AI에 어떤 영향을 미치고 더 매력적인 애플리케이션을 만드는지 이해하세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->