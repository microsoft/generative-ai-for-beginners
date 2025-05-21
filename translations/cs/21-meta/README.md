<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:15:35+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "cs"
}
-->
# Stavění s modely rodiny Meta

## Úvod

Tato lekce pokryje:

- Prozkoumání dvou hlavních modelů rodiny Meta - Llama 3.1 a Llama 3.2
- Pochopení použití a scénářů pro každý model
- Ukázka kódu pro zobrazení unikátních vlastností každého modelu

## Rodina modelů Meta

V této lekci prozkoumáme 2 modely z rodiny Meta nebo "stáda Llama" - Llama 3.1 a Llama 3.2.

Tyto modely jsou dostupné v různých variantách a jsou k dispozici na GitHub Model marketplace. Zde jsou další podrobnosti o používání GitHub Models pro [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelů:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Poznámka: Llama 3 je také dostupná na GitHub Models, ale nebude pokryta v této lekci*

## Llama 3.1

S 405 miliardami parametrů spadá Llama 3.1 do kategorie open source LLM.

Model je vylepšením předchozí verze Llama 3 tím, že nabízí:

- Větší kontextové okno - 128k tokenů oproti 8k tokenům
- Větší maximální počet výstupních tokenů - 4096 oproti 2048
- Lepší vícejazyčnou podporu - díky zvýšení počtu tréninkových tokenů

To umožňuje Llama 3.1 zvládat složitější případy použití při vytváření GenAI aplikací včetně:
- Volání nativních funkcí - schopnost volat externí nástroje a funkce mimo pracovní postup LLM
- Lepší výkon RAG - díky vyššímu kontextovému oknu
- Generování syntetických dat - schopnost vytvářet efektivní data pro úkoly, jako je doladění

### Volání nativních funkcí

Llama 3.1 byla doladěna, aby byla efektivnější při volání funkcí nebo nástrojů. Má také dva vestavěné nástroje, které model může identifikovat jako potřebné na základě zadání od uživatele. Tyto nástroje jsou:

- **Brave Search** - Může být použit k získání aktuálních informací, jako je počasí, provedením webového vyhledávání
- **Wolfram Alpha** - Může být použit pro složitější matematické výpočty, takže není nutné psát vlastní funkce.

Můžete také vytvořit vlastní nástroje, které LLM může volat.

V níže uvedeném příkladu kódu:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovém promptu.
- Pošleme uživatelský prompt, který se ptá na počasí v určitém městě.
- LLM odpoví voláním nástroje Brave Search, které bude vypadat takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Tento příklad pouze provádí volání nástroje, pokud chcete získat výsledky, budete si muset vytvořit bezplatný účet na stránce Brave API a definovat samotnou funkci*

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

Přestože je Llama 3.1 LLM, má jedno omezení - multimodalitu. To znamená, že je schopna používat různé typy vstupů, jako jsou obrázky, jako prompty a poskytovat odpovědi. Tato schopnost je jednou z hlavních vlastností Llama 3.2. Tyto vlastnosti také zahrnují:

- Multimodalitu - schopnost vyhodnocovat textové i obrazové prompty
- Malé až střední velikosti variant (11B a 90B) - to poskytuje flexibilní možnosti nasazení,
- Pouze textové varianty (1B a 3B) - to umožňuje model nasadit na edge / mobilní zařízení a poskytuje nízkou latenci

Podpora multimodality představuje velký krok ve světě open source modelů. Níže uvedený příklad kódu bere jak obrazový, tak textový prompt, aby získal analýzu obrazu z Llama 3.2 90B.

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

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce si prohlédněte naši [kolekci učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte ve zvyšování svých znalostí o generativní AI!

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI překladatele [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.