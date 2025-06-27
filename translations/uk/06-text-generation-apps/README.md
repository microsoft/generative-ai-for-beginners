<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T15:01:45+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "uk"
}
-->
# Створення додатків для генерації тексту

[![Створення додатків для генерації тексту](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.uk.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

Ви вже бачили, що в цій навчальній програмі є основні концепції, такі як підказки, і навіть ціла дисципліна під назвою "інженерія підказок". Багато інструментів, з якими ви можете взаємодіяти, такі як ChatGPT, Office 365, Microsoft Power Platform та інші, підтримують використання підказок для досягнення певних цілей.

Щоб додати такий досвід до додатку, вам потрібно зрозуміти такі поняття, як підказки, завершення, і вибрати бібліотеку для роботи. Саме цьому ви навчитеся в цьому розділі.

## Вступ

У цьому розділі ви:

- Дізнаєтеся про бібліотеку openai та її основні концепції.
- Створите додаток для генерації тексту, використовуючи openai.
- Зрозумієте, як використовувати такі концепції, як підказка, температура і токени, для створення додатку генерації тексту.

## Цілі навчання

Наприкінці цього уроку ви зможете:

- Пояснити, що таке додаток для генерації тексту.
- Створити додаток для генерації тексту, використовуючи openai.
- Налаштувати ваш додаток для використання більшої чи меншої кількості токенів, а також змінити температуру для різноманітного виходу.

## Що таке додаток для генерації тексту?

Зазвичай, коли ви створюєте додаток, він має якийсь інтерфейс, наприклад:

- Командний. Консольні додатки — це типові додатки, де ви вводите команду, і вона виконує завдання. Наприклад, `git` — це командний додаток.
- Інтерфейс користувача (UI). Деякі додатки мають графічні інтерфейси користувача (GUI), де ви натискаєте кнопки, вводите текст, вибираєте опції тощо.

### Консольні та UI додатки обмежені

Порівняйте це з командним додатком, де ви вводите команду:

- **Це обмежено**. Ви не можете просто ввести будь-яку команду, тільки ті, які підтримує додаток.
- **Мовно специфічно**. Деякі додатки підтримують багато мов, але за замовчуванням додаток створено для конкретної мови, навіть якщо ви можете додати більше мовної підтримки.

### Переваги додатків для генерації тексту

Чим відрізняється додаток для генерації тексту?

У додатку для генерації тексту у вас більше гнучкості, ви не обмежені набором команд або конкретною мовою введення. Натомість ви можете використовувати природну мову для взаємодії з додатком. Ще однією перевагою є те, що ви вже взаємодієте з джерелом даних, яке було навчено на великому корпусі інформації, тоді як традиційний додаток може бути обмежений тим, що є в базі даних.

### Що я можу створити за допомогою додатку для генерації тексту?

Є багато речей, які ви можете створити. Наприклад:

- **Чат-бот**. Чат-бот, який відповідає на запитання про теми, такі як ваша компанія та її продукти, може бути хорошим варіантом.
- **Помічник**. LLM чудово підходять для таких завдань, як підсумовування тексту, отримання інсайтів з тексту, створення тексту, такого як резюме, і багато іншого.
- **Асистент з кодування**. Залежно від мовної моделі, яку ви використовуєте, ви можете створити асистента з кодування, який допоможе вам писати код. Наприклад, ви можете використовувати продукт, такий як GitHub Copilot, а також ChatGPT, щоб допомогти вам писати код.

## Як я можу почати?

Ну, вам потрібно знайти спосіб інтеграції з LLM, що зазвичай передбачає такі два підходи:

- Використовуйте API. Тут ви створюєте веб-запити з вашою підказкою і отримуєте згенерований текст назад.
- Використовуйте бібліотеку. Бібліотеки допомагають інкапсулювати виклики API і роблять їх легшими у використанні.

## Бібліотеки/SDK

Існує кілька відомих бібліотек для роботи з LLM, таких як:

- **openai**, ця бібліотека полегшує підключення до вашої моделі та відправку підказок.

Потім є бібліотеки, які працюють на вищому рівні, такі як:

- **Langchain**. Langchain добре відомий і підтримує Python.
- **Semantic Kernel**. Semantic Kernel — це бібліотека від Microsoft, яка підтримує мови C#, Python і Java.

## Перший додаток, використовуючи openai

Давайте подивимося, як ми можемо створити наш перший додаток, які бібліотеки нам потрібні, скільки потрібно і так далі.

### Встановіть openai

Існує багато бібліотек для взаємодії з OpenAI або Azure OpenAI. Можна використовувати численні мови програмування, такі як C#, Python, JavaScript, Java та інші. Ми обрали використання бібліотеки `openai` Python, тому ми будемо використовувати `pip` для її встановлення.

```bash
pip install openai
```

### Створіть ресурс

Вам потрібно виконати наступні кроки:

- Створіть обліковий запис на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Отримайте доступ до Azure OpenAI. Перейдіть на [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) і запросіть доступ.

  > [!NOTE]
  > На момент написання вам потрібно подати заявку на доступ до Azure OpenAI.

- Встановіть Python <https://www.python.org/>
- Створіть ресурс служби Azure OpenAI. Дивіться цей посібник, як [створити ресурс](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Знайдіть ключ API та кінцеву точку

На цьому етапі вам потрібно сказати вашій бібліотеці `openai`, який ключ API використовувати. Щоб знайти ваш ключ API, перейдіть до розділу "Ключі та кінцева точка" вашого ресурсу Azure OpenAI і скопіюйте значення "Ключ 1".

![Ключі та кінцева точка в ресурсі Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Тепер, коли у вас є ця інформація, давайте вкажемо бібліотекам використовувати її.

> [!NOTE]
> Варто відокремити ваш ключ API від вашого коду. Ви можете зробити це, використовуючи змінні середовища.
>
> - Встановіть змінну середовища `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Налаштування конфігурації Azure

Якщо ви використовуєте Azure OpenAI, ось як ви налаштовуєте конфігурацію:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Вище ми налаштовуємо наступне:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` клас. Ось приклад:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

У наведеному вище коді ми створюємо об'єкт завершення і передаємо в нього модель, яку ми хочемо використовувати, і підказку. Потім ми виводимо згенерований текст.

### Завершення чату

До цього часу ви бачили, як ми використовували `Completion` to generate text. But there's another class called `ChatCompletion`, який більше підходить для чат-ботів. Ось приклад його використання:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Більше про цю функціональність у наступному розділі.

## Вправа - ваш перший додаток для генерації тексту

Тепер, коли ми дізналися, як налаштувати та налаштувати openai, настав час створити ваш перший додаток для генерації тексту. Щоб створити ваш додаток, виконайте наступні кроки:

1. Створіть віртуальне середовище та встановіть openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Якщо ви використовуєте Windows, введіть `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` значення.

1. Створіть файл _app.py_ і додайте в нього наступний код:

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
   > Якщо ви використовуєте Azure OpenAI, вам потрібно встановити `api_type` to `azure` and set the `api_key` на ваш ключ Azure OpenAI.

   Ви повинні побачити вихід, подібний до наступного:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Різні типи підказок для різних речей

Тепер ви побачили, як генерувати текст, використовуючи підказку. У вас навіть є програма, яка працює, яку ви можете змінювати та змінювати, щоб генерувати різні типи тексту.

Підказки можуть використовуватися для різних завдань. Наприклад:

- **Генерація типу тексту**. Наприклад, ви можете згенерувати вірш, запитання для вікторини тощо.
- **Пошук інформації**. Ви можете використовувати підказки для пошуку інформації, як у наступному прикладі: "Що означає CORS у веб-розробці?".
- **Генерація коду**. Ви можете використовувати підказки для генерації коду, наприклад, розробки регулярного виразу для перевірки електронних адрес або навіть згенерувати цілу програму, таку як веб-додаток.

## Більш практичний випадок використання: генератор рецептів

Уявіть, що у вас є інгредієнти вдома, і ви хочете щось приготувати. Для цього вам потрібен рецепт. Один із способів знайти рецепти — це використовувати пошукову систему або ви могли б використовувати LLM для цього.

Ви могли б написати підказку, як так:

> "Покажи мені 5 рецептів для страви з наступними інгредієнтами: курка, картопля та морква. У кожному рецепті вкажіть усі використані інгредієнти"

Враховуючи наведену вище підказку, ви можете отримати відповідь, подібну до:

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

Цей результат чудовий, я знаю, що приготувати. На цьому етапі, що може бути корисними поліпшеннями:

- Відфільтрувати інгредієнти, які я не люблю або на які у мене алергія.
- Скласти список покупок, якщо у мене немає всіх інгредієнтів вдома.

Для наведених вище випадків, давайте додамо додаткову підказку:

> "Будь ласка, видаліть рецепти з часником, так як у мене на нього алергія, і замініть його чимось іншим. Також, будь ласка, складіть список покупок для рецептів, враховуючи, що у мене вже є курка, картопля і морква вдома."

Тепер у вас є новий результат, а саме:

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

Це ваші п'ять рецептів, без згадки про часник, і ви також маєте список покупок, враховуючи те, що у вас вже є вдома.

## Вправа - створіть генератор рецептів

Тепер, коли ми розіграли сценарій, давайте напишемо код, щоб відповідати продемонстрованому сценарію. Для цього виконайте наступні кроки:

1. Використовуйте існуючий файл _app.py_ як відправну точку
1. Знайдіть змінну `prompt` і змініть її код на наступний:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Якщо ви зараз запустите код, ви повинні побачити вихід, подібний до:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ЗАУВАЖТЕ, ваш LLM є недетермінованим, тому ви можете отримувати різні результати щоразу, коли запускаєте програму.

   Чудово, давайте подивимося, як ми можемо покращити речі. Щоб покращити речі, ми хочемо переконатися, що код є гнучким, тому інгредієнти та кількість рецептів можуть бути покращені та змінені.

1. Давайте змінимо код наступним чином:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Тестовий запуск коду може виглядати так:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Покращення шляхом додавання фільтра та списку покупок

Тепер у нас є робочий додаток, здатний створювати рецепти, і він гнучкий, оскільки покладається на введення користувача, як за кількістю рецептів, так і за інгредієнтами.

Щоб ще більше покращити його, ми хочемо додати наступне:

- **Відфільтрувати інгредієнти**. Ми хочемо мати можливість відфільтрувати інгредієнти, які нам не подобаються або на які у нас алергія. Щоб здійснити цю зміну, ми можемо відредагувати нашу існуючу підказку і додати умову фільтрації в кінці, як так:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Вище ми додаємо `{filter}` в кінець підказки і також захоплюємо значення фільтра від користувача.

  Приклад введення при запуску програми може виглядати так:

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

  Як ви бачите, будь-які рецепти з молоком були відфільтровані. Але, якщо ви непереносимі лактози, ви можете захотіти відфільтрувати рецепти з сиром, тому потрібно бути ясним.

- **Скласти список покупок**. Ми хочемо скласти список покупок, враховуючи те, що у нас вже є вдома.

  Для цієї функціональності ми могли б спробувати вирішити все в одній підказці або розділити це на дві підказки. Давайте спробуємо останній підхід. Тут ми пропонуємо додати додаткову підказку, але для цього потрібно додати результат попередньої підказки як контекст до наступної підказки.

  Знайдіть частину в коді, яка виводить результат з першої підказки, і додайте наступний код нижче:

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

  Зверніть увагу на наступне:

  1. Ми створюємо нову підказку, додаючи результат з першої підказки до нової підказки:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Ми робимо новий запит, але також враховуючи кількість токенів, які ми запитали в першій підказці, тому цього разу ми говоримо, що `max_tokens` дорівнює 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Запустивши цей код, ми тепер отримуємо наступний вихід:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Покращте вашу установку

Те, що у нас є на даний момент, це код, який працює, але є кілька налаштувань, які ми повинні зробити, щоб покращити речі ще більше. Деякі речі, які ми повинні зробити, це:

- **Відокремити секрети від коду**, такі як ключ API. Секрети не належать до коду і повин

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо враховувати, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.