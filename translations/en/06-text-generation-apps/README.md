<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T22:29:17+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "en"
}
-->
# Building Text Generation Applications

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.en.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Click the image above to watch the video for this lesson)_

Throughout this curriculum, you've learned about core concepts like prompts and the field of "prompt engineering." Many tools, such as ChatGPT, Office 365, Microsoft Power Platform, and others, allow you to use prompts to achieve specific tasks.

To add such functionality to your app, you need to understand concepts like prompts, completions, and choose a library to work with. This chapter will teach you exactly that.

## Introduction

In this chapter, you will:

- Learn about the openai library and its core concepts.
- Build a text generation app using openai.
- Understand how to use concepts like prompt, temperature, and tokens to create a text generation app.

## Learning goals

By the end of this lesson, you'll be able to:

- Explain what a text generation app is.
- Build a text generation app using openai.
- Configure your app to use more or fewer tokens and adjust the temperature for varied output.

## What is a text generation app?

Typically, when you build an app, it has some kind of interface, such as:

- Command-based. Console apps are common examples where you type a command, and the app performs a task. For instance, `git` is a command-based app.
- User interface (UI). Some apps have graphical user interfaces (GUIs) where you click buttons, input text, select options, and more.

### Console and UI apps are limited

Compare this to a command-based app where you type a command:

- **It's limited**. You can't type just any command; only the ones supported by the app.
- **Language specific**. While some apps support multiple languages, they are often designed for a specific language by default, even if additional language support can be added.

### Benefits of text generation apps

How is a text generation app different?

A text generation app offers more flexibility. You're not restricted to a set of commands or a specific input language. Instead, you can use natural language to interact with the app. Another advantage is that the app interacts with a data source trained on a vast amount of information, whereas traditional apps might be limited to the data in their database.

### What can I build with a text generation app?

There are many possibilities, such as:

- **A chatbot**. A chatbot that answers questions about topics like your company and its products could be a great use case.
- **Helper**. Large language models (LLMs) excel at tasks like summarizing text, extracting insights, generating content like resumes, and more.
- **Code assistant**. Depending on the language model you use, you can create a code assistant to help you write code. For example, tools like GitHub Copilot and ChatGPT can assist in coding.

## How can I get started?

To integrate with an LLM, you typically have two options:

- Use an API. This involves constructing web requests with your prompt and receiving generated text in response.
- Use a library. Libraries simplify API calls and make them easier to use.

## Libraries/SDKs

Some well-known libraries for working with LLMs include:

- **openai**, which makes it easy to connect to your model and send prompts.

Other libraries operate at a higher level, such as:

- **Langchain**. A popular library that supports Python.
- **Semantic Kernel**. A Microsoft library that supports C#, Python, and Java.

## First app using openai

Let's explore how to build your first app, including the required libraries and setup.

### Install openai

There are many libraries available for interacting with OpenAI or Azure OpenAI. You can use various programming languages like C#, Python, JavaScript, Java, and more. For this example, we'll use the `openai` Python library and install it using `pip`.

```bash
pip install openai
```

### Create a resource

Follow these steps:

- Create an account on Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Request access to Azure OpenAI. Visit [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst).

  > [!NOTE]
  > At the time of writing, you need to apply for access to Azure OpenAI.

- Install Python <https://www.python.org/>
- Create an Azure OpenAI Service resource. Follow this guide to [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Locate API key and endpoint

Next, you need to configure your `openai` library with your API key. To find your API key, go to the "Keys and Endpoint" section of your Azure OpenAI resource and copy the "Key 1" value.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Once you have this information, you can instruct the library to use it.

> [!NOTE]
> It's a good practice to separate your API key from your code. You can use environment variables for this purpose.
>
> - Set the environment variable `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Setup configuration Azure

If you're using Azure OpenAI, here's how to configure it:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

In the code above, we set the following:

- `api_type` to `azure`, indicating the library should use Azure OpenAI instead of OpenAI.
- `api_key`, which is your API key from the Azure Portal.
- `api_version`, specifying the API version you want to use. The latest version at the time of writing is `2023-05-15`.
- `api_base`, which is the API endpoint found in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read variables like `OPENAI_API_KEY` and `API_BASE`. Set these variables in your terminal or use a library like `dotenv`.

## Generate text

To generate text, use the `Completion` class. Here's an example:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

In this code, we create a completion object, specify the model we want to use, and provide the prompt. Then, we print the generated text.

### Chat completions

So far, we've used `Completion` to generate text. However, there's another class called `ChatCompletion` that's better suited for chatbots. Here's an example:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

We'll explore this functionality further in an upcoming chapter.

## Exercise - your first text generation app

Now that we've learned how to set up and configure openai, let's build your first text generation app. Follow these steps:

1. Create a virtual environment and install openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > If you're using Windows, type `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Find your Azure OpenAI key by visiting [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), searching for `Open AI`, selecting the `Open AI resource`, and then selecting `Keys and Endpoint` to copy the `Key 1` value.

1. Create an _app.py_ file and add the following code:

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
   > If you're using Azure OpenAI, set the `api_type` to `azure` and use your Azure OpenAI key for `api_key`.

   You should see an output similar to the following:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Different types of prompts, for different things

Now you've seen how to generate text using a prompt. You even have a working program that you can modify to generate different types of text.

Prompts can be used for various tasks, such as:

- **Generate specific types of text**. For example, you can create a poem, quiz questions, etc.
- **Search for information**. Prompts can be used to find information, such as "What does CORS mean in web development?"
- **Generate code**. Prompts can help create code, such as a regular expression for email validation or even an entire program like a web app.

## A more practical use case: a recipe generator

Imagine you have some ingredients at home and want to cook something. To do that, you need a recipe. You could use a search engine or an LLM to find recipes.

You could write a prompt like this:

> "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used."

With this prompt, you might get a response like:

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

This result is great—you now know what to cook. To improve it further, you could:

- Filter out ingredients you dislike or are allergic to.
- Generate a shopping list in case you don't have all the necessary ingredients at home.

For these improvements, you could add another prompt:

> "Please remove recipes with garlic as I'm allergic and replace it with something else. Also, please produce a shopping list for the recipes, considering I already have chicken, potatoes, and carrots at home."

Now you'll get a new result:

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

Here are your five recipes, with no garlic included, and a shopping list based on what you already have at home.

## Exercise - build a recipe generator

Now that we've explored a scenario, let's write code to match it. Follow these steps:

1. Use the existing _app.py_ file as a starting point.
1. Locate the `prompt` variable and update its code to the following:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Running the code should produce an output similar to:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE: Your LLM is nondeterministic, so you might get different results each time you run the program.

   Great! Let's see how we can improve it. To make the code more flexible, we want to allow changes to the ingredients and the number of recipes.

1. Update the code as follows:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testing the updated code might look like this:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Improve by adding filter and shopping list

We now have a functional app that generates recipes and is flexible, relying on user inputs for the number of recipes and the ingredients.

To enhance it further, let's add the following features:

- **Filter out ingredients**. Allow users to exclude ingredients they dislike or are allergic to. To implement this, edit the existing prompt and add a filter condition at the end, like this:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Here, `{filter}` is added to the end of the prompt, and the filter value is captured from the user.

  An example input when running the program might look like this:

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

  As you can see, recipes containing milk have been filtered out. If you're lactose intolerant, you might also want to exclude recipes with cheese, so it's important to be specific.

- **Generate a shopping list**. Create a shopping list based on what you already have at home.

  For this functionality, you could either solve everything in one prompt or split it into two prompts. Let's try the latter approach. Add the result of the first prompt as context for the second prompt.

  Locate the part of the code where the result from the first prompt is printed, and add the following code below:
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

  1. We're creating a new prompt by appending the result from the first prompt to the new one:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. We make a new request, but this time we account for the number of tokens used in the first prompt, so we set `max_tokens` to 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Running this code, we now get the following output:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Enhance your setup

The code we have so far works, but there are some adjustments we can make to improve it further. Here are some suggestions:

- **Separate secrets from code**, such as the API key. Secrets should not be hardcoded and should be stored securely. To achieve this, we can use environment variables and libraries like `python-dotenv` to load them from a file. Here's an example of how this can be implemented:

  1. Create a `.env` file with the following content:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Note: For Azure, you need to set the following environment variables:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     In your code, you can load the environment variables like this:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Consider token length**. It's important to think about how many tokens are necessary to generate the desired text. Tokens cost money, so it's a good idea to be efficient with their usage. For instance, can the prompt be rephrased to use fewer tokens?

  To adjust the number of tokens used, you can modify the `max_tokens` parameter. For example, if you want to use 100 tokens, you would write:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experiment with temperature**. Temperature is an important factor that influences how your program behaves. A higher temperature value results in more random outputs, while a lower value makes the output more predictable. Decide whether you want more variation or consistency in your results.

  To change the temperature, use the `temperature` parameter. For example, if you want to set the temperature to 0.5, you would write:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Note: The closer the value is to 1.0, the more varied the output will be.

## Assignment

For this assignment, you can choose what to build.

Here are some ideas:

- Improve the recipe generator app further. Experiment with temperature values and prompts to see what you can create.
- Develop a "study buddy." This app should be able to answer questions about a specific topic, such as Python. You could use prompts like "What is a certain topic in Python?" or "Show me code for a certain topic," etc.
- Create a history bot that brings history to life. Instruct the bot to play the role of a historical figure and ask it questions about their life and era.

## Solution

### Study buddy

Below is a starter prompt. See how you can use it and customize it to suit your needs.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

Here are some prompts you could use:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Knowledge check

What does the concept of temperature control?

1. It determines how random the output is.
1. It determines the size of the response.
1. It determines the number of tokens used.

## 🚀 Challenge

While working on the assignment, experiment with different temperature values. Try setting it to 0, 0.5, and 1. Remember, 0 produces the least variation, and 1 produces the most. Which value works best for your app?

## Great Work! Continue Your Learning

After completing this lesson, explore our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to further enhance your Generative AI skills!

Move on to Lesson 7, where we will dive into [building chat applications](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.