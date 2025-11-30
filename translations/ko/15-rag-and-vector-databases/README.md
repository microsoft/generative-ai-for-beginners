<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-18T00:02:41+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "ko"
}
-->
# 검색 증강 생성(RAG) 및 벡터 데이터베이스

[![검색 증강 생성(RAG) 및 벡터 데이터베이스](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.ko.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

검색 애플리케이션 수업에서 우리는 대형 언어 모델(LLM)에 자신의 데이터를 통합하는 방법에 대해 간략히 배웠습니다. 이번 수업에서는 LLM 애플리케이션에서 데이터를 기반으로 하는 개념, 프로세스의 메커니즘, 임베딩 및 텍스트를 포함한 데이터를 저장하는 방법에 대해 더 깊이 탐구할 것입니다.

> **비디오 곧 공개 예정**

## 소개

이번 수업에서는 다음 내용을 다룹니다:

- RAG에 대한 소개, 그것이 무엇인지, 그리고 AI(인공지능)에서 왜 사용되는지.

- 벡터 데이터베이스가 무엇인지 이해하고 애플리케이션을 위한 벡터 데이터베이스를 생성하기.

- RAG를 애플리케이션에 통합하는 실용적인 예제.

## 학습 목표

이 수업을 완료한 후, 여러분은 다음을 할 수 있습니다:

- 데이터 검색 및 처리에서 RAG의 중요성을 설명할 수 있습니다.

- RAG 애플리케이션을 설정하고 데이터를 LLM에 기반화할 수 있습니다.

- LLM 애플리케이션에서 RAG와 벡터 데이터베이스를 효과적으로 통합할 수 있습니다.

## 우리의 시나리오: LLM을 자체 데이터로 강화하기

이번 수업에서는 교육 스타트업에 자신의 노트를 추가하여 챗봇이 다양한 주제에 대한 정보를 더 많이 얻을 수 있도록 하고자 합니다. 우리가 가진 노트를 사용하면 학습자들이 더 잘 공부하고 다양한 주제를 이해하여 시험 준비를 더 쉽게 할 수 있습니다. 시나리오를 만들기 위해 다음을 사용할 것입니다:

- `Azure OpenAI:` 챗봇을 생성하기 위해 사용할 LLM

- `AI 초보자를 위한 신경망 수업:` LLM을 기반으로 할 데이터

- `Azure AI Search` 및 `Azure Cosmos DB:` 데이터를 저장하고 검색 인덱스를 생성하기 위한 벡터 데이터베이스

사용자는 자신의 노트에서 연습 퀴즈를 생성하고, 복습 플래시 카드를 만들며, 간결한 개요로 요약할 수 있습니다. 시작하기 위해 RAG가 무엇이며 어떻게 작동하는지 살펴보겠습니다:

## 검색 증강 생성(RAG)

LLM 기반 챗봇은 사용자 프롬프트를 처리하여 응답을 생성합니다. 이는 상호작용을 위해 설계되었으며 다양한 주제에 대해 사용자와 소통합니다. 그러나 응답은 제공된 컨텍스트와 기본 교육 데이터에 제한됩니다. 예를 들어, GPT-4의 지식 컷오프는 2021년 9월로, 이 시점 이후에 발생한 이벤트에 대한 지식이 부족합니다. 또한, LLM을 훈련하는 데 사용된 데이터는 개인 노트나 회사의 제품 매뉴얼과 같은 기밀 정보를 제외합니다.

### RAG(검색 증강 생성)의 작동 방식

![RAG의 작동 방식을 보여주는 그림](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.ko.png)

예를 들어, 자신의 노트에서 퀴즈를 생성하는 챗봇을 배포하려면 지식 베이스와의 연결이 필요합니다. 이때 RAG가 구원에 나섭니다. RAG는 다음과 같이 작동합니다:

- **지식 베이스:** 검색 전에 이러한 문서를 수집하고 전처리해야 하며, 일반적으로 큰 문서를 작은 조각으로 나누고 텍스트 임베딩으로 변환한 후 데이터베이스에 저장합니다.

- **사용자 쿼리:** 사용자가 질문을 합니다.

- **검색:** 사용자가 질문을 하면 임베딩 모델이 지식 베이스에서 관련 정보를 검색하여 프롬프트에 통합될 추가 컨텍스트를 제공합니다.

- **증강 생성:** LLM은 검색된 데이터를 기반으로 응답을 향상시킵니다. 이는 사전 훈련된 데이터뿐만 아니라 추가된 컨텍스트에서 관련 정보를 기반으로 응답을 생성할 수 있게 합니다. 검색된 데이터는 LLM의 응답을 증강하는 데 사용됩니다. 이후 LLM은 사용자의 질문에 대한 답변을 반환합니다.

![RAG의 아키텍처를 보여주는 그림](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.ko.png)

RAG의 아키텍처는 인코더와 디코더로 구성된 트랜스포머를 사용하여 구현됩니다. 예를 들어, 사용자가 질문을 하면 입력 텍스트가 단어의 의미를 캡처하는 벡터로 '인코딩'되고, 벡터는 문서 인덱스로 '디코딩'되어 사용자 쿼리에 따라 새 텍스트를 생성합니다. LLM은 인코더-디코더 모델을 사용하여 출력을 생성합니다.

[RAG를 활용한 지식 집약적 NLP(자연어 처리 소프트웨어) 작업을 위한 검색 증강 생성](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) 논문에 따르면 RAG를 구현할 때 두 가지 접근 방식이 있습니다:

- **_RAG-Sequence_** 검색된 문서를 사용하여 사용자 쿼리에 대한 최적의 답변을 예측합니다.

- **RAG-Token** 문서를 사용하여 다음 토큰을 생성한 후 이를 검색하여 사용자의 쿼리에 답변합니다.

### RAG를 사용하는 이유는 무엇인가요?

- **정보 풍부성:** 텍스트 응답이 최신 상태를 유지하고 최신 정보를 제공할 수 있습니다. 따라서 내부 지식 베이스에 액세스하여 도메인별 작업 성능을 향상시킵니다.

- **허위 정보 감소:** 지식 베이스의 **검증 가능한 데이터**를 활용하여 사용자 쿼리에 대한 컨텍스트를 제공합니다.

- **비용 효율성:** LLM을 세부 조정하는 것보다 경제적입니다.

## 지식 베이스 생성

우리의 애플리케이션은 개인 데이터, 즉 AI 초보자를 위한 신경망 수업 커리큘럼을 기반으로 합니다.

### 벡터 데이터베이스

벡터 데이터베이스는 기존 데이터베이스와 달리 임베딩 벡터를 저장, 관리 및 검색하도록 설계된 특수 데이터베이스입니다. 이는 문서의 수치 표현을 저장합니다. 데이터를 수치 임베딩으로 분해하면 AI 시스템이 데이터를 더 쉽게 이해하고 처리할 수 있습니다.

LLM은 입력으로 허용하는 토큰 수에 제한이 있기 때문에 임베딩을 벡터 데이터베이스에 저장합니다. 전체 임베딩을 LLM에 전달할 수 없으므로 이를 작은 조각으로 나누어야 하며, 사용자가 질문을 하면 질문과 가장 유사한 임베딩이 프롬프트와 함께 반환됩니다. 조각화는 LLM을 통과하는 토큰 수를 줄여 비용을 절감합니다.

Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant, DeepLake와 같은 인기 있는 벡터 데이터베이스가 있습니다. Azure CLI를 사용하여 Azure Cosmos DB 모델을 생성하려면 다음 명령을 사용할 수 있습니다:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 텍스트에서 임베딩으로

데이터를 저장하기 전에 이를 벡터 임베딩으로 변환해야 합니다. 대형 문서나 긴 텍스트를 다룰 경우 예상되는 쿼리를 기준으로 이를 조각화할 수 있습니다. 조각화는 문장 수준 또는 단락 수준에서 수행할 수 있습니다. 조각화는 주변 단어에서 의미를 도출하므로 문서 제목을 추가하거나 조각 앞뒤에 일부 텍스트를 포함하여 조각에 다른 컨텍스트를 추가할 수 있습니다. 데이터를 다음과 같이 조각화할 수 있습니다:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

조각화된 후에는 다양한 임베딩 모델을 사용하여 텍스트를 임베딩할 수 있습니다. 사용할 수 있는 모델로는 word2vec, OpenAI의 ada-002, Azure Computer Vision 등이 있습니다. 사용할 모델을 선택할 때 사용하는 언어, 인코딩된 콘텐츠 유형(텍스트/이미지/오디오), 인코딩할 수 있는 입력 크기 및 임베딩 출력 길이를 고려해야 합니다.

OpenAI의 `text-embedding-ada-002` 모델을 사용한 텍스트 임베딩 예는 다음과 같습니다:
![단어 cat의 임베딩](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.ko.png)

## 검색 및 벡터 검색

사용자가 질문을 하면 검색기가 쿼리 인코더를 사용하여 이를 벡터로 변환한 후, 문서 검색 인덱스를 통해 입력과 관련된 벡터를 검색합니다. 완료되면 입력 벡터와 문서 벡터를 텍스트로 변환하여 LLM에 전달합니다.

### 검색

검색은 시스템이 검색 기준을 충족하는 문서를 인덱스에서 빠르게 찾으려고 할 때 발생합니다. 검색기의 목표는 문서를 가져와 컨텍스트를 제공하고 LLM을 데이터에 기반화하는 것입니다.

데이터베이스 내에서 검색을 수행하는 여러 방법이 있습니다:

- **키워드 검색** - 텍스트 검색에 사용됩니다.

- **시맨틱 검색** - 단어의 시맨틱 의미를 사용합니다.

- **벡터 검색** - 문서를 텍스트에서 임베딩 모델을 사용하여 벡터 표현으로 변환합니다. 검색은 사용자 질문과 가장 가까운 벡터 표현을 가진 문서를 쿼리하여 수행됩니다.

- **하이브리드** - 키워드 검색과 벡터 검색을 결합한 방식입니다.

검색에서 유사한 응답이 데이터베이스에 없을 경우 시스템은 가능한 최상의 정보를 반환합니다. 그러나 관련성에 대한 최대 거리를 설정하거나 키워드와 벡터 검색을 결합한 하이브리드 검색을 사용하는 등의 전략을 사용할 수 있습니다. 이번 수업에서는 키워드 검색과 벡터 검색을 결합한 하이브리드 검색을 사용합니다. 데이터를 조각과 임베딩을 포함하는 열이 있는 데이터 프레임에 저장합니다.

### 벡터 유사도

검색기는 지식 데이터베이스를 통해 가까운 임베딩을 검색하며, 가장 가까운 이웃은 유사한 텍스트입니다. 사용자가 쿼리를 요청하면 먼저 임베딩되고 유사한 임베딩과 일치합니다. 서로 다른 벡터가 얼마나 유사한지 찾는 데 일반적으로 사용되는 측정 방법은 코사인 유사도로, 두 벡터 간의 각도를 기반으로 합니다.

유사도를 측정하는 다른 대안으로는 벡터 끝점 간의 직선 거리인 유클리드 거리와 두 벡터의 대응 요소의 곱의 합을 측정하는 내적이 있습니다.

### 검색 인덱스

검색을 수행할 때 검색을 수행하기 전에 지식 베이스에 대한 검색 인덱스를 구축해야 합니다. 인덱스는 임베딩을 저장하며 대규모 데이터베이스에서도 가장 유사한 조각을 빠르게 검색할 수 있습니다. 로컬에서 인덱스를 생성하려면 다음을 사용할 수 있습니다:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 재랭킹

데이터베이스를 쿼리한 후 가장 관련성이 높은 결과를 정렬해야 할 수 있습니다. 재랭킹 LLM은 검색 결과의 관련성을 개선하기 위해 머신 러닝을 활용하여 이를 가장 관련성이 높은 순서로 정렬합니다. Azure AI Search를 사용하면 시맨틱 재랭커를 통해 자동으로 재랭킹이 수행됩니다. 가장 가까운 이웃을 사용한 재랭킹 작동 예는 다음과 같습니다:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 모든 것을 통합하기

마지막 단계는 데이터를 기반으로 한 응답을 얻을 수 있도록 LLM을 추가하는 것입니다. 이를 다음과 같이 구현할 수 있습니다:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## 애플리케이션 평가

### 평가 지표

- 자연스럽고 유창하며 인간다운 응답 품질

- 데이터 기반성: 제공된 문서에서 나온 응답인지 평가

- 관련성: 응답이 질문과 일치하고 관련성이 있는지 평가

- 유창성: 응답이 문법적으로 의미가 있는지 평가

## RAG(검색 증강 생성) 및 벡터 데이터베이스 사용 사례

함수 호출이 앱을 개선할 수 있는 다양한 사용 사례가 있습니다:

- 질문 및 답변: 회사 데이터를 기반으로 직원들이 질문할 수 있는 채팅 생성.

- 추천 시스템: 영화, 레스토랑 등 가장 유사한 값을 매칭하는 시스템 생성.

- 챗봇 서비스: 채팅 기록을 저장하고 사용자 데이터를 기반으로 대화를 개인화.

- 벡터 임베딩을 기반으로 한 이미지 검색, 이미지 인식 및 이상 탐지에 유용.

## 요약

이번 수업에서는 애플리케이션에 데이터를 추가하는 것부터 사용자 쿼리 및 출력까지 RAG의 기본 영역을 다루었습니다. RAG를 간단히 생성하려면 Semanti Kernel, Langchain 또는 Autogen과 같은 프레임워크를 사용할 수 있습니다.

## 과제

검색 증강 생성(RAG)에 대한 학습을 계속하기 위해 다음을 구축할 수 있습니다:

- 원하는 프레임워크를 사용하여 애플리케이션의 프론트엔드 구축

- LangChain 또는 Semantic Kernel 프레임워크를 사용하여 애플리케이션 재구성.

수업을 완료한 것을 축하합니다 👏.

## 학습은 여기서 멈추지 않습니다, 여정을 계속하세요

이 수업을 완료한 후, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상시키세요!

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 책임을 지지 않습니다.