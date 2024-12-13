## 소개

오픈 소스 LLM의 세계는 흥미롭고 끊임없이 진화하고 있습니다. 이 강의는 오픈 소스 모델에 대한 심층적인 정보를 제공하는 것을 목표로 합니다. 독점 모델과 오픈 소스 모델을 비교하는 정보가 필요하다면 ["다양한 LLM 탐색 및 비교" 강의](../../../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)를 참조하세요. 이 강의에서는 모델의 미세 조정(fine-tuning)에 대한 내용도 다룰 예정이지만, 보다 자세한 설명은 ["LLM 미세 조정" 강의](../../../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst)를 참조하세요.

## 학습 목표

- 오픈 소스 모델에 대한 이해 증진
- 오픈 소스 모델을 사용할 때의 이점 이해
- Hugging Face와 Azure AI Studio에서 이용 가능한 오픈 모델 탐색

## 오픈 소스 모델이란 무엇인가?

오픈 소스 소프트웨어는 다양한 분야에서 기술의 발전에 중요한 역할을 해왔습니다. 오픈 소스 이니셔티브(OSI)는 소프트웨어가 오픈 소스로 분류되기 위한 [10가지 기준](https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)을 정의했습니다. 소스 코드는 OSI가 승인한 라이선스에 따라 공개되어야 합니다.

LLM의 개발은 소프트웨어 개발과 유사한 요소를 가지고 있지만, 그 과정은 정확히 동일하지 않습니다. 이는 LLM 맥락에서 오픈 소스의 정의에 대한 커뮤니티 내 많은 논의를 불러일으켰습니다. 모델이 전통적인 오픈 소스 정의에 부합하려면 다음 정보가 공개되어야 합니다:

- 모델을 학습시키는 데 사용된 데이터셋.
- 학습의 일환으로서의 전체 모델 가중치.
- 평가 코드.
- 미세 조정 코드.
- 전체 모델 가중치 및 학습 메트릭.

현재 이 기준을 충족하는 모델은 소수에 불과합니다. [Allen Institute for Artificial Intelligence (AllenAI)가 만든 OLMo 모델](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst)이 이 범주에 속하는 모델 중 하나입니다.

이 강좌에서는 앞으로 이러한 모델을 "오픈 모델"이라고 부르겠습니다. 이는 작성 시점에 위의 기준에 부합하지 않을 수 있기 때문입니다.

## 오픈 모델의 이점

**높은 맞춤화 가능성** - 오픈 모델은 상세한 훈련 정보를 공개하기 때문에 연구자와 개발자가 모델의 내부를 수정할 수 있습니다. 이를 통해 특정 작업이나 연구 분야에 맞춘 고도로 특수화된 모델을 생성할 수 있습니다. 예를 들어, 코드 생성, 수학 연산, 생물학 등이 있습니다.

**비용** - 이러한 모델을 사용하고 배포하는 데 드는 토큰당 비용은 독점 모델보다 낮습니다. 생성형 AI 애플리케이션을 구축할 때, 이러한 모델을 사용하는 경우 성능 대비 가격을 고려해야 합니다.

![모델 비용](../../images/model-price.png?WT.mc_id=academic-105485-koreyst)  
출처: Artificial Analysis

**유연성** - 오픈 모델을 사용하면 다양한 모델을 사용하거나 결합하여 유연하게 작업할 수 있습니다. 예를 들어, 사용자가 사용자 인터페이스에서 직접 사용되는 모델을 선택할 수 있는 [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)가 있습니다.

![모델 선택](../../images/choose-model.png?WT.mc_id=academic-105485-koreyst)

## 다양한 개방형 모델 탐구

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst)는 Meta에서 개발한 오픈 모델로, 채팅 기반 응용 프로그램에 최적화되어 있습니다. 이는 대화 및 인간 피드백을 대량으로 포함한 미세 조정 방법 덕분입니다. 이 방법을 통해 모델은 인간의 기대에 더 부합하는 결과를 생성하여 더 나은 사용자 경험을 제공합니다.

Llama의 미세 조정 버전의 예로는 일본어에 특화된 [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)와 기본 모델의 향상된 버전인 [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst) 등이 있습니다.

### 미스트랄 (Mistral)

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)는 높은 성능과 효율성에 중점을 둔 오픈 모델입니다. 이 모델은 전문가 모델 집합을 하나의 시스템으로 결합하는 Mixture-of-Experts 접근 방식을 사용합니다. 입력에 따라 특정 모델이 선택되어 사용되기 때문에, 계산이 더 효과적입니다. 즉, 각 모델이 자신이 전문화된 입력에만 대응하게 합니다.

미스트랄의 파인튜닝된 일부 버전 예시는 의학 분야에 중점을 둔 [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)과 수학적 계산을 수행하는 [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)이 있습니다.

### 팔콘

[팔콘](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst)은 기술 혁신 연구소(**TII**)에서 만든 대규모 언어 모델(LLM)입니다. 팔콘-40B는 400억 개의 매개변수로 훈련되었으며, 적은 계산 예산으로도 GPT-3보다 더 나은 성능을 발휘하는 것으로 나타났습니다. 이는 FlashAttention 알고리즘과 다중 쿼리 어텐션을 사용하여 추론 시 메모리 요구 사항을 줄일 수 있기 때문입니다. 추론 시간이 감소함에 따라, 팔콘-40B는 채팅 애플리케이션에 적합합니다.

팔콘의 미세 조정된 버전의 예로는 오픈 모델을 기반으로 구축된 [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)와 기본 모델보다 높은 성능을 제공하는 [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)이 있습니다.

## 선택하는 방법

오픈 모델을 선택하는 데 정답은 없습니다. 시작하기 좋은 곳은 Azure AI Studio의 작업별 필터 기능을 사용하는 것입니다. 이를 통해 모델이 어떤 유형의 작업을 위해 훈련되었는지 이해할 수 있습니다. 또한, Hugging Face는 특정 지표에 기반하여 최고의 성능을 보이는 모델을 보여주는 LLM 리더보드를 관리하고 있습니다.

LLM을 여러 유형별로 비교할 때, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst)도 또 다른 훌륭한 자원입니다:

![모델 품질](../../images/model-quality.png?WT.mc_id=academic-105485-koreyst)
출처: Artificial Analysis

특정 용도에 대한 작업을 진행할 때, 동일한 영역에 집중하여 미세 조정된 버전을 찾는 것이 효과적일 수 있습니다. 다양한 오픈 모델을 실험하여 자신과 사용자 기대에 부합하는지 확인하는 것도 좋은 방법입니다.

## 다음 단계

오픈 모델의 가장 큰 장점은 빠르게 시작할 수 있다는 점입니다. [Azure AI Studio 모델 카탈로그](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)를 확인해보세요. 여기에는 우리가 논의한 특정 Hugging Face 컬렉션을 포함한 모델들이 소개되어 있습니다.

## 학습은 여기서 멈추지 않습니다, 여정을 계속하세요

이 강의를 완료한 후, 우리의 [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하고 생성형 AI 지식을 계속 향상시키세요!
