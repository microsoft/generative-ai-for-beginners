# ਮੈਟਾ ਪਰਿਵਾਰ ਮਾਡਲਾਂ ਨਾਲ ਬਣਾਉਣਾ

## ਪਰਿਚਯ

ਇਹ ਪਾਠ ਕਵਰ ਕਰੇਗਾ:

- ਦੋ ਮੁੱਖ ਮੈਟਾ ਪਰਿਵਾਰ ਮਾਡਲਾਂ ਨੂੰ ਖੋਜਣਾ - ਲਾਮਾ 3.1 ਅਤੇ ਲਾਮਾ 3.2
- ਹਰ ਮਾਡਲ ਦੇ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਤੇ ਦ੍ਰਿਸ਼ ਲਈ ਸਮਝਣਾ
- ਕੋਡ ਉਦਾਹਰਣ ਜੋ ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਖੂਬੀਆਂ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ

## ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਮੈਟਾ ਪਰਿਵਾਰ ਜਾਂ "ਲਾਮਾ ਹੇਰਡ" ਤੋਂ 2 ਮਾਡਲਾਂ ਦੀ ਜਾਣਚ ਕਰਾਂਗੇ - ਲਾਮਾ 3.1 ਅਤੇ ਲਾਮਾ 3.2।

ਇਹ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਵੈਰੀਐਂਟਾਂ ਵਿੱਚ ਆਉਂਦੇ ਹਨ ਅਤੇ GitHub ਮਾਡਲ ਮਾਰਕੀਟਪਲੇਸ 'ਤੇ ਉਪਲਬਧ ਹਨ। ਹੇਠਾਂ GitHub ਮਾਡਲਾਂ ਦਾ ਵਰਤੋਂ ਕਰਕੇ [AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) ਬਾਰੇ ਵਧੇਰੇ ਵੇਰਵਾ ਦਿੱਤਾ ਗਿਆ ਹੈ।

ਮਾਡਲ ਵੈਰੀਐਂਟ:
- ਲਾਮਾ 3.1 - 70B ਇੰਸਟ੍ਰਕਟ
- ਲਾਮਾ 3.1 - 405B ਇੰਸਟ੍ਰਕਟ
- ਲਾਮਾ 3.2 - 11B ਵਿਜ਼ਨ ਇੰਸਟ੍ਰਕਟ
- ਲਾਮਾ 3.2 - 90B ਵਿਜ਼ਨ ਇੰਸਟ੍ਰਕਟ

*ਟਿੱਪਣੀ: ਲਾਮਾ 3 ਵੀ GitHub ਮਾਡਲਾਂ 'ਤੇ ਉਪਲਬਧ ਹੈ ਪਰ ਇਸ ਪਾਠ ਵਿੱਚ ਇਸ ਨੂੰ ਕਵਰ ਨਹੀਂ ਕੀਤਾ ਜਾਵੇਗਾ*

## ਲਾਮਾ 3.1

405 ਅਰਬ ਪੈਰामीਟਰਾਂ ਨਾਲ, ਲਾਮਾ 3.1 ਖੁਲ੍ਹੇ ਸਰੋਤ ਵਾਲੇ LLM ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਫਿੱਟ ਹੁੰਦਾ ਹੈ।

ਇਹ ਮਾਡਲ ਪਹਿਲਾਂ ਜਾਰੀ ਲਾਮਾ 3 ਨਾਲੋਂ ਅੱਪਗਰੇਡ ਹੈ ਜਿਸ ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ:

- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਟੋਕਨ ਮੁਕਾਬਲੇ 8k ਟੋਕਨ
- ਵੱਡਾ ਅਧਿਕਤਮ ਨਿਕਾਸ ਟੋਕਨ - 4096 ਮੁਕਾਬਲੇ 2048
- ਵਧੀਆ ਬਹੁਭਾਸ਼ੀ ਸਹਾਇਤਾ - ਸਿਖਲਾਈ ਟੋਕਨਾਂ ਵਿੱਚ ਵਾਧੇ ਕਾਰਨ

ਇਹ ਲਾਮਾ 3.1 ਨੂੰ ਵਧੇਰੇ ਜਟਿਲ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਨੂੰ ਸੰਭਾਲਣ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ ਜਦੋਂ ਜੋੜੀ ਜਾਂਦੀ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ:
- ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ - LLM ਵਰਕਫਲੋ ਤੋਂ ਬਾਹਰ ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਸਮਰੱਥਾ
- ਵਧੀਆ RAG ਪ੍ਰਦਰਸ਼ਨ - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਦੇ ਕਾਰਨ
- ਕ੍ਰਿਤ੍ਰਿਮ ਡਾਟਾ ਸਿਰਜਣਾ - ਜਿਵੇਂ ਕਿ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਡਾਟਾ ਬਣਾਉਣ ਦੀ ਯੋਗਤਾ

### ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ

ਲਾਮਾ 3.1 ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਇਹ ਫੰਕਸ਼ਨ ਜਾਂ ਟੂਲ ਕਾਲਾਂ ਕਰਨ ਵਿੱਚ ਵਧੇਰੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੈ। ਇਸ ਵਿੱਚ ਦੋ ਬਣੇ-ਬਣਾਏ ਟੂਲ ਵੀ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਮਾਡਲ ਯੂਜ਼ਰ ਵੱਲੋਂ ਦਿੱਤੇ ਪ੍ਰਾਂਪਟ ਦੇ ਆਧਾਰ 'ਤੇ ਵਰਤਣ ਦੀ ਲੋੜ ਹੋਣ 'ਤੇ ਪਛਾਣ ਸਕਦਾ ਹੈ। ਇਹ ਟੂਲ ਹਨ:

- **Brave Search** - ਵੈੱਬ ਖੋਜ ਕਰਕੇ ਤਾਜ਼ਾ ਜਾਣਕਾਰੀ ਜਿਵੇਂ ਮੌਸਮ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ
- **Wolfram Alpha** - ਅਸاني ਨਾਲ ਜਟਿਲ ਗਣਿਤਿਕ ਹਿਸ਼ਾਬ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਜੋ ਆਪਣੇ ਫੰਕਸ਼ਨ ਲਿਖਣ ਦੀ ਲੋੜ ਨਾ ਹੋਵੇ।

ਤੁਸੀਂ ਆਪਣੇ ਆਪਣੇ ਕਸਟਮ ਟੂਲ ਵੀ ਬਣਾਉਂ ਸਕਦੇ ਹੋ ਜਿਨ੍ਹਾਂ ਨੂੰ LLM ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ:

- ਅਸੀਂ ਸਿਸਟਮ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਉਪਲਬਧ ਟੂਲ (brave_search, wolfram_alpha) ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ।
- ਇੱਕ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਭੇਜਦੇ ਹਾਂ ਜੋ ਕਿਸੇ ਸ਼ਹਿਰ ਦਾ ਮੌਸਮ ਪੁੱਛਦਾ ਹੈ।
- LLM Brave Search ਟੂਲ ਲਈ ਟੂਲ ਕਾਲ ਨਾਲ ਜਵਾਬ ਦੇਵੇਗਾ ਜੋ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਸੇਗਾ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ਟਿੱਪਣੀ: ਇਹ ਉਦਾਹਰਣ ਸਿਰਫ ਟੂਲ ਕਾਲ ਕਰਦਾ ਹੈ, ਜੇ ਤੁਸੀਂ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ Brave API ਪੰਨੇ 'ਤੇ ਮੁਫਤ ਖਾਤਾ ਬਣਾਉਣਾ ਪਵੇਗਾ ਅਤੇ ਖੁਦ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਪਵੇਗਾ।*

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

## ਲਾਮਾ 3.2

ਇੱਕ LLM ਹੋਣ ਦੇ ਬਾਵਜੂਦ, ਲਾਮਾ 3.1 ਦੀ ਇੱਕ ਸੀਮਾ ਇਹ ਹੈ ਕਿ ਇਹ ਬਹੁ-ਮੋਡਾਲਿਟੀ ਨਹੀਂ ਸਮਰਥਤ ਕਰਦਾ। ਇਸਦਾ ਅਰਥ ਹੈ ਕਿ ਇਹ ਤਸਵੀਰਾਂ ਵਰਗੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਇਨਪੁੱਟ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਵਰਤਣ ਅਤੇ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਅਸਮਰੱਥ ਹੈ। ਇਹ ਸਮਰੱਥਾ ਲਾਮਾ 3.2 ਦੀਆਂ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹੋਰ ਹਨ:

- ਬਹੁ-ਮੋਡਾਲਿਟੀ - ਪਾਠ ਅਤੇ ਤਸਵੀਰ ਦੋਹਾਂ ਪ੍ਰਾਂਪਟਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਸਮਰੱਥਾ
- ਛੋਟਾ ਤੋਂ ਮਧਿਆਮ ਆਕਾਰ ਵੈਰੀਐਂਟ (11B ਅਤੇ 90B) - ਜੋ ਲਚਕੀਲੇ ਤਰੀਕੇ ਨਾਲ ਤਿਆਰ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ
- ਸਿਰਫ਼ ਮਾਦਰੀ ਪਾਠ ਵੈਰੀਐਂਟ (1B ਅਤੇ 3B) - ਜੋ ਮਾਡਲ ਨੂੰ ਏਜ / ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤਿਆਰ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੇ ਹਨ ਅਤੇ ਘੱਟ ਲੇਟੰਸੀ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ

ਬਹੁ-ਮੋਡਾਲ ਸਹਾਇਤਾ ਖੁਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਦੁਨੀਆ ਵਿੱਚ ਇੱਕ ਵੱਡਾ ਕਦਮ ਦਰਸਾਉਂਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ ਕੋਡ ਉਦਾਹਰਣ ਵਿੱਚ, ਇਕ ਤਸਵੀਰ ਅਤੇ ਪਾਠ ਪ੍ਰਾਂਪਟ ਦੋਹਾਂ ਲਈ ਲਾਮਾ 3.2 90B ਤੋਂ ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

### ਲਾਮਾ 3.2 ਨਾਲ ਬਹੁ-ਮੋਡਾਲ ਸਹਾਇਤਾ

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

## ਸਿਖਲਾਈ ਇੱਥੇ ਨਹੀਂ ਰੁਕਦੀ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [ਜਨਰੇਟਿਵ AI ਲਰਨਿੰਗ ਕਲੇਕਸ਼ਨ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਆਪਣੀ ਜਨਰੇਟਿਵ AI ਜਾਣਕਾਰੀ ਨੂੰ ਸਤਰ ਉਪਰ ਲਿਜਾਣ ਲਈ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਡੀਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਿੱਥੇ ਅਸੀਂ ਸਹੀਅਤ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਇਸ ਗੱਲ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਤੀਰਤਾ ਹੋ ਸਕਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਿਤ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਵਿਸ਼ੇਸ਼ਗੀ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->