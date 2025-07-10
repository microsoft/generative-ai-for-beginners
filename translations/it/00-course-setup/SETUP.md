<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:29:06+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "it"
}
-->
# Configura il tuo ambiente di sviluppo

Abbiamo configurato questo repository e corso con un [contenitore di sviluppo](https://containers.dev?WT.mc_id=academic-105485-koreyst) che include un runtime universale in grado di supportare lo sviluppo in Python3, .NET, Node.js e Java. La configurazione correlata è definita nel file `devcontainer.json` situato nella cartella `.devcontainer/` alla radice di questo repository.

Per attivare il dev container, avvialo in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (per un runtime ospitato nel cloud) o in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (per un runtime ospitato localmente). Consulta [questa documentazione](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) per maggiori dettagli su come funzionano i dev container all’interno di VS Code.

> [!TIP]  
> Consigliamo di utilizzare GitHub Codespaces per iniziare rapidamente con il minimo sforzo. Offre una generosa [quota di utilizzo gratuita](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) per gli account personali. Configura i [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) per interrompere o eliminare i codespaces inattivi e massimizzare l’uso della tua quota.

## 1. Esecuzione degli assignment

Ogni lezione potrà includere assignment _opzionali_ forniti in uno o più linguaggi di programmazione, tra cui: Python, .NET/C#, Java e JavaScript/TypeScript. Questa sezione offre indicazioni generali sull’esecuzione di tali assignment.

### 1.1 Assignment in Python

Gli assignment in Python sono forniti come applicazioni (`.py`) o notebook Jupyter (`.ipynb`).  
- Per eseguire il notebook, aprilo in Visual Studio Code, quindi clicca su _Select Kernel_ (in alto a destra) e seleziona l’opzione Python 3 predefinita. Ora puoi cliccare su _Run All_ per eseguire tutto il notebook.  
- Per eseguire applicazioni Python da linea di comando, segui le istruzioni specifiche dell’assignment per selezionare i file corretti e fornire gli argomenti richiesti.

## 2. Configurazione dei provider

Gli assignment **possono** essere configurati per funzionare con uno o più deployment di Large Language Model (LLM) tramite un provider di servizi supportato come OpenAI, Azure o Hugging Face. Questi forniscono un _endpoint ospitato_ (API) a cui possiamo accedere programmaticamente con le credenziali corrette (chiave API o token). In questo corso, trattiamo i seguenti provider:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelli diversi, inclusa la serie principale GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) per modelli OpenAI con focus sulla readiness enterprise  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) per modelli open-source e server di inferenza

**Per questi esercizi dovrai utilizzare i tuoi account personali**. Gli assignment sono opzionali, quindi puoi scegliere di configurare uno, tutti o nessuno dei provider in base ai tuoi interessi. Ecco alcune indicazioni per la registrazione:

| Registrazione | Costo | Chiave API | Playground | Commenti |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Basata su progetto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Modelli multipli disponibili |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [È necessario richiedere l’accesso in anticipo](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://huggingface.co/pricing) | [Token di accesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat ha modelli limitati](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Segui le indicazioni qui sotto per _configurare_ questo repository per l’uso con i diversi provider. Gli assignment che richiedono un provider specifico conterranno uno di questi tag nel nome del file:  
 - `aoai` - richiede endpoint e chiave Azure OpenAI  
 - `oai` - richiede endpoint e chiave OpenAI  
 - `hf` - richiede token Hugging Face

Puoi configurare uno, nessuno o tutti i provider. Gli assignment correlati genereranno un errore in caso di credenziali mancanti.

### 2.1. Creare il file `.env`

Si presume che tu abbia già letto le indicazioni sopra, ti sia registrato presso il provider rilevante e abbia ottenuto le credenziali di autenticazione necessarie (API_KEY o token). Nel caso di Azure OpenAI, si presume inoltre che tu abbia un deployment valido di un servizio Azure OpenAI (endpoint) con almeno un modello GPT distribuito per il completamento chat.

Il passo successivo è configurare le tue **variabili d’ambiente locali** come segue:

1. Cerca nella cartella principale un file `.env.copy` che dovrebbe contenere qualcosa di simile a questo:

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

2. Copia quel file in `.env` usando il comando qui sotto. Questo file è _gitignore-d_, per mantenere i segreti al sicuro.

   ```bash
   cp .env.copy .env
   ```

3. Compila i valori (sostituisci i segnaposto a destra del `=`) come descritto nella sezione successiva.

3. (Opzionale) Se usi GitHub Codespaces, puoi salvare le variabili d’ambiente come _Codespaces secrets_ associate a questo repository. In tal caso, non sarà necessario configurare un file .env locale. **Tieni però presente che questa opzione funziona solo con GitHub Codespaces.** Dovrai comunque configurare il file .env se usi Docker Desktop.

### 2.2. Popolare il file `.env`

Diamo un’occhiata veloce ai nomi delle variabili per capire cosa rappresentano:

| Variabile  | Descrizione  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Questo è il token di accesso utente che hai configurato nel tuo profilo |
| OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare il servizio OpenAI non Azure |
| AZURE_OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare il servizio Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Questo è l’endpoint distribuito per una risorsa Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Questo è l’endpoint di deployment del modello per la _generazione di testo_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Questo è l’endpoint di deployment del modello per gli _embedding di testo_ |
| | |

Nota: Le ultime due variabili Azure OpenAI riflettono un modello predefinito per il completamento chat (generazione testo) e per la ricerca vettoriale (embedding) rispettivamente. Le istruzioni per configurarli saranno definite negli assignment rilevanti.

### 2.3 Configurare Azure: dal Portale

I valori dell’endpoint e della chiave Azure OpenAI si trovano nel [Portale Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), quindi iniziamo da lì.

1. Vai al [Portale Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Clicca sull’opzione **Keys and Endpoint** nella barra laterale (menu a sinistra).  
3. Clicca su **Show Keys** - dovresti vedere: KEY 1, KEY 2 e Endpoint.  
4. Usa il valore di KEY 1 per AZURE_OPENAI_API_KEY  
5. Usa il valore di Endpoint per AZURE_OPENAI_ENDPOINT

Ora ci servono gli endpoint per i modelli specifici che abbiamo distribuito.

1. Clicca sull’opzione **Model deployments** nella barra laterale (menu a sinistra) per la risorsa Azure OpenAI.  
2. Nella pagina di destinazione, clicca su **Manage Deployments**

Questo ti porterà al sito Azure OpenAI Studio, dove troveremo gli altri valori come descritto di seguito.

### 2.4 Configurare Azure: da Studio

1. Naviga su [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dalla tua risorsa** come descritto sopra.  
2. Clicca sulla scheda **Deployments** (barra laterale, sinistra) per vedere i modelli attualmente distribuiti.  
3. Se il modello desiderato non è distribuito, usa **Create new deployment** per distribuirlo.  
4. Ti servirà un modello di _text-generation_ - consigliamo: **gpt-35-turbo**  
5. Ti servirà un modello di _text-embedding_ - consigliamo **text-embedding-ada-002**

Ora aggiorna le variabili d’ambiente per riflettere il nome del _Deployment_ usato. Di solito sarà lo stesso nome del modello, a meno che tu non l’abbia cambiato esplicitamente. Ad esempio, potresti avere:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Non dimenticare di salvare il file .env quando hai finito**. Ora puoi uscire dal file e tornare alle istruzioni per eseguire il notebook.

### 2.5 Configurare OpenAI: dal Profilo

La tua chiave API OpenAI si trova nel tuo [account OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se non ne hai una, puoi registrarti e crearne una. Una volta ottenuta la chiave, puoi usarla per compilare la variabile `OPENAI_API_KEY` nel file `.env`.

### 2.6 Configurare Hugging Face: dal Profilo

Il tuo token Hugging Face si trova nel tuo profilo sotto [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Non pubblicare o condividere questi token pubblicamente. Crea invece un nuovo token per l’uso in questo progetto e copialo nel file `.env` sotto la variabile `HUGGING_FACE_API_KEY`. _Nota:_ tecnicamente non è una chiave API, ma viene usato per l’autenticazione, quindi manteniamo questa convenzione di denominazione per coerenza.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.