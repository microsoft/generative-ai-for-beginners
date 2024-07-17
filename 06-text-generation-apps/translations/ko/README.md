# 텍스트 생성 애플리케이션 개발

[![Building Text Generation Applications](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(위의 이미지를 클릭하여 이 수업의 동영상을 시청하세요.)_

지금까지 이 커리큘럼을 통해 프롬프트와 "프롬프트 엔지니어링"이라는 전체적인 개념과 같은 핵심 개념들을 보셨습니다. ChatGPT, Office 365, Microsoft Power Platform 등 다양한 도구들은 프롬프트를 사용하여 어떤 작업을 수행하는 데 도움을 주는 것을 확인하실 수 있습니다.

앱에 이러한 경험을 추가하려면 프롬프트, completion(완성어) 및 작업할 라이브러리와 관련된 개념을 이해해야 합니다. 이것이 바로 이번 장에서 배우게 될 내용입니다.

## 소개

이번 장에서는 다음을 하게 될 것입니다:

- OpenAI 라이브러리와 그 핵심 개념에 대해 학습합니다.
- OpenAI를 사용하여 텍스트 생성 앱을 개발합니다.
- 프롬프트, temperature(언어 생성 모델에서 생성된 텍스트의 다양성을 조절하는 하이퍼파라미터), 토큰과 같은 개념을 사용하여 텍스트 생성 앱을 구축하는 방법을 이해합니다.

## 학습 목표

이 장을 학습하고 나면 다음을 할 수 있게 될 것입니다:

- 텍스트 생성 앱이 무엇인지를 설명합니다.
- OpenAI를 사용하여 텍스트 생성 앱을 개발합니다.
- 앱을 더 많거나 더 적은 토큰을 사용하도록 구성하고, 또한 다양한 출력을 얻기 위해 temperature를 조절합니다.

## 텍스트 생성 애플리케이션이 무엇인가요?

일반적으로 앱을 개발할 때 다음과 같은 종류의 인터페이스가 있습니다:

- 명령 기반(Command-based): 콘솔 앱은 명령을 입력하고 해당 작업을 수행하는 전형적인 앱입니다. 예를 들어 git은 명령 기반 앱의 한 예입니다.
- 사용자 인터페이스 (UI): 일부 앱은 그래픽 사용자 인터페이스 (GUI)를 갖고 있습니다. 여기서는 버튼을 클릭하거나 텍스트를 입력하고 옵션을 선택하는 등의 작업을 수행합니다.

### 콘솔 및 UI 앱은 제한적입니다

명령 기반 앱에서 명령을 입력하는 것과 비교해보세요:

- **제한적입니다**. 모든 명령을 입력할 수 있는 것이 아니라, 앱이 지원하는 명령만 입력할 수 있습니다.
- **특정 언어에 한정됩니다**. 일부 앱은 여러 언어를 지원하지만, 기본적으로 앱은 특정 언어를 위해 구축되며, 추가적인 언어 지원이 가능한 경우에도 해당 언어에 한정됩니다.

### 텍스트 생성 앱의 장점

그렇다면 텍스트 생성 앱은 어떻게 다를까요?

텍스트 생성 앱에서는 더 많은 유연성을 가지며, 일련의 명령이나 특정 입력 언어에 제한되지 않습니다. 대신에 자연어를 사용하여 앱과 상호작용할 수 있습니다. 또 다른 장점은 이미 방대한 정보 코퍼스(말뭉치)로 훈련된 데이터 소스와 상호작용하고 있기 때문에, 전통적인 앱이 데이터베이스에 제한되는 것과는 달리 더 많은 가능성을 가집니다.

### 텍스트 생성 앱으로 무엇을 만들 수 있을까요?

많은 것들을 만들 수 있습니다. 예를 들어:

- **챗봇**. 회사와 제품에 대한 질문에 답변하는 챗봇을 만들 수 있습니다.
- **도움이 되는 도구**. LLM은 텍스트 요약, 텍스트에서 통찰력 얻기, 이력서와 같은 텍스트 생성 등에 뛰어납니다.
- **코드 어시스턴트**. 사용하는 언어 모델에 따라 코드 작성을 도와주는 코드 어시스턴트를 만들 수 있습니다. 예를 들어, GitHub Copilot과 ChatGPT와 같은 제품을 사용하여 코드 작성을 도와줄 수 있습니다.

## 어떻게 시작할 수 있을까요?

LLM과 통합하는 방법을 찾아야 합니다. 일반적으로 다음 두 가지 접근 방식을 사용합니다:

- API 사용. 여기서는 프롬프트와 함께 웹 요청을 생성하고 생성된 텍스트를 받아옵니다.
- 라이브러리 사용. 라이브러리는 API 호출을 캡슐화하고 사용하기 쉽게 만들어줍니다.

## 라이브러리/SDK

LLM과 작업하기 위해 몇 가지 잘 알려진 라이브러리가 있습니다:

- **openai**, 이 라이브러리는 모델에 연결하고 프롬프트를 보내는 것을 쉽게 만들어줍니다.

또한 다음과 같이 더 높은 수준에서 작동하는 라이브러리도 있습니다:

- **Langchain**. Langchain은 잘 알려진 라이브러리로, Python을 지원합니다.
- **Semantic Kernel**. Semantic Kernel은 Microsoft에서 지원하는 C#, Python, Java 등의 언어를 지원하는 라이브러리입니다.

## openai를 사용한 앱 개발

우리는 앱을 만드는 방법, 앱을 만들기 위해 어떤 라이브러리가 얼마나 필요한지 등을 살펴보겠습니다.

### openai 설치

OpenAI 또는 Azure OpenAI와 상호작용하기 위한 다양한 라이브러리가 있습니다. 그리고 이러한 다양한 라이브러리에서는 C#, Python, JavaScript, Java 등 다양한 프로그래밍 언어를 사용할 수도 있습니다. 저희는 `openai` Python 라이브러리를 사용하기로 선택했으므로, `pip`를 사용하여 설치하겠습니다.

```bash
pip install openai
```

### 리소스 생성

다음 단계를 수행해야 합니다:

- Azure에 계정을 만듭니다. [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)에서 계정을 만드세요.
- Azure Open AI에 액세스 권한을 얻으세요. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)로 이동하여 액세스를 요청하세요.

> [!NOTE]
> 작성 시점에서 Azure Open AI에 대한 액세스 신청이 필요합니다.

- Python을 설치합니다. <https://www.python.org/>
- Azure OpenAI 서비스 리소스를 생성했습니다. [리소스 생성 가이드](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)를 참조하세요.

### API 키와 엔드포인트 찾기

이 시점에서 `openai` 라이브러리에 사용할 API 키를 알려야 합니다. API 키를 찾으려면 Azure Open AI 리소스의 "Keys and Endpoint" 섹션으로 이동하고 "Key 1" 값을 복사하세요.

![Azure Portal의 Keys and Endpoint 리소스 블레이드](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

이제 이 정보를 복사했으니, 라이브러리에 사용하도록 지시합시다.

> [!NOTE]
> API 키를 코드와 분리하는 것이 좋습니다. 이를 위해 환경 변수를 사용할 수 있습니다.
>
> - 환경 변수 `OPENAI_API_KEY`를 API 키로 설정하세요.
>   `export OPENAI_API_KEY='sk-...'`

### Azure 설정 구성

Azure Open AI를 사용하는 경우, 다음과 같이 설정을 구성할 수 있습니다:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

위에서는 다음과 같이 설정하고 있습니다:

- `api_type`을 `azure`로 설정합니다. 이는 라이브러리가 OpenAI가 아닌 Azure Open AI를 사용하도록 지시합니다.
- `api_key`는 Azure Portal에서 찾을 수 있는 API 키입니다.
- `api_version`은 사용하려는 API의 버전입니다. 작성 시점에서 최신 버전은 `2023-05-15`입니다.
- `api_base`는 API의 엔드포인트입니다. API 키 옆에 Azure Portal에서 찾을 수 있습니다.

> [!NOTE] > `os.getenv`는 환경 변수를 읽는 함수입니다. `OPENAI_API_KEY`와 `API_BASE`와 같은 환경 변수를 읽을 때 사용할 수 있습니다. 이러한 환경 변수는 터미널에서 설정하거나 `dotenv`와 같은 라이브러리를 사용하여 설정할 수 있습니다.

## 텍스트 생성

텍스트를 생성하는 방법은 `Completion` 클래스를 사용하는 것입니다. 다음은 예시입니다:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

위의 코드에서는 완성 객체를 생성하고 사용할 모델과 프롬프트를 전달합니다. 그런 다음 생성된 텍스트를 출력합니다.

### 채팅 completions

지금까지 `Completion`을 사용하여 텍스트를 생성하는 방법을 살펴보았습니다. 그러나 챗봇에 더 적합한 `ChatCompletion`이라는 다른 클래스도 있습니다. 다음은 사용 예시입니다:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

이 기능에 대한 자세한 내용은 다음 장에서 다룰 예정입니다.

## 연습 - 첫 번째 텍스트 생성 앱

이제 openai를 설정하고 구성하는 방법을 배웠으니, 첫 번째 텍스트 생성 앱을 만들어 보는 시간입니다. 앱을 만들기 위해 다음 단계를 따르세요:

1. 가상 환경을 생성하고 openai를 설치하세요:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

> [!NOTE]
> Windows를 사용하는 경우 `source venv/bin/activate` 대신 `venv\Scripts\activate`를 입력하세요.

> [!NOTE]
> Azure Open AI 키를 찾으려면 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)로 이동하여 `Open AI`를 검색한 다음 `Open AI 리소스`를 선택하고 `Keys and Endpoint`를 선택하고 `Key 1` 값을 복사하세요.

1. _app.py_ 파일을 생성하고 다음 코드를 추가하세요:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure Open AI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make completion
   completion = openai.Completion.create(engine= deployment_name, model="davinci-002", prompt=prompt)

   # print response
   print(completion.choices[0].text)
   ```

> [!NOTE]
> Azure Open AI를 사용하는 경우, `api_type`을 `azure`로 설정하고 `api_key`를 Azure Open AI 키로 설정해야 합니다.

    다음과 같은 출력을 볼 수 있어야 합니다:

    ```output
     very unhappy _____.

    Once upon a time there was a very unhappy mermaid.
    ```

## 서로 다른 유형의 프롬프트를, 서로 다른 용도에 맞게

이제 프롬프트를 사용하여 텍스트를 생성하는 방법을 보았습니다. 심지어 다양한 유형의 텍스트를 생성하기 위해 수정하고 변경할 수 있는 프로그램이 작동 중입니다.

프롬프트는 다양한 작업에 사용할 수 있습니다. 예를 들어:

- **텍스트 유형 생성**. 시, 퀴즈 질문 등을 생성할 수 있습니다.
- **정보 조회**. '웹 개발에서 CORS는 무엇을 의미하는가?'와 같은 정보를 조회하는 데 프롬프트를 사용할 수 있습니다.
- **코드 생성**. 이메일 유효성 검사에 사용되는 정규식 또는 웹 앱과 같은 전체 프로그램을 생성하는 데 프롬프트를 사용할 수 있습니다.

## 더 실용적인 사용 사례: 레시피 생성기

가정에 있는 재료로 무언가 요리하고 싶을 때 레시피가 필요합니다. 레시피를 찾는 방법은 검색 엔진을 사용하거나 LLM을 사용할 수도 있습니다.

다음과 같은 프롬프트를 작성할 수 있습니다:

> "닭, 감자, 당근을 사용한 요리 5개를 보여주세요. 각 레시피에 사용된 모든 재료를 나열해주세요."

위의 프롬프트를 주면 다음과 유사한 응답을 받을 수 있습니다:

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

이 결과는 훌륭합니다. 무엇을 요리할지 알게 되었습니다. 이제 유용한 개선 사항은 다음과 같습니다:

- 싫어하는 재료나 알레르기가 있는 재료를 걸러내기.
- 재료가 부족한 경우를 대비해 쇼핑 목록을 작성하기.

위의 경우에 대해 추가적인 프롬프트를 추가해 보겠습니다:

> "대파를 대체할 다른 재료로 대체하고, 알레르기가 있는 사람을 위해 마늘이 포함된 레시피를 제거해주세요. 또한, 닭고기, 감자, 당근은 이미 집에 있으므로 쇼핑 목록을 작성해주세요."

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

이것이 당신의 다섯 가지 레시피입니다. 마늘은 포함되지 않았으며, 집에 이미 있는 재료를 고려한 쇼핑 목록도 있습니다.

## 연습 - 레시피 생성기 만들기

이제 우리가 시나리오를 플레이했으니, 해당 시나리오와 일치하는 코드를 작성해 봅시다. 다음 단계를 따라주세요:

1. 기존의 _app.py_ 파일을 시작점으로 사용합니다.
2. `prompt` 변수를 찾아서 다음과 같이 코드를 변경합니다:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   코드를 실행하면 다음과 유사한 출력이 표시됩니다:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 참고: LLM은 결정론적이지 않으므로 프로그램을 실행할 때마다 다른 결과를 얻을 수 있습니다.

   좋아요, 어떻게 개선할 수 있는지 알아봅시다. 개선하기 위해 코드가 유연하도록 만들어야 합니다. 따라서 재료와 레시피 수를 개선하고 변경할 수 있어야 합니다.

3. 다음과 같이 코드를 변경해 봅시다:

   ```python
   no_recipes = input("No of recipes (for example, 5: ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   코드를 테스트 실행하면 결과가 다음과 같을 수 있습니다:

   ```output
   No of recipes (for example, 5: 3
   List of ingredients (for example, chicken, potatoes, and carrots: milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 필터와 쇼핑 목록 추가로 개선하기

이제 우리는 레시피를 생성할 수 있는 작동하는 앱을 가지고 있으며, 이 앱은 사용자의 입력에 의존하여 레시피 수와 사용되는 재료를 유연하게 조정할 수 있습니다.

그리고 더 개선하기 위해 다음을 추가하고 싶습니다:

- **재료 필터링**. 싫어하는 재료나 알레르기 반응이 있는 재료를 필터링할 수 있도록 하고 싶습니다. 이 변경을 위해 기존의 프롬프트를 수정하여 끝에 필터 조건을 추가할 수 있습니다:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  위에서는 프롬프트 끝에 `{filter}`를 추가하고 사용자로부터 필터 값을 입력받도록 합니다.

  프로그램을 실행하는 예시 입력은 다음과 같을 수 있습니다:

  ```output
  No of recipes (for example, 5: 3
  List of ingredients (for example, chicken, potatoes, and carrots: onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free: no milk

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

  보시다시피, 우유가 들어간 레시피는 필터링되었습니다. 그러나 유당 불내증이 있다면 치즈가 들어간 레시피도 필터링하고 싶을 수 있으므로 명확하게 해야합니다.

- **쇼핑 목록 생성**. 우리는 이미 집에 있는 재료를 고려하여 쇼핑 목록을 생성하고 싶습니다.

  이 기능을 위해 우리는 하나의 프롬프트에서 모든 것을 해결하려고 시도할 수도 있고, 두 개의 프롬프트로 나눠서 해결할 수도 있습니다. 후자의 접근 방식을 시도해 보겠습니다. 여기서는 추가적인 프롬프트를 추가하는 것을 제안하고 있습니다. 그러나 이를 위해 이전 프롬프트의 결과를 후자의 프롬프트에 컨텍스트로 추가해야 합니다.

  코드에서 첫 번째 프롬프트의 결과를 출력하는 부분을 찾아서 다음 코드를 아래에 추가하세요:

  ```python
  old_prompt_result = completion.choices[0].text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].text)
  ```

  다음 사항을 주목하세요:

  1. 첫 번째 프롬프트의 결과를 새로운 프롬프트에 추가하여 새로운 프롬프트를 구성합니다:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  2. 첫 번째 프롬프트에서 요청한 토큰 수를 고려하여 새로운 요청을 만듭니다. 이번에는 `max_tokens`을 1200으로 설정합니다.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Taking this code for a spin, we now arrive at the following output:

     ```output
     No of recipes (for example, 5: 2
     List of ingredients (for example, chicken, potatoes, and carrots: apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free: sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 설정 개선하기

지금까지 작성한 코드는 작동하지만, 더 개선할 수 있는 몇 가지 조정 사항이 있습니다. 우리가 해야 할 몇 가지 작업은 다음과 같습니다:

- **비밀 정보와 코드 분리하기**, 예를 들어 API 키와 같은 비밀 정보는 코드에 포함되어서는 안 됩니다. 비밀 정보를 코드와 분리하기 위해 환경 변수와 `python-dotenv`와 같은 라이브러리를 사용하여 파일에서 로드할 수 있습니다. 코드에서 이렇게 구현할 수 있습니다:

  1. `.env` 파일을 다음 내용으로 생성하세요:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 참고로, Azure의 경우 다음 환경 변수를 설정해야 합니다:

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

- **토큰 길이에 대한 고려사항**. 우리는 원하는 텍스트를 생성하기 위해 얼마나 많은 토큰이 필요한지 고려해야 합니다. 토큰은 비용이 들기 때문에 가능한 경우, 토큰의 수를 절약할 수 있는 방법을 고려해야 합니다. 예를 들어, 프롬프트를 어떻게 구성하면 더 적은 토큰을 사용할 수 있을까요?

  사용할 토큰을 변경하려면 `max_tokens` 매개변수를 사용할 수 있습니다. 예를 들어, 100개의 토큰을 사용하려면 다음과 같이 할 수 있습니다:

  ```python
  completion = openai.Completion.create(model="davinci-002", prompt=prompt, max_tokens=100)
  ```

- **temperature 조절 실험**. temperature는 우리가 지금까지 언급하지 않았지만, 프로그램의 동작에 중요한 맥락입니다. temperature 값이 높을수록 출력이 더 무작위적이 됩니다. 반대로, temperature 값이 낮을수록 출력이 더 예측 가능해집니다. 출력에 변화를 원하는지 여부를 고려해보세요.

  temperature를 변경하려면 `temperature` 매개변수를 사용할 수 있습니다. 예를 들어, temperature를 0.5로 설정하려면 다음과 같이 할 수 있습니다:

  ```python
  completion = openai.Completion.create(model="davinci-002", prompt=prompt, temperature=0.5)
  ```

> 참고로, 값이 1.0에 가까울수록 출력이 더 다양해집니다.

## 과제

이 과제에서는 무엇을 구축할지 선택할 수 있습니다.

다음은 몇 가지 제안 사항입니다:

- 레시피 생성기 앱을 더 개선해 보세요. temperature 값과 프롬프트를 조정하여 어떤 결과를 얻을 수 있는지 확인해보세요.
- "스터디 버디"를 만들어 보세요. 이 앱은 Python과 같은 주제에 대한 질문에 답변할 수 있어야 합니다. "Python에서 특정 주제는 무엇인가요?"와 같은 프롬프트를 사용하거나, 특정 주제에 대한 코드를 보여달라는 프롬프트를 사용할 수도 있습니다.
- 역사 봇을 만들어 역사를 생생하게 만들어 보세요. 봇에게 특정 역사적 인물로 역할을 맡게 하고, 그 인물에 대한 생애와 시대에 대해 질문해 보세요.

## 정답 예시

### 스터디 버디

아래는 시작 프롬프트입니다. 이를 활용하고 원하는 대로 조정해보세요.

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

temperature 개념은 무엇을 하는 역할인가요?

1. 출력의 무작위성을 조절합니다.
2. 응답의 크기를 조절합니다.
3. 사용되는 토큰의 수를 조절합니다.

## 🚀 도전과제

과제를 수행할 때, temperature 값을 다양하게 변경해보세요. 0, 0.5, 1로 설정해보세요. 기억해주세요, 0은 가장 일정하고 1은 가장 다양한 값을 의미합니다. 어떤 값이 앱에 가장 적합한지 확인해보세요.

## 수고하셨습니다! 학습을 계속하세요

이 수업을 완료한 후에는 [Generative AI 학습 컬렉션](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)을 확인하여 Generative AI 지식을 더욱 향상시킬 수 있습니다!

7번 수업으로 이동하여 [채팅 애플리케이션을 구축하는 방법](../../../07-building-chat-applications/translations/ko/README.md?WT.mc_id=academic-105485-koreyst)을 살펴보세요!
