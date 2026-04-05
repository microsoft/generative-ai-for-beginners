# Scelta e Configurazione di un Fornitore LLM 🔑

I compiti **possono** anche essere configurati per funzionare con uno o più deployment di Large Language Model (LLM) tramite un fornitore di servizi supportato come OpenAI, Azure o Hugging Face. Questi forniscono un _endpoint ospitato_ (API) a cui possiamo accedere programmaticamente con le credenziali corrette (chiave API o token). In questo corso, discutiamo di questi fornitori:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) con modelli diversi inclusa la serie core GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) per modelli OpenAI con focus sulla prontezza enterprise
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) per modelli open-source e server di inferenza

**Dovrai usare i tuoi account per questi esercizi**. I compiti sono opzionali quindi puoi scegliere di configurare uno, tutti - o nessuno - dei fornitori in base ai tuoi interessi. Alcune indicazioni per la registrazione:

| Registrazione | Costo | Chiave API | Playground | Commenti |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Basata su progetto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Molteplici modelli disponibili |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prezzi](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Devi fare richiesta anticipata per l’accesso](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prezzi](https://huggingface.co/pricing) | [Token di accesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ha modelli limitati](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Segui le indicazioni qui sotto per _configurare_ questo repository per l’uso con diversi fornitori. I compiti che richiedono un fornitore specifico conterranno uno di questi tag nel nome del file:

- `aoai` - richiede endpoint e chiave Azure OpenAI
- `oai` - richiede endpoint e chiave OpenAI
- `hf` - richiede token Hugging Face

Puoi configurare uno, nessuno o tutti i fornitori. I compiti correlati daranno semplicemente errore in caso di credenziali mancanti.

## Crea il file `.env`

Supponiamo che tu abbia già letto le indicazioni sopra, ti sia registrato con il fornitore rilevante e abbia ottenuto le credenziali di autenticazione richieste (API_KEY o token). Nel caso di Azure OpenAI, supponiamo che tu abbia anche un deployment valido di un servizio Azure OpenAI (endpoint) con almeno un modello GPT distribuito per completamento chat.

Il passo successivo è configurare le tue **variabili d’ambiente locali** come segue:

1. Cerca nella cartella radice un file `.env.copy` che dovrebbe contenere qualcosa di simile:

   ```bash
   # Fornitore OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Predefinito impostato!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copia quel file in `.env` usando il comando qui sotto. Questo file è _gitignore-ato_, mantenendo i segreti al sicuro.

   ```bash
   cp .env.copy .env
   ```

3. Compila i valori (sostituisci i segnaposto a destra del `=`) come descritto nella sezione successiva.

4. (Opzionale) Se usi GitHub Codespaces, hai l’opzione di salvare le variabili d’ambiente come _segreti Codespaces_ associati a questo repository. In tal caso, non sarà necessario configurare un file .env locale. **Tuttavia, nota che questa opzione funziona solo se usi GitHub Codespaces.** Dovrai comunque configurare il file .env se usi Docker Desktop.

## Popola il file `.env`

Diamo un’occhiata rapida ai nomi delle variabili per capire cosa rappresentano:

| Variabile  | Descrizione  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Questo è il token di accesso utente che hai configurato nel tuo profilo |
| OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare il servizio per endpoint OpenAI non Azure |
| AZURE_OPENAI_API_KEY | Questa è la chiave di autorizzazione per usare quel servizio |
| AZURE_OPENAI_ENDPOINT | Questo è l’endpoint distribuito per una risorsa Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Questo è l’endpoint di deployment del modello di _generazione testo_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Questo è l’endpoint di deployment del modello di _embedding testo_ |
| | |

Nota: Le ultime due variabili Azure OpenAI riflettono un modello predefinito per completamento chat (generazione testo) e ricerca vettoriale (embedding) rispettivamente. Le istruzioni per configurarli saranno definite nei compiti rilevanti.

## Configura Azure: Dal Portale

I valori dell’endpoint e della chiave Azure OpenAI si trovano nel [Portale Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), quindi iniziamo da lì.

1. Vai al [Portale Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Clicca sull’opzione **Chiavi e Endpoint** nella barra laterale (menu a sinistra).
1. Clicca su **Mostra Chiavi** - dovresti vedere quanto segue: CHIAVE 1, CHIAVE 2 e Endpoint.
1. Usa il valore CHIAVE 1 per AZURE_OPENAI_API_KEY
1. Usa il valore Endpoint per AZURE_OPENAI_ENDPOINT

Successivamente, ci servono gli endpoint per i modelli specifici che abbiamo distribuito.

1. Clicca sull’opzione **Deployment modelli** nella barra laterale (menu a sinistra) per la risorsa Azure OpenAI.
1. Nella pagina di destinazione, clicca su **Gestisci Deployment**

Questo ti porterà al sito Azure OpenAI Studio, dove troveremo gli altri valori come descritto di seguito.

## Configura Azure: Da Studio

1. Naviga su [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dalla tua risorsa** come descritto sopra.
1. Clicca sulla scheda **Deployment** (barra laterale, sinistra) per vedere i modelli attualmente distribuiti.
1. Se il modello desiderato non è distribuito, usa **Crea nuovo deployment** per distribuirlo.
1. Ti servirà un modello di _generazione testo_ - consigliamo: **gpt-35-turbo**
1. Ti servirà un modello di _embedding testo_ - consigliamo **text-embedding-ada-002**

Ora aggiorna le variabili d’ambiente per riflettere il _Nome del Deployment_ usato. Questo sarà tipicamente lo stesso del nome del modello a meno che tu non l’abbia cambiato esplicitamente. Quindi, ad esempio, potresti avere:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Non dimenticare di salvare il file .env quando hai finito**. Ora puoi uscire dal file e tornare alle istruzioni per eseguire il notebook.

## Configura OpenAI: Dal Profilo

La tua chiave API OpenAI si trova nel tuo [account OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Se non ne hai una, puoi registrarti per un account e creare una chiave API. Una volta ottenuta la chiave, puoi usarla per popolare la variabile `OPENAI_API_KEY` nel file `.env`.

## Configura Hugging Face: Dal Profilo

Il tuo token Hugging Face si trova nel tuo profilo sotto [Token di Accesso](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Non pubblicare o condividere questi pubblicamente. Invece, crea un nuovo token per l’uso di questo progetto e copialo nel file `.env` sotto la variabile `HUGGING_FACE_API_KEY`. _Nota:_ Tecnicamente questo non è una chiave API ma viene usato per l’autenticazione, quindi manteniamo questa convenzione di denominazione per coerenza.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->