# Mistral 모델로 빌드하기

## 소개

이 수업에서는 다음 내용을 다룹니다:
- 다양한 Mistral 모델 탐색
- 각 모델의 사용 사례 및 시나리오 이해
- 각 모델의 고유 기능을 보여주는 코드 예제 탐색

## Mistral 모델

이 수업에서는 세 가지 Mistral 모델을 탐색합니다:
**Mistral Large**, **Mistral Small**, 그리고 **Mistral Nemo**.

이 모델들은 모두 GitHub Model 마켓플레이스에서 무료로 사용할 수 있습니다. 이 노트북의 코드는 이 모델들을 사용하여 실행됩니다. GitHub 모델을 사용하여 [AI 모델 프로토타입 만들기](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)에 대한 자세한 내용은 여기에서 확인하세요.

## Mistral Large 2 (2407)
Mistral Large 2는 현재 Mistral의 주력 모델이며 기업용으로 설계되었습니다.

이 모델은 기존 Mistral Large의 업그레이드 버전으로,
- 더 큰 컨텍스트 윈도우 - 128k 대 32k
- 수학 및 코딩 작업의 향상된 성능 - 평균 정확도 76.9% 대 60.4%
- 다국어 성능 향상 - 영어, 프랑스어, 독일어, 스페인어, 이탈리아어, 포르투갈어, 네덜란드어, 러시아어, 중국어, 일본어, 한국어, 아랍어, 힌디어 포함

이 기능들로 Mistral Large는 다음에서 뛰어납니다:
- *검색 증강 생성(RAG)* - 더 큰 컨텍스트 윈도우 덕분에
- *함수 호출* - 이 모델은 네이티브 함수 호출을 지원하여 외부 도구 및 API와의 통합이 가능합니다. 이러한 호출은 병렬로 또는 순차적으로 하나씩 호출할 수 있습니다.
- *코드 생성* - 이 모델은 Python, Java, TypeScript, C++ 생성에 뛰어납니다.

### Mistral Large 2를 사용한 RAG 예제

이 예제에서는 Mistral Large 2를 사용하여 텍스트 문서에 RAG 패턴을 실행합니다. 질문은 한국어로 작성되었으며 저자가 대학 입학 전 어떤 활동을 했는지에 대해 묻고 있습니다.

Cohere 임베딩 모델을 사용하여 텍스트 문서와 질문의 임베딩을 생성합니다. 이 샘플에서는 벡터 저장소로 faiss Python 패키지를 사용합니다.

Mistral 모델에 전달되는 프롬프트에는 질문과 질문과 유사한 검색된 청크가 모두 포함됩니다. 모델은 자연어 응답을 제공합니다.

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # 거리, 인덱스
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small
Mistral Small은 프리미어/기업용 범주에 속하는 Mistral 계열의 또 다른 모델입니다. 이름이 암시하듯이, 이 모델은 작은 언어 모델(SLM)입니다. Mistral Small 사용 시 장점은 다음과 같습니다:
- Mistral Large 및 NeMo 같은 Mistral LLM 대비 비용 절감 - 80% 가격 인하
- 낮은 지연 시간 - Mistral의 다른 LLM에 비해 빠른 응답
- 유연성 - 필요한 리소스에 대한 제한이 적어 다양한 환경에 배포 가능

Mistral Small은 다음에 적합합니다:
- 요약, 감정 분석, 번역 같은 텍스트 기반 작업
- 비용 효율성 덕분에 잦은 요청이 발생하는 애플리케이션
- 리뷰 및 코드 제안과 같은 낮은 지연 시간 코드 작업

## Mistral Small과 Mistral Large 비교

Mistral Small과 Large 간의 지연 시간 차이를 보기 위해 아래 셀을 실행하세요.

동일한 프롬프트에 대해 응답 시간 차이가 3-5초 정도임을 확인할 수 있습니다. 또한 응답 길이와 스타일도 참고하세요.

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

이번 수업에서 다룬 다른 두 모델과 비교하여, Mistral NeMo는 Apache2 라이선스를 가진 유일한 무료 모델입니다.

이는 Mistral의 초기 오픈 소스 LLM인 Mistral 7B에 대한 업그레이드로 여겨집니다.

NeMo 모델의 다른 특징은 다음과 같습니다:

- *더 효율적인 토크나이제이션:* 이 모델은 일반적으로 사용되는 tiktoken 대신 Tekken 토크나이저를 사용합니다. 이는 더 많은 언어 및 코드에 대해 더 나은 성능을 제공합니다.

- *파인튜닝:* 기본 모델이 파인튜닝 가능하도록 제공됩니다. 이를 통해 파인튜닝이 필요한 사용 사례에 더 큰 유연성을 제공합니다.

- *네이티브 함수 호출* - Mistral Large처럼 이 모델도 함수 호출 학습이 되어 있습니다. 이는 오픈 소스 모델 중 최초로 이 기능을 지원하는 모델 중 하나로 독특합니다.

### 토크나이저 비교

이 샘플에서는 Mistral NeMo가 Mistral Large와 비교하여 토크나이제이션을 어떻게 처리하는지 살펴봅니다.

두 샘플 모두 동일한 프롬프트를 사용하지만 NeMo가 Mistral Large보다 더 적은 토큰을 반환하는 것을 확인할 수 있습니다.

```bash
pip install mistral-common
```

```python 
# 필요한 패키지 가져오기:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral 토크나이저 불러오기

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# 메시지 목록 토큰화하기
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# 토큰 수 세기
print(len(tokens))
```

```python
# 필요한 패키지 불러오기:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 미스트랄 토크나이저 불러오기

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 메시지 목록 토크나이즈하기
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# 토큰 개수 세기
print(len(tokens))
```

## 학습은 여기서 끝나지 않습니다, 여정을 계속하세요

이 수업을 완료한 후, 우리의 [Generative AI Learning 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속해서 향상시키세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문 인력에 의한 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->