# Budovanie s modelmi rodiny Meta 

## Úvod 

Táto lekcia pokryje: 

- Preskúmanie dvoch hlavných modelov rodiny Meta - Llama 3.1 a Llama 3.2, plus aktuálne dostupné alternatívy použité v ukážkach kódu (Llama 3.3 a Llama 4) 
- Pochopenie prípadov použitia a scenárov pre každý model 
- Ukážka kódu na zobrazenie jedinečných vlastností každého modelu 


## Rodina modelov Meta 

V tejto lekcii preskúmame 2 modely z rodiny Meta alebo "Llama stádo" - Llama 3.1 a Llama 3.2. Spustiteľné príklady kódu používajú Llama 3.3 a Llama 4, ktoré sú aktuálne dostupnými alternatívami v katalógu Microsoft Foundry Models.

Tieto modely majú rôzne varianty a sú dostupné v [Microsoft Foundry Models katalógu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Poznámka:** GitHub Models sa ukončuje na konci júla 2026. Tu sú ďalšie podrobnosti o používaní [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) na prototypovanie s AI modelmi.

> **Poznámka:** Konkrétne verzie modelov, pre ktoré bola táto lekcia pôvodne napísaná (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), boli odvtedy vyradené z katalógu Microsoft Foundry Models. Nižšie uvedené príklady kódu používajú `Llama-3.3-70B-Instruct` a `Llama-4-Scout-17B-16E-Instruct` ako aktuálne dostupné alternatívy v katalógu Microsoft Foundry Models, takže stále fungujú.

Varianty modelov (ako pôvodne pokryté v tejto lekcii): 
- Llama 3.1 - 70B Instruct (vyradený) 
- Llama 3.1 - 405B Instruct (vyradený) 
- Llama 3.2 - 11B Vision Instruct (vyradený) 
- Llama 3.2 - 90B Vision Instruct (vyradený) 

Aktuálne dostupné alternatívy použité v ukážkach kódu: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Poznámka: Vyššie diskutované varianty Llama 3 sú zachované pre historický kontext a už nie sú dostupné v Microsoft Foundry Models.*

## Llama 3.1 

S 405 miliardami parametrov spadá Llama 3.1 do kategórie otvorených LLM (large language models). 

Model je vylepšením oproti skoršiemu vydaniu Llama 3 tým, že ponúka: 

- Väčšie kontextové okno - 128k tokenov oproti 8k tokenom 
- Väčší maximálny počet výstupných tokenov - 4096 oproti 2048 
- Lepšiu viacjazyčnú podporu - vďaka zvýšeniu počtu trénovacích tokenov 

To umožňuje Llama 3.1 zvládať komplexnejšie prípady použitia pri budovaní aplikácií GenAI vrátane: 
- Nativne volanie funkcií - schopnosť volať externé nástroje a funkcie mimo workflow LLM
- Lepší výkon RAG - vďaka väčšiemu kontextovému oknu 
- Generovanie syntetických dát - schopnosť vytvárať efektívne dáta pre úlohy ako doladenie modelu 

### Nativne volanie funkcií 

Llama 3.1 bola doladená tak, aby bola efektívnejšia pri vykonávaní volaní funkcií alebo nástrojov. Má tiež dva zabudované nástroje, ktoré model môže identifikovať ako potrebné na použitie na základe používateľského promptu. Tieto nástroje sú: 

- **Brave Search** - Môže sa použiť na získanie aktuálnych informácií ako počasie vykonaním webového vyhľadávania 
- **Wolfram Alpha** - Môže sa použiť na komplexnejšie matematické výpočty, takže nie je potrebné písať vlastné funkcie. 

Môžete si tiež vytvoriť svoje vlastné vlastné nástroje, ktoré môže LLM volať. 

V ukážke kódu nižšie: 

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovom promptu. 
- Posielame používateľský prompt, ktorý sa pýta na počasie v určitom meste. 
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Poznámka: Tento príklad len vykonáva volanie nástroja, ak chcete získať výsledky, musíte si vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu.

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

Napriek tomu, že je LLM, jednou z obmedzení Llama 3.1 je jeho absencia multimodality. Teda neschopnosť používať rôzne typy vstupov ako obrázky ako prompt a poskytovať odpovede. Táto schopnosť je jednou z hlavných funkcií Llama 3.2. Tieto funkcie zahŕňajú tiež: 

- Multimodalita - má schopnosť hodnotiť textové aj obrazové prompty 
- Variácie malej až strednej veľkosti (11B a 90B) - poskytuje flexibilné možnosti nasadenia, 
- Textové varianty (1B a 3B) - umožňujú nasadenie modelu na okraji / mobilných zariadeniach a poskytujú nízku latenciu 

Podpora multimodality predstavuje veľký krok vo svete open source modelov. Ukážka kódu nižšie prijíma ako vstup aj obrázok aj textový prompt na získanie analýzy obrázku. Keďže Llama 3.2 90B Vision Instruct bol vyradený, príklad používa `Llama-4-Scout-17B-16E-Instruct`, aktuálne dostupnú natívne multimodálnu alternatívu. 


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

## Učenie sa tu nekončí, pokračujte na ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zdokonaľovaní svojich znalostí o Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->