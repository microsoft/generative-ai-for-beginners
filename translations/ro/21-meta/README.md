<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:35:36+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ro"
}
-->
# Construirea cu Modelele Familiei Meta

## Introducere

Această lecție va acoperi:

- Explorarea celor două modele principale ale familiei Meta - Llama 3.1 și Llama 3.2
- Înțelegerea cazurilor de utilizare și scenariilor pentru fiecare model
- Exemple de cod pentru a arăta caracteristicile unice ale fiecărui model

## Familia de Modele Meta

În această lecție, vom explora 2 modele din familia Meta sau "Turma Llama" - Llama 3.1 și Llama 3.2

Aceste modele vin în diferite variante și sunt disponibile pe piața de modele GitHub. Iată mai multe detalii despre utilizarea modelelor GitHub pentru a [prototipa cu modele AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variante de model:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Notă: Llama 3 este de asemenea disponibil pe Modelele GitHub, dar nu va fi acoperit în această lecție*

## Llama 3.1

Cu 405 miliarde de parametri, Llama 3.1 se încadrează în categoria LLM open source.

Modul este o îmbunătățire a lansării anterioare Llama 3 prin oferirea:

- Fereastră de context mai mare - 128k token-uri vs 8k token-uri
- Max Output Tokens mai mare - 4096 vs 2048
- Suport multilingv mai bun - datorită creșterii numărului de token-uri de antrenament

Acestea permit Llama 3.1 să gestioneze cazuri de utilizare mai complexe atunci când construim aplicații GenAI, inclusiv:
- Apeluri native de funcții - capacitatea de a apela instrumente și funcții externe în afara fluxului de lucru LLM
- Performanță RAG mai bună - datorită ferestrei de context mai mari
- Generarea de date sintetice - capacitatea de a crea date eficiente pentru sarcini precum fine-tuning

### Apeluri native de funcții

Llama 3.1 a fost ajustat pentru a fi mai eficient la efectuarea apelurilor de funcții sau instrumente. De asemenea, are două instrumente încorporate pe care modelul le poate identifica ca fiind necesare să fie utilizate pe baza solicitării utilizatorului. Aceste instrumente sunt:

- **Brave Search** - Poate fi folosit pentru a obține informații actualizate, cum ar fi vremea, prin efectuarea unei căutări pe web
- **Wolfram Alpha** - Poate fi folosit pentru calcule matematice mai complexe, astfel încât nu este necesar să scrieți propriile funcții.

De asemenea, puteți crea propriile instrumente personalizate pe care LLM le poate apela.

În exemplul de cod de mai jos:

- Definim instrumentele disponibile (brave_search, wolfram_alpha) în solicitarea sistemului.
- Trimitem o solicitare utilizatorului care întreabă despre vremea într-un anumit oraș.
- LLM va răspunde cu un apel de instrument către instrumentul Brave Search care va arăta astfel `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Notă: Acest exemplu face doar apelul de instrument, dacă doriți să obțineți rezultatele, va trebui să creați un cont gratuit pe pagina API Brave și să definiți funcția în sine*

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

Deși este un LLM, o limitare pe care Llama 3.1 o are este multimodalitatea. Adică, capacitatea de a utiliza diferite tipuri de input, cum ar fi imagini, ca solicitări și de a oferi răspunsuri. Această abilitate este una dintre caracteristicile principale ale Llama 3.2. Aceste caracteristici includ:

- Multimodalitate - are capacitatea de a evalua atât solicitările text cât și cele de imagine
- Varianta de dimensiuni mici până la medii (11B și 90B) - aceasta oferă opțiuni flexibile de implementare,
- Variante doar text (1B și 3B) - aceasta permite modelului să fie implementat pe dispozitive edge / mobile și oferă latență redusă

Suportul multimodal reprezintă un mare pas în lumea modelelor open source. Exemplul de cod de mai jos ia atât o imagine cât și o solicitare text pentru a obține o analiză a imaginii de la Llama 3.2 90B.

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

## Învățarea nu se oprește aici, continuă Călătoria

După ce ai finalizat această lecție, verifică [colecția de învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți îmbunătățești cunoștințele despre AI Generativă!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să obținem acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem responsabili pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.