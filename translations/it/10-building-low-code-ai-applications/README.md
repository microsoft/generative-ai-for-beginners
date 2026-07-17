# Costruire Applicazioni AI Low Code

[![Costruire Applicazioni AI Low Code](../../../translated_images/it/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

## Introduzione

Ora che abbiamo imparato a costruire applicazioni per la generazione di immagini, parliamo di low code. L'AI generativa può essere utilizzata in una varietà di aree diverse, incluso il low code, ma cos'è il low code e come possiamo aggiungere l'AI ad esso?

Costruire app e soluzioni è diventato più facile sia per sviluppatori tradizionali che per non sviluppatori grazie all'uso di Piattaforme di Sviluppo Low Code. Le Piattaforme di Sviluppo Low Code consentono di costruire app e soluzioni con poco o nessun codice. Questo è possibile fornendo un ambiente di sviluppo visivo che consente di trascinare e rilasciare componenti per costruire app e soluzioni. Questo ti permette di sviluppare app e soluzioni più velocemente e con meno risorse. In questa lezione, approfondiremo come usare il Low Code e come migliorare lo sviluppo low code con l'AI utilizzando Power Platform.

Power Platform offre alle organizzazioni l'opportunità di dare potere ai propri team di costruire le proprie soluzioni tramite un ambiente intuitivo low-code o no-code. Questo ambiente aiuta a semplificare il processo di costruzione delle soluzioni. Con Power Platform, le soluzioni possono essere costruite in giorni o settimane anziché mesi o anni. Power Platform è composto da cinque prodotti chiave: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio.

Questa lezione copre:

- Introduzione all'AI Generativa in Power Platform
- Introduzione a Copilot e come usarlo
- Uso dell'AI Generativa per costruire app e flussi in Power Platform
- Comprendere i Modelli AI in Power Platform con AI Builder
- Costruire agenti intelligenti con Microsoft Copilot Studio

## Obiettivi di Apprendimento

Alla fine di questa lezione, sarai in grado di:

- Comprendere come funziona Copilot in Power Platform.

- Costruire un'app per il Tracciamento delle Assegnazioni Studentesche per la nostra startup educativa.

- Costruire un flusso per l'elaborazione delle fatture che usa l'AI per estrarre informazioni dalle fatture.

- Applicare le migliori pratiche nell'uso del Modello AI Crea Testo con GPT.

- Comprendere cos'è Microsoft Copilot Studio e come costruire agenti intelligenti con esso.

Gli strumenti e le tecnologie che userai in questa lezione sono:

- **Power Apps**, per l'app Tracciatore delle Assegnazioni Studentesche, che offre un ambiente di sviluppo low-code per costruire app per tracciare, gestire e interagire con i dati.

- **Dataverse**, per memorizzare i dati dell'app Tracciatore delle Assegnazioni Studentesche, dove Dataverse fornirà una piattaforma dati low-code per conservare i dati dell'app.

- **Power Automate**, per il flusso di elaborazione delle fatture dove avrai un ambiente low-code per costruire flussi di lavoro per automatizzare il processo di elaborazione delle fatture.

- **AI Builder**, per il Modello AI dell'elaborazione delle fatture dove userai modelli AI predefiniti per elaborare le fatture per la nostra startup.

## AI Generativa in Power Platform

Rafforzare lo sviluppo e l'applicazione low-code con l'AI generativa è un'area chiave per Power Platform. L'obiettivo è permettere a chiunque di costruire app, siti, dashboard potenziati da AI e automatizzare processi con AI, _senza richiedere competenze in data science_. Questo obiettivo si realizza integrando l'AI generativa nell'esperienza di sviluppo low-code di Power Platform sotto forma di Copilot e AI Builder.

### Come funziona?

Copilot è un assistente AI che ti consente di costruire soluzioni Power Platform descrivendo le tue esigenze in una serie di passaggi conversazionali usando il linguaggio naturale. Puoi per esempio istruire il tuo assistente AI indicando quali campi la tua app dovrà usare e lui creerà sia l'app che il modello dati sottostante oppure potresti specificare come impostare un flusso in Power Automate.

Puoi usare le funzionalità guidate da Copilot come caratteristica nelle schermate delle tue app per permettere agli utenti di scoprire intuizioni attraverso interazioni conversazionali.

AI Builder è una capacità AI low-code disponibile in Power Platform che ti permette di usare Modelli AI per aiutarti ad automatizzare processi e prevedere risultati. Con AI Builder puoi portare l'AI nelle tue app e flussi che si connettono ai tuoi dati in Dataverse o in varie fonti dati cloud, come SharePoint, OneDrive o Azure.

Copilot è disponibile in tutti i prodotti di Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio (precedentemente Power Virtual Agents). AI Builder è disponibile in Power Apps e Power Automate. In questa lezione, ci concentreremo su come usare Copilot e AI Builder in Power Apps e Power Automate per creare una soluzione per la nostra startup educativa.

### Copilot in Power Apps

Parte della Power Platform, Power Apps offre un ambiente di sviluppo low-code per costruire app per tracciare, gestire e interagire con dati. È una suite di servizi per lo sviluppo di app con una piattaforma dati scalabile e la capacità di connettersi a servizi cloud e dati on-premise. Power Apps ti permette di costruire app che funzionano su browser, tablet e telefoni, e possono essere condivise con colleghi. Power Apps facilita gli utenti nello sviluppo di app con un'interfaccia semplice, così ogni utente business o sviluppatore pro può creare app personalizzate. L'esperienza di sviluppo è anche migliorata con AI Generativa tramite Copilot.

La funzione assistente AI copilot in Power Apps ti permette di descrivere che tipo di app ti serve e quali informazioni vuoi che la tua app tracci, raccolga o mostri. Copilot genera quindi un'app Canvas responsiva basata sulla tua descrizione. Puoi poi personalizzare l'app per soddisfare le tue esigenze. L'AI Copilot genera e suggerisce anche una Tabella Dataverse con i campi necessari per memorizzare i dati che vuoi tracciare e alcuni dati di esempio. In questa lezione vedremo cos'è Dataverse e come puoi usarlo in Power Apps più avanti. Puoi poi personalizzare la tabella per soddisfare le tue esigenze utilizzando la funzione assistente AI Copilot attraverso passaggi conversazionali. Questa funzione è facilmente accessibile dalla schermata principale di Power Apps.

### Copilot in Power Automate

Parte della Power Platform, Power Automate permette agli utenti di creare flussi di lavoro automatizzati tra applicazioni e servizi. Aiuta ad automatizzare processi aziendali ripetitivi come comunicazione, raccolta dati e approvazioni di decisioni. La sua interfaccia semplice permette agli utenti di ogni livello tecnico (da principianti a sviluppatori esperti) di automatizzare compiti lavorativi. L'esperienza di sviluppo dei flussi è anche migliorata con AI Generativa tramite Copilot.

La funzione assistente AI copilot in Power Automate ti permette di descrivere che tipo di flusso ti serve e quali azioni vuoi che il tuo flusso esegua. Copilot genera quindi un flusso basato sulla tua descrizione. Puoi poi personalizzare il flusso per soddisfare le tue esigenze. L'AI Copilot genera e suggerisce anche le azioni necessarie per eseguire il compito che vuoi automatizzare. In questa lezione vedremo cos'è un flusso e come puoi usarlo in Power Automate più avanti. Puoi poi personalizzare le azioni per soddisfare le tue esigenze utilizzando la funzione assistente AI Copilot attraverso passaggi conversazionali. Questa funzione è facilmente accessibile dalla schermata principale di Power Automate.

## Costruire Agenti Intelligenti con Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (precedentemente Power Virtual Agents) è il membro low-code di Power Platform per costruire **agenti AI** — copiloti conversazionali capaci di rispondere a domande, prendere azioni e automatizzare compiti per conto dei tuoi utenti. Come il resto di Power Platform, costruisci questi agenti in un'esperienza visiva e orientata al linguaggio naturale: descrivi cosa vuoi che l'agente faccia, e Copilot Studio aiuta a strutturare le sue istruzioni, conoscenza e azioni.

Per la nostra startup educativa, potresti costruire un agente che risponde alle domande degli studenti sui corsi, controlla le scadenze degli incarichi e invia email a un istruttore — tutto senza scrivere codice.

Ecco alcune delle ultime capacità che rendono Copilot Studio potente:

- **Risposte generative dalla tua conoscenza**. Invece di redigere ogni conversazione manualmente, puoi collegare **fonti di conoscenza** — siti web pubblici, SharePoint, OneDrive, Dataverse, file caricati o dati aziendali tramite connettori — e l'agente genera risposte fondate da esse.

- **Orchestrazione generativa**. Piuttosto che fare affidamento su frasi trigger rigide, l'agente usa l'AI per comprendere una richiesta e decidere dinamicamente quale conoscenza, argomenti e azioni combinare per soddisfarla, incluso concatenare più passaggi.

- **Azioni e connettori**. Gli agenti possono *fare* cose, non solo chattare. Puoi fornire ad un agente azioni supportate da oltre 1.500 connettori Power Platform predefiniti, flussi Power Automate, API REST personalizzate, prompt o server **Model Context Protocol (MCP)**.

- **Agenti autonomi**. Gli agenti non sono limitati a rispondere in una finestra di chat. Puoi costruire **agenti autonomi** che si attivano per eventi — come una nuova email, un nuovo record in Dataverse o un file caricato — e agiscono in background per completare un compito.

- **Orchestrazione multi-agente**. Gli agenti possono chiamare altri agenti. Un agente Copilot Studio può passare il controllo ad altri agenti o essere esteso da essi, inclusi agenti pubblicati su Microsoft 365 Copilot e agenti costruiti in Microsoft Foundry.

- **Scelta del modello**. Oltre ai modelli integrati, puoi portare modelli dal catalogo modelli Microsoft Foundry per personalizzare come il tuo agente ragiona e risponde.

- **Pubblica ovunque**. Una volta costruito, un agente può essere pubblicato su molteplici canali — Microsoft Teams, Microsoft 365 Copilot, un sito web o app personalizzata, e altro ancora — con sicurezza, autenticazione e analytics gestiti tramite l'amministrazione Power Platform.

Puoi iniziare a costruire il tuo primo agente su [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) e imparare di più nella [documentazione Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Compito: Gestire gli incarichi studenti e le fatture per la nostra startup, usando Copilot

La nostra startup fornisce corsi online agli studenti. La startup è cresciuta rapidamente e ora fatica a soddisfare la domanda dei suoi corsi. La startup ti ha assunto come sviluppatore Power Platform per aiutarli a costruire una soluzione low code per gestire gli incarichi studenti e le fatture. La loro soluzione dovrebbe aiutarli a tracciare e gestire gli incarichi studenti tramite un'app e automatizzare il processo di elaborazione delle fatture tramite un flusso di lavoro. Ti è stato chiesto di usare l'AI Generativa per sviluppare la soluzione.

Quando inizi a usare Copilot, puoi usare la [Libreria di Prompt Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) per iniziare con i prompt. Questa libreria contiene una lista di prompt che puoi usare per costruire app e flussi con Copilot. Puoi anche usare i prompt nella libreria per farti un'idea di come descrivere le tue esigenze a Copilot.

### Costruire un'app per il tracciamento degli incarichi studenti per la nostra startup

Gli educatori della nostra startup hanno avuto difficoltà a tenere traccia degli incarichi studenti. Hanno usato un foglio di calcolo per tracciare gli incarichi ma è diventato difficile da gestire con l'aumento degli studenti. Ti hanno chiesto di costruire un'app che li aiuti a tracciare e gestire gli incarichi studenti. L'app dovrebbe permettere di aggiungere nuovi incarichi, visualizzare incarichi, aggiornare incarichi ed eliminare incarichi. L'app dovrebbe anche permettere a educatori e studenti di vedere gli incarichi che sono stati valutati e quelli che non sono stati valutati.

Costruirai l'app usando Copilot in Power Apps seguendo i passaggi seguenti:

1. Naviga alla schermata principale di [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Usa l'area di testo nella schermata principale per descrivere l'app che vuoi costruire. Per esempio, **_Voglio costruire un'app per tracciare e gestire gli incarichi studenti_**. Clicca sul pulsante **Invia** per inviare il prompt al Copilot AI.

![Descrivi l'app che vuoi costruire](../../../translated_images/it/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. Il Copilot AI suggerirà una Tabella Dataverse con i campi necessari per memorizzare i dati che vuoi tracciare e alcuni dati di esempio. Puoi poi personalizzare la tabella per soddisfare le tue esigenze usando la funzione assistente AI Copilot attraverso passaggi conversazionali.

   > **Importante**: Dataverse è la piattaforma dati sottostante per Power Platform. È una piattaforma dati low-code per memorizzare i dati dell'app. È un servizio completamente gestito che conserva i dati in modo sicuro nel Cloud Microsoft ed è fornito all'interno del tuo ambiente Power Platform. Offre funzioni incorporata di governance dei dati, come classificazione dei dati, provenienza dei dati, controllo degli accessi granulare e altro. Puoi imparare di più su Dataverse [qui](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campi suggeriti nella tua nuova tabella](../../../translated_images/it/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Gli educatori vogliono inviare email agli studenti che hanno inviato i loro incarichi per tenerli aggiornati sul progresso degli incarichi. Puoi usare Copilot per aggiungere un nuovo campo alla tabella per memorizzare l'email dello studente. Per esempio, puoi usare il seguente prompt per aggiungere una nuova colonna alla tabella: **_Voglio aggiungere una colonna per memorizzare l'email dello studente_**. Clicca sul pulsante **Invia** per inviare il prompt al Copilot AI.

![Aggiunta di un nuovo campo](../../../translated_images/it/copilot-new-column.35e15ff21acaf274.webp)

1. Il Copilot AI genererà un nuovo campo e potrai poi personalizzarlo per soddisfare le tue esigenze.


1. Una volta terminata la tabella, fai clic sul pulsante **Crea app** per creare l'app.

1. L'AI Copilot genererà un'app Canvas reattiva basata sulla tua descrizione. Potrai poi personalizzare l'app per soddisfare le tue esigenze.

1. Per gli educatori che vogliono inviare email agli studenti, puoi usare Copilot per aggiungere una nuova schermata all'app. Per esempio, puoi usare il seguente prompt per aggiungere una nuova schermata all'app: **_Voglio aggiungere una schermata per inviare email agli studenti_**. Fai clic sul pulsante **Invia** per inviare il prompt all'AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/it/copilot-new-screen.2e0bef7132a17392.webp)

1. L'AI Copilot genererà una nuova schermata e potrai poi personalizzarla per soddisfare le tue esigenze.

1. Una volta terminata l'app, fai clic sul pulsante **Salva** per salvare l'app.

1. Per condividere l'app con gli educatori, fai clic sul pulsante **Condividi** e poi di nuovo sul pulsante **Condividi**. Potrai quindi condividere l'app con gli educatori inserendo i loro indirizzi email.

> **Il tuo compito**: L'app che hai appena creato è un buon inizio ma può essere migliorata. Con la funzione di email, gli educatori possono solo inviare manualmente email agli studenti digitando i loro indirizzi. Puoi usare Copilot per creare un'automazione che permetta agli educatori di inviare automaticamente email agli studenti quando inviano i loro compiti? Un suggerimento: con il prompt giusto puoi usare Copilot in Power Automate per realizzare questo.

### Crea una tabella delle informazioni delle fatture per la nostra startup

Il team finanziario della nostra startup ha avuto difficoltà a tenere traccia delle fatture. Usano un foglio di calcolo per tracciare le fatture, ma è diventato difficile da gestire con l’aumento del numero di fatture. Ti hanno chiesto di creare una tabella che li aiuti a memorizzare, tracciare e gestire le informazioni delle fatture ricevute. La tabella sarà usata per creare un’automazione che estrarrà tutte le informazioni delle fatture e le memorizzerà nella tabella. La tabella deve inoltre permettere al team finanziario di vedere le fatture pagate e quelle non pagate.

La Power Platform ha una piattaforma dati sottostante chiamata Dataverse che ti permette di memorizzare i dati per le tue app e soluzioni. Dataverse offre una piattaforma dati low-code per memorizzare i dati dell'app. È un servizio completamente gestito che memorizza i dati in modo sicuro nel cloud Microsoft ed è fornito all'interno del tuo ambiente Power Platform. Dispone di capacità integrate di governance dei dati, come classificazione dei dati, tracciamento delle origini, controllo degli accessi granulare e altro. Puoi saperne di più [su Dataverse qui](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Perché dovremmo usare Dataverse per la nostra startup? Le tabelle standard e personalizzate all’interno di Dataverse offrono un’opzione di archiviazione sicura e basata sul cloud per i tuoi dati. Le tabelle permettono di memorizzare diversi tipi di dati, simile a come potresti usare più fogli di lavoro in un singolo file Excel. Puoi usare le tabelle per archiviare dati specifici per la tua organizzazione o esigenze aziendali. Alcuni dei benefici che la nostra startup otterrà usando Dataverse includono, ma non sono limitati a:

- **Facile da gestire**: sia i metadati che i dati sono archiviati nel cloud, quindi non devi preoccuparti dei dettagli di come sono memorizzati o gestiti. Puoi concentrarti sulla creazione delle tue app e soluzioni.

- **Sicuro**: Dataverse offre un’opzione di archiviazione sicura e basata sul cloud per i tuoi dati. Puoi controllare chi ha accesso ai dati nelle tue tabelle e come vi accede usando la sicurezza basata sui ruoli.

- **Metadati ricchi**: I tipi di dati e le relazioni sono usati direttamente all’interno di Power Apps

- **Logica e validazione**: Puoi usare regole aziendali, campi calcolati e regole di validazione per imporre la logica aziendale e mantenere la precisione dei dati.

Ora che sai cos’è Dataverse e perché usarlo, vediamo come puoi usare Copilot per creare una tabella in Dataverse per soddisfare i requisiti del nostro team finanziario.

> **Nota** : Userai questa tabella nella prossima sezione per creare un’automazione che estrarrà tutte le informazioni delle fatture e le memorizzerà nella tabella.

Per creare una tabella in Dataverse usando Copilot, segui i passaggi sottostanti:

1. Vai alla schermata iniziale di [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Nella barra di navigazione a sinistra, seleziona **Tabelle** e poi clicca su **Descrivi la nuova tabella**.

![Select new table](../../../translated_images/it/describe-new-table.0792373eb757281e.webp)

1. Nella schermata **Descrivi la nuova tabella**, usa l’area di testo per descrivere la tabella che vuoi creare. Per esempio, **_Voglio creare una tabella per memorizzare informazioni sulle fatture_**. Fai clic sul pulsante **Invia** per inviare il prompt all'AI Copilot.

![Describe the table](../../../translated_images/it/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. L’AI Copilot suggerirà una tabella Dataverse con i campi necessari per memorizzare i dati che vuoi tracciare e alcuni esempi di dati. Potrai quindi personalizzare la tabella secondo le tue esigenze usando la funzionalità assistente AI Copilot attraverso passaggi conversazionali.

![Suggested Dataverse table](../../../translated_images/it/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Il team finanziario vuole inviare un’email al fornitore per aggiornarlo sullo stato attuale della fattura. Puoi usare Copilot per aggiungere un nuovo campo alla tabella per memorizzare l’email del fornitore. Per esempio, puoi usare il seguente prompt per aggiungere un nuovo campo alla tabella: **_Voglio aggiungere una colonna per memorizzare l’email del fornitore_**. Fai clic sul pulsante **Invia** per inviare il prompt all'AI Copilot.

1. L'AI Copilot genererà un nuovo campo e potrai personalizzarlo secondo le tue esigenze.

1. Una volta terminata la tabella, fai clic sul pulsante **Crea** per creare la tabella.

## Modelli AI nella Power Platform con AI Builder

AI Builder è una capacità AI low-code disponibile in Power Platform che ti consente di usare Modelli AI per aiutarti ad automatizzare processi e prevedere risultati. Con AI Builder puoi integrare AI nelle tue app e flussi che si connettono ai dati in Dataverse o in varie fonti dati cloud, come SharePoint, OneDrive o Azure.

## Modelli AI predefiniti vs Modelli AI personalizzati

AI Builder fornisce due tipi di Modelli AI: Modelli AI predefiniti e Modelli AI personalizzati. I Modelli AI predefiniti sono modelli AI pronti all’uso, addestrati da Microsoft e disponibili in Power Platform. Questi aiutano ad aggiungere intelligenza alle tue app e flussi senza dover raccogliere dati, creare, addestrare e pubblicare i tuoi modelli. Puoi usare questi modelli per automatizzare processi e prevedere risultati.

Alcuni dei Modelli AI predefiniti disponibili in Power Platform includono:

- **Estrazione di frasi chiave**: Questo modello estrae frasi chiave dal testo.
- **Rilevamento della lingua**: Questo modello rileva la lingua di un testo.
- **Analisi del sentiment**: Questo modello rileva sentiment positivi, negativi, neutrali o misti in un testo.
- **Lettore di biglietti da visita**: Questo modello estrae informazioni da biglietti da visita.
- **Riconoscimento del testo**: Questo modello estrae testo dalle immagini.
- **Rilevamento oggetti**: Questo modello rileva ed estrae oggetti da immagini.
- **Elaborazione documenti**: Questo modello estrae informazioni da moduli.
- **Elaborazione fatture**: Questo modello estrae informazioni da fatture.

Con i Modelli AI personalizzati puoi portare il tuo modello in AI Builder in modo che funzioni come qualsiasi modello personalizzato di AI Builder, permettendoti di addestrare il modello usando i tuoi dati. Puoi usare questi modelli per automatizzare processi e prevedere risultati sia in Power Apps che in Power Automate. Quando usi il tuo modello sono presenti limitazioni da considerare. Leggi di più su queste [limitazioni](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/it/ai-builder-models.8069423b84cfc47f.webp)

## Compito #2 - Crea un flusso di elaborazione fatture per la nostra startup

Il team finanziario ha avuto difficoltà a elaborare le fatture. Usano un foglio di calcolo per tracciare le fatture, ma è diventato difficile da gestire con l’aumento del numero di fatture. Ti hanno chiesto di creare un flusso di lavoro che li aiuti a elaborare le fatture usando l’AI. Il flusso di lavoro dovrebbe permettere di estrarre informazioni dalle fatture e memorizzarle in una tabella Dataverse. Il flusso dovrebbe anche permettere di inviare un’email al team finanziario con le informazioni estratte.

Ora che sai cos’è AI Builder e perché usarlo, vediamo come puoi usare il Modello AI di Elaborazione Fatture in AI Builder, che abbiamo trattato prima, per creare un flusso di lavoro che aiuti il team finanziario a elaborare le fatture.

Per creare un flusso di lavoro che aiuti il team finanziario a elaborare le fatture usando il Modello AI di Elaborazione Fatture in AI Builder, segui i passaggi sottostanti:

1. Vai alla schermata iniziale di [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Usa l’area di testo nella schermata iniziale per descrivere il flusso di lavoro che vuoi creare. Per esempio, **_Elaborare una fattura quando arriva nella mia casella di posta_**. Fai clic sul pulsante **Invia** per inviare il prompt all'AI Copilot.

   ![Copilot power automate](../../../translated_images/it/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. L’AI Copilot suggerirà le azioni necessarie per completare il compito che vuoi automatizzare. Puoi cliccare sul pulsante **Avanti** per procedere ai passaggi successivi.

4. Nel passaggio successivo, Power Automate ti chiederà di configurare le connessioni richieste per il flusso. Una volta terminato, fai clic sul pulsante **Crea flusso** per creare il flusso.

5. L’AI Copilot genererà un flusso che potrai personalizzare per soddisfare le tue esigenze.

6. Aggiorna il trigger del flusso e imposta la **Cartella** sulla cartella dove saranno conservate le fatture. Per esempio, puoi impostare la cartella su **Posta in arrivo** (Inbox). Fai clic su **Mostra opzioni avanzate** e imposta **Solo con allegati** su **Sì**. Questo garantirà che il flusso venga eseguito solo quando viene ricevuta un’email con allegato nella cartella.

7. Rimuovi le seguenti azioni dal flusso: **HTML a testo**, **Componi**, **Componi 2**, **Componi 3** e **Componi 4** perché non le utilizzerai.

8. Rimuovi l’azione **Condizione** dal flusso perché non la utilizzerai. Dovrebbe risultare come nella seguente schermata:

   ![power automate, remove actions](../../../translated_images/it/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Fai clic sul pulsante **Aggiungi un'azione** e cerca **Dataverse**. Seleziona l’azione **Aggiungi una nuova riga**.

10. Nell’azione **Estrai informazioni dalle fatture**, aggiorna il campo **File fattura** per puntare al contenuto dell’allegato (**Attachment Content**) dall’email. Questo garantirà che il flusso estragga informazioni dall’allegato della fattura.

11. Seleziona la **Tabella** che hai creato prima. Per esempio, puoi selezionare la tabella **Informazioni fattura**. Scegli i contenuti dinamici dall’azione precedente per popolare i seguenti campi:

    - ID
    - Importo
    - Data
    - Nome
    - Stato - Imposta lo **Stato** su **In sospeso**.
    - Email del fornitore - Usa il contenuto dinamico **Da** (From) dal trigger **Quando arriva una nuova email**.

    ![power automate add row](../../../translated_images/it/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Una volta terminato il flusso, fai clic sul pulsante **Salva** per salvare il flusso. Puoi poi testare il flusso inviando un’email con una fattura alla cartella che hai specificato nel trigger.

> **Il tuo compito**: Il flusso che hai appena creato è un buon inizio, ora devi pensare a come costruire un’automazione che permetta al nostro team finanziario di inviare un’email al fornitore per aggiornarlo sullo stato attuale della loro fattura. Suggerimento: il flusso deve essere eseguito quando cambia lo stato della fattura.

## Usa un Modello AI di generazione testo in Power Automate

Il Modello AI Crea Testo con GPT in AI Builder ti permette di generare testo basato su un prompt ed è alimentato dal servizio Microsoft Azure OpenAI. Con questa capacità puoi integrare la tecnologia GPT (Generative Pre-Trained Transformer) nelle tue app e flussi per creare una varietà di flussi automatizzati e applicazioni intelligenti.

I modelli GPT sono sottoposti a un esteso addestramento su grandi quantità di dati, permettendo loro di produrre testo che assomiglia molto al linguaggio umano quando viene fornito un prompt. Quando integrati con l’automazione dei flussi di lavoro, modelli AI come GPT possono essere usati per snellire e automatizzare un’ampia gamma di compiti.

Per esempio, puoi creare flussi per generare automaticamente testo per vari casi d’uso, come bozze di email, descrizioni di prodotti e altro. Puoi anche usare il modello per generare testo per varie app, come chatbot e app di assistenza clienti che permettono agli operatori di rispondere efficacemente e rapidamente alle richieste dei clienti.

![create a prompt](../../../translated_images/it/create-prompt-gpt.69d429300c2e870a.webp)


Per imparare come usare questo Modello AI in Power Automate, consulta il modulo [Aggiungi intelligenza con AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Ottimo lavoro! Continua il tuo apprendimento

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'AI generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'AI generativa!

Vuoi personalizzare e ottenere di più da Copilot? Esplora [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — una collezione contributa dalla comunità di istruzioni, agenti, competenze e configurazioni per aiutarti a sfruttare al meglio GitHub Copilot.

Passa alla Lezione 11 dove vedremo come [integrare l'AI generativa con Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->