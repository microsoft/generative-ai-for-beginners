<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:17:16+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "it"
}
-->
# Configura il tuo ambiente di sviluppo

Abbiamo impostato questo repository e corso con un [contenitore di sviluppo](https://containers.dev?WT.mc_id=academic-105485-koreyst) che ha un runtime universale in grado di supportare lo sviluppo in Python3, .NET, Node.js e Java. La configurazione correlata è definita nel file `devcontainer.json` situato nella cartella `.devcontainer/` alla radice di questo repository.

Per attivare il contenitore di sviluppo, avvialo in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (per un runtime ospitato nel cloud) o in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (per un runtime ospitato su un dispositivo locale). Leggi [questa documentazione](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) per maggiori dettagli su come funzionano i contenitori di sviluppo all'interno di VS Code.

> [!TIP]  
> Raccomandiamo di utilizzare GitHub Codespaces per un avvio rapido con il minimo sforzo. Offre una generosa [quota di utilizzo gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) per account personali. Configura [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) per fermare o eliminare i codespaces inattivi per massimizzare l'uso della tua quota.

## 1. Esecuzione degli incarichi

Ogni lezione avrà incarichi _opzionali_ che possono essere forniti in una o più lingue di programmazione tra cui: Python, .NET/C#, Java e JavaScript/TypeScript. Questa sezione fornisce indicazioni generali relative all'esecuzione di tali incarichi.

### 1.1 Incarichi in Python

Gli incarichi in Python sono forniti sia come applicazioni (file `.py`) sia come notebook Jupyter (file `.ipynb`).
- Per eseguire il notebook, aprilo in Visual Studio Code quindi clicca su _Select Kernel_ (in alto a destra) e seleziona l'opzione predefinita Python 3 mostrata. Ora puoi _Run All_ per eseguire il notebook.
- Per eseguire applicazioni Python dalla riga di comando, segui le istruzioni specifiche dell'incarico per assicurarti di selezionare i file corretti e fornire gli argomenti richiesti.

## 2. Configurazione dei provider

Gli incarichi **possono** anche essere impostati per funzionare con uno o più deployment di Large Language Model (LLM) tramite un provider di servizi supportato come OpenAI, Azure o Hugging Face. Questi forniscono un _endpoint ospitato_ (API) a cui possiamo accedere programmaticamente con le credenziali corrette (chiave API o token). In questo corso, discutiamo di questi provider:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelli diversi inclusa la serie core GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) per modelli OpenAI con attenzione alla prontezza aziendale
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) per modelli open-source e server di inferenza

**Dovrai utilizzare i tuoi account per questi esercizi**. Gli incarichi sono opzionali quindi puoi scegliere di impostare uno, tutti - o nessuno - dei provider in base ai tuoi interessi. Alcune indicazioni per l'iscrizione:

| Iscrizione | Costo | Chiave API | Playground | Commenti |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basato su progetto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Molti modelli disponibili |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Devi fare richiesta anticipata per l'accesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://huggingface.co/pricing) | [Token di accesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ha modelli limitati](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Segui le istruzioni seguenti per _configurare_ questo repository per l'uso con diversi provider. Gli incarichi che richiedono un provider specifico conterranno uno di questi tag nel loro nome file:
- `aoai` - richiede endpoint Azure OpenAI, chiave
- `oai` - richiede endpoint OpenAI, chiave
- `hf` - richiede token Hugging Face

Puoi configurare uno, nessuno o tutti i provider. Gli incarichi correlati semplicemente daranno errore per credenziali mancanti.

### 2.1. Creare il file `.env`

Supponiamo che tu abbia già letto le indicazioni sopra e ti sia iscritto con il provider rilevante, ottenendo le credenziali di autenticazione richieste (API_KEY o token). Nel caso di Azure OpenAI, supponiamo che tu abbia anche un deployment valido di un servizio Azure OpenAI (endpoint) con almeno un modello GPT distribuito per il completamento chat.

Il passo successivo è configurare le tue **variabili di ambiente locali** come segue:

1. Cerca nella cartella principale un file `.env.copy` che dovrebbe avere contenuti simili a questo:

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

2. Copia quel file in `.env` usando il comando qui sotto. Questo file è _gitignore-d_, mantenendo al sicuro i segreti.

   ```bash
   cp .env.copy .env
   ```

3. Compila i valori (sostituisci i segnaposto sul lato destro di `=`) come descritto nella sezione successiva.

3. (Opzione) Se utilizzi GitHub Codespaces, hai la possibilità di salvare le variabili di ambiente come _segreti di Codespaces_ associati a questo repository. In tal caso, non sarà necessario impostare un file .env locale. **Tuttavia, nota che questa opzione funziona solo se utilizzi GitHub Codespaces.** Dovrai comunque impostare il file .env se utilizzi Docker Desktop invece.

### 2.2. Compilare il file `.env`

Diamo un'occhiata rapida ai nomi delle variabili per capire cosa rappresentano:

| Variabile  | Descrizione  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Questo è il token di accesso utente che hai impostato nel tuo profilo |
| OPENAI_API_KEY | Questa è la chiave di autorizzazione per utilizzare il servizio per endpoint OpenAI non-Azure |
| AZURE_OPENAI_API_KEY | Questa è la chiave di autorizzazione per utilizzare quel servizio |
| AZURE_OPENAI_ENDPOINT | Questo è l'endpoint distribuito per una risorsa Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Questo è l'endpoint di deployment del modello _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Questo è l'endpoint di deployment del modello _text embeddings_ |
| | |

Nota: Le ultime due variabili Azure OpenAI riflettono un modello predefinito per il completamento chat (generazione di testo) e la ricerca vettoriale (embedding) rispettivamente. Le istruzioni per impostarle saranno definite negli incarichi pertinenti.

### 2.3 Configurare Azure: dal portale

I valori di endpoint e chiave di Azure OpenAI si trovano nel [Portale di Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) quindi iniziamo da lì.

1. Vai al [Portale di Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clicca sull'opzione **Keys and Endpoint** nella barra laterale (menu a sinistra).
1. Clicca su **Show Keys** - dovresti vedere quanto segue: KEY 1, KEY 2 ed Endpoint.
1. Usa il valore di KEY 1 per AZURE_OPENAI_API_KEY
1. Usa il valore di Endpoint per AZURE_OPENAI_ENDPOINT

Successivamente, abbiamo bisogno degli endpoint per i modelli specifici che abbiamo distribuito.

1. Clicca sull'opzione **Model deployments** nella barra laterale (menu a sinistra) per la risorsa Azure OpenAI.
1. Nella pagina di destinazione, clicca su **Manage Deployments**

Questo ti porterà al sito web di Azure OpenAI Studio, dove troveremo gli altri valori come descritto di seguito.

### 2.4 Configurare Azure: dallo Studio

1. Vai su [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dalla tua risorsa** come descritto sopra.
1. Clicca sulla scheda **Deployments** (barra laterale, a sinistra) per visualizzare i modelli attualmente distribuiti.
1. Se il modello desiderato non è distribuito, usa **Create new deployment** per distribuirlo.
1. Avrai bisogno di un modello _text-generation_ - consigliamo: **gpt-35-turbo**
1. Avrai bisogno di un modello _text-embedding_ - consigliamo **text-embedding-ada-002**

Ora aggiorna le variabili di ambiente per riflettere il _Nome del deployment_ utilizzato. Questo sarà tipicamente lo stesso del nome del modello a meno che tu non l'abbia cambiato esplicitamente. Quindi, ad esempio, potresti avere:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Non dimenticare di salvare il file .env quando hai finito**. Ora puoi uscire dal file e tornare alle istruzioni per eseguire il notebook.

### 2.5 Configurare OpenAI: dal profilo

La tua chiave API di OpenAI può essere trovata nel tuo [account OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se non ne hai una, puoi iscriverti per un account e creare una chiave API. Una volta che hai la chiave, puoi usarla per popolare la variabile `OPENAI_API_KEY` nel file `.env`.

### 2.6 Configurare Hugging Face: dal profilo

Il tuo token Hugging Face può essere trovato nel tuo profilo sotto [Token di Accesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Non postare o condividere questi pubblicamente. Invece, crea un nuovo token per l'uso di questo progetto e copialo nel file `.env` sotto la variabile `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente non è una chiave API ma viene utilizzato per l'autenticazione quindi manteniamo quella convenzione di denominazione per coerenza.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.