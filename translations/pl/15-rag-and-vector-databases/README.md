<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-05-20T01:16:20+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "pl"
}
-->
# Generowanie wspomagane wyszukiwaniem (RAG) i bazy danych wektorowych

W lekcji dotyczącej aplikacji wyszukiwania krótko omówiliśmy, jak zintegrować własne dane z dużymi modelami językowymi (LLM). W tej lekcji zagłębimy się w pojęcia związane z ugruntowaniem danych w aplikacji LLM, mechanikę procesu oraz metody przechowywania danych, w tym zarówno osadzeń, jak i tekstu.

> **Wideo wkrótce**

## Wprowadzenie

W tej lekcji omówimy:

- Wprowadzenie do RAG, czym jest i dlaczego jest używane w AI (sztucznej inteligencji).

- Zrozumienie, czym są bazy danych wektorowych i tworzenie jednej dla naszej aplikacji.

- Praktyczny przykład integracji RAG z aplikacją.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wyjaśnić znaczenie RAG w odnajdywaniu i przetwarzaniu danych.

- Skonfigurować aplikację RAG i ugruntować swoje dane w LLM.

- Skuteczna integracja RAG i baz danych wektorowych w aplikacjach LLM.

## Nasz scenariusz: wzbogacanie naszych LLM o własne dane

W tej lekcji chcemy dodać własne notatki do startupu edukacyjnego, co pozwala chatbotowi uzyskać więcej informacji na różne tematy. Dzięki notatkom, które posiadamy, uczniowie będą mogli lepiej się uczyć i zrozumieć różne tematy, co ułatwi im przygotowanie się do egzaminów. Aby stworzyć nasz scenariusz, użyjemy:

- `Azure OpenAI:` LLM, którego użyjemy do stworzenia naszego chatbota

- `AI for beginners' lesson on Neural Networks`: to będą dane, na których ugruntujemy nasze LLM

- `Azure AI Search` i `Azure Cosmos DB:` baza danych wektorowych do przechowywania naszych danych i tworzenia indeksu wyszukiwania

Użytkownicy będą mogli tworzyć quizy ćwiczeniowe z notatek, fiszki do powtórek i podsumowywać je do zwięzłych przeglądów. Aby rozpocząć, przyjrzyjmy się, czym jest RAG i jak działa:

## Generowanie wspomagane wyszukiwaniem (RAG)

Chatbot oparty na LLM przetwarza zapytania użytkownika, aby generować odpowiedzi. Jest zaprojektowany do interakcji i angażuje użytkowników w szeroką gamę tematów. Jednak jego odpowiedzi są ograniczone do dostarczonego kontekstu i danych treningowych. Na przykład, GPT-4 ma ograniczenie wiedzy do września 2021 roku, co oznacza, że nie zna wydarzeń, które miały miejsce po tym okresie. Ponadto, dane używane do trenowania LLM wykluczają poufne informacje, takie jak osobiste notatki czy podręcznik produktowy firmy.

### Jak działają RAG (Generowanie wspomagane wyszukiwaniem)

Załóżmy, że chcesz wdrożyć chatbota, który tworzy quizy z twoich notatek, będziesz potrzebować połączenia z bazą wiedzy. Tutaj RAG przychodzi z pomocą. RAG działa w następujący sposób:

- **Baza wiedzy:** Przed wyszukiwaniem dokumenty te muszą zostać wczytane i przetworzone, zazwyczaj poprzez podział dużych dokumentów na mniejsze fragmenty, przekształcenie ich w osadzenia tekstowe i przechowywanie w bazie danych.

- **Zapytanie użytkownika:** użytkownik zadaje pytanie

- **Wyszukiwanie:** Gdy użytkownik zadaje pytanie, model osadzeń pobiera odpowiednie informacje z naszej bazy wiedzy, aby dostarczyć więcej kontekstu, który zostanie włączony do zapytania.

- **Generowanie wspomagane:** LLM wzbogaca swoją odpowiedź na podstawie pobranych danych. Pozwala to na generowanie odpowiedzi nie tylko na podstawie wstępnie wytrenowanych danych, ale także na podstawie istotnych informacji z dodanego kontekstu. Pobierane dane są używane do wzbogacania odpowiedzi LLM. LLM następnie zwraca odpowiedź na pytanie użytkownika.

Architektura RAG jest implementowana przy użyciu transformatorów składających się z dwóch części: enkodera i dekodera. Na przykład, gdy użytkownik zadaje pytanie, tekst wejściowy jest 'kodowany' na wektory uchwytujące znaczenie słów, a wektory są 'dekodowane' w nasz indeks dokumentów i generują nowy tekst na podstawie zapytania użytkownika. LLM wykorzystuje model enkoder-dekoder do generowania wyjścia.

Dwa podejścia przy implementacji RAG zgodnie z proponowanym artykułem: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) to:

- **_RAG-Sequence_** używanie pobranych dokumentów do przewidywania najlepszej możliwej odpowiedzi na zapytanie użytkownika

- **RAG-Token** używanie dokumentów do generowania następnego tokena, a następnie pobieranie ich w celu odpowiedzi na zapytanie użytkownika

### Dlaczego warto używać RAG? 

- **Bogactwo informacji:** zapewnia, że odpowiedzi tekstowe są aktualne i bieżące. Zatem poprawia wydajność w zadaniach specyficznych dla domeny, uzyskując dostęp do wewnętrznej bazy wiedzy.

- Redukuje fałszowanie poprzez wykorzystanie **weryfikowalnych danych** w bazie wiedzy do dostarczenia kontekstu do zapytań użytkowników.

- Jest **kosztowo efektywne**, ponieważ są bardziej ekonomiczne w porównaniu do dostrajania LLM.

## Tworzenie bazy wiedzy

Nasza aplikacja opiera się na naszych danych osobistych, tj. lekcji o sieciach neuronowych w programie AI For Beginners.

### Bazy danych wektorowych

Baza danych wektorowych, w przeciwieństwie do tradycyjnych baz danych, to specjalistyczna baza danych zaprojektowana do przechowywania, zarządzania i wyszukiwania osadzonych wektorów. Przechowuje numeryczne reprezentacje dokumentów. Rozbicie danych na numeryczne osadzenia ułatwia naszemu systemowi AI zrozumienie i przetwarzanie danych.

Przechowujemy nasze osadzenia w bazach danych wektorowych, ponieważ LLM mają ograniczenie liczby tokenów, które akceptują jako dane wejściowe. Ponieważ nie można przekazać całych osadzeń do LLM, musimy je podzielić na fragmenty, a gdy użytkownik zadaje pytanie, osadzenia najbardziej podobne do pytania zostaną zwrócone razem z zapytaniem. Podział na fragmenty również redukuje koszty związane z liczbą tokenów przekazywanych przez LLM.

Niektóre popularne bazy danych wektorowych to Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant i DeepLake. Możesz stworzyć model Azure Cosmos DB za pomocą Azure CLI z następującym poleceniem:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Od tekstu do osadzeń

Zanim przechowamy nasze dane, musimy je przekonwertować na osadzenia wektorowe przed ich przechowaniem w bazie danych. Jeśli pracujesz z dużymi dokumentami lub długimi tekstami, możesz je podzielić na fragmenty na podstawie oczekiwanych zapytań. Podział można przeprowadzić na poziomie zdania lub akapitu. Ponieważ podział wywodzi znaczenia z otaczających słów, możesz dodać dodatkowy kontekst do fragmentu, na przykład dodając tytuł dokumentu lub wstawiając tekst przed lub po fragmencie. Możesz podzielić dane w następujący sposób:

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

Po podzieleniu możemy następnie osadzić nasz tekst za pomocą różnych modeli osadzeń. Niektóre modele, które można użyć, to: word2vec, ada-002 przez OpenAI, Azure Computer Vision i wiele innych. Wybór modelu zależy od używanych języków, rodzaju kodowanej treści (tekst/obrazy/dźwięk), wielkości wejścia, które można zakodować, oraz długości wyjścia osadzenia.

Przykład osadzonego tekstu przy użyciu modelu `text-embedding-ada-002` OpenAI to:

## Wyszukiwanie i wyszukiwanie wektorowe

Kiedy użytkownik zadaje pytanie, retriever przekształca je w wektor za pomocą enkodera zapytań, a następnie przeszukuje nasz indeks wyszukiwania dokumentów w poszukiwaniu odpowiednich wektorów w dokumencie, które są związane z danymi wejściowymi. Po zakończeniu konwertuje zarówno wektor wejściowy, jak i wektory dokumentu na tekst i przekazuje je przez LLM.

### Wyszukiwanie

Wyszukiwanie ma miejsce, gdy system próbuje szybko znaleźć dokumenty z indeksu, które spełniają kryteria wyszukiwania. Celem retrievera jest uzyskanie dokumentów, które będą używane do dostarczenia kontekstu i ugruntowania LLM na twoich danych.

Istnieje kilka sposobów na przeprowadzenie wyszukiwania w naszej bazie danych, takich jak:

- **Wyszukiwanie słów kluczowych** - używane do wyszukiwania tekstu

- **Wyszukiwanie semantyczne** - używa semantycznego znaczenia słów

- **Wyszukiwanie wektorowe** - konwertuje dokumenty z tekstu na reprezentacje wektorowe za pomocą modeli osadzeń. Wyszukiwanie odbywa się poprzez zapytanie dokumentów, których reprezentacje wektorowe są najbliższe pytaniu użytkownika.

- **Hybrydowe** - połączenie zarówno wyszukiwania słów kluczowych, jak i wyszukiwania wektorowego.

Problem z wyszukiwaniem pojawia się, gdy w bazie danych nie ma podobnej odpowiedzi na zapytanie, wtedy system zwróci najlepsze informacje, jakie może uzyskać, jednak można użyć taktyk, takich jak ustawienie maksymalnej odległości dla istotności lub użycie wyszukiwania hybrydowego, które łączy zarówno słowa kluczowe, jak i wyszukiwanie wektorowe. W tej lekcji użyjemy wyszukiwania hybrydowego, połączenia zarówno wyszukiwania wektorowego, jak i słów kluczowych. Przechowamy nasze dane w ramce danych z kolumnami zawierającymi fragmenty oraz osadzenia.

### Podobieństwo wektorowe

Retriever przeszuka bazę wiedzy w poszukiwaniu osadzeń, które są blisko siebie, najbliższego sąsiada, ponieważ są to teksty, które są podobne. W scenariuszu, gdy użytkownik zadaje zapytanie, jest ono najpierw osadzane, a następnie dopasowywane do podobnych osadzeń. Powszechną miarą używaną do określenia, jak podobne są różne wektory, jest podobieństwo kosinusowe, które opiera się na kącie między dwoma wektorami.

Możemy mierzyć podobieństwo za pomocą innych alternatyw, które możemy użyć, takich jak odległość euklidesowa, która jest linią prostą między końcami wektorów, oraz iloczyn skalarny, który mierzy sumę iloczynów odpowiadających sobie elementów dwóch wektorów.

### Indeks wyszukiwania

Podczas wyszukiwania będziemy musieli zbudować indeks wyszukiwania dla naszej bazy wiedzy, zanim przeprowadzimy wyszukiwanie. Indeks przechowa nasze osadzenia i może szybko odnaleźć najpodobniejsze fragmenty nawet w dużej bazie danych. Możemy stworzyć nasz indeks lokalnie, używając:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

Po zapytaniu bazy danych może być konieczne posortowanie wyników od najbardziej istotnych. LLM do rerankingu wykorzystuje uczenie maszynowe do poprawy trafności wyników wyszukiwania, porządkując je od najbardziej istotnych. Korzystając z Azure AI Search, reranking jest wykonywany automatycznie za pomocą semantycznego rerankera. Przykład działania rerankingu przy użyciu najbliższych sąsiadów:

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

## Połączenie wszystkiego w całość

Ostatnim krokiem jest dodanie naszego LLM do całości, aby móc uzyskać odpowiedzi oparte na naszych danych. Możemy to zaimplementować w następujący sposób:

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

## Ocena naszej aplikacji

### Metryki oceny

- Jakość dostarczanych odpowiedzi, zapewniająca, że brzmią naturalnie, płynnie i ludzko

- Ugruntowanie danych: ocena, czy odpowiedź pochodzi z dostarczonych dokumentów

- Trafność: ocena, czy odpowiedź pasuje i jest związana z zadanym pytaniem

- Płynność - czy odpowiedź jest poprawna gramatycznie

## Przypadki użycia RAG (Generowanie wspomagane wyszukiwaniem) i baz danych wektorowych

Istnieje wiele różnych przypadków użycia, w których wywołania funkcji mogą poprawić twoją aplikację, takich jak:

- Pytania i odpowiedzi: ugruntowanie danych firmy do czatu, z którego mogą korzystać pracownicy, aby zadawać pytania.

- Systemy rekomendacji: gdzie można stworzyć system, który dopasowuje najbardziej podobne wartości, np. filmy, restauracje i wiele innych.

- Usługi chatbotów: możesz przechowywać historię czatu i personalizować rozmowę na podstawie danych użytkownika.

- Wyszukiwanie obrazów na podstawie osadzeń wektorowych, przydatne podczas rozpoznawania obrazów i wykrywania anomalii.

## Podsumowanie

Omówiliśmy podstawowe obszary RAG od dodawania naszych danych do aplikacji, zapytania użytkownika i wyjścia. Aby uprościć tworzenie RAG, można użyć takich frameworków jak Semanti Kernel, Langchain lub Autogen.

## Zadanie

Aby kontynuować naukę na temat Generowania wspomaganego wyszukiwaniem (RAG), możesz zbudować:

- Stwórz interfejs front-end dla aplikacji, korzystając z wybranego frameworka

- Wykorzystaj framework, LangChain lub Semantic Kernel, i odtwórz swoją aplikację.

Gratulacje z ukończenia lekcji 👏.

## Nauka nie kończy się tutaj, kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję nauki o AI generatywnej](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować pogłębianie swojej wiedzy na temat AI generatywnej!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.