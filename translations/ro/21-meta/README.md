<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:13:11+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ro"
}
-->
# Construind cu modelele din familia Meta

## Introducere

Această lecție va acoperi:

- Explorarea celor două modele principale din familia Meta - Llama 3.1 și Llama 3.2
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model
- Exemplu de cod pentru a evidenția caracteristicile unice ale fiecărui model

## Familia de modele Meta

În această lecție, vom explora 2 modele din familia Meta sau „Llama Herd” - Llama 3.1 și Llama 3.2

Aceste modele vin în diferite variante și sunt disponibile pe piața GitHub Model. Iată mai multe detalii despre utilizarea GitHub Models pentru [prototiparea cu modele AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variante de modele:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Notă: Llama 3 este de asemenea disponibil pe GitHub Models, dar nu va fi acoperit în această lecție*

## Llama 3.1

Cu 405 miliarde de parametri, Llama 3.1 se încadrează în categoria LLM open source.

Modelul este o îmbunătățire față de versiunea anterioară Llama 3, oferind:

- Fereastră de context mai mare - 128k tokeni față de 8k tokeni  
- Număr maxim de tokeni de ieșire mai mare - 4096 față de 2048  
- Suport multilingv mai bun - datorită creșterii numărului de tokeni de antrenament  

Acestea permit lui Llama 3.1 să gestioneze cazuri de utilizare mai complexe când construiești aplicații GenAI, inclusiv:  
- Native Function Calling - capacitatea de a apela unelte și funcții externe în afara fluxului de lucru LLM  
- Performanță RAG îmbunătățită - datorită ferestrei de context mai mari  
- Generare de date sintetice - capacitatea de a crea date eficiente pentru sarcini precum fine-tuning  

### Native Function Calling

Llama 3.1 a fost ajustat pentru a fi mai eficient în apelarea funcțiilor sau uneltelor. De asemenea, are două unelte încorporate pe care modelul le poate identifica ca fiind necesare în funcție de promptul utilizatorului. Aceste unelte sunt:

- **Brave Search** - Poate fi folosit pentru a obține informații actualizate, cum ar fi vremea, prin efectuarea unei căutări pe web  
- **Wolfram Alpha** - Poate fi folosit pentru calcule matematice mai complexe, astfel încât să nu fie nevoie să scrii propriile funcții  

Poți crea și propriile unelte personalizate pe care LLM le poate apela.

În exemplul de cod de mai jos:

- Definim uneltele disponibile (brave_search, wolfram_alpha) în promptul sistemului.  
- Trimitem un prompt de la utilizator care întreabă despre vremea într-un anumit oraș.  
- LLM va răspunde cu un apel către unealta Brave Search care va arăta astfel `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Notă: Acest exemplu face doar apelul către unealtă, dacă dorești să obții rezultatele, va trebui să îți creezi un cont gratuit pe pagina Brave API și să definești funcția propriu-zisă*

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

Deși este un LLM, o limitare a lui Llama 3.1 este multimodalitatea. Adică abilitatea de a folosi diferite tipuri de input, cum ar fi imagini ca prompturi și de a oferi răspunsuri. Această capacitate este una dintre caracteristicile principale ale lui Llama 3.2. Alte caracteristici includ:

- Multimodalitate - capacitatea de a evalua atât prompturi text, cât și imagini  
- Variante de dimensiuni mici și medii (11B și 90B) - oferă opțiuni flexibile de implementare  
- Variante doar text (1B și 3B) - permit implementarea modelului pe dispozitive edge / mobile și oferă latență scăzută  

Suportul multimodal reprezintă un pas important în lumea modelelor open source. Exemplul de cod de mai jos primește atât o imagine, cât și un prompt text pentru a obține o analiză a imaginii de la Llama 3.2 90B.

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

## Învățarea nu se oprește aici, continuă călătoria

După ce termini această lecție, consultă colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea cunoștințelor despre Generative AI!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.