import openai
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

openai.api_key = os.getenv("API_KEY") 

# enable below if you use Azure Open AI
openai.api_type = 'azure' 
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")


no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"


# engine
engine = "davinci-001"

# deployment_id
deployment_name = "chris-eastus"

completion = openai.Completion.create(engine=deployment_name, prompt=prompt, max_tokens=600)

# print response
print("Recipes:")
print(completion.choices[0].text)

old_prompt_result = completion.choices[0].text
prompt_shopping = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

new_prompt = f"{old_prompt_result} {prompt_shopping}"
completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=600)

# print response
print("Shopping list:")
print(completion.choices[0].text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.

