<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:07:45+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ko"
}
-->
# Meta 패밀리 모델로 빌드하기

## 소개

이번 수업에서는 다음 내용을 다룹니다:

- Meta 패밀리의 주요 모델 두 가지 - Llama 3.1과 Llama 3.2 탐색
- 각 모델의 사용 사례와 적용 시나리오 이해
- 각 모델의 고유 기능을 보여주는 코드 예제

## Meta 패밀리 모델

이번 수업에서는 Meta 패밀리 또는 "Llama Herd"의 두 모델인 Llama 3.1과 Llama 3.2를 살펴봅니다.

이 모델들은 다양한 변형으로 제공되며 GitHub Model 마켓플레이스에서 이용할 수 있습니다. GitHub Models를 사용해 [AI 모델 프로토타이핑](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)하는 방법에 대한 자세한 내용도 확인해 보세요.

모델 변형:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*참고: Llama 3도 GitHub Models에서 제공되지만 이번 수업에서는 다루지 않습니다*

## Llama 3.1

4050억 개의 파라미터를 가진 Llama 3.1은 오픈 소스 LLM 범주에 속합니다.

이 모델은 이전 버전인 Llama 3에서 다음과 같이 업그레이드되었습니다:

- 더 큰 컨텍스트 윈도우 - 8천 토큰에서 12만 8천 토큰으로 확대
- 최대 출력 토큰 수 증가 - 2048에서 4096으로
- 향상된 다국어 지원 - 훈련 토큰 수 증가 덕분에

이로 인해 Llama 3.1은 다음과 같은 복잡한 GenAI 애플리케이션 구축에 적합합니다:
- 네이티브 함수 호출 - LLM 워크플로우 외부의 외부 도구 및 함수 호출 가능
- 향상된 RAG 성능 - 더 큰 컨텍스트 윈도우 덕분에
- 합성 데이터 생성 - 미세 조정 같은 작업에 효과적인 데이터 생성 가능

### 네이티브 함수 호출

Llama 3.1은 함수나 도구 호출을 더 효과적으로 수행하도록 미세 조정되었습니다. 또한, 사용자 프롬프트에 따라 사용해야 할 도구를 모델이 인식할 수 있는 두 가지 내장 도구가 있습니다.

이 도구들은 다음과 같습니다:

- **Brave Search** - 웹 검색을 통해 최신 정보(예: 날씨)를 얻을 수 있음
- **Wolfram Alpha** - 복잡한 수학 계산에 사용 가능하며, 직접 함수를 작성할 필요 없음

사용자가 직접 LLM이 호출할 수 있는 맞춤 도구를 만들 수도 있습니다.

아래 코드 예제에서는:

- 시스템 프롬프트에 사용 가능한 도구들(brave_search, wolfram_alpha)을 정의합니다.
- 특정 도시의 날씨를 묻는 사용자 프롬프트를 보냅니다.
- LLM은 Brave Search 도구 호출로 응답하며, 다음과 같이 나타납니다: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*참고: 이 예제는 도구 호출만 수행하며, 결과를 얻으려면 Brave API 페이지에서 무료 계정을 만들고 함수를 직접 정의해야 합니다*

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

LLM임에도 불구하고 Llama 3.1의 한계 중 하나는 멀티모달 지원입니다. 즉, 이미지 같은 다양한 입력 유형을 프롬프트로 사용하고 응답할 수 있는 능력입니다. 이 기능이 Llama 3.2의 주요 특징 중 하나입니다. 그 외 특징은 다음과 같습니다:

- 멀티모달 지원 - 텍스트와 이미지 프롬프트 모두 평가 가능
- 소형에서 중형 크기 변형(11B 및 90B) - 유연한 배포 옵션 제공
- 텍스트 전용 변형(1B 및 3B) - 엣지/모바일 기기에서 배포 가능하며 낮은 지연 시간 제공

멀티모달 지원은 오픈 소스 모델 세계에서 큰 도약을 의미합니다. 아래 코드 예제는 이미지와 텍스트 프롬프트를 모두 사용해 Llama 3.2 90B로 이미지 분석을 수행합니다.

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

## 학습은 여기서 끝나지 않습니다, 여정을 계속하세요

이번 수업을 마친 후에는 [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성형 AI 지식을 계속해서 향상시키세요!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.