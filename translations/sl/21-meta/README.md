<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:17:20+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sl"
}
-->
# Gradnja z modeli Meta Family

## Uvod

Ta lekcija bo obravnavala:

- Raziskovanje dveh glavnih modelov Meta družine - Llama 3.1 in Llama 3.2
- Razumevanje primerov uporabe in scenarijev za vsak model
- Primer kode za prikaz edinstvenih značilnosti vsakega modela

## Meta Family modeli

V tej lekciji bomo raziskali 2 modela iz Meta družine ali "Llama Herd" - Llama 3.1 in Llama 3.2

Ti modeli so na voljo v različnih različicah in so na voljo na GitHub Model marketplace. Tukaj so podrobnosti o uporabi GitHub Modelov za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Različice modelov:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Opomba: Llama 3 je prav tako na voljo na GitHub Modelih, vendar ne bo obravnavan v tej lekciji*

## Llama 3.1

Z 405 milijardami parametrov se Llama 3.1 uvršča v kategorijo odprtokodnih LLM.

Model je nadgradnja prejšnje izdaje Llama 3 z naslednjimi izboljšavami:

- Večje kontekstno okno - 128k žetonov v primerjavi z 8k žetoni
- Večji največji izhodni žetoni - 4096 v primerjavi z 2048
- Boljša večjezična podpora - zaradi povečanja števila učnih žetonov

To omogoča Llama 3.1, da obravnava bolj kompleksne primere uporabe pri gradnji GenAI aplikacij, vključno z:
- Klicanje funkcij - sposobnost klicanja zunanjih orodij in funkcij zunaj delovnega toka LLM
- Boljša RAG zmogljivost - zaradi večjega kontekstnega okna
- Generiranje sintetičnih podatkov - sposobnost ustvarjanja učinkovitih podatkov za naloge, kot je fino prilagajanje

### Klicanje funkcij

Llama 3.1 je bila fino prilagojena, da je bolj učinkovita pri klicanju funkcij ali orodij. Prav tako ima dva vgrajena orodja, ki jih model lahko identificira kot potrebna glede na zahtevo uporabnika. Ta orodja so:

- **Brave Search** - Uporablja se za pridobivanje aktualnih informacij, kot je vreme, z izvajanjem spletnega iskanja
- **Wolfram Alpha** - Uporablja se za bolj kompleksne matematične izračune, tako da pisanje lastnih funkcij ni potrebno.

Prav tako lahko ustvarite svoja lastna orodja, ki jih LLM lahko kliče.

V spodnjem primeru kode:

- Določimo razpoložljiva orodja (brave_search, wolfram_alpha) v sistemski zahtevi.
- Pošljemo uporabniško zahtevo, ki sprašuje o vremenu v določenem mestu.
- LLM bo odgovoril z klicem orodja Brave Search, ki bo videti takole `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opomba: Ta primer le kliče orodje, če želite pridobiti rezultate, boste morali ustvariti brezplačen račun na strani Brave API in določiti samo funkcijo*

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

Kljub temu, da je LLM, ima Llama 3.1 eno omejitev, in sicer multimodalnost. To pomeni, da ne more uporabljati različnih vrst vhodnih podatkov, kot so slike, kot zahteve in podajati odgovore. Ta sposobnost je ena glavnih značilnosti Llama 3.2. Te značilnosti vključujejo:

- Multimodalnost - ima sposobnost ocenjevanja tako besedilnih kot slikovnih zahtev
- Različice majhne do srednje velikosti (11B in 90B) - to omogoča prilagodljive možnosti uporabe
- Različice samo za besedilo (1B in 3B) - to omogoča uporabo modela na robnih / mobilnih napravah in zagotavlja nizko zakasnitev

Podpora za multimodalnost predstavlja velik korak v svetu odprtokodnih modelov. Spodnji primer kode uporablja tako slikovno kot besedilno zahtevo za pridobitev analize slike iz Llama 3.2 90B.

### Podpora za multimodalnost z Llama 3.2

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

## Učenje se tukaj ne konča, nadaljujte pot

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo vašega znanja o Generative AI!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.