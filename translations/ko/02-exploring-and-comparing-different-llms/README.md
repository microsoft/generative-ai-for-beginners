# 다양한 LLM 탐색 및 비교

[![다양한 LLM 탐색 및 비교](../../../translated_images/ko/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _위 이미지 클릭 시 본 강의 영상 시청 가능_

이전 강의를 통해 생성형 AI가 기술 환경을 어떻게 변화시키고 있는지, 대형 언어 모델(LLM)이 어떻게 작동하는지, 그리고 스타트업과 같은 기업이 이를 어떻게 적용해 비즈니스를 성장시킬 수 있는지를 살펴보았습니다. 이번 장에서는 다양한 유형의 대형 언어 모델(LLM)을 비교 분석하여 각각의 장단점을 이해할 예정입니다.

우리 스타트업 여정의 다음 단계는 현재 LLM 생태계를 탐색하고, 우리의 사용 사례에 적합한 모델을 이해하는 것입니다.

## 소개

이번 강의에서는 다음 주제를 다룹니다:

- 현 LLM 생태계의 다양한 유형 소개
- Azure에서 사용 사례에 맞게 다양한 모델 테스트, 반복, 비교하기
- LLM 배포 방법

## 학습 목표

본 강의를 완료하면 다음을 할 수 있습니다:

- 자신의 사용 사례에 맞는 적합한 모델 선택
- 모델을 테스트, 반복, 성능 개선하는 방법 이해
- 기업들이 모델을 어떻게 배포하는지 알기

## 다양한 유형의 LLM 이해하기

LLM은 아키텍처, 학습 데이터, 사용 사례에 따라 여러 분류가 가능합니다. 이러한 차이를 이해하면 우리 스타트업이 시나리오에 적합한 모델을 선택하고, 테스트, 반복, 성능 개선하는 데 도움이 됩니다.

LLM 모델 종류는 매우 다양하며, 어떤 목표로 사용할지, 데이터 종류, 비용 준비 정도 등에 따라 선택이 달라집니다.

텍스트, 오디오, 비디오, 이미지 생성 등 어떤 용도로 사용할지에 따라 다른 유형의 모델을 선택할 수 있습니다.

- **오디오 및 음성 인식**. Whisper 스타일 모델은 여전히 범용 음성 인식에 유용하지만, 현재는 `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` 같은 최신 음성-텍스트 모델과 diarization 변형도 선택지가 됩니다. 시나리오에 맞는 언어 지원, diarization, 실시간 지원, 지연 시간, 비용 등을 평가하세요. 자세한 내용은 [OpenAI 음성-텍스트 문서](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst)를 참고하세요.

- **이미지 생성**. DALL-E와 Midjourney가 잘 알려진 이미지 생성 옵션이지만, 현재 OpenAI 이미지 API는 `gpt-image-2` 같은 GPT 이미지 모델 중심이며 Stable Diffusion, Imagen, Flux 등도 보편적인 선택입니다. 프롬프트 준수, 편집 지원, 스타일 제어, 안전성 요구, 라이선스를 비교하세요. 자세한 내용은 [OpenAI 이미지 생성 가이드](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst)와 커리큘럼 9장을 참고하세요.

- **텍스트 생성**. 텍스트 모델에는 첨단 모델, 추론 모델, 소형 저지연 모델, 오픈 가중치 모델이 포함됩니다. 예로는 OpenAI GPT-5.x, Anthropic Claude 4.x, Google Gemini 3.x, Meta Llama 4, Mistral 모델 등이 있습니다. 출시일이나 가격만으로 선택하지 말고 작업 품질, 지연, 컨텍스트 창, 도구 활용, 안전 행태, 지역 가용성, 총 비용을 비교하세요. [Microsoft Foundry 모델 카탈로그](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst)는 Azure에서 사용 가능한 모델 비교에 좋은 장소입니다.

- <strong>멀티모달리티</strong>. 다수 현재 모델은 텍스트 외 입력도 처리합니다. 일부 모델은 이미지, 오디오, 비디오 입력을 받고, 도구 호출이 가능하며, 특화 모델은 이미지, 오디오, 비디오 생성도 합니다. 예를 들어, OpenAI 현재 모델은 텍스트와 이미지 입력을 지원하며, Gemini 모델은 변형에 따라 텍스트, 코드, 이미지, 오디오, 비디오 입력을 지원하고, Llama 4 Scout와 Maverick은 오픈 가중치 네이티브 멀티모달 모델입니다. 워크플로우 제작 전 각 모델 카드에서 지원하는 입력 및 출력 유형을 확인하세요.

모델 선택은 기본 기능을 획득하는 의미이나, 충분치 않을 수도 있습니다. 종종 회사별 데이터가 있어 LLM에 알려줄 필요가 있는데, 이를 위한 여러 선택지가 있으며 이후 섹션에서 자세히 다루겠습니다.

### 파운데이션 모델과 LLM의 차이

파운데이션 모델이라는 용어는 [스탠포드 연구진이 만든 용어](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)로, 다음 기준을 따르는 AI 모델을 의미합니다:

- **비지도 학습 또는 자기지도 학습으로 훈련된다**, 즉 라벨이 없는 멀티모달 데이터를 사용해 훈련하며, 학습 과정에 인간 주석이나 레이블이 필요 없습니다.
- **매우 큰 모델이다**, 수십억 개의 파라미터로 구성된 매우 깊은 신경망에 기반합니다.
- **일반적으로 다른 모델의 ‘기초’ 역할을 한다**, 즉 파인튜닝을 통해 다른 모델의 기반으로 사용하기 위해 설계됩니다.

![파운데이션 모델과 LLM 비교](../../../translated_images/ko/FoundationModel.e4859dbb7a825c94.webp)

이미지 출처: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

이 차이를 좀 더 명확히 하기 위해, 역사적 예로 ChatGPT를 들 수 있습니다. 초기 ChatGPT 버전은 GPT-3.5를 파운데이션 모델로 사용했고, OpenAI는 채팅 특화 데이터를 활용해 챗봇 대화에 더 적합한 조정된 버전을 만들었습니다. 현대 AI 서비스는 여러 모델 변형을 라우팅하기 때문에 서비스 명과 내부 모델 명은 항상 같지 않습니다.

![파운데이션 모델](../../../translated_images/ko/Multimodal.2c389c6439e0fc51.webp)

이미지 출처: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 오픈 가중치/오픈 소스 모델과 독점 모델

LLM 분류 방법 중 하나는 모델이 오픈 가중치, 오픈 소스인지 아니면 독점인지 여부입니다.

오픈 소스 및 오픈 가중치 모델은 모델 아티팩트를 검사, 다운로드, 맞춤화할 수 있게 공개하지만 라이선스는 다릅니다. 일부는 완전한 오픈 소스이고, 일부는 사용 제한이 있는 오픈 가중치입니다. 배포, 데이터 현지성, 비용, 맞춤화에 더 많은 권한이 필요한 기업에 유용하며, 사용 전 라이선스 조건, 서비스 비용, 유지보수, 보안 업데이트, 평가 품질을 반드시 검토해야 합니다. 예로는 [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), 일부 [Mistral 모델](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst), 그리고 [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst)에 있는 다수가 있습니다.

독점 모델은 제공자 소유 및 호스팅 모델로, 프로덕션용으로 최적화되고 강력한 지원, 안전 시스템, 도구 통합 및 규모 확장성을 제공합니다. 그러나 고객은 보통 모델 가중치를 공개하거나 변경할 수 없으며, 개인 정보, 보존, 준수, 사용 조건 등에 대해 제공자 약관을 반드시 검토해야 합니다. 예로 [OpenAI 모델](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst)가 있습니다.

### 임베딩, 이미지 생성, 텍스트 및 코드 생성 구분

LLM은 생성하는 출력 유형에 따라 구분할 수 있습니다.

임베딩은 텍스트를 임베딩이라고 하는 수치형태(숫자 벡터)로 변환하는 모델군입니다. 임베딩은 기계가 단어 또는 문장 간 관계를 이해하기 쉽게 해주며, 분류 모델이나 군집화 모델과 같은 다른 모델들의 입력으로 쓰이기도 합니다. 임베딩 모델은 주로 전이 학습(데이터가 풍부한 대체 작업을 위한 모델을 만들고, 그 가중치(임베딩)를 다른 작업에 재사용)로 사용됩니다. 이 범주의 예는 [OpenAI 임베딩](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)입니다.

![임베딩](../../../translated_images/ko/Embedding.c3708fe988ccf760.webp)

이미지 생성 모델은 이미지를 생성하는 모델입니다. 이들은 이미지 편집, 합성, 변환 등에 쓰이며, LAION-5B 같은 대규모 이미지 데이터셋으로 훈련됩니다. 새로운 이미지를 생성하거나 인페인팅, 초해상도, 색채화 기법으로 기존 이미지 편집에 이용됩니다. 예로는 [GPT 이미지 모델](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion 모델](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst), Imagen 모델이 있습니다.

![이미지 생성](../../../translated_images/ko/Image.349c080266a763fd.webp)

텍스트 및 코드 생성 모델은 텍스트나 코드를 생성하는 모델입니다. 이들은 텍스트 요약, 번역, 질문 응답에 주로 사용됩니다. 텍스트 생성 모델은 BookCorpus 같은 대규모 텍스트 데이터셋으로 훈련되며 새 텍스트 생성이나 질문에 답하는 데 쓰입니다. 코드 생성 모델은 CodeParrot처럼 GitHub 같은 대규모 코드 데이터로 훈련되며 새 코드를 생성하거나 기존 코드의 버그 수정에 사용됩니다.

![텍스트 및 코드 생성](../../../translated_images/ko/Text.a8c0cf139e5cc2a0.webp)

### 인코더-디코더 vs 디코더 전용 모델

LLM의 다양한 아키텍처 유형을 설명하기 위해 비유를 사용해 보겠습니다.

당신의 매니저가 학생들을 위한 퀴즈를 작성하는 임무를 줬다고 가정하세요. 당신에게는 콘텐츠를 생성하는 동료와 검토하는 동료 두 명이 있습니다.

콘텐츠 생성자는 디코더 전용 모델과 같습니다: 주제를 보고 이미 작성한 내용을 참고해 그 문맥을 바탕으로 콘텐츠를 생성합니다. 흥미롭고 유익한 콘텐츠 작성에 매우 능하지만, 분류, 검색, 인코딩 작업에는 최적이 아닙니다. GPT 및 Llama 모델이 디코더 전용 모델 가족에 해당합니다.

검토자는 인코더 전용 모델과 같습니다. 작성된 강의와 답안을 보고 그 관계를 파악해 문맥을 이해하지만, 콘텐츠 생성에는 적합하지 않습니다. BERT가 인코더 전용 모델 예시입니다.

퀴즈를 생성하고 검토할 수 있는 사람이 있다고 상상하세요. 이것이 인코더-디코더 모델입니다. BART와 T5가 이에 해당합니다.

### 서비스와 모델 차이점

이제 서비스와 모델의 차이를 이야기해 보겠습니다. 서비스는 클라우드 서비스 제공자가 제공하는 제품으로, 종종 모델, 데이터 및 기타 구성 요소의 조합입니다. 모델은 서비스의 핵심 구성 요소로, 종종 파운데이션 모델, 즉 LLM입니다.

서비스는 프로덕션 사용에 최적화되어 있고 그래픽 사용자 인터페이스를 통해 모델보다 사용하기 쉽습니다. 다만, 서비스는 항상 무료가 아니며 구독이나 사용량 기반 과금이 필요할 수 있습니다. 서비스 소유자의 장비와 자원을 이용해 비용을 최적화하고 쉽게 확장할 수 있습니다. 예로 [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst)는 종량제 요금제를 제공하며, 엔터프라이즈급 보안과 책임 있는 AI 프레임워크도 제공합니다.

모델은 신경망 산출물로, 파라미터, 가중치, 아키텍처, 토크나이저, 지원 구성 등을 포함합니다. 모델을 로컬이나 사설 환경에서 실행하려면 적합한 하드웨어, 서비스 인프라, 모니터링, 적합한 오픈 소스/오픈 가중치 라이선스나 상용 라이선스가 필요합니다. Llama 4나 Mistral 모델 같은 오픈 가중치 모델은 자체 호스팅 가능하지만 여전히 계산력과 운영 전문성이 요구됩니다.

## Azure에서 성능 이해를 위해 다양한 모델을 테스트하고 반복하는 방법


우리 팀이 현재 LLM 환경을 탐색하고 그 시나리오에 적합한 몇 가지 후보를 식별한 후 다음 단계는 해당 데이터와 작업 부하에서 테스트하는 것입니다. 이는 실험과 측정을 통해 반복적으로 수행되는 과정입니다.
이전 단락에서 언급한 대부분의 모델(OpenAI 모델, Llama 4 및 Mistral 같은 오픈 웨이트 모델, Hugging Face 모델)은 [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst)에서 사용할 수 있습니다.

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst)는 이전 명칭 Azure AI Studio/Azure AI Foundry로, AI 앱과 에이전트를 구축하기 위한 통합 Azure 플랫폼입니다. 실험, 평가부터 배포, 모니터링 및 거버넌스에 이르는 라이프사이클 관리를 개발자가 쉽게 할 수 있도록 돕습니다. Microsoft Foundry의 모델 카탈로그를 통해 사용자는 다음을 할 수 있습니다:

- Azure에서 판매하는 모델과 파트너 및 커뮤니티 제공자의 모델을 포함하여 관심 있는 기초 모델을 카탈로그에서 찾을 수 있습니다. 사용자는 작업, 제공자, 라이선스, 배포 옵션 또는 이름으로 필터링할 수 있습니다.

![Model catalog](../../../translated_images/ko/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- 의도된 사용법과 학습 데이터에 대한 자세한 설명, 코드 샘플 및 내부 평가 라이브러리의 평가 결과를 포함한 모델 카드를 검토할 수 있습니다.

![Model card](../../../translated_images/ko/ModelCard.598051692c6e400d.webp)

- [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) 패널을 통해 업계에서 사용할 수 있는 다양한 모델 및 데이터 세트의 벤치마크를 비교하여 비즈니스 시나리오에 가장 적합한 모델을 평가할 수 있습니다.

![Model benchmarks](../../../translated_images/ko/ModelBenchmarks.254cb20fbd06c03a.webp)

- Microsoft Foundry의 실험 및 추적 기능을 활용하여 특정 작업 부하에서 모델 성능을 향상시키기 위해 지원되는 모델을 맞춤 학습시킬 수 있습니다.

![Model fine-tuning](../../../translated_images/ko/FineTuning.aac48f07142e36fd.webp)

- 원래의 사전 학습된 모델 또는 미세 조정된 버전을 원격 실시간 추론 엔드포인트에 배포할 수 있습니다. 관리되는 컴퓨팅이나 서버리스 배포 옵션을 사용하여 애플리케이션에서 이를 활용할 수 있습니다.

![Model deployment](../../../translated_images/ko/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> 카탈로그의 모든 모델이 미세 조정 및/또는 종량제 배포를 위해 현재 사용 가능한 것은 아닙니다. 모델의 기능과 제한 사항에 대한 자세한 내용은 모델 카드를 확인하세요.

## LLM 결과 향상하기

우리 스타트업 팀은 여러 종류의 LLM과 Microsoft Foundry라는 클라우드 플랫폼을 탐색하여 다양한 모델을 비교 평가하고 테스트 데이터에서 성능을 높여 추론 엔드포인트에 배포할 수 있었습니다.

그러나 언제 사전 학습된 모델 대신 모델을 미세 조정해야 할까요? 특정 작업 부하에서 모델 성능을 향상시키기 위한 다른 방법은 무엇일까요?

비즈니스가 LLM에서 원하는 결과를 얻기 위해 사용할 수 있는 여러 가지 접근 방식이 있습니다. LLM을 프로덕션에 배포할 때 훈련 정도와 함께 다양한 유형의 모델을 선택할 수 있으며, 복잡성, 비용 및 품질 면에서 차이가 있습니다. 다음은 몇 가지 다른 접근법입니다:

- **컨텍스트를 활용한 프롬프트 엔지니어링**. 프롬프트할 때 충분한 컨텍스트를 제공하여 원하는 응답을 얻는 방법입니다.

- **검색 보강 생성, RAG**. 예를 들어 데이터가 데이터베이스나 웹 엔드포인트에 존재한다면, 프롬프트 시에 해당 데이터 또는 일부를 포함하기 위해 관련 데이터를 가져와 사용자의 프롬프트 일부로 만들 수 있습니다.

- **미세 조정된 모델**. 여기서는 자신의 데이터로 모델을 추가 학습시켜 모델이 필요에 더 정확하고 반응적으로 만드나 비용이 많이 들 수 있습니다.

![LLMs deployment](../../../translated_images/ko/Deploy.18b2d27412ec8c02.webp)

이미지 출처: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 컨텍스트를 활용한 프롬프트 엔지니어링

사전 학습된 LLM은 짧은 프롬프트(예: 완성할 문장이나 질문)로도 일반적인 자연어 작업에서 매우 잘 작동하는데, 이를 “제로샷” 학습이라고 합니다.

하지만 사용자가 상세한 요청과 예제를 포함한 컨텍스트를 제공할수록 답변이 더 정확하고 기대에 부합할 가능성이 높아집니다. 프롬프트에 하나의 예제만 포함될 경우 이를 “원샷” 학습, 여러 예제를 포함하면 “few-shot learning”이라고 부릅니다.
컨텍스트를 활용한 프롬프트 엔지니어링은 가장 비용 효율적인 시작 방법입니다.

### 검색 보강 생성 (Retrieval Augmented Generation, RAG)

LLM은 학습에 사용된 데이터만을 활용해 답변을 생성할 수 있는 제한이 있습니다. 이는 학습 후 발생한 사실에 대해 알지 못하며, 비공개 정보(예: 회사 데이터)에 접근할 수 없음을 의미합니다.
이 문제는 RAG로 극복할 수 있는데, RAG는 문서 단위 조각들 형태의 외부 데이터를 프롬프트에 보강하는 기술입니다. 이는 프롬프트 길이 제한을 고려하면서 이루어집니다. [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst) 같은 벡터 데이터베이스 도구가 유용한 조각들을 다양한 미리 정의된 데이터 소스에서 검색해 프롬프트 컨텍스트에 추가하는 방식을 지원합니다.

이 기술은 충분한 데이터, 시간 또는 리소스가 없지만 특정 작업 부하에서 성능을 개선하고 허위 또는 오래되거나 지원되지 않는 답변의 위험을 줄이고 싶은 비즈니스에 매우 유용합니다.

### 미세 조정된 모델

미세 조정은 전이 학습을 활용해 모델을 특정 다운스트림 작업이나 문제 해결에 ‘적응’시키는 과정입니다. 이는 few-shot learning과 RAG와 달리 새 모델이 생성되며 가중치와 편향이 업데이트됩니다. 프롬프트(입력)와 그에 대응하는 출력(완성) 쌍으로 구성된 훈련 예제 세트가 필요합니다.
이 방법은 다음 경우에 권장됩니다:

- **더 작은 작업 특화 모델 사용**. 비즈니스가 대형 첨단 모델에 반복적으로 프롬프트를 넣는 대신 좁은 작업에 대해 더 작은 모델을 미세 조정하여 비용 효율적이고 더 빠른 솔루션을 원할 때입니다.

- **지연시간 고려**. 특정 사용 사례에서 지연시간이 중요해 매우 긴 프롬프트를 사용하거나 모델이 학습해야 할 예제 수가 프롬프트 길이 제한에 맞지 않을 때입니다.

- **안정적인 동작 적응**. 비즈니스에 높은 품질의 예제가 많은 경우, 모델이 일관되게 작업 패턴, 출력 형식, 톤 또는 도메인 특화 스타일을 따르도록 할 때입니다. 신속하게 바뀌는 최신 사실이나 비공개 지식이 문제라면 미세 조정만 의존하지 말고 RAG 사용을 권장합니다.

### 학습된 모델

LLM을 처음부터 학습시키는 것은 의심할 여지없이 가장 어렵고 복잡한 방법으로, 막대한 양의 데이터, 숙련된 인력, 적절한 컴퓨팅 파워가 필요합니다. 이 옵션은 비즈니스가 도메인 특화된 사용 사례와 대량의 도메인 중심 데이터를 가진 경우에만 고려해야 합니다.

## 지식 확인

LLM 완성 결과를 향상시키기 위한 좋은 접근법은 무엇일까요?

1. 컨텍스트를 활용한 프롬프트 엔지니어링
1. RAG
1. 미세 조정된 모델

A: 이 세 가지 모두 도움이 될 수 있습니다. 빠른 개선을 위해 컨텍스트를 활용한 프롬프트 엔지니어링부터 시작하고, 모델에 최신 사실이나 비공개 비즈니스 데이터가 필요하면 RAG를 사용하세요. 충분한 고품질 예제가 있고 모델이 일관되게 작업, 형식, 톤 또는 도메인 패턴을 따라야 할 때 미세 조정을 선택하세요.

## 🚀 도전 과제

비즈니스를 위해 [RAG 사용 방법](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)을 더 읽어보세요.

## 잘 하셨습니다, 학습을 계속하세요

이 수업을 마친 후, [Generative AI Learning 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성형 AI 지식을 계속 향상시키세요!

3과로 이동하여 [생성형 AI를 책임감 있게 구축하는 방법](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->