<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T09:50:46+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "it"
}
-->
# Introduzione all'IA Generativa e ai Modelli di Linguaggio di Grandi Dimensioni

[![Introduzione all'IA Generativa e ai Modelli di Linguaggio di Grandi Dimensioni](../../../translated_images/01-lesson-banner.2424cfd092f43366707ee2d15749f62f76f80ea3cb0816f4f31d0abd5ffd4dd1.it.png)](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

_(Clicca sull'immagine sopra per vedere il video di questa lezione)_

L'IA generativa è un'intelligenza artificiale in grado di generare testo, immagini e altri tipi di contenuti. Ciò che la rende una tecnologia fantastica è che democratizza l'IA, chiunque può usarla con solo un prompt testuale, una frase scritta in linguaggio naturale. Non è necessario imparare un linguaggio come Java o SQL per realizzare qualcosa di utile, tutto ciò che serve è usare il proprio linguaggio, esprimere ciò che si desidera e un modello di IA fornisce un suggerimento. Le applicazioni e l'impatto di questo sono enormi: puoi scrivere o comprendere report, redigere applicazioni e molto altro, tutto in pochi secondi.

In questo curriculum, esploreremo come la nostra startup sfrutta l'IA generativa per sbloccare nuovi scenari nel mondo dell'educazione e come affrontiamo le inevitabili sfide legate alle implicazioni sociali della sua applicazione e ai limiti della tecnologia.

## Introduzione

Questa lezione coprirà:

- Introduzione allo scenario aziendale: la nostra idea di startup e missione.
- IA generativa e come siamo arrivati all'attuale panorama tecnologico.
- Funzionamento interno di un modello di linguaggio di grandi dimensioni.
- Principali capacità e casi d'uso pratici dei Modelli di Linguaggio di Grandi Dimensioni.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, comprenderai:

- Cos'è l'IA generativa e come funzionano i Modelli di Linguaggio di Grandi Dimensioni.
- Come puoi sfruttare i modelli di linguaggio di grandi dimensioni per diversi casi d'uso, con un focus sugli scenari educativi.

## Scenario: la nostra startup educativa

L'Intelligenza Artificiale Generativa (IA) rappresenta l'apice della tecnologia IA, spingendo i confini di ciò che una volta si pensava impossibile. I modelli di IA generativa hanno diverse capacità e applicazioni, ma per questo curriculum esploreremo come sta rivoluzionando l'educazione attraverso una startup fittizia. Ci riferiremo a questa startup come _la nostra startup_. La nostra startup opera nel settore dell'educazione con la dichiarazione di missione ambiziosa di

> _migliorare l'accessibilità all'apprendimento, su scala globale, garantendo un accesso equo all'educazione e fornendo esperienze di apprendimento personalizzate a ogni studente, secondo le loro esigenze_.

Il team della nostra startup è consapevole che non sarà in grado di raggiungere questo obiettivo senza sfruttare uno degli strumenti più potenti dei tempi moderni: i Modelli di Linguaggio di Grandi Dimensioni (LLM).

Si prevede che l'IA generativa rivoluzionerà il modo in cui apprendiamo e insegniamo oggi, con gli studenti che hanno a disposizione insegnanti virtuali 24 ore al giorno che forniscono grandi quantità di informazioni ed esempi, e gli insegnanti in grado di sfruttare strumenti innovativi per valutare i loro studenti e fornire feedback.

![Cinque giovani studenti che guardano un monitor - immagine di DALLE2](../../../translated_images/students-by-DALLE2.b70fddaced1042ee47092320243050c4c9a7da78b31eeba515b09b2f0dca009b.it.png)

Per iniziare, definiamo alcuni concetti e terminologia di base che useremo durante il curriculum.

## Come abbiamo ottenuto l'IA Generativa?

Nonostante l'enorme _hype_ creato ultimamente dall'annuncio dei modelli di IA generativa, questa tecnologia è in lavorazione da decenni, con i primi sforzi di ricerca che risalgono agli anni '60. Siamo ora a un punto in cui l'IA possiede capacità cognitive umane, come la conversazione, come mostrato ad esempio da [OpenAI ChatGPT](https://openai.com/chatgpt) o [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), che utilizza anche un modello GPT per le conversazioni di ricerca web di Bing.

Facendo un passo indietro, i primissimi prototipi di IA consistevano in chatbot scritti a macchina, basati su una base di conoscenza estratta da un gruppo di esperti e rappresentata in un computer. Le risposte nella base di conoscenza venivano attivate da parole chiave presenti nel testo di input.
Tuttavia, divenne presto chiaro che un tale approccio, utilizzando chatbot scritti a macchina, non si adattava bene.

### Un approccio statistico all'IA: Machine Learning

Un punto di svolta arrivò negli anni '90, con l'applicazione di un approccio statistico all'analisi del testo. Questo portò allo sviluppo di nuovi algoritmi – conosciuti come machine learning – capaci di apprendere modelli dai dati senza essere esplicitamente programmati. Questo approccio permette alle macchine di simulare la comprensione del linguaggio umano: un modello statistico viene addestrato su coppie di testo-etichetta, permettendo al modello di classificare il testo di input sconosciuto con un'etichetta predefinita che rappresenta l'intenzione del messaggio.

### Reti neurali e assistenti virtuali moderni

Negli ultimi anni, l'evoluzione tecnologica dell'hardware, in grado di gestire quantità maggiori di dati e calcoli più complessi, ha incoraggiato la ricerca nell'IA, portando allo sviluppo di algoritmi di machine learning avanzati noti come reti neurali o algoritmi di deep learning.

Le reti neurali (e in particolare le Reti Neurali Ricorrenti – RNN) hanno significativamente migliorato l'elaborazione del linguaggio naturale, permettendo la rappresentazione del significato del testo in modo più significativo, valorizzando il contesto di una parola in una frase.

Questa è la tecnologia che ha alimentato gli assistenti virtuali nati nel primo decennio del nuovo secolo, molto abili nell'interpretare il linguaggio umano, identificare un bisogno e compiere un'azione per soddisfarlo – come rispondere con uno script predefinito o utilizzare un servizio di terze parti.

### Oggi, IA Generativa

Ecco come siamo arrivati all'IA Generativa oggi, che può essere vista come un sottoinsieme del deep learning.

![IA, ML, DL e IA Generativa](../../../translated_images/AI-diagram.c391fa518451a40de58d4f792c88adb8568d8cb4c48eed6e97b6b16e621eeb77.it.png)

Dopo decenni di ricerca nel campo dell'IA, una nuova architettura di modelli – chiamata _Transformer_ – ha superato i limiti delle RNN, essendo in grado di ricevere sequenze di testo molto più lunghe come input. I Transformer sono basati sul meccanismo di attenzione, permettendo al modello di dare pesi diversi agli input che riceve, 'prestando maggiore attenzione' dove le informazioni più rilevanti sono concentrate, indipendentemente dal loro ordine nella sequenza di testo.

La maggior parte dei recenti modelli di IA generativa – noti anche come Modelli di Linguaggio di Grandi Dimensioni (LLM), poiché lavorano con input e output testuali – sono infatti basati su questa architettura. Ciò che è interessante di questi modelli – addestrati su una grande quantità di dati non etichettati provenienti da fonti diverse come libri, articoli e siti web – è che possono essere adattati a una vasta gamma di compiti e generare testo grammaticalmente corretto con un'apparenza di creatività. Quindi, non solo hanno incredibilmente migliorato la capacità di una macchina di 'comprendere' un testo di input, ma hanno abilitato la capacità di generare una risposta originale in linguaggio umano.

## Come funzionano i modelli di linguaggio di grandi dimensioni?

Nel prossimo capitolo esploreremo diversi tipi di modelli di IA generativa, ma per ora diamo un'occhiata a come funzionano i modelli di linguaggio di grandi dimensioni, con un focus sui modelli OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, testo in numeri**: I Modelli di Linguaggio di Grandi Dimensioni ricevono un testo come input e generano un testo come output. Tuttavia, essendo modelli statistici, funzionano molto meglio con i numeri rispetto alle sequenze di testo. Ecco perché ogni input al modello viene elaborato da un tokenizer, prima di essere utilizzato dal modello principale. Un token è un frammento di testo – costituito da un numero variabile di caratteri, quindi il compito principale del tokenizer è dividere l'input in un array di token. Poi, ogni token viene mappato con un indice di token, che è la codifica intera del frammento di testo originale.

![Esempio di tokenizzazione](../../../translated_images/tokenizer-example.80a5c151ee7d1bd485eff5aca60ac3d2c1eaaff4c0746e09b98c696c959afbfa.it.png)

- **Predizione dei token di output**: Dati n token come input (con max n variabile da un modello all'altro), il modello è in grado di prevedere un token come output. Questo token viene poi incorporato nell'input dell'iterazione successiva, in un pattern di finestra espandibile, permettendo un'esperienza utente migliore di ottenere una (o più) frase come risposta. Questo spiega perché, se hai mai giocato con ChatGPT, potresti aver notato che a volte sembra fermarsi nel mezzo di una frase.

- **Processo di selezione, distribuzione di probabilità**: Il token di output viene scelto dal modello secondo la sua probabilità di verificarsi dopo la sequenza di testo corrente. Questo perché il modello prevede una distribuzione di probabilità su tutti i possibili 'token successivi', calcolata in base al suo addestramento. Tuttavia, non sempre il token con la probabilità più alta viene scelto dalla distribuzione risultante. Un grado di casualità viene aggiunto a questa scelta, in modo che il modello agisca in modo non deterministico - non otteniamo esattamente lo stesso output per lo stesso input. Questo grado di casualità viene aggiunto per simulare il processo di pensiero creativo e può essere regolato utilizzando un parametro del modello chiamato temperatura.

## Come può la nostra startup sfruttare i Modelli di Linguaggio di Grandi Dimensioni?

Ora che abbiamo una migliore comprensione del funzionamento interno di un modello di linguaggio di grandi dimensioni, vediamo alcuni esempi pratici dei compiti più comuni che possono svolgere abbastanza bene, con uno sguardo al nostro scenario aziendale.
Abbiamo detto che la capacità principale di un Modello di Linguaggio di Grandi Dimensioni è _generare un testo da zero, a partire da un input testuale, scritto in linguaggio naturale_.

Ma che tipo di input e output testuale?
L'input di un modello di linguaggio di grandi dimensioni è noto come prompt, mentre l'output è noto come completamento, termine che si riferisce al meccanismo del modello di generare il prossimo token per completare l'input corrente. Approfondiremo cosa è un prompt e come progettarlo in modo da ottenere il massimo dal nostro modello. Ma per ora, diciamo solo che un prompt può includere:

- Una **istruzione** che specifica il tipo di output che ci aspettiamo dal modello. Questa istruzione a volte può includere alcuni esempi o dati aggiuntivi.

  1. Sintesi di un articolo, libro, recensioni di prodotti e altro, insieme all'estrazione di intuizioni da dati non strutturati.
    
    ![Esempio di sintesi](../../../translated_images/summarization-example.7b7ff97147b3d790477169f442b5e3f8f78079f152450e62c45dbdc23b1423c1.it.png)
  
  2. Ideazione creativa e progettazione di un articolo, un saggio, un compito o altro.
      
     ![Esempio di scrittura creativa](../../../translated_images/creative-writing-example.e24a685b5a543ad1287ad8f6c963019518920e92a1cf7510f354e85b0830fbe8.it.png)

- Una **domanda**, posta sotto forma di conversazione con un agente.
  
  ![Esempio di conversazione](../../../translated_images/conversation-example.60c2afc0f595fa599f367d36ccc3909ffc15e1d5265cb33b907d3560f3d03116.it.png)

- Un frammento di **testo da completare**, che implicitamente è una richiesta di assistenza alla scrittura.
  
  ![Esempio di completamento del testo](../../../translated_images/text-completion-example.cbb0f28403d427524f8f8c935f84d084a9765b683a6bf37f977df3adb868b0e7.it.png)

- Un frammento di **codice** insieme alla richiesta di spiegare e documentare, o un commento che chiede di generare un pezzo di codice che svolge un compito specifico.
  
  ![Esempio di codice](../../../translated_images/coding-example.50ebabe8a6afff20267c91f18aab1957ddd9561ee2988b2362b7365aa6796935.it.png)

Gli esempi sopra sono piuttosto semplici e non sono destinati a essere una dimostrazione esaustiva delle capacità dei Modelli di Linguaggio di Grandi Dimensioni. Sono pensati per mostrare il potenziale dell'uso dell'IA generativa, in particolare ma non limitato ai contesti educativi.

Inoltre, l'output di un modello di IA generativa non è perfetto e a volte la creatività del modello può lavorare contro di esso, risultando in un output che è una combinazione di parole che l'utente umano può interpretare come una mistificazione della realtà, o può essere offensivo. L'IA generativa non è intelligente - almeno nella definizione più comprensiva di intelligenza, che include il ragionamento critico e creativo o l'intelligenza emotiva; non è deterministica, e non è affidabile, poiché fabbricazioni, come riferimenti errati, contenuti e affermazioni, possono essere combinati con informazioni corrette e presentati in modo persuasivo e sicuro. Nelle lezioni seguenti, affronteremo tutte queste limitazioni e vedremo cosa possiamo fare per mitigarle.

## Compito

Il tuo compito è leggere di più sull'[IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) e provare a identificare un'area in cui aggiungeresti l'IA generativa oggi che non la ha. In che modo l'impatto sarebbe diverso dal farlo "alla vecchia maniera", puoi fare qualcosa che non potevi prima, o sei più veloce? Scrivi un riassunto di 300 parole su come sarebbe la tua startup AI da sogno e includi intestazioni come "Problema", "Come userei l'IA", "Impatto" e opzionalmente un piano aziendale.

Se hai svolto questo compito, potresti anche essere pronto per candidarti all'incubatore di Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) offriamo crediti sia per Azure, OpenAI, mentoring e molto altro, dai un'occhiata!

## Verifica della conoscenza

Cosa è vero sui modelli di linguaggio di grandi dimensioni?

1. Ottieni la stessa risposta ogni volta.
1. Fa le cose perfettamente, ottimo nel sommare numeri, produrre codice funzionante ecc.
1. La risposta può variare nonostante l'uso dello stesso prompt. È anche ottimo nel darti una prima bozza di qualcosa, sia testo che codice. Ma devi migliorare i risultati.

A: 3, un LLM è non deterministico, la risposta varia, tuttavia, puoi controllare la sua varianza tramite un'impostazione di temperatura. Inoltre, non dovresti aspettarti che faccia le cose perfettamente, è qui per fare il lavoro pesante per te, il che spesso significa che ottieni un buon primo tentativo di qualcosa che devi gradualmente migliorare.

## Ottimo lavoro! Continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza sull'IA generativa!

Vai alla Lezione 2 dove esamineremo come [esplorare e confrontare diversi tipi di LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.