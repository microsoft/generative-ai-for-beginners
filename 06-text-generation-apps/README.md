# Building Text Generation Applications

[![Building Text Generation Applications](./images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Click the image above to view video of this lesson)_

You've seen so far through this curriculum that there are core concepts like prompts and even a whole discipline called "prompt engineering". Many tools you can interact with like ChatGPT, Office 365, Microsoft Power Platform and more, support you using prompts to accomplish something.

For you to add such an experience to an app, you need to understand concepts like prompts, completions and choose a library to work with. That's exactly what you'll learn in this chapter.

## Introduction

In this chapter, you will:

- Learn about the openai library and it's core concepts.
- Build a text generation app using openai.
- Understand how to use concepts like prompt, temperature, and tokens to build a text generation app.

## Learning goals

At the end of this lesson, you'll be able to:

- Explain what a text generation app is.
- Build a text generation app using openai.
- Configure your app to use more or less tokens and also change the temperature, for a varied output.

## What is a text generation app?

Normally when you build an app it has some kind of interface like the following:

- Command-based. Console apps are typical apps where you type a command and it carries out a task. For example, `git` is a command-based app.
- User interface (UI). Some apps have graphical user interfaces (GUIs) where you click buttons, input text, select options and more.

### Console and UI apps are limited

Compare it to a command-based app where you type a command:

- **It's limited**. You can't just type any command, only the ones that the app supports.
- **Language specific**. Some apps support many languages, but by default the app is built for a specific language, even if you can add more language support.

### Benefits of text generation apps

So how is a text generation app different?

In a text generation app, you have more flexibility, you're not limited to a set of commands or a specific input language. Instead, you can use natural language to interact with the app. Another benefit is that because you're already interacting with a data source that has been trained on a vast corpus of information, whereas a traditional app might be limited on what's in a database.

### What can I build with a text generation app?

There are many things you can build. For example:

- **A chatbot**. A chatbot answering questions about topics, like your company and its products could be a good match.
- **Helper**. LLMs are great at things like summarizing text, getting insights from text, producing text like resumes and more.
- **Code assistant**. Depending on the language model you use, you can build a code assistant that helps you write code. For example, you can use a product like GitHub Copilot as well as ChatGPT to help you write code.

## How can I get started?

Well, you need to find a way to integrate with an LLM which usually entails the following two approaches:

- Use an API. Here you're constructing web requests with your prompt and get generated text back.
- Use a library. Libraries help encapsulate the API calls and make them easier to use.

## Libraries/SDKs

There are a few well known libraries for working with LLMs like:

- **openai**, this library makes it easy to connect to your model and send in prompts.

Then there are libraries that operate on a higher level like:

- **Langchain**. Langchain is well known and supports Python.
- **Semantic Kernel**. Semantic Kernel is a library by Microsoft supporting the languages C#, Python, and Java.

## First app using openai

Let's see how we can build our first app, what libraries we need, how much is required and so on.

### Install openai

There are many libraries out there for interacting with OpenAI or Azure OpenAI. It's possible to use numerous programming languages as well like C#, Python, JavaScript, Java and more. We've chosen to use the `openai` Python library, so we'll use `pip` to install it.

```bash
pip install openai
```

### Create a resource

You need to carry out the following steps:

- Create an account on Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Gain access to Azure OpenAI. Go to [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) and request access.

  > [!NOTE]
  > At the time of writing, you need to apply for access to Azure OpenAI.

- Install Python <https://www.python.org/>
- Have created an Azure OpenAI Service resource. See this guide for how to [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Locate API key and endpoint

At this point, you need to tell your `openai` library what API key to use. To find your API key, go to "Keys and Endpoint" section of your Azure OpenAI resource and copy the "Key 1" value.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Now that you have this information copied, let's instruct the libraries to use it.

> [!NOTE]
> It's worth separating your API key from your code. You can do so by using environment variables.
>
> - Set the environment variable `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Setup configuration Azure

If you're using Azure OpenAI, here's how you setup configuration:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Above we're setting the following:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. Here's an example:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

In the above code, we create a completion object and pass in the model we want to use and the prompt. Then we print the generated text.

### Chat completions

So far, you've seen how we've been using `Completion` to generate text. But there's another class called `ChatCompletion` that is more suited for chatbots. Here's an example of using it:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

More on this functionality in an upcoming chapter.

## Exercise - your first text generation app

Now that we learned how to set up and configure openai, it's time to build your first text generation app. To build your app, follow these steps:

1. Create a virtual environment and install openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > If you're using Windows type `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. Create an _app.py_ file and give it the following code:

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
   completion = client.chat.completions.create(model=deployment, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > If you're using Azure OpenAI, you need to set the `api_type` to `azure` and set the `api_key` to your Azure OpenAI key.

   You should see an output like the following:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Different types of prompts, for different things

Now you've seen how to generate text using a prompt. You even have a program up and running that you can modify and change to generate different types of text.

Prompts can be used for all sorts of tasks. For example:

- **Generate a type of text**. For example, you can generate a poem, questions for a quiz etc.
- **Lookup information**. You can use prompts to look for information like the following example 'What does CORS mean in web development?'.
- **Generate code**. You can use prompts to generate code, for example developing a regular expression used to validate emails or why not generate an entire program, like a web app?

## A more practical use case: a recipe generator

Imagine you have ingredients at home and you want to cook something. For that, you need a recipe. A way to find recipes is to use a search engine or you could use an LLM to do so.

You could write a prompt like so:

> "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"

Given the above prompt, you might get a response similar to:

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

This outcome is great, I know what to cook. At this point, what could be useful improvements are:

- Filtering out ingredients I don't like or am allergic to.
- Produce a shopping list, in case I don't have all the ingredients at home.

For the above cases, let's add an additional prompt:

> "Please remove recipes with garlic as I'm allergic and replace it with something else. Also, please produce a shopping list for the recipes, considering I already have chicken, potatoes and carrots at home."

Now you have a new result, namely:

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

That's your five recipes, with no garlic mentioned and you also have a shopping list considering what you already have at home.

## Exercise - build a recipe generator

Now that we have played out a scenario, let's write code to match the demonstrated scenario. To do so, follow these steps:

1. Use the existing _app.py_ file as a starting point
1. Locate the `prompt` variable and change its code to the following:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   If you now run the code, you should see an output similar to:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, your LLM is nondeterministic, so you might get different results every time you run the program.

   Great, let's see how we can improve things. To improve things, we want to make sure the code is flexible, so ingredients and number of recipes can be improved and changed.

1. Let's change the code in the following way:

   ```python
   no_recipes = input("No of recipes (for example, 5: ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Taking the code for a test run, could look like this:

   ```output
   No of recipes (for example, 5: 3
   List of ingredients (for example, chicken, potatoes, and carrots: milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Improve by adding filter and shopping list

We now have a working app capable of producing recipes and it's flexible as it relies on inputs from the user, both on the number of recipes but also the ingredients used.

To further improve it, we want to add the following:

- **Filter out ingredients**. We want to be able to filter out ingredients we don't like or are allergic to. To accomplish this change, we can edit our existing prompt and add a filter condition to the end of it like so:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Above, we add `{filter}` to the end of the prompt and we also capture the filter value from the user.

  An example input of running the program can now look like so:

  ```output
  No of recipes (for example, 5: 3
  List of ingredients (for example, chicken, potatoes, and carrots: onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free: no milk

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

  As you can see, any recipes with milk in it has been filtered out. But, if you're lactose intolerant, you might want to filter out recipes with cheese in them as well, so there's a need to be clear.

- **Produce a shopping list**. We want to produce a shopping list, considering what we already have at home.

  For this functionality, we could either try to solve everything in one prompt or we could split it up into two prompts. Let's try the latter approach. Here we're suggesting adding an additional prompt, but for that to work, we need to add the result of the former prompt as context to the latter prompt.

  Locate the part in the code that prints out the result from the first prompt and add the following code below:

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

  Note the following:

  1. We're constructing a new prompt by adding the result from the first prompt to the new prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. We make a new request, but also considering the number of tokens we asked for in the first prompt, so this time we say `max_tokens` is 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Taking this code for a spin, we now arrive at the following output:

     ```output
     No of recipes (for example, 5: 2
     List of ingredients (for example, chicken, potatoes, and carrots: apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free: sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Improve your setup

What we have so far is code that works, but there are some tweaks we should be doing to improve things further. Some things we should do are:

- **Separate secrets from code**, like the API key. Secrets do not belong in code and should be stored in a secure location. To separate secrets from code, we can use environment variables and libraries like `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file with the following content:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Note, for Azure, you need to set the following environment variables:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     In code, you would load the environment variables like so:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **A word on token length**. We should consider how many tokens we need to generate the text we want. Tokens cost money, so where possible, we should try to be economical with the number of tokens we use. For example, can we phrase the prompt so that we can use less tokens?

  To change the tokens used, you can use the `max_tokens` parameter. For example, if you want to use 100 tokens, you would do:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimenting with temperature**. Temperature is something we haven't mentioned so far but is an important context for how our program performs. The higher the temperature value the more random the output will be. Conversely the lower the temperature value the more predictable the output will be. Consider whether you want variation in your output or not.

  To alter the temperature, you can use the `temperature` parameter. For example, if you want to use a temperature of 0.5, you would do:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Note, the closer to 1.0, the more varied the output.

## Assignment

For this assignment, you can choose what to build.

Here are some suggestions:

- Tweak the recipe generator app to improve it further. Play around with temperature values, and the prompts to see what you can come up with.
- Build a "study buddy". This app should be able to answer questions about a topic for example Python, you could have prompts like "What is a certain topic in Python?", or you could have a prompt that says, show me code for a certain topic etc.
- History bot, make history come alive, instruct the bot to play a certain historical character and ask it questions about its life and times.

## Solution

### Study buddy

Below is a starter prompt, see how you can use it and tweak it to your liking.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

Here are some prompts you could be using:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Knowledge check

What does the concept temperature do?

1. It controls how random the output is.
1. It controls how big the response is.
1. It controls how many tokens are used.

## 🚀 Challenge

When working on the assignment, try to vary the temperature, try set it to 0, 0.5, and 1. Remember that 0 is the least varied and 1 is the most, what value works best for your app?

## Great Work! Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

Head over to Lesson 7 where we will look at how to [build chat applications](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!
