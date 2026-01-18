<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T19:05:39+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "ro"
}
-->
# Generarea augmentată prin recuperare (RAG) și bazele de date vectoriale

[![Generarea augmentată prin recuperare (RAG) și bazele de date vectoriale](../../../../../translated_images/ro/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

În lecția despre aplicațiile de căutare, am învățat pe scurt cum să integrezi propriile date în modelele de limbaj mari (LLM). În această lecție, vom aprofunda conceptele de fundamentare a datelor în aplicația ta LLM, mecanica procesului și metodele de stocare a datelor, inclusiv atât încorporările, cât și textul.

> **Video în curând**

## Introducere

În această lecție vom acoperi următoarele:

- O introducere în RAG, ce este și de ce este folosit în AI (inteligența artificială).

- Înțelegerea a ceea ce sunt bazele de date vectoriale și crearea uneia pentru aplicația noastră.

- Un exemplu practic despre cum să integrăm RAG într-o aplicație.

## Obiectivele de învățare

După ce vei termina această lecție, vei putea:

- Explica importanța RAG în recuperarea și procesarea datelor.

- Configura o aplicație RAG și să îți fundamentezi datele pe un LLM.

- Integrarea eficientă a RAG și bazelor de date vectoriale în aplicațiile LLM.

## Scenariul nostru: îmbunătățirea LLM-urilor cu datele noastre

Pentru această lecție, vrem să adăugăm propriile noastre notițe în startup-ul educațional, care permite chatbot-ului să obțină mai multe informații despre diferite subiecte. Folosind notițele pe care le avem, cursanții vor putea studia mai bine și înțelege diferitele teme, făcând mai ușoară revizuirea pentru examene. Pentru a crea scenariul nostru, vom folosi:

- `Azure OpenAI:` LLM-ul pe care îl vom folosi pentru a crea chatbot-ul

- `Lecția AI pentru începători despre rețele neuronale:` acestea vor fi datele pe care ne vom fundamenta LLM-ul

- `Azure AI Search` și `Azure Cosmos DB:` baza de date vectorială pentru a stoca datele și a crea un index de căutare

Utilizatorii vor putea crea teste practice din notițele lor, carduri de revizuire și rezuma aceste notițe în sinteze concise. Pentru a începe, să vedem ce este RAG și cum funcționează:

## Generarea augmentată prin recuperare (RAG)

Un chatbot alimentat de un LLM procesează solicitările utilizatorului pentru a genera răspunsuri. Este conceput să fie interactiv și să interacționeze cu utilizatorii pe o gamă largă de subiecte. Totuși, răspunsurile sale sunt limitate la contextul furnizat și la datele de antrenament fundamentale. De exemplu, limita de cunoștințe a GPT-4 este septembrie 2021, ceea ce înseamnă că nu are cunoștințe despre evenimentele care au avut loc după această dată. În plus, datele folosite pentru antrenarea LLM-urilor exclud informații confidențiale, cum ar fi notițele personale sau manualul de produs al unei companii.

### Cum funcționează RAG-urile (Generarea augmentată prin recuperare)

![drawing showing how RAGs work](../../../../../translated_images/ro/how-rag-works.f5d0ff63942bd3a6.webp)

Să presupunem că dorești să implementezi un chatbot care creează teste din notițele tale, vei avea nevoie de o conexiune la baza de cunoștințe. Aici intervine RAG. RAG-urile funcționează astfel:

- **Baza de cunoștințe:** Înainte de recuperare, aceste documente trebuie ingerate și preprocesate, de obicei prin fragmentarea documentelor mari în bucăți mai mici, transformarea lor în încorporări textuale și stocarea lor într-o bază de date.

- **Întrebarea utilizatorului:** utilizatorul pune o întrebare

- **Recuperare:** când utilizatorul pune o întrebare, modelul de încorporare recuperează informațiile relevante din baza de cunoștințe pentru a oferi mai mult context care va fi încorporat în prompt.

- **Generare augmentată:** LLM-ul își îmbunătățește răspunsul pe baza datelor recuperate. Acest lucru permite ca răspunsul generat să nu fie bazat doar pe datele pre-antrenate, ci și pe informații relevante din contextul adăugat. Datele recuperate sunt folosite pentru a augmenta răspunsurile LLM-ului. LLM-ul oferă apoi un răspuns întrebării utilizatorului.

![drawing showing how RAGs architecture](../../../../../translated_images/ro/encoder-decode.f2658c25d0eadee2.webp)

Arhitectura RAG-urilor este implementată folosind transformatoare compuse din două părți: un encoder și un decoder. De exemplu, când un utilizator pune o întrebare, textul de intrare este „encodat” în vectori care surprind semnificația cuvintelor, iar vectorii sunt „decodați” în indexul nostru de documente și generează text nou bazat pe întrebarea utilizatorului. LLM-ul folosește un model encoder-decoder pentru a genera ieșirea.

Două abordări în implementarea RAG conform lucrării propuse: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) sunt:

- **_RAG-Sequence_** folosește documentele recuperate pentru a prezice cel mai bun răspuns posibil la o întrebare a utilizatorului

- **RAG-Token** folosește documentele pentru a genera următorul token, apoi le recuperează pentru a răspunde la întrebarea utilizatorului

### De ce să folosești RAG-uri? 

- **Bogăția informațiilor:** garantează că răspunsurile text sunt actualizate și curente. Astfel, îmbunătățește performanța pe sarcini specifice domeniului prin accesarea bazei interne de cunoștințe.

- Reduce fabricarea de informații prin utilizarea de **date verificabile** în baza de cunoștințe pentru a oferi context întrebărilor utilizatorului.

- Este **rentabil** deoarece sunt mai economice comparativ cu ajustarea fină a unui LLM

## Crearea unei baze de cunoștințe

Aplicația noastră este bazată pe datele personale, adică lecția despre Rețeaua Neuronală din curriculum-ul AI pentru Începători.

### Bazele de date vectoriale

O bază de date vectorială, spre deosebire de bazele de date tradiționale, este o bază de date specializată creată pentru a stoca, gestiona și căuta vectori încorporați. Aceasta stochează reprezentări numerice ale documentelor. Fragmentarea datelor în reprezentări numerice face mai ușoară înțelegerea și procesarea datelor de către sistemul AI.

Stocăm încorporările noastre în bazele de date vectoriale deoarece LLM-urile au o limită privind numărul de tokeni pe care îi acceptă ca intrare. Deoarece nu poți trimite toate încorporările unui LLM, trebuie să le împărțim în bucăți, iar când un utilizator pune o întrebare, sunt returnate încorporările cele mai apropiate de întrebare împreună cu promptul. Fragmentarea reduce și costurile legate de numărul de tokeni trimiși prin LLM.

Unele baze de date vectoriale populare includ Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant și DeepLake. Poți crea un model Azure Cosmos DB folosind Azure CLI cu următoarea comandă:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Din text în încorporări

Înainte să stocăm datele, trebuie să le convertim în încorporări vectoriale înainte de a fi depozitate în baza de date. Dacă lucrezi cu documente mari sau texte lungi, le poți fragmenta în funcție de întrebările pe care le aștepți. Fragmentarea se poate face la nivel de propoziție sau de paragraf. Deoarece fragmentarea derivă sensuri din cuvintele din jur, poți adăuga context suplimentar la o bucată, de exemplu, adăugând titlul documentului sau includerea unor texte înainte sau după fragment. Poți fragmenta datele astfel:

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

    # Dacă ultima bucată nu a atins lungimea minimă, adaugă-o oricum
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Odată fragmentate, putem încorpora textul folosind diferite modele de încorporare. Unele modele pe care le poți folosi includ: word2vec, ada-002 de la OpenAI, Azure Computer Vision și multe altele. Alegerea modelului depinde de limbile folosite, tipul de conținut codificat (text/imagine/audio), dimensiunea intrării pe care o poate codifica și lungimea ieșirii din încorporare.

Un exemplu de text încorporat folosind modelul `text-embedding-ada-002` de la OpenAI este:
![an embedding of the word cat](../../../../../translated_images/ro/cat.74cbd7946bc9ca38.webp)

## Recuperare și căutare vectorială

Când un utilizator pune o întrebare, sistemul de recuperare o transformă într-un vector folosind codificatorul de interogare, apoi caută în indexul nostru de documente vectori relevanți din document legate de intrare. După aceea, convertește vectorii de intrare și vectorii documentelor în text și îl transmite prin LLM.

### Recuperare

Recuperarea are loc când sistemul încearcă să găsească rapid documentele din index care corespund criteriilor de căutare. Scopul recuperatorului este să obțină documente care vor fi folosite pentru a oferi context și a fundamenta LLM-ul pe datele tale.

Există mai multe moduri de a efectua căutarea în baza noastră de date, cum ar fi:

- **Căutare după cuvinte-cheie** - folosită pentru căutări textuale

- **Căutare vectorială** - convertește documentele din text în reprezentări vectoriale folosind modele de încorporare, permițând o **căutare semantică** bazată pe semnificația cuvintelor. Recuperarea se face prin interogarea documentelor ale căror reprezentări vectoriale sunt cele mai apropiate de întrebarea utilizatorului.

- **Hibridă** - combinație între căutarea după cuvinte-cheie și căutarea vectorială.

O provocare la recuperare apare atunci când nu există un răspuns similar în baza de date, sistemul va returna atunci cea mai bună informație pe care o poate obține, însă poți folosi tactici precum stabilirea distanței maxime pentru relevanță sau utilizarea căutării hibride care combină atât cuvinte-cheie cât și vectori. În această lecție vom folosi căutarea hibridă, o combinație între căutarea vectorială și cea după cuvinte-cheie. Vom stoca datele într-un dataframe cu coloane ce conțin bucățile, precum și încorporările.

### Similaritatea vectorială

Recuperatorul va căuta în baza de cunoștințe pentru încorporări care sunt apropiate unele de altele, cel mai apropiat vecin, deoarece sunt texte similare. În scenariu, când un utilizator pune o întrebare, aceasta este mai întâi încorporată și apoi comparată cu încorporări similare. Măsura comună folosită pentru a determina cât de similare sunt vectorii diferiți este similaritatea cosinus, bazată pe unghiul dintre doi vectori.

Putem măsura similitudinea și cu alte alternative, cum ar fi distanța euclidiană, care este linia dreaptă dintre capetele vectorilor, și produsul scalar care măsoară suma produselor elementelor corespunzătoare a doi vectori.

### Indexul de căutare

Pentru a face recuperare, trebuie să construim un index de căutare pentru baza noastră de cunoștințe înainte de a efectua căutarea. Un index va stoca încorporările și poate recupera rapid cele mai similare bucăți chiar și într-o bază de date mare. Putem crea indexul local folosind:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Creează indexul de căutare
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Pentru a interoga indexul, poți folosi metoda kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-rangarea

Odată ce ai interogat baza de date, poate fi necesar să sortezi rezultatele în ordinea relevanței. Un LLM de rerangare utilizează învățarea automată pentru a îmbunătăți relevanța rezultatelor căutării prin ordonarea lor de la cele mai relevante. Folosind Azure AI Search, rerangarea se face automat pentru tine folosind un reranker semantic. Un exemplu despre cum funcționează rerangarea folosind cei mai apropiați vecini:

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

Ultimul pas este să adăugăm LLM-ul în ecuație pentru a putea obține răspunsuri fundamentate pe datele noastre. Putem implementa acest lucru astfel:

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

    # folosește completarea chatului pentru a genera un răspuns
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Evaluarea aplicației noastre

### Metrici de evaluare

- Calitatea răspunsurilor furnizate, asigurându-se că sună natural, fluent și asemănător cu un om

- Fundamentarea datelor: evaluarea dacă răspunsul provine din documentele furnizate

- Relevanță: evaluarea dacă răspunsul corespunde și este legat de întrebarea pusă

- Fluență - dacă răspunsul are sens din punct de vedere gramatical

## Cazuri de utilizare pentru folosirea RAG (Generarea augmentată prin recuperare) și bazelor de date vectoriale

Există multe cazuri diferite în care apelurile de funcții pot îmbunătăți aplicația ta, cum ar fi:

- Întrebări și răspunsuri: fundamentarea datelor companiei tale într-un chat ce poate fi folosit de angajați pentru a pune întrebări.

- Sisteme de recomandare: unde poți crea un sistem care potrivește cele mai similare valori, ex. filme, restaurante și multe altele.

- Servicii chatbot: poți stoca istoricul conversațiilor și personaliza conversația bazat pe datele utilizatorului.

- Căutare imagine bazată pe încorporări vectoriale, utilă pentru recunoașterea imaginilor și detectarea anomaliilor.

## Rezumat

Am acoperit ariile fundamentale ale RAG de la adăugarea datelor în aplicație, interogarea utilizatorului până la ieșire. Pentru a simplifica crearea RAG, poți folosi cadre de lucru precum Semantic Kernel, Langchain sau Autogen.

## Tema

Pentru a continua învățarea despre Generarea augmentată prin recuperare (RAG), poți construi:

- Un front-end pentru aplicație folosind cadrul de lucru preferat

- Folosește un framework, fie LangChain fie Semantic Kernel, și recreează aplicația ta.

Felicitări pentru terminarea lecției 👏.

## Învățarea nu se oprește aici, continuă călătoria

După ce ai terminat această lecție, aruncă o privire la colecția noastră [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți crești cunoștințele despre AI Generativ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->