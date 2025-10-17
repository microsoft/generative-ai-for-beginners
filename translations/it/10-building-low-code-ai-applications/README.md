<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "846ac8e3b7dcfb697d3309fec05f0fea",
  "translation_date": "2025-10-17T16:09:24+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "it"
}
-->
# Creare Applicazioni AI a Basso Codice

[![Creare Applicazioni AI a Basso Codice](../../../translated_images/10-lesson-banner.a01ac8fe3fd86310c2e4065c0b3c584879f33b8ce797311821a636992f8a5b2f.it.png)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

## Introduzione

Ora che abbiamo imparato a creare applicazioni per generare immagini, parliamo di basso codice. L'AI generativa può essere utilizzata in diversi ambiti, incluso il basso codice, ma cos'è il basso codice e come possiamo aggiungere l'AI ad esso?

Creare app e soluzioni è diventato più semplice per sviluppatori tradizionali e non, grazie all'uso delle piattaforme di sviluppo a basso codice. Queste piattaforme permettono di creare app e soluzioni con poco o nessun codice, fornendo un ambiente di sviluppo visivo che consente di trascinare e rilasciare componenti per costruire app e soluzioni. Questo permette di sviluppare app e soluzioni più velocemente e con meno risorse. In questa lezione, approfondiremo l'uso del basso codice e come migliorare lo sviluppo a basso codice con l'AI utilizzando Power Platform.

Power Platform offre alle organizzazioni l'opportunità di dare ai propri team la possibilità di creare soluzioni personalizzate attraverso un ambiente intuitivo a basso codice o senza codice. Questo ambiente semplifica il processo di creazione delle soluzioni. Con Power Platform, le soluzioni possono essere sviluppate in giorni o settimane invece che in mesi o anni. Power Platform è composto da cinque prodotti principali: Power Apps, Power Automate, Power BI, Power Pages e Copilot Studio.

Questa lezione copre:

- Introduzione all'AI generativa in Power Platform
- Introduzione a Copilot e come utilizzarlo
- Utilizzo dell'AI generativa per creare app e flussi in Power Platform
- Comprensione dei modelli AI in Power Platform con AI Builder

## Obiettivi di Apprendimento

Alla fine di questa lezione, sarai in grado di:

- Comprendere come funziona Copilot in Power Platform.

- Creare un'app per il monitoraggio degli incarichi degli studenti per la nostra startup educativa.

- Creare un flusso di elaborazione delle fatture che utilizza l'AI per estrarre informazioni dalle fatture.

- Applicare le migliori pratiche nell'uso del modello AI "Create Text with GPT".

Gli strumenti e le tecnologie che utilizzerai in questa lezione sono:

- **Power Apps**, per l'app di monitoraggio degli incarichi degli studenti, che fornisce un ambiente di sviluppo a basso codice per creare app per monitorare, gestire e interagire con i dati.

- **Dataverse**, per archiviare i dati dell'app di monitoraggio degli incarichi degli studenti, dove Dataverse fornirà una piattaforma dati a basso codice per archiviare i dati dell'app.

- **Power Automate**, per il flusso di elaborazione delle fatture, dove avrai un ambiente di sviluppo a basso codice per creare flussi di lavoro per automatizzare il processo di elaborazione delle fatture.

- **AI Builder**, per il modello AI di elaborazione delle fatture, dove utilizzerai modelli AI predefiniti per elaborare le fatture della nostra startup.

## AI Generativa in Power Platform

Migliorare lo sviluppo e le applicazioni a basso codice con l'AI generativa è un'area chiave di interesse per Power Platform. L'obiettivo è permettere a tutti di creare app, siti, dashboard e automatizzare processi con l'AI, _senza richiedere competenze in data science_. Questo obiettivo viene raggiunto integrando l'AI generativa nell'esperienza di sviluppo a basso codice in Power Platform sotto forma di Copilot e AI Builder.

### Come funziona?

Copilot è un assistente AI che ti permette di creare soluzioni Power Platform descrivendo i tuoi requisiti in una serie di passaggi conversazionali utilizzando il linguaggio naturale. Ad esempio, puoi istruire il tuo assistente AI indicando quali campi la tua app utilizzerà e lui creerà sia l'app che il modello di dati sottostante, oppure puoi specificare come configurare un flusso in Power Automate.

Puoi utilizzare le funzionalità guidate da Copilot come una caratteristica nei tuoi schermi delle app per permettere agli utenti di scoprire informazioni attraverso interazioni conversazionali.

AI Builder è una capacità AI a basso codice disponibile in Power Platform che ti consente di utilizzare modelli AI per aiutarti ad automatizzare processi e prevedere risultati. Con AI Builder puoi portare l'AI nelle tue app e flussi che si connettono ai tuoi dati in Dataverse o in varie fonti di dati cloud, come SharePoint, OneDrive o Azure.

Copilot è disponibile in tutti i prodotti Power Platform: Power Apps, Power Automate, Power BI, Power Pages e Power Virtual Agents. AI Builder è disponibile in Power Apps e Power Automate. In questa lezione, ci concentreremo su come utilizzare Copilot e AI Builder in Power Apps e Power Automate per creare una soluzione per la nostra startup educativa.

### Copilot in Power Apps

Come parte di Power Platform, Power Apps fornisce un ambiente di sviluppo a basso codice per creare app per monitorare, gestire e interagire con i dati. È una suite di servizi di sviluppo app con una piattaforma dati scalabile e la capacità di connettersi a servizi cloud e dati on-premises. Power Apps ti permette di creare app che funzionano su browser, tablet e telefoni e possono essere condivise con i colleghi. Power Apps semplifica lo sviluppo di app con un'interfaccia semplice, in modo che ogni utente aziendale o sviluppatore professionista possa creare app personalizzate. L'esperienza di sviluppo delle app è anche migliorata con l'AI generativa attraverso Copilot.

La funzione di assistente AI Copilot in Power Apps ti permette di descrivere il tipo di app di cui hai bisogno e quali informazioni vuoi che la tua app monitori, raccolga o mostri. Copilot genera quindi un'app Canvas reattiva basata sulla tua descrizione. Puoi poi personalizzare l'app per soddisfare le tue esigenze. L'AI Copilot genera e suggerisce anche una tabella Dataverse con i campi necessari per archiviare i dati che vuoi monitorare e alcuni dati di esempio. Vedremo cos'è Dataverse e come puoi usarlo in Power Apps più avanti in questa lezione. Puoi poi personalizzare la tabella per soddisfare le tue esigenze utilizzando la funzione di assistente AI Copilot attraverso passaggi conversazionali. Questa funzione è facilmente accessibile dalla schermata iniziale di Power Apps.

### Copilot in Power Automate

Come parte di Power Platform, Power Automate consente agli utenti di creare flussi di lavoro automatizzati tra applicazioni e servizi. Aiuta ad automatizzare i processi aziendali ripetitivi come la comunicazione, la raccolta dati e le approvazioni delle decisioni. La sua interfaccia semplice permette agli utenti di ogni livello tecnico (dai principianti agli sviluppatori esperti) di automatizzare le attività lavorative. L'esperienza di sviluppo dei flussi di lavoro è anche migliorata con l'AI generativa attraverso Copilot.

La funzione di assistente AI Copilot in Power Automate ti permette di descrivere il tipo di flusso di cui hai bisogno e quali azioni vuoi che il tuo flusso esegua. Copilot genera quindi un flusso basato sulla tua descrizione. Puoi poi personalizzare il flusso per soddisfare le tue esigenze. L'AI Copilot genera e suggerisce anche le azioni necessarie per eseguire il compito che vuoi automatizzare. Vedremo cosa sono i flussi e come puoi usarli in Power Automate più avanti in questa lezione. Puoi poi personalizzare le azioni per soddisfare le tue esigenze utilizzando la funzione di assistente AI Copilot attraverso passaggi conversazionali. Questa funzione è facilmente accessibile dalla schermata iniziale di Power Automate.

## Compito: Gestire gli incarichi degli studenti e le fatture per la nostra startup, utilizzando Copilot

La nostra startup offre corsi online agli studenti. La startup è cresciuta rapidamente e ora fatica a tenere il passo con la domanda dei suoi corsi. La startup ti ha assunto come sviluppatore Power Platform per aiutarli a creare una soluzione a basso codice per gestire gli incarichi degli studenti e le fatture. La soluzione dovrebbe essere in grado di aiutare a monitorare e gestire gli incarichi degli studenti attraverso un'app e automatizzare il processo di elaborazione delle fatture attraverso un flusso di lavoro. Ti è stato chiesto di utilizzare l'AI generativa per sviluppare la soluzione.

Quando inizi a utilizzare Copilot, puoi utilizzare la [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) per iniziare con i prompt. Questa libreria contiene un elenco di prompt che puoi utilizzare per creare app e flussi con Copilot. Puoi anche utilizzare i prompt nella libreria per avere un'idea di come descrivere i tuoi requisiti a Copilot.

### Creare un'app per il monitoraggio degli incarichi degli studenti per la nostra startup

Gli educatori della nostra startup hanno difficoltà a tenere traccia degli incarichi degli studenti. Hanno utilizzato un foglio di calcolo per monitorare gli incarichi, ma questo è diventato difficile da gestire con l'aumento del numero di studenti. Ti hanno chiesto di creare un'app che li aiuti a monitorare e gestire gli incarichi degli studenti. L'app dovrebbe permettere loro di aggiungere nuovi incarichi, visualizzare gli incarichi, aggiornare gli incarichi e eliminare gli incarichi. L'app dovrebbe anche permettere agli educatori e agli studenti di visualizzare gli incarichi che sono stati valutati e quelli che non lo sono stati.

Creerai l'app utilizzando Copilot in Power Apps seguendo i passaggi seguenti:

1. Vai alla schermata iniziale di [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Usa l'area di testo nella schermata iniziale per descrivere l'app che vuoi creare. Ad esempio, **_Voglio creare un'app per monitorare e gestire gli incarichi degli studenti_**. Clicca sul pulsante **Invia** per inviare il prompt a Copilot AI.

![Descrivi l'app che vuoi creare](../../../translated_images/copilot-chat-prompt-powerapps.84250f341d060830a296b68512e6b3b3aa3a4559f4f1c2d7bafeba8ad3fcd17a.it.png)

1. Copilot AI suggerirà una tabella Dataverse con i campi necessari per archiviare i dati che vuoi monitorare e alcuni dati di esempio. Puoi poi personalizzare la tabella per soddisfare le tue esigenze utilizzando la funzione di assistente AI Copilot attraverso passaggi conversazionali.

   > **Importante**: Dataverse è la piattaforma dati sottostante per Power Platform. È una piattaforma dati a basso codice per archiviare i dati dell'app. È un servizio completamente gestito che archivia i dati in modo sicuro nel cloud Microsoft ed è fornito all'interno del tuo ambiente Power Platform. Include funzionalità di governance dei dati integrate, come classificazione dei dati, tracciabilità dei dati, controllo di accesso granulare e altro. Puoi saperne di più su Dataverse [qui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campi suggeriti nella tua nuova tabella](../../../translated_images/copilot-dataverse-table-powerapps.f4cc07b5d5f9327bd3783dd288debb2a959ce3320107512e235137aebd8a1a4c.it.png)

1. Gli educatori vogliono inviare email agli studenti che hanno inviato i loro incarichi per tenerli aggiornati sullo stato dei loro incarichi. Puoi utilizzare Copilot per aggiungere un nuovo campo alla tabella per archiviare l'email dello studente. Ad esempio, puoi utilizzare il seguente prompt per aggiungere un nuovo campo alla tabella: **_Voglio aggiungere una colonna per archiviare l'email dello studente_**. Clicca sul pulsante **Invia** per inviare il prompt a Copilot AI.

![Aggiungere un nuovo campo](../../../translated_images/copilot-new-column.35e15ff21acaf2745965d427b130f2be772f0484835b44fe074d496b1a455f2a.it.png)

1. Copilot AI genererà un nuovo campo e potrai poi personalizzare il campo per soddisfare le tue esigenze.

1. Una volta completata la tabella, clicca sul pulsante **Crea app** per creare l'app.

1. Copilot AI genererà un'app Canvas reattiva basata sulla tua descrizione. Puoi poi personalizzare l'app per soddisfare le tue esigenze.

1. Per permettere agli educatori di inviare email agli studenti, puoi utilizzare Copilot per aggiungere una nuova schermata all'app. Ad esempio, puoi utilizzare il seguente prompt per aggiungere una nuova schermata all'app: **_Voglio aggiungere una schermata per inviare email agli studenti_**. Clicca sul pulsante **Invia** per inviare il prompt a Copilot AI.

![Aggiungere una nuova schermata tramite un'istruzione prompt](../../../translated_images/copilot-new-screen.2e0bef7132a173928bc621780b39799e03982d315cb5a9ff75a34b08054641d4.it.png)

1. Copilot AI genererà una nuova schermata e potrai poi personalizzare la schermata per soddisfare le tue esigenze.

1. Una volta completata l'app, clicca sul pulsante **Salva** per salvare l'app.

1. Per condividere l'app con gli educatori, clicca sul pulsante **Condividi** e poi clicca di nuovo sul pulsante **Condividi**. Puoi poi condividere l'app con gli educatori inserendo i loro indirizzi email.

> **Il tuo compito**: L'app che hai appena creato è un buon inizio ma può essere migliorata. Con la funzione email, gli educatori possono inviare email agli studenti solo manualmente, dovendo digitare le loro email. Puoi utilizzare Copilot per creare un'automazione che permetta agli educatori di inviare email agli studenti automaticamente quando inviano i loro incarichi? Il tuo suggerimento è che con il giusto prompt puoi utilizzare Copilot in Power Automate per creare questo.

### Creare una Tabella di Informazioni sulle Fatture per la nostra Startup

Il team finanziario della nostra startup ha difficoltà a tenere traccia delle fatture. Hanno utilizzato un foglio di calcolo per monitorare le fatture, ma questo è diventato difficile da gestire con l'aumento del numero di fatture. Ti hanno chiesto di creare una tabella che li aiuti ad archiviare, monitorare e gestire le informazioni delle fatture ricevute. La tabella dovrebbe essere utilizzata per creare un'automazione che estragga tutte le informazioni delle fatture e le archivi nella tabella. La tabella dovrebbe anche permettere al team finanziario di visualizzare le fatture che sono state pagate e quelle che non sono state pagate.

Power Platform ha una piattaforma dati sottostante chiamata Dataverse che ti permette di archiviare i dati per le tue app e soluzioni. Dataverse fornisce una piattaforma dati a basso codice per archiviare i dati dell'app. È un servizio completamente gestito che archivia i dati in modo sicuro nel cloud Microsoft ed è fornito all'interno del tuo ambiente Power Platform. Include funzionalità di governance dei dati integrate, come classificazione dei dati, tracciabilità dei dati, controllo di accesso granulare e altro. Puoi saperne di più [su Dataverse qui](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).
Perché dovremmo utilizzare Dataverse per la nostra startup? Le tabelle standard e personalizzate all'interno di Dataverse offrono un'opzione di archiviazione sicura e basata su cloud per i tuoi dati. Le tabelle ti permettono di archiviare diversi tipi di dati, in modo simile a come potresti utilizzare più fogli di lavoro in un singolo file Excel. Puoi utilizzare le tabelle per archiviare dati specifici per le esigenze della tua organizzazione o azienda. Alcuni dei vantaggi che la nostra startup otterrà utilizzando Dataverse includono, ma non si limitano a:

- **Facile da gestire**: Sia i metadati che i dati sono archiviati nel cloud, quindi non devi preoccuparti dei dettagli su come vengono archiviati o gestiti. Puoi concentrarti sulla creazione delle tue app e soluzioni.

- **Sicuro**: Dataverse offre un'opzione di archiviazione sicura e basata su cloud per i tuoi dati. Puoi controllare chi ha accesso ai dati nelle tue tabelle e come possono accedervi utilizzando la sicurezza basata sui ruoli.

- **Metadati ricchi**: I tipi di dati e le relazioni sono utilizzati direttamente all'interno di Power Apps.

- **Logica e validazione**: Puoi utilizzare regole aziendali, campi calcolati e regole di validazione per applicare la logica aziendale e mantenere l'accuratezza dei dati.

Ora che sai cos'è Dataverse e perché dovresti usarlo, vediamo come puoi utilizzare Copilot per creare una tabella in Dataverse che soddisfi i requisiti del nostro team finanziario.

> **Nota**: Utilizzerai questa tabella nella prossima sezione per creare un'automazione che estrarrà tutte le informazioni delle fatture e le archivierà nella tabella.

Per creare una tabella in Dataverse utilizzando Copilot, segui i passaggi seguenti:

1. Vai alla schermata principale di [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Nella barra di navigazione a sinistra, seleziona **Tabelle** e poi clicca su **Descrivi la nuova tabella**.

![Seleziona nuova tabella](../../../translated_images/describe-new-table.0792373eb757281e3c5f542f84cad3b5208bfe0e5c4a7786dd2bd31aa848a23c.it.png)

3. Nella schermata **Descrivi la nuova tabella**, utilizza l'area di testo per descrivere la tabella che desideri creare. Ad esempio, **_Voglio creare una tabella per archiviare le informazioni delle fatture_**. Clicca sul pulsante **Invia** per inviare il prompt al Copilot AI.

![Descrivi la tabella](../../../translated_images/copilot-chat-prompt-dataverse.feb2f81e5872b9d2b05d45d11bb6830e0f2ef6a2d4742413bc9a1e50a45bbb89.it.png)

4. Il Copilot AI suggerirà una tabella Dataverse con i campi necessari per archiviare i dati che desideri monitorare e alcuni dati di esempio. Puoi quindi personalizzare la tabella per soddisfare le tue esigenze utilizzando la funzione di assistenza del Copilot AI attraverso passaggi conversazionali.

![Tabella Dataverse suggerita](../../../translated_images/copilot-dataverse-table.b3bc936091324d9db1e943d640df1c7a7df598e66d30f5b8a2999048e26a5073.it.png)

5. Il team finanziario desidera inviare un'email al fornitore per aggiornarlo sullo stato attuale della sua fattura. Puoi utilizzare Copilot per aggiungere un nuovo campo alla tabella per archiviare l'email del fornitore. Ad esempio, puoi utilizzare il seguente prompt per aggiungere un nuovo campo alla tabella: **_Voglio aggiungere una colonna per archiviare l'email del fornitore_**. Clicca sul pulsante **Invia** per inviare il prompt al Copilot AI.

6. Il Copilot AI genererà un nuovo campo e potrai quindi personalizzare il campo per soddisfare le tue esigenze.

7. Una volta completata la tabella, clicca sul pulsante **Crea** per creare la tabella.

## Modelli AI in Power Platform con AI Builder

AI Builder è una funzionalità AI a basso codice disponibile in Power Platform che ti consente di utilizzare modelli AI per aiutarti ad automatizzare i processi e prevedere risultati. Con AI Builder puoi portare l'intelligenza artificiale nelle tue app e flussi che si collegano ai tuoi dati in Dataverse o in varie fonti di dati cloud, come SharePoint, OneDrive o Azure.

## Modelli AI predefiniti vs Modelli AI personalizzati

AI Builder offre due tipi di modelli AI: Modelli AI predefiniti e Modelli AI personalizzati. I modelli AI predefiniti sono modelli AI pronti all'uso, addestrati da Microsoft e disponibili in Power Platform. Questi ti aiutano ad aggiungere intelligenza alle tue app e flussi senza dover raccogliere dati e poi creare, addestrare e pubblicare i tuoi modelli. Puoi utilizzare questi modelli per automatizzare i processi e prevedere risultati.

Alcuni dei modelli AI predefiniti disponibili in Power Platform includono:

- **Estrazione di frasi chiave**: Questo modello estrae frasi chiave dal testo.
- **Rilevamento della lingua**: Questo modello rileva la lingua di un testo.
- **Analisi del sentiment**: Questo modello rileva sentimenti positivi, negativi, neutri o misti nel testo.
- **Lettore di biglietti da visita**: Questo modello estrae informazioni dai biglietti da visita.
- **Riconoscimento del testo**: Questo modello estrae testo dalle immagini.
- **Rilevamento degli oggetti**: Questo modello rileva ed estrae oggetti dalle immagini.
- **Elaborazione documenti**: Questo modello estrae informazioni dai moduli.
- **Elaborazione delle fatture**: Questo modello estrae informazioni dalle fatture.

Con i modelli AI personalizzati puoi portare il tuo modello in AI Builder in modo che possa funzionare come qualsiasi modello personalizzato di AI Builder, permettendoti di addestrare il modello utilizzando i tuoi dati. Puoi utilizzare questi modelli per automatizzare i processi e prevedere risultati sia in Power Apps che in Power Automate. Quando utilizzi il tuo modello ci sono limitazioni che si applicano. Leggi di più su queste [limitazioni](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![Modelli AI Builder](../../../translated_images/ai-builder-models.8069423b84cfc47f6bb989bc3cd0584b5b2471c80fad80bf504d356928a08c9c.it.png)

## Compito #2 - Crea un flusso di elaborazione delle fatture per la nostra startup

Il team finanziario ha avuto difficoltà a elaborare le fatture. Hanno utilizzato un foglio di calcolo per monitorare le fatture, ma è diventato difficile da gestire con l'aumento del numero di fatture. Ti hanno chiesto di creare un flusso di lavoro che li aiuti a elaborare le fatture utilizzando l'AI. Il flusso di lavoro dovrebbe consentire loro di estrarre informazioni dalle fatture e archiviare le informazioni in una tabella Dataverse. Il flusso di lavoro dovrebbe anche consentire loro di inviare un'email al team finanziario con le informazioni estratte.

Ora che sai cos'è AI Builder e perché dovresti usarlo, vediamo come puoi utilizzare il modello AI di elaborazione delle fatture in AI Builder, che abbiamo trattato in precedenza, per creare un flusso di lavoro che aiuti il team finanziario a elaborare le fatture.

Per creare un flusso di lavoro che aiuti il team finanziario a elaborare le fatture utilizzando il modello AI di elaborazione delle fatture in AI Builder, segui i passaggi seguenti:

1. Vai alla schermata principale di [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Utilizza l'area di testo nella schermata principale per descrivere il flusso di lavoro che desideri creare. Ad esempio, **_Elabora una fattura quando arriva nella mia casella di posta_**. Clicca sul pulsante **Invia** per inviare il prompt al Copilot AI.

   ![Copilot Power Automate](../../../translated_images/copilot-chat-prompt-powerautomate.f377e478cc8412de4394fab09e5b72f97b3fc9312526b516ded426102f51c30d.it.png)

3. Il Copilot AI suggerirà le azioni necessarie per eseguire il compito che desideri automatizzare. Puoi cliccare sul pulsante **Avanti** per procedere con i passaggi successivi.

4. Nel passaggio successivo, Power Automate ti chiederà di configurare le connessioni necessarie per il flusso. Una volta completato, clicca sul pulsante **Crea flusso** per creare il flusso.

5. Il Copilot AI genererà un flusso e potrai quindi personalizzare il flusso per soddisfare le tue esigenze.

6. Aggiorna il trigger del flusso e imposta la **Cartella** sulla cartella in cui verranno archiviati gli allegati delle fatture. Ad esempio, puoi impostare la cartella su **Posta in arrivo**. Clicca su **Mostra opzioni avanzate** e imposta **Solo con allegati** su **Sì**. Questo garantirà che il flusso venga eseguito solo quando viene ricevuta un'email con un allegato nella cartella.

7. Rimuovi le seguenti azioni dal flusso: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** e **Compose 4** perché non le utilizzerai.

8. Rimuovi l'azione **Condition** dal flusso perché non la utilizzerai. Dovrebbe apparire come nello screenshot seguente:

   ![Power Automate, rimuovi azioni](../../../translated_images/powerautomate-remove-actions.7216392fe684ceba4b73c6383edd1cc5e7ded11afd0ca812052a11487d049ef8.it.png)

9. Clicca sul pulsante **Aggiungi un'azione** e cerca **Dataverse**. Seleziona l'azione **Aggiungi una nuova riga**.

10. Nell'azione **Estrai informazioni dalle fatture**, aggiorna il **File della fattura** per puntare al **Contenuto dell'allegato** dell'email. Questo garantirà che il flusso estragga informazioni dall'allegato della fattura.

11. Seleziona la **Tabella** che hai creato in precedenza. Ad esempio, puoi selezionare la tabella **Informazioni sulle fatture**. Scegli il contenuto dinamico dall'azione precedente per popolare i seguenti campi:

    - ID
    - Importo
    - Data
    - Nome
    - Stato - Imposta lo **Stato** su **In sospeso**.
    - Email del fornitore - Utilizza il contenuto dinamico **Da** dal trigger **Quando arriva una nuova email**.

    ![Power Automate aggiungi riga](../../../translated_images/powerautomate-add-row.5edce45e5dd3d51e5152688dc140ad43e1423e7a9fef9a206f82a7965ea68d73.it.png)

12. Una volta completato il flusso, clicca sul pulsante **Salva** per salvare il flusso. Puoi quindi testare il flusso inviando un'email con una fattura alla cartella che hai specificato nel trigger.

> **Il tuo compito**: Il flusso che hai appena creato è un buon inizio, ora devi pensare a come puoi creare un'automazione che permetta al nostro team finanziario di inviare un'email al fornitore per aggiornarlo sullo stato attuale della sua fattura. Il tuo suggerimento: il flusso deve essere eseguito quando lo stato della fattura cambia.

## Utilizza un modello AI di generazione di testo in Power Automate

Il modello AI "Crea testo con GPT" in AI Builder ti consente di generare testo basato su un prompt ed è alimentato dal Microsoft Azure OpenAI Service. Con questa funzionalità, puoi incorporare la tecnologia GPT (Generative Pre-Trained Transformer) nelle tue app e flussi per creare una varietà di flussi automatizzati e applicazioni perspicaci.

I modelli GPT subiscono un ampio addestramento su enormi quantità di dati, permettendo loro di produrre testo che somiglia molto al linguaggio umano quando viene fornito un prompt. Quando integrati con l'automazione dei flussi di lavoro, i modelli AI come GPT possono essere sfruttati per semplificare e automatizzare una vasta gamma di attività.

Ad esempio, puoi creare flussi per generare automaticamente testo per una varietà di casi d'uso, come: bozze di email, descrizioni di prodotti e altro. Puoi anche utilizzare il modello per generare testo per una varietà di app, come chatbot e app di assistenza clienti che consentono agli agenti del servizio clienti di rispondere in modo efficace ed efficiente alle richieste dei clienti.

![Crea un prompt](../../../translated_images/create-prompt-gpt.69d429300c2e870a12ec95556cda9bacf6a173e452cdca02973c90df5f705cee.it.png)

Per imparare come utilizzare questo modello AI in Power Automate, consulta il modulo [Aggiungi intelligenza con AI Builder e GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Ottimo lavoro! Continua a imparare

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'AI generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'AI generativa!

Vai alla Lezione 11 dove vedremo come [integrare l'AI generativa con Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.