<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T09:08:25+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do generatywnej AI i dużych modeli językowych

_(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

Generatywna AI to sztuczna inteligencja zdolna do generowania tekstu, obrazów i innych rodzajów treści. Co czyni ją fantastyczną technologią, to fakt, że demokratyzuje AI - każdy może ją używać, mając do dyspozycji jedynie tekstowy prompt, zdanie napisane w naturalnym języku. Nie musisz uczyć się języków takich jak Java czy SQL, aby osiągnąć coś wartościowego, wystarczy użyć swojego języka, określić, czego chcesz, a model AI przedstawi propozycję. Zastosowania i wpływ są ogromne - możesz pisać lub rozumieć raporty, tworzyć aplikacje i wiele więcej, wszystko w ciągu kilku sekund.

W tym programie nauczania zbadamy, jak nasz startup wykorzystuje generatywną AI do otwierania nowych scenariuszy w świecie edukacji oraz jak radzimy sobie z nieuchronnymi wyzwaniami związanymi z społecznymi implikacjami jej zastosowania i ograniczeniami technologicznymi.

## Wprowadzenie

Ta lekcja obejmie:

- Wprowadzenie do scenariusza biznesowego: nasz pomysł na startup i misję.
- Generatywna AI i jak doszliśmy do obecnego krajobrazu technologicznego.
- Wewnętrzne działanie dużego modelu językowego.
- Główne możliwości i praktyczne zastosowania dużych modeli językowych.

## Cele nauki

Po ukończeniu tej lekcji zrozumiesz:

- Czym jest generatywna AI i jak działają duże modele językowe.
- Jak możesz wykorzystać duże modele językowe w różnych scenariuszach, ze szczególnym uwzględnieniem edukacji.

## Scenariusz: nasz edukacyjny startup

Generatywna sztuczna inteligencja (AI) reprezentuje szczyt technologii AI, przesuwając granice tego, co kiedyś uważano za niemożliwe. Modele generatywne AI mają wiele możliwości i zastosowań, ale w ramach tego programu nauczania zbadamy, jak rewolucjonizuje edukację poprzez fikcyjny startup. Odniesiemy się do tego startupu jako _nasz startup_. Nasz startup działa w dziedzinie edukacji z ambitnym celem

> _poprawa dostępności w nauce na skalę globalną, zapewnienie równego dostępu do edukacji i dostarczanie spersonalizowanych doświadczeń edukacyjnych każdemu uczniowi zgodnie z jego potrzebami_.

Zespół naszego startupu zdaje sobie sprawę, że nie osiągniemy tego celu bez wykorzystania jednego z najpotężniejszych narzędzi współczesności – dużych modeli językowych (LLM).

Oczekuje się, że generatywna AI zrewolucjonizuje sposób, w jaki uczymy się i nauczamy dzisiaj, z uczniami mającymi do dyspozycji wirtualnych nauczycieli 24 godziny na dobę, którzy dostarczają ogromne ilości informacji i przykładów, oraz nauczycieli mogących korzystać z innowacyjnych narzędzi do oceny swoich uczniów i udzielania feedbacku.

Aby zacząć, zdefiniujmy kilka podstawowych pojęć i terminów, których będziemy używać w całym programie nauczania.

## Jak uzyskaliśmy generatywną AI?

Pomimo niezwykłego _szumu_ stworzonego ostatnio przez ogłoszenia modeli generatywnej AI, ta technologia jest tworzona od dziesięcioleci, a pierwsze wysiłki badawcze sięgają lat 60. Jesteśmy teraz w punkcie, w którym AI posiada ludzkie zdolności poznawcze, takie jak rozmowa, co pokazują na przykład [OpenAI ChatGPT](https://openai.com/chatgpt) lub [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), które również używają modelu GPT do wyszukiwania w Bing.

Wracając nieco, pierwsze prototypy AI składały się z pisanych chatbotów, opierających się na bazie wiedzy wyciągniętej z grupy ekspertów i reprezentowanej w komputerze. Odpowiedzi w bazie wiedzy były wyzwalane przez słowa kluczowe pojawiające się w tekście wejściowym.
Jednak szybko stało się jasne, że takie podejście, używając pisanych chatbotów, nie skalowało się dobrze.

### Statystyczne podejście do AI: uczenie maszynowe

Przełom nastąpił w latach 90., kiedy zastosowano statystyczne podejście do analizy tekstu. Doprowadziło to do rozwoju nowych algorytmów – znanych jako uczenie maszynowe – zdolnych do nauki wzorców z danych bez wyraźnego programowania. To podejście pozwala maszynom symulować rozumienie języka ludzkiego: model statystyczny jest trenowany na parach tekst-etykieta, umożliwiając modelowi klasyfikację nieznanego tekstu wejściowego z predefiniowaną etykietą reprezentującą zamiar wiadomości.

### Sieci neuronowe i nowoczesni wirtualni asystenci

W ostatnich latach technologiczna ewolucja sprzętu, zdolnego do obsługi większych ilości danych i bardziej skomplikowanych obliczeń, zachęciła do badań nad AI, prowadząc do rozwoju zaawansowanych algorytmów uczenia maszynowego, znanych jako sieci neuronowe lub algorytmy głębokiego uczenia.

Sieci neuronowe (a w szczególności Recurrent Neural Networks – RNNs) znacząco poprawiły przetwarzanie języka naturalnego, umożliwiając reprezentację znaczenia tekstu w bardziej znaczący sposób, ceniąc kontekst słowa w zdaniu.

To jest technologia, która napędzała wirtualnych asystentów powstałych w pierwszej dekadzie nowego wieku, bardzo biegłych w interpretacji języka ludzkiego, identyfikacji potrzeby i wykonywaniu działania, aby ją zaspokoić – jak odpowiedź na predefiniowany skrypt lub konsumowanie usługi zewnętrznej.

### Obecnie, generatywna AI

Tak właśnie doszliśmy do generatywnej AI dzisiaj, która może być postrzegana jako podzbiór głębokiego uczenia.

Po dekadach badań w dziedzinie AI nowa architektura modelu – zwana _Transformer_ – pokonała ograniczenia RNNs, będąc w stanie przyjąć znacznie dłuższe sekwencje tekstu jako dane wejściowe. Transformatory opierają się na mechanizmie uwagi, umożliwiając modelowi nadanie różnych wag wejściom, które otrzymuje, 'zwracając większą uwagę' tam, gdzie koncentrują się najbardziej istotne informacje, niezależnie od ich kolejności w sekwencji tekstowej.

Większość niedawnych modeli generatywnej AI – znanych również jako duże modele językowe (LLMs), ponieważ pracują z tekstowymi wejściami i wyjściami – jest rzeczywiście oparta na tej architekturze. Co ciekawe w tych modelach – trenowanych na ogromnej ilości nieoznakowanych danych z różnych źródeł, takich jak książki, artykuły i strony internetowe – jest to, że mogą być dostosowane do szerokiej gamy zadań i generować gramatycznie poprawny tekst z pozorami kreatywności. Tak więc, nie tylko znacznie zwiększyły zdolność maszyny do 'rozumienia' tekstu wejściowego, ale umożliwiły jej zdolność do generowania oryginalnej odpowiedzi w języku ludzkim.

## Jak działają duże modele językowe?

W następnym rozdziale będziemy eksplorować różne typy modeli generatywnej AI, ale na razie przyjrzyjmy się, jak działają duże modele językowe, koncentrując się na modelach OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, tekst na liczby**: Duże modele językowe otrzymują tekst jako dane wejściowe i generują tekst jako dane wyjściowe. Jednak będąc modelami statystycznymi, lepiej radzą sobie z liczbami niż sekwencjami tekstowymi. Dlatego każdy tekst wejściowy do modelu jest przetwarzany przez tokenizer, zanim zostanie użyty przez rdzeń modelu. Token to fragment tekstu – składający się z zmiennej liczby znaków, więc głównym zadaniem tokenizera jest podzielenie wejścia na tablicę tokenów. Następnie każdy token jest mapowany na indeks tokena, który jest całkowitym kodowaniem oryginalnego fragmentu tekstu.

- **Przewidywanie tokenów wyjściowych**: Mając n tokenów jako dane wejściowe (z maksymalnym n różniącym się w zależności od modelu), model jest w stanie przewidzieć jeden token jako dane wyjściowe. Ten token jest następnie włączany do wejścia następnej iteracji, w rozszerzającym się wzorze okna, umożliwiając lepsze doświadczenie użytkownika w uzyskiwaniu jednej (lub wielu) zdania jako odpowiedzi. To wyjaśnia, dlaczego, jeśli kiedykolwiek bawiłeś się ChatGPT, mogłeś zauważyć, że czasami wygląda, jakby zatrzymywał się w połowie zdania.

- **Proces wyboru, rozkład prawdopodobieństwa**: Token wyjściowy jest wybierany przez model zgodnie z jego prawdopodobieństwem wystąpienia po bieżącej sekwencji tekstowej. Dzieje się tak, ponieważ model przewiduje rozkład prawdopodobieństwa dla wszystkich możliwych 'następnych tokenów', obliczony na podstawie jego treningu. Jednak nie zawsze jest wybierany token o najwyższym prawdopodobieństwie z wynikowego rozkładu. Do tego wyboru dodawany jest stopień losowości, w sposób, który sprawia, że model działa w sposób niedeterministyczny - nie otrzymujemy dokładnie tego samego wyjścia dla tego samego wejścia. Ten stopień losowości jest dodawany, aby symulować proces kreatywnego myślenia i można go dostosować za pomocą parametru modelu zwanego temperaturą.

## Jak nasz startup może wykorzystać duże modele językowe?

Teraz, gdy lepiej rozumiemy wewnętrzne działanie dużego modelu językowego, zobaczmy kilka praktycznych przykładów najczęstszych zadań, które mogą wykonywać całkiem dobrze, z uwzględnieniem naszego scenariusza biznesowego.
Powiedzieliśmy, że główną zdolnością dużego modelu językowego jest _generowanie tekstu od podstaw, zaczynając od tekstowego wejścia, napisanego w języku naturalnym_.

Ale jakiego rodzaju tekstowe wejście i wyjście?
Wejście dużego modelu językowego jest znane jako prompt, podczas gdy wyjście jest znane jako completion, termin odnoszący się do mechanizmu modelu generowania następnego tokena w celu ukończenia bieżącego wejścia. Zagłębimy się w to, czym jest prompt i jak go zaprojektować, aby uzyskać jak najwięcej z naszego modelu. Ale na razie powiedzmy tylko, że prompt może zawierać:

- **Instrukcję** określającą rodzaj wyjścia, którego oczekujemy od modelu. Ta instrukcja czasami może zawierać przykłady lub dodatkowe dane.

  1. Podsumowanie artykułu, książki, recenzji produktu i innych, wraz z wyciąganiem wniosków z nieustrukturyzowanych danych.

  2. Kreatywne tworzenie i projektowanie artykułu, eseju, zadania lub innych.

- **Pytanie**, zadane w formie rozmowy z agentem.

- Fragment **tekstu do ukończenia**, który implicitnie jest prośbą o pomoc w pisaniu.

- Fragment **kodu** wraz z prośbą o wyjaśnienie i dokumentację lub komentarz proszący o wygenerowanie kawałka kodu wykonującego określone zadanie.

Powyższe przykłady są dość proste i nie mają na celu wyczerpującej demonstracji możliwości dużych modeli językowych. Mają na celu pokazanie potencjału wykorzystania generatywnej AI, w szczególności, ale nie ograniczając się do kontekstów edukacyjnych.

Ponadto, wyjście modelu generatywnej AI nie jest doskonałe i czasami kreatywność modelu może działać przeciwko niemu, skutkując wyjściem będącym kombinacją słów, które użytkownik ludzki może interpretować jako mistyfikację rzeczywistości lub może być obraźliwe. Generatywna AI nie jest inteligentna - przynajmniej w bardziej kompleksowym znaczeniu inteligencji, obejmującym krytyczne i kreatywne myślenie lub inteligencję emocjonalną; nie jest deterministyczna i nie jest godna zaufania, ponieważ fałszywe informacje, takie jak błędne odniesienia, treści i stwierdzenia, mogą być łączone z poprawnymi informacjami i przedstawiane w przekonujący i pewny sposób. W kolejnych lekcjach będziemy zajmować się wszystkimi tymi ograniczeniami i zobaczymy, co możemy zrobić, aby je złagodzić.

## Zadanie

Twoim zadaniem jest przeczytanie więcej o [generatywnej AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) i spróbuj zidentyfikować obszar, w którym dodałbyś generatywną AI dzisiaj, gdzie jej jeszcze nie ma. Jak różniłby się wpływ od wykonywania tego "starym sposobem", czy możesz zrobić coś, czego wcześniej nie mogłeś, czy jesteś szybszy? Napisz 300-słowe podsumowanie, jak wyglądałby twój wymarzony startup AI i zawrzyj nagłówki takie jak "Problem", "Jak użyłbym AI", "Wpływ" i opcjonalnie plan biznesowy.

Jeśli wykonałeś to zadanie, możesz być gotowy do aplikacji do inkubatora Microsoftu, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) oferujemy kredyty zarówno dla Azure, OpenAI, mentoring i wiele więcej, sprawdź to!

## Sprawdzenie wiedzy

Co jest prawdziwe o dużych modelach językowych?

1. Za każdym razem otrzymujesz dokładnie tę samą odpowiedź.
2. Robi wszystko perfekcyjnie, świetnie dodaje liczby, tworzy działający kod itp.
3. Odpowiedź może się różnić pomimo użycia tego samego promptu. Jest również świetny w dostarczaniu pierwszej wersji czegoś, czy to tekstu czy kodu. Ale musisz poprawić wyniki.

Odpowiedź: 3, LLM jest niedeterministyczny, odpowiedź się różni, jednak możesz kontrolować jej zmienność za pomocą ustawienia temperatury. Nie powinieneś też oczekiwać, że robi wszystko perfekcyjnie, jest tu, aby wykonać ciężką pracę za ciebie, co często oznacza, że otrzymujesz dobrą pierwszą próbę czegoś, co musisz stopniowo poprawiać.

## Świetna robota! Kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować pogłębianie wiedzy o generatywnej AI!

Przejdź do Lekcji 2, gdzie przyjrzymy się, jak [eksplorować i porównywać różne typy LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku krytycznych informacji zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.