# Fondamenti di Prompt Engineering

[![Fondamenti di Prompt Engineering](../../../translated_images/it/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduzione
Questo modulo copre concetti e tecniche essenziali per creare prompt efficaci nei modelli generativi di IA. Il modo in cui scrivi il prompt per un LLM è importante. Un prompt accuratamente progettato può ottenere una migliore qualità di risposta. Ma cosa significano esattamente termini come _prompt_ e _prompt engineering_? E come miglioro l'_input_ del prompt che invio all'LLM? Queste sono le domande a cui cercheremo di rispondere in questo capitolo e nel successivo.

_L’IA generativa_ è in grado di creare nuovi contenuti (ad esempio, testo, immagini, audio, codice, ecc.) in risposta alle richieste degli utenti. Ci riesce usando _Large Language Models_ come la serie GPT di OpenAI ("Generative Pre-trained Transformer") che sono addestrati per usare linguaggio naturale e codice.

Gli utenti possono ora interagire con questi modelli usando paradigmi familiari come la chat, senza necessità di competenze tecniche o formazione. I modelli sono _basati su prompt_ - gli utenti inviano un input testuale (prompt) e ricevono in risposta la risposta IA (completion). Possono quindi "chattare con l’IA" in modo iterativo, in conversazioni a più turni, raffinando il loro prompt fino a quando la risposta corrisponde alle loro aspettative.

I "prompt" diventano ora l'_interfaccia di programmazione_ primaria per le app di IA generativa, dicendo ai modelli cosa fare e influenzando la qualità delle risposte restituite. Il "Prompt Engineering" è un campo di studio in rapida crescita che si concentra sulla _progettazione e ottimizzazione_ dei prompt per fornire risposte coerenti e di qualità su larga scala.

## Obiettivi di Apprendimento

In questa lezione, impariamo cosa è il Prompt Engineering, perché è importante e come possiamo creare prompt più efficaci per un modello dato e un obiettivo applicativo. Comprenderemo i concetti fondamentali e le migliori pratiche per il prompt engineering - e impareremo a conoscere un ambiente "sandbox" interattivo di Jupyter Notebooks dove possiamo vedere questi concetti applicati a esempi reali.

Alla fine di questa lezione saremo in grado di:

1. Spiegare cosa è il prompt engineering e perché è importante.
2. Descrivere i componenti di un prompt e come vengono usati.
3. Imparare le migliori pratiche e tecniche per il prompt engineering.
4. Applicare le tecniche apprese a esempi reali, usando un endpoint OpenAI.

## Termini Chiave

Prompt Engineering: La pratica di progettare e perfezionare gli input per guidare i modelli IA verso la produzione di output desiderati.  
Tokenizzazione: Il processo di conversione del testo in unità più piccole, chiamate token, che un modello può comprendere e elaborare.  
Instruction-Tuned LLMs: Large Language Models (LLM) che sono stati affinati con istruzioni specifiche per migliorare accuratezza e pertinenza delle risposte.

## Ambiente di Apprendimento Sandbox

Il prompt engineering è attualmente più un’arte che una scienza. Il modo migliore per migliorare la nostra intuizione è _praticare di più_ e adottare un approccio di tentativi ed errori che combina competenze nel dominio applicativo con tecniche consigliate e ottimizzazioni specifiche per modello.

Il Jupyter Notebook che accompagna questa lezione fornisce un ambiente _sandbox_ dove puoi provare ciò che impari - man mano oppure come parte della sfida di codice alla fine. Per eseguire gli esercizi, avrai bisogno di:

1. **Una chiave API Azure OpenAI** - l’endpoint del servizio per un LLM distribuito.  
2. **Un runtime Python** - in cui eseguire il Notebook.  
3. **Variabili di ambiente locali** - _completa ora i passaggi [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) per prepararti_.

Il notebook fornisce esercizi di _partenza_ - ma sei incoraggiato ad aggiungere le tue sezioni di _Markdown_ (descrizione) e _Codice_ (richieste di prompt) per provare più esempi o idee - e costruire la tua intuizione sulla progettazione dei prompt.

## Guida Illustrata

Vuoi avere un quadro generale di cosa tratta questa lezione prima di immergerti? Dai un’occhiata a questa guida illustrata, che ti dà un’idea dei temi principali trattati e dei punti chiave su cui riflettere. La roadmap della lezione ti guida dalla comprensione dei concetti fondamentali e delle sfide, fino a come affrontarli con le tecniche e le migliori pratiche di prompt engineering rilevanti. Nota che la sezione "Tecniche Avanzate" in questa guida si riferisce ai contenuti trattati nel _capitolo successivo_ di questo curriculum.

![Guida Illustrata al Prompt Engineering](../../../translated_images/it/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## La Nostra Startup

Ora, parliamo di come _questo argomento_ si collega alla missione della nostra startup di [portare l’innovazione AI nell’istruzione](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vogliamo costruire applicazioni AI-driven per l’_apprendimento personalizzato_ - quindi riflettiamo su come diversi utenti della nostra applicazione potrebbero "progettare" i prompt:

- **Amministratori** potrebbero chiedere all’IA di _analizzare i dati del curriculum per identificare lacune nella copertura_. L’IA può riassumere i risultati o visualizzarli con il codice.  
- **Educatori** potrebbero chiedere all’IA di _generare un piano di lezione per un pubblico e un argomento target_. L’IA può costruire il piano personalizzato in un formato specificato.  
- **Studenti** potrebbero chiedere all’IA di _tutorarli in una materia difficile_. L’IA può ora guidare gli studenti con lezioni, suggerimenti ed esempi su misura per il loro livello.

Questo è solo la punta dell’iceberg. Dai un’occhiata a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una libreria open source di prompt curata da esperti di istruzione - per capire meglio le possibilità! _Prova a eseguire alcuni di quei prompt nel sandbox o usando l’OpenAI Playground per vedere cosa succede!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Che cos’è il Prompt Engineering?

Abbiamo iniziato questa lezione definendo il **Prompt Engineering** come il processo di _progettazione e ottimizzazione_ degli input testuali (prompt) per fornire risposte coerenti e di qualità (completion) per un dato obiettivo applicativo e modello. Possiamo pensare a questo come a un processo in 2 fasi:

- _progettare_ il prompt iniziale per un modello e obiettivo dato  
- _rifinire_ il prompt in modo iterativo per migliorare la qualità della risposta

Si tratta necessariamente di un processo di tentativi ed errori che richiede intuizione ed impegno da parte dell’utente per ottenere risultati ottimali. Perché è importante? Per rispondere a questa domanda, dobbiamo prima capire tre concetti:

- _Tokenizzazione_ = come il modello "vede" il prompt  
- _Base LLMs_ = come il modello di base "processa" un prompt  
- _Instruction-Tuned LLMs_ = come il modello può ora vedere "compiti"

### Tokenizzazione

Un LLM vede i prompt come una _sequenza di token_ dove diversi modelli (o versioni dello stesso modello) possono tokenizzare lo stesso prompt in modi diversi. Poiché gli LLM sono addestrati su token (e non su testo grezzo), il modo in cui i prompt vengono tokenizzati ha un impatto diretto sulla qualità della risposta generata.

Per avere un’intuizione su come funziona la tokenizzazione, prova strumenti come il [Tokenizer OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrato qui sotto. Copia il tuo prompt - e vedi come viene convertito in token, prestando attenzione a come vengono gestiti gli spazi bianchi e la punteggiatura. Nota che questo esempio mostra un LLM più vecchio (GPT-3) - quindi provarlo con un modello più recente potrebbe produrre un risultato diverso.

![Tokenizzazione](../../../translated_images/it/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concetto: Modelli Fondamentali

Una volta che un prompt è tokenizzato, la funzione principale del ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modello fondamentale) è predire il token successivo in quella sequenza. Poiché gli LLM sono addestrati su grandi dataset testuali, hanno una buona comprensione delle relazioni statistiche tra i token e possono fare quella previsione con una certa confidenza. Nota che non comprendono il _significato_ delle parole nel prompt o nel token; vedono solo un modello che possono "completare" con la loro previsione successiva. Possono continuare a prevedere la sequenza fino a quando non viene interrotta dall’intervento dell’utente o da qualche condizione predefinita.

Vuoi vedere come funziona il completamento basato su prompt? Inserisci il prompt sopra nell'[_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) di Azure OpenAI Studio con le impostazioni predefinite. Il sistema è configurato per trattare i prompt come richieste di informazioni - quindi dovresti vedere un completamento che soddisfa questo contesto.

Ma se l’utente volesse vedere qualcosa di specifico che rispondesse a un certo criterio o obiettivo di compito? Qui entrano in gioco gli LLM _instruction-tuned_.

![Base LLM Chat Completion](../../../translated_images/it/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concetto: Instruction Tuned LLMs

Un [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte dal modello fondamentale e lo affina con esempi o coppie input/output (ad esempio "messaggi" multi-turno) che possono contenere istruzioni chiare - e la risposta dell’IA cerca di seguire quell’istruzione.

Questo usa tecniche come il Reinforcement Learning con Feedback Umano (RLHF) che può addestrare il modello a _seguire istruzioni_ e _imparare dal feedback_ in modo da produrre risposte più adatte per applicazioni pratiche e più pertinenti agli obiettivi dell’utente.

Proviamolo - rivisita il prompt sopra, ma ora cambia il _messaggio di sistema_ per fornire la seguente istruzione come contesto:

> _Riassumi il contenuto fornito per uno studente di seconda elementare. Mantieni il risultato in un paragrafo con 3-5 punti elenco._

Vedi come il risultato è ora adattato per riflettere l’obiettivo e il formato desiderati? Un educatore può ora usare direttamente questa risposta nelle loro slide per quella classe.

![Instruction Tuned LLM Chat Completion](../../../translated_images/it/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Perché abbiamo bisogno del Prompt Engineering?

Ora che sappiamo come i prompt vengono processati dagli LLM, parliamo del _perché_ è necessario il prompt engineering. La risposta risiede nel fatto che gli attuali LLM presentano diverse sfide che rendono più difficile ottenere _completion affidabili e coerenti_ senza mettere impegno nella costruzione e ottimizzazione dei prompt. Per esempio:

1. **Le risposte del modello sono stocastiche.** Lo _stesso prompt_ probabilmente produrrà risposte diverse con modelli o versioni di modelli differenti. E può anche produrre risultati diversi con lo _stesso modello_ in momenti diversi. _Le tecniche di prompt engineering possono aiutarci a minimizzare queste variazioni fornendo migliori limiti e protezioni_.

1. **I modelli possono fabbricare risposte.** I modelli sono pre-addestrati con dataset _grandi ma finiti_, quindi mancano di conoscenza su concetti al di fuori di quel campo di addestramento. Di conseguenza, possono produrre completion inaccurate, immaginarie o direttamente contraddittorie rispetto ai fatti noti. _Le tecniche di prompt engineering aiutano gli utenti a identificare e mitigare queste fabbricazioni, ad esempio chiedendo all’IA citazioni o ragionamenti_.

1. **Le capacità dei modelli variano.** Modelli più recenti o nuove generazioni di modelli avranno capacità più ricche ma anche particolarità uniche e compromessi in termini di costo e complessità. _Il prompt engineering può aiutarci a sviluppare migliori pratiche e workflow che astraggono le differenze e si adattano ai requisiti specifici del modello in modo scalabile e fluido_.

Vediamo questo in azione nell’OpenAI o Azure OpenAI Playground:

- Usa lo stesso prompt con diverse distribuzioni LLM (es. OpenAI, Azure OpenAI, Hugging Face) - hai notato variazioni?  
- Usa lo stesso prompt ripetutamente con la _stessa_ distribuzione LLM (es. playground Azure OpenAI) - come sono cambiate queste variazioni?

### Esempio di Fabbricazioni

In questo corso, usiamo il termine **"fabbricazione"** per riferirci al fenomeno in cui gli LLM a volte generano informazioni factualmente errate a causa di limiti nel loro addestramento o altri vincoli. Potresti aver sentito questo fenomeno chiamato _"allucinazioni"_ in articoli popolari o paper di ricerca. Tuttavia, raccomandiamo fortemente di usare il termine _"fabbricazione"_ così da non antropomorfizzare accidentalmente il comportamento attribuendo una caratteristica umana a un risultato generato da macchina. Questo inoltre rinforza le [linee guida di Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) dal punto di vista terminologico, eliminando termini che possono essere considerati offensivi o non inclusivi in alcuni contesti.

Vuoi avere un’idea di come funzionano le fabbricazioni? Pensa a un prompt che istruisce l’IA a generare contenuti su un argomento inesistente (per assicurarti che non sia presente nel dataset di addestramento). Per esempio - ho provato questo prompt:

> **Prompt:** genera un piano di lezione sulla Guerra Marziana del 2076.
Una ricerca sul web mi ha mostrato che esistevano resoconti di fantasia (ad esempio, serie televisive o libri) sulle guerre marziane - ma nessuno nel 2076. Il buon senso ci dice anche che il 2076 è _nel futuro_ e quindi non può essere associato a un evento reale.

Allora cosa succede quando eseguiamo questo prompt con diversi fornitori di LLM?

> **Risposta 1**: OpenAI Playground (GPT-35)

![Risposta 1](../../../translated_images/it/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Risposta 2**: Azure OpenAI Playground (GPT-35)

![Risposta 2](../../../translated_images/it/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Risposta 3**: : Hugging Face Chat Playground (LLama-2)

![Risposta 3](../../../translated_images/it/04-fabrication-huggingchat.faf82a0a51278956.webp)

Come previsto, ogni modello (o versione del modello) produce risposte leggermente diverse grazie al comportamento stocastico e alle variazioni nelle capacità del modello. Ad esempio, un modello si rivolge a un pubblico di ottava classe mentre l’altro assume uno studente delle superiori. Ma tutti e tre i modelli hanno generato risposte che potrebbero convincere un utente poco informato che l’evento fosse reale.

Le tecniche di prompt engineering come il _metaprompting_ e la _configurazione della temperatura_ possono ridurre in parte le fabbricazioni del modello. Nuove _architetture_ per il prompt engineering incorporano anche nuovi strumenti e tecniche in modo fluido nel flusso del prompt, per mitigare o ridurre alcuni di questi effetti.

## Caso di Studio: GitHub Copilot

Concludiamo questa sezione dando un’idea di come il prompt engineering sia usato nelle soluzioni reali osservando un Caso di Studio: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot è il tuo "AI Pair Programmer": converte prompt testuali in completamenti di codice ed è integrato nel tuo ambiente di sviluppo (ad esempio, Visual Studio Code) per un’esperienza utente fluida. Come documentato nella serie di blog sottostante, la versione iniziale si basava sul modello OpenAI Codex - con gli ingegneri che hanno rapidamente compreso la necessità di affinare il modello e sviluppare migliori tecniche di prompt engineering per migliorare la qualità del codice. A luglio, hanno [presentato un modello AI migliorato che supera Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) per suggerimenti ancora più rapidi.

Leggi i post in ordine, per seguire il loro percorso di apprendimento.

- **Maggio 2023** | [GitHub Copilot sta migliorando nella comprensione del tuo codice](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maggio 2023** | [Dentro GitHub: lavorare con gli LLM dietro GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Giugno 2023** | [Come scrivere prompt migliori per GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Luglio 2023** | [.. GitHub Copilot supera Codex con un modello AI migliorato](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Luglio 2023** | [Guida per sviluppatori al Prompt Engineering e agli LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Settembre 2023** | [Come costruire un'app LLM aziendale: lezioni apprese da GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Puoi anche esplorare il loro [blog di Ingegneria](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) per altri post come [questo](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) che mostra come questi modelli e tecniche siano _applicati_ per far funzionare applicazioni nel mondo reale.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Costruzione del Prompt

Abbiamo visto perché il prompt engineering è importante - ora comprendiamo come i prompt sono _costruiti_ per poter valutare diverse tecniche per un design di prompt più efficace.

### Prompt Base

Iniziamo con il prompt base: un input testuale inviato al modello senza altro contesto. Ecco un esempio - quando inviamo le prime parole dell’inno nazionale degli Stati Uniti all’OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), il modello completa istantaneamente la risposta con le righe successive, illustrando il comportamento base di previsione.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Sembra che tu stia iniziando il testo de "The Star-Spangled Banner", l’inno nazionale degli Stati Uniti. Il testo completo è ...       |

### Prompt Complesso

Ora aggiungiamo contesto e istruzioni a quel prompt base. La [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ci permette di costruire un prompt complesso come una raccolta di _messaggi_ con:

- Coppie input/output che riflettono l’input dell’_utente_ e la risposta dell’_assistente_.
- Messaggio di sistema che imposta il contesto per il comportamento o la personalità dell’assistente.

La richiesta ora è nella forma seguente, dove la _tokenizzazione_ cattura efficacemente informazioni rilevanti dal contesto e dalla conversazione. Cambiare il contesto di sistema può influire sulla qualità delle completazioni tanto quanto gli input utente forniti.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt Istruttivo

Nei esempi sopra, il prompt dell’utente era una semplice domanda testuale che può essere interpretata come una richiesta di informazioni. Con prompt di tipo _istruzione_, possiamo usare quel testo per specificare un compito con più dettagli, fornendo una guida migliore all’AI. Ecco un esempio:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Tipo di Istruzione  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Scrivi una descrizione della Guerra Civile                                                                                                                                                                                           | _ha restituito un paragrafo semplice_                                                                                      | Semplice            |
| Scrivi una descrizione della Guerra Civile. Fornisci date ed eventi chiave e descrivi la loro importanza                                                                                                                               | _ha restituito un paragrafo seguito da un elenco di date chiave con descrizioni_                                           | Complesso           |
| Scrivi una descrizione della Guerra Civile in 1 paragrafo. Fornisci 3 punti elenco con date chiave e la loro importanza. Fornisci altri 3 punti elenco con figure storiche importanti e il loro contributo. Restituisci l’output come file JSON | _restituisce dettagli più estesi in un riquadro di testo, formattato come JSON che puoi copiare-incollare in un file e validare se necessario_ | Complesso. Formattato. |

## Contenuto Primario

Negli esempi sopra, il prompt era ancora piuttosto aperto, permettendo all’LLM di decidere quale parte del dataset pre-addestrato fosse rilevante. Con il modello di design del _contenuto primario_, il testo di input è diviso in due parti:

- un’istruzione (azione)
- contenuto rilevante (che influenza l’azione)

Ecco un esempio in cui l’istruzione è "riassumi questo in 2 frasi".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle antiche civiltà da prima della storia registrata. È chiamato come il dio romano Giove.[19] Quando visto dalla Terra, Giove può essere abbastanza luminoso da far proiettare ombre visibili dalla sua luce riflessa,[20] e in media è il terzo oggetto naturale più luminoso nel cielo notturno dopo Luna e Venere. <br/> **Riassumi questo in 2 brevi frasi** | Giove, quinto pianeta dal Sole, è il più grande del Sistema Solare ed è noto per essere uno degli oggetti più luminosi nel cielo notturno. Chiamato come il dio romano Giove, è un gigante gassoso la cui massa è due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. |

Il segmento di contenuto primario può essere usato in vari modi per guidare istruzioni più efficaci:

- **Esempi** - invece di dire al modello cosa fare con un’istruzione esplicita, dagli esempi di cosa fare e lascia che ne deduca il modello il modello.
- **Suggerimenti** - segui l’istruzione con un “suggerimento” che prepara il completamento, guidando il modello verso risposte più rilevanti.
- **Template** - sono “ricette” ripetibili per prompt con segnaposto (variabili) che possono essere personalizzati con dati per casi d’uso specifici.

Esploriamo queste tecniche in azione.

### Uso di Esempi

Questo è un approccio in cui si usa il contenuto primario per "nutrire il modello" con alcuni esempi del risultato desiderato per una determinata istruzione, lasciando che inferisca lo schema desiderato. In base al numero di esempi forniti, possiamo avere zero-shot prompting, one-shot prompting, few-shot prompting ecc.

Il prompt ora consiste di tre componenti:

- Descrizione del compito
- Alcuni esempi del risultato desiderato
- L’inizio di un nuovo esempio (che diventa una descrizione implicita del compito)

| Tipo di Apprendimento | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot             | "Il Sole sta brillando". Traduci in spagnolo                                                                                                        | "El Sol está brillando".    |
| One-shot              | "Il Sole sta brillando" => "El Sol está brillando". <br> "È una giornata fredda e ventosa" =>                                                      | "Es un día frío y ventoso". |
| Few-shot              | Il giocatore ha corso le basi => Baseball <br/> Il giocatore ha fatto un ace => Tennis <br/> Il giocatore ha fatto un sei => Cricket <br/> Il giocatore ha fatto una schiacciata => | Basket                     |
|                       |                                                                                                                                                       |                             |

Nota come abbiamo dovuto fornire istruzione esplicita ("Traduci in spagnolo") nel zero-shot prompting, ma questa viene dedotta nell’esempio one-shot. L’esempio few-shot mostra come aggiungere più esempi permette ai modelli di fare inferenze più accurate senza alcuna istruzione aggiuntiva.

### Suggerimenti nel Prompt

Un’altra tecnica per usare il contenuto primario è fornire _suggerimenti_ invece di esempi. In questo caso, si dà al modello un piccolo spunto nella direzione giusta iniziando con uno spezzone che riflette il formato desiderato della risposta. Il modello quindi "prende il suggerimento" per continuare in quella direzione.

| Numero di Suggerimenti | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                      | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle antiche civiltà da prima della storia registrata. <br/>**Riassumi questo**                                       | Giove è il pianeta più grande del nostro Sistema Solare e il quinto in ordine di distanza dal Sole. È un gigante gassoso con una massa pari a 1/1000 di quella del Sole, ma più pesante di tutti gli altri pianeti messi insieme. Le antiche civiltà conoscono Giove da molto tempo, ed è facilmente visibile nel cielo notturno. |
| 1              | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle civiltà antiche fin da prima della storia registrata. <br/>**Riassumi Questo** <br/> Quello che abbiamo imparato è che Giove | è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti messi insieme. È facilmente visibile a occhio nudo ed è noto fin dai tempi antichi.                        |
| 2              | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle civiltà antiche fin da prima della storia registrata. <br/>**Riassumi Questo** <br/> Le 3 principali informazioni che abbiamo imparato:         | 1. Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. <br/> 2. È un gigante gassoso con una massa pari a un millesimo di quella del Sole...<br/> 3. Giove è stato visibile a occhio nudo fin dai tempi antichi ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Un modello di prompt è una _ricetta predefinita per un prompt_ che può essere memorizzata e riutilizzata secondo necessità, per garantire esperienze utente più coerenti su larga scala. Nella sua forma più semplice, è semplicemente una raccolta di esempi di prompt come [questo da OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) che fornisce sia i componenti interattivi del prompt (messaggi utente e sistema) che il formato di richiesta guidato dall’API - per supportare il riutilizzo.

Nella sua forma più complessa come [questo esempio da LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) contiene _segnaposto_ che possono essere sostituiti con dati provenienti da varie fonti (input utente, contesto di sistema, fonti di dati esterne ecc.) per generare un prompt dinamicamente. Ciò ci permette di creare una libreria di prompt riutilizzabili che possono essere usati per fornire esperienze utenti coerenti **programmaticamente** e su larga scala.

Infine, il vero valore dei modelli risiede nella capacità di creare e pubblicare _librerie di prompt_ per domini applicativi verticali - dove il modello del prompt è ora _ottimizzato_ per riflettere contesti o esempi specifici dell’applicazione che rendono le risposte più rilevanti e precise per il pubblico target. Il repository [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) è un ottimo esempio di questo approccio, curando una libreria di prompt per il dominio educativo con enfasi su obiettivi chiave come la pianificazione delle lezioni, la progettazione del curriculum, il tutoraggio degli studenti ecc.

## Supporting Content

Se consideriamo la costruzione del prompt come una istruzione (compito) e un target (contenuto primario), allora il _contenuto secondario_ è come un contesto aggiuntivo che forniamo per **influenzare in qualche modo l’output**. Può trattarsi di parametri di sintonia, istruzioni di formattazione, tassonomie tematiche ecc. che aiutano il modello a _personalizzare_ la sua risposta per soddisfare gli obiettivi o le aspettative desiderate dell’utente.

Per esempio: dato un catalogo di corsi con metadati estesi (nome, descrizione, livello, tag di metadati, docente ecc.) su tutti i corsi disponibili nel curriculum:

- possiamo definire un’istruzione per "riassumere il catalogo corsi per l’autunno 2023"
- possiamo usare il contenuto primario per fornire alcuni esempi del risultato desiderato
- possiamo usare il contenuto secondario per identificare i 5 "tag" principali di interesse.

Ora, il modello può fornire un riassunto nel formato mostrato dai pochi esempi - ma se un risultato ha più tag, può dare priorità ai 5 tag identificati nel contenuto secondario.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Pratiche Consigliate per il Prompting

Ora che sappiamo come i prompt possono essere _costruiti_, possiamo iniziare a pensare a come _progettarli_ per riflettere le migliori pratiche. Possiamo dividerlo in due parti - avere la giusta _mentalità_ e applicare le giuste _tecniche_.

### Mentalità di Prompt Engineering

Il Prompt Engineering è un processo di prova ed errore quindi tieni a mente tre fattori guida generali:

1. **La conoscenza del dominio è importante.** La precisione e rilevanza della risposta dipendono dal _dominio_ in cui l’applicazione o l’utente operano. Applica la tua intuizione e competenza di dominio per **personalizzare ulteriormente le tecniche**. Per esempio, definisci _personalità specifiche del dominio_ nei prompt di sistema, oppure usa _modelli specifici del dominio_ nei prompt utente. Fornisci contenuti secondari che riflettano contesti specifici del dominio, oppure usa _indizi ed esempi specifici del dominio_ per guidare il modello verso schemi d’uso familiari.

2. **La conoscenza del modello è importante.** Sappiamo che i modelli sono di natura stocastica. Ma le implementazioni dei modelli possono variare anche in termini di dataset di training usato (conoscenza pre-addestrata), le capacità che forniscono (es. tramite API o SDK) e il tipo di contenuti per cui sono ottimizzati (es. codice vs immagini vs testo). Comprendi punti di forza e limiti del modello che usi, e usa questa conoscenza per _prioritizzare compiti_ o costruire _modelli personalizzati_ ottimizzati per le capacità del modello.

3. **Iterazione e validazione sono importanti.** I modelli evolvono rapidamente, così come le tecniche di prompt engineering. Come esperto di dominio potresti avere contesti o criteri aggiuntivi specifici _per la tua_ applicazione, che potrebbero non valere per la comunità più ampia. Usa strumenti e tecniche di prompt engineering per “dare una spinta” alla costruzione di prompt, quindi itera e valida i risultati usando la tua intuizione e competenza. Registra i tuoi insight e crea una **base di conoscenza** (es. librerie di prompt) che possa essere usata da altri come nuovo riferimento, per iterazioni più rapide in futuro.

## Pratiche Consigliate

Ora vediamo le pratiche comuni raccomandate da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e dai professionisti di [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Cosa                              | Perché                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Valuta i modelli più recenti.       | Le nuove generazioni di modelli probabilmente hanno caratteristiche e qualità migliorate – ma potrebbero anche comportare costi maggiori. Valutali per impatto, quindi prendi decisioni di migrazione.                                                                                |
| Separa istruzioni e contesto   | Verifica se il tuo modello/fornitore definisce _delimitatori_ per distinguere più chiaramente istruzioni, contenuto primario e secondario. Questo può aiutare i modelli ad assegnare pesi più precisi ai token.                                                         |
| Sii specifico e chiaro             | Fornisci più dettagli sul contesto desiderato, risultato, lunghezza, formato, stile ecc. Questo migliorerà sia la qualità che la coerenza delle risposte. Registra le ricette in modelli riutilizzabili.                                                          |
| Sii descrittivo, usa esempi      | I modelli possono rispondere meglio con un approccio “mostra e racconta”. Parti da un approccio `zero-shot` dove dai un’istruzione (ma senza esempi) poi prova il `few-shot` come raffinamento, fornendo alcuni esempi dell’output desiderato. Usa analogie. |
| Usa indizi per avviare le completamenti | Spingilo verso il risultato desiderato dando alcune parole o frasi guida che può usare come punto di partenza per la risposta.                                                                                                               |
| Ribadisci                       | A volte potrebbe essere necessario ripetere istruzioni al modello. Dai istruzioni prima e dopo il contenuto primario, usa un’istruzione e un indizio ecc. Itera e valida per capire cosa funziona.                                                         |
| L’ordine conta                     | L’ordine in cui presenti le informazioni al modello può influire sull’output, anche negli esempi di apprendimento, a causa del bias di recency. Prova opzioni diverse per vedere cosa funziona meglio.                                                               |
| Dai un “via d’uscita” al modello           | Fornisci una risposta di completamento di _fallback_ che il modello può fornire se non riesce a completare il compito per qualsiasi motivo. Questo può ridurre la possibilità che generi risposte false o inventate.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Come per ogni buona pratica, ricorda che _i tuoi risultati possono variare_ in base al modello, al compito e al dominio. Usa questi spunti come punto di partenza e itera per trovare cosa funziona meglio per te. Rivaluta costantemente il tuo processo di prompt engineering man mano che nuovi modelli e strumenti diventano disponibili, con attenzione alla scalabilità del processo e alla qualità della risposta.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Compito

Congratulazioni! Sei arrivato alla fine della lezione! È tempo di mettere alla prova alcuni di quei concetti e tecniche con esempi reali!

Per il nostro compito, useremo un Jupyter Notebook con esercizi che puoi completare in modo interattivo. Puoi anche aggiungere al Notebook tue celle Markdown e di codice per esplorare idee e tecniche in autonomia.

### Per iniziare, fai un fork del repo, quindi

- (Raccomandato) Avvia GitHub Codespaces
- (In alternativa) Clona il repo sul tuo dispositivo locale e usalo con Docker Desktop
- (In alternativa) Apri il Notebook con il runtime per notebook che preferisci.

### Poi, configura le variabili d’ambiente

- Copia il file `.env.copy` nella root del repo in `.env` e compila i valori `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Torna alla [sezione Learning Sandbox](#ambiente-di-apprendimento-sandbox) per imparare come fare.

### Poi, apri il Jupyter Notebook

- Seleziona il kernel di runtime. Se usi le opzioni 1 o 2, seleziona semplicemente il kernel Python 3.10.x predefinito fornito dal container di sviluppo.

Sei pronto per eseguire gli esercizi. Nota che qui non ci sono risposte “giuste o sbagliate” - si tratta solo di esplorare opzioni con tentativi ed errori e sviluppare l’intuizione su cosa funziona per un dato modello e dominio applicativo.

_Per questo motivo in questa lezione non ci sono segmenti di codice soluzione. Al loro posto, il Notebook avrà celle Markdown intitolate "La mia soluzione:" che mostrano un esempio di output come riferimento._

 <!--
LESSON TEMPLATE:
Wrap the section with a summary and resources for self-guided learning.
-->

## Verifica della conoscenza

Quale dei seguenti è un buon prompt che segue alcune buone pratiche ragionevoli?

1. Mostrami un’immagine di una macchina rossa  
2. Mostrami un’immagine di una macchina rossa marca Volvo e modello XC90 parcheggiata su una scogliera con il sole al tramonto  
3. Mostrami un’immagine di una macchina rossa marca Volvo e modello XC90

A: 2, è il miglior prompt perché fornisce dettagli su "cosa" e specifica (non una qualsiasi macchina ma una marca e modello specifici) e descrive anche l’ambiente complessivo. 3 è il secondo migliore perché contiene anche molte descrizioni.

## 🚀 Sfida

Prova a sfruttare la tecnica dell’"indizio" con il prompt: Completa la frase "Mostrami un’immagine di una macchina rossa marca Volvo e ". Cosa risponde, e come la miglioreresti?

## Ottimo lavoro! Continua a imparare

Vuoi saperne di più su diversi concetti di Prompt Engineering? Vai alla [pagina di apprendimento continuato](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per trovare altre ottime risorse su questo tema.

Vai alla Lezione 5 dove vedremo [tecniche avanzate di prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->