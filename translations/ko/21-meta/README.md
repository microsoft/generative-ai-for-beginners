<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:28:04+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ko"
}
-->
# Meta 패밀리 모델로 구축하기

## 소개

이 강의에서는 다음을 다룹니다:

- 두 가지 주요 Meta 패밀리 모델 - Llama 3.1과 Llama 3.2 탐색
- 각 모델의 사용 사례와 시나리오 이해
- 각 모델의 독특한 기능을 보여주는 코드 예시

## Meta 패밀리 모델

이 강의에서는 Meta 패밀리 또는 "Llama Herd"의 두 가지 모델 - Llama 3.1과 Llama 3.2를 탐색합니다.

이 모델들은 다양한 변형으로 제공되며 GitHub 모델 마켓플레이스에서 사용할 수 있습니다. GitHub 모델을 사용하여 [AI 모델로 프로토타입 만들기](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)에 대한 자세한 내용은 여기에서 확인하세요.

모델 변형:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*참고: Llama 3도 GitHub 모델에서 사용할 수 있지만 이 강의에서는 다루지 않습니다*

## Llama 3.1

4050억 개의 파라미터를 가진 Llama 3.1은 오픈 소스 LLM 카테고리에 속합니다.

이 모드는 이전 릴리스 Llama 3의 업그레이드로 다음을 제공합니다:

- 더 큰 컨텍스트 윈도우 - 128k 토큰 대 8k 토큰
- 더 큰 최대 출력 토큰 - 4096 대 2048
- 향상된 다국어 지원 - 훈련 토큰 증가로 인한

이로 인해 Llama 3.1은 GenAI 애플리케이션을 구축할 때 더 복잡한 사용 사례를 처리할 수 있습니다:
- 네이티브 함수 호출 - LLM 워크플로 외부의 외부 도구 및 함수 호출 기능
- 향상된 RAG 성능 - 더 높은 컨텍스트 윈도우로 인한
- 합성 데이터 생성 - 미세 조정과 같은 작업에 효과적인 데이터를 생성할 수 있는 기능

### 네이티브 함수 호출

Llama 3.1은 함수 또는 도구 호출을 더 효과적으로 수행하도록 미세 조정되었습니다. 또한 사용자의 프롬프트에 따라 사용해야 할 필요성을 인식할 수 있는 두 가지 내장 도구가 있습니다. 이 도구들은 다음과 같습니다:

- **Brave Search** - 웹 검색을 수행하여 날씨와 같은 최신 정보를 얻을 수 있습니다.
- **Wolfram Alpha** - 복잡한 수학적 계산을 수행할 수 있어 자체 함수를 작성할 필요가 없습니다.

사용자가 호출할 수 있는 맞춤형 도구를 만들 수도 있습니다.

아래 코드 예시에서는:

- 시스템 프롬프트에서 사용 가능한 도구(brave_search, wolfram_alpha)를 정의합니다.
- 특정 도시의 날씨에 대해 묻는 사용자 프롬프트를 보냅니다.
- LLM은 Brave Search 도구에 대한 도구 호출로 응답할 것이며, 이는 `<|python_tag|>brave_search.call(query="Stockholm weather")`처럼 보일 것입니다.

*참고: 이 예시는 도구 호출만 수행하며, 결과를 얻고 싶다면 Brave API 페이지에서 무료 계정을 생성하고 함수를 정의해야 합니다*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

LLM임에도 불구하고, Llama 3.1의 한 가지 제한점은 멀티모달리티입니다. 즉, 이미지를 프롬프트로 사용하고 응답을 제공하는 기능입니다. 이 기능은 Llama 3.2의 주요 특징 중 하나입니다. 이러한 기능에는 다음이 포함됩니다:

- 멀티모달리티 - 텍스트와 이미지 프롬프트 모두를 평가할 수 있는 기능
- 소형에서 중형 크기 변형(11B 및 90B) - 유연한 배포 옵션 제공
- 텍스트 전용 변형(1B 및 3B) - 모델을 엣지/모바일 장치에 배포할 수 있어 저지연성을 제공합니다.

멀티모달 지원은 오픈 소스 모델 세계에서 큰 진전을 나타냅니다. 아래 코드 예시는 이미지와 텍스트 프롬프트 모두를 사용하여 Llama 3.2 90B에서 이미지 분석을 얻습니다.

### Llama 3.2의 멀티모달 지원

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## 학습은 여기서 멈추지 않습니다, 여정을 계속하세요

이 강의를 마친 후, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 Generative AI 지식을 계속 업그레이드하세요!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확한 부분이 있을 수 있습니다. 원본 문서는 해당 언어로 작성된 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.