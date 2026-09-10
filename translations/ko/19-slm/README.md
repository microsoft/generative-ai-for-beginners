# 생성 AI 초보자를 위한 소형 언어 모델 소개
생성 AI는 새로운 콘텐츠를 생성할 수 있는 시스템을 만드는 데 중점을 둔 인공 지능의 매혹적인 분야입니다. 이 콘텐츠는 텍스트와 이미지에서 음악, 심지어 전체 가상 환경에 이르기까지 다양합니다. 생성 AI의 가장 흥미로운 응용 분야 중 하나는 언어 모델 영역입니다.

## 소형 언어 모델이란 무엇인가?

소형 언어 모델(SLM)은 대형 언어 모델(LLM)의 축소 버전을 의미하며, LLM의 많은 아키텍처 원칙과 기술을 활용하면서도 계산적 요구가 크게 줄어든 모델입니다.

SLM은 인간과 유사한 텍스트를 생성하도록 설계된 언어 모델의 하위 집합입니다. GPT-4와 같은 대형 모델과 달리 SLM은 더 작고 효율적이어서 계산 자원이 제한된 애플리케이션에 이상적입니다. 크기가 작음에도 불구하고 다양한 작업을 수행할 수 있습니다. 일반적으로 SLM은 LLM을 압축하거나 증류하여 구축되며, 원래 모델의 기능과 언어 능력의 상당 부분을 유지하는 것을 목표로 합니다. 모델 크기 감소는 전체 복잡성을 줄여 메모리 사용과 계산 요구 측면에서 SLM을 더욱 효율적으로 만듭니다. 이러한 최적화에도 불구하고 SLM은 여전히 다양한 자연어 처리(NLP) 작업을 수행할 수 있습니다:

- 텍스트 생성: 일관되고 맥락에 적합한 문장 또는 단락 생성.
- 텍스트 완성: 주어진 프롬프트를 기반으로 문장 예측 및 완성.
- 번역: 텍스트를 한 언어에서 다른 언어로 변환.
- 요약: 긴 텍스트를 짧고 소화하기 쉬운 요약으로 압축.

다만 대형 모델과 비교했을 때 성능이나 이해 깊이에서 일부 트레이드오프가 있습니다.

## 소형 언어 모델은 어떻게 작동하는가?
SLM은 방대한 텍스트 데이터를 학습합니다. 학습 중에 언어의 패턴과 구조를 습득하여 문법적으로 정확하고 맥락에 맞는 텍스트를 생성할 수 있게 됩니다. 학습 과정은 다음과 같습니다:

- 데이터 수집: 다양한 소스의 대규모 텍스트 데이터 수집.
- 전처리: 학습에 적합하도록 데이터 정리 및 구성.
- 학습: 기계 학습 알고리즘을 사용해 모델이 텍스트를 이해하고 생성하는 방법 학습.
- 미세 조정: 특정 작업에서 성능을 향상시키기 위한 모델 조정.

SLM의 개발은 전체 LLM이 무거운 자원 요구로 인해 비현실적일 수 있는 모바일 장치나 엣지 컴퓨팅 플랫폼과 같은 자원 제한 환경에서 배포 가능한 모델에 대한 증가하는 필요와 부합합니다. SLM은 효율성에 중점을 두어 성능과 접근성 간 균형을 이루며 다양한 분야에서 광범위한 적용을 가능하게 합니다.

![slm](../../../translated_images/ko/slm.4058842744d0444a.webp)

## 학습 목표

이 수업에서는 SLM에 대한 지식을 소개하고 Microsoft Phi-3와 결합하여 텍스트 콘텐츠, 비전 및 MoE의 다양한 시나리오를 학습하고자 합니다.

수업이 끝나면 다음 질문에 답할 수 있어야 합니다:

- SLM이란 무엇인가?
- SLM과 LLM의 차이점은 무엇인가?
- Microsoft Phi-3/3.5 패밀리는 무엇인가?
- Microsoft Phi-3/3.5 패밀리로 어떻게 추론을 실행하는가?

준비되셨나요? 시작합시다.

## 대형 언어 모델(LLM)과 소형 언어 모델(SLM)의 차이점

LLM과 SLM 모두 확률적 기계 학습의 기본 원칙을 바탕으로 구축되며, 아키텍처 설계, 학습 방법론, 데이터 생성 프로세스, 모델 평가 기술에서 유사한 접근 방식을 따릅니다. 그러나 여러 주요 요소에서 두 모델 유형이 구별됩니다.

## 소형 언어 모델의 응용 분야

SLM은 다음과 같은 다양한 응용 분야를 가집니다:

- 챗봇: 고객 지원 및 대화형 사용자 상호작용 제공.
- 콘텐츠 생성: 아이디어 생성 또는 전체 기사 초안 작성 지원.
- 교육: 학생들의 글쓰기 과제 지원 또는 언어 학습 도움.
- 접근성: 텍스트 음성 변환 시스템과 같은 장애인용 도구 생성.

<strong>크기</strong>
  
LLM과 SLM의 주요 구분점은 모델 규모에 있습니다. ChatGPT(GPT-4)와 같은 LLM은 약 1.76조 개 매개변수를 포함하는 반면, 오픈 소스 SLM인 Mistral 7B는 약 70억 개로 훨씬 적은 매개변수를 가집니다. 이 격차는 주로 모델 아키텍처와 학습 과정의 차이 때문입니다. 예를 들어, ChatGPT는 인코더-디코더 프레임워크 내에서 자기 주의 메커니즘을 사용하지만, Mistral 7B는 디코더 전용 모델 내에서 보다 효율적인 슬라이딩 윈도우 주의를 사용합니다. 이 아키텍처 차이는 모델의 복잡성과 성능에 큰 영향을 미칩니다.

<strong>이해력</strong>

SLM은 특정 도메인 내에서 성능을 최적화하는 경향이 있어 매우 전문화되어 있지만, 여러 지식 분야에 걸쳐 광범위한 맥락 이해를 제공하는 능력은 제한될 수 있습니다. 반면, LLM은 더 포괄적인 수준에서 인간과 같은 지능을 시뮬레이트하는 것을 목표로 합니다. 광범위하고 다양한 데이터셋으로 학습되어 여러 분야에서 우수한 성능을 제공하며, 더 높은 범용성과 적응성을 가집니다. 따라서 LLM은 자연어 처리 및 프로그래밍과 같은 광범위한 후속 작업에 더 적합합니다.

<strong>컴퓨팅</strong>

LLM의 학습 및 배치는 대규모 GPU 클러스터를 포함한 막대한 컴퓨팅 인프라를 필요로 하는 자원 집약적 과정입니다. 예를 들어, ChatGPT와 같은 모델을 처음부터 학습하려면 수천 개의 GPU를 장기간 사용해야 할 수 있습니다. 반면, SLM은 매개변수 수가 적어 컴퓨팅 자원 측면에서 접근성이 더 좋습니다. Mistral 7B와 같은 모델은 적당한 GPU가 장착된 로컬 머신에서도 학습 및 실행할 수 있으나, 학습에는 여전히 여러 GPU에 걸쳐 몇 시간이 필요합니다.

<strong>편향</strong>

편향은 LLM에서 잘 알려진 문제이며, 주로 학습 데이터의 특성에서 비롯됩니다. 이러한 모델은 인터넷에서 수집된 원시, 공개 데이터를 사용하기 때문에 특정 집단이 과소대표되거나 오해될 수 있고, 잘못된 라벨링이 포함될 수 있으며, 방언, 지리적 차이, 문법 규칙에 영향을 받는 언어적 편향이 반영될 수 있습니다. 또한, LLM 아키텍처의 복잡성은 편향을 악화시킬 수 있으며, 세심한 미세 조정 없이는 이런 편향이 눈에 띄지 않을 수 있습니다. 한편, SLM은 보다 제한적이고 도메인 특정 데이터셋으로 학습되어 이러한 편향에 상대적으로 덜 민감하지만 완전히 예외는 아닙니다.

<strong>추론</strong>

SLM의 크기 축소는 추론 속도 측면에서 상당한 이점을 제공합니다. 광범위한 병렬 처리가 필요 없이 지역 하드웨어에서 효율적으로 결과를 생성할 수 있습니다. 반면, LLM은 크기와 복잡성 때문에 적절한 추론 시간을 달성하려면 상당한 병렬 계산 자원이 요구됩니다. 다수의 동시 사용자가 있을 경우 특히 배포 규모가 클 때 LLM의 응답 속도가 느려집니다.

요약하면, LLM과 SLM은 기계 학습의 기초는 공유하지만 모델 크기, 자원 요구량, 맥락 이해력, 편향에 대한 민감도, 추론 속도 측면에서 크게 다릅니다. 이 차이는 각각의 용도에 따른 적합성을 반영하며, LLM은 더 범용적이지만 자원 소모가 크고, SLM은 계산 요구가 적은 도메인 특화 효율성을 제공합니다.

***참고: 이 수업에서는 Microsoft Phi-3 / 3.5를 예로 SLM을 소개합니다.***

## Phi-3 / Phi-3.5 패밀리 소개

Phi-3 / 3.5 패밀리는 주로 텍스트, 비전, 에이전트(MoE) 응용 시나리오를 대상으로 합니다:

### Phi-3 / 3.5 Instruct

주로 텍스트 생성, 채팅 완성, 콘텐츠 정보 추출 등에 사용됩니다.

**Phi-3-mini**

38억 매개변수의 언어 모델로 Microsoft Foundry, Hugging Face, Ollama에서 사용할 수 있습니다. Phi-3 모델은 주요 벤치마크에서 동급 및 더 큰 언어 모델들을 크게 능가합니다(아래 벤치마크 수치 참고, 높을수록 우수). Phi-3-mini는 두 배 크기 모델들보다 뛰어나며, Phi-3-small 및 Phi-3-medium은 GPT-3.5를 포함한 더 큰 모델을 능가합니다.

**Phi-3-small & medium**

70억 매개변수만으로도 Phi-3-small은 다양한 언어, 추론, 코딩, 수학 벤치마크에서 GPT-3.5T를 능가합니다.

140억 매개변수의 Phi-3-medium은 이 추세를 이어가며 Gemini 1.0 Pro를 능가합니다.

**Phi-3.5-mini**

Phi-3-mini의 업그레이드 버전으로 생각할 수 있습니다. 매개변수는 동일하지만 다중 언어 지원 능력(아랍어, 중국어, 체코어, 덴마크어, 네덜란드어, 영어, 핀란드어, 프랑스어, 독일어, 히브리어, 헝가리어, 이탈리아어, 일본어, 한국어, 노르웨이어, 폴란드어, 포르투갈어, 러시아어, 스페인어, 스웨덴어, 태국어, 터키어, 우크라이나어 등 20개 이상 지원)을 개선하고 긴 문맥 지원을 강화했습니다.

38억 매개변수의 Phi-3.5-mini는 동급 언어 모델을 능가하고 두 배 크기 모델과 동등한 성능을 보입니다.

### Phi-3 / 3.5 Vision

Phi-3/3.5의 Instruct 모델은 Phi의 이해 능력으로 생각할 수 있으며, Vision은 Phi가 세계를 이해할 수 있도록 눈을 제공하는 역할입니다.


**Phi-3-Vision**

42억 매개변수의 Phi-3-vision은 일반 시각 추론 작업, OCR, 표 및 도표 이해 작업에서 Claude-3 Haiku 및 Gemini 1.0 Pro V 같은 더 큰 모델들을 능가합니다.


**Phi-3.5-Vision**

Phi-3-Vision의 업그레이드 버전으로, 다중 이미지 지원이 추가되었습니다. 이는 단순히 사진을 보는 것뿐 아니라 비디오도 볼 수 있는 시각 능력 향상으로 생각할 수 있습니다.

Phi-3.5-vision은 OCR, 테이블 및 차트 이해 작업에서 Claude-3.5 Sonnet 및 Gemini 1.5 Flash 등 더 큰 모델들을 능가하며, 일반 시각 지식 추론 작업에서는 동등한 성능을 냅니다. 다중 프레임 입력을 지원하여 여러 입력 이미지에 대한 추론이 가능합니다.


### Phi-3.5-MoE

<strong><em>전문가 혼합(MoE)</em></strong>는 동일한 계산 예산으로 모델이나 데이터셋 크기를 대폭 확장할 수 있도록 사전 학습 과정을 훨씬 덜 많은 계산으로 가능하게 합니다. 특히 MoE 모델은 밀집 모델에 비해 사전 학습 시에 동일한 품질을 훨씬 빠르게 달성할 수 있습니다.

Phi-3.5-MoE는 16x38억 매개변수 전문가 모듈로 구성됩니다. 66억 활성 매개변수만으로도 더 큰 모델과 유사한 수준의 추론, 언어 이해 및 수학 능력을 보여줍니다.

우리는 다양한 시나리오에 따라 Phi-3/3.5 패밀리 모델을 사용할 수 있습니다. LLM과 달리 Phi-3/3.5-mini 또는 Phi-3/3.5-Vision을 엣지 장치에 배포할 수 있습니다.


## Phi-3/3.5 패밀리 모델 사용법

Phi-3/3.5를 다양한 시나리오에 사용하기를 희망합니다. 다음으로는 각기 다른 시나리오를 기반으로 Phi-3/3.5를 사용하는 방법을 소개하겠습니다.

![phi3](../../../translated_images/ko/phi3.655208c3186ae381.webp)

### 클라우드 API를 통한 추론

**Microsoft Foundry 모델**

> **참고:** GitHub Models는 2026년 7월 말에 서비스가 종료됩니다. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)가 직접적인 대체 서비스입니다.

Microsoft Foundry 모델이 가장 직접적인 방법입니다. Foundry 모델 카탈로그를 통해 Phi-3/3.5-Instruct 모델에 빠르게 접근할 수 있습니다. Azure AI Inference SDK / OpenAI SDK와 결합하여 코드로 API에 접근해 Phi-3/3.5-Instruct 호출을 완료할 수 있습니다. 또한 Playground에서 다양한 효과를 테스트할 수도 있습니다.

- 데모: 중국어 시나리오에서 Phi-3-mini와 Phi-3.5-mini 효과 비교

![phi3](../../../translated_images/ko/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ko/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

비전 및 MoE 모델을 사용하려는 경우 Microsoft Foundry를 통해 호출을 완료할 수 있습니다. 관심 있다면 Phi-3 Cookbook을 읽어 Microsoft Foundry를 통한 Phi-3/3.5 Instruct, Vision, MoE 호출 방법을 학습하세요. [이 링크 클릭](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

클라우드 기반 Microsoft Foundry Models 카탈로그 외에도 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)을 사용해 관련 호출을 완료할 수 있습니다. NVIDIA NIM(NVIDIA Inference Microservices)은 클라우드, 데이터 센터, 워크스테이션 등 다양한 환경에서 AI 모델을 효율적으로 배포할 수 있도록 설계된 가속화된 추론 마이크로서비스 세트입니다.

NVIDIA NIM의 주요 특징은 다음과 같습니다:

- **배포 용이성:** NIM은 단일 명령어로 AI 모델 배포가 가능해 기존 워크플로우에 쉽게 통합할 수 있습니다.

- **최적화된 성능:** NVIDIA의 사전 최적화된 추론 엔진인 TensorRT와 TensorRT-LLM을 활용하여 낮은 지연 시간과 높은 처리량을 보장합니다.
- **확장성:** NIM은 Kubernetes의 자동 확장 기능을 지원하여 다양한 작업 부하를 효과적으로 처리할 수 있습니다.
- **보안 및 제어:** 조직은 자체 관리 인프라에서 NIM 마이크로서비스를 자체 호스팅하여 데이터와 애플리케이션에 대한 제어를 유지할 수 있습니다.
- **표준 API:** NIM은 업계 표준 API를 제공하여 챗봇, AI 어시스턴트 등 AI 애플리케이션을 쉽게 구축하고 통합할 수 있습니다.

NIM은 NVIDIA AI Enterprise의 일부로, AI 모델의 배포 및 운영을 단순화하여 NVIDIA GPU에서 효율적으로 실행되도록 합니다.

- 데모: NVIDIA NIM을 사용하여 Phi-3.5-Vision-API 호출하기 [[이 링크 클릭](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 로컬 실행하기
Phi-3 또는 GPT-3와 같은 언어 모델과 관련된 추론(inference)은 입력받은 데이터에 기반해 응답이나 예측을 생성하는 과정을 말합니다. Phi-3에 프롬프트나 질문을 제공하면, 훈련된 신경망을 사용해 훈련 데이터의 패턴과 관계를 분석하여 가장 가능성 높고 관련성 높은 응답을 추론합니다.

**Hugging Face Transformer**
Hugging Face Transformers는 자연어 처리(NLP) 및 기타 머신러닝 작업을 위해 설계된 강력한 라이브러리입니다. 주요 특징은 다음과 같습니다:

1. **사전 학습된 모델:** 텍스트 분류, 명명된 개체 인식, 질문 응답, 요약, 번역, 텍스트 생성 등 다양한 작업에 사용할 수 있는 수천 개의 사전 학습 모델을 제공합니다.

2. **프레임워크 호환성:** PyTorch, TensorFlow, JAX 등 여러 딥러닝 프레임워크를 지원하여 한 프레임워크에서 모델을 학습시키고 다른 프레임워크에서 사용할 수 있습니다.

3. **멀티모달 기능:** NLP 외에도 컴퓨터 비전(예: 이미지 분류, 객체 탐지) 및 오디오 처리(예: 음성 인식, 오디오 분류) 작업도 지원합니다.

4. **사용 용이성:** 모델을 쉽게 다운로드하고 미세 조정할 수 있는 API와 도구를 제공해 초보자와 전문가 모두 접근하기 쉽습니다.

5. **커뮤니티 및 자료:** 활발한 커뮤니티와 광범위한 문서, 튜토리얼, 가이드가 있어 사용자들이 시작하고 라이브러리를 최대한 활용할 수 있도록 돕습니다.
[공식 문서](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 또는 [GitHub 저장소](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)를 참조하세요.

이 방법이 가장 널리 사용되지만, GPU 가속이 필요합니다. 특히 Vision이나 MoE 같은 시나리오는 계산량이 많아 양자화하지 않으면 CPU에서 매우 느립니다.


- 데모: Transformer를 사용하여 Phi-3.5-Instruct 호출하기 [이 링크 클릭](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 데모: Transformer를 사용하여 Phi-3.5-Vision 호출하기 [이 링크 클릭](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 데모: Transformer를 사용하여 Phi-3.5-MoE 호출하기 [이 링크 클릭](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)는 대형 언어 모델(LLM)을 로컬 컴퓨터에서 쉽게 실행할 수 있게 설계된 플랫폼입니다. Llama 3.1, Phi 3, Mistral, Gemma 2 등 다양한 모델을 지원합니다. 모델 가중치, 구성, 데이터를 하나의 패키지로 묶어 사용자들이 자신만의 모델을 커스터마이징하고 생성하기 쉽게 만듭니다. macOS, Linux, Windows용으로 제공되며 클라우드 서비스에 의존하지 않고 LLM을 실험하거나 배포하고자 하는 사용자에게 적합한 도구입니다. Ollama는 가장 직접적인 방법으로, 다음 명령어만 실행하면 됩니다.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)은 Microsoft의 오프라인 온디바이스 런타임으로, Phi 같은 모델을 완전히 내 하드웨어에서 실행할 수 있습니다. Azure 구독, API 키, 네트워크 연결이 필요 없습니다. 사용 가능한 최적 실행 제공자(NPU, GPU, CPU)를 자동 선택하며 OpenAI 호환 엔드포인트를 노출해 기존의 `openai`/Azure AI Inference SDK 코드를 최소한의 변경으로 사용할 수 있습니다. 시작하려면 [Foundry Local 문서](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)를 참조하세요.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

또는 Python에서 직접 SDK를 사용할 수 있습니다:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**GenAI용 ONNX Runtime**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst)은 크로스 플랫폼 추론 및 학습 머신러닝 가속기입니다. ONNX Runtime for Generative AI (GENAI)는 다양한 플랫폼에서 생성 AI 모델을 효율적으로 실행할 수 있도록 지원하는 강력한 도구입니다.

## ONNX Runtime이란?
ONNX Runtime은 머신러닝 모델의 고성능 추론을 가능하게 하는 오픈소스 프로젝트입니다. 머신러닝 모델 표준 표현 형식인 Open Neural Network Exchange(ONNX) 포맷을 지원합니다. ONNX Runtime은 PyTorch, TensorFlow/Keras 등의 딥러닝 프레임워크 모델뿐만 아니라 scikit-learn, LightGBM, XGBoost 같은 고전적 머신러닝 라이브러리 모델도 지원합니다. 다양한 하드웨어, 드라이버, 운영체제와 호환되며, 그래프 최적화 및 변환과 함께 하드웨어 가속기를 활용해 최적의 성능을 제공합니다.

## 생성 AI란?
생성 AI는 텍스트, 이미지, 음악 등 새로운 콘텐츠를 생성할 수 있는 AI 시스템을 말합니다. 예로 GPT-3 같은 언어 모델, Stable Diffusion 같은 이미지 생성 모델이 있습니다. ONNX Runtime for GenAI 라이브러리는 ONNX 모델용 생성 AI 루프, 즉 ONNX Runtime 추론, 로짓 처리, 검색 및 샘플링, KV 캐시 관리를 제공합니다.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI는 생성 AI 모델 지원을 위해 ONNX Runtime의 기능을 확장합니다. 주요 기능은 다음과 같습니다:

- **광범위한 플랫폼 지원:** Windows, Linux, macOS, Android, iOS 등 다양한 플랫폼에서 작동합니다.
- **모델 지원:** LLaMA, GPT-Neo, BLOOM 등 인기 있는 많은 생성 AI 모델을 지원합니다.
- **성능 최적화:** NVIDIA GPU, AMD GPU 등 다양한 하드웨어 가속기 최적화를 포함합니다.
- **사용 용이성:** 최소 코드로 텍스트, 이미지 등 콘텐츠를 생성할 수 있도록 애플리케이션에 쉽게 통합할 수 있는 API를 제공합니다.
- 사용자는 고수준의 generate() 메서드를 호출하거나 모델을 반복 실행하여 한 번에 한 토큰씩 생성하며, 반복 중에 생성 매개변수를 선택적으로 업데이트할 수 있습니다.
- ONNX Runtime은 토큰 시퀀스 생성용 greedy/beam 서치와 TopP, TopK 샘플링을 지원하며, 반복 페널티 같은 내장 로짓 처리 기능도 제공합니다. 사용자 지정 채점 기능도 쉽게 추가할 수 있습니다.

## 시작하기
ONNX Runtime for GENAI를 시작하려면 다음 단계를 따르세요:

### ONNX Runtime 설치하기:
```Python
pip install onnxruntime
```
### 생성 AI 확장 설치하기:
```Python
pip install onnxruntime-genai
```

### 모델 실행: Python에서 간단한 예시:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### 데모: ONNX Runtime GenAI로 Phi-3.5-Vision 호출하기


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


<strong>기타</strong>

ONNX Runtime, Ollama, Foundry Local 참조 방법 외에도, 각 제조사가 제공하는 모델 참조 방법을 기반으로 정량적 모델 참조도 완성할 수 있습니다. 예를 들어 Apple Metal과 함께 Apple MLX 프레임워크, NPU가 탑재된 Qualcomm QNN, CPU/GPU용 Intel OpenVINO 등이 있습니다. 더 많은 내용을 원하시면 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)을 참고하세요.


## 더 알아보기

Phi-3/3.5 가족의 기초를 배웠지만, SLM에 대해 더 배우려면 추가 지식이 필요합니다. 답을 찾으려면 Phi-3 Cookbook을 참조하세요. 더 알아보고 싶다면 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)을 방문하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->