# 생성형 AI 초보자를 위한 소형 언어 모델 소개
생성형 AI는 새로운 콘텐츠를 생성할 수 있는 시스템을 만드는 데 중점을 둔 인공지능의 흥미로운 분야입니다. 이 콘텐츠는 텍스트와 이미지, 음악, 심지어 전체 가상 환경까지 포함할 수 있습니다. 생성형 AI의 가장 흥미로운 응용 분야 중 하나는 언어 모델 분야입니다.

## 소형 언어 모델이란?

소형 언어 모델(Small Language Model, SLM)은 대형 언어 모델(LLM)의 축소판으로 LLM의 많은 아키텍처 원칙과 기법을 활용하면서도 계산적 부담이 크게 줄어든 모델을 의미합니다.

SLM은 인간처럼 텍스트를 생성하도록 설계된 언어 모델의 하위 집합입니다. GPT-4와 같은 대형 모델과는 달리, SLM은 더 컴팩트하고 효율적이어서 계산 자원이 제한된 환경에서 이상적입니다. 크기가 작지만 여전히 다양한 작업을 수행할 수 있습니다. 일반적으로 SLM은 LLM을 압축하거나 증류하여 만들어지며, 원본 모델의 기능과 언어 능력의 상당 부분을 유지하려고 합니다. 모델 크기 축소는 전반적인 복잡도를 낮추어 메모리와 계산 요구 측면에서 SLM을 더 효율적으로 만듭니다. 이러한 최적화에도 불구하고 SLM은 여러 자연어 처리(NLP) 작업을 수행할 수 있습니다:

- 텍스트 생성: 일관성 있고 맥락에 맞는 문장이나 단락 생성.
- 텍스트 완성: 주어진 프롬프트 기반으로 문장을 예측하고 완성.
- 번역: 한 언어의 텍스트를 다른 언어로 변환.
- 요약: 긴 텍스트를 간결하고 이해하기 쉬운 요약으로 압축.

다만 대형 모델에 비해 성능이나 이해 깊이에서 일부 트레이드오프가 있습니다.

## 소형 언어 모델은 어떻게 작동하나요?
SLM은 방대한 양의 텍스트 데이터를 학습합니다. 학습 중 텍스트의 패턴과 구조를 익혀 문법적으로 정확하고 맥락에 맞는 텍스트를 생성할 수 있게 됩니다. 훈련 과정은 다음과 같습니다:

- 데이터 수집: 다양한 출처에서 대규모 텍스트 데이터셋 수집.
- 전처리: 학습에 적합하도록 데이터 정제 및 조직화.
- 학습: 기계 학습 알고리즘을 활용해 텍스트 이해 및 생성 능력 학습.
- 미세 조정: 특정 작업에서 성능 향상을 위한 모델 조정.

SLM 개발은 모바일 기기나 엣지 컴퓨팅 플랫폼과 같은 자원이 제한된 환경에서 배포해야 하는 모델에 대한 수요 증가에 부합합니다. 대규모 LLM은 무거운 자원 요구로 실용적이지 않을 수 있습니다. 효율성에 집중해 SLM은 성능과 접근성의 균형을 이루어 다양한 영역에서 널리 활용될 수 있습니다.

![slm](../../../translated_images/ko/slm.4058842744d0444a.webp)

## 학습 목표

본 강의에서는 SLM 지식을 소개하고 Microsoft Phi-3와 결합해 텍스트 콘텐츠, 비전, MoE의 다양한 시나리오를 학습할 것입니다.

강의 종료 시 아래 질문들에 답할 수 있기를 기대합니다:

- SLM이란 무엇인가요?
- SLM과 LLM의 차이는 무엇인가요?
- Microsoft Phi-3/3.5 패밀리란 무엇인가요?
- Microsoft Phi-3/3.5 패밀리로 추론을 수행하려면 어떻게 하나요?

준비되었나요? 시작해 봅시다.

## 대형 언어 모델(LLM)과 소형 언어 모델(SLM)의 차이점

LLM과 SLM 모두 확률적 머신러닝의 기본 원리를 바탕으로 비슷한 아키텍처 설계, 학습 방법론, 데이터 생성 과정, 모델 평가 기법을 따릅니다. 하지만 몇 가지 중요한 요인이 이 두 모델 유형을 구분합니다.

## 소형 언어 모델의 응용 분야

SLM은 다음과 같은 다양한 분야에 활용됩니다:

- 챗봇: 고객 지원 제공 및 사용자와 대화형 상호작용.
- 콘텐츠 생성: 작가를 도와 아이디어 생성이나 전체 기사 초안 작성.
- 교육: 학생의 글쓰기 과제 지원 및 새로운 언어 학습 보조.
- 접근성: 텍스트 음성 변환 시스템 등 장애인을 위한 도구 개발.

<strong>크기</strong>
  
LLM과 SLM의 주요 차이는 모델의 크기에 있습니다. ChatGPT(GPT-4) 같은 LLM은 약 1.76조 개의 매개변수를 포함하는 반면, Mistral 7B와 같은 오픈소스 SLM은 약 70억 개의 매개변수로 설계되어 훨씬 작습니다. 이는 주로 모델 아키텍처와 학습 과정의 차이 때문입니다. 예컨대, ChatGPT는 인코더-디코더 구조 내에서 자체 주의 메커니즘을 사용하지만, Mistral 7B는 디코더 전용 모델에서 슬라이딩 윈도우 어텐션을 사용해 효율적인 학습이 가능합니다. 이 아키텍처의 차이는 모델 복잡도와 성능에 큰 영향을 미칩니다.

<strong>이해력</strong>

SLM은 특정 도메인 내에서 최적화되어 높은 전문성을 가지지만, 광범위한 분야에서 넓은 맥락 이해를 제공하는 데는 한계가 있을 수 있습니다. 반면 LLM은 다양한 방대한 데이터셋으로 학습되어 더 포괄적이고 인간에 가까운 지능 시뮬레이션을 목표로 합니다. 따라서 LLM은 자연어 처리, 프로그래밍 등 더 다양한 후속 작업에 적합합니다.

**계산 자원**

LLM의 학습과 배포는 대규모 GPU 클러스터 등 막대한 계산 인프라가 필요합니다. 예를 들어, ChatGPT 같은 모델을 처음부터 학습하려면 수천 대의 GPU가 오랜 기간 필요합니다. 반면 SLM은 매개변수 수가 적어 계산 자원 면에서 접근성이 높습니다. Mistral 7B 같은 모델은 중간 수준 GPU를 갖춘 로컬 머신에서 학습 및 실행 가능하지만, 학습에는 여전히 여러 GPU에 걸쳐 수 시간이 필요합니다.

<strong>편향</strong>

편향은 LLM에서 알려진 문제로, 주로 학습 데이터 특성에서 비롯됩니다. 이들 모델은 인터넷에서 수집된 원시 공개 데이터를 사용하는 경우가 많아, 특정 집단이 과소 또는 잘못 대표되거나 잘못된 라벨링, 방언·지리적 차이나 문법적 편향이 반영될 수 있습니다. 또한 LLM의 복잡한 아키텍처는 편향을 악화시키기도 하며, 세밀한 미세 조정 없이는 발견이 어려울 수 있습니다. 반면 SLM은 더 제한적이고 도메인 특화된 데이터셋으로 학습되기 때문에 이러한 편향에 덜 민감하지만 완전히 자유롭지는 않습니다.

**추론 속도**

SLM의 작은 크기는 추론 속도 면에서 큰 이점을 제공합니다. 로컬 하드웨어에서 광범위한 병렬 처리가 필요 없이 효율적으로 결과를 생성할 수 있습니다. 반면 LLM은 크기와 복잡성 때문에 적절한 추론 시간을 유지하려면 상당한 병렬 계산 자원이 필요합니다. 다수의 동시 사용자도 LLM의 응답 속도를 늦출 수 있으며, 특히 대규모 배포 시 더 심각합니다.

요약하면, LLM과 SLM은 모두 머신러닝을 근간으로 하지만, 모델 크기, 자원 요구량, 맥락 이해, 편향 민감성, 추론 속도 측면에서 크게 차이가 있습니다. 이러한 차이는 각각의 사용 사례 적합성을 반영하며, LLM은 더 범용적이지만 자원 집약적이고, SLM은 도메인별 효율성을 제공하면서도 계산 요구가 적은 장점이 있습니다.

***참고: 본 강의에서는 Microsoft Phi-3 / 3.5를 예로 들어 SLM을 소개합니다.***

## Phi-3 / Phi-3.5 패밀리 소개

Phi-3 / 3.5 패밀리는 주로 텍스트, 비전, 에이전트(MoE) 응용 시나리오를 대상으로 합니다:

### Phi-3 / 3.5 인스트럭트

주로 텍스트 생성, 채팅 완성, 콘텐츠 정보 추출 등에 사용됩니다.

**Phi-3-mini**

3.8B 매개변수 언어 모델이며 Microsoft Foundry, Hugging Face, Ollama에서 사용할 수 있습니다. Phi-3 모델은 주요 벤치마크에서 동급 또는 더 큰 크기의 언어 모델을 크게 능가합니다(아래 벤치마크 참고, 숫자가 높을수록 우수). Phi-3-mini는 두 배 크기의 모델보다 뛰어나며, Phi-3-small과 Phi-3-medium은 GPT-3.5를 포함한 더 큰 모델보다도 우수합니다.

**Phi-3-small & medium**

단 7B 매개변수만 가진 Phi-3-small은 다양한 언어, 추론, 코딩, 수학 벤치마크에서 GPT-3.5T를 능가합니다.

14B 매개변수를 가진 Phi-3-medium도 이러한 흐름을 이어가며 Gemini 1.0 Pro를 능가합니다.

**Phi-3.5-mini**

Phi-3-mini의 업그레이드 버전으로 볼 수 있습니다. 매개변수 수는 동일하지만, 다중 언어 지원 능력이 향상되었습니다(20개 이상 언어 지원: 아랍어, 중국어, 체코어, 덴마크어, 네덜란드어, 영어, 핀란드어, 프랑스어, 독일어, 히브리어, 헝가리어, 이탈리아어, 일본어, 한국어, 노르웨이어, 폴란드어, 포르투갈어, 러시아어, 스페인어, 스웨덴어, 태국어, 터키어, 우크라이나어) 그리고 긴 문맥 지원이 강화되었습니다.

3.8B 매개변수 Phi-3.5-mini는 동급 언어 모델보다 우수하며 두 배 크기의 모델과 견줄 만합니다.

### Phi-3 / 3.5 비전

Phi-3/3.5 인스트럭트 모델은 Phi의 이해 능력에 해당하며, 비전은 Phi에게 세상을 이해하는 눈을 제공합니다.


**Phi-3-Vision**

4.2B 매개변수만 가진 Phi-3-vision은 이 흐름을 이어가며 일반적인 시각 추론, OCR, 표 및 다이어그램 이해 작업에서 Claude-3 Haiku, Gemini 1.0 Pro 등 더 큰 모델을 능가합니다.


**Phi-3.5-Vision**

Phi-3.5-Vision은 Phi-3-Vision의 업그레이드 버전으로 다중 이미지 지원이 추가되었습니다. 단순히 사진만 보는 것이 아니라 동영상도 볼 수 있는 비전 향상으로 이해할 수 있습니다.

Phi-3.5-vision은 OCR, 표 및 차트 이해 작업에서 Claude-3.5 Sonnet, Gemini 1.5 Flash 등의 더 큰 모델보다 우수하며, 일반 시각 지식 추론 작업에서는 동등한 성능을 보입니다. 다중 프레임 입력을 지원하여 여러 입력 이미지를 기반으로 추론할 수 있습니다.


### Phi-3.5-MoE

<strong><em>전문가 혼합(Mixture of Experts, MoE)</em></strong>는 적은 연산량으로 사전 학습 가능하게 하여, 동일한 연산 예산으로 모델 또는 데이터셋 크기를 크게 확장할 수 있습니다. 특히, MoE 모델은 조밀한(dense) 모델과 동일한 품질을 사전 학습 중 훨씬 빠르게 달성할 수 있습니다.

Phi-3.5-MoE는 16개의 3.8B 전문가 모듈로 구성됩니다. 6.6B 활성 매개변수만으로도 훨씬 큰 모델과 유사한 수준의 추론, 언어 이해, 수학 능력을 보여 줍니다.

Phi-3/3.5 패밀리 모델은 다양한 시나리오 기반으로 사용할 수 있습니다. LLM과 달리 Phi-3/3.5-mini 또는 Phi-3/3.5-Vision은 엣지 디바이스에 배포할 수 있습니다.


## Phi-3/3.5 패밀리 모델 사용 방법

Phi-3/3.5를 다양한 시나리오에 적용하는 것을 목표로 합니다. 다음으로 시나리오별로 Phi-3/3.5를 사용하는 방법을 살펴보겠습니다.

![phi3](../../../translated_images/ko/phi3.655208c3186ae381.webp)

### 클라우드 API를 통한 추론

**Microsoft Foundry 모델**

> **참고:** GitHub Models는 2026년 7월 말에 종료됩니다. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)가 직접적인 대체입니다.

Microsoft Foundry Models는 가장 직접적인 접근 방법입니다. Foundry 모델 카탈로그를 통해 Phi-3/3.5-Instruct 모델에 빠르게 접근할 수 있습니다. Azure AI Inference SDK / OpenAI SDK와 결합하면 코드로 API에 접근하여 Phi-3/3.5-Instruct 호출을 완료할 수 있습니다. Playground를 통해 다양한 결과를 테스트할 수도 있습니다.

- 데모: 중국어 시나리오에서 Phi-3-mini와 Phi-3.5-mini의 효과 비교

![phi3](../../../translated_images/ko/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ko/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

비전 및 MoE 모델을 사용하려면 Microsoft Foundry를 통해 호출할 수 있습니다. 관심 있다면 Phi-3 Cookbook에서 Microsoft Foundry를 통해 Phi-3/3.5 Instruct, Vision, MoE를 호출하는 방법을 참고하시기 바랍니다. [이 링크 클릭](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

클라우드 기반 Microsoft Foundry Models 카탈로그 외에도 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)을 사용하여 관련 호출을 완료할 수 있습니다. NVIDIA NIM(NVIDIA Inference Microservices)은 클라우드, 데이터 센터, 워크스테이션 등 다양한 환경에서 AI 모델을 효율적으로 배포할 수 있도록 지원하는 가속화된 추론 마이크로서비스 집합입니다.

NVIDIA NIM의 주요 특징은 다음과 같습니다:

- **손쉬운 배포:** NIM은 단일 명령으로 AI 모델 배포를 가능하게 하여, 기존 워크플로우에 간단히 통합할 수 있습니다.

- **최적화된 성능:** TensorRT 및 TensorRT-LLM과 같은 NVIDIA의 사전 최적화된 추론 엔진을 활용하여 낮은 지연 시간과 높은 처리량을 보장합니다.
- **확장성:** NIM은 Kubernetes에서 자동 확장을 지원하여 다양한 워크로드를 효과적으로 처리할 수 있습니다.
- **보안 및 제어:** 조직은 자체 관리 인프라에서 NIM 마이크로서비스를 자체 호스팅하여 데이터와 애플리케이션에 대한 제어를 유지할 수 있습니다.
- **표준 API:** NIM은 업계 표준 API를 제공하여 챗봇, AI 어시스턴트 등 AI 애플리케이션 구축 및 통합을 쉽게 만듭니다.

NIM은 NVIDIA AI Enterprise의 일부로, AI 모델 배포와 운영화를 간소화하여 NVIDIA GPU에서 효율적으로 실행되도록 합니다.

- 데모: NVIDIA NIM을 사용하여 Phi-3.5-Vision-API 호출하기 [[이 링크 클릭](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 로컬 실행
Phi-3 또는 GPT-3과 같은 언어 모델에서의 추론은 입력받은 내용을 바탕으로 응답이나 예측을 생성하는 과정을 의미합니다. Phi-3에 프롬프트나 질문을 제공하면, 훈련된 신경망을 사용해 훈련 데이터 내 패턴과 관계를 분석하여 가장 가능성 높고 적절한 응답을 추론합니다.

**Hugging Face Transformer**
Hugging Face Transformers는 자연어 처리(NLP) 및 기타 머신러닝 작업을 위해 설계된 강력한 라이브러리입니다. 주요 사항은 다음과 같습니다:

1. **사전학습 모델:** 텍스트 분류, 개체명 인식, 질문 응답, 요약, 번역, 텍스트 생성 등 다양한 작업에 사용할 수 있는 수천 개의 사전학습 모델을 제공합니다.

2. **프레임워크 상호운용성:** PyTorch, TensorFlow, JAX 등 여러 딥러닝 프레임워크를 지원하여 한 프레임워크에서 모델을 훈련시키고 다른 프레임워크에서 활용할 수 있습니다.

3. **멀티모달 기능:** NLP 외에도 컴퓨터 비전(예: 이미지 분류, 객체 탐지) 및 오디오 처리(예: 음성 인식, 오디오 분류) 작업을 지원합니다.

4. **사용 용이성:** 모델 다운로드와 파인튜닝을 쉽게 할 수 있도록 API와 도구를 제공하여 초보자와 전문가 모두에게 접근성이 좋습니다.

5. **커뮤니티 및 자료:** 활발한 커뮤니티와 방대한 문서, 튜토리얼, 가이드가 있어 사용자가 시작하고 최대한 활용할 수 있게 돕습니다.
[공식 문서](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 또는 [GitHub 저장소](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)를 참고하세요.

가장 일반적으로 사용되는 방법이지만 GPU 가속이 필요합니다. 특히 Vision과 MoE 같은 시나리오는 계산량이 많아 양자화가 되지 않으면 CPU에서 매우 느립니다.


- 데모: Transformer를 사용해 Phi-3.5-Instruct 호출하기 [이 링크 클릭](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 데모: Transformer를 사용해 Phi-3.5-Vision 호출하기 [이 링크 클릭](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 데모: Transformer를 사용해 Phi-3.5-MoE 호출하기 [이 링크 클릭](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)는 대형 언어 모델(LLM)을 로컬에서 쉽게 실행할 수 있게 해주는 플랫폼입니다. Llama 3.1, Phi 3, Mistral, Gemma 2 등 다양한 모델을 지원합니다. 모델 가중치, 구성, 데이터를 하나의 패키지로 묶어 사용자가 직접 모델을 커스터마이징하고 만들기 쉽게 합니다. macOS, Linux, Windows에서 사용 가능하며, 클라우드 서비스에 의존하지 않고 LLM을 실험하거나 배포하려는 경우 훌륭한 도구입니다. Ollama는 가장 직접적인 방법이며, 다음 명령어만 실행하면 됩니다.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)은 Phi 같은 모델을 완전히 자체 하드웨어에서 오프라인으로 실행하기 위한 Microsoft의 온디바이스 런타임입니다 — Azure 구독, API 키, 네트워크 연결이 필요하지 않습니다. 사용 가능한 최적의 실행 공급자(NPU, GPU, CPU)를 자동으로 선택하며, OpenAI 호환 엔드포인트를 노출하여 기존의 `openai`/Azure AI Inference SDK 코드가 거의 변경 없이 이를 가리킬 수 있습니다. 시작하려면 [Foundry Local 문서](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)를 참조하세요.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

또는 Python에서 SDK를 직접 사용하세요:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**Generative AI용 ONNX Runtime**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst)은 크로스 플랫폼 추론 및 학습 머신러닝 가속기입니다. Generative AI(GENAI)용 ONNX Runtime은 다양한 플랫폼에서 생성 AI 모델을 효율적으로 실행할 수 있게 돕는 강력한 도구입니다.

## ONNX Runtime이란?
ONNX Runtime은 머신러닝 모델의 고성능 추론을 가능하게 하는 오픈소스 프로젝트입니다. ONNX 형식을 지원하는데, 이는 머신러닝 모델 표현 표준입니다. ONNX Runtime 추론은 고객 경험을 빠르게 하고 비용을 절감할 수 있게 하며, PyTorch, TensorFlow/Keras 같은 딥러닝 프레임워크 뿐만 아니라 scikit-learn, LightGBM, XGBoost 등 전통적 머신러닝 라이브러리 모델도 지원합니다. ONNX Runtime은 다양한 하드웨어, 드라이버, 운영체제와 호환되며, 하드웨어 가속기 활용과 그래프 최적화 및 변환을 통해 최적의 성능을 제공합니다.

## 생성 AI란?
생성 AI는 텍스트, 이미지, 음악 등 새로운 콘텐츠를 학습한 데이터를 바탕으로 생성할 수 있는 AI 시스템을 뜻합니다. 예로는 GPT-3 같은 언어 모델, Stable Diffusion 같은 이미지 생성 모델이 있습니다. ONNX Runtime for GenAI 라이브러리는 ONNX 모델에 대한 생성 AI 루프를 제공하며, ONNX Runtime을 통한 추론, 로짓 처리, 탐색 및 샘플링, KV 캐시 관리 등을 포함합니다.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI는 생성 AI 모델을 지원하도록 ONNX Runtime 기능을 확장한 것입니다. 주요 기능은 다음과 같습니다:

- **광범위한 플랫폼 지원:** Windows, Linux, macOS, Android, iOS 등 다양한 플랫폼에서 작동합니다.
- **모델 지원:** LLaMA, GPT-Neo, BLOOM 등 인기 있는 생성 AI 모델을 지원합니다.
- **성능 최적화:** NVIDIA, AMD GPU 등 다양한 하드웨어 가속기를 위한 최적화를 포함합니다.
- **사용 용이성:** 쉽게 통합할 수 있는 API를 제공하여 최소한의 코드로 텍스트, 이미지 등 콘텐츠를 생성할 수 있습니다.
- 사용자는 고수준의 generate() 메서드를 호출하거나 모델의 각 반복을 루프에서 실행하여 토큰 하나씩 생성하며 루프 내에서 생성 매개변수를 선택적으로 업데이트할 수 있습니다.
- ONNX Runtime은 토큰 시퀀스 생성을 위한 greedy/beam 탐색, TopP, TopK 샘플링과 반복 페널티 같은 내장 로짓 처리도 지원합니다. 또한 사용자 정의 점수 매기기도 쉽게 추가할 수 있습니다.

## 시작하기
ONNX Runtime for GENAI를 시작하려면 다음 단계를 따르세요:

### ONNX Runtime 설치:
```Python
pip install onnxruntime
```
### 생성 AI 확장 설치:
```Python
pip install onnxruntime-genai
```

### 모델 실행: Python 간단 예제:
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
### 데모: ONNX Runtime GenAI로 Phi-3.5-Vision 호출


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

ONNX Runtime, Ollama, Foundry Local 참조 방법 외에도 제조사별 모델 참조 방식을 기반으로 하는 정량화 모델 참조를 완성할 수 있습니다. 예를 들어 Apple Metal용 Apple MLX 프레임워크, NPU용 Qualcomm QNN, CPU/GPU용 Intel OpenVINO 등이 있습니다. 자세한 내용은 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다.


## 더 알아보기

우리는 Phi-3/3.5 패밀리의 기본을 배웠지만 SLM에 대해 더 배우려면 추가 지식이 필요합니다. 답은 Phi-3 Cookbook에서 찾을 수 있습니다. 더 배우고 싶다면 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)을 방문하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->