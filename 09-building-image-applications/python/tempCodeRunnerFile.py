client = AzureOpenAI(
  api_key=os.environ['AZURE_OPENAI_API_DALLE_KEY'],  # this is also the default, it can be omitted
  api_version = os.environ['AZURE_OPENAI_API_DALLE_VERSION'],  # e.g. "2023-06-01-preview"
  azure_endpoint=os.environ['AZURE_OPENAI_DALLE_ENDPOINT'] 
  )