# Izgradnja s Meta obiteljskim modelima 

## Uvod 

Ova lekcija će obuhvatiti: 

- Istraživanje dva glavna Meta obiteljska modela - Llama 3.1 i Llama 3.2 
- Razumijevanje slučajeva upotrebe i scenarija za svaki model 
- Primjer koda za prikaz jedinstvenih značajki svakog modela 


## Meta obitelj modela 

U ovoj lekciji istražit ćemo 2 modela iz Meta obitelji ili "Llama stada" - Llama 3.1 i Llama 3.2.

Ovi modeli dolaze u različitim varijantama i dostupni su u [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Napomena:** GitHub Models se ukida krajem srpnja 2026. Više detalja o korištenju [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiziranje s AI modelima potražite ovdje.

Varijante modela: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Napomena: Llama 3 je također dostupna u Microsoft Foundry Models, ali neće biti obrađena u ovoj lekciji*

## Llama 3.1 

S 405 milijardi parametara, Llama 3.1 spada u kategoriju otvorenih LLM modela. 

Model je nadogradnja ranijeg izdanja Llama 3, nudeći: 

- Veći kontekstni prozor - 128k tokena naspram 8k tokena 
- Veći maksimalni broj izlaznih tokena - 4096 naspram 2048 
- Bolja višeslojna podrška - zbog povećanja broja tokena za treniranje 

Ovo omogućava Llama 3.1 da se nosi s kompleksnijim slučajevima upotrebe pri izgradnji GenAI aplikacija uključujući: 
- Izvorni pozivi funkcija - mogućnost korištenja vanjskih alata i funkcija izvan LLM toka rada
- Bolja RAG izvedba - zbog većeg kontekstnog prozora 
- Generiranje sintetičkih podataka - mogućnost stvaranja učinkovitih podataka za zadatke poput fino podešavanja 

### Izvorni pozivi funkcija 

Llama 3.1 je fino podešen da bude učinkovitiji u pozivanju funkcija ili alata. Također ima dva ugrađena alata koje model može prepoznati kao potrebne za upotrebu temeljem korisničkog upita. Ti alati su: 

- **Brave Search** - može se koristiti za dobivanje ažurnih informacija poput vremenske prognoze putem pretraživanja na webu 
- **Wolfram Alpha** - može se koristiti za složenije matematičke izračune, pa nije potrebno pisati vlastite funkcije. 

Također možete kreirati vlastite prilagođene alate koje LLM može pozivati. 

U sljedećem primjeru koda: 

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskom promptu. 
- Šaljemo korisnički upit koji pita o vremenu u određenom gradu. 
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Napomena: Ovaj primjer samo poziva alat, ako želite dobiti rezultate, morat ćete kreirati besplatan račun na Brave API stranici i definirati samu funkciju.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Nabavite ih s vaše stranice "Pregled" Microsoft Foundry projekta
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Unatoč tome što je LLM, jedna od ograničenja Llama 3.1 je nedostatak multimodalnosti. To jest, nemogućnost korištenja različitih vrsta ulaza poput slika kao prompta i pružanja odgovora. Ova sposobnost je jedna od glavnih značajki Llama 3.2. Ostale značajke uključuju: 

- Multimodalnost - može evaluirati i tekst i slike kao promptove 
- Varijante male do srednje veličine (11B i 90B) - što pruža fleksibilne mogućnosti implementacije, 
- Tekstualne varijante (1B i 3B) - omogućavaju implementaciju na edge / mobilne uređaje i pružaju nisku latenciju 

Podrška za multimodalnost predstavlja veliki iskorak u svijetu modela otvorenog koda. Sljedeći primjer koda prima i sliku i tekstualni prompt za analizu slike iz Llama 3.2 90B. 


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

# Preuzmite ih s vaše Microsoft Foundry projekta stranice "Pregled"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## Učenje se ne zaustavlja ovdje, nastavi putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite nadograđivati svoje znanje o Generativnoj umjetnoj inteligenciji!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->