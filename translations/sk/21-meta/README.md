# Budovanie s modelmi rodiny Meta 

## Úvod 

Táto lekcia pokryje: 

- Preskúmanie dvoch hlavných modelov rodiny Meta - Llama 3.1 a Llama 3.2 
- Pochopenie použitia a scenárov pre každý model 
- Ukážka kódu pre zobrazenie jedinečných vlastností každého modelu 


## Rodina modelov Meta 

V tejto lekcii preskúmame 2 modely z rodiny Meta alebo "Llama stáda" - Llama 3.1 a Llama 3.2.

Tieto modely sú dostupné v rôznych variantách a nájdete ich v [katalógu Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Poznámka:** GitHub Models bude ukončený na konci júla 2026. Tu sú ďalšie informácie o používaní [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) na prototypovanie AI modelov.

Varianty modelov: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Poznámka: Llama 3 je tiež dostupná v Microsoft Foundry Models, ale v tejto lekcii nebude pokrytá*

## Llama 3.1 

S 405 miliardami parametrov patrí Llama 3.1 do kategórie open source veľkých jazykových modelov (LLM). 

Model je vylepšením predchádzajúceho vydania Llama 3, pričom ponúka: 

- Väčšie kontextové okno - 128k tokenov oproti 8k tokenom 
- Väčší maximálny počet výstupných tokenov - 4096 oproti 2048 
- Lepšiu podporu viacjazyčnosti - vďaka zvýšeniu počtu tréningových tokenov 

Vďaka tomu je Llama 3.1 schopná zvládať zložitejšie použitia pri tvorbe aplikácií GenAI, vrátane: 
- Nativne volanie funkcií - schopnosť volať externé nástroje a funkcie mimo workflow LLM
- Lepší výkon RAG - vďaka väčšiemu kontextovému oknu 
- Generovanie syntetických dát - schopnosť vytvárať efektívne dáta pre úlohy ako jemné dolaďovanie 

### Nativne volanie funkcií 

Llama 3.1 bola doladená tak, aby bola efektívnejšia pri volaní funkcií alebo nástrojov. Má aj dva zabudované nástroje, ktoré model dokáže identifikovať ako potrebné použiť na základe používateľského promptu. Tieto nástroje sú: 

- **Brave Search** - Môže sa použiť na získanie aktuálnych informácií, napr. počasia, vykonaním webového vyhľadávania 
- **Wolfram Alpha** - Môže sa použiť na zložitejšie matematické výpočty, takže nie je potrebné písať vlastné funkcie. 

Môžete si tiež vytvoriť vlastné vlastné nástroje, ktoré môže LLM volať. 

V ukážke kódu nižšie: 

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovom príkaze. 
- Posielame používateľský prompt, ktorý sa pýta na počasie v konkrétnom meste. 
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Poznámka: Tento príklad iba volá nástroj, ak chcete získať výsledky, budete si musieť vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Získajte ich zo stránky „Prehľad“ vášho projektu Microsoft Foundry
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

Napriek tomu, že je to LLM, jedným z obmedzení Llama 3.1 je absencia multimodality. Teda neschopnosť použiť rôzne typy vstupov ako obrázky pre prompt a poskytnúť odpovede. Táto schopnosť je jednou z hlavných vlastností Llama 3.2. Medzi jej vlastnosti tiež patrí: 

- Multimodalita - schopnosť vyhodnocovať textové aj obrazové prompti 
- Variácie malej až strednej veľkosti (11B a 90B) - čo poskytuje flexibilné možnosti nasadenia, 
- Variácie iba s textom (1B a 3B) - umožňuje nasadenie modelu na edge / mobilných zariadeniach a poskytuje nízku latenciu 

Podpora multimodality predstavuje veľký krok vo svete open source modelov. Ukážka kódu nižšie prijíma ako vstup obraz aj textový prompt na získanie analýzy obrazu od Llama 3.2 90B. 


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

# Získajte ich zo stránky „Prehľad“ vášho projektu Microsoft Foundry
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

## Učenie sa tu nekončí, pokračujte v ceste

Po ukončení tejto lekcie si pozrite našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zvyšovaní vašich znalostí o generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->