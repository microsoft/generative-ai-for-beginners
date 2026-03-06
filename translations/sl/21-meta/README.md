# Gradnja z modeli družine Meta

## Uvod

Ta lekcija bo zajemala:

- Raziskovanje dveh glavnih modelov družine Meta - Llama 3.1 in Llama 3.2
- Razumevanje primerov uporabe in scenarijev za vsak model
- Kodo, ki prikazuje edinstvene značilnosti vsakega modela

## Družina modelov Meta

V tej lekciji bomo raziskali 2 modela iz družine Meta ali "Llama Herd" - Llama 3.1 in Llama 3.2.

Ti modeli so na voljo v različnih različicah in so dostopni na tržnici GitHub Model. Tukaj so podrobnosti o uporabi GitHub Model za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Različice modela:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Opomba: Llama 3 je prav tako na voljo na GitHub Modelih, vendar v tej lekciji ne bo obravnavan*

## Llama 3.1

S 405 milijard parametrov Llama 3.1 spada v kategorijo odprtokodnih LLM-jev.

Model je nadgradnja prejšnje izdaje Llama 3, saj ponuja:

- Večje okno konteksta - 128k tokenov v primerjavi z 8k tokeni
- Večje maksimalno število izhodnih tokenov - 4096 v primerjavi z 2048
- Boljša večjezična podpora - zaradi povečanega števila učnih tokenov

To omogoča Llama 3.1 obravnavati bolj zapletene primere uporabe pri izdelavi GenAI aplikacij, vključno z:
- Nativno klicanje funkcij - možnost klicanja zunanjih orodij in funkcij izven poteka LLM
- Boljša zmogljivost RAG - zaradi večjega okna konteksta
- Generiranje sintetičnih podatkov - možnost ustvarjanja učinkovitih podatkov za naloge, kot je fino prilagajanje

### Nativno klicanje funkcij

Llama 3.1 je natančno dodelan, da je učinkovitejši pri klicanju funkcij ali orodij. Prav tako ima dve vgrajeni orodji, ki jih model lahko prepozna kot potrebni za uporabo na podlagi poziva uporabnika. Ta orodja sta:

- **Brave Search** - lahko se uporablja za pridobivanje ažurnih informacij, kot je vreme, z izvajanjem spletnega iskanja
- **Wolfram Alpha** - se lahko uporablja za bolj zapletene matematične izračune, zato ni potrebno pisati lastnih funkcij.

Lahko pa ustvarite tudi svoja lastna orodja, ki jih lahko LLM kliče.

V spodnjem primeru kode:

- Določimo razpoložljiva orodja (brave_search, wolfram_alpha) v sistemskem pozivu.
- Pošljemo uporabniški poziv, ki vpraša o vremenu v določenem mestu.
- LLM bo odgovoril s klicem orodja Brave Search, kar bo izgledalo tako: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opomba: Ta primer samo izvede klic orodja, če želite dobiti rezultate, morate ustvariti brezplačen račun na strani Brave API in definirati funkcijo samega klica.

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

Kljub temu da je LLM, ena omejitev Llama 3.1 je njena nezmožnost multimodalnosti. To pomeni, da ne zmore uporabljati različnih vrst vhodov, kot so slike kot pozivi, in zagotoviti odzive. Ta zmogljivost je ena glavnih funkcij Llama 3.2. Te funkcije vključujejo tudi:

- Multimodalnost - zmožnost obdelave tako besedilnih kot slikovnih pozivov
- Majhne do srednje velike različice (11B in 90B) - zagotavljajo fleksibilne možnosti nameščanja,
- Samo besedilne različice (1B in 3B) - omogočajo namestitev na robne / mobilne naprave in zagotavljajo nizko zakasnitev

Podpora multimodalnosti predstavlja velik korak v svetu odprtokodnih modelov. Spodnji primer kode prejme tako sliko kot besedilni poziv za analizo slike z Llama 3.2 90B.

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

## Učenje tukaj ne konča, nadaljujte pot

Po zaključku te lekcije si oglejte našo [kolekcijo učenja generativne umetne inteligence](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgrajevanjem vašega znanja generativne umetne inteligence!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovi izvorni jezikovni različici je treba šteti za avtoritativni vir. Za kritične informacije priporočamo strokovni prevod s strani človeka. Nismo odgovorni za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->