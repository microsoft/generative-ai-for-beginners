# Fondamenti di Prompt Engineering

[![Fondamenti di Prompt Engineering](../../../translated_images/it/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduzione
Questo modulo copre i concetti e le tecniche essenziali per creare prompt efficaci nei modelli di AI generativa. Anche il modo in cui scrivi il tuo prompt a un LLM è importante. Un prompt accuratamente progettato può ottenere una migliore qualità di risposta. Ma cosa significano esattamente termini come _prompt_ e _prompt engineering_? E come posso migliorare l'_input_ del prompt che invio all'LLM? Queste sono le domande a cui cercheremo di rispondere in questo capitolo e nel prossimo.

_L'AI generativa_ è in grado di creare nuovi contenuti (ad esempio testi, immagini, audio, codice ecc.) in risposta alle richieste dell'utente. Lo fa utilizzando _Large Language Models_ come la serie GPT di OpenAI ("Generative Pre-trained Transformer") che sono addestrati per usare linguaggio naturale e codice.

Gli utenti possono ora interagire con questi modelli usando paradigmi familiari come la chat, senza necessità di competenze tecniche o formazione. I modelli sono _prompt-based_ - gli utenti inviano un input di testo (prompt) e ricevono indietro la risposta AI (completion). Possono poi "chattare con l'AI" iterativamente, in conversazioni multi-turno, affinando il loro prompt finché la risposta soddisfa le loro aspettative.

I "prompt" diventano ora l'_interfaccia di programmazione_ principale per le app di AI generativa, dicendo ai modelli cosa fare e influenzando la qualità delle risposte restituite. Il "Prompt Engineering" è un campo in rapida crescita che si concentra sulla _progettazione e ottimizzazione_ dei prompt per fornire risposte coerenti e di qualità su larga scala.

## Obiettivi di apprendimento

In questa lezione impariamo cos'è il Prompt Engineering, perché è importante e come possiamo creare prompt più efficaci per un dato modello e obiettivo applicativo. Comprenderemo i concetti chiave e le migliori pratiche per il prompt engineering - e conosceremo un ambiente "sandbox" interattivo con Jupyter Notebooks dove potremo vedere questi concetti applicati a esempi reali.

Alla fine di questa lezione saremo in grado di:

1. Spiegare cos'è il prompt engineering e perché è importante.
2. Descrivere i componenti di un prompt e come vengono usati.
3. Imparare le migliori pratiche e tecniche per il prompt engineering.
4. Applicare le tecniche apprese a esempi reali, usando un endpoint OpenAI.

## Termini chiave

Prompt Engineering: La pratica di progettare e perfezionare gli input per guidare i modelli AI verso la produzione di output desiderati.
Tokenizzazione: Il processo di conversione del testo in unità più piccole, chiamate token, che un modello può capire e processare.
Instruction-Tuned LLMs: Modelli di Linguaggio di Grandi Dimensioni (LLMs) che sono stati affinati con istruzioni specifiche per migliorare l'accuratezza e la pertinenza delle risposte.

## Ambiente di apprendimento sandbox

Il prompt engineering è attualmente più un'arte che una scienza. Il modo migliore per migliorare la nostra intuizione è _praticare di più_ adottando un approccio di tentativi ed errori che combina competenza nel dominio applicativo con tecniche raccomandate e ottimizzazioni specifiche del modello.

Il Jupyter Notebook che accompagna questa lezione offre un ambiente _sandbox_ dove puoi provare ciò che impari - man mano o come parte della sfida di codice alla fine. Per eseguire gli esercizi, avrai bisogno di:

1. **Una chiave API Azure OpenAI** - il servizio endpoint per un LLM distribuito.
2. **Un runtime Python** - in cui il Notebook può essere eseguito.
3. **Variabili d'ambiente locali** - _completa ora i passaggi del [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) per prepararti_.

Il notebook viene fornito con esercizi _starter_ - ma sei incoraggiato ad aggiungere sezioni tue in _Markdown_ (descrizione) e _Codice_ (richieste di prompt) per provare più esempi o idee - e costruire la tua intuizione per il design dei prompt.

## Guida illustrata

Vuoi avere una panoramica di ciò che questa lezione tratta prima di approfondire? Dai un'occhiata a questa guida illustrata, che ti dà un'idea dei temi principali e dei punti chiave su cui riflettere in ciascuno. Il percorso della lezione ti conduce dalla comprensione dei concetti di base e delle sfide, all'affrontarle con tecniche di prompt engineering rilevanti e best practice. Nota che la sezione "Tecniche Avanzate" in questa guida si riferisce ai contenuti trattati nel _capitolo successivo_ di questo curriculum.

![Guida illustrata al Prompt Engineering](../../../translated_images/it/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## La nostra startup

Ora, parliamo di come _questo argomento_ si collega alla missione della nostra startup di [portare l'innovazione AI nell'educazione](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vogliamo costruire applicazioni AI per l'_apprendimento personalizzato_ - quindi pensiamo a come diversi utenti della nostra applicazione potrebbero "progettare" i prompt:

- **Amministratori** potrebbero chiedere all'AI di _analizzare i dati del curriculum per identificare lacune nella copertura_. L'AI può riassumere i risultati o visualizzarli con codice.
- **Educatori** potrebbero chiedere all'AI di _generare un piano di lezione per un pubblico e un argomento target_. L'AI può costruire un piano personalizzato in un formato specificato.
- **Studenti** potrebbero chiedere all'AI di _tutorarli in una materia difficile_. L'AI ora può guidare gli studenti con lezioni, suggerimenti ed esempi adattati al loro livello.

Questo è solo la punta dell'iceberg. Dai un'occhiata a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una libreria open source di prompt curata da esperti di educazione - per avere una visione più ampia delle possibilità! _Prova a eseguire alcuni di questi prompt nella sandbox o usando l'OpenAI Playground per vedere cosa succede!_

<!--
TEMPLATE DELLA LEZIONE:
Questa unità dovrebbe coprire il concetto chiave #1.
Rafforzare il concetto con esempi e riferimenti.

CONCETTO #1:
Prompt Engineering.
Definirlo e spiegare perché è necessario.
-->

## Cos'è il Prompt Engineering?

Abbiamo iniziato questa lezione definendo il **Prompt Engineering** come il processo di _progettare e ottimizzare_ input di testo (prompt) per fornire risposte coerenti e di qualità (completamenti) per un dato obiettivo applicativo e modello. Possiamo pensare a questo come un processo in 2 fasi:

- _progettare_ il prompt iniziale per un dato modello e obiettivo
- _affinare_ il prompt iterativamente per migliorare la qualità della risposta

Questo è necessariamente un processo di tentativi ed errori che richiede intuizione e impegno dell'utente per ottenere risultati ottimali. Allora perché è importante? Per rispondere a questa domanda, dobbiamo prima comprendere tre concetti:

- _Tokenizzazione_ = come il modello "vede" il prompt
- _Base LLMs_ = come il modello base "processa" un prompt
- _Instruction-Tuned LLMs_ = come il modello ora può vedere "compiti"

### Tokenizzazione

Un LLM vede i prompt come una _sequenza di token_ dove modelli diversi (o versioni di un modello) possono tokenizzare lo stesso prompt in modi differenti. Poiché gli LLM sono addestrati sui token (e non sul testo grezzo), il modo in cui i prompt vengono tokenizzati influisce direttamente sulla qualità della risposta generata.

Per intuire come funziona la tokenizzazione, prova strumenti come il [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrato sotto. Copia il tuo prompt - e vedi come viene convertito in token, prestando attenzione a come gli spazi bianchi e la punteggiatura vengono gestiti. Nota che questo esempio mostra un LLM più vecchio (GPT-3) - quindi provare con un modello più nuovo potrebbe produrre un risultato diverso.

![Tokenizzazione](../../../translated_images/it/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concetto: Modelli di Fondazione

Una volta che un prompt è tokenizzato, la funzione principale del ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modello di Fondazione) è prevedere il token successivo in quella sequenza. Poiché gli LLM sono addestrati su enormi dataset testuali, hanno una buona conoscenza delle relazioni statistiche tra token e possono fare questa previsione con una certa fiducia. Nota che non comprendono il _significato_ delle parole nel prompt o nei token; vedono soltanto un pattern che possono "completare" con la loro previsione successiva. Possono continuare a prevedere la sequenza fino a quando non vengono interrotti dall'utente o da una condizione prestabilita.

Vuoi vedere come funziona il completamento basato su prompt? Inserisci il prompt sopra nel [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) con le impostazioni predefinite. Il sistema è configurato per trattare i prompt come richieste di informazioni - quindi dovresti vedere un completamento che soddisfa questo contesto.

Ma cosa succede se l'utente voleva vedere qualcosa di specifico che rispondesse a certi criteri o obiettivi del compito? Qui entrano in gioco gli LLM _istruiti_.

![Completamento chat Base LLM](../../../translated_images/it/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concetto: LLMs istruiti

Un [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte dal modello di fondazione e lo affina con esempi o coppie input/output (ad esempio, "messaggi" multi-turno) che possono contenere istruzioni chiare - e la risposta dell'AI tenta di seguire quell'istruzione.

Questo usa tecniche come Reinforcement Learning with Human Feedback (RLHF) che possono addestrare il modello a _seguire istruzioni_ e _imparare dal feedback_ in modo da produrre risposte più adatte alle applicazioni pratiche e più rilevanti per gli obiettivi dell'utente.

Proviamolo - riprendi il prompt sopra, ma ora cambia il _messaggio di sistema_ per fornire la seguente istruzione come contesto:

> _Riassumi i contenuti forniti per uno studente di seconda elementare. Mantieni il risultato in un paragrafo con 3-5 punti elenco._

Vedi come il risultato ora è tarato per riflettere l'obiettivo e il formato desiderati? Un educatore può ora usare direttamente questa risposta nelle sue slide per quella lezione.

![Completamento chat LLM istruito](../../../translated_images/it/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Perché abbiamo bisogno del Prompt Engineering?

Ora che sappiamo come i prompt vengono elaborati dagli LLM, parliamo del _perché_ abbiamo bisogno del prompt engineering. La risposta risiede nel fatto che gli attuali LLM presentano diverse sfide che rendono più difficile ottenere _completamenti affidabili e coerenti_ senza sforzi nella costruzione e ottimizzazione del prompt. Per esempio:

1. **Le risposte del modello sono stocastiche.** Lo _stesso prompt_ probabilmente produrrà risposte diverse con modelli o versioni di modello diverse. E potrebbe anche dare risultati differenti con lo _stesso modello_ in momenti diversi. _Le tecniche di prompt engineering possono aiutarci a minimizzare queste variazioni fornendo guide migliori_.

1. **I modelli possono fabbricare risposte.** I modelli sono pre-addestrati con dataset _grandi ma finiti_, cioè mancano di conoscenza su concetti al di fuori di tale ambito. Di conseguenza, possono produrre completamenti inaccurati, immaginari o direttamente contrari ai fatti noti. _Le tecniche di prompt engineering aiutano gli utenti a identificare e mitigare tali fabbricazioni, per esempio chiedendo all'AI citazioni o ragionamenti_.

1. **Le capacità dei modelli variano.** Modelli più nuovi o generazioni di modelli più recenti hanno capacità più ricche ma anche peculiarità uniche e compromessi in termini di costo e complessità. _Il prompt engineering può aiutarci a sviluppare best practice e flussi di lavoro che astraggono le differenze e si adattano ai requisiti specifici del modello in modo scalabile e fluido_.

Vediamo questo in azione nell'OpenAI o Azure OpenAI Playground:

- Usa lo stesso prompt con diverse distribuzioni LLM (es. OpenAI, Azure OpenAI, Hugging Face) - hai notato le variazioni?
- Usa lo stesso prompt ripetutamente con la _stessa_ distribuzione LLM (es. Azure OpenAI playground) - come differivano queste variazioni?

### Esempio di fabbricazioni

In questo corso, usiamo il termine **"fabbricazione"** per riferirci al fenomeno in cui gli LLM a volte generano informazioni fattualmente errate a causa di limiti nel loro addestramento o altri vincoli. Potresti aver sentito questo definito come _"allucinazioni"_ in articoli popolari o lavori di ricerca. Tuttavia, raccomandiamo fortemente di usare il termine _"fabbricazione"_ per evitare di antropomorfizzare questo comportamento attribuendo una caratteristica umana a un risultato guidato da una macchina. Questo rinforza anche le [linee guida per un'AI Responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) da una prospettiva terminologica, eliminando termini che potrebbero anche essere considerati offensivi o non inclusivi in alcuni contesti.

Vuoi avere un'idea di come funzionano le fabbricazioni? Pensa a un prompt che istruisce l'AI a generare contenuti su un argomento inesistente (per assicurarti che non sia presente nel dataset di addestramento). Per esempio - ho provato questo prompt:

> **Prompt:** genera un piano di lezione sulla Guerra Marziana del 2076.

Una ricerca web mi ha mostrato che esistono racconti di fantasia (ad esempio serie televisive o libri) sulle guerre marziane - ma nessuno ambientato nel 2076. Il buon senso ci dice anche che il 2076 è _nel futuro_ e quindi non può essere associato a un evento reale.


Cosa succede quando eseguiamo questo prompt con diversi fornitori di LLM?

> **Risposta 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/it/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Risposta 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/it/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Risposta 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/it/04-fabrication-huggingchat.faf82a0a51278956.webp)

Come previsto, ogni modello (o versione di modello) produce risposte leggermente diverse grazie al comportamento stocastico e alle variazioni nelle capacità del modello. Ad esempio, un modello si rivolge a un pubblico di ottava classe mentre l'altro presume un liceale. Ma tutti e tre i modelli hanno generato risposte che potrebbero convincere un utente non informato che l'evento fosse reale.

Tecniche di ingegneria del prompt come _metaprompting_ e _configurazione della temperatura_ possono ridurre le fabbricazioni del modello fino a un certo punto. Nuove _architetture_ di ingegneria del prompt incorporano anche nuovi strumenti e tecniche senza soluzione di continuità nel flusso del prompt, per mitigare o ridurre alcuni di questi effetti.

## Caso di Studio: GitHub Copilot

Concludiamo questa sezione per avere un'idea di come l'ingegneria del prompt viene utilizzata nelle soluzioni del mondo reale esaminando un Caso di Studio: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot è il tuo "Programmatore AI in Coppia" - converte prompt di testo in completamenti di codice ed è integrato nel tuo ambiente di sviluppo (es. Visual Studio Code) per un'esperienza utente fluida. Come documentato nella serie di blog sottostante, la prima versione si basava sul modello OpenAI Codex - con gli ingegneri che hanno presto realizzato la necessità di affinare il modello e sviluppare migliori tecniche di ingegneria del prompt, per migliorare la qualità del codice. A luglio, hanno [presentato un modello AI migliorato che va oltre Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) per suggerimenti ancora più veloci.

Leggi i post in ordine, per seguire il loro percorso di apprendimento.

- **Maggio 2023** | [GitHub Copilot sta migliorando nella comprensione del tuo codice](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maggio 2023** | [Inside GitHub: lavorare con gli LLM dietro GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Giugno 2023** | [Come scrivere prompt migliori per GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Luglio 2023** | [.. GitHub Copilot va oltre Codex con modello AI migliorato](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Luglio 2023** | [Guida per sviluppatori all’ingegneria del prompt e agli LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Settembre 2023** | [Come costruire un'app enterprise LLM: lezioni da GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Puoi anche sfogliare il loro [blog di ingegneria](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) per altri post come [questo](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) che mostra come questi modelli e tecniche vengono _applicati_ per guidare applicazioni del mondo reale.

---

<!--
MODELLO DELLA LEZIONE:
Questa unità dovrebbe coprire il concetto chiave #2.
Rinforzare il concetto con esempi e riferimenti.

CONCETTO #2:
Progettazione del Prompt.
Illustrato con esempi.
-->

## Costruzione del Prompt

Abbiamo visto perché l'ingegneria del prompt è importante - ora capiamo come i prompt sono _costruiti_ così possiamo valutare diverse tecniche per una progettazione del prompt più efficace.

### Prompt di Base

Cominciamo con il prompt base: un input di testo inviato al modello senza altro contesto. Ecco un esempio - quando inviamo le prime parole dell'inno nazionale USA all'[API Completion di OpenAI](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) essa completa istantaneamente la risposta con le righe successive, illustrando il comportamento base di predizione.

| Prompt (Input)     | Completion (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Sembra che tu stia iniziando il testo di "The Star-Spangled Banner," l'inno nazionale degli Stati Uniti. Il testo completo è ... |

### Prompt Complesso

Ora aggiungiamo contesto e istruzioni a quel prompt base. L'[API Chat Completion](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ci permette di costruire un prompt complesso come una raccolta di _messaggi_ con:

- Coppie input/output che riflettono l'input _utente_ e la risposta _assistente_.
- Messaggio di sistema che imposta il contesto per il comportamento o la personalità dell'assistente.

Ora la richiesta è nella forma qui sotto, dove la _tokenizzazione_ cattura efficacemente informazioni rilevanti dal contesto e dalla conversazione. Cambiare il contesto di sistema ora può avere un impatto sulla qualità dei completamenti, come gli input forniti dall'utente.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt Istruzione

Negli esempi qui sopra, il prompt utente era una semplice richiesta di testo che può essere interpretata come una domanda di informazioni. Con i prompt di _istruzione_, possiamo usare quel testo per specificare un compito con maggiore dettaglio, fornendo una migliore guida all'IA. Ecco un esempio:

| Prompt (Input)                                                                                                                                                                                                                         | Completion (Output)                                                                                                        | Tipo di Istruzione  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Scrivi una descrizione della Guerra Civile                                                                                                                                                                                            | _ha restituito un semplice paragrafo_                                                                                      | Semplice            |
| Scrivi una descrizione della Guerra Civile. Fornisci date ed eventi chiave e descrivi la loro importanza                                                                                                                                 | _ha restituito un paragrafo seguito da un elenco di date ed eventi chiave con descrizioni_                                  | Complesso           |
| Scrivi una descrizione della Guerra Civile in 1 paragrafo. Fornisci 3 punti elenco con date chiave e il loro significato. Fornisci altri 3 punti elenco con figure storiche chiave e i loro contributi. Restituisci l'output come file JSON | _restituisce dettagli più estesi in una casella di testo, formattati come JSON che puoi copiare/incollare in un file e convalidare se necessario_ | Complesso. Formattato. |

## Contenuto Primario

Negli esempi qui sopra, il prompt era ancora abbastanza aperto, permettendo al LLM di decidere quale parte del suo dataset pre-addestrato fosse rilevante. Con il modello di progettazione _contenuto primario_, il testo di input è diviso in due parti:

- un'istruzione (azione)
- contenuto rilevante (che influenza l'azione)

Ecco un esempio dove l'istruzione è "riassumi questo in 2 frasi".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle antiche civiltà da prima della storia registrata. È chiamato così dal dio romano Giove.[19] Visto dalla Terra, Giove può essere abbastanza luminoso da far proiettare ombre visibili,[20] ed è in media il terzo oggetto naturale più luminoso nel cielo notturno dopo la Luna e Venere. <br/> **Riassumi questo in 2 brevi frasi** | Giove, il quinto pianeta dal Sole, è il più grande del Sistema Solare ed è noto per essere uno degli oggetti più luminosi nel cielo notturno. Chiamato come il dio romano Giove, è un gigante gassoso la cui massa è due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. |

Il segmento di contenuto primario può essere usato in vari modi per guidare istruzioni più efficaci:

- **Esempi** - invece di dire al modello cosa fare con un’istruzione esplicita, dagli esempi di cosa fare e lascia che inferisca il modello.
- **Suggerimenti** - segui l’istruzione con un "suggerimento" che prepara il completamento, guidando il modello verso risposte più rilevanti.
- **Template** - queste sono "ricette" ripetibili per prompt con segnaposto (variabili) che possono essere personalizzate con dati per casi d’uso specifici.

Esploriamo queste soluzioni in azione.

### Uso degli Esempi

Questo è un approccio dove usi il contenuto primario per "fornire al modello" alcuni esempi dell’output desiderato per una determinata istruzione, e lasci che inferisca il modello per l’output richiesto. In base al numero di esempi forniti, possiamo avere zero-shot prompting, one-shot prompting, few-shot prompting ecc.

Ora il prompt consiste di tre componenti:

- Una descrizione del compito
- Alcuni esempi dell’output desiderato
- L’inizio di un nuovo esempio (che diventa una descrizione implicita del compito)

| Tipo di Apprendimento | Prompt (Input)                                                                                                                                        | Completion (Output)         |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot             | "Il Sole brilla". Traduci in spagnolo                                                                                                              | "El Sol está brillando".    |
| One-shot              | "Il Sole brilla" => "El Sol está brillando". <br> "È un giorno freddo e ventoso" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot              | Il giocatore ha corso le basi => Baseball <br/> Il giocatore ha servito un ace => Tennis <br/> Il giocatore ha segnato un sei => Cricket <br/> Il giocatore ha fatto una schiacciata => | Basket                     |
|                       |                                                                                                                                                       |                             |

Nota come abbiamo dovuto fornire un'istruzione esplicita ("Traduci in spagnolo") nel prompting zero-shot, ma essa viene dedotta nell'esempio one-shot. L'esempio few-shot mostra come aggiungere più esempi permetta ai modelli di fare inferenze più accurate senza istruzioni aggiuntive.

### Suggerimenti per il Prompt

Un'altra tecnica per usare il contenuto primario è fornire _suggerimenti_ invece di esempi. In questo caso, stiamo dando al modello un incoraggiamento nella giusta direzione iniziando con un frammento che riflette il formato di risposta desiderato. Il modello quindi "prende il suggerimento" e continua in quella direzione.

| Numero di Suggerimenti | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Output)                                                                                                                                                                                                                                                                                       |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                      | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle antiche civiltà da prima della storia registrata. <br/>**Riassumi questo**                                       | Giove è il pianeta più grande del nostro Sistema Solare ed il quinto dal Sole. È un gigante gassoso con una massa pari a 1/1000 di quella del Sole, ma più pesante di tutti gli altri pianeti messi insieme. Le antiche civiltà conoscono Giove da molto tempo, ed è facilmente visibile nel cielo notturno. |
| 1                      | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle antiche civiltà da prima della storia registrata. <br/>**Riassumi questo** <br/> Ciò che abbiamo imparato è che Giove | è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti messi insieme. È facilmente visibile a occhio nudo ed è noto sin dai tempi antichi.                        |

| 2              | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è conosciuto dalle civiltà antiche fin da prima della storia registrata. <br/>**Riassumi Questo** <br/> I 3 fatti principali che abbiamo imparato:         | 1. Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. <br/> 2. È un gigante gassoso con una massa pari a un millesimo di quella del Sole...<br/> 3. Giove è visibile ad occhio nudo fin dai tempi antichi ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelli di Prompt

Un modello di prompt è una _ricetta predefinita per un prompt_ che può essere memorizzata e riutilizzata secondo necessità, per ottenere esperienze utente più coerenti su larga scala. Nella sua forma più semplice, è semplicemente una raccolta di esempi di prompt come [questo di OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) che fornisce sia i componenti interattivi del prompt (messaggi utente e di sistema) sia il formato della richiesta basata su API - per supportare il riuso.

Nella forma più complessa, come [questo esempio di LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contiene _segnaposto_ che possono essere sostituiti con dati provenienti da varie fonti (input utente, contesto di sistema, fonti di dati esterne, ecc.) per generare un prompt dinamicamente. Questo ci permette di creare una libreria di prompt riutilizzabili che possono essere usati per guidare esperienze utente coerenti **programmaticamente** su larga scala.

Infine, il vero valore dei modelli risiede nella capacità di creare e pubblicare _librerie di prompt_ per domini applicativi verticali - dove il modello di prompt è ora _ottimizzato_ per riflettere il contesto specifico dell'applicazione o esempi che rendono le risposte più rilevanti e precise per il pubblico utente target. Il repository [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) è un ottimo esempio di questo approccio, curando una libreria di prompt per il dominio educativo con enfasi su obiettivi chiave come pianificazione delle lezioni, progettazione del curriculum, tutoraggio degli studenti, ecc.

## Contenuti di Supporto

Se consideriamo la costruzione di un prompt come composta da un’istruzione (compito) e un obiettivo (contenuto principale), allora il _contenuto secondario_ è come un contesto aggiuntivo che forniamo per **influenzare in qualche modo l’output**. Può essere parametri di tuning, istruzioni di formattazione, tassonomie di argomenti ecc. che aiutano il modello a _personalizzare_ la risposta per soddisfare gli obiettivi o le aspettative dell’utente.

Per esempio: dato un catalogo di corsi con metadati estesi (nome, descrizione, livello, tag di metadati, docente, ecc.) su tutti i corsi disponibili nel curriculum:

- possiamo definire un’istruzione per "riassumere il catalogo corsi per l'autunno 2023"
- possiamo usare il contenuto principale per fornire alcuni esempi del risultato desiderato
- possiamo usare il contenuto secondario per identificare i 5 principali "tag" di interesse.

Ora, il modello può fornire un riassunto nel formato mostrato dai pochi esempi - ma se un risultato ha più tag, può dare priorità ai 5 tag identificati nel contenuto secondario.

---

<!--
MODELLO DI LEZIONE:
Questa unità dovrebbe coprire il concetto base #1.
Rafforzare il concetto con esempi e riferimenti.

CONCETTO #3:
Tecniche di Prompt Engineering.
Quali sono alcune tecniche base per il prompt engineering?
Illustralo con alcuni esercizi.
-->

## Buone Pratiche per il Prompting

Ora che sappiamo come i prompt possono essere _costruiti_, possiamo iniziare a pensare a come _progettarli_ riflettendo le migliori pratiche. Possiamo considerare questo in due parti - avere la giusta _mentalità_ e applicare le giuste _tecniche_.

### Mentalità di Prompt Engineering

Il Prompt Engineering è un processo di tentativi ed errori quindi tieni a mente tre fattori guida generali:

1. **La comprensione del dominio è importante.** La precisione e rilevanza della risposta dipendono dal _dominio_ in cui quell’applicazione o utente opera. Applica la tua intuizione e competenza nel dominio per **personalizzare ulteriormente le tecniche**. Per esempio, definisci _personalità specifiche per dominio_ nei tuoi prompt di sistema, oppure usa _modelli specifici per dominio_ nei tuoi prompt utente. Fornisci contenuti secondari che riflettano contesti specifici del dominio, o usa _indizi ed esempi specifici al dominio_ per guidare il modello verso schemi d’uso familiari.

2. **La comprensione del modello è importante.** Sappiamo che i modelli sono per natura stochastic. Ma le implementazioni dei modelli possono variare in termini di dataset di addestramento usati (conoscenza pre-addestrata), capacità offerte (es. via API o SDK) e tipo di contenuti per cui sono ottimizzati (es. codice vs immagini vs testo). Comprendi punti di forza e limitazioni del modello che stai usando e usa questa conoscenza per _dare priorità ai compiti_ o costruire _modelli personalizzati_ ottimizzati per le capacità del modello.

3. **Iterazione e Validazione sono importanti.** I modelli evolvono rapidamente, così come le tecniche per il prompt engineering. Come esperto del dominio, potresti avere altri contesti o criteri specifici per _la tua_ applicazione, che potrebbero non applicarsi alla comunità più ampia. Usa strumenti e tecniche di prompt engineering per "dare una spinta" alla costruzione del prompt, poi itera e valida i risultati con la tua intuizione e competenza nel dominio. Registra le tue intuizioni e crea una **base di conoscenza** (es. librerie di prompt) che possa essere usata come nuova base da altri, per iterazioni più rapide in futuro.

## Migliori Pratiche

Esaminiamo ora alcune pratiche comuni raccomandate dai professionisti di [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Cosa                             | Perché                                                                                                                                                                                                                                             |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Valuta i modelli più recenti.    | Le nuove generazioni di modelli probabilmente hanno funzionalità e qualità migliorate - ma possono anche avere costi maggiori. Valutale per impatto, poi prendi decisioni di migrazione.                                                          |
| Separa istruzioni e contesto     | Verifica se il tuo modello/fornitore definisce _delimitatori_ per distinguere meglio istruzioni, contenuti primari e secondari. Questo può aiutare i modelli ad assegnare pesi più accurati ai token.                                               |
| Sii specifico e chiaro           | Fornisci più dettagli sul contesto desiderato, obiettivo, lunghezza, formato, stile ecc. Questo migliorerà qualità e coerenza delle risposte. Registra le ricette in modelli riutilizzabili.                                                      |
| Sii descrittivo, usa esempi      | I modelli possono rispondere meglio ad un approccio "mostra e spiega". Inizia con un approccio a `zero-shot` dove dai solo un’istruzione (ma nessun esempio) poi prova `few-shot` come raffinamento, fornendo pochi esempi del risultato desiderato. Usa analogie. |
| Usa indizi per avviare completamenti | Spingilo verso un risultato desiderato fornendogli parole o frasi iniziali che può usare come punto di partenza per la risposta.                                                                                                                   |
| Raddoppia                      | A volte potresti dover ripetere te stesso al modello. Dai istruzioni prima e dopo il contenuto primario, usa un’istruzione e un indizio, ecc. Itera e valida per vedere cosa funziona.                                                               |
| L’ordine conta                 | L’ordine in cui presenti le informazioni al modello può influenzare l’output, anche negli esempi di apprendimento, grazie al bias da recenza. Prova opzioni diverse per vedere cosa funziona meglio.                                                |
| Dai al modello una “via d’uscita” | Dai al modello una risposta di _fallback_ che può fornire se non può completare il compito per qualsiasi motivo. Questo può ridurre le probabilità che i modelli generino risposte false o inventate.                                                 |
|                                |                                                                                                                                                                                                                                                   |

Come per ogni buona pratica, ricordati che _i risultati possono variare_ in base al modello, al compito e al dominio. Usa questi come punto di partenza, e itera per trovare ciò che funziona meglio per te. Riesamina costantemente il processo di prompt engineering man mano che nuovi modelli e strumenti diventano disponibili, concentrandoti su scalabilità del processo e qualità delle risposte.

<!--
MODELLO DI LEZIONE:
Questa unità dovrebbe fornire una sfida di codice se applicabile

SFIDA:
Link ad un Jupyter Notebook con solo i commenti nel codice nelle istruzioni (le sezioni di codice sono vuote).

SOLUZIONE:
Link a una copia di quel Notebook con i prompt compilati ed eseguiti, mostrando un esempio di output.
-->

## Compito

Congratulazioni! Sei arrivato alla fine della lezione! È ora di mettere alla prova alcuni di quei concetti e tecniche con esempi reali!

Per il nostro compito useremo un Jupyter Notebook con esercizi che puoi completare in modo interattivo. Puoi anche estendere il Notebook con tue celle Markdown e di codice per esplorare idee e tecniche in autonomia.

### Per iniziare, clona il repo, poi

- (Consigliato) Avvia GitHub Codespaces
- (In alternativa) Clona il repo sul tuo dispositivo locale e usalo con Docker Desktop
- (In alternativa) Apri il Notebook con il tuo ambiente preferito per notebook.

### Poi, configura le variabili d'ambiente

- Copia il file `.env.copy` nella root del repo in `.env` e compila i valori `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Torna alla [sezione Learning Sandbox](#ambiente-di-apprendimento-sandbox) per sapere come fare.

### Poi, apri il Jupyter Notebook

- Seleziona il kernel di runtime. Se usi le opzioni 1 o 2, seleziona semplicemente il kernel Python 3.10.x di default fornito dal contenitore di sviluppo.

Sei pronto per eseguire gli esercizi. Nota che qui non ci sono risposte _giuste o sbagliate_ - solo esplorazioni per tentativi ed errori e costruzione dell’intuizione su cosa funziona per un dato modello e dominio applicativo.

_Per questo motivo non ci sono segmenti di Soluzione Codice in questa lezione. Invece, il Notebook avrà celle Markdown intitolate “La Mia Soluzione:” che mostrano un esempio di output come riferimento._

 <!--
MODELLO DI LEZIONE:
Chiudi la sezione con un riepilogo e risorse per apprendimento autodiretto.
-->

## Verifica della conoscenza

Quale dei seguenti è un buon prompt che segue alcune ragionevoli buone pratiche?

1. Mostrami un’immagine di una macchina rossa
2. Mostrami un’immagine di una macchina rossa marca Volvo modello XC90 parcheggiata vicino a una scogliera con il sole che tramonta
3. Mostrami un’immagine di una macchina rossa marca Volvo modello XC90

A: 2, è il miglior prompt perché fornisce dettagli sul "cosa" e va nello specifico (non solo una macchina qualsiasi ma una marca e modello specifico) e descrive anche l’ambiente complessivo. 3 è la seconda migliore perché contiene anch’esso molte descrizioni.

## 🚀 Sfida

Prova a utilizzare la tecnica del "suggerimento" con il prompt: Completa la frase "Mostrami un’immagine di una macchina rossa marca Volvo e ". Cosa risponde e come la miglioreresti?

## Ottimo lavoro! Continua a imparare

Vuoi saperne di più su concetti diversi del Prompt Engineering? Vai alla [pagina di apprendimento continuativo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per trovare altre ottime risorse su questo argomento.

Passa alla Lezione 5 dove vedremo [tecniche avanzate di prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->