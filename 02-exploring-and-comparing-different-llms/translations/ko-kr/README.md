# 다양한 대형 언어 모델 탐색 및 비교

[![다양한 대형 언어 모델 탐색 및 비교](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/J1mWzw0P74c?WT.mc_id=academic-105485-koreyst)

> *위의 이미지를 클릭하여 이 수업의 비디오를 시청하세요.*

이전 시간에는 생성형 AI가 기술 환경을 어떻게 변화시키고 있는지, 대규모 언어 모델(LLM)이 어떻게 작동하는지, 우리 스타트업과 같은 기업이 어떻게 이를 사용 사례(use-case)에 적용하고 성장할 수 있는지 살펴보았습니다! 이번 장에서는 다양한 유형의 대규모 언어 모델인 LLM을 비교하고 대조하며 장단점을 알아보고자 합니다.

우리 스타트업 과정에서의 다음 단계는 오늘날의 대규모 언어 모델(LLM) 경향을 어떤 모델이 우리의 사용 사례에 적합한지 살표보는 것입니다.  

## 소개

이 수업에서는 다음 내용을 다룰 것입니다:

- 현재 대형 언어 모델(LLMs)의 다양한 유형.
- Azure에서 사용 사례에 대한 다른 모델을 테스트하고 반복적으로 비교하는 방법.
- 대형 언어 모델(LLM)을 배포하는 방법.

## 학습 목표

이 수업을 마치면 다음을 할 수 있게 될것 입니다:

- 사용 사례에 적합한 모델 선택.
- 어떻게 모델의 성능을 개선시키고, 어떻게 반복하며, 어떻게 테스트하는지.
- 기업이 모델을 배포하는 방법을 이해합니다.

## 다양한 종류의 LLMs 이해하기

대형 언어 모델(Large Language Models, LLMs)은 아키텍처, 훈련 데이터 및 사용 사례에 따라 여러 가지 범주로 나눌 수 있습니다. 이러한 차이점을 이해하면 우리 스타트업이 시나리오에 적합한 모델을 선택하고 테스트, 반복 및 성능을 개선하는 방법을 이해할 수 있게 될 것입니다.

다양한 종류에 LLM 모델이 있는데, 사용 목적, 데이터, 예산 등에 따라 모델을 선택할 수 있습니다.

텍스트, 오디오, 비디오, 이미지 생성 등 모델을 사용하려는 목적에 따라 다른 종류의 모델을 선택할 수 있습니다.

- **오디오 및 음성 인식**. 이러한 용도로는 음성 인식을 목적으로 하는 범용 모델인 위스퍼 유형이 적합합니다. 다양한 오디오에 대해 훈련되어 다국어 음성 인식을 수행할 수 있습니다. [여기에서 위스퍼형 모델에 대해 자세히 알아보기](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **이미지 생성**. 이미지 생성의 경우, DALL-E와 Midjourney가 잘 알려진 두 가지 선택지입니다. DALL-E는 Azure OpenAI에서 제공합니다. [여기에서 DALL-E에 대해 자세히 알아보세요](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) 그리고 이 커리큘럼의 9장도 참조하세요.

- **텍스트 생성**. 대부분의 모델은 텍스트 생성을 위해 훈련되며, GPT-3.5부터 GPT-4까지 다양한 선택 사항이 있습니다.  비용도 제각각이며 GPT-4가 가장 비쌉니다. 기능 및 비용 측면에서 여러분의 요구 사항에 가장 적합한 모델을 확인하려면 [Azure Open AI 플레이그라운드](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst)를 살펴보는 것이 좋습니다.

모델을 선택하면 몇 가지 기본 기능을 사용할 수 있지만 이것만으로는 충분하지 않을 수 있습니다. 가끔 회사별로 특정 데이터를 LLM에게 알려줘야 할 수도 있습니다. 그러한 경우에 접근하는 방법으로는 몇 가지가 있으며, 다음 섹션에서 자세히 설명해보겠습니다.

### Foundation Models 대 LLMs

Foundation Model이라는 용어는 [스탠포드 연구자들에 의해 만들어진 것](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst)이으로, 다음과 같은 몇 가지 기준을 따르는 AI 모델로 정의됩니다:

- **비감독 학습(unsupervised learning) 또는 자가 지도 학습(self-supervised learning)을 사용하여 훈련됩니다.** 이는 레이블이 지정되지 않은 다중 모드 데이터에 대해 학습되고, 학습 과정에서 사람의 주석이나 데이터 레이블 지정이 필요하지 않다는 것을 의미합니다.
- **매우 큰 모델입니다.** 수십억 개의 매개변수로 훈련된 매우 깊은 신경망(deep neural networks)을 기반으로 합니다.
- **일반적으로 다른 모델의 '기반(foundation)' 역할을 합니다.** 미세 조정을 통해 다른 모델을 구축할 수 있는 출발점으로 사용할 수 있습니다.

![Foundation Models 대 LLMs](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

이미지 출처: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

이 차이를 더 명확하게 설명하기 위해 ChatGPT를 예로 들어보겠습니다. ChatGPT의 첫 번째 버전을 구축하기 위해 GPT-3.5라는 모델이 기반 모델로 사용되었습니다. 이것은 OpenAI가 채팅과 관련된 특정 데이터를 사용하여 GPT-3.5의 튜닝된 버전을 생성했다는 것을 의미합니다. 이 튜닝된 버전은 대화 시나리오에서 잘 작동하는 것을 목표로 하였으며, 이를 통해 챗봇과 같은 대화형 상황에서 우수한 성능을 발휘하도록 특화되었습니다.

![Foundation Model](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

이미지 출처: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### 오픈 소스 모델과 독점 모델의 차이

LLM을 분류하는 또 다른 방법은 오픈 소스인지 독점 모델인지 여부입니다.

오픈 소스 모델은 대중에게 공개되어 누구나 사용할 수 있는 모델입니다. 이러한 모델은 모델을 만든 회사나 연구 커뮤니티에서 제공하는 경우가 많습니다.

오픈 소스 모델은 대중에게 공개되어 누구든지 사용할 수 있는 모델입니다. 보통 모델을 만든 회사나 연구 커뮤니티에서 제공하는 경우가 많습니다. 이러한 모델은 LLM의 다양한 사용 사례에 맞게 검수, 수정 및 맞춤화가 가능합니다. 그러나 이러한 모델이 항상 프로덕션용으로 최적화된 것은 아니며 독점 모델만큼 성능이 뛰어나지 않을 수 있습니다. 더불어 오픈 소스 모델에 대한 자금 지원이 제한적일 수 있으므로 장기적으로 유지 관리되지 않거나 최신 연구 성과물로 업데이트되지 않을 수 있습니다. 인기 있는 오픈 소스 모델의 예로는 [알파카(Alpaca)](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [블룸(bloom)](https://sapling.ai/llm/bloom?WT.mc_id=academic-105485-koreyst), [라마(LLaMa)](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst) 등이 있습니다.

독점 모델은 기업이 소유하고 대중에게 공개하지 않는 모델입니다. 종종 이러한 모델은 프로덕션용으로 최적화되어 있습니다. 그러나 이러한 모델은 다른 사용 사례에 맞게 검수, 수정 또는 맞춤형 설정이 제한됩니다. 또한 항상 무료로 제공되는 것은 아니며, 사용하려면 구독 또는 결제가 필요할 수 있습니다.
또한 사용자는 모델을 훈련하는데 사용되는 데이터에 대한 제어권이 없으므로, 데이터 개인 정보 보호 및 AI 사용의 책임을 모델 소유자에게 의존해야 합니다. 인기 있는 독점 모델의 예로는 [OpenAI models](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) 또는 [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst) 등이 있습니다.

### 임베딩, 이미지 생성, 텍스트 및 코드 생성 비교

LLMs는 생성하는 결과에 따라 다양한 범주로 나눌 수 있습니다.

임베딩(Embedding; 이하 임베딩)은 텍스트를 수치적 형태, 즉 임베딩이라고 불리는 입력 텍스트의 수치적 표현으로 변환할 수 있는 일련의 모델들입니다. 임베딩을 사용하면 기계가 단어나 문장 간의 관계를 더 쉽게 이해할 수 있으며, 분류 모델이나 수치 데이터에서 더 나은 성능을 보이는 군집화(clustering) 모델과 같은 다른 모델들에 입력으로 사용될 수 있습니다. 임베딩 모델은 종종 전이 학습(transfer learning)에 사용되는데, 이는 대량의 데이터가 있는 대리 작업(surrogate task)을 위해 모델이 구축되고, 그 후 모델 가중치(임베딩)가 다른 하위 작업에 재사용되는 방식입니다. 이러한 유형의 예로는 [OpenAI 임베딩](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst)이 있습니다.

![Embedding](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

이미지 생성 모델은 이미지를 생성하는 모델입니다. 이러한 모델들은 이미지 편집, 이미지 합성 및 이미지 변환에 자주 사용됩니다. 이미지 생성 모델은 [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst)와 같은 대규모 이미지 데이터셋을 기반으로 학습되며, 새로운 이미지를 생성하거나 인페인팅(inpainting), 초고해상도(super-resolution), 색상화(colorization) 기술을 사용하여 기존 이미지를 편집하는 데 사용될 수 있습니다. 예시로는 [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst)와 [Stable Diffusion 모델](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) 등이 있습니다.

![Image generation](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

텍스트 및 코드 생성 모델은 텍스트나 코드를 생성하는 모델입니다. 이러한 모델들은 텍스트 요약, 번역, 질문 응답 등에 자주 사용됩니다. 텍스트 생성 모델은 [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst)와 같은 대규모 텍스트 데이터셋을 기반으로 학습되며, 새로운 텍스트를 생성하거나 질문에 답하는 데 사용될 수 있습니다. 코드 생성 모델, 예를 들어 [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst)은 GitHub와 같은 대규모 코드 데이터셋을 기반으로 학습되며, 새로운 코드를 생성하거나 기존 코드의 버그를 수정하는 데 사용될 수 있습니다.

![Text and code generation](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### 인코더-디코더 vs 디코더 전용

LLM의 다양한 유형의 아키텍처에 대해 이야기를 하기 위해 비유를 해볼게요.

학생들을 위한 퀴즈를 내는 임무를 맡았다고 상상해봅시다. 두 명의 동료가 있으며, 한 명은 내용 생성을, 다른 한 명을 내용 검토를 담당합니다.

내용 생성자(작성자)는 디코더 전용 모델과 같습니다. 주제를 보고 이미 작성한 내용을 참고해서 이를 기반으로 코스를 작성하게 됩니다. 매력적이고 유익한 내용을 작성하는데 능숙하지만, 주제와 학습 목표를 이해하는 데는 그다지 능숙하지 않습니다. 디코더 전용 모델의 예로는 GPT-3와 같은 GPT 계열 모델이 있습니다.

검토자는 인코더 전용 모델과 같습니다. 작성된 코스와 답변을 보고 그들 사이의 관계를 파악하고 맥락을 이해하지만, 내용을 생성하는 데는 능숙하지 않습니다. 인코더 전용 모델의 예로는 BERT와 같은 모델이 있습니다.

퀴즈를 만들고 검토할 수 있는 사람이 있다고 상상해 보세요. 이것이 인코더-디코더 모델입니다. 예로는 BART와 T5가 있습니다.

### 서비스 vs 모델

자, 이제 서비스와 모델의 차이점에 대해 이야기해 보겠습니다. 서비스는 클라우드 서비스 공급업체가 제공하는 상품으로, 모델, 데이터 및 기타 구성 요소의 조합으로 이루어진 경우가 많습니다. 모델은 서비스의 핵심 구성 요소이며, 종종 LLM과 같은 기반 모델(foundation model)입니다.

서비스는 종종 프로덕션 용도로 최적화되어 있으며, 그래픽 사용자 인터페이스를 통해 모델을 직접 사용하는 것보다 쉽습니다. 그러나 서비스는 항상 무료로 제공되는 것은 아니며, 서비스 제공자의 장비와 리소스를 활용하고 비용을 최적화하며 쉽게 확장할 수 있는 대신 구독 또는 지불을 해야 사용할 수 있습니다. 예를 들어 종량제 요금제를 제공하는 [Azure OpenAI 서비스](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst)는 사용자가 서비스를 사용한 양에 비례하여 요금이 부과됩니다. 또한 Azure OpenAI 서비스는 모델의 기능 위에 엔터프라이즈급 보안 및 신뢰할 수 있는 AI 프레임워크를 제공합니다.

모델은 매개변수, 가중치 등이 포함된 신경망에 불과합니다. 그러나 기업이 로컬에서 실행하려면 장비를 구입하고, 확장할 수 있는 구조를 구축하고, 라이선스를 구매하거나 오픈 소스 모델을 사용해야 합니다. LLaMA와 같은 모델을 사용할 수 있지만, 모델을 실행하기 위한 컴퓨팅 성능이 필요하죠.

## Azure에서 다양한 모델을 테스트하고 성능을 이해하기 위해 반복하는 방법

우리 팀이 현재 LLM 환경을 탐색하고

팀이 현재 LLM 현황을 살펴보고 시나리오에 적합한 몇 가지 후보를 파악했다면, 다음 단계는 자신의 데이터와 워크로드에 대해 테스트하는 것입니다. 이 과정은 실험과 측정을 통해 반복적으로 수행됩니다.
이전 단락에서 언급한 대부분의 모델(OpenAI 모델, Llama2와 같은 오픈 소스 모델, Hugging Face 트랜스포머)은 [Azure 머신 러닝 스튜디오](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst)의 [기초 모델](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) 카탈로그에서 사용할 수 있습니다.

[Auure 머신 러닝](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst)은 데이터 과학자와 머신 러닝 엔지니어가 단일 플랫폼에서 전체 머신 러닝 수명 주기(학습, 테스트, 배포 및 MLOps 처리)를 관리할 수 있도록 설계된 클라우드 서비스입니다. 머신 러닝 스튜디오는 이 서비스에 대한 그래픽 사용자 인터페이스를 제공하며, 사용자는 이를 통해 다음과 같은 작업을 수행할 수 있습니다:

- 카탈로그에서 관심 있는 기반 모델(Foundation Model)을 찾고, 작업, 라이센스 또는 이름별로 필터링합니다. 카탈로그에 아직 포함되지 않은 새로운 모델을 가져올 수도 있습니다.
- 모델 카드를 검토하여 자세한 설명 및 코드 샘플을 확인하고, 샘플 추론 위젯을 사용하여 샘플 프롬프트를 제공하고 결과를 테스트할 수 있습니다.

![Model card](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- 특정 워크로드와 입력된 데이터 세트에 대한 객관적 평가 지표(metric)를 사용하여 모델 성능을 평가합니다.

![Model evaluation](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Azure 머신 러닝의 실험 및 추적 기능을 활용하여 특정 워크로드에서 모델의 성능을 개선하기 위해 맞춤형 훈련 데이터로 모델을 미세 조정(Fine-tune)합니다.

![Model fine-tuning](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- 사전 학습(pre-trained)된 원본 모델 또는 미세 조정(find-tuned)된 버전을 원격 실시간 추론(remote real time inference) 또는 배치 엔드포인트(batch endpoint)에 배포하여 애플리케이션이 이를 사용할 수 있도록 합니다.

![Model deployment](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## LLM 결과 개선하기

스타트업 팀과 함께 다양한 종류의 LLM과 클라우드 플랫폼(Azure 머신 러닝)을 통해 여러 모델을 비교하고, 테스트 데이터에서 평가하며, 성능을 개선하고 추론 엔드포인트에 배포할 수 있는 방법을 살펴봤습니다.

하지만 언제 사전 학습된 모델을 사용하기보다 모델을 미세 조정해야 할까요? 특정 워크로드에서 모델 성능을 개선하기 위한 다른 접근 방식이 있을까요?

기업이 LLM에서 필요한 결과를 얻기 위해 사용할 수 있는 몇 가지 접근 방식이 있으며, 다양한 학습 정도를 가진 다양한 유형의 모델을 선택할 수 있습니다.

복잡성, 비용 및 품질 수준이 다른 유형의 모델을 프로덕션 환경에 배포하는 방법은 다음과 같습니다:

- **컨텍스트가 포함된 프롬프트 엔지니어링**. 프롬프트에 충분한 컨텍스트를 제공하여 필요한 응답을 얻을 수 있도록 하는 아이디어입니다.

- **검색 증강 생성(Retrieval Augmented Generation), RAG**. 데이터가 데이터베이스나 웹 엔드포인트에 존재할 수 있으며, 프롬프트 시 이 데이터 또는 그 일부를 포함시키기 위해 관련 데이터를 가져와 사용자의 프롬프트의 일부로 만드는 것입니다.

- **미세 조정된 모델**. 자체 데이터로 모델을 추가로 학습시키면 모델이 더 정확하고 필요에 맞게 반응할 수 있지만 비용이 많이 들 수 있습니다.

![LLMs deployment](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Img source: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### 컨텍스트가 포함된 프롬프트 엔지니어링

사전 학습된 LLM은 일반화된 자연어 작업에서 매우 잘 작동하며, 문장 완성이나 질문 같은 짧은 프롬프트로도 호출할 수도 있습니다. 이를 "제로샷(zero-shot)" 러닝이라고 합니다.

그러나 사용자가 자신의 질문을 상세한 요청과 예시 - 즉 컨텍스트 - 로 구체화할수록, 답변은 사용자의 기대에 더 정확하고 가까워집니다. 이 경우, 프롬프트에 예시가 하나만 포함되어 있으면 "원샷(one-shot)" 러닝, 여러 예시가 포함되어 있으면 "퓨샷(few-shot)" 러닝이라고 합니다.

컨텍스트가 포함된 프롬프트 엔지니어링은 시작하기에 가장 비용 효율적인 접근법입니다.

### 검색 증강 생성(Retrieval Augmented Generation), RAG

LLM은 훈련 과정에서 사용된 데이터만을 이용하여 답변을 생성할 수 있는 한계를 가지고 있습니다. 훈련 과정 이후에 발생한 사실에 대해 알지 못하며, 비공개 정보(예: 회사 데이터)에 접근할 수 없습니다.
이 문제는 RAG, 즉 외부 데이터를 문서 조각(chunk) 형태로 프롬프트에 추가하는 기술을 통해 극복할 수 있습니다. 이는 프롬프트 길이 제한을 고려하여 다양한 사전 정의된 데이터 소스에서 유용한 조각들을 검색하여 프롬프트 컨텍스트에 추가하는 벡터 데이터베이스 도구(예: [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst))를 통해 지원됩니다.

이 기술은 기업이 LLM을 미세 조정할 충분한 데이터, 시간, 자원이 충분하지 않지만, 특정 워크로드의 성능을 개선하고 현실의 오해나 유해한 내용에 대한 위험을 줄이고자 할 때 매우 유용합니다.

### 미세 조정된 모델

미세 조정은 전이 학습을 활용하여 모델을 하위 작업(다운스크림 작업)에 '적응'시키거나 특정 문제를 해결하는 프로세스입니다. 퓨샷 러닝이나 RAG와 달리, 미세 조정은 업데이트된 가중치와 편향을 가진 새로운 모델을 생성하는 결과를 가져옵니다. 이는 단일 입력(프롬프트)과 관련 출력(완성; completion)으로 구성된 일련의 학습 예제 세트가 필요합니다.
미세 조정 방식이 선호되는 경우는 다음과 같습니다:

- **미세 조정된 모델 사용**. 기업에서 고성능 모델 대신 임베딩 모델처럼 성능이 덜 좋은 모델을 사용하고자 할 때, 미세 조정하여 비용 효율적이고 빠른 솔루션을 사용할 수 있습니다.

- **지연 시간 고려**. 특정 사용 사례에서 지연 시간이 중요하므로, 매우 긴 프롬프트를 사용하거나 모델에게 학습시켜야 할 예시의 수가 프롬프트 길이 제한에 맞지 않는 경우가 있습니다.

- **최신 상태 유지**. 기업에서 많은 고품질 데이터와 정확한 레이블을 가지고 있으며, 시간이 지나도 이 데이터를 최신 상태로 유지하는 데 필요한 자원을 보유하고 있는 경우.

### 훈련된 모델

LLM을 처음부터 훈련시키는 것은 의심할 여지 없이 가장 어렵고 복잡한 접근 방법이며, 방대한 양의 데이터와 숙련된 인력, 충분한 컴퓨팅 컴퓨팅 파워가 필요합니다. 이 옵션은 기업의 도메인별 사용 사례와 막대한 양의 도메인 데이터가 있는 상황에서만 고려해야 합니다.

## Knowledge check

LLM 완료(completion) 결과를 개선하기 위한 좋은 접근 방식은 무엇일까요?

1. 컨텍스트가 있는 신속한 엔지니어링
2. RAG
3. 미세 조정된 모델

A: 3, 시간과 리소스가 충분하고 고품질의 데이터가 있다면 최신 상태를 유지하기 위해 미세 조정이 더 나은 옵션입니다. 그러나 시간이 부족하고 개선을 원한다면 RAG을 고려하는 것이 좋습니다.

## 🚀 도전해보기

비즈니스에 RAG을 어떻게 사용할 수 있는지에 대해 더 알아보세요. [RAG 사용 방법](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst)을 읽어보세요.

## 훌륭해요, 학습을 계속해보세요

이 강좌를 완료한 후, 생성형 AI 지식을 더 향상시키기 위해 [생성형 AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하세요!

Lesson 3으로 이동하여 [생성형 AI를 책임 있게 사용하는 방법](../../../03-using-generative-ai-responsibly/translations/ko-kr/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!  
