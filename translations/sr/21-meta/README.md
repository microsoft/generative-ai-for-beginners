<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:16:44+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "sr"
}
-->
# Izgradnja sa Meta porodicom modela

## Uvod

Ova lekcija će pokriti:

- Istraživanje dva glavna modela iz Meta porodice - Llama 3.1 i Llama 3.2
- Razumevanje upotrebe i scenarija za svaki model
- Primer koda koji pokazuje jedinstvene karakteristike svakog modela

## Meta porodica modela

U ovoj lekciji ćemo istražiti 2 modela iz Meta porodice ili "Llama stada" - Llama 3.1 i Llama 3.2

Ovi modeli dolaze u različitim varijantama i dostupni su na GitHub Model tržištu. Ovde su dodatne informacije o korišćenju GitHub Modela za [prototipiranje sa AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varijante modela:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Napomena: Llama 3 je takođe dostupna na GitHub Modelima, ali neće biti pokrivena u ovoj lekciji*

## Llama 3.1

Sa 405 milijardi parametara, Llama 3.1 spada u kategoriju open source LLM.

Model je unapređenje ranijeg izdanja Llama 3 i nudi:

- Veći kontekstualni prozor - 128k tokena naspram 8k tokena
- Veći maksimalni izlazni tokeni - 4096 naspram 2048
- Bolja podrška za više jezika - zbog povećanja broja trening tokena

Ovo omogućava Llama 3.1 da se nosi sa složenijim slučajevima upotrebe pri izradi GenAI aplikacija, uključujući:
- Pozivanje nativnih funkcija - sposobnost pozivanja eksternih alata i funkcija izvan LLM radnog toka
- Bolje RAG performanse - zbog većeg kontekstualnog prozora
- Generisanje sintetičkih podataka - sposobnost kreiranja efektivnih podataka za zadatke kao što je fino podešavanje

### Pozivanje nativnih funkcija

Llama 3.1 je fino podešena da bude efikasnija u pravljenju poziva funkcija ili alata. Takođe ima dva ugrađena alata koje model može prepoznati kao potrebne za korišćenje na osnovu korisničkog zahteva. Ovi alati su:

- **Brave Search** - Može se koristiti za dobijanje najnovijih informacija kao što je vreme putem web pretrage
- **Wolfram Alpha** - Može se koristiti za složenije matematičke proračune, tako da pisanje sopstvenih funkcija nije potrebno.

Takođe možete kreirati sopstvene prilagođene alate koje LLM može pozvati.

U sledećem primeru koda:

- Definišemo dostupne alate (brave_search, wolfram_alpha) u sistemskom zahtevu.
- Šaljemo korisnički zahtev koji pita o vremenu u određenom gradu.
- LLM će odgovoriti pozivom alata Brave Search, koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Napomena: Ovaj primer samo pravi poziv alata, ako želite da dobijete rezultate, potrebno je da kreirate besplatan nalog na Brave API stranici i definišete samu funkciju*

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

Iako je LLM, jedno ograničenje koje Llama 3.1 ima je multimodalnost. To jest, sposobnost korišćenja različitih tipova ulaza kao što su slike kao zahtevi i pružanje odgovora. Ova sposobnost je jedna od glavnih karakteristika Llama 3.2. Ove karakteristike takođe uključuju:

- Multimodalnost - ima sposobnost evaluacije i tekstualnih i slikovnih zahteva
- Varijacije male do srednje veličine (11B i 90B) - ovo pruža fleksibilne opcije za implementaciju,
- Varijacije samo za tekst (1B i 3B) - ovo omogućava modelu da bude implementiran na edge/mobilnim uređajima i pruža nisku latenciju

Podrška za multimodalnost predstavlja veliki korak u svetu open source modela. Sledeći primer koda uzima i slikovni i tekstualni zahtev kako bi dobio analizu slike od Llama 3.2 90B.

### Multimodalna podrška sa Llama 3.2

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

## Učenje se ne završava ovde, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite sa usavršavanjem svog znanja o generativnoj AI!

**Одрицање од одговорности**:  
Овај документ је преведен користећи AI услугу превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални људски превод. Не преузимамо одговорност за било каква неспоразума или погрешна тумачења која проистичу из употребе овог превода.