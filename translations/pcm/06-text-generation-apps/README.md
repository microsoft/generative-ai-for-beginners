# Diwey Build Text Generation Applications

[![Diwey Build Text Generation Applications](../../../translated_images/pcm/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Tap di picture wey dey above to watch video of dis lekson)_

You don already see so far through dis kurs say dem get strong tins like prompts and even one whole discipline wey dem dey call "prompt engineering". Plenti tools wey you fit dey use like ChatGPT, Office 365, Microsoft Power Platform and others, dem dey help you use prompts to fit do sometin.

To add dis kain tapiensh to one app, you gats sabi strong tins like prompts, completions and choose library to work with. Na wetin you go learn for dis chapter be dat one.

## Introduction

For dis chapter, you go:

- Learn about di openai library and im main tins.
- Build text generation app wey go dey use openai.
- Understand how to use tins like prompt, temperature, and tokens to build text generation app.

## Di tins wey you go learn

When dis lekson finish, you go fit:

- Explain wetin text generation app be.
- Build text generation app with openai.
- Configure your app to use more or less tokens and also change temperature, for different output.

## Wetin be text generation app?

Normally if you dey build app, e go get some kain interface like dis one:

- Command-based. Console apps na typical app where you go dey type command and e go do di task. For example, `git` na command-based app.
- User interface (UI). Some app get graphical user interfaces (GUI) wey you go dey click buttons, put text, select options and more.

### Console and UI apps get limit

Make you compare am with command-based app wey you dey type command:

- **E get limit**. You no fit type any command, only di one wey di app support.
- **E dey for one language**. Some app fit support plenti languages, but by default e go dey for one language, even if you fit add more languages.

### Benefits of text generation apps

So how text generation app different?

For text generation app, you get more flexibility, no be only set commands or one specific input language. Instead, you fit use natural language talk to di app. Another benefit be say you dey interact with big data wey dem don train on many tins, but normal app fit get limit for wetin dey inside dia database.

### Wetin fit build with text generation app?

Plenti tins wey you fit build. For example:

- **Chatbot**. Chatbot wey go fit answer questions about tins like your company and dia products go make brain.
- **Helper**. LLMs good for tins like to summarize text, get insights from text, produce text like resume and more.
- **Code assistant**. Depending on language model wey you use, you fit build code assistant wey go help you write code. For example, you fit use product like GitHub Copilot and ChatGPT to help write code.

## How to start?

You need to find better way to connect with LLM. Usually e get two ways:

- Use API. You go fit construct web requests with your prompt and get generated text back.
- Use library. Libraries dey encapsulate API calls and make dem easy for use.

## Libraries/SDKs

Some popular libraries for working with LLMs be:

- **openai**, dis library make e easy to connect to your model and send prompts.

Then some libraries dey wey dey operate at higher level like:

- **Langchain**. Langchain dey popular and e support Python.
- **Semantic Kernel**. Semantic Kernel na library by Microsoft wey support C#, Python, and Java.

## First app using openai

Make we see how to build our first app, which libraries we need, how much we need and so on.

### Install openai

Plenty libraries dey for interacting with OpenAI or Azure OpenAI. You fit use many programming languages like C#, Python, JavaScript, Java and more. We choose to use `openai` Python library, so we go use `pip` to install am.

```bash
pip install openai
```

### Create resource

You gots to do dis steps:

- Create account for Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Get access to Azure OpenAI. Go [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) and request access.

  > [!NOTE]
  > As I dey write dis, you gots to apply to get access for Azure OpenAI.

- Install Python <https://www.python.org/>
- Have created Azure OpenAI Service resource. See guide on how to [create resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Find API key and endpoint

Now, you gots tell your `openai` library the API key to use. To find API key, go to "Keys and Endpoint" section on your Azure OpenAI resource and copy "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Now that you get dis info copy, make we tell library to use am.

> [!NOTE]
> E better separate your API key from your code. You fit do am using environment variables.
>
> - Set environment variable `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Setup Azure config

If you dey use Azure OpenAI (wey be part of Microsoft Foundry now), dis na how to setup config. We dey use standard `OpenAI` client wey point to Azure OpenAI `/openai/v1/` endpoint, wey dey work with Responses API and no need `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

We dey set dis as below:

- `api_key`, na your Azure Portal or Microsoft Foundry portal API key.
- `base_url`, na your Foundry resource endpoint with `/openai/v1/` added. Stable v1 endpoint dey work across OpenAI and Azure OpenAI with no `api_version` needed.

> [!NOTE] > `os.environ` dey read environment variables. You fit use am read environment variables like `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`. Set dem in terminal or use library like `dotenv`.

## Generate text

To generate text, you dey use Responses API by `responses.create` method. See example:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # na dis your model deployment name be dat
    input=prompt,
    store=False,
)
print(response.output_text)
```

For code above, we create response and pass model we wan use plus prompt. Then we print generated text with `response.output_text`.

### Multi-turn conversations

Responses API good for both single-turn text generation and multi-turn chatbots - you provide list of messages inside `input` to build conversation:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

More about dis functionality go come for next chapter.

## Exercise - your first text generation app

Now we don learn how to set up and configure openai, na time to build your first text generation app. To build, follow steps:

1. Create virtual environment and install openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > If you dey use Windows, type `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Find your Azure OpenAI key by going [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), search `Open AI`, select `Open AI resource`, then select `Keys and Endpoint` and copy `Key 1`.

1. Create _app.py_ file and put this code inside:

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
   > If you dey use plain OpenAI (no Azure), use `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (no `base_url`) and pass model name like `gpt-4o-mini` instead deployment name.

   You go see output like dis:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Different types of prompts, for different tins

Now you don see how to generate text with prompt. You even get program wey don start run wey you fit change to generate different text type.

Prompts fit use for plenty task. For example:

- **Generate type of text**. For example, you fit generate poem, quiz questions etc.
- **Lookup information**. You fit use prompts to find info like example 'What does CORS mean in web development?'.
- **Generate code**. You fit use prompts to generate code, example develop regular expression to validate emails or even generate whole program, like web app?

## More practical use case: recipe generator

Imagine say you get ingredients for house and you wan cook sometin. For dat, you need recipe. One way to find recipe na use search engine or you fit use LLM.

You fit write prompt like dis:

> "Show me 5 recipes for dish with these ingredients: chicken, potatoes, and carrots. For each recipe, list all ingredients used"

If you give prompt like dis, you fit get response like:

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

Dis result good well well, I sabi wetin to cook. Now wetin fit make am better be:

- Filter ingredients wey I no like or wey I dey allergic to.
- Make shopping list, if I no get all ingredients for house.

For dis cases, make we add one more prompt:

> "Please remove recipes with garlic as I dey allergic and replace am with something else. Also, please produce shopping list for recipes, considering say I get chicken, potatoes and carrots for house."

Now you get new result, as e be so:

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

Dis na your five recipes, no garlic inside and you get shopping list based on wetin you get for house.

## Exercise - build recipe generator

Now we don act one scenario, make we write code wey match di scenario. Follow steps below:

1. Use di _app.py_ file wey you get as start point
1. Find `prompt` variable and change im code to dis:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   If you run code now, you go see output like dis:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, your LLM fit give different results every time because e no dey deterministic.

   Correct, make we see how to improve tins. To improve, we wan make sure code flexible, so ingredients and number of recipes fit change.

1. Make we change code like dis:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # put di number of recipes join inside di prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Test code fit look like dis:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Improve by adding filter and shopping list

We get working app wey fit produce recipes and e flexible as e dey rely on user input, number of recipes and ingredients.

To make am better, we wan add dis ones:

- **Filter ingredients wey we no like**. We wan fit filter ingredients we no like or allergic to. To do dis, we fit edit prompt and add filter instruction at end like dis:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  For above, we add `{filter}` at end of prompt and also catch filter value from user.

  Example input running program fit be like dis:

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

  You fit see any recipes with milk don filter out. But if you lactose intolerant, you fit also want filter recipes wey get cheese, so you gots be clear.


- **Make one shopping list**. We wan make one shopping list, dey look wetin we don get for house.

  For dis work, we fit try solve everything for one prompt or split am into two prompts. Make we try di second waka. Here we dey suggest add one more prompt, but for dat to work, we gats add di result of di first prompt as info for di second prompt.

  Find di part wey dey code wey dey print result from di first prompt, den add dis code down below:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print di response
  print("Shopping list:")
  print(response.output_text)
  ```

  Make you watch di following:

  1. We dey form one new prompt by adding di result wey come from di first prompt inside di new prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. We dey make one new request, but also dey check di number of tokens we ask for in di first prompt, so dis time we talk say `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     If you run dis code, di output we go get na dis one:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Make your setup beta

Wetin we get so far na code wey dey work, but some small corrections fit make am beta. Some tins we gats do be like dis:

- **Separate secret tins from code**, like API key. Secret tins no supposed dey inside code, dem suppose dey for safe place. To separate secret tins from code, we fit use environment variables and tools like `python-dotenv` to load dem from file. Dis na how e go be for code:

  1. Create `.env` file wey get dis tins:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Note, for Azure OpenAI for Microsoft Foundry, you gats set dis environment variables instead:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     For code, you go load dem environment variables like dis:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Talk about token length**. We suppose consider how many tokens we need to make text we want. Tokens dey cost money, so if we fit, make we try reduce di number of tokens we dey use. Example, fit talk di prompt to make e use less tokens?

  To change how many tokens, you fit use `max_output_tokens` parameter. Example, if you want make e use 100 tokens, you go do:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Try different temperature level**. Temperature na one thing we no talk before but e important for how our program go perform. If temperature too high, output go dey more random. If temperature low, output go dey more predictable. Think if you want change your output or no.

  To change temperature, you fit use `temperature` parameter. Example, if you want set temperature to 0.5, you go do:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Note, if temperature near 1.0, output go dey more different.

## Assignment

For dis assignment, you fit decide wetin you go build.

Here be some ideas:

- Make di recipe generator app better. Play with temperature values and prompts to see wetin fit come out.
- Build "study buddy". Dis app suppose fit answer questions about one topic, like Python. You fit get prompts like "Wetin be certain topic for Python?", or one prompt wey talk say, show me code for this topic.
- History bot, make history come alive, tell di bot make e act like one historical person and ask am questions about e life and time.

## Solution

### Study buddy

Dis na one starter prompt, see how you fit use am and change am to your liking.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

Here be some prompts you fit use:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Knowledge check

Wetin di temperature concept dey do?

1. E dey control how random di output dey.
1. E dey control how big di answer go be.
1. E dey control how many tokens we go use.

## 🚀 Challenge

When you dey do di assignment, try change di temperature. Try put am for 0, 0.5, and 1. Remember say 0 na di least change and 1 na di most. Which one better for your app?

## Great Work! Continue Your Learning

After you finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue dey learn more about Generative AI!

Head go Lesson 7 where we go waka look how to [build chat applications](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->