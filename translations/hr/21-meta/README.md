<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:17:06+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hr"
}
-->
# Izgradnja s Meta obiteljskim modelima

## Uvod

Ova lekcija pokriva:

- Istraživanje dva glavna Meta obiteljska modela - Llama 3.1 i Llama 3.2
- Razumijevanje primjena i scenarija za svaki model
- Primjer koda koji pokazuje jedinstvene značajke svakog modela

## Meta obitelj modela

U ovoj lekciji istražit ćemo 2 modela iz Meta obitelji ili "Llama krda" - Llama 3.1 i Llama 3.2

Ovi modeli dolaze u različitim varijantama i dostupni su na GitHub Model marketplaceu. Ovdje su dodatni detalji o korištenju GitHub modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varijante modela:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Napomena: Llama 3 je također dostupna na GitHub modelima, ali neće biti pokrivena u ovoj lekciji*

## Llama 3.1

S 405 milijardi parametara, Llama 3.1 spada u kategoriju otvorenog izvora LLM.

Model je nadogradnja na raniju verziju Llama 3, nudeći:

- Veći kontekstualni prozor - 128k tokena naspram 8k tokena
- Veći maksimalni izlazni tokeni - 4096 naspram 2048
- Bolja podrška za više jezika - zbog povećanja broja trening tokena

To omogućuje Llama 3.1 da se nosi s kompleksnijim slučajevima korištenja pri izgradnji GenAI aplikacija, uključujući:
- Pozivanje nativnih funkcija - sposobnost pozivanja vanjskih alata i funkcija izvan LLM tijeka rada
- Bolja RAG izvedba - zbog većeg kontekstualnog prozora
- Generiranje sintetičkih podataka - sposobnost stvaranja učinkovitih podataka za zadatke kao što je fino podešavanje

### Pozivanje nativnih funkcija

Llama 3.1 je fino podešena da bude učinkovitija u pozivanju funkcija ili alata. Također ima dva ugrađena alata koje model može prepoznati kao potrebne za korištenje na temelju korisničkog upita. Ti alati su:

- **Brave Search** - Može se koristiti za dobivanje ažurnih informacija poput vremenske prognoze putem web pretraživanja
- **Wolfram Alpha** - Može se koristiti za složenije matematičke izračune, tako da nije potrebno pisati vlastite funkcije.

Također možete stvoriti vlastite prilagođene alate koje LLM može pozivati.

U primjeru koda dolje:

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskom upitu.
- Šaljemo korisnički upit koji pita o vremenu u određenom gradu.
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Napomena: Ovaj primjer samo poziva alat, ako želite dobiti rezultate, trebate stvoriti besplatan račun na Brave API stranici i definirati samu funkciju`

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

Unatoč tome što je LLM, jedno ograničenje koje Llama 3.1 ima je multimodalnost. To jest, sposobnost korištenja različitih vrsta ulaza, kao što su slike, kao upiti i davanje odgovora. Ova sposobnost je jedna od glavnih značajki Llama 3.2. Te značajke također uključuju:

- Multimodalnost - ima sposobnost evaluacije tekstualnih i slikovnih upita
- Varijacije malih do srednjih veličina (11B i 90B) - to pruža fleksibilne opcije implementacije,
- Varijacije samo za tekst (1B i 3B) - to omogućuje modelu da se implementira na rubnim / mobilnim uređajima i pruža nisku latenciju

Podrška za multimodalnost predstavlja veliki korak u svijetu modela otvorenog izvora. Primjer koda dolje uzima i slikovni i tekstualni upit za dobivanje analize slike iz Llama 3.2 90B.

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

## Učenje ne završava ovdje, nastavi putovanje

Nakon završetka ove lekcije, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generative AI!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo da prevod bude tačan, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne odgovaramo za bilo kakva nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.