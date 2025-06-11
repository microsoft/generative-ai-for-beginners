# Set up the query for generating responses
from azure.identity import DefaultAzureCredential
from azure.identity import get_bearer_token_provider
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
openai_client = AzureOpenAI(
    api_version="2024-06-01",
    azure_endpoint="https://phi4-test-resource.cognitiveservices.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2025-01-01-preview",
    azure_ad_token_provider=token_provider
)

search_client = SearchClient(
    endpoint="https://hotels-sample-index.search.windows.net",
    index_name="hotels-sample-index",
    credential=AzureKeyCredential("M8wpWZga2bQglwkC4ygX2skVnStLkO4lsSHsf7EXAwAzSeBOdL6H")
)

# This prompt provides instructions to the model. 
# The prompt includes the query and the source, which are specified further down in the code.
GROUNDED_PROMPT="""
You are a friendly assistant that recommends hotels based on activities and amenities.
Answer the query using only the sources provided below in a friendly and concise bulleted manner.
Answer ONLY with the facts listed in the list of sources below.
If there isn't enough information below, say you don't know.
Do not generate answers that don't use the sources below.
Query: {query}
Sources:\n{sources}
"""

# The query is sent to the search engine, but it's also passed in the prompt
query="Can you recommend a few hotels near the ocean with beach access and good views"

# Retrieve the selected fields from the search index related to the question
search_results = search_client.search(
    search_text=query,
    top=5,
    select="Description,HotelName,Tags"
)
sources_formatted = "\n".join([f'{document["HotelName"]}:{document["Description"]}:{document["Tags"]}' for document in search_results])

response = openai_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
        }
    ],
    model="gpt-4.1"
)

print(response.choices[0].message.content)