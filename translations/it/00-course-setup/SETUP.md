<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:47:32+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "it"
}
-->
# Configura il tuo ambiente di sviluppo

Abbiamo configurato questo repository e corso con un [contenitore di sviluppo](https://containers.dev?WT.mc_id=academic-105485-koreyst) che ha un runtime universale in grado di supportare lo sviluppo in Python3, .NET, Node.js e Java. La configurazione correlata è definita nel file `devcontainer.json` situato nella cartella `.devcontainer/` alla radice di questo repository.

Per attivare il contenitore di sviluppo, avvialo in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (per un runtime ospitato nel cloud) o in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (per un runtime ospitato su dispositivo locale). Leggi [questa documentazione](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) per maggiori dettagli su come funzionano i contenitori di sviluppo all'interno di VS Code.

> [!TIP]  
> Consigliamo di utilizzare GitHub Codespaces per un avvio rapido con il minimo sforzo. Offre una generosa [quota di utilizzo gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) per gli account personali. Configura i [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) per interrompere o eliminare i codespaces inattivi per massimizzare l'uso della tua quota.


## 1. Esecuzione degli esercizi

Ogni lezione avrà esercizi _opzionali_ che possono essere forniti in una o più lingue di programmazione, tra cui: Python, .NET/C#, Java e JavaScript/TypeScript. Questa sezione fornisce indicazioni generali relative all'esecuzione di questi esercizi.

### 1.1 Esercizi Python

Gli esercizi Python sono forniti come applicazioni (file `.py`) o come notebook Jupyter (file `.ipynb`). 
- Per eseguire il notebook, aprilo in Visual Studio Code, quindi clicca su _Select Kernel_ (in alto a destra) e seleziona l'opzione predefinita Python 3 mostrata. Ora puoi selezionare _Run All_ per eseguire il notebook.
- Per eseguire le applicazioni Python dalla riga di comando, segui le istruzioni specifiche dell'esercizio per assicurarti di selezionare i file corretti e fornire gli argomenti richiesti.

## 2. Configurazione dei provider

Gli esercizi **possono** anche essere configurati per funzionare contro una o più implementazioni di modelli di linguaggio di grandi dimensioni (LLM) attraverso un provider di servizi supportato come OpenAI, Azure o Hugging Face. Questi forniscono un _endpoint ospitato_ (API) a cui possiamo accedere programmaticamente con le giuste credenziali (chiave API o token). In questo corso, discutiamo di questi provider:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelli diversi tra cui la serie principale GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) per i modelli OpenAI con focus sulla prontezza aziendale
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) per modelli open-source e server di inferenza

**Dovrai utilizzare i tuoi account per questi esercizi**. Gli esercizi sono opzionali, quindi puoi scegliere di configurare uno, tutti o nessuno dei provider in base ai tuoi interessi. Alcune indicazioni per l'iscrizione:

| Iscrizione | Costo | Chiave API | Playground | Commenti |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basato su progetto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Molteplici modelli disponibili |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Devi applicare in anticipo per l'accesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://huggingface.co/pricing) | [Token di accesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ha modelli limitati](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Segui le istruzioni di seguito per _configurare_ questo repository per l'uso con diversi provider. Gli esercizi che richiedono un provider specifico conterranno uno di questi tag nel loro nome file:
 - `aoai` - richiede endpoint Azure OpenAI, chiave
 - `oai` - richiede endpoint OpenAI, chiave
 - `hf` - richiede token Hugging Face

Puoi configurare uno, nessuno o tutti i provider. Gli esercizi correlati semplicemente genereranno errori in caso di credenziali mancanti.

###  2.1. Crea file `.env`

Supponiamo che tu abbia già letto le indicazioni sopra e ti sia registrato con il provider rilevante, ottenendo le credenziali di autenticazione richieste (API_KEY o token). Nel caso di Azure OpenAI, supponiamo che tu abbia anche un'implementazione valida di un servizio Azure OpenAI (endpoint) con almeno un modello GPT distribuito per il completamento delle chat.

Il passo successivo è configurare le tue **variabili di ambiente locali** come segue:


1. Cerca nella cartella radice un file `.env.copy` che dovrebbe avere contenuti come questo:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copia quel file in `.env` usando il comando sotto. Questo file è _gitignore-d_, mantenendo i segreti al sicuro.

   ```bash
   cp .env.copy .env
   ```

3. Compila i valori (sostituisci i segnaposto sul lato destro di `=`) come descritto nella sezione successiva.

3. (Opzione) Se utilizzi GitHub Codespaces, hai l'opzione di salvare le variabili di ambiente come _segreti di Codespaces_ associati a questo repository. In tal caso, non sarà necessario configurare un file .env locale. **Tuttavia, nota che questa opzione funziona solo se utilizzi GitHub Codespaces.** Dovrai comunque configurare il file .env se utilizzi Docker Desktop.


### 2.2. Popolare il file `.env`

Diamo un'occhiata veloce ai nomi delle variabili per capire cosa rappresentano:

| Variabile  | Descrizione  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Questo è il token di accesso utente che hai configurato nel tuo profilo |
| OPENAI_API_KEY | Questa è la chiave di autorizzazione per l'uso del servizio per endpoint OpenAI non Azure |
| AZURE_OPENAI_API_KEY | Questa è la chiave di autorizzazione per l'uso di quel servizio |
| AZURE_OPENAI_ENDPOINT | Questo è l'endpoint distribuito per una risorsa Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Questo è l'endpoint di distribuzione del modello di _generazione del testo_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Questo è l'endpoint di distribuzione del modello di _embedding del testo_ |
| | |

Nota: Le ultime due variabili Azure OpenAI riflettono un modello predefinito per il completamento delle chat (generazione del testo) e la ricerca vettoriale (embedding) rispettivamente. Le istruzioni per configurarli saranno definite negli esercizi rilevanti.


### 2.3 Configura Azure: Dal portale

I valori dell'endpoint e della chiave Azure OpenAI saranno trovati nel [Portale di Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), quindi iniziamo da lì.

1. Vai al [Portale di Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clicca sull'opzione **Chiavi e Endpoint** nella barra laterale (menu a sinistra).
1. Clicca su **Mostra Chiavi** - dovresti vedere quanto segue: KEY 1, KEY 2 e Endpoint.
1. Usa il valore KEY 1 per AZURE_OPENAI_API_KEY
1. Usa il valore dell'Endpoint per AZURE_OPENAI_ENDPOINT

Successivamente, abbiamo bisogno degli endpoint per i modelli specifici che abbiamo distribuito.

1. Clicca sull'opzione **Distribuzioni dei modelli** nella barra laterale (menu a sinistra) per la risorsa Azure OpenAI.
1. Nella pagina di destinazione, clicca su **Gestisci Distribuzioni**

Questo ti porterà al sito web di Azure OpenAI Studio, dove troveremo gli altri valori come descritto di seguito.

### 2.4 Configura Azure: Da Studio

1. Vai a [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dalla tua risorsa** come descritto sopra.
1. Clicca sulla scheda **Distribuzioni** (barra laterale, a sinistra) per visualizzare i modelli attualmente distribuiti.
1. Se il modello desiderato non è distribuito, usa **Crea nuova distribuzione** per distribuirlo.
1. Avrai bisogno di un modello di _generazione del testo_ - consigliamo: **gpt-35-turbo**
1. Avrai bisogno di un modello di _embedding del testo_ - consigliamo **text-embedding-ada-002**

Ora aggiorna le variabili di ambiente per riflettere il _nome di distribuzione_ utilizzato. Questo sarà tipicamente lo stesso del nome del modello a meno che tu non lo abbia cambiato esplicitamente. Quindi, come esempio, potresti avere:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Non dimenticare di salvare il file .env quando hai finito**. Ora puoi uscire dal file e tornare alle istruzioni per eseguire il notebook.

### 2.5 Configura OpenAI: Dal profilo

La tua chiave API OpenAI può essere trovata nel tuo [account OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se non ne hai una, puoi registrarti per un account e creare una chiave API. Una volta che hai la chiave, puoi usarla per popolare la variabile `OPENAI_API_KEY` nel file `.env`.

### 2.6 Configura Hugging Face: Dal profilo

Il tuo token Hugging Face può essere trovato nel tuo profilo sotto [Token di accesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Non pubblicare o condividere questi pubblicamente. Invece, crea un nuovo token per l'uso di questo progetto e copialo nel file `.env` sotto la variabile `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente questo non è una chiave API ma viene utilizzato per l'autenticazione, quindi manteniamo quella convenzione di denominazione per coerenza.

**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.