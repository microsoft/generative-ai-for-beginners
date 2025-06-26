<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:36:40+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sl"
}
-->
# Gradnja z modeli Meta družine

## Uvod

Ta lekcija bo zajemala:

- Raziskovanje dveh glavnih modelov Meta družine - Llama 3.1 in Llama 3.2
- Razumevanje primerov uporabe in scenarijev za vsak model
- Vzorec kode za prikaz edinstvenih lastnosti vsakega modela

## Meta družina modelov

V tej lekciji bomo raziskali 2 modela iz Meta družine ali "Llama črede" - Llama 3.1 in Llama 3.2

Ti modeli so na voljo v različnih različicah in so dostopni na tržnici modelov GitHub. Tukaj so dodatne informacije o uporabi GitHub modelov za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Različice modelov:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Opomba: Llama 3 je prav tako na voljo na GitHub Models, vendar ne bo zajeta v tej lekciji*

## Llama 3.1

Z 405 milijardami parametrov se Llama 3.1 uvršča v kategorijo odprtokodnih LLM.

Model je nadgradnja prejšnje izdaje Llama 3 z izboljšavami:

- Večje kontekstno okno - 128k tokenov v primerjavi z 8k tokeni
- Večji maksimalni izhodni tokeni - 4096 v primerjavi z 2048
- Boljša podpora za več jezikov - zaradi povečanja števila učnih tokenov

To omogoča Llama 3.1, da obravnava bolj zapletene primere uporabe pri gradnji GenAI aplikacij, vključno z:
- Klicanje funkcij - sposobnost klicanja zunanjih orodij in funkcij zunaj delovnega toka LLM
- Boljša RAG zmogljivost - zaradi večjega kontekstnega okna
- Sintetično generiranje podatkov - sposobnost ustvarjanja učinkovitih podatkov za naloge, kot je fino nastavljanje

### Klicanje funkcij

Llama 3.1 je bila fino nastavljena, da je bolj učinkovita pri klicanju funkcij ali orodij. Ima tudi dve vgrajeni orodji, ki jih model lahko prepozna kot potrebna za uporabo glede na poziv uporabnika. Ta orodja so:

- **Brave Search** - Lahko se uporablja za pridobivanje najnovejših informacij, kot je vreme, z izvajanjem spletnega iskanja
- **Wolfram Alpha** - Lahko se uporablja za bolj zapletene matematične izračune, tako da pisanje lastnih funkcij ni potrebno.

Prav tako lahko ustvarite svoja prilagojena orodja, ki jih lahko LLM pokliče.

V spodnjem primeru kode:

- Določimo razpoložljiva orodja (brave_search, wolfram_alpha) v sistemskem pozivu.
- Pošljemo uporabniški poziv, ki sprašuje o vremenu v določenem mestu.
- LLM bo odgovoril s klicem orodja Brave Search, ki bo izgledal takole `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Opomba: Ta primer naredi le klic orodja, če želite dobiti rezultate, boste morali ustvariti brezplačen račun na strani Brave API in definirati funkcijo sami*

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

Kljub temu, da je LLM, ima Llama 3.1 eno omejitev, to je multimodalnost. To pomeni, da lahko uporablja različne vrste vhodov, kot so slike kot pozivi in zagotavlja odgovore. Ta sposobnost je ena glavnih značilnosti Llama 3.2. Te značilnosti vključujejo tudi:

- Multimodalnost - ima sposobnost ocenjevanja tako besedilnih kot slikovnih pozivov
- Različice majhne do srednje velikosti (11B in 90B) - to omogoča prilagodljive možnosti implementacije,
- Samo besedilne različice (1B in 3B) - to omogoča modelu, da se izvaja na robnih/mobilnih napravah in zagotavlja nizko zakasnitev

Podpora za multimodalnost predstavlja velik korak v svetu odprtokodnih modelov. Spodnji primer kode uporablja tako slikovni kot besedilni poziv za pridobitev analize slike iz Llama 3.2 90B.

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

## Učenje se tukaj ne konča, nadaljujte svojo pot

Po zaključku te lekcije si oglejte našo [Zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.