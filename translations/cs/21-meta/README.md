<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:35:02+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "cs"
}
-->
# Stavba s modely rodiny Meta

## Úvod

Tato lekce pokryje:

- Zkoumání dvou hlavních modelů rodiny Meta - Llama 3.1 a Llama 3.2
- Porozumění použití a scénářům pro každý model
- Ukázkový kód k předvedení unikátních vlastností každého modelu

## Rodina modelů Meta

V této lekci prozkoumáme 2 modely z rodiny Meta nebo "Llama Herd" - Llama 3.1 a Llama 3.2.

Tyto modely existují v různých variantách a jsou dostupné na tržišti modelů GitHub. Zde je více informací o používání GitHub Models pro [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelů:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Poznámka: Llama 3 je také dostupná na GitHub Models, ale nebude pokryta v této lekci*

## Llama 3.1

S 405 miliardami parametrů se Llama 3.1 řadí do kategorie open source LLM.

Tento model je vylepšením dřívější verze Llama 3 a nabízí:

- Větší kontextové okno - 128k tokenů vs 8k tokenů
- Větší maximální počet výstupních tokenů - 4096 vs 2048
- Lepší podpora více jazyků - díky zvýšení počtu tréninkových tokenů

To umožňuje Llama 3.1 zvládat složitější případy použití při stavbě GenAI aplikací, včetně:
- Nativní volání funkcí - schopnost volat externí nástroje a funkce mimo workflow LLM
- Lepší výkon RAG - díky vyššímu kontextovému oknu
- Generování syntetických dat - schopnost vytvářet efektivní data pro úkoly jako je jemné doladění

### Nativní volání funkcí

Llama 3.1 byla jemně doladěna, aby byla efektivnější při volání funkcí nebo nástrojů. Má také dva vestavěné nástroje, které model může identifikovat jako potřebné k použití na základě uživatelského podnětu. Tyto nástroje jsou:

- **Brave Search** - Může být použit k získání aktuálních informací, jako je počasí, provedením webového vyhledávání
- **Wolfram Alpha** - Může být použit pro složitější matematické výpočty, takže psaní vlastních funkcí není nutné.

Můžete také vytvořit vlastní nástroje, které LLM může volat.

V níže uvedeném příkladu kódu:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovém podnětu.
- Posíláme uživatelský podnět, který se ptá na počasí v určitém městě.
- LLM odpoví voláním nástroje Brave Search, které bude vypadat takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Tento příklad pouze provádí volání nástroje, pokud byste chtěli získat výsledky, budete potřebovat vytvořit bezplatný účet na stránce Brave API a definovat samotnou funkci*

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

Navzdory tomu, že je LLM, má Llama 3.1 jednu omezenou vlastnost - multimodalitu. To znamená schopnost používat různé typy vstupů, jako jsou obrázky jako podněty a poskytovat odpovědi. Tato schopnost je jednou z hlavních vlastností Llama 3.2. Tyto vlastnosti také zahrnují:

- Multimodalitu - schopnost vyhodnocovat jak textové, tak obrazové podněty
- Variace malé až střední velikosti (11B a 90B) - to poskytuje flexibilní možnosti nasazení,
- Variace pouze textové (1B a 3B) - to umožňuje model nasadit na edge / mobilní zařízení a poskytuje nízkou latenci

Podpora multimodality představuje velký krok ve světě open source modelů. Níže uvedený příklad kódu bere jak obrazový, tak textový podnět, aby získal analýzu obrazu od Llama 3.2 90B.

### Multimodální podpora s Llama 3.2

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

## Učení nekončí zde, pokračujte v cestě

Po dokončení této lekce se podívejte na naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozšiřování svých znalostí o Generative AI!

**Zřeknutí se odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, uvědomte si prosím, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné interpretace vyplývající z použití tohoto překladu.