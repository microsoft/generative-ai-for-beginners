# Práca s modelmi rodiny Meta 

## Úvod 

Táto lekcia pokryje: 

- Preskúmanie dvoch hlavných modelov rodiny Meta - Llama 3.1 a Llama 3.2 
- Pochopenie prípadov použitia a scénarov pre každý model 
- Ukážka kódu na demonštráciu jedinečných funkcií každého modelu 


## Rodina modelov Meta 

V tejto lekcii preskúmame 2 modely z rodiny Meta alebo „Llama stádo“ - Llama 3.1 a Llama 3.2.

Tieto modely prichádzajú v rôznych variantoch a sú dostupné v katalógu [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Poznámka:** GitHub Models bude ukončený koncom júla 2026. Tu sú ďalšie podrobnosti o používaní [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) na prototypovanie s AI modelmi.

Varianty modelov: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Poznámka: Llama 3 je tiež dostupná v Microsoft Foundry Models, ale nebude pokrytá v tejto lekcii*

## Llama 3.1 

S 405 miliardami parametrov patrí Llama 3.1 do kategórie open source LLM. 

Model je vylepšením oproti skoršiemu vydaniu Llama 3 tým, že ponúka: 

- Väčšie kontextové okno - 128k tokenov vs 8k tokenov 
- Väčší maximálny počet výstupných tokenov - 4096 vs 2048 
- Lepšiu podporu viacjazyčnosti - vďaka zvýšeniu počtu trénovacích tokenov 

Tieto schopnosti umožňujú Llama 3.1 zvládať zložitejšie prípady použitia pri budovaní aplikácií GenAI vrátane: 
- Nativne volanie funkcií - schopnosť volať externé nástroje a funkcie mimo toku LLM
- Lepší výkon RAG - vďaka väčšiemu kontextovému oknu 
- Generovanie syntetických dát - schopnosť vytvárať efektívne dáta pre úlohy ako jemné doladenie 

### Nativne volanie funkcií 

Llama 3.1 bola doladená tak, aby bola efektívnejšia pri volaní funkcií alebo nástrojov. Má tiež dva vstavané nástroje, ktoré model môže identifikovať ako potrebné použiť na základe výzvy od používateľa. Tieto nástroje sú: 

- **Brave Search** - Môže byť použitý na získanie aktuálnych informácií, napríklad počasie, vykonaním vyhľadávania na webe 
- **Wolfram Alpha** - Môže byť použitý na komplikovanejšie matematické výpočty, takže nie je potrebné písať vlastné funkcie. 

Môžete tiež vytvoriť svoje vlastné vlastné nástroje, ktoré môže LLM volať. 

V príklade kódu nižšie: 

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovej výzve. 
- Posielame používateľskú výzvu, ktorá sa pýta na počasie v určitom meste. 
- LLM odpovie volaním nástroja Brave Search, ktoré bude vyzerať takto `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Poznámka: Tento príklad iba vykonáva volanie nástroja, ak chcete získať výsledky, budete si musieť vytvoriť bezplatný účet na stránke Brave API a definovať samotnú funkciu.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Získajte ich z stránky "Prehľad" vášho projektu Microsoft Foundry
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

Napriek tomu, že je LLM, jedným obmedzením Llama 3.1 je jej nedostatok multimodality. To znamená neschopnosť použiť rôzne typy vstupov, ako sú obrázky vo výzvach, a poskytovať odpovede. Táto schopnosť je jednou z hlavných funkcií Llama 3.2. Tieto funkcie tiež zahŕňajú: 

- Multimodalita - schopnosť hodnotiť textové aj obrazové výzvy 
- Variácie menšej až strednej veľkosti (11B a 90B) - ktoré poskytujú flexibilné možnosti nasadenia, 
- Výhradne textové variácie (1B a 3B) - umožňujú nasadenie modelu na edge/mobilných zariadeniach a poskytujú nízku latenciu 

Podpora multimodality predstavuje veľký krok vo svete open source modelov. Príklad kódu nižšie berie ako vstup obrázok aj textovú výzvu na získanie analýzy obrázka od Llama 3.2 90B. 


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

# Získajte ich z stránky "Prehľad" vášho projektu Microsoft Foundry
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

## Učenie tu nekončí, pokračujte v ceste

Po dokončení tejto lekcie si pozrite našu [zbierku pre učenie Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali vo zvyšovaní svojich vedomostí o Generatívnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->