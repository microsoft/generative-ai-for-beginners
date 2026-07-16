# Fondamenti di Prompt Engineering

[![Fondamenti di Prompt Engineering](../../../translated_images/it/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introduzione
Questo modulo copre concetti e tecniche essenziali per creare prompt efficaci nei modelli di intelligenza artificiale generativa. Anche il modo in cui si scrive il prompt per un LLM è importante. Un prompt accuratamente realizzato può ottenere una migliore qualità di risposta. Ma cosa significano esattamente termini come _prompt_ e _prompt engineering_? E come posso migliorare il _input_ del prompt che invio all'LLM? Queste sono le domande a cui cercheremo di rispondere in questo capitolo e nel successivo.

L'_intelligenza artificiale generativa_ è in grado di creare nuovi contenuti (ad es. testo, immagini, audio, codice, ecc.) in risposta alle richieste degli utenti. Ciò avviene usando _Large Language Models_ come la serie GPT di OpenAI ("Generative Pre-trained Transformer") addestrati per usare il linguaggio naturale e il codice.

Gli utenti ora possono interagire con questi modelli usando paradigmi familiari come la chat, senza necessità di competenze o formazione tecnica. I modelli sono _basati su prompt_ - gli utenti inviano un input testuale (prompt) e ricevono la risposta dell'IA (completion). Possono poi "chattare con l’IA" in modo iterativo, in conversazioni multi-turno, affinando il prompt finché la risposta non corrisponde alle loro aspettative.

I "prompt" diventano ora l'_interfaccia di programmazione_ principale per le app di intelligenza artificiale generativa, indicando ai modelli cosa fare e influenzando la qualità delle risposte ricevute. Il "Prompt Engineering" è un campo di studio in rapida crescita che si concentra sulla _progettazione e ottimizzazione_ dei prompt per fornire risposte coerenti e di qualità su larga scala.

## Obiettivi di Apprendimento

In questa lezione, impariamo cos'è il Prompt Engineering, perché è importante e come possiamo creare prompt più efficaci per un dato modello e obiettivo applicativo. Comprenderemo i concetti fondamentali e le migliori pratiche per il prompt engineering - e conosceremo un ambiente di "sandbox" interattivo in Jupyter Notebooks dove possiamo vedere questi concetti applicati a esempi reali.

Alla fine di questa lezione saremo in grado di:

1. Spiegare cos'è il prompt engineering e perché conta.
2. Descrivere i componenti di un prompt e come vengono utilizzati.
3. Imparare le migliori pratiche e tecniche per il prompt engineering.
4. Applicare le tecniche apprese a esempi reali, utilizzando un endpoint OpenAI.

## Termini Chiave

Prompt Engineering: La pratica di progettare e perfezionare input per guidare i modelli di IA a produrre output desiderati.
Tokenizzazione: Il processo di conversione del testo in unità più piccole, chiamate token, che un modello può comprendere e processare.
Instruction-Tuned LLMs: Large Language Models (LLM) che sono stati ottimizzati con istruzioni specifiche per migliorare l'accuratezza e la pertinenza delle risposte.

## Sandbox di Apprendimento

Il prompt engineering è attualmente più arte che scienza. Il modo migliore per migliorare la nostra intuizione è _praticare di più_ e adottare un approccio di tentativi ed errori che combini l’esperienza nel dominio applicativo con le tecniche raccomandate e le ottimizzazioni specifiche del modello.

Il Jupyter Notebook che accompagna questa lezione fornisce un ambiente _sandbox_ dove puoi provare ciò che apprendi - man mano o come parte della sfida di codice alla fine. Per eseguire gli esercizi, avrai bisogno di:

1. **Una chiave API Azure OpenAI** - il servizio endpoint per un LLM distribuito.
2. **Un runtime Python** - nel quale eseguire il Notebook.
3. **Variabili ambientali locali** - _completa ora i passaggi di [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) per prepararti_.

Il notebook include esercizi _iniziali_ - ma sei incoraggiato ad aggiungere le tue sezioni _Markdown_ (descrizione) e _Code_ (richieste di prompt) per provare più esempi o idee - e sviluppare la tua intuizione per la progettazione dei prompt.

## Guida Illustrata

Vuoi avere una panoramica di ciò che questa lezione copre prima di immergerti? Dai un’occhiata a questa guida illustrata, che ti dà un’idea degli argomenti principali trattati e dei punti chiave su cui riflettere in ciascuno. La roadmap della lezione ti porta dalla comprensione dei concetti fondamentali e delle sfide fino ad affrontarle con tecniche di prompt engineering rilevanti e migliori pratiche. Nota che la sezione "Tecniche Avanzate" in questa guida fa riferimento ai contenuti trattati nel _capitolo successivo_ di questo curriculum.

![Guida Illustrata al Prompt Engineering](../../../translated_images/it/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## La Nostra Startup

Ora, parliamo di come _questo argomento_ si collega alla nostra missione startup per [portare innovazione AI nell'istruzione](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Vogliamo costruire applicazioni AI per l'_apprendimento personalizzato_ - quindi pensiamo a come diversi utenti della nostra applicazione potrebbero "progettare" prompt:

- Gli **Amministratori** potrebbero chiedere all'AI di _analizzare i dati del curriculum per identificare lacune nella copertura_. L’AI può riassumere i risultati o visualizzarli con codice.
- Gli **Educatori** potrebbero chiedere all'AI di _generare un piano di lezione per un pubblico e un argomento specifici_. L’AI può costruire il piano personalizzato in un formato specificato.
- Gli **Studenti** potrebbero chiedere all'AI di _fornire tutoraggio in una materia difficile_. L’AI ora può guidarli con lezioni, suggerimenti ed esempi adattati al loro livello.

Questa è solo la punta dell’iceberg. Dai un’occhiata a [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una libreria open-source di prompt curata da esperti di istruzione - per farti un’idea più ampia delle possibilità! _Prova a eseguire alcuni di questi prompt nel sandbox o usando l’OpenAI Playground per vedere cosa succede!_

<!--
TEMPLATE DELLA LEZIONE:
Questa unità dovrebbe coprire il concetto fondamentale #1.
Rinforza il concetto con esempi e riferimenti.

CONCETTO #1:
Prompt Engineering.
Definiscilo e spiega perché è necessario.
-->

## Cos'è il Prompt Engineering?

Abbiamo iniziato questa lezione definendo il **Prompt Engineering** come il processo di _progettazione e ottimizzazione_ degli input testuali (prompt) per fornire risposte coerenti e di qualità (completion) per un dato obiettivo applicativo e modello. Possiamo pensarlo come un processo in 2 fasi:

- _progettare_ il prompt iniziale per un dato modello e obiettivo
- _perfezionare_ il prompt in modo iterativo per migliorare la qualità della risposta

Questo è necessariamente un processo di tentativi ed errori che richiede intuizione e impegno da parte dell’utente per ottenere risultati ottimali. Quindi perché è importante? Per rispondere a questa domanda, dobbiamo prima comprendere tre concetti:

- _Tokenizzazione_ = come il modello "vede" il prompt
- _Base LLMs_ = come il modello base "processa" un prompt
- _Instruction-Tuned LLMs_ = come il modello ora può vedere le "attività"

### Tokenizzazione

Un LLM vede i prompt come una _sequenza di token_ dove modelli diversi (o versioni di un modello) possono tokenizzare lo stesso prompt in modi differenti. Poiché gli LLM sono addestrati su token (e non su testo grezzo), il modo in cui i prompt vengono tokenizzati ha un impatto diretto sulla qualità della risposta generata.

Per farti un’idea di come funziona la tokenizzazione, prova strumenti come il [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrato qui sotto. Copia il tuo prompt - e osserva come viene convertito in token, facendo attenzione a come vengono trattati gli spazi bianchi e i segni di punteggiatura. Nota che questo esempio mostra un LLM più vecchio (GPT-3) - quindi provarlo con un modello più recente potrebbe dare un risultato diverso.

![Tokenizzazione](../../../translated_images/it/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concetto: Modelli Fondamentali

Una volta tokenizzato un prompt, la funzione principale del ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modello fondamentale) è prevedere il token successivo in quella sequenza. Poiché gli LLM sono addestrati su enormi dataset testuali, hanno una buona percezione delle relazioni statistiche tra token e possono fare quella previsione con una certa confidenza. Nota che non comprendono il _significato_ delle parole nel prompt o del token; vedono solo un modello che possono "completare" con la previsione successiva. Possono continuare a prevedere la sequenza fino a quando non vengono interrotti dall’intervento dell’utente o da una condizione predefinita.

Vuoi vedere come funziona il completamento basato su prompt? Inserisci il prompt soprastante nel [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) con le impostazioni predefinite. Il sistema è configurato per trattare i prompt come richieste di informazioni - quindi dovresti vedere un completamento che soddisfa questo contesto.

Ma cosa succede se l’utente voleva vedere qualcosa di specifico che soddisfi determinati criteri o obiettivi di attività? Qui entrano in gioco gli LLM _instruction-tuned_.

![Completamento chat Base LLM](../../../translated_images/it/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concetto: Instruction Tuned LLMs

Un [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte dal modello fondamentale e lo affina con esempi o coppie input/output (ad es. "messaggi" multi-turno) che possono contenere istruzioni chiare - e la risposta dell'IA cerca di seguire quell’istruzione.

Questo utilizza tecniche come l’apprendimento per rinforzo con feedback umano (RLHF) che può addestrare il modello a _seguire le istruzioni_ e _imparare dal feedback_ in modo da produrre risposte più adeguate alle applicazioni pratiche e più rilevanti per gli obiettivi degli utenti.

Proviamolo - riprendi il prompt sopra, ma ora cambia il _messaggio di sistema_ fornendo la seguente istruzione come contesto:

> _Riassumi i contenuti forniti per uno studente di seconda elementare. Tieni il risultato in un paragrafo con 3-5 punti elenco._

Vedi come il risultato è ora tarato per riflettere l’obiettivo e il formato desiderati? Un educatore può ora usare direttamente questa risposta nelle sue slide per quella lezione.

![Completamento chat Instruction Tuned LLM](../../../translated_images/it/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Perché abbiamo bisogno del Prompt Engineering?

Ora che sappiamo come i prompt vengono processati dagli LLM, parliamo del _perché_ abbiamo bisogno del prompt engineering. La risposta risiede nel fatto che gli LLM attuali presentano diverse sfide che rendono difficile ottenere _completamenti affidabili e coerenti_ senza dedicare impegno alla costruzione e all’ottimizzazione del prompt. Per esempio:

1. **Le risposte del modello sono stocastiche.** Lo _stesso prompt_ probabilmente produrrà risposte diverse con modelli o versioni diverse. E può produrre anche risultati differenti con _lo stesso modello_ in momenti diversi. _Le tecniche di prompt engineering possono aiutarci a minimizzare queste variazioni fornendo guide migliori_.

1. **I modelli possono fabbricare risposte.** I modelli sono pre-addestrati con dataset _grandi ma finiti_, quindi mancano di conoscenza su concetti al di fuori di quel campo di addestramento. Di conseguenza, possono produrre completamenti inaccurati, immaginari o direttamente contrari a fatti conosciuti. _Le tecniche di prompt engineering aiutano gli utenti a identificare e mitigare tali fabbricazioni, per esempio chiedendo citazioni o ragionamenti all’IA_.

1. **Le capacità dei modelli variano.** Modelli più recenti o nuove generazioni offrono capacità più ricche ma anche caratteristiche uniche e compromessi in termini di costi e complessità. _Il prompt engineering può aiutarci a sviluppare best practice e workflow che astraono le differenze e si adattano ai requisiti specifici del modello in modi scalabili e fluidi_.

Vediamolo in azione nell’OpenAI o nell’Azure OpenAI Playground:

- Usa lo stesso prompt con diverse distribuzioni LLM (es. OpenAI, Azure OpenAI, Hugging Face): hai notato le variazioni?
- Usa ripetutamente lo stesso prompt con la _stessa_ distribuzione LLM (es. Azure OpenAI playground): come sono cambiate queste variazioni?

### Esempio di Fabbricazioni

In questo corso, usiamo il termine **"fabbricazione"** per riferirci al fenomeno per cui gli LLM a volte generano informazioni fattualmente errate a causa di limiti nel loro addestramento o altri vincoli. Potresti aver sentito parlare di questo come _"allucinazioni"_ in articoli popolari o paper di ricerca. Tuttavia, raccomandiamo fortemente di usare _"fabbricazione"_ come termine per non antropomorfizzare accidentalmente il comportamento attribuendo un tratto umano a un risultato guidato dalla macchina. Questo rafforza anche le [linee guida sull’IA responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) da una prospettiva terminologica, rimuovendo termini che potrebbero essere considerati offensivi o non inclusivi in alcuni contesti.

Vuoi capire come funzionano le fabbricazioni? Pensa a un prompt che istruisce l’IA a generare contenuti per un argomento inesistente (per assicurarti che non sia presente nel dataset di addestramento). Per esempio - ho provato questo prompt:

> **Prompt:** genera un piano di lezione per la Guerra Marziana del 2076.

Una ricerca web mi ha mostrato che esistono racconti di fantasia (ad es. serie televisive o libri) sulle guerre marziane - ma nessuna nel 2076. Il buon senso ci dice anche che il 2076 è _nel futuro_ e quindi non può essere associato a un evento reale.


Cosa succede quindi quando eseguiamo questo prompt con diversi fornitori di LLM?

> **Risposta 1**: OpenAI Playground (GPT-35)

![Risposta 1](../../../translated_images/it/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Risposta 2**: Azure OpenAI Playground (GPT-35)

![Risposta 2](../../../translated_images/it/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Risposta 3**: : Hugging Face Chat Playground (LLama-2)

![Risposta 3](../../../translated_images/it/04-fabrication-huggingchat.faf82a0a51278956.webp)

Come previsto, ogni modello (o versione del modello) produce risposte leggermente diverse grazie a comportamenti stocastici e variazioni nelle capacità del modello. Ad esempio, un modello si rivolge a un pubblico di ottava elementare mentre l'altro assume uno studente delle superiori. Ma tutti e tre i modelli hanno generato risposte che potrebbero convincere un utente non informato che l’evento fosse reale.

Tecniche di prompt engineering come _metaprompting_ e _configurazione della temperatura_ possono ridurre in qualche misura le fabbricazioni del modello. Nuove _architetture_ di prompt engineering integrano anche nuovi strumenti e tecniche senza soluzione di continuità nel flusso del prompt, per mitigare o ridurre alcuni di questi effetti.

## Caso di Studio: GitHub Copilot

Concludiamo questa sezione dando un’idea di come il prompt engineering venga utilizzato in soluzioni reali guardando un caso di studio: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot è il tuo "programmatore AI in coppia" - converte prompt testuali in completamenti di codice ed è integrato nel tuo ambiente di sviluppo (es. Visual Studio Code) per un’esperienza utente fluida. Come documentato nella serie di blog qui sotto, la versione più originaria si basava sul modello OpenAI Codex - con ingegneri che hanno rapidamente compreso la necessità di affinare il modello e sviluppare migliori tecniche di prompt engineering per migliorare la qualità del codice. A luglio, hanno [presentato un modello AI migliore che va oltre Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) per suggerimenti ancora più rapidi.

Leggi i post in ordine per seguire il loro percorso di apprendimento.

- **Maggio 2023** | [GitHub Copilot migliora la comprensione del tuo codice](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maggio 2023** | [Dentro GitHub: lavorare con i LLM dietro GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Giugno 2023** | [Come scrivere prompt migliori per GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Luglio 2023** | [.. GitHub Copilot va oltre Codex con un modello AI migliorato](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Luglio 2023** | [Guida per sviluppatori al Prompt Engineering e LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Settembre 2023** | [Come costruire una app LLM aziendale: lezioni da GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Puoi anche sfogliare il loro [blog di Ingegneria](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) per altri post come [questo](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) che mostrano come questi modelli e tecniche vengano _applicati_ per alimentare applicazioni del mondo reale.

---

<!--
TEMPLATE DELLA LEZIONE:
Questa unità dovrebbe coprire il concetto chiave #2.
Rinforza il concetto con esempi e riferimenti.

CONCETTO #2:
Progettazione del Prompt.
Illustrato con esempi.
-->

## Costruzione del Prompt

Abbiamo visto perché il prompt engineering è importante - ora capiamo come i prompt vengono _costruiti_ così possiamo valutare diverse tecniche per una progettazione del prompt più efficace.

### Prompt Base

Iniziamo con il prompt base: un input testuale inviato al modello senza altro contesto. Ecco un esempio - quando inviamo le prime parole dell’inno nazionale degli USA all’OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) completa istantaneamente la risposta con le righe successive, illustrando il comportamento predittivo di base.

| Prompt (Input)     | Completamento (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Sembra che tu stia iniziando il testo di "The Star-Spangled Banner", l’inno nazionale degli Stati Uniti. Il testo completo è ...             |

### Prompt Complesso

Ora aggiungiamo contesto e istruzioni a quel prompt base. La [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) ci permette di costruire un prompt complesso come una raccolta di _messaggi_ con:

- Coppie input/output che riflettono l’input _utente_ e la risposta _assistente_.
- Messaggio di sistema che imposta il contesto per il comportamento o la personalità dell’assistente.

La richiesta ora è nella forma sottostante, dove la _tokenizzazione_ cattura efficacemente informazioni rilevanti dal contesto e dalla conversazione. Ora, cambiare il contesto di sistema può essere altrettanto impattante sulla qualità dei completamenti quanto gli input utente forniti.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt con Istruzioni

Negli esempi sopra, il prompt utente era una semplice query testuale che può essere interpretata come una richiesta di informazioni. Con i prompt a _istruzioni_, possiamo usare quel testo per specificare un compito in modo più dettagliato, fornendo una guida migliore all’AI. Ecco un esempio:

| Prompt (Input)                                                                                                                                                                                                                         | Completamento (Output)                                                                                                        | Tipo di Istruzione |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _ha restituito un semplice paragrafo_                                                                                       | Semplice           |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _ha restituito un paragrafo seguito da una lista di date chiave con descrizioni_                                             | Complesso          |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _restituisce dettagli più estesi in una casella di testo, formattati come JSON da poter copiare/incollare su un file e convalidare secondo necessità_ | Complesso. Formattato. |

## Contenuto Primario

Negli esempi sopra, il prompt era ancora abbastanza aperto, lasciando all’LLM la decisione su quale parte del suo dataset pre-addestrato fosse rilevante. Con il pattern di progettazione _contenuto primario_, il testo di input è diviso in due parti:

- un’istruzione (azione)
- contenuto rilevante (che influenza l’azione)

Ecco un esempio in cui l’istruzione è “riassumere questo in 2 frasi”.

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completamento (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus. <br/> **Summarize this in 2 short sentences** | Giove, il quinto pianeta dal Sole, è il più grande del Sistema Solare e noto per essere uno degli oggetti più luminosi nel cielo notturno. Chiamato come il dio romano Giove, è un gigante gassoso la cui massa è due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme.                     |

Il segmento di contenuto primario può essere usato in vari modi per guidare istruzioni più efficaci:

- **Esempi** - invece di dire esplicitamente al modello cosa fare con un’istruzione precisa, dargli esempi di cosa fare e lasciargli dedurre il modello.
- **Suggerimenti** - seguire l’istruzione con un "segnale" che stimola il completamento, guidando il modello verso risposte più rilevanti.
- **Template** - queste sono 'ricette' ripetibili per prompt con segnaposto (variabili) personalizzabili con dati per casi specifici.

Esploriamoli in azione.

### Uso di Esempi

Approccio che usa il contenuto primario per "nutrire il modello" con esempi del risultato desiderato per una data istruzione, lasciando al modello dedurre il modello di output desiderato. In base al numero di esempi forniti, possiamo avere zero-shot prompting, one-shot prompting, few-shot prompting ecc.

Ora il prompt consiste in tre componenti:

- Una descrizione del compito
- Alcuni esempi dell’output desiderato
- L’inizio di un nuovo esempio (che diventa una descrizione implicita del compito)

| Tipo di Apprendimento | Prompt (Input)                                                                                                                                        | Completamento (Output)         |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
| Zero-shot             | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".        |
| One-shot              | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso".     |
| Few-shot              | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                     |
|                       |                                                                                                                                                       |                               |

Nota come abbiamo dovuto fornire istruzioni esplicite ("Translate to Spanish") nel prompting zero-shot, ma queste vengono dedotte nell’esempio one-shot. L’esempio few-shot mostra come aggiungere più esempi permetta ai modelli di fare inferenze più accurate senza istruzioni aggiunte.

### Suggerimenti per il Prompt

Un’altra tecnica per usare il contenuto primario è fornire _suggerimenti_ piuttosto che esempi. In questo caso, stiamo dando al modello una spinta nella direzione giusta iniziando con un frammento che riflette il formato di risposta desiderato. Il modello quindi "prende il suggerimento" e continua in quella direzione.

| Numero di Suggerimenti | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completamento (Output)                                                                                                                                                                                                                                                                                       |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                      | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This**                                       | Giove è il pianeta più grande del nostro Sistema Solare e il quinto dal Sole. È un gigante gassoso con una massa pari a 1/1000 di quella del Sole, ma è più pesante di tutti gli altri pianeti messi insieme. Le civiltà antiche conoscono Giove da molto tempo ed è facilmente visibile nel cielo notturno.       |
| 1                      | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br/>**Summarize This** <br/> What we learned is that Jupiter | è il quinto pianeta dal Sole ed è il più grande nel Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti messi insieme. È facilmente visibile a occhio nudo ed è noto sin dall’antichità.                           |

| 2              | Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. È un gigante gassoso con una massa pari a un millesimo di quella del Sole, ma due volte e mezzo quella di tutti gli altri pianeti del Sistema Solare messi insieme. Giove è uno degli oggetti più luminosi visibili a occhio nudo nel cielo notturno, ed è noto alle civiltà antiche fin da prima della storia registrata. <br/>**Riassumi Questo** <br/> Le 3 Principali Informazioni Che Abbiamo Imparato:         | 1. Giove è il quinto pianeta dal Sole ed il più grande del Sistema Solare. <br/> 2. È un gigante gassoso con una massa pari a un millesimo di quella del Sole...<br/> 3. Giove è visibile ad occhio nudo fin dai tempi antichi ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Modelli di Prompt

Un modello di prompt è una _ricetta predefinita per un prompt_ che può essere archiviata e riutilizzata secondo necessità, per fornire esperienze utente più coerenti su larga scala. Nella sua forma più semplice, è semplicemente una raccolta di esempi di prompt come [questo di OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) che fornisce sia i componenti interattivi del prompt (messaggi utente e di sistema) sia il formato di richiesta API - per supportare il riutilizzo.

Nella sua forma più complessa come [questo esempio di LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) contiene _segnaposto_ che possono essere sostituiti con dati provenienti da varie fonti (input utente, contesto di sistema, fonti dati esterne ecc.) per generare un prompt dinamicamente. Questo ci permette di creare una libreria di prompt riutilizzabili che possono essere usati per guidare esperienze utente coerenti **programmaticamente** su larga scala.

Infine, il vero valore dei modelli risiede nella capacità di creare e pubblicare _librerie di prompt_ per domini applicativi verticali - dove il modello di prompt è ora _ottimizzato_ per riflettere un contesto o esempi specifici dell’applicazione che rendono le risposte più pertinenti e accurate per il pubblico di utenti target. Il repository [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) è un ottimo esempio di questo approccio, raccogliendo una libreria di prompt per il dominio educativo con enfasi su obiettivi chiave come la pianificazione delle lezioni, la progettazione dei curricula, il tutoraggio degli studenti ecc.

## Contenuto di Supporto

Se consideriamo la costruzione di un prompt come composta da una istruzione (compito) e un target (contenuto principale), allora il _contenuto secondario_ è come un contesto aggiuntivo che forniamo per **influenzare in qualche modo l’output**. Potrebbe trattarsi di parametri di regolazione, istruzioni di formattazione, tassonomie di argomenti ecc. che possono aiutare il modello a _personalizzare_ la sua risposta per soddisfare gli obiettivi o le aspettative desiderate dall’utente.

Ad esempio: dato un catalogo corsi con metadata estesi (nome, descrizione, livello, tag dei metadata, istruttore ecc.) su tutti i corsi disponibili nel curriculum:

- possiamo definire un’istruzione per "riassumere il catalogo corsi per l’autunno 2023"
- possiamo usare il contenuto primario per fornire alcuni esempi dell’output desiderato
- possiamo usare il contenuto secondario per identificare i 5 "tag" di interesse più importanti.

Ora, il modello può fornire un riassunto nel formato mostrato dai pochi esempi - ma se un risultato ha più tag, può dare priorità ai 5 tag identificati nel contenuto secondario.

---

<!--
TEMPLATE DELLA LEZIONE:
Questa unità dovrebbe coprire il concetto fondamentale #1.
Rafforzare il concetto con esempi e riferimenti.

CONCETTO #3:
Tecniche di Prompt Engineering.
Quali sono alcune tecniche di base per il prompt engineering?
Illustrale con alcuni esercizi.
-->

## Migliori Pratiche per il Prompting

Ora che sappiamo come i prompt possono essere _costruiti_, possiamo iniziare a pensare a come _progettarli_ per riflettere le migliori pratiche. Possiamo considerare questo in due parti - avere il giusto _mindset_ e applicare le giuste _tecniche_.

### Mentalità del Prompt Engineering

Il Prompt Engineering è un processo di tentativi ed errori, quindi tieni a mente tre fattori guida ampi:

1. **La Comprensione del Dominio è Importante.** L’accuratezza e la pertinenza della risposta dipendono dal _dominio_ in cui quell’applicazione o utente opera. Applica la tua intuizione ed esperienza di dominio per **personalizzare ulteriormente le tecniche**. Per esempio, definisci _personalità specifiche del dominio_ nei tuoi prompt di sistema, oppure usa _modelli specifici del dominio_ nei prompt utente. Fornisci contenuti secondari che riflettano contesti specifici del dominio, o usa _indizi ed esempi specifici del dominio_ per indirizzare il modello verso schemi d’uso familiari.

2. **La Comprensione del Modello è Importante.** Sappiamo che i modelli sono di natura stocastica. Ma le implementazioni dei modelli possono anche variare in termini di dataset di addestramento utilizzato (conoscenza pre-addestrata), capacità offerte (es. via API o SDK) e tipo di contenuto per cui sono ottimizzati (es. codice vs immagini vs testo). Comprendi i punti di forza e i limiti del modello che stai usando, e usa quella conoscenza per _prioritizzare i compiti_ o costruire _modelli personalizzati_ ottimizzati per le capacità del modello.

3. **Iterazione e Validazione Sono Importanti.** I modelli stanno evolvendo rapidamente, così come le tecniche di prompt engineering. In quanto esperto del dominio, potresti avere altro contesto o criteri per _la tua_ applicazione specifica, che potrebbero non valere per la comunità più ampia. Usa strumenti e tecniche di prompt engineering per "dare il via" alla costruzione del prompt, poi itera e valida i risultati usando la tua intuizione ed esperienza di dominio. Registra le tue intuizioni e crea una **base di conoscenza** (es. librerie di prompt) che può essere usata come nuovo punto di partenza da altri, per iterazioni più rapide in futuro.

## Migliori Pratiche

Ora diamo un’occhiata alle migliori pratiche comuni raccomandate da [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) e dai professionisti di [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Cosa                             | Perché                                                                                                                                                                                                                                             |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Valutare i modelli più recenti. | Le nuove generazioni di modelli probabilmente avranno funzionalità e qualità migliorate - ma potrebbero anche comportare costi più elevati. Valutali per l’impatto, poi prendi decisioni di migrazione.                                             |
| Separare istruzioni e contesto  | Verifica se il tuo modello/fornitore definisce _delimitatori_ per distinguere istruzioni, contenuti primari e secondari in modo più chiaro. Questo può aiutare i modelli ad assegnare pesi ai token in modo più accurato.                            |
| Essere specifici e chiari        | Fornisci più dettagli riguardo al contesto desiderato, risultato, lunghezza, formato, stile ecc. Questo migliorerà sia qualità che coerenza delle risposte. Registra ricette in modelli riutilizzabili.                                           |
| Essere descrittivi, usare esempi | I modelli possono rispondere meglio con un approccio “mostra e racconta”. Inizia con un approccio `zero-shot` dove dai un’istruzione (ma senza esempi), poi prova `few-shot` come raffinamento, fornendo alcuni esempi dell’output desiderato. Usa analogie. |
| Usa indizi per avviare le risposte | Spingilo verso un risultato desiderato fornendo alcune parole o frasi iniziali che può usare come punto di partenza per la risposta.                                                                                                            |
| Insisti                        | A volte potresti dover ripetere le istruzioni al modello. Dai istruzioni prima e dopo il contenuto principale, usa un’istruzione e un indizio, ecc. Itera e valida per vedere cosa funziona.                                                       |
| L’Ordine Conta                  | L’ordine in cui presenti le informazioni al modello può influenzare l’output, anche negli esempi di apprendimento, grazie al bias di recenza. Prova diverse opzioni per vedere cosa funziona meglio.                                               |
| Dai al modello una “via d’uscita” | Fornisci al modello una risposta _fallback_ che può fornire se non può completare il compito per qualche motivo. Questo può ridurre le probabilità che generi risposte false o inventate.                                                       |
|                                 |                                                                                                                                                                                                                                                   |

Come per ogni migliore pratica, ricorda che _la tua esperienza può variare_ in base al modello, al compito e al dominio. Usale come punto di partenza, e itera per trovare ciò che funziona meglio per te. Rivaluta costantemente il tuo processo di prompt engineering man mano che nuovi modelli e strumenti diventano disponibili, con un focus sulla scalabilità del processo e la qualità della risposta.

<!--
TEMPLATE DELLA LEZIONE:
Questa unità dovrebbe fornire una sfida di codice se applicabile

SFIDA:
Collega un Jupyter Notebook con solo i commenti di codice nelle istruzioni (le sezioni di codice sono vuote).

SOLUZIONE:
Collega una copia di quel Notebook con i prompt compilati e eseguiti, mostrando un esempio di output.
-->

## Compito

Congratulazioni! Sei arrivato alla fine della lezione! È ora di mettere alla prova alcuni di quei concetti e tecniche con esempi reali!

Per il nostro compito useremo un Jupyter Notebook con esercizi che puoi completare interattivamente. Puoi anche estendere il Notebook con tue celle Markdown e di codice per esplorare idee e tecniche in autonomia.

### Per iniziare, fork del repo, quindi

- (Consigliato) Avvia GitHub Codespaces
- (In alternativa) Clona il repo sul tuo dispositivo locale e usalo con Docker Desktop
- (In alternativa) Apri il Notebook con il tuo ambiente di runtime preferito.

### Successivamente, configura le tue variabili ambientali

- Copia il file `.env.copy` nella root del repo in `.env` e compila i valori di `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_DEPLOYMENT`. Torna alla [sezione Learning Sandbox](#sandbox-di-apprendimento) per imparare come fare.

### Poi, apri il Jupyter Notebook

- Seleziona il kernel di runtime. Se usi le opzioni 1 o 2, seleziona semplicemente il kernel Python 3.10.x predefinito fornito dal contenitore di sviluppo.

Sei pronto per eseguire gli esercizi. Nota che qui non ci sono risposte _giuste o sbagliate_ - solo esplorazione tramite tentativi ed errori e costruzione di intuizione su cosa funziona per un dato modello e dominio applicativo.

_Per questo motivo non ci sono segmenti di Soluzione al Codice in questa lezione. Invece, il Notebook avrà celle Markdown intitolate "La Mia Soluzione:" che mostrano un esempio di output a titolo di riferimento._

 <!--
TEMPLATE DELLA LEZIONE:
Concludi la sezione con un sommario e risorse per l’apprendimento autodiretto.
-->

## Verifica delle conoscenze

Quale dei seguenti è un buon prompt seguendo alcune pratiche ragionevoli?

1. Mostrami un'immagine di un’auto rossa
2. Mostrami un’immagine di un’auto rossa marca Volvo e modello XC90 parcheggiata su una scogliera con il sole al tramonto
3. Mostrami un’immagine di un’auto rossa marca Volvo e modello XC90

A: 2, è il miglior prompt in quanto fornisce dettagli su "cosa" e entra nei particolari (non una qualsiasi auto ma una marca e modello specifici) e descrive anche l’ambientazione complessiva. Il 3 è il secondo migliore poiché contiene anch’esso molta descrizione.

## 🚀 Sfida

Vedi se puoi sfruttare la tecnica delle "indicazioni" con il prompt: Completa la frase "Mostrami un’immagine di un’auto rossa marca Volvo e ". Come risponde, e come lo miglioreresti?

## Ottimo Lavoro! Continua ad Imparare

Vuoi saperne di più su diversi concetti di Prompt Engineering? Vai alla [pagina di apprendimento continuato](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per trovare altre ottime risorse su questo tema.

Vai alla Lezione 5 dove vedremo [tecniche avanzate di prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->