[![Modelli Open Source](../../../translated_images/it/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning del Tuo LLM

Usare i grandi modelli linguistici per costruire applicazioni di intelligenza artificiale generativa comporta nuove sfide. Un problema chiave è garantire la qualità della risposta (accuratezza e pertinenza) nel contenuto generato dal modello per una data richiesta dell'utente. Nelle lezioni precedenti, abbiamo discusso tecniche come il prompt engineering e la generazione aumentata da retrieval che cercano di risolvere il problema _modificando l'input prompt_ al modello esistente.

Nella lezione di oggi, discutiamo una terza tecnica, il **fine-tuning**, che cerca di affrontare la sfida _riaddestrando il modello stesso_ con dati aggiuntivi. Approfondiamo i dettagli.

## Obiettivi di Apprendimento

Questa lezione introduce il concetto di fine-tuning per modelli linguistici pre-allenati, esplora i benefici e le sfide di questo approccio, e fornisce indicazioni su quando e come usare il fine-tuning per migliorare le prestazioni dei tuoi modelli di intelligenza artificiale generativa.

Al termine di questa lezione, dovresti essere in grado di rispondere alle seguenti domande:

- Cos'è il fine-tuning per i modelli linguistici?
- Quando e perché il fine-tuning è utile?
- Come posso fare il fine-tuning di un modello pre-addestrato?
- Quali sono i limiti del fine-tuning?

Pronto? Iniziamo.

## Guida Illustrata

Vuoi avere una panoramica di ciò che affronteremo prima di immergerci? Dai un'occhiata a questa guida illustrata che descrive il percorso di apprendimento per questa lezione - dall'apprendere i concetti principali e la motivazione per il fine-tuning, fino a capire il processo e le migliori pratiche per eseguire il compito di fine-tuning. È un argomento affascinante da esplorare, quindi non dimenticare di visitare la pagina [Risorse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) per ulteriori link a supporto del tuo percorso di apprendimento autonomo!

![Guida Illustrata al Fine Tuning dei Modelli Linguistici](../../../translated_images/it/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Cos'è il fine-tuning per i modelli linguistici?

Per definizione, i grandi modelli linguistici sono _pre-addestrati_ su grandi quantità di testo provenienti da fonti diverse incluso internet. Come abbiamo imparato nelle lezioni precedenti, abbiamo bisogno di tecniche come _prompt engineering_ e _generazione aumentata da retrieval_ per migliorare la qualità delle risposte del modello alle domande ("prompt") dell'utente.

Una tecnica popolare di prompt engineering implica fornire al modello maggiori indicazioni su cosa ci si aspetta nella risposta, sia dando _istruzioni_ (indicazioni esplicite) sia _dando qualche esempio_ (indicazioni implicite). Questo è chiamato _few-shot learning_ ma ha due limitazioni:

- I limiti di token del modello possono restringere il numero di esempi che puoi fornire e limitarne l'efficacia.
- I costi dei token del modello possono rendere costoso aggiungere esempi a ogni prompt e limitare la flessibilità.

Il fine-tuning è una pratica comune nei sistemi di machine learning dove si prende un modello pre-addestrato e lo si riaddestra con nuovi dati per migliorarne le prestazioni su un compito specifico. Nel contesto dei modelli linguistici, possiamo fare il fine-tuning del modello pre-addestrato _con un insieme selezionato di esempi per un dato compito o dominio applicativo_ per creare un **modello personalizzato** che può essere più accurato e pertinente per quel compito o dominio specifico. Un beneficio collaterale del fine-tuning è che può anche ridurre il numero di esempi necessari per il few-shot learning - riducendo l'uso di token e i costi correlati.

## Quando e perché dovremmo fare il fine-tuning dei modelli?

In _questo_ contesto, quando parliamo di fine-tuning intendiamo il fine-tuning **supervisionato** dove il riaddestramento è fatto **aggiungendo nuovi dati** che non facevano parte del dataset originale di addestramento. Questo è diverso da un approccio di fine-tuning non supervisionato dove il modello è riaddestrato sui dati originali, ma con iperparametri differenti.

La cosa principale da ricordare è che il fine-tuning è una tecnica avanzata che richiede un certo livello di competenza per ottenere i risultati desiderati. Se fatto in modo errato, potrebbe non fornire i miglioramenti attesi e potrebbe perfino degradare le prestazioni del modello per il dominio target.

Quindi, prima di imparare "come" fare il fine-tuning dei modelli linguistici, devi sapere "perché" dovresti prendere questa strada e "quando" iniziare il processo di fine-tuning. Inizia ponendoti queste domande:

- **Caso d'Uso**: Qual è il tuo _caso d'uso_ per il fine-tuning? Quale aspetto del modello pre-addestrato attuale vuoi migliorare?
- **Alternative**: Hai provato _altre tecniche_ per raggiungere i risultati desiderati? Usale per creare una baseline di confronto.
  - Prompt engineering: Prova tecniche come il few-shot prompting con esempi di risposte rilevanti al prompt. Valuta la qualità delle risposte.
  - Generazione Aumentata da Retrieval: Prova ad aumentare i prompt con risultati di query estratti dai tuoi dati. Valuta la qualità delle risposte.
- **Costi**: Hai identificato i costi del fine-tuning?
  - Possibilità di tuning - il modello pre-addestrato è disponibile per il fine-tuning?
  - Sforzo - per preparare i dati di addestramento, valutare e perfezionare il modello.
  - Risorse computazionali - per eseguire i lavori di fine-tuning e distribuire il modello fine-tuned.
  - Dati - accesso a esempi di qualità sufficiente per l'impatto del fine-tuning.
- **Benefici**: Hai confermato i benefici del fine-tuning?
  - Qualità - il modello fine-tuned ha superato la baseline?
  - Costo - riduce l'uso dei token semplificando i prompt?
  - Estendibilità - puoi riutilizzare il modello base per nuovi domini?

Rispondendo a queste domande, dovresti essere in grado di decidere se il fine-tuning è l'approccio giusto per il tuo caso d'uso. Idealmente, l'approccio è valido solo se i benefici superano i costi. Una volta deciso di procedere, è tempo di pensare a _come_ fare il fine-tuning del modello pre-addestrato.

Vuoi ottenere più approfondimenti sul processo decisionale? Guarda [Fare il fine-tuning o non farlo](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Come possiamo fare il fine-tuning di un modello pre-addestrato?

Per fare il fine-tuning di un modello pre-addestrato, devi avere:

- un modello pre-addestrato da fine-tunare
- un dataset da usare per il fine-tuning
- un ambiente di addestramento per eseguire il lavoro di fine-tuning
- un ambiente di hosting per distribuire il modello fine-tuned

## Fine-Tuning in Azione

> **Nota:** `gpt-35-turbo` / `gpt-3.5-turbo`, citati in alcuni tutorial qui sotto, sono ritirati sia per l'inferenza che per il fine-tuning. Se oggi inizi un nuovo lavoro di fine-tuning, punta su un modello attualmente supportato invece - per esempio `gpt-4o-mini` o `gpt-4.1-mini`. Vedi la [lista dei modelli per fine-tuning](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) per l'insieme attuale di modelli fine-tunabili. I concetti e i passaggi in questi tutorial sono ancora validi.

Le risorse seguenti forniscono tutorial passo passo per guidarti attraverso un esempio reale usando un modello selezionato con un dataset curato. Per seguire questi tutorial, hai bisogno di un account presso il provider specifico, insieme all'accesso al modello e ai dataset rilevanti.

| Provider     | Tutorial                                                                                                                                                                       | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Come fare il fine-tuning dei modelli di chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Impara a fare il fine-tuning di un `gpt-35-turbo` per un dominio specifico ("assistente ricette") preparando i dati di addestramento, eseguendo il lavoro di fine-tuning, e usando il modello fine-tunato per l'inferenza.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Tutorial sul fine-tuning di GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Impara a fare il fine-tuning di un modello `gpt-35-turbo-0613` **su Azure** seguendo i passaggi per creare e caricare dati di addestramento, eseguire il lavoro di fine-tuning. Distribuire e usare il nuovo modello.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Fine-tuning LLMs con Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Questo post sul blog ti guida nel fare il fine-tuning di un _LLM open_ (es.: `CodeLlama 7B`) usando la libreria [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) e [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) con dataset aperti [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) su Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs con AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (o AutoTrain Advanced) è una libreria python sviluppata da Hugging Face che permette il fine-tuning per molti compiti diversi inclusi i LLM. AutoTrain è una soluzione no-code e il fine-tuning può essere fatto nella tua cloud, su Hugging Face Spaces o localmente. Supporta sia una GUI web, CLI e l’addestramento tramite file di configurazione yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs con Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth è un framework open source che supporta il fine-tuning e il reinforcement learning (RL) per LLM. Unsloth semplifica l’addestramento locale, la valutazione e il deployment con [notebook] pronti all'uso (https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Supporta anche text-to-speech (TTS), BERT e modelli multimodali. Per iniziare, leggi la loro guida passo-passo [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Compito

Seleziona uno dei tutorial sopra e seguilo. _Potremmo replicare una versione di questi tutorial in Jupyter Notebooks in questo repo solo a scopo di riferimento. Usa direttamente le fonti originali per ottenere le versioni più aggiornate_.

## Ottimo lavoro! Continua il tuo apprendimento.

Dopo aver completato questa lezione, visita la nostra [collezione di apprendimento sull'IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'Intelligenza Artificiale Generativa!

Congratulazioni!! Hai completato la lezione finale della serie v2 di questo corso! Non smettere di imparare e costruire. \*\*Dai un'occhiata alla pagina [RISORSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) per un elenco di ulteriori suggerimenti solo su questo argomento.

La nostra serie v1 di lezioni è stata aggiornata anch'essa con più compiti e concetti. Quindi prenditi un minuto per rinfrescare le tue conoscenze - e per favore [condividi le tue domande e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) per aiutarci a migliorare queste lezioni per la comunità.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->