<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:14:38+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tl"
}
-->
# Pagbuo Gamit ang Meta Family Models

## Panimula

Saklaw ng araling ito ang:

- Paggalugad sa dalawang pangunahing Meta family models - Llama 3.1 at Llama 3.2
- Pag-unawa sa mga use-cases at sitwasyon para sa bawat modelo
- Halimbawa ng code upang ipakita ang mga natatanging tampok ng bawat modelo

## Ang Meta Family ng Mga Modelo

Sa araling ito, susuriin natin ang 2 modelo mula sa Meta family o "Llama Herd" - Llama 3.1 at Llama 3.2

Ang mga modelong ito ay may iba't ibang variant at makukuha sa GitHub Model marketplace. Narito ang higit pang detalye sa paggamit ng GitHub Models upang [gumawa ng prototype gamit ang mga AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mga Variant ng Modelo:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Nota: Ang Llama 3 ay makukuha rin sa GitHub Models ngunit hindi ito saklaw ng araling ito*

## Llama 3.1

Sa 405 Bilyong Parameter, ang Llama 3.1 ay pasok sa kategorya ng open source LLM.

Ang mode ay isang pag-upgrade sa naunang release na Llama 3 sa pamamagitan ng pag-aalok ng:

- Mas malaking context window - 128k tokens kumpara sa 8k tokens
- Mas malaking Max Output Tokens - 4096 kumpara sa 2048
- Mas mahusay na Multilingual Support - dahil sa pagtaas ng mga training tokens

Ang mga ito ay nagbibigay-daan sa Llama 3.1 na hawakan ang mas kumplikadong mga kaso ng paggamit kapag gumagawa ng GenAI applications kabilang ang:
- Native Function Calling - ang kakayahang tumawag ng mga panlabas na tools at function sa labas ng LLM workflow
- Mas mahusay na RAG Performance - dahil sa mas mataas na context window
- Synthetic Data Generation - ang kakayahang lumikha ng epektibong data para sa mga gawain tulad ng fine-tuning

### Native Function Calling

Ang Llama 3.1 ay na-fine-tune upang maging mas epektibo sa paggawa ng function o tool calls. Mayroon din itong dalawang built-in na tools na maaaring makilala ng modelo bilang kailangang gamitin batay sa prompt mula sa user. Ang mga tool na ito ay:

- **Brave Search** - Maaaring gamitin upang makuha ang pinakabagong impormasyon tulad ng panahon sa pamamagitan ng pagganap ng web search
- **Wolfram Alpha** - Maaaring gamitin para sa mas kumplikadong mathematical calculations kaya hindi na kinakailangan ang pagsusulat ng sariling mga function.

Maaari ka ring lumikha ng sarili mong custom tools na maaaring tawagin ng LLM.

Sa halimbawa ng code sa ibaba:

- Tinutukoy namin ang mga available na tools (brave_search, wolfram_alpha) sa system prompt.
- Magpadala ng user prompt na nagtatanong tungkol sa panahon sa isang tiyak na lungsod.
- Ang LLM ay tutugon gamit ang isang tool call sa Brave Search tool na magmumukhang ganito `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: Ang halimbawang ito ay gumagawa lamang ng tool call, kung nais mong makuha ang mga resulta, kakailanganin mong lumikha ng libreng account sa Brave API page at tukuyin ang function mismo*

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

Kahit na isang LLM, ang isang limitasyon na mayroon ang Llama 3.1 ay ang multimodality. Ibig sabihin, ang kakayahang gumamit ng iba't ibang uri ng input tulad ng mga imahe bilang mga prompt at pagbibigay ng mga tugon. Ang kakayahang ito ay isa sa mga pangunahing tampok ng Llama 3.2. Kasama rin sa mga tampok na ito ang:

- Multimodality - may kakayahang suriin ang parehong text at image prompts
- Maliit hanggang Katamtamang laki ng mga variation (11B at 90B) - nagbibigay ito ng flexible deployment options,
- Text-only variations (1B at 3B) - nagbibigay-daan ito sa modelo na ma-deploy sa edge / mobile devices at nagbibigay ng mababang latency

Ang multimodal support ay kumakatawan sa isang malaking hakbang sa mundo ng open source models. Ang halimbawa ng code sa ibaba ay tumatanggap ng parehong imahe at text prompt upang makakuha ng pagsusuri ng imahe mula sa Llama 3.2 90B.

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

## Hindi natatapos dito ang pagkatuto, ipagpatuloy ang Paglalakbay

Matapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

**Pagtatatuwa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkaka-tugma. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.