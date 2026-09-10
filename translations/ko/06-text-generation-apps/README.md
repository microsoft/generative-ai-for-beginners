# 텍스트 생성 애플리케이션 구축

[![텍스트 생성 애플리케이션 구축](../../../translated_images/ko/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(위 이미지를 클릭하여 본 수업 동영상 보기)_

지금까지 이 커리큘럼을 통해 프롬프트와 "프롬프트 엔지니어링"이라는 분야 같은 핵심 개념들을 보셨습니다. ChatGPT, Office 365, Microsoft Power Platform 등과 같이 많은 도구들은 무언가를 수행하기 위해 프롬프트를 사용할 수 있도록 지원합니다.

앱에 이러한 경험을 추가하려면 프롬프트, 완료(Completion)와 같은 개념을 이해하고 작업할 라이브러리를 선택해야 합니다. 이번 장에서 정확히 이 내용을 배울 것입니다.

## 소개

이 장에서 여러분은:

- openai 라이브러리와 그 핵심 개념에 대해 배웁니다.
- openai를 사용하여 텍스트 생성 앱을 만듭니다.
- 텍스트 생성 앱을 만들기 위해 프롬프트, 온도, 토큰과 같은 개념을 사용하는 방법을 이해합니다.

## 학습 목표

이 수업이 끝나면 여러분은:

- 텍스트 생성 앱이 무엇인지 설명할 수 있습니다.
- openai를 사용하여 텍스트 생성 앱을 만들 수 있습니다.
- 출력의 다양성을 위해 더 많거나 적은 토큰을 사용하고 온도를 변경하도록 앱을 구성할 수 있습니다.

## 텍스트 생성 앱이란?

일반적으로 앱을 만들 때는 다음과 같은 인터페이스를 갖춥니다:

- 명령 기반. 콘솔 앱은 명령을 입력하고 작업을 수행하는 전형적인 앱입니다. 예를 들어 `git`은 명령 기반 앱입니다.
- 사용자 인터페이스(UI). 일부 앱은 버튼 클릭, 텍스트 입력, 옵션 선택 등이 가능한 그래픽 사용자 인터페이스(GUI)를 갖고 있습니다.

### 콘솔 및 UI 앱의 한계

명령을 입력하는 명령 기반 앱과 비교하면:

- <strong>한정적입니다</strong>. 앱에서 지원하는 명령만 입력할 수 있습니다.
- **언어 의존적입니다**. 일부 앱은 여러 언어를 지원하지만 기본적으로 특정 언어를 위해 만들어져 있으며 추가 언어 지원도 가능합니다.

### 텍스트 생성 앱의 장점

그렇다면 텍스트 생성 앱은 어떻게 다를까요?

텍스트 생성 앱에서는 더 많은 유연성이 있습니다. 미리 정해진 명령이나 특정 입력 언어에 제한받지 않고 자연어를 사용하여 앱과 상호작용할 수 있습니다. 또 다른 장점은, 전통적인 앱이 데이터베이스의 내용에 제한될 수 있는 것과 달리, 이미 방대한 자료에 대해 학습된 데이터 소스와 상호작용한다는 점입니다.

### 텍스트 생성 앱으로 무엇을 만들 수 있을까요?

여러 가지를 만들 수 있습니다. 예를 들어:

- <strong>챗봇</strong>. 회사와 제품 등에 관한 질문에 답하는 챗봇이 좋은 예입니다.
- <strong>도우미</strong>. LLM은 텍스트 요약, 텍스트에서 인사이트 추출, 이력서와 같은 텍스트 생성에 매우 유용합니다.
- **코드 어시스턴트**. 사용하는 언어 모델에 따라 코드를 작성하도록 돕는 코딩 어시스턴트를 만들 수 있습니다. 예를 들어 GitHub Copilot과 ChatGPT 등이 있습니다.

## 어떻게 시작할 수 있나요?

LLM과 통합할 방법을 찾아야 하며, 일반적으로 다음 두 가지 접근법이 있습니다:

- API 사용. 프롬프트를 포함한 웹 요청을 보내 생성된 텍스트를 받는 방식입니다.
- 라이브러리 사용. 라이브러리는 API 호출을 캡슐화하여 더 쉽게 사용할 수 있도록 합니다.

## 라이브러리/SDK

LLM과 작업할 때 잘 알려진 몇 가지 라이브러리들이 있습니다:

- **openai**. 이 라이브러리를 사용하면 모델과 쉽게 연결하고 프롬프트를 보낼 수 있습니다.

그리고 다음과 같은 더 상위 수준의 라이브러리도 있습니다:

- **Langchain**. 잘 알려져 있으며 Python을 지원합니다.
- **Semantic Kernel**. Microsoft에서 만든 라이브러리로 C#, Python, Java를 지원합니다.

## openai를 사용한 첫 번째 앱

첫 번째 앱을 어떻게 만드는지, 필요한 라이브러리는 무엇인지, 얼마나 필요한지 등을 살펴봅시다.

### openai 설치하기

OpenAI 또는 Azure OpenAI와 상호작용하기 위해 많은 라이브러리가 있습니다. C#, Python, JavaScript, Java 등 다양한 프로그래밍 언어를 사용할 수 있습니다. 우리는 `openai` Python 라이브러리를 사용하기로 했으므로 `pip`로 설치합니다.

```bash
pip install openai
```

### 리소스 생성하기

다음 단계를 수행해야 합니다:

- Azure 계정 생성하기 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI 접근 권한 획득하기. [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 에서 접근 요청을 합니다.

  > [!NOTE]
  > 작성 시점 기준으로 Azure OpenAI 접근을 신청해야 합니다.

- Python 설치하기 <https://www.python.org/>
- Azure OpenAI 서비스 리소스 생성하기. [리소스 생성 가이드](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)를 참고하세요.

### API 키 및 엔드포인트 찾기

지금부터는 `openai` 라이브러리에 어떤 API 키를 사용할지 알려줘야 합니다. API 키를 찾으려면 Azure OpenAI 리소스의 "키 및 엔드포인트" 섹션으로 가서 "키 1" 값을 복사합니다.

![Azure 포털에서 키 및 엔드포인트 리소스 블레이드](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

정보를 복사했으면, 이제 라이브러리가 이를 사용하도록 지시합시다.

> [!NOTE]
> API 키를 코드와 분리하는 것이 좋습니다. 환경 변수를 사용해 할 수 있습니다.
>
> - 환경 변수 `OPENAI_API_KEY` 에 API 키를 설정합니다.
>   `export OPENAI_API_KEY='sk-...'`

### Azure 구성 설정

Azure OpenAI(현재 Microsoft Foundry의 일부)를 사용한다면 다음과 같이 설정합니다. 표준 `OpenAI` 클라이언트를 Azure OpenAI `/openai/v1/` 엔드포인트에 지정하여 사용하며, Responses API와 작동하고 `api_version`이 필요 없습니다:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

위 코드에서는 다음을 설정합니다:

- `api_key`, Azure 포털 또는 Microsoft Foundry 포털에서 찾은 API 키입니다.
- `base_url`, `/openai/v1/`가 붙은 Foundry 리소스 엔드포인트입니다. 안정적인 v1 엔드포인트는 OpenAI 및 Azure OpenAI에서 `api_version` 관리 없이 작동합니다.

> [!NOTE] > `os.environ`은 환경 변수를 읽습니다. `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` 같은 환경 변수를 터미널에서 설정하거나 `dotenv` 같은 라이브러리를 사용해 설정할 수 있습니다.

## 텍스트 생성하기

텍스트를 생성하는 방법은 Responses API의 `responses.create` 메서드를 사용하는 것입니다. 다음은 예제입니다:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # 이것은 당신의 모델 배포 이름입니다
    input=prompt,
    store=False,
)
print(response.output_text)
```

위 코드에서는 응답을 생성하고 원하는 모델과 프롬프트를 전달합니다. 그리고 `response.output_text`를 통해 생성된 텍스트를 출력합니다.

### 다중 대화(turn) 처리

Responses API는 단일 회차 텍스트 생성과 다중 회차 챗봇 모두에 적합합니다 - `input`에 메시지 목록을 제공하여 대화를 구성합니다:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

이 기능에 대한 자세한 내용은 다음 장에서 다룹니다.

## 연습 - 첫 번째 텍스트 생성 앱 만들기

openai 설정과 구성 방법을 배웠으니, 이제 첫 번째 텍스트 생성 앱을 빌드할 차례입니다. 단계별로 따라하세요:

1. 가상환경을 만들고 openai를 설치합니다:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 윈도우를 사용하는 경우 `source venv/bin/activate` 대신 `venv\Scripts\activate`를 입력하세요.

   > [!NOTE]
   > Azure OpenAI 키는 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 에서 `Open AI`를 검색, `Open AI 리소스` 선택 후 `키 및 엔드포인트`에서 `키 1` 값을 복사하여 찾으세요.

1. _app.py_ 파일을 만들고 다음 코드를 넣으세요:

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
   > Azure가 아닌 일반 OpenAI 사용 시, `client = OpenAI(api_key="<여기에 OpenAI 키 입력>")` (base_url 제외)를 사용하고 배포 이름 대신 모델 이름 예: `gpt-5-mini`를 전달하세요.

   다음과 유사한 출력이 있어야 합니다:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 다양한 유형의 프롬프트, 다양한 용도

이제 프롬프트로 텍스트를 생성하는 방법을 알게 되었습니다. 수정하고 변경하여 다양한 유형의 텍스트를 생성할 수 있는 프로그램도 완성했습니다.

프롬프트는 여러 가지 작업에 사용할 수 있습니다. 예를 들어:

- **특정 유형의 텍스트 생성**. 예를 들어 시, 퀴즈 질문 등을 생성할 수 있습니다.
- **정보 조회**. 예를 들어 '웹 개발에서 CORS는 무엇을 의미하나요?' 같은 정보를 찾는 데 프롬프트를 사용할 수 있습니다.
- **코드 생성**. 이메일 검증에 사용하는 정규 표현식을 만들거나 전체 프로그램, 웹 앱을 생성할 수도 있습니다.

## 좀 더 실용적인 예: 레시피 생성기

집에 재료가 있고 요리를 하고 싶다고 가정해보세요. 그럴 때 필요한 것이 레시피입니다. 레시피를 찾는 방법으로 검색 엔진을 사용하거나 LLM을 사용할 수 있습니다.

프롬프트를 다음과 같이 작성할 수 있습니다:

> "다음 재료로 만든 요리 5가지 레시피를 보여주세요: 닭고기, 감자, 당근. 각 레시피에 사용된 모든 재료를 나열하세요"

위 프롬프트를 주면 다음과 비슷한 응답을 받을 수 있습니다:

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

결과가 아주 좋아서 무엇을 요리할지 알 수 있습니다. 이 시점에서 유용할 수 있는 개선사항은:

- 싫어하거나 알레르기가 있는 재료 필터링하기
- 집에 모든 재료가 없을 경우 쇼핑 목록 생성하기

위 사례를 위해 추가 프롬프트를 넣어봅니다:

> "마늘은 알레르기가 있어서 제외하고 대신 다른 재료로 대체해 주세요. 또한, 닭고기, 감자, 당근은 이미 집에 있으니 쇼핑 목록도 만들어 주세요."

이제 새로운 결과를 받게 됩니다:

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

마늘이 포함되지 않은 5가지 레시피와 이미 집에 있는 재료를 고려한 쇼핑 목록입니다.

## 연습 - 레시피 생성기 만들기

시나리오를 살펴봤으니, 이제 매칭되는 코드를 작성해봅니다. 다음 단계를 따라 하세요:

1. 기존 _app.py_ 파일을 시작점으로 사용합니다.
1. `prompt` 변수를 찾아 다음 코드로 변경하세요:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   지금 코드를 실행하면 다음과 비슷한 출력이 나타납니다:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 참고로, LLM은 비결정론적이므로 실행할 때마다 결과가 달라질 수 있습니다.

   좋습니다. 이제 개선할 방법을 살펴봅시다. 코드를 유연하게 만들어 재료와 레시피 수 모두 변경할 수 있도록 할 것입니다.

1. 다음과 같이 코드를 변경합시다:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 재료와 함께 프롬프트에 레시피 수를 보간합니다
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   테스트 실행용 코드는 다음과 같을 수 있습니다:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 필터 및 쇼핑 목록 추가로 개선하기

이제 레시피를 생성할 수 있는 작동하는 앱이 생겼고, 사용자가 레시피 수와 재료를 입력하여 유연하게 작동합니다.

더 개선하려면 다음을 추가할 것입니다:

- **재료 필터링**. 싫어하거나 알레르기가 있는 재료를 걸러낼 수 있어야 합니다. 기존 프롬프트 끝에 필터 조건을 추가하여 달성할 수 있습니다:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  위 코드에서 끝에 `{filter}`를 추가하고 사용자로부터 필터 값을 입력받습니다.

  프로그램 실행 시 예시 입력은 다음과 같을 수 있습니다:

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

  보시다시피 우유가 들어간 레시피는 걸러졌습니다. 하지만 유당불내증이라면 치즈가 들어간 레시피도 걸러야 하므로 명확한 필터링이 필요합니다.


- **장보기 목록 작성하기**. 집에 이미 있는 것을 고려하여 장보기 목록을 작성하고자 합니다.

  이 기능을 위해 모든 것을 한 번의 프롬프트로 해결할 수도 있고, 두 개의 프롬프트로 나눌 수도 있습니다. 후자의 방법을 시도해 봅시다. 여기서는 추가 프롬프트를 제안하지만, 이를 위해서는 이전 프롬프트의 결과를 이후 프롬프트에 컨텍스트로 추가해야 합니다.

  첫 번째 프롬프트의 결과를 출력하는 코드 부분을 찾아 아래 코드를 추가하세요:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 응답 출력
  print("Shopping list:")
  print(response.output_text)
  ```

  다음 사항을 참고하세요:

  1. 첫 번째 프롬프트의 결과를 새로운 프롬프트에 추가하여 새 프롬프트를 구성합니다:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 새로운 요청을 하지만 첫 번째 프롬프트에서 요청한 토큰 수를 고려하여 이번에는 `max_output_tokens`를 1200으로 설정합니다.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     이 코드를 실행하면 다음과 같은 출력이 나타납니다:

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

지금까지는 작동하는 코드지만, 좀 더 개선하기 위한 조정 사항이 있습니다. 우리가 해야 할 몇 가지 작업은 다음과 같습니다:

- **코드에서 비밀 정보 분리하기**, API 키처럼. 비밀 정보는 코드에 포함되지 말아야 하며 안전한 위치에 저장되어야 합니다. 비밀 정보를 코드에서 분리하기 위해 환경 변수와 `python-dotenv`와 같은 라이브러리를 사용하여 파일에서 로드할 수 있습니다. 코드에서 어떻게 보이는지 확인해보겠습니다:

  1. 다음 내용을 가진 `.env` 파일을 만듭니다:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 참고로, Microsoft Foundry의 Azure OpenAI를 사용할 경우 다음 환경 변수를 설정해야 합니다:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     코드에서는 환경 변수를 다음과 같이 로드합니다:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **토큰 길이에 대해 한마디**. 생성할 텍스트에 필요한 토큰 수를 고려해야 합니다. 토큰은 비용이 발생하므로 가능하면 토큰 사용을 경제적으로 해야 합니다. 예를 들어 프롬프트를 적절히 구성하여 토큰 수를 줄일 수 있나요?

  토큰 수를 변경하려면 `max_output_tokens` 매개변수를 사용할 수 있습니다. 예를 들어 100 토큰을 사용하려면 다음과 같이 합니다:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **온도 실험하기**. 온도라는 개념은 지금까지 언급하지 않았지만, 프로그램 성능에 중요한 컨텍스트입니다. 온도 값이 높을수록 출력이 더 무작위적이고, 낮을수록 예측 가능해집니다. 출력에서 변화를 원하시는지 생각해보세요.

  온도를 변경하려면 `temperature` 매개변수를 사용하세요. 예를 들어 0.5의 온도를 원하면 다음과 같이 합니다:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 참고로 1.0에 가까울수록 출력이 더 다양해집니다.

- **추론 모델은 `temperature`를 사용하지 않습니다**. 이는 2026년의 중요한 변화입니다. Microsoft Foundry에서 현재 사용되는 비폐기 모델들은 추론 모델 (GPT-5 계열, o-시리즈)이며, 이들은 `temperature`나 `top_p` (또한 `max_tokens` 대신 `max_output_tokens`)를 지원하지 않습니다. `gpt-5-mini`에 `temperature`를 전달하면 "지원하지 않는 매개변수" 오류가 발생합니다. 따라서 위 온도 예제를 시도하려면 샘플링 제어를 아직 지원하는 모델—예를 들어 [Microsoft Foundry 모델 카탈로그](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)의 오픈 Llama 모델 `Llama-3.3-70B-Instruct` 같은 모델을 사용하세요. GPT-5 같은 추론 모델의 경우 출력 제어는 다음 방식으로 합니다:
  - **프롬프트 엔지니어링** - 명확한 지시, 예제, 구조화된 출력 (레슨 [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) 참조)이 샘플링 제어 기능을 대신합니다.
  - **추론 제어** - 추론 노력 및 장황함과 같은 매개변수들은 추론 깊이와 지연 및 비용의 균형을 맞춥니다.

  요약하자면: `temperature`/`top_p`는 아직 많은 모델(Llama, Mistral, Phi, GPT-4.x 계열—단 GPT-4.x는 폐기 중)에 유효하지만, 추론 모델인 GPT-5 쪽은 프롬프트 엔지니어링과 추론 제어 방향으로 나아가고 있습니다.

## 과제

이번 과제에서는 원하는 것을 만들 수 있습니다.

다음은 몇 가지 제안입니다:

- 레시피 생성기 앱을 좀 더 개선해 보세요. 온도 값을 조정하고 프롬프트를 변경해 어떤 결과가 나오는지 살펴보세요.
- "스터디 버디"를 만들어 보세요. 예를 들어 Python 주제에 대한 질문에 답할 수 있어야 하며, "Python의 특정 주제란 무엇인가요?" 또는 "특정 주제 코드를 보여주세요" 같은 프롬프트를 사용할 수 있습니다.
- 역사 봇을 만들어 역사를 생생하게 표현해 보세요. 봇에게 특정 역사적 인물을 연기하도록 지시하고 그 인물의 삶과 시대에 대해 질문해 보세요.

## 솔루션

### 스터디 버디

아래는 시작 프롬프트입니다. 어떻게 사용하는지 보고 원하는 대로 조정해보세요.

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

## 지식 확인

온도 개념은 무엇을 하나요?

1. 출력이 얼마나 무작위적인지 조절합니다.
1. 응답이 얼마나 큰지 조절합니다.
1. 얼마나 많은 토큰을 사용하는지 조절합니다.

## 🚀 도전 과제

과제를 진행할 때 온도를 다양하게 설정해 보세요. 0, 0.5, 1로 설정해 보세요. 0은 가장 변화가 적고 1은 가장 변화가 큽니다. 앱에 가장 잘 맞는 값은 무엇인가요?

## 잘 하셨어요! 학습을 계속하세요

이번 레슨을 완료한 후에는 [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 생성적 AI 지식을 계속 향상하세요!

7과로 이동하여 [채팅 애플리케이션 만들기](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)를 살펴보세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->