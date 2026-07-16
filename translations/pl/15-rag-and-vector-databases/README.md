# Retrieval Augmented Generation (RAG) i bazy danych wektorowych

[![Retrieval Augmented Generation (RAG) i bazy danych wektorowych](../../../translated_images/pl/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

W lekcji o aplikacjach wyszukiwania krótko nauczyliśmy się, jak integrować własne dane z dużymi modelami językowymi (LLM). W tej lekcji zagłębimy się w koncepcje osadzenia danych w aplikacji LLM, mechanikę tego procesu oraz metody przechowywania danych, w tym zarówno osadzeń, jak i tekstu.

> **Wideo wkrótce**

## Wprowadzenie

W tej lekcji omówimy następujące zagadnienia:

- Wprowadzenie do RAG, czym jest i dlaczego jest stosowane w AI (sztucznej inteligencji).

- Zrozumienie, czym są bazy danych wektorowych i utworzenie jednej dla naszej aplikacji.

- Praktyczny przykład integracji RAG w aplikacji.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Wyjaśnić znaczenie RAG w wyszukiwaniu i przetwarzaniu danych.

- Skonfigurować aplikację RAG i osadzić swoje dane w LLM

- Skutecznie integrować RAG i bazy danych wektorowych w aplikacjach LLM.

## Nasz scenariusz: wzbogacanie naszych LLM o własne dane

W tej lekcji chcemy dodać własne notatki do startupu edukacyjnego, co pozwoli chatbotowi uzyskać więcej informacji na różne tematy. Korzystając z naszych notatek, uczniowie będą mogli lepiej się uczyć i rozumieć różne zagadnienia, co ułatwi przygotowania do egzaminów. Do stworzenia naszego scenariusza użyjemy:

- `Azure OpenAI:` LLM, którego użyjemy do stworzenia naszego chatbota

- `Lekcja "AI dla początkujących" o sieciach neuronowych`: to będą dane, na których osadzimy nasz LLM

- `Azure AI Search` i `Azure Cosmos DB:` bazy danych wektorowej do przechowywania danych i utworzenia indeksu wyszukiwania

Użytkownicy będą mogli tworzyć quizy do ćwiczeń na podstawie swoich notatek, fiszki do powtórek i podsumowania w zwięzłej formie. Aby zacząć, przyjrzyjmy się czym jest RAG i jak działa:

## Retrieval Augmented Generation (RAG)

Chatbot zasilany LLM przetwarza zapytania użytkowników, aby generować odpowiedzi. Jest zaprojektowany jako interaktywny i angażuje się z użytkownikami na wiele tematów. Jednak jego odpowiedzi są ograniczone do kontekstu dostarczonego i podstawowych danych treningowych. Na przykład, wiedza GPT-4 sięga września 2021, co oznacza brak informacji o wydarzeniach po tej dacie. Ponadto dane użyte do trenowania LLM nie zawierają poufnych informacji takich jak notatki osobiste czy instrukcje produktów firmy.

### Jak działają RAG (Retrieval Augmented Generation)

![rysunek pokazujący działanie RAG](../../../translated_images/pl/how-rag-works.f5d0ff63942bd3a6.webp)

Załóżmy, że chcesz uruchomić chatbota tworzącego quizy z twoich notatek, potrzebujesz połączenia z bazą wiedzy. Tutaj z pomocą przychodzi RAG. RAG działa następująco:

- **Baza wiedzy:** przed wyszukiwaniem dokumenty muszą być załadowane i wstępnie przetworzone, zwykle dzieląc duże dokumenty na mniejsze fragmenty, przekształcając je na osadzenia tekstowe i przechowując je w bazie danych.

- **Zapytanie użytkownika:** użytkownik zadaje pytanie

- **Wyszukiwanie:** gdy użytkownik zadaje pytanie, model osadzający wyszukuje odpowiednie informacje w bazie wiedzy, aby dostarczyć dodatkowy kontekst włączany do promptu.

- **Zwiększona generacja:** LLM ulepsza swoją odpowiedź na podstawie pobranych danych. Pozwala to na generowanie odpowiedzi nie tylko na podstawie danych treningowych, ale także na podstawie istotnych informacji z dodatkowego kontekstu. Pobranie danych służy do rozszerzenia odpowiedzi LLM. Następnie LLM zwraca odpowiedź na pytanie użytkownika.

![rysunek pokazujący architekturę RAG](../../../translated_images/pl/encoder-decode.f2658c25d0eadee2.webp)

Architektura RAG jest implementowana za pomocą transformatorów składających się z dwóch części: enkodera i dekodera. Na przykład, gdy użytkownik zadaje pytanie, tekst wejściowy jest 'kodowany' na wektory odzwierciedlające znaczenie słów, a te wektory są 'dekodowane' w naszym indeksie dokumentów i generują nowy tekst na podstawie zapytania użytkownika. LLM używa modelu enkoder-dekoder do generowania wyjścia.

Dwa podejścia przy implementacji RAG według artykułu: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) to:

- **_RAG-Sequence_** wykorzystujący pobrane dokumenty do przewidywania najlepszej możliwej odpowiedzi na pytanie użytkownika

- **RAG-Token** korzystający z dokumentów do generowania kolejnego tokena, następnie pobierający dokumenty, by odpowiedzieć na pytanie użytkownika

### Dlaczego warto używać RAG?

- **Bogactwo informacji:** zapewnia, że tekstowe odpowiedzi są aktualne i bieżące. Poprawia w ten sposób wydajność w zadaniach specyficznych dla domeny przez dostęp do wewnętrznej bazy wiedzy.

- Redukuje tworzenie fałszywych informacji wykorzystując **weryfikowalne dane** w bazie wiedzy, które dostarczają kontekst zapytaniom użytkowników.

- Jest **opłacalne**, ponieważ jest tańsze niż dostrajanie (fine-tuning) LLM.

## Tworzenie bazy wiedzy

Nasza aplikacja opiera się na naszych osobistych danych, tj. lekcji o sieciach neuronowych z programu „AI dla początkujących”.

### Bazy danych wektorowych

Baza danych wektorowych, w przeciwieństwie do tradycyjnych baz danych, to specjalistyczna baza zaprojektowana do przechowywania, zarządzania i wyszukiwania wektorów osadzonych. Przechowuje numeryczne reprezentacje dokumentów. Podzielenie danych na numeryczne osadzenia ułatwia naszemu systemowi AI zrozumienie i przetworzenie danych.

Przechowujemy nasze osadzenia w bazach danych wektorowych, ponieważ LLM mają limit tokenów, które mogą przyjąć jako wejście. Ponieważ nie można przekazać całych osadzeń do LLM, musimy podzielić je na fragmenty, a gdy użytkownik zada pytanie, zwracane są osadzenia najbardziej podobne do pytania wraz z promptem. Dzielenie na fragmenty również zmniejsza koszty związane z liczbą tokenów przetwarzanych przez LLM.

Popularne bazy danych wektorowych to Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Możesz utworzyć model Azure Cosmos DB używając Azure CLI za pomocą następującego polecenia:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od tekstu do osadzeń

Przed zapisaniem danych musimy przekształcić je na osadzenia wektorowe, zanim zostaną przechowane w bazie danych. Jeśli pracujesz z dużymi dokumentami lub długimi tekstami, możesz dzielić je na fragmenty na podstawie oczekiwanych zapytań. Dzielenie może odbywać się na poziomie zdań lub akapitów. Ponieważ dzielenie wydobywa znaczenia z otaczających słów, możesz dodać trochę kontekstu do fragmentu, np. tytuł dokumentu lub tekst poprzedzający lub następujący po fragmencie. Możesz podzielić dane w następujący sposób:

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

    # Jeśli ostatni fragment nie osiągnął minimalnej długości, dodaj go mimo to
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Po podzieleniu możemy osadzić nasz tekst, używając różnych modeli osadzających. Niektóre modele, które możesz użyć, to: word2vec, ada-002 od OpenAI, Azure Computer Vision i wiele innych. Wybór modelu zależy od języków, które używasz, rodzaju kodowanej zawartości (tekst/obraz/dźwięk), wielkości wejścia, które może zakodować, i długości wyjścia osadzenia.

Przykład osadzonego tekstu z użyciem modelu OpenAI `text-embedding-ada-002` to:
![osadzenie słowa kot](../../../translated_images/pl/cat.74cbd7946bc9ca38.webp)

## Wyszukiwanie i przeszukiwanie wektorowe

Gdy użytkownik zada pytanie, retriever przekształca je na wektor używając enkodera zapytań, następnie przeszukuje nasz indeks dokumentów pod kątem odpowiednich wektorów w dokumentach związanych z zapytaniem. Po znalezieniu zamienia zarówno wektor wejściowy, jak i wektory dokumentów na tekst i przekazuje je do LLM.

### Wyszukiwanie

Wyszukiwanie zachodzi, gdy system próbuje szybko znaleźć dokumenty w indeksie spełniające kryteria wyszukiwania. Celem retrievera jest pozyskanie dokumentów, które będą użyte do dostarczenia kontekstu i osadzenia LLM na twoich danych.

Istnieje kilka metod wykonania wyszukiwania w naszej bazie danych, takich jak:

- **Wyszukiwanie słów kluczowych** - używane do wyszukiwania tekstowego

- **Wyszukiwanie wektorowe** - przekształca dokumenty z tekstu na reprezentacje wektorowe za pomocą modeli osadzeń, zezwalając na **wyszukiwanie semantyczne** oparte na znaczeniu słów. Wyszukiwanie odbywa się przez zapytanie o dokumenty, których reprezentacje wektorowe są najbliższe pytaniu użytkownika.

- **Hybdrydowe** - połączenie wyszukiwania słów kluczowych i wektorowego.

Problemem przy wyszukiwaniu jest sytuacja, gdy w bazie nie ma podobnej odpowiedzi do zapytania, wtedy system zwraca najlepsze dostępne informacje, jednak można stosować strategie, takie jak ustawienie maksymalnej odległości dla relewantności lub użycie wyszukiwania hybrydowego, które łączy słowa kluczowe i wyszukiwanie wektorowe. W tej lekcji użyjemy wyszukiwania hybrydowego, łączącego oba sposoby. Dane przechowamy w dataframe z kolumnami zawierającymi fragmenty i osadzenia.

### Podobieństwo wektorowe

Retriever wyszukuje w bazie wiedzy osadzenia bliskie sobie, czyli najbliższego sąsiada, ponieważ są to podobne teksty. W scenariuszu, gdy użytkownik zadaje pytanie, jest ono najpierw osadzane, a następnie dopasowywane do podobnych osadzeń. Powszechnie stosowaną miarą podobieństwa wektorów jest podobieństwo cosinusowe, oparte na kącie między dwoma wektorami.

Możemy też mierzyć podobieństwo używając innych alternatyw, takich jak odległość Euklidesowa, będąca prostą odcinkiem między końcami wektorów, oraz iloczyn skalarny, który mierzy sumę iloczynów odpowiadających sobie elementów dwóch wektorów.

### Indeks wyszukiwania

Podczas wyszukiwania musimy najpierw zbudować indeks wyszukiwania dla naszej bazy wiedzy. Indeks przechowa nasze osadzenia i szybko wyszuka najbardziej podobne fragmenty nawet w dużej bazie danych. Indeks możemy stworzyć lokalnie używając:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Utwórz indeks wyszukiwania
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Aby zapytać indeks, możesz użyć metody kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponowne sortowanie wyników

Po zapytaniu bazy danych być może będziesz musiał posortować wyniki od najbardziej relewantnych. LLM do ponownego sortowania wykorzystuje uczenie maszynowe, aby poprawić relewantność wyników przez ich uporządkowanie od najbardziej istotnych. Korzystając z Azure AI Search, ponowne sortowanie wykonuje się automatycznie za pomocą semantycznego rerankera. Przykład działania ponownego sortowania z użyciem najbliższych sąsiadów:

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

## Podsumowanie całości

Ostatnim krokiem jest dodanie naszego LLM, aby możliwe było uzyskanie odpowiedzi osadzonych na naszych danych. Możemy to zaimplementować następująco:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Przekonwertuj pytanie na wektor zapytania
    query_vector = create_embeddings(user_input)

    # Znajdź najbardziej podobne dokumenty
    distances, indices = nbrs.kneighbors([query_vector])

    # dodaj dokumenty do zapytania, aby dostarczyć kontekst
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # połącz historię i dane wejściowe użytkownika
    history.append(user_input)

    # utwórz obiekt wiadomości
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # użyj API odpowiedzi do wygenerowania odpowiedzi
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Ocena naszej aplikacji

### Metryki oceny

- Jakość dostarczanych odpowiedzi, zapewniająca naturalne, płynne i ludzkie brzmienie

- Osadzenie danych: ocena, czy odpowiedź pochodzi z dostarczonych dokumentów

- Relewantność: ocena, czy odpowiedź pasuje i jest powiązana z zadanym pytaniem

- Płynność - czy odpowiedź jest gramatycznie poprawna

## Zastosowania RAG (Retrieval Augmented Generation) i baz danych wektorowych

Istnieje wiele zastosowań, gdzie wywołania funkcji mogą poprawić twoją aplikację, takich jak:

- Pytania i odpowiedzi: osadzenie danych firmy w czacie, który mogą używać pracownicy do zadawania pytań.

- Systemy rekomendacji: tworzenie systemu dopasowującego najbardziej podobne wartości, np. filmy, restauracje i wiele innych.

- Usługi chatbotów: możesz przechowywać historię rozmów i personalizować konwersacje na podstawie danych użytkownika.

- Wyszukiwanie obrazów na podstawie osadzeń wektorowych, przydatne w rozpoznawaniu obrazów i wykrywaniu anomalii.

## Podsumowanie

Omówiliśmy podstawowe zagadnienia RAG od dodawania danych do aplikacji, zapytania użytkownika po wyjście. Aby uprościć tworzenie RAG, można użyć frameworków takich jak Semantic Kernel, Langchain lub Autogen.

## Zadanie domowe

Aby kontynuować naukę o Retrieval Augmented Generation (RAG), możesz zbudować:

- Front-end dla aplikacji używając wybranego przez siebie frameworka

- Wykorzystać framework, taki jak LangChain lub Semantic Kernel, i odtworzyć swoją aplikację.

Gratulacje za ukończenie lekcji 👏.

## Nauka się tutaj nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [kolekcję Nauki o AI Generatywnym](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby nadal podnosić swoje umiejętności w generatywnym AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->