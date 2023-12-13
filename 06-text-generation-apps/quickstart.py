import os
from dotenv import load_dotenv

# Load environment variables from test.env file
# without env file, would call like this: AZURE_OPENAI_KEY='3288625089822e' AZURE_OPENAI_ENDPOINT='https://oaijh.openai.azure.com/'  python quickstart.py

load_dotenv()
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-10-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = 'gpt-35-turbo-instruct'  # This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

print('Sending a test completion job')
start_phrase = f'Show me {no_recipes} recipes for a dish with the following ingredients I already have: {ingredients}. Per recipe, list all the ingredients used but makes sure it is {filter}'
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=600)
print(response.choices[0].text)

response_text = response.choices[0].text
start_phrase2 = f'{response_text} . Please provide a shopping list for the ingredients that I do not have.'
response2 = client.completions.create(model=deployment_name, prompt=start_phrase2, max_tokens=1600)
print('Shopping list:')
print(response2.choices[0].text)