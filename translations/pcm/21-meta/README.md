# Building Wit di Meta Family Models 

## Introduction 

Dis lesson go cover: 

- Explorin di two main Meta family models - Llama 3.1 an Llama 3.2 
- Understanding di use-cases an scenarios for each model 
- Code sample to show di unique features of each model 


## Di Meta Family of Models 

For dis lesson, we go explore 2 models from di Meta family or "Llama Herd" - Llama 3.1 an Llama 3.2.

Dem models dey come in different variants an dey available on top di GitHub Model marketplace. Here na more details on how to use GitHub Models to [prototype wit AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Model Variants: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Note: Llama 3 still dey available for GitHub Models but we no go cover am for dis lesson*

## Llama 3.1 

Wit 405 Billion Parameters, Llama 3.1 dey fit inside di open source LLM category. 

Di model na upgrade to di earlier release Llama 3 by offering: 

- Bigger context window - 128k tokens against 8k tokens 
- Bigger Max Output Tokens - 4096 against 2048 
- Better Multilingual Support - because di training tokens dem increase 

Dis ones make Llama 3.1 fit handle more complex use cases when you dey build GenAI applications like: 
- Native Function Calling - di ability to call external tools an functions outside di LLM workflow
- Better RAG Performance - because of di higher context window 
- Synthetic Data Generation - di ability to create better data for tasks like fine-tuning 

### Native Function Calling 

Llama 3.1 don dey fine-tuned to dey more effective when e come to making function or tool calls. E get two built-in tools wey di model fit sabi sey e need to use based on wetin di user talk. Dem tools be: 

- **Brave Search** - Fit use am to get up-to-date information like di weather by doing web search 
- **Wolfram Alpha** - Fit use am for complex maths calculations so you no need to write your own functions. 

You fit create your own custom tools wey di LLM fit call too. 

For di code example wey dey below: 

- We define di available tools (brave_search, wolfram_alpha) for di system prompt. 
- Send user prompt wey ask about di weather for one particular city. 
- Di LLM go respond with tool call to di Brave Search tool wey go look like dis `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Note: Dis example just dey make di tool call, if you want get di results, you go need create free account for di Brave API page an define di function itself.

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

Even though e be LLM, one limitation of Llama 3.1 na say e no fit do multimodality. Meaning e no fit use different types of input like images as prompts and gimme responses. Dis ability na one of di main features of Llama 3.2. Dem features include: 

- Multimodality - fit evaluate both text and image prompts 
- Small to Medium size variations (11B and 90B) - dis one give flexible deployment options, 
- Text-only variations (1B and 3B) - dis one make e possible to deploy di model for edge / mobile devices and e give low latency 

Di multimodal support na big step for di world of open source models. Di code example wey dey below go take both image and text prompt to get analysis of di image from Llama 3.2 90B. 


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

## Learning no stop for here, continue di journey

After you don finish dis lesson, make you check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to dey level up your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make e correct, abeg sabi say automated translation fit get error or no too correct. The original document wey e dey come from na di correct source. For important tin dem, e better make human professional translate am. We no go take responsibility for any wrong understanding or wahala wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->