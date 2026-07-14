# Gradnja s modeli družine Meta  

## Uvod  

Ta lekcija bo zajemala:  

- Raziskovanje dveh glavnih modelov družine Meta - Llama 3.1 in Llama 3.2  
- Razumevanje primerov uporabe in scenarijev za vsak model  
- Vzorec kode za prikaz edinstvenih lastnosti vsakega modela  


## Družina modelov Meta  

V tej lekciji bomo raziskali 2 modela iz družine Meta ali "Llama Herd" - Llama 3.1 in Llama 3.2.  

Ti modeli so na voljo v različnih različicah v [katalogu Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).  

> **Opomba:** GitHub Models bo upokojil konec julija 2026. Tukaj so podrobnosti o uporabi [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiranje z AI modeli.  

Različice modelov:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Opomba: Llama 3 je prav tako na voljo v Microsoft Foundry Models, vendar v tej lekciji ne bo obravnavana*  

## Llama 3.1  

Pri 405 milijardah parametrov Llama 3.1 spada v kategorijo odprtokodnih velikih jezikovnih modelov (LLM).  

Model je nadgradnja prejšnje različice Llama 3, ki ponuja:  

- Večje kontekstno okno - 128k tokenov v primerjavi z 8k tokeni  
- Višjo maksimalno dolžino izhoda - 4096 v primerjavi z 2048  
- Boljšo podporo več jezikom - zaradi povečanja števila učnih tokenov  

To omogoča Llama 3.1, da obvladuje bolj kompleksne primere uporabe pri gradnji aplikacij generativne umetne inteligence, vključno z:  
- Nativno klicanje funkcij - zmožnost klicanja zunanjih orodij in funkcij zunaj delovnega toka LLM  
- Boljšo učinkovitost RAG - zaradi večjega kontekstnega okna  
- Generiranje sintetičnih podatkov - možnost ustvarjanja učinkovitih podatkov za naloge, kot je dodatno učenje (fine-tuning)  

### Nativno klicanje funkcij  

Llama 3.1 je bilo dodatno prilagojeno za bolj učinkovito klicanje funkcij ali orodij. Prav tako ima vgrajeni dve orodji, ki jih model lahko prepozna, da jih treba uporabiti na podlagi poziva uporabnika. Ta orodja sta:  

- **Brave Search** - lahko se uporablja za pridobivanje aktualnih informacij, kot je vreme, z izvajanjem spletnega iskanja  
- **Wolfram Alpha** - lahko se uporablja za bolj kompleksne matematične izračune, tako da ni treba pisati lastnih funkcij.  

Prav tako lahko ustvarite lastna prilagojena orodja, ki jih LLM lahko kliče.  

V spodnjem primeru kode:  

- Definiramo razpoložljiva orodja (brave_search, wolfram_alpha) v sistemskem pozivu.  
- Pošljemo uporabniški poziv, ki vpraša o vremenu v določenem mestu.  
- LLM bo odgovoril s klicem orodja Brave Search, ki bo izgledal tako `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Opomba: Ta primer samo izvede klic orodja, če želite dobiti rezultate, boste morali ustvariti brezplačen račun na strani Brave API in definirati funkcijo samega klica.  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Te pridobite na strani "Pregled" vašega Microsoft Foundry projekta
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

Kljub temu da je LLM, ena izmed omejitev modela Llama 3.1 je njegova pomanjkljiva multimodalnost. To pomeni, da ne more uporabljati različnih vrst vhodnih podatkov, kot so slike za pozive, in zagotavljati odzive. Ta zmožnost je ena izmed glavnih lastnosti Llama 3.2. Te lastnosti vključujejo tudi:  

- Multimodalnost - zmožnost oceniti tako besedilne kot slikovne pozive  
- Majhne do srednje velike različice (11B in 90B) - kar omogoča prilagodljive možnosti uvajanja,  
- Samo besedilne različice (1B in 3B) - kar omogoča uvajanje na robnih / mobilnih napravah in zagotavlja nizko zakasnitev  

Podpora multimodalnosti predstavlja velik korak v svetu odprtokodnih modelov. Spodnji kodni primer uporablja tako sliko kot besedilni poziv za analizo slike z Llama 3.2 90B.  


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

# Pridobite jih iz strani "Pregled" vašega Microsoft Foundry projekta
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

## Učenje tukaj ne preneha, nadaljujte pot  

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadgradite svoje znanje o generativni umetni inteligenci!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->