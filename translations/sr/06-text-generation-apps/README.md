# Израда апликација за генерисање текста

[![Израда апликација за генерисање текста](../../../translated_images/sr/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Кликните на слику горе да бисте погледали видео из ове лекције)_

До сада сте кроз овај план учења видели да постоје основни појмови као што су промптови и чак цела дисциплина названа „промпт инженеринг“. Многи алати са којима можете интераговати као што су ChatGPT, Office 365, Microsoft Power Platform и други, подржавају вас у коришћењу промптова за постизање нечега.

Да бисте додали такво искуство у апликацију, потребно је да разумете појмове као што су промптови, комплетирања и да одаберете библиотеку са којом ћете радити. Управо то ћете научити у овом поглављу.

## Увод

У овом поглављу ћете:

- Научити о библиотеци openai и њеним основним концептима.
- Направити апликацију за генерисање текста користећи openai.
- Разумети како да користите појмове као што су промпт, температура и токени за изградњу апликације за генерисање текста.

## Циљеви учења

На крају ове лекције моћи ћете да:

- Објасните шта је апликација за генерисање текста.
- Направите апликацију за генерисање текста користећи openai.
- Конфигуришете апликацију да користи више или мање токена и да мењате температуру за разноврснији излаз.

## Шта је апликација за генерисање текста?

Обично када правите апликацију, она има неки вид интерфејса као што је следеће:

- Командно засновани. Конзолне апликације су типичне апликације где укуцате команду и она извршава задатак. На пример, `git` је командно заснована апликација.
- Кориснички интерфејс (UI). Неке апликације имају графичке корисничке интерфејсе (GUI) где кликате на дугмад, уносите текст, бирате опције и више.

### Конзолне и UI апликације су ограничене

Упоредите то са командно заснованом апликацијом у којој куцате команду:

- **Ограничена је**. Не можете само написати било коју команду, већ само оне које апликација подржава.
- **Језички специфична**. Неке апликације подржавају многе језике, али по подразумеваној вредности апликација је направљена за одређени језик, чак и ако можете додати више језичке подршке.

### Предности апликација за генерисање текста

Како се онда апликација за генерисање текста разликује?

У апликацији за генерисање текста имате већу флексибилност, нисте ограничени на скуп команди или одређени улазни језик. Уместо тога, можете користити природни језик за интеракцију са апликацијом. Друга предност је што већ интерагујете са извором података који је трениран на огромном корпусу информација, док је традиционална апликација можда ограничена на оно што је у бази података.

### Шта могу направити са апликацијом за генерисање текста?

Можете направити много тога. На пример:

- **Чатбот**. Чатбот који одговара на питања о темама, као што су ваша компанија и њени производи, може бити добар избор.
- **Помоћник**. Велики језички модели (LLM) су сјајни за ствари као што су резимирање текста, добијање увида из текста, производњу текста као што су биографије и више.
- **Помоћник за код**. У зависности од језичког модела који користите, можете направити помоћника за код који вам помаже да пишете код. На пример, можете користити производ као што је GitHub Copilot као и ChatGPT да вам помогну у писању кода.

## Како могу почети?

Па, треба да пронађете начин да се интегришете са LLM који обично укључује двa приступа:

- Користите API. Овде конструишете веб захтеве са вашим промптом и добијате генерисани текст назад.
- Користите библиотеку. Библиотеке помажу да се API позиви упакују и учине их лакшим за коришћење.

## Библиотеке/SDK-ови

Постоји неколико добро познатих библиотеках за рад са LLM-овима као што су:

- **openai**, ова библиотека олакшава повезивање са вашим моделом и слање промптова.

Постоје и библиотеке које раде на вишем нивоу као што су:

- **Langchain**. Langchain је добро познат и подржава Python.
- **Semantic Kernel**. Semantic Kernel је библиотека од Microsoft-а која подржава језике C#, Python и Java.

## Прва апликација користећи openai

Хајде да видимо како можемо направити прву апликацију, које библиотеке су нам потребне, колико је потребно и тако даље.

### Инсталирај openai

Постоји много библиотека за интеракцију са OpenAI или Azure OpenAI. Могуће је користити различите програмске језике попут C#, Python, JavaScript, Java и других. Ми смо изабрали да користимо `openai` Python библиотеку, па ћемо користити `pip` за инсталацију.

```bash
pip install openai
```

### Креирај ресурс

Потребно је извршити следеће кораке:

- Креирајте налог на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Добијте приступ Azure OpenAI. Идите на [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и затражите приступ.

  > [!NOTE]
  > У време писања, потребно је да се пријавите за приступ Azure OpenAI.

- Инсталирајте Python <https://www.python.org/>
- Креирајте Azure OpenAI Service ресурс. Погледајте овај водич како [креирати ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Пронађите API кључ и крајњу тачку

У овом тренутку треба да кажете вашој `openai` библиотеци који API кључ да користи. Да бисте пронашли ваш API кључ, идите у одељак "Keys and Endpoint" вашег Azure OpenAI ресурса и копирајте вредност "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Сада када имате ову информацију, хајде да упутимо библиотеке да је користе.

> [!NOTE]
> Вредно је раздвојити ваш API кључ од вашег кода. То можете урадити коришћењем системских променљивих окружења.
>
> - Поставите променљиву окружења `OPENAI_API_KEY` на ваш API кључ.
>   `export OPENAI_API_KEY='sk-...'`

### Подешавање конфигурације Azure

Ако користите Azure OpenAI (сад део Microsoft Foundry), ево како подесити конфигурацију. Користимо стандардног `OpenAI` клијента усмереног на Azure OpenAI `/openai/v1/` крајњу тачку, који ради са Responses API и не захтева `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Горенаведено поставља следеће:

- `api_key`, ово је ваш API кључ пронађен у Azure порталу или Microsoft Foundry порталу.
- `base_url`, ово је крајња тачка вашег Foundry ресурса са додатком `/openai/v1/`. Стабилна v1 крајња тачка ради са OpenAI и Azure OpenAI без управљања `api_version`.

> [!NOTE] > `os.environ` чита променљиве окружења. Можете га користити за читање променљивих као што су `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Поставите те променљиве у вашем терминалу или уз помоћ библиотеке као што је `dotenv`.

## Генериши текст

Начин за генерисање текста је коришћење Responses API преко метода `responses.create`. Ево примера:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ово је име ваше имплементације модела
    input=prompt,
    store=False,
)
print(response.output_text)
```

У горе наведеном коду, правимо одговор и прослеђујемо модел који желимо да користимо и промпт. Затим исписујемо генерисани текст преко `response.output_text`.

### Разговори са више рунди

Responses API је добро погодан и за једнорундно генерисање текста и за вишерундне четботове - пружите листу порука у `input` за састављање разговора:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Више о овој функционалности у наредном поглављу.

## Вежба - ваша прва апликација за генерисање текста

Сада када смо научили како да подесимо и конфигуришемо openai, време је да направите своју прву апликацију за генерисање текста. Да бисте направили апликацију, следите ове кораке:

1. Направите виртуелно окружење и инсталирајте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако користите Windows, укуцајте `venv\Scripts\activate` уместо `source venv/bin/activate`.

   > [!NOTE]
   > Пронађите ваш Azure OpenAI кључ тако што ћете отићи на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) и потражити `Open AI`, изаберите `Open AI ресурс`, а затим изаберите `Keys and Endpoint` и копирајте вредност `Key 1`.

1. Креирајте фајл _app.py_ и у њега убаците следећи код:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # додајте ваш код за завршетак
   prompt = "Complete the following: Once upon a time there was a"

   # направите захтев користећи Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # испишите одговор
   print(response.output_text)
   ```

   > [!NOTE]
   > Ако користите обични OpenAI (не Azure), користите `client = OpenAI(api_key="<замените ову вредност вашим OpenAI кључем>")` (без `base_url`) и проследите име модела као што је `gpt-5-mini` уместо имена деплојмента.

   Требало би да видите излаз сличан следећем:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различите врсте промптова, за различите ствари

Сада сте видели како да генеришете текст користећи промпт. Чак имате програм који ради и који можете модификовати и мењати да генерише различите врсте текста.

Промптови могу да се користе за све врсте задатака. На пример:

- **Генеришите врсту текста**. На пример, можете генерисати песму, питања за квиз итд.
- **Претрага информација**. Можете користити промптове да тражите информације као у следећем примеру 'Шта значи CORS у веб развоју?'.
- **Генеришите код**. Можете користити промптове за генерисање кода, на пример развијајући регуларни израз који се користи за валидацију мејлова или чак генерисати цео програм, као што је веб апликација?

## Прагматичнији случај коришћења: генератор рецепата

Замислите да имате састојке код куће и желите да скувате нешто. За то вам треба рецепт. Начин да пронађете рецепте је да користите претраживач или да користите LLM.

Можете написати промпт овако:

> "Покажи ми 5 рецепата за јело са следећим састојцима: пилетина, кромпир и шаргарепа. За сваки рецепт наброј све састојке који се користе"

На основу горе наведеног промпта, могли бисте добити одговор сличан овоме:

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

Овај резултат је одличан, знам шта ћу да кувам. У овом тренутку корисна побољшања су:

- Филтрирање састојака које не волим или на које сам алергичан.
- Прављење листе за куповину, у случају да немам све састојке код куће.

За горе наведене случајеве, додајмо додатни промпт:

> "Молим уклони рецепте са белим луком јер сам алергичан и замени их нечим другим. Такође, направи листу за куповину за рецепте, имајући у виду да већ имам пилетину, кромпир и шаргарепу код куће."

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

То су ваших пет рецепата, без поменутог белог лука и имате листу за куповину с обзиром на оно што већ имате код куће.

## Вежба - направите генератор рецепата

Сада када смо одиграли сценарио, хајде да напишемо код који одговара демонстрираном сценарију. Да бисте то урадили, следите ове кораке:

1. Користите постојећи фајл _app.py_ као почетну тачку
1. Пронађите променљиву `prompt` и промените њен код у следећи:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ако сада покренете код, требало би да видите излаз сличан овоме:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > НАПОМЕНА, ваш LLM је нередуктиван, па можда добијете различите резултате сваки пут кад покренете програм.

   Одлично, хајде да видимо како можемо унапредити ствари. Да бисмо унапредили ствари, желимо да код буде флексибилан, тако да састојци и број рецепата могу да се промене и прилагоде.

1. Хајде да променимо код на следећи начин:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # интерполирај број рецепата у упит и састојке
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Узимајући код за тест покретање, могао би изгледати овако:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Унапреди додавањем филтера и листе за куповину

Сада имамо радну апликацију способну да производи рецепте и флексибилну је јер се ослања на уносе корисника, и за број рецепата и за састојке који се користе.

Даље побољшање подразумева додавање следећег:

- **Филтрирање састојака**. Желимо да можемо филтрирати састојке које не волимо или на које смо алергични. Да бисмо ово остварили, можемо изменити наш постојећи промпт и додати услов филтера на крају промпта овако:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Горенаведено додатно убацује `{filter}` на крај промпта и такође хвата вредност филтра од корисника.

  Пример уноса током покретања програма сада може изгледати овако:

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

  Као што видите, сви рецепти који садрже млеко су филтрирани. Али, ако сте нетолерантни на лактозу, можда ћете желети да филтрирате и рецепте који садрже сир, па је потребно бити јасан о томе.


- **Направите списак за куповину**. Желимо да направимо списак за куповину, узимајући у обзир шта већ имамо код куће.

  За ову функционалност, могли бисмо покушати да решимо све у једном упиту или да га поделимо у два упита. Хајде да покушамо са другом опцијом. Овде предлажемо додавање додатног упита, али да би то функционисало, морамо додати резултат првог упита као контекст другом упиту.

  Пронађите део у коду који исписује резултат из првог упита и додајте следећи код испод:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # испиши одговор
  print("Shopping list:")
  print(response.output_text)
  ```

  Обратите пажњу на следеће:

  1. Конструишемо нови упит додавањем резултата из првог упита у нови упит:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Правимо нови захтев, али такође узимајући у обзир број токена које смо тражили у првом упиту, па овог пута кажемо да је `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Испробавајући овај код, добијамо следећи излаз:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Побољшајте своје окружење

Досад имамо код који ради, али постоје нека подешавања која би требало урадити да бисмо ствари додатно побољшали. Неке ствари које треба урадити су:

- **Одвојите тајне од кода**, попут API кључа. Тајне не припадају у код и треба их чувати на безбедном месту. Да бисмо одвојили тајне од кода, можемо користити променљиве окружења и библиотеке као што је `python-dotenv` да их учитамо из фајла. Ево како то изгледа у коду:

  1. Направите `.env` фајл са следећим садржајем:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Напомена, за Azure OpenAI у Microsoft Foundry, уместо тога морате поставити следеће променљиве окружења:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     У коду, променљиве окружења бисте учитали овако:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Реч о дужини токена**. Требало би да размислимо колико токена је потребно за генерисање текста који желимо. Токени коштају новац, па где год је могуће, требало би да будемо економични у коришћењу броја токена. На пример, да ли можемо формулисати упит тако да користимо мање токена?

  Да бисте променили број коришћених токена, можете користити параметар `max_output_tokens`. На пример, ако желите да користите 100 токена, урадили бисте овако:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментисање са температуром**. Температура је нешто што до сада нисмо поменули, али је важан контекст како наш програм функционише. Што је температура већа, то је излаз насумичнији. Насупрот томе, што је температура нижа, излаз је предвидљивији. Размислите да ли желите варијације у свом излазу или не.

  Да бисте променили температуру, можете користити параметар `temperature`. На пример, ако желите да користите температуру 0.5, урадили бисте овако:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Напомена, што је ближе 1.0, излаз је разноликији.

- **Модели за расуђивање не користе `temperature`**. Ово је важна промена у 2026. Тренутни, не депрецирирани модели на Microsoft Foundry су **модели за расуђивање** (GPT-5 породице, o-серија) - и они **не подржавају `temperature` или `top_p`** (нити `max_tokens`; користити `max_output_tokens`). Ако пошаљете `temperature` ка `gpt-5-mini` добићете грешку "параметар није подржан". Дакле, да бисте испробали пример са температуром изнад, усмерите се на модел који и даље подржава контролу узорковања - на пример отворени **Llama** модел као `Llama-3.3-70B-Instruct` из [Microsoft Foundry модела каталога](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), позивајући га преко Foundry Models / Azure AI Inference ендеоинта (на исти начин као пример `githubmodels-*`). За моделе за расуђивање као GPT-5, контролишете излаз другачије:
  - **Инжењеринг упита (prompt engineering)** - јасна упутства, примери и структурисани излаз (погледајте лекцију [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) замењују функције које су раније обављали параметри узорковања.
  - **Контроле расуђивања** - параметри као што су напор/обим расуђивања тргују дубином расуђивања за латентност и трошак.

  Укратко: `temperature`/`top_p` су и даље валидни на многим моделима (Llama, Mistral, Phi, и GPT-4.x породици - мада GPT-4.x се депрецирира), али правац је инжењеринг упита + контроле расуђивања на моделима за расуђивање као што је GPT-5.

## Задатак

За овај задатак, можете изабрати шта ћете направити.

Ево неких предлога:

- Подесите апликацију генератора рецепата да је додатно побољшате. Играте се са вредностима температуре и упитима да видите шта можете добити.
- Направите "учног друга". Ова апликација треба да буде у стању да одговара на питања о одређеној теми, на пример Python, могли бисте имати упите као „Шта је одређена тема у Питону?“, или упит који каже, покажи ми код за одређену тему итд.
- Бот за историју, оживите историју, наложите боту да игра одређену историјску личност и питајте га питања о њеном животу и времену.

## Решење

### Учни друг

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

Шта ради концепт температура?

1. Контролише колико је излаз насумичан.
1. Контролише колико велики одговор је.
1. Контролише колико се токена користи.

## 🚀 Изазов

Док радите на задатку, покушајте да мењате температуру, покушајте да је подесите на 0, 0.5 и 1. Запамтите да је 0 најмање разнолико, а 1 највише. Која вредност најбоље функционише за вашу апликацију?

## Одличан посао! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да усавршавате своје знање о генеративној вештачкој интелигенцији!

Крените на Лекцију 7 где ћемо погледати како [правити апликације за ћаскање](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->