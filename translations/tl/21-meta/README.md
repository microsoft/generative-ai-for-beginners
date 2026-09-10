# Paggawa Gamit ang Meta Family Models 

## Panimula 

Tatalakayin sa araling ito ang: 

- Pagsisiyasat sa dalawang pangunahing Meta family models - Llama 3.1 at Llama 3.2 
- Pag-unawa sa mga gamit at sitwasyon para sa bawat modelo 
- Halimbawang code upang ipakita ang natatanging mga tampok ng bawat modelo 


## Ang Pamilya ng Mga Modelo ng Meta 

Sa araling ito, susuriin natin ang 2 modelo mula sa pamilya ng Meta o "Llama Herd" - Llama 3.1 at Llama 3.2.

Ang mga modelong ito ay may iba't ibang uri at makukuha sa [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Note:** Ang GitHub Models ay magtatapos sa katapusan ng Hulyo 2026. Narito ang karagdagang impormasyon tungkol sa paggamit ng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para mag-prototype gamit ang AI models.

Mga Variant ng Modelo: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Tandaan: Ang Llama 3 ay makukuha rin sa Microsoft Foundry Models ngunit hindi sasaklawin sa araling ito*

## Llama 3.1 

Sa 405 Bilyong Parameters, ang Llama 3.1 ay kabilang sa kategorya ng open source LLM. 

Ang modelo ay isang upgrade sa naunang release na Llama 3 sa pamamagitan ng pag-aalok ng: 

- Mas malaking context window - 128k tokens laban sa 8k tokens 
- Mas malaking Max Output Tokens - 4096 laban sa 2048 
- Mas mahusay na Multilingual Support - dahil sa pagtaas ng mga training tokens 

Pinapayagan ng mga ito ang Llama 3.1 na hawakan ang mas kumplikadong mga kaso ng paggamit kapag bumubuo ng mga GenAI application kabilang ang: 
- Native Function Calling - ang kakayahang tawagan ang mga panlabas na tool at function sa labas ng LLM workflow
- Mas mahusay na RAG Performance - dahil sa mas mataas na context window 
- Synthetic Data Generation - ang kakayahang lumikha ng epektibong data para sa mga gawain tulad ng fine-tuning 

### Native Function Calling 

Ang Llama 3.1 ay na-fine-tune upang maging mas epektibo sa paggawa ng function o tool calls. Mayroon din itong dalawang built-in na tool na maaaring makilala ng modelo bilang kailangang gamitin base sa prompt mula sa user. Ang mga tool na ito ay: 

- **Brave Search** - Maaaring gamitin para makakuha ng napapanahong impormasyon tulad ng panahon sa pamamagitan ng paggawa ng web search 
- **Wolfram Alpha** - Maaaring gamitin para sa mas komplikadong mga kalkulasyon sa matematika kaya hindi na kailangang sumulat ng sarili mong mga function. 

Maaari ka ring gumawa ng sarili mong custom tools na maaaring tawagin ng LLM. 

Sa halimbawang code sa ibaba: 

- Dinedefine natin ang mga available tools (brave_search, wolfram_alpha) sa system prompt. 
- Nagpapadala ng user prompt na nagtatanong tungkol sa panahon sa isang partikular na lungsod. 
- Ang LLM ay sasagot gamit ang tool call sa Brave Search tool na magiging ganito `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Tandaan: Ang halimbawa na ito ay nagpapagawa lamang ng tool call, kung nais mong makuha ang resulta, kailangan mong gumawa ng libreng account sa Brave API page at idefine ang mismong function.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Kunin ito mula sa "Overview" na pahina ng iyong Microsoft Foundry na proyekto
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

Bagama't isang LLM, isang limitasyon ng Llama 3.1 ay ang kakulangan nito sa multimodality. Ibig sabihin, ang kawalan ng kakayahang gumamit ng iba't ibang uri ng input tulad ng mga larawan bilang mga prompt at magbigay ng mga sagot. Ang kakayahang ito ay isa sa mga pangunahing tampok ng Llama 3.2. Kasama rin sa mga tampok na ito ang: 

- Multimodality - may kakayahang suriin ang parehong text at image prompts 
- Maliit hanggang Katamtamang laki ng mga variant (11B at 90B) - nagbibigay ito ng flexible na mga opsyon sa deployment, 
- Text-only variant (1B at 3B) - nagpapahintulot sa modelo na ma-deploy sa edge / mobile device at nagbibigay ng mababang latency 

Ang suporta para sa multimodal ay isang malaking hakbang sa mundo ng open source models. Ang halimbawang code sa ibaba ay tumatanggap ng parehong imahe at text prompt upang makakuha ng pagsusuri ng larawan mula sa Llama 3.2 90B. 


### Multimodal Support gamit ang Llama 3.2

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

# Kunin ito mula sa pahina ng "Overview" ng iyong Microsoft Foundry na proyekto
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

## Hindi dito nagtatapos ang pag-aaral, ipagpatuloy ang paglalakbay

Pagkatapos matapos ang araling ito, silipin ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->