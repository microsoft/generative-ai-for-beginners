<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57c41f2af71001a2cff9d8eb797cb843",
  "translation_date": "2025-06-25T07:09:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "it"
}
-->
# Contribuire

Questo progetto accoglie contributi e suggerimenti. La maggior parte dei contributi richiede di accettare un Accordo di Licenza per i Contributori (CLA) dichiarando che hai il diritto di concederci i diritti di utilizzo del tuo contributo. Per dettagli, visita <https://cla.microsoft.com>.

> Importante: quando traduci testo in questo repository, assicurati di non utilizzare la traduzione automatica. Verificheremo le traduzioni tramite la comunità, quindi offriti volontario solo per le traduzioni nelle lingue in cui sei competente.

Quando invii una pull request, un bot CLA determinerà automaticamente se è necessario fornire un CLA e decorerà il PR di conseguenza (ad esempio, etichetta, commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.

## Codice di Condotta

Questo progetto ha adottato il [Codice di Condotta Open Source di Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Per ulteriori informazioni leggi le [FAQ del Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) o contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per qualsiasi domanda o commento aggiuntivo.

## Domande o Problemi?

Si prega di non aprire problemi su GitHub per domande di supporto generale poiché l'elenco di GitHub dovrebbe essere utilizzato per richieste di funzionalità e segnalazioni di bug. In questo modo possiamo tracciare più facilmente i problemi o i bug effettivi dal codice e mantenere la discussione generale separata dal codice effettivo.

## Errori di battitura, Problemi, Bug e contributi

Ogni volta che invii modifiche al repository Generative AI for Beginners, segui queste raccomandazioni.

* Esegui sempre il fork del repository sul tuo account prima di apportare modifiche
* Non combinare più modifiche in una sola pull request. Ad esempio, invia qualsiasi correzione di bug e aggiornamento della documentazione utilizzando PR separati
* Se la tua pull request mostra conflitti di unione, assicurati di aggiornare il tuo main locale per essere uno specchio di ciò che è nel repository principale prima di apportare modifiche
* Se stai inviando una traduzione, crea un PR per tutti i file tradotti poiché non accettiamo traduzioni parziali per il contenuto
* Se stai inviando una correzione di errori di battitura o della documentazione, puoi combinare modifiche in un unico PR dove appropriato

## Guida Generale per la scrittura

- Assicurati che tutti i tuoi URL siano racchiusi tra parentesi quadre seguite da una parentesi senza spazi extra intorno o all'interno `[](../..)`.
- Assicurati che qualsiasi link relativo (cioè link ad altri file e cartelle nel repository) inizi con un `./` riferendosi a un file o una cartella situata nella directory di lavoro corrente o un `../` riferendosi a un file o una cartella situata in una directory di lavoro principale.
- Assicurati che qualsiasi link relativo (cioè link ad altri file e cartelle nel repository) abbia un ID di tracciamento (cioè `?` o `&` poi `wt.mc_id=` o `WT.mc_id=`) alla fine.
- Assicurati che qualsiasi URL dai seguenti domini _github.com, microsoft.com, visualstudio.com, aka.ms e azure.com_ abbia un ID di tracciamento (cioè `?` o `&` poi `wt.mc_id=` o `WT.mc_id=`) alla fine.
- Assicurati che i tuoi link non abbiano un locale specifico per paese (cioè `/en-us/` o `/en/`).
- Assicurati che tutte le immagini siano memorizzate nella cartella `./images`.
- Assicurati che le immagini abbiano nomi descrittivi usando caratteri inglesi, numeri e trattini nel nome della tua immagine.

## Workflow di GitHub

Quando invii una pull request, verranno attivati quattro diversi workflow per convalidare le regole precedenti. Segui semplicemente le istruzioni elencate qui per superare i controlli del workflow.

- [Controlla Percorsi Relativi Interrotti](../..)
- [Controlla Percorsi con Tracciamento](../..)
- [Controlla URL con Tracciamento](../..)
- [Controlla URL Senza Locale](../..)

### Controlla Percorsi Relativi Interrotti

Questo workflow garantisce che qualsiasi percorso relativo nei tuoi file funzioni. Questo repository è distribuito su GitHub pages quindi devi essere molto attento quando digiti i link che collegano tutto insieme per non indirizzare nessuno al posto sbagliato.

Per assicurarti che i tuoi link funzionino correttamente usa semplicemente VS code per controllarli.

Ad esempio, quando passi il mouse su qualsiasi link nei tuoi file, ti verrà chiesto di seguire il link premendo **ctrl + click**

![Screenshot di VS code per seguire i link](../../translated_images/vscode-follow-link.85520ab6a1237adcf01cc9cd8c228ce7b32ae685a034250bd5109e2682b9dfca.it.png)

Se clicchi su un link e non funziona localmente, sicuramente attiverà il workflow e non funzionerà su GitHub.

Per risolvere questo problema, prova a digitare il link con l'aiuto di VS code.

Quando digiti `./` o `../` VS code ti inviterà a scegliere tra le opzioni disponibili in base a ciò che hai digitato.

![Screenshot di VS code per selezionare il percorso relativo](../../translated_images/vscode-select-relative-path.3804eb73c3a9e5f2d345e3d3288f8173a9e584254d0e505d8bcbc6461dbf1f6c.it.png)

Segui il percorso cliccando sul file o cartella desiderato e sarai sicuro che il tuo percorso non sia interrotto.

Una volta aggiunto il percorso relativo corretto, salva e invia le tue modifiche, il workflow verrà attivato di nuovo per verificare le tue modifiche. Se superi il controllo, sei a posto.

### Controlla Percorsi con Tracciamento

Questo workflow garantisce che qualsiasi percorso relativo abbia il tracciamento. Questo repository è distribuito su GitHub pages quindi dobbiamo tracciare il movimento tra i diversi file e cartelle.

Per assicurarti che i tuoi percorsi relativi abbiano il tracciamento, controlla semplicemente il seguente testo `?wt.mc_id=` alla fine del percorso. Se è aggiunto ai tuoi percorsi relativi, supererai questo controllo.

In caso contrario, potresti ricevere il seguente errore.

![Screenshot del commento di GitHub che controlla i percorsi mancanti di tracciamento](../../translated_images/github-check-paths-missing-tracking-comment.880d4afe03e898ffadeebe0f61f7fdea7525c25238bead9fecabc81a0a83b1c0.it.png)

Per risolvere questo problema, prova ad aprire il percorso del file evidenziato dal workflow e aggiungi l'ID di tracciamento alla fine dei percorsi relativi.

Una volta aggiunto l'ID di tracciamento, salva e invia le tue modifiche, il workflow verrà attivato di nuovo per verificare le tue modifiche. Se superi il controllo, sei a posto.

### Controlla URL con Tracciamento

Questo workflow garantisce che qualsiasi URL web abbia il tracciamento. Questo repository è disponibile a tutti, quindi devi assicurarti di tracciare l'accesso per sapere da dove proviene il traffico.

Per assicurarti che i tuoi URL abbiano il tracciamento, controlla semplicemente il seguente testo `?wt.mc_id=` alla fine dell'URL. Se è aggiunto ai tuoi URL, supererai questo controllo.

In caso contrario, potresti ricevere il seguente errore.

![Screenshot del commento di GitHub che controlla gli URL mancanti di tracciamento](../../translated_images/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e3179e59e1bd7d44f16637a1bb1ab265562565251166841ef.it.png)

Per risolvere questo problema, prova ad aprire il percorso del file evidenziato dal workflow e aggiungi l'ID di tracciamento alla fine degli URL.

Una volta aggiunto l'ID di tracciamento, salva e invia le tue modifiche, il workflow verrà attivato di nuovo per verificare le tue modifiche. Se superi il controllo, sei a posto.

### Controlla URL Senza Locale

Questo workflow garantisce che qualsiasi URL web non abbia un locale specifico per paese. Questo repository è disponibile a tutti in tutto il mondo, quindi devi assicurarti di non includere il locale del tuo paese negli URL.

Per assicurarti che i tuoi URL non abbiano il locale del paese, controlla semplicemente il seguente testo `/en-us/` o `/en/` o qualsiasi altro locale di lingua ovunque nell'URL. Se non è presente nei tuoi URL, supererai questo controllo.

In caso contrario, potresti ricevere il seguente errore.

![Screenshot del commento di GitHub che controlla il locale del paese](../../translated_images/github-check-country-locale-comment.2f4fe93228161dee6ec8210f3d6ccc66af6864f6b178b8d96f30818498fba72a.it.png)

Per risolvere questo problema, prova ad aprire il percorso del file evidenziato dal workflow e rimuovi il locale del paese dagli URL.

Una volta rimosso il locale del paese, salva e invia le tue modifiche, il workflow verrà attivato di nuovo per verificare le tue modifiche. Se superi il controllo, sei a posto.

Congratulazioni! Ti contatteremo il prima possibile con un feedback sul tuo contributo.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione umana professionale. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.