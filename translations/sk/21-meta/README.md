# Stavať s modelmi rodiny Meta

## Úvod

Táto lekcia pokryje:

- Preskúmanie dvoch hlavných modelov rodiny Meta - Llama 3.1 a Llama 3.2
- Pochopenie prípadov použitia a scenárov pre každý model
- Ukážka kódu na predvedenie jedinečných funkcií každého modelu

## Rodina modelov Meta

V tejto lekcii preskúmame 2 modely z rodiny Meta alebo „Llama Herd“ - Llama 3.1 a Llama 3.2.

Tieto modely sú dostupné v rôznych variantách a sú dostupné na GitHub Model Marketplace. Tu sú bližšie informácie o používaní GitHub Models na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelov:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Poznámka: Llama 3 je taktiež dostupný na GitHub Models, ale v tejto lekcii nebude pokrytý*

## Llama 3.1

S 405 miliardami parametrov patrí Llama 3.1 do kategórie otvorených zdrojových LLM.

Model je vylepšením predchádzajúceho vydania Llama 3 ponúkajúc:

- Väčšie kontextové okno - 128k tokenov oproti 8k tokenom
- Väčší Max Output Tokens - 4096 oproti 2048
- Lepšiu viacjazyčnú podporu - vďaka zvýšeniu počtu tréningových tokenov

Tieto vlastnosti umožňujú Llama 3.1 zvládať zložitejšie prípady použitia pri budovaní GenAI aplikácií vrátane:
- Nativne volanie funkcií - schopnosť volať externé nástroje a funkcie mimo workflow LLM
- Lepší výkon RAG - vďaka väčšiemu kontextovému oknu
- Generovanie syntetických dát - schopnosť vytvárať efektívne dáta pre úlohy ako doladenie

### Nativne volanie funkcií

Llama 3.1 bol doladený tak, aby bol efektívnejší pri volaní funkcií alebo nástrojov. Má tiež dva zabudované nástroje, ktoré model dokáže identifikovať ako potrebné použiť na základe promptu používateľa. Tieto nástroje sú:

- **Brave Search** - Môže byť použitý na získavanie aktuálnych informácií ako počasie vykonaním webového vyhľadávania
- **Wolfram Alpha** - Môže byť použitý na zložitejšie matematické výpočty, takže písanie vlastných funkcií nie je potrebné.

Môžete si tiež vytvoriť vlastné vlastné nástroje, ktoré LLM dokáže volať.

V ukážke kódu nižšie:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovom promte.
- Posielame používateľský prompt s otázkou na počasie v určitom meste.
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Tento príklad iba vykoná volanie nástroja, ak chcete získať výsledky, budete si musieť vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu.

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

Napriek tomu, že ide o LLM, jedným z obmedzení Llama 3.1 je jeho nedostatok multimodality. Teda neschopnosť používať rôzne druhy vstupov ako obrázky ako prompty a poskytovať odpovede. Táto schopnosť je jednou z hlavných vlastností Llama 3.2. Tieto vlastnosti zahŕňajú tiež:

- Multimodalita - má schopnosť vyhodnocovať textové aj obrazové prompty
- Varianty od malej po strednú veľkosť (11B a 90B) - poskytujú flexibilné možnosti nasadenia,
- Textové varianty (1B a 3B) - umožňujú model nasadiť na edge / mobilných zariadeniach a poskytujú nízku latenciu

Podpora multimodality predstavuje veľký krok vo svete open source modelov. Ukážka kódu nižšie berie ako vstup obrázok aj textový prompt, aby získala analýzu obrázka od Llama 3.2 90B.

### Podpora multimodality s Llama 3.2

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

## Učenie tu nekončí, pokračujte na ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu pre učenie Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v rozvíjaní svojich znalostí o generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pri dôležitých informáciách sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z používania tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->