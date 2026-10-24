# Створення додатків для генерації тексту

[![Створення додатків для генерації тексту](../../../translated_images/uk/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

Ви вже бачили в цьому навчальному курсі, що існують основні поняття, такі як підказки, і навіть ціла дисципліна під назвою «інжиніринг підказок». Багато інструментів, з якими ви можете взаємодіяти, як ChatGPT, Office 365, Microsoft Power Platform і більше, підтримують використання підказок для досягнення певної мети.

Щоб додати таку функціональність у додаток, вам потрібно зрозуміти поняття підказок, завершень і вибрати бібліотеку для роботи. Саме цього ви навчитеся в цій главі.

## Вступ

У цій главі ви:

- Дізнаєтесь про бібліотеку openai та її основні поняття.
- Побудуєте додаток для генерації тексту з використанням openai.
- Зрозумієте, як використовувати такі поняття, як підказка, температура і токени для створення додатка генерації тексту.

## Цілі навчання

Наприкінці цього уроку ви зможете:

- Пояснити, що таке додаток для генерації тексту.
- Побудувати додаток для генерації тексту з використанням openai.
- Налаштувати додаток для використання більшої або меншої кількості токенів, а також змінити температуру, щоб отримати різноманітний результат.

## Що таке додаток для генерації тексту?

Зазвичай, коли ви створюєте додаток, він має якийсь інтерфейс, наприклад такий:

- Командний рядок. Додатки в консолі є типовими додатками, де ви вводите команду, і вона виконує завдання. Наприклад, `git` — це додаток на основі командного рядка.
- Користувацький інтерфейс (UI). Деякі додатки мають графічні інтерфейси користувача (GUI), де ви натискаєте кнопки, вводите текст, вибираєте опції тощо.

### Додатки в консолі та з UI обмежені

Порівняйте це з додатком на основі командного рядка, де ви вводите команду:

- **Обмеження**. Ви не можете ввести будь-яку команду, лише ті, які підтримує додаток.
- **Специфічність мови**. Деякі додатки підтримують багато мов, але за замовчуванням додаток створений для конкретної мови, навіть якщо ви можете додати підтримку більше мов.

### Переваги додатків для генерації тексту

Отже, чим відрізняється додаток для генерації тексту?

У додатку для генерації тексту ви маєте більшу гнучкість, вас не обмежують набір команд або конкретна вхідна мова. Замість цього ви можете використовувати природну мову для взаємодії з додатком. Ще одна перевага — ви вже взаємодієте з джерелом даних, яке було навчено на великій кількості інформації, тоді як традиційний додаток може бути обмежений тим, що знаходиться в базі даних.

### Що можна створити з додатком для генерації тексту?

Можна створити багато різного. Наприклад:

- **Чатбот**. Чатбот, що відповідає на питання про теми, наприклад про вашу компанію та її продукти, може бути гарним варіантом.
- **Помічник**. ВЕЛи (великі мовні моделі) чудово підходять для таких задач, як узагальнення тексту, отримання інсайтів з тексту, створення текстів, наприклад резюме, тощо.
- **Асистент коду**. Залежно від мовної моделі, яку ви використовуєте, ви можете створити асистента коду, який допомагає писати код. Наприклад, можна використовувати продукти, як GitHub Copilot, а також ChatGPT для допомоги у написанні коду.

## Як почати?

Отже, вам потрібно знайти спосіб інтегруватися з ВЕЛ, що зазвичай передбачає два основні підходи:

- Використання API. Тут ви формуєте веб-запити з вашою підказкою і отримуєте згенерований текст у відповідь.
- Використання бібліотеки. Бібліотеки допомагають інкапсулювати виклики API і роблять їх простішими у використанні.

## Бібліотеки/SDK

Існує кілька відомих бібліотек для роботи з ВЕЛ, наприклад:

- **openai** — ця бібліотека полегшує підключення до вашої моделі та надсилання підказок.

Також є бібліотеки, які працюють на більш високому рівні, наприклад:

- **Langchain**. Langchain добре відома і підтримує Python.
- **Semantic Kernel**. Semantic Kernel — бібліотека від Microsoft, що підтримує мови C#, Python і Java.

## Перший додаток з використанням openai

Давайте подивимось, як створити наш перший додаток, які бібліотеки потрібні, скільки потрібно і так далі.

### Встановлення openai

Існує багато бібліотек для взаємодії з OpenAI або Azure OpenAI. Можна використовувати різні мови програмування, такі як C#, Python, JavaScript, Java та інші. Ми вибрали бібліотеку `openai` для Python, тому встановимо її за допомогою `pip`.

```bash
pip install openai
```

### Створення ресурсу

Потрібно виконати такі кроки:

- Створити обліковий запис у Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Отримати доступ до Azure OpenAI. Перейдіть до [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) і подайте запит на доступ.

  > [!NOTE]
  > На момент написання ви повинні подати заявку на доступ до Azure OpenAI.

- Встановити Python <https://www.python.org/>
- Створити ресурс Azure OpenAI Service. Дивіться цей посібник, як [створити ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Знайти API ключ і кінцеву точку

На цей момент потрібно повідомити бібліотеці `openai`, який API ключ використовувати. Щоб знайти API ключ, перейдіть у розділ "Keys and Endpoint" вашого ресурсу Azure OpenAI і скопіюйте значення "Key 1".

![Ключі та кінцева точка ресурсу в Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Тепер, коли ви скопіювали цю інформацію, давайте навчимо бібліотеки її використовувати.

> [!NOTE]
> Варто відокремити ваш API ключ від коду. Це можна зробити за допомогою змінних середовища.
>
> - Встановіть змінну середовища `OPENAI_API_KEY` зі значенням вашого API ключа.
>   `export OPENAI_API_KEY='sk-...'`

### Налаштування конфігурації Azure

Якщо ви використовуєте Azure OpenAI (зараз частина Microsoft Foundry), ось як налаштувати конфігурацію. Ми використовуємо стандартний клієнт `OpenAI`, спрямований на кінцеву точку Azure OpenAI `/openai/v1/`, який працює з Responses API і не вимагає `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Вище ми встановлюємо наступне:

- `api_key` — це ваш API ключ, який можна знайти в порталі Azure або Microsoft Foundry.
- `base_url` — це кінцева точка вашого ресурсу Foundry з додаванням `/openai/v1/`. Стабільна версія v1 працює як з OpenAI, так і з Azure OpenAI без управління `api_version`.

> [!NOTE] > `os.environ` читає змінні середовища. Ви можете використовувати її для читання змінних середовища, таких як `AZURE_OPENAI_API_KEY` та `AZURE_OPENAI_ENDPOINT`. Налаштуйте ці змінні середовища у вашому терміналі або за допомогою бібліотеки, як `dotenv`.

## Генерація тексту

Щоб генерувати текст, використовуйте Responses API через метод `responses.create`. Ось приклад:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

У наведеному коді ми створюємо відповідь, передаємо модель, яку хочемо використовувати, і підказку. Потім виводимо згенерований текст за допомогою `response.output_text`.

### Багатократні діалоги

Responses API підходить як для одноповерхневої генерації тексту, так і для багатокрокових чатботів — ви передаєте список повідомлень у `input`, щоб побудувати розмову:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Більше про цю функціональність у наступній главі.

## Вправи - ваш перший додаток генерації тексту

Тепер, коли ми навчилися налаштовувати і конфігурувати openai, настав час створити ваш перший додаток генерації тексту. Для цього виконайте наступні кроки:

1. Створіть віртуальне середовище та встановіть openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Якщо ви використовуєте Windows, введіть `venv\Scripts\activate` замість `source venv/bin/activate`.

   > [!NOTE]
   > Знайдіть ваш Azure OpenAI ключ, перейшовши на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), пошукайте `Open AI`, виберіть `Open AI resource`, потім виберіть `Keys and Endpoint` і скопіюйте значення `Key 1`.

1. Створіть файл _app.py_ і вставте в нього наступний код:

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
   > Якщо ви використовуєте звичайний OpenAI (не Azure), використовуйте `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) і передайте назву моделі, як `gpt-5-mini` замість імені розгортання.

   Ви повинні побачити примерно такий вивід:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Різні типи підказок для різних задач

Тепер ви побачили, як генерувати текст за допомогою підказки. У вас уже є програма, що працює, яку ви можете модифікувати і змінювати для генерації різних типів тексту.

Підказки можна використовувати для різноманітних задач. Наприклад:

- **Генерація певного типу тексту**. Наприклад, можна створити вірш, питання для вікторини тощо.
- **Пошук інформації**. Можна використовувати підказки для пошуку інформації, наприклад: «Що означає CORS у веб-розробці?».
- **Генерація коду**. Можна генерувати код, наприклад, розробляючи регулярний вираз для валідації електронних пошт або навіть створити цілком програму, як веб-додаток.

## Практичний випадок: генератор рецептів

Уявіть, що у вас є інгредієнти вдома, і ви хочете приготувати страву. Для цього вам потрібен рецепт. Один із способів знайти рецепти — скористатись пошуковою системою, або ж можна використати ВЕЛ.

Ви можете написати таку підказку:

> "Покажи мені 5 рецептів страви з такими інгредієнтами: курка, картопля і морква. Для кожного рецепту перерахуй всі використані інгредієнти."

З огляду на цю підказку, ви можете отримати відповідь, подібну до:

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

Цей результат чудовий, я знаю, що готувати. На цьому етапі корисними покращеннями можуть бути:

- Фільтрація інгредієнтів, які мені не подобаються чи на які у мене алергія.
- Створення списку покупок, на випадок якщо деяких інгредієнтів немає вдома.

Для цих випадків додамо додаткову підказку:

> "Будь ласка, видали рецепти з часником, оскільки у мене алергія, і заміни його на щось інше. Також, сформуй список покупок для рецептів, беручи до уваги, що у мене вдома вже є курка, картопля і морква."

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

Це ваші п’ять рецептів без часнику, і у вас також є список покупок з урахуванням того, що є вдома.

## Вправа - створіть генератор рецептів

Тепер, коли ми розіграли сценарій, давайте напишемо код, який відповідатиме цьому сценарію. Для цього виконайте такі кроки:

1. Використайте існуючий файл _app.py_ як відправну точку
1. Знайдіть змінну `prompt` і змініть її код на наступний:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Якщо зараз запустити код, ви повинні побачити приблизно такий результат:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ЗАУВАЖЕННЯ: ваша ВЕЛ є нестабільною, тому результати можуть відрізнятися при кожному запуску програми.

   Чудово, давайте подивимося, як можна покращити ситуацію. Щоб покращити додаток, потрібно зробити код гнучким, щоб можна було змінювати інгредієнти і кількість рецептів.

1. Змініть код таким чином:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Код для тестування може виглядати так:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Покращення: додавання фільтра та списку покупок

У нас тепер працює додаток, що може створювати рецепти, і він гнучкий, бо покладається на вхідні дані від користувача — як щодо кількості рецептів, так і інгредієнтів.

Щоб покращити додаток, додамо наступне:

- **Фільтрація інгредієнтів**. Потрібно мати можливість фільтрувати інгредієнти, які не подобаються або є алергія. Для цього ми можемо змінити поточну підказку, додавши умову фільтру в кінці, ось так:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Вище ми додали `{filter}` у кінець підказки і також захоплюємо значення фільтра від користувача.

  Приклад запуску програми тепер може виглядати так:

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

  Як бачите, рецепти з молоком були відфільтровані. Але якщо у вас непереносимість лактози, можливо, ви хотіли б відфільтрувати рецепти з сиром. Тому варто бути точнішим.

- **Створення списку покупок**. Ми хочемо створити список покупок, враховуючи те, що вже є вдома.

  Для цієї функціональності ми можемо або зробити все в одній підказці, або розділити на дві. Спробуємо другий підхід. Тут пропонуємо додати додаткову підказку, але щоб це працювало, нам потрібно додати результат першої підказки як контекст для другої.

  Знайдіть у коді місце, яке виводить результат першої підказки, і додайте наступний код нижче:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Зверніть увагу на наступне:

  1. Ми створюємо нову підказку, додаючи результат першої підказки до нової:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Робимо новий запит, враховуючи також кількість токенів, які ми вказали в першій підказці, тому на цей раз ми вказуємо `max_output_tokens` як 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Запустивши цей код, ми отримуємо наступний результат:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Покращте вашу конфігурацію

Те, що ми маємо наразі — це код, який працює, але є деякі налаштування, які варто зробити, щоб покращити ситуацію. Ось дещо, що слід зробити:

- **Відокремити секрети від коду**, такі як API-ключ. Секрети не повинні бути в коді і мають зберігатися у безпечному місці. Щоб відокремити секрети від коду, ми можемо використовувати змінні оточення та бібліотеки на кшталт `python-dotenv` для завантаження їх з файлу. Ось як це виглядає у коді:

  1. Створіть файл `.env` з таким вмістом:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Зауважте, для Azure OpenAI у Microsoft Foundry потрібно встановити такі змінні оточення замість цього:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     У коді ви завантажуєте змінні оточення так:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Слово про довжину токенів**. Нам варто задуматися, скільки токенів потрібно, щоб згенерувати бажаний текст. Токени коштують грошей, тож де можливо, варто економити на їх кількості. Наприклад, чи можна сформулювати запит так, щоб використовувати менше токенів?

  Щоб змінити кількість токенів, можна використовувати параметр `max_output_tokens`. Наприклад, щоб використати 100 токенів, зробіть так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експерименти з температурою**. Температура — це те, про що ми досі не згадували, але вона важливий контекст того, як працює наша програма. Чим вищий показник температури, тим більш випадковим буде результат. Навпаки, чим нижча температура, тим більш передбачуваним буде вихід. Визначте, чи хочете ви варіативність у результаті, чи ні.

  Щоб змінити температуру, використовуйте параметр `temperature`. Наприклад, щоб встановити температуру 0.5, зробіть так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Зауважте, чим ближче до 1.0, тим різноманітнішим буде результат.

- **Моделі розмислу не використовують `temperature`**. Це важливий зсув 2026 року. Поточні, не застарілі моделі у Microsoft Foundry — це **моделі розмислу** (сімейство GPT-5, o-series) — і вони **не підтримують `temperature` чи `top_p`** (також не підтримують `max_tokens`; використовуйте `max_output_tokens`). Якщо надіслати `temperature` до `gpt-5-mini`, ви отримаєте помилку "параметр не підтримується". Отже, щоб спробувати приклад з температурою вище, використовуйте модель, яка ще підтримує керування семплінгом — наприклад відкриту **Llama** модель, як `Llama-3.3-70B-Instruct` з [каталогу моделей Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), яку викликають через Foundry Models / Azure AI Inference endpoint (так само, як і зразки `githubmodels-*`). Для моделей розмислу, таких як GPT-5, вихід керується інакше:
  - **Інженерія промптів** — чіткі інструкції, приклади та структурований вивід (див. урок [04 - Інженерія промптів](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) виконують те, що раніше робили управління семплінгом.
  - **Контроль розмислу** — параметри на кшталт зусиль/розлогості розмислу балансують глибину розмислу з часом очікування та вартістю.

  Коротко: `temperature`/`top_p` досі діють у багатьох моделях (Llama, Mistral, Phi та сімейство GPT-4.x — хоча GPT-4.x поступово застаріває), але тренд — це інженерія промптів + контроль розмислу у моделях розмислу типу GPT-5.

## Завдання

Для цього завдання ви можете обрати, що створити.

Ось кілька пропозицій:

- Покращте додаток генератора рецептів. Пограйте з параметрами температури та промптів, подивіться, що зможете придумати.
- Створіть "помічника для навчання". Цей додаток має вміти відповідати на питання з певної теми, наприклад Python: можна використовувати промпти, як-от "Що таке певна тема у Python?", або промпт типу "Покажи мені код для певної теми" і так далі.
- Історичний бот, оживіть історію, дайте боту інструкцію грати роль конкретної історичної особи і ставте йому питання про її життя та часи.

## Розв’язок

### Помічник для навчання

Нижче наведений стартовий промпт, погляньте, як можна його використати та налаштувати під себе.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Історичний бот

Ось кілька промптів, які можна використати:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Перевірка знань

Що робить параметр температура?

1. Він керує тим, наскільки випадковий буде вихід.
1. Він керує розміром відповіді.
1. Він керує кількістю використаних токенів.

## 🚀 Виклик

Працюючи над завданням, спробуйте змінювати температуру: встановіть 0, 0.5 і 1. Пам’ятайте: 0 — найменша варіативність, 1 — найбільша. Яке значення найкраще підходить для вашого додатка?

## Відмінна робота! Продовжуйте навчання

Після завершення цього уроку перегляньте нашу [колекцію Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб і далі підвищувати свої знання з генеративного штучного інтелекту!

Перейдіть до Уроку 7, де ми дізнаємося, як [створювати чат-додатки](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->