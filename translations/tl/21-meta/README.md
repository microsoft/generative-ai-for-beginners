<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:12:11+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tl"
}
-->
# Paggawa gamit ang Meta Family Models

## Panimula

Saklaw ng araling ito ang:

- Pagsusuri sa dalawang pangunahing Meta family models - Llama 3.1 at Llama 3.2
- Pag-unawa sa mga gamit at sitwasyon para sa bawat modelo
- Halimbawa ng code upang ipakita ang natatanging katangian ng bawat modelo

## Ang Meta Family ng mga Modelo

Sa araling ito, tatalakayin natin ang 2 modelo mula sa Meta family o "Llama Herd" - Llama 3.1 at Llama 3.2

Ang mga modelong ito ay may iba't ibang variant at makukuha sa GitHub Model marketplace. Narito ang karagdagang detalye sa paggamit ng GitHub Models para sa [prototyping gamit ang AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Mga Variant ng Modelo:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Note: Available din ang Llama 3 sa GitHub Models pero hindi ito tatalakayin sa araling ito*

## Llama 3.1

Sa 405 Bilyong Parameters, ang Llama 3.1 ay kabilang sa open source LLM category.

Ang modelong ito ay isang upgrade mula sa naunang Llama 3 sa pamamagitan ng:

- Mas malaking context window - 128k tokens kumpara sa 8k tokens
- Mas malaking Max Output Tokens - 4096 kumpara sa 2048
- Mas mahusay na Multilingual Support - dahil sa pagdami ng training tokens

Dahil dito, kaya ng Llama 3.1 na hawakan ang mas kumplikadong mga kaso ng paggamit sa paggawa ng GenAI applications kabilang ang:
- Native Function Calling - kakayahang tumawag ng mga external na tools at functions sa labas ng LLM workflow
- Mas mahusay na RAG Performance - dahil sa mas malaking context window
- Synthetic Data Generation - kakayahang gumawa ng epektibong data para sa mga gawain tulad ng fine-tuning

### Native Function Calling

Ang Llama 3.1 ay na-fine-tune upang maging mas epektibo sa pagtawag ng mga function o tool. Mayroon din itong dalawang built-in na tools na kayang tukuyin ng modelo na kailangang gamitin base sa prompt ng user. Ang mga tools na ito ay:

- **Brave Search** - Maaaring gamitin para makakuha ng pinakabagong impormasyon tulad ng lagay ng panahon sa pamamagitan ng web search
- **Wolfram Alpha** - Maaaring gamitin para sa mas kumplikadong mga kalkulasyon sa matematika kaya hindi na kailangang magsulat ng sariling mga function

Maaari ka ring gumawa ng sarili mong custom tools na maaaring tawagin ng LLM.

Sa halimbawa ng code sa ibaba:

- Ipinapahayag natin ang mga available na tools (brave_search, wolfram_alpha) sa system prompt.
- Nagpapadala ng user prompt na nagtatanong tungkol sa lagay ng panahon sa isang partikular na lungsod.
- Sasagot ang LLM gamit ang tool call sa Brave Search tool na magmumukhang ganito `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Note: Ang halimbawang ito ay gumagawa lamang ng tool call, kung nais mong makuha ang resulta, kailangan mong gumawa ng libreng account sa Brave API page at idefine ang function mismo*

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

Bagamat isang LLM, may limitasyon ang Llama 3.1 sa multimodality. Ibig sabihin, ang kakayahang gumamit ng iba't ibang uri ng input tulad ng mga larawan bilang prompt at magbigay ng tugon. Isa ito sa mga pangunahing katangian ng Llama 3.2. Kasama rin sa mga katangiang ito ang:

- Multimodality - may kakayahang suriin ang parehong text at image prompts
- Maliit hanggang Katamtamang laki na mga variant (11B at 90B) - nagbibigay ito ng flexible na mga opsyon sa deployment
- Text-only na mga variant (1B at 3B) - nagbibigay-daan ito para ma-deploy ang modelo sa edge / mobile devices at nagbibigay ng mababang latency

Ang suporta sa multimodal ay isang malaking hakbang sa mundo ng open source models. Ang halimbawa ng code sa ibaba ay tumatanggap ng parehong larawan at text prompt upang makakuha ng pagsusuri ng larawan mula sa Llama 3.2 90B.

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

## Hindi dito nagtatapos ang pag-aaral, ipagpatuloy ang paglalakbay

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.