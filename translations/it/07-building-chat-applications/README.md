# Costruire applicazioni di chat potenziate da AI generativa

[![Costruire applicazioni di chat potenziate da AI generativa](../../../translated_images/it/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Fai clic sull'immagine sopra per vedere il video di questa lezione)_

Ora che abbiamo visto come costruire app di generazione di testo, esploriamo le applicazioni di chat.

Le applicazioni di chat si sono integrate nella nostra vita quotidiana, offrendo più di un semplice mezzo per conversazioni informali. Sono parti integranti del servizio clienti, del supporto tecnico e persino di sofisticati sistemi di consulenza. Probabilmente hai ricevuto assistenza da un'applicazione di chat non molto tempo fa. Con l'integrazione di tecnologie avanzate come l'AI generativa in queste piattaforme, aumenta la complessità e con essa le sfide.

Alcune domande a cui dobbiamo rispondere sono:

- **Costruire l'app**. Come possiamo costruire in modo efficiente e integrare senza soluzione di continuità queste applicazioni potenziate dall'AI per casi d'uso specifici?
- **Monitoraggio**. Una volta distribuite, come possiamo monitorare e assicurarci che le applicazioni operino al massimo livello di qualità, sia in termini di funzionalità sia di adesione ai [sei principi dell'AI responsabile](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Mentre entriamo sempre più in un'epoca definita dall'automazione e dalle interazioni fluide uomo-macchina, comprendere come l'AI generativa trasforma la portata, la profondità e l'adattabilità delle applicazioni di chat diventa essenziale. Questa lezione esplorerà gli aspetti dell'architettura che supportano questi sistemi complessi, analizzerà le metodologie per l'affinamento in compiti specifici di dominio e valuterà le metriche e considerazioni pertinenti per garantire una distribuzione responsabile dell'AI.

## Introduzione

Questa lezione copre:

- Tecniche per costruire e integrare efficacemente applicazioni di chat.
- Come applicare personalizzazione e affinamento alle applicazioni.
- Strategie e considerazioni per monitorare efficacemente le applicazioni di chat.

## Obiettivi di apprendimento

Al termine di questa lezione sarai in grado di:

- Descrivere le considerazioni per costruire e integrare applicazioni di chat nei sistemi esistenti.
- Personalizzare applicazioni di chat per casi d'uso specifici.
- Identificare le metriche chiave e le considerazioni per monitorare e mantenere efficacemente la qualità delle applicazioni di chat potenziate da AI.
- Assicurare che le applicazioni di chat sfruttino l'AI in modo responsabile.

## Integrare l'AI generativa nelle applicazioni di chat

Elevare le applicazioni di chat attraverso l'AI generativa non significa solo renderle più intelligenti; si tratta di ottimizzare la loro architettura, performance e interfaccia utente per offrire un'esperienza di qualità. Ciò include l'analisi delle basi architetturali, delle integrazioni API e delle considerazioni sull'interfaccia utente. Questa sezione mira a offrirti una roadmap completa per navigare questi paesaggi complessi, che tu stia collegandoli a sistemi esistenti o costruendoli come piattaforme autonome.

Al termine di questa sezione sarai dotato delle competenze necessarie per costruire e incorporare applicazioni di chat in modo efficiente.

### Chatbot o applicazione di chat?

Prima di procedere con la costruzione di applicazioni di chat, confrontiamo 'chatbot' e 'applicazioni di chat potenziate da AI,' che svolgono ruoli e funzionalità distinti. Lo scopo principale di un chatbot è automatizzare compiti conversazionali specifici, come rispondere a domande frequenti o tracciare un pacco. Di solito è governato da logica basata su regole o algoritmi AI complessi. Invece, un'applicazione di chat potenziata da AI è un ambiente molto più ampio progettato per facilitare varie forme di comunicazione digitale, come chat di testo, voce e video tra utenti umani. La caratteristica distintiva è l'integrazione di un modello AI generativo che simula conversazioni sfumate, simili a quelle umane, generando risposte basate su una grande varietà di input e contesti. Un'applicazione di chat alimentata da AI generativa può impegnarsi in discussioni a dominio aperto, adattarsi a contesti conversazionali in evoluzione e persino produrre dialoghi creativi o complessi.

La tabella qui sotto evidenzia le differenze e somiglianze chiave per aiutarci a capire i loro ruoli unici nella comunicazione digitale.

| Chatbot                               | Applicazione di Chat potenziata da AI generativa     |
| ------------------------------------- | -------------------------------------- |
| Focalizzato sul compito e basato su regole | Consapevole del contesto                          |
| Spesso integrato in sistemi più grandi  | Può ospitare uno o più chatbot                    |
| Limitato a funzioni programmate       | Integra modelli AI generativi                     |
| Interazioni specializzate e strutturate | Capace di discussioni a dominio aperto            |

### Sfruttare funzionalità predefinite con SDK e API

Quando costruisci un'applicazione di chat, un ottimo primo passo è valutare cosa esiste già. Usare SDK e API per costruire applicazioni di chat è una strategia vantaggiosa per diversi motivi. Integrando SDK e API ben documentate, posizioni strategicamente la tua applicazione per un successo a lungo termine, affrontando problematiche di scalabilità e manutenzione.

- **Accelera il processo di sviluppo e riduce il carico**: Affidarsi a funzionalità predefinite invece del processo costoso di costruirle da zero ti permette di concentrarti su altri aspetti dell'applicazione che possono essere più importanti, come la logica di business.
- **Migliore performance**: Quando costruisci funzionalità da zero, alla fine ti chiedi "Come scala? Questa applicazione è in grado di gestire un improvviso aumento di utenti?" SDK e API ben mantenute spesso includono soluzioni integrate per queste problematiche.
- **Manutenzione più semplice**: Aggiornamenti e miglioramenti sono più facili da gestire poiché la maggior parte delle API e SDK richiedono semplicemente l'aggiornamento di una libreria quando viene rilasciata una versione nuova.
- **Accesso a tecnologia all'avanguardia**: Sfruttare modelli raffinati e addestrati su grandi dataset offre alla tua applicazione capacità di linguaggio naturale.

Accedere alle funzionalità di uno SDK o API tipicamente comporta ottenere il permesso di usare i servizi forniti, spesso tramite una chiave unica o token di autenticazione. Useremo la libreria Python di OpenAI per esplorare come appare questo processo. Puoi provarlo anche tu nel seguente [notebook per OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) o [notebook per Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) di questa lezione.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

L'esempio sopra utilizza il modello GPT-5 mini con la Responses API per completare il prompt, ma nota che la chiave API è impostata prima di farlo. Riceveresti un errore se non impostassi la chiave.

## Esperienza Utente (UX)

I principi generali di UX si applicano alle applicazioni di chat, ma ecco alcune considerazioni aggiuntive particolarmente importanti a causa dei componenti di machine learning coinvolti.

- **Meccanismo per affrontare l'ambiguità**: I modelli di AI generativa occasionalmente generano risposte ambigue. Una funzionalità che consente agli utenti di richiedere chiarimenti può essere utile in tali casi.
- **Ritenzione del contesto**: I modelli avanzati di AI generativa hanno la capacità di ricordare il contesto all'interno di una conversazione, che può essere una risorsa necessaria per l'esperienza utente. Consentire agli utenti di controllare e gestire il contesto migliora l'esperienza, ma introduce il rischio di conservare informazioni sensibili. Considerazioni su quanto a lungo queste informazioni vengano conservate, come l'introduzione di una politica di retention, possono bilanciare la necessità di contesto con la privacy.
- **Personalizzazione**: Con la capacità di apprendere e adattarsi, i modelli AI offrono un'esperienza individualizzata per l'utente. Personalizzare l'esperienza utente tramite funzionalità come i profili utente non solo fa sentire l'utente compreso, ma aiuta anche nella ricerca di risposte specifiche, creando un'interazione più efficiente e soddisfacente.

Un esempio di personalizzazione è l'impostazione "Istruzioni personalizzate" in ChatGPT di OpenAI. Ti permette di fornire informazioni su te stesso che possono essere importanti come contesto per i tuoi prompt. Ecco un esempio di istruzione personalizzata.

![Impostazioni delle istruzioni personalizzate in ChatGPT](../../../translated_images/it/custom-instructions.b96f59aa69356fcf.webp)

Questo "profilo" invia a ChatGPT la richiesta di creare un piano di lezione sulle liste collegate. Nota che ChatGPT considera il fatto che l'utente potrebbe desiderare un piano di lezione più approfondito basato sulla sua esperienza.

![Un prompt in ChatGPT per un piano di lezione sulle liste collegate](../../../translated_images/it/lesson-plan-prompt.cc47c488cf1343df.webp)

### Framework dei messaggi di sistema di Microsoft per grandi modelli linguistici

[Microsoft ha fornito linee guida](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) per scrivere messaggi di sistema efficaci durante la generazione delle risposte dai LLM, suddivise in 4 aree:

1. Definire a chi è rivolto il modello, nonché le sue capacità e limitazioni.
2. Definire il formato di output del modello.
3. Fornire esempi specifici che dimostrino il comportamento previsto del modello.
4. Fornire ulteriori linee guida comportamentali.

### Accessibilità

Che un utente abbia disabilità visive, uditive, motorie o cognitive, un'applicazione di chat ben progettata dovrebbe essere utilizzabile da tutti. La lista seguente suddivide funzionalità specifiche mirate a migliorare l'accessibilità per varie disabilità utente.

- **Funzionalità per disabilità visive**: Temi ad alto contrasto e testo ridimensionabile, compatibilità con lettori di schermo.
- **Funzionalità per disabilità uditive**: Funzioni text-to-speech e speech-to-text, segnali visivi per notifiche audio.
- **Funzionalità per disabilità motorie**: Supporto per navigazione tramite tastiera, comandi vocali.
- **Funzionalità per disabilità cognitive**: Opzioni di linguaggio semplificato.

## Personalizzazione e affinamento per modelli linguistici specifici di dominio

Immagina un'applicazione di chat che comprende il gergo della tua azienda e anticipa le domande specifiche che i suoi utenti fanno comunemente. Ci sono un paio di approcci da menzionare:

- **Sfruttare modelli DSL**. DSL sta per domain specific language (linguaggio specifico di dominio). Puoi sfruttare un modello cosiddetto DSL addestrato su un dominio specifico per comprenderne concetti e scenari.
- **Applicare fine-tuning**. Il fine-tuning è il processo di ulteriore addestramento del modello con dati specifici.

## Personalizzazione: usare un DSL

Sfruttare modelli linguistici specifici di dominio (modelli DSL) può aumentare l'engagement utente fornendo interazioni specializzate e contestualmente rilevanti. È un modello addestrato o perfezionato per comprendere e generare testo relativo a un campo, industria o soggetto specifico. Le opzioni per usare un modello DSL possono variare dal costruirne uno da zero all'usare modelli preesistenti tramite SDK e API. Un'altra opzione è il fine-tuning, che coinvolge prendere un modello pre-addestrato esistente e adattarlo per un dominio specifico.

## Personalizzazione: applicare fine-tuning

Il fine-tuning è spesso considerato quando un modello pre-addestrato non è sufficiente in un dominio specializzato o per un compito specifico.

Per esempio, le domande mediche sono complesse e richiedono molto contesto. Quando un medico diagnostica un paziente si basa su vari fattori come lo stile di vita o condizioni preesistenti, e può persino affidarsi a riviste mediche recenti per convalidare la diagnosi. In scenari così sfumati, un'applicazione di chat AI a uso generico non può essere una fonte affidabile.

### Scenario: un'applicazione medica

Considera un'applicazione di chat pensata per assistere professionisti medici fornendo riferimenti rapidi a linee guida di trattamento, interazioni farmacologiche o risultati di ricerche recenti.

Un modello generico potrebbe essere adeguato per rispondere a domande mediche di base o fornire consigli generali, ma potrebbe avere difficoltà con:

- **Casi altamente specifici o complessi**. Per esempio, un neurologo potrebbe chiedere all'app: "Quali sono le migliori pratiche attuali per gestire l'epilessia resistente ai farmaci in pazienti pediatrici?"
- **Mancanza di aggiornamenti recenti**. Un modello generico potrebbe faticare a fornire risposte attuali che incorporino i più recenti progressi in neurologia e farmacologia.

In casi come questi, il fine-tuning del modello con un dataset medico specializzato può migliorare significativamente la sua capacità di gestire queste complesse richieste mediche in modo più accurato e affidabile. Ciò richiede accesso a un vasto dataset rilevante che rappresenti le sfide e domande specifiche del dominio da affrontare.

## Considerazioni per un'esperienza di chat AI di alta qualità

Questa sezione delinea i criteri per applicazioni di chat "di alta qualità", che includono la raccolta di metriche azionabili e l'adesione a un quadro che sfrutta responsabilmente la tecnologia AI.

### Metriche chiave

Per mantenere alte prestazioni dell'applicazione, è essenziale monitorare metriche chiave e considerazioni. Queste misurazioni non solo assicurano la funzionalità dell'applicazione, ma valutano anche la qualità del modello AI e dell'esperienza utente. Di seguito una lista che copre metriche basi, AI ed esperienza utente da considerare.

| Metrica                      | Definizione                                                                                                             | Considerazioni per lo sviluppatore chat                                   |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Misura il tempo in cui l'applicazione è operativa e accessibile dagli utenti.                                            | Come minimizzerai i tempi di inattività?                                  |
| **Tempo di risposta**         | Il tempo impiegato dall'applicazione per rispondere a una query dell'utente.                                            | Come puoi ottimizzare l'elaborazione delle richieste per migliorare i tempi di risposta? |
| **Precisione**                | Il rapporto tra previsioni positive corrette e il totale delle previsioni positive.                                      | Come convaliderai la precisione del tuo modello?                          |
| **Richiamo (Sensibilità)**    | Il rapporto tra previsioni positive corrette e il numero reale di positivi.                                            | Come misurerai e migliorerai il richiamo?                                |
| **Punteggio F1**              | La media armonica di precisione e richiamo, che bilancia il compromesso tra entrambi.                                   | Qual è il tuo obiettivo di punteggio F1? Come bilancerai precisione e richiamo? |
| **Perplessità**               | Misura quanto bene la distribuzione di probabilità prevista dal modello si allinea con la distribuzione reale dei dati. | Come minimizzerai la perplessità?                                        |
| **Metriche di soddisfazione utente** | Misura la percezione dell'utente sull'applicazione. Spesso raccolte tramite sondaggi.                                   | Con quale frequenza raccoglierai feedback utente? Come ti adatterai in base a esso? |
| **Tasso di errore**           | Il tasso con cui il modello commette errori nella comprensione o nell'output.                                           | Quali strategie hai in atto per ridurre i tassi di errore?                |
| **Cicli di riaddestramento** | La frequenza con cui il modello viene aggiornato per incorporare nuovi dati e approfondimenti.                          | Quanto spesso riaddestrerai il modello? Cosa innesca un ciclo di riaddestramento? |

| **Rilevamento Anomalie**    | Strumenti e tecniche per identificare schemi insoliti che non si conformano al comportamento previsto.                 | Come risponderai alle anomalie?                                         |

### Implementare Pratiche di AI Responsabile nelle Applicazioni di Chat

L'approccio di Microsoft all'AI Responsabile ha identificato sei principi che dovrebbero guidare lo sviluppo e l'uso dell'AI. Di seguito i principi, la loro definizione e le cose che uno sviluppatore di chat dovrebbe considerare e perché dovrebbero prenderle sul serio.

| Principi               | Definizione di Microsoft                               | Considerazioni per lo Sviluppatore di Chat                             | Perché è Importante                                                                |
| ---------------------- | ----------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Equità                 | I sistemi AI dovrebbero trattare tutte le persone in modo equo. | Assicurarsi che l'applicazione di chat non discrimini in base ai dati degli utenti. | Per costruire fiducia e inclusività tra gli utenti; evita implicazioni legali.     |
| Affidabilità e Sicurezza | I sistemi AI dovrebbero funzionare in modo affidabile e sicuro. | Implementare test e sistemi di sicurezza per minimizzare errori e rischi. | Garantisce la soddisfazione dell'utente e previene potenziali danni.               |
| Privacy e Sicurezza     | I sistemi AI dovrebbero essere sicuri e rispettare la privacy. | Implementare forti misure di crittografia e protezione dei dati.      | Per proteggere i dati sensibili degli utenti e rispettare le leggi sulla privacy.  |
| Inclusività            | I sistemi AI dovrebbero responsabilizzare tutti e coinvolgere le persone. | Progettare interfacce UI/UX accessibili e facili da usare per pubblici diversi. | Assicura che un maggior numero di persone possa utilizzare efficacemente l'applicazione. |
| Trasparenza            | I sistemi AI dovrebbero essere comprensibili.         | Fornire documentazione chiara e motivazioni per le risposte AI.       | Gli utenti sono più propensi a fidarsi di un sistema se possono capire come vengono prese le decisioni. |
| Responsabilità         | Le persone dovrebbero essere responsabili dei sistemi AI. | Stabilire un processo chiaro per la revisione e il miglioramento delle decisioni AI. | Consente miglioramenti continui e misure correttive in caso di errori.             |

## Compito

Consulta [assignment](../../../07-building-chat-applications/python). Ti guiderà attraverso una serie di esercizi, dal primo utilizzo di prompt in chat, alla classificazione e sintesi di testi e altro ancora. Nota che i compiti sono disponibili in diversi linguaggi di programmazione!

## Ottimo lavoro! Continua il percorso

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento sull’AI Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza dell’AI Generativa!

Vai alla Lezione 8 per vedere come puoi iniziare a [costruire applicazioni di ricerca](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->