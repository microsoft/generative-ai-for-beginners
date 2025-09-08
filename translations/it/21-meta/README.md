<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:09:24+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "it"
}
-->
# Costruire con i modelli della famiglia Meta

## Introduzione

In questa lezione vedremo:

- Esplorare i due principali modelli della famiglia Meta - Llama 3.1 e Llama 3.2
- Comprendere i casi d’uso e gli scenari per ciascun modello
- Esempio di codice per mostrare le caratteristiche uniche di ogni modello

## La famiglia di modelli Meta

In questa lezione esploreremo 2 modelli della famiglia Meta o "Llama Herd" - Llama 3.1 e Llama 3.2

Questi modelli sono disponibili in diverse varianti e si trovano nel marketplace GitHub Model. Ecco maggiori dettagli sull’uso dei modelli GitHub per [prototipare con modelli AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varianti del modello:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Nota: Llama 3 è disponibile anche su GitHub Models ma non sarà trattato in questa lezione*

## Llama 3.1

Con 405 miliardi di parametri, Llama 3.1 rientra nella categoria degli LLM open source.

Il modello è un aggiornamento rispetto alla versione precedente Llama 3, offrendo:

- Finestra di contesto più ampia - 128k token contro 8k token  
- Numero massimo di token in output più alto - 4096 contro 2048  
- Migliore supporto multilingue - grazie all’aumento dei token di addestramento  

Queste caratteristiche permettono a Llama 3.1 di gestire casi d’uso più complessi nella costruzione di applicazioni GenAI, tra cui:  
- Native Function Calling - la capacità di chiamare strumenti e funzioni esterne al flusso di lavoro LLM  
- Migliore performance RAG - grazie alla finestra di contesto più ampia  
- Generazione di dati sintetici - la possibilità di creare dati efficaci per attività come il fine-tuning  

### Native Function Calling

Llama 3.1 è stato ottimizzato per essere più efficace nel chiamare funzioni o strumenti. Ha inoltre due strumenti integrati che il modello può riconoscere come necessari in base al prompt dell’utente. Questi strumenti sono:

- **Brave Search** - può essere usato per ottenere informazioni aggiornate come il meteo effettuando una ricerca sul web  
- **Wolfram Alpha** - può essere usato per calcoli matematici complessi, evitando di dover scrivere funzioni personalizzate  

È anche possibile creare strumenti personalizzati che l’LLM può chiamare.

Nell’esempio di codice qui sotto:

- Definiamo gli strumenti disponibili (brave_search, wolfram_alpha) nel prompt di sistema.  
- Inviamo un prompt utente che chiede informazioni sul meteo in una certa città.  
- L’LLM risponderà con una chiamata allo strumento Brave Search che apparirà così `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: questo esempio effettua solo la chiamata allo strumento, se vuoi ottenere i risultati dovrai creare un account gratuito sulla pagina Brave API e definire la funzione stessa*

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

Nonostante sia un LLM, una limitazione di Llama 3.1 è la multimodalità, cioè la capacità di usare diversi tipi di input come immagini nei prompt e fornire risposte. Questa capacità è una delle caratteristiche principali di Llama 3.2. Tra le sue funzionalità troviamo anche:

- Multimodalità - capacità di valutare sia prompt testuali che immagini  
- Varianti di dimensioni piccole e medie (11B e 90B) - che offrono opzioni di deployment flessibili  
- Varianti solo testo (1B e 3B) - che permettono di distribuire il modello su dispositivi edge/mobile con bassa latenza  

Il supporto multimodale rappresenta un grande passo avanti nel mondo dei modelli open source. L’esempio di codice qui sotto prende sia un’immagine che un prompt testuale per ottenere un’analisi dell’immagine da Llama 3.2 90B.

### Supporto multimodale con Llama 3.2

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

## L’apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento sull’Intelligenza Artificiale Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze su Generative AI!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.