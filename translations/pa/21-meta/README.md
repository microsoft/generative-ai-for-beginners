# ਮੈਟਾ ਪਰਿਵਾਰ ਮਾਡਲਾਂ ਨਾਲ ਬਣਾਉਣਾ

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਸਮੇਤ ਕੀਤਾ ਜਾਵੇਗਾ:

- ਦੋ ਮੁੱਖ ਮੈਟਾ ਪਰਿਵਾਰ ਮਾਡਲਾਂ ਦੀ ਜਾਂਚ - ਲਾਮਾ 3.1 ਅਤੇ ਲਾਮਾ 3.2
- ਹਰ ਮਾਡਲ ਲਈ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਤੇ ਪੱਧਰ ਸਮਝਣਾ
- ਹਰ ਮਾਡਲ ਦੀ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਰਸਾਉਣ ਲਈ ਕੋਡ ਉਦਾਹਰਨ


## ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਮੈਟਾ ਪਰਿਵਾਰ ਜਾਂ "ਲਾਮਾ ਹੇਰਡ" ਤੋਂ 2 ਮਾਡਲਾਂ ਲਾਮਾ 3.1 ਅਤੇ ਲਾਮਾ 3.2 ਦੀ ਜਾਂਚ ਕਰਾਂਗੇ।

ਇਹ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਵੈਰੀਅਂਟਾਂ ਵਿੱਚ ਉਪਲਬਧ ਹਨ ਅਤੇ [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲਦੇ ਹਨ।

> **ਨੋਟ:** GitHub ਮਾਡਲਜ਼ ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਵਿੱਚ ਬੰਦ ਹੋ ਰਹੇ ਹਨ। ਇੱਥੇ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ਦੀ ਵਰਤੋਂ ਕਰਕੇ AI ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਕਰਨ ਦੇ ਹੋਰ ਵੇਰਵੇ ਦਿੱਤੇ ਗਏ ਹਨ।

ਮਾਡਲ ਵੈਰੀਅਂਟ:
- ਲਾਮਾ 3.1 - 70B ਇੰਸਟਰਕਟ
- ਲਾਮਾ 3.1 - 405B ਇੰਸਟਰਕਟ
- ਲਾਮਾ 3.2 - 11B ਵਿਜ਼ਨ ਇੰਸਟਰਕਟ
- ਲਾਮਾ 3.2 - 90B ਵਿਜ਼ਨ ਇੰਸਟਰਕਟ

*ਨੋਟ: ਲਾਮਾ 3 ਵੀ Microsoft Foundry Models ਵਿੱਚ ਉਪਲਬਧ ਹੈ ਪਰ ਇਸ ਪਾਠ ਵਿੱਚ ਨਹੀਂ ਵੇਖਿਆ ਜਾਵੇਗਾ*

## ਲਾਮਾ 3.1

405 ਬਿਲੀਅਨ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ, ਲਾਮਾ 3.1 ਓਪਨ ਸੋਰਸ LLM ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦਾ ਹੈ।

ਮਾਡਲ ਪਹਿਲਾਂ ਦੇ ਰਿਲੀਜ਼ ਲਾਮਾ 3 ਦਾ ਅੱਪਗ੍ਰੇਡ ਹੈ ਜੋ ਇਹ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ:

- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਟੋਕਨ ਤੁਲਨਾ 8k ਟੋਕਨਾਂ ਦੇ ਨਾਲ
- ਵੱਡੇ ਜ਼ਿਆਦਾ ਆਉਟਪੁੱਟ ਟੋਕਨ - 4096 ਦਾ 2048 ਦੇ ਨਾਲ
- ਬਿਹਤਰ ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ - ਪ੍ਰਸ਼ਿਸ਼ਣ ਟੋਕਨਾਂ ਵਿੱਚ ਵਾਧੇ ਕਰਕੇ

ਇਹ ਲਾਮਾ 3.1 ਨੂੰ ਜੇਨ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਜਟਿਲ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਨੂੰ ਸੰਭਾਲਣ ਦੇ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ ਜਿਵੇਂ:
- ਮੁਲ ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ - ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਜੋ LLM ਵਰਕਫਲੋ ਤੋਂ ਬਾਹਰ ਹਨ
- ਬਿਹਤਰ RAG ਪ੍ਰਦਰਸ਼ਨ - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਕਾਰਨ
- ਕ੍ਰਿਤ੍ਰਿਮ ਡਾਟਾ ਬਨਾਨਾ - ਕੰਮਾਂ ਲਈ ਪ੍ਰਭਾਵਸ਼ाली ਡਾਟਾ ਬਣਾਉਣ ਦੀ ਯੋਗਤਾ ਜਿਸਦਾ ਉਦੇਸ਼ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਹੈ

### ਮੁਲ ਨੈਟਿਵ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ

ਲਾਮਾ 3.1 ਨੂੰ ਫੰਕਸ਼ਨ ਜਾਂ ਟੂਲ ਕਾਲਾਂ ਵਿੱਚ ਜ਼ਿਆਦਾ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣਾਉਣ ਲਈ ਬਹੁਤ ਸੁਧਾਰਿਆ ਗਿਆ ਹੈ। ਇਸਮੇਂ ਦੋ ਇੰਬਿਲਟ ਟੂਲ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਮਾਡਲ ਉਪਭੋਗਤਾ ਦੇ ਪ੍ਰੌੰਪਟ ਦੇ ਅਧਾਰ 'ਤੇ ਵਰਤੋਂ ਲਈ ਲੋੜੀਂਦਾ ਸਮਝ ਸਕਦਾ ਹੈ। ਇਹ ਟੂਲ ਹਨ:

- **ਬਰੇਵ ਸਰਚ** - ਵੈੱਬ ਸਰਚ ਕਰਕੇ ਤਾਜ਼ਾ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤੋਂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਮੌਸਮ
- **ਵੋਲਫਰਾਮ ਅਲਫਾ** - ਵੱਧ ਜਟਿਲ ਗਣਿਤੀ ਗਣਨਾਵਾਂ ਲਈ ਵਰਤੋਂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਤਾਂ ਕਿ ਆਪਣੇ ਫੰਕਸ਼ਨ ਲਿਖਣ ਦੀ ਲੋੜ ਨਾ ਰਹੇ।

ਤੁਸੀਂ ਆਪਣੀਆਂ ਕਸਟਮ ਟੂਲਾਂ ਵੀ ਬਣਾ ਸਕਦੇ ਹੋ ਜੋ LLM ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ:

- ਸਿਸਟਮ ਪ੍ਰੌੰਪਟ ਵਿੱਚ ਉਪਲਬਧ ਟੂਲਾਂ (brave_search, wolfram_alpha) ਦੀ ਪਰਿਭਾਸ਼ਾ ਕੀਤੀ ਗਈ ਹੈ।
- ਐਸਾ ਉਪਭੋਗਤਾ ਪ੍ਰੌੰਪਟ ਭੇਜੋ ਜੋ ਕਿਸੇ ਸ਼ਹਿਰ ਵਿੱਚ ਮੌਸਮ ਬਾਰੇ ਪੁੱਛਦਾ ਹੈ।
- LLM ਬਰੇਵ ਸਰਚ ਟੂਲ ਨੂੰ ਕਾਲ ਨਾਲ ਜਵਾਬ ਦੇਵੇਗਾ ਜੋ ਐਸਾ ਲੱਗੇਗਾ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ਨੋਟ: ਇਹ ਉਦਾਹਰਨ ਸਿਰਫ ਟੂਲ ਕਾਲ ਕਰਦੀ ਹੈ, ਜੇ ਤੁਸੀਂ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ ਬਰੇਵ API ਪੰਨੇ 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉਣਾ ਪਵੇਗਾ ਅਤੇ ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਪਵੇਗਾ।*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਦੇ "ਸਮਰੀ" ਪੰਨੇ ਤੋਂ ਲਵੋ
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

ਇੱਕ LLM ਹੋਣ ਦੇ ਬਾਵਜੂਦ, ਲਾਮਾ 3.1 ਦੀ ਇੱਕ ਸੀਮਾ ਇਹ ਹੈ ਕਿ ਉਹ ਬਹੁ-ਮੋਡੀਅਲ ਨਾ ਹੋਣਾ। ਇਸ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਇਨਪੁੱਟ ਵਜੋਂ ਤਸਵੀਰਾਂ ਵਰਗੀ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਨਾ ਕਰਨਾ ਅਤੇ ਜਵਾਬ ਨਾ ਦੇਣਾ। ਇਹ ਯੋਗਤਾ ਲਾਮਾ 3.2 ਦੀ ਇੱਕ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ। ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ:

- ਬਹੁ-ਮੋਡੀਅਲਟੀ - ਟੈਕਸਟ ਅਤੇ ਇਮੇਜ਼ ਪ੍ਰੌੰਪਟਾਂ ਦੋਹਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਯੋਗਤਾ
- ਛੋਟੇ ਤੋਂ ਮਧਿਮ ਆਕਾਰ ਦੇ ਵੈਰੀਅਂਟ (11B ਅਤੇ 90B) - ਇਹ ਲਚਕੀਲੇ ਤਾਇਨਾਤੀ ਵਿਕਲਪ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ
- ਸਿਰਫ਼ ਟੈਕਸਟ ਵਾਲੇ ਵੈਰੀਅਂਟ (1B ਅਤੇ 3B) - ਇਸ ਮਾਡਲ ਨੂੰ ਐਜ/ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤਾਇਨਾਤ ਕਰਨਾ ਆਸਾਨ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਘੱਟ ਲੇਟੈਂਸੀ ਦਿੰਦਾ ਹੈ

ਬਹੁ-ਮੋਡੀਅਲ ਸਹਾਇਤਾ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਦੁਨੀਆ ਵਿੱਚ ਇੱਕ ਵੱਡਾ ਕੱਦ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ, ਦੋਹਾਂ ਇੱਕ ਤਸਵੀਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰੌੰਪਟ ਲੈ ਕੇ ਲਾਮਾ 3.2 90B ਤੋਂ ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਪ੍ਰਾਪਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।


### ਲਾਮਾ 3.2 ਨਾਲ ਬਹੁ-ਮੋਡੀਅਲ ਸਹਾਇਤਾ

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

# ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਦੇ "ਸਮਰੀ" ਪੰਨੇ ਤੋਂ ਲਵੋ
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## ਸਿੱਖਣਾ ਇੱਥੇ ਨਾ ਰੁਕੇ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡਾ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ ਜੇਨਰੇਟਿਵ ਏਆਈ ਜਾਣਕਾਰੀ ਨੂੰ ਹੋਰ ਉੱਪਰ ਲੈ ਜਾ ਸਕੋ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->