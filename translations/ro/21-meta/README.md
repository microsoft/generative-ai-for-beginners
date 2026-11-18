# Construirea cu modelele familiei Meta 

## Introducere 

Această lecție va acoperi: 

- Explorarea celor două modele principale din familia Meta - Llama 3.1 și Llama 3.2, plus alternativele disponibile în prezent folosite în exemplele de cod (Llama 3.3 și Llama 4) 
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model 
- Exemplu de cod pentru a arăta caracteristicile unice ale fiecărui model 


## Familia de modele Meta 

În această lecție, vom explora 2 modele din familia Meta sau „Turma Llama” - Llama 3.1 și Llama 3.2. Exemplele de cod care pot fi rulate utilizează Llama 3.3 și Llama 4, care sunt alternative disponibile în prezent în catalogul Microsoft Foundry Models.

Aceste modele vin în diferite variante și sunt disponibile în [catalogul Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Notă:** GitHub Models se va retrage la sfârșitul lunii iulie 2026. Iată mai multe detalii despre utilizarea [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pentru a prototipa cu modele AI.

> **Notă:** Versiunile specifice ale modelului pentru care a fost scrisă inițial această lecție (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) au fost ulterior retrase din catalogul Microsoft Foundry Models. Exemplele de cod de mai jos folosesc `Llama-3.3-70B-Instruct` și `Llama-4-Scout-17B-16E-Instruct` ca alternative disponibile în prezent în catalogul Microsoft Foundry Models, deci încă pot fi rulate.

Variantele modelelor (așa cum au fost acoperite inițial în această lecție): 
- Llama 3.1 - 70B Instruct (retras) 
- Llama 3.1 - 405B Instruct (retras) 
- Llama 3.2 - 11B Vision Instruct (retras) 
- Llama 3.2 - 90B Vision Instruct (retras) 

Alternativele disponibile în prezent folosite în exemplele de cod: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Notă: Variantele Llama 3 discutate mai sus sunt păstrate pentru context istoric și nu mai sunt disponibile în Microsoft Foundry Models.*

## Llama 3.1 

Cu 405 miliarde de parametri, Llama 3.1 se încadrează în categoria LLM open source. 

Modelul este o actualizare a versiunii anterioare Llama 3, oferind: 

- Fereastră de context mai mare - 128k tokeni față de 8k tokeni 
- Număr maxim de tokeni de ieșire mai mare - 4096 față de 2048 
- Suport multilingv mai bun - datorită creșterii numărului de tokeni de antrenament 

Acestea îi permit lui Llama 3.1 să gestioneze cazuri de utilizare mai complexe când se construiesc aplicații GenAI incluzând: 
- Apelarea nativă a funcțiilor - capacitatea de a apela unelte și funcții externe în afara fluxului de lucru LLM
- Performanță RAG mai bună - datorită ferestrei de context mai largi 
- Generarea de date sintetice - capacitatea de a crea date eficiente pentru sarcini precum fine-tuning-ul 

### Apelarea nativă a funcțiilor 

Llama 3.1 a fost ajustat fin pentru a face apeluri către funcții sau unelte mai eficiente. De asemenea, are două unelte integrate pe care modelul le poate identifica ca necesare în funcție de promptul utilizatorului. Aceste unelte sunt: 

- **Brave Search** - Poate fi folosit pentru a obține informații actualizate, cum ar fi vremea, prin efectuarea unei căutări pe web 
- **Wolfram Alpha** - Poate fi folosit pentru calcule matematice mai complexe, deci nu este necesar să scrieți propriile funcții. 

De asemenea, puteți crea propriile unelte personalizate pe care LLM-ul le poate apela. 

În exemplul de cod de mai jos: 

- Definim uneltele disponibile (brave_search, wolfram_alpha) în promptul sistemului. 
- Trimitem un prompt utilizator care întreabă despre vremea dintr-un anumit oraș. 
- LLM va răspunde cu un apel către unealta Brave Search care va arăta astfel `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Notă: Acest exemplu face doar apelul către unealtă, dacă doriți să obțineți rezultatele, va trebui să creați un cont gratuit pe pagina Brave API și să definiți funcția propriu-zisă.

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

Deși este un LLM, o limitare a lui Llama 3.1 este lipsa multimodalității. Adică, incapacitatea de a folosi diferite tipuri de intrări, cum ar fi imagini ca prompturi și de a oferi răspunsuri. Această capacitate este una dintre principalele caracteristici ale lui Llama 3.2. Aceste caracteristici includ și: 

- Multimodalitate - are capacitatea de a evalua atât prompturi text, cât și de imagine 
- Variante de dimensiuni mici până la medii (11B și 90B) - oferă opțiuni flexibile de implementare, 
- Variante doar text (1B și 3B) - permit implementarea modelului pe dispozitive edge/mobile și oferă latență redusă 

Suportul multimodal reprezintă un mare pas în lumea modelelor open source. Exemplul de cod de mai jos folosește atât o imagine, cât și un prompt text pentru a obține o analiză a imaginii. Deoarece Llama 3.2 90B Vision Instruct a fost retras, exemplul folosește `Llama-4-Scout-17B-16E-Instruct`, o alternativă multimodală nativă disponibilă în prezent. 


### Suport Multimodal cu Llama 3.2

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

## Învățarea nu se oprește aici, continuă călătoria

După ce ai terminat această lecție, consultă colecția noastră [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți dezvolți cunoștințele despre Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->