# 입문자를 위한 생성형 AI와 소형 언어 모델 소개

생성형 AI는 텍스트와 이미지부터 음악, 가상 환경까지 다양한 콘텐츠를 생성할 수 있는 시스템을 만드는 데 중점을 둔 인공지능의 흥미로운 분야입니다. 그중에서도 언어 모델은 생성형 AI의 가장 흥미로운 응용 분야 중 하나입니다.

## 소형 언어 모델(Small Language Models)이란?

소형 언어 모델(SLM)은 대형 언어 모델(LLM)의 축소판으로, LLM의 아키텍처 원칙과 기술을 활용하면서도 계산 자원 소모를 크게 줄인 모델입니다.

SLM은 인간과 유사한 텍스트를 생성하도록 설계된 언어 모델의 하위 집합으로, GPT-4와 같은 대형 모델과 달리 더 작고 효율적이기 때문에 컴퓨팅 자원이 제한된 응용 분야에 적합합니다.
SLM은 일반적으로 LLM을 압축하거나 증류하여 구축되며, 원래 모델의 기능과 언어적 능력을 상당 부분 유지하려고 합니다. 모델 크기를 줄이면 메모리 사용량과 계산 요구 사항이 낮아져 다음과 같은 다양한 자연어 처리(NLP) 작업을 수행할 수 있습니다:

- 텍스트 생성: 일관되고 문맥에 맞는 문장이나 단락을 생성합니다.
- 텍스트 완성: 주어진 프롬프트에 따라 문장을 예측하고 완성합니다.
- 번역: 텍스트를 한 언어에서 다른 언어로 변환합니다.
- 요약: 긴 텍스트를 더 간결하고 이해하기 쉬운 요약으로 압축합니다.

하지만 더 큰 모델에 비해 성능이나 이해의 깊이에서 약간의 한계가 있을 수 있습니다.

## 소형 언어 모델의 작동 원리

SLM은 방대한 양의 텍스트 데이터를 통해 훈련되며, 이 과정에서 언어의 패턴과 구조를 학습하여 문법적으로 정확하고 문맥상 적절한 텍스트를 생성할 수 있습니다. 훈련 과정은 다음과 같습니다:

- 데이터 수집: 다양한 소스에서 대량의 텍스트 데이터셋을 수집합니다.
- 전처리: 훈련에 적합하도록 데이터를 정리하고 구성합니다.
- 훈련: 기계 학습 알고리즘을 사용하여 모델에 텍스트 생성 및 이해 방법을 학습시킵니다.
- 파인 튜닝: 특정 작업의 성능을 향상시키기 위해 모델을 조정합니다.

SLM의 개발은 모바일 기기나 엣지 컴퓨팅 플랫폼과 같이 리소스가 제한된 환경에서도 모델을 배포해야 하는 요구를 충족합니다. 효율성에 초점을 맞춘 설계를 통해 성능과 접근성의 균형을 유지하여 다양한 분야에서 폭넓게 활용될 수 있습니다.

![slm](../../img/slm.png?WT.mc_id=academic-105485-koreyst)

## 학습 목표

이 강의에서는 SLM에 대한 지식을 소개하고, 이를 Microsoft Phi-3와 결합하여 텍스트 콘텐츠, 비전(Vision), MoE(Mixture of Experts) 등의 다양한 시나리오에서 활용하는 방법을 배울 것입니다.

이번 강의를 마치면 다음 질문에 답할 수 있습니다:

- SLM이란 무엇인가?
- SLM과 LLM의 차이점은 무엇인가?
- Microsoft Phi-3/3.5 패밀리는 무엇인가?
- Microsoft Phi-3/3.5 패밀리를 어떻게 활용하는가?

준비되셨나요? 시작해봅시다.

## 대형 언어 모델(LLMs)과 소형 언어 모델(SLMs)의 차이점

LLMs과 SLMs은 모두 확률론적 기계 학습의 기본 원리를 기반으로 하며, 아키텍처 설계, 훈련 방법론, 데이터 생성 프로세스, 모델 평가 기술에서 유사한 접근을 따릅니다. 그러나 이 두 모델을 구분하는 몇 가지 핵심요소가 있습니다.

## 소형 언어 모델의 응용 분야
SLM은 다음과 같은 다양한 응용 분야에서 사용됩니다:

- 챗봇: 고객 지원을 제공하고 사용자와 대화형으로 소통합니다.
- 콘텐츠 생성: 아이디어를 제공하거나 전체 글을 작성하는데 도움을 줍니다.
- 교육: 학생들의 작문 과제를 돕거나 새로운 언어 학습을 지원합니다.
- 접근성: 텍스트-음성 변환 시스템과 같은 장애인을 위한 도구를 만듭니다.

**모델 크기**

LLM과 SLM의 가장 큰 차이점은 모델의 규모입니다. 예를 들어, GPT-4와 같은 LLM은 약 1조 7,600억 개의 파라미터로 구성될 수 있는 반면, Mistral 7B와 같은 오픈 소스 SLM은 약 70억 개의 파라미터를 가집니다. 이러한 차이는 모델의 아키텍처와 훈련 프로세스의 차이에서 비롯됩니다. 예를 들어, ChatGPT는 인코더-디코더 프레임워크 내에서 자기 어텐션 메커니즘을 사용하지만, Mistral 7B는 슬라이딩 윈도우 어텐션을 사용하여 디코더 전용 모델 내에서 더 효율적인 훈련을 가능하게 합니다. 이러한 아키텍처의 차이는 모델의 복잡성과 성능에 큰 영향을 미칩니다. 

**이해력**

SLM은 특정 도메인 내에서의 성능에 최적화되어 고도로 전문화되어 있지만, 여러 분야에 걸쳐 광범위한 맥락적 이해를 제공하는 데는 한계가 있을 수 있습니다. 반면에 LLM은 방대한 양의 다양한 데이터셋으로 훈련되어 여러 분야에서 높은 성능을 발휘하도록 설계되었습니다. 방대한 양의 다양한 데이터셋으로 훈련된 LLM은 여러 분야에서 두루 활용되며, 적응력과 다재다능함이 뛰어납니다. 그래서 자연어 처리나 프로그래밍과 같은 더 넓은 범위의 작업에 더 적합합니다.

**계산 자원**

LLM의 훈련과 배포는 리소스 집약적이며, 대규모 GPU 클러스터 등의 상당한 컴퓨팅 인프라가 필요합니다. 예를 들어, ChatGPT와 같은 모델을 처음부터 훈련하려면 수천 개의 GPU로도 긴 시간이 필요할 수 있습니다.  반면에 SLM은 파라미터 수가 적어 계산 자원 측면에서 접근성이 높습니다. Mistral 7B와 같은 모델은 적당한 GPU를 갖춘 로컬 머신에서도 훈련하고 실행할 수 있지만, 훈련에는 여전히 여러 GPU에서 몇 시간이 소요됩니다.

**편향성**

LLM은 훈련 데이터의 특성으로 인해 편향 문제가 발생할 수 있습니다. 인터넷의 공개 데이터를 기반으로 훈련되기 때문에 특정 그룹을 과소 대표하거나 잘못 대표할 수 있고, 잘못된 라벨링을 도입 및 방언, 지리적 변이, 문법 규칙에 영향을 받는 언어적 편향을 반영할 수 있습니다. 또한 LLM 아키텍처의 복잡성은 세심한 파인튜닝 없이는 눈에 띄지 않게 편향을 악화시킬 수 있습니다.  반면에 SLM은 더 제한적이고 도메인 특화된 데이터셋으로 훈련되기 때문에 이러한 편향에 덜 취약하지만, 완전히 자유로운 것은 아닙니다.

**추론 속도**

SLM은 작은 크기로 인해 추론 속도 면에서 큰 이점을 제공합니다. 로컬 하드웨어에서 효율적으로 출력을 생성할 수 있으며, 대규모 병렬 처리가 필요하지 않습니다. 반면에 LLM은 크기와 복잡성으로 인해 추론 시간이 느릴 수 있으며, 특히 여러 사용자가 동시에 접근하는 경우 응답 시간이 더욱 지연될 수 있습니다.

요약하자면, LLM과 SLM은 머신러닝에 기반을 두고 있지만, 모델 크기, 자원 요구 사항, 맥락 이해, 편향 취약성, 추론 속도 등에서 상당한 차이가 있습니다. 이러한 차이는 각각의 사용 사례에 대한 적합성을 반영하며, LLM은 더 다재다능하지만 자원 소모가 크고, SLM은 특정 분야에서 효율성을 제공하면서 계산 요구 사항이 줄어듭니다.

***참고: 이 장에서는 Microsoft Phi-3 / 3.5를 예로 들어 SLM을 소개하겠습니다.***

## Microsoft Phi-3 / Phi-3.5 패밀리 소개

Phi-3 / 3.5 패밀리는 주로 텍스트, 비전(Vision), 에이전트(MoE) 응용 시나리오를 대상으로 합니다:

### Phi-3 / 3.5 Instruct

주로 텍스트 생성, 대화 완성, 정보 추출 등에 사용됩니다.

**Phi-3-mini**

3.8억 개의 파라미터를 가진 언어 모델로, Microsoft Azure AI Studio, Hugging Face, Ollama에서 사용할 수 있습니다. Phi-3 모델은 주요 벤치마크에서 동등하거나 더 큰 크기의 언어 모델보다 우수한 성능을 보입니다.(아래 벤치마크 수치를 참조하세요. 수치가 높을수록 좋습니다). Phi-3-mini는 크기가 두 배인 모델보다 뛰어난 성능을 보이며, Phi-3-small과 Phi-3-medium은 GPT-3.5를 포함한 더 큰 모델보다도 우수합니다.

**Phi-3-small & medium**

단 70억 개의 파라미터로 구성된 Phi-3-small은 다양한 언어, 추론, 코딩, 수학 벤치마크에서 GPT-3.5T를 뛰어넘는 성능을 보입니다.

140억 개의 파라미터를 가진 Phi-3-medium도 이러한 추세를 이어가며 Gemini 1.0 Pro보다 뛰어난 성능 보입니다.

**Phi-3.5-mini**

Phi-3-mini의 업그레이드 버전으로 볼 수 있습니다. 파라미터 수는 변함이 없지만, 다국어 지원 능력을 향상시켰습니다. (아랍어, 중국어, 체코어, 덴마크어, 네덜란드어, 영어, 핀란드어, 프랑스어, 독일어, 히브리어, 헝가리어, 이탈리아어, 일본어, 한국어, 노르웨이어, 폴란드어, 포르투갈어, 러시아어, 스페인어, 스웨덴어, 태국어, 터키어, 우크라이나어 등 20개 이상의 언어 지원) 그리고 긴 컨텍스트의 지원이 강화되었습니다. 

3.8억 개의 파라미터를 가진 Phi-3.5-mini는 동일한 크기의 언어 모델보다 우수하며, 크기가 두 배인 모델과 동등한 성능을 보입니다.

### Phi-3 / 3.5 Vision

Phi-3/3.5의 Instruct 모델이 Phi의 이해 능력이라면, Vision 모델은 Phi에게 세상을 이해하는 눈을 제공합니다.

**Phi-3-Vision**

단 42억 개의 파라미터를 가진 Phi-3-vision은 일반적인 시각적 추론 작업, OCR, 표 및 다이어그램 이해 작업에서 Claude-3 Haiku와 Gemini 1.0 Pro V와 같은 더 큰 모델보다 뛰어난 성능을 보입니다.

**Phi-3.5-Vision**

Phi-3-Vision의 업그레이드 버전으로, 다중 이미지 지원을 추가했습니다. 이제 단순히 이미지를 보는 것뿐만 아니라 동영상까지도 볼 수 있다고 생각하시면 됩니다.

Phi-3.5-Vision은 OCR, 표 및 차트 이해 작업에서 Claude-3.5 Sonnet과 Gemini 1.5 Flash와 같은 더 큰 모델을 능가하며, 일반적인 시각적 지식 추론 작업에서도 동등한 성능을 보입니다. 다중 프레임 입력을 지원, 즉 여러 입력 이미지에 대한 추론을 수행할 수 있습니다.

### Phi-3.5-MoE

***전문가 혼합(Mixture of Experts, MoE)*** 은 모델이 훨씬 적은 계산량으로 사전 훈련될 수 있게 하며, 이는 고밀도 모델과 동일한 계산 예산으로 모델이나 데이터셋의 크기를 크게 확장할 수 있음을 의미합니다. 특히, MoE 모델은 사전 학습 중에 고밀도 모델과 동일한 품질을 훨씬 더 빨리 달성할 수 있습니다. 

Phi-3.5-MoE는 16개의 3.8억 개 파라미터를 가진 전문가 모듈로 구성됩니다. 단 66억 개의 활성 파라미터만으로 구성된 Phi-3.5-MoE는 훨씬 더 큰 모델과 유사한 수준의 추론, 언어 이해, 수학 능력을 달성합니다.

Phi-3/3.5 패밀리 모델은 다양한 시나리오에 맞춰 활용할 수 있으며, LLM과 달리 Phi-3/3.5-mini나 Phi-3/3.5-Vision은 엣지 디바이스에도 배포할 수 있습니다.

## Phi-3/3.5 패밀리 모델 사용 방법

이제 다양한 시나리오에서 Phi-3/3.5 모델을 어떻게 활용할 수 있는지 알아보겠습니다. 다음으로, 다양한 시나리오를 기반으로 Phi-3/3.5를 사용해 보겠습니다.

![phi3](../../img/phi3.png?WT.mc_id=academic-105485-koreyst)

### 클라우드 API를 통한 추론

**GitHub Models**

GitHub Models는 가장 직접적인 방법입니다. GitHub Models를 통해 Phi-3/3.5-Instruct 모델에 빠르게 접근할 수 있습니다. Azure AI Inference SDK나 OpenAI SDK와 결합하여 코드로 API에 접근하여 Phi-3/3.5-Instruct를 호출할 수 있습니다. 또한 Playground를 통해 다양한 효과를 테스트할 수도 있습니다.

- 데모: 중국어 시나리오에서 Phi-3-mini와 Phi-3.5-mini의 효과 비교

![phi3](../../img/gh1.png?WT.mc_id=academic-105485-koreyst)

![phi35](../../img/gh2.png?WT.mc_id=academic-105485-koreyst)


**Azure AI Studio**

아니면 비전과 MoE 모델을 사용하고자 한다면, Azure AI Studio를 통해 호출할 수 있습니다. 관심이 있다면, Phi-3 Cookbook을 읽어 Azure AI Studio를 통해 Phi-3/3.5 Instruct, Vision, MoE를 호출하는 방법을 배울 수 있습니다. [이 링크를 클릭하세요.](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)

**NVIDIA NIM**

Azure와 GitHub에서 제공하는 클라우드 기반 모델 카탈로그 솔루션 외에도, [Nivida NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst)을 사용하여 관련 호출을 완료할 수 있습니다. NVIDIA NIM을 통해 Phi-3/3.5 패밀리의 API 호출을 할 수 있습니다. NVIDIA NIM(NVIDIA Inference Microservices)은 클라우드, 데이터 센터, 워크스테이션 등 다양한 환경에서 AI 모델을 효율적으로 배포할 수 있도록 설계된 가속화된 추론 마이크로서비스 세트입니다.

NVIDIA NIM의 주요 특징:

- **간편한 배포**: NIM은 단일 명령으로 AI 모델을 배포할 수 있어 기존 워크플로우에 쉽게 통합할 수 있습니다.
- **최적화된 성능**: NVIDIA의 사전 최적화된 추론 엔진(TensorRT, TensorRT-LLM 등)을 활용하여 낮은 지연 시간과 높은 처리량을 보장합니다.
- **확장성**: Kubernetes에서 자동 확장을 지원하여 다양한 워크로드를 효과적으로 처리할 수 있습니다.
보안 및 제어: 조직은 자체 관리 인프라에 NIM 마이크로서비스를 자체 호스팅하여 데이터와 애플리케이션에 대한 제어를 유지할 수 있습니다.
- **표준 API**: NIM은 업계 표준 API를 제공하여 챗봇, AI 어시스턴트 등과 같은 AI 애플리케이션을 쉽게 구축하고 통합할 수 있습니다.

NIM은 NVIDIA AI Enterprise의 일부로, AI 모델의 배포와 운영을 간소화하여 NVIDIA GPU에서 효율적으로 실행되도록 합니다.

- 데모: NVIDIA NIM을 사용하여 Phi-3.5-Vision API 호출하려면 [[이 링크를 클릭하세요](../..//python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]

### 로컬 환경에서 Phi-3/3.5 추론하기

Phi-3 또는 GPT-3와 같은 언어 모델에서 추론은 입력받은 내용에 기반하여 응답이나 예측을 생성하는 과정을 말합니다. 프롬프트나 질문을 Phi-3에 제공하면, 훈련된 신경망을 사용하여 훈련된 데이터의 패턴과 관계를 분석하여 가장 가능성 있고 관련성 높은 응답을 추론합니다.

**Hugging Face Transformers**

Hugging Face Transformers는 자연어 처리(Natural Language Processing, NLP) 및 기타 머신러닝 작업을 위한 강력한 라이브러리입니다. 주요 특징은 다음과 같습니다:

1. **사전 훈련된 모델**: 텍스트 분류, 개체명 인식, 질문 응답, 요약, 번역, 텍스트 생성 등 다양한 작업에 사용할 수 있는 수천 개의 사전 훈련된 모델을 제공합니다.

2. **프레임워크 호환성**: PyTorch, TensorFlow, JAX 등 여러 딥러닝 프레임워크를 지원합니다. 한 프레임워크에서 모델을 훈련하고 다른 프레임워크에서 사용할 수 있습니다.


3. **멀티모달 기능**: NLP 외에도 컴퓨터 비전(이미지 분류, 물체 인식 등) 및 오디오 처리(음성 인식, 오디오 분류 등) 작업도 지원합니다.

4. **사용 편의성**: 모델을 쉽게 다운로드하고 파인튜닝할 수 있는 API와 도구를 제공하여 초보자와 전문가 모두에게 접근성이 높습니다.

5. **커뮤니티와 리소스**: Hugging Face는 활발한 커뮤니티와 광범위한 문서, 튜토리얼, 가이드가 있어 사용자가 시작하고 라이브러리를 최대한 활용할 수 있도록 돕습니다. [공식 문서](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 또는 [GitHub 리포지토리](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)를 참조하세요.

이 방법은 가장 일반적으로 사용되지만 GPU 가속이 필요합니다. Vision이나 MoE와 같은 시나리오는 많은 계산이 필요하며, 양자화하지 않으면 CPU에서 매우 제한적입니다.

- 데모: Transformer를 사용하여 Phi-3.5-Instruct 호출하기 - [이 링크를 클릭하세요](../..//python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)
- 데모: Transformer를 사용하여 Phi-3.5-Vision 호출하기 - [이 링크를 클릭하세요](../..//python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)
- 데모: Transformer를 사용하여 Phi-3.5-MoE 호출하기 - [이 링크를 클릭하세요](../..//python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**

[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)는 로컬에서 대형 언어 모델(LLM)을 실행하기 쉽게 만들어주는 플랫폼입니다. Llama 3.1, Phi 3, Mistral, Gemma 2 등 다양한 모델을 지원합니다. Ollama는 모델 가중치, 구성, 데이터를 하나의 패키지로 묶어 사용자가 자신만의 모델을 커스터마이징하고 생성할 수 있게 합니다. Ollama는 macOS, Linux, Windows에서 사용할 수 있습니다. 클라우드 서비스를 사용하지 않고 LLM을 실험하거나 배포하고자 한다면 훌륭한 도구입니다. Ollama는 가장 직접적인 방법으로, 다음 명령을 실행하면 됩니다.


```bash

ollama run phi3.5

```


**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst)은 플랫폼 간 추론 및 훈련 머신러닝 가속기입니다. ONNX Runtime for Generative AI(GENAI)는 생성형 AI 모델을 다양한 플랫폼에서 효율적으로 실행할 수 있도록 도와주는 강력한 도구입니다.

## ONNX Runtime이란?
ONNX Runtime은 머신러닝 모델의 고성능 추론을 가능하게 하는 오픈 소스 프로젝트입니다. ONNX(Open Neural Network Exchange) 형식의 모델을 지원하며, 이는 머신러닝 모델을 표현하는 표준입니다. ONNX Runtime 추론은 더 빠른 사용자 경험과 낮은 비용을 가능하게 하며, PyTorch, TensorFlow/Keras 등의 딥러닝 프레임워크와 scikit-learn, LightGBM, XGBoost 등의 클래식 머신러닝 라이브러리의 모델을 지원합니다. ONNX Runtime은 다양한 하드웨어, 드라이버, 운영 체제와 호환되며, 하드웨어 가속기를 활용하여 최적의 성능을 제공합니다.

## 생성형 AI란?
생성형 AI는 훈련된 데이터를 바탕으로 새로운 콘텐츠(텍스트, 이미지, 음악 등)를 생성할 수 있는 AI 시스템을 말합니다. GPT-3와 같은 언어 모델이나 Stable Diffusion과 같은 이미지 생성 모델이 예시입니다. ONNX Runtime for GenAI 라이브러리는 ONNX 모델에 대한 생성형 AI 루프를 제공하며 여기에는 ONNX Runtime을 사용한 추론, 로짓 처리, 검색 및 샘플링, KV 캐시 관리를 포함합니다.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI는 ONNX Runtime의 기능을 확장하여 생성형 AI 모델을 지원합니다. 주요 특징은 다음과 같습니다:

- **광범위한 플랫폼 지원**: Windows, Linux, macOS, Android, iOS 등 다양한 플랫폼에서 작동합니다.
- **모델 지원**: LLaMA, GPT-Neo, BLOOM 등 많은 인기 있는 생성형 AI 모델을 지원합니다.
- **성능 최적화**: NVIDIA GPU, AMD GPU 등 다양한 하드웨어 가속기에 대한 최적화를 포함합니다.
- **사용 편의성**: 애플리케이션에 쉽게 통합할 수 있는 API를 제공하여 최소한의 코드로 텍스트, 이미지 등의 콘텐츠를 생성할 수 있습니다.
- 사용자는 고수준의 generate() 메서드를 호출하거나 모델의 각 반복을 루프 내에서 실행하여 한 번에 한 토큰씩 생성하고, 필요에 따라 루프 내에서 생성 파라미터를 업데이트할 수 있습니다.
- ONNX 런타임은 그리디/빔 서치 및 TopP, TopK 샘플링을 지원하여 토큰 시퀀스를 생성하고, 반복 패널티와 같은 내장된 로짓 처리를 제공합니다. 또한, 사용자 정의 스코어링을 쉽게 추가할 수 있습니다.


## 시작하기
ONNX Runtime for GENAI를 시작하려면 다음 단계를 따르세요:

### ONNX Runtime 설치:
```Python
pip install onnxruntime
```
### 생성형 AI 익스텐션 설치:
```Python
pip install onnxruntime-genai
```
### 모델 실행: Python의 간단한 예시:
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
### 데모: ONNX Runtime GenAI를 사용하여 Phi-3.5-Vision 호출하기


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
    
    code += tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**기타**

ONNX Runtime과 Ollama 외에도, 다양한 제조업체에서 제공하는 방법을 통해 양자화된 모델의 추론을 수행할 수 있습니다. 예를 들어 Apple Metal과 함께 Apple MLX 프레임워크, NPU와 함께 Qualcomm QNN, CPU/GPU와 함께 Intel OpenVINO 등을 사용할 수 있습니다. 더 많은 내용은 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)에서 찾을 수 있습니다.



## 더 알아보기

이제 Phi-3/3.5 패밀리의 기본 개념을 배웠지만, SLM을 더 깊이 이해하려면 추가 학습이 필요합니다. 더 많은 정보가 궁금하다면 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)을 방문해 보세요.
