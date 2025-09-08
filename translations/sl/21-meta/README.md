<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:13:59+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sl"
}
-->
# Gradnja z modeli družine Meta

## Uvod

Ta lekcija bo zajemala:

- Raziskovanje dveh glavnih modelov družine Meta - Llama 3.1 in Llama 3.2  
- Razumevanje primerov uporabe in scenarijev za vsak model  
- Primer kode, ki prikazuje edinstvene lastnosti vsakega modela  

## Družina modelov Meta

V tej lekciji bomo raziskali 2 modela iz družine Meta ali "Llama Herd" - Llama 3.1 in Llama 3.2

Ti modeli so na voljo v različnih različicah in jih najdete na GitHub Model marketplace. Tukaj so podrobnosti o uporabi GitHub Modelov za [prototipiranje z AI modeli](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Različice modelov:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Opomba: Llama 3 je prav tako na voljo na GitHub Modelih, vendar v tej lekciji ne bo obravnavan*

## Llama 3.1

Z 405 milijardami parametrov spada Llama 3.1 v kategorijo odprtokodnih LLM-jev.

Model je nadgradnja prejšnje različice Llama 3 in prinaša:

- Večje kontekstno okno - 128k tokenov v primerjavi z 8k tokeni  
- Večje maksimalno število izhodnih tokenov - 4096 v primerjavi z 2048  
- Boljšo večjezično podporo - zaradi povečanja števila učnih tokenov  

To omogoča Llama 3.1, da obvladuje bolj zahtevne primere uporabe pri gradnji GenAI aplikacij, vključno z:  
- Native Function Calling - možnost klicanja zunanjih orodij in funkcij izven LLM delovnega toka  
- Boljšo RAG zmogljivost - zaradi večjega kontekstnega okna  
- Generiranje sintetičnih podatkov - možnost ustvarjanja učinkovitih podatkov za naloge, kot je fino prilagajanje  

### Native Function Calling

Llama 3.1 je fino prilagojen, da je učinkovitejši pri klicanju funkcij ali orodij. Ima tudi dve vgrajeni orodji, ki jih model prepozna kot potrebni za uporabo glede na uporabniški poziv. Ta orodja sta:

- **Brave Search** - omogoča pridobivanje ažurnih informacij, kot je vreme, z iskanjem po spletu  
- **Wolfram Alpha** - omogoča izvajanje zahtevnejših matematičnih izračunov, zato ni treba pisati lastnih funkcij  

Lahko pa ustvarite tudi svoja lastna orodja, ki jih lahko LLM kliče.

V spodnjem primeru kode:

- Določimo razpoložljiva orodja (brave_search, wolfram_alpha) v sistemskem pozivu.  
- Pošljemo uporabniški poziv, ki sprašuje o vremenu v določenem mestu.  
- LLM bo odgovoril s klicem orodja Brave Search, ki bo izgledal takole `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Opomba: Ta primer samo izvede klic orodja, če želite dobiti rezultate, boste morali ustvariti brezplačen račun na strani Brave API in definirati funkcijo*  

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

Čeprav je LLM, ima Llama 3.1 eno omejitev – multimodalnost. To pomeni, da lahko uporablja različne vrste vhodov, kot so slike kot pozivi, in na njih odgovarja. Ta sposobnost je ena glavnih lastnosti Llama 3.2. Druge lastnosti vključujejo:

- Multimodalnost - zmožnost ocenjevanja tako besedilnih kot slikovnih pozivov  
- Majhne do srednje velike različice (11B in 90B) - kar omogoča prilagodljive možnosti nameščanja  
- Samo besedilne različice (1B in 3B) - omogočajo namestitev na robne/mobilne naprave in zagotavljajo nizko zakasnitev  

Podpora multimodalnosti predstavlja velik korak v svetu odprtokodnih modelov. Spodnji primer kode uporablja tako sliko kot besedilni poziv za analizo slike z Llama 3.2 90B.

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

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o Generativni AI!

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.