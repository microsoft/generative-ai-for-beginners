# Прављење апликација за генерисање текста

[![Прављење апликација за генерисање текста](../../../translated_images/sr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

Досад сте у овом курикулуму видели да постоје основни концепти као што су промпти и чак читава дисциплина која се зове "инжењеринг промпта". Многи алати са којима можете интерактивно радити као што су ChatGPT, Office 365, Microsoft Power Platform и други, подржавају коришћење промпта за постизање нечега.

Да бисте такво искуство додали апликацији, потребно је да разумете концепте као што су промпти, комплетирања и да одаберете библиотеку са којом ћете радити. Баш то ћете научити у овом поглављу.

## Увод

У овом поглављу ћете:

- Упознати се са библиотеком openai и њеним основним концептима.
- Направити апликацију за генерисање текста користећи openai.
- Разумети како се користе концепти као што су промпт, температура и токени за прављење апликације за генерисање текста.

## Циљеви учења

На крају ове лекције, моћи ћете да:

- Објасните шта је апликација за генерисање текста.
- Направите апликацију за генерисање текста користећи openai.
- Конфигуришете апликацију да користи више или мање токена и да промените температуру ради варирајућег излаза.

## Шта је апликација за генерисање текста?

Обично, када правите апликацију, она има неки облик интерфејса као што је следећи:

- На основу команди. Конзолне апликације су типичне апликације у којима уносите команду и она обавља задатак. На пример, `git` је апликација заснована на командама.
- Кориснички интерфејс (UI). Неке апликације имају графичке корисничке интерфејсе (GUI) где кликате на дугмад, уносите текст, бирати опције и друго.

### Конзолне и UI апликације су ограничене

Упоредите са апликацијом заснованом на командама у којој куцате команду:

- **Ограничене су**. Не можете само унети било коју команду, већ само оне које апликација подржава.
- **Специфичне за језик**. Неке апликације подржавају много језика, али по подразумеваној вредности апликација је направљена за одређени језик, чак и ако можете додати више језика.

### Предности апликација за генерисање текста

Како се онда апликација за генерисање текста разликује?

У апликацији за генерисање текста имате већу флексибилност, нисте ограничени скуповима команди или специфичним улазним језиком. Уместо тога, можете користити природни језик за интеракцију са апликацијом. Још једна предност је што већ интерактујете са извором података који је трениран на огромном корпусу информација, док традиционална апликација може бити ограничена тиме што има у бази података.

### Шта могу направити са апликацијом за генерисање текста?

Можете направити много тога. На пример:

- **Чатбот**. Чатбот који одговара на питања о темама, као што је ваша компанија и њени производи, може бити добар избор.
- **Помоћник**. ЛЛМ-ови су одлични за ствари као што су резимирање текста, добијање увида из текста, креирање текста као што су биографије и друго.
- **Асистент за кодирање**. У зависности од модела језика који користите, можете направити асистента за кодирање који вам помаже да пишете код. На пример, можете користити производе као што су GitHub Copilot и ChatGPT да вам помогну у писању кода.

## Како могу да почнем?

Па, потребно је да пронађете начин да се интегришете са ЛЛМ-ом, што обично подразумева две следеће приступе:

- Користите API. Овде конструишете веб-захтеве са вашим промптом и добијате генерисани текст назад.
- Користите библиотеку. Библиотеке помажу да се API позиви инкапсулирају и учине лакшим за коришћење.

## Библиотеке/SDK-ови

Постоји неколико добро познатих библиотека за рад са ЛЛМ-овима као што су:

- **openai**, ова библиотека олакшава повезивање са вашим моделом и слање промпта.

Постоје затим библиотеке које раде на вишем нивоу као што су:

- **Langchain**. Langchain је добро познат и подржава Python.
- **Semantic Kernel**. Semantic Kernel је библиотека компаније Microsoft која подржава језике C#, Python и Java.

## Прва апликација користећи openai

Хајде да видимо како да направимо нашу прву апликацију, које библиотеке нам требају, колико је потребно и тако даље.

### Инсталирање openai

Постоји много библиотека за интеракцију са OpenAI или Azure OpenAI. Такође је могуће користити више програмских језика као што су C#, Python, JavaScript, Java и други. Ми смо изабрали да користимо `openai` Python библиотеку, па ћемо користити `pip` да је инсталирамо.

```bash
pip install openai
```

### Креирање ресурса

Потребно је извршити следеће кораке:

- Креирати налог на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Добити приступ Azure OpenAI-у. Идите на [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и затражите приступ.

  > [!NOTE]
  > У време писања овог текста, потребно је пријавити се за приступ Azure OpenAI-у.

- Инсталирати Python <https://www.python.org/>
- Креирати ресурс Azure OpenAI сервиса. Погледајте овај водич како [креирати ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Пронађите API кључ и endpoint

У овом тренутку, потребно је да вашем `openai` библиотеци кажете који API кључ да користи. Да бисте пронашли API кључ, одете у одељак "Keys and Endpoint" вашег Azure OpenAI ресурса и копирате вредност "Key 1".

![Keys and Endpoint ресурс у Azure Portalu](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Сада када имате ове информације копиране, дајмо упутства библиотекама да их користе.

> [!NOTE]
> Вреди раздвојити ваш API кључ од вашег кода. То можете урадити коришћењем променљивих окружења.
>
> - Поставите променљиву окружења `OPENAI_API_KEY` на ваш API кључ.
>   `export OPENAI_API_KEY='sk-...'`

### Подешавање конфигурације за Azure

Ако користите Azure OpenAI (сад део Microsoft Foundry), ево како се подешава конфигурација. Користимо стандардног `OpenAI` клијента усмереног на Azure OpenAI `/openai/v1/` endpoint, који ради са Responses API-јем и не захтева `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Горње поставља следеће:

- `api_key`, то је ваш API кључ који се налази у Azure порталу или Microsoft Foundry порталу.
- `base_url`, то је ваш Foundry ресурс endpoint са додатком `/openai/v1/`. Стабилан v1 endpoint ради и са OpenAI и Azure OpenAI без управљања `api_version`.

> [!NOTE] > `os.environ` чита променљиве окружења. Можете га користити да читате променљиве окружења као што су `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Поставите ове променљиве окружења у вашем терминалу или користећи библиотеку као што је `dotenv`.

## Генерисање текста

Начин да се генерише текст је коришћењем Responses API преко метoде `responses.create`. Ево примера:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

У горе наведеном коду правимо одговор и прослеђујемо модел који желимо да користимо и промпт. Затим штампамо генерисани текст преко `response.output_text`.

### Вишекратне конверзације

Responses API је добро прилагођен како за једнократну генерисање текста тако и за вишекратне разговоре у чатботовима - пружате листу порука у `input` да бисте изградили конверзацију:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Више о овој функционалности у наредном поглављу.

## Вежба - ваша прва апликација за генерисање текста

Сада када смо научили како да подесимо и конфигуришемо openai, време је да направите своју прву апликацију за генерисање текста. Да бисте направили апликацију, следите ове кораке:

1. Креирајте виртуелно окружење и инсталирајте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако користите Windows, уместо `venv\Scripts\activate` унесите `source venv/bin/activate`.

   > [!NOTE]
   > Пронађите свој Azure OpenAI кључ тако што ћете посетити [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), потражити `Open AI` и изабрати `Open AI resource`, а затим изабрати `Keys and Endpoint` и копирати вредност `Key 1`.

1. Креирајте датотеку _app.py_ и ставите следећи код:

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
   > Ако користите чист OpenAI (не Azure), користите `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) и проследите име модела као што је `gpt-5-mini` уместо имена деплоја.

   Требало би да видите излаз као следећи:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различити типови промпта, за различите ствари

Сада сте видели како се генерише текст користећи промпт. Чак имате програм који ради и који можете модификовати и мењати да генерише различите типове текста.

Промпти се могу користити за све врсте задатака. На пример:

- **Генерисање врсте текста**. На пример, можете генерисати песму, питања за квиз итд.
- **Претраживање информација**. Можете користити промпте за проналажење информација као што је пример „Шта значи CORS у веб развоју?“.
- **Генерисање кода**. Можете користити промпте за генерисање кода, на пример за развој регуларног израза који служи за валидацију имејлова или зашто не генерисати целу програмску апликацију, као што је веб апликација?

## Практичнији пример: генератор рецепата

Замислите да имате састојке код куће и желите нешто да скувате. За то вам треба рецепт. Један начин да пронађете рецепте је коришћење претраживача, или можете користити ЛЛМ за то.

Можете написати промпт овако:

> "Покажи ми 5 рецепата за јело са следећим састојцима: пилетина, кромпир и шаргарепа. За сваки рецепт наведи све састојке који су коришћени."

Са горњим промптом, могао бисте добити сличан одговор као:

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

Оваквису резултати сјајни, знам шта да кувам. У овом тренутку, корисна побољшања могу бити:

- Филтрирање састојака које не волим или на које сам алергичан.
- Направити листу за куповину, у случају да немам све састојке код куће.

За горње случајеве, хајде да додамо додатни промпт:

> "Молим уклони рецепте који садрже бели лук јер сам алергичан и замени га нечим другим. Такође, направи листу за куповину за рецепте, имајући у виду да већ имам пилетину, кромпир и шаргарепу код куће."

Сада имате нови резултат, а то је:

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

То су ваших пет рецепата, без помена белог лука, и такође имате листу за куповину узимајући у обзир шта већ имате код куће.

## Вежба - направи генератор рецепата

Сада када смо одиграли сценарио, хајде да напишемо код који одговара представљеном сценарију. Да бисте то урадили, следите ове кораке:

1. Користите постојећу датотеку _app.py_ као почетну тачку
1. Пронађите променљиву `prompt` и промените њен код у следеће:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ако сада покренете код, требало би да видите излаз сличан овом:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > НАПОМЕНА, ваш ЛЛМ је недетерминистички, па можете добити различите резултате сваки пут када покренете програм.

   Одлично, хајде да видимо како можемо побољшати ствари. Да бисмо их побољшали, желимо да код буде флексибилан, тако да састојци и број рецепата могу бити лако побољшани и промењени.

1. Променимо код на следећи начин:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Тест покретње кода могао би изгледати овако:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Побољшати додавањем филтра и листе за куповину

Сада имамо радну апликацију способну да прави рецепте и флексибилна је јер зависи од уноса корисника, како у броју рецепата, тако и састојака који се користе.

Да бисмо је додатно побољшали, желимо да додамо следеће:

- **Филтрирање састојака**. Желимо да можемо филтрирати састојке које не волимо или на које смо алергични. Да бисмо то постигли, можемо изменити наш постојећи промпт и додати услов филтра на крају промпта овако:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Горње додамо `{filter}` на крају промпта и такође унесемо вредност филтра корисника.

  Пример улаза при покретању програма сада може изгледати овако:

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

  Као што видите, рецепти који садрже млеко су филтрирани. Али, ако сте нетолерантни на лактозу, можда желите да филтрирате рецепте који садрже сир, па је потребно бити јасан.

- **Прављење листе за куповину**. Желимо направити листу за куповину узимајући у обзир шта већ имамо код куће.

  За ову функционалност, могли бисмо покушати све решити у једном промпту или да поделимо на два промпта. Покушајмо овај други приступ. Предлажемо додавање додатног промпта, али да би то функционисало, потребно је резултат првог промпта додати као контекст другом промпту.

  Пронађите део кода који штампа резултат из првог промпта и испод додајте следећи код:

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

  1. Конструишемо нови промпт додавањем резултата из првог промпта у нови промпт:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Правимо нови захтев, али и рачунајући број токена који смо тражили у првом промпту, тако да овај пут кажемо да је `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Када покренемо овај код, добијамо следећи излаз:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Побољшајте своју конфигурацију

Оно што имамо до сада је код који ради, али постоје неки подешавања која бисмо требали урадити даље да побољшамо ствари. Неке ствари које бисмо требали урадити су:

- **Одвојити тајне од кода**, као што је API кључ. Тајне не припадају у код и треба их чувати на безбедном месту. Да бисмо одвојили тајне од кода, можемо користити променљиве окружења и библиотеке као што је `python-dotenv` да их учитамо из фајла. Ево како би то изгледало у коду:

  1. Направите фајл `.env` са следећим садржајем:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Напомена, за Azure OpenAI у Microsoft Foundry, уместо тога треба подесити следеће променљиве окружења:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     У коду бисте учитали променљиве окружења овако:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Реч о дужини токена**. Требало би да размислимо колико токена нам је потребно да генеришемо жељени текст. Токени коштају, па где год је могуће, требало би бити економичан са бројем токена које користимо. На пример, можемо ли формулисати упит тако да користимо мање токена?

  Да бисте променили број коришћених токена, можете користити параметар `max_output_tokens`. На пример, ако желите да користите 100 токена, урадили бисте:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментисање са температуром**. Температура је нешто што до сада нисмо споменули, али је важан контекст за то како наш програм функционише. Што је температура већа, излаз је хаотичнији. Супротно, што је температура нижа, излаз је предвидљивији. Размислите да ли желите варијацију у вашем излазу или не.

  Да бисте променили температуру, можете користити параметар `temperature`. На пример, ако желите да користите температуру од 0.5, урадили бисте:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Напомена, што је ближе 1.0, излаз је разноликији.

- **Разумевајући да модели за закључивање не користе `temperature`**. Ово је важан помак у 2026. Тренутни, незаобилазни модели на Microsoft Foundry су **модели за закључивање** (породица GPT-5, o-серија) - и они **не подржавају `temperature` или `top_p`** (нити `max_tokens`; користите `max_output_tokens`). Ако пошаљете `temperature` на `gpt-5-mini` добићете грешку "параметар није подржан". Тако да ако желите пробати пример са температуром горе, усмерите га ка моделу који још увек подржава контроле узорковања - на пример отворени **Llama** модел као што је `Llama-3.3-70B-Instruct` из [Microsoft Foundry каталога модела](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), позван преко Foundry Models / Azure AI Inference крајње тачке (на исти начин као и `githubmodels-*` примери). За моделе за закључивање попут GPT-5, управљате излазом другачије:
  - **Инжењеринг упита** - јасна упутства, примери и структурирани излаз (погледајте лекцију [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) обављају посао који су некада радили подешавачи узорковања.
  - **Контрола закључивања** - параметри као што су улагање напора/в verbosity балансирају дубину закључивања у односу на латенцију и трошкове.

  Укратко: `temperature`/`top_p` су још увек валидни код многих модела (Llama, Mistral, Phi, и породице GPT-4.x - иако GPT-4.x се постепено укида), али правац развоја је инжењеринг упита + контрола закључивања на моделима за закључивање као што је GPT-5.

## Задатак

За овај задатак можете одабрати шта ћете направити.

Ево неких предлога:

- Побољшати апликацију за генерисање рецепата. Играјте се са вредностима температуре и упитима да бисте видели шта можете да смислите.
- Направите "практичног колегу за учење". Ова апликација би требало да буде у стању да одговара на питања о теми, на пример Python, могли бисте имати упите као што су "Шта је одређена тема у Python-у?", или упит који каже, покажи ми код за одређену тему итд.
- Бот за историју, оживите историју, наредите боту да игра одређеног историјског лика и питајте га о његовом животу и времену.

## Решење

### Практични колега за учење

Испод је почетни упит, видите како га можете користити и прилагодити по свом укусу.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Бот за историју

Ево неколико упита које бисте могли користити:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Провера знања

Шта ради концепт температуре?

1. Контролише колико је излаз случајан.
1. Контролише колико је одговор велики.
1. Контролише колико токена се користи.

## 🚀 Изазов

Док радите на задатку, покушајте да вариирате температуру, покушајте да је поставите на 0, 0.5, и 1. Запамтите да је 0 најмање варијабилна, а 1 највише. Која вредност најбоље функционише за вашу апликацију?

## Сјајан рад! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бисте наставили да унапређујете своје знање о генеративној вештачкој интелигенцији!

Пребаците се на Лекцију 7 где ћемо погледати како да [правимо апликације за ћаскање](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->