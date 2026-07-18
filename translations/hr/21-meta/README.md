# Izgradnja s Meta obiteljskim modelima 

## Uvod 

Ova lekcija će obuhvatiti: 

- Istraživanje dva glavna Meta obiteljska modela - Llama 3.1 i Llama 3.2 
- Razumijevanje slučajeva upotrebe i scenarija za svaki model 
- Primjer koda za prikaz jedinstvenih značajki svakog modela 


## Meta obitelj modela 

U ovoj lekciji istražit ćemo 2 modela iz Meta obitelji ili "Llama stada" - Llama 3.1 i Llama 3.2.

Ti modeli dolaze u različitim varijantama i dostupni su u [Microsoft Foundry Models katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Napomena:** GitHub Models se povlači krajem srpnja 2026. Za više detalja o korištenju [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) za prototipiziranje s AI modelima.

Varijante modela: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Napomena: Llama 3 je također dostupna u Microsoft Foundry Models, ali neće biti obrađena u ovoj lekciji*

## Llama 3.1 

S 405 milijardi parametara, Llama 3.1 spada u kategoriju open source velikih jezičnih modela. 

Model je nadogradnja ranije verzije Llama 3 nudeći: 

- Veći kontekstni prozor - 128k tokena naspram 8k tokena 
- Veći maksimalni broj izlaznih tokena - 4096 naspram 2048 
- Bolju podršku za više jezika - zbog povećanja broja trening tokena 

To omogućuje Llama 3.1 da se nosi s kompleksnijim slučajevima upotrebe pri izgradnji GenAI aplikacija uključujući: 
- Nativno pozivanje funkcija - mogućnost pozivanja vanjskih alata i funkcija izvan LLM toka rada
- Bolje RAG performanse - zbog većeg kontekstnog prozora 
- Generaciju sintetičkih podataka - sposobnost kreiranja učinkovitih podataka za zadatke poput finog podešavanja 

### Nativno pozivanje funkcija 

Llama 3.1 je fino podešen da bude učinkovitiji u pozivanju funkcija ili alata. Također ima dva ugrađena alata koje model može prepoznati kao potrebne na temelju uputa korisnika. Ti alati su: 

- **Brave Search** - može se koristiti za dobivanje ažuriranih informacija poput vremenske prognoze pretraživanjem weba 
- **Wolfram Alpha** - može se koristiti za složenije matematičke izračune pa nije potrebno pisati vlastite funkcije. 

Također možete kreirati vlastite prilagođene alate koje LLM može pozivati. 

U primjeru koda ispod: 

- Definiramo dostupne alate (brave_search, wolfram_alpha) u sistemskoj uputi. 
- Šaljemo korisnički upit koji pita o vremenu u određenom gradu. 
- LLM će odgovoriti pozivom alata Brave Search koji će izgledati ovako `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Napomena: Ovaj primjer samo vrši poziv alata, ako želite dobiti rezultate, morat ćete kreirati besplatan račun na Brave API stranici i definirati samu funkciju.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Nabavite ih s vaše Microsoft Foundry projektne stranice "Pregled"
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

Unatoč tome što je LLM, jedna od ograničenja Llama 3.1 je nedostatak multimodalnosti. To jest, nemogućnost korištenja različitih vrsta ulaza poput slika kao uputu i pružanja odgovora. Ta sposobnost je jedna od glavnih značajki Llama 3.2. Te značajke također uključuju: 

- Multimodalnost - sposobnost procjene i tekstualnih i slikovnih uputa 
- Varijante malih do srednjih veličina (11B i 90B) - pruža fleksibilne opcije uvođenja u rad, 
- Varijante samo za tekst (1B i 3B) - omogućuje implementaciju modela na rubnim / mobilnim uređajima i pruža nisku latenciju 

Multimodalna podrška predstavlja veliki korak u svijetu open source modela. Primjer koda ispod prima i sliku i tekstualnu uputu za dobivanje analize slike od Llama 3.2 90B. 


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

# Nabavite ih s stranice "Pregled" vašeg Microsoft Foundry projekta
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

## Učenje ne prestaje ovdje, nastavi putovanje

Nakon dovršetka ove lekcije, pogledajte našu [Kolekciju za učenje generativne umjetne inteligencije](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->