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

prompt = input("Ask me a question. ")

response = client.chat.completions.create(
    model="gpt-4-32k", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
    ]
)

print(response.choices[0].message.content)