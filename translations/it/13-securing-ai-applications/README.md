<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-05-19T22:41:01+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "it"
}
-->
# Proteggere le tue applicazioni di AI generativa

## Introduzione

Questa lezione coprirà:

- La sicurezza nel contesto dei sistemi di AI.
- Rischi e minacce comuni ai sistemi di AI.
- Metodi e considerazioni per proteggere i sistemi di AI.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, avrai una comprensione di:

- Le minacce e i rischi per i sistemi di AI.
- Metodi e pratiche comuni per proteggere i sistemi di AI.
- Come l'implementazione di test di sicurezza può prevenire risultati inaspettati e l'erosione della fiducia degli utenti.

## Cosa significa sicurezza nel contesto dell'AI generativa?

Man mano che le tecnologie di Intelligenza Artificiale (AI) e Machine Learning (ML) modellano sempre più le nostre vite, è fondamentale proteggere non solo i dati dei clienti ma anche i sistemi di AI stessi. L'AI/ML è sempre più utilizzata a supporto di processi decisionali di alto valore in settori dove una decisione errata può portare a conseguenze gravi.

Ecco i punti chiave da considerare:

- **Impatto dell'AI/ML**: L'AI/ML ha impatti significativi sulla vita quotidiana e, come tale, salvaguardarli è diventato essenziale.
- **Sfide di sicurezza**: Questo impatto che l'AI/ML ha necessita di un'adeguata attenzione per affrontare la necessità di proteggere i prodotti basati su AI da attacchi sofisticati, siano essi da parte di troll o gruppi organizzati.
- **Problemi strategici**: L'industria tecnologica deve affrontare in modo proattivo le sfide strategiche per garantire la sicurezza a lungo termine dei clienti e la sicurezza dei dati.

Inoltre, i modelli di Machine Learning sono in gran parte incapaci di distinguere tra input malevoli e dati anomali benigni. Una fonte significativa di dati di addestramento deriva da dataset pubblici non curati e non moderati, aperti ai contributi di terzi. Gli attaccanti non hanno bisogno di compromettere i dataset quando sono liberi di contribuire ad essi. Col tempo, i dati malevoli a bassa fiducia diventano dati fidati ad alta fiducia, se la struttura/formattazione dei dati rimane corretta.

Per questo è fondamentale garantire l'integrità e la protezione dei depositi di dati che i tuoi modelli utilizzano per prendere decisioni.

## Comprendere le minacce e i rischi dell'AI

In termini di AI e sistemi correlati, l'avvelenamento dei dati si distingue come la minaccia di sicurezza più significativa oggi. L'avvelenamento dei dati avviene quando qualcuno modifica intenzionalmente le informazioni utilizzate per addestrare un'AI, facendola commettere errori. Questo è dovuto all'assenza di metodi standardizzati di rilevamento e mitigazione, unito alla nostra dipendenza da dataset pubblici non affidabili o non curati per l'addestramento. Per mantenere l'integrità dei dati e prevenire un processo di addestramento difettoso, è fondamentale tracciare l'origine e la provenienza dei tuoi dati. Altrimenti, il vecchio adagio "immondizia dentro, immondizia fuori" risulta vero, portando a prestazioni del modello compromesse.

Ecco esempi di come l'avvelenamento dei dati può influenzare i tuoi modelli:

1. **Inversione delle etichette**: In un compito di classificazione binaria, un avversario inverte intenzionalmente le etichette di un piccolo sottoinsieme di dati di addestramento. Ad esempio, campioni benigni sono etichettati come malevoli, portando il modello ad apprendere associazioni errate.\
   **Esempio**: Un filtro antispam che classifica erroneamente email legittime come spam a causa di etichette manipolate.
2. **Avvelenamento delle caratteristiche**: Un attaccante modifica sottilmente le caratteristiche nei dati di addestramento per introdurre bias o fuorviare il modello.\
   **Esempio**: Aggiungere parole chiave irrilevanti alle descrizioni dei prodotti per manipolare i sistemi di raccomandazione.
3. **Iniezione di dati**: Iniettare dati malevoli nel set di addestramento per influenzare il comportamento del modello.\
   **Esempio**: Introdurre recensioni false degli utenti per alterare i risultati dell'analisi del sentiment.
4. **Attacchi con backdoor**: Un avversario inserisce un pattern nascosto (backdoor) nei dati di addestramento. Il modello impara a riconoscere questo pattern e si comporta malevolmente quando viene attivato.\
   **Esempio**: Un sistema di riconoscimento facciale addestrato con immagini con backdoor che identifica erroneamente una persona specifica.

La MITRE Corporation ha creato [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), una base di conoscenza di tattiche e tecniche impiegate dagli avversari in attacchi reali ai sistemi di AI.

> Ci sono un numero crescente di vulnerabilità nei sistemi abilitati all'AI, poiché l'incorporazione dell'AI aumenta la superficie d'attacco dei sistemi esistenti oltre quelli degli attacchi informatici tradizionali. Abbiamo sviluppato ATLAS per sensibilizzare su queste vulnerabilità uniche e in evoluzione, poiché la comunità globale incorpora sempre più l'AI in vari sistemi. ATLAS è modellato sul framework MITRE ATT&CK® e le sue tattiche, tecniche e procedure (TTP) sono complementari a quelle in ATT&CK.

Molto simile al framework MITRE ATT&CK®, ampiamente utilizzato nella cybersecurity tradizionale per pianificare scenari avanzati di emulazione delle minacce, ATLAS fornisce un set di TTP facilmente ricercabile che può aiutare a comprendere meglio e prepararsi a difendersi dagli attacchi emergenti.

Inoltre, l'Open Web Application Security Project (OWASP) ha creato una "[lista dei Top 10](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" delle vulnerabilità più critiche trovate nelle applicazioni che utilizzano LLM. La lista evidenzia i rischi di minacce come il già citato avvelenamento dei dati insieme ad altre come:

- **Iniezione di prompt**: una tecnica in cui gli attaccanti manipolano un Large Language Model (LLM) attraverso input accuratamente elaborati, facendolo comportare al di fuori del suo comportamento previsto.
- **Vulnerabilità della catena di fornitura**: I componenti e il software che compongono le applicazioni utilizzate da un LLM, come moduli Python o dataset esterni, possono essere compromessi portando a risultati inaspettati, bias introdotti e persino vulnerabilità nell'infrastruttura sottostante.
- **Eccessiva fiducia**: Gli LLM sono fallibili e sono stati inclini a "allucinare", fornendo risultati inaccurati o non sicuri. In diverse circostanze documentate, le persone hanno preso i risultati per buoni portando a conseguenze negative non intenzionali nel mondo reale.

Il Cloud Advocate di Microsoft Rod Trent ha scritto un ebook gratuito, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), che approfondisce queste e altre minacce emergenti dell'AI e fornisce una guida estesa su come affrontare al meglio questi scenari.

## Test di sicurezza per sistemi di AI e LLM

L'intelligenza artificiale (AI) sta trasformando vari domini e industrie, offrendo nuove possibilità e benefici per la società. Tuttavia, l'AI presenta anche sfide e rischi significativi, come la privacy dei dati, il bias, la mancanza di spiegabilità e il potenziale abuso. Pertanto, è cruciale garantire che i sistemi di AI siano sicuri e responsabili, nel senso che aderiscano a standard etici e legali e possano essere affidati da utenti e stakeholder.

Il test di sicurezza è il processo di valutazione della sicurezza di un sistema di AI o LLM, identificando e sfruttando le loro vulnerabilità. Questo può essere eseguito da sviluppatori, utenti o revisori di terze parti, a seconda dello scopo e dell'ambito del test. Alcuni dei metodi di test di sicurezza più comuni per i sistemi di AI e LLM sono:

- **Sanitizzazione dei dati**: Questo è il processo di rimozione o anonimizzazione delle informazioni sensibili o private dai dati di addestramento o dall'input di un sistema di AI o LLM. La sanitizzazione dei dati può aiutare a prevenire la perdita di dati e la manipolazione malevola riducendo l'esposizione di dati riservati o personali.
- **Test adversariali**: Questo è il processo di generazione e applicazione di esempi adversariali all'input o all'output di un sistema di AI o LLM per valutarne la robustezza e la resilienza contro attacchi adversariali. I test adversariali possono aiutare a identificare e mitigare le vulnerabilità e le debolezze di un sistema di AI o LLM che potrebbero essere sfruttate dagli attaccanti.
- **Verifica del modello**: Questo è il processo di verifica della correttezza e completezza dei parametri del modello o dell'architettura di un sistema di AI o LLM. La verifica del modello può aiutare a rilevare e prevenire il furto del modello garantendo che il modello sia protetto e autenticato.
- **Validazione dell'output**: Questo è il processo di validazione della qualità e affidabilità dell'output di un sistema di AI o LLM. La validazione dell'output può aiutare a rilevare e correggere la manipolazione malevola garantendo che l'output sia coerente e accurato.

OpenAI, leader nei sistemi di AI, ha istituito una serie di _valutazioni di sicurezza_ come parte della loro iniziativa di rete di red teaming, mirata a testare i sistemi di output di AI nella speranza di contribuire alla sicurezza dell'AI.

> Le valutazioni possono variare da semplici test di Q&A a simulazioni più complesse. Come esempi concreti, ecco alcune valutazioni sviluppate da OpenAI per valutare i comportamenti dell'AI da diverse angolazioni:

#### Persuasione

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): Quanto bene un sistema di AI può ingannare un altro sistema di AI facendogli dire una parola segreta?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): Quanto bene un sistema di AI può convincere un altro sistema di AI a donare denaro?
- [Proposta di voto](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): Quanto bene un sistema di AI può influenzare il supporto di un altro sistema di AI a una proposta politica?

#### Steganografia (messaggistica nascosta)

- [Steganografia](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): Quanto bene un sistema di AI può passare messaggi segreti senza essere scoperto da un altro sistema di AI?
- [Compressione del testo](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): Quanto bene un sistema di AI può comprimere e decomprimere messaggi, per consentire di nascondere messaggi segreti?
- [Punto di Schelling](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): Quanto bene un sistema di AI può coordinarsi con un altro sistema di AI, senza comunicazione diretta?

### Sicurezza dell'AI

È imperativo che ci impegniamo a proteggere i sistemi di AI da attacchi malevoli, uso improprio o conseguenze indesiderate. Questo include adottare misure per garantire la sicurezza, l'affidabilità e la fiducia nei sistemi di AI, come:

- Proteggere i dati e gli algoritmi utilizzati per addestrare e far funzionare i modelli di AI
- Prevenire l'accesso non autorizzato, la manipolazione o il sabotaggio dei sistemi di AI
- Rilevare e mitigare bias, discriminazioni o problemi etici nei sistemi di AI
- Garantire la responsabilità, la trasparenza e la spiegabilità delle decisioni e azioni dell'AI
- Allineare gli obiettivi e i valori dei sistemi di AI con quelli degli esseri umani e della società

La sicurezza dell'AI è importante per garantire l'integrità, la disponibilità e la riservatezza dei sistemi di AI e dei dati. Alcune delle sfide e opportunità della sicurezza dell'AI sono:

- Opportunità: Incorporare l'AI nelle strategie di cybersecurity poiché può svolgere un ruolo cruciale nell'identificare le minacce e migliorare i tempi di risposta. L'AI può aiutare ad automatizzare e aumentare il rilevamento e la mitigazione degli attacchi informatici, come phishing, malware o ransomware.
- Sfida: L'AI può anche essere utilizzata dagli avversari per lanciare attacchi sofisticati, come generare contenuti falsi o fuorvianti, impersonare utenti o sfruttare vulnerabilità nei sistemi di AI. Pertanto, gli sviluppatori di AI hanno una responsabilità unica nel progettare sistemi che siano robusti e resilienti contro l'uso improprio.

### Protezione dei dati

Gli LLM possono rappresentare rischi per la privacy e la sicurezza dei dati che utilizzano. Ad esempio, gli LLM possono potenzialmente memorizzare e divulgare informazioni sensibili dai loro dati di addestramento, come nomi personali, indirizzi, password o numeri di carte di credito. Possono anche essere manipolati o attaccati da attori malevoli che vogliono sfruttare le loro vulnerabilità o bias. Pertanto, è importante essere consapevoli di questi rischi e adottare misure appropriate per proteggere i dati utilizzati con gli LLM. Ci sono diversi passaggi che puoi intraprendere per proteggere i dati utilizzati con gli LLM. Questi passaggi includono:

- **Limitare la quantità e il tipo di dati che condividono con gli LLM**: Condividi solo i dati che sono necessari e pertinenti per gli scopi previsti, e evita di condividere qualsiasi dato che sia sensibile, riservato o personale. Gli utenti dovrebbero anche anonimizzare o crittografare i dati che condividono con gli LLM, ad esempio rimuovendo o mascherando qualsiasi informazione identificativa, o utilizzando canali di comunicazione sicuri.
- **Verificare i dati che gli LLM generano**: Controlla sempre l'accuratezza e la qualità dell'output generato dagli LLM per assicurarti che non contengano informazioni indesiderate o inappropriate.
- **Segnalare e allertare eventuali violazioni dei dati o incidenti**: Sii vigile su qualsiasi attività o comportamento sospetto o anomalo degli LLM, come generare testi che sono irrilevanti, inaccurati, offensivi o dannosi. Questo potrebbe essere un'indicazione di una violazione dei dati o di un incidente di sicurezza.

La sicurezza dei dati, la governance e la conformità sono fondamentali per qualsiasi organizzazione che voglia sfruttare il potere dei dati e dell'AI in un ambiente multi-cloud. Proteggere e governare tutti i tuoi dati è un'impresa complessa e sfaccettata. Devi proteggere e governare diversi tipi di dati (strutturati, non strutturati e dati generati dall'AI) in diverse posizioni attraverso più cloud, e devi tenere conto delle normative esistenti e future sulla sicurezza dei dati, la governance e l'AI. Per proteggere i tuoi dati, devi adottare alcune migliori pratiche e precauzioni, come:

- Utilizzare servizi o piattaforme cloud che offrono funzionalità di protezione e privacy dei dati.
- Utilizzare strumenti di qualità e validazione dei dati per controllare i tuoi dati per errori, incoerenze o anomalie.
- Utilizzare framework di governance ed etica dei dati per garantire che i tuoi dati siano utilizzati in modo responsabile e trasparente.

### Emulazione delle minacce reali - AI red teaming

L'emulazione delle minacce reali è ora considerata una pratica standard nella costruzione di sistemi di AI resilienti, impiegando strumenti, tattiche, procedure simili per identificare i rischi per i sistemi e testare la risposta dei difensori.

> La pratica del red teaming dell'AI si è evoluta per assumere un significato più ampio: non copre solo la ricerca di vulnerabilità di sicurezza, ma include anche la ricerca di altri fallimenti del sistema, come la generazione di contenuti potenzialmente dannosi. I sistemi di AI presentano nuovi rischi, e il red teaming è fondamentale per comprendere quei rischi nuovi, come l'iniezione di prompt e la produzione di contenuti non fondati. - [Microsoft AI Red Team costruisce il futuro di un'AI più sicura](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

Di seguito sono riportati gli approfondimenti chiave che hanno modellato il programma di AI Red Team di Microsoft.

1. **Ambito espansivo del red teaming dell'AI:**
   Il red teaming dell'AI ora comprende sia gli aspetti di sicurezza che quelli di AI Responsabile (RAI). Tradizionalmente, il red teaming si concentrava

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Anche se ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.