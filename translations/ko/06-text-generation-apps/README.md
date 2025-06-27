<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:08:57+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ko"
}
-->
# 텍스트 생성 애플리케이션 구축

[![텍스트 생성 애플리케이션 구축](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ko.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(위의 이미지를 클릭하면 이 강의의 비디오를 볼 수 있습니다)_

지금까지 이 커리큘럼을 통해 프롬프트와 "프롬프트 엔지니어링"이라는 전체 분야와 같은 핵심 개념을 보았습니다. ChatGPT, Office 365, Microsoft Power Platform 등과 같은 도구를 사용하여 프롬프트를 통해 무언가를 달성할 수 있습니다.

앱에 이러한 경험을 추가하려면 프롬프트, 완료와 같은 개념을 이해하고 사용할 라이브러리를 선택해야 합니다. 이 장에서 바로 그 점을 배울 것입니다.

## 소개

이 장에서 당신은:

- openai 라이브러리와 그 핵심 개념에 대해 배웁니다.
- openai를 사용하여 텍스트 생성 앱을 구축합니다.
- 프롬프트, 온도, 토큰과 같은 개념을 사용하여 텍스트 생성 앱을 구축하는 방법을 이해합니다.

## 학습 목표

이 강의가 끝나면, 당신은:

- 텍스트 생성 앱이 무엇인지 설명할 수 있습니다.
- openai를 사용하여 텍스트 생성 앱을 구축할 수 있습니다.
- 앱을 구성하여 더 많은 또는 더 적은 토큰을 사용하고 출력의 다양성을 위해 온도를 변경할 수 있습니다.

## 텍스트 생성 앱이란 무엇인가?

보통 앱을 구축할 때 다음과 같은 인터페이스를 가집니다:

- 명령 기반. 콘솔 앱은 일반적으로 명령을 입력하면 작업을 수행하는 앱입니다. 예를 들어, `git`는 명령 기반 앱입니다.
- 사용자 인터페이스 (UI). 일부 앱은 버튼을 클릭하고, 텍스트를 입력하고, 옵션을 선택하는 등 그래픽 사용자 인터페이스(GUI)를 가지고 있습니다.

### 콘솔 및 UI 앱의 한계

명령을 입력하는 명령 기반 앱과 비교해 보세요:

- **제한적입니다**. 앱이 지원하는 명령만 입력할 수 있습니다.
- **언어 특정적입니다**. 일부 앱은 여러 언어를 지원하지만 기본적으로 앱은 특정 언어에 맞춰져 있으며, 추가 언어 지원을 추가할 수 있습니다.

### 텍스트 생성 앱의 이점

그렇다면 텍스트 생성 앱은 어떻게 다른가요?

텍스트 생성 앱에서는 더 많은 유연성을 가지고 있으며, 특정 명령 세트나 특정 입력 언어에 제한되지 않습니다. 대신 자연어를 사용하여 앱과 상호작용할 수 있습니다. 또 다른 이점은 이미 방대한 정보 코퍼스에 대해 훈련된 데이터 소스와 상호작용하기 때문에 전통적인 앱이 데이터베이스에 제한될 수 있는 것과 다릅니다.

### 텍스트 생성 앱으로 무엇을 만들 수 있나요?

만들 수 있는 것이 많습니다. 예를 들어:

- **챗봇**. 회사와 그 제품에 대한 질문을 대답하는 챗봇은 좋은 선택일 수 있습니다.
- **도우미**. LLM은 텍스트 요약, 텍스트에서 인사이트 얻기, 이력서와 같은 텍스트 생성 등에서 훌륭합니다.
- **코드 어시스턴트**. 사용하는 언어 모델에 따라 코드를 작성하는 데 도움을 주는 코드 어시스턴트를 만들 수 있습니다. 예를 들어 GitHub Copilot과 ChatGPT를 사용하여 코드를 작성하는 데 도움을 받을 수 있습니다.

## 어떻게 시작할 수 있나요?

일반적으로 LLM과 통합하는 방법을 찾아야 하며, 이는 다음 두 가지 접근 방식을 포함합니다:

- API 사용. 여기서 프롬프트와 함께 웹 요청을 작성하고 생성된 텍스트를 반환받습니다.
- 라이브러리 사용. 라이브러리는 API 호출을 캡슐화하고 사용하기 쉽게 만듭니다.

## 라이브러리/SDK

LLM을 다루기 위한 몇 가지 잘 알려진 라이브러리가 있습니다:

- **openai**, 이 라이브러리는 모델에 쉽게 연결하고 프롬프트를 보낼 수 있게 합니다.

그리고 더 높은 수준에서 작동하는 라이브러리가 있습니다:

- **Langchain**. Langchain은 잘 알려져 있으며 Python을 지원합니다.
- **Semantic Kernel**. Semantic Kernel은 Microsoft가 지원하는 라이브러리로 C#, Python, Java 언어를 지원합니다.

## 첫 번째 앱 만들기 openai 사용

첫 번째 앱을 어떻게 만들 수 있는지, 필요한 라이브러리가 무엇인지, 얼마나 필요한지 등을 살펴보겠습니다.

### openai 설치

OpenAI 또는 Azure OpenAI와 상호작용하기 위한 많은 라이브러리가 있습니다. C#, Python, JavaScript, Java 등 다양한 프로그래밍 언어를 사용할 수 있습니다. 우리는 `openai` Python 라이브러리를 선택했으므로 `pip`를 사용하여 설치할 것입니다.

```bash
pip install openai
```

### 리소스 생성

다음 단계를 수행해야 합니다:

- Azure 계정 생성 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI에 접근 권한 얻기. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)로 이동하여 접근 요청하기.

  > [!NOTE]
  > 작성 시점에서 Azure OpenAI에 접근하려면 신청해야 합니다.

- Python 설치 <https://www.python.org/>
- Azure OpenAI 서비스 리소스를 생성했습니다. [리소스 생성](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)에 대한 가이드를 참조하세요.

### API 키 및 엔드포인트 찾기

이 시점에서 `openai` 라이브러리에 사용할 API 키를 알려야 합니다. API 키를 찾으려면 Azure OpenAI 리소스의 "키 및 엔드포인트" 섹션으로 이동하여 "키 1" 값을 복사하세요.

![Azure 포털의 키 및 엔드포인트 리소스 블레이드](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

이 정보를 복사했으므로 라이브러리가 이를 사용하도록 지시해 봅시다.

> [!NOTE]
> API 키를 코드에서 분리하는 것이 좋습니다. 환경 변수를 사용하여 수행할 수 있습니다.
>
> - 환경 변수 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`를 설정하세요.

### Azure 구성 설정

Azure OpenAI를 사용하는 경우 구성 설정 방법은 다음과 같습니다:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

위에서는 다음을 설정하고 있습니다:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` 클래스. 다음은 예시입니다:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

위 코드에서는 사용하고자 하는 모델과 프롬프트를 전달하여 완료 객체를 생성한 후 생성된 텍스트를 출력합니다.

### 채팅 완료

지금까지 `Completion` to generate text. But there's another class called `ChatCompletion`을 사용하여 채팅봇에 더 적합한 방법을 보았습니다. 다음은 그것을 사용하는 예입니다:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

이 기능에 대한 자세한 내용은 다음 장에서 다룹니다.

## 연습 - 첫 번째 텍스트 생성 앱

이제 openai 설정 및 구성을 배웠으므로 첫 번째 텍스트 생성 앱을 구축할 시간입니다. 앱을 구축하려면 다음 단계를 따르세요:

1. 가상 환경을 만들고 openai를 설치합니다:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows를 사용하는 경우 `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` 값을 입력하세요.

1. _app.py_ 파일을 만들고 다음 코드를 입력하세요:

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

   다음과 같은 출력이 표시되어야 합니다:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 다양한 작업을 위한 다양한 프롬프트 유형

이제 프롬프트를 사용하여 텍스트를 생성하는 방법을 보았습니다. 다양한 유형의 텍스트를 생성하기 위해 수정하고 변경할 수 있는 프로그램도 실행 중입니다.

프롬프트는 다양한 작업에 사용할 수 있습니다. 예를 들어:

- **텍스트 유형 생성**. 예를 들어, 시를 생성하거나 퀴즈를 위한 질문을 생성할 수 있습니다.
- **정보 조회**. '웹 개발에서 CORS는 무엇을 의미하나요?'와 같은 정보를 찾기 위해 프롬프트를 사용할 수 있습니다.
- **코드 생성**. 예를 들어 이메일 유효성을 검사하는 정규 표현식을 개발하거나 웹 앱과 같은 전체 프로그램을 생성하는 등 코드를 생성하기 위해 프롬프트를 사용할 수 있습니다.

## 더 실용적인 사용 사례: 레시피 생성기

집에 있는 재료로 요리를 하고 싶다고 상상해보세요. 이를 위해 레시피가 필요합니다. 레시피를 찾는 방법은 검색 엔진을 사용하는 것이나 LLM을 사용하는 것입니다.

다음과 같은 프롬프트를 작성할 수 있습니다:

> "닭고기, 감자, 당근을 사용한 요리의 레시피 5개를 보여주세요. 각 레시피에 사용된 모든 재료를 나열하세요."

위의 프롬프트를 통해 다음과 같은 응답을 받을 수 있습니다:

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

이 결과는 훌륭합니다. 이제 무엇을 요리할지 알 수 있습니다. 이 시점에서 유용한 개선점은 다음과 같습니다:

- 좋아하지 않거나 알레르기가 있는 재료를 필터링합니다.
- 집에 없는 재료가 있을 경우 쇼핑 목록을 만듭니다.

위의 경우에 대해 추가 프롬프트를 추가해 봅시다:

> "마늘에 알레르기가 있으므로 마늘이 포함된 레시피를 제거하고 다른 것으로 대체해 주세요. 또한, 집에 이미 닭고기, 감자, 당근이 있는 것을 고려하여 레시피에 필요한 쇼핑 목록을 작성해 주세요."

이제 새로운 결과가 있습니다:

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

이것이 마늘이 언급되지 않은 5개의 레시피이며, 집에 이미 있는 것을 고려한 쇼핑 목록도 있습니다.

## 연습 - 레시피 생성기 구축

이제 시나리오를 실행해 보았으니, 시연된 시나리오에 맞는 코드를 작성해 봅시다. 이를 위해 다음 단계를 따르세요:

1. 기존 _app.py_ 파일을 시작점으로 사용합니다.
1. `prompt` 변수를 찾아 다음 코드로 변경합니다:

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

   > 참고: LLM은 비결정적이므로 프로그램을 실행할 때마다 다른 결과를 얻을 수 있습니다.

   좋습니다, 이제 개선할 수 있는 방법을 봅시다. 개선하려면 코드가 유연하여 재료와 레시피 수를 개선하고 변경할 수 있도록 하고 싶습니다.

1. 코드를 다음과 같이 변경해 봅시다:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   테스트 실행을 위한 코드는 다음과 같을 수 있습니다:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 필터 및 쇼핑 목록 추가하여 개선

이제 레시피를 생성할 수 있는 작동하는 앱이 있으며, 사용자 입력에 따라 유연하게 작동합니다. 레시피 수뿐만 아니라 사용된 재료도 입력받습니다.

이를 더욱 개선하기 위해 다음을 추가하고자 합니다:

- **재료 필터링**. 좋아하지 않거나 알레르기가 있는 재료를 필터링할 수 있도록 하고 싶습니다. 이 변경을 달성하기 위해 기존 프롬프트를 편집하고 끝에 필터 조건을 추가할 수 있습니다:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  위에서는 `{filter}`를 프롬프트 끝에 추가하고 사용자로부터 필터 값을 캡처합니다.

  프로그램을 실행할 때의 예제 입력은 다음과 같습니다:

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

  보시다시피 우유가 포함된 레시피는 모두 필터링되었습니다. 그러나 유당 불내증이 있는 경우 치즈가 포함된 레시피도 필터링하고 싶을 수 있으므로 명확히 할 필요가 있습니다.

- **쇼핑 목록 작성**. 집에 이미 있는 것을 고려하여 쇼핑 목록을 작성하고 싶습니다.

  이 기능을 위해 모든 것을 하나의 프롬프트로 해결하려고 시도할 수 있거나 두 개의 프롬프트로 나눌 수 있습니다. 후자의 접근 방식을 시도해 봅시다. 여기서는 추가 프롬프트를 추가하는 것을 제안하지만, 이를 위해서는 첫 번째 프롬프트의 결과를 두 번째 프롬프트에 대한 컨텍스트로 추가해야 합니다.

  첫 번째 프롬프트의 결과를 출력하는 코드 부분을 찾아 아래의 코드를 추가합니다:

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

  다음을 주의하세요:

  1. 첫 번째 프롬프트의 결과를 새로운 프롬프트에 추가하여 새로운 프롬프트를 구성하고 있습니다:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 첫 번째 프롬프트에서 요청한 토큰 수를 고려하여 새로운 요청을 하며, 이번에는 `max_tokens`를 1200으로 설정합니다.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
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

## 설정 개선

지금까지 작동하는 코드가 있지만, 몇 가지 개선을 통해 더 나은 결과를 얻을 수 있습니다. 우리가 해야 할 몇 가지 사항은 다음과 같습니다:

- **코드에서 비밀 분리**, 예를 들어 API 키. 비밀은 코드에 속하지 않으며 안전한 위치에 저장되어야 합니다. 코드에서 비밀을 분리하려면 환경 변수와 `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` 파일과 같은 라이브러리를 사용할 수 있습니다:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 참고: Azure의 경우 다음 환경 변수를 설정해야 합니다:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     코드에서는 환경 변수를 다음과 같이 로드합니다:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **토큰 길이에 대한 한마디**. 필요한 텍스트를 생성하기 위해 얼마나 많은 토큰이 필요한지 고려해야 합니다. 토큰은 비용이 발생하므로 가능한 한 적은 토큰을 사용하는 것이 경제적입니다. 예를 들어, 프롬프트를 어떻게 표현하여 적은 토큰을 사용할 수 있을까요?

  사용된 토큰을 변경하려면 `max_tokens` 매개변수를 사용할 수 있습니다. 예를 들어 100개의 토큰을 사용하려면 다음과 같이 합니다:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **온도 실험**. 온도는 지금까지 언급하지 않았지만 프로그램의 성능에 중요한 맥락입니다. 온도 값이 높을수록 출력이 더 랜덤해집니다. 반대로 온도 값이 낮을수록 출력이 더 예측 가능해집니다. 출력에 변화를 원하는지 여부를 고려하세요.

  온도를 변경하려면 `temperature` 매개변수를 사용할 수 있습니다. 예를 들어 온도를 0.5로 설정하려면 다음과 같이 합니다:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 참고: 1.0에 가까울수록 출력이 더 다양해집니다.

## 과제

이 과제에서는 무엇을 만들지 선택할 수 있습니다.

다음은 몇 가지 제안입니다:

- 레시피 생성기 앱을 조정하여 더 개선해 보세요. 온도 값과 프롬프트를 실험하여 어떤 결과를 얻을 수 있는지 보세요.
- "공부 친구"를 만들어 보세요. 이 앱은 예를 들어 Python과 같은 주제에 대한 질문에 답할 수 있어야 합니다. "Python에서 특정 주제는 무엇인가요?"와 같은 프롬프트를 가질 수 있으며, 특정 주제에 대한 코드를 보여달라는 프롬프트도 가질 수 있습니다.
- 역사 봇을 만들어 역사를 생생하게 만들어 보세요. 봇에게 특정 역사적 인물을 연기하도록 지시하고 그의 삶과 시대에 대한 질문을 해보세요.

## 솔루션

### 공부 친구

아래는 시작 프롬프트입니다. 사용하여 원하는 대로 조정해 보세요.

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

1. 출력의 무작위성을 제어합니다.
1. 응답의 크기를 제어합니다.
1. 사용된 토큰 수를 제어합니다.

## 🚀 도전 과제

과제를 수행할 때 온도를 다양하게 설정해 보세요. 0, 0.5, 1로 설정해 보세요. 0은 가장 적게 변하고 1은 가장 많이 변한다는 것을 기억하세요. 앱에 가장 잘 맞는 값은 무엇인가요?

## 훌륭한 작업! 학습을 계속하세요

이 강의를 완료한 후, [Generative AI Learning collection](https

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만 자동 번역은 오류나 부정확성을 포함할 수 있습니다. 원본 문서는 해당 언어로 작성된 것이 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인적 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.