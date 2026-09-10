[![Modelli Open Source](../../../translated_images/it/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduzione

Gli agenti AI rappresentano un entusiasmante sviluppo nell'IA generativa, consentendo ai Modelli Linguistici di Grandi Dimensioni (LLM) di evolvere da assistenti a agenti capaci di intraprendere azioni. I framework per agenti AI permettono agli sviluppatori di creare applicazioni che danno accesso agli LLM a strumenti e gestione dello stato. Questi framework migliorano anche la visibilità, permettendo a utenti e sviluppatori di monitorare le azioni pianificate dagli LLM, migliorando così la gestione dell'esperienza.

La lezione coprirà i seguenti argomenti:

- Comprendere cos'è un agente AI - Cos'è esattamente un agente AI?
- Esplorare cinque diversi framework per agenti AI - Cosa li rende unici?
- Applicare questi agenti AI a diversi casi d'uso - Quando dovremmo usare agenti AI?

## Obiettivi di apprendimento

Dopo aver seguito questa lezione, sarai in grado di:

- Spiegare cosa sono gli agenti AI e come possono essere utilizzati.
- Avere una comprensione delle differenze tra alcuni dei framework più popolari per agenti AI, e come differiscono.
- Comprendere come funzionano gli agenti AI per costruire applicazioni con essi.

## Cosa Sono gli Agenti AI?

Gli agenti AI sono un campo molto entusiasmante nel mondo dell'IA generativa. Con questo entusiasmo a volte arriva una confusione di termini e la loro applicazione. Per mantenere le cose semplici e inclusive della maggior parte degli strumenti che si riferiscono agli agenti AI, useremo questa definizione:

Gli agenti AI consentono ai Modelli Linguistici di Grandi Dimensioni (LLM) di svolgere compiti dando loro accesso a uno **stato** e a **strumenti**.

![Modello Agente](../../../translated_images/it/what-agent.21f2893bdfd01e6a.webp)

Definiamo questi termini:

**Modelli Linguistici di Grandi Dimensioni** - Questi sono i modelli a cui si fa riferimento in questo corso come GPT-5, GPT-4o, e Llama 3.3, ecc.

**Stato** - Si riferisce al contesto in cui sta lavorando l'LLM. L'LLM usa il contesto delle azioni passate e il contesto attuale, guidando le sue decisioni per le azioni successive. I framework per agenti AI consentono agli sviluppatori di mantenere questo contesto più facilmente.

**Strumenti** - Per completare il compito richiesto dall'utente e pianificato dall'LLM, l'LLM ha bisogno di accedere a degli strumenti. Alcuni esempi di strumenti possono essere un database, un'API, un'applicazione esterna o anche un altro LLM!

Queste definizioni speriamo ti diano una buona base andando avanti mentre esaminiamo come vengono implementate. Esploriamo alcuni diversi framework per agenti AI:

## Agenti LangChain

[Agenti LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) è un'implementazione delle definizioni che abbiamo fornito sopra.

Per gestire lo **stato**, usa una funzione integrata chiamata `AgentExecutor`. Questa accetta l'`agent` definito e gli `tools` a sua disposizione.

L'`Agent Executor` conserva anche la cronologia della chat per fornire il contesto della conversazione.

![Agenti Langchain](../../../translated_images/it/langchain-agents.edcc55b5d5c43716.webp)

LangChain offre un [catalogo di strumenti](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) che possono essere importati nella tua applicazione a cui l'LLM può accedere. Questi sono creati dalla comunità e dal team di LangChain.

Puoi quindi definire questi strumenti e passarli all'`Agent Executor`.

La visibilità è un altro aspetto importante quando si parla di agenti AI. È importante per gli sviluppatori di applicazioni capire quale strumento l'LLM sta usando e perché. Per questo, il team di LangChain ha sviluppato LangSmith.

## AutoGen

Il prossimo framework per agenti AI di cui parleremo è [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Il focus principale di AutoGen sono le conversazioni. Gli agenti sono sia **conversabili** che **personalizzabili**.

**Conversabile -** Gli LLM possono iniziare e continuare una conversazione con un altro LLM per completare un compito. Questo si fa creando `AssistantAgents` e dando loro un messaggio di sistema specifico.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizzabile** - Gli agenti possono essere definiti non solo come LLM ma anche come un utente o uno strumento. Come sviluppatore, puoi definire un `UserProxyAgent` che è responsabile di interagire con l'utente per ottenere feedback nel completare un compito. Questo feedback può continuare l'esecuzione del compito oppure fermarla.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stato e Strumenti

Per cambiare e gestire lo stato, un agente assistente genera codice Python per completare il compito.

Ecco un esempio del processo:

![AutoGen](../../../translated_images/it/autogen.dee9a25a45fde584.webp)

#### LLM Definito con un Messaggio di Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Questo messaggio di sistema dirige questo specifico LLM su quali funzioni sono rilevanti per il suo compito. Ricorda, con AutoGen puoi avere più `AssistantAgents` definiti con messaggi di sistema differenti.

#### La Chat è Iniziata dall'Utente

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Questo messaggio dall'user_proxy (umano) è ciò che inizia il processo dell'agente per esplorare le possibili funzioni che dovrebbe eseguire.

#### La Funzione viene Eseguita

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Una volta elaborata la chat iniziale, l'agente invierà lo strumento suggerito da chiamare. In questo caso, è una funzione chiamata `get_weather`. A seconda della configurazione, questa funzione può essere automatizzata ed eseguita dall'agente oppure eseguita basandosi sull'input dell'utente.

Puoi trovare una lista di [esempi di codice AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) per esplorare ulteriormente come iniziare a costruire.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) è l'SDK open-source di Microsoft per costruire agenti AI e sistemi multi-agente sia in **Python** che in **.NET**. Riunisce i punti di forza di due progetti Microsoft precedenti — le funzionalità aziendali di **Semantic Kernel** e l'orchestrazione multi-agente di **AutoGen** — in un unico framework supportato. Se stai iniziando oggi un nuovo progetto agente, questo è il successore consigliato di AutoGen.

Il framework si adatta da un singolo **agente chat** fino a complessi **flussi di lavoro multi-agente**, e si integra direttamente con Microsoft Foundry, Azure OpenAI e OpenAI. Fornisce anche osservabilità integrata tramite OpenTelemetry, così puoi tracciare esattamente cosa stanno facendo i tuoi agenti.

### Stato e Strumenti

**Stato** - Il framework gestisce per te il contesto della conversazione attraverso **threads**. Un agente tiene traccia della cronologia dei messaggi (richieste utente, chiamate agli strumenti e risultati), così ogni turno si basa sui precedenti. I threads possono anche essere salvati, permettendo di mettere in pausa e riprendere una conversazione in seguito.

**Strumenti** - Dai a un agente strumenti passando semplici funzioni Python. I parametri annotati con tipo vengono automaticamente trasformati in uno schema, così il modello sa come e quando chiamarli (function calling). Il framework supporta anche server Model Context Protocol (MCP) e strumenti ospitati come un interprete di codice.

Ecco un esempio di un singolo agente con uno strumento personalizzato:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Per connetterti invece a Azure OpenAI in Microsoft Foundry, passa il tuo endpoint e le credenziali al client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Flussi di lavoro multi-agente

Dove il framework eccelle davvero è nell'orchestrare diversi agenti insieme. Ad esempio, puoi far eseguire agenti uno dopo l'altro (ognuno passando il suo contesto al prossimo) oppure distribuire più agenti in parallelo e aggregare i loro risultati:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Esegui gli agenti in sequenza, passando il contesto della conversazione lungo la catena
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribuisci agli agenti in parallelo, quindi aggrega le loro risposte
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Per installare il framework e iniziare:

```bash
pip install agent-framework-core
# Integrazioni opzionali
pip install agent-framework-openai       # OpenAI e Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Puoi esplorare di più nel [repository Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) e nella [documentazione ufficiale](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Il prossimo framework agente che esploreremo è [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). È noto come un agente "code-first" perché invece di lavorare strettamente con `stringhe`, può lavorare con DataFrame in Python. Questo diventa estremamente utile per compiti di analisi e generazione dati. Può essere cose come la creazione di grafici e tabelle o la generazione di numeri casuali.

### Stato e Strumenti

Per gestire lo stato della conversazione, TaskWeaver usa il concetto di un `Planner`. Il `Planner` è un LLM che prende la richiesta dagli utenti e mappa i compiti che devono essere completati per soddisfare questa richiesta.

Per completare i compiti, il `Planner` ha accesso alla collezione di strumenti chiamati `Plugins`. Questi possono essere classi Python o un interprete di codice generico. Questi plugin sono archiviati come embedding così che l'LLM possa cercare meglio il plugin corretto.

![Taskweaver](../../../translated_images/it/taskweaver.da8559999267715a.webp)

Ecco un esempio di un plugin per gestire il rilevamento di anomalie:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Il codice viene verificato prima di essere eseguito. Un'altra caratteristica per gestire il contesto in Taskweaver è l'`esperienza`. L'esperienza permette che il contesto di una conversazione venga conservato a lungo termine in un file YAML. Questo può essere configurato affinché l'LLM migliori nel tempo su certi compiti dato che viene esposto a conversazioni precedenti.

## JARVIS

L'ultimo framework agente che esploreremo è [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ciò che rende JARVIS unico è che utilizza un LLM per gestire lo `stato` della conversazione e gli `strumenti` sono altri modelli AI. Ciascuno di questi modelli AI è specializzato in compiti specifici come il rilevamento di oggetti, la trascrizione o la didascalia delle immagini.

![JARVIS](../../../translated_images/it/jarvis.762ddbadbd1a3a33.webp)

L'LLM, essendo un modello a scopo generale, riceve la richiesta dall'utente e identifica il compito specifico e qualsiasi argomento/dato necessario per completare il compito.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

L'LLM quindi formatta la richiesta in un modo che il modello AI specializzato possa interpretare, come JSON. Quando il modello AI ha restituito la sua previsione basata sul compito, l'LLM riceve la risposta.

Se sono necessari più modelli per completare il compito, l'LLM interpreterà anche la risposta di quei modelli prima di metterli insieme per generare la risposta all'utente.

L'esempio qui sotto mostra come funzionerebbe quando un utente richiede una descrizione e il conteggio degli oggetti in un'immagine:

## Compito

Per continuare il tuo apprendimento sugli agenti AI, puoi costruire con Microsoft Agent Framework:

- Un'applicazione che simula una riunione aziendale con diversi dipartimenti di una startup educativa.
- Crea messaggi di sistema che guidano gli LLM a comprendere diverse persone e priorità, e permetti all'utente di proporre una nuova idea di prodotto.
- L'LLM dovrebbe poi generare domande di follow-up da ogni dipartimento per raffinare e migliorare la proposta e l'idea di prodotto.

## L'apprendimento non termina qui, continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza dell'IA generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->