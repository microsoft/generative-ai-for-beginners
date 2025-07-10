<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:08:46+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "pa"
}
-->
# ਮੈਟਾ ਫੈਮਿਲੀ ਮਾਡਲਾਂ ਨਾਲ ਬਣਾਉਣਾ

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਇਹ ਕਵਰ ਕੀਤਾ ਜਾਵੇਗਾ:

- ਦੋ ਮੁੱਖ ਮੈਟਾ ਫੈਮਿਲੀ ਮਾਡਲਾਂ ਦੀ ਖੋਜ - Llama 3.1 ਅਤੇ Llama 3.2  
- ਹਰ ਮਾਡਲ ਦੇ ਉਪਯੋਗ ਕੇਸ ਅਤੇ ਸਥਿਤੀਆਂ ਨੂੰ ਸਮਝਣਾ  
- ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਣ ਲਈ ਕੋਡ ਉਦਾਹਰਨ  

## ਮੈਟਾ ਫੈਮਿਲੀ ਦੇ ਮਾਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਮੈਟਾ ਫੈਮਿਲੀ ਜਾਂ "Llama Herd" ਦੇ 2 ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਕਰਾਂਗੇ - Llama 3.1 ਅਤੇ Llama 3.2

ਇਹ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਵਰਜਨਾਂ ਵਿੱਚ ਆਉਂਦੇ ਹਨ ਅਤੇ GitHub ਮਾਡਲ ਮਾਰਕੀਟਪਲੇਸ 'ਤੇ ਉਪਲਬਧ ਹਨ। GitHub ਮਾਡਲਾਂ ਨਾਲ [AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਇੱਥੇ ਵੇਰਵਾ ਦਿੱਤਾ ਗਿਆ ਹੈ।

ਮਾਡਲ ਵਰਜਨ:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*ਨੋਟ: Llama 3 ਵੀ GitHub ਮਾਡਲਾਂ 'ਤੇ ਉਪਲਬਧ ਹੈ ਪਰ ਇਸ ਪਾਠ ਵਿੱਚ ਇਸ ਬਾਰੇ ਨਹੀਂ ਚਰਚਾ ਕੀਤੀ ਜਾਵੇਗੀ*

## Llama 3.1

405 ਬਿਲੀਅਨ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ, Llama 3.1 ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਵਾਲੇ LLM ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦਾ ਹੈ।

ਇਹ ਮਾਡਲ ਪਹਿਲਾਂ ਆਏ Llama 3 ਦੇ ਅਪਗ੍ਰੇਡ ਵਜੋਂ ਹੈ ਜੋ ਇਹ ਸਹੂਲਤਾਂ ਦਿੰਦਾ ਹੈ:

- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਟੋਕਨ ਬਨਾਮ 8k ਟੋਕਨ  
- ਵੱਧ ਤੋਂ ਵੱਧ ਆਉਟਪੁੱਟ ਟੋਕਨ - 4096 ਬਨਾਮ 2048  
- ਬਿਹਤਰ ਬਹੁਭਾਸ਼ੀ ਸਹਿਯੋਗ - ਟ੍ਰੇਨਿੰਗ ਟੋਕਨਾਂ ਦੀ ਵਾਧੇ ਕਾਰਨ  

ਇਹ Llama 3.1 ਨੂੰ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਵੱਧ ਜਟਿਲ ਉਪਯੋਗ ਕੇਸਾਂ ਨੂੰ ਸੰਭਾਲਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ:  
- ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ - LLM ਵਰਕਫਲੋ ਤੋਂ ਬਾਹਰ ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਸਮਰੱਥਾ  
- ਬਿਹਤਰ RAG ਪ੍ਰਦਰਸ਼ਨ - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਕਾਰਨ  
- ਸਿੰਥੇਟਿਕ ਡੇਟਾ ਜਨਰੇਸ਼ਨ - ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਰਗੇ ਕੰਮਾਂ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਡੇਟਾ ਬਣਾਉਣ ਦੀ ਸਮਰੱਥਾ  

### ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ

Llama 3.1 ਨੂੰ ਫੰਕਸ਼ਨ ਜਾਂ ਟੂਲ ਕਾਲਾਂ ਕਰਨ ਵਿੱਚ ਹੋਰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣਾਉਣ ਲਈ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਸ ਵਿੱਚ ਦੋ ਇੰਬਿਲਟ ਟੂਲ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਮਾਡਲ ਯੂਜ਼ਰ ਦੇ ਪ੍ਰਾਂਪਟ ਦੇ ਆਧਾਰ 'ਤੇ ਵਰਤਣ ਦੀ ਲੋੜ ਸਮਝ ਸਕਦਾ ਹੈ। ਇਹ ਟੂਲ ਹਨ:

- **Brave Search** - ਵੈੱਬ ਖੋਜ ਕਰਕੇ ਮੌਸਮ ਵਰਗੀਆਂ ਤਾਜ਼ਾ ਜਾਣਕਾਰੀਆਂ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ  
- **Wolfram Alpha** - ਵੱਧ ਜਟਿਲ ਗਣਿਤੀ ਗਣਨਾਵਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਇਸ ਨਾਲ ਆਪਣੀਆਂ ਫੰਕਸ਼ਨਾਂ ਲਿਖਣ ਦੀ ਲੋੜ ਨਹੀਂ ਰਹਿੰਦੀ  

ਤੁਸੀਂ ਆਪਣੇ ਕਸਟਮ ਟੂਲ ਵੀ ਬਣਾ ਸਕਦੇ ਹੋ ਜਿਨ੍ਹਾਂ ਨੂੰ LLM ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ:

- ਅਸੀਂ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਉਪਲਬਧ ਟੂਲ (brave_search, wolfram_alpha) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ।  
- ਇੱਕ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਭੇਜਦੇ ਹਾਂ ਜੋ ਕਿਸੇ ਸ਼ਹਿਰ ਦੇ ਮੌਸਮ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ।  
- LLM Brave Search ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੇਗਾ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦੇਵੇਗਾ `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*ਨੋਟ: ਇਹ ਉਦਾਹਰਨ ਸਿਰਫ ਟੂਲ ਕਾਲ ਕਰਦੀ ਹੈ, ਜੇ ਤੁਸੀਂ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ Brave API ਪੇਜ 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉਣਾ ਪਵੇਗਾ ਅਤੇ ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਪਵੇਗਾ*  

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

ਇੱਕ LLM ਹੋਣ ਦੇ ਬਾਵਜੂਦ, Llama 3.1 ਦੀ ਇੱਕ ਸੀਮਾ ਮਲਟੀਮੋਡੈਲਿਟੀ ਹੈ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਇਹ ਵੱਖ-ਵੱਖ ਕਿਸਮ ਦੇ ਇਨਪੁਟ ਜਿਵੇਂ ਕਿ ਚਿੱਤਰਾਂ ਨੂੰ ਪ੍ਰਾਂਪਟ ਵਜੋਂ ਵਰਤ ਸਕਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਦੇ ਸਕਦਾ ਹੈ। ਇਹ ਸਮਰੱਥਾ Llama 3.2 ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- ਮਲਟੀਮੋਡੈਲਿਟੀ - ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਦੋਹਾਂ ਪ੍ਰਾਂਪਟਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਸਮਰੱਥਾ  
- ਛੋਟੇ ਤੋਂ ਦਰਮਿਆਨੇ ਆਕਾਰ ਦੇ ਵਰਜਨ (11B ਅਤੇ 90B) - ਇਹ ਲਚਕੀਲੇ ਤੌਰ 'ਤੇ ਡਿਪਲੋਇਮੈਂਟ ਦੇ ਵਿਕਲਪ ਦਿੰਦੇ ਹਨ  
- ਸਿਰਫ ਟੈਕਸਟ ਵਾਲੇ ਵਰਜਨ (1B ਅਤੇ 3B) - ਇਹ ਮਾਡਲ ਨੂੰ ਐਜ/ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਡਿਪਲੋਇ ਕਰਨ ਅਤੇ ਘੱਟ ਲੇਟੈਂਸੀ ਪ੍ਰਦਾਨ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ  

ਮਲਟੀਮੋਡਲ ਸਹਿਯੋਗ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਦੁਨੀਆ ਵਿੱਚ ਇੱਕ ਵੱਡਾ ਕਦਮ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ ਇੱਕ ਚਿੱਤਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਦੋਹਾਂ ਲਏ ਗਏ ਹਨ ਤਾਂ ਜੋ Llama 3.2 90B ਤੋਂ ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾ ਸਕੇ।  

### Llama 3.2 ਨਾਲ ਮਲਟੀਮੋਡਲ ਸਹਿਯੋਗ

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

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ Generative AI ਦੀ ਜਾਣਕਾਰੀ ਨੂੰ ਹੋਰ ਉੱਚੇ ਪੱਧਰ 'ਤੇ ਲੈ ਜਾ ਸਕੋ!

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।