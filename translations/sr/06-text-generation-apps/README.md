# Израда апликација за генерисање текста

[![Израда апликација за генерисање текста](../../../translated_images/sr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

До сада сте видели у овом курикулуму да постоје кључни концепти као што су упити и чак цела дисциплина која се зове "инжењеринг упита". Многи алати са којима можете комуницирати као што су ChatGPT, Office 365, Microsoft Power Platform и други, подржавају вас у коришћењу упита да постижете нешто.

Да бисте додали такво искуство апликацији, морате разумети концепте као што су упити, комплетирања и изабрати библиотеку за рад. Управо то ћете научити у овом поглављу.

## Увод

У овом поглављу ћете:

- Научити о библиотеци openai и њеним основним концептима.
- Направити апликацију за генерисање текста користећи openai.
- Разумети како користити концепте као што су упит, температура и токени да бисте направили апликацију за генерисање текста.

## Циљеви учења

На крају ове лекције, моћи ћете да:

- Објасните шта је апликација за генерисање текста.
- Направите апликацију за генерисање текста користећи openai.
- Конфигуришете апликацију да користи више или мање токена и такође промените температуру, за разноврснији резултат.

## Шта је апликација за генерисање текста?

Обично, када правите апликацију, она има неки вид интерфејса као што је следећи:

- Командно-линијски. Конзолне апликације су типичне апликације где укуцате команду и она извршава задатак. На пример, `git` је командно-линијска апликација.
- Кориснички интерфејс (UI). Неке апликације имају графички кориснички интерфејс (GUI) где кликате на дугмад, уносите текст, бирајте опције и више.

### Конзолне и UI апликације имају ограничења

Упоредите то са командно-линијском апликацијом кад куцате команду:

- **Ограничено је**. Не можете унети било коју команду, само оне које апликација подржава.
- **Језички специфично**. Неки програми подржавају више језика, али по подразумеваној вредности апликација је направљена за одређени језик, чак и ако можете додати подршку за више језика.

### Предности апликација за генерисање текста

Како се онда апликација за генерисање текста разликује?

У апликацији за генерисање текста имате већу флексибилност, нисте ограничени на скуп команди или одређени улазни језик. Уместо тога, можете користити природни језик за интеракцију са апликацијом. Још једна предност је што већ комуницирате са извором података који је обучен на огромном корпусу информација, док традиционална апликација може бити ограничена на оно што је у бази података.

### Шта могу направити помоћу апликације за генерисање текста?

Постоји много ствари које можете направити. На пример:

- **Чет-бот**. Чет-бот који одговара на питања о темама, као што су ваша компанија и њени производи, могао би бити добар избор.
- **Помоћник**. Велику улогу LLM-ови имају у задацима као што су сажимање текста, извлачење увида из текста, прављење текстова као што су биографије и више.
- **Асистент за код**. У зависности од језичког модела који користите, можете направити асистента за писање кода. На пример, можете користити производ као GitHub Copilot као и ChatGPT који вам помаже у писању кода.

## Како да почнем?

Па, морате наћи начин да се интегришете са LLM-ом, што обично подразумева следећа два приступа:

- Користите API. Овде правите веб захтеве са вашим упитом и добијате генерисани текст као одговор.
- Користите библиотеку. Библиотеке помажу да се API позиви инкапсулирају и да буду лакши за коришћење.

## Библиотеке/SDK-ови

Постоји неколико познатих библиотека за рад са LLM-овима као што су:

- **openai**, ова библиотека олакшава повезивање са вашим моделом и слање упита.

Затим постоје библиотеке које раде на вишем нивоу као што су:

- **Langchain**. Langchain је познат и подржава Python.
- **Semantic Kernel**. Semantic Kernel је библиотека компаније Microsoft која подржава језике C#, Python и Java.

## Прва апликација користећи openai

Хајде да видимо како да направимо нашу прву апликацију, које библиотеке нам требају, колико је потребно и тако даље.

### Инсталирање openai

Постоји много библиотека за интеракцију са OpenAI или Azure OpenAI. Могуће је користити и различите програмске језике као што су C#, Python, JavaScript, Java и више. Ми смо изабрали да користимо `openai` Python библиотеку, тако да ћемо користити `pip` за њену инсталацију.

```bash
pip install openai
```

### Креирање ресурса

Морате извршити следеће кораке:

- Креирајте налог на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Добите приступ Azure OpenAI. Идите на [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и захтевате приступ.

  > [!NOTE]
  > У време писања овог текста, потребно је да поднесете захтев за приступ Azure OpenAI-у.

- Инсталирајте Python <https://www.python.org/>
- Креирали сте ресурс Azure OpenAI сервиса. Погледајте овај водич како да [направите ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Пронађите API кључ и крајњу тачку

У овом тренутку, морате рећи вашој `openai` библиотеци који API кључ да користи. Да бисте пронашли ваш API кључ, идите у одељак "Keys and Endpoint" ваше Azure OpenAI услуге и копирајте вредност "Key 1".

![Keys and Endpoint resource blade у Azure порталу](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Сада када имате ове информације копиране, дајмо библиотекама инструкције да их користе.

> [!NOTE]
> Вреди раздвојити ваш API кључ од кода. То можете учинити коришћењем системских променљивих околине.
>
> - Поставите системску променљиву `OPENAI_API_KEY` на ваш API кључ.
>   `export OPENAI_API_KEY='sk-...'`

### Подешавање Azure конфигурације

Ако користите Azure OpenAI (сада део Microsoft Foundry), ево како подесити конфигурацију. Користимо стандардног `OpenAI` клијента усмереног на Azure OpenAI `/openai/v1/` крајњу тачку, који ради са Responses API-јем и не захтева `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Горњи код подешава следеће:

- `api_key`, ово је ваш API кључ пронађен у Azure порталу или Microsoft Foundry порталу.
- `base_url`, ово је крајња тачка Foundry ресурса са додатком `/openai/v1/`. Стабилна v1 крајња тачка ради и са OpenAI и Azure OpenAI без потребе за управљањем `api_version`.

> [!NOTE] > `os.environ` чита системске променљиве околине. Можете га користити за читање променљивих као што су `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Поставите ове променљиве у вашем терминалу или коришћењем библиотеке као `dotenv`.

## Генерисање текста

Начин за генерисање текста је коришћење Responses API преко `responses.create` методе. Ево примера:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

У горе наведеном коду, креирамо одговор и шаљемо модел који желимо да користимо и упит. Затим исписујемо генерисани текст преко `response.output_text`.

### Разговори са више корака

Responses API је погодан и за генерацију текста у једном кораку и за чет-ботове са више корака - достављате листу порука у `input` да бисте изградили разговор:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Више о овој функционалности у наредном поглављу.

## Вежба – ваша прва апликација за генерисање текста

Сада када смо научили како подесити и конфигурисати openai, време је да направите вашу прву апликацију за генерисање текста. Да бисте направили апликацију, пратите ове кораке:

1. Креирајте виртуелно окружење и инсталирајте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако користите Windows, уместо `venv\Scripts\activate` укуцајте `source venv/bin/activate`.

   > [!NOTE]
   > Пронађите ваш Azure OpenAI кључ тако што ћете отићи на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), тражити `Open AI`, изабрати `Open AI resource`, затим изабрати `Keys and Endpoint` и копирати вредност `Key 1`.

1. Креирајте фајл _app.py_ и унесите следећи код:

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
   > Ако користите обични OpenAI (не Azure), користите `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) и уместо имена распореда унесите име модела попут `gpt-5-mini`.

   Требало би да видите излаз као следећи:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различите врсте упита, за различите задатке

Сада када сте видели како да генеришете текст помоћу упита, имате програм који ради и који можете изменити и прилагодити за генерисање различитих врста текста.

Упити се могу користити за све врсте задатака. На пример:

- **Генерисање врсте текста**. На пример, можете генерисати песму, питања за квиз итд.
- **Тражење информација**. Можете користити упите за претрагу информација као у следећем примеру 'Шта значи CORS у веб развоју?'.
- **Генерисање кода**. Можете користити упите за генерисање кода, на пример за развој регулярних израза за валидацију имејлова или чак за генерисање целе апликације као што је веб апликација.

## Практичнији пример: генератор рецепата

Замислите да имате састојке код куће и желите нешто да скувате. За то вам треба рецепт. Начин да пронађете рецепте је коришћење претраживача или можете користити LLM да то урадите.

Можете написати упит овако:

> "Прикажи ми 5 рецепата за јело са следећим састојцима: пилетина, кромпир и шаргарепа. По рецепту наброј све коришћене састојке"

Уз тај упит, можете добити одговор сличан овом:

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

Овај резултат је сјајан, знам шта да кувам. У овом тренутку, корисне надоградње могу бити:

- Филтрирање састојака које не волим или на које сам алергичан.
- Прављење листе за куповину, у случају да немам све састојке код куће.

За горе наведене случајеве, додамо још један упит:

> "Молим уклони рецепте са белим луком јер сам алергичан и замени их нечим другим. Такође, направи листу за куповину за рецепте, имајући у виду да већ имам пилетину, кромпир и шаргарепу код куће."

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

То су ваши пет рецепата, без белог лука у њима и имате листу за куповину имајући у виду шта већ имате код куће.

## Вежба – направите генератор рецепата

Сада када смо разиграли сценарио, хајде да напишемо код који одговара приказаном сценарију. Да бисте то урадили, пратите ове кораке:

1. Користите постојећи фајл _app.py_ као полазну основу
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

   > НАПОМЕНА, ваш LLM није детерминистички, па можете добијати различите резултате сваки пут кад покренете програм.

   Сјајно, видимо како можемо унапредити ствари. Да бисмо унапредили ствари, желимо да обезбедимо флексибилност кода, како би се састојци и број рецепата могли лако мењати.

1. Хајде да променимо код на следећи начин:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Тестирање тог кода може изгледати овако:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Унапређивање додавањем филтера и листе за куповину

Сада имамо радну апликацију која може да прави рецепте и флексибилна је јер се ослања на уносе корисника, и за број рецепата и за коришћене састојке.

Да бисмо додатно унапредили апликацију, желимо да додамо следеће:

- **Филтрирање састојака**. Желимо да можемо филтрирати састојке које не волимо или на које смо алергични. Да бисмо то постигли, можемо изменити постојећи упит додавши услов за филтер на крају, овако:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Горњи код додаје `{filter}` на крај упита и такође хвата вредност филтера од корисника.

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

  Као што видите, рецепти који садрже млеко су филтрирани. Али, ако сте нетолерантни на лактозу, можда ћете желети филтрирати и рецепте са сиром, па је важно бити јасан.

- **Прављење листе за куповину**. Желимо да направимо листу за куповину имајући у виду шта већ имамо код куће.

  За ову функционалност можемо покушати да све решимо једним упитом или да га растемо на два упита. Покушаћемо овај други приступ. Овде предлажемо додавање додатног упита, али да би то функционисало, морамо резултат првог упита додати као контекст другом.

  Пронађите део кода који исписује резултат првог упита и испод додајте следећи код:

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

  1. Конструишемо нови упит додавањем резултата из првог упита у нови упит:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Пошиљамо нови захтев, али такође узимајући у обзир број токена које смо тражили у првом упиту, овог пута кажемо да је `max_output_tokens` 1200.

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

## Унапредите своју конфигурацију

Оно што до сада имамо је код који ради, али постоје неке измене које бисмо требали урадити да бисмо ствари додатно побољшали. Неке ствари које бисмо требали урадити су:

- **Одвојити тајне од кода**, као што је API кључ. Тајне не припадају коду и треба их чувати на безбедном месту. Да бисмо одвојили тајне од кода, можемо користити променљиве окружења и библиотеке као што је `python-dotenv` за учитавање из фајла. Ево како то изгледа у коду:

  1. Направите фајл `.env` са следећим садржајем:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Напомена, за Azure OpenAI у Microsoft Foundry, уместо тога морате подесити следеће променљиве окружења:

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

- **Реч о дужини токена**. Требало би да размислимо колико токена нам је потребно да генеришемо текст који желимо. Токени коштају, па бисмо где је могуће требали бити штедљиви у броју коришћених токена. На пример, можемо ли формулисати промпт тако да користимо мање токена?

  За промену броја коришћених токена можете користити параметар `max_output_tokens`. На пример, ако желите да користите 100 токена, урадили бисте:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментисање са температуром**. Температура је нешто што до сада нисмо помињали, али је важан параметар за рад нашег програма. Што је вредност температуре већа, резултат је насумичнији. Супротно томе, што је температура нижа, резултат је предвидљивији. Размислите да ли желите варијацију у свом резултату или не.

  За промену температуре можете користити параметар `temperature`. На пример, ако желите температуру 0.5, урадили бисте:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Напомена, што је ближе 1.0, резултат ће бити разноврснији.

- **Разлозни модели не користе `temperature`**. Ово је важна промена за 2026. Тренутни, не застарели модели у Microsoft Foundry су **модели за расуђивање** (породица GPT-5, o-series) - и они **не подржавају `temperature` или `top_p`** (нити `max_tokens`; користите `max_output_tokens`). Ако пошаљете `temperature` у `gpt-5-mini` добићете грешку "параметар није подржан". Дакле, да бисте испробали пример са температуром горе, усмерите га на модел који и даље подржава контроле узорковања - на пример отворени **Llama** модел као што је `Llama-3.3-70B-Instruct` из [каталога модела Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), позван преко Foundry Models / Azure AI Inference ендпоинта (на исти начин као `githubmodels-*` узорци). За разложне моделе као што је GPT-5, излаз се управља другачије:
  - **Инжењеринг промпта** - јасна упутства, примери и структурирани излаз (погледајте лекцију [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) раде посао који су раније радили параметри узорковања.
  - **Контроле расуђивања** - параметри као што су напор/детаљност расуђивања балансирају дубину расуђивања и латенцију и трошкове.

  Укратко: `temperature`/`top_p` су и даље валидни на многим моделима (Llama, Mistral, Phi и породица GPT-4.x - мада GPT-4.x се одустаје), али смер је ка инжењерингу промпта + контролама расуђивања на разложним моделима као што је GPT-5.

## Задатак

За овај задатак можете изабрати шта ћете направити.

Ево неких предлога:

- Подесите апликацију генератора рецепата да је додатно побољшате. Играјте се са вредностима температуре и промптима да видите шта можете постићи.
- Направите "помоћника за учење". Ова апликација треба да буде у стању да одговара на питања о теми, на пример Python, са промптима као што су "Шта је одређена тема у Python-у?", или да има промпт који каже, покажи ми код за одређену тему итд.
- Бот за историју, оживите историју, наредите боту да игра одређени историјски лик и питајте га о његовом животу и времену.

## Решење

### Помагач у учењу

Испод је почетни промпт, видите како га можете користити и прилагодити по свом укусу.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Бот за историју

Ево неких промпта које можете користити:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Провера знања

Шта ради концепт температуре?

1. Контролише колико је излаз насумичан.
1. Контролише колико је одговор обиман.
1. Контролише колико се токена користи.

## 🚀 Изазов

Током рада на задатку, покушајте да мењате температуру, поставите је на 0, 0.5 и 1. Запамтите да је 0 најмање разноврсна, а 1 највише. Која вредност најбоље функционише за вашу апликацију?

## Одличан посао! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да наставите да унапређујете своје знање о генеративној вештачкој интелигенцији!

Пређите на Лекцију 7 где ћемо погледати како да [направите апликације за чет](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->