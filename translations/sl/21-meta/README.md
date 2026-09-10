# Gradnja z modeli Meta družine 

## Uvod 

Ta lekcija bo obravnavala: 

- Raziskovanje dveh glavnih Meta družinskih modelov - Llama 3.1 in Llama 3.2 
- Razumevanje primerov uporabe in scenarijev za vsak model 
- Primer kode, ki prikazuje edinstvene lastnosti vsakega modela 


## Meta družina modelov 

V tej lekciji bomo raziskali 2 modela iz Meta družine ali "Llama črede" - Llama 3.1 in Llama 3.2.

Ti modeli so na voljo v različnih različicah in so na voljo v [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Opomba:** GitHub modeli se bodo prenehali uporabljati konec julija 2026. Tukaj so podrobnosti o uporabi [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiranje z AI modeli.

Različice modelov: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Opomba: Llama 3 je na voljo tudi v Microsoft Foundry Models, a ne bo obravnavan v tej lekciji*

## Llama 3.1 

Z 405 milijardami parametrov spada Llama 3.1 v kategorijo odprtokodnih velikih jezikovnih modelov. 

Model je nadgradnja prej izdanega Llama 3 z izboljšavami: 

- Večje kontekstno okno - 128k tokenov v primerjavi z 8k tokeni 
- Večje največje število izhodnih tokenov - 4096 v primerjavi z 2048 
- Boljša večjezična podpora - zaradi povečanja števila učnih tokenov 

To omogoča Llama 3.1, da obravnava bolj kompleksne primere uporabe pri gradnji GenAI aplikacij, vključno z: 
- Nativno klicanje funkcij - možnost klicanja zunanjih orodij in funkcij zunaj delovnega toka LLM
- Boljšimi RAG zmogljivostmi - zaradi večjega kontekstnega okna 
- Generiranjem sintetičnih podatkov - možnost ustvarjanja učinkovitih podatkov za naloge, kot je fino prilagajanje 

### Nativno klicanje funkcij 

Llama 3.1 je fino prilagojen, da je učinkovitejši pri klicanju funkcij ali orodij. Ima tudi dve vgrajeni orodji, ki jih model lahko prepozna kot potrebni uporabi glede na uporabniški poziv. Ti orodji sta: 

- **Brave Search** - lahko se uporablja za pridobitev aktualnih informacij, kot je vreme, s spletnim iskanjem 
- **Wolfram Alpha** - lahko se uporablja za kompleksnejše matematične izračune, tako da ni potrebno pisati lastnih funkcij. 

Prav tako lahko ustvarite lastna prilagojena orodja, ki jih lahko LLM kliče. 

V spodnjem primer kode: 

- Določimo na voljo orodji (brave_search, wolfram_alpha) v sistemskem pozivu. 
- Pošljemo uporabniški poziv, ki sprašuje o vremenu v določenem mestu. 
- LLM bo odgovoril s klicem orodja Brave Search, ki bo izgledal takole `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Opomba: Ta primer samo naredi klic orodja, če želite dobiti rezultate, boste morali ustvariti brezplačen račun na strani Brave API in definirati funkcijo samega klica.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Pridobite jih s strani "Pregled" vašega Microsoft Foundry projekta
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

Kljub temu, da je LLM, je ena omejitev Llama 3.1 njegova pomanjkljivost multimodalnosti. To pomeni, da ni sposoben uporabljati različnih vrst vhodov, kot so slike za pozive in podajati odgovore. Ta sposobnost je ena glavnih lastnosti Llama 3.2. Te lastnosti vključujejo tudi: 

- Multimodalnost - ima sposobnost ocene tako besedilnih kot slikovnih pozivov 
- Majhne do srednje velikosti različice (11B in 90B) - to nudi fleksibilne možnosti namestitve, 
- Samo besedilne različice (1B in 3B) - to omogoča namestitev modela na edge / mobilne naprave in zagotavlja nizko zakasnitev 

Podpora multimodalnosti predstavlja velik korak v svetu odprtokodnih modelov. Spodnji primer kode uporabi tako sliko kot besedilni poziv za pridobitev analize slike iz Llama 3.2 90B. 


### Multimodalna podpora z Llama 3.2

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

# Pridobite jih na strani "Pregled" vašega projekta Microsoft Foundry
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

## Učenje se tukaj ne ustavi, nadaljujte pot

Po zaključku te lekcije si oglejte našo [Zbirko za učenje Generativne umetne inteligence](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete nadgrajevanje svojega znanja o Generativni umetni inteligenci!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->