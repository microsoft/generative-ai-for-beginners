# pylint: disable=all
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
prompt = "Complete the following: Once upon a time there was a"
# make a request using the Responses API
response = client.responses.create(model=deployment, input=prompt, store=False)

# print response
print(response.output_text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.