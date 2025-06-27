<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:36:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hr"
}
-->
# Izgradnja s modelima obitelji Meta

## Uvod

Ova lekcija će pokriti:

- Istraživanje dva glavna modela obitelji Meta - Llama 3.1 i Llama 3.2
- Razumijevanje upotrebe i scenarija za svaki model
- Primjer koda koji pokazuje jedinstvene značajke svakog modela

## Obitelj modela Meta

U ovoj lekciji istražit ćemo 2 modela iz obitelji Meta ili "Llama Herd" - Llama 3.1 i Llama 3.2

Ovi modeli dolaze u različitim varijantama i dostupni su na GitHub Model marketplace. Evo više detalja o korištenju GitHub modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varijante modela:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Napomena: Llama 3 je također dostupna na GitHub modelima, ali neće biti pokrivena u ovoj lekciji*

## Llama 3.1

S 405 milijardi parametara, Llama 3.1 spada u kategoriju otvorenog izvora LLM.

Model je nadogradnja na ranije izdanje Llama 3 nudeći:

- Veći kontekstni prozor - 128k tokena naspram 8k tokena
- Veći maksimalni izlazni tokeni - 4096 naspram 2048
- Bolja podrška za više jezika - zbog povećanja broja tokena za obuku

Ovo omogućava Llama 3.1 da se nosi s kompleksnijim slučajevima korištenja pri izgradnji GenAI aplikacija, uključujući:
- Pozivanje nativnih funkcija - sposobnost pozivanja vanjskih alata i funkcija izvan LLM tijeka rada
- Bolja izvedba RAG - zbog većeg kontekstnog prozora
- Generiranje sintetičkih podataka - sposobnost stvaranja učinkovitih podataka za zadatke kao što je fino podešavanje

### Pozivanje nativnih funkcija

Llama 3.1 je fino podešena da bude učinkovitija u pozivanju funkcija ili alata. Također ima dva ugrađena alata koje model može identificirati kao potrebne za korištenje na temelju upita korisnika. Ti alati su:

- **Brave Search** - Može se koristiti za dobivanje ažuriranih informacija poput vremena putem web pretraživanja
- **Wolfram Alpha** - Može se koristiti za složenije matematičke izračune tako da pisanje vlastitih funkcija nije potrebno.

Možete također stvoriti vlastite prilagođene alate koje LLM može pozvati.

U primjeru koda ispod:

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskom upitu.
- Šaljemo korisnički upit koji pita o vremenu u određenom gradu.
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Napomena: Ovaj primjer samo vrši poziv alata, ako želite dobiti rezultate, trebate kreirati besplatan račun na stranici Brave API i definirati samu funkciju`

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

Unatoč tome što je LLM, jedna ograničenja koju Llama 3.1 ima je multimodalnost. To jest, sposobnost korištenja različitih vrsta unosa kao što su slike kao upiti i davanje odgovora. Ova sposobnost je jedna od glavnih značajki Llama 3.2. Te značajke također uključuju:

- Multimodalnost - ima sposobnost procjene i tekstualnih i slikovnih upita
- Male do srednje varijacije veličine (11B i 90B) - ovo pruža fleksibilne opcije implementacije,
- Samo tekstualne varijacije (1B i 3B) - ovo omogućava da se model implementira na rubnim / mobilnim uređajima i pruža nisku latenciju

Podrška za multimodalnost predstavlja veliki korak u svijetu modela otvorenog izvora. Primjer koda ispod uzima i sliku i tekstualni upit kako bi dobio analizu slike iz Llama 3.2 90B.

### Podrška za multimodalnost s Llama 3.2

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

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj AI!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja mogu nastati korištenjem ovog prijevoda.