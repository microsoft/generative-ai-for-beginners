# ਮੈਟਾ ਪਰਿਵਾਰ ਕੁੱਲ ਮਾਡਲਾਂ ਨਾਲ ਬਣਾਉਣਾ

## ਪਰਿਚਯ

ਇਹ ਪਾਠ ਕਵਰ ਕਰੇਗਾ:

- ਦੋ ਮੁੱਖ ਮੈਟਾ ਪਰਿਵਾਰ ਕੁੱਲ ਮਾਡਲਾਂ ਦੀ ਖੋਜ - ਲੰਮਾ 3.1 ਅਤੇ ਲੰਮਾ 3.2
- ਹਰ ਮਾਡਲ ਦੇ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਤੇ ਸੰਦਰਭਾਂ ਨੂੰ ਸਮਝਣਾ
- ਹਰ ਮਾਡਲ ਦੀਆਂ ਵਿਲੱਖਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਿਖਾਉਂਦਾ ਕੋਡ ਉਦਾਹਰਨ


## ਮੈਟਾ ਪਰਿਵਾਰ ਦੇ ਮਾਡਲ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਮੈਟਾ ਪਰਿਵਾਰ ਜਾਂ "ਲੰਮਾ ਹਰਡ" ਦੇ 2 ਮਾਡਲਾਂ ਦੀ ਪੜਚੋਲ ਕਰਾਂਗੇ - ਲੰਮਾ 3.1 ਅਤੇ ਲੰਮਾ 3.2।

ਇਹ ਮਾਡਲ ਵੱਖ-ਵੱਖ ਰੂਪਾਂ ਵਿੱਚ ਹੁੰਦੇ ਹਨ ਅਤੇ [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਉਪਲਬਧ ਹਨ।

> **ਨੋਟ:** GitHub Models ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਰਿਹਾ ਹੈ। ਇੱਥੇ ਹੋਰ ਵੇਰਵਿਆਂ ਲਈ ਦੇਖੋ ਕਿ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ਨਾਲ ਕਿਵੇਂ AI ਮਾਡਲਾਂ ਦੇ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

ਮਾਡਲ ਦੇ ਰੂਪ:
- ਲੰਮਾ 3.1 - 70B ਇੰਸਟ੍ਰਕਟ
- ਲੰਮਾ 3.1 - 405B ਇੰਸਟ੍ਰਕਟ
- ਲੰਮਾ 3.2 - 11B ਵਿਜ਼ਨ ਇੰਸਟ੍ਰਕਟ
- ਲੰਮਾ 3.2 - 90B ਵਿਜ਼ਨ ਇੰਸਟ੍ਰਕਟ

*ਨੋਟ: ਲੰਮਾ 3 ਮਾਈਕਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਮਾਡਲਾਂ ਵਿੱਚ ਵੀ ਉਪਲਬਧ ਹੈ ਪਰ ਇਸ ਪਾਠ ਵਿੱਚ ਕਵਰ ਨਹੀਂ ਕੀਤਾ ਜਾਵੇਗਾ*

## ਲੰਮਾ 3.1

405 ਬਿਲੀਅਨ ਪੈਰਾਮੀਟਰਾਂ ਦੇ ਨਾਲ, ਲੰਮਾ 3.1 ਖੁੱਲ੍ਹੇ ਸਰੋਤ LLM ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦਾ ਹੈ।

ਇਹ ਮਾਡਲ ਪਹਿਲਾਂ ਜਾਰੀ ਕੀਤੇ ਲੰਮਾ 3 ਵਿੱਚ ਸਰਾੰਮ ਤੋਂ ਅੱਪਗਰੇਡ ਹੈ:

- ਵੱਡਾ ਸੰਦਰਭ ਵਿੰਡੋ - 128k ਟੋਕਨ ਮੁਕਾਬਲੇ 8k ਟੋਕਨ
- ਵੱਡਾ ਅਧਿਕਤਮ ਆਉਟਪੁੱਟ ਟੋਕਨ - 4096 ਮੁਕਾਬਲੇ 2048
- ਵਧੀਆ ਬਹੁਭਾਸ਼ੀ ਸਮਰਥਨ - ਟ੍ਰੇਨਿੰਗ ਟੋਕਨਾਂ ਵਿੱਚ ਵਾਧੇ ਕਾਰਨ

ਇਹ ਲੰਮਾ 3.1 ਨੂੰ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣ ਵੇਲੇ ਹੋਰ ਜਟਿਲ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਨੂੰ ਸੰਭਾਲਣ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ, ਜਿਵੇਂ:
- ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ - ਬਾਹਰੀ ਟੂਲਾਂ ਅਤੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ LLM ਵਰਕਫਲੋ ਤੋਂ ਬਾਹਰ ਕਾਲ ਕਰਨ ਦੀ ਸਮਰਥਾ
- ਵਧੀਆ RAG ਪ੍ਰਦਰਸ਼ਨ - ਵੱਡੇ ਸੰਦਰਭ ਵਿੰਡੋ ਕਾਰਨ
- ਸਿੰਥੇਟਿਕ ਡਾਟਾ ਪੈਦਾਵਾਰ - ਜਿਵੇਂ ਸੁਧਾਰ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਡਾਟਾ ਬਣਾਉਣ ਦੀ ਸਮਰਥਾ

### ਮੂਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ

ਲੰਮਾ 3.1 ਨੂੰ ਫੰਕਸ਼ਨ ਜਾਂ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਬਿਹਤਰ ਤਰੀਕੇ ਨਾਲ ਕਰਨ ਲਈ ਸੁਧਾਰਿਆ ਗਿਆ ਹੈ। ਇਹਦੇ ਵਿੱਚ ਦੋ ਅੰਦਰੂਨੀ ਟੂਲ ਹਨ ਜੋ ਮਾਡਲ ਵਰਤੋਂਕਾਰ ਦੀ ਪ੍ਰੰਪਟ ਨੂੰ ਦੇਖ ਕੇ ਵਰਤੋਂ ਲਈ ਪਹਚਾਣ ਸਕਦਾ ਹੈ। ਇਹ ਟੂਲ ਹਨ:

- **Brave Search** - ਵੈੱਬ ਖੋਜ ਕਰਕੇ ਤਾਜ਼ਾ ਜਾਣਕਾਰੀ ਜਿਵੇਂ ਮੌਸਮ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ
- **Wolfram Alpha** - ਕੁਝ ਹੋਰ ਜਟਿਲ ਗਣਿਤੀ ਗਣਨਾਵਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਇਸ ਲਈ ਆਪਣੀਆਂ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਲਿਖਣ ਦੀ ਜ਼ਰੂਰਤ ਨਹੀਂ ਹੁੰਦੀ।

ਤੁਸੀਂ ਆਪਣੇ ਖ਼ਾਸ ਟੂਲ ਵੀ ਬਣਾ ਸਕਦੇ ਹੋ ਜੋ LLM ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਉਦਾਹਰਨ ਵਿੱਚ:

- ਅਸੀਂ ਪ੍ਰਣਾਲੀ ਪ੍ਰੰਪਟ ਵਿੱਚ ਉਪਲਬਧ ਟੂਲ (brave_search, wolfram_alpha) ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ।
- ਵਰਤੋਂਕਾਰ ਤੋਂ ਮੌਸਮ ਬਾਰੇ ਪ੍ਰੰਪਟ ਭੇਜਦੇ ਹਾਂ ਜੋ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਸ਼ਹਿਰ ਲਈ ਹੁੰਦੀ ਹੈ।
- LLM ਇੱਕ Brave Search ਟੂਲ ਨੂੰ ਕਾਲ ਨਾਲ ਜਵਾਬ ਦੇਵੇਗਾ ਜਿਸਦਾ ਰੂਪ ਇਹ ਹੋਵੇਗਾ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ਨੋਟ: ਇਹ ਉਦਾਹਰਨ ਸਿਰਫ ਟੂਲ ਕਾਲ ਕਰਦੀ ਹੈ, ਜੇਕਰ ਤੁਸੀਂ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ Brave API ਪੇਜ 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉਣਾ ਪਵੇਗਾ ਅਤੇ ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ ਪਵੇਗਾ।

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ਆਪਣੀ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਦੀ "ਓਵਰਵਿਊ" ਪੇਜ਼ ਤੋਂ ਇਹ ਪ੍ਰਾਪਤ ਕਰੋ
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

## ਲੰਮਾ 3.2

ਇੱਕ LLM ਹੋਣ ਦੇ ਬਾਵਜੂਦ, ਲੰਮਾ 3.1 ਦੀ ਇੱਕ ਸੀਮਾ ਹੈ ਇਸ ਦੀ ਬਹੁ-ਮੋਡਾਲਿਟੀ ਦੀ ਘਾਟ। ਜਿਸਦਾ ਅਰਥ ਹੈ ਕਿ ਇਹ ਭਿੰਨ ਪ੍ਰਕਾਰ ਦੇ ਇਨਪੁਟ ਜਿਵੇਂ ਚਿੱਤਰਾਂ ਨੂੰ ਪ੍ਰੰਪਟ ਵਜੋਂ ਵਰਤ ਕੇ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਅਸਮਰਥ ਹੈ। ਇਹ ਸਮਰਥਾ ਲੰਮਾ 3.2 ਦੀ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਇਹਨਾਂ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ:

- ਬਹੁ-ਮੋਡਾਲਿਟੀ - ਇਨਪੁਟ ਵਜੋਂ ਦੋਹਾਂ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਪ੍ਰੰਪਟਾਂ ਨੂੰ ਮੂਲਾਂਕਣ ਕਰਨ ਦੀ ਸਮਰਥਾ
- ਛੋਟੇ ਤੋ ਮੱਧਮਾਕਾਰ (11B ਅਤੇ 90B) ਵਿਰੀਅਸ਼ਨ - ਇਹ ਲਚਕੀਲੇ ਤਰੀਕੇ ਨਾਲ ਤਾਇਨਾਤ ਕਰਨ ਦੇ ਵਿਕਲਪ ਦਿੰਦਾ ਹੈ,
- ਸਿਰਫ ਟੈਕਸਟ (1B ਅਤੇ 3B) ਵਿਰੀਅਸ਼ਨ - ਇਹ ਮਾਡਲ ਨੂੰ ਐਜ ਜਾਂ ਮੋਬਾਈਲ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤਾਇਨਾਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਅਤੇ ਘੱਟ ਲੇਟੈਂਸੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ

ਬਹੁ-ਮੋਡਾਲ ਸਪੋਰਟ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਦੁਨੀਆ ਵਿੱਚ ਇੱਕ ਵੱਡਾ ਕਦਮ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਉਦਾਹਰਨ ਇੱਕ ਚਿੱਤਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰੰਪਟ ਦੋਹਾਂ ਮੰਗਦਾ ਹੈ ਤਾਂ ਜੋ ਲੰਮਾ 3.2 90B ਤੋਂ ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਲਿਆ ਜਾ ਸਕੇ।


### ਲੰਮਾ 3.2 ਨਾਲ ਬਹੁ-ਮੋਡਾਲ ਸਹਾਇਤਾ

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

# ਇਹਨਾਂ ਨੂੰ ਆਪਣੀ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਦੇ "ਸਾਰਾਂਸ਼" ਪੰਨੇ ਤੋਂ ਲਿਆਓ
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

## ਸਿੱਖਣਾ ਇਹਥੇ ਨਹੀਂ ਰੁਕਦਾ, ਯਾਤਰਾ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਦੇ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਆਪਣੀ ਜਨਰੇਟਿਵ AI ਗਿਆਨ ਵਿੱਚ ਵਾਧਾ ਕਰਦੇ ਰਹੋ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->