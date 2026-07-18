[![Modelli Open Source](../../../translated_images/it/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning del tuo LLM

Utilizzare grandi modelli di linguaggio per costruire applicazioni di intelligenza artificiale generativa comporta nuove sfide. Una questione chiave è garantire la qualità della risposta (accuratezza e pertinenza) nel contenuto generato dal modello per una specifica richiesta dell'utente. Nelle lezioni precedenti, abbiamo discusso tecniche come l'ingegneria del prompt e la generazione aumentata da recupero che cercano di risolvere il problema *modificando l'input del prompt* al modello esistente.

Nella lezione di oggi, discutiamo una terza tecnica, il **fine-tuning**, che cerca di affrontare la sfida *riaddestrando il modello stesso* con dati aggiuntivi. Approfondiamo i dettagli.

## Obiettivi di Apprendimento

Questa lezione introduce il concetto di fine-tuning per modelli di linguaggio pre-addestrati, esplora i vantaggi e le sfide di questo approccio e fornisce indicazioni su quando e come utilizzare il fine-tuning per migliorare le prestazioni dei tuoi modelli di intelligenza artificiale generativa.

Alla fine di questa lezione, dovresti essere in grado di rispondere alle seguenti domande:

- Cos'è il fine-tuning per modelli di linguaggio?
- Quando e perché il fine-tuning è utile?
- Come posso effettuare il fine-tuning di un modello pre-addestrato?
- Quali sono i limiti del fine-tuning?

Pronti? Iniziamo.

## Guida Illustrata

Vuoi avere una panoramica di cosa tratteremo prima di addentrarci? Dai un’occhiata a questa guida illustrata che descrive il percorso di apprendimento per questa lezione - dall’apprendere i concetti base e la motivazione del fine-tuning, alla comprensione del processo e delle migliori pratiche per eseguire il fine-tuning. È un argomento affascinante da esplorare, quindi non dimenticare di consultare la pagina [Risorse](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) per link aggiuntivi a supporto del tuo percorso di apprendimento autonomo!

![Guida Illustrata al Fine-Tuning dei Modelli di Linguaggio](../../../translated_images/it/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Cos'è il fine-tuning per modelli di linguaggio?

Per definizione, i grandi modelli di linguaggio sono *pre-addestrati* su grandi quantità di testo proveniente da fonti diverse, incluso internet. Come abbiamo imparato nelle lezioni precedenti, abbiamo bisogno di tecniche come *prompt engineering* e *generazione aumentata da recupero* per migliorare la qualità delle risposte del modello alle domande dell’utente ("prompt").

Una tecnica popolare di prompt engineering consiste nel fornire al modello una maggiore guida su cosa ci si aspetta nella risposta, sia fornendo *istruzioni* (guida esplicita) sia *fornendo qualche esempio* (guida implicita). Questo è noto come *few-shot learning* ma presenta due limitazioni:

- I limiti di token del modello possono restringere il numero di esempi che puoi fornire, limitandone l’efficacia.
- I costi in token del modello possono rendere costoso aggiungere esempi a ogni prompt, limitandone la flessibilità.

Il fine-tuning è una pratica comune nei sistemi di machine learning dove si prende un modello pre-addestrato e lo si riaddestra con nuovi dati per migliorarne le prestazioni su un compito specifico. Nel contesto dei modelli di linguaggio, possiamo effettuare il fine-tuning del modello pre-addestrato *con un set curato di esempi per un dato compito o dominio applicativo* per creare un **modello personalizzato** che può essere più accurato e rilevante per quel compito o dominio specifico. Un vantaggio secondario del fine-tuning è che può anche ridurre il numero di esempi necessari per il few-shot learning - riducendo l’uso di token e i costi correlati.

## Quando e perché dovremmo fare fine-tuning ai modelli?

In *questo* contesto, quando parliamo di fine-tuning, ci riferiamo al fine-tuning **supervisionato** dove il riaddestramento si fa **aggiungendo nuovi dati** che non facevano parte del dataset originale di addestramento. Questo è diverso dall’approccio di fine-tuning non supervisionato dove il modello viene riaddestrato sui dati originali, ma con iperparametri diversi.

La cosa principale da ricordare è che il fine-tuning è una tecnica avanzata che richiede un certo livello di competenza per ottenere i risultati desiderati. Se fatto in modo errato, potrebbe non fornire i miglioramenti attesi, e può anche degradare le prestazioni del modello per il dominio target.

Quindi, prima di imparare "come" fare fine-tuning ai modelli di linguaggio, devi sapere "perché" dovresti prendere questa strada, e "quando" iniziare il processo di fine-tuning. Inizia ponendoti queste domande:

- **Caso d'Uso**: Qual è il tuo *caso d’uso* per il fine-tuning? Quale aspetto del modello pre-addestrato attuale vuoi migliorare?
- **Alternative**: Hai provato *altre tecniche* per ottenere i risultati desiderati? Usale per creare una base di confronto.
  - Prompt engineering: Prova tecniche come few-shot prompting con esempi di risposte di prompt rilevanti. Valuta la qualità delle risposte.
  - Generazione Aumentata da Recupero: Prova ad arricchire i prompt con risultati di query recuperati dalla ricerca sui tuoi dati. Valuta la qualità delle risposte.
- **Costi**: Hai identificato i costi del fine-tuning?
  - Sintonizzabilità - il modello pre-addestrato è disponibile per il fine-tuning?
  - Sforzo - per preparare i dati di addestramento, valutare e rifinire il modello.
  - Calcolo - per eseguire i job di fine-tuning e distribuire il modello fine-tuned
  - Dati - accesso a esempi di qualità sufficienti per l’impatto del fine-tuning
- **Benefici**: Hai confermato i benefici del fine-tuning?
  - Qualità - il modello fine-tuned ha superato la baseline?
  - Costo - riduce l’uso di token semplificando i prompt?
  - Estendibilità - puoi riutilizzare il modello base per nuovi domini?

Rispondendo a queste domande dovresti essere in grado di decidere se il fine-tuning è l’approccio giusto per il tuo caso d’uso. Idealmente, l’approccio è valido solo se i benefici superano i costi. Una volta deciso di procedere, è tempo di pensare a *come* puoi effettuare il fine-tuning del modello pre-addestrato.

Vuoi approfondire il processo decisionale? Guarda [Fare fine-tuning o non farlo](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Come possiamo fare il fine-tuning di un modello pre-addestrato?

Per fare il fine-tuning di un modello pre-addestrato, hai bisogno di:

- un modello pre-addestrato da fine-tunare
- un dataset da usare per il fine-tuning
- un ambiente di addestramento dove eseguire il job di fine-tuning
- un ambiente di hosting per distribuire il modello fine-tuned

## Fine-Tuning su Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) è il luogo dove oggi puoi fare fine-tuning, distribuire e gestire modelli personalizzati su Azure (unendo ciò che prima era Azure OpenAI Studio e Azure AI Studio). Prima di avviare un lavoro, è utile capire le scelte che Foundry ti offre - e le migliori pratiche raccomandate dalla piattaforma. Sotto il cofano, Foundry usa **LoRA (low-rank adaptation)** per fare fine-tuning in modo efficiente, mantenendo l’addestramento più rapido ed economico rispetto al riaddestramento di ogni singolo peso.

### Passo 1: Scegli una tecnica di addestramento

Foundry supporta tre tecniche di fine-tuning. **Inizia con SFT** - copre la più ampia gamma di scenari.

| Tecnica | Cosa fa | Quando usarla |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Addestra su coppie di esempi input/output affinché il modello impari a produrre le risposte desiderate. | Predefinita per la maggior parte dei compiti: specializzazione di dominio, prestazioni sul compito, stile e tono, seguire istruzioni e adattamento linguistico. |
| **Direct Preference Optimization (DPO)** | Impara da coppie di risposte *preferite vs. non preferite* per allineare le uscite alle preferenze umane. | Miglioramento della qualità della risposta, sicurezza e allineamento quando hai feedback comparativi. |
| **Reinforcement Fine-Tuning (RFT)** | Utilizza segnali di ricompensa da *valutatori* per ottimizzare comportamenti complessi con l’apprendimento per rinforzo. | Domini oggettivi, ricchi di ragionamento (matematica, chimica, fisica) con risposte chiare giuste/sbagliate. Richiede più competenze ML. |

### Passo 2: Scegli un livello di addestramento

Foundry ti permette di scegliere come e dove si esegue l’addestramento:

- **Standard** - addestra nella regione delle tue risorse e garantisce la residenza dei dati. Usalo quando i dati devono restare in una regione specifica.
- **Global** - più economico e veloce per la coda usando capacità oltre la tua regione (i dati e i pesi sono copiati nella regione di addestramento). Un buon default quando la residenza dei dati non è un requisito.
- **Developer** - il costo più basso, usando capacità inattiva senza garanzie di latenza/SLA (i job possono essere interrotti e ripresi). Ideale per sperimentazione.

### Passo 3: Scegli un modello base

I modelli fine-tunabili includono OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, e `gpt-4.1-nano` (SFT; la famiglia 4o/4.1 supporta anche DPO), i modelli di ragionamento `o4-mini` e `gpt-5` (RFT), più modelli open-source come `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, e `gpt-oss-20b` (SFT su risorse Foundry). Controlla sempre l’attuale [lista dei modelli per fine-tuning](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) per metodi supportati, regioni e disponibilità.

> Foundry offre due modalità: **serverless** (prezzi a consumo, nessuna quota GPU da gestire, OpenAI e modelli selezionati) e **managed compute** (porta le tue VM tramite Azure Machine Learning per la più ampia gamma di modelli). La maggior parte dovrebbe iniziare con serverless.

### Migliori pratiche di Foundry

- **Prima la baseline.** Misura il modello base con prompt engineering e RAG *prima* di fare fine-tuning, così puoi dimostrare i miglioramenti.
- **Inizia in piccolo, poi scala.** Parti con 50-100 esempi di alta qualità per validare l’approccio, poi sali a 500+ per la produzione. La qualità batte la quantità - pota gli esempi di bassa qualità.
- **Formatta correttamente i dati.** I file di training e validazione devono essere JSONL, UTF-8 **con BOM**, sotto i 512 MB, usando il formato messaggi chat-completions. Includi sempre un file di validazione per monitorare l’overfitting.
- **Mantieni il prompt di sistema durante l’inferenza.** Usa lo stesso messaggio di sistema quando chiami il modello che hai usato durante l’addestramento.
- **Valuta i checkpoint - non distribuire ciecamente l’ultimo.** Foundry mantiene gli ultimi tre epoch come checkpoint distribuibili; scegli quello che generalizza meglio guardando `train_loss` / `valid_loss` e accuratezza sui token.
- **Misura il costo in token insieme alla qualità** quando confronti il modello fine-tuned con la baseline.
- **Itera con fine-tuning continuo.** Puoi rifinire un modello già fine-tuned su nuovi dati (supportato per modelli OpenAI).
- **Tieni d’occhio i costi di hosting.** Un modello personalizzato distribuito fattura all’ora, e una distribuzione inattiva viene rimossa dopo 15 giorni - pulisci ciò che non ti serve.

Segui la guida passo-passo in [Personalizza un modello con fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), e consulta le guide per [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) e [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) quando sei pronto per le altre tecniche.

## Fine-Tuning in Azione

Le seguenti risorse offrono tutorial passo-passo che ti guidano attraverso un esempio reale su un modello attualmente supportato con un dataset curato. Per seguirli, hai bisogno di un account presso il provider specifico, insieme all’accesso al modello e ai dataset rilevanti.

| Provider     | Tutorial                                                                                                                                                                       | Descrizione                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Come fare fine-tuning a modelli chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Impara a fare fine-tuning a un modello chat recente di OpenAI per un dominio specifico ("assistente ricette") preparando i dati di training, eseguendo il job di fine-tuning, e usando il modello fine-tuned per l’inferenza.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Personalizza un modello con fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Impara a fare fine-tuning a un modello attualmente supportato come `gpt-4.1-mini` **su Azure** con Microsoft Foundry: prepara e carica i dati di training e validazione, esegui il job di fine-tuning, poi distribuisci e usa il nuovo modello.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Questo post del blog ti guida nel fine-tuning di un _LLM aperto_ (es: `CodeLlama 7B`) usando la libreria [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) con [dataset](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) aperti su Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (o AutoTrain Advanced) è una libreria python sviluppata da Hugging Face che consente il fine-tuning per molteplici compiti incluso il fine-tuning di LLM. AutoTrain è una soluzione senza codice e il fine-tuning può essere fatto nel tuo cloud, su Hugging Face Spaces o localmente. Supporta sia un’interfaccia web GUI, CLI e il training tramite file di configurazione yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth è un framework open-source che supporta il fine-tuning degli LLM e il reinforcement learning (RL). Unsloth semplifica il training locale, la valutazione e il deployment con [notebook](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) pronti all’uso. Supporta anche modelli text-to-speech (TTS), BERT e multimodali. Per iniziare, leggi la loro guida passo-passo [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Compito

Seleziona uno dei tutorial sopra e seguilo passo passo. _Potremmo replicare una versione di questi tutorial in Jupyter Notebooks in questo repository solo come riferimento. Si prega di utilizzare direttamente le fonti originali per ottenere le versioni più aggiornate_.

## Ottimo lavoro! Continua ad imparare.

Dopo aver completato questa lezione, consulta la nostra [collezione di apprendimento sull’IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza sull’IA Generativa!

Congratulazioni!! Hai completato l’ultima lezione della serie v2 di questo corso! Non smettere di imparare e costruire. \*\*Consulta la pagina [RISORSE](RESOURCES.md?WT.mc_id=academic-105485-koreyst) per una lista di suggerimenti aggiuntivi solo su questo argomento.

La nostra serie di lezioni v1 è stata aggiornata con più compiti e concetti. Quindi prenditi un minuto per rinfrescare le tue conoscenze - e per favore [condividi le tue domande e feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) per aiutarci a migliorare queste lezioni per la comunità.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->