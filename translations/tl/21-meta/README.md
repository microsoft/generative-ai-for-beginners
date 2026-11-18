# Paggawa Gamit ang Mga Modelo ng Pamilyang Meta 

## Panimula 

Saklaw ng araling ito: 

- Pagsisiyasat sa dalawang pangunahing modelo ng pamilyang Meta - Llama 3.1 at Llama 3.2, pati na rin ang kasalukuyang mga alternatibong magagamit na ginamit sa mga halimbawa ng code (Llama 3.3 at Llama 4) 
- Pag-unawa sa mga gamit at senaryo para sa bawat modelo 
- Halimbawa ng code upang ipakita ang kakaibang mga tampok ng bawat modelo 


## Ang Pamilyang Meta ng mga Modelo 

Sa araling ito, susuriin natin ang 2 modelo mula sa pamilyang Meta o "Llama Herd" - Llama 3.1 at Llama 3.2. Ang mga maaaring patakbuhing halimbawa ng code ay gumagamit ng Llama 3.3 at Llama 4, na kasalukuyang magagamit na mga alternatibo sa katalogo ng Microsoft Foundry Models.

Ang mga modelong ito ay may iba't ibang variant at magagamit sa [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Tandaan:** Ang GitHub Models ay magtatapos sa huling bahagi ng Hulyo 2026. Narito ang karagdagang detalye sa paggamit ng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) upang gumawa ng mga prototype gamit ang mga modelo ng AI.

> **Tandaan:** Ang mga espesipikong bersyon ng modelo na orihinal na ginamit sa araling ito (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) ay hindi na available sa katalogo ng Microsoft Foundry Models. Ang mga halimbawang code sa ibaba ay gumagamit ng `Llama-3.3-70B-Instruct` at `Llama-4-Scout-17B-16E-Instruct` bilang kasalukuyang magagamit na mga alternatibo sa katalogo ng Microsoft Foundry Models, kaya maaari pa rin silang patakbuhin ngayon.

Mga Variant ng Modelo (ayon sa orihinal na nilalaman ng araling ito): 
- Llama 3.1 - 70B Instruct (hindi na ginagamit) 
- Llama 3.1 - 405B Instruct (hindi na ginagamit) 
- Llama 3.2 - 11B Vision Instruct (hindi na ginagamit) 
- Llama 3.2 - 90B Vision Instruct (hindi na ginagamit) 

Kasalukuyang magagamit na mga alternatibo na ginamit sa mga halimbawa ng code: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Tandaan: Ang mga variant ng Llama 3 na tinalakay sa itaas ay pinanatili para sa pangkasaysayan at hindi na magagamit sa Microsoft Foundry Models.*

## Llama 3.1 

Sa 405 Bilyong Parameters, ang Llama 3.1 ay kabilang sa kategorya ng open source LLM. 

Ang modelo ay isang pag-upgrade mula sa naunang bersyon ng Llama 3 sa pamamagitan ng pagbibigay ng: 

- Mas malaki ang window ng kontektsto - 128k tokens laban sa 8k tokens 
- Mas malaking Max Output Tokens - 4096 laban sa 2048 
- Mas mahusay na suporta sa maramihang wika - dahil sa pagdami ng mga training tokens 

Nagbibigay-daan ang mga ito sa Llama 3.1 na hawakan ang mas kumplikadong mga gamit kapag gumagawa ng mga GenAI application kabilang ang: 
- Native Function Calling - ang kakayahang tumawag ng mga external na tool at function sa labas ng workflow ng LLM
- Mas mahusay na RAG Performance - dahil sa mas mataas na window ng kontektsto 
- Synthetic Data Generation - ang kakayahang gumawa ng epektibong data para sa mga gawain tulad ng fine-tuning 

### Native Function Calling 

Ang Llama 3.1 ay na-fine-tune upang maging mas epektibo sa pagtawag ng function o tool. Mayroon din itong dalawang built-in na tool na kayang kilalanin ng modelo na kailangang gamitin ayon sa prompt mula sa user. Ang mga tool na ito ay: 

- **Brave Search** - Maaaring gamitin upang makakuha ng pinakabagong impormasyon tulad ng panahon sa pamamagitan ng web search 
- **Wolfram Alpha** - Maaaring gamitin para sa mas kumplikadong mga kalkulasyon sa matematika kaya hindi na kailangang magsulat ng sariling function. 

Maaari ka ring gumawa ng sarili mong mga custom tools na maaaring tawagin ng LLM. 

Sa halimbawa ng code sa ibaba: 

- Tinutukoy namin ang mga magagamit na tool (brave_search, wolfram_alpha) sa system prompt. 
- Nagpapadala ng user prompt na nagtatanong tungkol sa panahon sa isang partikular na lungsod. 
- Sasagutin ng LLM sa pamamagitan ng pagtawag sa tool na Brave Search na magmumukhang ganito `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Tandaan: Ang halimbawa na ito ay gumagawa lamang ng pagtawag sa tool, kung nais mong makuha ang mga resulta, kakailanganin mong gumawa ng libre o libreng account sa Brave API page at tukuyin mismo ang function.

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

Bagamat isang LLM, isang limitasyon ng Llama 3.1 ay ang kakulangan sa multimodality. Ibig sabihin, hindi nito kayang gamitin ang iba't ibang uri ng input tulad ng mga larawan bilang mga prompt at magbigay ng tugon. Ang kakayahang ito ay isa sa mga pangunahing tampok ng Llama 3.2. Kabilang din sa mga tampok na ito ang: 

- Multimodality - may kakayahang suriin ang parehong text at image prompts 
- Maliit hanggang Katamtamang laki ng mga variant (11B at 90B) - nagbibigay ng mga flexible na opsyon para sa deployment, 
- Pure text na mga variant (1B at 3B) - nagbibigay-daan sa modelo na ma-deploy sa mga edge / mobile device at nagbibigay ng mababang latency 

Ang suporta sa multimodal ay isang malaking hakbang sa mundo ng open source na mga modelo. Ang halimbawa ng code sa ibaba ay tumatanggap ng parehong larawan at text prompt upang makakuha ng pagsusuri ng larawan. Dahil ang Llama 3.2 90B Vision Instruct ay hindi na ginagamit, ang halimbawa ay gumagamit ng `Llama-4-Scout-17B-16E-Instruct`, isang kasalukuyang magagamit na natively multimodal na alternatibo. 


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

## Hindi nagtatapos ang pag-aaral dito, ipagpatuloy ang paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->