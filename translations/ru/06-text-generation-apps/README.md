<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:44:40+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ru"
}
-->
# Создание приложений для генерации текста

[![Создание приложений для генерации текста](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ru.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

Вы уже видели в этом курсе, что существуют ключевые понятия, такие как prompts, и даже целая дисциплина под названием «prompt engineering». Многие инструменты, с которыми вы можете взаимодействовать, например ChatGPT, Office 365, Microsoft Power Platform и другие, поддерживают работу с prompts для выполнения различных задач.

Чтобы добавить такой функционал в приложение, нужно понять такие понятия, как prompts, completions, и выбрать библиотеку для работы. Именно этому вы научитесь в этой главе.

## Введение

В этой главе вы:

- Познакомитесь с библиотекой openai и её основными понятиями.
- Создадите приложение для генерации текста с использованием openai.
- Поймёте, как использовать такие параметры, как prompt, temperature и tokens для создания приложения генерации текста.

## Цели обучения

К концу урока вы сможете:

- Объяснить, что такое приложение для генерации текста.
- Создать приложение для генерации текста с помощью openai.
- Настроить приложение для использования большего или меньшего количества токенов, а также изменить temperature для разнообразного результата.

## Что такое приложение для генерации текста?

Обычно при создании приложения у него есть какой-то интерфейс, например:

- Командный интерфейс. Консольные приложения — это типичные программы, где вы вводите команду, и она выполняет задачу. Например, `git` — это приложение с командным интерфейсом.
- Пользовательский интерфейс (UI). Некоторые приложения имеют графический интерфейс (GUI), где вы кликаете по кнопкам, вводите текст, выбираете опции и так далее.

### Консольные и UI-приложения имеют ограничения

Сравним с приложением с командным интерфейсом, где вы вводите команду:

- **Ограничения**. Вы не можете ввести любую команду, только те, которые поддерживает приложение.
- **Языковая специфика**. Некоторые приложения поддерживают несколько языков, но по умолчанию они создаются для конкретного языка, даже если можно добавить поддержку других.

### Преимущества приложений для генерации текста

Чем же отличается приложение для генерации текста?

В таких приложениях больше гибкости: вы не ограничены набором команд или конкретным языком ввода. Вместо этого вы можете использовать естественный язык для взаимодействия с приложением. Ещё одно преимущество — вы работаете с источником данных, обученным на огромном объёме информации, тогда как традиционное приложение ограничено содержимым базы данных.

### Что можно создать с помощью приложения для генерации текста?

Возможностей много, например:

- **Чат-бот**. Чат-бот, отвечающий на вопросы о вашей компании и её продуктах, может быть отличным вариантом.
- **Помощник**. Большие языковые модели отлично справляются с такими задачами, как суммирование текста, извлечение инсайтов, создание текстов, например резюме, и многое другое.
- **Ассистент по коду**. В зависимости от используемой языковой модели можно создать помощника для написания кода. Например, можно использовать GitHub Copilot или ChatGPT для помощи в программировании.

## Как начать?

Для начала нужно интегрироваться с LLM, что обычно делается двумя способами:

- Использовать API. Вы формируете веб-запрос с вашим prompt и получаете сгенерированный текст.
- Использовать библиотеку. Библиотеки инкапсулируют вызовы API и упрощают работу с ними.

## Библиотеки/SDK

Существуют несколько известных библиотек для работы с LLM, например:

- **openai** — эта библиотека упрощает подключение к модели и отправку prompts.

Также есть библиотеки более высокого уровня, например:

- **Langchain**. Известная библиотека, поддерживающая Python.
- **Semantic Kernel**. Библиотека от Microsoft, поддерживающая C#, Python и Java.

## Первое приложение с использованием openai

Давайте посмотрим, как создать первое приложение, какие библиотеки нужны, сколько всего потребуется и так далее.

### Установка openai

Существует множество библиотек для взаимодействия с OpenAI или Azure OpenAI. Можно использовать разные языки программирования, такие как C#, Python, JavaScript, Java и другие. Мы выбрали библиотеку `openai` для Python, поэтому установим её с помощью `pip`.

```bash
pip install openai
```

### Создание ресурса

Вам нужно выполнить следующие шаги:

- Создать аккаунт в Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Получить доступ к Azure OpenAI. Перейдите по ссылке [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и подайте заявку на доступ.

  > [!NOTE]
  > На момент написания необходимо подать заявку на доступ к Azure OpenAI.

- Установить Python <https://www.python.org/>
- Создать ресурс Azure OpenAI Service. Инструкция по созданию ресурса доступна здесь: [создать ресурс](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Найти API ключ и endpoint

Теперь нужно указать библиотеке `openai`, какой API ключ использовать. Чтобы найти ключ, перейдите в раздел «Keys and Endpoint» вашего ресурса Azure OpenAI и скопируйте значение «Key 1».

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Когда у вас есть эта информация, давайте укажем библиотекам использовать её.

> [!NOTE]
> Рекомендуется хранить API ключ отдельно от кода. Это можно сделать с помощью переменных окружения.
>
> - Установите переменную окружения `OPENAI_API_KEY` со значением вашего ключа.
>   `export OPENAI_API_KEY='sk-...'`

### Настройка конфигурации Azure

Если вы используете Azure OpenAI, настройка выглядит так:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Здесь мы задаём:

- `api_type` равным `azure`. Это указывает библиотеке использовать Azure OpenAI, а не OpenAI.
- `api_key` — ваш API ключ из Azure Portal.
- `api_version` — версия API, которую вы хотите использовать. На момент написания последняя версия — `2023-05-15`.
- `api_base` — endpoint API. Его можно найти в Azure Portal рядом с вашим API ключом.

> [!NOTE] > `os.getenv` — функция для чтения переменных окружения. Её можно использовать для получения значений `OPENAI_API_KEY` и `API_BASE`. Установите эти переменные в терминале или с помощью библиотеки, например `dotenv`.

## Генерация текста

Для генерации текста используется класс `Completion`. Пример:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

В этом коде мы создаём объект completion, передаём модель и prompt, затем выводим сгенерированный текст.

### Чат-комплешены

До этого мы использовали `Completion` для генерации текста. Но есть другой класс — `ChatCompletion`, который лучше подходит для чат-ботов. Пример использования:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Подробнее об этой функциональности будет в следующей главе.

## Упражнение — ваше первое приложение для генерации текста

Теперь, когда мы научились настраивать и конфигурировать openai, пора создать первое приложение для генерации текста. Следуйте этим шагам:

1. Создайте виртуальное окружение и установите openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Если вы используете Windows, введите `venv\Scripts\activate` вместо `source venv/bin/activate`.

   > [!NOTE]
   > Найдите ваш ключ Azure OpenAI, зайдя на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), найдите `Open AI`, выберите ресурс `Open AI resource`, затем перейдите в `Keys and Endpoint` и скопируйте значение `Key 1`.

1. Создайте файл _app.py_ и вставьте следующий код:

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
   > Если вы используете Azure OpenAI, установите `api_type` в `azure` и `api_key` в ваш ключ Azure OpenAI.

   Вы должны увидеть примерно такой вывод:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Разные типы prompts для разных задач

Теперь вы знаете, как генерировать текст с помощью prompt. У вас есть программа, которую можно запускать и изменять для генерации разных типов текста.

Prompts можно использовать для самых разных задач, например:

- **Генерация определённого типа текста**. Например, стихотворение, вопросы для викторины и т.д.
- **Поиск информации**. Можно использовать prompts для поиска информации, например: «Что означает CORS в веб-разработке?».
- **Генерация кода**. Можно создавать код, например регулярные выражения для проверки email или даже целые программы, например веб-приложения.

## Более практичный пример: генератор рецептов

Представьте, что у вас дома есть ингредиенты, и вы хотите что-то приготовить. Для этого нужен рецепт. Можно воспользоваться поисковой системой или LLM.

Вы можете написать prompt так:

> «Покажи 5 рецептов блюд с такими ингредиентами: курица, картофель и морковь. Для каждого рецепта перечисли все используемые ингредиенты.»

В ответ вы можете получить что-то вроде:

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

Отличный результат — теперь я знаю, что приготовить. На этом этапе полезными улучшениями могут быть:

- Исключение ингредиентов, которые мне не нравятся или на которые у меня аллергия.
- Создание списка покупок, если дома не хватает каких-то ингредиентов.

Для этого добавим дополнительный prompt:

> «Пожалуйста, исключи рецепты с чесноком, так как у меня аллергия, и замени его на что-то другое. Также составь список покупок для рецептов, учитывая, что у меня дома уже есть курица, картофель и морковь.»

Теперь вы получите новый результат:

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

Вот ваши пять рецептов без чеснока и список покупок с учётом имеющихся продуктов.

## Упражнение — создайте генератор рецептов

Теперь, когда мы рассмотрели сценарий, давайте напишем код, соответствующий ему. Следуйте этим шагам:

1. Используйте существующий файл _app.py_ как отправную точку.
1. Найдите переменную `prompt` и замените её содержимое на следующее:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Если запустить код, вы увидите примерно такой вывод:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, ваша LLM — недетерминированна, поэтому результаты могут отличаться при каждом запуске.

Отлично, теперь посмотрим, как улучшить приложение. Чтобы сделать его гибким, нужно, чтобы количество рецептов и ингредиенты можно было менять.

1. Изменим код следующим образом:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

Для тестового запуска код может выглядеть так:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Улучшаем, добавляя фильтр и список покупок

Теперь у нас есть рабочее приложение, которое может создавать рецепты и гибко настраивается пользователем — как по количеству рецептов, так и по ингредиентам.

Чтобы улучшить его, добавим:

- **Фильтрацию ингредиентов**. Хотим исключать ингредиенты, которые не нравятся или вызывают аллергию. Для этого изменим prompt, добавив условие фильтрации в конце:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Здесь мы добавляем `{filter}` в конец prompt и также получаем значение фильтра от пользователя.

  Пример ввода при запуске программы:

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

  Как видите, рецепты с молоком отфильтрованы. Но если у вас непереносимость лактозы, возможно, стоит исключить и рецепты с сыром, поэтому важно чётко указывать фильтр.

- **Создание списка покупок**. Хотим составлять список покупок с учётом того, что уже есть дома.

  Для этого можно либо решить всё одним prompt, либо разделить на два. Попробуем второй вариант. Предлагается добавить дополнительный prompt, но для этого нужно передать результат первого prompt как контекст для второго.

  Найдите в коде место, где выводится результат первого prompt, и добавьте следующий код ниже:

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

Обратите внимание:

1. Мы формируем новый prompt, добавляя к нему результат первого prompt:

   ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
  1. Мы делаем новый запрос, учитывая количество токенов, которые запросили в первом запросе, поэтому на этот раз указываем `max_tokens` равным 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Запустив этот код, мы получаем следующий результат:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Улучшите вашу настройку

То, что у нас есть сейчас — это рабочий код, но есть несколько моментов, которые стоит доработать для улучшения. Вот что стоит сделать:

- **Отделить секреты от кода**, например, API-ключ. Секреты не должны храниться в коде, их нужно сохранять в безопасном месте. Чтобы отделить секреты от кода, можно использовать переменные окружения и библиотеки вроде `python-dotenv` для загрузки их из файла. Вот как это может выглядеть в коде:

  1. Создайте файл `.env` со следующим содержимым:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Обратите внимание, для Azure нужно задать следующие переменные окружения:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     В коде переменные окружения загружаются так:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Несколько слов о длине токенов**. Нужно учитывать, сколько токенов требуется для генерации нужного текста. Токены стоят денег, поэтому по возможности стоит экономить их количество. Например, можно ли сформулировать запрос так, чтобы использовать меньше токенов?

  Чтобы изменить количество используемых токенов, можно использовать параметр `max_tokens`. Например, если нужно использовать 100 токенов, делаем так:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Эксперименты с параметром temperature**. Температура — это параметр, о котором мы пока не говорили, но он важен для работы программы. Чем выше значение temperature, тем более случайным будет результат. Чем ниже — тем более предсказуемым. Подумайте, хотите ли вы получить разнообразный результат или более стабильный.

  Чтобы изменить температуру, используйте параметр `temperature`. Например, чтобы установить температуру 0.5, сделайте так:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Обратите внимание, чем ближе к 1.0, тем более разнообразным будет результат.

## Задание

Для этого задания вы можете выбрать, что хотите создать.

Вот несколько идей:

- Улучшите приложение генератора рецептов. Поиграйте с параметрами temperature и запросами, чтобы посмотреть, что получится.
- Создайте «учебного помощника». Это приложение должно уметь отвечать на вопросы по теме, например, по Python. Можно использовать запросы вроде «Что такое определённая тема в Python?» или «Покажи код по определённой теме» и т.п.
- Исторический бот — оживите историю, попросите бота сыграть роль какого-то исторического персонажа и задавайте ему вопросы о его жизни и эпохе.

## Решение

### Учебный помощник

Ниже приведён стартовый запрос, посмотрите, как его можно использовать и подстроить под себя.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Исторический бот

Вот несколько примеров запросов, которые можно использовать:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Проверка знаний

Что делает параметр temperature?

1. Он контролирует, насколько случайным будет результат.
1. Он контролирует размер ответа.
1. Он контролирует, сколько токенов используется.

## 🚀 Вызов

При выполнении задания попробуйте менять temperature, установите значения 0, 0.5 и 1. Помните, что 0 — это наименее разнообразный результат, а 1 — самый разнообразный. Какое значение лучше всего подходит для вашего приложения?

## Отличная работа! Продолжайте обучение

После завершения этого урока загляните в нашу [коллекцию по Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

Переходите к уроку 7, где мы рассмотрим, как [создавать чат-приложения](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.