# Costruire con i Modelli della Famiglia Meta

## Introduzione

Questa lezione coprirà:

- Esplorare i due principali modelli della famiglia Meta - Llama 3.1 e Llama 3.2
- Comprendere i casi d'uso e gli scenari per ciascun modello
- Esempio di codice per mostrare le caratteristiche uniche di ogni modello


## La Famiglia di Modelli Meta

In questa lezione, esploreremo 2 modelli della famiglia Meta o "Llama Herd" - Llama 3.1 e Llama 3.2.

Questi modelli sono disponibili in diverse varianti nel [catalogo Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** GitHub Models sarà dismesso alla fine di luglio 2026. Qui troverai maggiori dettagli sull'uso di [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) per prototipare con modelli di IA.

Varianti del modello:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Nota: Llama 3 è disponibile anche in Microsoft Foundry Models ma non sarà trattato in questa lezione*

## Llama 3.1

Con 405 miliardi di parametri, Llama 3.1 rientra nella categoria degli LLM open source.

Il modello è un aggiornamento della precedente versione Llama 3 offrendo:

- Finestra di contesto più ampia - 128k token contro 8k token
- Numero massimo di token in output più alto - 4096 contro 2048
- Supporto multilingue migliore - grazie all’aumento dei token di addestramento

Questo permette a Llama 3.1 di gestire casi d’uso più complessi nello sviluppo di applicazioni GenAI, tra cui:
- Chiamate Native a Funzioni - la capacità di chiamare strumenti e funzioni esterne al flusso di lavoro LLM
- Migliore performance RAG - grazie alla finestra di contesto più ampia
- Generazione di Dati Sintetici - la capacità di creare dati efficaci per compiti come il fine-tuning

### Chiamate Native a Funzioni

Llama 3.1 è stato fine-tuned per essere più efficace nelle chiamate di funzioni o strumenti. Ha anche due strumenti integrati che il modello può identificare come necessari da usare in base al prompt dell’utente. Questi strumenti sono:

- **Brave Search** - Può essere usato per ottenere informazioni aggiornate come il meteo eseguendo una ricerca sul web
- **Wolfram Alpha** - Può essere usato per calcoli matematici più complessi, quindi scrivere funzioni proprie non è richiesto.

Puoi anche creare i tuoi strumenti personalizzati che l’LLM può chiamare.

Nell’esempio di codice seguente:

- Definiamo gli strumenti disponibili (brave_search, wolfram_alpha) nel prompt di sistema.
- Inviamo un prompt utente che chiede informazioni sul meteo in una certa città.
- L’LLM risponderà con una chiamata allo strumento Brave Search che apparirà così `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: questo esempio fa solo la chiamata allo strumento; se vuoi ottenere i risultati, dovrai creare un account gratuito sulla pagina API di Brave e definire la funzione stessa.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Ottienili dalla pagina "Panoramica" del tuo progetto Microsoft Foundry
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

Nonostante sia un LLM, una limitazione di Llama 3.1 è la mancanza di multimodalità. Cioè, l’incapacità di usare diversi tipi di input come immagini come prompt e fornire risposte. Questa capacità è una delle principali caratteristiche di Llama 3.2. Queste caratteristiche includono anche:

- Multimodalità - ha la capacità di valutare sia prompt testuali che visivi
- Varianti di dimensioni piccole e medie (11B e 90B) - questo fornisce opzioni di distribuzione flessibili,
- Varianti solo testuali (1B e 3B) - questo permette al modello di essere distribuito su dispositivi edge/mobile e offre bassa latenza

Il supporto multimodale rappresenta un grande passo nel mondo dei modelli open source. L’esempio di codice seguente prende sia un’immagine che un prompt testuale per ottenere un’analisi dell’immagine da Llama 3.2 90B.


### Supporto Multimodale con Llama 3.2

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

# Ottienili dalla pagina "Panoramica" del tuo progetto Microsoft Foundry
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

## L’apprendimento non termina qui, continua il viaggio

Dopo aver completato questa lezione, consulta la nostra [collezione di apprendimento sull’Intelligenza Artificiale Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull’IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->