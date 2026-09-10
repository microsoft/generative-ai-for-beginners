# Práce s modely rodiny Meta 

## Úvod 

Tato lekce pokryje: 

- Prozkoumání dvou hlavních modelů rodiny Meta - Llama 3.1 a Llama 3.2 
- Pochopení použití a scénářů pro každý model 
- Ukázka kódu předvádějící jedinečné vlastnosti každého modelu 


## Rodina modelů Meta 

V této lekci prozkoumáme 2 modely z rodiny Meta nebo „Llama stáda“ - Llama 3.1 a Llama 3.2.

Tyto modely jsou dostupné v různých variantách a naleznete je v [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Poznámka:** GitHub Models končí ke konci července 2026. Více informací o použití [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pro prototypování AI modelů najdete zde.

Varianty modelů: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Poznámka: Llama 3 je také dostupná v Microsoft Foundry Models, ale nebude pokryta v této lekci*

## Llama 3.1 

S 405 miliardami parametrů se Llama 3.1 řadí mezi otevřené zdrojové LLM. 

Model je vylepšením oproti předchozímu vydání Llama 3 tím, že nabízí: 

- Větší kontextové okno - 128k tokenů oproti 8k tokenům 
- Větší maximální počet výstupních tokenů - 4096 oproti 2048 
- Lepší vícejazyčnou podporu - díky zvýšení počtu tréninkových tokenů 

To umožňuje Llama 3.1 zvládat složitější případy použití při budování GenAI aplikací, včetně: 
- Nativní volání funkcí - možnost volat externí nástroje a funkce mimo LLM pracovní tok
- Lepší výkon RAG - díky většímu kontextovému oknu 
- Generování syntetických dat - schopnost vytvářet efektivní data pro úlohy jako jemné doladění 

### Nativní volání funkcí 

Llama 3.1 byla doladěna, aby byla efektivnější při volání funkcí nebo nástrojů. Má také dva vestavěné nástroje, které model může na základě uživatelského promptu identifikovat jako potřebné k použití. Tyto nástroje jsou: 

- **Brave Search** - Lze použít k získání aktuálních informací, jako je počasí, provedením webového vyhledávání 
- **Wolfram Alpha** - Lze použít pro složitější matematické výpočty, takže není nutné psát vlastní funkce. 

Můžete také vytvářet vlastní nástroje, které může LLM volat. 

V ukázce kódu níže: 

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovém promptu. 
- Odesíláme uživatelský prompt ptající se na počasí v určitém městě. 
- LLM odpoví voláním nástroje Brave Search, které bude vypadat takto `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Poznámka: Tento příklad pouze provede volání nástroje, pokud chcete získat výsledky, budete si muset vytvořit bezplatný účet na stránce Brave API a definovat samotnou funkci.

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

Přestože je Llama 3.1 LLM, její omezení je nedostatek multimodality. To znamená neschopnost používat různé typy vstupů, jako jsou obrázky jako prompty a poskytovat odpovědi. Tuto schopnost má jedna z hlavních funkcí Llama 3.2. Tyto funkce také zahrnují: 

- Multimodalita - schopnost vyhodnocovat jak textové, tak obrazové prompty 
- Varianty od malé po střední velikost (11B a 90B) - poskytuje flexibilní možnosti nasazení, 
- Pouze textové varianty (1B a 3B) - umožňuje nasazení na edge / mobilních zařízeních a poskytuje nízkou latenci 

Podpora multimodality představuje velký krok ve světě open source modelů. Ukázka kódu níže přijímá jak obraz, tak textový prompt pro analýzu obrázku modelem Llama 3.2 90B. 


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

Po dokončení této lekce si prohlédněte naši [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a pokračujte ve zvyšování svých znalostí o Generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->