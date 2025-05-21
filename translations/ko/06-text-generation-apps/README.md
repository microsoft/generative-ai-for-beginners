<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T10:02:02+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ko"
}
-->
# 텍스트 생성 애플리케이션 구축하기

[![텍스트 생성 애플리케이션 구축하기](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.ko.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(위 이미지를 클릭하면 이 강의의 비디오를 볼 수 있습니다)_

지금까지 이 커리큘럼을 통해 프롬프트와 같은 핵심 개념과 "프롬프트 엔지니어링"이라는 전체 분야가 있다는 것을 보았습니다. ChatGPT, Office 365, Microsoft Power Platform 등과 같은 도구들은 프롬프트를 사용하여 무언가를 성취할 수 있도록 지원합니다.

이러한 경험을 앱에 추가하려면 프롬프트, 완료와 같은 개념을 이해하고 사용할 라이브러리를 선택해야 합니다. 이 장에서는 바로 그것을 배우게 됩니다.

## 소개

이 장에서 여러분은:

- openai 라이브러리와 그 핵심 개념에 대해 배웁니다.
- openai를 사용하여 텍스트 생성 앱을 만듭니다.
- 프롬프트, 온도, 토큰과 같은 개념을 사용하여 텍스트 생성 앱을 구축하는 방법을 이해합니다.

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- 텍스트 생성 앱이 무엇인지 설명할 수 있습니다.
- openai를 사용하여 텍스트 생성 앱을 구축할 수 있습니다.
- 더 많은 또는 적은 토큰을 사용하도록 앱을 구성하고 온도를 변경하여 다양한 출력을 얻을 수 있습니다.

## 텍스트 생성 앱이란 무엇인가요?

일반적으로 앱을 만들 때 다음과 같은 인터페이스가 있습니다:

- 명령 기반. 콘솔 앱은 명령을 입력하고 작업을 수행하는 전형적인 앱입니다. 예를 들어, `git`는 명령 기반 앱입니다.
- 사용자 인터페이스(UI). 일부 앱은 버튼을 클릭하고, 텍스트를 입력하고, 옵션을 선택하는 등의 그래픽 사용자 인터페이스(GUI)를 가지고 있습니다.

### 콘솔 및 UI 앱의 제한점

명령을 입력하는 명령 기반 앱과 비교하면:

- **제한적입니다**. 앱이 지원하는 명령만 입력할 수 있습니다.
- **언어 특정적입니다**. 일부 앱은 여러 언어를 지원하지만 기본적으로 특정 언어를 위해 구축됩니다. 더 많은 언어 지원을 추가할 수 있다 하더라도 말입니다.

### 텍스트 생성 앱의 이점

그렇다면 텍스트 생성 앱은 어떻게 다른가요?

텍스트 생성 앱에서는 명령 집합이나 특정 입력 언어에 제한되지 않고 더 많은 유연성을 제공합니다. 대신 자연어를 사용하여 앱과 상호 작용할 수 있습니다. 또 다른 이점은 방대한 정보 코퍼스를 기반으로 훈련된 데이터 소스와 이미 상호 작용하고 있다는 것입니다. 반면 전통적인 앱은 데이터베이스에 있는 것에 제한될 수 있습니다.

### 텍스트 생성 앱으로 무엇을 만들 수 있나요?

다양한 것들을 만들 수 있습니다. 예를 들어:

- **챗봇**. 회사와 제품에 대한 질문을 답변하는 챗봇은 좋은 선택이 될 수 있습니다.
- **도우미**. LLM은 텍스트 요약, 텍스트에서 인사이트 얻기, 이력서 같은 텍스트 생성 등에 탁월합니다.
- **코드 어시스턴트**. 사용하는 언어 모델에 따라 코드를 작성하는 데 도움을 주는 코드 어시스턴트를 만들 수 있습니다. 예를 들어, GitHub Copilot이나 ChatGPT와 같은 제품을 사용하여 코드를 작성하는 데 도움을 받을 수 있습니다.

## 어떻게 시작할 수 있나요?

LLM과 통합하는 방법을 찾아야 하며, 일반적으로 다음 두 가지 접근 방식을 포함합니다:

- API 사용. 여기서는 프롬프트와 함께 웹 요청을 구성하고 생성된 텍스트를 반환받습니다.
- 라이브러리 사용. 라이브러리는 API 호출을 캡슐화하여 사용하기 쉽게 만듭니다.

## 라이브러리/SDK

LLM을 다루기 위한 잘 알려진 라이브러리 몇 가지가 있습니다:

- **openai**, 이 라이브러리는 모델에 쉽게 연결하고 프롬프트를 보낼 수 있게 해줍니다.

그 다음으로는 더 높은 수준에서 작동하는 라이브러리들이 있습니다:

- **Langchain**. Langchain은 잘 알려져 있으며 Python을 지원합니다.
- **Semantic Kernel**. Semantic Kernel은 Microsoft에서 제공하는 라이브러리로 C#, Python, Java 언어를 지원합니다.

## 첫 번째 앱 만들기 - openai 사용

이제 첫 번째 앱을 만드는 방법, 필요한 라이브러리, 요구 사항 등을 살펴보겠습니다.

### openai 설치

OpenAI 또는 Azure OpenAI와 상호 작용하는 많은 라이브러리가 있습니다. C#, Python, JavaScript, Java 등 여러 프로그래밍 언어를 사용할 수 있습니다. 우리는 `openai` Python 라이브러리를 선택했으므로 `pip`을 사용하여 설치할 것입니다.

```bash
pip install openai
```

### 리소스 생성

다음 단계를 수행해야 합니다:

- Azure 계정 생성 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI에 접근 권한 얻기. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)로 이동하여 접근 권한을 요청합니다.

  > [!NOTE]
  > 작성 당시에는 Azure OpenAI에 접근하기 위해 신청해야 합니다.

- Python 설치 <https://www.python.org/>
- Azure OpenAI 서비스 리소스를 생성합니다. [리소스 생성](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)에 대한 가이드를 참조하세요.

### API 키 및 엔드포인트 찾기

이 시점에서 `openai` 라이브러리에 사용할 API 키를 알려줘야 합니다. API 키를 찾으려면 Azure OpenAI 리소스의 "키 및 엔드포인트" 섹션으로 이동하여 "키 1" 값을 복사합니다.

![Azure 포털의 키 및 엔드포인트 리소스 블레이드](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

이 정보를 복사했으니 이제 라이브러리에게 이를 사용하도록 지시합시다.

> [!NOTE]
> API 키를 코드와 분리하는 것이 좋습니다. 환경 변수를 사용하여 이를 수행할 수 있습니다.
>
> - 환경 변수 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`를 설정합니다.

### Azure 설정 구성

Azure OpenAI를 사용하는 경우 설정 구성 방법은 다음과 같습니다:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

위에서 우리는 다음을 설정하고 있습니다:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` 클래스. 예시는 다음과 같습니다:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

위 코드에서는 완료 객체를 생성하고 사용할 모델과 프롬프트를 전달합니다. 그런 다음 생성된 텍스트를 출력합니다.

### 채팅 완료

지금까지 `Completion` to generate text. But there's another class called `ChatCompletion`을 사용해 왔으며, 이는 챗봇에 더 적합합니다. 다음은 이를 사용하는 예시입니다:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

이 기능에 대한 자세한 내용은 다음 장에서 다룰 것입니다.

## 연습 - 첫 번째 텍스트 생성 앱

이제 openai를 설정하고 구성하는 방법을 배웠으니, 첫 번째 텍스트 생성 앱을 구축할 시간입니다. 앱을 구축하려면 다음 단계를 따르세요:

1. 가상 환경을 만들고 openai를 설치합니다:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows를 사용하는 경우 `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI 리소스` and then select `키 및 엔드포인트` and copy the `키 1` 값을 입력합니다.

1. _app.py_ 파일을 생성하고 다음 코드를 입력합니다:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Azure OpenAI를 사용하는 경우 `api_type` to `azure` and set the `api_key`를 Azure OpenAI 키로 설정해야 합니다.

   다음과 같은 출력을 볼 수 있어야 합니다:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 다양한 작업을 위한 다양한 프롬프트

이제 프롬프트를 사용하여 텍스트를 생성하는 방법을 보았습니다. 수정하고 변경하여 다양한 유형의 텍스트를 생성할 수 있는 프로그램도 실행 중입니다.

프롬프트는 다양한 작업에 사용할 수 있습니다. 예를 들어:

- **특정 유형의 텍스트 생성**. 예를 들어, 시, 퀴즈 질문 등을 생성할 수 있습니다.
- **정보 조회**. 다음과 같은 예시를 통해 정보를 조회할 수 있습니다: '웹 개발에서 CORS는 무엇을 의미하나요?'.
- **코드 생성**. 예를 들어 이메일을 검증하는 데 사용되는 정규 표현식을 개발하거나 웹 앱과 같은 전체 프로그램을 생성하는 데 사용할 수 있습니다.

## 더 실용적인 사용 사례: 레시피 생성기

집에 있는 재료로 요리를 하고 싶다고 상상해보세요. 그러기 위해서는 레시피가 필요합니다. 레시피를 찾는 방법 중 하나는 검색 엔진을 사용하는 것이거나 LLM을 사용하는 것입니다.

다음과 같은 프롬프트를 작성할 수 있습니다:

> "다음 재료로 요리할 수 있는 요리 5가지의 레시피를 보여주세요: 닭고기, 감자, 당근. 각 레시피에 사용된 모든 재료를 나열하세요."

위의 프롬프트를 사용하면 다음과 유사한 응답을 받을 수 있습니다:

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

이 결과는 훌륭합니다. 무엇을 요리할지 알 수 있습니다. 이 시점에서 유용한 개선 사항은 다음과 같습니다:

- 싫어하거나 알레르기가 있는 재료를 필터링합니다.
- 집에 없는 재료를 고려하여 쇼핑 목록을 작성합니다.

위의 경우에 대해 추가 프롬프트를 추가해봅시다:

> "마늘에 알레르기가 있으니 마늘이 들어간 레시피는 제거하고 다른 것으로 대체해주세요. 또한, 닭고기, 감자, 당근은 이미 집에 있으니 이를 고려하여 쇼핑 목록을 작성해주세요."

이제 새로운 결과가 나옵니다:

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

이것이 마늘이 언급되지 않은 다섯 가지 레시피이며, 집에 이미 있는 것을 고려한 쇼핑 목록도 있습니다.

## 연습 - 레시피 생성기 구축

이제 시나리오를 실행했으니, 시연된 시나리오에 맞는 코드를 작성해봅시다. 이를 위해 다음 단계를 따르세요:

1. 기존 _app.py_ 파일을 시작점으로 사용합니다
1. `prompt` 변수를 찾아 코드를 다음과 같이 변경합니다:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   이제 코드를 실행하면 다음과 유사한 출력을 볼 수 있습니다:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM은 비결정적이므로 프로그램을 실행할 때마다 다른 결과를 얻을 수 있습니다.

   좋습니다, 이제 어떻게 개선할 수 있는지 보겠습니다. 개선하기 위해서는 코드를 유연하게 만들어 재료와 레시피 수를 개선하고 변경할 수 있도록 해야 합니다.

1. 코드를 다음과 같이 변경합니다:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   코드를 테스트 실행하면 다음과 같을 수 있습니다:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 필터 및 쇼핑 목록 추가하여 개선하기

이제 레시피를 생성할 수 있는 작동하는 앱이 있으며, 사용자 입력에 따라 레시피 수와 사용되는 재료 모두 유연하게 설정할 수 있습니다.

이를 더욱 개선하기 위해 다음을 추가하고자 합니다:

- **재료 필터링**. 좋아하지 않거나 알레르기가 있는 재료를 필터링할 수 있기를 원합니다. 이를 위해 기존 프롬프트를 편집하고 다음과 같이 끝에 필터 조건을 추가할 수 있습니다:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  위에서는 프롬프트의 끝에 `{filter}`를 추가하고 사용자로부터 필터 값을 캡처합니다.

  프로그램을 실행할 때의 예시 입력은 다음과 같습니다:

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

  보시다시피 우유가 들어간 레시피는 모두 필터링되었습니다. 그러나 유당 불내증이 있는 경우 치즈가 들어간 레시피도 필터링하고 싶을 수 있으므로 명확해야 할 필요가 있습니다.

- **쇼핑 목록 작성**. 이미 집에 있는 것을 고려하여 쇼핑 목록을 작성하고자 합니다.

  이 기능을 위해 모든 것을 하나의 프롬프트로 해결하거나 두 개의 프롬프트로 나눌 수 있습니다. 후자의 접근 방식을 시도해 봅시다. 여기서는 추가 프롬프트를 추가하되, 이를 위해서는 첫 번째 프롬프트의 결과를 두 번째 프롬프트에 대한 컨텍스트로 추가해야 합니다.

  첫 번째 프롬프트의 결과를 출력하는 코드 부분을 찾아 그 아래에 다음 코드를 추가합니다:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  다음 사항에 유의하세요:

  1. 첫 번째 프롬프트의 결과를 새 프롬프트에 추가하여 새 프롬프트를 구성합니다:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 첫 번째 프롬프트에서 요청한 토큰 수를 고려하여 새 요청을 만듭니다. 이번에는 `max_tokens`를 1200으로 설정합니다.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     이 코드를 실행해 보면 다음과 같은 출력이 나옵니다:

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

지금까지 작동하는 코드를 가지고 있지만, 더 개선하기 위해 몇 가지 조정을 해야 합니다. 개선해야 할 사항은 다음과 같습니다:

- **코드에서 비밀 정보 분리하기**, API 키와 같은 비밀 정보. 비밀 정보는 코드에 포함되지 않고 안전한 위치에 저장되어야 합니다. 코드를 비밀 정보와 분리하기 위해 환경 변수와 `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` 파일과 같은 라이브러리를 사용할 수 있습니다. 다음 내용이 포함된 파일:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 참고, Azure의 경우 다음 환경 변수를 설정해야 합니다:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     코드에서는 다음과 같이 환경 변수를 로드합니다:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **토큰 길이에 대한 한마디**. 원하는 텍스트를 생성하기 위해 얼마나 많은 토큰이 필요한지 고려해야 합니다. 토큰은 비용이 들기 때문에 가능한 한 경제적으로 사용해야 합니다. 예를 들어, 프롬프트를 어떻게 표현하면 더 적은 토큰을 사용할 수 있을까요?

  사용되는 토큰을 변경하려면 `max_tokens` 매개변수를 사용할 수 있습니다. 예를 들어, 100개의 토큰을 사용하려면 다음과 같이 합니다:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **온도 실험하기**. 온도는 지금까지 언급하지 않았지만 프로그램 성능에 중요한 컨텍스트입니다. 온도 값이 높을수록 출력이 더 무작위가 됩니다. 반대로 온도 값이 낮을수록 출력이 더 예측 가능해집니다. 출력에서 변화를 원할지 여부를 고려하세요.

  온도를 변경하려면 `temperature` 매개변수를 사용할 수 있습니다. 예를 들어, 0.5의 온도를 사용하려면 다음과 같이 합니다:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 참고, 1.0에 가까울수록 출력이 더 다양해집니다.

## 과제

이번 과제에서는 무엇을 만들지 선택할 수 있습니다.

다음은 몇 가지 제안입니다:

- 레시피 생성 앱을 수정하여 더 개선해 보세요. 온도 값과 프롬프트를 실험하여 어떤 결과를 얻을 수 있는지 확인하세요.
- "공부 친구"를 만들어 보세요. 이 앱은 예를 들어 Python에 대한 질문에 답할 수 있어야 합니다. "Python의 특정 주제는 무엇인가요?"와 같은 프롬프트를 가질 수 있거나 특정 주제에 대한 코드를 보여달라는 프롬프트를 가질 수 있습니다.
- 역사 봇, 역사를 생생하게 만들어 보세요. 특정 역사적 인물을 연기하도록 봇에게 지시하고 그의 삶과 시대에 대해 질문하세요.

## 솔루션

### 공부 친구

아래는 시작 프롬프트입니다. 이를 사용하고 원하는 대로 조정해 보세요.

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

1. 출력의 무작위성을 제어합니다.
1. 응답의 크기를 제어합니다.
1. 사용되는 토큰 수를 제어합니다.

## 🚀 도전

과제를 수행할 때 온도를 다양하게 설정해 보세요. 0, 0.5, 1로 설정해 보세요. 0은 가장 덜 다양하고 1은 가장 다양합니다. 어떤 값이 앱에 가장 적합한지 확인해 보세요.

## 훌륭한 작업! 학습을 계속하세요

이 강의를 완료한 후 [Generative AI 학습 컬렉션](

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.