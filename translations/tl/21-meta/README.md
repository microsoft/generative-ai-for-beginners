# Paggawa Gamit ang Meta Family Models 

## Panimula 

Tatalakayin sa araling ito ang: 

- Pagsisiyasat sa dalawang pangunahing mga modelo ng Meta family - Llama 3.1 at Llama 3.2, pati na rin ang kasalukuyang magagamit na mga alternatibo na ginagamit sa mga halimbawa ng code (Llama 3.3 at Llama 4) 
- Pag-unawa sa mga sitwasyon at gamit para sa bawat modelo 
- Halimbawa ng code upang ipakita ang natatanging mga tampok ng bawat modelo 


## Ang Meta Family ng mga Modelo 

Sa araling ito, susuriin natin ang 2 modelo mula sa pamilya ng Meta o "Llama Herd" - Llama 3.1 at Llama 3.2. Ang mga maipapatakbong halimbawa ng code ay gumagamit ng Llama 3.3 at Llama 4, na kasalukuyang magagamit na mga alternatibo sa catalog ng Microsoft Foundry Models.

Ang mga modelong ito ay may iba't ibang mga variant at makikita sa [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Tandaan:** Ang GitHub Models ay magwawakas sa katapusan ng Hulyo 2026. Narito ang higit pang detalye sa paggamit ng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para sa pag-prototype gamit ang mga AI models.

> **Tandaan:** Ang mga tiyak na bersyon ng modelo na pinanggalingan ng araling ito (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) ay hindi na makikita sa catalog ng Microsoft Foundry Models. Ang mga halimbawa ng code sa ibaba ay gumagamit ng `Llama-3.3-70B-Instruct` at `Llama-4-Scout-17B-16E-Instruct` bilang kasalukuyang magagamit na mga alternatibo sa catalog ng Microsoft Foundry Models, kaya ito ay tumatakbo pa rin hanggang ngayon.

Mga Variant ng Modelo (tinalakay sa orihinal na araling ito): 
- Llama 3.1 - 70B Instruct (hindi na ginagamit) 
- Llama 3.1 - 405B Instruct (hindi na ginagamit) 
- Llama 3.2 - 11B Vision Instruct (hindi na ginagamit) 
- Llama 3.2 - 90B Vision Instruct (hindi na ginagamit) 

Kasalukuyang magagamit na mga alternatibo na ginagamit sa mga halimbawa ng code: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Tandaan: Ang mga Llama 3 na variant na tinalakay sa itaas ay itinago para sa kasaysayan at hindi na makikita sa Microsoft Foundry Models.*

## Llama 3.1 

Sa 405 Bilyong Parameter, ang Llama 3.1 ay kabilang sa bukas na source na kategorya ng LLM. 

Ang modelo ay isang pag-upgrade sa naunang inilabas na Llama 3 sa pamamagitan ng pag-aalok ng: 

- Mas malaking context window - 128k tokens kumpara sa 8k tokens 
- Mas malaking Max Output Tokens - 4096 kumpara sa 2048 
- Mas mahusay na Suporta sa Multilingual - dahil sa pagdami ng training tokens 

Pinapayagan ng mga ito ang Llama 3.1 na hawakan ang mas kumplikadong mga kaso ng gamit kapag bumubuo ng mga GenAI application kabilang ang: 
- Native Function Calling - ang kakayahang tumawag ng mga panlabas na tool at function sa labas ng workflow ng LLM
- Mas mahusay na RAG Performance - dahil sa mas mataas na context window 
- Synthetic Data Generation - ang kakayahang gumawa ng epektibong data para sa mga gawain tulad ng fine-tuning 

### Native Function Calling 

Ang Llama 3.1 ay na-fine-tune upang maging mas epektibo sa pagtawag ng function o mga tool. Mayroon din itong dalawang built-in na tool na maaaring matukoy ng modelo na kailangang gamitin batay sa prompt mula sa user. Ang mga tool na ito ay: 

- **Brave Search** - Maaaring gamitin para makakuha ng napapanahong impormasyon tulad ng panahon sa pamamagitan ng pagsasagawa ng web search 
- **Wolfram Alpha** - Maaaring gamitin para sa mas kumplikadong mga kalkulasyong matematikal kaya hindi na kailangang magsulat ng sariling mga function. 

Maaari ka ring gumawa ng sarili mong custom na mga tool na maaaring tawagin ng LLM. 

Sa halimbawa ng code sa ibaba: 

- Tinatalaga namin ang mga magagamit na tool (brave_search, wolfram_alpha) sa system prompt. 
- Nagpapadala ng user prompt na nagtatanong tungkol sa panahon sa isang partikular na lungsod. 
- Ang LLM ay sasagot gamit ang tool call sa Brave Search tool na magmumukha ganito `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Tandaan: Ang halimbawa lamang na ito ay gumagawa ng tawag sa tool, kung nais mong makuha ang mga resulta, kailangan mong gumawa ng libreng account sa Brave API page at idefine ang function mismo.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Sa kabila ng pagiging isang LLM, ang isang limitasyon ng Llama 3.1 ay ang kakulangan nito sa multimodality. Ibig sabihin, hindi nito magamit ang iba't ibang uri ng input tulad ng mga larawan bilang mga prompt at magbigay ng mga tugon. Ang kakayahang ito ay isa sa mga pangunahing tampok ng Llama 3.2. Kasama rin sa mga tampok na ito: 

- Multimodality - may kakayahang suriin ang parehong mga text at image prompt 
- Maliit hanggang katamtamang laki ng mga variation (11B at 90B) - nagbibigay ito ng flexible na mga opsyon sa deployment, 
- Variations na text-only (1B at 3B) - pinapayagan ang modelo na ideploy sa mga edge / mobile na device at nagbibigay ng mababang latency 

Ang suporta sa multimodal ay isang malaking hakbang sa mundo ng mga open source na modelo. Ang halimbawa ng code sa ibaba ay tumatanggap ng parehong larawan at text prompt upang makakuha ng pagsusuri ng larawan. Dahil ang Llama 3.2 90B Vision Instruct ay hindi na ginagamit, ang halimbawa ay gumagamit ng `Llama-4-Scout-17B-16E-Instruct`, isang kasalukuyang magagamit na native multimodal na alternatibo. 


### Suporta sa Multimodal gamit ang Llama 3.2

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Hindi dito nagtatapos ang pagkatuto, ipagpatuloy ang paglalakbay

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagtaas ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->