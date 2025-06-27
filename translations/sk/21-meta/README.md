<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:35:17+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sk"
}
-->
# Budovanie s modelmi Meta Family

## Úvod

Táto lekcia pokrýva:

- Preskúmanie dvoch hlavných modelov Meta family - Llama 3.1 a Llama 3.2
- Porozumenie prípadom použitia a scenárom pre každý model
- Ukážka kódu, ktorá ukazuje unikátne vlastnosti každého modelu

## Meta Family modelov

V tejto lekcii preskúmame 2 modely z Meta family alebo "Llama stáda" - Llama 3.1 a Llama 3.2

Tieto modely sú dostupné v rôznych variantoch a sú dostupné na GitHub Model marketplace. Tu sú ďalšie detaily o používaní GitHub Models na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelov:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Poznámka: Llama 3 je tiež dostupný na GitHub Models, ale v tejto lekcii nebude pokrytý*

## Llama 3.1

S 405 miliardami parametrov sa Llama 3.1 radí do kategórie open source LLM.

Model je vylepšením predchádzajúcej verzie Llama 3 a ponúka:

- Väčšie kontextové okno - 128k tokenov vs 8k tokenov
- Väčšie maximálne výstupné tokeny - 4096 vs 2048
- Lepšiu viacjazyčnú podporu - vďaka zvýšeniu počtu tréningových tokenov

Tieto vlastnosti umožňujú Llama 3.1 zvládať zložitejšie prípady použitia pri budovaní GenAI aplikácií vrátane:
- Natívne volanie funkcií - schopnosť volať externé nástroje a funkcie mimo pracovného toku LLM
- Lepší výkon RAG - vďaka väčšiemu kontextovému oknu
- Generovanie syntetických dát - schopnosť vytvárať efektívne dáta pre úlohy ako doladenie

### Natívne volanie funkcií

Llama 3.1 bola doladená, aby bola efektívnejšia pri volaní funkcií alebo nástrojov. Má tiež dva vstavané nástroje, ktoré model môže identifikovať ako potrebné na použitie na základe užívateľskej výzvy. Tieto nástroje sú:

- **Brave Search** - Môže sa použiť na získanie aktuálnych informácií, ako je počasie, vykonaním webového vyhľadávania
- **Wolfram Alpha** - Môže sa použiť na zložitejšie matematické výpočty, takže písanie vlastných funkcií nie je potrebné.

Môžete tiež vytvoriť vlastné nástroje, ktoré LLM môže volať.

V ukážke kódu nižšie:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovej výzve.
- Posielame užívateľskú výzvu, ktorá sa pýta na počasie v určitom meste.
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Táto ukážka iba robí volanie nástroja, ak chcete získať výsledky, budete si musieť vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu`

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

Aj keď je Llama 3.1 LLM, jedným z jej obmedzení je multimodalita. Teda schopnosť používať rôzne typy vstupov, ako sú obrázky, ako výzvy a poskytovať odpovede. Táto schopnosť je jednou z hlavných vlastností Llama 3.2. Tieto vlastnosti zahŕňajú aj:

- Multimodalita - má schopnosť hodnotiť textové aj obrazové výzvy
- Variácie v malých až stredných veľkostiach (11B a 90B) - to poskytuje flexibilné možnosti nasadenia,
- Variácie len pre text (1B a 3B) - to umožňuje nasadenie modelu na okrajové / mobilné zariadenia a poskytuje nízku latenciu

Podpora multimodality predstavuje veľký krok vo svete open source modelov. Ukážka kódu nižšie berie ako vstup obrázok aj textovú výzvu na získanie analýzy obrázka od Llama 3.2 90B.

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

## Učenie sa tu nekončí, pokračujte na ceste

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste naďalej zvyšovali svoje znalosti o Generative AI!

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.