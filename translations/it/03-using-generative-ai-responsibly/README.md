<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-05-19T14:38:23+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "it"
}
-->
# Uso responsabile dell'AI generativa

> _Clicca sull'immagine sopra per vedere il video di questa lezione_

È facile essere affascinati dall'AI, e in particolare dall'AI generativa, ma è necessario considerare come usarla in modo responsabile. Bisogna pensare a come garantire che il risultato sia equo, non dannoso e altro ancora. Questo capitolo mira a fornire il contesto menzionato, cosa considerare e come intraprendere passi attivi per migliorare l'uso dell'AI.

## Introduzione

Questa lezione coprirà:

- Perché dovresti dare priorità all'AI responsabile quando costruisci applicazioni di AI generativa.
- I principi fondamentali dell'AI responsabile e come si relazionano all'AI generativa.
- Come mettere in pratica questi principi di AI responsabile attraverso strategie e strumenti.

## Obiettivi di apprendimento

Dopo aver completato questa lezione saprai:

- L'importanza dell'AI responsabile quando costruisci applicazioni di AI generativa.
- Quando pensare e applicare i principi fondamentali dell'AI responsabile nella costruzione di applicazioni di AI generativa.
- Quali strumenti e strategie sono disponibili per mettere in pratica il concetto di AI responsabile.

## Principi di AI responsabile

L'entusiasmo per l'AI generativa non è mai stato così alto. Questo entusiasmo ha portato molti nuovi sviluppatori, attenzione e finanziamenti in questo settore. Sebbene ciò sia molto positivo per chiunque voglia costruire prodotti e aziende utilizzando l'AI generativa, è anche importante procedere in modo responsabile.

Durante questo corso, ci concentriamo sulla costruzione della nostra startup e del nostro prodotto educativo AI. Utilizzeremo i principi dell'AI responsabile: equità, inclusività, affidabilità/sicurezza, sicurezza e privacy, trasparenza e responsabilità. Con questi principi, esploreremo come si relazionano al nostro uso dell'AI generativa nei nostri prodotti.

## Perché dovresti dare priorità all'AI responsabile

Quando costruisci un prodotto, adottare un approccio incentrato sull'essere umano mantenendo in mente il miglior interesse dell'utente porta ai migliori risultati.

L'unicità dell'AI generativa è il suo potere di creare risposte utili, informazioni, guide e contenuti per gli utenti. Questo può essere fatto senza molti passaggi manuali che possono portare a risultati molto impressionanti. Senza una pianificazione e strategie adeguate, può anche purtroppo portare a risultati dannosi per i tuoi utenti, il tuo prodotto e la società nel suo complesso.

Esaminiamo alcuni (ma non tutti) di questi potenziali risultati dannosi:

### Allucinazioni

Le allucinazioni sono un termine usato per descrivere quando un LLM produce contenuti che sono completamente privi di senso o qualcosa che sappiamo essere fattualmente errato basato su altre fonti di informazione.

Prendiamo ad esempio se costruissimo una funzione per la nostra startup che permetta agli studenti di fare domande storiche a un modello. Uno studente pone la domanda `Who was the sole survivor of Titanic?`

Il modello produce una risposta come quella qui sotto:

Questa è una risposta molto sicura e dettagliata. Purtroppo, è errata. Anche con una minima quantità di ricerca, si scoprirebbe che ci sono stati più di un sopravvissuto al disastro del Titanic. Per uno studente che sta appena iniziando a ricercare questo argomento, questa risposta può essere abbastanza persuasiva da non essere messa in discussione e trattata come un fatto. Le conseguenze di ciò possono portare il sistema AI a essere inaffidabile e influire negativamente sulla reputazione della nostra startup.

Con ogni iterazione di un dato LLM, abbiamo visto miglioramenti nelle prestazioni per ridurre al minimo le allucinazioni. Anche con questo miglioramento, noi come costruttori e utenti di applicazioni dobbiamo comunque rimanere consapevoli di queste limitazioni.

### Contenuto dannoso

Abbiamo coperto nella sezione precedente quando un LLM produce risposte errate o prive di senso. Un altro rischio di cui dobbiamo essere consapevoli è quando un modello risponde con contenuti dannosi.

Il contenuto dannoso può essere definito come:

- Fornire istruzioni o incoraggiare autolesionismo o danni a determinati gruppi.
- Contenuto odioso o denigratorio.
- Guidare la pianificazione di qualsiasi tipo di attacco o atti violenti.
- Fornire istruzioni su come trovare contenuti illegali o commettere atti illegali.
- Visualizzare contenuti sessualmente espliciti.

Per la nostra startup, vogliamo assicurarci di avere gli strumenti e le strategie giuste in atto per prevenire che questo tipo di contenuto venga visto dagli studenti.

### Mancanza di equità

L'equità è definita come "garantire che un sistema AI sia privo di pregiudizi e discriminazioni e che tratti tutti in modo equo e uguale". Nel mondo dell'AI generativa, vogliamo assicurarci che le visioni del mondo esclusive dei gruppi emarginati non siano rinforzate dall'output del modello.

Questi tipi di output non solo sono distruttivi per costruire esperienze di prodotto positive per i nostri utenti, ma causano anche ulteriori danni sociali. Come costruttori di applicazioni, dovremmo sempre tenere a mente una base utenti ampia e diversificata quando costruiamo soluzioni con l'AI generativa.

## Come usare l'AI generativa in modo responsabile

Ora che abbiamo identificato l'importanza dell'AI generativa responsabile, vediamo 4 passaggi che possiamo fare per costruire le nostre soluzioni AI in modo responsabile:

### Misurare i potenziali danni

Nel test del software, testiamo le azioni previste di un utente su un'applicazione. Allo stesso modo, testare un insieme diversificato di prompt che gli utenti probabilmente useranno è un buon modo per misurare il potenziale danno.

Poiché la nostra startup sta costruendo un prodotto educativo, sarebbe utile preparare un elenco di prompt relativi all'istruzione. Questo potrebbe coprire un determinato argomento, fatti storici e prompt sulla vita studentesca.

### Mitigare i potenziali danni

È ora il momento di trovare modi per prevenire o limitare il potenziale danno causato dal modello e dalle sue risposte. Possiamo guardare a questo in 4 diversi livelli:

- **Modello**. Scegliere il modello giusto per il caso d'uso giusto. Modelli più grandi e complessi come GPT-4 possono causare più rischi di contenuti dannosi quando applicati a casi d'uso più piccoli e specifici. Utilizzare i dati di addestramento per perfezionare il modello riduce anche il rischio di contenuti dannosi.

- **Sistema di sicurezza**. Un sistema di sicurezza è un insieme di strumenti e configurazioni sulla piattaforma che serve il modello che aiutano a mitigare il danno. Un esempio di questo è il sistema di filtraggio dei contenuti sul servizio Azure OpenAI. I sistemi dovrebbero anche rilevare attacchi di jailbreak e attività indesiderate come richieste da bot.

- **Metaprompt**. I metaprompt e il grounding sono modi in cui possiamo indirizzare o limitare il modello basato su determinati comportamenti e informazioni. Questo potrebbe essere l'uso di input di sistema per definire determinati limiti del modello. Inoltre, fornire output più rilevanti per l'ambito o il dominio del sistema.

Può anche essere l'uso di tecniche come la Generazione Aumentata dal Recupero (RAG) per far sì che il modello attinga informazioni solo da una selezione di fonti fidate. C'è una lezione più avanti in questo corso per [costruire applicazioni di ricerca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Esperienza utente**. L'ultimo livello è dove l'utente interagisce direttamente con il modello attraverso l'interfaccia della nostra applicazione in qualche modo. In questo modo possiamo progettare l'UI/UX per limitare l'utente sui tipi di input che possono inviare al modello così come il testo o le immagini visualizzate all'utente. Quando distribuiamo l'applicazione AI, dobbiamo anche essere trasparenti su cosa la nostra applicazione di AI generativa può e non può fare.

Abbiamo un'intera lezione dedicata a [Progettare UX per applicazioni AI](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Valutare il modello**. Lavorare con LLM può essere impegnativo perché non abbiamo sempre il controllo sui dati su cui è stato addestrato il modello. Indipendentemente da ciò, dovremmo sempre valutare le prestazioni e gli output del modello. È comunque importante misurare l'accuratezza del modello, la somiglianza, la fondatezza e la rilevanza dell'output. Questo aiuta a fornire trasparenza e fiducia a stakeholder e utenti.

### Operare una soluzione di AI generativa responsabile

Costruire una pratica operativa attorno alle tue applicazioni AI è la fase finale. Questo include la collaborazione con altre parti della nostra startup come Legal e Security per garantire che siamo conformi a tutte le politiche normative. Prima del lancio, vogliamo anche costruire piani attorno alla consegna, gestione degli incidenti e rollback per prevenire qualsiasi danno ai nostri utenti dalla crescita.

## Strumenti

Sebbene il lavoro di sviluppo di soluzioni AI responsabili possa sembrare molto, è un lavoro che vale la pena. Man mano che l'area dell'AI generativa cresce, più strumenti per aiutare gli sviluppatori a integrare responsabilità nei loro flussi di lavoro matureranno. Ad esempio, l'[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) può aiutare a rilevare contenuti e immagini dannosi tramite una richiesta API.

## Verifica delle conoscenze

Quali sono alcune cose di cui devi preoccuparti per garantire un uso responsabile dell'AI?

1. Che la risposta sia corretta.
2. Uso dannoso, che l'AI non sia utilizzata per scopi criminali.
3. Garantire che l'AI sia priva di pregiudizi e discriminazioni.

A: 2 e 3 sono corretti. L'AI responsabile ti aiuta a considerare come mitigare effetti dannosi e pregiudizi e altro ancora.

## 🚀 Sfida

Leggi su [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) e vedi cosa puoi adottare per il tuo utilizzo.

## Ottimo lavoro, continua il tuo apprendimento

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento AI generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'AI generativa!

Passa alla Lezione 4 dove esamineremo i [Fondamenti dell'Ingegneria dei Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Anche se ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.