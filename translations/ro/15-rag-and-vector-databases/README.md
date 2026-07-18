# Generarea Augmentată prin Recuperare (RAG) și Baze de Date Vectoriale

[![Generarea Augmentată prin Recuperare (RAG) și Baze de Date Vectoriale](../../../translated_images/ro/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

În lecția despre aplicații de căutare, am învățat pe scurt cum să integrăm propriile date în Modele Mari de Limbaj (LLM). În această lecție, vom aprofunda conceptele fundamentării datelor în aplicația noastră LLM, mecanica procesului și metodele de stocare a datelor, incluzând atât embeddings cât și text.

> **Video În Curând**

## Introducere

În această lecție vom acoperi următoarele:

- O introducere în RAG, ce este și de ce este utilizat în AI (inteligența artificială).

- Înțelegerea a ceea ce sunt bazele de date vectoriale și crearea uneia pentru aplicația noastră.

- Un exemplu practic despre cum să integrăm RAG într-o aplicație.

## Obiective de Învățare

După ce veți finaliza această lecție, veți putea:

- Explica semnificația RAG în recuperarea și procesarea datelor.

- Configura aplicația RAG și să fundamentați datele în LLM-ul vostru.

- Integrarea eficientă a RAG și Bazelor de Date Vectoriale în Aplicații LLM.

## Scenariul Nostru: îmbunătățirea LLM-urilor noastre cu propriile date

Pentru această lecție, dorim să adăugăm propriile noastre notițe în startup-ul educațional, care permite chatbot-ului să obțină mai multe informații despre diferite subiecte. Folosind notițele pe care le avem, cursanții vor putea studia mai bine și înțelege diferitele teme, făcând mai ușoară revizuirea pentru examenele lor. Pentru a crea scenariul nostru, vom folosi:

- `Azure OpenAI:` LLM-ul pe care îl vom folosi pentru a crea chatbot-ul nostru

- `Lecția AI pentru Începători despre Rețele Neuronale:` aceasta va fi baza de date pe care vom fundamenta LLM-ul nostru

- `Azure AI Search` și `Azure Cosmos DB:` baza de date vectorială pentru stocarea datelor și crearea unui index de căutare

Utilizatorii vor putea crea chestionare practice din notițele lor, carduri de revizuire și să le rezume în sinteze concise. Pentru a începe, să ne uităm la ce este RAG și cum funcționează:

## Generarea Augmentată prin Recuperare (RAG)

Un chatbot alimentat de LLM procesează prompt-urile utilizatorului pentru a genera răspunsuri. Este conceput să fie interactiv și să interacționeze cu utilizatorii pe o gamă largă de subiecte. Totuși, răspunsurile sale sunt limitate la contextul oferit și la datele sale de bază de antrenament. De exemplu, limita de cunoștințe GPT-4 este septembrie 2021, ceea ce înseamnă că nu are cunoștințe despre evenimentele care au avut loc după această perioadă. În plus, datele utilizate pentru antrenarea LLM-urilor exclud informațiile confidențiale, cum ar fi notițele personale sau manualele produselor unei companii.

### Cum funcționează RAG-urile (Generarea Augmentată prin Recuperare)

![desen care arată cum funcționează RAG-urile](../../../translated_images/ro/how-rag-works.f5d0ff63942bd3a6.webp)

Să presupunem că doriți să implementați un chatbot care creează quiz-uri din notițele voastre, veți avea nevoie de o legătură către baza de cunoștințe. Aici intervine RAG. RAG-urile funcționează astfel:

- **Bază de cunoștințe:** Înainte de recuperare, aceste documente trebuie ingestate și preprocesate, tipic prin împărțirea documentelor mari în bucăți mai mici, transformarea lor în embeddings de text și stocarea lor într-o bază de date.

- **Interogarea utilizatorului:** utilizatorul pune o întrebare

- **Recuperare:** Când utilizatorul pune o întrebare, modelul de embedding recuperează informații relevante din baza de cunoștințe pentru a oferi mai mult context care va fi inclus în prompt.

- **Generare augmentată:** LLM-ul își îmbunătățește răspunsul pe baza datelor recuperate. Acest lucru permite ca răspunsul generat să nu fie bazat doar pe datele pre-antrenate, ci și pe informații relevante din contextul adăugat. Datele recuperate sunt folosite pentru a amplifica răspunsurile LLM-ului. Modelul apoi returnează un răspuns la întrebarea utilizatorului.

![desen care arată arhitectura RAG](../../../translated_images/ro/encoder-decode.f2658c25d0eadee2.webp)

Arhitectura pentru RAG-uri este implementată folosind transformatoare care constau din două părți: un encoder și un decoder. De exemplu, când un utilizator pune o întrebare, textul de intrare este „encodat” în vectori care surprind semnificația cuvintelor iar acești vectori sunt „decodați” în indexul nostru de documente și generează text nou bazat pe interogarea utilizatorului. LLM-ul folosește un model encoder-decoder pentru a genera ieșirea.

Două abordări pentru implementarea RAG conform lucrării propuse: [Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sunt:

- **_RAG-Sequence_** folosind documentele recuperate pentru a prezice cel mai bun răspuns posibil la o interogare a utilizatorului

- **RAG-Token** folosind documente pentru a genera următorul token, apoi le recuperează pentru a răspunde la întrebarea utilizatorului

### De ce să folosiți RAG-uri? 

- **Bogăția informațională:** asigură răspunsuri text actualizate și relevante. Astfel, îmbunătățește performanța în sarcini specifice domeniului prin accesarea bazei de cunoștințe interne.

- Reduce fabricarea informațiilor utilizând **date verificabile** din baza de cunoștințe pentru a oferi context întrebărilor utilizatorului.

- Este **cost-eficient** întrucât este mai economic comparativ cu ajustarea fină a unui LLM

## Crearea unei baze de cunoștințe

Aplicația noastră se bazează pe datele noastre personale, adică lecția despre Rețele Neuronale din curriculumul AI pentru Începători.

### Baze de Date Vectoriale

O bază de date vectorială, spre deosebire de bazele de date tradiționale, este o bază de date specializată concepută pentru a stoca, gestiona și căuta vectori încorporați. Aceasta stochează reprezentări numerice ale documentelor. Descompunerea datelor în embeddings numerice facilitează sistemului nostru AI înțelegerea și procesarea datelor.

Stocăm embeddings-urile noastre în baze de date vectoriale deoarece LLM-urile au o limită a numărului de tokeni pe care îi pot primi ca intrare. Deoarece nu puteți trimite toate embeddings-urile unui LLM, va trebui să le împărțim în părți și când un utilizator pune o întrebare, embeddings-urile cele mai asemănătoare întrebării vor fi returnate împreună cu promptul. Împărțirea în bucăți reduce și costurile legate de numărul de tokeni trimiși unui LLM.

Unele baze de date vectoriale populare includ Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant și DeepLake. Puteți crea un model Azure Cosmos DB folosind Azure CLI cu comanda următoare:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Din text către embeddings

Înainte de a stoca datele, trebuie să le convertim în embeddings vectoriale înainte de a fi stocate în bază de date. Dacă lucrați cu documente mari sau texte lungi, le puteți împărți în bucăți pe baza interogărilor pe care le așteptați. Împărțirea în bucăți poate fi realizată la nivel de propoziție sau la nivel de paragraf. Deoarece împărțirea derivă sensul din cuvintele din jur, puteți adăuga context suplimentar unei bucăți, de exemplu, prin adăugarea titlului documentului sau includerea unui text înainte sau după bucata respectivă. Puteți împărți datele astfel:

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

    # Dacă ultimul fragment nu a atins lungimea minimă, adaugă-l oricum
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Odată împărțite, putem apoi să încorporăm textul folosind diferite modele de embedding. Unele modele pe care le puteți folosi includ: word2vec, ada-002 de la OpenAI, Azure Computer Vision și multe altele. Selectarea unui model depinde de limbile folosite, tipul de conținut codificat (text/imagine/audio), dimensiunea intrării pe care o poate codifica și lungimea ieșirii embedding.

Un exemplu de text încorporat folosind modelul OpenAI `text-embedding-ada-002` este:
![o încorporare a cuvântului pisică](../../../translated_images/ro/cat.74cbd7946bc9ca38.webp)

## Recuperare și Căutare Vectorială

Când un utilizator pune o întrebare, sistemul de recuperare o transformă într-un vector folosind encoder-ul de interogare, apoi caută prin indexul nostru de documente vectorii relevanți care sunt legați de intrare. După aceasta, convertește atât vectorul de intrare cât și vectorii documentelor în text și le trece prin LLM.

### Recuperare

Recuperarea are loc când sistemul încearcă să găsească rapid documentele din index care satisfac criteriile de căutare. Scopul sistemului de recuperare este să obțină documente care vor fi folosite pentru a oferi context și a fundamenta LLM-ul pe datele voastre.

Există mai multe moduri de a efectua căutări în baza noastră de date, cum ar fi:

- **Căutare după cuvinte cheie** - folosită pentru căutări textuale

- **Căutare vectorială** - convertește documentele din text în reprezentări vectoriale folosind modele de embedding, permițând o **căutare semantică** bazată pe sensul cuvintelor. Recuperarea se face interogând documentele ale căror reprezentări vectoriale sunt cele mai apropiate de întrebarea utilizatorului.

- **Hibridă** - o combinație între căutarea după cuvinte cheie și căutarea vectorială.

O provocare la recuperare apare când nu există un răspuns similar la interogare în baza de date, sistemul va oferi atunci cea mai bună informație găsită, însă puteți folosi tactici precum setarea distanței maxime pentru relevanță sau folosirea căutării hibride care combină atât cuvintele cheie cât și căutarea vectorială. În această lecție vom folosi căutarea hibridă, o combinație de căutare vectorială și după cuvinte cheie. Vom stoca datele noastre într-un dataframe cu coloane ce conțin bucățile precum și embeddings-urile.

### Similaritate Vectorială

Sistemul de recuperare va căuta în baza de cunoștințe embeddings care sunt apropiate ca semnificație, cel mai apropiat vecin, deoarece sunt texte similare. În scenariu, când un utilizator pune o interogare, aceasta este mai întâi încorporată apoi se potrivește cu embeddings similare. Măsurătorile comune folosite pentru a determina cât de similare sunt vectorii sunt similaritatea cosinus, care se bazează pe unghiul dintre doi vectori.

Putem măsura similitudinea și cu alte alternative, cum ar fi distanța euclidiană, care este linia dreaptă dintre capetele vectorilor, și produsul scalar care măsoară suma produselor elementelor corespunzătoare a doi vectori.

### Index de căutare

Pentru a face recuperarea, trebuie să construim un index de căutare pentru baza noastră de cunoștințe înainte să efectuăm căutarea. Un index va stoca embeddings-urile noastre și poate recupera rapid bucățile cele mai similare chiar și într-o bază de date mare. Putem crea indexul local folosind:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Creează indexul de căutare
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Pentru a interoga indexul, poți folosi metoda kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-rangare

După ce ați interogat baza de date, poate fi necesar să sortați rezultatele în ordinea relevanței. Un LLM de re-rangare utilizează Machine Learning pentru a îmbunătăți relevanța rezultatelor căutării prin ordonarea lor de la cel mai relevant. Folosind Azure AI Search, re-rangarea este făcută automat pentru dvs. folosind un re-ranker semantic. Un exemplu despre cum funcționează re-rangarea folosind cei mai apropiați vecini:

```python
# Găsiți cele mai similare documente
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Afișați cele mai similare documente
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Punând totul cap la cap

Ultimul pas este adăugarea LLM-ului nostru în mix pentru a putea obține răspunsuri fundamentate pe datele noastre. Putem implementa astfel:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convertește întrebarea într-un vector de interogare
    query_vector = create_embeddings(user_input)

    # Găsește cele mai similare documente
    distances, indices = nbrs.kneighbors([query_vector])

    # adaugă documente la interogare pentru a oferi context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combină istoricul și inputul utilizatorului
    history.append(user_input)

    # creează un obiect mesaj
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # folosește API-ul Responses pentru a genera un răspuns
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

### Metrice de evaluare

- Calitatea răspunsurilor furnizate asigurându-se că sună natural, fluent și omenește

- Fundamentarea datelor: evaluarea dacă răspunsul provine din documentele furnizate

- Relevanța: evaluarea dacă răspunsul corespunde și este legat de întrebarea pusă

- Fluența - dacă răspunsul are sens din punct de vedere gramatical

## Cazuri de utilizare pentru RAG (Generarea Augmentată prin Recuperare) și baze de date vectoriale

Există multe cazuri diferite în care apelurile funcțiilor pot îmbunătăți aplicația dvs. precum:

- Întrebări și răspunsuri: fundamentarea datelor companiei pe un chat care poate fi utilizat de angajați pentru a pune întrebări.

- Sisteme de recomandare: unde puteți crea un sistem care potrivește valorile cele mai similare, ex. filme, restaurante și multe altele.

- Servicii chatbot: puteți stoca istoricul conversației și personaliza dialogul pe baza datelor utilizatorului.

- Căutarea imaginilor bazată pe embeddings vectoriale, utilă pentru recunoașterea imaginilor și detectarea anomaliilor.

## Rezumat

Am acoperit zonele fundamentale ale RAG, de la adăugarea datelor în aplicație, la interogarea utilizatorului și ieșire. Pentru a simplifica crearea RAG, puteți folosi framework-uri precum Semantic Kernel, Langchain sau Autogen.

## Tema

Pentru a continua învățarea Generării Augmentate prin Recuperare (RAG), puteți construi:

- Creați o interfață front-end pentru aplicație folosind framework-ul preferat

- Utilizați un framework, fie LangChain fie Semantic Kernel, și recreați aplicația dvs.

Felicitări pentru finalizarea lecției 👏.

## Învățarea nu se oprește aici, continuați călătoria

După finalizarea acestei lecții, consultați colecția noastră [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să vă dezvoltați cunoștințele despre Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->