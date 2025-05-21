<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T17:21:50+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "bg"
}
-->
# Създаване на приложения за генериране на текст

[![Създаване на приложения за генериране на текст](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.bg.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Кликнете върху изображението по-горе, за да гледате видео от този урок)_

До момента сте видели в тази учебна програма, че има основни концепции като подканите и дори цяла дисциплина, наречена "инженеринг на подканите". Много инструменти, с които можете да взаимодействате, като ChatGPT, Office 365, Microsoft Power Platform и други, ви подкрепят в използването на подканите, за да постигнете нещо.

За да добавите такова изживяване в приложение, трябва да разберете концепции като подканите, завършванията и да изберете библиотека, с която да работите. Това е точно това, което ще научите в тази глава.

## Въведение

В тази глава ще:

- Научите за библиотеката openai и нейните основни концепции.
- Създадете приложение за генериране на текст, използвайки openai.
- Разберете как да използвате концепции като подканите, температурата и токените, за да създадете приложение за генериране на текст.

## Цели на обучението

В края на този урок ще можете да:

- Обясните какво е приложение за генериране на текст.
- Създадете приложение за генериране на текст, използвайки openai.
- Конфигурирате вашето приложение да използва повече или по-малко токени и също така да променя температурата за разнообразен изход.

## Какво е приложение за генериране на текст?

Обикновено, когато създавате приложение, то има някакъв интерфейс, като следния:

- Команден интерфейс. Конзолните приложения са типични приложения, където въвеждате команда и то изпълнява задача. Например, `git` е приложение с команден интерфейс.
- Потребителски интерфейс (UI). Някои приложения имат графични потребителски интерфейси (GUI), където кликвате бутони, въвеждате текст, избирате опции и др.

### Конзолни и UI приложения са ограничени

Сравнете го с приложение с команден интерфейс, където въвеждате команда:

- **Ограничено е**. Не можете просто да въведете всяка команда, само тези, които приложението поддържа.
- **Специфично за език**. Някои приложения поддържат много езици, но по подразбиране приложението е създадено за конкретен език, дори ако можете да добавите повече езикова поддръжка.

### Ползи от приложенията за генериране на текст

Как е различно приложението за генериране на текст?

В приложение за генериране на текст имате повече гъвкавост, не сте ограничени до набор от команди или специфичен входен език. Вместо това можете да използвате естествен език за взаимодействие с приложението. Друга полза е, че тъй като вече взаимодействате с източник на данни, който е обучен върху огромен корпус от информация, докато традиционно приложение може да е ограничено до това, което е в база данни.

### Какво мога да създам с приложение за генериране на текст?

Има много неща, които можете да създадете. Например:

- **Чатбот**. Чатбот, отговарящ на въпроси по теми като вашата компания и нейните продукти, може да бъде добро съответствие.
- **Помощник**. LLMs са страхотни в неща като обобщаване на текст, получаване на прозрения от текст, създаване на текст като резюмета и др.
- **Асистент за код**. В зависимост от езиковия модел, който използвате, можете да създадете асистент за код, който да ви помага да пишете код. Например, можете да използвате продукт като GitHub Copilot, както и ChatGPT, за да ви помогнат да пишете код.

## Как мога да започна?

Е, трябва да намерите начин да се интегрирате с LLM, което обикновено включва следните два подхода:

- Използване на API. Тук изграждате уеб заявки с вашата подкана и получавате генериран текст обратно.
- Използване на библиотека. Библиотеките помагат за капсулиране на API обажданията и ги правят по-лесни за използване.

## Библиотеки/SDK

Има няколко добре познати библиотеки за работа с LLM като:

- **openai**, тази библиотека улеснява свързването с вашия модел и изпращането на подканите.

След това има библиотеки, които работят на по-високо ниво, като:

- **Langchain**. Langchain е добре известен и поддържа Python.
- **Semantic Kernel**. Semantic Kernel е библиотека от Microsoft, поддържаща езиците C#, Python и Java.

## Първо приложение, използвайки openai

Нека видим как можем да създадем нашето първо приложение, какви библиотеки са ни необходими, колко е необходимо и т.н.

### Инсталиране на openai

Има много библиотеки там за взаимодействие с OpenAI или Azure OpenAI. Възможно е да се използват различни програмни езици, като C#, Python, JavaScript, Java и други. Избрахме да използваме библиотеката `openai` Python, така че ще използваме `pip`, за да я инсталираме.

```bash
pip install openai
```

### Създаване на ресурс

Трябва да извършите следните стъпки:

- Създайте акаунт в Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Получете достъп до Azure OpenAI. Отидете на [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и заявете достъп.

  > [!NOTE]
  > Към момента на писане трябва да кандидатствате за достъп до Azure OpenAI.

- Инсталирайте Python <https://www.python.org/>
- Създайте ресурс за Azure OpenAI Service. Вижте това ръководство за как да [създадете ресурс](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Намиране на API ключ и крайна точка

На този етап трябва да кажете на вашата библиотека `openai` какъв API ключ да използва. За да намерите вашия API ключ, отидете в секцията "Ключове и крайна точка" на вашия ресурс Azure OpenAI и копирайте стойността "Ключ 1".

![Ключове и крайна точка на ресурс в Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Сега, когато сте копирали тази информация, нека инструктираме библиотеките да я използват.

> [!NOTE]
> Струва си да отделите вашия API ключ от вашия код. Можете да направите това, като използвате променливи на средата.
>
> - Задайте променливата на средата `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Настройка на конфигурацията в Azure

Ако използвате Azure OpenAI, ето как да настроите конфигурацията:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

По-горе задаваме следното:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` клас. Ето един пример:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

В горния код създаваме обект за завършване и подаваме модела, който искаме да използваме и подканата. След това отпечатваме генерирания текст.

### Завършвания за чат

Досега сте видели как използваме `Completion` to generate text. But there's another class called `ChatCompletion`, което е по-подходящо за чатботове. Ето един пример за използването му:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Повече за тази функционалност в предстоящата глава.

## Упражнение - вашето първо приложение за генериране на текст

Сега, когато научихме как да настроим и конфигурираме openai, е време да създадете вашето първо приложение за генериране на текст. За да създадете вашето приложение, следвайте тези стъпки:

1. Създайте виртуална среда и инсталирайте openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ако използвате Windows, въведете `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` стойност.

1. Създайте файл _app.py_ и му дайте следния код:

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
   > Ако използвате Azure OpenAI, трябва да зададете `api_type` to `azure` and set the `api_key` на вашия Azure OpenAI ключ.

   Трябва да видите изход, подобен на следния:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Различни видове подкани за различни неща

Сега сте видели как да генерирате текст, използвайки подкана. Дори имате програма, която работи и която можете да променяте и променяте, за да генерирате различни видове текст.

Подканите могат да се използват за всякакви задачи. Например:

- **Генериране на вид текст**. Например, можете да генерирате стихотворение, въпроси за тест и т.н.
- **Търсене на информация**. Можете да използвате подкани, за да търсите информация като следния пример 'Какво означава CORS в уеб разработката?'.
- **Генериране на код**. Можете да използвате подкани, за да генерирате код, например разработване на регулярни изрази, използвани за валидиране на имейли или защо не генерирате цяла програма, като уеб приложение?

## По-практичен случай: генератор на рецепти

Представете си, че имате съставки вкъщи и искате да сготвите нещо. За това ви е необходима рецепта. Един начин да намерите рецепти е да използвате търсачка или да използвате LLM за това.

Можете да напишете подкана като следната:

> "Покажи ми 5 рецепти за ястие с следните съставки: пиле, картофи и моркови. За всяка рецепта изброи всички използвани съставки"

Дадена горната подкана, може да получите отговор, подобен на:

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

Този резултат е страхотен, знам какво да готвя. На този етап какви биха могли да бъдат полезни подобрения са:

- Филтриране на съставки, които не харесвам или към които съм алергичен.
- Създаване на списък за пазаруване, в случай че нямам всички съставки вкъщи.

За горните случаи нека добавим допълнителна подкана:

> "Моля, премахнете рецепти с чесън, тъй като съм алергичен, и го заменете с нещо друго. Също така, моля, създайте списък за пазаруване за рецептите, като се има предвид, че вече имам пиле, картофи и моркови вкъщи."

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

Това са вашите пет рецепти, без споменаване на чесън и също така имате списък за пазаруване, като се има предвид това, което вече имате вкъщи.

## Упражнение - създайте генератор на рецепти

Сега, когато сме изиграли сценарий, нека напишем код, който да съответства на демонстрирания сценарий. За да направите това, следвайте тези стъпки:

1. Използвайте съществуващия файл _app.py_ като начална точка
1. Намерете променливата `prompt` и променете кода й на следното:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ако сега стартирате кода, трябва да видите изход, подобен на:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ЗАБЕЛЕЖКА, вашият LLM е недетерминиран, така че може да получите различни резултати всеки път, когато стартирате програмата.

   Страхотно, нека видим как можем да подобрим нещата. За да подобрим нещата, искаме да се уверим, че кодът е гъвкав, така че съставките и броят на рецептите могат да бъдат подобрени и променени.

1. Нека променим кода по следния начин:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Проверката на кода може да изглежда така:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Подобрение чрез добавяне на филтър и списък за пазаруване

Сега имаме работещо приложение, способно да произвежда рецепти и то е гъвкаво, тъй като разчита на входове от потребителя, както за броя на рецептите, така и за използваните съставки.

За да го подобрим още повече, искаме да добавим следното:

- **Филтриране на съставки**. Искаме да можем да филтрираме съставки, които не харесваме или към които сме алергични. За да постигнем тази промяна, можем да редактираме съществуващата ни подкана и да добавим условие за филтър в края й, както следва:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  По-горе добавяме `{filter}` в края на подкана и също така заснемаме стойността на филтъра от потребителя.

  Пример за въвеждане на изпълнение на програмата сега може да изглежда така:

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

  Както виждате, всякакви рецепти с мляко в тях са филтрирани. Но ако сте непоносим към лактоза, може да искате да филтрирате и рецепти с кашкавал в тях, така че има нужда да бъдете ясни.

- **Създаване на списък за пазаруване**. Искаме да създадем списък за пазаруване, като се има предвид това, което вече имаме вкъщи.

  За тази функционалност можем или да се опитаме да решим всичко в една подкана, или да я разделим на две подкани. Нека опитаме втория подход. Тук предлагаме добавяне на допълнителна подкана, но за да работи това, трябва да добавим резултата от предишната подкана като контекст към следващата подкана.

  Намерете частта от кода, която отпечатва резултата от първата подкана, и добавете следния код по-долу:

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

  Забележете следното:

  1. Конструираме нова подкана, като добавяме резултата от първата подкана към новата подкана:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Правим ново запитване, но също така като се има предвид броят на токените, които поискахме в първата подкана, така че този път казваме `max_tokens` е 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Пробата на този код сега води до следния изход:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Подобрете вашата настройка

Това, което имаме досега, е код, който работи, но има някои корекции, които трябва да направим, за да подобрим нещата още повече. Някои неща, които трябва да направим, са:

- **Отделете тайните от кода**, като API ключа. Тайните не принадлежат към кода и трябва да бъдат съхранявани на сигурно място. За да отделим тайните от кода, можем да

**Отказ от отговорност**:
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за никакви недоразумения или погрешни интерпретации, произтичащи от използването на този превод.