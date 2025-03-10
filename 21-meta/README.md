# Building With the Meta Family Models 

## Introduction 

This lesson will cover: 

- Exploring the two main Meta family models - Llama 3.1 and Llama 3.2 
- Understanding the use-cases and scenarios for each model 
- Code sample to show the unique features of each model 


## The Meta Family of Models 

In this lesson, we will explore 2 models from the Meta family or "Llama Herd" - Llama 3.1 and Llama 3.2 

These models come in different variants and are available on the GitHub Model marketplace. Here are more details on using GitHub Models to [prototype with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Model Variants: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Note: Llama 3 is also available on GitHub Models but won't be covered in this lesson*

## Llama 3.1 

At 405 Billion Parameters, Llama 3.1 fits into the open source LLM category. 

The mode is an upgrade to the earlier release Llama 3 by offering: 

- Larger context window - 128k tokens vs 8k tokens 
- Larger Max Output Tokens - 4096 vs 2048 
- Better Multilingual Support - due to increase in training tokens 

These enables Llama 3.1 to handle more complex use cases  when building GenAI applications including: 
- Native Function Calling - the ability to call external tools and functions outside of the LLM workflow
- Better RAG Performance - due to the higher context window 
- Synthetic Data Generation - the ability to create effective data for tasks such as fine-tuning 

### Native Function Calling 

Llama 3.1 has been fine-tuned to be more effective at making function or tool calls. It also has two built-in tools that the model can identify as needing to be used based on the prompt from the user. These tools are: 

- **Brave Search** - Can be used to get up-to-date information like the weather by performing a web search 
- **Wolfram Alpha** - Can be used for more complex mathematical calculations so writing your own functions is not required. 

You can also create your own custom tools that LLM can call. 

In the code example below: 

- We define the available tools (brave_search, wolfram_alpha) in the system prompt. 
- Send a user prompt that asks about the weather in a certain city. 
- The LLM will respond with a tool call to the Brave Search tool which will look like this `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Note: This example only makes the tool call, if you would like to get the results, you will need to create a free account on the Brave API page and define the function itself` 

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

Despite being an LLM, one limitation that Llama 3.1 has is multimodality. That is, being able to use different types of input such as images as prompts and providing responses. This ability is one of the main features of Llama 3.2. These features also include: 

- Multimodality -  has the ability to evaluate both text and image prompts 
- Small to Medium size variations (11B and 90B) - this provides flexible deployment options, 
- Text-only variations (1B and 3B) - this allows the model to be deployed on edge / mobile devices and provides low latency 

The multimodal support represents a big step in the world of open source models. The code example below takes both an image and text prompt to get an analysis of the image from Llama 3.2 90B. 


### Multimodal Support with Llama 3.2

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

## Learning does not stop here, continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

