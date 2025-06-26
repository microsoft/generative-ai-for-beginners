<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:33:44+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "it"
}
-->
# Fondamenti di Ingegneria dei Prompt

## Introduzione

Questo modulo copre concetti e tecniche essenziali per creare prompt efficaci nei modelli di AI generativa. Anche il modo in cui scrivi il tuo prompt a un LLM è importante. Un prompt ben elaborato può ottenere una risposta di qualità migliore. Ma cosa significano esattamente termini come _prompt_ e _ingegneria dei prompt_? E come posso migliorare l'_input_ del prompt che invio all'LLM? Queste sono le domande a cui cercheremo di rispondere in questo capitolo e nel prossimo.

L'_AI generativa_ è in grado di creare nuovi contenuti (ad esempio, testi, immagini, audio, codice, ecc.) in risposta alle richieste degli utenti. Lo fa utilizzando _Modelli di Linguaggio di Grandi Dimensioni_ come la serie GPT ("Generative Pre-trained Transformer") di OpenAI, che sono addestrati per utilizzare il linguaggio naturale e il codice.

Gli utenti possono ora interagire con questi modelli utilizzando paradigmi familiari come la chat, senza necessitare di competenze tecniche o formazione. I modelli sono _basati su prompt_ - gli utenti inviano un input testuale (prompt) e ricevono la risposta dell'AI (completamento). Possono quindi "chattare con l'AI" iterativamente, in conversazioni multi-turno, affinando il loro prompt fino a quando la risposta non corrisponde alle loro aspettative.

I "prompt" diventano ora l'interfaccia _principale di programmazione_ per le app di AI generativa, indicando ai modelli cosa fare e influenzando la qualità delle risposte restituite. L'"ingegneria dei prompt" è un campo di studio in rapida crescita che si concentra sulla _progettazione e ottimizzazione_ dei prompt per fornire risposte coerenti e di qualità su larga scala.

## Obiettivi di Apprendimento

In questa lezione, impariamo cos'è l'Ingegneria dei Prompt, perché è importante e come possiamo creare prompt più efficaci per un determinato modello e obiettivo applicativo. Comprenderemo i concetti fondamentali e le migliori pratiche per l'ingegneria dei prompt - e apprenderemo un ambiente interattivo di "sandbox" con Jupyter Notebooks dove possiamo vedere questi concetti applicati a esempi reali.

Alla fine di questa lezione saremo in grado di:

1. Spiegare cos'è l'ingegneria dei prompt e perché è importante.
2. Descrivere i componenti di un prompt e come vengono utilizzati.
3. Imparare le migliori pratiche e tecniche per l'ingegneria dei prompt.
4. Applicare le tecniche apprese a esempi reali, utilizzando un endpoint OpenAI.

## Termini Chiave

Ingegneria dei Prompt: La pratica di progettare e affinare gli input per guidare i modelli di AI verso la produzione di output desiderati.
Tokenizzazione: Il processo di conversione del testo in unità più piccole, chiamate token, che un modello può comprendere e elaborare.
LLM Sintonizzati su Istruzioni: Modelli di Linguaggio di Grandi Dimensioni (LLM) che sono stati perfezionati con istruzioni specifiche per migliorare l'accuratezza e la rilevanza delle loro risposte.

## Sandbox di Apprendimento

L'ingegneria dei prompt è attualmente più un'arte che una scienza. Il modo migliore per migliorare la nostra intuizione è _praticare di più_ e adottare un approccio di tentativi ed errori che combini l'esperienza del dominio applicativo con tecniche raccomandate e ottimizzazioni specifiche del modello.

Il Jupyter Notebook che accompagna questa lezione fornisce un ambiente _sandbox_ dove puoi provare ciò che impari - man mano che procedi o come parte della sfida di codice alla fine. Per eseguire gli esercizi, avrai bisogno di:

1. **Una chiave API Azure OpenAI** - l'endpoint del servizio per un LLM distribuito.
2. **Un Runtime Python** - in cui il Notebook può essere eseguito.
3. **Variabili d'Ambiente Locali** - _completa ora i passaggi di [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) per prepararti_.

Il notebook viene fornito con esercizi _di partenza_ - ma sei incoraggiato ad aggiungere le tue sezioni di _Markdown_ (descrizione) e _Codice_ (richieste di prompt) per provare più esempi o idee - e costruire la tua intuizione per il design dei prompt.

## Guida Illustrata

Vuoi avere una visione d'insieme di ciò che copre questa lezione prima di immergerti? Dai un'occhiata a questa guida illustrata, che ti dà un'idea dei principali argomenti trattati e dei punti chiave da considerare in ciascuno. La roadmap della lezione ti porta dalla comprensione dei concetti fondamentali e delle sfide all'affrontarle con tecniche e migliori pratiche di ingegneria dei prompt pertinenti. Nota che la sezione "Tecniche Avanzate" in questa guida si riferisce ai contenuti trattati nel _prossimo_ capitolo di questo curriculum.

## La Nostra Startup

Ora, parliamo di come _questo argomento_ si relaziona alla nostra missione di startup di [portare l'innovazione AI nell'educazione](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vogliamo costruire applicazioni AI-powered di _apprendimento personalizzato_ - quindi pensiamo a come diversi utenti della nostra applicazione potrebbero "progettare" i prompt:

- **Amministratori** potrebbero chiedere all'AI di _analizzare i dati del curriculum per identificare lacune nella copertura_. L'AI può riassumere i risultati o visualizzarli con il codice.
- **Educatori** potrebbero chiedere all'AI di _generare un piano di lezione per un pubblico e un argomento target_. L'AI può costruire il piano personalizzato in un formato specificato.
- **Studenti** potrebbero chiedere all'AI di _tutorarli in una materia difficile_. L'AI può ora guidare gli studenti con lezioni, suggerimenti ed esempi adattati al loro livello.

Questo è solo la punta dell'iceberg. Dai un'occhiata a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una libreria di prompt open-source curata da esperti di educazione - per avere un'idea più ampia delle possibilità! _Prova a eseguire alcuni di questi prompt nel sandbox o utilizzando l'OpenAI Playground per vedere cosa succede!_

## Cos'è l'Ingegneria dei Prompt?

Abbiamo iniziato questa lezione definendo **Ingegneria dei Prompt** come il processo di _progettazione e ottimizzazione_ degli input testuali (prompt) per fornire risposte coerenti e di qualità (completamenti) per un determinato obiettivo applicativo e modello. Possiamo pensare a questo come a un processo in 2 fasi:

- _progettare_ il prompt iniziale per un dato modello e obiettivo
- _affinare_ il prompt iterativamente per migliorare la qualità della risposta

Questo è necessariamente un processo di tentativi ed errori che richiede intuizione e sforzo da parte dell'utente per ottenere risultati ottimali. Quindi perché è importante? Per rispondere a questa domanda, dobbiamo prima comprendere tre concetti:

- _Tokenizzazione_ = come il modello "vede" il prompt
- _LLM di Base_ = come il modello di base "processa" un prompt
- _LLM Sintonizzati su Istruzioni_ = come il modello può ora vedere i "compiti"

### Tokenizzazione

Un LLM vede i prompt come una _sequenza di token_ dove modelli diversi (o versioni di un modello) possono tokenizzare lo stesso prompt in modi diversi. Poiché gli LLM sono addestrati sui token (e non sul testo grezzo), il modo in cui i prompt vengono tokenizzati ha un impatto diretto sulla qualità della risposta generata.

Per ottenere un'intuizione su come funziona la tokenizzazione, prova strumenti come il [Tokenizer di OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrato di seguito. Copia il tuo prompt - e vedi come viene convertito in token, prestando attenzione a come vengono gestiti i caratteri di spazio bianco e i segni di punteggiatura. Nota che questo esempio mostra un vecchio LLM (GPT-3) - quindi provare questo con un modello più recente potrebbe produrre un risultato diverso.

### Concetto: Modelli di Base

Una volta che un prompt è tokenizzato, la funzione primaria del ["LLM di Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modello di base) è di prevedere il token in quella sequenza. Poiché gli LLM sono addestrati su enormi set di dati testuali, hanno una buona percezione delle relazioni statistiche tra i token e possono fare quella previsione con una certa fiducia. Nota che non comprendono il _significato_ delle parole nel prompt o nel token; vedono solo un modello che possono "completare" con la loro prossima previsione. Possono continuare a prevedere la sequenza fino a quando non viene terminata dall'intervento dell'utente o da una condizione pre-stabilita.

Vuoi vedere come funziona il completamento basato su prompt? Inserisci il prompt sopra nello [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) di Azure OpenAI con le impostazioni predefinite. Il sistema è configurato per trattare i prompt come richieste di informazioni - quindi dovresti vedere un completamento che soddisfa questo contesto.

Ma cosa succede se l'utente voleva vedere qualcosa di specifico che soddisfacesse alcuni criteri o obiettivi di compito? È qui che entrano in gioco gli LLM _sintonizzati su istruzioni_.

### Concetto: LLM Sintonizzati su Istruzioni

Un [LLM Sintonizzato su Istruzioni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) inizia con il modello di base e lo affina con esempi o coppie di input/output (ad esempio, "messaggi" multi-turno) che possono contenere istruzioni chiare - e la risposta dell'AI tenta di seguire quell'istruzione.

Questo utilizza tecniche come l'Apprendimento per Rinforzo con Feedback Umano (RLHF) che possono addestrare il modello a _seguire istruzioni_ e _imparare dal feedback_ in modo che produca risposte più adatte alle applicazioni pratiche e più rilevanti per gli obiettivi degli utenti.

Proviamolo - riprendi il prompt sopra, ma ora cambia il _messaggio di sistema_ per fornire la seguente istruzione come contesto:

> _Riassumi il contenuto che ti viene fornito per uno studente di seconda elementare. Mantieni il risultato in un paragrafo con 3-5 punti elenco._

Vedi come il risultato è ora sintonizzato per riflettere l'obiettivo e il formato desiderati? Un educatore può ora utilizzare direttamente questa risposta nelle sue slide per quella classe.

## Perché abbiamo bisogno dell'Ingegneria dei Prompt?

Ora che sappiamo come i prompt vengono processati dagli LLM, parliamo del _perché_ abbiamo bisogno dell'ingegneria dei prompt. La risposta risiede nel fatto che gli attuali LLM presentano una serie di sfide che rendono _completamenti affidabili e coerenti_ più difficili da ottenere senza mettere impegno nella costruzione e ottimizzazione dei prompt. Ad esempio:

1. **Le risposte dei modelli sono stocastiche.** Lo _stesso prompt_ probabilmente produrrà risposte diverse con modelli o versioni di modelli diversi. E potrebbe anche produrre risultati diversi con lo _stesso modello_ in momenti diversi. _Le tecniche di ingegneria dei prompt possono aiutarci a minimizzare queste variazioni fornendo migliori guide_.

2. **I modelli possono fabbricare risposte.** I modelli sono pre-addestrati con _set di dati ampi ma finiti_, il che significa che mancano di conoscenza su concetti al di fuori di quel campo di addestramento. Di conseguenza, possono produrre completamenti che sono inaccurati, immaginari o direttamente contraddittori a fatti noti. _Le tecniche di ingegneria dei prompt aiutano gli utenti a identificare e mitigare tali fabbricazioni ad esempio, chiedendo all'AI per citazioni o ragionamenti_.

3. **Le capacità dei modelli variano.** I modelli più recenti o le generazioni di modelli avranno capacità più ricche ma porteranno anche eccentricità uniche e compromessi in termini di costi e complessità. _L'ingegneria dei prompt può aiutarci a sviluppare migliori pratiche e flussi di lavoro che astraono le differenze e si adattano ai requisiti specifici del modello in modi scalabili e senza soluzione di continuità_.

Vediamo questo in azione nell'OpenAI o Azure OpenAI Playground:

- Usa lo stesso prompt con diverse distribuzioni LLM (ad esempio, OpenAI, Azure OpenAI, Hugging Face) - hai visto le variazioni?
- Usa lo stesso prompt ripetutamente con la _stessa_ distribuzione LLM (ad esempio, Azure OpenAI playground) - come differivano queste variazioni?

### Esempio di Fabbricazioni

In questo corso, usiamo il termine **"fabbricazione"** per riferirci al fenomeno in cui gli LLM a volte generano informazioni fattualmente errate a causa di limitazioni nel loro addestramento o altri vincoli. Potresti aver sentito anche questo termine riferito come _"allucinazioni"_ in articoli popolari o documenti di ricerca. Tuttavia, raccomandiamo fortemente di usare il termine _"fabbricazione"_ in modo da non antropomorfizzare accidentalmente il comportamento attribuendo una caratteristica umana a un risultato guidato dalla macchina. Questo rinforza anche le [linee guida sull'AI Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) da una prospettiva terminologica, rimuovendo termini che potrebbero essere considerati offensivi o non inclusivi in alcuni contesti.

Vuoi avere un'idea di come funzionano le fabbricazioni? Pensa a un prompt che istruisce l'AI a generare contenuti per un argomento inesistente (per assicurarti che non si trovi nel set di dati di addestramento). Ad esempio - ho provato questo prompt:

> **Prompt:** genera un piano di lezione sulla Guerra di Marte del 2076.

Una ricerca web mi ha mostrato che ci sono racconti di fantasia (ad esempio, serie televisive o libri) su guerre marziane - ma nessuna nel 2076. Il buon senso ci dice anche che il 2076 è _nel futuro_ e quindi, non può essere associato a un evento reale.

Quindi cosa succede quando eseguiamo questo prompt con diversi fornitori LLM?

> **Risposta 1**: OpenAI Playground (GPT-35)

> **Risposta 2**: Azure OpenAI Playground (GPT-35)

> **Risposta 3**: : Hugging Face Chat Playground (LLama-2)

Come previsto, ogni modello (o versione del modello) produce risposte leggermente diverse grazie al comportamento stocastico e alle variazioni delle capacità del modello. Ad esempio, un modello si rivolge a un pubblico di ottava classe mentre l'altro assume uno studente di scuola superiore. Ma tutti e tre i modelli hanno generato risposte che potrebbero convincere un utente non informato che l'evento fosse reale.

Le tecniche di ingegneria dei prompt come il _metaprompting_ e la _configurazione della temperatura_ possono ridurre le fabbricazioni del modello fino a un certo punto. Le nuove _architetture_ di ingegneria dei prompt incorporano anche nuovi strumenti e tecniche in modo fluido nel flusso dei prompt, per mitigare o ridurre alcuni di questi effetti.

## Studio di Caso: GitHub Copilot

Concludiamo questa sezione ottenendo un'idea di come l'ingegneria dei prompt sia utilizzata in soluzioni reali guardando a uno Studio di Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot è il tuo "Programmatore in Coppia AI" - converte i prompt testuali in completamenti di codice ed è integrato nel tuo ambiente di sviluppo (ad esempio, Visual Studio Code) per un'esperienza utente fluida. Come documentato nella serie di blog di seguito, la prima versione era basata sul modello Codex di OpenAI - con gli ingegneri che realizzavano rapidamente la necessità di affinare il modello e sviluppare migliori tecniche di ingegneria dei prompt, per migliorare la qualità del codice. A luglio, hanno [debuttato con un modello AI migliorato che va oltre Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) per suggerimenti ancora più veloci.

Leggi i post in ordine, per seguire il loro percorso di apprendimento.

- **Maggio 2023** | [GitHub Copilot sta migliorando nella comprensione del tuo codice](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst
Infine, il vero valore dei modelli sta nella capacità di creare e pubblicare _librerie di prompt_ per domini applicativi verticali - dove il modello di prompt è ora _ottimizzato_ per riflettere il contesto specifico dell'applicazione o esempi che rendono le risposte più pertinenti e accurate per il pubblico di utenti mirato. Il repository [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) è un ottimo esempio di questo approccio, curando una libreria di prompt per il settore educativo con enfasi su obiettivi chiave come la pianificazione delle lezioni, la progettazione del curriculum, il tutoraggio degli studenti ecc.

## Contenuto di Supporto

Se pensiamo alla costruzione di un prompt come avere un'istruzione (compito) e un obiettivo (contenuto principale), allora il _contenuto secondario_ è come un contesto aggiuntivo che forniamo per **influenzare l'output in qualche modo**. Potrebbe trattarsi di parametri di regolazione, istruzioni di formattazione, tassonomie di argomenti ecc. che possono aiutare il modello a _personalizzare_ la sua risposta per adattarsi agli obiettivi o alle aspettative desiderate dall'utente.

Ad esempio: Dato un catalogo dei corsi con metadati estesi (nome, descrizione, livello, tag dei metadati, istruttore ecc.) su tutti i corsi disponibili nel curriculum:

- possiamo definire un'istruzione per "riassumere il catalogo dei corsi per l'autunno 2023"
- possiamo utilizzare il contenuto principale per fornire alcuni esempi del risultato desiderato
- possiamo utilizzare il contenuto secondario per identificare i 5 principali "tag" di interesse.

Ora, il modello può fornire un riassunto nel formato mostrato dai pochi esempi - ma se un risultato ha più tag, può dare priorità ai 5 tag identificati nel contenuto secondario.

---

<!--
MODELLO DI LEZIONE:
Questa unità dovrebbe coprire il concetto fondamentale #1.
Rafforza il concetto con esempi e riferimenti.

CONCETTO #3:
Tecniche di Prompt Engineering.
Quali sono alcune tecniche di base per il prompt engineering?
Illustralo con alcuni esercizi.
-->

## Migliori Pratiche di Prompting

Ora che sappiamo come i prompt possono essere _costruiti_, possiamo iniziare a pensare a come _progettarli_ per riflettere le migliori pratiche. Possiamo pensarci in due parti - avere la giusta _mentalità_ e applicare le giuste _tecniche_.

### Mentalità del Prompt Engineering

Il Prompt Engineering è un processo di tentativi ed errori, quindi tieni a mente tre ampi fattori guida:

1. **La comprensione del dominio è importante.** L'accuratezza e la pertinenza della risposta sono una funzione del _dominio_ in cui quell'applicazione o utente opera. Applica la tua intuizione e competenza nel dominio per **personalizzare ulteriormente le tecniche**. Ad esempio, definisci _personalità specifiche del dominio_ nei tuoi prompt di sistema, o usa _modelli specifici del dominio_ nei tuoi prompt utente. Fornisci contenuti secondari che riflettano contesti specifici del dominio, o usa _indicazioni ed esempi specifici del dominio_ per guidare il modello verso modelli di utilizzo familiari.

2. **La comprensione del modello è importante.** Sappiamo che i modelli sono stocastici per natura. Ma le implementazioni dei modelli possono anche variare in termini di dataset di addestramento che utilizzano (conoscenza pre-addestrata), le capacità che forniscono (ad esempio, tramite API o SDK) e il tipo di contenuto per cui sono ottimizzati (ad esempio, codice vs. immagini vs. testo). Comprendi i punti di forza e i limiti del modello che stai utilizzando e usa quella conoscenza per _dare priorità ai compiti_ o costruire _modelli personalizzati_ ottimizzati per le capacità del modello.

3. **Iterazione e convalida sono importanti.** I modelli si evolvono rapidamente, così come le tecniche per il prompt engineering. Come esperto di dominio, potresti avere altri contesti o criteri _per la tua_ applicazione specifica, che potrebbero non applicarsi alla comunità più ampia. Usa strumenti e tecniche di prompt engineering per "avviare" la costruzione del prompt, quindi itera e convalida i risultati utilizzando la tua intuizione e competenza nel dominio. Registra i tuoi approfondimenti e crea una **base di conoscenza** (ad esempio, librerie di prompt) che possa essere utilizzata come nuova base da altri, per iterazioni più rapide in futuro.

## Migliori Pratiche

Ora diamo un'occhiata alle pratiche comuni raccomandate dai praticanti di [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Cosa                              | Perché                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Valutare i modelli più recenti.   | Le nuove generazioni di modelli potrebbero avere caratteristiche e qualità migliorate - ma potrebbero anche comportare costi più elevati. Valutali per l'impatto, quindi prendi decisioni di migrazione.                                                                                |
| Separare istruzioni e contesto    | Verifica se il tuo modello/fornitore definisce _delimitatori_ per distinguere istruzioni, contenuti primari e secondari in modo più chiaro. Questo può aiutare i modelli ad assegnare pesi più accurati ai token.                                                         |
| Essere specifici e chiari         | Fornisci più dettagli sul contesto desiderato, risultato, lunghezza, formato, stile ecc. Questo migliorerà sia la qualità che la coerenza delle risposte. Cattura le ricette in modelli riutilizzabili.                                                          |
| Essere descrittivi, usare esempi  | I modelli possono rispondere meglio a un approccio "mostra e racconta". Inizia con un `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valori. Torna alla [sezione Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) per imparare come.

### Ora, apri il Jupyter Notebook

- Seleziona il kernel di runtime. Se utilizzi le opzioni 1 o 2, seleziona semplicemente il kernel Python 3.10.x predefinito fornito dal contenitore di sviluppo.

Sei pronto per eseguire gli esercizi. Nota che qui non ci sono risposte _giuste o sbagliate_ - si tratta solo di esplorare opzioni per tentativi ed errori e costruire l'intuizione su ciò che funziona per un determinato modello e dominio applicativo.

_Per questo motivo non ci sono segmenti di Soluzione di Codice in questa lezione. Invece, il Notebook avrà celle Markdown intitolate "La mia Soluzione:" che mostrano un esempio di output di riferimento._

<!--
MODELLO DI LEZIONE:
Avvolgi la sezione con un riassunto e risorse per l'apprendimento autonomo.
-->

## Verifica delle conoscenze

Quale delle seguenti è un buon prompt seguendo alcune ragionevoli migliori pratiche?

1. Mostrami un'immagine di un'auto rossa
2. Mostrami un'immagine di un'auto rossa di marca Volvo e modello XC90 parcheggiata su una scogliera con il sole che tramonta
3. Mostrami un'immagine di un'auto rossa di marca Volvo e modello XC90

A: 2, è il miglior prompt poiché fornisce dettagli su "cosa" e va nello specifico (non solo un'auto qualsiasi ma una marca e modello specifici) e descrive anche l'ambientazione generale. 3 è il successivo migliore poiché contiene anche molte descrizioni.

## 🚀 Sfida

Vedi se riesci a sfruttare la tecnica "cue" con il prompt: Completa la frase "Mostrami un'immagine di un'auto rossa di marca Volvo e ". Cosa risponde, e come lo miglioreresti?

## Ottimo lavoro! Continua il tuo apprendimento

Vuoi saperne di più sui diversi concetti di Prompt Engineering? Vai alla [pagina di apprendimento continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per trovare altre risorse interessanti su questo argomento.

Passa alla Lezione 5 dove esamineremo le [tecniche avanzate di prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.