# Retrieval Augmented Generation (RAG) i Bazy Danych Wektorowe

[![Retrieval Augmented Generation (RAG) i Bazy Danych Wektorowe](../../images/15-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

W lekcji dotyczącej aplikacji wyszukiwania krótko nauczyliśmy się, jak integrować własne dane z Dużymi Modelami Językowymi (LLM). W tej lekcji zagłębimy się w koncepcje osadzania danych w aplikacji LLM, mechanizmy tego procesu oraz metody przechowywania danych, w tym zarówno embeddingów, jak i tekstu.

> **Wideo wkrótce**

## Wprowadzenie

W tej lekcji omówimy następujące zagadnienia:

- Wprowadzenie do RAG, czym jest i dlaczego jest używane w AI (sztucznej inteligencji).

- Zrozumienie, czym są bazy danych wektorowe i stworzenie jednej dla naszej aplikacji.

- Praktyczny przykład integracji RAG w aplikacji.

## Cele Nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Wyjaśnić znaczenie RAG w odzyskiwaniu i przetwarzaniu danych.

- Skonfigurować aplikację RAG i osadzić dane w LLM.

- Efektywnie integrować RAG i Bazy Danych Wektorowe w Aplikacjach LLM.

## Nasz Scenariusz: wzbogacanie naszych LLM o własne dane

W tej lekcji chcemy dodać własne notatki do startupu edukacyjnego, co pozwoli chatbotowi uzyskać więcej informacji na różne tematy. Korzystając z naszych notatek, uczniowie będą mogli lepiej się uczyć i rozumieć różne tematy, co ułatwi powtórki do egzaminów. Aby stworzyć nasz scenariusz, użyjemy:

- `Azure OpenAI:` LLM, którego użyjemy do stworzenia naszego chatbota

- `Lekcja AI dla początkujących o Sieciach Neuronowych:` to będą dane, na których osadzimy nasz LLM

- `Azure AI Search` i `Azure Cosmos DB:` baza danych wektorowa do przechowywania naszych danych i tworzenia indeksu wyszukiwania

Użytkownicy będą mogli tworzyć quizy z własnych notatek, fiszki do powtórek i podsumowywać je do zwięzłych przeglądów. Aby zacząć, przyjrzyjmy się, czym jest RAG i jak działa:

## Retrieval Augmented Generation (RAG)

Chatbot zasilany przez LLM przetwarza prompty użytkownika, aby generować odpowiedzi. Jest zaprojektowany tak, aby był interaktywny i angażował użytkowników w szeroki zakres tematów. Jednak jego odpowiedzi są ograniczone do dostarczonego kontekstu i danych treningowych. Na przykład, wiedza GPT-4 kończy się we wrześniu 2021 roku, co oznacza, że brakuje mu wiedzy o wydarzeniach, które miały miejsce po tym okresie. Ponadto, dane użyte do treningu LLM wykluczają informacje poufne, takie jak osobiste notatki czy podręcznik produktu firmy.

### Jak działają RAG (Retrieval Augmented Generation)

![rysunek pokazujący jak działają RAG](../../images/how-rag-works.png?WT.mc_id=academic-105485-koreyst)

Załóżmy, że chcesz wdrożyć chatbota, który tworzy quizy z Twoich notatek, będziesz potrzebować połączenia z bazą wiedzy. Tutaj z pomocą przychodzi RAG. RAG działają w następujący sposób:

- **Baza wiedzy:** Przed odzyskiwaniem te dokumenty muszą zostać przetworzone i przetworzone wstępnie, zazwyczaj dzieląc duże dokumenty na mniejsze części, przekształcając je w embeddingi tekstowe i przechowując je w bazie danych.

- **Zapytanie użytkownika:** użytkownik zadaje pytanie

- **Odzyskiwanie:** Gdy użytkownik zadaje pytanie, model embeddingu pobiera istotne informacje z naszej bazy wiedzy, aby zapewnić więcej kontekstu, który zostanie włączony do promptu.

- **Generowanie wzbogacone:** LLM wzbogaca swoją odpowiedź na podstawie pobranych danych. Pozwala to na generowanie odpowiedzi nie tylko na podstawie wstępnie wytrenowanych danych, ale także istotnych informacji z dodanego kontekstu. Pobrane dane są używane do wzbogacania odpowiedzi LLM. Następnie LLM zwraca odpowiedź na pytanie użytkownika.

![rysunek pokazujący architekturę RAG](../../images/encoder-decode.png?WT.mc_id=academic-105485-koreyst)

Architektura RAG jest implementowana przy użyciu transformatorów składających się z dwóch części: kodera i dekodera. Na przykład, gdy użytkownik zadaje pytanie, tekst wejściowy jest „kodowany” w wektory przechwytujące znaczenie słów, a wektory są „dekodowane” w naszym indeksie dokumentów i generują nowy tekst na podstawie zapytania użytkownika. LLM używa zarówno modelu koder-dekoder do generowania wyniku.

Dwa podejścia przy wdrażaniu RAG zgodnie z proponowanym artykułem: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) to:

- **_RAG-Sequence_** używanie pobranych dokumentów do przewidywania najlepszej możliwej odpowiedzi na zapytanie użytkownika

- **RAG-Token** używanie dokumentów do generowania następnego tokena, a następnie pobieranie ich w celu odpowiedzi na zapytanie użytkownika

### Dlaczego warto używać RAG?

- **Bogactwo informacji:** zapewnia, że odpowiedzi tekstowe są aktualne. W związku z tym zwiększa wydajność w zadaniach specyficznych dla domeny poprzez dostęp do wewnętrznej bazy wiedzy.

- Zmniejsza fabrykację poprzez wykorzystanie **weryfikowalnych danych** w bazie wiedzy do zapewnienia kontekstu dla zapytań użytkowników.

- Jest **opłacalny**, ponieważ jest bardziej ekonomiczny w porównaniu do dostrajania LLM

## Tworzenie bazy wiedzy

Nasza aplikacja opiera się na naszych danych osobowych, tj. lekcji Sieci Neuronowych z programu AI Dla Początkujących.

### Bazy Danych Wektorowe

Baza danych wektorowa, w przeciwieństwie do tradycyjnych baz danych, jest specjalistyczną bazą danych zaprojektowaną do przechowywania, zarządzania i przeszukiwania osadzonych wektorów. Przechowuje numeryczne reprezentacje dokumentów. Podział danych na numeryczne embeddingi ułatwia naszemu systemowi AI zrozumienie i przetwarzanie danych.

Przechowujemy nasze embeddingi w bazach danych wektorowych, ponieważ LLM mają limit liczby tokenów, które akceptują jako dane wejściowe. Ponieważ nie można przekazać całych embeddingów do LLM, będziemy musieli podzielić je na fragmenty, a gdy użytkownik zada pytanie, embeddingi najbardziej podobne do pytania zostaną zwrócone wraz z promptem. Podział na fragmenty zmniejsza również koszty związane z liczbą tokenów przekazywanych przez LLM.

Niektóre popularne bazy danych wektorowe to Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Możesz utworzyć model Azure Cosmos DB za pomocą Azure CLI za pomocą następującego polecenia:

```bash
az login
az group create -n <nazwa-grupy-zasobów> -l <lokalizacja>
az cosmosdb create -n <nazwa-cosmos-db> -r <nazwa-grupy-zasobów>
az cosmosdb list-keys -n <nazwa-cosmos-db> -g <nazwa-grupy-zasobów>
```

### Od tekstu do embeddingów

Zanim zapiszemy nasze dane, będziemy musieli przekonwertować je na embeddingi wektorowe, zanim zostaną zapisane w bazie danych. Jeśli pracujesz z dużymi dokumentami lub długimi tekstami, możesz je podzielić na fragmenty w oparciu o oczekiwane zapytania. Podział na fragmenty można wykonać na poziomie zdania lub akapitu. Ponieważ podział na fragmenty czerpie znaczenie ze słów wokół nich, możesz dodać inny kontekst do fragmentu, na przykład dodając tytuł dokumentu lub dołączając tekst przed lub po fragmencie. Możesz podzielić dane w następujący sposób:

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

    # Jeśli ostatni fragment nie osiągnął minimalnej długości, dodaj go mimo wszystko
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Po podziale na fragmenty możemy następnie osadzić nasz tekst za pomocą różnych modeli embeddingu. Niektóre modele, których możesz użyć, to: word2vec, ada-002 firmy OpenAI, Azure Computer Vision i wiele innych. Wybór modelu do użycia będzie zależał od języków, których używasz, rodzaju kodowanej treści (tekst/obrazy/audio), rozmiaru danych wejściowych, które może zakodować i długości wyniku embeddingu.

Przykład osadzonego tekstu przy użyciu modelu `text-embedding-ada-002` firmy OpenAI:
![embedding słowa kot](../../images/cat.png?WT.mc_id=academic-105485-koreyst)

## Odzyskiwanie i Wyszukiwanie Wektorowe

Gdy użytkownik zadaje pytanie, retriever przekształca je w wektor za pomocą kodera zapytań, a następnie przeszukuje nasz indeks wyszukiwania dokumentów w poszukiwaniu odpowiednich wektorów w dokumencie, które są powiązane z danymi wejściowymi. Po zakończeniu konwertuje zarówno wektor wejściowy, jak i wektory dokumentów na tekst i przekazuje je do LLM.

### Odzyskiwanie

Odzyskiwanie ma miejsce, gdy system próbuje szybko znaleźć dokumenty z indeksu, które spełniają kryteria wyszukiwania. Celem retrievera jest uzyskanie dokumentów, które zostaną wykorzystane do zapewnienia kontekstu i osadzenia LLM na Twoich danych.

Istnieje kilka sposobów przeprowadzania wyszukiwania w naszej bazie danych, takich jak:

- **Wyszukiwanie słów kluczowych** - używane do wyszukiwania tekstów

- **Wyszukiwanie semantyczne** - wykorzystuje semantyczne znaczenie słów

- **Wyszukiwanie wektorowe** - konwertuje dokumenty z tekstu na reprezentacje wektorowe za pomocą modeli embeddingu. Odzyskiwanie odbywa się poprzez zapytanie o dokumenty, których reprezentacje wektorowe są najbliższe pytaniu użytkownika.

- **Hybrydowe** - połączenie wyszukiwania słów kluczowych i wektorowego.

Wyzwanie związane z odzyskiwaniem pojawia się, gdy w bazie danych nie ma podobnej odpowiedzi na zapytanie, system zwróci wtedy najlepsze dostępne informacje, jednak można zastosować taktyki, takie jak ustawienie maksymalnej odległości dla istotności lub użycie wyszukiwania hybrydowego, które łączy wyszukiwanie słów kluczowych i wektorowe. W tej lekcji użyjemy wyszukiwania hybrydowego, połączenia wyszukiwania wektorowego i słów kluczowych. Będziemy przechowywać nasze dane w ramce danych z kolumnami zawierającymi fragmenty oraz embeddingi.

### Podobieństwo Wektorowe

Retriever przeszuka bazę wiedzy w poszukiwaniu embeddingów, które są blisko siebie, najbliższego sąsiada, ponieważ są to teksty podobne. W scenariuszu, gdy użytkownik zadaje zapytanie, jest ono najpierw osadzane, a następnie dopasowywane do podobnych embeddingów. Powszechną miarą używaną do określenia podobieństwa różnych wektorów jest podobieństwo kosinusowe, które opiera się na kącie między dwoma wektorami.

Możemy mierzyć podobieństwo za pomocą innych alternatyw, takich jak odległość euklidesowa, która jest prostą linią między punktami końcowymi wektorów, oraz iloczyn skalarny, który mierzy sumę iloczynów odpowiadających sobie elementów dwóch wektorów.

### Indeks wyszukiwania

Podczas odzyskiwania będziemy musieli zbudować indeks wyszukiwania dla naszej bazy wiedzy przed wykonaniem wyszukiwania. Indeks będzie przechowywać nasze embeddingi i może szybko odzyskać najbardziej podobne fragmenty nawet w dużej bazie danych. Możemy stworzyć nasz indeks lokalnie za pomocą:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Utwórz indeks wyszukiwania
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Aby zapytać indeks, możesz użyć metody kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Ponowne rangowanie

Po zapytaniu bazy danych może być konieczne posortowanie wyników od najbardziej istotnych. LLM do ponownego rangowania wykorzystuje uczenie maszynowe do poprawy trafności wyników wyszukiwania poprzez uporządkowanie ich od najbardziej istotnych. Korzystając z Azure AI Search, ponowne rangowanie jest wykonywane automatycznie za pomocą semantycznego rerankera. Przykład działania ponownego rangowania przy użyciu najbliższych sąsiadów:

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
        print(f"Indeks {index} nie znaleziony w ramce danych")
```

## Łączenie wszystkiego w całość

Ostatnim krokiem jest dodanie naszego LLM do miksu, aby móc uzyskać odpowiedzi oparte na naszych danych. Możemy to zaimplementować w następujący sposób:

```python
user_input = "czym jest perceptron?"

def chatbot(user_input):
    # Przekonwertuj pytanie na wektor zapytania
    query_vector = create_embeddings(user_input)

    # Znajdź najbardziej podobne dokumenty
    distances, indices = nbrs.kneighbors([query_vector])

    # dodaj dokumenty do zapytania, aby zapewnić kontekst
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # połącz historię i dane wejściowe użytkownika
    history.append(user_input)

    # utwórz obiekt wiadomości
    messages=[
        {"role": "system", "content": "Jesteś asystentem AI, który pomaga w pytaniach dotyczących AI."},
        {"role": "user", "content": history[-1]}
    ]

    # użyj uzupełniania czatu do wygenerowania odpowiedzi
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

### Metryki Oceny

- Jakość dostarczonych odpowiedzi zapewniająca, że brzmią naturalnie, płynnie i jak ludzkie

- Ugruntowanie danych: ocena, czy odpowiedź pochodziła z dostarczonych dokumentów

- Trafność: ocena, czy odpowiedź pasuje i jest związana z zadanym pytaniem

- Płynność - czy odpowiedź ma sens gramatyczny

## Przypadki użycia RAG (Retrieval Augmented Generation) i baz danych wektorowych

Istnieje wiele różnych przypadków użycia, w których wywołania funkcji mogą ulepszyć Twoją aplikację, na przykład:

- Odpowiadanie na pytania: osadzenie danych firmowych w czacie, który może być używany przez pracowników do zadawania pytań.

- Systemy rekomendacji: gdzie można stworzyć system, który dopasowuje najbardziej podobne wartości, np. filmy, restauracje i wiele innych.

- Usługi chatbotów: możesz przechowywać historię czatów i personalizować rozmowę w oparciu o dane użytkownika.

- Wyszukiwanie obrazów oparte na embeddingach wektorowych, przydatne przy rozpoznawaniu obrazów i wykrywaniu anomalii.

## Podsumowanie

Omówiliśmy podstawowe obszary RAG, od dodawania naszych danych do aplikacji, zapytania użytkownika i wyniku. Aby uprościć tworzenie RAG, możesz użyć frameworków takich jak Semantic Kernel, Langchain lub Autogen.

## Zadanie

Aby kontynuować naukę o Retrieval Augmented Generation (RAG), możesz zbudować:

- Zbuduj front-end dla aplikacji za pomocą wybranego frameworka

- Wykorzystaj framework, LangChain lub Semantic Kernel, i odtwórz swoją aplikację.

Gratulacje za ukończenie lekcji 👏.

## Nauka się tu nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej AI!
