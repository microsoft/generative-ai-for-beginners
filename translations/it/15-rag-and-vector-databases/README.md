# Generazione Aumentata dal Recupero (RAG) e Database Vettoriali

[![Generazione Aumentata dal Recupero (RAG) e Database Vettoriali](../../../translated_images/it/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Nella lezione sulle applicazioni di ricerca, abbiamo brevemente imparato come integrare i propri dati nei Modelli Linguistici di Grandi Dimensioni (LLM). In questa lezione, approfondiremo ulteriormente i concetti di radicamento dei dati nella tua applicazione LLM, la meccanica del processo e i metodi per memorizzare dati, inclusi embedding e testo.

> **Video in arrivo**

## Introduzione

In questa lezione tratteremo i seguenti argomenti:

- Un’introduzione a RAG, cos’è e perché viene usato nell’IA (intelligenza artificiale).

- Comprendere cosa sono i database vettoriali e crearne uno per la nostra applicazione.

- Un esempio pratico su come integrare RAG in un’applicazione.

## Obiettivi di apprendimento

Dopo aver completato questa lezione, sarai in grado di:

- Spiegare l’importanza di RAG nel recupero e nella elaborazione dei dati.

- Configurare un’applicazione RAG e radicare i tuoi dati in un LLM.

- Integrare efficacemente RAG e Database Vettoriali nelle applicazioni LLM.

## Il nostro scenario: migliorare i nostri LLM con i nostri dati

Per questa lezione, vogliamo aggiungere le nostre note alla startup educativa, che permette al chatbot di ottenere più informazioni sulle diverse materie. Usando le note che abbiamo, gli studenti potranno studiare meglio e comprendere i diversi argomenti, rendendo più facile ripassare per gli esami. Per creare il nostro scenario, useremo:

- `Azure OpenAI:` l’LLM che useremo per creare il nostro chatbot

- `Lezione AI per principianti sulle Reti Neurali`: questi saranno i dati su cui radicheremo il nostro LLM

- `Azure AI Search` e `Azure Cosmos DB:` database vettoriale per memorizzare i nostri dati e creare un indice di ricerca

Gli utenti potranno creare quiz di pratica dalle loro note, flashcard di revisione e riassumerli in panoramiche concise. Per cominciare, vediamo cos’è RAG e come funziona:

## Generazione Aumentata dal Recupero (RAG)

Un chatbot alimentato da un LLM elabora i prompt dell’utente per generare risposte. È progettato per essere interattivo e coinvolgere gli utenti su una vasta gamma di argomenti. Tuttavia, le sue risposte sono limitate al contesto fornito e ai dati di addestramento di base. Ad esempio, la conoscenza di GPT-4 si ferma a settembre 2021, il che significa che non conosce eventi avvenuti dopo questo periodo. Inoltre, i dati usati per addestrare gli LLM escludono informazioni riservate come note personali o manuali dei prodotti aziendali.

### Come funzionano i RAG (Generazione Aumentata dal Recupero)

![disegno che mostra come funzionano i RAG](../../../translated_images/it/how-rag-works.f5d0ff63942bd3a6.webp)

Supponiamo che tu voglia distribuire un chatbot che crea quiz dalle tue note, avrai bisogno di una connessione al knowledge base. È qui che interveniene RAG. I RAG operano come segue:

- **Base di conoscenza:** Prima del recupero, questi documenti devono essere ingeriti e preprocessati, tipicamente suddividendo grandi documenti in frammenti più piccoli, trasformandoli in embedding testuali e memorizzandoli in un database.

- **Query utente:** l’utente formula una domanda

- **Recupero:** Quando un utente fa una domanda, il modello di embedding recupera informazioni rilevanti dalla base di conoscenza per fornire più contesto che verrà incorporato nel prompt.

- **Generazione aumentata:** l’LLM migliora la sua risposta basandosi sui dati recuperati. Ciò permette alla risposta generata di non basarsi solo sui dati pre-addestrati ma anche su informazioni rilevanti dal contesto aggiunto. I dati recuperati sono usati per aumentare le risposte dell’LLM. L’LLM quindi fornisce una risposta alla domanda dell’utente.

![disegno che mostra l'architettura dei RAG](../../../translated_images/it/encoder-decode.f2658c25d0eadee2.webp)

L’architettura dei RAG è implementata usando transformer che consistono in due parti: un encoder e un decoder. Per esempio, quando un utente fa una domanda, il testo di input viene “codificato” in vettori che catturano il significato delle parole e i vettori sono “decodificati” nel nostro indice di documenti e generano nuovo testo basato sulla domanda dell’utente. L’LLM usa sia un modello encoder-decoder per generare l’output.

Due approcci per implementare RAG secondo la proposta nel paper: [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sono:

- **_RAG-Sequence_** usando documenti recuperati per predire la migliore risposta possibile alla query utente

- **RAG-Token** usando documenti per generare il token successivo, poi recuperarli per rispondere alla query dell’utente

### Perché usare i RAG?

- **Ricchezza di informazioni:** assicura che le risposte testuali siano aggiornate e attuali. Migliora quindi le prestazioni su compiti specifici di dominio accedendo alla base di conoscenza interna.

- Riduce la generazione di risposte inventate utilizzando **dati verificabili** nella base di conoscenza per fornire il contesto alle query utente.

- È **economico** in quanto più conveniente rispetto al fine-tuning di un LLM.

## Creare una base di conoscenza

La nostra applicazione si basa sui nostri dati personali, cioè la lezione sulle Reti Neurali del curriculum AI per principianti.

### Database vettoriali

Un database vettoriale, a differenza dei database tradizionali, è un database specializzato progettato per memorizzare, gestire e cercare vettori incorporati. Memorizza rappresentazioni numeriche dei documenti. Suddividere i dati in embedding numerici facilita al sistema AI la comprensione e l’elaborazione dei dati.

Memorizziamo i nostri embedding nei database vettoriali poiché gli LLM hanno un limite sul numero di token che accettano come input. Poiché non puoi passare l’intero embedding a un LLM, dovremo suddividerli in frammenti e quando un utente fa una domanda, verranno restituiti gli embedding più simili alla domanda insieme al prompt. Il chunking riduce anche i costi sul numero di token inviati attraverso un LLM.

Alcuni database vettoriali popolari includono Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant e DeepLake. Puoi creare un modello Azure Cosmos DB usando Azure CLI con il seguente comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Da testo a embedding

Prima di memorizzare i nostri dati, dobbiamo convertirli in embedding vettoriali prima di conservarli nel database. Se lavori con documenti grandi o testi lunghi, puoi suddividerli in frammenti basati sulle query previste. Il chunking può avvenire a livello di frase o di paragrafo. Poiché il chunking deriva significati dalle parole intorno, puoi aggiungere altro contesto a un frammento, per esempio aggiungendo il titolo del documento o includendo testo prima o dopo il frammento. Puoi suddividere i dati come segue:

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

    # Se l'ultimo blocco non ha raggiunto la lunghezza minima, aggiungilo comunque
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Una volta suddivisi in chunk, possiamo poi incorporare il nostro testo usando diversi modelli di embedding. Alcuni modelli che puoi usare includono: word2vec, ada-002 di OpenAI, Azure Computer Vision e molti altri. La scelta del modello dipenderà dalle lingue che usi, dal tipo di contenuto codificato (testo/immagini/audio), dalla dimensione dell’input che può codificare e dalla lunghezza dell’output embedding.

Un esempio di testo incorporato usando il modello `text-embedding-ada-002` di OpenAI è:
![un embedding della parola gatto](../../../translated_images/it/cat.74cbd7946bc9ca38.webp)

## Recupero e ricerca vettoriale

Quando un utente fa una domanda, il retriever la trasforma in un vettore usando l’encoder della query, quindi cerca attraverso il nostro indice di ricerca documenti vettoriali rilevanti legati all’input. Una volta fatto, converte sia il vettore di input che i vettori del documento in testo e li passa attraverso l’LLM.

### Recupero

Il recupero avviene quando il sistema si sforza di trovare rapidamente i documenti nell’indice che soddisfano i criteri di ricerca. Lo scopo del retriever è ottenere documenti che verranno usati per fornire contesto e radicare l’LLM sui tuoi dati.

Ci sono diversi modi per eseguire la ricerca nel nostro database come:

- **Ricerca per parole chiave** - usata per ricerche testuali

- **Ricerca vettoriale** - converte documenti da testo a rappresentazioni vettoriali usando modelli di embedding, permettendo una **ricerca semantica** usando il significato delle parole. Il recupero sarà effettuato interrogando i documenti le cui rappresentazioni vettoriali sono più vicine alla domanda dell’utente.

- **Ibrido** - una combinazione di ricerca per parole chiave e vettoriale.

Una sfida del recupero si verifica quando non esiste una risposta simile alla query nel database; il sistema restituirà la miglior informazione possibile, tuttavia, puoi usare tattiche come impostare la distanza massima per la rilevanza o usare la ricerca ibrida che combina parole chiave e vettoriale. In questa lezione useremo la ricerca ibrida, combinazione di ricerca vettoriale e per parole chiave. Memorizzeremo i nostri dati in un dataframe con colonne contenenti sia i chunk che gli embedding.

### Similarità vettoriale

Il retriever cercherà nella base di conoscenza embedding vicini tra loro, i più prossimi vicini, poiché rappresentano testi simili. Nel nostro scenario, un utente formula una query, questa viene prima incorporata e poi confrontata con embedding simili. La misura comune usata per trovare quanto sono simili vettori diversi è la similarità coseno, basata sull’angolo tra due vettori.

Possiamo misurare la similarità anche con alternative come la distanza euclidea, che è la linea retta tra gli endpoint dei vettori, e il prodotto scalare, che misura la somma dei prodotti degli elementi corrispondenti di due vettori.

### Indice di ricerca

Prima di eseguire il recupero, dobbiamo costruire un indice di ricerca per la nostra base di conoscenza. Un indice memorizzerà i nostri embedding e potrà rapidamente recuperare i chunk più simili anche in database di grandi dimensioni. Possiamo creare il nostro indice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Crea l'indice di ricerca
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Per interrogare l'indice, puoi usare il metodo kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Riordinamento

Una volta interrogato il database, potresti dover ordinare i risultati dal più rilevante. Un LLM di riordinamento utilizza il Machine Learning per migliorare la rilevanza dei risultati di ricerca, ordinandoli dal più rilevante. Usando Azure AI Search, il riordinamento viene fatto automaticamente per te tramite un semantic reranker. Ecco un esempio di come funziona il riordinamento usando i vicini più prossimi:

```python
# Trova i documenti più simili
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Stampa i documenti più simili
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

L’ultimo passo è aggiungere il nostro LLM nel circuito per poter ottenere risposte basate sui nostri dati. Possiamo implementarlo come segue:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Converti la domanda in un vettore di query
    query_vector = create_embeddings(user_input)

    # Trova i documenti più simili
    distances, indices = nbrs.kneighbors([query_vector])

    # aggiungi documenti alla query per fornire contesto
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combina la cronologia con l'input dell'utente
    history.append(user_input)

    # crea un oggetto messaggio
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # usa l'API Risposte per generare una risposta
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Valutazione della nostra applicazione

### Metriche di valutazione

- Qualità delle risposte offerte assicurandosi che siano naturali, fluenti e simili a risposte umane

- Radicamento dei dati: valutare se la risposta proviene da documenti forniti

- Rilevanza: valutare che la risposta corrisponda e sia collegata alla domanda posta

- Fluidità: se la risposta ha senso grammaticalmente

## Casi d’uso per RAG e database vettoriali

Ci sono molti casi d’uso diversi dove le chiamate di funzione possono migliorare la tua app, come:

- Domande e Risposte: radicare i dati aziendali a una chat che può essere usata dai dipendenti per fare domande.

- Sistemi di raccomandazione: dove puoi creare un sistema che abbina valori più simili, per esempio film, ristoranti e molto altro.

- Servizi chatbot: puoi memorizzare la cronologia chat e personalizzare la conversazione basata sui dati utente.

- Ricerca immagini basata su embedding vettoriali, utile nel riconoscimento immagini e rilevamento anomalie.

## Sommario

Abbiamo coperto gli aspetti fondamentali di RAG dall’aggiunta dei dati all’applicazione, la query utente e l’output. Per semplificare la creazione di RAG, puoi usare framework come Semantic Kernel, Langchain o Autogen.

## Compito

Per continuare il tuo apprendimento sulla Generazione Aumentata dal Recupero (RAG) puoi costruire:

- Costruire un front-end per l’applicazione usando il framework che preferisci

- Utilizzare un framework, sia LangChain che Semantic Kernel, e ricreare la tua applicazione.

Congratulazioni per aver completato la lezione 👏.

## L’apprendimento non finisce qui, continua il viaggio

Dopo aver completato questa lezione, dai un’occhiata alla nostra [collezione di apprendimento sull’IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare la tua conoscenza dell’IA generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->