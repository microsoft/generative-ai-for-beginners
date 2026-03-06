# Izgradnja s Meta obiteljskim modelima

## Uvod

Ova lekcija će obuhvatiti:

- Istraživanje dva glavna Meta obiteljska modela - Llama 3.1 i Llama 3.2
- Razumijevanje upotrebe i scenarija za svaki model
- Primjer koda koji prikazuje jedinstvene značajke svakog modela

## Meta obitelj modela

U ovoj lekciji istražit ćemo 2 modela iz Meta obitelji ili "Llama čopora" - Llama 3.1 i Llama 3.2.

Ovi modeli dolaze u različitim varijantama i dostupni su na GitHub Model marketplaceu. Evo više detalja o korištenju GitHub modela za [prototipiranje s AI modelima](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varijante modela:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Napomena: Llama 3 je također dostupan na GitHub modelima, ali neće biti obrađen u ovoj lekciji*

## Llama 3.1

S 405 milijardi parametara, Llama 3.1 spada u kategoriju otvorenih LLM modela.

Model je nadogradnja ranijeg izdanja Llama 3 pružajući:

- Veće kontekstno prozorsko razdoblje - 128k tokena naspram 8k tokena
- Veći maksimalni broj izlaznih tokena - 4096 naspram 2048
- Bolju podršku za više jezika - zbog povećanja broja trening tokena

Ovo omogućuje Llama 3.1 da se nosi s kompleksnijim slučajevima upotrebe pri izgradnji GenAI aplikacija uključujući:
- Native Function Calling - sposobnost pozivanja vanjskih alata i funkcija izvan LLM tijeka
- Bolje performanse u RAG-u - zbog većeg kontekstnog prozora
- Generiranje sintetičkih podataka - sposobnost stvaranja efikasnih podataka za zadatke poput finog podešavanja

### Native Function Calling

Llama 3.1 je dodatno fino podešen da bude učinkovitiji u pozivima funkcija ili alata. Također ima dva ugrađena alata koja model može prepoznati kao potrebna za korištenje na temelju upita od korisnika. Ti alati su:

- **Brave Search** - može se koristiti za dobivanje ažurnih informacija poput vremenske prognoze putem web pretraživanja
- **Wolfram Alpha** - može se koristiti za složenije matematičke izračune pa nije potrebno pisati vlastite funkcije

Također možete kreirati vlastite prilagođene alate koje LLM može pozivati.

U primjeru koda ispod:

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskom promptu.
- Šaljemo korisnički upit koji traži informacije o vremenu u određenom gradu.
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Napomena: Ovaj primjer samo izvršava poziv alata, ako želite dobiti rezultate, morate kreirati besplatan račun na Brave API stranici i definirati samu funkciju.

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

Iako je LLM, jedna ograničenost Llama 3.1 je nedostatak multimodalnosti. To jest, nemogućnost korištenja različitih vrsta ulaza poput slika kao prompta i davanja odgovora. Ova sposobnost je jedna od glavnih značajki Llama 3.2. Te značajke također uključuju:

- Multimodalnost - sposobnost evaluacije tekstualnih i slikovnih prompta
- Varijacije male do srednje veličine (11B i 90B) - pružaju fleksibilne opcije implementacije,
- Varijacije samo za tekst (1B i 3B) - omogućavaju implementaciju na rubnim/mobilnim uređajima i pružaju nisku latenciju

Podrška za multimodalnost predstavlja veliki korak u svijetu otvorenih modela. Primjer koda ispod prima i sliku i tekstualni prompt za dobivanje analize slike od Llama 3.2 90B.

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

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju učenja Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili usavršavati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju odgovornosti**:
Ovaj dokument preveden je pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i važećim. Za važne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za eventualna nesporazuma ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->