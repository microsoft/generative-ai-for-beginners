<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:05:23+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "en"
}
-->
# Building With the Meta Family Models 

## Introduction 

This lesson will cover: 

- Exploring the two main Meta family models - Llama 3.1 and Llama 3.2 
- Understanding the use cases and scenarios for each model 
- Code samples demonstrating the unique features of each model 


## The Meta Family of Models 

In this lesson, we will explore 2 models from the Meta family or "Llama Herd" - Llama 3.1 and Llama 3.2 

These models come in different variants and are available on the GitHub Model marketplace. Here are more details on using GitHub Models to [prototype with AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Model Variants: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Note: Llama 3 is also available on GitHub Models but won’t be covered in this lesson*

## Llama 3.1 

With 405 Billion Parameters, Llama 3.1 fits into the open source LLM category. 

This model is an upgrade to the earlier release Llama 3 by offering: 

- Larger context window - 128k tokens vs 8k tokens 
- Larger Max Output Tokens - 4096 vs 2048 
- Better Multilingual Support - thanks to an increase in training tokens 

These improvements enable Llama 3.1 to handle more complex use cases when building GenAI applications including: 
- Native Function Calling - the ability to call external tools and functions outside of the LLM workflow
- Better RAG Performance - due to the larger context window 
- Synthetic Data Generation - the ability to create effective data for tasks like fine-tuning 

### Native Function Calling 

Llama 3.1 has been fine-tuned to be more effective at making function or tool calls. It also includes two built-in tools that the model can recognize as needed based on the user’s prompt. These tools are: 

- **Brave Search** - Can be used to get up-to-date information like the weather by performing a web search 
- **Wolfram Alpha** - Can be used for more complex mathematical calculations, so you don’t need to write your own functions. 

You can also create your own custom tools that the LLM can call. 

In the code example below: 

- We define the available tools (brave_search, wolfram_alpha) in the system prompt. 
- Send a user prompt asking about the weather in a specific city. 
- The LLM will respond with a tool call to the Brave Search tool, which will look like this `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Note: This example only makes the tool call; if you want to get the results, you’ll need to create a free account on the Brave API page and define the function itself* 

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

Although Llama 3.1 is a powerful LLM, one limitation is multimodality — the ability to use different types of input such as images as prompts and provide responses. This capability is one of the main features of Llama 3.2. Other features include: 

- Multimodality - can process both text and image prompts 
- Small to Medium size variants (11B and 90B) - offering flexible deployment options 
- Text-only variants (1B and 3B) - allowing deployment on edge/mobile devices with low latency 

The multimodal support marks a significant advancement in open source models. The code example below takes both an image and a text prompt to get an analysis of the image from Llama 3.2 90B. 


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

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to keep advancing your Generative AI skills!

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.