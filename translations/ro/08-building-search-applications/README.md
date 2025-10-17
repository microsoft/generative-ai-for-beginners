<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-17T22:04:41+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "ro"
}
-->
# Construirea unei aplicații de căutare

[![Introducere în AI Generativ și Modele de Limbaj Extinse](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.ro.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții_

Modelele de limbaj extinse (LLMs) nu se limitează doar la chatbot-uri și generarea de text. Este posibil să construim aplicații de căutare utilizând Embeddings. Embeddings sunt reprezentări numerice ale datelor, cunoscute și sub denumirea de vectori, și pot fi utilizate pentru căutarea semantică a datelor.

În această lecție, veți construi o aplicație de căutare pentru startup-ul nostru educațional. Startup-ul nostru este o organizație non-profit care oferă educație gratuită studenților din țările în curs de dezvoltare. Avem un număr mare de videoclipuri pe YouTube pe care studenții le pot folosi pentru a învăța despre AI. Startup-ul nostru dorește să construiască o aplicație de căutare care să permită studenților să caute un videoclip pe YouTube introducând o întrebare.

De exemplu, un student ar putea scrie „Ce sunt Jupyter Notebooks?” sau „Ce este Azure ML?” iar aplicația de căutare va returna o listă de videoclipuri relevante pentru întrebare și, mai mult, aplicația de căutare va returna un link către locul din videoclip unde se află răspunsul la întrebare.

## Introducere

În această lecție, vom aborda:

- Căutarea semantică vs. căutarea pe bază de cuvinte cheie.
- Ce sunt Text Embeddings.
- Crearea unui Index de Text Embeddings.
- Căutarea într-un Index de Text Embeddings.

## Obiective de învățare

După finalizarea acestei lecții, veți putea:

- Să faceți diferența între căutarea semantică și cea pe bază de cuvinte cheie.
- Să explicați ce sunt Text Embeddings.
- Să creați o aplicație utilizând Embeddings pentru a căuta date.

## De ce să construim o aplicație de căutare?

Crearea unei aplicații de căutare vă va ajuta să înțelegeți cum să utilizați Embeddings pentru a căuta date. De asemenea, veți învăța cum să construiți o aplicație de căutare care poate fi utilizată de studenți pentru a găsi rapid informații.

Lecția include un Index de Embeddings al transcrierilor de pe YouTube pentru canalul [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) de la Microsoft. AI Show este un canal de YouTube care vă învață despre AI și machine learning. Indexul de Embeddings conține Embeddings pentru fiecare dintre transcrierile de pe YouTube până în octombrie 2023. Veți folosi acest Index de Embeddings pentru a construi o aplicație de căutare pentru startup-ul nostru. Aplicația de căutare returnează un link către locul din videoclip unde se află răspunsul la întrebare. Acesta este un mod excelent pentru ca studenții să găsească rapid informațiile de care au nevoie.

Următorul este un exemplu de interogare semantică pentru întrebarea „poți folosi rstudio cu azure ml?”. Verificați URL-ul YouTube, veți vedea că URL-ul conține un timestamp care vă duce la locul din videoclip unde se află răspunsul la întrebare.

![Interogare semantică pentru întrebarea "poți folosi rstudio cu Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.ro.png)

## Ce este căutarea semantică?

Acum probabil vă întrebați, ce este căutarea semantică? Căutarea semantică este o tehnică de căutare care utilizează semantica sau sensul cuvintelor dintr-o interogare pentru a returna rezultate relevante.

Iată un exemplu de căutare semantică. Să presupunem că doriți să cumpărați o mașină, ați putea căuta „mașina visurilor mele”. Căutarea semantică înțelege că nu „visați” la o mașină, ci căutați să cumpărați mașina „ideală”. Căutarea semantică înțelege intenția dvs. și returnează rezultate relevante. Alternativa este „căutarea pe bază de cuvinte cheie”, care ar căuta literal vise despre mașini și ar returna adesea rezultate irelevante.

## Ce sunt Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) sunt o tehnică de reprezentare a textului utilizată în [procesarea limbajului natural](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Text embeddings sunt reprezentări numerice semantice ale textului. Embeddings sunt utilizate pentru a reprezenta datele într-un mod ușor de înțeles de către o mașină. Există multe modele pentru construirea de text embeddings, iar în această lecție ne vom concentra pe generarea de embeddings utilizând Modelul de Embedding OpenAI.

Iată un exemplu, imaginați-vă că următorul text se află într-o transcriere dintr-unul dintre episoadele de pe canalul AI Show de pe YouTube:

```text
Today we are going to learn about Azure Machine Learning.
```

Vom transmite textul către API-ul OpenAI Embedding și acesta va returna următorul embedding format din 1536 de numere, adică un vector. Fiecare număr din vector reprezintă un aspect diferit al textului. Pentru concizie, iată primele 10 numere din vector.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Cum se creează Indexul de Embeddings?

Indexul de Embeddings pentru această lecție a fost creat cu o serie de scripturi Python. Veți găsi scripturile împreună cu instrucțiunile în [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) din folderul 'scripts' al acestei lecții. Nu este necesar să rulați aceste scripturi pentru a finaliza lecția, deoarece Indexul de Embeddings este deja furnizat.

Scripturile efectuează următoarele operațiuni:

1. Transcrierea fiecărui videoclip de pe YouTube din playlist-ul [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) este descărcată.
2. Utilizând [Funcțiile OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), se încearcă extragerea numelui vorbitorului din primele 3 minute ale transcrierii de pe YouTube. Numele vorbitorului pentru fiecare videoclip este stocat în Indexul de Embeddings numit `embedding_index_3m.json`.
3. Textul transcrierii este apoi împărțit în **segmente de text de 3 minute**. Segmentul include aproximativ 20 de cuvinte suprapuse din segmentul următor pentru a se asigura că Embedding-ul segmentului nu este întrerupt și pentru a oferi un context mai bun de căutare.
4. Fiecare segment de text este apoi transmis către API-ul OpenAI Chat pentru a rezuma textul în 60 de cuvinte. Rezumatul este, de asemenea, stocat în Indexul de Embeddings `embedding_index_3m.json`.
5. În cele din urmă, textul segmentului este transmis către API-ul OpenAI Embedding. API-ul Embedding returnează un vector de 1536 de numere care reprezintă semnificația semantică a segmentului. Segmentul împreună cu vectorul OpenAI Embedding este stocat într-un Index de Embeddings `embedding_index_3m.json`.

### Baze de date vectoriale

Pentru simplitatea lecției, Indexul de Embeddings este stocat într-un fișier JSON numit `embedding_index_3m.json` și încărcat într-un Pandas DataFrame. Totuși, în producție, Indexul de Embeddings ar fi stocat într-o bază de date vectorială, cum ar fi [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), printre altele.

## Înțelegerea similarității cosinusului

Am învățat despre text embeddings, următorul pas este să învățăm cum să folosim text embeddings pentru a căuta date și, în special, pentru a găsi cele mai similare embeddings cu o interogare dată utilizând similaritatea cosinusului.

### Ce este similaritatea cosinusului?

Similaritatea cosinusului este o măsură a similarității între doi vectori, cunoscută și sub denumirea de `căutare a celui mai apropiat vecin`. Pentru a efectua o căutare bazată pe similaritatea cosinusului, trebuie să _vectorizați_ textul interogării utilizând API-ul OpenAI Embedding. Apoi calculați _similaritatea cosinusului_ între vectorul interogării și fiecare vector din Indexul de Embeddings. Amintiți-vă, Indexul de Embeddings are un vector pentru fiecare segment de text al transcrierii de pe YouTube. În cele din urmă, sortați rezultatele după similaritatea cosinusului, iar segmentele de text cu cea mai mare similaritate cosinus sunt cele mai asemănătoare cu interogarea.

Din punct de vedere matematic, similaritatea cosinusului măsoară cosinusul unghiului dintre doi vectori proiectați într-un spațiu multidimensional. Această măsurătoare este benefică, deoarece dacă două documente sunt departe unul de celălalt în funcție de distanța euclidiană din cauza dimensiunii, ele ar putea totuși să aibă un unghi mai mic între ele și, prin urmare, o similaritate cosinus mai mare. Pentru mai multe informații despre ecuațiile de similaritate cosinus, consultați [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Construirea primei aplicații de căutare

În continuare, vom învăța cum să construim o aplicație de căutare utilizând Embeddings. Aplicația de căutare va permite studenților să caute un videoclip introducând o întrebare. Aplicația de căutare va returna o listă de videoclipuri relevante pentru întrebare. De asemenea, aplicația de căutare va returna un link către locul din videoclip unde se află răspunsul la întrebare.

Această soluție a fost construită și testată pe Windows 11, macOS și Ubuntu 22.04 utilizând Python 3.10 sau o versiune ulterioară. Puteți descărca Python de pe [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Temă - construirea unei aplicații de căutare pentru a ajuta studenții

Am introdus startup-ul nostru la începutul acestei lecții. Acum este momentul să îi ajutăm pe studenți să construiască o aplicație de căutare pentru evaluările lor.

În această temă, veți crea Serviciile Azure OpenAI care vor fi utilizate pentru a construi aplicația de căutare. Veți crea următoarele Servicii Azure OpenAI. Veți avea nevoie de un abonament Azure pentru a finaliza această temă.

### Porniți Azure Cloud Shell

1. Autentificați-vă în [portalul Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Selectați pictograma Cloud Shell din colțul din dreapta sus al portalului Azure.
3. Selectați **Bash** pentru tipul de mediu.

#### Creați un grup de resurse

> Pentru aceste instrucțiuni, folosim grupul de resurse numit "semantic-video-search" în East US.
> Puteți schimba numele grupului de resurse, dar când schimbați locația resurselor,
> verificați [tabelul de disponibilitate al modelelor](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Creați o resursă Azure OpenAI Service

Din Azure Cloud Shell, rulați următoarea comandă pentru a crea o resursă Azure OpenAI Service.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Obțineți endpoint-ul și cheile pentru utilizare în această aplicație

Din Azure Cloud Shell, rulați următoarele comenzi pentru a obține endpoint-ul și cheile pentru resursa Azure OpenAI Service.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Implementați modelul OpenAI Embedding

Din Azure Cloud Shell, rulați următoarea comandă pentru a implementa modelul OpenAI Embedding.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Soluție

Deschideți [notebook-ul soluției](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) în GitHub Codespaces și urmați instrucțiunile din Jupyter Notebook.

Când rulați notebook-ul, vi se va solicita să introduceți o interogare. Caseta de introducere va arăta astfel:

![Caseta de introducere pentru utilizator pentru a introduce o interogare](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.ro.png)

## Felicitări! Continuați să învățați

După ce ați finalizat această lecție, consultați [colecția noastră de învățare despre AI generativ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să vă dezvoltați cunoștințele despre AI generativ!

Mergeți la Lecția 9, unde vom analiza cum să [construim aplicații de generare de imagini](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.