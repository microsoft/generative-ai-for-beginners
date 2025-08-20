<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:13:47+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hr"
}
-->
# Izgradnja s Meta obiteljskim modelima

## Uvod

Ova lekcija će obuhvatiti:

- Istraživanje dva glavna Meta obiteljska modela - Llama 3.1 i Llama 3.2  
- Razumijevanje primjena i scenarija za svaki model  
- Primjer koda koji prikazuje jedinstvene značajke svakog modela  

## Meta obitelj modela

U ovoj lekciji istražit ćemo 2 modela iz Meta obitelji ili "Llama stada" - Llama 3.1 i Llama 3.2

Ovi modeli dolaze u različitim varijantama i dostupni su na GitHub Model marketplaceu. Više detalja o korištenju GitHub modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varijante modela:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Napomena: Llama 3 je također dostupan na GitHub modelima, ali neće biti obrađen u ovoj lekciji*

## Llama 3.1

S 405 milijardi parametara, Llama 3.1 spada u kategoriju open source LLM modela.

Ovaj model je nadogradnja ranijeg izdanja Llama 3 i donosi:

- Veći kontekstni prozor - 128k tokena naspram 8k tokena  
- Veći maksimalni broj izlaznih tokena - 4096 naspram 2048  
- Bolju podršku za više jezika - zahvaljujući povećanom broju tokena u treningu  

Ove značajke omogućuju Llama 3.1 da se nosi s kompleksnijim slučajevima upotrebe prilikom izgradnje GenAI aplikacija, uključujući:  
- Native Function Calling - mogućnost pozivanja vanjskih alata i funkcija izvan LLM tijeka rada  
- Bolju RAG izvedbu - zahvaljujući većem kontekstnom prozoru  
- Generiranje sintetičkih podataka - sposobnost stvaranja učinkovitih podataka za zadatke poput fino podešavanja  

### Native Function Calling

Llama 3.1 je fino podešen da bude učinkovitiji u pozivanju funkcija ili alata. Također ima dva ugrađena alata koje model može prepoznati kao potrebne za korištenje na temelju korisničkog upita. Ti alati su:

- **Brave Search** - može se koristiti za dobivanje ažurnih informacija poput vremenske prognoze putem web pretraživanja  
- **Wolfram Alpha** - može se koristiti za složenije matematičke izračune, pa nije potrebno pisati vlastite funkcije  

Također možete kreirati vlastite prilagođene alate koje LLM može pozivati.

U donjem primjeru koda:

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskom promptu.  
- Šaljemo korisnički upit koji pita za vremensku prognozu u određenom gradu.  
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Napomena: Ovaj primjer samo poziva alat, ako želite dobiti rezultate, potrebno je kreirati besplatan račun na Brave API stranici i definirati samu funkciju*

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

Iako je LLM, jedna od ograničenja Llama 3.1 je multimodalnost, odnosno mogućnost korištenja različitih vrsta ulaza poput slika kao prompta i pružanja odgovora. Ta sposobnost jedna je od glavnih značajki Llama 3.2. Ostale značajke uključuju:

- Multimodalnost - sposobnost evaluacije i tekstualnih i slikovnih prompta  
- Varijante male i srednje veličine (11B i 90B) - pružaju fleksibilne opcije za implementaciju  
- Varijante samo za tekst (1B i 3B) - omogućuju implementaciju na edge/mobilnim uređajima s niskom latencijom  

Podrška za multimodalnost predstavlja veliki iskorak u svijetu open source modela. Donji primjer koda koristi i sliku i tekstualni prompt za dobivanje analize slike od Llama 3.2 90B.

### Multimodalna podrška s Llama 3.2

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

## Učenje ne prestaje ovdje, nastavi putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) i nastavite podizati svoje znanje o Generativnoj AI!

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.