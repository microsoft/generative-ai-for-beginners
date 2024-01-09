from openai import AzureOpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key=os.environ['AZURE_OPENAI_KEY'],  
  api_version = "2023-10-01-preview"
  )

deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']

# add your completion code
prompt = "Complete the following: Once upon a time there was a"

# make completion
completion = client.completions.create(model=deployment, prompt=prompt)

# print response
print(completion.choices[0].text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
