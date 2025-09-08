<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:12:59+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sk"
}
-->
# Budovanie s modelmi Meta rodiny

## Úvod

Táto lekcia pokryje:

- Preskúmanie dvoch hlavných modelov Meta rodiny - Llama 3.1 a Llama 3.2  
- Pochopenie prípadov použitia a scenárov pre každý model  
- Ukážka kódu na demonštráciu jedinečných vlastností každého modelu  

## Meta rodina modelov

V tejto lekcii preskúmame 2 modely z Meta rodiny alebo „Llama Herd“ – Llama 3.1 a Llama 3.2

Tieto modely sú dostupné v rôznych variantoch a nájdete ich na GitHub Model marketplace. Tu sú podrobnosti o používaní GitHub Models na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelov:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Poznámka: Llama 3 je tiež dostupná na GitHub Models, ale v tejto lekcii ju nebudeme pokrývať*

## Llama 3.1

S 405 miliardami parametrov patrí Llama 3.1 do kategórie open source LLM.

Tento model je vylepšením predchádzajúcej verzie Llama 3 a prináša:

- Väčšie kontextové okno – 128k tokenov oproti 8k tokenom  
- Väčší maximálny počet výstupných tokenov – 4096 oproti 2048  
- Lepšiu podporu viacerých jazykov – vďaka zvýšenému počtu trénovacích tokenov  

Vďaka tomu dokáže Llama 3.1 zvládnuť zložitejšie prípady použitia pri tvorbe GenAI aplikácií, vrátane:  
- Nativne volanie funkcií – možnosť volať externé nástroje a funkcie mimo LLM workflow  
- Lepší výkon RAG – vďaka väčšiemu kontextovému oknu  
- Generovanie syntetických dát – schopnosť vytvárať efektívne dáta pre úlohy ako doladenie modelu  

### Nativne volanie funkcií

Llama 3.1 bola doladená tak, aby efektívnejšie volala funkcie alebo nástroje. Má tiež dva zabudované nástroje, ktoré model dokáže rozpoznať a použiť na základe používateľského promptu. Tieto nástroje sú:

- **Brave Search** – používa sa na získanie aktuálnych informácií, napríklad počasia, vykonaním webového vyhľadávania  
- **Wolfram Alpha** – slúži na zložitejšie matematické výpočty, takže nie je potrebné písať vlastné funkcie  

Môžete si tiež vytvoriť vlastné nástroje, ktoré môže LLM volať.

V príklade kódu nižšie:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovom prompte.  
- Posielame používateľský prompt, ktorý sa pýta na počasie v konkrétnom meste.  
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Poznámka: Tento príklad iba vykoná volanie nástroja, ak chcete získať výsledky, musíte si vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu*  

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

Napriek tomu, že ide o LLM, jedným z obmedzení Llama 3.1 je multimodalita, teda schopnosť používať rôzne typy vstupov, ako sú obrázky, ako prompt a poskytovať odpovede. Táto schopnosť je jednou z hlavných vlastností Llama 3.2. Medzi ďalšie vlastnosti patria:

- Multimodalita – schopnosť vyhodnocovať textové aj obrazové prompty  
- Variácie malých až stredných veľkostí (11B a 90B) – poskytujú flexibilné možnosti nasadenia  
- Variácie iba s textom (1B a 3B) – umožňujú nasadenie na edge / mobilných zariadeniach s nízkou latenciou  

Podpora multimodality predstavuje veľký krok vo svete open source modelov. Príklad kódu nižšie využíva ako obrazový, tak textový prompt na získanie analýzy obrázka od Llama 3.2 90B.

### Multimodálna podpora s Llama 3.2

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

## Učenie tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej rozvíjali svoje znalosti o Generatívnej AI!

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.