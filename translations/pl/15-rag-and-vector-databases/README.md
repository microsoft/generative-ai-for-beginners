<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:13:17+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "pl"
}
-->
# Retrieval Augmented Generation (RAG) i bazy danych wektorowych

[![Retrieval Augmented Generation (RAG) i bazy danych wektorowych](../../../../../translated_images/pl/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

W lekcji o zastosowaniach wyszukiwania krótko omówiliśmy, jak zintegrować własne dane z dużymi modelami językowymi (LLM). W tej lekcji zagłębimy się w koncepcje osadzania danych w aplikacji LLM, mechanikę procesu oraz metody przechowywania danych, obejmujące zarówno osadzenia (embeddings), jak i tekst.

> **Wideo wkrótce**

## Wprowadzenie

W tej lekcji omówimy:

- Wprowadzenie do RAG — czym jest i dlaczego jest stosowane w sztucznej inteligencji (AI).

- Zrozumienie, czym są bazy danych wektorowych i stworzenie takiej dla naszej aplikacji.

- Praktyczny przykład integracji RAG w aplikacji.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wyjaśnić znaczenie RAG w wyszukiwaniu i przetwarzaniu danych.

- Skonfigurować aplikację RAG i osadzić dane w LLM.

- Skutecznie zintegrować RAG oraz bazy danych wektorowych w aplikacjach LLM.

## Nasz scenariusz: wzbogacenie LLM o własne dane

W tej lekcji chcemy dodać własne notatki do startupu edukacyjnego, co pozwoli chatbotowi uzyskać więcej informacji na różne tematy. Korzystając z posiadanych notatek, uczniowie będą mogli lepiej się uczyć i rozumieć różne zagadnienia, co ułatwi im powtórki do egzaminów. Do stworzenia naszego scenariusza wykorzystamy:

- `Azure OpenAI:` LLM, którego użyjemy do stworzenia chatbota

- `Lekcję "AI dla początkujących" o sieciach neuronowych:` to będą dane, na których osadzimy nasz LLM

- `Azure AI Search` i `Azure Cosmos DB:` baza danych wektorowych do przechowywania danych oraz tworzenia indeksu wyszukiwawczego

Użytkownicy będą mogli tworzyć quizy na podstawie notatek, fiszki do powtórek i streszczenia w zwięzłej formie. Zanim zaczniemy, przyjrzyjmy się, czym jest RAG i jak działa:

## Retrieval Augmented Generation (RAG)

Chatbot oparty o LLM przetwarza teksty użytkowników, by generować odpowiedzi. Jest zaprojektowany do interakcji i prowadzenia rozmów na szeroki zakres tematów. Jednak jego odpowiedzi są ograniczone do dostarczonego kontekstu i danych, na których został wytrenowany. Na przykład, GPT-4 ma cutoff wiedzy na wrzesień 2021, co oznacza, że nie zna wydarzeń po tej dacie. Ponadto dane używane do trenowania LLM wykluczają poufne informacje jak notatki osobiste czy instrukcje obsługi firmy.

### Jak działają RAG (Retrieval Augmented Generation)

![rysunek przedstawiający działanie RAG](../../../../../translated_images/pl/how-rag-works.f5d0ff63942bd3a6.webp)

Załóżmy, że chcesz wdrożyć chatbota tworzącego quizy na podstawie twoich notatek; potrzebujesz połączenia z bazą wiedzy. Tu z pomocą przychodzi RAG. RAG działa następująco:

- **Baza wiedzy:** Przed pobraniem, dokumenty muszą zostać wczytane i przetworzone, zwykle dzieląc duże dokumenty na mniejsze fragmenty, konwertując je do osadzeń tekstowych i przechowując w bazie danych.

- **Zapytanie użytkownika:** użytkownik zadaje pytanie

- **Pobieranie (Retrieval):** W momencie zapytania, model osadzający pobiera istotne informacje z bazy wiedzy, aby dostarczyć kontekst, który zostanie dołączony do promptu.

- **Generowanie z uzupełnieniem (Augmented Generation):** LLM ulepsza swoją odpowiedź na podstawie pobranych danych. Pozwala to generować odpowiedzi nie tylko oparte na danych treningowych, ale też na dodanym kontekście. Pobierane dane wzbogacają odpowiedzi LLM, który następnie zwraca odpowiedź na pytanie użytkownika.

![rysunek przedstawiający architekturę RAG](../../../../../translated_images/pl/encoder-decode.f2658c25d0eadee2.webp)

Architektura RAG jest realizowana za pomocą transformatorów, składających się z dwóch części: enkodera i dekodera. Na przykład, gdy użytkownik zadaje pytanie, tekst wejściowy jest "zakodowany" na wektory oddające znaczenie słów, a następnie te wektory są "dekodowane" w indeks dokumentów i generują nowy tekst na podstawie zapytania użytkownika. LLM wykorzystuje model enkoder-dekoder do wygenerowania odpowiedzi.

Dwa podejścia do implementacji RAG według zaproponowanego artykułu: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) to:

- **_RAG-Sequence_** używający pobranych dokumentów do przewidzenia najlepszej możliwej odpowiedzi na zapytanie użytkownika

- **RAG-Token** używający dokumentów do generowania następnego tokenu, po czym ponownie pobierający dokumenty do odpowiedzi na zapytanie użytkownika

### Dlaczego warto używać RAG? 

- **Bogactwo informacji:** zapewnia, że odpowiedzi tekstowe są aktualne i na bieżąco. Poprawia wydajność w zadaniach domenowych, uzyskując dostęp do wewnętrznej bazy wiedzy.

- Ogranicza wymyślanie informacji dzięki wykorzystaniu **weryfikowalnych danych** w bazie wiedzy, by dostarczyć kontekst do zapytań użytkownika.

- Jest **opłacalne**, gdyż jest tańsze niż dostrajanie (fine-tuning) LLM.

## Tworzenie bazy wiedzy

Nasza aplikacja bazuje na naszych osobistych danych, tj. lekcji o sieciach neuronowych z kursu AI dla początkujących.

### Bazy danych wektorowych

Baza danych wektorowych, w przeciwieństwie do tradycyjnych baz, jest specjalistyczną bazą zaprojektowaną do przechowywania, zarządzania i wyszukiwania osadzonych wektorów. Przechowuje numeryczne reprezentacje dokumentów. Rozłożenie danych na osadzenia numeryczne ułatwia systemowi AI zrozumienie i przetwarzanie danych.

Przechowujemy nasze osadzenia w bazach danych wektorowych, ponieważ LLM mają limit tokenów przyjmowanych jako wejście. Nie można przekazać całych osadzeń do LLM, więc trzeba je podzielić na fragmenty, a gdy użytkownik zada pytanie, zwrócone zostaną osadzenia najbardziej odpowiadające pytaniu, razem z promptem. Podział na fragmenty (chunking) także redukuje koszty związane z liczbą tokenów przetwarzanych przez LLM.

Popularne bazy danych wektorowych to Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Model Azure Cosmos DB można utworzyć za pomocą Azure CLI poleceniem:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od tekstu do osadzeń

Zanim przechowamy dane, musimy je konwertować do osadzeń wektorowych przed zapisem w bazie. Pracując z dużymi dokumentami lub długimi tekstami, można je dzielić na fragmenty według przewidywanych zapytań. Podział można robić na poziomie zdania lub akapitu. Ponieważ podział opiera się na znaczeniu słów w ich otoczeniu, można dodać dodatkowy kontekst do fragmentu, np. tytuł dokumentu lub trochę tekstu przed i po fragmencie. Można dzielić dane w ten sposób:

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

    # Jeśli ostatnia część nie osiągnęła minimalnej długości, dodaj ją mimo to
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Po podziale możemy osadzić tekst korzystając z różnych modeli osadzających. Do wyboru są modele takie jak: word2vec, ada-002 od OpenAI, Azure Computer Vision i wiele innych. Wybór modelu zależy od języków, typu kodowanej treści (tekst/obraz/audio), rozmiaru wejścia, które może zakodować oraz długości osadzenia na wyjściu.

Przykład osadzonego tekstu za pomocą modelu OpenAI `text-embedding-ada-002`:

![osadzenie słowa cat](../../../../../translated_images/pl/cat.74cbd7946bc9ca38.webp)

## Wyszukiwanie i wyszukiwanie wektorowe

Gdy użytkownik zada pytanie, pobieracz (retriever) konwertuje je na wektor za pomocą enkodera zapytania, a następnie przeszukuje nasz indeks dokumentów, znajdując wektory powiązane z zapytaniem. Po ukończeniu konwertuje zarówno wektor zapytania, jak i wektory dokumentów na tekst i przesyła go do LLM.

### Pobieranie (Retrieval)

Pobieranie ma miejsce, gdy system szybko próbuje znaleźć dokumenty z indeksu spełniające kryteria wyszukiwania. Celem pobieracza jest uzyskanie dokumentów, które posłużą za kontekst i osadzenie LLM na twoich danych.

Istnieje kilka sposobów wyszukiwania w bazie danych, m.in.:

- **Wyszukiwanie słów kluczowych** – używane do wyszukiwań tekstowych

- **Wyszukiwanie wektorowe** – konwertuje dokumenty z tekstu na reprezentacje wektorowe przy pomocy modeli osadzających, umożliwiając **wyszukiwanie semantyczne** na bazie znaczenia słów. Pobieranie polega na zapytaniu dokumentów, których wektorowe reprezentacje są najbliższe pytaniu użytkownika.

- **Hybrydowe** – połączenie obu metod: wyszukiwania słów kluczowych i wektorowego.

Problem pojawia się, gdy w bazie nie ma podobnej odpowiedzi na zapytanie — system wtedy zwraca najlepszą dostępną informację. Można jednak zastosować taktyki jak ustawienie maksymalnej odległości dla relewantności czy użycie wyszukiwania hybrydowego łączącego słowa kluczowe i wektorowe. W tej lekcji użyjemy wyszukiwania hybrydowego, łączącego obie metody. Dane będziemy przechowywać w dataframe z kolumnami zawierającymi fragmenty oraz osadzenia.

### Podobieństwo wektorów

Pobieracz przeszukuje bazę wiedzy w poszukiwaniu osadzeń blisko położonych, czyli najbliższych sąsiadów, ponieważ mają one podobny tekst. W scenariuszu, gdy użytkownik zadaje zapytanie, najpierw jest ono osadzone, a potem dopasowywane do podobnych osadzeń. Najczęściej stosowaną miarą podobieństwa jest podobieństwo cosinusowe, oparte na kącie między dwoma wektorami.

Alternatywnie można zastosować odległość euklidesową, czyli linię prostą między końcami wektorów, lub iloczyn skalarny, mierzący sumę iloczynów odpowiadających sobie elementów obu wektorów.

### Indeks wyszukiwania

Przed wykonaniem wyszukiwania musimy zbudować indeks wyszukiwania dla naszej bazy wiedzy. Indeks przechowuje osadzenia i pozwala szybko odnajdować najbardziej zbliżone fragmenty nawet w dużej bazie danych. Indeks lokalnie można stworzyć za pomocą:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Utwórz indeks wyszukiwania
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Aby zapytać indeks, możesz użyć metody kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponowne sortowanie wyników (re-ranking)

Po zapytaniu bazy możesz chcieć posortować wyniki od najbardziej relewantnych. Model rerankujący LLM wykorzystuje uczenie maszynowe, by poprawić relewantność wyników, układając je od najlepiej pasujących. W Azure AI Search reranking wykonywany jest automatycznie przez semantyczny re-ranker. Przykład działania rerankingu z użyciem najbliższych sąsiadów:

```python
# Znajdź najbardziej podobne dokumenty
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Wydrukuj najbardziej podobne dokumenty
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Połączenie wszystkiego razem

Ostatnim krokiem jest dodanie naszego LLM, aby uzyskać odpowiedzi osadzone w danych. Możemy to zaimplementować następująco:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Zamień pytanie na wektor zapytania
    query_vector = create_embeddings(user_input)

    # Znajdź najbardziej podobne dokumenty
    distances, indices = nbrs.kneighbors([query_vector])

    # dodaj dokumenty do zapytania, aby zapewnić kontekst
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # połącz historię z danymi od użytkownika
    history.append(user_input)

    # utwórz obiekt wiadomości
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # użyj uzupełniania czatu, aby wygenerować odpowiedź
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Ocena naszej aplikacji

### Metryki oceny

- Jakość odpowiedzi — brzmi naturalnie, płynnie i jak od człowieka

- Osadzenie w danych: ocena, czy odpowiedź pochodzi z dostarczonych dokumentów

- Trafność: ocena, czy odpowiedź odpowiada i jest związana z zadanym pytaniem

- Płynność — czy odpowiedź jest poprawna gramatycznie i sensowna

## Przykłady użycia RAG i baz danych wektorowych

Istnieje wiele przypadków, gdzie wywołania funkcji mogą ulepszyć aplikację, np.:

- Pytania i odpowiedzi: osadzenie danych firmowych w czacie, z którego pracownicy mogą korzystać pytając o informacje.

- Systemy rekomendacji: tworzenie systemów dopasowujących najbardziej podobne wartości, np. filmy, restauracje i inne.

- Usługi chatbotów: przechowywanie historii czatów i personalizacja rozmowy na podstawie danych użytkownika.

- Wyszukiwanie obrazów na bazie osadzeń wektorowych, przydatne w rozpoznawaniu obrazów i wykrywaniu anomalii.

## Podsumowanie

Omówiliśmy podstawowe aspekty RAG: dodanie danych do aplikacji, zapytanie użytkownika oraz generowanie odpowiedzi. Aby uprościć tworzenie RAG, można używać frameworków jak Semantic Kernel, Langchain czy Autogen.

## Zadanie

Aby kontynuować naukę Retrieval Augmented Generation (RAG) możesz:

- Zbudować front-end aplikacji używając wybranego frameworka

- Wykorzystać framework, np. LangChain lub Semantic Kernel, i odtworzyć aplikację.

Gratulacje za ukończenie lekcji 👏.

## Nauka się nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji zapoznaj się z naszą [kolekcją Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę z zakresu generatywnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za źródło nadrzędne. W przypadku informacji o znaczeniu krytycznym zaleca się skorzystanie z profesjonalnego, ludzkiego tłumaczenia. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->