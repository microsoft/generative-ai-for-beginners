<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T12:09:21+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sr"
}
-->
# Израда апликација за генерисање текста

[![Израда апликација за генерисање текста](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.sr.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

До сада сте у овом курикулуму видели да постоје основни појмови као што су промптови и чак цела дисциплина која се зове „prompt engineering“. Многи алати са којима можете да комуницирате, као што су ChatGPT, Office 365, Microsoft Power Platform и други, подржавају коришћење промптова да бисте нешто постигли.

Да бисте такво искуство додали у апликацију, потребно је да разумете појмове као што су промптови, комплетирања и да одаберете библиотеку за рад. Управо то ћете научити у овом поглављу.

## Увод

У овом поглављу ћете:

- Упознати се са библиотеком openai и њеним основним појмовима.
- Направити апликацију за генерисање текста користећи openai.
- Разумети како да користите појмове као што су prompt, temperature и tokens за израду апликације за генерисање текста.

## Циљеви учења

На крају ове лекције моћи ћете да:

- Објасните шта је апликација за генерисање текста.
- Направите апликацију за генерисање текста користећи openai.
- Конфигуришете апликацију да користи више или мање токена и да мењате температуру ради различитих резултата.

## Шта је апликација за генерисање текста?

Обично када правите апликацију, она има неки вид интерфејса као што је следеће:

- Командна линија. Конзолне апликације су типичне апликације у којима укуцате команду и она изврши задатак. На пример, `git` је апликација заснована на командама.
- Кориснички интерфејс (UI). Неке апликације имају графички кориснички интерфејс (GUI) где кликате на дугмад, уносите текст, бирајте опције и слично.

### Конзолне и UI апликације имају ограничења

Упоредите то са апликацијом заснованом на командама у којој укуцате команду:

- **Ограничено је**. Не можете унети било коју команду, већ само оне које апликација подржава.
- **Језички специфично**. Неке апликације подржавају више језика, али по дефаулту су направљене за одређени језик, чак и ако можете додати подршку за друге језике.

### Предности апликација за генерисање текста

Како се онда апликација за генерисање текста разликује?

У апликацији за генерисање текста имате већу флексибилност, нисте ограничени на скуп команда или одређени улазни језик. Уместо тога, можете користити природни језик за интеракцију са апликацијом. Још једна предност је што већ комуницирате са извором података који је обучен на огромном корпусу информација, док традиционална апликација може бити ограничена на оно што је у бази података.

### Шта могу да направим са апликацијом за генерисање текста?

Постоји много ствари које можете направити. На пример:

- **Чатбот**. Чатбот који одговара на питања о темама као што су ваша компанија и њени производи може бити добар избор.
- **Помоћник**. LLM модели су одлични за ствари као што су сажимање текста, извлачење увида из текста, креирање текста као што су биографије и још много тога.
- **Асистент за кодирање**. У зависности од језичког модела који користите, можете направити асистента за кодирање који вам помаже да пишете код. На пример, можете користити производе као што су GitHub Copilot или ChatGPT да вам помогну у писању кода.

## Како да почнем?

Потребно је да пронађете начин да се интегришете са LLM моделом, што обично подразумева два приступа:

- Користите API. Овде конструишете веб захтеве са вашим промптом и добијате генерисани текст као одговор.
- Користите библиотеку. Библиотеке помажу да се API позиви обављају лакше и једноставније.

## Библиотеке/SDK-ови

Постоји неколико добро познатих библиотека за рад са LLM моделима као што су:

- **openai**, ова библиотека олакшава повезивање са вашим моделом и слање промптова.

Постоје и библиотеке које раде на вишем нивоу као што су:

- **Langchain**. Langchain је добро познат и подржава Python.
- **Semantic Kernel**. Semantic Kernel је библиотека компаније Microsoft која подржава језике C#, Python и Java.

## Прва апликација користећи openai

Хајде да видимо како можемо направити нашу прву апликацију, које библиотеке су нам потребне, колико је тога потребно и тако даље.

### Инсталирање openai

Постоји много библиотека за интеракцију са OpenAI или Azure OpenAI. Могуће је користити различите програмске језике као што су C#, Python, JavaScript, Java и други. Ми смо изабрали да користимо `openai` Python библиотеку, па ћемо је инсталирати помоћу `pip`.

```bash
pip install openai
```

### Креирање ресурса

Потребно је да урадите следеће кораке:

- Креирајте налог на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Добијте приступ Azure OpenAI. Идите на [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и затражите приступ.

  > [!NOTE]
  > У време писања, потребно је да поднесете захтев за приступ Azure OpenAI.

- Инсталирајте Python <https://www.python.org/>
- Креирајте Azure OpenAI Service ресурс. Погледајте овај водич како да [креирате ресурс](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Пронађите API кључ и endpoint

Сада морате да кажете `openai` библиотеци који API кључ да користи. Да бисте пронашли свој API кључ, идите у одељак „Keys and Endpoint“ вашег Azure OpenAI ресурса и копирајте вредност „Key 1“.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Када сте копирали ове податке, упутимо библиотеке да их користе.

> [!NOTE]
> Вредно је раздвојити ваш API кључ од кода. То можете урадити коришћењем променљивих окружења.
>
> - Поставите променљиву окружења `OPENAI_API_KEY` на ваш API кључ.
>   `export OPENAI_API_KEY='sk-...'`

### Подешавање конфигурације за Azure

Ако користите Azure OpenAI, ево како да подесите конфигурацију:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Горњи код подешава следеће:

- `api_type` на `azure`. Ово говори библиотеци да користи Azure OpenAI, а не OpenAI.
- `api_key`, ваш API кључ који сте пронашли у Azure порталу.
- `api_version`, верзија API-ја коју желите да користите. У време писања, најновија верзија је `2023-05-15`.
- `api_base`, endpoint API-ја. Можете га пронаћи у Azure порталу поред вашег API кључа.

> [!NOTE] > `os.getenv` је функција која чита променљиве окружења. Можете је користити да прочитате променљиве као што су `OPENAI_API_KEY` и `API_BASE`. Поставите ове променљиве у вашем терминалу или користећи библиотеку као што је `dotenv`.

## Генерисање текста

Начин да генеришете текст је коришћењем класе `Completion`. Ево примера:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

У горњем коду креирамо објекат за комплетирање и прослеђујемо модел који желимо да користимо и промпт. Затим исписујемо генерисани текст.

### Чат комплетирања

До сада сте видели како користимо `Completion` за генерисање текста. Али постоји још једна класа која се зове `ChatCompletion` и која је погоднија за чатботове. Ево примера коришћења:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Више о овој функционалности у неком од наредних поглавља.

## Вежба – ваша прва апликација за генерисање текста

Сада када смо научили како да подесимо и конфигуришемо openai, време је да направите своју прву апликацију за генерисање текста. Да бисте направили апликацију, пратите ове кораке:

1. Креирајте виртуелно окружење и инсталирајте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако користите Windows укуцајте `venv\Scripts\activate` уместо `source venv/bin/activate`.

   > [!NOTE]
   > Пронађите свој Azure OpenAI кључ тако што ћете отићи на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), претражити `Open AI`, изабрати `Open AI resource`, а затим ући у `Keys and Endpoint` и копирати вредност `Key 1`.

1. Креирајте фајл _app.py_ и убаците следећи код:

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
   > Ако користите Azure OpenAI, потребно је да поставите `api_type` на `azure` и `api_key` на ваш Azure OpenAI кључ.

   Требало би да видите излаз сличан овом:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различите врсте промптова за различите намене

Сада сте видели како да генеришете текст користећи промпт. Имали сте програм који ради и који можете модификовати да генерише различите врсте текста.

Промптови се могу користити за разне задатке. На пример:

- **Генерисање одређеног типа текста**. На пример, можете генерисати песму, питања за квиз и слично.
- **Претрага информација**. Можете користити промптове да тражите информације, као у примеру „Шта значи CORS у веб развоју?“.
- **Генерисање кода**. Можете користити промптове за генерисање кода, на пример за развој регуларних израза који валидају имејлове или чак за генерисање целе апликације, као што је веб апликација.

## Практичнији пример: генератор рецепата

Замислите да имате састојке код куће и желите да скувате нешто. За то вам треба рецепт. Један начин да пронађете рецепте је да користите претраживач, али можете користити и LLM модел.

Можете написати промпт овако:

> „Покажи ми 5 рецепата за јело са следећим састојцима: пилеће месо, кромпир и шаргарепа. За сваки рецепт наведи све састојке који се користе.“

На основу овог промпта, можете добити одговор сличан овом:

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

Овај резултат је сјајан, знам шта да кувам. У овом тренутку, корисна побољшања могу бити:

- Филтрирање састојака које не волим или на које сам алергичан.
- Креирање листе за куповину, у случају да немам све састојке код куће.

За ове случајеве, додајмо још један промпт:

> „Молим те, уклони рецепте са белим луком јер сам алергичан и замени га нечим другим. Такође, направи листу за куповину за ове рецепте, узимајући у обзир да већ имам пилеће месо, кромпир и шаргарепу код куће.“

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

То су ваших пет рецепата без белог лука и имате листу за куповину узимајући у обзир шта већ имате код куће.

## Вежба – направите генератор рецепата

Сада када смо прошли сценарио, хајде да напишемо код који одговара приказаном примеру. Пратите ове кораке:

1. Користите постојећи фајл _app.py_ као полазну основу.
1. Пронађите променљиву `prompt` и замените њен код следећим:

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

   > NOTE, ваш LLM није детерминистички, па можете добити различите резултате сваки пут када покренете програм.

   Сјајно, хајде да видимо како можемо да унапредимо ствари. Да бисмо то урадили, желимо да код буде флексибилан, тако да се састојци и број рецепата могу лако мењати.

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

### Унапређење додавањем филтера и листе за куповину

Сада имамо радну апликацију која може да генерише рецепте и флексибилна је јер зависи од уноса корисника, како броја рецепата тако и састојака.

Да бисмо је додатно унапредили, желимо да додамо следеће:

- **Филтрирање састојака**. Желимо да можемо да филтрирамо састојке које не волимо или на које смо алергични. Да бисмо то урадили, можемо изменити постојећи промпт и додати услов за филтер на крају, овако:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Горњи код додаје `{filter}` на крај промпта и такође хвата вредност филтера од корисника.

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

  Као што видите, сви рецепти који садрже млеко су филтрирани. Али ако сте нетолерантни на лактозу, можда ћете желети да филтрирате и рецепте са сиром, па је потребно бити прецизан.

- **Креирање листе за куповину**. Желимо да направимо листу за куповину узимајући у обзир шта већ имамо код куће.

  За ову функционалност можемо покушати да решимо све у једном промпту или да га поделимо на два промпта. Покушаћемо са другом опцијом. Предлажемо да додамо додатни промпт, али да би то функционисало, морамо резултат првог промпта додати као контекст другом промпту.

  Пронађите део кода који исписује резултат првог промпта и додајте следећи код испод:

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

  Обратите пажњу на следеће:

  1. Конструишемо нови промпт тако што додајемо резултат из првог промпта у нови промпт:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. Правимо нови захтев, али такође узимајући у обзир број токена које смо тражили у првом упиту, па овог пута кажемо да је `max_tokens` 1200.

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

Покренувши овај код, добијамо следећи резултат:

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

До сада имамо код који ради, али постоје неке измене које бисмо требали урадити да бисмо ствари додатно унапредили. Неке ствари које треба урадити су:

- **Одвојите тајне од кода**, као што је API кључ. Тајне не припадају коду и треба их чувати на безбедном месту. Да бисмо одвојили тајне од кода, можемо користити променљиве окружења и библиотеке као што је `python-dotenv` да их учитамо из фајла. Ево како би то изгледало у коду:

  1. Направите `.env` фајл са следећим садржајем:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Напомена, за Azure, потребно је подесити следеће променљиве окружења:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     У коду, променљиве окружења бисте учитали овако:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Реч о дужини токена**. Треба да размислимо колико токена нам је потребно да генеришемо жељени текст. Токени коштају, па где год је могуће, треба да будемо штедљиви са бројем токена које користимо. На пример, можемо ли формулисати упит тако да користимо мање токена?

  Да бисте променили број коришћених токена, можете користити параметар `max_tokens`. На пример, ако желите да користите 100 токена, урадите овако:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Експериментисање са температуром**. Температура је нешто што до сада нисмо поменули, али је важан параметар који утиче на рад нашег програма. Што је вредност температуре већа, излаз је насумичнији. Супротно томе, што је температура нижа, излаз је предвидљивији. Размислите да ли желите варијације у излазу или не.

  Да бисте променили температуру, користите параметар `temperature`. На пример, ако желите температуру 0.5, урадите овако:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Напомена, што је ближе 1.0, излаз је разноврснији.

## Задатак

За овај задатак можете изабрати шта ћете направити.

Ево неких предлога:

- Подесите апликацију за генерисање рецепата да је додатно унапредите. Играјте се са вредностима температуре и упитима да видите шта можете да направите.
- Направите „партнера за учење“. Ова апликација треба да може да одговара на питања о одређеној теми, на пример Python. Можете имати упите као „Шта је одређена тема у Python-у?“, или упит који каже, покажи ми код за одређену тему итд.
- Бот за историју, оживите историју, наредите боту да глуми одређену историјску личност и постављајте му питања о њеном животу и времену.

## Решење

### Партнер за учење

Испод је почетни упит, погледајте како га можете користити и прилагодити по свом укусу.

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

Шта ради параметар temperature?

1. Контролише колико је излаз насумичан.
1. Контролише колико је одговор обиман.
1. Контролише колико токена се користи.

## 🚀 Изазов

Док радите на задатку, покушајте да мењате температуру, подесите је на 0, 0.5 и 1. Запамтите да је 0 најмање варијабилно, а 1 највише. Која вредност најбоље функционише за вашу апликацију?

## Одличан посао! Наставите са учењем

Након завршетка ове лекције, погледајте нашу [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) да бисте наставили да унапређујете своје знање о генеративној вештачкој интелигенцији!

Прелазите на Лекцију 7 где ћемо погледати како да [правимо апликације за ћаскање](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.