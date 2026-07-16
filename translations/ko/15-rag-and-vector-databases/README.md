# 검색 보강 생성(RAG) 및 벡터 데이터베이스

[![검색 보강 생성(RAG) 및 벡터 데이터베이스](../../../translated_images/ko/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

검색 애플리케이션 수업에서 자체 데이터를 대형 언어 모델(LLM)에 통합하는 방법을 간단히 배웠습니다. 이번 수업에서는 LLM 애플리케이션에서 데이터를 기반으로 하는 개념, 프로세스의 메커니즘, 임베딩과 텍스트 모두를 포함하는 데이터 저장 방법에 대해 더 자세히 살펴보겠습니다.

> **비디오 곧 제공 예정**

## 소개

이번 수업에서는 다음 내용을 다룹니다:

- RAG에 대한 소개, 이것이 무엇인지 그리고 인공지능(AI)에서 왜 사용되는지.

- 벡터 데이터베이스가 무엇인지 이해하고 애플리케이션을 위한 벡터 데이터베이스 생성.

- RAG를 애플리케이션에 통합하는 실용적인 예제.

## 학습 목표

이 수업을 완료하면 다음을 할 수 있습니다:

- 데이터 검색 및 처리에서 RAG의 중요성을 설명할 수 있습니다.

- RAG 애플리케이션을 설정하고 데이터를 LLM에 기반할 수 있습니다.

- LLM 애플리케이션에서 RAG와 벡터 데이터베이스를 효과적으로 통합할 수 있습니다.

## 시나리오: 자체 데이터로 LLM 향상하기

이번 수업에서는 교육 스타트업에 자체 노트를 추가하여 챗봇이 다양한 주제에 대해 더 많은 정보를 얻을 수 있도록 하려 합니다. 보유한 노트를 사용하면 학습자가 더 잘 학습하고 다양한 주제를 이해하여 시험 준비가 더 쉬워집니다. 시나리오를 만들기 위해 다음을 사용합니다:

- `Azure OpenAI:` 챗봇을 만들기 위해 사용할 LLM

- `AI for beginners' 수업의 신경망`: LLM에 기반할 데이터

- `Azure AI Search` 및 `Azure Cosmos DB:` 데이터를 저장하고 검색 인덱스를 생성하기 위한 벡터 데이터베이스

사용자는 노트에서 연습 퀴즈를 만들고, 복습용 플래시카드를 생성하며, 간결한 개요로 요약할 수 있습니다. 시작하기 위해 RAG가 무엇이고 어떻게 작동하는지 살펴봅시다:

## 검색 보강 생성(Retrieval Augmented Generation, RAG)

LLM 기반 챗봇은 사용자 프롬프트를 처리하여 응답을 생성합니다. 광범위한 주제에 대해 상호작용할 수 있도록 설계되었으나, 그 응답은 제공된 컨텍스트 및 기초 훈련 데이터에 한정됩니다. 예를 들어, GPT-4의 지식 컷오프는 2021년 9월로, 이 이후 발생한 사건에 대한 지식이 부족합니다. 또한 LLM 학습에 사용되는 데이터에는 개인 노트나 회사 제품 매뉴얼 같은 비밀 정보는 포함되지 않습니다.

### RAG(검색 보강 생성)이 작동하는 방식

![RAG 작동 방식 도식](../../../translated_images/ko/how-rag-works.f5d0ff63942bd3a6.webp)

예를 들어 노트에서 퀴즈를 생성하는 챗봇을 배포하고자 할 때, 지식 베이스와 연결이 필요합니다. 이때 RAG가 도움을 줍니다. RAG의 작동 방식은 다음과 같습니다:

- **지식 베이스:** 검색 전에 문서는 수집되고 전처리되어야 하며, 보통 큰 문서를 작은 청크로 나누고, 텍스트 임베딩으로 변환한 후 데이터베이스에 저장합니다.

- **사용자 질문:** 사용자가 질문을 합니다.

- **검색:** 사용자가 질문하면 임베딩 모델이 지식 베이스에서 관련 정보를 검색하여 프롬프트에 포함할 더 많은 문맥을 제공합니다.

- **보강 생성:** LLM은 검색된 데이터를 기반으로 응답을 향상시킵니다. 이를 통해 사전 학습 데이터뿐만 아니라 추가된 문맥의 관련 정보를 활용하여 응답을 생성할 수 있습니다. 그런 다음 LLM은 사용자 질문에 대한 답변을 반환합니다.

![RAG 아키텍처 도식](../../../translated_images/ko/encoder-decode.f2658c25d0eadee2.webp)

RAG 아키텍처는 인코더와 디코더 두 부분으로 구성된 트랜스포머를 사용하여 구현됩니다. 예를 들어, 사용자가 질문하면 입력 텍스트가 단어의 의미를 담은 벡터로 '인코딩'되고, 이 벡터는 문서 인덱스로 '디코딩'되어 사용자의 쿼리에 기반한 새 텍스트를 생성합니다. LLM은 인코더-디코더 모델을 사용하여 출력을 생성합니다.

제안된 논문 [Knowledge intensive NLP 작업을 위한 검색 보강 생성(Retrieval-Augmented Generation)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)에 따르면 RAG 구현에 두 가지 접근법이 있습니다:

- **_RAG-Sequence_**: 검색된 문서를 사용해 사용자 질문에 최적의 답변을 예측

- **RAG-Token**: 문서를 사용해 다음 토큰을 생성하고, 이를 반복하여 사용자 질문에 답변

### 왜 RAG를 사용하는가?

- **정보의 풍부함:** 최신 텍스트 응답을 보장합니다. 따라서 도메인 특정 작업에서 내부 지식 베이스에 접근하여 성능을 향상시킵니다.

- 데이터베이스에 저장된 <strong>검증 가능한 데이터</strong>를 활용하여 허구적 정보 생성을 줄입니다.

- LLM을 미세 조정하는 것보다 <strong>비용 효과적</strong>입니다.

## 지식 베이스 생성

애플리케이션은 AI For Beginners 교육 과정의 신경망 수업에 대한 개인 데이터에 기반합니다.

### 벡터 데이터베이스

벡터 데이터베이스는 전통적인 데이터베이스와 달리 임베딩된 벡터를 저장, 관리, 검색하도록 설계된 특수 데이터베이스입니다. 문서의 수치적 표현을 저장합니다. 데이터를 수치 임베딩으로 분해하면 AI 시스템이 데이터를 더 쉽게 이해하고 처리할 수 있습니다.

임베딩을 벡터 데이터베이스에 저장하는 이유는 LLM이 입력으로 허용하는 토큰 수에 제한이 있기 때문입니다. 모든 임베딩을 LLM에 전달할 수 없으므로 청크로 나누고 사용자가 질문할 때 질문과 가장 유사한 임베딩을 프롬프트와 함께 반환합니다. 청크 분할은 LLM을 통과하는 토큰 수를 줄여 비용도 절감합니다.

인기 있는 벡터 데이터베이스로는 Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant, DeepLake 등이 있습니다. 다음 명령어로 Azure CLI에서 Azure Cosmos DB 모델을 생성할 수 있습니다:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 텍스트를 임베딩으로 변환하기

데이터를 저장하기 전에 임베딩 벡터로 변환해야 합니다. 대규모 문서나 긴 텍스트를 다룰 경우 예상 질문에 따라 청크로 나눌 수 있습니다. 청크 분할은 문장 단위 또는 단락 단위로 할 수 있습니다. 청크는 주변 단어에서 의미를 추출하므로 문서 제목이나 청크 앞뒤 텍스트를 첨부해 컨텍스트를 더할 수 있습니다. 다음과 같이 데이터를 청크할 수 있습니다:

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

    # 마지막 청크가 최소 길이에 도달하지 못했더라도 어쨌든 추가하세요
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

청크 분할 후, 다양한 임베딩 모델을 사용해 텍스트를 임베딩할 수 있습니다. 사용할 수 있는 모델에는 word2vec, OpenAI의 ada-002, Azure Computer Vision 등이 있습니다. 모델 선택은 사용하는 언어, 인코딩하는 콘텐츠 유형(텍스트/이미지/오디오), 인코딩 가능한 입력 크기, 임베딩 출력 길이에 따라 다릅니다.

OpenAI의 `text-embedding-ada-002` 모델을 사용한 임베딩 텍스트 예시는 다음과 같습니다:
![cat 단어 임베딩 이미지](../../../translated_images/ko/cat.74cbd7946bc9ca38.webp)

## 검색 및 벡터 검색

사용자가 질문하면 검색기는 쿼리 인코더를 사용해 질문을 임베딩 벡터로 변환하고, 문서 검색 인덱스에서 관련 벡터를 찾아냅니다. 그러고 나서 입력 벡터와 문서 벡터를 텍스트로 변환해 LLM에 전달합니다.

### 검색

검색은 시스템이 인덱스에서 검색 기준에 맞는 문서를 빠르게 찾는 과정입니다. 검색기의 목표는 문서를 찾아 LLM에 문맥을 제공하고 데이터를 기반으로 응답하게 하는 것입니다.

데이터베이스 내 검색 수행 방법으로는 다음과 같은 것들이 있습니다:

- **키워드 검색** - 텍스트 검색용

- **벡터 검색** - 문서를 임베딩 모델로 텍스트에서 벡터 표현으로 변환하고, 단어 의미를 이용한 **의미 검색(semantic search)** 수행. 사용자 질문과 가장 가까운 벡터 문서를 질의함.

- <strong>하이브리드</strong> - 키워드 및 벡터 검색의 조합

검색의 문제점은 데이터베이스에 쿼리와 유사한 답변이 없으면 최선의 정보를 반환한다는 점입니다. 그러나 관련성 최대 거리 설정이나 키워드-벡터 검색 혼합인 하이브리드 검색 등을 이용할 수 있습니다. 이번 수업에서는 벡터 및 키워드 검색을 혼합한 하이브리드 검색을 사용하며, 데이터는 청크와 임베딩을 포함하는 데이터프레임에 저장합니다.

### 벡터 유사도

검색기는 지식 베이스에서 임베딩이 가까운 것, 즉 가장 유사한 이웃을 찾습니다. 사용자 쿼리가 주어지면 먼저 임베딩되고 그와 유사한 임베딩과 매칭됩니다. 벡터 간 유사도 측정 방법으로는 두 벡터 사이 각도를 기반으로 하는 코사인 유사도가 일반적입니다.

그 외 대안으로 유클리드 거리(벡터 끝점 간 직선 거리), 점곱(dot product, 두 벡터 대응 요소 곱의 합)이 있습니다.

### 검색 인덱스

검색 전에 지식 베이스를 위한 검색 인덱스를 구축해야 합니다. 인덱스는 임베딩을 저장하고 큰 데이터베이스에서도 가장 유사한 청크를 빠르게 검색할 수 있습니다. 로컬에서 인덱스를 생성하려면:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 검색 인덱스를 생성합니다
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 인덱스를 조회하려면 kneighbors 메서드를 사용할 수 있습니다
distances, indices = nbrs.kneighbors(embeddings)
```

### 재정렬 (Re-ranking)

검색 결과를 받은 후 가장 관련성 높은 결과 순으로 정렬할 필요가 있을 수 있습니다. 재정렬 LLM은 머신러닝을 이용해 결과를 관련성 순으로 향상시킵니다. Azure AI Search에서는 의미 기반 재정렬기가 자동으로 재정렬을 수행합니다. 최근접 이웃을 사용한 재정렬 예시는 다음과 같습니다:

```python
# 가장 유사한 문서 찾기
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 가장 유사한 문서 출력하기
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 전체 통합

마지막 단계는 LLM을 추가해 데이터에 기반한 응답을 얻는 것입니다. 다음과 같이 구현할 수 있습니다:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 질문을 쿼리 벡터로 변환합니다
    query_vector = create_embeddings(user_input)

    # 가장 유사한 문서를 찾습니다
    distances, indices = nbrs.kneighbors([query_vector])

    # 컨텍스트 제공을 위해 문서를 쿼리에 추가합니다
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 기록과 사용자 입력을 결합합니다
    history.append(user_input)

    # 메시지 객체를 생성합니다
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 응답 API를 사용하여 응답을 생성합니다
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## 애플리케이션 평가

### 평가 지표

- 자연스럽고 유창하며 인간적인 응답 품질 평가

- 기반 데이터성: 응답이 제공된 문서에서 나온 것인지 평가

- 관련성: 응답이 질문과 일치하며 관련이 있는지 평가

- 유창성: 문법적 이해 여부 평가

## RAG(검색 보강 생성)와 벡터 데이터베이스 사용 사례

함수 호출이 애플리케이션을 개선할 수 있는 다양한 사용 사례는 다음과 같습니다:

- 질문과 답변: 회사 데이터를 기반으로 직원이 질문할 수 있는 채팅 구축

- 추천 시스템: 예를 들어 영화, 식당 등과 가장 유사한 값을 매칭하는 시스템 생성

- 챗봇 서비스: 채팅 기록 저장 및 사용자 데이터 기반 대화 개인화

- 벡터 임베딩 기반 이미지 검색: 이미지 인식 및 이상 탐지에 유용

## 요약

RAG의 기본 영역, 즉 애플리케이션에 데이터 추가, 사용자 쿼리 및 출력 과정을 다뤘습니다. RAG 생성 간소화를 위해 Semanti Kernel, Langchain, Autogen 같은 프레임워크를 사용할 수 있습니다.

## 과제

검색 보강 생성(RAG) 학습을 이어가려면 다음을 구축해 보세요:

- 원하는 프레임워크를 사용해 애플리케이션 프론트엔드 구축

- LangChain 또는 Semantic Kernel 등 프레임워크를 이용해 애플리케이션 재구성

수업을 완주하신 것을 축하드립니다 👏.

## 학습은 여기서 멈추지 않습니다, 여정을 계속하세요

수업 완료 후에는 [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 확장하세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->