# Di way wey we go take build Text Generation Applications

[![Di way wey we go take build Text Generation Applications](../../../translated_images/pcm/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Click di picture wey dey top to watch video lesson for dis one)_

As you don see so far for dis curriculum, di main concepts be like prompts and even one full field wey dem dey call "prompt engineering". Plenty tools you fit use like ChatGPT, Office 365, Microsoft Power Platform and others, dey help you use prompts to do things.

If you wan add dis kind experience insaid app, you need sabi concepts like prompts, completions and choose one library wey you go fit work with. Na exactly dis one you go learn for dis chapter.

## Introduction

For dis chapter, you go:

- Learn about openai library and dia main concepts.
- Build text generation app wey use openai.
- Understand how you fit use concepts like prompt, temperature, and tokens to build text generation app.

## Wetin you go fit achieve

When dis lesson finish, you go fit:

- Explain wetin text generation app be.
- Build text generation app wey use openai.
- Configure your app to use more or less tokens and fit change the temperature, so output go dey different.

## Wetin be text generation app?

Normally if you dey build app e get some kind interface like dis one down:

- Command-based. Console apps be typical apps wey you go type command and e go do di work. Example na `git` wey be command-based app.
- User interface (UI). Some apps get graphical user interfaces (GUIs) wey you fit click button, put text, choose options and plenty more.

### Console and UI apps get limit

Compare am to command-based app wey you just dey type command:

- **E get limit**. You no fit just type any command, na only di commands wey di app fit support.
- **E dey language specific**. Some apps fit support many languages but normally, app go be for one language unless you add more support.

### Wetin good for text generation apps

So how text generation app different?

For text generation app, you get more freedom, you no limit to commands or one input language. You fit use normal language to interact with the app. Another benefit na say you dey talk to one data source wey don train from plenty information, but normal app fit get limit on wetin dey database.

### Wetin I fit build with text generation app?

Plenty things fit build. Example:

- **Chatbot**. Chatbot wey go answer questions about your company and products go make sense.
- **Helper**. LLMs sabi summarize text, find insights for text, produce texts like resumes and more.
- **Code assistant**. Depending on di language model, you fit build code helper wey go help you write code. Example, you fit use GitHub Copilot or ChatGPT to help write code.

## How I go start?

You need way to integrate with LLM, normally e get two ways:

- Use API. Here you dey create web requests with prompt and you go get generated text back.
- Use library. Libraries dey wrap API calls make dem easy to use.

## Libraries/SDKs

Some popular libraries wey you fit use with LLMs na:

- **openai**, dis library dey easy to connect model and send prompts.

Then some libraries dey high level like:

- **Langchain**. Langchain popular and na Python dey support am.
- **Semantic Kernel**. Semantic Kernel na Microsoft library wey dey support C#, Python and Java.

## First app wey use openai

Make we check how to build first app, which libraries we need, how much e cost and so on.

### Install openai

Plenty libraries dey for working with OpenAI or Azure OpenAI. You fit use many programming languages like C#, Python, JavaScript, Java and more. We choose `openai` Python library, so we go use `pip` install am.

```bash
pip install openai
```

### Create resource

You need do di following:

- Create account for Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Get access to Azure OpenAI. Go [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) and request access.

  > [!NOTE]
  > As we dey write dis, you need apply for access to Azure OpenAI.

- Install Python <https://www.python.org/>
- Create Azure OpenAI Service resource. Check guide for how to [create resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Find API key and endpoint

Now, you go tell your `openai` library which API key to use. To find am, go "Keys and Endpoint" section for Azure OpenAI resource and copy "Key 1" value.

![Keys and Endpoint resource blade for Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

When you don copy dis info, make we tell libraries to use am.

> [!NOTE]
> E better make you keep API key apart from your code. You fit do dis by using environment variables.
>
> - Set environment variable `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Setup Azure configuration

If you dey use Azure OpenAI (part of Microsoft Foundry now), dis na how to setup. We use standard `OpenAI` client point to Azure OpenAI `/openai/v1/` endpoint, wey work with Responses API no need `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

For here, we dey set the following:

- `api_key`, na your API key wey you find for Azure or Foundry portal.
- `base_url`, na Foundry resource endpoint with `/openai/v1/` added. Stable v1 endpoint work for OpenAI and Azure OpenAI, no need `api_version` management.

> [!NOTE] > `os.environ` dey read environment variables. You fit use am to read variables like `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT`. Set environment variables for your terminal or use library like `dotenv`.

## Generate text

To generate text, use Responses API via `responses.create` method. Example be dis:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

For di code wey dey above, we create response, pass model and prompt. Then we print di generated text using `response.output_text`.

### Multi-turn conversation

Responses API good for single-turn text generation and multi-turn chatbots - you dey provide message list in `input` to make conversation:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

More about dis one go come for next chapter.

## Exercise - your first text generation app

Now we don learn how to setup and configure openai, time reach to build your first text generation app. To build am, follow steps:

1. Create virtual environment and install openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > If you dey use Windows, type `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Find your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search `Open AI`, select `Open AI resource` then select `Keys and Endpoint` and copy `Key 1` value.

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
   > If you dey use normal OpenAI (no Azure), use `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (no `base_url`) and pass model name like `gpt-5-mini` instead of deployment name.

   You go see output like dis:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Different types of prompts for different things

Now you don see how to generate text using prompt. You even get program wey dey run wey you fit change to generate different type text.

Prompts fit do plenty tasks. Example:

- **Generate text wey different**. You fit generate poem, quiz questions and so on.
- **Find information**. Prompt fit help you find information like 'Wetin CORS mean for web development?'.
- **Generate code**. Use prompt to generate code like regular expression to validate email or even build full web app.

## One better example: recipe generator

Imagine say you get ingredients for house and you wan cook something. You need recipe. One way to find recipe na search engine, another na use LLM.

You fit write prompt like dis:

> "Show me 5 recipes for di dish wey get ingredients: chicken, potatoes, and carrots. Make recipe include all ingredients."

With dat prompt, you fit see something like:

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

Dis result good well, I know wetin to cook. Now, wetin fit still improve na:

- Remove ingredients wey I no like or I allergic to.
- Make shopping list if I no get all ingredients.

For that one, make we add another prompt:

> "Please remove recipes with garlic cos I allergic, replace am with something else. Also, make shopping list for recipes, I get chicken, potatoes, and carrots already."

Now you get new answer:

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

Na you five recipes dat, garlic no dey, and you get shopping list based on wetin you get.

## Exercise - build recipe generator

Now we don play this scenario, make we write code to do am. To do am, follow steps:

1. Use _app.py_ file as starting point
1. Find `prompt` variable and change code to:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   When you run code now, you fit see output like:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, your LLM no dey give same answer every time, so output fit change when you run am again.

   Good, make we see how to improve am. To improve, we wan make code flexible, so ingredients and recipe number fit change.

1. Make code changes like this:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Make test run fit look like dis:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Improve by adding filter and shopping list

Now we get app wey fit make recipes and e flexible as e dey take user input for recipe count and ingredients.

To make am better, we wan add:

- **Filter ingredients**. Make we fit filter ingredients we no like or allergic to. We fit change prompt, add filter condition for end:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Dis one we add `{filter}` for prompt end and capture filter value from user.

  Sample program run input fit like dis:

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

  As you fit see, recipes wey get milk don comot. But if person get lactose intolerance, fit want remove cheese recipes too, so e good to clear.

- **Make shopping list**. Make we generate shopping list based on wetin we get.

  For dis one, we fit try solve all for one prompt or split am two prompts. Make we try the second way. For dis, we add another prompt, but to make am work, we go take first prompt result as context for second prompt.

  Find place wey code dey print first prompt result and add code below:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Note this:

  1. We dey build new prompt by adding first prompt result to new prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. We request new output also setting token count, this time `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     If you run dis code, you go see output like:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Make your setup better

Wetin we get so far na code wey dey work, but some small changes dey we suppose do to make am beta pass. Some tins we fit do na:

- **Separate secrets from code**, like the API key. Secrets no suppose dey inside code and we suppose put dem for safe place. To separate secrets from code, we fit use environment variables and libraries like `python-dotenv` to load dem from file. Dis na how e go be for code:

  1. Create one `.env` file wey get dis kain content:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Note, for Azure OpenAI for Microsoft Foundry, you need set dis kain environment variables instead:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     For code, na so you go load environment variables:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **One word on token length**. We suppose think how many tokens we need to generate di text we want. Tokens dey cost money, so if e fit, we suppose try use less tokens. Example, fit we talk di prompt so that e use less tokens?

  To change di tokens wey you dey use, you fit use di `max_output_tokens` parameter. Example if you want use 100 tokens, you go do like this:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experiment with temperature**. Temperature na somtin we never talk before but e important for how our program go perform. Di higher temperature value, di more random di output go be. Di lower di temperature value, di more you fit predict di output. Make you consider if you want make your output get variation or no.

  To change temperature, you fit use di `temperature` parameter. Example if you want use temperature 0.5, you go do like this:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Note, di closer to 1.0, di more di output go vary.

- **Reasoning models no dey use `temperature`**. Dis one na important shift for 2026. Di current, non-deprecated models for Microsoft Foundry na **reasoning models** (di GPT-5 family, o-series) - and dem **no dey support `temperature` or `top_p`** (nor `max_tokens`; use `max_output_tokens`). If you send `temperature` to `gpt-5-mini` you go get "parameter not supported" error. So to try di temperature example wey we talk before, point am to model wey still get sampling controls - example na open **Llama** model like `Llama-3.3-70B-Instruct` from di [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), wey you fit call through Foundry Models / Azure AI Inference endpoint (di same way as di `githubmodels-*` samples). For reasoning models like GPT-5, you control di output differently:
  - **Prompt engineering** - clear instructions, examples, and structured output (check lesson [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) dey do di work wey di sampling knobs use to do.
  - **Reasoning controls** - parameters like reasoning effort/verbosity dey tradeoff depth of reasoning against latency and cost.

  For short: `temperature`/`top_p` still valid for plenty models (Llama, Mistral, Phi, and di GPT-4.x family - though GPT-4.x dey deprecate), but di way forward na prompt engineering + reasoning controls for reasoning models like GPT-5.

## Assignment

For dis assignment, you fit choose wetin you wan build.

Here some suggestions:

- Tweak di recipe generator app to make am beta pass. Play around with temperature values, and di prompts to see wetin you fit come up with.
- Build one "study buddy". Dis app suppose fit answer questions about one topic, for example Python, you fit get prompts like "Wetin be some topic for Python?", or prompt wey talk, show me code for one certain topic etc.
- History bot, make history come alive, tell di bot to play one certain historical character and ask am questions about e life and times.

## Solution

### Study buddy

Below na starter prompt, see how you fit use am and tweak am to your liking.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

Here some prompts wey you fit use:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Knowledge check

Wetin di concept temperature dey do?

1. E dey control how random di output be.
1. E dey control how big di response be.
1. E dey control how many tokens we use.

## 🚀 Challenge

When you dey work on di assignment, try make temperature different, try set am to 0, 0.5, and 1. Remember say 0 na di least variation and 1 na di most. Which value dey work best for your app?

## Great Work! Continue Your Learning

After you don finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to improve your Generative AI knowledge!

Head go Lesson 7 wey we go see how to [build chat applications](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->