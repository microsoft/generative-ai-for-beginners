<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:28:43+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "it"
}
-->
# Fondamenti di Prompt Engineering

## Introduzione

Questo modulo copre i concetti essenziali e le tecniche per creare prompt efficaci nei modelli di intelligenza artificiale generativa. Anche il modo in cui scrivi il tuo prompt a un LLM è importante. Un prompt ben progettato può ottenere una risposta di qualità migliore. Ma cosa significano esattamente termini come _prompt_ e _prompt engineering_? E come posso migliorare l'input del prompt che invio al LLM? Queste sono le domande a cui cercheremo di rispondere in questo capitolo e nel successivo.

L'_intelligenza artificiale generativa_ è in grado di creare nuovi contenuti (ad esempio, testo, immagini, audio, codice ecc.) in risposta alle richieste degli utenti. Raggiunge questo obiettivo utilizzando _Modelli di Linguaggio di Grandi Dimensioni_ come la serie GPT ("Generative Pre-trained Transformer") di OpenAI, che sono addestrati per utilizzare il linguaggio naturale e il codice.

Gli utenti possono ora interagire con questi modelli utilizzando paradigmi familiari come la chat, senza bisogno di alcuna competenza tecnica o formazione. I modelli sono basati su _prompt_ - gli utenti inviano un input di testo (prompt) e ricevono la risposta dell'IA (completamento). Possono quindi "chattare con l'IA" in modo iterativo, in conversazioni multi-turno, perfezionando il loro prompt finché la risposta non corrisponde alle loro aspettative.

I "Prompt" diventano ora l'interfaccia di _programmazione_ principale per le app di intelligenza artificiale generativa, dicendo ai modelli cosa fare e influenzando la qualità delle risposte restituite. Il "Prompt Engineering" è un campo di studio in rapida crescita che si concentra sulla _progettazione e ottimizzazione_ dei prompt per fornire risposte coerenti e di qualità su larga scala.

## Obiettivi di Apprendimento

In questa lezione, impariamo cos'è il Prompt Engineering, perché è importante e come possiamo creare prompt più efficaci per un determinato modello e obiettivo applicativo. Comprenderemo i concetti fondamentali e le migliori pratiche per il prompt engineering - e apprenderemo un ambiente "sandbox" interattivo Jupyter Notebooks dove possiamo vedere questi concetti applicati a esempi reali.

Alla fine di questa lezione saremo in grado di:

1. Spiegare cos'è il prompt engineering e perché è importante.
2. Descrivere i componenti di un prompt e come vengono utilizzati.
3. Imparare le migliori pratiche e tecniche per il prompt engineering.
4. Applicare le tecniche apprese a esempi reali, utilizzando un endpoint OpenAI.

## Termini Chiave

Prompt Engineering: La pratica di progettare e perfezionare gli input per guidare i modelli di IA verso la produzione di output desiderati.  
Tokenizzazione: Il processo di conversione del testo in unità più piccole, chiamate token, che un modello può comprendere e elaborare.  
LLM Ottimizzati per Istruzioni: Modelli di Linguaggio di Grandi Dimensioni (LLM) che sono stati ottimizzati con istruzioni specifiche per migliorare l'accuratezza e la rilevanza delle loro risposte.

## Sandbox di Apprendimento

Il prompt engineering è attualmente più arte che scienza. Il modo migliore per migliorare la nostra intuizione è _praticare di più_ e adottare un approccio di tentativi ed errori che combina l'esperienza nel dominio applicativo con tecniche raccomandate e ottimizzazioni specifiche del modello.

Il Jupyter Notebook che accompagna questa lezione fornisce un ambiente _sandbox_ dove puoi provare ciò che impari - man mano che procedi o come parte della sfida di codice alla fine. Per eseguire gli esercizi, avrai bisogno di:

1. **Una chiave API di Azure OpenAI** - l'endpoint del servizio per un LLM distribuito.
2. **Un Runtime Python** - in cui eseguire il Notebook.
3. **Variabili d'Ambiente Locali** - _completa i passaggi di [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) ora per prepararti_.

Il notebook viene fornito con esercizi _iniziali_ - ma sei incoraggiato ad aggiungere le tue sezioni _Markdown_ (descrizione) e _Codice_ (richieste di prompt) per provare più esempi o idee - e costruire la tua intuizione per il design del prompt.

## Guida Illustrata

Vuoi avere un quadro generale di ciò che copre questa lezione prima di immergerti? Dai un'occhiata a questa guida illustrata, che ti dà un'idea dei principali argomenti trattati e dei punti chiave su cui riflettere per ciascuno. La roadmap della lezione ti porta dalla comprensione dei concetti fondamentali e delle sfide ad affrontarli con tecniche e migliori pratiche di prompt engineering pertinenti. Nota che la sezione "Tecniche Avanzate" in questa guida si riferisce ai contenuti trattati nel _prossimo_ capitolo di questo curriculum.

## La Nostra Startup

Ora, parliamo di come _questo argomento_ si relaziona alla nostra missione di startup di [portare l'innovazione AI nell'educazione](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vogliamo costruire applicazioni AI-powered per l'_apprendimento personalizzato_ - quindi pensiamo a come diversi utenti della nostra applicazione potrebbero "progettare" i prompt:

- **Amministratori** potrebbero chiedere all'IA di _analizzare i dati del curriculum per identificare lacune nella copertura_. L'IA può riassumere i risultati o visualizzarli con il codice.
- **Educatori** potrebbero chiedere all'IA di _generare un piano di lezione per un pubblico e un argomento target_. L'IA può costruire il piano personalizzato in un formato specificato.
- **Studenti** potrebbero chiedere all'IA di _tutorarli in una materia difficile_. L'IA può ora guidare gli studenti con lezioni, suggerimenti ed esempi su misura per il loro livello.

Questo è solo la punta dell'iceberg. Dai un'occhiata a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una libreria di prompt open-source curata da esperti di educazione - per avere un'idea più ampia delle possibilità! _Prova a eseguire alcuni di questi prompt nel sandbox o utilizzando l'OpenAI Playground per vedere cosa succede!_

## Cos'è il Prompt Engineering?

Abbiamo iniziato questa lezione definendo il **Prompt Engineering** come il processo di _progettazione e ottimizzazione_ degli input di testo (prompt) per fornire risposte coerenti e di qualità (completamenti) per un determinato obiettivo applicativo e modello. Possiamo pensare a questo come a un processo in 2 fasi:

- _progettazione_ del prompt iniziale per un determinato modello e obiettivo
- _perfezionamento_ del prompt in modo iterativo per migliorare la qualità della risposta

Questo è necessariamente un processo di tentativi ed errori che richiede intuizione ed impegno da parte dell'utente per ottenere risultati ottimali. Ma perché è importante? Per rispondere a questa domanda, dobbiamo prima comprendere tre concetti:

- _Tokenizzazione_ = come il modello "vede" il prompt
- _LLM di Base_ = come il modello di base "processa" un prompt
- _LLM Ottimizzati per Istruzioni_ = come il modello può ora vedere "compiti"

### Tokenizzazione

Un LLM vede i prompt come una _sequenza di token_ dove modelli diversi (o versioni di un modello) possono tokenizzare lo stesso prompt in modi diversi. Poiché gli LLM sono addestrati sui token (e non sul testo grezzo), il modo in cui i prompt vengono tokenizzati ha un impatto diretto sulla qualità della risposta generata.

Per avere un'intuizione su come funziona la tokenizzazione, prova strumenti come il [Tokenizer di OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrato di seguito. Copia il tuo prompt - e vedi come viene convertito in token, prestando attenzione a come vengono gestiti i caratteri di spazio bianco e i segni di punteggiatura. Nota che questo esempio mostra un LLM più vecchio (GPT-3) - quindi provare questo con un modello più recente potrebbe produrre un risultato diverso.

### Concetto: Modelli di Base

Una volta che un prompt è tokenizzato, la funzione primaria del ["LLM di Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modello di base) è di prevedere il token in quella sequenza. Poiché gli LLM sono addestrati su enormi dataset di testo, hanno una buona comprensione delle relazioni statistiche tra i token e possono fare quella previsione con una certa sicurezza. Nota che non comprendono il _significato_ delle parole nel prompt o nel token; vedono solo un modello che possono "completare" con la loro prossima previsione. Possono continuare a prevedere la sequenza fino a quando non viene interrotta dall'intervento dell'utente o da qualche condizione pre-stabilita.

Vuoi vedere come funziona il completamento basato su prompt? Inserisci il prompt sopra nel [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) di Azure OpenAI con le impostazioni predefinite. Il sistema è configurato per trattare i prompt come richieste di informazioni - quindi dovresti vedere un completamento che soddisfa questo contesto.

Ma cosa succede se l'utente voleva vedere qualcosa di specifico che soddisfacesse alcuni criteri o obiettivi di compito? È qui che entrano in gioco gli LLM _ottimizzati per istruzioni_.

### Concetto: LLM Ottimizzati per Istruzioni

Un [LLM Ottimizzato per Istruzioni](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) inizia con il modello di base e lo ottimizza con esempi o coppie di input/output (ad esempio, "messaggi" multi-turno) che possono contenere istruzioni chiare - e la risposta dell'IA tenta di seguire quella istruzione.

Questo utilizza tecniche come il Reinforcement Learning con Feedback Umano (RLHF) che possono addestrare il modello a _seguire istruzioni_ e _imparare dal feedback_ in modo che produca risposte più adatte alle applicazioni pratiche e più pertinenti agli obiettivi dell'utente.

Proviamolo - rivedi il prompt sopra, ma ora cambia il _messaggio di sistema_ per fornire la seguente istruzione come contesto:

> _Riepiloga il contenuto fornito per uno studente di seconda elementare. Mantieni il risultato in un paragrafo con 3-5 punti elenco._

Vedi come il risultato è ora sintonizzato per riflettere l'obiettivo e il formato desiderati? Un educatore può ora utilizzare direttamente questa risposta nelle sue diapositive per quella classe.

## Perché abbiamo bisogno del Prompt Engineering?

Ora che sappiamo come i prompt vengono elaborati dagli LLM, parliamo del _perché_ abbiamo bisogno del prompt engineering. La risposta risiede nel fatto che gli attuali LLM presentano una serie di sfide che rendono più difficile ottenere _completamenti affidabili e coerenti_ senza mettere impegno nella costruzione e ottimizzazione dei prompt. Ad esempio:

1. **Le risposte del modello sono stocastiche.** Lo _stesso prompt_ probabilmente produrrà risposte diverse con modelli o versioni di modelli diversi. E potrebbe anche produrre risultati diversi con lo _stesso modello_ in momenti diversi. _Le tecniche di prompt engineering possono aiutarci a minimizzare queste variazioni fornendo migliori linee guida_.

2. **I modelli possono fabbricare risposte.** I modelli sono pre-addestrati con _dataset grandi ma finiti_, il che significa che mancano di conoscenza su concetti al di fuori di quell'ambito di addestramento. Di conseguenza, possono produrre completamenti che sono inaccurati, immaginari o direttamente contraddittori rispetto a fatti noti. _Le tecniche di prompt engineering aiutano gli utenti a identificare e mitigare tali fabbricazioni, ad esempio chiedendo all'IA citazioni o ragionamenti_.

3. **Le capacità dei modelli varieranno.** I modelli più recenti o le generazioni di modelli avranno capacità più ricche ma porteranno anche peculiarità uniche e compromessi in termini di costi e complessità. _Il prompt engineering può aiutarci a sviluppare migliori pratiche e flussi di lavoro che astraggono le differenze e si adattano ai requisiti specifici del modello in modi scalabili e senza soluzione di continuità_.

Vediamo questo in azione nell'OpenAI o Azure OpenAI Playground:

- Usa lo stesso prompt con diverse distribuzioni LLM (ad esempio, OpenAI, Azure OpenAI, Hugging Face) - hai visto le variazioni?
- Usa lo stesso prompt ripetutamente con la _stessa_ distribuzione LLM (ad esempio, Azure OpenAI playground) - come sono differite queste variazioni?

### Esempio di Fabbricazioni

In questo corso, utilizziamo il termine **"fabbricazione"** per riferirci al fenomeno in cui gli LLM a volte generano informazioni fattualmente errate a causa di limitazioni nel loro addestramento o altri vincoli. Potresti aver sentito questo termine riferito come _"allucinazioni"_ in articoli popolari o documenti di ricerca. Tuttavia, raccomandiamo fortemente di utilizzare il termine _"fabbricazione"_ in modo da non antropomorfizzare accidentalmente il comportamento attribuendo un tratto umano a un risultato guidato dalla macchina. Questo rinforza anche le [linee guida di AI Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) da una prospettiva terminologica, rimuovendo termini che potrebbero anche essere considerati offensivi o non inclusivi in alcuni contesti.

Vuoi avere un'idea di come funzionano le fabbricazioni? Pensa a un prompt che istruisce l'IA a generare contenuti per un argomento inesistente (per assicurarti che non sia presente nel dataset di addestramento). Ad esempio - ho provato questo prompt:

> **Prompt:** genera un piano di lezione sulla Guerra Marziana del 2076.

Una ricerca sul web mi ha mostrato che c'erano racconti di fantasia (ad esempio, serie televisive o libri) sulle guerre marziane - ma nessuno nel 2076. Il buon senso ci dice anche che il 2076 è _nel futuro_ e quindi non può essere associato a un evento reale.

Quindi cosa succede quando eseguiamo questo prompt con diversi fornitori di LLM?

> **Risposta 1**: OpenAI Playground (GPT-35)

> **Risposta 2**: Azure OpenAI Playground (GPT-35)

> **Risposta 3**: Hugging Face Chat Playground (LLama-2)

Come previsto, ogni modello (o versione del modello) produce risposte leggermente diverse grazie al comportamento stocastico e alle variazioni delle capacità del modello. Ad esempio, un modello si rivolge a un pubblico di ottava elementare mentre l'altro assume uno studente delle superiori. Ma tutti e tre i modelli hanno generato risposte che potrebbero convincere un utente non informato che l'evento fosse reale.

Le tecniche di prompt engineering come il _metaprompting_ e la _configurazione della temperatura_ possono ridurre le fabbricazioni del modello in una certa misura. Nuove _architetture_ di prompt engineering incorporano anche nuovi strumenti e tecniche senza soluzione di continuità nel flusso del prompt, per mitigare o ridurre alcuni di questi effetti.

## Studio di Caso: GitHub Copilot

Concludiamo questa sezione ottenendo un'idea di come il prompt engineering venga utilizzato in soluzioni reali esaminando uno Studio di Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot è il tuo "AI Pair Programmer" - converte i prompt di testo in completamenti di codice ed è integrato nel tuo ambiente di sviluppo (ad esempio, Visual Studio Code) per un'esperienza utente senza soluzione di continuità. Come documentato nella serie di blog di seguito, la versione più antica era basata sul modello Codex di OpenAI - con gli ingegneri che hanno rapidamente realizzato la necessità di ottimizzare il modello e sviluppare migliori tecniche di prompt engineering, per migliorare la qualità del codice. A luglio, hanno [debuttato un modello AI migliorato che va oltre Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) per suggerimenti ancora più veloci.

Leggi i post in ordine, per seguire il loro percorso di apprendimento.

- **Maggio 2023** | [GitHub Copilot sta migliorando nel comprendere il tuo codice](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maggio 2023** | [Dentro GitHub: Lavorare con gli LLM dietro GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Giugno 2023** |
Il vero valore dei modelli risiede nella capacità di creare e pubblicare _librerie di prompt_ per domini applicativi verticali, dove il modello di prompt è ora _ottimizzato_ per riflettere il contesto o gli esempi specifici dell'applicazione che rendono le risposte più pertinenti e accurate per il pubblico di utenti mirato. Il repository [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) è un ottimo esempio di questo approccio, curando una libreria di prompt per il dominio dell'istruzione con enfasi su obiettivi chiave come la pianificazione delle lezioni, la progettazione del curriculum, il tutoraggio degli studenti ecc.

## Contenuto di supporto

Se pensiamo alla costruzione dei prompt come avere un'istruzione (compito) e un obiettivo (contenuto principale), allora il _contenuto secondario_ è come un contesto aggiuntivo che forniamo per **influenzare l'output in qualche modo**. Potrebbe essere parametri di regolazione, istruzioni di formattazione, tassonomie di argomenti ecc. che possono aiutare il modello a _personalizzare_ la sua risposta per adattarsi agli obiettivi o alle aspettative desiderate dell'utente.

Ad esempio: Dato un catalogo di corsi con metadati estesi (nome, descrizione, livello, tag di metadati, istruttore ecc.) su tutti i corsi disponibili nel curriculum:

- possiamo definire un'istruzione per "riassumere il catalogo dei corsi per l'autunno 2023"
- possiamo utilizzare il contenuto principale per fornire alcuni esempi del risultato desiderato
- possiamo utilizzare il contenuto secondario per identificare i primi 5 "tag" di interesse.

Ora, il modello può fornire un riassunto nel formato mostrato dagli esempi, ma se un risultato ha più tag, può dare priorità ai 5 tag identificati nel contenuto secondario.

---

<!--
MODELLO DI LEZIONE:
Questa unità dovrebbe coprire il concetto principale #1.
Rinforza il concetto con esempi e riferimenti.

CONCETTO #3:
Tecniche di Ingegneria del Prompt.
Quali sono alcune tecniche di base per l'ingegneria del prompt?
Illustrale con alcuni esercizi.
-->

## Migliori pratiche di Prompting

Ora che sappiamo come i prompt possono essere _costruiti_, possiamo iniziare a pensare a come _progettarli_ per riflettere le migliori pratiche. Possiamo pensare a questo in due parti: avere la giusta _mentalità_ e applicare le giuste _tecniche_.

### Mentalità dell'Ingegneria del Prompt

L'ingegneria del prompt è un processo di prova ed errore, quindi tieni a mente tre ampi fattori guida:

1. **La comprensione del dominio è importante.** L'accuratezza e la pertinenza delle risposte sono una funzione del _dominio_ in cui quell'applicazione o utente opera. Applica la tua intuizione e competenza nel dominio per **personalizzare ulteriormente le tecniche**. Ad esempio, definisci _personalità specifiche del dominio_ nei tuoi prompt di sistema o utilizza _modelli specifici del dominio_ nei tuoi prompt utente. Fornisci contenuti secondari che riflettono contesti specifici del dominio o usa _indizi ed esempi specifici del dominio_ per guidare il modello verso modelli di utilizzo familiari.

2. **La comprensione del modello è importante.** Sappiamo che i modelli sono stocastici per natura. Ma le implementazioni dei modelli possono anche variare in termini di dataset di addestramento che utilizzano (conoscenza pre-addestrata), le capacità che forniscono (ad esempio, tramite API o SDK) e il tipo di contenuto per cui sono ottimizzati (ad esempio, codice vs. immagini vs. testo). Comprendi i punti di forza e le limitazioni del modello che stai utilizzando e usa quella conoscenza per _priorizzare i compiti_ o costruire _modelli personalizzati_ ottimizzati per le capacità del modello.

3. **Iterazione e validazione sono importanti.** I modelli stanno evolvendo rapidamente, e così anche le tecniche per l'ingegneria del prompt. Come esperto del dominio, potresti avere altri contesti o criteri per la tua specifica applicazione che potrebbero non applicarsi alla comunità più ampia. Usa strumenti e tecniche di ingegneria del prompt per "dare il via" alla costruzione dei prompt, poi iterare e validare i risultati usando la tua intuizione e competenza nel dominio. Registra i tuoi insight e crea una **base di conoscenza** (ad esempio, librerie di prompt) che può essere utilizzata come nuovo punto di partenza da altri, per iterazioni più rapide in futuro.

## Migliori pratiche

Ora diamo un'occhiata alle pratiche comuni raccomandate dai professionisti di [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Cosa                              | Perché                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Valuta i modelli più recenti.     | Le nuove generazioni di modelli potrebbero avere caratteristiche e qualità migliorate, ma potrebbero anche comportare costi più elevati. Valutali per l'impatto, poi prendi decisioni di migrazione.                                                  |
| Separa istruzioni e contesto      | Controlla se il tuo modello/fornitore definisce _delimitatori_ per distinguere istruzioni, contenuto primario e secondario più chiaramente. Questo può aiutare i modelli ad assegnare pesi più accurati ai token.                                     |
| Sii specifico e chiaro            | Fornisci più dettagli sul contesto desiderato, risultato, lunghezza, formato, stile ecc. Questo migliorerà sia la qualità che la coerenza delle risposte. Cattura ricette in modelli riutilizzabili.                                                 |
| Sii descrittivo, usa esempi       | I modelli potrebbero rispondere meglio a un approccio "mostra e racconta". Inizia con un `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valori. Torna alla [sezione Sandbox di apprendimento](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) per imparare come.

### Successivamente, apri il Jupyter Notebook

- Seleziona il kernel di runtime. Se utilizzi le opzioni 1 o 2, seleziona semplicemente il kernel Python 3.10.x predefinito fornito dal container di sviluppo.

Sei pronto per eseguire gli esercizi. Nota che non ci sono risposte _giuste o sbagliate_ qui: stiamo solo esplorando opzioni tramite prova ed errore e costruendo intuizioni su ciò che funziona per un determinato modello e dominio applicativo.

_Per questo motivo non ci sono segmenti di Soluzione Codice in questa lezione. Invece, il Notebook avrà celle Markdown intitolate "La mia soluzione:" che mostrano un esempio di output per riferimento._

 <!--
MODELLO DI LEZIONE:
Concludi la sezione con un riassunto e risorse per l'apprendimento autonomo.
-->

## Verifica delle conoscenze

Quale delle seguenti è un buon prompt seguendo alcune pratiche ragionevoli?

1. Mostrami un'immagine di auto rossa
2. Mostrami un'immagine di auto rossa della marca Volvo e modello XC90 parcheggiata vicino a una scogliera con il sole che tramonta
3. Mostrami un'immagine di auto rossa della marca Volvo e modello XC90

A: 2, è il miglior prompt poiché fornisce dettagli su "cosa" e entra nei particolari (non solo un'auto qualsiasi ma una marca e modello specifici) e descrive anche l'ambientazione generale. 3 è il prossimo migliore poiché contiene anche molta descrizione.

## 🚀 Sfida

Vedi se puoi sfruttare la tecnica del "cue" con il prompt: Completa la frase "Mostrami un'immagine di auto rossa della marca Volvo e ". Cosa risponde e come lo miglioreresti?

## Ottimo lavoro! Continua il tuo apprendimento

Vuoi saperne di più sui diversi concetti di Ingegneria del Prompt? Vai alla [pagina di apprendimento continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per trovare altre ottime risorse su questo argomento.

Vai alla Lezione 5 dove esamineremo le [tecniche avanzate di prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Anche se ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.