<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:09:36+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "pa"
}
-->
# ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲਾਂ ਨਾਲ ਨਿਰਮਾਣ 

## ਪੇਸ਼ਕਸ਼ 

ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ: 

- ਦੋ ਮੁੱਖ ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲਾਂ - Llama 3.1 ਅਤੇ Llama 3.2 ਦੀ ਖੋਜ 
- ਹਰ ਮਾਡਲ ਲਈ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਤੇ ਦ੍ਰਿਸ਼ਾਂ ਨੂੰ ਸਮਝਣਾ 
- ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਣ ਲਈ ਕੋਡ ਨਮੂਨਾ 

## ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲ 

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਮੈਟਾ ਪਰਿਵਾਰ ਜਾਂ "Llama ਝੁੰਡ" ਦੇ 2 ਮਾਡਲਾਂ - Llama 3.1 ਅਤੇ Llama 3.2 ਦੀ ਖੋਜ ਕਰਾਂਗੇ 

ਇਹ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਰੂਪਾਂ ਵਿੱਚ ਆਉਂਦੇ ਹਨ ਅਤੇ GitHub ਮਾਡਲ ਮਾਰਕੀਟਪਲੇਸ 'ਤੇ ਉਪਲਬਧ ਹਨ। [AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਕਰਨ ਲਈ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) GitHub ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਬਾਰੇ ਹੋਰ ਵੇਰਵੇ ਇੱਥੇ ਹਨ।

ਮਾਡਲ ਵੈਰੀਐਂਟਸ: 
- Llama 3.1 - 70B ਇਨਸਟਰਕਟ 
- Llama 3.1 - 405B ਇਨਸਟਰਕਟ 
- Llama 3.2 - 11B ਵਿਜ਼ਨ ਇਨਸਟਰਕਟ 
- Llama 3.2 - 90B ਵਿਜ਼ਨ ਇਨਸਟਰਕਟ 

*ਨੋਟ: Llama 3 ਵੀ GitHub ਮਾਡਲਾਂ 'ਤੇ ਉਪਲਬਧ ਹੈ ਪਰ ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰ ਨਹੀਂ ਕੀਤਾ ਜਾਵੇਗਾ*

## Llama 3.1 

405 ਬਿਲੀਅਨ ਪੈਰਾਮੀਟਰਾਂ 'ਤੇ, Llama 3.1 ਖੁੱਲ੍ਹੇ ਸਰੋਤ LLM ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਫਿੱਟ ਹੁੰਦਾ ਹੈ। 

ਮੋਡ ਪਹਿਲੇ ਰਿਲੀਜ਼ Llama 3 ਵਿੱਚ ਅਪਗਰੇਡ ਹੈ ਜੋ ਇਹ ਪੇਸ਼ਕਸ਼ ਕਰਦਾ ਹੈ: 

- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਟੋਕਨ ਵਿ. 8k ਟੋਕਨ 
- ਵੱਡੇ ਮੈਕਸ ਆਉਟਪੁੱਟ ਟੋਕਨ - 4096 ਵਿ. 2048 
- ਬਿਹਤਰ ਬਹੁਭਾਸ਼ਾਈ ਸਹਾਇਤਾ - ਟ੍ਰੇਨਿੰਗ ਟੋਕਨ ਵਿੱਚ ਵਾਧੇ ਦੇ ਕਾਰਨ 

ਇਹ Llama 3.1 ਨੂੰ GenAI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਨਿਰਮਾਣ ਕਰਦੇ ਸਮੇਂ ਹੋਰ ਜਟਿਲ ਵਰਤੋਂ ਦੇ ਕੇਸ ਸੰਭਾਲਣ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ ਜਿਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ: 
- ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ - LLM ਵਰਕਫਲੋ ਦੇ ਬਾਹਰ ਬਾਹਰੀ ਟੂਲ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨ ਦੀ ਯੋਗਤਾ 
- ਬਿਹਤਰ RAG ਪ੍ਰਦਰਸ਼ਨ - ਉੱਚੇ ਸੰਦਰਭ ਵਿੰਡੋ ਦੇ ਕਾਰਨ 
- ਸੰਸਲੇਸ਼ਣ ਡਾਟਾ ਉਤਪਾਦਨ - ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਰਗੇ ਕੰਮਾਂ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਡਾਟਾ ਬਣਾਉਣ ਦੀ ਯੋਗਤਾ 

### ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ 

Llama 3.1 ਨੂੰ ਫੰਕਸ਼ਨ ਜਾਂ ਟੂਲ ਕਾਲਾਂ ਕਰਨ ਵਿੱਚ ਹੋਰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣਾਉਣ ਲਈ ਸੁਧਾਰਿਆ ਗਿਆ ਹੈ। ਇਸ ਵਿੱਚ ਦੋ ਅੰਦਰੂਨੀ ਟੂਲ ਵੀ ਹਨ ਜੋ ਮਾਡਲ ਉਪਭੋਗਤਾ ਦੀ ਪ੍ਰੰਪਟ ਦੇ ਆਧਾਰ 'ਤੇ ਵਰਤਣ ਦੀ ਲੋੜ ਹੋਣ ਦੇ ਨਾਤੇ ਪਛਾਣ ਸਕਦਾ ਹੈ। ਇਹ ਟੂਲ ਹਨ: 

- **ਬਰੇਵ ਸਰਚ** - ਵੈੱਬ ਖੋਜ ਕਰਕੇ ਮੌਸਮ ਵਰਗਾ ਤਾਜ਼ਾ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ 
- **ਵੋਲਫਰਾਮ ਅਲਫਾ** - ਹੋਰ ਜਟਿਲ ਗਣਿਤੀ ਗਣਨਾਵਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਜੋ ਆਪਣੇ ਫੰਕਸ਼ਨ ਲਿਖਣ ਦੀ ਲੋੜ ਨਾ ਹੋਵੇ। 

ਤੁਸੀਂ ਆਪਣੇ ਖੁਦ ਦੇ ਕਸਟਮ ਟੂਲ ਵੀ ਬਣਾਉਣ ਦੇ ਯੋਗ ਹੋ ਸਕਦੇ ਹੋ ਜੋ LLM ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ। 

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ: 

- ਅਸੀਂ ਸਿਸਟਮ ਪ੍ਰੰਪਟ ਵਿੱਚ ਉਪਲਬਧ ਟੂਲ (brave_search, wolfram_alpha) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ। 
- ਇੱਕ ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ ਭੇਜੋ ਜੋ ਕਿਸੇ ਨਿਰਧਾਰਤ ਸ਼ਹਿਰ ਦੇ ਮੌਸਮ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ। 
- LLM Brave Search ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਜਵਾਬ ਦੇਵੇਗਾ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖਾਈ ਦੇਵੇਗਾ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*ਨੋਟ: ਇਹ ਉਦਾਹਰਨ ਸਿਰਫ ਟੂਲ ਕਾਲ ਕਰਦਾ ਹੈ, ਜੇ ਤੁਸੀਂ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ Brave API ਪੇਜ 'ਤੇ ਇੱਕ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੋਵੇਗੀ ਅਤੇ ਫੰਕਸ਼ਨ ਨੂੰ ਖੁਦ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਹੋਵੇਗਾ` 

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

ਇੱਕ LLM ਹੋਣ ਦੇ ਬਾਵਜੂਦ, ਇੱਕ ਪਾਬੰਦੀ ਜੋ Llama 3.1 ਵਿੱਚ ਹੈ ਉਹ ਹੈ ਬਹੁ-ਮਾਡਲਤਾ। ਇਹ ਹੈ, ਤਸਵੀਰਾਂ ਵਰਗੇ ਵੱਖ-ਵੱਖ ਪ੍ਰਕਾਰ ਦੇ ਇਨਪੁੱਟ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣਾ ਅਤੇ ਜਵਾਬ ਪ੍ਰਦਾਨ ਕਰਨਾ। ਇਹ ਯੋਗਤਾ Llama 3.2 ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵੀ ਸ਼ਾਮਲ ਹਨ: 

- ਬਹੁ-ਮਾਡਲਤਾ - ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਦੋਹਾਂ ਪ੍ਰੰਪਟਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਯੋਗਤਾ ਹੈ 
- ਛੋਟੇ ਤੋਂ ਦਰਮਿਆਨੇ ਆਕਾਰ ਦੇ ਰੂਪਾਂ (11B ਅਤੇ 90B) - ਇਹ ਲਚਕੀਲੇ ਤਹਿਨਾਤੀ ਵਿਕਲਪ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ, 
- ਸਿਰਫ-ਟੈਕਸਟ ਰੂਪਾਂ (1B ਅਤੇ 3B) - ਇਹ ਮਾਡਲ ਨੂੰ ਐਜ / ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤਹਿਨਾਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਅਤੇ ਘੱਟ ਲੈਟੈਂਸੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ 

ਮਲਟੀਮੋਡਲ ਸਹਾਇਤਾ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਦੁਨੀਆ ਵਿੱਚ ਇੱਕ ਵੱਡਾ ਕਦਮ ਦਰਸਾਉਂਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ ਦੋਹਾਂ ਇੱਕ ਚਿੱਤਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਲੈਂਦੇ ਹਨ ਤਾਂ ਜੋ Llama 3.2 90B ਤੋਂ ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ। 

### Llama 3.2 ਨਾਲ ਬਹੁ-ਮਾਡਲ ਸਹਾਇਤਾ

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

## ਸਿੱਖਣਾ ਇੱਥੇ ਨਹੀਂ ਰੁਕਦਾ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਹ ਪਾਠ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [ਜਨਰੇਟਿਵ AI ਸਿੱਖਣ ਸੰਗ੍ਰਹਿ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਦੇਖੋ ਤਾਂ ਜੋ ਆਪਣੀ ਜਨਰੇਟਿਵ AI ਗਿਆਨ ਦੀ ਪੱਧਰੀ ਉਚਾਈ ਲਈ ਸਿਖਲਾਈ ਜਾਰੀ ਰੱਖੋ!

**ਦਸਤਾਵੇਜ਼**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।