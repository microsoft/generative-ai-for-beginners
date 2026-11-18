# Gradnja z modeli družine Meta 

## Uvod 

Ta lekcija bo zajemala: 

- Raziskovanje dveh glavnih modelov družine Meta - Llama 3.1 in Llama 3.2, ter trenutno razpoložljivih alternativ, uporabljenih v primerih kode (Llama 3.3 in Llama 4) 
- Razumevanje primerov uporabe in scenarijev za vsak model 
- Primer kode, ki prikazuje edinstvene značilnosti vsakega modela 


## Družina modelov Meta 

V tej lekciji bomo raziskali 2 modela iz družine Meta ali "Čreda Llama" - Llama 3.1 in Llama 3.2. Uporabljeni primerni kodi uporabljata Llama 3.3 in Llama 4, ki so trenutno razpoložljive alternative v katalogu Microsoft Foundry Models.

Ti modeli prihajajo v različnih različicah in so na voljo v [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Opomba:** GitHub Models se bo upokojil konec julija 2026. Tukaj so podrobnosti o uporabi [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiranje z AI modeli.

> **Opomba:** Specifične različice modelov, na katerih je bila ta lekcija prvotno napisana (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), so bile od takrat odstranjene iz kataloga Microsoft Foundry Models. Primeri kode spodaj uporabljajo `Llama-3.3-70B-Instruct` in `Llama-4-Scout-17B-16E-Instruct` kot trenutno razpoložljive alternative v katalogu Microsoft Foundry Models, zato še vedno delujejo danes.

Različice modelov (kot je prvotno zajeto v tej lekciji): 
- Llama 3.1 - 70B Instruct (ukinjeno) 
- Llama 3.1 - 405B Instruct (ukinjeno) 
- Llama 3.2 - 11B Vision Instruct (ukinjeno) 
- Llama 3.2 - 90B Vision Instruct (ukinjeno) 

Trenutno razpoložljive alternative, uporabljene v primerih kode: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Opomba: Različice Llama 3, omenjene zgoraj, so ohranjene za zgodovinski kontekst in niso več na voljo v Microsoft Foundry Models.*

## Llama 3.1 

Z 405 milijardami parametrov, Llama 3.1 spada v kategorijo odprtokodnih LLM. 

Model je nadgradnja prejšnje izdaje Llama 3, saj ponuja: 

- Večje kontekstno okno - 128k tokenov v primerjavi z 8k tokeni 
- Več maksimalnih izhodnih tokenov - 4096 v primerjavi z 2048 
- Boljša podpora več jezikov - zaradi povečanja števila učnih tokenov 

To omogoča Llama 3.1, da obravnava zahtevnejše primere uporabe pri gradnji GenAI aplikacij, vključno z: 
- Nativno klicanje funkcij - sposobnost klicanja zunanjih orodij in funkcij zunaj LLM poteka dela
- Boljša RAG zmogljivost - zaradi večjega kontekstnega okna 
- Sintetična generacija podatkov - sposobnost ustvarjanja učinkovitih podatkov za naloge, kot je fino nastavljanje 

### Nativno klicanje funkcij 

Llama 3.1 je bil dodatno prilagojen za učinkovitejše izvajanje klicev funkcij ali orodij. Ima tudi dve vgrajeni orodji, ki jih model lahko prepozna kot potrebni za uporabo glede na uporabniški poziv. Ta orodja so: 

- **Brave Search** - lahko se uporabi za pridobitev ažurnih informacij, kot je vreme, z iskanjem po spletu 
- **Wolfram Alpha** - se lahko uporabi za bolj kompleksne matematične izračune, zato pisanje lastnih funkcij ni potrebno. 

Lahko ustvarite tudi lastna prilagojena orodja, ki jih LLM lahko pokliče. 

V spodnjem primeru kode: 

- Določimo razpoložljiva orodja (brave_search, wolfram_alpha) v sistemskem pozivu. 
- Pošljemo uporabniški poziv, ki sprašuje o vremenu v določenem mestu. 
- LLM bo odgovoril s klicem orodja Brave Search, ki bo izgledal tako `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Opomba: Ta primer samo izvrši klic orodja, če želite dobiti rezultate, boste morali ustvariti brezplačen račun na strani Brave API in definirati funkcijo samo.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Čeprav je LLM, je ena omejitev Llama 3.1 pomanjkanje multimodalnosti. To pomeni, da ne more uporabiti različnih vrst vhodov, kot so slike kot pozivi, in ponuditi odgovore. Ta sposobnost je ena glavnih lastnosti Llama 3.2. Te lastnosti vključujejo tudi: 

- Multimodalnost - ima sposobnost oceniti tako besedilne kot slikovne pozive 
- Različice majhne do srednje velikosti (11B in 90B) - to ponuja fleksibilne možnosti namestitve, 
- Samo besedilne različice (1B in 3B) - to omogoča namestitev modela na robne / mobilne naprave in ponuja nizko zakasnitev 

Podpora multimodalnosti predstavlja velik korak v svetu odprtokodnih modelov. Spodnji primer kode sprejme tako sliko kot besedilni poziv za analizo slike. Ker je Llama 3.2 90B Vision Instruct ukinjen, primer uporablja `Llama-4-Scout-17B-16E-Instruct`, trenutno razpoložljivo nativno multimodalno alternativo. 


### Podpora multimodalnosti z Llama 3.2

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Učenje se tukaj ne ustavi, nadaljujte potovanje

Po končani tej lekciji si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o ustvarjalni umetni inteligenci!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->