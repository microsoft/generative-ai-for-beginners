# Budowanie Aplikacji Wyszukiwania

[![Wprowadzenie do Generatywnej SI i Dużych Modeli Językowych](../../images/08-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji_

LLM-y to nie tylko chatboty i generowanie tekstu. Możliwe jest również budowanie aplikacji wyszukiwania przy użyciu Embeddingów. Embeddingi to numeryczne reprezentacje danych, znane również jako wektory, i mogą być używane do semantycznego wyszukiwania danych.

W tej lekcji zbudujesz aplikację wyszukiwania dla naszego startupu edukacyjnego. Nasz startup to organizacja non-profit, która zapewnia darmową edukację uczniom w krajach rozwijających się. Nasz startup posiada dużą liczbę filmów na YouTube, których uczniowie mogą używać do nauki o SI. Nasz startup chce zbudować aplikację wyszukiwania, która pozwoli uczniom wyszukiwać filmy na YouTube wpisując pytanie.

Na przykład, uczeń może wpisać 'Czym są notebooki Jupyter?' lub 'Czym jest Azure ML', a aplikacja wyszukiwania zwróci listę filmów na YouTube, które są istotne dla pytania, a co więcej, aplikacja wyszukiwania zwróci link do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie.

## Wprowadzenie

W tej lekcji omówimy:

- Wyszukiwanie semantyczne vs wyszukiwanie po słowach kluczowych.
- Czym są osadzenia tekstu (Text Embeddings).
- Tworzenie indeksu osadzeń tekstu.
- Przeszukiwanie indeksu osadzeń tekstu.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Rozróżnić wyszukiwanie semantyczne i wyszukiwanie po słowach kluczowych.
- Wyjaśnić, czym są osadzenia tekstu.
- Stworzyć aplikację wykorzystującą osadzenia do wyszukiwania danych.

## Dlaczego budować aplikację wyszukiwania?

Tworzenie aplikacji wyszukiwania pomoże Ci zrozumieć, jak używać osadzeń do wyszukiwania danych. Nauczysz się również, jak zbudować aplikację wyszukiwania, która może być używana przez uczniów do szybkiego znajdowania informacji.

Lekcja zawiera indeks osadzeń transkrypcji z YouTube dla kanału Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) na YouTube. AI Show to kanał YouTube, który uczy Cię o SI i uczeniu maszynowym. Indeks osadzeń zawiera osadzenia dla każdej transkrypcji z YouTube do października 2023 roku. Użyjesz indeksu osadzeń do zbudowania aplikacji wyszukiwania dla naszego startupu. Aplikacja wyszukiwania zwraca link do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie. Jest to świetny sposób dla uczniów, aby szybko znaleźć potrzebne informacje.

Poniżej znajduje się przykład zapytania semantycznego dla pytania 'czy można używać RStudio z Azure ML?'. Spójrz na adres URL YouTube, zobaczysz, że adres URL zawiera znacznik czasu, który przenosi Cię do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie.

![Zapytanie semantyczne dla pytania "czy można używać RStudio z Azure ML"](../../images/query-results.png?WT.mc_id=academic-105485-koreyst)

## Czym jest wyszukiwanie semantyczne?

Teraz możesz się zastanawiać, czym jest wyszukiwanie semantyczne? Wyszukiwanie semantyczne to technika wyszukiwania, która wykorzystuje semantykę, czyli znaczenie, słów w zapytaniu, aby zwrócić istotne wyniki.

Oto przykład wyszukiwania semantycznego. Powiedzmy, że szukasz samochodu, możesz wyszukać 'samochód moich marzeń', wyszukiwanie semantyczne rozumie, że nie `marzysz` o samochodzie, ale raczej szukasz swojego `idealnego` samochodu. Wyszukiwanie semantyczne rozumie Twoją intencję i zwraca istotne wyniki. Alternatywą jest `wyszukiwanie po słowach kluczowych`, które dosłownie szukałoby marzeń o samochodach i często zwraca nieistotne wyniki.

## Czym są osadzenia tekstu?

[Osadzenia tekstu](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) to technika reprezentacji tekstu używana w [przetwarzaniu języka naturalnego](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Osadzenia tekstu to semantyczne numeryczne reprezentacje tekstu. Osadzenia są używane do reprezentowania danych w sposób, który jest łatwy do zrozumienia dla maszyny. Istnieje wiele modeli do budowania osadzeń tekstu, w tej lekcji skupimy się na generowaniu osadzeń przy użyciu modelu osadzeń OpenAI.

Oto przykład, wyobraź sobie, że następujący tekst znajduje się w transkrypcji z jednego z odcinków kanału AI Show na YouTube:

```text
Dzisiaj dowiemy się o Azure Machine Learning.
```

Przekazalibyśmy tekst do API osadzeń OpenAI, a on zwróciłby następujące osadzenie składające się z 1536 liczb, czyli wektor. Każda liczba w wektorze reprezentuje inny aspekt tekstu. Dla zwięzłości, oto pierwsze 10 liczb w wektorze.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Jak tworzony jest indeks osadzeń?

Indeks osadzeń dla tej lekcji został utworzony za pomocą serii skryptów Pythona. Znajdziesz skrypty wraz z instrukcjami w pliku [README](../../scripts/README.md?WT.mc_id=academic-105485-koreyst) w folderze 'scripts` dla tej lekcji. Nie musisz uruchamiać tych skryptów, aby ukończyć tę lekcję, ponieważ indeks osadzeń jest dostarczony dla Ciebie.

Skrypty wykonują następujące operacje:

1. Pobierana jest transkrypcja dla każdego filmu na YouTube z playlisty [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1).
2. Przy użyciu [funkcji OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), podejmowana jest próba wyodrębnienia nazwiska prelegenta z pierwszych 3 minut transkrypcji YouTube. Nazwisko prelegenta dla każdego filmu jest przechowywane w indeksie osadzeń o nazwie `embedding_index_3m.json`.
3. Tekst transkrypcji jest następnie dzielony na **3-minutowe segmenty tekstu**. Segment zawiera około 20 słów nakładających się z następnego segmentu, aby upewnić się, że osadzenie dla segmentu nie jest ucięte i aby zapewnić lepszy kontekst wyszukiwania.
4. Każdy segment tekstu jest następnie przekazywany do API czatu OpenAI w celu podsumowania tekstu w 60 słowach. Podsumowanie jest również przechowywane w indeksie osadzeń `embedding_index_3m.json`.
5. Wreszcie, segment tekstu jest przekazywany do API osadzeń OpenAI. API osadzeń zwraca wektor 1536 liczb, które reprezentują semantyczne znaczenie segmentu. Segment wraz z wektorem osadzenia OpenAI jest przechowywany w indeksie osadzeń `embedding_index_3m.json`.

### Bazy danych wektorowych

Dla uproszczenia lekcji, indeks osadzeń jest przechowywany w pliku JSON o nazwie `embedding_index_3m.json` i ładowany do DataFrame Pandas. Jednak w produkcji indeks osadzeń byłby przechowywany w bazie danych wektorowych, takiej jak [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), żeby wymienić tylko kilka.

## Zrozumienie podobieństwa cosinusowego

Dowiedzieliśmy się o osadzeniach tekstu, następnym krokiem jest nauczenie się, jak używać osadzeń tekstu do wyszukiwania danych, a w szczególności znajdowania najbardziej podobnych osadzeń do danego zapytania przy użyciu podobieństwa cosinusowego.

### Czym jest podobieństwo cosinusowe?

Podobieństwo cosinusowe to miara podobieństwa między dwoma wektorami, usłyszysz też o tym jako o `wyszukiwaniu najbliższego sąsiada`. Aby wykonać wyszukiwanie podobieństwa cosinusowego, musisz _zwektoryzować_ tekst _zapytania_ za pomocą API osadzeń OpenAI. Następnie obliczyć _podobieństwo cosinusowe_ między wektorem zapytania a każdym wektorem w indeksie osadzeń. Pamiętaj, indeks osadzeń ma wektor dla każdego segmentu tekstu transkrypcji YouTube. Na koniec posortuj wyniki według podobieństwa cosinusowego, a segmenty tekstu z najwyższym podobieństwem cosinusowym są najbardziej podobne do zapytania.

Z matematycznego punktu widzenia, podobieństwo cosinusowe mierzy cosinus kąta między dwoma wektorami rzutowanymi w wielowymiarowej przestrzeni. Ten pomiar jest korzystny, ponieważ jeśli dwa dokumenty są oddalone od siebie w odległości euklidesowej ze względu na rozmiar, nadal mogą mieć mniejszy kąt między nimi, a zatem wyższe podobieństwo cosinusowe. Aby uzyskać więcej informacji o równaniach podobieństwa cosinusowego, zobacz [Podobieństwo cosinusowe](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Budowanie pierwszej aplikacji wyszukiwania

Następnie dowiemy się, jak zbudować aplikację wyszukiwania przy użyciu osadzeń. Aplikacja wyszukiwania pozwoli uczniom wyszukiwać film wpisując pytanie. Aplikacja wyszukiwania zwróci listę filmów, które są istotne dla pytania. Aplikacja wyszukiwania zwróci również link do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie.

To rozwiązanie zostało zbudowane i przetestowane na Windows 11, macOS i Ubuntu 22.04 przy użyciu Pythona 3.10 lub nowszego. Możesz pobrać Pythona z [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Zadanie - budowanie aplikacji wyszukiwania, aby pomóc uczniom

Przedstawiliśmy nasz startup na początku tej lekcji. Teraz nadszedł czas, aby umożliwić uczniom zbudowanie aplikacji wyszukiwania dla ich ocen.

W tym zadaniu utworzysz usługi Azure OpenAI, które będą używane do zbudowania aplikacji wyszukiwania. Utworzysz następujące usługi Azure OpenAI. Będziesz potrzebować subskrypcji Azure, aby ukończyć to zadanie.

### Uruchom Azure Cloud Shell

1. Zaloguj się do [portalu Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Wybierz ikonę Cloud Shell w prawym górnym rogu portalu Azure.
3. Wybierz **Bash** jako typ środowiska.

#### Utwórz grupę zasobów

> Dla tych instrukcji używamy grupy zasobów o nazwie "semantic-video-search" w regionie East US.
> Możesz zmienić nazwę grupy zasobów, ale przy zmianie lokalizacji zasobów
> sprawdź [tabelę dostępności modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Utwórz zasób Azure OpenAI Service

Z Azure Cloud Shell uruchom następujące polecenie, aby utworzyć zasób Azure OpenAI Service.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Pobierz endpoint i klucze do użycia w tej aplikacji

Z Azure Cloud Shell uruchom następujące polecenia, aby uzyskać endpoint i klucze dla zasobu Azure OpenAI Service.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Wdróż model osadzeń OpenAI

Z Azure Cloud Shell uruchom następujące polecenie, aby wdrożyć model osadzeń OpenAI.

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

## Rozwiązanie

Otwórz [notatnik z rozwiązaniem](../../python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) w GitHub Codespaces i postępuj zgodnie z instrukcjami w Jupyter Notebook.

Gdy uruchomisz notatnik, zostaniesz poproszony o wprowadzenie zapytania. Pole wprowadzania będzie wyglądać tak:

![Pole wprowadzania dla użytkownika do wprowadzenia zapytania](../../images/notebook-search.png?WT.mc_id=academic-105485-koreyst)

## Świetna Praca! Kontynuuj Naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję materiałów edukacyjnych na temat Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby nadal podnosić swoją wiedzę o Generatywnej SI!

Przejdź do Lekcji 9, gdzie przyjrzymy się, jak [budować aplikacje generujące obrazy](../../../09-building-image-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
