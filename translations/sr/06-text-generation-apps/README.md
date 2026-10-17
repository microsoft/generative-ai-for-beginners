# Прављење апликација за генерисање текста

[![Прављење апликација за генерисање текста](../../../translated_images/sr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Кликните на слику изнад да бисте погледали видео о овом часу)_

До сада сте кроз овај курикулум видели да постоје основни појмови као што су упити и чак читава дисциплина званa "производња упита". Многи алати са којима можете комуницирати попут ChatGPT-а, Office 365, Microsoft Power Platform и других, вам помажу користећи упите да постигнете нешто.

Да бисте такво искуство додали апликацији, потребно је да разумете појмове као што су упити, допуне и да одаберете библиотеку са којом ћете радити. Управо то ћете научити у овом поглављу.

## Увод

У овом поглављу ћете:

- Научити о библиотеци openai и њеним основним појмовима.
- Направити апликацију за генерисање текста користећи openai.
- Разумети како да користите појмове као што су упит, температура и токени за прављење апликације за генерисање текста.

## Циљеви учења

На крају овог часа, моћи ћете да:

- Објасните шта је апликација за генерисање текста.
- Направите апликацију за генерисање текста користећи openai.
- Конфигуришете апликацију да користи више или мање токена и такође промените температуру за разноврстан излаз.

## Шта је апликација за генерисање текста?

Обично када правите апликацију, она има неку врсту корисничког интерфејса као што је следеће:

- На бази команди. Конзолне апликације су типичне апликације где укуцате команду и она изврши задатак. На пример, `git` је апликација заснована на командама.
- Кориснички интерфејс (UI). Неке апликације имају графичке корисничке интерфејсе (GUI) где кликћете на дугмад, уносите текст, бирати опције и више.

### Конзолне и UI апликације су ограничене

Упоредите то са апликацијом заснованом на командама где куцате команду:

- **Оне су ограничене**. Не можете само унети било коју команду, већ само оне које апликација подржава.
- **Језички специфичне**. Неке апликације подржавају много језика, али апликација је по дифолту направљена за одређени језик, чак иако можете додати подршку за више језика.

### Предности апликација за генерисање текста

Како се онда апликација за генерисање текста разликује?

У апликацији за генерисање текста имате већу флексибилност, нисте ограничени на скуп команда или одређени улазни језик. Уместо тога, можете користити природни језик за интеракцију са апликацијом. Једна друга предност је што већ радите са извором података који је трениран на великом корпусу информација, док традиционална апликација може бити ограничена на оно што је у бази података.

### Шта могу направити са апликацијом за генерисање текста?

Постоји много ствари које можете направити. На пример:

- **Чет-бот**. Чет-бот који одговара на питања о темама, као што су ваша компанија и њени производи, може бити добра опција.
- **Помоћник**. Вели моћни језички модели (LLMs) су одлични у стварима као што су сажимање текста, добијање увида из текста, производњу текста попут биографија и више.
- **Помоћник за код**. У зависности од језичког модела који користите, можете направити помоћника за писање кода. На пример, можете користити производ попут GitHub Copilot и ChatGPT за помоћ у писању кода.

## Како да почнем?

Па, потребно је наћи начин да се интегришете са LLM-ом што обично подразумева следећа два приступа:

- Користите API. Овде конструишете веб захтеве са вашим упитом и добијате генерисани текст назад.
- Користите библиотеку. Библиотеке помажу да инкапсулирају API позиве и олакшавају коришћење.

## Библиотеке/SDK-ови

Постоји неколико познатих библиотека за рад са LLM-овима, као што су:

- **openai**, ова библиотека олакшава повезивање са вашим моделом и слање упита.

Онда постоје библиотеке које раде на вишем нивоу, као што су:

- **Langchain**. Langchain је добро познат и подржава Python.
- **Semantic Kernel**. Semantic Kernel је библиотека компаније Microsoft која подржава језике C#, Python и Java.

## Прва апликација користећи openai

Хајде да видимо како можемо направити нашу прву апликацију, које библиотеке нам требају, колико је потребно и тако даље.

### Инсталирање openai

Постоји много библиотека за интеракцију са OpenAI или Azure OpenAI. Могуће је користити различите програмске језике као што су C#, Python, JavaScript, Java и други. Одлучили смо да користимо `openai` Python библиотеку, па ћемо користити `pip` да је инсталирамо.

```bash
pip install openai
```

### Креирање ресурса

Потребно је обавити следеће кораке:

- Креирајте налог на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Приступите Azure OpenAI-ју. Идите на [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и затражите приступ.

  > [!NOTE]
  > У време писања, потребно је затражити приступ Azure OpenAI-ју.

- Инсталирајте Python <https://www.python.org/>
- Креирајте Azure OpenAI сервис ресурс. Погледајте овај водич како да [направите ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Лоцирање API кључа и крајње тачке

У овом тренутку морате својој `openai` библиотеци рећи који API кључ да користи. Да бисте пронашли свој API кључ, идите у одељак "Keys and Endpoint" вашег Azure OpenAI ресурса и копирајте вредност "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Сад кад имате те информације копиране, хајде да кажемо библиотекама да их користе.

> [!NOTE]
> Вреди раздвојити свој API кључ од кода. То можете урадити коришћењем променљивих окружења.
>
> - Поставите променљиву окружења `OPENAI_API_KEY` на свој API кључ.
>   `export OPENAI_API_KEY='sk-...'`

### Подешавање конфигурације Azure

Ако користите Azure OpenAI (сада део Microsoft Foundry), ево како подесити конфигурацију. Користимо стандардног `OpenAI` клијента усмереног на Azure OpenAI `/openai/v1/` крајњу точку, која ради са Responses API-јем и не захтева `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Горњим кодом подешавамо следеће:

- `api_key`, ово је ваш API кључ који се налази у Azure порталу или Microsoft Foundry порталу.
- `base_url`, ово је ваша Foundry ресурс крајња тачка са `/openai/v1/` додатом на крају. Стабилна v1 крајња тачка ради преко OpenAI и Azure OpenAI без потребе за `api_version` управљањем.

> [!NOTE] > `os.environ` чита променљиве окружења. Можете га користити за читање променљивих окружења као што су `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Подесите ове променљиве у терминалу или користећи библиотеку као што је `dotenv`.

## Генерисање текста

Начин генерисања текста је коришћење Responses API преко `responses.create` методе. Ево примера:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

У горњем коду креирамо одговор и прослеђујемо модел који желимо да користимо и упит. Затим исписујемо генерисани текст преко `response.output_text`.

### Разговори са више корака (multi-turn)

Responses API је погодан и за генерисање текста у једном кораку и за чет-ботове са више корака - прослеђујете листу порука у `input` да бисте изградили разговор:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Више о овој функцији у наредном поглављу.

## Вежба - ваша прва апликација за генерисање текста

Сада када смо научили како да подесимо и конфигуришемо openai, време је да направимо вашу прву апликацију за генерисање текста. За прављење апликације следите ове кораке:

1. Направите виртуелно окружење и инсталирајте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако користите Windows, уместо `venv\Scripts\activate` укуцајте `source venv/bin/activate`.

   > [!NOTE]
   > Пронађите свој Azure OpenAI кључ тако што ћете ићи на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) и потражити `Open AI`, затим изаберите `Open AI resource` и након тога `Keys and Endpoint` и копирајте вредност `Key 1`.

1. Направите _app.py_ фајл и ставите следећи код:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Ако користите обични OpenAI (не Azure), користите `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) и проследите име модела као `gpt-5-mini` уместо имена деплоја.

   Требало би да добијете излаз као следећи:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различите врсте упита, за различите ствари

Сада када сте видели како да генеришете текст користећи упит. Чак имате и програм који ради и који можете модификовати и мењати за генерисање различитих врста текста.

Упити се могу користити за разне задатке. На пример:

- **Генерисање врсте текста**. На пример, можете генерисати песму, питања за квиз и сл.
- **Претрага информација**. Можете користити упите да тражите информације као у примеру 'Шта значи CORS у веб развоју?'.
- **Генерисање кода**. Можете користити упите за генерисање кода, на пример за развој regular expression-а за валидацију електронских адреса или чак генерисање целе апликације, као веб апликације.

## Практични случај: генератор рецепата

Замислите да имате састојке код куће и желите нешто да скувате. За то вам треба рецепт. Један начин да пронађете рецепте је коришћење претраживача или можете користити LLM за то.

Можете написати упит овако:

> "Прикажи ми 5 рецепата за јело са следећим састојцима: пилеће месо, кромпир и шаргарепа. По рецепту, наброј све састојке који су коришћени"

На основу горе наведеног упита, добили бисте одговор сличан овоме:

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

Овај резултат је одличан, знам шта да кувам. У овом тренутку, корисна побољшања би могла бити:

- Филтрирање састојака које не волим или сам на њих алергичан.
- Прављење листе за куповину у случају да немам све састојке код куће.

За горе наведене случајеве, додајмо додатни упит:

> "Молим те уклони рецепте са бели лук јер сам алергичан и замени га нечим другим. Такође, направи листу за куповину за рецепте имајући у виду да већ имам пилеће месо, кромпир и шаргарепу код куће."

Сада имате нови резултат, наиме:

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

То су ваши пет рецепата, без бели лука и такође имате листу за куповину узимајући у обзир шта већ имате код куће.

## Вежба - направите генератор рецепата

Сада када смо прошли сценарио, хајде да напишемо код за приказани сценарио. Да бисте то урадили, следите ове кораке:

1. Користите постојећи _app.py_ фајл као почетну тачку
1. Пронађите променљиву `prompt` и промените њен код на следећи:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ако сада покренете код, требало би да добијете излаз као:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > НАПОМЕНА, ваш LLM је недетерминистички, па можда добијете различите резултате сваки пут када покренете програм.

   Одлично, хајде да видимо како можемо побољшати ствари. Да бисмо то урадили, желимо да код буде флексибилан, тако да се састојци и број рецепата могу побољшавати и мењати.

1. Променимо код на следећи начин:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Тест покретање кода може изгледати овако:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Побољшајте додавањем филтра и листе за куповину

Сада имамо радну апликацију која је способна да произведе рецепте и флексибилна је јер зависи од уноса корисника, како у броју рецепата, тако и у коришћеним састојцима.

Да бисмо је додатно побољшали, желимо да додамо следеће:

- **Филтрирање састојака**. Желимо да можемо филтрирати састојке које не волимо или на које смо алергични. За ову промену можемо уредити постојећи упит и на крај додати услов филтра као:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Горњим додамо `{filter}` на крај упита и такође добијамо вредност филтра од корисника.

  Пример уноса приликом покретања програма сада може изгледати овако:

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

  Као што видите, сви рецепти са млеком су филтрирани. Али, ако имате нетолеранцију на лактозу, можда ћете желети филтрирати и рецепте са сиром, па је потребно бити јасан у захтеву.

- **Прављење листе за куповину**. Желимо да направимо листу за куповину узимајући у обзир шта већ имамо код куће.

  За ову функцију можемо покушати да решимо све у једном упиту или можемо поделити на два упита. Покушаћемо ову другу опцију. Овде предлажемо додавање додатног упита, али за то да ради, морамо резултат првог упита користити као контекст у другом упиту.

  Пронађите део кода који штампа резултат првог упита и испод додајте следећи код:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Обратите пажњу на следеће:

  1. Конструишемо нови упит додавајући резултат првог упита у нови упит:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Правимо нови захтев, али такође узимајући у обзир број токена које смо тражили у првом упиту, па овог пута кажемо да је `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Покретањем овог кода доћи ћемо до следећег излаза:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Побољшајте своје подешавање

Оно што до сада имамо је код који ради, али постоје нека подешавања која бисмо требали урадити даље како бисмо унапредили ствари. Неке ствари које бисмо требали урадити су:

- **Одвојите тајне од кода**, попут API кључа. Тајне не припадају коду и треба их чувати на безбедном месту. Да бисмо одвојили тајне од кода, можемо користити променљиве окружења и библиотеке као што је `python-dotenv` да их учитамо из фајла. Ево како то изгледа у коду:

  1. Направите `.env` фајл са следећим садржајем:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Напомена, за Azure OpenAI у Microsoft Foundry, потребно је уместо тога поставити следеће променљиве окружења:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     У коду, променљиве окружења учитали бисте овако:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Реч о дужини токена**. Требало би да размотримо колико токена је потребно за генерисање текста који желимо. Токени коштају, па где год је могуће, требало би да будемо економичнији са бројем токена које користимо. На пример, можемо ли формулисати упит тако да користимо мање токена?

  Да бисте променили број коришћених токена, можете користити параметар `max_output_tokens`. На пример, ако желите да користите 100 токена, урадили бисте:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментисање са температуром**. Температура је нешто што до сада нисмо помињали, али је важан контекст за рад нашег програма. Што је вредност температуре већа, излаз ће бити насумичнији. Насупрот томе, што је температура нижа, излаз ће бити предвидљивији. Размислите да ли желите варијацију у вашем излазу или не.

  Да бисте изменили температуру, можете користити параметар `temperature`. На пример, ако желите да употребите температуру од 0.5, урадили бисте:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Напомена, што је ближе 1.0, излаз је разноврснији.

- **Разумевајући модели не користе `temperature`**. Ово је важна промена за 2026. Тренутни, незаобилазни модели на Microsoft Foundry су **модели размишљања** (породица GPT-5, o-series) - и они **не подржавају `temperature` или `top_p`** (нити `max_tokens`; користите `max_output_tokens`). Ако пошаљете `temperature` ка `gpt-5-mini` добићете грешку "параметар није подржан". Дакле, да бисте испробали пример температуре горе, усмерите га ка моделу који и даље подржава контролу узорковања - на пример отворени **Llama** модел као што је `Llama-3.3-70B-Instruct` из [Microsoft Foundry каталога модела](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), позван преко Foundry Models / Azure AI Inference крајње тачке (на исти начин као пример `githubmodels-*`). За моделе размишљања као GPT-5, излаз се управља другачије:
  - **Инжењеринг упита** - јасне инструкције, примери и структурисан излаз (погледајте лекцију [04 - Инжењеринг упита](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) раде посао који су контроле узорковања некада радиле.
  - **Контрола разумевања** - параметри као што су напор размишљања/детаљност размењују дубину размишљања са латенцијом и трошковима.

  Укратко: `temperature`/`top_p` су и даље важећи на многим моделима (Llama, Mistral, Phi и породица GPT-4.x - иако GPT-4.x је у фази прекидања подршке), али смер кретања је инжењеринг упита + контрола разумевања на моделима размишљања као GPT-5.

## Задатак

За овај задатак можете сами изабрати шта ћете направити.

Ево неких предлога:

- Подесите апликацију за генерисање рецепата да бисте је даље унапредили. Играјте се са вредностима температуре и упитима да видите шта можете да добијете.
- Направите „партнера за учење“. Ова апликација треба да буде у стању да одговара на питања о одређеној теми, на пример Python, где можете имати упите као „Шта је одређена тема у Python-у?“, или упит који каже, покажи ми код за одређену тему итд.
- Бот за историју, оживите историју, наредите боту да игра одређену историјску личност и постављајте му питања о њеном животу и времену.

## Решење

### Партнер за учење

Испод је почетни упит, видите како га можете користити и подесити по свом укусу.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Бот за историју

Ево неких упита које бисте могли користити:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Провера знања

Шта ради концепт температуре?

1. Контролише колико је излаз насумичан.
1. Контролише колика је величина одговора.
1. Контролише колико се токена користи.

## 🚀 Изазов

Када радите на задатку, покушајте да варирате температуру, подесите је на 0, 0.5 и 1. Запамтите да је 0 најмање варијабилна, а 1 највише. Која вредност најбоље функционише за вашу апликацију?

## Одличан посао! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [колекцију за учење генеративне AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бисте наставили да унапређујете своје знање о генеративној AI!

Идите на Лекцију 7 где ћемо погледати како да [правите апликације за ћаскање](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->