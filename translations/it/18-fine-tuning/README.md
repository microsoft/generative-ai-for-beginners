<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "68664f7e754a892ae1d8d5e2b7bd2081",
  "translation_date": "2025-05-20T07:46:24+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "it"
}
-->
[![Modelli Open Source](../../../translated_images/18-lesson-banner.8487555c3e3225eefc1dc84e72c8e00bce1ee76db867a080628fb0fbb04aa0d2.it.png)](https://aka.ms/gen-ai-lesson18-gh?WT.mc_id=academic-105485-koreyst)

# Ottimizzazione del tuo LLM

Utilizzare modelli di linguaggio di grandi dimensioni per costruire applicazioni di intelligenza artificiale generativa comporta nuove sfide. Un problema chiave è garantire la qualità delle risposte (precisione e rilevanza) nel contenuto generato dal modello per una specifica richiesta dell'utente. Nelle lezioni precedenti, abbiamo discusso tecniche come la progettazione del prompt e la generazione aumentata dal recupero che cercano di risolvere il problema _modificando l'input del prompt_ al modello esistente.

Nella lezione di oggi, discutiamo una terza tecnica, **fine-tuning**, che cerca di affrontare la sfida _riaddestrando il modello stesso_ con dati aggiuntivi. Entriamo nei dettagli.

## Obiettivi di apprendimento

Questa lezione introduce il concetto di fine-tuning per modelli di linguaggio pre-addestrati, esplora i vantaggi e le sfide di questo approccio e fornisce indicazioni su quando e come utilizzare il fine-tuning per migliorare le prestazioni dei tuoi modelli di intelligenza artificiale generativa.

Alla fine di questa lezione, dovresti essere in grado di rispondere alle seguenti domande:

- Cos'è il fine-tuning per i modelli di linguaggio?
- Quando e perché è utile il fine-tuning?
- Come posso ottimizzare un modello pre-addestrato?
- Quali sono le limitazioni del fine-tuning?

Pronto? Iniziamo.

## Guida illustrata

Vuoi avere una visione d'insieme di ciò che tratteremo prima di immergerci? Dai un'occhiata a questa guida illustrata che descrive il percorso di apprendimento di questa lezione - dall'apprendimento dei concetti fondamentali e della motivazione per il fine-tuning, alla comprensione del processo e delle migliori pratiche per eseguire il compito di fine-tuning. Questo è un argomento affascinante da esplorare, quindi non dimenticare di controllare la pagina [Risorse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) per ulteriori link a supporto del tuo percorso di apprendimento autonomo!

![Guida illustrata al fine-tuning dei modelli di linguaggio](../../../translated_images/18-fine-tuning-sketchnote.92733966235199dd260184b1aae3a84b877c7496bc872d8e63ad6fa2dd96bafc.it.png)

## Cos'è il fine-tuning per i modelli di linguaggio?

Per definizione, i modelli di linguaggio di grandi dimensioni sono _pre-addestrati_ su grandi quantità di testo provenienti da fonti diverse, inclusi internet. Come abbiamo appreso nelle lezioni precedenti, abbiamo bisogno di tecniche come _la progettazione del prompt_ e _la generazione aumentata dal recupero_ per migliorare la qualità delle risposte del modello alle domande dell'utente ("prompt").

Una tecnica popolare di progettazione del prompt coinvolge fornire al modello più indicazioni su ciò che è atteso nella risposta, sia fornendo _istruzioni_ (indicazioni esplicite) o _dandogli alcuni esempi_ (indicazioni implicite). Questo è chiamato _apprendimento con pochi esempi_, ma ha due limitazioni:

- I limiti di token del modello possono restringere il numero di esempi che puoi fornire e limitare l'efficacia.
- I costi dei token del modello possono rendere costoso aggiungere esempi a ogni prompt e limitare la flessibilità.

Il fine-tuning è una pratica comune nei sistemi di apprendimento automatico in cui prendiamo un modello pre-addestrato e lo riaddestriamo con nuovi dati per migliorare le sue prestazioni su un compito specifico. Nel contesto dei modelli di linguaggio, possiamo ottimizzare il modello pre-addestrato _con un insieme curato di esempi per un compito o dominio applicativo specifico_ per creare un **modello personalizzato** che potrebbe essere più preciso e rilevante per quel compito o dominio specifico. Un vantaggio collaterale del fine-tuning è che può anche ridurre il numero di esempi necessari per l'apprendimento con pochi esempi - riducendo l'uso di token e i costi correlati.

## Quando e perché dovremmo ottimizzare i modelli?

In _questo_ contesto, quando parliamo di fine-tuning, ci riferiamo al fine-tuning **supervisionato** dove il riaddestramento viene fatto **aggiungendo nuovi dati** che non facevano parte del dataset di addestramento originale. Questo è diverso da un approccio di fine-tuning non supervisionato dove il modello viene riaddestrato sui dati originali, ma con iperparametri diversi.

La cosa chiave da ricordare è che il fine-tuning è una tecnica avanzata che richiede un certo livello di competenza per ottenere i risultati desiderati. Se fatto in modo errato, potrebbe non fornire i miglioramenti attesi e potrebbe persino degradare le prestazioni del modello per il tuo dominio mirato.

Quindi, prima di imparare "come" ottimizzare i modelli di linguaggio, devi sapere "perché" dovresti prendere questa strada e "quando" iniziare il processo di fine-tuning. Inizia ponendoti queste domande:

- **Caso d'uso**: Qual è il tuo _caso d'uso_ per il fine-tuning? Quale aspetto del modello pre-addestrato attuale vuoi migliorare?
- **Alternative**: Hai provato _altre tecniche_ per ottenere i risultati desiderati? Usale per creare un punto di riferimento per il confronto.
  - Progettazione del prompt: Prova tecniche come il prompting con pochi esempi con esempi di risposte pertinenti al prompt. Valuta la qualità delle risposte.
  - Generazione Aumentata dal Recupero: Prova ad aumentare i prompt con i risultati delle query recuperati cercando i tuoi dati. Valuta la qualità delle risposte.
- **Costi**: Hai identificato i costi per il fine-tuning?
  - Ottimizzabilità - il modello pre-addestrato è disponibile per il fine-tuning?
  - Sforzo - per preparare i dati di addestramento, valutare e affinare il modello.
  - Calcolo - per eseguire i lavori di fine-tuning e distribuire il modello ottimizzato
  - Dati - accesso a esempi di qualità sufficiente per l'impatto del fine-tuning
- **Benefici**: Hai confermato i benefici per il fine-tuning?
  - Qualità - il modello ottimizzato ha superato il punto di riferimento?
  - Costo - riduce l'uso di token semplificando i prompt?
  - Estensibilità - puoi riutilizzare il modello di base per nuovi domini?

Rispondendo a queste domande, dovresti essere in grado di decidere se il fine-tuning è l'approccio giusto per il tuo caso d'uso. Idealmente, l'approccio è valido solo se i benefici superano i costi. Una volta deciso di procedere, è il momento di pensare a _come_ puoi ottimizzare il modello pre-addestrato.

Vuoi ottenere più informazioni sul processo decisionale? Guarda [Ottimizzare o non ottimizzare](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Come possiamo ottimizzare un modello pre-addestrato?

Per ottimizzare un modello pre-addestrato, hai bisogno di:

- un modello pre-addestrato da ottimizzare
- un dataset da utilizzare per il fine-tuning
- un ambiente di addestramento per eseguire il lavoro di fine-tuning
- un ambiente di hosting per distribuire il modello ottimizzato

## Fine-Tuning in Azione

Le seguenti risorse forniscono tutorial passo-passo per guidarti attraverso un esempio reale utilizzando un modello selezionato con un dataset curato. Per seguire questi tutorial, hai bisogno di un account sul provider specifico, insieme all'accesso al modello e ai dataset pertinenti.

| Provider     | Tutorial                                                                                                                                                                       | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Come ottimizzare i modelli di chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)          | Impara a ottimizzare un `gpt-35-turbo` per un dominio specifico ("assistente di ricette") preparando i dati di addestramento, eseguendo il lavoro di fine-tuning e utilizzando il modello ottimizzato per l'inferenza.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Tutorial di fine-tuning GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Impara a ottimizzare un modello `gpt-35-turbo-0613` **su Azure** seguendo i passaggi per creare e caricare i dati di addestramento, eseguire il lavoro di fine-tuning. Distribuisci e usa il nuovo modello.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Fine-tuning dei LLM con Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Questo post sul blog ti guida nell'ottimizzazione di un _LLM aperto_ (es: `CodeLlama 7B`) utilizzando la libreria [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) e [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) con dataset aperti [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) su Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning dei LLM con AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (o AutoTrain Advanced) è una libreria Python sviluppata da Hugging Face che consente il fine-tuning per molti compiti diversi, incluso il fine-tuning dei LLM. AutoTrain è una soluzione senza codice e il fine-tuning può essere fatto nel tuo cloud, su Hugging Face Spaces o localmente. Supporta sia un'interfaccia grafica basata sul web, CLI e l'addestramento tramite file di configurazione yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Compito

Seleziona uno dei tutorial sopra e seguilo. _Potremmo replicare una versione di questi tutorial in Jupyter Notebooks in questo repository solo per riferimento. Utilizza le fonti originali direttamente per ottenere le versioni più recenti_.

## Ottimo lavoro! Continua il tuo apprendimento.

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'intelligenza artificiale generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza dell'intelligenza artificiale generativa!

Congratulazioni!! Hai completato l'ultima lezione della serie v2 per questo corso! Non smettere di imparare e costruire. \*\*Dai un'occhiata alla pagina [RISORSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) per un elenco di suggerimenti aggiuntivi solo per questo argomento.

La nostra serie di lezioni v1 è stata anche aggiornata con più compiti e concetti. Quindi prenditi un minuto per rinfrescare la tua conoscenza - e per favore [condividi le tue domande e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) per aiutarci a migliorare queste lezioni per la comunità.

**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.