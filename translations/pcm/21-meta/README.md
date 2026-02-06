# How to Build Wit Meta Family Models

## Introduction

Dis lesson go cover:

- How to sabi di two main Meta family models - Llama 3.1 and Llama 3.2
- How to understand di use-cases and di kind work wey each model fit do
- Code sample wey go show di special features wey each model get

## Di Meta Family of Models

For dis lesson, we go look two models from di Meta family or "Llama Herd" - Llama 3.1 and Llama 3.2.

Dis models get different types and dem dey available for GitHub Model marketplace. You fit find more info about how to use GitHub Models to [prototype wit AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Model Variants:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Note: Llama 3 dey available for GitHub Models too but we no go talk about am for dis lesson.*

## Llama 3.1

Wit 405 Billion Parameters, Llama 3.1 dey inside di open source LLM category.

Dis model na upgrade to di earlier release Llama 3, e dey offer:

- Bigger context window - 128k tokens instead of 8k tokens
- Bigger Max Output Tokens - 4096 instead of 2048
- Better Multilingual Support - because e get more training tokens

Dis things make Llama 3.1 fit handle more complex work when you dey build GenAI applications like:
- Native Function Calling - di ability to call external tools and functions outside di LLM workflow
- Better RAG Performance - because e get higher context window
- Synthetic Data Generation - di ability to create better data for tasks like fine-tuning

### Native Function Calling

Llama 3.1 don dey fine-tuned to sabi well well how to make function or tool calls. E get two built-in tools wey di model fit recognize say e need to use based on wetin di user talk. Di tools na:

- **Brave Search** - Fit help you find up-to-date info like weather by doing web search
- **Wolfram Alpha** - Fit help you do complex mathematical calculations so you no need to write your own functions.

You fit also create your own custom tools wey di LLM fit call.

For di code example below:

- We go define di tools wey dey available (brave_search, wolfram_alpha) for di system prompt.
- Send user prompt wey dey ask about di weather for one city.
- Di LLM go reply wit tool call to di Brave Search tool wey go look like dis `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Note: Dis example na only di tool call e go make, if you wan get di results, you go need create free account for di Brave API page and define di function itself.*

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

Even though Llama 3.1 na LLM, one wahala wey e get na say e no sabi multimodality. Dat one mean say e no fit use different types of input like images as prompts and give response. Dis ability na one of di main features wey Llama 3.2 get. Di features include:

- Multimodality - e fit check both text and image prompts
- Small to Medium size variations (11B and 90B) - dis one dey give flexible deployment options
- Text-only variations (1B and 3B) - dis one dey make di model fit deploy for edge/mobile devices and e dey fast

Di multimodal support na big step for di world of open source models. Di code example below go use both image and text prompt to get analysis of di image from Llama 3.2 90B.

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

## Learning no dey end here, continue di Journey

After you don finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more about Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e good make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->