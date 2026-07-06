from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure Azure OpenAI service client 
client = OpenAI()
deployment = "gpt-4o-mini"

no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}: "

response = client.responses.create(model=deployment, input=prompt, max_output_tokens=600, temperature=0.1, store=False)


# print response
print("Recipes:")
old_prompt_result = response.output_text
if not old_prompt_result:
    print("No response received.")
else:
    print(old_prompt_result)

    prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "
    new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
    response = client.responses.create(model=deployment, input=new_prompt, max_output_tokens=600, temperature=0, store=False)

    # print response
    print("\n=====Shopping list ======= \n")
    if response.output_text:
        print(response.output_text)

