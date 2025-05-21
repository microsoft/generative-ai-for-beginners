<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:53:28+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ko"
}
-->
# Mistral 모델로 빌드하기

## 소개

이 강의에서는 다음 내용을 다룹니다:
- 다양한 Mistral 모델 탐색
- 각 모델의 사용 사례 및 시나리오 이해
- 각 모델의 독특한 기능을 보여주는 코드 샘플

## Mistral 모델

이 강의에서는 3가지 다른 Mistral 모델을 탐색합니다: **Mistral Large**, **Mistral Small** 및 **Mistral Nemo**.

이 모델들은 모두 Github Model 마켓플레이스에서 무료로 제공됩니다. 이 노트북의 코드는 이 모델들을 사용하여 실행됩니다. Github Models를 사용하여 [AI 모델로 프로토타입 제작](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)에 대한 자세한 내용은 여기를 참조하세요.

## Mistral Large 2 (2407)
Mistral Large 2는 현재 Mistral의 주력 모델로, 기업용으로 설계되었습니다.

이 모델은 원래 Mistral Large의 업그레이드 버전으로 다음을 제공합니다:
- 더 큰 컨텍스트 윈도우 - 128k vs 32k
- 수학 및 코딩 작업에서의 향상된 성능 - 평균 정확도 76.9% vs 60.4%
- 다국어 성능 향상 - 포함 언어: 영어, 프랑스어, 독일어, 스페인어, 이탈리아어, 포르투갈어, 네덜란드어, 러시아어, 중국어, 일본어, 한국어, 아랍어, 힌디어.

이러한 기능 덕분에 Mistral Large는 다음에서 뛰어납니다:
- *Retrieval Augmented Generation (RAG)* - 더 큰 컨텍스트 윈도우 덕분에
- *함수 호출* - 이 모델은 외부 도구 및 API와의 통합을 허용하는 기본 함수 호출을 지원합니다. 이러한 호출은 병렬로 또는 순차적으로 하나씩 수행될 수 있습니다.
- *코드 생성* - 이 모델은 Python, Java, TypeScript 및 C++ 생성에서 뛰어납니다.

### Mistral Large 2를 사용한 RAG 예제

이 예제에서는 Mistral Large 2를 사용하여 텍스트 문서에 대해 RAG 패턴을 실행합니다. 질문은 한국어로 작성되었으며, 저자의 대학 입학 전 활동에 대해 묻습니다.

이 샘플에서는 Cohere Embeddings Model을 사용하여 텍스트 문서 및 질문의 임베딩을 생성합니다. 이 샘플에서는 faiss Python 패키지를 벡터 저장소로 사용합니다.

Mistral 모델에 보내진 프롬프트에는 질문과 질문과 유사한 검색된 청크가 포함됩니다. 모델은 자연어 응답을 제공합니다.

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
Mistral Small은 Mistral 모델군의 또 다른 모델로, 프리미어/기업 카테고리에 속합니다. 이름에서 알 수 있듯이, 이 모델은 Small Language Model (SLM)입니다. Mistral Small을 사용하는 이점은 다음과 같습니다:
- Mistral Large 및 NeMo와 같은 Mistral LLM에 비해 비용 절감 - 80% 가격 인하
- 낮은 대기 시간 - Mistral의 LLM에 비해 빠른 응답
- 유연성 - 필요한 자원에 대한 제한이 적어 다양한 환경에서 배포 가능

Mistral Small은 다음에 적합합니다:
- 요약, 감정 분석 및 번역과 같은 텍스트 기반 작업
- 비용 효율성 때문에 빈번한 요청이 발생하는 애플리케이션
- 코드 검토 및 코드 제안과 같은 낮은 대기 시간의 코드 작업

## Mistral Small과 Mistral Large 비교

Mistral Small과 Large의 대기 시간 차이를 보여주기 위해 아래 셀을 실행하세요.

3-5초의 응답 시간 차이를 볼 수 있습니다. 동일한 프롬프트에 대한 응답 길이와 스타일도 주목하세요.

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

이 강의에서 논의된 다른 두 모델과 비교할 때, Mistral NeMo는 Apache2 라이선스를 가진 유일한 무료 모델입니다.

이 모델은 이전 오픈 소스 LLM인 Mistral 7B의 업그레이드로 간주됩니다.

NeMo 모델의 다른 기능은 다음과 같습니다:

- *더 효율적인 토큰화:* 이 모델은 일반적으로 사용되는 tiktoken 대신 Tekken 토크나이저를 사용합니다. 이를 통해 더 많은 언어와 코드에서 더 나은 성능을 제공합니다.

- *파인튜닝:* 기본 모델은 파인튜닝이 가능합니다. 이는 파인튜닝이 필요할 수 있는 사용 사례에 대해 더 큰 유연성을 제공합니다.

- *기본 함수 호출* - Mistral Large와 마찬가지로 이 모델은 함수 호출에 대해 훈련되었습니다. 이는 오픈 소스 모델 중 처음으로 이를 수행하는 독특한 모델로 만듭니다.

### 토크나이저 비교

이 샘플에서는 Mistral NeMo가 Mistral Large와 비교하여 토큰화를 처리하는 방법을 살펴봅니다.

두 샘플 모두 동일한 프롬프트를 사용하지만, NeMo가 Mistral Large보다 적은 토큰을 반환하는 것을 볼 수 있습니다.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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

# Count the number of tokens
print(len(tokens))
```

## 학습은 여기서 멈추지 않습니다. 여정을 계속하세요

이 강의를 완료한 후, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성적 AI 지식을 계속 향상시키세요!

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임지지 않습니다.