# Stavba s modely Meta Family

## Úvod

Tato lekce pokryje:

- Prozkoumání dvou hlavních modelů rodiny Meta - Llama 3.1 a Llama 3.2
- Porozumění případům použití a scénářům pro každý model
- Ukázku kódu, která ukazuje jedinečné vlastnosti každého modelu

## Rodina modelů Meta

V této lekci prozkoumáme 2 modely z rodiny Meta nebo "Llama Herd" - Llama 3.1 a Llama 3.2.

Tyto modely jsou k dispozici v různých variantách a jsou dostupné na GitHub Model marketplace. Zde jsou další podrobnosti o používání GitHub Modelů pro [prototypování s AI modely](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianty modelů: 
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Poznámka: Llama 3 je také dostupný na GitHub Models, ale v této lekci není pokryt*

## Llama 3.1

S 405 miliardami parametrů spadá Llama 3.1 do kategorie open source LLM.

Model je vylepšením předchozího vydání Llama 3 tím, že nabízí:

- Větší kontextové okno – 128k tokenů vs 8k tokenů
- Větší maximální počet výstupních tokenů – 4096 vs 2048
- Lepší vícejazyčnou podporu – díky většímu množství tréninkových tokenů

To umožňuje Llama 3.1 zvládat složitější případy použití při tvorbě GenAI aplikací, včetně: 
- Nativní volání funkcí – schopnost volat externí nástroje a funkce mimo pracovní tok LLM
- Lepší výkon RAG – díky většímu kontextovému oknu
- Generování syntetických dat – schopnost vytvářet efektivní data pro úlohy jako doladění

### Nativní volání funkcí

Llama 3.1 byl doladěn tak, aby byl efektivnější při volání funkcí nebo nástrojů. Má také dva vestavěné nástroje, které model rozpozná jako potřebné k použití na základě uživatelského promptu. Tyto nástroje jsou:

- **Brave Search** – Lze použít k získání aktuálních informací, jako je počasí, pomocí webového vyhledávání
- **Wolfram Alpha** – Lze použít k složitějším matematickým výpočtům, takže není třeba psát vlastní funkce.

Také můžete vytvořit své vlastní nástroje, které může LLM volat.

V ukázce kódu níže:

- Definujeme dostupné nástroje (brave_search, wolfram_alpha) v systémovém promptu.
- Pošleme uživatelský prompt, který se ptá na počasí v určitém městě.
- LLM odpoví voláním nástroje Brave Search, které bude vypadat takto `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Poznámka: Tento příklad pouze volá nástroj, pokud chcete získat výsledky, musíte si vytvořit bezplatný účet na stránce Brave API a definovat samotnou funkci.

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

Přestože je Llama 3.1 LLM, jeho omezením je nedostatek multimodality. To znamená, že nemůže používat různé typy vstupů, jako jsou obrázky jako prompt a poskytovat odpovědi. Tuto schopnost představuje jedna z hlavních funkcí Llama 3.2. Mezi další vlastnosti patří:

- Multimodalita – schopnost hodnotit jak textové, tak obrazové prompty
- Variace malých až středních velikostí (11B a 90B) – poskytují flexibilní možnosti nasazení
- Textové varianty (1B a 3B) – umožňují nasazení modelu na okrajová / mobilní zařízení a poskytují nízkou latenci

Podpora multimodality představuje významný krok ve světě open source modelů. Ukázka kódu níže používá jak obraz, tak textový prompt pro získání analýzy obrázku z Llama 3.2 90B.

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

## Učení zde nekončí, pokračujte v cestě

Po dokončení této lekce si prohlédněte naši [sbírku Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste pokračovali v prohlubování svých znalostí o Generativní AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za žádné nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->