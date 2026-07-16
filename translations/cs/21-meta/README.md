# Stavba s modely rodiny Meta 

## Úvod 

Tato lekce bude pokrývat: 

- Prozkoumání dvou hlavních modelů rodiny Meta - Llama 3.1 a Llama 3.2 
- Pochopení případů použití a scénářů pro každý model 
- Ukázkový kód pro předvedení unikátních funkcí každého modelu 


## Rodina modelů Meta 

V této lekci prozkoumáme 2 modely z rodiny Meta nebo "Llama Herd" - Llama 3.1 a Llama 3.2.

Tyto modely jsou k dispozici v různých variantách a najdete je v [katalogu Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Poznámka:** GitHub Models bude ukončen na konci července 2026. Více informací o využití [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pro prototypování s AI modely.

Varianty modelů: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Poznámka: Llama 3 je také dostupná v Microsoft Foundry Models, ale nebude v této lekci pokryta*

## Llama 3.1 

S 405 miliardami parametrů spadá Llama 3.1 do kategorie open source velkých jazykových modelů. 

Model je vylepšením dřívější verze Llama 3 tím, že nabízí: 

- Větší kontextové okno - 128k tokenů oproti 8k tokenům 
- Větší maximální počet výstupních tokenů - 4096 oproti 2048 
- Lepší vícejazyčnou podporu - díky zvýšení počtu tréninkových tokenů 

To umožňuje Llama 3.1 zvládat složitější případy použití při vytváření aplikací GenAI včetně: 
- Nativního volání funkcí - schopnost volat externí nástroje a funkce mimo workflow LLM
- Lepší výkon RAG - díky většímu kontextovému oknu 
- Generování syntetických dat - schopnost vytvářet efektivní data pro úkoly jako doladění modelu 

### Nativní volání funkcí 

Llama 3.1 byla doladěna tak, aby byla efektivnější při volání funkcí nebo nástrojů. Má také dva vestavěné nástroje, které model dokáže identifikovat a použít na základě požadavku uživatele. Tyto nástroje jsou: 

- **Brave Search** - může být použit k získání aktuálních informací, například počasí, provedením webového vyhledávání 
- **Wolfram Alpha** - může být použit pro složitější matematické výpočty, takže není třeba psát vlastní funkce. 

Můžete si také vytvořit vlastní nástroje, které může LLM volat. 

V příkladu kódu níže: 

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovém promptu. 
- Odesíláme uživatelský prompt, který se ptá na počasí v určitém městě. 
- LLM odpoví voláním nástroje Brave Search, které bude vypadat takto `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Poznámka: Tento příklad pouze volá nástroj, pokud chcete získat výsledky, musíte si vytvořit zdarma účet na stránce Brave API a definovat samotnou funkci.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Získejte je ze stránky „Přehled“ vašeho projektu Microsoft Foundry
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

Přestože je Llama 3.1 LLM, její omezením je absence multimodality. To znamená, že není schopna využívat různé typy vstupu, jako jsou obrázky jako prompt, a poskytovat odpovědi. Tato schopnost je jednou z hlavních funkcí Llama 3.2. Další funkce zahrnují: 

- Multimodalita - schopnost zpracovávat jak textové, tak obrazové prompty 
- Malé až střední velikosti varianty (11B a 90B) - což umožňuje flexibilní možnosti nasazení, 
- Varianta pouze s textem (1B a 3B) - umožňuje nasazení na edge / mobilních zařízeních s nízkou latencí 

Multimodální podpora představuje velký krok ve světě open source modelů. Níže uvedený příklad kódu využívá jak obrazový, tak textový prompt k analýze obrázku modelem Llama 3.2 90B. 


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

# Získejte je ze stránky „Přehled“ vašeho projektu Microsoft Foundry
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

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce se podívejte na naši [sbírku Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste mohli dál zvyšovat své znalosti v oblasti generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->