from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure the OpenAI client against the Azure OpenAI (Microsoft Foundry) v1 endpoint
client = OpenAI(
  api_key=os.environ['AZURE_OPENAI_API_KEY'],  
  base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

# add your completion code
persona = input("Tell me the historical character I want to be: ")
question = input("Ask your question about the historical character: ")
prompt = f"""
You are going to play as a historical character {persona}. 

Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond the accurate answer only. Don't create content yourself. If you don't know something, tell that you don't remember.

Provide answer for the question: {question}
"""
# make a request using the Responses API
response = client.responses.create(model=deployment, input=prompt, store=False)

# print response
print(response.output_text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.