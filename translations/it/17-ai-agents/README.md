<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11f03c81f190d9cbafd0f977dcbede6c",
  "translation_date": "2025-06-26T00:16:43+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "it"
}
-->
[![Modelli Open Source](../../../translated_images/17-lesson-banner.a5b918fb0920e4e6d8d391a100f5cb1d5929f4c2752c937d40392905dec82592.it.png)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Introduzione

Gli Agenti AI rappresentano uno sviluppo entusiasmante nell'AI Generativa, permettendo ai Modelli di Linguaggio di Grandi Dimensioni (LLM) di evolvere da assistenti ad agenti capaci di prendere azioni. I framework degli Agenti AI consentono agli sviluppatori di creare applicazioni che danno agli LLM accesso a strumenti e gestione dello stato. Questi framework migliorano anche la visibilità, permettendo agli utenti e agli sviluppatori di monitorare le azioni pianificate dagli LLM, migliorando così la gestione dell'esperienza.

La lezione coprirà i seguenti argomenti:

- Comprendere cosa è un Agente AI - Che cos'è esattamente un Agente AI?
- Esplorare quattro diversi framework di Agenti AI - Cosa li rende unici?
- Applicare questi Agenti AI a diversi casi d'uso - Quando dovremmo usare gli Agenti AI?

## Obiettivi di apprendimento

Dopo aver seguito questa lezione, sarai in grado di:

- Spiegare cosa sono gli Agenti AI e come possono essere utilizzati.
- Avere una comprensione delle differenze tra alcuni dei framework di Agenti AI popolari e come si differenziano.
- Comprendere come funzionano gli Agenti AI per costruire applicazioni con loro.

## Cosa sono gli Agenti AI?

Gli Agenti AI sono un campo molto entusiasmante nel mondo dell'AI Generativa. Con questo entusiasmo, a volte arriva una confusione di termini e della loro applicazione. Per mantenere le cose semplici e inclusive della maggior parte degli strumenti che si riferiscono agli Agenti AI, utilizzeremo questa definizione:

Gli Agenti AI permettono ai Modelli di Linguaggio di Grandi Dimensioni (LLM) di svolgere compiti dando loro accesso a uno **stato** e **strumenti**.

![Modello Agente](../../../translated_images/what-agent.21f2893bdfd01e6a7fd09b0416c2b15594d97f44bbb2ab5a1ff8bf643d2fcb3d.it.png)

Definiamo questi termini:

**Modelli di Linguaggio di Grandi Dimensioni** - Questi sono i modelli citati in tutto il corso come GPT-3.5, GPT-4, Llama-2, ecc.

**Stato** - Questo si riferisce al contesto in cui l'LLM sta lavorando. L'LLM utilizza il contesto delle sue azioni passate e il contesto attuale, guidando il suo processo decisionale per azioni successive. I framework degli Agenti AI permettono agli sviluppatori di mantenere questo contesto più facilmente.

**Strumenti** - Per completare il compito richiesto dall'utente e pianificato dall'LLM, l'LLM ha bisogno di accesso a strumenti. Alcuni esempi di strumenti possono essere un database, un'API, un'applicazione esterna o anche un altro LLM!

Queste definizioni speriamo ti diano una buona base per andare avanti mentre guardiamo a come vengono implementate. Esploriamo alcuni diversi framework di Agenti AI:

## Agenti LangChain

[Agenti LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) è un'implementazione delle definizioni che abbiamo fornito sopra.

Per gestire lo **stato**, utilizza una funzione integrata chiamata `AgentExecutor`. Questa accetta il definito `agent` e il `tools` che sono disponibili.

Il `Agent Executor` memorizza anche la cronologia della chat per fornire il contesto della chat.

![Agenti Langchain](../../../translated_images/langchain-agents.edcc55b5d5c437169a2037211284154561183c58bcec6d4ac2f8a79046fac9af.it.png)

LangChain offre un [catalogo di strumenti](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) che possono essere importati nella tua applicazione in cui l'LLM può avere accesso. Questi sono creati dalla comunità e dal team di LangChain.

Puoi quindi definire questi strumenti e passarli al `Agent Executor`.

La visibilità è un altro aspetto importante quando si parla di Agenti AI. È importante per gli sviluppatori di applicazioni comprendere quale strumento l'LLM sta utilizzando e perché. Per questo, il team di LangChain ha sviluppato LangSmith.

## AutoGen

Il prossimo framework di Agenti AI che discuteremo è [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Il focus principale di AutoGen sono le conversazioni. Gli agenti sono sia **conversabili** che **personalizzabili**.

**Conversabili -** Gli LLM possono iniziare e continuare una conversazione con un altro LLM per completare un compito. Questo viene fatto creando `AssistantAgents` e dando loro un messaggio di sistema specifico.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizzabili** - Gli agenti possono essere definiti non solo come LLM ma come un utente o uno strumento. Come sviluppatore, puoi definire un `UserProxyAgent` che è responsabile dell'interazione con l'utente per il feedback nel completare un compito. Questo feedback può continuare l'esecuzione del compito o fermarlo.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stato e Strumenti

Per cambiare e gestire lo stato, un agente assistente genera codice Python per completare il compito.

Ecco un esempio del processo:

![AutoGen](../../../translated_images/autogen.dee9a25a45fde584fedd84b812a6e31de5a6464687cdb66bb4f2cb7521391856.it.png)

#### LLM Definito con un Messaggio di Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Questo messaggio di sistema indirizza questo specifico LLM alle funzioni rilevanti per il suo compito. Ricorda, con AutoGen puoi avere più AssistantAgents definiti con diversi messaggi di sistema.

#### Chat Iniziata dall'Utente

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Questo messaggio dal proxy utente (Umano) è ciò che avvierà il processo dell'Agente per esplorare le possibili funzioni che dovrebbe eseguire.

#### Funzione Eseguita

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Una volta elaborata la chat iniziale, l'Agente invierà il suggerimento dello strumento da chiamare. In questo caso, è una funzione chiamata `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`. Questi possono essere classi Python o un interprete di codice generale. Questi plugin sono memorizzati come embeddings in modo che l'LLM possa meglio cercare il plugin corretto.

![Taskweaver](../../../translated_images/taskweaver.da8559999267715a95b7677cf9b7d7dd8420aee6f3c484ced1833f081988dcd5.it.png)

Ecco un esempio di un plugin per gestire il rilevamento di anomalie:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Il codice viene verificato prima dell'esecuzione. Un'altra caratteristica per gestire il contesto in Taskweaver è `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` della conversazione e il `tools` sono altri modelli AI. Ciascuno dei modelli AI sono modelli specializzati che svolgono determinati compiti come rilevamento oggetti, trascrizione o didascalia delle immagini.

![JARVIS](../../../translated_images/jarvis.762ddbadbd1a3a3364d4ca3db1a7a9c0d2180060c0f8da6f7bd5b5ea2a115aa7.it.png)

L'LLM, essendo un modello di uso generale, riceve la richiesta dall'utente e identifica il compito specifico e qualsiasi argomento/dato necessario per completare il compito.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

L'LLM quindi formatta la richiesta in modo che il modello AI specializzato possa interpretarla, come JSON. Una volta che il modello AI ha restituito la sua previsione basata sul compito, l'LLM riceve la risposta.

Se sono necessari più modelli per completare il compito, interpreterà anche la risposta di quei modelli prima di unirli per generare la risposta all'utente.

L'esempio seguente mostra come funzionerebbe quando un utente richiede una descrizione e un conteggio degli oggetti in un'immagine:

## Compito

Per continuare il tuo apprendimento sugli Agenti AI puoi costruire con AutoGen:

- Un'applicazione che simula una riunione aziendale con diversi dipartimenti di una startup educativa.
- Creare messaggi di sistema che guidano gli LLM nella comprensione di diverse persone e priorità, e permettere all'utente di presentare una nuova idea di prodotto.
- L'LLM dovrebbe quindi generare domande di follow-up da ciascun dipartimento per perfezionare e migliorare la presentazione e l'idea del prodotto.

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'AI Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'AI Generativa!

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.