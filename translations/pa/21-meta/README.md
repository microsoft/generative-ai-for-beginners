<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:29:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "pa"
}
-->
# ਮੈਟਾ ਪਰਿਵਾਰ ਮਾਡਲ ਨਾਲ ਨਿਰਮਾਣ 

## ਪੜਚੋਲ 

ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰੇਜ ਕੀਤੀ ਜਾਵੇਗੀ: 

- ਦੋ ਮੁੱਖ ਮੈਟਾ ਪਰਿਵਾਰ ਮਾਡਲਾਂ - Llama 3.1 ਅਤੇ Llama 3.2 ਦੀ ਖੋਜ 
- ਹਰ ਮਾਡਲ ਲਈ ਵਰਤੋਂ-ਮਾਮਲੇ ਅਤੇ ਦ੍ਰਿਸ਼ਾਂ ਨੂੰ ਸਮਝਣਾ 
- ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਣ ਲਈ ਕੋਡ ਨਮੂਨਾ 

## ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲ 

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਮੈਟਾ ਪਰਿਵਾਰ ਜਾਂ "Llama Herd" ਦੇ 2 ਮਾਡਲਾਂ - Llama 3.1 ਅਤੇ Llama 3.2 ਦੀ ਖੋਜ ਕਰਾਂਗੇ 

ਇਹ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਰੂਪਾਂ ਵਿੱਚ ਆਉਂਦੇ ਹਨ ਅਤੇ GitHub ਮਾਡਲ ਮਾਰਕੀਟਪਲੇਸ 'ਤੇ ਉਪਲਬਧ ਹਨ। ਇੱਥੇ GitHub ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ [AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਹੈ।

ਮਾਡਲ ਵੈਰੀਐਂਟ: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*ਨੋਟ: Llama 3 ਵੀ GitHub ਮਾਡਲਾਂ 'ਤੇ ਉਪਲਬਧ ਹੈ ਪਰ ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰੇਜ ਨਹੀਂ ਕੀਤੀ ਜਾਵੇਗੀ*

## Llama 3.1 

405 ਬਿਲੀਅਨ ਪੈਰਾਮੀਟਰਾਂ 'ਤੇ, Llama 3.1 ਖੁੱਲ੍ਹੇ ਸਰੋਤ LLM ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦਾ ਹੈ। 

ਇਹ ਮਾਡਲ ਪਹਿਲੇ ਰਿਲੀਜ਼ Llama 3 ਦਾ ਨਵੀਨਤਮ ਰੂਪ ਹੈ ਜੋ ਪੇਸ਼ ਕਰਦਾ ਹੈ: 

- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਟੋਕਨ ਵਿਰੁੱਧ 8k ਟੋਕਨ 
- ਵੱਡੇ ਮੈਕਸ ਆਉਟਪੁੱਟ ਟੋਕਨ - 4096 ਵਿਰੁੱਧ 2048 
- ਬਿਹਤਰ ਬਹੁਭਾਸ਼ੀ ਸਮਰਥਨ - ਸਿਖਲਾਈ ਟੋਕਨ ਵਿੱਚ ਵਾਧੇ ਦੇ ਕਾਰਨ 

ਇਹ Llama 3.1 ਨੂੰ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਨਿਰਮਾਣ ਵਿੱਚ ਵੱਧ ਸੁਖਾਲੇ ਉਪਯੋਗਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: 
- ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ - LLM ਵਰਕਫਲੋ ਦੇ ਬਾਹਰ ਬਾਹਰੀ ਸੰਦ ਅਤੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਸਮਰਥਾ 
- ਬਿਹਤਰ RAG ਪ੍ਰਦਰਸ਼ਨ - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਦੇ ਕਾਰਨ 
- ਕ੍ਰਿਤ੍ਰਿਮ ਡਾਟਾ ਉਤਪਾਦਨ - ਸੁਧਾਰ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਡਾਟਾ ਬਣਾਉਣ ਦੀ ਸਮਰਥਾ 

### ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ 

Llama 3.1 ਨੂੰ ਫੰਕਸ਼ਨ ਜਾਂ ਸੰਦ ਕਾਲ ਕਰਨ ਵਿੱਚ ਵੱਧ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਇਸ ਵਿੱਚ ਦੋ ਅੰਦਰੂਨੀ ਸੰਦ ਹਨ ਜੋ ਮਾਡਲ ਯੂਜ਼ਰ ਦੇ ਪ੍ਰਾਂਪਟ ਦੇ ਅਧਾਰ 'ਤੇ ਵਰਤਣ ਦੀ ਲੋੜ ਦੇ ਤੌਰ 'ਤੇ ਪਛਾਣ ਸਕਦਾ ਹੈ। ਇਹ ਸੰਦ ਹਨ: 

- **Brave Search** - ਵੈੱਬ ਖੋਜ ਕਰਕੇ ਮੌਸਮ ਵਾਂਗ ਨਵੀਨਤਮ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ 
- **Wolfram Alpha** - ਵੱਧ ਜਟਿਲ ਗਣਿਤੀ ਦੀਆਂ ਗਣਨਾਵਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਕਿ ਤੁਹਾਨੂੰ ਆਪਣੇ ਫੰਕਸ਼ਨ ਲਿਖਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ। 

ਤੁਸੀਂ ਆਪਣੇ ਆਪਣੇ ਕਸਟਮ ਸੰਦ ਵੀ ਬਣਾਉਣ ਦੀ ਸਮਰਥਾ ਰੱਖਦੇ ਹੋ ਜੋ LLM ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ। 

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ: 

- ਅਸੀਂ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਉਪਲਬਧ ਸੰਦਾਂ (brave_search, wolfram_alpha) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ। 
- ਉਪਭੋਗਤਾ ਪ੍ਰਾਂਪਟ ਭੇਜੋ ਜੋ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਸ਼ਹਿਰ ਵਿੱਚ ਮੌਸਮ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ। 
- LLM Brave Search ਸੰਦ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਪ੍ਰਤੀਕਿਰਿਆ ਦੇਵੇਗਾ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਲੱਗੇਗਾ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ਨੋਟ: ਇਹ ਉਦਾਹਰਨ ਸਿਰਫ ਸੰਦ ਕਾਲ ਕਰਦੀ ਹੈ, ਜੇ ਤੁਸੀਂ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ Brave API ਪੇਜ਼ 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੋਵੇਗੀ ਅਤੇ ਫੰਕਸ਼ਨ ਨੂੰ ਖੁਦ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ`

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2 

ਇੱਕ LLM ਹੋਣ ਦੇ ਬਾਵਜੂਦ, ਇੱਕ ਸੀਮਿਤੀ ਜੋ Llama 3.1 ਵਿੱਚ ਹੈ ਉਹ ਹੈ ਮਲਟੀਮੋਡੈਲਿਟੀ। ਇਸ ਦਾ ਮਤਲਬ ਹੈ, ਵੱਖ-ਵੱਖ ਕਿਸਮ ਦੇ ਇਨਪੁਟ ਜਿਵੇਂ ਕਿ ਚਿੱਤਰਾਂ ਨੂੰ ਪ੍ਰਾਂਪਟ ਦੇ ਤੌਰ 'ਤੇ ਵਰਤਣ ਅਤੇ ਜਵਾਬ ਪ੍ਰਦਾਨ ਕਰਨ ਦੀ ਸਮਰਥਾ। ਇਹ ਸਮਰਥਾ Llama 3.2 ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵੀ ਸ਼ਾਮਲ ਹਨ: 

- ਮਲਟੀਮੋਡੈਲਿਟੀ - ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਦੋਹਾਂ ਪ੍ਰਾਂਪਟਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਸਮਰਥਾ ਹੈ 
- ਛੋਟੇ ਤੋਂ ਦਰਮਿਆਨੇ ਆਕਾਰ ਦੇ ਰੂਪਾਂ (11B ਅਤੇ 90B) - ਇਹ ਲਚਕੀਲੇ ਤਹਿਣੀ ਵਿਕਲਪ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, 
- ਸਿਰਫ ਟੈਕਸਟ ਰੂਪਾਂ (1B ਅਤੇ 3B) - ਇਹ ਮਾਡਲ ਨੂੰ ਐਜ / ਮੋਬਾਈਲ ਜੰਤਰਾਂ 'ਤੇ ਤਹਿਣੀ ਕਰਨ ਦੀ ਸਮਰਥਾ ਦਿੰਦਾ ਹੈ ਅਤੇ ਘੱਟ ਵਿਲੰਬਤਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ 

ਮਲਟੀਮੋਡਲ ਸਮਰਥਨ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਦੁਨੀਆ ਵਿੱਚ ਇੱਕ ਵੱਡਾ ਕਦਮ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ ਇੱਕ ਚਿੱਤਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਦੋਹਾਂ ਲੈਂਦਾ ਹੈ ਤਾਂ ਕਿ Llama 3.2 90B ਤੋਂ ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ। 

### Llama 3.2 ਨਾਲ ਮਲਟੀਮੋਡਲ ਸਮਰਥਨ

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## ਸਿੱਖਿਆ ਇੱਥੇ ਨਹੀਂ ਰੁਕਦੀ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning ਸੰਗ੍ਰਹਿ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਜੋ ਆਪਣੀ Generative AI ਜਾਣਕਾਰੀ ਨੂੰ ਅੱਗੇ ਵਧਾਇਆ ਜਾ ਸਕੇ!

**ਅਸਵੀਕਾਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਸਚੇਤ ਰਹੋ ਕਿ ਸਵਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਗਲਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸਦੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਵਸਥਾਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।