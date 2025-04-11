# Wprowadzenie do Generatywnej Sztucznej Inteligencji i Dużych Modeli Językowych

[![Wprowadzenie do Generatywnej Sztucznej Inteligencji i Dużych Modeli Językowych](../../images/01-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

_(Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji)_

Generatywna SI to sztuczna inteligencja zdolna do generowania tekstu, obrazów i innych rodzajów treści. To, co czyni ją fantastyczną technologią, to fakt, że demokratyzuje ona sztuczną inteligencję - każdy może z niej korzystać, używając jedynie polecenia tekstowego, zdania napisanego w języku naturalnym. Nie ma potrzeby uczenia się języka takiego jak Java czy SQL, aby osiągnąć coś wartościowego - wystarczy użyć własnego języka, określić czego się potrzebuje, a model SI przedstawi sugestię. Zastosowania i wpływ tej technologii są ogromne - możesz pisać lub analizować raporty, tworzyć aplikacje i wiele więcej, wszystko w ciągu kilku sekund.

W tym kursie zbadamy, jak nasz startup wykorzystuje generatywną SI do odblokowania nowych scenariuszy w świecie edukacji i jak radzimy sobie z nieodłącznymi wyzwaniami związanymi z implikacjami społecznymi jej zastosowania oraz ograniczeniami technologii.

## Wprowadzenie

Ta lekcja obejmie:

- Wprowadzenie do scenariusza biznesowego: nasz pomysł na startup i misję.
- Generatywną SI i jak doszliśmy do obecnego krajobrazu technologicznego.
- Wewnętrzne działanie dużego modelu językowego.
- Główne możliwości i praktyczne przypadki użycia Dużych Modeli Językowych.

## Cele Nauki

Po ukończeniu tej lekcji zrozumiesz:

- Czym jest generatywna SI i jak działają Duże Modele Językowe.
- Jak możesz wykorzystać duże modele językowe do różnych przypadków użycia, ze szczególnym uwzględnieniem scenariuszy edukacyjnych.

## Scenariusz: nasz edukacyjny startup

Generatywna Sztuczna Inteligencja (SI) reprezentuje szczyt technologii SI, przesuwając granice tego, co kiedyś uważano za niemożliwe. Modele generatywnej SI mają wiele możliwości i zastosowań, ale w tym kursie zbadamy, jak rewolucjonizuje ona edukację poprzez fikcyjny startup. Będziemy odnosić się do tego startupu jako _naszego startupu_. Nasz startup działa w domenie edukacyjnej z ambitną misją:

> _poprawy dostępności w nauce na globalną skalę, zapewniając równy dostęp do edukacji i dostarczając spersonalizowanych doświadczeń edukacyjnych każdemu uczącemu się, zgodnie z jego potrzebami_.

Zespół naszego startupu zdaje sobie sprawę, że nie będziemy w stanie osiągnąć tego celu bez wykorzystania jednego z najpotężniejszych narzędzi współczesności – Dużych Modeli Językowych (Large Language Models, LLM).

Oczekuje się, że Generatywna SI zrewolucjonizuje sposób, w jaki dziś uczymy się i nauczamy, dając studentom do dyspozycji wirtualnych nauczycieli przez 24 godziny na dobę, którzy dostarczają ogromnych ilości informacji i przykładów, a nauczycielom umożliwiając wykorzystanie innowacyjnych narzędzi do oceny swoich uczniów i udzielania im informacji zwrotnych.

![Pięciu młodych studentów patrzących na monitor - obraz wygenerowany przez DALLE2](../../images/students-by-DALLE2.png?WT.mc_id=academic-105485-koreyst)

Na początek zdefiniujmy kilka podstawowych pojęć i terminologię, których będziemy używać w całym kursie.

## Jak doszliśmy do Generatywnej SI?

Pomimo niezwykłego _szumu_ wywołanego ostatnio przez ogłoszenie modeli generatywnej SI, technologia ta rozwijała się przez dekady, a pierwsze wysiłki badawcze sięgają lat 60. Obecnie znajdujemy się w punkcie, w którym SI ma ludzkie zdolności poznawcze, takie jak prowadzenie rozmowy, co pokazują na przykład [OpenAI ChatGPT](https://openai.com/chatgpt) czy [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), który również wykorzystuje model GPT do rozmów w wyszukiwarce Bing.

Cofając się nieco, pierwsze prototypy SI składały się z chatbotów pisanych na maszynie, opierających się na bazie wiedzy uzyskanej od grupy ekspertów i przedstawionej w komputerze. Odpowiedzi z bazy wiedzy były wyzwalane przez słowa kluczowe pojawiające się w tekście wejściowym.
Jednak szybko stało się jasne, że takie podejście, wykorzystujące chatboty pisane na maszynie, nie skalowało się dobrze.

### Statystyczne podejście do SI: Uczenie Maszynowe

Punkt zwrotny nastąpił w latach 90., wraz z zastosowaniem statystycznego podejścia do analizy tekstu. Doprowadziło to do rozwoju nowych algorytmów – znanych jako uczenie maszynowe – zdolnych do uczenia się wzorców z danych bez wyraźnego programowania. To podejście pozwala maszynom symulować ludzkie rozumienie języka: model statystyczny jest trenowany na parach tekst-etykieta, umożliwiając modelowi klasyfikowanie nieznanego tekstu wejściowego z predefiniowaną etykietą reprezentującą intencję wiadomości.

### Sieci neuronowe i nowoczesni wirtualni asystenci

W ostatnich latach ewolucja technologiczna sprzętu, zdolnego do obsługi większych ilości danych i bardziej złożonych obliczeń, zachęciła do badań nad SI, prowadząc do rozwoju zaawansowanych algorytmów uczenia maszynowego znanych jako sieci neuronowe lub algorytmy głębokiego uczenia.

Sieci neuronowe (a szczególnie Rekurencyjne Sieci Neuronowe – RNN) znacznie ulepszyły przetwarzanie języka naturalnego, umożliwiając reprezentację znaczenia tekstu w bardziej znaczący sposób, uwzględniając kontekst słowa w zdaniu.

Jest to technologia, która zasilała wirtualnych asystentów powstałych w pierwszej dekadzie nowego wieku, bardzo biegłych w interpretowaniu ludzkiego języka, identyfikowaniu potrzeby i wykonywaniu działania, aby ją zaspokoić – jak odpowiadanie za pomocą predefiniowanego skryptu lub korzystanie z usługi zewnętrznej.

### Teraźniejszość, Generatywna SI

Tak więc doszliśmy do dzisiejszej Generatywnej SI, którą można postrzegać jako podzbiór głębokiego uczenia.

![SI, ML, DL i Generatywna SI](../../images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)

Po dekadach badań w dziedzinie SI, nowa architektura modelu – zwana _Transformer_ – przezwyciężyła ograniczenia RNN, będąc w stanie pobrać znacznie dłuższe sekwencje tekstu jako dane wejściowe. Transformery opierają się na mechanizmie uwagi (attention mechanism), umożliwiającym modelowi nadawanie różnych wag otrzymywanym danym wejściowym, 'zwracając większą uwagę' tam, gdzie skoncentrowane są najbardziej istotne informacje, niezależnie od ich kolejności w sekwencji tekstu.

Większość najnowszych modeli generatywnej SI – znanych również jako Duże Modele Językowe (LLM), ponieważ pracują z tekstowymi danymi wejściowymi i wyjściowymi – jest rzeczywiście oparta na tej architekturze. Co ciekawe w tych modelach – wytrenowanych na ogromnej ilości nieoznakowanych danych z różnych źródeł, takich jak książki, artykuły i strony internetowe – mogą one być dostosowane do szerokiej gamy zadań i generować gramatycznie poprawny tekst z pozorem kreatywności. Tak więc nie tylko niewiarygodnie zwiększyły zdolność maszyny do 'rozumienia' tekstu wejściowego, ale umożliwiły jej zdolność do generowania oryginalnej odpowiedzi w ludzkim języku.

## Jak działają duże modele językowe?

W następnym rozdziale zbadamy różne typy modeli Generatywnej SI, ale na razie przyjrzyjmy się, jak działają duże modele językowe, skupiając się na modelach OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, tekst na liczby**: Duże Modele Językowe otrzymują tekst jako wejście i generują tekst jako wyjście. Jednak będąc modelami statystycznymi, pracują one znacznie lepiej z liczbami niż z sekwencjami tekstu. Dlatego każde wejście do modelu jest przetwarzane przez tokenizer, zanim zostanie użyte przez rdzeń modelu. Token to fragment tekstu – składający się ze zmiennej liczby znaków, więc głównym zadaniem tokenizera jest podzielenie danych wejściowych na tablicę tokenów. Następnie każdy token jest mapowany z indeksem tokenu, który jest liczbowym kodowaniem oryginalnego fragmentu tekstu.

![Przykład tokenizacji](../../images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

- **Przewidywanie tokenów wyjściowych**: Mając n tokenów jako wejście (z maksymalnym n różniącym się w zależności od modelu), model jest w stanie przewidzieć jeden token jako wyjście. Ten token jest następnie włączany do danych wejściowych w następnej iteracji, w schemacie rozszerzającego się okna, umożliwiając lepsze doświadczenie użytkownika polegające na uzyskaniu jednego (lub wielu) zdania jako odpowiedzi. To wyjaśnia, dlaczego, jeśli kiedykolwiek bawiłeś się ChatGPT, mogłeś zauważyć, że czasami wygląda, jakby zatrzymywał się w środku zdania.

- **Proces selekcji, rozkład prawdopodobieństwa**: Token wyjściowy jest wybierany przez model zgodnie z jego prawdopodobieństwem wystąpienia po bieżącej sekwencji tekstu. Dzieje się tak, ponieważ model przewiduje rozkład prawdopodobieństwa wszystkich możliwych "następnych tokenów", obliczony na podstawie jego treningu. Jednak nie zawsze token o najwyższym prawdopodobieństwie jest wybierany z wynikowego rozkładu. Do tego wyboru dodawany jest stopień losowości, w taki sposób, że model działa w sposób niedeterministyczny - nie otrzymujemy dokładnie takiego samego wyniku dla tych samych danych wejściowych. Ten stopień losowości jest dodawany, aby symulować proces kreatywnego myślenia i może być dostrojony za pomocą parametru modelu zwanego temperaturą.

## Jak nasz startup może wykorzystać Duże Modele Językowe?

Teraz, gdy lepiej rozumiemy wewnętrzne działanie dużego modelu językowego, zobaczmy kilka praktycznych przykładów najczęstszych zadań, które mogą wykonywać całkiem dobrze, mając na uwadze nasz scenariusz biznesowy.
Powiedzieliśmy, że główną zdolnością Dużego Modelu Językowego jest _generowanie tekstu od podstaw, zaczynając od tekstowego wejścia, napisanego w języku naturalnym_.

Ale jaki rodzaj wejścia i wyjścia tekstowego?
Wejście dużego modelu językowego znane jest jako prompt, podczas gdy wyjście znane jest jako uzupełnienie (completion), termin, który odnosi się do mechanizmu modelu generowania następnego tokenu w celu uzupełnienia bieżącego wejścia. Będziemy zagłębiać się w to, czym jest prompt i jak go zaprojektować w sposób umożliwiający uzyskanie jak najwięcej z naszego modelu. Ale na razie powiedzmy tylko, że prompt może zawierać:

- **Instrukcję** określającą rodzaj wyjścia, jakiego oczekujemy od modelu. Ta instrukcja czasami może zawierać przykłady lub dodatkowe dane.

  1. Podsumowanie artykułu, książki, recenzji produktu i więcej, wraz z wydobywaniem wniosków z nieustrukturyzowanych danych.

  ![Przykład podsumowania](../../images/summarization-example.png?WT.mc_id=academic-105485-koreyst)

  2. Kreatywne tworzenie pomysłów i projektowanie artykułu, eseju, zadania lub więcej.

     ![Przykład kreatywnego pisania](../../images/creative-writing-example.png?WT.mc_id=academic-105485-koreyst)

- **Pytanie**, zadane w formie rozmowy z agentem.

  ![Przykład rozmowy](../../images/conversation-example.png?WT.mc_id=academic-105485-koreyst)

- Fragment **tekstu do uzupełnienia**, który w sposób domyślny jest prośbą o pomoc w pisaniu.

  ![Przykład uzupełniania tekstu](../../images/text-completion-example.png?WT.mc_id=academic-105485-koreyst)

- Fragment **kodu** wraz z prośbą o wyjaśnienie i dokumentację, lub komentarz proszący o wygenerowanie fragmentu kodu wykonującego określone zadanie.

  ![Przykład kodowania](../../images/coding-example.png?WT.mc_id=academic-105485-koreyst)

Powyższe przykłady są dość proste i nie mają na celu wyczerpującej demonstracji możliwości Dużych Modeli Językowych. Mają one pokazać potencjał wykorzystania generatywnej SI, w szczególności, ale nie tylko, w kontekstach edukacyjnych.

Ponadto, wyjście modelu generatywnej SI nie jest doskonałe i czasami kreatywność modelu może działać przeciwko niemu, dając w rezultacie kombinację słów, którą ludzki użytkownik może interpretować jako mistyfikację rzeczywistości, lub może być obraźliwa. Generatywna SI nie jest inteligentna - przynajmniej w szerszej definicji inteligencji, obejmującej krytyczne i kreatywne rozumowanie czy inteligencję emocjonalną; nie jest deterministyczna i nie jest godna zaufania, ponieważ zmyślenia, takie jak błędne odniesienia, treści i stwierdzenia, mogą być łączone z poprawnymi informacjami i przedstawiane w przekonujący i pewny sposób. W kolejnych lekcjach będziemy zajmować się wszystkimi tymi ograniczeniami i zobaczymy, co możemy zrobić, aby je złagodzić.

## Zadanie

Twoim zadaniem jest dowiedzieć się więcej o [generatywnej SI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) i spróbować zidentyfikować obszar, w którym dodałbyś generatywną SI dziś, a który jej nie posiada. Jaki byłby wpływ w porównaniu do robienia tego "starym sposobem", czy możesz zrobić coś, czego nie mogłeś wcześniej, czy jesteś szybszy? Napisz podsumowanie liczące 300 słów na temat tego, jak wyglądałby Twój wymarzony startup AI i dodaj nagłówki takie jak "Problem", "Jak wykorzystałbym AI", "Wpływ" i opcjonalnie plan biznesowy.

Jeśli wykonałeś to zadanie, możesz być nawet gotowy, aby aplikować do inkubatora Microsoftu, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) oferujemy kredyty zarówno na Azure, OpenAI, mentoring i wiele więcej, sprawdź to!

## Sprawdzenie wiedzy

Co jest prawdą o dużych modelach językowych?

1. Za każdym razem otrzymujesz dokładnie taką samą odpowiedź.
1. Robi rzeczy perfekcyjnie, świetnie dodaje liczby, produkuje działający kod itp.
1. Odpowiedź może się różnić, mimo używania tego samego promptu. Jest również świetny w dostarczaniu pierwszej wersji czegoś, czy to tekstu, czy kodu. Ale musisz ulepszyć wyniki.

A: 3, LLM jest niedeterministyczny, odpowiedź się różni, jednak możesz kontrolować jej zmienność za pomocą ustawienia temperatury. Nie powinieneś również oczekiwać, że będzie robić rzeczy perfekcyjnie, jest tutaj, aby wykonać za ciebie ciężką pracę, co często oznacza, że otrzymujesz dobrą pierwszą próbę czegoś, co musisz stopniowo ulepszać.

## Świetna praca! Kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję materiałów do nauki Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy o Generatywnej SI!

Przejdź do Lekcji 2, gdzie przyjrzymy się [eksploracji i porównaniu różnych typów LLM](../../../02-exploring-and-comparing-different-llms/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
