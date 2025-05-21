<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:15:54+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sk"
}
-->
# Budovanie s modelmi Meta Family

## Úvod

Táto lekcia pokryje:

- Preskúmanie dvoch hlavných modelov Meta family - Llama 3.1 a Llama 3.2
- Pochopenie prípadov použitia a scenárov pre každý model
- Ukážka kódu, ktorá zobrazuje jedinečné vlastnosti každého modelu

## Meta Family of Models

V tejto lekcii preskúmame 2 modely z rodiny Meta alebo "Llama Herd" - Llama 3.1 a Llama 3.2

Tieto modely sú dostupné v rôznych variantoch a sú dostupné na GitHub Model marketplace. Tu sú podrobnosti o používaní GitHub Models na [prototypovanie s AI modelmi](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelov:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Poznámka: Llama 3 je tiež dostupná na GitHub Models, ale nebude pokrytá v tejto lekcii*

## Llama 3.1

S 405 miliardami parametrov, Llama 3.1 sa radí do kategórie open source LLM.

Model je vylepšením skoršej verzie Llama 3 tým, že ponúka:

- Väčšie okno kontextu - 128k tokenov oproti 8k tokenom
- Väčšie Max Output Tokens - 4096 oproti 2048
- Lepšiu podporu viacerých jazykov - vďaka zvýšeniu počtu tréningových tokenov

Tieto vlastnosti umožňujú Llama 3.1 zvládať zložitejšie prípady použitia pri budovaní GenAI aplikácií vrátane:
- Natívne volanie funkcií - schopnosť volať externé nástroje a funkcie mimo pracovného toku LLM
- Lepší výkon RAG - vďaka vyššiemu oknu kontextu
- Generovanie syntetických dát - schopnosť vytvárať efektívne dáta pre úlohy ako jemné doladenie

### Natívne volanie funkcií

Llama 3.1 bola jemne doladená, aby bola efektívnejšia pri volaní funkcií alebo nástrojov. Má tiež dva vstavané nástroje, ktoré model dokáže identifikovať ako potrebné na použitie na základe výzvy od používateľa. Tieto nástroje sú:

- **Brave Search** - Môže byť použitý na získanie aktuálnych informácií, ako je počasie, vykonaním webového vyhľadávania
- **Wolfram Alpha** - Môže byť použitý na zložitejšie matematické výpočty, takže nie je potrebné písať vlastné funkcie.

Môžete tiež vytvoriť vlastné nástroje, ktoré LLM môže volať.

V ukážke kódu nižšie:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovej výzve.
- Pošleme výzvu používateľa, ktorá sa pýta na počasie v určitom meste.
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Táto ukážka len vykonáva volanie nástroja, ak by ste chceli získať výsledky, budete potrebovať vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu*

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

Aj keď je LLM, jedným z obmedzení Llama 3.1 je multimodalita. To znamená, schopnosť používať rôzne typy vstupov, ako sú obrázky ako výzvy a poskytovať odpovede. Táto schopnosť je jednou z hlavných vlastností Llama 3.2. Tieto vlastnosti zahŕňajú:

- Multimodalita - má schopnosť hodnotiť textové aj obrazové výzvy
- Malé až stredné veľkostné varianty (11B a 90B) - to poskytuje flexibilné možnosti nasadenia,
- Varianty iba textové (1B a 3B) - to umožňuje modelu byť nasadený na okrajových / mobilných zariadeniach a poskytuje nízku latenciu

Podpora multimodality predstavuje veľký krok v oblasti open source modelov. Ukážka kódu nižšie berie ako vstup obraz a textovú výzvu, aby získala analýzu obrazu od Llama 3.2 90B.

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

## Učenie nekončí tu, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [Generative AI Learning kolekciu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozširovaní vašich znalostí o Generative AI!

**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.