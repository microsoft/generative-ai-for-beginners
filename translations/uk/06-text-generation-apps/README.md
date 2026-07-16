# Створення додатків для генерації тексту

[![Створення додатків для генерації тексту](../../../translated_images/uk/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Клікніть на зображення вище, щоб переглянути відео цього уроку)_

Ви вже бачили в цьому курсі, що існують базові поняття, такі як prompts, і навіть ціла дисципліна під назвою "prompt engineering". Багато інструментів, з якими ви можете взаємодіяти, як ChatGPT, Office 365, Microsoft Power Platform та інші, підтримують використання prompt-ів для досягнення певної мети.

Щоб додати такий досвід у додаток, вам потрібно зрозуміти поняття, як-от prompts, completions та вибрати бібліотеку для роботи. Саме цьому ви навчитеся в цьому розділі.

## Вступ

У цьому розділі ви:

- Дізнаєтеся про бібліотеку openai та її основні концепції.
- Побудуєте додаток для генерації тексту, використовуючи openai.
- Зрозумієте, як використовувати такі поняття, як prompt, temperature та tokens для створення додатка з генерації тексту.

## Цілі навчання

Наприкінці цього уроку ви зможете:

- Пояснити, що таке додаток для генерації тексту.
- Побудувати додаток для генерації тексту, використовуючи openai.
- Налаштувати додаток на використання більшої або меншої кількості токенів та змінювати температуру для отримання різноманітного результату.

## Що таке додаток для генерації тексту?

Зазвичай, коли ви створюєте додаток, він має певний інтерфейс, наприклад такий:

- Командний інтерфейс. Консольні додатки — це типові додатки, де ви вводите команду, і вона виконує завдання. Наприклад, `git` — це командний додаток.
- Користувацький інтерфейс (UI). Деякі додатки мають графічний інтерфейс користувача (GUI), де ви клікаєте кнопки, вводите текст, вибираєте опції тощо.

### Консольні та UI-додатки мають обмеження

Порівняйте це з командним додатком, де ви вводите команду:

- **Обмежено**. Ви не можете вводити будь-яку команду, лише ті, які підтримує додаток.
- **Мовно залежно**. Деякі додатки підтримують багато мов, але за замовчуванням додаток створено для конкретної мови, навіть якщо можна додати підтримку інших мов.

### Переваги додатків генерації тексту

Отже, чим відрізняється додаток для генерації тексту?

У додатку для генерації тексту ви маєте більшу гнучкість, вас не обмежують набір команд або конкретна вхідна мова. Замість цього ви можете використовувати природну мову для взаємодії з додатком. Ще одна перевага — ви вже працюєте з джерелом даних, натренованим на величезному корпусі інформації, тоді як традиційний додаток може бути обмежений тим, що знаходиться в базі даних.

### Що я можу створити за допомогою додатка для генерації тексту?

Ви можете створити багато чого. Наприклад:

- **Чатбот**. Чатбот, який відповідає на питання про різні теми, наприклад вашу компанію та її продукти, може бути гарним варіантом.
- **Помічник**. Величезні мовні моделі (LLM) чудово справляються з такими завданнями, як узагальнення тексту, отримання інсайтів, створення текстів, наприклад, резюме тощо.
- **Асистент з коду**. Залежно від використовуваної мовної моделі можна створити асистента, який допомагає писати код. Наприклад, можна використати такі продукти, як GitHub Copilot та ChatGPT для допомоги з написанням коду.

## Як розпочати?

Отже, вам потрібно знайти спосіб інтеграції з LLM, що зазвичай передбачає два підходи:

- Використання API. Тут ви формуєте веб-запити з вашим prompt і отримуєте згенерований текст.
- Використання бібліотеки. Бібліотеки допомагають інкапсулювати виклики API і роблять їх легшими у використанні.

## Бібліотеки/SDK

Існує кілька відомих бібліотек для роботи з LLM, таких як:

- **openai**, ця бібліотека полегшує підключення до вашої моделі та надсилання prompt-ів.

Також є бібліотеки, які працюють на більш абстрактному рівні, як:

- **Langchain**. Langchain добре відомий і підтримує Python.
- **Semantic Kernel**. Semantic Kernel — це бібліотека від Microsoft, що підтримує мови C#, Python та Java.

## Перший додаток із використанням openai

Давайте подивимось, як створити наш перший додаток, які бібліотеки потрібні, скільки потрібно ресурсів тощо.

### Встановлення openai

Існує багато бібліотек для взаємодії з OpenAI або Azure OpenAI. Також можна використовувати багато мов програмування, таких як C#, Python, JavaScript, Java та інші. Ми обрали бібліотеку `openai` для Python, тож будемо встановлювати її через `pip`.

```bash
pip install openai
```

### Створіть ресурс

Потрібно виконати наступні кроки:

- Створити обліковий запис на Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Отримати доступ до Azure OpenAI. Перейдіть за посиланням [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) та подайте заявку на доступ.

  > [!NOTE]
  > На час написання потрібно подавати заявку на доступ до Azure OpenAI.

- Встановити Python <https://www.python.org/>
- Створити ресурс Azure OpenAI Service. Дивіться цей посібник, як [створити ресурс](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Знайдіть ключ API та endpoint

На даному етапі, потрібно вказати бібліотеці `openai` ваш ключ API. Щоб знайти ключ API, перейдіть до розділу «Keys and Endpoint» вашого ресурсу Azure OpenAI та скопіюйте значення «Key 1».

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Тепер, коли у вас ця інформація скопійована, давайте накажемо бібліотеці її використовувати.

> [!NOTE]
> Варто відокремити ваш ключ API від коду. Це можна зробити за допомогою змінних середовища.
>
> - Встановіть змінну середовища `OPENAI_API_KEY` вашим ключем API.
>   `export OPENAI_API_KEY='sk-...'`

### Налаштування конфігурації Azure

Якщо ви використовуєте Azure OpenAI (тепер частина Microsoft Foundry), ось як налаштувати конфігурацію. Ми використовуємо стандартного клієнта `OpenAI`, направленого на endpoint Azure OpenAI `/openai/v1/`, що працює з Responses API і не потребує `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Тут ми вказуємо наступне:

- `api_key` — це ваш ключ API, знайдений у порталі Azure або Microsoft Foundry.
- `base_url` — це endpoint вашого Foundry ресурсу з додатковим `/openai/v1/`. Стабільний v1 endpoint працює як у OpenAI, так і в Azure OpenAI без керування `api_version`.

> [!NOTE] > `os.environ` читає змінні середовища. Ви можете використовувати його для читання змінних, як `AZURE_OPENAI_API_KEY` та `AZURE_OPENAI_ENDPOINT`. Встановлюйте ці змінні середовища в терміналі або за допомогою бібліотеки, як `dotenv`.

## Генерація тексту

Текст генерується за допомогою Responses API через метод `responses.create`. Ось приклад:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # це назва вашого розгортання моделі
    input=prompt,
    store=False,
)
print(response.output_text)
```

У наведеному коді ми створюємо відповідь, передаємо модель, яку хочемо використати, і prompt. Потім виводимо згенерований текст через `response.output_text`.

### Багатокрокові розмови

Responses API добре підходить як для одноразової генерації тексту, так і для багатокрокових чатботів — ви надаєте список повідомлень в `input` для побудови розмови:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Більше про цю функціональність у наступному розділі.

## Вправа — ваш перший додаток для генерації тексту

Тепер, коли ми навчилися налаштовувати і конфігурувати openai, настав час створити ваш перший додаток для генерації тексту. Для цього виконайте наступні кроки:

1. Створіть віртуальне середовище та встановіть openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Якщо ви використовуєте Windows, введіть `venv\Scripts\activate` замість `source venv/bin/activate`.

   > [!NOTE]
   > Знайдіть ваш ключ Azure OpenAI, перейшовши на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), знайдіть `Open AI`, виберіть `Open AI resource`, потім `Keys and Endpoint` і скопіюйте значення `Key 1`.

1. Створіть файл _app.py_ і додайте туди наступний код:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # додайте свій код виконання
   prompt = "Complete the following: Once upon a time there was a"

   # зробіть запит, використовуючи API відповідей
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # виведіть відповідь
   print(response.output_text)
   ```

   > [!NOTE]
   > Якщо ви використовуєте звичайний OpenAI (не Azure), використовуйте `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) і передайте ім'я моделі, наприклад `gpt-4o-mini`, замість імені розгортання.

   Ви побачите такий вивід:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Різні типи prompt-ів для різних задач

Тепер ви побачили, як генерувати текст за допомогою prompt. У вас навіть працює програма, яку можна змінювати, щоб генерувати різноманітні типи тексту.

Prompt-и можна використовувати для різних завдань, наприклад:

- **Генерувати тип тексту**. Наприклад, створити вірш, питання для вікторини тощо.
- **Знаходити інформацію**. Ви можете використовувати prompt-и для пошуку інформації, як у прикладі: «Що означає CORS у веб-розробці?».
- **Генерувати код**. Використовуйте prompt-и для створення коду, наприклад, формування регулярного виразу для перевірки email-адрес або навіть розробки цілого додатка, наприклад веб-додатка.

## Практичний приклад: генератор рецептів

Уявіть, що у вас вдома є інгредієнти, і ви хочете щось приготувати. Для цього вам потрібен рецепт. Один з способів знайти рецепт — скористатися пошуковою системою або використати LLM.

Ви могли б написати prompt так:

> "Покажи мені 5 рецептів страв із такими інгредієнтами: курка, картопля і морква. Для кожного рецепта вкажи всі використані інгредієнти."

Відповідь на такий prompt може виглядати так:

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

Результат чудовий, я знаю, що готувати. На цьому етапі корисними покращеннями можуть бути:

- Відфільтрувати інгредієнти, які мені не подобаються або на які у мене алергія.
- Згенерувати список покупок, якщо вдома немає усіх інгредієнтів.

Для цього додамо додатковий prompt:

> "Будь ласка, видали рецепти з часником, бо у мене алергія, і заміни його на щось інше. Також, будь ласка, згенеруй список покупок для рецептів, враховуючи, що вдома вже є курка, картопля і морква."

Тепер у вас новий результат, а саме:

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

Це ваші п'ять рецептів без часнику і з урахуванням того, що у вас вдома є інгредієнти, а також зі списком покупок.

## Вправа — створіть генератор рецептів

Тепер, коли ми програли цей сценарій, давайте напишемо код, що відповідає показаному сценарію. Для цього виконайте наступні кроки:

1. Використайте існуючий файл _app.py_ як стартову точку
1. Знайдіть змінну `prompt` і замініть її код на такий:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Якщо тепер запустити код, ви побачите результат приблизно такий:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ЗАУВАЖЕННЯ: ваша LLM є недетермінованою, тому при кожному запуску результат може відрізнятися.

   Чудово, давайте подивимось, як можна покращити код. Щоб зробити його гнучким, інгредієнти та кількість рецептів потрібно можна легко змінювати.

1. Змініть код таким чином:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # вставте кількість рецептів у підказку та інгредієнти
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Приклад тестового запуску коду може виглядати так:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Покращення шляхом додавання фільтра та списку покупок

Тепер у нас працюючий додаток, здатний генерувати рецепти, який гнучкий, оскільки вимагає вводити кількість рецептів та інгредієнти від користувача.

Щоб покращити його далі, додамо наступне:

- **Фільтрувати інгредієнти**. Хочемо вміти фільтрувати інгредієнти, які нам не подобаються або на які у нас алергія. Для цього можна змінити prompt, додавши вкінці умову фільтрації, як ось так:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Тут ми додали `{filter}` наприкінці prompt і також отримуємо значення фільтра від користувача.

  Приклад введення при запуску програми тепер може виглядати так:

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

  Як бачите, всі рецепти з молоком відфільтровано. Але, якщо у вас непереносимість лактози, ви можете захотіти фільтрувати також рецепти з сиром, тому важливо бути точним.


- **Створіть список покупок**. Ми хочемо створити список покупок, враховуючи те, що вже є вдома.

  Для цієї функціональності ми можемо або спробувати вирішити все в одному запиті, або розділити це на два запити. Спробуємо другий підхід. Тут ми пропонуємо додати додатковий запит, але для цього потрібно додати результат першого запиту як контекст для другого.

  Знайдіть частину коду, яка виводить результат з першого запиту, і додайте наступний код нижче:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # надрукувати відповідь
  print("Shopping list:")
  print(response.output_text)
  ```

  Зверніть увагу на наступне:

  1. Ми формуємо новий запит, додаючи результат першого запиту до нового запиту:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Ми робимо новий запит, але також враховуємо кількість токенів, яку просили у першому запиті, тож цього разу встановлюємо `max_output_tokens` на 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Запускаючи цей код, ми отримуємо наступний вивід:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Покращіть своє налаштування

Те, що ми маємо наразі — це код, який працює, але є кілька удосконалень, які варто зробити, щоб покращити все далі. Декілька речей, які варто зробити:

- **Відокремте секрети від коду**, як, наприклад, API-ключ. Секрети не повинні зберігатися в коді і мають зберігатися в безпечному місці. Щоб відокремити секрети від коду, ми можемо використовувати змінні середовища та бібліотеки на кшталт `python-dotenv` для завантаження з файлу. Ось як це виглядатиме у коді:

  1. Створіть файл `.env` з таким вмістом:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Зверніть увагу, для Azure OpenAI в Microsoft Foundry потрібно встановити такі змінні середовища замість:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     У коді змінні середовища можна завантажити ось так:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Слово про довжину токенів**. Слід враховувати, скільки токенів потрібно для генерації потрібного тексту. Токени коштують гроші, тож де можливо, варто економно використовувати їхню кількість. Наприклад, чи можемо ми сформувати промпт так, щоб використати менше токенів?

  Щоб змінити кількість токенів, які використовуються, можна вказати параметр `max_output_tokens`. Наприклад, якщо хочете використати 100 токенів, виконайте так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментування з температурою**. Температура — це те, про що ми досі не згадували, але це важливий параметр для роботи програми. Чим вище значення температури, тим більш випадковим буде результат. Навпаки, чим нижче температура, тим передбачуванішим буде вивід. Визначте, чи хочете ви варіації у виводі, чи ні.

  Щоб змінити температуру, можна використовувати параметр `temperature`. Наприклад, якщо хочете встановити температуру 0.5, це буде так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Зверніть увагу, що чим ближче до 1.0, тим різноманітнішим буде вивід.

## Завдання

Для цього завдання ви можете обрати, що саме створювати.

Ось кілька пропозицій:

- Покращуйте додаток генерації рецептів. Поиграйтеся з параметрами температури та промптами, щоб побачити, що вийде.
- Створіть "друга для навчання". Цей додаток має вміти відповідати на питання з певної теми, наприклад Python, у вас можуть бути промпти на кшталт "Що таке певна тема в Python?", або промпт, що показує код для певної теми тощо.
- Бот історії, оживіть історію, накажіть боту грати роль певної історичної особи та задавайте йому питання про її життя та час.

## Розв’язок

### Друг для навчання

Нижче наведено стартовий промпт, подивіться, як його можна використати та змінити на свій смак.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Бот історії

Ось кілька промптів, які ви можете використовувати:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Перевірка знань

Що робить параметр temperature?

1. Він контролює, наскільки випадковим буде вивід.
1. Він контролює розмір відповіді.
1. Він контролює кількість використаних токенів.

## 🚀 Виклик

Працюючи над завданням, спробуйте варіювати температуру, встановіть її на 0, 0.5 і 1. Пам’ятайте, що 0 — це найменш варіативний, а 1 — найбільш. Яке значення найкраще підходить для вашого додатку?

## Відмінна робота! Продовжуйте навчання

Після завершення цього уроку перегляньте нашу [колекцію з вивчення генеративного ШІ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), щоб і надалі поглиблювати свої знання про генеративний ШІ!

Завітайте до Уроку 7, де ми розглянемо, як [створювати чат-застосунки](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->