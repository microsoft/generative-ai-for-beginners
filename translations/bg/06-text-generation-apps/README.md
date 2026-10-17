# Създаване на приложения за текстово генериране  

[![Създаване на приложения за текстово генериране](../../../translated_images/bg/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)  

> _(Кликнете върху изображението по-горе, за да гледате видео на този урок)_  

Дотук в тази учебна програма сте видели, че има основни концепции като заявки (prompts) и дори цяла дисциплина, наречена "prompt engineering". Много инструменти, с които можете да взаимодействате, като ChatGPT, Office 365, Microsoft Power Platform и други, ви подкрепят с помощта на заявки за постигане на дадена цел.  

За да добавите такова преживяване към приложение, трябва да разберете концепциите като заявки, допълнения (completions) и да изберете библиотека, с която да работите. Това точно ще научите в тази глава.  

## Въведение  

В тази глава ще:  

- Научите за библиотеката openai и нейните основни концепции.  
- Създадете приложение за текстово генериране с помощта на openai.  
- Разберете как да използвате концепции като заявка, температура и токени, за да създадете приложение за текстово генериране.  

## Учебни цели  

В края на този урок ще можете да:  

- Обясните какво представлява приложение за текстово генериране.  
- Създадете приложение за текстово генериране с помощта на openai.  
- Конфигурирате приложението си да използва повече или по-малко токени и да променяте температурата за разнообразен изход.  

## Какво е приложение за текстово генериране?  

Обикновено, когато създавате приложение, то има някакъв вид интерфейс, като например:  

- Базирано на команди. Конзолните приложения са типични приложения, където въвеждате команда и тя изпълнява задача. Например, `git` е приложение базирано на команди.  
- Потребителски интерфейс (UI). Някои приложения имат графични потребителски интерфейси (GUI), където натискате бутoни, въвеждате текст, избирате опции и други.  

### Конзолните и UI приложения са ограничени  

Сравнете ги с приложение базирано на команди, където въвеждате команда:  

- **То е ограничено**. Не можете просто да напишете каквато и да е команда, а само тези, които приложението поддържа.  
- **Специфично за език**. Някои приложения поддържат много езици, но по подразбиране приложението е създадено за конкретен език, дори ако може да добавите поддръжка и за други езици.  

### Предимства на приложенията за текстово генериране  

Какво е различното с приложението за текстово генериране?  

В приложения за текстово генериране имате повече гъвкавост, не сте ограничени до набор от команди или до конкретен входен език. Вместо това използвате естествен език, за да взаимодействате с приложението. Друго предимство е, че вече взаимодействате с източник на данни, който е бил обучен върху огромен корпус от информация, докато традиционното приложение може да бъде ограничено от това, което има в базата данни.  

### Какво мога да създам с приложение за текстово генериране?  

Можете да създадете много неща. Например:  

- **Чатбот**. Чатбот, който отговаря на въпроси за теми като вашата компания и нейните продукти, може да бъде добро решение.  
- **Помощник**. Големите езикови модели са отлични в задачи като обобщаване на текст, извличане на прозрения от текст, генериране на текст като автобиографии и други.  
- **Асистент за код**. В зависимост от използвания езиков модел, можете да изградите асистент, който да ви помага при писане на код. Например, можете да използвате продукти като GitHub Copilot, както и ChatGPT, за да помогнат при писането на код.  

## Как мога да започна?  

Трябва да намерите начин да се интегрирате с голям езиков модел (LLM), което обикновено включва следните два подхода:  

- Използване на API. Тук изграждате уеб заявки с вашата заявка и получавате обратно генериран текст.  
- Използване на библиотека. Библиотеките опростяват API повикванията и ги правят по-лесни за ползване.  

## Библиотеки/SDK  

Има няколко широкоизвестни библиотеки за работа с големи езикови модели, като:  

- **openai** – тази библиотека улеснява свързването с вашия модел и изпращането на заявки.  

Има библиотеки, които работят на по-високо ниво, като:  

- **Langchain**. Langchain е добре позната и поддържа Python.  
- **Semantic Kernel**. Semantic Kernel е библиотека от Microsoft, която поддържа езици C#, Python и Java.  

## Първо приложение с openai  

Нека видим как можем да създадем първото си приложение, какви библиотеки са ни нужни, колко всъщност е необходимо и така нататък.  

### Инсталиране на openai  

Има много библиотеки за взаимодействие с OpenAI или Azure OpenAI. Може да използвате различни програмни езици като C#, Python, JavaScript, Java и други. Ние избрахме да използваме Python библиотеката `openai`, затова ще използваме `pip` за инсталация.  

```bash
pip install openai
```
  
### Създаване на ресурс  

Трябва да изпълните следните стъпки:  

- Създайте акаунт в Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).  
- Получете достъп до Azure OpenAI. Отидете на [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) и подайте заявка за достъп.  

  > [!NOTE]  
  > Към момента на писане, трябва да кандидатствате за достъп до Azure OpenAI.  

- Инсталирайте Python <https://www.python.org/>  
- Създайте ресурс на Azure OpenAI Service. Вижте това ръководство как да [създадете ресурс](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).  

### Намерете API ключ и крайна точка  

Сега трябва да информирате вашата библиотека `openai` кой API ключ да използва. За да намерите своя API ключ, отидете в секцията "Keys and Endpoint" на вашия Azure OpenAI ресурс и копирайте стойността на "Key 1".  

![Раздел Keys and Endpoint в Azure портал](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)  

След като имате тази информация, нека инструктираме библиотеките да я използват.  

> [!NOTE]  
> Струва си да отделите API ключа си от кода. Можете да го направите чрез използване на променливи на средата (environment variables).  
>  
> - Задайте променливата на средата `OPENAI_API_KEY` със стойност вашия API ключ.  
>   `export OPENAI_API_KEY='sk-...'`  

### Конфигуриране за Azure  

Ако използвате Azure OpenAI (сега част от Microsoft Foundry), ето как да конфигурирате настройките. Използваме стандартния клиент `OpenAI`, насочен към Azure OpenAI `/openai/v1/` крайна точка, която работи с Responses API и не изисква `api_version`:  

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```
  
По-горе задаваме следното:  

- `api_key` – това е вашият API ключ, намерен в Azure портал или портала на Microsoft Foundry.  
- `base_url` – това е вашият Foundry ресурсен крайна точка с присъединен `/openai/v1/`. Стабилната v1 крайна точка работи едновременно с OpenAI и Azure OpenAI без нужда от управление на `api_version`.  

> [!NOTE] > `os.environ` чете променливите на средата. Можете да я използвате за четене на променливи като `AZURE_OPENAI_API_KEY` и `AZURE_OPENAI_ENDPOINT`. Задайте тези променливи в терминала или чрез библиотека като `dotenv`.  

## Генериране на текст  

Начинът за генериране на текст е чрез използване на Responses API чрез метода `responses.create`. Ето пример:  

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```
  
В кода по-горе създаваме отговор и подаваме модела, който искаме да използваме, както и заявката (prompt). След това отпечатваме генерирания текст чрез `response.output_text`.  

### Конверсии с няколко хода  

Responses API е подходящ както за еднократни заявки за текстово генериране, така и за многоходови чатботи – подавате списък с съобщения в `input`, за да създадете разговор:  

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```
  
Повече за тази функционалност в следваща глава.  

## Упражнение – вашето първо приложение за текстово генериране  

Сега, след като научихме как да настроим и конфигурираме openai, време е да създадете първото си приложение за текстово генериране. За да го направите, следвайте тези стъпки:  

1. Създайте виртуална среда и инсталирайте openai:  

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```
  
   > [!NOTE]  
   > Ако използвате Windows, въведете `venv\Scripts\activate` вместо `source venv/bin/activate`.  

   > [!NOTE]  
   > Намерете вашия Azure OpenAI ключ като отидете на [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) и потърсите `Open AI`, след което изберете `Open AI resource` и после изберете `Keys and Endpoint` и копирайте стойността на `Key 1`.  

1. Създайте файл _app.py_ и му дайте следния код:  

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
   > Ако използвате обикновен OpenAI (не Azure), използвайте `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (без `base_url`) и подайте име на модел като `gpt-5-mini` вместо име на разполагане.  

   Трябва да видите изход подобен на следния:  

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```
  
## Различни типове заявки за различни неща  

Вече видяхте как да генерирате текст с помощта на заявка. Дори имате работеща програма, която можете да променяте, за да генерирате различни типове текст.  

Заявките могат да се използват за различни задачи. Например:  

- **Генериране на вид текст**. Например, можете да генерирате стихотворение, въпроси за викторина и т.н.  
- **Търсене на информация**. Можете да използвате заявки, за да търсите информация като например „Какво означава CORS в уеб разработката?“.  
- **Генериране на код**. Можете да използвате заявки за генериране на код, например разработване на регулярен израз за валидиране на имейли или защо не да генерирате цяла програма като уеб приложение?  

## По-практичен сценарий: генератор на рецепти  

Представете си, че имате съставки вкъщи и искате да сготвите нещо. За това ви трябва рецепта. Един начин да намерите рецепти е да използвате търсачка или можете да използвате LLM за това.  

Можете да напишете заявка като:  

> "Покажи ми 5 рецепти за ястие с следните съставки: пиле, картофи и моркови. За всяка рецепта изброи всички използвани съставки"  

С тази заявка можете да получите отговор подобен на:  

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
  
Този резултат е отличен, знам какво да сготвя. На този етап полезни подобрения биха били:  

- Филтриране на съставки, които не харесвам или към които съм алергичен.  
- Създаване на списък за пазаруване, в случай че нямам всички съставки вкъщи.  

За горните случаи, нека добавим допълнителна заявка:  

> "Моля, премахнете рецепти с чесън, защото съм алергичен, и го заменете с нещо друго. Също така, моля, създайте списък за пазаруване за рецептите, като отчитате, че вече имам пиле, картофи и моркови вкъщи."  

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
  
Това са вашите пет рецепти, без упоменат чесън, и също така имате списък за пазаруване, отчитайки наличностите ви вкъщи.  

## Упражнение – създаване на генератор на рецепти  

След като разгледахме сценария, нека напишем код, който да го отразява. Следвайте тези стъпки:  

1. Използвайте съществуващия файл _app.py_ като начален пункт  
1. Намерете променливата `prompt` и променете нейния код на следното:  

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```
  
   Ако пуснете кода, трябва да видите изход, подобен на:  

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```
  
   > ЗАБЕЛЕЖКА: големите езикови модели не са детерминирани, така че може да получите различни резултати всеки път при изпълнение на програмата.  

   Отлично, нека видим как да подобрим нещата. За това искаме кодът да е гъвкав, така че съставките и броят на рецептите да могат да се променят и подобряват.  

1. Променете кода по следния начин:  

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```
  
   Тестване на кода може да изглежда така:  

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```
  
### Подобрение чрез добавяне на филтър и списък за пазаруване  

Сега имаме работещо приложение, което е в състояние да генерира рецепти и е гъвкаво, тъй като разчита на входни данни от потребителя, и по отношение на броя рецепти, и по отношение на използваните съставки.  

За да бъде още по-добро, искаме да добавим следното:  

- **Филтриране на съставки**. Искаме да можем да филтрираме съставки, които не харесваме или сме алергични към тях. За да постигнем това, можем да редактираме съществуващата заявка и да добавим условие за филтър в края й по този начин:  

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```
  
  По-горе добавяме `{filter}` в края на заявката и също така извличаме стойността на филтъра от потребителя.  

  Примерен вход при изпълнение на програмата вече може да изглежда така:  

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
  
  Както виждате, всички рецепти с мляко са филтрирани. Но ако сте непоносим(а) към лактоза, може да искате да филтрирате и рецепти с сирене, така че е важно да сте ясни.  

- **Създаване на списък за пазаруване**. Искаме да създадем списък за пазаруване, отчитайки какво вече имаме вкъщи.  

  За тази функция можем да опитаме да решим всичко с една заявка или да я разделим на две заявки. Нека пробваме втория подход. Тук предлагаме добавяне на допълнителна заявка, но за да работи, трябва да добавим резултата от първата заявка като контекст към втората.  

  Намерете мястото в кода, където се отпечатва резултатът от първата заявка, и добавете следния код под него:  

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```
  
  Обърнете внимание на следното:  

  1. Създаваме нова заявка като добавяме резултата от първата заявка в новата:  

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
  
  1. Правим нова заявка, като също отчитаме броя токени, които поискахме в първата заявка, така че този път казваме `max_output_tokens` е 1200.  

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```
  
     След като изпълните този код, ще получите следния изход:  

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

Това, което имаме досега, е работещ код, но има някои корекции, които трябва да направим, за да подобрим нещата още повече. Някои неща, които трябва да направим, са:

- **Разделяне на тайни от кода**, като API ключа. Тайните не трябва да се съхраняват в кода и трябва да се пазят на сигурно място. За да разделим тайните от кода, можем да използваме променливи на средата и библиотеки като `python-dotenv`, за да ги заредим от файл. Ето как би изглеждало това в кода:

  1. Създайте файл `.env` със следното съдържание:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Забележка, за Azure OpenAI в Microsoft Foundry трябва вместо това да зададете следните променливи на средата:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     В кода обаче бихте заредили променливите на средата по следния начин:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Думичка за дължината на токените**. Трябва да обмислим колко токена са необходими, за да генерираме желания текст. Токените струват пари, затова, където е възможно, трябва да бъдем икономични с броя токени, които използваме. Например, можем ли да формулираме подканата така, че да използваме по-малко токени?

  За да промените броя използвани токени, можете да използвате параметъра `max_output_tokens`. Например, ако искате да използвате 100 токена, бихте направили следното:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Експериментиране с температурата**. Температурата е нещо, което досега не сме споменавали, но е важен контекст за начина, по който се представя програмата ни. Колкото по-висока е стойността на температурата, толкова по-случаен ще бъде изходът. Обратно, колкото по-ниска е стойността на температурата, толкова по-предсказуем ще бъде изходът. Помислете дали искате разнообразие в изхода си или не.

  За да промените температурата, можете да използвате параметъра `temperature`. Например, ако искате да използвате температура 0.5, бихте направили следното:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Забележка, колкото по-близо до 1.0, толкова по-разнообразен е изходът.

- **Моделите за разсъждение не използват `temperature`**. Това е важна промяна за 2026 г. Настоящите, непремахнати модели в Microsoft Foundry са **модели за разсъждение** (семейството GPT-5, o-серия) - и те **не поддържат `temperature` или `top_p`** (нито `max_tokens`; използвайте `max_output_tokens`). Ако изпратите `temperature` към `gpt-5-mini`, ще получите грешка "параметърът не се поддържа". Така че, за да изпробвате горния пример с температурата, направете го с модел, който все още поддържа контроли за вземане на проби - например отворен **Llama** модел като `Llama-3.3-70B-Instruct` от [каталога с модели на Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), извикан чрез крайна точка Foundry Models / Azure AI Inference (по същия начин както примерите `githubmodels-*`). За модели за разсъждение като GPT-5 контролирахте изхода по друг начин:
  - **Инженерство на подканите** - ясни инструкции, примери и структурирани изходи (виж урок [04 - Инженерство на подканите](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) вършат работата, която преди правеха настройки за вземане на проби.
  - **Контроли за разсъждение** - параметри като усилие/подробност в разсъждението търгуват между дълбочина на разсъждението спрямо забавяне и цена.

  Накратко: `temperature`/`top_p` все още са валидни при много модели (Llama, Mistral, Phi и семейството GPT-4.x - макар GPT-4.x да се премахва), но посоката е инженерство на подканите + контроли за разсъждение при модели за разсъждение като GPT-5.

## Задача

За тази задача можете да изберете какво да създадете.

Ето някои предложения:

- Коригирайте приложението за генериране на рецепти, за да го подобрите още повече. Играйте си с температурните стойности и подканите, за да видите какво можете да постигнете.
- Създайте "учебен партньор". Това приложение трябва да може да отговаря на въпроси за дадена тема, например Python, можете да имате подканите "Какво е дадена тема в Python?", или подканата да казва, покажи ми код за определена тема и т.н.
- Исторически бот, направете историята жива, инструктирайте бота да играе ролята на определен исторически герой и го питайте въпроси за неговия живот и време.

## Решение

### Учебен партньор

По-долу е начална подканa, вижте как можете да я използвате и променяте по ваш вкус.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Исторически бот

Ето някои подканите, които можете да използвате:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Проверка на знанията

Какво прави концепцията температура?

1. Контролира колко случаен е изходът.
1. Контролира колко голям е отговорът.
1. Контролира колко токена се използват.

## 🚀 Предизвикателство

Когато работите по задачата, опитайте да променяте температурата, задайте я на 0, 0.5 и 1. Запомнете, че 0 е най-малко разнообразна, а 1 е най-разнообразната. Коя стойност работи най-добре за вашето приложение?

## Отлична работа! Продължете обучението си

След като завършите този урок, разгледайте нашата [колекция за обучение по Генеративен AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), за да продължите да развивате знанията си по Генеративен AI!

Отправете се към Урок 7, където ще разгледаме как да [създаваме чат приложения](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->