<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:30:27+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "it"
}
-->
# Generazione Aumentata dal Recupero (RAG) e Database di Vettori

Nella lezione sulle applicazioni di ricerca, abbiamo appreso brevemente come integrare i tuoi dati nei Modelli di Linguaggio di Grandi Dimensioni (LLMs). In questa lezione, approfondiremo ulteriormente i concetti di fondare i tuoi dati nella tua applicazione LLM, i meccanismi del processo e i metodi per memorizzare i dati, inclusi sia gli embeddings che il testo.

> **Video in arrivo**

## Introduzione

In questa lezione tratteremo i seguenti argomenti:

- Un'introduzione a RAG, cosa è e perché viene utilizzato nell'intelligenza artificiale (IA).

- Comprendere cosa sono i database di vettori e crearne uno per la nostra applicazione.

- Un esempio pratico su come integrare RAG in un'applicazione.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Spiegare l'importanza di RAG nel recupero e nel trattamento dei dati.

- Configurare l'applicazione RAG e fondare i tuoi dati su un LLM

- Integrazione efficace di RAG e Database di Vettori nelle applicazioni LLM.

## Il nostro scenario: migliorare i nostri LLM con i nostri dati

Per questa lezione, vogliamo aggiungere le nostre note nella startup educativa, che consente al chatbot di ottenere maggiori informazioni sui diversi argomenti. Utilizzando le note che abbiamo, gli studenti potranno studiare meglio e comprendere i diversi argomenti, rendendo più facile la revisione per i loro esami. Per creare il nostro scenario, useremo:

- `Azure OpenAI:` il LLM che useremo per creare il nostro chatbot

- `AI for beginners' lesson on Neural Networks`: questi saranno i dati su cui fondiamo il nostro LLM

- `Azure AI Search` e `Azure Cosmos DB:` database di vettori per memorizzare i nostri dati e creare un indice di ricerca

Gli utenti saranno in grado di creare quiz di pratica dalle loro note, flash card di revisione e riassumerle in panoramiche concise. Per iniziare, vediamo cosa è RAG e come funziona:

## Generazione Aumentata dal Recupero (RAG)

Un chatbot alimentato da LLM elabora i prompt degli utenti per generare risposte. È progettato per essere interattivo e coinvolge gli utenti su una vasta gamma di argomenti. Tuttavia, le sue risposte sono limitate al contesto fornito e ai suoi dati di addestramento di base. Ad esempio, il cutoff della conoscenza di GPT-4 è settembre 2021, il che significa che manca di conoscenza degli eventi che si sono verificati dopo questo periodo. Inoltre, i dati utilizzati per addestrare i LLM escludono informazioni riservate come note personali o il manuale di prodotto di un'azienda.

### Come funzionano i RAG (Generazione Aumentata dal Recupero)

Supponiamo che tu voglia distribuire un chatbot che crei quiz dalle tue note, avrai bisogno di una connessione al database di conoscenza. È qui che RAG viene in soccorso. I RAG operano come segue:

- **Database di conoscenza:** Prima del recupero, questi documenti devono essere ingeriti e preprocessati, tipicamente suddividendo documenti di grandi dimensioni in parti più piccole, trasformandoli in embeddings di testo e memorizzandoli in un database.

- **Query dell'utente:** l'utente pone una domanda

- **Recupero:** Quando un utente pone una domanda, il modello di embedding recupera informazioni pertinenti dal nostro database di conoscenza per fornire più contesto che verrà incorporato nel prompt.

- **Generazione Aumentata:** il LLM migliora la sua risposta basandosi sui dati recuperati. Consente alla risposta generata di non essere solo basata sui dati pre-addestrati ma anche su informazioni pertinenti dal contesto aggiunto. I dati recuperati vengono utilizzati per aumentare le risposte del LLM. Il LLM poi restituisce una risposta alla domanda dell'utente.

L'architettura per i RAG è implementata utilizzando trasformatori costituiti da due parti: un encoder e un decoder. Ad esempio, quando un utente pone una domanda, il testo di input viene 'codificato' in vettori che catturano il significato delle parole e i vettori vengono 'decodificati' nel nostro indice di documenti e generano nuovo testo basato sulla query dell'utente. Il LLM utilizza sia un modello encoder-decoder per generare l'output.

Due approcci nell'implementazione di RAG secondo il documento proposto: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sono:

- **_RAG-Sequence_** utilizzando documenti recuperati per prevedere la migliore risposta possibile a una query dell'utente

- **RAG-Token** utilizzando documenti per generare il prossimo token, quindi recuperarli per rispondere alla query dell'utente

### Perché dovresti usare i RAG? 

- **Ricchezza di informazioni:** assicura che le risposte di testo siano aggiornate e attuali. Pertanto, migliora le prestazioni su compiti specifici del dominio accedendo al database di conoscenza interno.

- Riduce la fabbricazione utilizzando **dati verificabili** nel database di conoscenza per fornire contesto alle query degli utenti.

- È **economico** poiché sono più economici rispetto alla messa a punto di un LLM

## Creazione di un database di conoscenza

La nostra applicazione si basa sui nostri dati personali, ovvero la lezione sulla Rete Neurale nel curriculum AI For Beginners.

### Database di Vettori

Un database di vettori, a differenza dei database tradizionali, è un database specializzato progettato per memorizzare, gestire e cercare vettori embedded. Memorizza rappresentazioni numeriche dei documenti. Suddividere i dati in embeddings numerici rende più facile per il nostro sistema AI comprendere e elaborare i dati.

Memorizziamo i nostri embeddings nei database di vettori poiché i LLM hanno un limite sul numero di token che accettano come input. Poiché non puoi passare l'intero embeddings a un LLM, dovremo suddividerli in parti e quando un utente pone una domanda, gli embeddings più simili alla domanda verranno restituiti insieme al prompt. La suddivisione riduce anche i costi sul numero di token passati attraverso un LLM.

Alcuni popolari database di vettori includono Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Puoi creare un modello Azure Cosmos DB utilizzando Azure CLI con il seguente comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dal testo agli embeddings

Prima di memorizzare i nostri dati, dovremo convertirli in embeddings di vettori prima che siano memorizzati nel database. Se stai lavorando con documenti di grandi dimensioni o testi lunghi, puoi suddividerli in base alle query che ti aspetti. La suddivisione può essere fatta a livello di frase o a livello di paragrafo. Poiché la suddivisione deriva significati dalle parole intorno a loro, puoi aggiungere un altro contesto a una parte, ad esempio, aggiungendo il titolo del documento o includendo del testo prima o dopo la parte. Puoi suddividere i dati come segue:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Una volta suddivisi, possiamo poi embeddare il nostro testo utilizzando diversi modelli di embedding. Alcuni modelli che puoi utilizzare includono: word2vec, ada-002 di OpenAI, Azure Computer Vision e molti altri. La scelta di un modello da utilizzare dipenderà dalle lingue che stai utilizzando, dal tipo di contenuto codificato (testo/immagini/audio), dalla dimensione dell'input che può codificare e dalla lunghezza dell'output di embedding.

Un esempio di testo embeddato utilizzando il modello `text-embedding-ada-002` di OpenAI è:

## Recupero e Ricerca di Vettori

Quando un utente pone una domanda, il retriever la trasforma in un vettore utilizzando l'encoder di query, poi cerca nel nostro indice di ricerca documenti per vettori pertinenti nel documento che sono correlati all'input. Una volta fatto, converte sia il vettore di input che i vettori del documento in testo e li passa attraverso il LLM.

### Recupero

Il recupero avviene quando il sistema cerca rapidamente di trovare i documenti dall'indice che soddisfano i criteri di ricerca. L'obiettivo del retriever è ottenere documenti che verranno utilizzati per fornire contesto e fondare il LLM sui tuoi dati.

Ci sono diversi modi per eseguire la ricerca all'interno del nostro database, come:

- **Ricerca per parola chiave** - utilizzata per le ricerche di testo

- **Ricerca semantica** - utilizza il significato semantico delle parole

- **Ricerca vettoriale** - converte i documenti da testo a rappresentazioni vettoriali utilizzando modelli di embedding. Il recupero verrà effettuato interrogando i documenti le cui rappresentazioni vettoriali sono più vicine alla domanda dell'utente.

- **Ibrido** - una combinazione sia di ricerca per parola chiave che di ricerca vettoriale.

Una sfida con il recupero si presenta quando non c'è una risposta simile alla query nel database, il sistema restituirà quindi la migliore informazione che possono ottenere, tuttavia, puoi utilizzare tattiche come impostare la distanza massima per la rilevanza o utilizzare la ricerca ibrida che combina sia parole chiave che ricerca vettoriale. In questa lezione utilizzeremo la ricerca ibrida, una combinazione sia di ricerca vettoriale che di ricerca per parola chiave. Memorizzeremo i nostri dati in un dataframe con colonne contenenti le parti così come gli embeddings.

### Somiglianza vettoriale

Il retriever cercherà nel database di conoscenza embeddings che sono vicini, il vicino più vicino, poiché sono testi che sono simili. Nello scenario in cui un utente pone una query, viene prima embeddato e poi abbinato a embeddings simili. La misura comune che viene utilizzata per trovare quanto sono simili diversi vettori è la somiglianza coseno che si basa sull'angolo tra due vettori.

Possiamo misurare la somiglianza utilizzando altre alternative come la distanza euclidea che è la linea retta tra i punti finali dei vettori e il prodotto scalare che misura la somma dei prodotti degli elementi corrispondenti di due vettori.

### Indice di ricerca

Quando si esegue il recupero, dovremo costruire un indice di ricerca per il nostro database di conoscenza prima di eseguire la ricerca. Un indice memorizzerà i nostri embeddings e potrà recuperare rapidamente le parti più simili anche in un database di grandi dimensioni. Possiamo creare il nostro indice localmente utilizzando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Ri-classificazione

Una volta che hai interrogato il database, potresti aver bisogno di ordinare i risultati dai più rilevanti. Un LLM di ri-classificazione utilizza l'apprendimento automatico per migliorare la rilevanza dei risultati di ricerca ordinandoli dai più rilevanti. Utilizzando Azure AI Search, la ri-classificazione viene effettuata automaticamente per te utilizzando un ri-classificatore semantico. Un esempio di come funziona la ri-classificazione utilizzando i vicini più vicini:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Mettere tutto insieme

L'ultimo passo è aggiungere il nostro LLM al mix per essere in grado di ottenere risposte che sono fondate sui nostri dati. Possiamo implementarlo come segue:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Valutare la nostra applicazione

### Metriche di valutazione

- Qualità delle risposte fornite assicurandosi che suoni naturale, fluente e simile a un essere umano

- Fondazione dei dati: valutare se la risposta è provenuta dai documenti forniti

- Rilevanza: valutare se la risposta corrisponde ed è correlata alla domanda posta

- Fluidità - se la risposta ha senso grammaticalmente

## Casi d'uso per l'utilizzo di RAG (Generazione Aumentata dal Recupero) e database di vettori

Ci sono molti diversi casi d'uso in cui le chiamate di funzione possono migliorare la tua app come:

- Domande e risposte: fondare i dati della tua azienda su una chat che può essere utilizzata dai dipendenti per porre domande.

- Sistemi di raccomandazione: dove puoi creare un sistema che corrisponde ai valori più simili, ad esempio film, ristoranti e molti altri.

- Servizi di chatbot: puoi memorizzare la cronologia delle chat e personalizzare la conversazione basata sui dati dell'utente.

- Ricerca di immagini basata su embeddings vettoriali, utile quando si fa riconoscimento di immagini e rilevamento di anomalie.

## Riepilogo

Abbiamo coperto le aree fondamentali di RAG dall'aggiunta dei nostri dati all'applicazione, la query dell'utente e l'output. Per semplificare la creazione di RAG, puoi utilizzare framework come Semanti Kernel, Langchain o Autogen.

## Compito

Per continuare il tuo apprendimento della Generazione Aumentata dal Recupero (RAG) puoi costruire:

- Costruire un front-end per l'applicazione utilizzando il framework di tua scelta

- Utilizzare un framework, sia LangChain che Semantic Kernel, e ricreare la tua applicazione.

Congratulazioni per aver completato la lezione 👏.

## L'apprendimento non si ferma qui, continua il viaggio

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'AI generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza dell'AI generativa!

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Anche se ci impegniamo per l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.