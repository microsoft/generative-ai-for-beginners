# Meta 패밀리 모델로 구축하기 

## 소개 

이 수업에서는 다음 내용을 다룹니다: 

- 두 가지 주요 Meta 패밀리 모델 - Llama 3.1 및 Llama 3.2 탐구 
- 각 모델의 사용 사례 및 시나리오 이해 
- 각 모델의 고유 기능을 보여주는 코드 샘플 


## Meta 패밀리 모델 

이 수업에서는 Meta 패밀리 또는 "Llama Herd"의 두 모델인 Llama 3.1과 Llama 3.2를 살펴봅니다.

이 모델들은 다양한 변형으로 제공되며, [Microsoft Foundry Models 카탈로그](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)에서 확인할 수 있습니다.

> **참고:** GitHub Models는 2026년 7월 말에 서비스를 종료합니다. AI 모델 프로토타이핑에 대해 더 자세한 내용은 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 사용법을 참고하세요.

모델 변형: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*참고: Llama 3도 Microsoft Foundry Models에서 사용 가능하지만 이 수업에서는 다루지 않습니다*

## Llama 3.1 

4050억 개의 파라미터를 가진 Llama 3.1은 오픈 소스 LLM 범주에 속합니다. 

이 모델은 이전 릴리스인 Llama 3의 업그레이드로 다음을 제공합니다: 

- 더 큰 컨텍스트 윈도우 - 8k 토큰 대비 128k 토큰 
- 더 큰 최대 출력 토큰 - 2048 대비 4096 
- 더 나은 다국어 지원 - 훈련 토큰 증가로 인함 

이는 Llama 3.1이 다음과 같은 복잡한 GenAI 애플리케이션 사용 사례를 처리할 수 있게 합니다: 
- 네이티브 함수 호출 - LLM 워크플로우 외부의 외부 도구와 함수 호출 기능
- 더 나은 RAG 성능 - 더 높은 컨텍스트 윈도우 덕분에 
- 합성 데이터 생성 - 미세 조정과 같은 작업을 위한 효과적인 데이터 생성 능력 

### 네이티브 함수 호출 

Llama 3.1은 함수 또는 도구 호출을 보다 효율적으로 수행하도록 미세 조정되었습니다. 또한 모델은 사용자 프롬프트에 따라 사용해야 할 내장 도구 두 가지를 인식할 수 있습니다. 이 도구들은: 

- **Brave Search** - 웹 검색을 수행해 날씨와 같은 최신 정보를 얻을 수 있음 
- **Wolfram Alpha** - 보다 복잡한 수학 계산에 사용할 수 있어 직접 함수를 작성할 필요 없음 

사용자 정의 도구를 생성하여 LLM이 호출할 수도 있습니다. 

아래 코드 예제에서는: 

- 시스템 프롬프트에 사용 가능한 도구들 (brave_search, wolfram_alpha)을 정의합니다. 
- 특정 도시의 날씨에 대해 묻는 사용자 프롬프트 전송 
- LLM이 Brave Search 도구 호출로 응답하며, 이는 `<|python_tag|>brave_search.call(query="Stockholm weather")`와 같이 보입니다 

*참고: 이 예제는 도구 호출만 수행하며 결과를 얻으려면 Brave API 페이지에서 무료 계정을 생성하고 함수를 직접 정의해야 합니다.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Microsoft Foundry 프로젝트의 "개요" 페이지에서 이것들을 가져옵니다
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Llama 3.1은 LLM임에도 멀티모달 처리 기능이 부족하다는 제한점이 있습니다. 즉, 이미지와 같은 다양한 유형의 입력을 프롬프트로 사용하고 응답을 제공하는 기능이 없습니다. 이 기능은 Llama 3.2의 주요 특징 중 하나입니다. 기타 특징으로는: 

- 멀티모달리티 - 텍스트와 이미지 프롬프트를 모두 평가하는 능력 
- 소형에서 중형 크기 변형 (11B와 90B) - 유연한 배포 옵션 제공 
- 텍스트 전용 변형 (1B와 3B) - 엣지/모바일 장치에서 배포 가능하며 낮은 지연 시간 제공 

멀티모달 지원은 오픈 소스 모델 세계에 큰 진전을 의미합니다. 아래 코드 예제는 이미지와 텍스트 프롬프트를 모두 사용하여 Llama 3.2 90B에서 이미지 분석을 받습니다. 


### Llama 3.2와 멀티모달 지원

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

# Microsoft Foundry 프로젝트의 "개요" 페이지에서 이를 가져오세요
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

이 수업을 완료한 후, 우리의 [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상하세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->