<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:08:10+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ko"
}
-->
# 메타 패밀리 모델 구축

## 소개

이 강의에서는 다음 내용을 다룹니다:

- 두 가지 주요 메타 패밀리 모델 - Llama 3.1과 Llama 3.2 탐색
- 각 모델의 사용 사례와 시나리오 이해
- 각 모델의 고유한 기능을 보여주는 코드 샘플

## 메타 패밀리 모델

이 강의에서는 메타 패밀리 또는 "Llama Herd"의 두 모델 - Llama 3.1과 Llama 3.2를 탐색합니다.

이 모델들은 다양한 변형으로 제공되며 GitHub 모델 마켓플레이스에서 이용할 수 있습니다. GitHub 모델을 사용하여 [AI 모델로 프로토타입 제작](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)에 대한 자세한 내용은 여기를 참고하세요.

모델 변형:
- Llama 3.1 - 70B 인스트럭트
- Llama 3.1 - 405B 인스트럭트
- Llama 3.2 - 11B 비전 인스트럭트
- Llama 3.2 - 90B 비전 인스트럭트

*참고: Llama 3도 GitHub 모델에서 이용할 수 있지만, 이 강의에서는 다루지 않습니다*

## Llama 3.1

405억 개의 파라미터로 구성된 Llama 3.1은 오픈 소스 LLM 카테고리에 속합니다.

이 모델은 이전 버전인 Llama 3의 업그레이드로 다음을 제공합니다:

- 더 큰 컨텍스트 창 - 128k 토큰 vs 8k 토큰
- 더 큰 최대 출력 토큰 - 4096 vs 2048
- 다국어 지원 향상 - 훈련 토큰 증가로 인해

이로 인해 Llama 3.1은 GenAI 애플리케이션을 구축할 때 더 복잡한 사용 사례를 처리할 수 있습니다. 예를 들어:
- 네이티브 함수 호출 - LLM 워크플로 외부의 외부 도구와 함수를 호출하는 기능
- 더 나은 RAG 성능 - 더 높은 컨텍스트 창 덕분에
- 합성 데이터 생성 - 미세 조정과 같은 작업을 위한 효과적인 데이터를 생성하는 기능

### 네이티브 함수 호출

Llama 3.1은 함수 또는 도구 호출을 더 효과적으로 수행하도록 미세 조정되었습니다. 또한 사용자로부터의 프롬프트에 따라 사용해야 할 필요가 있는 두 가지 내장 도구를 식별할 수 있습니다. 이러한 도구는:

- **Brave Search** - 웹 검색을 수행하여 날씨와 같은 최신 정보를 얻을 수 있습니다
- **Wolfram Alpha** - 더 복잡한 수학적 계산을 수행할 수 있어 자신의 함수를 작성할 필요가 없습니다.

사용자가 호출할 수 있는 사용자 정의 도구도 만들 수 있습니다.

아래 코드 예제에서는:

- 시스템 프롬프트에서 사용 가능한 도구(brave_search, wolfram_alpha)를 정의합니다.
- 특정 도시의 날씨에 대해 묻는 사용자 프롬프트를 보냅니다.
- LLM은 Brave Search 도구에 대한 도구 호출로 응답하며, 이는 `<|python_tag|>brave_search.call(query="Stockholm weather")`처럼 보일 것입니다.

*참고: 이 예제는 도구 호출만 수행하며, 결과를 얻으려면 Brave API 페이지에서 무료 계정을 생성하고 함수 자체를 정의해야 합니다.*

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

LLM임에도 불구하고 Llama 3.1은 멀티모달리티라는 제한이 있습니다. 즉, 이미지를 프롬프트로 사용하고 응답을 제공하는 등 다양한 유형의 입력을 사용할 수 있는 능력입니다. 이 능력은 Llama 3.2의 주요 기능 중 하나입니다. 이러한 기능에는 다음이 포함됩니다:

- 멀티모달리티 - 텍스트와 이미지 프롬프트를 모두 평가할 수 있는 능력
- 소형에서 중형 크기 변형(11B 및 90B) - 유연한 배포 옵션 제공
- 텍스트 전용 변형(1B 및 3B) - 엣지/모바일 장치에서 모델을 배포할 수 있으며 낮은 대기 시간 제공

멀티모달 지원은 오픈 소스 모델 세계에서 큰 진전을 나타냅니다. 아래 코드 예제는 이미지와 텍스트 프롬프트를 모두 사용하여 Llama 3.2 90B로부터 이미지 분석을 얻습니다.

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

이 강의를 완료한 후, [생성 AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상하세요!

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.