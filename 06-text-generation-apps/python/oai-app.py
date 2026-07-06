from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI()
deployment = "gpt-4o-mini"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
# make a request using the Responses API
response = client.responses.create(model=deployment, input=prompt, store=False)

# print response
print(response.output_text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
