# Construind cu Modelele Familiei Meta 

## Introducere 

Această lecție va acoperi: 

- Explorarea celor două modele principale din familia Meta - Llama 3.1 și Llama 3.2 
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model 
- Exemplu de cod pentru a arăta caracteristicile unice ale fiecărui model 


## Familia de modele Meta 

În această lecție, vom explora 2 modele din familia Meta sau „Cotele Llama” - Llama 3.1 și Llama 3.2.

Aceste modele vin în diferite variante și sunt disponibile în [catalogul Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Notă:** GitHub Models se va retrage la sfârșitul lunii iulie 2026. Iată mai multe informații despre utilizarea [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) pentru prototiparea cu modele AI.

Variantele modelului: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Notă: Llama 3 este, de asemenea, disponibil în Microsoft Foundry Models, dar nu va fi acoperit în această lecție*

## Llama 3.1 

Cu 405 miliarde de parametri, Llama 3.1 se încadrează în categoria LLM open source. 

Modelul este o actualizare a versiunii anterioare Llama 3, oferind: 

- Fereastră de context mai mare - 128k tokeni față de 8k tokeni 
- Număr maxim mai mare de tokeni de ieșire - 4096 față de 2048 
- Suport multilingv mai bun - datorită creșterii numărului de tokeni de antrenament 

Acestea permit lui Llama 3.1 să gestioneze cazuri de utilizare mai complexe atunci când se construiesc aplicații GenAI, inclusiv: 
- Apelare nativă a funcțiilor - capacitatea de a apela unelte și funcții externe în afara fluxului de lucru LLM
- Performanță RAG mai bună - datorită ferestrei de context mai mare 
- Generare de date sintetice - capacitatea de a crea date eficiente pentru sarcini precum ajustarea fină 

### Apelare nativă a funcțiilor 

Llama 3.1 a fost ajustat fin pentru a fi mai eficient în efectuarea apelurilor către funcții sau unelte. De asemenea, are două unelte încorporate pe care modelul le poate identifica ca fiind necesar de utilizat bazat pe promptul utilizatorului. Aceste unelte sunt: 

- **Brave Search** - Poate fi folosit pentru a obține informații actualizate, cum ar fi vremea, prin efectuarea unei căutări pe web 
- **Wolfram Alpha** - Poate fi folosit pentru calcule matematice mai complexe, astfel încât să nu fie necesar să scrii propriile funcții. 

De asemenea, poți crea uneltele tale personalizate pe care LLM-ul le poate apela. 

În exemplul de cod de mai jos: 

- Definim uneltele disponibile (brave_search, wolfram_alpha) în promptul sistemului. 
- Trimitem un prompt de la utilizator care întreabă despre vremea într-un anumit oraș. 
- LLM-ul va răspunde cu un apel de unealtă către Brave Search, care va arăta astfel `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Notă: Acest exemplu face doar apelul către unealtă, dacă dorești să obții rezultatele, va trebui să creezi un cont gratuit pe pagina API Brave și să definești funcția în sine.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Obțineți acestea de pe pagina „Prezentare generală” a proiectului Microsoft Foundry
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

Deși este un LLM, o limitare a lui Llama 3.1 este lipsa multimodalității. Adică, incapacitatea de a folosi tipuri diferite de intrare, precum imagini ca prompturi și a oferi răspunsuri. Această capacitate este una dintre principalele caracteristici ale Llama 3.2. Aceste caracteristici includ și: 

- Multimodalitate - are capacitatea de a evalua atât prompturi text cât și imagini 
- Variante de dimensiuni mici și medii (11B și 90B) - oferă opțiuni flexibile de implementare, 
- Variante doar text (1B și 3B) - permit modelului să fie implementat pe dispozitive edge / mobile și oferă latență scăzută 

Suportul multimodal reprezintă un pas important în lumea modelelor open source. Exemplul de cod de mai jos ia atât o imagine cât și un prompt text pentru a obține o analiză a imaginii de la Llama 3.2 90B. 


### Suport multimodal cu Llama 3.2

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

# Obțineți acestea de pe pagina „Prezentare generală” a proiectului dvs. Microsoft Foundry
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

## Învățarea nu se oprește aici, continuă călătoria

După ce termini această lecție, verifică colecția noastră de [Învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți dezvolți cunoștințele despre AI Generativ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->