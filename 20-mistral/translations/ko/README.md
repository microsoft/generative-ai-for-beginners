# Mistral 모델로 빌드하기

## 소개

이 레슨에서는 다음의 내용을 다룹니다:
- 다양한 Mistral 모델 탐색
- 각 모델의 사용 사례와 시나리오 이해
- 각 모델의 고유한 기능을 보여주는 코드 예제

## Mistral 모델들
이 레슨에서는 **Mistral Large**, **Mistral Small**, 그리고 **Mistral Nemo**라는 세 가지 Mistral 모델을 살펴보겠습니다.

세 모델 모두 Github Model 마켓플레이스에서 무료로 이용 가능합니다. 현 레슨에서는 이 세 모델들을 사용하여 코드를 실행할 예정입니다. Github Models를 사용하여 AI 모델로 프로토타입 제작에 대한 자세한 내용은 [여기에서 확인할 수 있습니다.](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 

## Mistral Large 2 (2407)
Mistral Large 2는 현재 Mistral의 대표 모델로, 기업용으로 설계되었습니다. 

이 모델은 기존 Mistral Large 모델을 업그레이드한 것으로, 다음과 같은 개선 사항이 있습니다. 

- 더 큰 context window - 32k에서 128k로 확대
- 더 나아진 수학 및 코딩 작성 성능 - 평균 정확도가 60.4%에서 76.9%로 증가
- 더 향상된 다국어 성능 - 지원 언어에는 영어, 프랑스어, 독일어, 스페인어, 이탈리아어, 포르투갈어, 네덜란드어, 러시아어, 중국어, 일본어, 한국어, 아랍어, 힌디어가 포함

이러한 기능을 통해 Mistral Large는 다음과 같은 분야에 적합합니다: 
- *검색 증강 생성(Retrieval Augmented Generation, RAG)* - 넓어진 context window 덕분에 더 나은 성능 발휘
- *함수 호출(Function Calling)* - 외부 도구와 API와의 통합을 가능하게 하는 네이티브 함수 호출 기능 제공. 해당 호출을 병렬 또는 순차적인 순서로 차례대로 수행 가능.
- *코드 생성(Code Generation)* - Python, Java, TypeScript, C++ 코드를 생성하는 데 우수한 성능을 발휘

### Mistral Large 2을 사용한 RAG 예제 

이 예제에서는 Mistral Large 2를 사용해 텍스트 문서에 대한 RAG 패턴을 실행합니다. 질문은 한국어로 작성되었으며, 저자가 대학에 들어가기 전 했던 활동에 대해 묻고 있습니다. 

Cohere Embeddings Model을 사용해 텍스트와 질문의 임베딩을 생성하며, faiss Python 패키지를 벡터 저장소로 사용합니다.

Mistral 모델에 보내는 프롬프트에는 질문과 유사한 검색 결과 청크들이 포함됩니다. 모델은 이 정보에 기반해 자연어 응답을 제공합니다. 

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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
Mistral Small은 Mistral 제품군 내의 프리미어/기업용 카테고리에 속한 또 다른 모델입니다. 이름에서 알 수 있듯이 소형 언어 모델(SLM)이죠. Mistral Small은 다음과 같은 장점이 있습니다:
- 비용 절감 - Mistral Large와 NeMo같은 Mistral LLMs에 비해 80% 비용 절감
- 짧은 지연 시간 - Mistral LLM에 비해 빠른 응답 속도
- 유연성 - 리소스 요구 사항이 적어 다양한 환경에서 배포 가능


Mistral Small은 다음과 같은 경우에 적합합니다:

- 요약, 감정 분석, 번역 등 텍스트 기반 작업
- 비용 효율성으로 인해 자주 요청이 필요한 애플리케이션
- 즉각적인 응답이 필요한 코드 검토, 코드 제안 등의 작업

## Mistral Small과 Mistral Large 비교
아래 코드 셀을 실행하여 Mistral Small과 Large의 응답 시간 차이를 비교해보겠습니다. 

실행해보면 동일한 프롬프트에 대해 3-5초 정도의 응답 시간 차이를 확인할 수 있으며, 응답 길이와 스타일 차이도 살펴볼 수 있습니다.

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
이 레슨에서 다루는 다른 두 모델과 비교하여 Mistral NeMo는 Apache2 라이선스를 가진 유일한 무료 모델입니다. 

NeMo는 Mistral의 이전 오픈 소스 LLM인 Mistral 7B의 업그레이드된 모델로 볼 수 있습니다. 

NeMo 모델의 특징은 다음과 같습니다:

- *더 효율적인 토큰화* - tiktoken 대신 Tekken tokenizer를 사용해 더 많은 언어와 코드에서 더 나은 성능 발휘

- *파인튜닝* - 기본 모델은 파인튜닝이 가능하여, 파인튜닝이 필요한 사용 사례에 더 유연하게 활용할 수 있음

- *네이티브 함수 호출* - Mistral Large처럼 function calling에 대한 학습이 되어 있음. 오픈 소스 모델로서는 최초로 이 기능을 갖추었다는 점이 독특함


## Tokenizer 비교

다음 샘플에서는 Mistral NeMo가 Mistral Large와 비교하여 어떻게 tokenization을 처리하는지 살펴봅니다. 

두 샘플 모두 동일한 프롬프트를 사용하지만, NeMo가 Mistral Large보다 적은 수의 토큰을 반환하는 것을 확인할 수 있습니다.

```bash
pip install mistral-common
```

```python 
# 필요한 패키지 임포트:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral 토크나이저 로드

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# 메시지 목록 토큰화
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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
# 필요한 패키지 임포트:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral 토크나이저 로드

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 메시지 목록 토큰화
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

## 여기서 멈추지 말고, 더 깊이 탐구해 보세요

이 레슨을 마쳤다면, [생성형 AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)에서 더 많은 내용을 확인하며 생성형 AI 지식을 한 단계 더 높여보세요!
