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

# add your completion code
prompt = "Complete the following: Once upon a time there was a"

# engine
engine = "davinci-001"

# deployment_id, azure specific
deployment_name = os.getenv("DEPLOYMENT_NAME")

completion = openai.Completion.create(engine=deployment_name, prompt=prompt, max_tokens=600)

# print response
print(completion.choices[0].text)


#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.

