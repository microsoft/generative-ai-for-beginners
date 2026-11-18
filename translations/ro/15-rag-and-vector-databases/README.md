# Generarea Augmentată cu Recuperare (RAG) și Bazele de Date Vectoriale

[![Generarea Augmentată cu Recuperare (RAG) și Bazele de Date Vectoriale](../../../translated_images/ro/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

În lecția despre aplicațiile de căutare, am învățat pe scurt cum să integrăm propriile date în Modelele Mari de Limbaj (LLM). În această lecție, vom aprofunda conceptele privind fundamentarea datelor în aplicația ta LLM, mecanica procesului și metodele de stocare a datelor, inclusiv atât încorporări cât și text.

> **Video În Curând**

## Introducere

În această lecție vom acoperi următoarele:

- O introducere în RAG, ce este și de ce se folosește în AI (inteligența artificială).

- Înțelegerea bazelor de date vectoriale și crearea uneia pentru aplicația noastră.

- Un exemplu practic despre cum să integrăm RAG într-o aplicație.

## Obiectivele de Învățare

După finalizarea acestei lecții, vei putea:

- Explica semnificația RAG în recuperarea și procesarea datelor.

- Configura o aplicație RAG și fundamenta un LLM cu datele tale

- Integra eficient RAG și bazele de date vectoriale în aplicațiile LLM.

## Scenariul Nostru: îmbunătățirea LLM-urilor cu propriile noastre date

Pentru această lecție, dorim să adăugăm notițele noastre în startup-ul educațional, ceea ce permite chatbot-ului să obțină mai multe informații despre diferite subiecte. Folosind notițele pe care le avem, cursanții vor putea să studieze mai bine și să înțeleagă diversele teme, făcând mai ușoară revizuirea pentru examene. Pentru a crea acest scenariu vom folosi:

- `Azure OpenAI:` LLM-ul pe care îl vom folosi pentru a crea chatbot-ul nostru

- `AI for beginners' lesson on Neural Networks`: acestea vor fi datele pe care le vom fundamenta în LLM-ul nostru

- `Azure AI Search` și `Azure Cosmos DB:` baza de date vectorială pentru a stoca datele și a crea un index de căutare

Utilizatorii vor putea crea teste practice și flashcarduri de revizuire din notițele lor și să rezume acele notițe în prezentări concise. Ca să începem, să vedem ce este RAG și cum funcționează:

## Generarea Augmentată cu Recuperare (RAG)

Un chatbot alimentat de LLM procesează prompturile utilizatorului pentru a genera răspunsuri. Este conceput să fie interactiv și să interacționeze cu utilizatorii pe o gamă largă de subiecte. Cu toate acestea, răspunsurile sale sunt limitate la contextul oferit și la datele de antrenament fundamentale. De exemplu, limita de cunoștințe pentru GPT-4 este septembrie 2021, ceea ce înseamnă că îi lipsesc informațiile despre evenimentele care au avut loc după această perioadă. În plus, datele folosite pentru antrenarea LLM exclud informații confidențiale cum ar fi notițele personale sau manualul de produs al unei companii.

### Cum funcționează RAG-urile (Generarea Augmentată cu Recuperare)

![desen care arată cum funcționează RAG-urile](../../../translated_images/ro/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Să presupunem că vrei să lansezi un chatbot care creează teste din notițele tale, vei avea nevoie de o conexiune la baza de cunoștințe. Aici intervine RAG. RAG-urile operează astfel:

- **Baza de cunoștințe:** Înainte de recuperare, aceste documente trebuie încărcate și preprocesate, de obicei prin divizarea documentelor mari în bucăți mai mici, transformarea acestora în încorporări text și stocarea într-o bază de date.

- **Întrebarea utilizatorului:** utilizatorul pune o întrebare

- **Recuperare:** Când utilizatorul pune o întrebare, modelul de încorporare recuperează informații relevante din baza noastră de cunoștințe pentru a oferi mai mult context ce va fi încorporat în prompt.

- **Generare Augmentată:** LLM amplifică răspunsul său pe baza datelor recuperate. Aceasta permite ca răspunsul generat să se bazeze nu doar pe date pre-antrenate, ci și pe informații relevante din contextul adăugat. Datele recuperate sunt folosite pentru a augmenta răspunsurile LLM-ului. LLM-ul răspunde apoi la întrebarea utilizatorului.

![Diagramă care arată arhitectura RAG](../../../translated_images/ro/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG combină un recuperator cu un generator: interogarea este convertită într-un vector, comparată cu indexul documentelor pentru a găsi fragmente text relevante, iar aceste fragmente sunt oferite ca context unui LLM, care generează răspunsul. Recuperatorul și generatorul pot folosi modele diferite; RAG nu necesită un transformator encoder-decoder.

Două abordări în implementarea RAG conform lucrării propuse: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sunt:

- **_RAG-Sequence_** folosind documente recuperate pentru a prezice cel mai bun răspuns posibil la o întrebare utilizatorului

- **RAG-Token** folosind documente pentru a genera următorul token, apoi le recuperează pentru a răspunde întrebării utilizatorului

### De ce ai folosi RAG? 

- **Bogăția informațională:** asigură că răspunsurile textuale sunt actualizate și curente. Prin urmare, îmbunătățește performanța în sarcini specifice domeniului prin accesarea bazei interne de cunoștințe.

- Reduce inventarea prin utilizarea **datelor verificabile** din baza de cunoștințe pentru a oferi context întrebărilor utilizatorului.

- Este **rentabil** deoarece este mai economică comparativ cu ajustarea fină a unui LLM

## Crearea unei baze de cunoștințe

Aplicația noastră se bazează pe datele noastre personale, adică lecția despre Rețele Neuronale din curriculum-ul AI pentru Începători.

### Baze de date vectoriale

O bază de date vectorială, spre deosebire de bazele de date tradiționale, este o bază specializată proiectată pentru a stoca, gestiona și căuta vectori încorporați. Stochează reprezentări numerice ale documentelor. Descompunerea datelor în încorporări numerice face mai ușor pentru sistemul nostru AI să înțeleagă și să proceseze datele.

Deoarece LLM-urile au o limită a numărului de tokeni de intrare, împărțim documentele în bucăți înainte de a le încorpora. Când un utilizator pune o întrebare, încorporările cele mai similare cu întrebarea identifică fragmentele text relevante, care sunt returnate împreună cu promptul. Fragmentarea reduce și numărul de tokeni trimiși LLM-ului și, prin urmare, poate reduce costurile.

Unele baze de date vectoriale populare includ Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant și DeepLake. Poți crea un model Azure Cosmos DB folosind Azure CLI cu următoarea comandă:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Din text la încorporări

Înainte de a stoca datele, va trebui să le convertim în încorporări vectoriale înainte de a fi stocate în baza de date. Dacă lucrezi cu documente mari sau texte lungi, le poți împărți în bucăți bazate pe întrebările la care te aștepți. Fragmentarea se poate face la nivel de propoziție sau la nivel de paragraf. Deoarece fragmentarea extrage sensuri din cuvintele din jur, poți adăuga context suplimentar unui fragment, de exemplu, prin adăugarea titlului documentului sau includerea unui text înainte sau după fragment. Poți fragmenta datele astfel:

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

Odată fragmentate, putem apoi încorpora textul folosind diferite modele de încorporare. Unele modele pe care le poți folosi includ: word2vec, ada-002 de la OpenAI, Azure Computer Vision și multe altele. Alegerea unui model depinde de limbile folosite, tipul conținutului codificat (text/imagine/audio), dimensiunea intrării pe care o poate codifica și lungimea încorporării rezultate.

Un exemplu de text încorporat folosind modelul `text-embedding-ada-002` al OpenAI este:
![o încorporare a cuvântului pisică](../../../translated_images/ro/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Recuperare și căutare vectorială

Când un utilizator pune o întrebare, retriever-ul o transformă într-un vector folosind codificatorul de întrebări, apoi caută în indexul nostru de căutare al documentelor vectorii relevanți pentru întrebarea introdusă. Odată făcută această căutare, convertește atât vectorul de intrare cât și vectorii documentelor în text și îl transmite prin LLM.

### Recuperare

Recuperarea are loc când sistemul încearcă să găsească rapid documentele din index care satisfac criteriile de căutare. Scopul retriever-ului este să obțină documente care să fie folosite pentru a oferi context și fundament pentru LLM pe baza datelor tale.

Există mai multe modalități de a efectua căutarea în baza noastră de date, cum ar fi:

- **Căutare după cuvinte cheie** - folosită pentru căutări în text

- **Căutare vectorială** - convertește documentele din text în reprezentări vectoriale folosind modele de încorporare, permițând o **căutare semantică** bazată pe sensul cuvintelor. Recuperarea se face prin interogarea documentelor ale căror vectori sunt cei mai apropiați de întrebarea utilizatorului.

- **Hibridă** - o combinație între căutarea după cuvinte cheie și cea vectorială.

O provocare a recuperării apare când nu există un răspuns similar întrebării în baza de date, sistemul va returna atunci cele mai bune informații pe care le poate găsi, însă poți folosi tactici precum setarea distanței maxime pentru relevanță sau folosirea căutării hibride care combină căutarea după cuvinte cheie și vectorială. În această lecție vom folosi căutarea hibridă, o combinație între căutarea vectorială și cea după cuvinte cheie. Vom stoca datele noastre într-un dataframe cu coloane care conțin fragmentele și încorporările.

### Similaritatea vectorială

Retriever-ul va căuta în baza de cunoștințe încorporările care sunt apropiate între ele—cei mai apropiați vecini—deoarece ele reprezintă texte similare. În acest scenariu, când un utilizator trimite o întrebare, aceasta este mai întâi încorporată și apoi comparată cu încorporări similare. Măsurarea cea mai comună utilizată pentru a compara similaritatea vectorială este similaritatea unghiulară, bazată pe unghiul dintre doi vectori.

Alte metrici pe care le putem folosi pentru a măsura similaritatea includ distanța euclidiană, care este linia dreaptă între capetele vectorilor, și produsul scalar, care măsoară suma produselor elementelor corespunzătoare din cei doi vectori.

### Index de căutare

Când facem recuperare, va trebui să construim un index de căutare pentru baza noastră de cunoștințe înainte de a efectua căutarea. Un index va stoca încorporările și poate prelua rapid fragmentele cele mai similare chiar și într-o bază de date mare. Putem crea indexul local folosind:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ordonare

Odată ce ai interogat baza de date, poate fi nevoie să sortezi rezultatele de la cele mai relevante. Un LLM de re-ordonare utilizează învățarea automată pentru a îmbunătăți relevanța rezultatelor căutării prin ordonarea lor de la cele mai relevante. Folosind Azure AI Search, re-ordonarea se face automat pentru tine folosind un re-ranker semantic. Un exemplu de funcționare a re-ordonării folosind cei mai apropiați vecini:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Punând totul cap la cap

Ultimul pas este să adăugăm LLM-ul în ecuație pentru a putea obține răspunsuri fundamentate pe datele noastre. Putem implementa acest lucru astfel:

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
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use the Responses API to generate a response
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Evaluarea aplicației noastre

### Metrici de evaluare

- Calitatea răspunsurilor furnizate, asigurându-se că sună natural, fluent și uman

- Fundamentarea datelor: evaluarea dacă răspunsul provine din documentele furnizate

- Relevanță: evaluarea dacă răspunsul corespunde și este legat de întrebarea pusă

- Fluență - dacă răspunsul are sens din punct de vedere gramatical

## Cazuri de utilizare pentru RAG (Generarea Augmentată cu Recuperare) și baze de date vectoriale

Există multe cazuri diferite în care RAG poate îmbunătăți aplicația ta, cum ar fi:

- Întrebări și răspunsuri: fundamentarea datelor companiei tale într-un chat care poate fi folosit de angajați pentru a pune întrebări.

- Sisteme de recomandare: unde poți crea un sistem care să potrivească cele mai similare valori, ex. filme, restaurante și multe altele.

- Servicii chatbot: poți stoca istoricul conversațiilor și personaliza conversația bazat pe datele utilizatorului.

- Căutare imagine bazată pe încorporări vectoriale, utilă în recunoașterea imaginilor și detectarea anomaliilor.

## Rezumat

Am acoperit zonele fundamentale ale RAG de la adăugarea datelor în aplicație, întrebarea utilizatorului și ieșirea. Pentru a simplifica crearea RAG, poți folosi framework-uri precum Semantic Kernel, LangChain sau AutoGen.

## Temă

Pentru a-ți continua învățarea despre Retrieval Augmented Generation (RAG), poți construi:

- Construiește o interfață frontală pentru aplicație folosind framework-ul preferat

- Utilizează un framework, fie LangChain sau Semantic Kernel, și recreează aplicația ta.

Felicitări pentru finalizarea lecției 👏.

## Învățarea nu se oprește aici, continuă călătoria

După ce ai terminat această lecție, consultă colecția noastră [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea cunoștințelor despre Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->