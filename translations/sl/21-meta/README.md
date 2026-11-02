# Gradnja z Meta družinskimi modeli 

## Uvod 

Ta lekcija bo zajemala: 

- Pregled dveh glavnih Meta družinskih modelov - Llama 3.1 in Llama 3.2, plus trenutno razpoložljive alternative, uporabljene v primerih kode (Llama 3.3 in Llama 4) 
- Razumevanje primerov uporabe in scenarijev za vsak model 
- Primer kode, ki pokaže edinstvene funkcije vsakega modela 


## Meta družina modelov 

V tej lekciji bomo raziskali 2 modela iz Meta družine ali "črede Llama" - Llama 3.1 in Llama 3.2. Različice primerljive kode uporabljajo Llama 3.3 in Llama 4, ki so trenutno razpoložljive alternative v katalogu Microsoft Foundry Models.

Ti modeli so na voljo v različnih variantah in so dostopni v [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Opomba:** GitHub modeli se upokojijo konec julija 2026. Tukaj so podrobnosti o uporabi [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiranje z AI modeli.

> **Opomba:** Specifične verzije modelov, na katerih je ta lekcija prvotno temeljila (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), so bile medtem upokojene iz Microsoft Foundry Models kataloga. Primeri kode spodaj uporabljajo `Llama-3.3-70B-Instruct` in `Llama-4-Scout-17B-16E-Instruct` kot trenutno razpoložljive alternative v katalogu Microsoft Foundry Models, tako da še vedno delujejo danes.

Variacije modelov (kot so bile prvotno zajete v tej lekciji): 
- Llama 3.1 - 70B Instruct (upokojen) 
- Llama 3.1 - 405B Instruct (upokojen) 
- Llama 3.2 - 11B Vision Instruct (upokojen) 
- Llama 3.2 - 90B Vision Instruct (upokojen) 

Trenutno razpoložljive alternative, uporabljene v primerih kode: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Opomba: Zgoraj obravnavane variante Llama 3 so ohranjene za zgodovinski kontekst in niso več na voljo v Microsoft Foundry Models.*

## Llama 3.1 

Z 405 milijardami parametrov spada Llama 3.1 v kategorijo odprtokodnih LLM. 

Model je nadgradnja prej izdane različice Llama 3 z: 

- Večjim kontekstnim oknom - 128k tokenov proti 8k tokenov 
- Večjo maksimalno dolžino izhodnih tokenov - 4096 proti 2048 
- Boljšo večjezično podporo - zaradi povečanja trening tokenov 

To omogoča Llama 3.1 obravnavo bolj zapletenih primerov uporabe pri gradnji GenAI aplikacij, vključno z: 
- Nativnim klicem funkcij - sposobnost klicanja zunanjih orodij in funkcij izven LLM delovnega toka
- Boljšo zmogljivost RAG - zaradi večjega kontekstnega okna 
- Generiranjem sintetičnih podatkov - sposobnost ustvarjanja učinkovitih podatkov za naloge, kot je fino nastavljanje 

### Nativni klic funkcij 

Llama 3.1 je bolje fino nastavljena za učinkovito izvajanje klicev funkcij ali orodij. Ima tudi dve vgrajeni orodji, ki jih lahko model prepozna kot potrebna za uporabo glede na uporabniški poziv. Ta orodja sta: 

- **Brave Search** - lahko se uporablja za pridobivanje ažurnih informacij, npr. vremenske napovedi z izvedbo spletnega iskanja 
- **Wolfram Alpha** - lahko se uporablja za bolj kompleksne matematične izračune, zato ni treba pisati lastnih funkcij. 

Prav tako lahko ustvarite svoja lastna orodja, ki jih lahko LLM kliče. 

V primeru kode spodaj: 

- Določimo na voljo orodja (brave_search, wolfram_alpha) v sistemskem pozivu. 
- Pošljemo uporabniški poziv, ki vpraša o vremenu v določenem mestu. 
- LLM bo odgovoril s klicem orodja Brave Search, ki bo izgledal tako `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Opomba: Ta primer samo naredi klic orodja, če želite dobiti rezultate, morate ustvariti brezplačen račun na Brave API strani in definirati funkcijo samega klica.

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

Kljub temu, da je LLM, ena pomanjkljivost Llama 3.1 je pomanjkanje multimodalnosti. To pomeni, da ne more uporabljati različnih vrst vhodov, kot so slike kot pozivi in zagotavljati odzivov. Ta zmogljivost je ena glavnih funkcij Llama 3.2. Te funkcije vključujejo tudi: 

- Multimodalnost - ima sposobnost ocenjevanja tako besedilnih kot slikovnih pozivov 
- Majhne do srednje velike različice (11B in 90B) - to omogoča prilagodljive možnosti nameščanja, 
- Samo besedilne različice (1B in 3B) - to omogoča nameščanje modela na robnih / mobilnih napravah in zagotavlja nizko zakasnitev 

Multimodalna podpora predstavlja velik korak v svetu odprtokodnih modelov. Primer kode spodaj uporablja tako sliko kot tekstovni poziv za pridobitev analize slike. Ker je Llama 3.2 90B Vision Instruct upokojen, primer uporablja `Llama-4-Scout-17B-16E-Instruct`, trenutno na voljo nativno multimodalno alternativo. 


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

## Učenje tukaj ne preneha, nadaljujte pot

Po zaključku te lekcije si oglejte našo [kolekcijo učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->