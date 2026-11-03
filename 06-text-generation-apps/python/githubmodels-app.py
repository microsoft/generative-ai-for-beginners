import os
from openai import OpenAI

# Get these from your Microsoft Foundry project's "Overview" page
# (GitHub Models is retiring end of July 2026 - see https://ai.azure.com/catalog/models)
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]

model_name = "gpt-5-mini"

# The OpenAI client points at the Microsoft Foundry OpenAI-compatible /openai/v1/ endpoint,
# which serves OpenAI models as well as models like Llama, Mistral, and Phi.
client = OpenAI(
    base_url=f"{endpoint.rstrip('/')}/openai/v1/",
    api_key=token,
)

prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"

# make a request using the Responses API
response = client.responses.create(
    input=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ],
    model=model_name,
    # Note: gpt-5 reasoning models don't accept temperature/top_p; leave them at their defaults.
    store=False,
)

print(response.output_text)
