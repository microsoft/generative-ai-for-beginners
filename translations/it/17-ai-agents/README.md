[![Modelli Open Source](../../../translated_images/it/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introduzione

Gli agenti IA rappresentano un entusiasmante sviluppo nell'IA generativa, consentendo ai modelli linguistici di grandi dimensioni (LLM) di evolversi da assistenti ad agenti capaci di intraprendere azioni. I framework di agenti IA permettono agli sviluppatori di creare applicazioni che danno accesso ai LLM a strumenti e gestione dello stato. Questi framework migliorano anche la visibilità, consentendo agli utenti e agli sviluppatori di monitorare le azioni pianificate dai LLM, migliorando così la gestione dell'esperienza.

La lezione coprirà le seguenti aree:

- Comprendere cos'è un Agente IA - Che cos'è esattamente un Agente IA?
- Esplorare cinque diversi framework di agenti IA - Cosa li rende unici?
- Applicare questi agenti IA a diversi casi d'uso - Quando dovremmo usare gli agenti IA?

## Obiettivi di apprendimento

Dopo aver seguito questa lezione, sarai in grado di:

- Spiegare cosa sono gli Agenti IA e come possono essere utilizzati.
- Comprendere le differenze tra alcuni dei popolari framework di agenti IA e in cosa differiscono.
- Capire come funzionano gli Agenti IA per costruire applicazioni con essi.

## Cosa sono gli Agenti IA?

Gli Agenti IA sono un campo molto entusiasmante nel mondo dell'IA generativa. Con questo entusiasmo talvolta arriva una confusione terminologica e applicativa. Per mantenere le cose semplici e includere la maggior parte degli strumenti che si riferiscono agli Agenti IA, useremo questa definizione:

Gli Agenti IA consentono ai modelli linguistici di grandi dimensioni (LLM) di eseguire compiti dandogli accesso a uno **stato** e a **strumenti**.

![Modello Agente](../../../translated_images/it/what-agent.21f2893bdfd01e6a.webp)

Definiamo questi termini:

**Modelli Linguistici di Grandi Dimensioni** - Questi sono i modelli riferiti in tutto questo corso, come GPT-3.5, GPT-4, Llama-2, ecc.

**Stato** - Si riferisce al contesto in cui il LLM sta lavorando. Il LLM utilizza il contesto delle sue azioni passate e il contesto attuale, guidando il suo processo decisionale per azioni successive. I framework di agenti IA permettono agli sviluppatori di mantenere questo contesto più facilmente.

**Strumenti** - Per completare il compito che l'utente ha richiesto e che il LLM ha pianificato, il LLM ha bisogno di accesso agli strumenti. Alcuni esempi di strumenti possono essere un database, un'API, un'applicazione esterna o anche un altro LLM!

Queste definizioni dovrebbero darti una buona base per il futuro mentre vedremo come sono implementati. Esploriamo alcuni diversi framework di agenti IA:

## Agenti LangChain

[Agenti LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) è un'implementazione delle definizioni fornite sopra.

Per gestire lo **stato** , utilizza una funzione integrata chiamata `AgentExecutor`. Questa accetta l'`agent` definito e gli `tools` a disposizione.

L'`Agent Executor` memorizza anche la cronologia della chat per fornire il contesto della conversazione.

![Agenti LangChain](../../../translated_images/it/langchain-agents.edcc55b5d5c43716.webp)

LangChain offre un [catalogo di strumenti](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) che possono essere importati nella tua applicazione e a cui il LLM può accedere. Questi sono realizzati dalla comunità e dal team di LangChain.

Puoi quindi definire questi strumenti e passarli all'`Agent Executor`.

La visibilità è un altro aspetto importante quando si parla di agenti IA. È importante per gli sviluppatori comprendere quale strumento il LLM sta utilizzando e perché. Per questo, il team di LangChain ha sviluppato LangSmith.

## AutoGen

Il prossimo framework di agenti IA di cui parleremo è [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Il focus principale di AutoGen sono le conversazioni. Gli agenti sono sia **conversabili** che **personalizzabili**.

**Conversabili -** I LLM possono iniziare e continuare una conversazione con un altro LLM per completare un compito. Questo viene fatto creando `AssistantAgents` e dando loro un messaggio di sistema specifico.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizzabili** - Gli agenti possono essere definiti non solo come LLM ma anche come utente o strumento. Come sviluppatore, puoi definire un `UserProxyAgent` responsabile di interagire con l'utente per ricevere feedback sul completamento di un compito. Questo feedback può continuare l'esecuzione del compito o fermarla.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stato e Strumenti

Per cambiare e gestire lo stato, un agente assistente genera codice Python per completare il compito.

Ecco un esempio del processo:

![AutoGen](../../../translated_images/it/autogen.dee9a25a45fde584.webp)

#### LLM definito con un messaggio di sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Questo messaggio di sistema indica a questo specifico LLM quali funzioni sono rilevanti per il suo compito. Ricorda, con AutoGen puoi avere più AssistantAgents definiti con messaggi di sistema differenti.

#### La chat è avviata dall'utente

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Questo messaggio dall'user_proxy (umano) è ciò che avvierà il processo dell'agente per esplorare le possibili funzioni che dovrebbe eseguire.

#### Funzione eseguita

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Una volta processata la chat iniziale, l'agente invierà lo strumento suggerito da chiamare. In questo caso, è una funzione chiamata `get_weather`. A seconda della tua configurazione, questa funzione può essere eseguita automaticamente e letta dall'agente o eseguita in base all'input dell'utente.

Puoi trovare una lista di [esempi di codice AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) per esplorare ulteriormente come iniziare a costruire.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) è l'SDK open-source di Microsoft per costruire agenti IA e sistemi multi-agente sia in **Python** che in **.NET**. Riunisce i punti di forza di due progetti Microsoft precedenti — le funzioni enterprise di **Semantic Kernel** e l'orchestrazione multi-agente di **AutoGen** — in un singolo framework supportato. Se stai iniziando un nuovo progetto agente oggi, questo è il successore consigliato di AutoGen.

Il framework scala da un singolo **agente di chat** fino a complessi **flussi di lavoro multi-agente**, e si integra direttamente con Microsoft Foundry, Azure OpenAI e OpenAI. Fornisce anche osservabilità integrata tramite OpenTelemetry così puoi tracciare esattamente cosa stanno facendo i tuoi agenti.

### Stato e Strumenti

**Stato** - Il framework gestisce il contesto della conversazione per te attraverso **thread**. Un agente tiene traccia della cronologia dei messaggi (richieste dell'utente, chiamate agli strumenti e risultati), così ogni turno si costruisce sui precedenti. I thread possono anche essere persistiti, permettendo di mettere in pausa e riprendere una conversazione in seguito.

**Strumenti** - Dai ad un agente strumenti passando funzioni Python semplici. I parametri annotati con tipi sono automaticamente trasformati in uno schema, così il modello sa come e quando chiamarli (function calling). Il framework supporta anche server Model Context Protocol (MCP) e strumenti ospitati come un interprete di codice.

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

Per connetterti invece ad Azure OpenAI in Microsoft Foundry, passa il tuo endpoint e le credenziali al client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Flussi di lavoro multi-agente

Dove il framework si distingue davvero è nell'orchestrare più agenti insieme. Per esempio, puoi eseguire agenti uno dopo l'altro (ognuno passando il proprio contesto al successivo) o distribuire a diversi agenti in parallelo e aggregare i loro risultati:

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

Il prossimo framework agente che esploreremo è [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). È noto come un agente "code-first" perché invece di lavorare strettamente con `stringhe` , può lavorare con DataFrame in Python. Questo diventa estremamente utile per compiti di analisi e generazione dati. Questo può essere cose come creazione di grafici e diagrammi o generazione di numeri casuali.

### Stato e Strumenti

Per gestire lo stato della conversazione, TaskWeaver utilizza il concetto di `Planner`. Il `Planner` è un LLM che prende la richiesta dagli utenti e mappa i compiti che devono essere completati per soddisfare quella richiesta.

Per completare i compiti, il `Planner` ha accesso a una collezione di strumenti chiamati `Plugins`. Questi possono essere classi Python o un interprete di codice generale. Questi plugin sono memorizzati come embedding in modo che il LLM possa cercare meglio il plugin corretto.

![Taskweaver](../../../translated_images/it/taskweaver.da8559999267715a.webp)

Ecco un esempio di un plugin per gestire il rilevamento di anomalie:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Il codice viene verificato prima dell'esecuzione. Un'altra caratteristica per gestire il contesto in Taskweaver è `experience`. L'esperienza consente di conservare a lungo termine il contesto di una conversazione in un file YAML. Questo può essere configurato affinché il LLM migliori nel tempo su determinati compiti dato che è esposto a conversazioni precedenti.

## JARVIS

L'ultimo framework agente che esploreremo è [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ciò che rende JARVIS unico è che utilizza un LLM per gestire lo `stato` della conversazione e gli `strumenti` sono altri modelli di IA. Ciascuno dei modelli IA è specializzato in compiti specifici come il rilevamento di oggetti, la trascrizione o la descrizione di immagini.

![JARVIS](../../../translated_images/it/jarvis.762ddbadbd1a3a33.webp)

L'LLM, essendo un modello generico, riceve la richiesta dall'utente e identifica il compito specifico e qualsiasi argomento/dato necessario per completare il compito.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

L'LLM quindi formatta la richiesta in un modo che il modello AI specializzato possa interpretare, come JSON. Una volta che il modello IA ha restituito la sua previsione basata sul compito, l'LLM riceve la risposta.

Se sono necessari più modelli per completare il compito, interpreterà anche la risposta di quei modelli prima di unirli per generare la risposta all'utente.

L'esempio sotto mostra come funzionerebbe quando un utente richiede una descrizione e il conteggio degli oggetti in un'immagine:

## Compito

Per continuare il tuo apprendimento sugli Agenti IA puoi costruire con Microsoft Agent Framework:

- Un'applicazione che simula una riunione aziendale con diversi dipartimenti di una startup educativa.
- Crea messaggi di sistema che guidano i LLM a comprendere diverse persone e priorità, e permettono all'utente di presentare un'idea di nuovo prodotto.
- Il LLM dovrebbe poi generare domande di approfondimento da ogni dipartimento per affinare e migliorare la presentazione e l'idea del prodotto.

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza dell'IA generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->