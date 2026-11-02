# Rad s Meta obiteljskim modelima 

## Uvod 

Ova lekcija će obraditi: 

- Istraživanje dva glavna Meta obiteljska modela - Llama 3.1 i Llama 3.2, plus trenutno dostupne alternative korištene u primjerima koda (Llama 3.3 i Llama 4) 
- Razumijevanje upotrebe i scenarija za svaki model 
- Primjer koda koji prikazuje jedinstvene značajke svakog modela 


## Meta obitelj modela 

U ovoj lekciji istražujemo 2 modela iz Meta obitelji ili "Llama stada" - Llama 3.1 i Llama 3.2. Izvršni primjeri koda koriste Llama 3.3 i Llama 4, koji su trenutno dostupne alternative u Microsoft Foundry Models katalogu.

Ovi modeli dolaze u različitim varijantama i dostupni su u [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Napomena:** GitHub Models se povlači krajem srpnja 2026. Više detalja o korištenju [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiziranje s AI modelima.

> **Napomena:** Specifične verzije modela za koje je ova lekcija izvorno napisana (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) uklonjene su iz Microsoft Foundry Models kataloga. Primjeri koda dolje koriste `Llama-3.3-70B-Instruct` i `Llama-4-Scout-17B-16E-Instruct` kao trenutno dostupne alternative u Microsoft Foundry Models katalogu, pa još uvijek rade danas.

Varijante modela (kako je izvorno pokriveno u ovoj lekciji): 
- Llama 3.1 - 70B Instruct (povučen) 
- Llama 3.1 - 405B Instruct (povučen) 
- Llama 3.2 - 11B Vision Instruct (povučen) 
- Llama 3.2 - 90B Vision Instruct (povučen) 

Trenutno dostupne alternative korištene u primjerima koda: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Napomena: Gornje varijante Llama 3 zadržane su za povijesni kontekst i više nisu dostupne u Microsoft Foundry Models.*

## Llama 3.1 

Sa 405 milijardi parametara, Llama 3.1 spada u kategoriju otvorenih LLM-ova. 

Model je nadogradnja ranijeg izdanja Llama 3 jer nudi: 

- Veće kontekstno okno - 128k tokena naspram 8k tokena 
- Veći maksimalni broj izlaznih tokena - 4096 naspram 2048 
- Bolju podršku za više jezika - zbog povećanja broja tokena za treniranje 

Ovo omogućuje Llama 3.1 da se nosi sa složenijim slučajevima upotrebe pri izgradnji GenAI aplikacija uključujući: 
- Izvorno pozivanje funkcija - mogućnost poziva vanjskih alata i funkcija izvan LLM toka rada
- Bolje RAG performanse - zahvaljujući većem kontekstnom oknu 
- Generiranje sintetičkih podataka - sposobnost stvaranja učinkovitih podataka za zadatke poput fino podešavanja 

### Izvorno pozivanje funkcija 

Llama 3.1 je fino podešen da bude učinkovitiji u pozivanju funkcija ili alata. Također ima dva ugrađena alata koje model može prepoznati kao potrebne za korištenje na temelju korisničkog upita. Ti alati su: 

- **Brave Search** - Može se koristiti za dobivanje ažuriranih informacija poput vremenske prognoze obavljajući pretragu weba 
- **Wolfram Alpha** - Može se koristiti za složenije matematičke izračune pa nije potrebno pisati vlastite funkcije. 

Također možete izraditi vlastite prilagođene alate koje LLM može pozivati. 

U primjeru koda dolje: 

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskom promptu. 
- Šaljemo korisnički upit koji pita o vremenu u određenom gradu. 
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Napomena: Ovaj primjer samo poziva alat, ako želite dobiti rezultate, morate kreirati besplatan račun na Brave API stranici i definirati samu funkciju.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Iako je LLM, jedna od ograničenja Llama 3.1 je nedostatak multimodalnosti. To jest, nemogućnost korištenja različitih tipova ulaza poput slika kao upite i pružanje odgovora. Ta sposobnost je jedna od glavnih značajki Llama 3.2. Te značajke uključuju: 

- Multimodalnost - sposobnost evaluacije i tekstualnih i slikovnih upita 
- Varijacije male do srednje veličine (11B i 90B) - što pruža fleksibilne opcije implementacije, 
- Samo tekstualne varijante (1B i 3B) - omogućuje implementaciju na edge / mobilnim uređajima i pruža malu latenciju 

Multimodalna podrška predstavlja veliki korak u svijetu otvorenih modela. Primjer koda ispod prima i slikovni i tekstualni upit da bi se dobila analiza slike. Budući da je Llama 3.2 90B Vision Instruct ukinut, primjer koristi `Llama-4-Scout-17B-16E-Instruct`, trenutno dostupnu izvorno multimodalnu alternativu. 


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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Učenje ne staje ovdje, nastavite putovanje

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) za nastavak unaprjeđivanja vašeg znanja o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->