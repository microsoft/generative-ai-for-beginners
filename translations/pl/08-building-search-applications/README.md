<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58953c08b8ba7073b836d4270ea0fe86",
  "translation_date": "2025-10-18T00:51:08+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "pl"
}
-->
# Tworzenie aplikacji wyszukiwania

[![Wprowadzenie do generatywnej AI i dużych modeli językowych](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.pl.png)](https://youtu.be/W0-nzXjOjr0?si=GcsqiTTvd7RKbo7V)

> > _Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji_

Modele językowe (LLM) to nie tylko chatboty i generowanie tekstu. Możliwe jest również tworzenie aplikacji wyszukiwania za pomocą Embeddings. Embeddings to numeryczne reprezentacje danych, znane również jako wektory, które mogą być używane do semantycznego wyszukiwania danych.

W tej lekcji zbudujesz aplikację wyszukiwania dla naszego startupu edukacyjnego. Nasz startup to organizacja non-profit, która oferuje darmową edukację uczniom w krajach rozwijających się. Posiadamy dużą liczbę filmów na YouTube, które uczniowie mogą wykorzystać do nauki o AI. Nasz startup chce stworzyć aplikację wyszukiwania, która pozwoli uczniom znaleźć film na YouTube, wpisując pytanie.

Na przykład, uczeń może wpisać „Co to są Jupyter Notebooks?” lub „Co to jest Azure ML?”, a aplikacja wyszukiwania zwróci listę filmów na YouTube, które są związane z pytaniem. Co więcej, aplikacja wyszukiwania zwróci link do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie.

## Wprowadzenie

W tej lekcji omówimy:

- Wyszukiwanie semantyczne vs wyszukiwanie słów kluczowych.
- Czym są Text Embeddings.
- Tworzenie indeksu Text Embeddings.
- Wyszukiwanie w indeksie Text Embeddings.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Rozróżnić wyszukiwanie semantyczne od wyszukiwania słów kluczowych.
- Wyjaśnić, czym są Text Embeddings.
- Stworzyć aplikację wykorzystującą Embeddings do wyszukiwania danych.

## Dlaczego warto stworzyć aplikację wyszukiwania?

Tworzenie aplikacji wyszukiwania pomoże Ci zrozumieć, jak używać Embeddings do wyszukiwania danych. Nauczysz się również, jak zbudować aplikację wyszukiwania, która może być używana przez uczniów do szybkiego znajdowania informacji.

Lekcja zawiera indeks Embedding transkryptów z kanału YouTube Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show to kanał YouTube, który uczy o sztucznej inteligencji i uczeniu maszynowym. Indeks Embedding zawiera Embeddings dla każdego z transkryptów na YouTube do października 2023 roku. Wykorzystasz ten indeks do stworzenia aplikacji wyszukiwania dla naszego startupu. Aplikacja wyszukiwania zwróci link do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie. To świetny sposób, aby uczniowie mogli szybko znaleźć potrzebne informacje.

Poniżej znajduje się przykład semantycznego zapytania dla pytania „Czy można używać rstudio z azure ml?”. Sprawdź URL na YouTube, zobaczysz, że zawiera on znacznik czasu, który przenosi Cię do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie.

![Semantyczne zapytanie dla pytania "Czy można używać rstudio z Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.pl.png)

## Co to jest wyszukiwanie semantyczne?

Możesz się zastanawiać, czym jest wyszukiwanie semantyczne? Wyszukiwanie semantyczne to technika wyszukiwania, która wykorzystuje semantykę, czyli znaczenie słów w zapytaniu, aby zwrócić odpowiednie wyniki.

Oto przykład wyszukiwania semantycznego. Powiedzmy, że chcesz kupić samochód, możesz wyszukać „mój wymarzony samochód”. Wyszukiwanie semantyczne rozumie, że nie `śnisz` o samochodzie, ale raczej szukasz swojego `idealnego` samochodu. Wyszukiwanie semantyczne rozumie Twoje intencje i zwraca odpowiednie wyniki. Alternatywą jest `wyszukiwanie słów kluczowych`, które dosłownie wyszukiwałoby sny o samochodach i często zwracałoby nieistotne wyniki.

## Czym są Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) to technika reprezentacji tekstu używana w [przetwarzaniu języka naturalnego](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Text embeddings to semantyczne numeryczne reprezentacje tekstu. Embeddings są używane do reprezentowania danych w sposób łatwy do zrozumienia przez maszynę. Istnieje wiele modeli do tworzenia text embeddings, w tej lekcji skupimy się na generowaniu embeddings za pomocą modelu OpenAI Embedding.

Oto przykład: wyobraź sobie, że poniższy tekst pochodzi z transkryptu jednego z odcinków na kanale YouTube AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Przekazujemy tekst do OpenAI Embedding API, które zwraca następujący embedding składający się z 1536 liczb, czyli wektora. Każda liczba w wektorze reprezentuje inny aspekt tekstu. Dla skrótu, oto pierwsze 10 liczb w wektorze.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Jak tworzony jest indeks Embedding?

Indeks Embedding dla tej lekcji został stworzony za pomocą serii skryptów w Pythonie. Znajdziesz te skrypty wraz z instrukcjami w [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) w folderze 'scripts' dla tej lekcji. Nie musisz uruchamiać tych skryptów, aby ukończyć tę lekcję, ponieważ indeks Embedding jest już dla Ciebie przygotowany.

Skrypty wykonują następujące operacje:

1. Transkrypt każdego filmu na YouTube z playlisty [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) jest pobierany.
2. Korzystając z [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), podejmowana jest próba wyodrębnienia imienia mówcy z pierwszych 3 minut transkryptu YouTube. Imię mówcy dla każdego filmu jest przechowywane w indeksie Embedding o nazwie `embedding_index_3m.json`.
3. Tekst transkryptu jest dzielony na **3-minutowe segmenty tekstowe**. Segment zawiera około 20 słów nakładających się z następnym segmentem, aby zapewnić, że Embedding dla segmentu nie zostanie przerwany i aby zapewnić lepszy kontekst wyszukiwania.
4. Każdy segment tekstowy jest przekazywany do OpenAI Chat API w celu podsumowania tekstu w 60 słowach. Podsumowanie jest również przechowywane w indeksie Embedding `embedding_index_3m.json`.
5. Na koniec tekst segmentu jest przekazywany do OpenAI Embedding API. Embedding API zwraca wektor składający się z 1536 liczb, które reprezentują semantyczne znaczenie segmentu. Segment wraz z wektorem Embedding OpenAI jest przechowywany w indeksie Embedding `embedding_index_3m.json`.

### Bazy danych wektorowych

Dla uproszczenia lekcji indeks Embedding jest przechowywany w pliku JSON o nazwie `embedding_index_3m.json` i ładowany do Pandas DataFrame. Jednak w produkcji indeks Embedding byłby przechowywany w bazie danych wektorowych, takiej jak [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), i inne.

## Zrozumienie podobieństwa kosinusowego

Nauczyliśmy się o text embeddings, kolejnym krokiem jest nauka, jak używać text embeddings do wyszukiwania danych, a w szczególności znajdowania najbardziej podobnych embeddings do danego zapytania za pomocą podobieństwa kosinusowego.

### Co to jest podobieństwo kosinusowe?

Podobieństwo kosinusowe to miara podobieństwa między dwoma wektorami, często nazywana `wyszukiwaniem najbliższego sąsiada`. Aby przeprowadzić wyszukiwanie podobieństwa kosinusowego, należy _wektoryzować_ tekst _zapytania_ za pomocą OpenAI Embedding API. Następnie obliczyć _podobieństwo kosinusowe_ między wektorem zapytania a każdym wektorem w indeksie Embedding. Pamiętaj, że indeks Embedding zawiera wektor dla każdego segmentu tekstowego transkryptu YouTube. Na koniec posortuj wyniki według podobieństwa kosinusowego, a segmenty tekstowe z najwyższym podobieństwem kosinusowym są najbardziej podobne do zapytania.

Z matematycznego punktu widzenia podobieństwo kosinusowe mierzy kosinus kąta między dwoma wektorami w przestrzeni wielowymiarowej. Ta miara jest korzystna, ponieważ jeśli dwa dokumenty są daleko od siebie w odległości euklidesowej z powodu rozmiaru, mogą nadal mieć mniejszy kąt między sobą, a zatem wyższe podobieństwo kosinusowe. Więcej informacji na temat równań podobieństwa kosinusowego znajdziesz w [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Tworzenie pierwszej aplikacji wyszukiwania

Następnie nauczymy się, jak zbudować aplikację wyszukiwania za pomocą Embeddings. Aplikacja wyszukiwania pozwoli uczniom wyszukiwać filmy, wpisując pytanie. Aplikacja wyszukiwania zwróci listę filmów, które są związane z pytaniem. Aplikacja wyszukiwania zwróci również link do miejsca w filmie, gdzie znajduje się odpowiedź na pytanie.

To rozwiązanie zostało zbudowane i przetestowane na Windows 11, macOS i Ubuntu 22.04, używając Python 3.10 lub nowszego. Możesz pobrać Pythona z [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Zadanie - tworzenie aplikacji wyszukiwania, aby umożliwić uczniom

Przedstawiliśmy nasz startup na początku tej lekcji. Teraz nadszedł czas, aby umożliwić uczniom stworzenie aplikacji wyszukiwania do ich ocen.

W tym zadaniu utworzysz usługi Azure OpenAI, które będą używane do budowy aplikacji wyszukiwania. Utworzysz następujące usługi Azure OpenAI. Aby ukończyć to zadanie, będziesz potrzebować subskrypcji Azure.

### Uruchomienie Azure Cloud Shell

1. Zaloguj się do [portalu Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Wybierz ikonę Cloud Shell w prawym górnym rogu portalu Azure.
3. Wybierz **Bash** jako typ środowiska.

#### Utworzenie grupy zasobów

> W tych instrukcjach używamy grupy zasobów o nazwie „semantic-video-search” w regionie East US.
> Możesz zmienić nazwę grupy zasobów, ale zmieniając lokalizację zasobów,
> sprawdź [tabelę dostępności modeli](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Utworzenie zasobu Azure OpenAI Service

Z poziomu Azure Cloud Shell uruchom następujące polecenie, aby utworzyć zasób Azure OpenAI Service.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Pobranie punktu końcowego i kluczy do użycia w tej aplikacji

Z poziomu Azure Cloud Shell uruchom następujące polecenia, aby pobrać punkt końcowy i klucze dla zasobu Azure OpenAI Service.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Wdrożenie modelu OpenAI Embedding

Z poziomu Azure Cloud Shell uruchom następujące polecenie, aby wdrożyć model OpenAI Embedding.

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

Otwórz [notebook z rozwiązaniem](./python/aoai-solution.ipynb?WT.mc_id=academic-105485-koreyst) w GitHub Codespaces i postępuj zgodnie z instrukcjami w Jupyter Notebook.

Po uruchomieniu notebooka zostaniesz poproszony o wpisanie zapytania. Pole do wprowadzania będzie wyglądać tak:

![Pole do wprowadzania zapytania przez użytkownika](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.pl.png)

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat generatywnej AI!

Przejdź do lekcji 9, gdzie przyjrzymy się, jak [tworzyć aplikacje generujące obrazy](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.