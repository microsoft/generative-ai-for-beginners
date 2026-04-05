# Pagtatayo Gamit ang Mga Modelo ng Pamilyang Meta

## Panimula

Tatalakayin sa araling ito:

- Pagsusuri sa dalawang pangunahing modelo ng pamilyang Meta - Llama 3.1 at Llama 3.2
- Pag-unawa sa mga gamit at senaryo para sa bawat modelo
- Halimbawang kodigo upang ipakita ang mga natatanging katangian ng bawat modelo

## Ang Pamilyang Meta ng Mga Modelo

Sa araling ito, susuriin natin ang 2 modelo mula sa pamilyang Meta o "Llama Herd" - Llama 3.1 at Llama 3.2.

Ang mga modelong ito ay may iba't ibang bersyon at makukuha sa GitHub Model marketplace. Narito ang karagdagang detalye sa paggamit ng GitHub Models para sa [pagsubok gamit ang mga AI model](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mga Bersyon ng Modelo:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Paalala: Ang Llama 3 ay available rin sa GitHub Models ngunit hindi tatalakayin sa araling ito*

## Llama 3.1

Sa 405 Bilyong Parameter, ang Llama 3.1 ay kabilang sa kategorya ng open source LLM.

Ang modelo ay isang upgrade mula sa naunang Llama 3 sa pamamagitan ng pag-aalok ng:

- Mas malaking context window - 128k tokens kumpara sa 8k tokens
- Mas malaking Max Output Tokens - 4096 kumpara sa 2048
- Mas mahusay na Multilingual Support - dahil sa pagtaas ng training tokens

Pinapayagan nito ang Llama 3.1 na hawakan ang mas kumplikadong mga gamit sa paggawa ng GenAI applications kabilang ang:
- Native Function Calling - ang kakayahang tumawag sa mga external na kasangkapan at function na hiwalay sa LLM workflow
- Mas mahusay na RAG Performance - dahil sa mas mataas na context window
- Synthetic Data Generation - ang kakayahang lumikha ng epektibong data para sa mga gawain tulad ng fine-tuning

### Native Function Calling

Ang Llama 3.1 ay na-fine tune upang maging mas epektibo sa paggawa ng function o tool calls. Mayroon din itong dalawang built-in na kasangkapan na maaaring tuklasin ng modelo na kailangang gamitin batay sa prompt ng gumagamit. Ang mga kasangkapang ito ay:

- **Brave Search** - Maaaring gamitin upang makuha ang napapanahong impormasyon tulad ng panahon sa pamamagitan ng web search
- **Wolfram Alpha** - Maaaring gamitin para sa mas komplikadong kalkulasyon sa matematika kaya hindi na kailangang magsulat ng sarili mong mga function.

Maaari ka ring gumawa ng sarili mong custom na mga kasangkapan na maaaring tawagin ng LLM.

Sa halimbawang kodigo sa ibaba:

- Dinideklara namin ang mga available na kasangkapan (brave_search, wolfram_alpha) sa system prompt.
- Nagpapadala ng user prompt na nagtatanong tungkol sa panahon sa isang lungsod.
- Tutugon ang LLM gamit ang tool call sa Brave Search tool na magiging ganito `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Paalala: Ang halimbawang ito ay gumagawa lamang ng tool call, kung nais mong makuha ang mga resulta, kailangan mong gumawa ng libreng account sa Brave API page at ideklara ang mismong function.

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

Sa kabila ng pagiging LLM, isang limitasyon ng Llama 3.1 ay ang kakulangan nito sa multimodality. Ibig sabihin, hindi nito magamit ang iba't ibang uri ng input tulad ng mga larawan bilang mga prompt at magbigay ng tugon. Ang kakayahang ito ay isa sa mga pangunahing tampok ng Llama 3.2. Kasama sa mga tampok na ito:

- Multimodality - may kakayahang magsuri ng parehong text at image prompts
- Maliit hanggang katamtamang laki ng mga bersyon (11B at 90B) - nagbibigay ito ng flexible na mga pagpipilian sa deployment,
- Mga text-only na bersyon (1B at 3B) - nagbibigay-daan ito sa modelo na mai-deploy sa mga edge/mobile devices at may mababang latency

Ang suporta sa multimodal ay isang malaking hakbang sa mundo ng mga open source na modelo. Ang halimbawang kodigo sa ibaba ay tumatanggap ng parehong larawan at text prompt upang makakuha ng pagsusuri ng larawan mula sa Llama 3.2 90B.

### Multimodal Support sa Llama 3.2

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

## Hindi dito nagtatapos ang pag-aaral, ipagpatuloy ang iyong paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat pinagsisikapan naming maging tumpak ang salin, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga mali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mga mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->