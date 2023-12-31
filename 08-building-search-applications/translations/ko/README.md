# 검색 애플리케이션 만들기

[![Introduction to Generative AI and Large Language Models](../../images/08-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](TBD)

> **비디오 제공 예정**

LLM(대형 언어 모델)은 챗봇과 텍스트 생성 이상의 기능을 가지고 있습니다. Embedding을 사용하여 검색 애플리케이션을 만들 수도 있습니다. Embedding은 데이터의 수치적 표현인 벡터로, 데이터의 의미 기반 검색에 사용할 수 있습니다.

이 레슨에서는 교육 스타트업을 위한 검색 애플리케이션을 만들 것입니다. 우리 스타트업은 개발도상국의 학생들에게 무료 교육을 제공하는 비영리 기관입니다. 우리 스타트업은 학생들이 AI에 대해 배울 수 있는 많은 수의 YouTube 비디오를 보유하고 있습니다. 우리 스타트업은 학생들이 질문을 입력하여 YouTube 비디오를 검색할 수 있는 검색 애플리케이션을 만들고자 합니다.

예를 들어, 학생이 'Jupyter Notebook이란 무엇인가?' 또는 'Azure ML이란 무엇인가?'라고 입력할 수 있고, 검색 애플리케이션은 해당 질문과 관련된 YouTube 비디오 목록을 반환하며, 더 나아가 검색 애플리케이션은 질문의 답변이 있는 비디오의 위치로 이동할 수 있는 링크를 반환할 것입니다.

## 소개

이 레슨에서는 다음 내용을 다룰 것입니다:

- 의미 기반 검색과 키워드 검색의 차이점.
- 텍스트 Embedding이란 무엇인가.
- 텍스트 Embedding 인덱스 생성.
- 텍스트 Embedding 인덱스 검색.

## 학습 목표

이 레슨을 마친 후에는 다음을 할 수 있습니다:

- 의미 기반 검색과 키워드 검색의 차이를 설명할 수 있습니다.
- 텍스트 Embedding이란 무엇인지 설명할 수 있습니다.
- Embedding을 사용하여 데이터를 검색하는 애플리케이션을 만들 수 있습니다.

## 검색 애플리케이션을 만드는 이유

검색 애플리케이션을 만드는 것은 Embedding을 사용하여 데이터를 검색하는 방법을 이해하는 데 도움이 됩니다. 또한 학생들이 정보를 빠르게 찾을 수 있는 검색 애플리케이션을 만드는 방법을 배우게 될 것입니다.

이 레슨에는 Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-koreyst) YouTube 채널의 YouTube 비디오 트랜스크립트의 Embedding 인덱스가 포함되어 있습니다. AI Show는 AI와 머신러닝에 대해 가르치는 YouTube 채널입니다. Embedding 인덱스에는 2023년 10월까지의 각 YouTube 트랜스크립트에 대한 Embedding이 포함되어 있습니다. 우리 스타트업을 위해 Embedding 인덱스를 사용하여 검색 애플리케이션을 만들 것입니다. 검색 애플리케이션은 질문의 답변이 있는 비디오의 위치로 이동할 수 있는 링크를 반환합니다. 이는 학생들이 필요한 정보를 빠르게 찾는 좋은 방법입니다.

다음은 질문 'Azure ML에서 rstudio를 사용할 수 있나요?'에 대한 의미 기반 쿼리의 예입니다. YouTube URL을 확인해보면, 질문의 답변이 있는 비디오의 위치로 이동하는 타임스탬프가 URL에 포함되어 있습니다.

![Semantic query for the question "can you use rstudio with Azure ML"](../../images/query-results.png?WT.mc_id=academic-105485-koreyst)

## 의미 기반 검색이란 무엇인가요?

이제 아마도 궁금해하실 것 같습니다. 의미 기반 검색이란 무엇일까요? 의미 기반 검색은 쿼리의 단어들의 의미, 즉 의미론을 활용하여 관련된 결과를 반환하는 검색 기술입니다.

다음은 의미 기반 검색의 예시입니다. 예를 들어, 차를 구매하려고 한다고 가정해봅시다. '내 꿈의 차'라고 검색할 수 있습니다. 의미 기반 검색은 여러분이 차에 대해 '꿈을 꾸는' 것이 아니라 '이상적인' 차를 구매하려고 한다는 것을 이해합니다. 의미 기반 검색은 여러분의 의도를 이해하고 관련된 결과를 반환합니다. 반면에 '키워드 검색'은 차에 대한 꿈을 진정으로 검색하고 종종 관련 없는 결과를 반환합니다.

## 텍스트 임베딩이란 무엇인가요?

[텍스트 임베딩](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst)은 [자연어 처리](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst)에서 사용되는 텍스트 표현 기술입니다. 텍스트 임베딩은 텍스트의 의미론적인 수치적 표현입니다. 임베딩은 기계가 이해하기 쉬운 방식으로 데이터를 표현하는 데 사용됩니다. 텍스트 임베딩을 구축하기 위한 다양한 모델이 있지만, 이 레슨에서는 OpenAI 임베딩 모델을 사용하여 임베딩을 생성하는 방법에 초점을 맞출 것입니다.

다음은 AI Show YouTube 채널의 에피소드 중 하나의 트랜스크립트에서 가져온 텍스트의 예시입니다:

```text
오늘은 Azure Machine Learning에 대해 배우게 될 것입니다.
```

텍스트를 OpenAI Embedding API에 전달하면, 1536개의 숫자로 구성된 임베딩이 반환됩니다. 각 숫자는 텍스트의 다른 측면을 나타냅니다. 간결함을 위해, 임베딩의 첫 10개 숫자만 표시하면 아래와 같습니다.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## 임베딩 인덱스는 어떻게 생성되나요?

이 레슨의 임베딩 인덱스는 일련의 Python 스크립트를 사용하여 생성되었습니다. 이 스크립트는 이 레슨의 `scripts` 폴더에 있는 [README](../../scripts/README.md?WT.mc_id=academic-105485-koreyst)와 함께 제공됩니다. 이 레슨을 완료하기 위해 이 스크립트를 실행할 필요는 없습니다. 왜냐하면 임베딩 인덱스가 이미 제공되기 때문입니다.

이 스크립트는 다음과 같은 작업을 수행합니다:

1. [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-koreyst) 재생목록의 각 YouTube 비디오의 트랜스크립트를 다운로드합니다.
2. [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst)를 사용하여 YouTube 트랜스크립트의 처음 3분에서 스피커 이름을 추출하려고 시도합니다. 각 비디오의 스피커 이름은 `embedding_index_3m.json`이라는 임베딩 인덱스에 저장됩니다.
3. 그런 다음 트랜스크립트 텍스트를 **3분 텍스트 세그먼트**로 분할합니다. 세그먼트에는 임베딩이 잘리지 않도록 하고 더 나은 검색 문맥을 제공하기 위해 다음 세그먼트에서 약 20개의 단어가 겹치도록 설계되었습니다.
4. 각 텍스트 세그먼트는 OpenAI Chat API에 전달되어 텍스트를 60단어로 요약합니다. 이 요약은 임베딩 인덱스 `embedding_index_3m.json`에도 저장됩니다.
5. 마지막으로, 세그먼트 텍스트는 OpenAI Embedding API에 전달됩니다. Embedding API는 세그먼트의 의미론적인 의미를 나타내는 1536개의 숫자 벡터를 반환합니다. 세그먼트와 OpenAI Embedding 벡터는 임베딩 인덱스 `embedding_index_3m.json`에 저장됩니다.

### 벡터 데이터베이스

레슨의 간소화를 위해 임베딩 인덱스는 `embedding_index_3m.json`이라는 JSON 파일에 저장되고 Pandas 데이터프레임으로 로드됩니다. 그러나 실제 운영 환경에서는 임베딩 인덱스를 [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst)와 같은 벡터 데이터베이스에 저장됩니다.

## 코사인 유사도 이해하기

텍스트 임베딩에 대해 배웠으니, 다음 단계는 코사인 유사도를 사용하여 데이터를 검색하고 특정 쿼리에 가장 유사한 임베딩을 찾는 방법을 배우는 것입니다.

### 코사인 유사도란 무엇인가요?

코사인 유사도는 두 벡터 사이의 유사성을 측정하는 방법으로, 이를 `최근접 이웃 검색 (nearest neighbor search)`이라고도 합니다. 코사인 유사도 검색을 수행하려면 OpenAI Embedding API를 사용하여 _쿼리_ 텍스트를 _벡터화_ 해야 합니다. 그런 다음 쿼리 벡터와 임베딩 인덱스의 각 벡터 간의 _코사인 유사도_ 를 계산합니다. 기억하세요, 임베딩 인덱스에는 각 YouTube 트랜스크립트 텍스트 세그먼트에 대한 벡터가 있습니다. 마지막으로, 코사인 유사도에 따라 결과를 정렬하고, 코사인 유사도가 가장 높은 텍스트 세그먼트가 쿼리와 가장 유사합니다.

수학적인 관점에서 코사인 유사도는 다차원 공간에 투영된 두 벡터 사이의 각도의 코사인을 측정합니다. 이 측정은 유용합니다. 왜냐하면 두 문서가 크기 때문에 유클리드 거리로 인해 멀리 떨어져 있을지라도, 그들 사이의 각도가 더 작고 따라서 코사인 유사도가 더 높을 수 있기 때문입니다. 코사인 유사도 방정식에 대한 자세한 정보는 [코사인 유사도](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst)를 참조하세요.

## 첫 번째 검색 애플리케이션 만들기

이제 임베딩을 사용하여 검색 애플리케이션을 만드는 방법을 배우겠습니다. 검색 애플리케이션은 학생들이 질문을 입력하여 비디오를 검색할 수 있게 해줍니다. 검색 애플리케이션은 질문과 관련된 비디오 목록을 반환합니다. 또한 검색 애플리케이션은 질문의 답변이 있는 비디오의 위치로 이동할 수 있는 링크를 반환합니다.

이 솔루션은 Windows 11, macOS 및 Ubuntu 22.04에서 Python 3.10 이상을 사용하여 빌드 및 테스트되었습니다. Python은 [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)에서 다운로드할 수 있습니다.

## 과제 - 학생들이 사용할 수 있도록 검색 애플리케이션 만들기

이 레슨의 시작에서 우리 스타트업을 소개했습니다. 이제 학생들이 자신의 평가를 위해 검색 애플리케이션을 만들 수 있도록 해야 합니다.

이 과제에서는 검색 애플리케이션을 구축하는 데 사용될 Azure OpenAI 서비스를 생성합니다. 다음 Azure OpenAI 서비스를 생성해야 합니다. 이 과제를 완료하려면 Azure 구독이 필요합니다.

### Azure Cloud Shell 시작하기

1. [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)에 로그인합니다.
2. Azure 포털의 오른쪽 상단에 있는 Cloud Shell 아이콘을 선택합니다.
3. 환경 유형으로 **Bash**를 선택합니다.

#### 리소스 그룹 생성

> 이 안내에서는 동부 미국에 있는 "semantic-video-search"라는 리소스 그룹을 사용합니다.
> 리소스 그룹의 이름을 변경할 수 있지만, 리소스의 위치를 변경할 때는 [모델 가용성 테이블](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)을 확인하세요.

```shell
az group create --name semantic-video-search --location eastus
```

#### Azure OpenAI 서비스 리소스 생성

Azure Cloud Shell에서 다음 명령을 실행하여 Azure OpenAI 서비스 리소스를 생성합니다.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### 애플리케이션에서 사용할 엔드포인트와 키 가져오기

Azure Cloud Shell에서 다음 명령을 실행하여 Azure OpenAI 서비스 리소스의 엔드포인트와 키를 가져옵니다.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### OpenAI 임베딩 모델 배포

Azure Cloud Shell에서 다음 명령을 실행하여 OpenAI 임베딩 모델을 배포합니다.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
```

## 해답

GitHub Codespaces에서 [해답 노트북](../../solution.ipynb?WT.mc_id=academic-105485-koreyst)을 열고 Jupyter Notebook의 지침을 따르세요.

노트북을 실행할 때, 쿼리를 입력하라는 메시지가 표시됩니다. 입력 상자는 다음과 같이 보일 것입니다:

![사용자가 쿼리를 입력하는 입력 상자](../../images/notebook-search.png?WT.mc_id=academic-105485-koreyst)

## 수고하셨습니다. 학습을 계속하세요!

이 레슨을 완료한 후, [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 Generative AI 지식을 더욱 향상시킬 수 있습니다!

Lesson 9로 이동하여 [이미지 생성 애플리케이션 구축하기](../../../09-building-image-applications/translations/ko/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!
