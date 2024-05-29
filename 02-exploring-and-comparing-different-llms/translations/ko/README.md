# 다양한 LLM 탐색과 비교

[![Exploring and comparing different LLMs](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/J1mWzw0P74c?WT.mc_id=academic-105485-koreyst)

> *위의 이미지를 클릭하여 이 레슨의 비디오를 시청하세요.*

이전 레슨에서 우리는 생성형 AI가 기술적인 환경을 변화시키고, 대형 언어 모델 (LLM)이 어떻게 작동하는지, 그리고 우리 스타트업과 같은 비즈니스가 그들을 사용하여 사용 사례를 적용하고 성장할 수 있는지를 보았습니다. 이 장에서는 다른 유형의 대형 언어 모델인 LLM을 비교하고 대조하여 그들의 장단점을 이해하기 위해 탐색할 것입니다.

우리 스타트업의 여정에서 다음 단계는 현재의 대형 언어 모델 (LLM) 환경을 탐색하고 우리의 사용 사례에 적합한 모델을 이해하는 것입니다.

## 소개

이 레슨에서는 다음을 다룰 것입니다:

- 현재 풍경에서 다양한 유형의 LLM.
- Azure에서 사용 사례에 대한 다른 모델을 테스트, 반복 및 비교하는 방법.
- LLM을 배포하는 방법.

## 학습 목표

이 레슨을 마치면 다음을 할 수 있게 될 것입니다:

- 사용 사례에 적합한 적절한 모델 선택.
- 모델의 테스트, 반복 및 성능 개선 방법 이해.
- 비즈니스가 모델을 배포하는 방법 알기.

## 다양한 유형의 LLM 이해하기

대형 언어 모델 (LLM)은 아키텍처, 훈련 데이터 및 사용 사례에 따라 여러 가지 범주로 나뉠 수 있습니다. 이러한 차이점을 이해하면 우리 스타트업이 시나리오에 맞는 올바른 모델을 선택하고 성능을 테스트, 반복 및 개선하는 방법을 이해할 수 있습니다.

LLM 모델에는 텍스트, 오디오, 비디오, 이미지 생성 등을 위한 다양한 유형이 있습니다. 모델 선택은 사용 목적, 데이터, 비용 등에 따라 달라집니다.

- **오디오 및 음성 인식**. 이를 위해 Whisper 유형의 모델은 음성 인식을 위해 훌륭한 선택입니다. 일반적인 용도로 사용되며, 다양한 오디오로 훈련되어 다국어 음성 인식을 수행할 수 있습니다. [여기에서 Whisper 유형 모델에 대해 자세히 알아보세요](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **이미지 생성**. 이미지 생성을 위해 DALL-E와 Midjourney는 매우 잘 알려진 선택지입니다. DALL-E는 Azure OpenAI에서 제공됩니다. [DALL-E에 대해 더 알아보세요](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) 및 이 커리큘럼의 9장에서도 자세히 다룹니다.

- **텍스트 생성**. 대부분의 모델은 텍스트 생성을 위해 훈련되었으며, GPT-3.5에서 GPT-4까지 다양한 선택지가 있습니다. 각 모델은 다른 비용이 발생하며, GPT-4가 가장 비싸다는 점을 유념해야 합니다. 능력과 비용 측면에서 어떤 모델이 가장 적합한지 평가하기 위해 [Azure Open AI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst)을 살펴보는 것이 좋습니다.

모델을 선택하면 기본 기능을 얻을 수 있지만, 종종 회사별 데이터를 LLM에게 알려줘야 할 필요가 있습니다. 이에 대한 접근 방식에는 몇 가지 다른 선택지가 있으며, 이후 섹션에서 자세히 알아보겠습니다.

### Foundation Models VS LLMs

Foundation Model이라는 용어는 [스탠포드 연구원들에 의해 만들어졌으며](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst), 다음과 같은 기준을 따르는 AI 모델을 의미합니다:

- **비지도 학습 또는 자기 지도 학습을 사용하여 훈련됩니다**, 즉, 레이블이 없는 멀티 모달 데이터로 훈련되며, 훈련 과정에서 인간의 주석 또는 데이터 레이블링이 필요하지 않습니다.
- **매우 큰 모델**로, 수십억 개의 매개변수로 훈련된 매우 깊은 신경망을 기반으로 합니다.
- **일반적으로 다른 모델을 위한 '기반'으로 사용됩니다**, 즉, 다른 모델을 구축하기 위한 출발점으로 사용될 수 있으며, 이는 세밀한 조정을 통해 이루어질 수 있습니다.

![Foundation Models versus LLMs](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

이미지 출처: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

이 구분을 더 명확히 하기 위해 ChatGPT를 예로 들어보겠습니다. ChatGPT의 첫 번째 버전을 구축하기 위해 GPT-3.5라는 모델이 Foundation Model로 사용되었습니다. 이는 OpenAI가 일부 채팅 관련 데이터를 사용하여 GPT-3.5의 튜닝된 버전을 만들었으며, 이 모델은 채팅봇과 같은 대화 시나리오에서 잘 동작하는 것에 특화되었습니다.

![Foundation Model](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

이미지 출처: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 오픈 소스 VS 독점 모델 (Proprietary Models)

LLM을 분류하는 또 다른 방법은 오픈 소스인지 독점 모델인지에 따라 나눌 수 있습니다.

오픈 소스 모델은 일반에 공개되어 누구나 사용할 수 있는 모델입니다. 이러한 모델은 일반적으로 해당 모델을 개발한 회사나 연구 커뮤니티에 의해 제공됩니다. 이러한 모델은 검토, 수정 및 사용 사례에 맞게 사용자 정의할 수 있습니다. 그러나 이러한 모델은 항상 프로덕션 환경에 최적화되지 않을 수 있으며, 독점 모델만큼 성능이 우수하지 않을 수도 있습니다. 또한, 오픈 소스 모델의 자금 지원은 제한적일 수 있으며, 장기적으로 유지되지 않거나 최신 연구로 업데이트되지 않을 수도 있습니다. 대표적인 오픈 소스 모델로는 [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://sapling.ai/llm/bloom?WT.mc_id=academic-105485-koreyst) 및 [LLaMA](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst)이 있습니다.

독점 모델 (Proprietary models)은 회사에 소유되어 일반에 공개되지 않는 모델입니다. 이러한 모델은 일반적으로 프로덕션 환경에 최적화되어 있습니다. 그러나 이러한 모델은 사용자가 검토, 수정 또는 사용 사례에 맞게 사용자 정의할 수 없습니다. 또한, 이러한 모델은 항상 무료로 제공되지 않을 수 있으며, 사용을 위해 구독 또는 결제가 필요할 수 있습니다. 또한, 사용자는 모델을 훈련하는 데 사용되는 데이터를 제어할 수 없으므로 데이터 프라이버시와 AI의 책임있는 사용을 보장하기 위해 모델 소유자에게 의존해야 합니다. 대표적인 독점 모델로는 [OpenAI 모델](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) 및 [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst)가 있습니다.

### 임베딩 VS 이미지 생성 VS 텍스트 및 코드 생성

LLM은 생성하는 출력에 따라 다양한 범주로 분류될 수 있습니다.

임베딩은 텍스트를 숫자 형태로 변환하는 모델의 집합으로, 입력 텍스트의 수치적 표현인 임베딩을 생성합니다. 임베딩은 기계가 단어나 문장 간의 관계를 이해하기 쉽게 만들어주며, 분류 모델이나 클러스터링 모델과 같은 다른 모델의 입력으로 사용될 수 있습니다. 임베딩 모델은 전이 학습(transfer learning)에 자주 사용되며, 풍부한 데이터가 있는 대리 과제를 위해 모델이 구축되고, 그런 다음 모델 가중치(임베딩)가 다른 하위 작업에 재사용됩니다. 이 범주의 예로는 [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)가 있습니다.

![Embedding](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

이미지 생성 모델은 이미지를 생성하는 모델입니다. 이러한 모델은 이미지 편집, 이미지 합성 및 이미지 변환에 자주 사용됩니다. 이미지 생성 모델은 대규모 이미지 데이터셋(예: [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst))으로 훈련되며, 새로운 이미지를 생성하거나 인페인팅, 초해상도 및 색상화 기술을 사용하여 기존 이미지를 편집하는 데 사용될 수 있습니다. 예시로는 [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst)와 [Stable Diffusion 모델](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst)이 있습니다.

![이미지 생성](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

텍스트 및 코드 생성 모델은 텍스트나 코드를 생성하는 모델입니다. 이러한 모델은 텍스트 요약, 번역 및 질문에 대한 답변과 같은 작업에 자주 사용됩니다. 텍스트 생성 모델은 대규모 텍스트 데이터셋(예: [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst))으로 훈련되며, 새로운 텍스트를 생성하거나 질문에 답변하는 데 사용될 수 있습니다. 코드 생성 모델인 [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)과 같은 모델은 대규모 코드 데이터셋(예: GitHub)으로 훈련되며, 새로운 코드를 생성하거나 기존 코드의 버그를 수정하는 데 사용될 수 있습니다.

 ![Text and code generation](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### 인코더-디코더 (Encoder-Decoder) VS 디코더 전용 (Decoder-only)

LLM의 다양한 아키텍처에 대해 이야기하기 위해 비유를 사용해보겠습니다.

상사가 학생들을 위한 퀴즈 작성 과제를 주었습니다. 두 명의 동료가 있습니다. 한 명은 콘텐츠 작성을 담당하고 다른 한 명은 검토를 담당합니다.

콘텐츠 작성자는 디코더 전용 (Decoder-only) 모델과 비슷합니다. 그들은 주제를 살펴보고 이미 작성된 내용을 확인한 후에 그에 기반하여 코스를 작성할 수 있습니다. 그들은 매력적이고 유익한 콘텐츠 작성에 능숙하지만, 주제와 학습 목표를 이해하는 데는 그리 능숙하지 않습니다. GPT-3와 같은 GPT 계열 모델이 디코더 모델의 예입니다.

검토자는 인코더 전용 모델과 비슷합니다. 그들은 작성된 코스와 답변을 살펴보고 그들 사이의 관계를 인지하며 문맥을 이해하지만, 콘텐츠 생성에는 능숙하지 않습니다. 인코더 전용 모델의 예로는 BERT가 있습니다.

퀴즈를 작성하고 검토할 수 있는 사람이 있다고 상상해보세요. 이것이 인코더-디코더 (Encoder-Decoder) 모델입니다. BART와 T5가 그 예입니다.

### 서비스 VS 모델

이제 서비스와 모델의 차이에 대해 이야기해보겠습니다. 서비스는 클라우드 서비스 제공업체가 제공하는 제품으로, 종종 모델, 데이터 및 기타 구성 요소의 조합입니다. 모델은 서비스의 핵심 구성 요소이며, 종종 LLM과 같은 기반 모델입니다.

서비스는 종종 프로덕션 사용에 최적화되어 있으며, 그래픽 사용자 인터페이스를 통해 모델보다 쉽게 사용할 수 있습니다. 그러나 서비스는 항상 무료로 제공되지 않을 수 있으며, 서비스를 사용하기 위해 구독 또는 결제가 필요할 수 있습니다. 이는 서비스 소유자의 장비와 리소스를 활용하여 비용을 최적화하고 쉽게 확장할 수 있도록 하는 대가입니다. Azure OpenAI 서비스는 이러한 예로, 사용자는 서비스를 사용한 양에 비례하여 비용을 지불하는 pay-as-you-go 요금제를 제공합니다. 또한, Azure OpenAI 서비스는 모델의 기능에 더해 기업용 보안 및 책임 있는 AI 프레임워크를 제공합니다.

모델은 매개변수, 가중치 등을 포함한 신경망 자체입니다. 회사는 이러한 모델을 로컬에서 실행할 수 있지만, 장비를 구매하고 확장할 구조를 구축하고 라이선스를 구매하거나 오픈 소스 모델을 사용해야 합니다. LLaMA와 같은 모델은 계산 성능이 필요하며, 모델을 실행하기 위해 컴퓨팅 자원이 필요합니다.

## Azure에서 성능을 이해하기 위해 다른 모델로 테스트하고 반복하는 방법

팀은 현재 LLMs의 현황을 조사하고 시나리오에 적합한 몇 가지 좋은 후보 모델을 식별한 후, 다음 단계는 해당 데이터와 작업 부하에서 이들을 테스트하는 것입니다. 이는 실험과 측정을 통해 반복적으로 수행되는 과정입니다.
이전 단락에서 언급한 대부분의 모델들(OpenAI 모델, Llama2와 같은 오픈 소스 모델, Hugging Face transformers)은 [Azure Machine Learning studio](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst)의 [Foundation Models](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) 카탈로그에서 사용할 수 있습니다.

[Azure Machine Learning](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst)은 데이터 과학자와 ML 엔지니어를 위해 설계된 클라우드 서비스로, ML 수명주기 전체(학습, 테스트, 배포 및 MLOps 처리)를 단일 플랫폼에서 관리할 수 있도록 지원합니다. Machine Learning studio는 이 서비스에 대한 그래픽 사용자 인터페이스를 제공하며 사용자가 다음을 수행할 수 있도록 합니다:

- 카탈로그에서 관심 있는 Foundation Model을 태스크, 라이선스 또는 이름으로 필터링하여 찾을 수 있습니다. 카탈로그에 아직 포함되지 않은 새로운 모델을 가져올 수도 있습니다.
- 상세한 설명과 코드 샘플을 포함한 모델 카드를 검토하고, 샘플 프롬프트를 제공하여 결과를 테스트하는 샘플 추론 위젯을 사용하여 모델을 테스트할 수 있습니다.

![Model card](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- 특정 작업 부하와 입력으로 제공된 특정 데이터 세트에 대한 객관적인 평가 메트릭을 사용하여 모델 성능을 평가할 수 있습니다.

![Model evaluation](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Azure Machine Learning의 실험 및 추적 기능을 활용하여 특정 작업 부하에서 모델 성능을 개선하기 위해 사용자 지정 훈련 데이터로 모델을 세밀하게 조정할 수 있습니다.

![Model fine-tuning](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- 원래의 사전 훈련된 모델 또는 세밀하게 조정된 버전을 원격 실시간 추론 또는 배치 엔드포인트에 배포하여 응용 프로그램에서 사용할 수 있도록 할 수 있습니다.

![Model deployment](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## LLM 결과 개선하기

우리 스타트업 팀은 다양한 종류의 LLM과 Cloud Platform (Azure Machine Learning)을 탐색하여 다른 모델을 비교하고, 테스트 데이터로 평가하고, 성능을 개선하고, 추론 엔드포인트에 배포할 수 있는 기능을 활용했습니다.

그러나 언제 모델을 fine-tuning하여 사전 훈련된 모델 대신 사용해야 할까요? 특정 작업 부하에서 모델 성능을 개선하기 위한 다른 접근 방식이 있을까요?

비즈니스가 LLM에서 필요한 결과를 얻기 위해 사용할 수 있는 여러 가지 접근 방식이 있습니다. 다양한 수준의 훈련을 거친 다른 유형의 모델을 선택할 수 있으며, 복잡성, 비용 및 품질이 다른 LLM을 프로덕션에 배포할 수 있습니다. 다음은 몇 가지 다른 접근 방식입니다:

- **컨텍스트를 고려한 프롬프트 엔지니어링**. 프롬프트할 때 충분한 컨텍스트를 제공하여 필요한 응답을 얻을 수 있도록 하는 것입니다.

- **검색 증강 생성 (Retrieval Augmented Generation), RAG**. 데이터가 데이터베이스나 웹 엔드포인트에 존재할 수 있습니다. 프롬프트할 때 해당 데이터 또는 그 일부를 포함하도록하여 관련 데이터를 가져와 사용자의 프롬프트의 일부로 만들 수 있습니다.

- **파인튜닝 모델**. 여기서는 자체 데이터로 모델을 추가로 훈련시켜 모델이 더 정확하고 사용자의 요구에 더 잘 대응하지만 비용이 발생할 수 있습니다.

![LLMs deployment](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

이미지 출처: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 컨텍스트를 고려한 프롬프트 엔지니어링

사전 훈련된 LLM은 일반적인 자연어 작업에서 매우 잘 작동합니다. 짧은 프롬프트(문장을 완성하거나 질문하는 것과 같은)로도 호출하면 "제로샷" 학습이라고 할 수 있습니다.

그러나 사용자가 자세한 요청과 예제를 포함한 "컨텍스트"로 쿼리를 구성할수록 정확도가 높아지고 사용자의 기대에 가장 가까워집니다. 이 경우, 프롬프트에 하나의 예제만 포함되어 있다면 "원샷" 학습이라고 하며, 여러 개의 예제가 포함되어 있다면 "퓨샷" 학습이라고 합니다.
컨텍스트를 고려한 프롬프트 엔지니어링은 가장 비용 효율적인 접근 방식입니다.

### 검색 증강 생성 (Retrieval Augmented Generation, RAG)

LLM은 훈련 과정에서 사용된 데이터만을 사용하여 답변을 생성할 수 있는 제한이 있습니다. 이는 LLM이 훈련 과정 이후에 발생한 사실에 대해 알지 못하며, 회사 데이터와 같은 비공개 정보에 접근할 수 없다는 것을 의미합니다.
이러한 제한은 RAG를 통해 극복할 수 있습니다. RAG는 프롬프트를 외부 데이터로 확장하는 기술로, 문장 길이 제한을 고려하여 문서의 일부인 청크 형태로 외부 데이터를 프롬프트 컨텍스트에 추가합니다. 이는 벡터 데이터베이스 도구(예: [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst))에 의해 지원되며, 다양한 사전 정의된 데이터 소스에서 유용한 청크를 검색하여 프롬프트에 추가합니다.

이 기술은 비즈니스가 충분한 데이터, 충분한 시간 또는 리소스가 없어 LLM을 fine-tuning하는 것이 어려운 경우에 매우 유용합니다. 특정 작업 부하에서 성능을 개선하고 현실의 왜곡이나 유해한 콘텐츠의 위험을 줄이기 위해 사용됩니다.

### Fine-tuning된 모델

Fine-tuning은 전이 학습을 활용하여 모델을 '적응(adapt)'시켜 다운스트림 작업을 수행하거나 특정 문제를 해결하는 과정입니다. Few-shot learning과 RAG와는 달리, 가중치와 편향이 업데이트된 새로운 모델이 생성됩니다. 이는 다음 경우에 선호되는 접근 방식입니다:

- **Fine-tuned 모델 사용**. 비즈니스가 고성능 모델 대신 임베딩 모델과 같은 능력이 덜한 모델을 사용하고자 하는 경우로, 더 비용 효율적이고 빠른 솔루션을 얻을 수 있습니다.

- **지연 시간 고려**. 특정 사용 사례에서 지연 시간이 중요하므로 매우 긴 프롬프트를 사용할 수 없거나 모델에서 학습해야 할 예제 수가 프롬프트 길이 제한과 일치하지 않는 경우입니다.

- **최신 상태 유지**. 비즈니스가 많은 양의 고품질 데이터와 실제 레이블을 보유하고 있으며, 이러한 데이터를 시간이 지나도 최신 상태로 유지하기 위해 필요한 리소스를 갖추고 있는 경우입니다.

### 훈련된 모델

LLM을 처음부터 훈련하는 것은 의심할 여지없이 가장 어렵고 복잡한 접근 방식으로, 대량의 데이터, 숙련된 리소스 및 적절한 컴퓨팅 파워가 필요합니다. 이 옵션은 비즈니스가 도메인 특정 사용 사례와 대량의 도메인 중심 데이터를 보유한 경우에만 고려해야 합니다.

## 지식 확인

LLM 완성 결과를 개선하기 위한 좋은 접근 방식은 무엇일까요?

1. 컨텍스트를 고려한 프롬프트 엔지니어링
1. RAG
1. 파인튜닝된 모델

A:3, 시간과 리소스, 고품질 데이터가 있는 경우, 파인튜닝은 최신 상태를 유지하기 위한 더 나은 옵션입니다. 그러나 시간이 부족하고 개선을 고려하는 경우에는 RAG를 먼저 고려하는 것이 좋습니다.

## 🚀 도전과제

비즈니스에 [RAG를 사용하는 방법](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)에 대해 더 알아보세요.

## 수고하셨습니다. 학습을 계속하세요!

이 레슨을 완료한 후 [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 Generative AI 지식을 계속 향상시킬 수 있습니다!

Lesson 3로 이동하여 [책임감 있게 생성형 AI 사용하기 ](../../../03-using-generative-ai-responsibly/translations/ko/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!
