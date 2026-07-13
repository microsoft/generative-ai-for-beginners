# Создание приложений для генерации текста

[![Создание приложений для генерации текста](../../../translated_images/ru/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

Как вы уже видели в этой учебной программе, существуют основные концепции, такие как подсказки, и даже целая дисциплина, называемая "prompt engineering" (инжиниринг подсказок). Многие инструменты, с которыми вы можете взаимодействовать, например ChatGPT, Office 365, Microsoft Power Platform и другие, поддерживают использование подсказок для выполнения задач.

Чтобы добавить такой опыт в приложение, вам нужно понять такие концепции, как подсказки, дополнения, и выбрать библиотеку для работы с ними. Именно этому вы научитесь в этой главе.

## Введение

В этой главе вы:

- Узнаете о библиотеке openai и её основных понятиях.
- Создадите приложение для генерации текста с использованием openai.
- Поймете, как использовать такие параметры как prompt, temperature и tokens для создания приложения генерации текста.

## Цели обучения

После завершения урока вы сможете:

- Объяснить, что такое приложение для генерации текста.
- Создать приложение для генерации текста с использованием openai.
- Настроить приложение для использования большего или меньшего количества токенов, а также изменять температуру для получения разнообразных результатов.

## Что такое приложение для генерации текста?

Обычно, когда вы создаёте приложение, у него есть какой-то интерфейс, например:

- Командный интерфейс. Консольные приложения — типичные приложения, где вы вводите команду и она выполняет задачу. Например, `git` — это приложение с командным интерфейсом.
- Пользовательский интерфейс (UI). Некоторые приложения имеют графический интерфейс (GUI), где вы кликаете кнопки, вводите текст, выбираете опции и многое другое.

### Консольные и UI приложения имеют ограничения

Сравните это с приложением с командным интерфейсом, где вы вводите команду:

- **Ограничено**. Вы не можете вводить любую команду, а только те, которые поддерживает приложение.
- **Язык специфичен**. Некоторые приложения поддерживают много языков, но по умолчанию приложение построено для конкретного языка, даже если можно добавить поддержку других.

### Преимущества приложений генерации текста

Чем же приложение генерации текста отличается?

В приложении генерации текста у вас больше гибкости, вы не ограничены набором команд или конкретным языком ввода. Вместо этого вы можете использовать естественный язык для взаимодействия с приложением. Ещё одно преимущество — вы уже взаимодействуете с источником данных, который обучен на огромном корпусе информации, тогда как традиционное приложение может быть ограничено тем, что есть в базе данных.

### Что можно создать с приложением генерации текста?

Можно создать многое. Например:

- **Чатбот**. Чатбот, который отвечает на вопросы по темам, таким как ваша компания и её продукты, может быть отличным вариантом.
- **Помощник**. LLM превосходны в таких задачах, как суммирование текста, получение инсайтов из текста, создание текстов, например резюме, и многое другое.
- **Ассистент по коду**. В зависимости от используемой языковой модели, вы можете создать ассистента по коду, который помогает писать код. Например, можно использовать такие продукты, как GitHub Copilot, а также ChatGPT, чтобы помогать писать код.

## С чего начать?

Вам нужно найти способ интеграции с LLM, что обычно включает два подхода:

- Использовать API. Здесь вы формируете веб-запросы с вашей подсказкой и получаете сгенерированный текст в ответ.
- Использовать библиотеку. Библиотеки помогают инкапсулировать вызовы API и упрощают их использование.

## Библиотеки/SDK

Существуют несколько хорошо известных библиотек для работы с LLM, например:

- **openai**, эта библиотека упрощает подключение к вашей модели и отправку подсказок.

Кроме того, есть библиотеки более высокого уровня, такие как:

- **Langchain**. Langchain хорошо известна и поддерживает Python.
- **Semantic Kernel**. Semantic Kernel — это библиотека от Microsoft, поддерживающая языки C#, Python и Java.

## Первое приложение с использованием openai

Давайте посмотрим, как создать наше первое приложение, какие библиотеки нужны, сколько всего требуется и так далее.

### Установка openai

Существует много библиотек для взаимодействия с OpenAI или Azure OpenAI. Можно использовать множество языков программирования: C#, Python, JavaScript, Java и другие. Мы выбрали библиотеку `openai` для Python, поэтому будем использовать `pip` для установки.

```bash
pip install openai
```

### Создание ресурса

Вам нужно выполнить следующие шаги:

- Создать аккаунт в Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Получить доступ к Azure OpenAI. Перейдите по ссылке [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и запросите доступ.

  > [!NOTE]
  > На момент написания необходимо подавать заявку на доступ к Azure OpenAI.

- Установить Python <https://www.python.org/>
- Создать ресурс Azure OpenAI Service. Смотрите руководство как [создать ресурс](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Найти ключ API и endpoint

Теперь нужно указать библиотеке `openai` какой ключ API использовать. Чтобы найти ключ API, зайдите в раздел "Keys and Endpoint" вашего ресурса Azure OpenAI и скопируйте значение "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Теперь, когда вы скопировали эту информацию, давайте укажем библиотекам использовать её.

> [!NOTE]
> Рекомендуется отделять ключ API от кода. Для этого можно использовать переменные окружения.
>
> - Установите переменную окружения `OPENAI_API_KEY` в ваш ключ API.
>   `export OPENAI_API_KEY='sk-...'`

### Настройка конфигурации Azure

Если вы используете Azure OpenAI (теперь часть Microsoft Foundry), вот как настроить конфигурацию. Мы используем стандартный клиент `OpenAI`, направленный на endpoint Azure OpenAI `/openai/v1/`, который работает с Responses API и не требует параметра `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Выше мы настраиваем следующее:

- `api_key` — это ваш ключ API, найденный в портале Azure или Microsoft Foundry.
- `base_url` — это endpoint вашего ресурса Foundry с добавлением `/openai/v1/`. Стабильный endpoint v1 работает как с OpenAI, так и с Azure OpenAI без управления `api_version`.

> [!NOTE] > `os.environ` считывает переменные окружения. Вы можете использовать её для чтения переменных `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Установите эти переменные в терминале или с помощью библиотеки, например, `dotenv`.

## Генерация текста

Для генерации текста используется Responses API через метод `responses.create`. Вот пример:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # это имя вашей развертки модели
    input=prompt,
    store=False,
)
print(response.output_text)
```

В приведённом коде мы создаём отклик, указывая модель и подсказку. Затем выводим сгенерированный текст через `response.output_text`.

### Многошаговые разговоры

Responses API хорошо подходит и для одношаговой генерации текста, и для многошаговых чатботов — вы передаете список сообщений в `input`, формируя разговор:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Подробнее об этой функциональности в следующей главе.

## Упражнение — ваше первое приложение генерации текста

Теперь, когда мы научились настраивать и конфигурировать openai, пора создать первое приложение генерации текста. Для создания приложения выполните следующие шаги:

1. Создайте виртуальное окружение и установите openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Если вы используете Windows, введите `venv\Scripts\activate` вместо `source venv/bin/activate`.

   > [!NOTE]
   > Найдите свой ключ Azure OpenAI, зайдя на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), найдите `Open AI`, выберите `Open AI resource`, затем `Keys and Endpoint` и скопируйте значение `Key 1`.

1. Создайте файл _app.py_ и поместите в него следующий код:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # добавьте ваш код завершения
   prompt = "Complete the following: Once upon a time there was a"

   # сделайте запрос, используя Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # вывести ответ на печать
   print(response.output_text)
   ```

   > [!NOTE]
   > Если вы используете обычный OpenAI (не Azure), используйте `client = OpenAI(api_key="<замените этот ключ вашим OpenAI ключом>")` (без `base_url`) и передавайте имя модели, например, `gpt-4o-mini`, вместо имени деплоя.

   Вы должны увидеть вывод примерно такой:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Разные типы подсказок для разных задач

Теперь вы видели, как генерировать текст с использованием подсказки. У вас даже есть программа, которую можно запускать, модифицировать и изменять, чтобы генерировать разные типы текста.

Подсказки можно использовать для разных задач. Например:

- **Генерация типа текста**. Например, вы можете сгенерировать поэму, вопросы для викторины и так далее.
- **Поиск информации**. Подсказки можно использовать для поиска информации, например: «Что означает CORS в веб-разработке?».
- **Генерация кода**. Можно генерировать код с помощью подсказок, например, создавать регулярные выражения для проверки электронной почты или даже сгенерировать целую программу, например веб-приложение.

## Более практический кейс: генератор рецептов

Представьте, что у вас есть ингредиенты дома, и вы хотите что-то приготовить. Для этого вам нужен рецепт. Один из способов найти рецепты — использовать поисковую систему, а можно использовать LLM.

Вы можете написать подсказку так:

> "Покажи мне 5 рецептов блюд с такими ингредиентами: курица, картофель и морковь. Для каждого рецепта перечисли все используемые ингредиенты"

По этой подсказке вы можете получить ответ примерно такой:

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

Этот результат отличный, я знаю, что готовить. На этом этапе полезными улучшениями могут быть:

- Исключение ингредиентов, которые мне не нравятся или на которые у меня аллергия.
- Создание списка покупок, если дома нет всех ингредиентов.

Для этих случаев добавим дополнительную подсказку:

> "Пожалуйста, исключи рецепты с чесноком, я на него аллергик, и замени его чем-то другим. Также составь список покупок для рецептов, учитывая, что у меня дома уже есть курица, картофель и морковь."

Теперь у вас новый результат, а именно:

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

Вот ваши пять рецептов без упоминания чеснока, а также список покупок с учетом ингредиентов, уже имеющихся у вас дома.

## Упражнение — создайте генератор рецептов

После того, как мы описали сценарий, давайте напишем код, соответствующий этому сценарию. Для этого выполните следующие шаги:

1. Используйте существующий файл _app.py_ как отправную точку
1. Найдите переменную `prompt` и измените её код на следующий:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Если теперь запустить код, вы должны увидеть вывод примерно такой:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > Обратите внимание, ваша LLM недетерминирована, поэтому результаты могут отличаться при каждом запуске программы.

   Отлично, теперь посмотрим, как можно улучшить функциональность. Чтобы улучшить, нам нужно сделать код гибким, чтобы можно было менять ингредиенты и количество рецептов.

1. Изменим код следующим образом:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # интерполировать количество рецептов в подсказку и ингредиенты
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Тестовый запуск кода может выглядеть так:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Улучшаем, добавляя фильтр и список покупок

У нас теперь есть рабочее приложение, способное создавать рецепты, и оно гибкое, так как полагается на ввод пользователя — и по количеству рецептов, и по используемым ингредиентам.

Для дальнейшего улучшения добавим следующее:

- **Фильтр ингредиентов**. Мы хотим иметь возможность исключать ингредиенты, которые нам не нравятся или вызывают аллергию. Для этого можно изменить существующую подсказку и добавить условие фильтра в конце, например так:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Здесь мы добавляем `{filter}` в конец подсказки и также получаем значение фильтра от пользователя.

  Пример запуска программы с вводом может выглядеть так:

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

  Как видите, все рецепты, содержащие молоко, были отфильтрованы. Но если у вас непереносимость лактозы, возможно, понадобится дополнительно исключить рецепты с сыром, так что нужно быть точным.


- **Составьте список покупок**. Мы хотим составить список покупок, учитывая то, что у нас уже есть дома.

  Для этой функциональности мы можем либо попробовать решить всё одним запросом, либо разделить на два запроса. Давайте попробуем второй подход. Здесь мы предлагаем добавить дополнительный запрос, но для этого нужно добавить результат первого запроса как контекст ко второму.

  Найдите в коде часть, которая выводит результат первого запроса, и добавьте следующий код ниже:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # вывести ответ
  print("Shopping list:")
  print(response.output_text)
  ```

  Обратите внимание на следующее:

  1. Мы формируем новый запрос, добавляя к нему результат первого:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Мы делаем новый запрос, при этом учитывая количество токенов, запрошенных в первом запросе, поэтому на этот раз задаём `max_output_tokens` равным 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Протестировав этот код, мы получим следующий вывод:

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

Пока у нас есть рабочий код, но есть несколько улучшений, которые стоит сделать. Некоторые из них:

- **Отделите секреты от кода**, например, API-ключ. Секреты не должны находиться в коде, их нужно хранить в безопасном месте. Чтобы отделить секреты от кода, можно использовать переменные окружения и библиотеки вроде `python-dotenv` для загрузки из файла. Вот как это будет выглядеть в коде:

  1. Создайте файл `.env` со следующим содержимым:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Обратите внимание, для Azure OpenAI в Microsoft Foundry следует вместо этого задать следующие переменные окружения:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     В коде переменные окружения загружаются так:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Слово о длине токенов**. Нужно учитывать, сколько токенов потребуется для генерации текста. Токены стоят денег, поэтому по возможности стоит экономить их количество. Например, можно переформулировать запрос так, чтобы использовать меньше токенов?

  Чтобы изменить количество токенов, используйте параметр `max_output_tokens`. Например, чтобы использовать 100 токенов, сделайте так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Эксперименты с температурой**. Температура — понятие, о котором мы ещё не упоминали, но оно важно для работы программы. Чем выше значение температуры, тем более случайным будет вывод. И наоборот, чем ниже температура, тем более предсказуемым будет результат. Подумайте, хотите ли вы вариативности в выводе.

  Чтобы изменить температуру, используйте параметр `temperature`. Например, чтобы установить температуру 0.5, выполните:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Обратите внимание, чем ближе к 1.0, тем разнообразнее вывод.

## Задание

Для этого задания вы можете выбрать, что создавать.

Вот несколько предложений:

- Улучшите приложение генератора рецептов. Поиграйте с значениями температуры и запросами, чтобы посмотреть, что у вас получится.
- Создайте "учебного помощника". Это приложение должно уметь отвечать на вопросы по теме, например, Python, можно задать вопросы вроде "Что такое такая-то тема в Python?" или запросить показать код по определённой теме.
- Исторический бот: оживите историю, попросите бота сыграть определённого исторического персонажа и задайте ему вопросы о его жизни и эпохе.

## Решение

### Учебный помощник

Ниже приведён стартовый запрос, посмотрите, как можно его использовать и менять по своему усмотрению.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Исторический бот

Вот несколько запросов, которые можно использовать:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Проверка знаний

Что делает параметр температура?

1. Он контролирует, насколько случайным будет вывод.
1. Он контролирует, насколько большой будет ответ.
1. Он контролирует, сколько токенов используется.

## 🚀 Задача

Во время выполнения задания попробуйте менять температуру, установите её в 0, 0.5 и 1. Помните, что 0 — наименее вариативное значение, а 1 — максимально вариативное. Какое значение лучше всего подходит для вашего приложения?

## Отличная работа! Продолжайте обучение

После завершения этого урока ознакомьтесь с нашей [коллекцией по обучению генеративному ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить развивать свои знания в области генеративного ИИ!

Перейдите к Уроку 7, где мы рассмотрим, как [создавать чат-приложения](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->