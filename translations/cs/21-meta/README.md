<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:12:47+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "cs"
}
-->
# Tvorba s modely rodiny Meta

## Úvod

Tato lekce pokryje:

- Prozkoumání dvou hlavních modelů rodiny Meta – Llama 3.1 a Llama 3.2
- Pochopení použití a scénářů pro každý model
- Ukázkový kód, který demonstruje jedinečné vlastnosti každého modelu

## Rodina modelů Meta

V této lekci prozkoumáme 2 modely z rodiny Meta neboli „Llama Herd“ – Llama 3.1 a Llama 3.2

Tyto modely jsou dostupné v různých variantách a najdete je na GitHub Model marketplace. Více informací o používání GitHub Models k [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelů:
- Llama 3.1 – 70B Instruct
- Llama 3.1 – 405B Instruct
- Llama 3.2 – 11B Vision Instruct
- Llama 3.2 – 90B Vision Instruct

*Poznámka: Llama 3 je také dostupná na GitHub Models, ale v této lekci ji nebudeme pokrývat*

## Llama 3.1

S 405 miliardami parametrů spadá Llama 3.1 do kategorie open source LLM.

Model je vylepšením předchozí verze Llama 3 a nabízí:

- Větší kontextové okno – 128k tokenů oproti 8k tokenům
- Větší maximální počet výstupních tokenů – 4096 oproti 2048
- Lepší vícejazyčnou podporu – díky zvýšenému počtu tréninkových tokenů

Díky tomu dokáže Llama 3.1 zvládat složitější scénáře při tvorbě GenAI aplikací, včetně:
- Nativního volání funkcí – schopnost volat externí nástroje a funkce mimo workflow LLM
- Lepšího výkonu RAG – díky většímu kontextovému oknu
- Generování syntetických dat – schopnost vytvářet efektivní data pro úkoly jako je doladění modelu

### Nativní volání funkcí

Llama 3.1 byla doladěna tak, aby efektivněji volala funkce nebo nástroje. Má také dva vestavěné nástroje, které model dokáže rozpoznat a použít na základě uživatelského promptu. Tyto nástroje jsou:

- **Brave Search** – lze použít k získání aktuálních informací, například počasí, pomocí webového vyhledávání
- **Wolfram Alpha** – slouží pro složitější matematické výpočty, takže není potřeba psát vlastní funkce

Můžete si také vytvořit vlastní nástroje, které může LLM volat.

V níže uvedeném příkladu kódu:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovém promptu.
- Odesíláme uživatelský prompt, který se ptá na počasí v určitém městě.
- LLM odpoví voláním nástroje Brave Search, které bude vypadat takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Tento příklad pouze volá nástroj, pokud chcete získat výsledky, musíte si vytvořit bezplatný účet na stránce Brave API a definovat samotnou funkci*

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

Přestože je Llama 3.1 LLM, jednou z jejích omezení je multimodalita, tedy schopnost používat různé typy vstupů, například obrázky jako prompt a poskytovat odpovědi. Tato schopnost je jednou z hlavních vlastností Llama 3.2. Mezi další vlastnosti patří:

- Multimodalita – schopnost zpracovávat textové i obrazové prompty
- Varianty malých až středních velikostí (11B a 90B) – poskytují flexibilní možnosti nasazení
- Textové varianty (1B a 3B) – umožňují nasazení na edge / mobilních zařízeních s nízkou latencí

Podpora multimodality představuje velký krok ve světě open source modelů. Níže uvedený příklad kódu využívá jak obrazový, tak textový prompt k analýze obrázku modelem Llama 3.2 90B.

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

## Učení zde nekončí, pokračujte na své cestě

Po dokončení této lekce si prohlédněte naši [kolekci Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte v rozšiřování svých znalostí o Generative AI!

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.