# Building Wit de Meta Family Models 

## Introduction 

Dis lekshon go cover: 

- Exploring di two main Meta family models - Llama 3.1 and Llama 3.2 
- Understanding di use-cases and scenarios for each model 
- Code sample wey go show di unique features of each model 


## Di Meta Family of Models 

For dis lekshon, we go explore 2 models from Meta family or "Llama Herd" - Llama 3.1 and Llama 3.2.

Dis models get different variants and dem dey for [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Note:** GitHub Models dey retire for end of July 2026. Here get more info on how to use [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) take prototype wit AI models.

Model Variants: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Note: Llama 3 still dey available for Microsoft Foundry Models but we no go cover am for dis lekshon*

## Llama 3.1 

With 405 Billion Parameters, Llama 3.1 dey fit inside di open source LLM category. 

Di model be upgrade to di earlier release Llama 3 by coming with: 

- Bigger context window - 128k tokens compare to 8k tokens 
- Bigger Max Output Tokens - 4096 compare to 2048 
- Better Multilingual Support - because of increased training tokens 

Dis ones make Llama 3.1 fit handle more complex use cases when you dey build GenAI applications like: 
- Native Function Calling - di power to call external tools and functions outside di LLM workflow
- Better RAG Performance - because di bigger context window 
- Synthetic Data Generation - di ability to create better data for tasks like fine-tuning 

### Native Function Calling 

Llama 3.1 don fine-tune am make e dey more effective to make function or tool calls. E get two built-in tools weh di model fit sabi say e need use based on di prompt wey user give. Dis tools na: 

- **Brave Search** - Fit use am find fresh information like weather by doing web search 
- **Wolfram Alpha** - Fit use am for complex mathematical calculations make you no need write your own functions. 

You fit still create your own custom tools wey di LLM fit call. 

For di code example below: 

- We define di available tools (brave_search, wolfram_alpha) for di system prompt. 
- Send user prompt wey ask about weather for one particular city. 
- Di LLM go respond wit tool call to Brave Search weh go be like this `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Note: Dis example dey only do di tool call, if you wan get di results, you go need create free account for Brave API page and define di function yourself.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Collect dem from your Microsoft Foundry project "Overview" page
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

## Llama 3.2 

Even though e be LLM, one limitation of Llama 3.1 na say e no get multimodality. That one mean say e no fit use different kinds of input like images as prompts and give response. Dis power na one of di main features of Llama 3.2. Dem features still get: 

- Multimodality - e fit evaluate both text and image prompts 
- Small to Medium size variations (11B and 90B) - dis one dey give flexible deployment options, 
- Text-only variations (1B and 3B) - dis one allow di model deploy for edge / mobile devices and e dey provide low latency 

Di multimodal support na big step for open source models world. Di code example below dey take both image and text prompt to get analysis of di image from Llama 3.2 90B. 


### Multimodal Support wit Llama 3.2

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

# Comot dem from your Microsoft Foundry project "Overview" page
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

## Learning no stop here, continue di journey

After you don finish dis lekshon, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to level up your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->