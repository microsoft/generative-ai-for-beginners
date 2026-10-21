# Создание приложений для генерации текста

[![Создание приложений для генерации текста](../../../translated_images/ru/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

Вы уже видели в этой учебной программе, что есть основные концепции, такие как подсказки, и даже целая дисциплина под названием "инженерия подсказок". Многие инструменты, с которыми вы можете взаимодействовать, такие как ChatGPT, Office 365, Microsoft Power Platform и другие, поддерживают использование подсказок для выполнения задач.

Чтобы добавить такой опыт в приложение, вам нужно понять концепции подсказок, дополнений и выбрать библиотеку для работы. Именно этому вы научитесь в этой главе.

## Введение

В этой главе вы:

- Узнаете о библиотеке openai и ее основных концепциях.
- Создадите приложение для генерации текста с использованием openai.
- Поймете, как использовать такие концепции, как подсказка, температура и токены, для создания приложения генерации текста.

## Цели обучения

В конце этого урока вы сможете:

- Объяснить, что такое приложение для генерации текста.
- Создать приложение генерации текста с использованием openai.
- Настроить ваше приложение для использования большего или меньшего количества токенов, а также изменить температуру для получения разнообразного результата.

## Что такое приложение для генерации текста?

Обычно, когда вы создаете приложение, у него есть какой-то интерфейс, например:

- Командный. Консольные приложения — это типичные приложения, где вы вводите команду, и оно выполняет задачу. Например, `git` — это командное приложение.
- Пользовательский интерфейс (UI). Некоторые приложения имеют графические пользовательские интерфейсы (GUI), где вы нажимаете кнопки, вводите текст, выбираете опции и т.д.

### Консольные и UI приложения ограничены

Сравните это с командным приложением, где вы вводите команду:

- **Это ограничено**. Вы не можете просто так ввести любую команду, только те, которые поддерживает приложение.
- **Специфично для языка**. Некоторые приложения поддерживают многие языки, но по умолчанию приложение создается для конкретного языка, даже если вы можете добавить поддержку других языков.

### Преимущества приложений для генерации текста

Чем же приложение для генерации текста отличается?

В таких приложениях у вас есть больше свободы, вы не ограничены набором команд или конкретным языком ввода. Вместо этого вы можете использовать естественный язык для взаимодействия с приложением. Еще одним преимуществом является то, что вы уже взаимодействуете с источником данных, обученным на огромном корпусе информации, тогда как традиционное приложение может иметь ограничение тем, что содержится в базе данных.

### Что я могу построить с помощью приложения для генерации текста?

Вы можете создать множество вещей. Например:

- **Чатбот**. Чатбот, отвечающий на вопросы о темах, таких как ваша компания и ее продукты, может быть отличным вариантом.
- **Помощник**. Большие языковые модели отлично справляются с такими задачами, как суммирование текста, извлечение инсайтов из текста, создание текстов, например резюме и многое другое.
- **Ассистент по коду**. В зависимости от используемой языковой модели вы можете создать помощника для написания кода. Например, можно использовать продукты, такие как GitHub Copilot, а также ChatGPT для помощи в написании кода.

## Как начать?

Для этого нужно найти способ интегрироваться с большой языковой моделью (LLM), что обычно заключается в следующих двух подходах:

- Использовать API. Здесь вы формируете веб-запросы с вашей подсказкой и получаете обратно сгенерированный текст.
- Использовать библиотеку. Библиотеки помогают инкапсулировать вызовы API и делают их проще в использовании.

## Библиотеки/SDK

Есть несколько хорошо известных библиотек для работы с LLM, таких как:

- **openai**, эта библиотека облегчает подключение к вашей модели и отправку подсказок.

Есть также библиотеки, работающие на более высоком уровне, например:

- **Langchain**. Langchain хорошо известен и поддерживает Python.
- **Semantic Kernel**. Semantic Kernel — библиотека от Microsoft, поддерживающая C#, Python и Java.

## Первое приложение с использованием openai

Давайте посмотрим, как создать наше первое приложение, какие библиотеки нужны, сколько всего требуется и так далее.

### Установка openai

Существует множество библиотек для взаимодействия с OpenAI или Azure OpenAI. Возможно использовать разные языки программирования, такие как C#, Python, JavaScript, Java и др. Мы выбрали библиотеку Python `openai`, поэтому будем использовать `pip` для ее установки.

```bash
pip install openai
```

### Создание ресурса

Необходимо выполнить следующие шаги:

- Создать учетную запись в Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Получить доступ к Azure OpenAI. Перейдите на [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и запросите доступ.

  > [!NOTE]
  > На момент написания нужно подать заявку на доступ к Azure OpenAI.

- Установить Python <https://www.python.org/>
- Создать ресурс Azure OpenAI Service. См. руководство, как [создать ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Найти ключ API и конечную точку

Теперь нужно сообщить вашей библиотеке `openai`, какой ключ API использовать. Чтобы найти ключ API, перейдите в раздел "Keys and Endpoint" вашего ресурса Azure OpenAI и скопируйте значение "Key 1".

![Панель ключей и конечных точек в Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Теперь, когда вы скопировали эту информацию, давайте укажем библиотекам использовать ее.

> [!NOTE]
> Стоит отделять ключ API от кода. Это можно сделать с помощью переменных окружения.
>
> - Установите переменную окружения `OPENAI_API_KEY` в значение вашего ключа API.
>   `export OPENAI_API_KEY='sk-...'`

### Настройка конфигурации Azure

Если вы используете Azure OpenAI (теперь часть Microsoft Foundry), вот как настроить конфигурацию. Мы используем стандартный клиент `OpenAI`, направленный на конечную точку Azure OpenAI `/openai/v1/`, которая работает с Responses API и не требует `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Выше мы задаем следующее:

- `api_key` — это ваш ключ API, найденный в портале Azure или портале Microsoft Foundry.
- `base_url` — это конечная точка вашего ресурса Foundry с добавленным `/openai/v1/`. Стабильная конечная точка v1 работает как с OpenAI, так и с Azure OpenAI без управления `api_version`.

> [!NOTE] > `os.environ` читает переменные окружения. Вы можете использовать его для чтения переменных окружения, таких как `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Установите эти переменные окружения в вашем терминале или используйте библиотеку, такую как `dotenv`.

## Генерация текста

Для генерации текста используется Responses API через метод `responses.create`. Пример:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

В приведенном выше коде мы создаем отклик, передаем модель, которую хотим использовать, и подсказку. Затем выводим сгенерированный текст через `response.output_text`.

### Многошаговые диалоги

Responses API хорошо подходит как для генерации текста с одним ходом, так и для многошаговых чатботов — вы передаете список сообщений в `input` для построения разговора:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Подробнее об этой функциональности в следующей главе.

## Упражнение - ваше первое приложение генерации текста

Теперь, когда мы научились настраивать openai, пора создать ваше первое приложение генерации текста. Для этого выполните шаги:

1. Создайте виртуальное окружение и установите openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Если вы используете Windows, введите `venv\Scripts\activate` вместо `source venv/bin/activate`.

   > [!NOTE]
   > Найдите свой ключ Azure OpenAI, перейдя на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) и найдите `Open AI`, затем выберите `Open AI resource` и затем выберите `Keys and Endpoint` и скопируйте значение `Key 1`.

1. Создайте файл _app.py_ и добавьте туда следующий код:

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
   > Если вы используете обычный OpenAI (не Azure), используйте `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) и передайте имя модели, например `gpt-5-mini` вместо имени развёртывания.

   Вы должны увидеть примерно такой вывод:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Разные типы подсказок для разных задач

Теперь вы видите, как сгенерировать текст с помощью подсказки. У вас есть программа, которую можно запускать, изменять и создавать разные типы текста.

Подсказки можно использовать для самых разных задач. Например:

- **Генерация типа текста**. Например, вы можете сгенерировать стихотворение, вопросы для викторины и т.д.
- **Поиск информации**. Можно использовать подсказки для поиска информации, например: «Что означает CORS в веб-разработке?».
- **Генерация кода**. Можно использовать подсказки для генерации кода, например, создание регулярного выражения для проверки электронной почты или даже нагенерировать целую программу, например веб-приложение.

## Более практический пример: генератор рецептов

Представьте, что у вас дома есть ингредиенты, и вы хотите что-то приготовить. Для этого нужен рецепт. Чтобы найти рецепты, можно использовать поисковик, а можно применить LLM.

Вы можете написать такую подсказку:

> "Покажи мне 5 рецептов блюда со следующими ингредиентами: курица, картофель и морковь. Для каждого рецепта перечисли все используемые ингредиенты."

В ответ вы можете получить примерно следующее:

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

Этот результат отличный, я знаю, что приготовить. Теперь что могло бы быть полезным улучшением:

- Исключить ингредиенты, которые мне не нравятся или на которые у меня аллергия.
- Создать список покупок, если у меня дома не все ингредиенты.

Для этого добавим дополнительную подсказку:

> "Пожалуйста, исключи рецепты с чесноком, так как у меня аллергия, и замени его чем-то другим. Также, составь список покупок для рецептов, учитывая, что у меня дома уже есть курица, картофель и морковь."

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

Это ваши пять рецептов без чеснока, и у вас есть список покупок с учётом имеющихся ингредиентов.

## Упражнение - создать генератор рецептов

Теперь, когда мы рассмотрели сценарий, давайте напишем код, который соответствует показанному сценарию. Для этого выполните шаги:

1. Используйте существующий файл _app.py_ в качестве отправной точки
1. Найдите переменную `prompt` и замените её код на следующий:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Если теперь запустить код, вы должны увидеть вывод, похожий на:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ЗАМЕТКА, ваша LLM является недетерминированной, поэтому результаты могут отличаться при каждом запуске программы.

   Отлично, давайте посмотрим, как можно улучшить. Для улучшения кода мы хотим, чтобы он был гибким, так чтобы ингредиенты и количество рецептов можно было менять.

1. Изменим код следующим образом:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Пример тестового запуска может выглядеть так:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Улучшение — добавление фильтра и списка покупок

У нас теперь есть работающие приложение, способное создавать рецепты, и оно гибкое, так как опирается на ввод пользователя, как по количеству рецептов, так и по используемым ингредиентам.

Для дальнейшего улучшения добавим следующее:

- **Фильтрация ингредиентов**. Мы хотим иметь возможность исключать ингредиенты, которые не нравятся или вызывают аллергию. Для этого можно изменить подсказку, добавив условие фильтра в её конец, например так:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Здесь мы добавляем `{filter}` в конец подсказки и также получаем значение фильтра от пользователя.

  Пример ввода при запуске программы теперь может выглядеть так:

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

  Как видите, рецепты с молоком исключены. Но если у вас непереносимость лактозы, вы, возможно, захотите исключить рецепты с сыром, поэтому важно быть точным.

- **Создание списка покупок**. Мы хотим составить список покупок с учётом того, что уже есть дома.

  Для этой задачи можно либо попытаться решить всё в одном запросе, либо разделить на две подсказки. Попробуем второй вариант. Здесь предлагается добавить дополнительную подсказку, но для этого нужно добавить результат первой подсказки в качестве контекста для второй.

  Найдите место в коде, где выводится результат первой подсказки, и добавьте следующий код ниже:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Обратите внимание на следующее:

  1. Мы формируем новую подсказку, добавляя результат первой подсказки к новой:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Делаем новый запрос, учитывая количество токенов, запрошенных в первой подсказке, на этот раз говорим, что `max_output_tokens` — 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     При запуске этого кода получаем следующий вывод:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Улучшите свою настройку

Что у нас есть на данный момент — это код, который работает, но есть некоторые улучшения, которые мы должны внести для дальнейшего улучшения. Некоторые из того, что мы должны сделать:

- **Отделить секреты от кода**, например API-ключ. Секреты не должны храниться в коде и должны размещаться в безопасном месте. Чтобы отделить секреты от кода, мы можем использовать переменные окружения и библиотеки, такие как `python-dotenv`, чтобы загружать их из файла. Вот как это будет выглядеть в коде:

  1. Создайте файл `.env` со следующим содержимым:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Примечание: для Azure OpenAI в Microsoft Foundry необходимо вместо этого установить следующие переменные окружения:

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

- **Слово о длине токенов**. Нам стоит учитывать, сколько токенов нужно для генерации требуемого текста. Токены стоят денег, поэтому, где возможно, стоит стараться экономить количество используемых токенов. Например, можем ли мы сформулировать запрос так, чтобы использовать меньше токенов?

  Чтобы изменить количество используемых токенов, можно использовать параметр `max_output_tokens`. Например, если хотите использовать 100 токенов, сделайте так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Эксперименты с температурой**. Температура — это параметр, о котором мы ещё не упоминали, но он важен для того, как работает наша программа. Чем выше значение температуры, тем более случайным будет результат. И наоборот, чем ниже значение температуры, тем более предсказуемым будет результат. Решите, хотите ли вы вариативности в выводе или нет.

  Чтобы изменить температуру, можно использовать параметр `temperature`. Например, если хотите использовать температуру 0.5, сделайте так:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Примечание: чем ближе к 1.0, тем более разнообразным будет результат.

- **Модели reasoning не используют `temperature`**. Это важное изменение, появляющееся к 2026 году. Текущие, не устаревшие модели в Microsoft Foundry — это **reasoning-модели** (семейство GPT-5, o-series) — и они **не поддерживают `temperature` или `top_p`** (а также `max_tokens`; используйте `max_output_tokens`). Если отправить `temperature` на `gpt-5-mini`, вы получите ошибку "параметр не поддерживается". Чтобы попробовать пример с температурой выше, используйте модель, которая по-прежнему поддерживает управление сэмплированием — например, открытую **Llama** модель, такую как `Llama-3.3-70B-Instruct` из [каталога моделей Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), вызванную через конечную точку Foundry Models / Azure AI Inference (так же, как и `githubmodels-*` в примерах). Для reasoning моделей вроде GPT-5 управление выводом происходит иначе:
  - **Промпт инженеринг** — чёткие инструкции, примеры и структурированный вывод (см. урок [04 — Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) выполняют ту работу, которую ранее делали настройки сэмплирования.
  - **Управление рассуждениями** — параметры, такие как усилие рассуждений/многословие, балансируют глубину рассуждений с задержкой и стоимостью.

  Кратко: `temperature`/`top_p` всё ещё актуальны для многих моделей (Llama, Mistral, Phi и семейства GPT-4.x — хотя GPT-4.x устаревает), но направление развития — это создание подсказок + управление рассуждениями в моделях рассуждений, таких как GPT-5.

## Задание

Для этого задания вы можете выбрать, что создавать.

Вот несколько предложений:

- Улучшите приложение генератора рецептов. Поиграйте с параметрами температуры и подсказками, чтобы посмотреть, что вы сможете придумать.
- Создайте "учебного помощника". Это приложение должно уметь отвечать на вопросы по теме, например Python, можно использовать подсказки вроде «Что такое определённая тема в Python?» или подсказку «Покажи мне код по определённой теме» и т.д.
- Исторический бот, оживите историю, заставьте бота играть роль определённого исторического персонажа и задавайте ему вопросы о его жизни и времени.

## Решение

### Учебный помощник

Ниже приведена начальная подсказка, посмотрите, как вы можете её использовать и настроить по своему вкусу.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Исторический бот

Вот несколько подсказок, которые вы можете использовать:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Проверка знаний

Что делает концепция температуры?

1. Она контролирует, насколько случайным будет результат.
1. Она контролирует размер ответа.
1. Она контролирует, сколько токенов используется.

## 🚀 Вызов

При выполнении задания попробуйте менять температуру, установите её в 0, 0.5 и 1. Помните, что 0 — наименее вариативное значение, а 1 — наиболее. Какое значение лучше всего подходит для вашего приложения?

## Отличная работа! Продолжайте обучение

После завершения этого урока посмотрите нашу [коллекцию по изучению генеративного ИИ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), чтобы продолжить повышать свои знания в области генеративного ИИ!

Перейдите к уроку 7, где мы рассмотрим, как [создавать чат-приложения](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->