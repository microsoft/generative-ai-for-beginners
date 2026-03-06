# Costruire con i Modelli della Famiglia Meta

## Introduzione

Questa lezione coprirà:

- Esplorare i due principali modelli della famiglia Meta - Llama 3.1 e Llama 3.2
- Comprendere i casi d'uso e gli scenari per ciascun modello
- Esempio di codice per mostrare le caratteristiche uniche di ogni modello

## La Famiglia di Modelli Meta

In questa lezione, esploreremo 2 modelli della famiglia Meta o "Mandria Llama" - Llama 3.1 e Llama 3.2.

Questi modelli sono disponibili in diverse varianti e sono disponibili nel marketplace Modelli di GitHub. Ecco maggiori dettagli sull'uso dei Modelli GitHub per [prototipare con modelli AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianti del Modello:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Nota: Llama 3 è disponibile anche su Modelli GitHub ma non sarà trattato in questa lezione*

## Llama 3.1

Con 405 miliardi di parametri, Llama 3.1 rientra nella categoria LLM open source.

Il modello è un aggiornamento della precedente versione Llama 3 offrendo:

- Finestra di contesto più ampia - 128k token contro 8k token
- Numero massimo di token in output maggiore - 4096 contro 2048
- Supporto multilingue migliore - grazie all'aumento dei token di addestramento

Queste caratteristiche permettono a Llama 3.1 di gestire casi d'uso più complessi nella costruzione di applicazioni GenAI, inclusi:
- Chiamata nativa di funzioni - la capacità di chiamare strumenti e funzioni esterne al flusso di lavoro LLM
- Migliori prestazioni RAG - grazie alla finestra di contesto più ampia
- Generazione di dati sintetici - la capacità di creare dati efficaci per attività come il fine-tuning

### Chiamata Nativa di Funzioni

Llama 3.1 è stato affinato per essere più efficace nel fare chiamate a funzioni o strumenti. Ha anche due strumenti integrati che il modello può identificare come necessari in base al prompt dell'utente. Questi strumenti sono:

- **Brave Search** - Può essere usato per ottenere informazioni aggiornate come il meteo effettuando una ricerca sul web
- **Wolfram Alpha** - Può essere usato per calcoli matematici più complessi, quindi non è necessario scrivere funzioni proprie

Puoi anche creare i tuoi strumenti personalizzati che l'LLM può chiamare.

Nel codice di esempio qui sotto:

- Definiamo gli strumenti disponibili (brave_search, wolfram_alpha) nel prompt di sistema.
- Inviamo un prompt utente che chiede del meteo in una certa città.
- L'LLM risponderà con una chiamata allo strumento Brave Search che apparirà così `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: questo esempio fa solo la chiamata allo strumento; se desideri ottenere i risultati, dovrai creare un account gratuito sulla pagina Brave API e definire la funzione stessa.

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

Nonostante sia un LLM, una limitazione di Llama 3.1 è la mancanza di multimodalità. Cioè, l'incapacità di usare diversi tipi di input come immagini come prompt e fornire risposte. Questa capacità è una delle caratteristiche principali di Llama 3.2. Queste caratteristiche includono anche:

- Multimodalità - ha la capacità di valutare sia prompt di testo che immagini
- Varianti di piccole e medie dimensioni (11B e 90B) - ciò offre opzioni di deployment flessibili,
- Varianti solo testo (1B e 3B) - permettono il deployment su dispositivi edge / mobili e offrono bassa latenza

Il supporto multimodale rappresenta un grande passo nel mondo dei modelli open source. L'esempio di codice qui sotto prende sia un'immagine che un prompt di testo per ottenere un'analisi dell'immagine da Llama 3.2 90B.

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

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, consulta la nostra [collezione di apprendimento sull'IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'IA generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Dichiarazione di non responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per la precisione, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda la traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->