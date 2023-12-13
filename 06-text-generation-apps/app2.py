import openai

openai.api_key = "3288625084374a1596d85d0a0739822e"

openai.api_type = 'azure' 
openai.api_version = '2023-05-15'
openai.api_base = "https://oaijh.openai.azure.com/"
deployment_name = "code-davinci-002"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"

# make completion
completion = openai.Completion.create(engine= deployment_name, model="davinci-002", prompt=prompt)

# print response
print(completion.choices[0].text)