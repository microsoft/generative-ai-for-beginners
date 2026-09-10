# Building Wit de Meta Family Models 

## Introduction 

Dis lesson go cover: 

- Exploring di two main Meta family models - Llama 3.1 an Llama 3.2 
- Understanding di use-cases an scenarios for each model 
- Code sample to show di unique features of each model 


## The Meta Family of Models 

For dis lesson, we go explore 2 models from di Meta family or "Llama Herd" - Llama 3.1 an Llama 3.2.

Dem models dey come for different variants an dem dey available for di [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Note:** GitHub Models dey retire by end July 2026. Here na more details on how to use [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) to prototype wit AI models.

Model Variants: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Note: Llama 3 still dey for Microsoft Foundry Models but dis lesson no go cover am*

## Llama 3.1 

For 405 Billion Parameters, Llama 3.1 dey fit inside di open source LLM category. 

Di model na upgrade from di earlier release Llama 3 by offering: 

- Bigger context window - 128k tokens vs 8k tokens 
- Bigger Max Output Tokens - 4096 vs 2048 
- Better Multilingual Support - cause e get more training tokens 

Dis ones help Llama 3.1 handle more complex use cases when you dey build GenAI apps including: 
- Native Function Calling - ability to call external tools an functions wey no be part of di LLM workflow
- Better RAG Performance - cause e get higher context window 
- Synthetic Data Generation - ability to create better data for things like fine-tuning 

### Native Function Calling 

Llama 3.1 don dey fine-tuned well to make function or tool calls better. E get two tools wey di model fit sabi say e go use based on di user prompt. Dem tools be: 

- **Brave Search** - Fit use am get up-to-date info like weather by doing web search 
- **Wolfram Alpha** - Fit use am for more complex maths calculations so you no need write your own functions. 

You fit still create your own custom tools wey di LLM fit call. 

For di code example below: 

- We define di tools wey dey available (brave_search, wolfram_alpha) inside di system prompt. 
- Send user prompt wey dey ask about weather for one city. 
- Di LLM go respond wit tool call to Brave Search tool wey go look like dis `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Note: Dis example na to make di tool call only, if you want get results, you go need create free account for Brave API page an define di function itself.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Comot dem from your Microsoft Foundry project "Overview" page
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

Even though na LLM, one wahala for Llama 3.1 na say e no fit do multimodality. Meaning say e no fit use different kinds input like images as prompts an give answer. Dis ability na one of di main features for Llama 3.2. Di features dem also include: 

- Multimodality - fit look text an image prompts well 
- Small to Medium size variations (11B an 90B) - dis one dey give flexible deployment options, 
- Text-only variations (1B an 3B) - dis one make di model fit to deploy for edge / mobile devices an e get low latency 

Di multimodal support na big step for di open source models world. Di code example below dey take both image an text prompt to get analysis of di image from Llama 3.2 90B. 


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

# Collect dis from your Microsoft Foundry project "Overview" page side
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

After you don finish dis lesson, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more for Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->