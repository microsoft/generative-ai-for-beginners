# Създаване на приложения за генериране на текст

[![Създаване на приложения за генериране на текст](../../../translated_images/bg/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

Досега в този учебен план сте видели, че има основни понятия като подсказки и дори цяла дисциплина, наречена "проектиране на подсказки". Много от инструментите, с които можете да взаимодействате, като ChatGPT, Office 365, Microsoft Power Platform и други, поддържат използването на подсказки за изпълнение на задачи.

За да добавите такава функционалност към приложение, трябва да разберете понятия като подсказки, допълнения и да изберете библиотека за работа. Това е точно това, което ще научите в тази глава.

## Въведение

В тази глава ще:

- Научите за библиотеката openai и нейните основни понятия.
- Създадете приложение за генериране на текст с помощта на openai.
- Разберете как да използвате понятия като подсказка (prompt), температура и токени, за да изградите приложение за генериране на текст.

## Учебни цели

В края на този урок ще можете да:

- Обясните какво е приложение за генериране на текст.
- Създадете приложение за генериране на текст с помощта на openai.
- Конфигурирате приложението си да използва повече или по-малко токени и също да променяте температурата за разнообразен изход.

## Какво е приложение за генериране на текст?

Обикновено, когато създавате приложение, то има някакъв вид интерфейс, например:

- Базирано на команди. Конзолните приложения са типични приложения, където въвеждате команда и тя изпълнява задача. Например, `git` е приложение базирано на команди.
- Потребителски интерфейс (UI). Някои приложения имат графични потребителски интерфейси (GUI), където щраквате бутони, въвеждате текст, избирате опции и др.

### Конзолните и UI приложения са ограничени

Сравнете с приложение, базирано на команда, където въвеждате команда:

- **Те са ограничени**. Не можете просто да напишете произволна команда, а само тези, които приложението поддържа.
- **Езиково специфични**. Някои приложения поддържат много езици, но по подразбиране приложението е строено за конкретен език, дори ако можете да добавите поддръжка за повече езици.

### Ползи от приложения за генериране на текст

Значи какво прави приложението за генериране на текст различно?

В приложение за генериране на текст имате повече гъвкавост, не сте ограничени до набор от команди или специфичен входен език. Вместо това, можете да използвате естествен език, за да взаимодействате с приложението. Друга полза е, че вече взаимодействате с източник на данни, който е обучен върху огромен корпус от информация, докато традиционно приложение може да бъде ограничено от това, което е в база данни.

### Какво мога да създам с приложение за генериране на текст?

Много различни неща можете да създадете. Например:

- **Чатбот**. Чатбот, който отговаря на въпроси по теми като вашата компания и нейните продукти, може да бъде подходящ.
- **Асистент**. Големите езикови модели (LLM) са отлични в неща като обобщаване на текст, извличане на информация от текст, създаване на текстове като автобиографии и други.
- **Асистент по кодиране**. В зависимост от езиковия модел, който използвате, можете да създадете асистент за кодиране, който да ви помага да пишете код. Например, можете да използвате продукти като GitHub Copilot, както и ChatGPT, за помощ при писане на код.

## Как мога да започна?

Трябва да намерите начин да се интегрирате с голям езиков модел (LLM), което обикновено включва следните два подхода:

- Използване на API. Тук конструирате уеб заявки с вашата подсказка и получавате генериран текст обратно.
- Използване на библиотека. Библиотеките помагат да се капсулират API повикванията и ги правят по-лесни за използване.

## Библиотеки/SDK

Има няколко добре познати библиотеки за работа с LLM, като:

- **openai**, тази библиотека улеснява свързването към вашия модел и изпращането на подсказки.

След това има библиотеки, които оперират на по-високо ниво, като:

- **Langchain**. Langchain е добре познат и поддържа Python.
- **Semantic Kernel**. Semantic Kernel е библиотека от Microsoft, поддържаща езици като C#, Python и Java.

## Първо приложение с openai

Нека видим как можем да създадем първото си приложение, какви библиотеки са ни нужни, колко е необходимо и т.н.

### Инсталиране на openai

Има много библиотеки за работа с OpenAI или Azure OpenAI. Възможно е да се използват различни програмни езици като C#, Python, JavaScript, Java и други. Избрахме да използваме Python библиотеката `openai`, затова ще използваме `pip` за инсталиране.

```bash
pip install openai
```

### Създаване на ресурс

Трябва да извършите следните стъпки:

- Създайте акаунт в Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Получете достъп до Azure OpenAI. Посетете [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и подайте заявка за достъп.

  > [!NOTE]
  > Към момента на писане, трябва да кандидатствате за достъп до Azure OpenAI.

- Инсталирайте Python <https://www.python.org/>
- Създайте ресурс Azure OpenAI Service. Вижте това ръководство за [създаване на ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Намерете API ключ и крайна точка

В този момент трябва да посочите на библиотеката `openai` кой API ключ да използва. За да намерите своя ключ, отидете в секцията "Keys and Endpoint" на ресурса Azure OpenAI и копирайте стойността "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Сега, след като сте копирали тази информация, нека инструктираме библиотеките да я използват.

> [!NOTE]
> Струва си да отделите API ключа си от кода. Можете да направите това чрез използване на променливи на средата.
>
> - Задайте променлива на средата `OPENAI_API_KEY` с вашия API ключ.
>   `export OPENAI_API_KEY='sk-...'`

### Настройка на конфигурация за Azure

Ако използвате Azure OpenAI (сега част от Microsoft Foundry), ето как настройвате конфигурацията. Използваме стандартния клиент `OpenAI`, насочен към крайна точка на Azure OpenAI `/openai/v1/`, който работи с Responses API и не изисква `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

По-горе задаваме следното:

- `api_key`, това е вашият API ключ, намерен в Azure Portal или Microsoft Foundry портала.
- `base_url`, това е крайният адрес на вашия Foundry ресурс с добавен `/openai/v1/`. Стабилният v1 endpoint работи както с OpenAI, така и с Azure OpenAI без нужда от управление на `api_version`.

> [!NOTE] > `os.environ` чете променливи на средата. Можете да го използвате за четене на променливи като `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Задайте тези променливи в терминала си или чрез библиотека като `dotenv`.

## Генериране на текст

Начинът за генериране на текст е чрез използване на Responses API чрез метода `responses.create`. Ето пример:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # това е името на вашето разгръщане на модела
    input=prompt,
    store=False,
)
print(response.output_text)
```

В горния код създаваме отговор и подаваме модела, който искаме да използваме, и подсказката. След това отпечатваме генерирания текст чрез `response.output_text`.

### Разговори с много ходове

Responses API е подходящ и за едно-ходови текстови генерации, и за много-ходови чатботи – подавате списък със съобщения в `input`, за да изградите разговор:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Повече за тази функционалност в предстоящи глави.

## Упражнение - първото ви приложение за генериране на текст

След като научихме как да настроим и конфигурираме openai, време е да създадете първото си приложение за генериране на текст. За да направите това, следвайте тези стъпки:

1. Създайте виртуална среда и инсталирайте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако използвате Windows, напишете `venv\Scripts\activate`, вместо `source venv/bin/activate`.

   > [!NOTE]
   > Намерете вашия Azure OpenAI ключ, като посетите [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), потърсите `Open AI`, изберете `Open AI resource`, след това изберете `Keys and Endpoint` и копирайте стойността на `Key 1`.

1. Създайте файл _app.py_ и добавете следния код:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # добавете вашия код за завършване
   prompt = "Complete the following: Once upon a time there was a"

   # направете заявка с помощта на Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # отпечатайте отговора
   print(response.output_text)
   ```

   > [!NOTE]
   > Ако използвате обикновен OpenAI (не Azure), използвайте `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) и подайте име на модел като `gpt-5-mini` вместо име на деплоймънт.

   Трябва да видите изход като следния:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различни видове подсказки за различни неща

Вече видяхте как да генерирате текст с помощта на подсказка. Вече имате работеща програма, която можете да модифицирате и променяте, за да генерирате различни видове текст.

Подсказките могат да се използват за всякакви задачи. Например:

- **Генериране на тип текст**. Например, можете да генерирате стихотворение, въпроси за викторина и др.
- **Търсене на информация**. Можете да използвате подсказки, за да търсите информация, например: 'Какво означава CORS в уеб разработката?'.
- **Генериране на код**. Можете да използвате подсказки за генериране на код, например разработване на регулярни изрази за валидиране на имейли или защо не генерирате цяла програма, като уеб приложение?

## По-практичен пример: генератор на рецепти

Представете си, че имате продукти вкъщи и искате да сготвите нещо. За това ви трябва рецепта. Един начин да намерите рецепти е да използвате търсачка или можете да използвате LLM за тази цел.

Можете да напишете подсказка като:

> "Покажи ми 5 рецепти за ястие със следните продукти: пиле, картофи и моркови. За всяка рецепта, изброи всички използвани продукти."

Получавайки горната подсказка, може да получите отговор подобен на:

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

Този резултат е чудесен, знам какво да сготвя. В този момент полезни подобрения могат да бъдат:

- Филтриране на продукти, които не харесвам или съм алергичен към тях.
- Създаване на списък за пазаруване, ако нямам всички продукти вкъщи.

За горните случаи нека добавим допълнителна подсказка:

> "Моля, премахни рецепти с чесън, тъй като съм алергичен, и ги замени с друго. Също така, моля, създай списък за пазаруване за рецептите, като имаш предвид, че вече имам пиле, картофи и моркови вкъщи."

Сега имате нов резултат, а именно:

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

Това са вашите пет рецепти, без да се споменава чесън, и също имате списък за пазаруване, съобразен с това, което вече имате вкъщи.

## Упражнение - създайте генератор на рецепти

След като вече разгледахме сценарий, нека напишем код, който да съответства на демонстрирания сценарий. За да направите това, следвайте тези стъпки:

1. Използвайте съществуващия файл _app.py_ като отправна точка.
1. Намерете променливата `prompt` и променете нейния код на следния:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ако сега стартирате кода, ще видите изход, подобен на:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ЗАБЕЛЕЖКА, вашият LLM е недетерминистичен, така че можете да получите различни резултати всеки път, когато стартирате програмата.

   Отлично, нека видим как можем да подобрим нещата. За да подобрим нещата, искаме кодът да бъде гъвкав, така че съставките и броят на рецептите да могат да се променят.

1. Да променим кода по следния начин:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # интерполирайте броя на рецептите в подканата и съставките
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Възможен тестов пробег на кода може да изглежда така:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Подобрение чрез добавяне на филтър и списък за пазаруване

Вече имаме работещо приложение, способно да генерира рецепти и е гъвкаво, тъй като се основава на потребителски вход, както за броя рецепти, така и за използваните съставки.

За по-нататъшно подобрение искаме да добавим следното:

- **Филтриране на съставки**. Искаме да можем да филтрираме съставки, които не харесваме или към които имаме алергия. За тази промяна можем да редактираме съществуващата подсказка и да добавим филтърна част в края ѝ, както следва:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  По-горе добавяме `{filter}` в края на подсказката и също така събираме стойността на филтъра от потребителя.

  Примерен вход при стартиране на програмата може да изглежда така:

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

  Както виждате, всички рецепти, съдържащи мляко, са филтрирани. Но ако сте с непоносимост към лактоза, може да искате да филтрирате рецепти с сирене, така че е необходимо да сте ясни.


- **Създайте списък за пазаруване**. Искаме да създадем списък за пазаруване, като вземем предвид какво вече имаме вкъщи.

  За тази функционалност можем или да опитаме да решим всичко с един подканващ текст (prompt), или да го разделим на два подканващи текста. Нека опитаме втория подход. Тук предлагаме да добавим допълнителен подканващ текст, но за да работи това, трябва да добавим резултата от първия подканващ текст като контекст към втория.

  Намерете частта в кода, която извежда резултата от първия подканващ текст и добавете следния код под нея:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # отпечатване на отговора
  print("Shopping list:")
  print(response.output_text)
  ```

  Обърнете внимание на следното:

  1. Създаваме нов подканващ текст, като добавяме резултата от първия подканващ текст към новия подканващ текст:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Правим нова заявка, като също отчитаме броя на токените, за които поискахме в първия подканващ текст, затова този път казваме, че `max_output_tokens` е 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Като изпробваме този код, вече стигаме до следния изход:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Подобрете настройката си

Това, което имаме досега, е работещ код, но има някои настройки, които трябва да направим, за да подобрим нещата допълнително. Някои неща, които трябва да направим, са:

- **Отделете тайните от кода**, като ключа на API. Тайните не принадлежат в кода и трябва да се съхраняват на сигурно място. За да отделим тайните от кода, можем да използваме променливи на средата и библиотеки като `python-dotenv`, за да ги зареждаме от файл. Ето как би изглеждало това в кода:

  1. Създайте `.env` файл със следното съдържание:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Забележка, за Azure OpenAI в Microsoft Foundry трябва да зададете следните променливи на средата вместо това:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     В кода бихте заредили променливите на средата по следния начин:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Дума за дължината на токените**. Трябва да обмислим колко токена ни трябват, за да генерираме желания текст. Токените струват пари, така че където е възможно, трябва да се опитаме да бъдем икономични с броя токени, които използваме. Например, можем ли да формулираме подканващия текст така, че да използваме по-малко токени?

  За да промените използваните токени, можете да използвате параметъра `max_output_tokens`. Например, ако искате да използвате 100 токена, бихте направили:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментиране с температурата**. Температурата е нещо, което досега не сме споменавали, но е важен контекст за това как програмата ни работи. Колкото по-висока е стойността на температурата, толкова по-случаен ще бъде изходът. Обратно, колкото по-ниска е стойността на температурата, толкова по-предсказуем ще бъде изходът. Помислете дали искате вариация в изхода си или не.

  За да промените температурата, можете да използвате параметъра `temperature`. Например, ако искате да използвате температура 0.5, бихте направили:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Забележка, колкото по-близо е до 1.0, толкова по-разнообразен ще бъде изходът.

- **Моделите за разсъждение не използват `temperature`**. Това е важна промяна за 2026 г. Настоящите, нерепатирани модели в Microsoft Foundry са **модели за разсъждение** (семейството GPT-5, o-серия) - и те **не поддържат `temperature` или `top_p`** (нито `max_tokens`; използвайте `max_output_tokens`). Ако изпратите `temperature` към `gpt-5-mini`, ще получите грешка "параметърът не се поддържа". За да изпробвате горния пример с температурата, насочете го към модел, който все още поддържа контроли за семплиране - например отворен **Llama** модел като `Llama-3.3-70B-Instruct` от [каталога с модели на Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), извикан чрез крайна точка Foundry Models / Azure AI Inference (по същия начин както примерите `githubmodels-*`). За модели за разсъждение като GPT-5, вие управлявате изхода по друг начин:
  - **Инженерство на подканващия текст** – ясни инструкции, примери и структурирани резултати (виж урок [04 - Основи на инженерство на подканващия текст](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) вършат работата, която регулировките на семплирането досега извършваха.
  - **Контроли за разсъждение** - параметри като усилие/многословие при разсъждение търгуват дълбочината на разсъждение срещу латентност и разходи.

  С две думи: `temperature`/`top_p` все още са валидни за много модели (Llama, Mistral, Phi и семейството GPT-4.x - въпреки че GPT-4.x се изважда от употреба), но посоката е инженеринг на подканващия текст + контроли за разсъждение за модели за разсъждение като GPT-5.

## Задача

За тази задача можете да изберете какво да изградите.

Ето някои предложения:

- Направете подобрения на приложението за генериране на рецепти. Играйте си с стойностите на температурата и подканващите текстове, за да видите какво можете да измислите.
- Създайте „учебен помощник“. Това приложение трябва да може да отговаря на въпроси по тема, например Python, можете да имате подканващи текстове като „Какво е определена тема в Python?“, или можете да имате подканващ текст, който казва, покажи ми код за определена тема и т.н.
- Бот за история, вдъхнете живот на историята, инструктирайте бота да играе роля на определена историческа личност и му задавайте въпроси за живота и времето ѝ.

## Решение

### Учебен помощник

По-долу е началният подканващ текст, вижте как можете да го използвате и адаптирате според вашия вкус.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Исторически бот

Ето някои подканващи текстове, които можете да използвате:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Проверка на знанията

Какво прави концепцията за температура?

1. Управлява колко случаен е изходът.
1. Управлява колко голям е отговорът.
1. Управлява колко токена се използват.

## 🚀 Предизвикателство

Когато работите по задачата, опитайте да променяте температурата, задайте я на 0, 0.5 и 1. Запомнете, че 0 е най-малко разнообразната, а 1 е най-разнообразната. Коя стойност работи най-добре за вашето приложение?

## Отлична работа! Продължете да учите

След като завършите този урок, разгледайте нашата [сбирка за обучение по генеративен изкуствен интелект](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си в областта на генеративния изкуствен интелект!

Отидете в Урок 7, където ще разгледаме как да [създаваме чат приложения](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->