# 텍스트 생성 애플리케이션 구축

[![Building Text Generation Applications](../../../translated_images/ko/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(위 이미지를 클릭하여 이 강의의 비디오를 시청하세요)_

이 커리큘럼을 통해 지금까지 프롬프트 같은 핵심 개념과 "프롬프트 엔지니어링"이라는 하나의 전공 분야까지 살펴보았습니다. ChatGPT, Office 365, Microsoft Power Platform 등 상호작용할 수 있는 많은 도구들이 어떤 작업을 수행하기 위해 프롬프트를 사용하는 방식을 지원합니다.

앱에 이러한 경험을 추가하려면 프롬프트, 완료(Completion)와 같은 개념을 이해하고 작업할 라이브러리를 선택해야 합니다. 바로 이 장에서 그 내용을 배우게 될 것입니다.

## 소개

이 장에서는 다음을 배우게 됩니다:

- openai 라이브러리와 그 핵심 개념에 대해 알아봅니다.
- openai를 사용하여 텍스트 생성 애플리케이션을 구축합니다.
- 텍스트 생성 앱을 구축하기 위해 프롬프트(prompt), 온도(temperature), 토큰(tokens)과 같은 개념을 사용하는 방법을 이해합니다.

## 학습 목표

이 강의가 끝나면 다음을 할 수 있게 됩니다:

- 텍스트 생성 앱이 무엇인지 설명할 수 있습니다.
- openai를 사용하여 텍스트 생성 앱을 구축할 수 있습니다.
- 앱을 구성하여 더 많거나 적은 토큰을 사용하고 온도를 변경하여 다양한 출력을 생성할 수 있습니다.

## 텍스트 생성 앱이란 무엇인가요?

일반적으로 앱을 구축할 때 다음과 같은 인터페이스를 가집니다:

- 명령어 기반. 콘솔 앱은 명령어를 입력하면 작업을 수행하는 전형적인 앱입니다. 예를 들어 `git`은 명령어 기반 앱입니다.
- 사용자 인터페이스(UI). 일부 앱은 버튼을 클릭하고, 텍스트를 입력하고, 옵션을 선택하는 그래픽 사용자 인터페이스(GUI)를 가지고 있습니다.

### 콘솔 및 UI 앱의 한계

명령어를 타이핑하는 명령어 기반 앱과 비교해봅시다:

- <strong>제한적입니다</strong>. 지원하는 명령어만 입력할 수 있습니다.
- **특정 언어에 종속적입니다**. 일부 앱은 여러 언어를 지원하지만 기본적으로 특정 언어에 맞춰 제작됩니다. 물론 더 많은 언어를 추가할 수 있습니다.

### 텍스트 생성 앱의 장점

그렇다면 텍스트 생성 앱은 어떻게 다를까요?

텍스트 생성 앱에서는 더 큰 유연성이 있습니다. 정해진 명령어나 특정 입력 언어에 제한되지 않고 자연어를 사용하여 앱과 상호작용할 수 있습니다. 또 다른 장점은 이미 방대한 텍스트 자료에 대해 학습된 데이터 소스와 상호작용하게 된다는 점입니다. 반면 전통적인 앱은 데이터베이스 내 정보에 제한될 수 있습니다.

### 텍스트 생성 앱으로 무엇을 만들 수 있나요?

많은 것을 만들 수 있습니다. 예를 들어:

- <strong>챗봇</strong>. 회사와 제품에 관한 질문에 답하는 챗봇이 좋은 예입니다.
- <strong>도우미</strong>. LLM은 텍스트 요약, 텍스트에서 인사이트 얻기, 이력서 등 텍스트 생성에 매우 유용합니다.
- **코드 어시스턴트**. 사용하는 언어 모델에 따라, 코드를 작성하는 데 도움을 주는 어시스턴트를 만들 수 있습니다. 예를 들어 GitHub Copilot, ChatGPT 같은 제품을 활용할 수 있습니다.

## 어떻게 시작할 수 있을까요?

보통 LLM과 통합하는 방법은 다음 두 가지 접근법을 포함합니다:

- API 사용. 프롬프트를 포함한 웹 요청을 만들고 생성된 텍스트를 반환받습니다.
- 라이브러리 사용. 라이브러리는 API 호출을 캡슐화하여 사용을 쉽게 만듭니다.

## 라이브러리/SDK

LLM과 작업할 때 잘 알려진 몇 가지 라이브러리가 있습니다:

- **openai**: 이 라이브러리는 모델에 쉽게 연결하고 프롬프트를 전송할 수 있도록 해줍니다.

또 더 높은 수준에서 동작하는 라이브러리도 있습니다:

- **Langchain**: Langchain은 잘 알려져 있으며 Python을 지원합니다.
- **Semantic Kernel**: Semantic Kernel은 Microsoft에서 만든 라이브러리로 C#, Python, Java를 지원합니다.

## openai를 사용한 첫 앱

첫 번째 앱을 어떻게 만들지, 필요한 라이브러리와 요구사항 등을 살펴보겠습니다.

### openai 설치

OpenAI 혹은 Azure OpenAI와 상호작용하는 라이브러리는 많습니다. C#, Python, JavaScript, Java 등 다양한 프로그래밍 언어도 사용할 수 있습니다. 여기서는 `openai` Python 라이브러리를 사용하기로 하였고, `pip`로 설치할 것입니다.

```bash
pip install openai
```

### 리소스 생성

다음 단계를 수행해야 합니다:

- Azure에서 계정을 만듭니다 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI에 접근 권한을 얻습니다. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 에서 접근 신청을 합니다.

  > [!NOTE]
  > 작성 시점 기준으로 Azure OpenAI 접근 권한 신청이 필요합니다.

- Python 설치 <https://www.python.org/>
- Azure OpenAI 서비스 리소스를 생성해야 합니다. [리소스 생성 가이드](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)를 참조하세요.

### API 키 및 엔드포인트 찾기

이제 `openai` 라이브러리에서 사용할 API 키를 알려줘야 합니다. Azure OpenAI 리소스의 "Keys and Endpoint" 섹션으로 가서 "Key 1" 값을 복사하세요.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

이 정보를 복사했으면 라이브러리가 이를 사용하도록 설정해봅시다.

> [!NOTE]
> API 키를 코드와 분리하는 것이 좋습니다. 환경 변수를 사용하면 됩니다.
>
> - 환경 변수 `OPENAI_API_KEY` 를 API 키로 설정하세요.
>   `export OPENAI_API_KEY='sk-...'`

### Azure 구성 설정

Azure OpenAI (현재 Microsoft Foundry 포함)를 사용하는 경우 설정 방법은 다음과 같습니다. 표준 `OpenAI` 클라이언트를 Azure OpenAI `/openai/v1/` 엔드포인트에 연결하여 Responses API를 사용하며 `api_version`이 필요 없습니다:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

위 구성은 다음을 설정합니다:

- `api_key`: Azure 포털이나 Microsoft Foundry 포털에서 찾은 API 키.
- `base_url`: Foundry 리소스 엔드포인트에 `/openai/v1/`가 추가된 URL. 안정적인 v1 엔드포인트는 OpenAI 및 Azure OpenAI에서 `api_version` 관리 없이 작동합니다.

> [!NOTE] > `os.environ`은 환경 변수를 읽는 방법입니다. 이를 사용해 `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` 같은 환경 변수를 읽을 수 있습니다. 이 환경 변수들은 터미널에 설정하거나 `dotenv` 같은 라이브러리로 설정하세요.

## 텍스트 생성

텍스트를 생성하는 방법은 Responses API의 `responses.create` 메서드를 사용하는 것입니다. 예시는 다음과 같습니다:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # 이것은 당신의 모델 배포 이름입니다
    input=prompt,
    store=False,
)
print(response.output_text)
```

위 코드에서는 응답을 생성하고 사용할 모델과 프롬프트를 전달합니다. 그런 다음 `response.output_text`로 생성된 텍스트를 출력합니다.

### 다중 대화(turn) 지원

Responses API는 싱글턴 텍스트 생성뿐 아니라 다중 턴 챗봇에도 적합합니다 - 대화를 쌓기 위해 `input`에 메시지 목록을 제공합니다:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

이 기능에 대한 자세한 내용은 다음 챕터에서 다룹니다.

## 연습 - 첫 번째 텍스트 생성 앱 만들기

이제 openai 설치 및 설정법을 배웠으니 첫 텍스트 생성 앱을 만들어 봅시다. 다음 단계를 따르세요:

1. 가상 환경을 만들고 openai를 설치합니다:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows를 사용하는 경우 `source venv/bin/activate` 대신 `venv\Scripts\activate`를 입력하세요.

   > [!NOTE]
   > Azure OpenAI 키를 찾으려면 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 에서 `Open AI`를 검색하고 `Open AI 리소스`를 선택한 후 `Keys and Endpoint`에서 `Key 1` 값을 복사하세요.

1. _app.py_ 파일을 생성하고 다음 코드를 작성하세요:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 완료 코드를 추가하세요
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API를 사용하여 요청을 만드세요
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 응답을 출력하세요
   print(response.output_text)
   ```

   > [!NOTE]
   > Azure가 아닌 일반 OpenAI를 사용하는 경우 `client = OpenAI(api_key="<OpenAI 키로 교체>")` (base_url 없음)로 사용하고, 배포 이름 대신 `gpt-4o-mini` 같은 모델 이름을 전달하세요.

   다음과 같은 출력이 예상됩니다:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 다양한 유형의 프롬프트, 용도별로

이제 프롬프트를 사용해 텍스트 생성하는 방법을 봤습니다. 심지어 수정하여 다양한 유형의 텍스트를 생성할 수도 있는 프로그램이 준비되었습니다.

프롬프트는 여러 작업에 사용할 수 있습니다. 예를 들어:

- **텍스트 생성**: 예를 들어 시를 생성하거나 퀴즈용 질문을 만들 수 있습니다.
- **정보 조회**: 프롬프트를 통해 '웹 개발에서 CORS가 무엇인가?' 같은 정보를 찾을 수 있습니다.
- **코드 생성**: 이메일 검증 정규식 생성 등 코드를 생성할 수 있으며, 전체 웹 앱 같은 프로그램도 만들 수 있습니다.

## 좀 더 실용적인 사용 사례: 레시피 생성기

집에 재료가 있고 무언가 요리하고 싶다고 상상해봅시다. 그러려면 레시피가 필요합니다. 레시피를 찾기 위해 검색 엔진을 사용할 수도 있고, LLM을 활용할 수도 있습니다.

다음과 같은 프롬프트를 작성할 수 있습니다:

> "닭고기, 감자, 당근이 포함된 요리 레시피 5개를 보여주세요. 각 레시피마다 사용된 모든 재료를 나열해주세요."

위 프롬프트에 대해 다음과 유사한 응답을 받을 수 있습니다:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

이 결과는 훌륭하며 무엇을 요리할지 알 수 있습니다. 이때 유용할 수 있는 개선점은:

- 싫어하거나 알레르기가 있는 재료를 필터링하는 것.
- 집에 없는 재료를 위해 쇼핑 리스트를 생성하는 것.

위 경우를 위해 다음과 같은 추가 프롬프트를 작성해봅시다:

> "마늘 알레르기가 있어 마늘이 들어간 레시피는 제외해 주세요. 대신 다른 재료로 대체하시고, 집에 닭고기, 감자, 당근이 있다고 가정해 레시피에 필요한 쇼핑 리스트도 작성해 주세요."

그러면 다음과 같은 새 결과를 받게 됩니다:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

이것이 마늘이 들어가지 않은 다섯 가지 레시피이며, 이미 집에 있는 재료를 고려한 쇼핑 리스트도 포함되어 있습니다.

## 연습 - 레시피 생성기 만들기

시나리오를 따라 해 보았으니 이제 이를 코드로 작성해봅시다. 다음 단계를 따르세요:

1. 기존 _app.py_ 파일을 출발점으로 사용하세요
1. `prompt` 변수를 찾아 다음 코드로 변경하세요:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   코드를 실행하면 다음과 유사한 출력을 볼 수 있습니다:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 참고: LLM은 비결정적이므로 실행할 때마다 결과가 다를 수 있습니다.

   좋아요, 이제 개선 방법을 봅시다. 코드를 유연하게 만들어 재료와 레시피 수를 변경할 수 있도록 만들고 싶습니다.

1. 다음과 같이 코드를 변경합시다:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 레시피 수를 재료와 함께 프롬프트에 보간합니다
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   테스트 실행 코드는 다음과 비슷할 수 있습니다:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 필터 및 쇼핑 리스트 추가로 개선하기

이제 사용자의 입력에 따라 레시피 수와 재료를 조정할 수 있는 유연한 레시피 생성 앱이 완성되었습니다.

추가 개선을 위해 다음을 추가하고 싶습니다:

- **재료 필터링**: 싫어하거나 알레르기가 있는 재료를 걸러내고 싶습니다. 이를 위해 기존 프롬프트 끝에 필터 조건을 추가할 수 있습니다:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  위 코드에서는 `prompt` 끝에 `{filter}`를 추가하고 사용자로부터 필터 값을 받습니다.

  예를 들면 다음과 같습니다:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  보시다시피 우유가 들어간 모든 레시피는 필터링 되었지만, 유당불내증이라면 치즈가 들어간 레시피까지 필터링해야 할 수도 있으므로 명확한 필터링이 필요합니다.


- **쇼핑 목록 작성**. 집에 이미 있는 것을 고려하여 쇼핑 목록을 작성하고자 합니다.

  이 기능을 위해 모든 것을 한 번의 프롬프트로 해결할 수도 있고 두 개의 프롬프트로 나눌 수도 있습니다. 후자의 방식을 시도해 보겠습니다. 여기서는 추가 프롬프트를 넣는 것을 제안하지만, 이를 위해 이전 프롬프트의 결과를 이후 프롬프트의 컨텍스트로 추가해야 합니다.

  첫 번째 프롬프트의 결과를 출력하는 코드 부분을 찾아 아래 코드를 그 밑에 추가하세요:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 응답 출력
  print("Shopping list:")
  print(response.output_text)
  ```

  다음 사항에 주목하세요:

  1. 첫 번째 프롬프트의 결과를 새로운 프롬프트에 추가하여 새 프롬프트를 구성합니다:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 새 요청을 만들되 첫 번째 프롬프트에서 요청한 토큰 수를 고려하며 이번에는 `max_output_tokens`를 1200으로 설정합니다.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     이 코드를 실행하면 이제 다음과 같은 출력이 나옵니다:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 설정 개선하기

지금까지의 코드는 작동하지만, 더 개선할 수 있는 몇 가지 조정 사항이 있습니다. 해야 할 일은 다음과 같습니다:

- **코드에서 비밀 정보 분리하기**, 예를 들어 API 키 같은 경우. 비밀 정보는 코드 내에 있어서는 안 되며 안전한 위치에 저장되어야 합니다. 비밀 정보를 코드에서 분리하기 위해 환경 변수와 `python-dotenv` 같은 라이브러리를 사용하여 파일에서 로드할 수 있습니다. 코드 예시는 다음과 같습니다:

  1. 다음 내용을 포함하는 `.env` 파일을 만듭니다:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 참고로, Microsoft Foundry에서 Azure OpenAI를 사용할 경우 다음 환경 변수를 설정해야 합니다:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     코드에서는 다음과 같이 환경 변수를 로드할 수 있습니다:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **토큰 길이에 대하여**. 생성하려는 텍스트에 필요한 토큰 수를 고려해야 합니다. 토큰은 비용이 발생하므로 가능한 한 토큰 사용을 경제적으로 해야 합니다. 예를 들어, 프롬프트를 다르게 표현하여 토큰 수를 줄일 수 있나요?

  사용하는 토큰 수를 바꾸려면 `max_output_tokens` 매개변수를 사용할 수 있습니다. 예를 들어, 100 토큰을 사용하려면 다음과 같이 합니다:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **온도 실험하기**. 지금까지 온도에 대해 언급하지 않았지만, 프로그램 성능에 중요한 요소입니다. 온도가 높을수록 출력이 더 무작위적입니다. 반대로 온도가 낮을수록 출력이 더 예측 가능합니다. 출력에서 변화를 원하느냐에 따라 설정하세요.

  온도를 바꾸려면 `temperature` 매개변수를 사용합니다. 예를 들어, 온도를 0.5로 설정하려면 다음과 같이 합니다:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 참고로 1.0에 가까울수록 출력이 더 다양해집니다.

## 과제

이번 과제에서는 무엇을 만들지 선택할 수 있습니다.

다음은 몇 가지 제안입니다:

- 레시피 생성기 앱을 더 개선해 보세요. 온도 값과 프롬프트를 조정하며 실험해 보세요.
- "스터디 버디"를 만들어 보세요. 이 앱은 예를 들어 Python 같은 주제에 대해 질문에 답변할 수 있어야 합니다. “Python에서 특정 주제란 무엇인가요?”와 같은 프롬프트나 “특정 주제에 대한 코드를 보여 주세요” 같은 프롬프트가 있을 수 있습니다.
- 역사 봇을 만들어 역사를 생생하게 재현하세요. 봇에게 특정 역사적 인물 역할을 맡기고 그 인물의 삶과 시기에 대해 질문하세요.

## 해답

### 스터디 버디

아래는 시작용 프롬프트입니다. 이것을 어떻게 사용하고 원하는 대로 조정할 수 있는지 확인해 보세요.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 역사 봇

다음은 사용할 수 있는 몇 가지 프롬프트입니다:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 지식 점검

온도 개념은 무엇을 하나요?

1. 출력이 얼마나 무작위적인지를 제어합니다.
1. 응답 크기를 제어합니다.
1. 사용된 토큰 수를 제어합니다.

## 🚀 도전 과제

과제를 진행할 때 온도를 0, 0.5, 1로 다양하게 설정해 보세요. 0은 가장 덜 변하며 1은 가장 변동성이 많습니다. 어떤 값이 앱에 가장 적합한지 확인하세요.

## 훌륭합니다! 학습을 계속하세요

이 수업을 마친 후에는 [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성 AI 지식을 계속 향상하세요!

7강으로 가서 [채팅 애플리케이션 구축 방법](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)도 살펴보세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->