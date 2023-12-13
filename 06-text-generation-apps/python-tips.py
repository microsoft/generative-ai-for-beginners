import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-10-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = 'gpt-35-turbo-instruct'  # This will correspond to the custom name you chose for your deployment when you deployed a model.

number_of_tips = input("Number of tips (for example, 5: ")
topic = input("Topic (for example, general, environments, : ")

start_phrase = f'You are an expert teacher on python. Your job is to provide tips to a beginner understand python. Please provide them with {number_of_tips} tips on {topic}.'
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=600)
print('Here are your tips:')
print(response.choices[0].text)