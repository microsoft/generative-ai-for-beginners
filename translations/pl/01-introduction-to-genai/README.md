<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T09:51:24+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do Generatywnej AI i Dużych Modeli Językowych

_(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

Generatywna AI to sztuczna inteligencja zdolna do generowania tekstu, obrazów i innych typów treści. To, co czyni ją fantastyczną technologią, to fakt, że demokratyzuje AI - każdy może z niej korzystać, mając jedynie tekstowy prompt, zdanie napisane w języku naturalnym. Nie musisz uczyć się języka takiego jak Java czy SQL, aby osiągnąć coś wartościowego, wystarczy, że użyjesz swojego języka, określisz, czego chcesz, a model AI przedstawi Ci sugestię. Aplikacje i wpływ tej technologii są ogromne: możesz pisać lub rozumieć raporty, tworzyć aplikacje i wiele więcej, wszystko w kilka sekund.

W tym programie nauczania zbadamy, jak nasz startup wykorzystuje generatywną AI do otwierania nowych scenariuszy w świecie edukacji oraz jak radzimy sobie z nieuniknionymi wyzwaniami związanymi z społecznymi implikacjami jej zastosowania i ograniczeniami technologicznymi.

## Wprowadzenie

Ta lekcja obejmie:

- Wprowadzenie do scenariusza biznesowego: nasz pomysł na startup i misja.
- Generatywna AI i jak dotarliśmy do obecnego krajobrazu technologicznego.
- Wewnętrzne działanie dużego modelu językowego.
- Główne możliwości i praktyczne zastosowania Dużych Modeli Językowych.

## Cele nauki

Po ukończeniu tej lekcji będziesz rozumieć:

- Czym jest generatywna AI i jak działają Duże Modele Językowe.
- Jak można wykorzystać duże modele językowe do różnych zastosowań, ze szczególnym uwzględnieniem scenariuszy edukacyjnych.

## Scenariusz: nasz edukacyjny startup

Generatywna Sztuczna Inteligencja (AI) reprezentuje szczyt technologii AI, przesuwając granice tego, co wcześniej uważano za niemożliwe. Modele generatywnej AI mają wiele możliwości i zastosowań, ale w tym programie nauczania zbadamy, jak rewolucjonizuje edukację poprzez fikcyjny startup. Będziemy odnosić się do tego startupu jako _nasz startup_. Nasz startup działa w dziedzinie edukacji z ambitnym oświadczeniem misji

> _poprawa dostępności w nauce na skalę globalną, zapewnienie równego dostępu do edukacji i dostarczanie spersonalizowanych doświadczeń edukacyjnych każdemu uczniowi, zgodnie z jego potrzebami_.

Zespół naszego startupu zdaje sobie sprawę, że nie będziemy w stanie osiągnąć tego celu bez wykorzystania jednego z najpotężniejszych narzędzi współczesnych czasów – Dużych Modeli Językowych (LLM).

Oczekuje się, że generatywna AI zrewolucjonizuje sposób, w jaki uczymy się i nauczamy dzisiaj, z uczniami mającymi do dyspozycji wirtualnych nauczycieli przez 24 godziny na dobę, którzy dostarczają ogromnych ilości informacji i przykładów, a nauczyciele mogą wykorzystywać innowacyjne narzędzia do oceny swoich uczniów i udzielania im informacji zwrotnej.

Aby zacząć, zdefiniujmy kilka podstawowych pojęć i terminologii, które będziemy używać w całym programie nauczania.

## Jak zdobyliśmy Generatywną AI?

Pomimo niezwykłego _szumu_ wywołanego ostatnio przez ogłoszenie modeli generatywnej AI, ta technologia jest rozwijana od dekad, z pierwszymi badaniami sięgającymi lat 60. Jesteśmy teraz na etapie, w którym AI ma ludzkie zdolności poznawcze, jak rozmowa, co pokazują na przykład [OpenAI ChatGPT](https://openai.com/chatgpt) czy [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), który również używa modelu GPT do wyszukiwania w sieci Bing.

Wracając nieco wstecz, pierwsze prototypy AI składały się z czatbotów pisanych na maszynie, opierających się na bazie wiedzy wyekstrahowanej od grupy ekspertów i reprezentowanej w komputerze. Odpowiedzi w bazie wiedzy były wywoływane przez słowa kluczowe pojawiające się w tekście wejściowym. Jednak szybko stało się jasne, że takie podejście, wykorzystujące czatboty pisane na maszynie, nie skalowało się dobrze.

### Statystyczne podejście do AI: Uczenie maszynowe

Punkt zwrotny nastąpił w latach 90., wraz z zastosowaniem statystycznego podejścia do analizy tekstu. Doprowadziło to do rozwoju nowych algorytmów – znanych jako uczenie maszynowe – zdolnych do uczenia się wzorców z danych bez potrzeby jawnego programowania. To podejście pozwala maszynom symulować rozumienie języka ludzkiego: model statystyczny jest trenowany na parach tekst-etykieta, co umożliwia modelowi klasyfikację nieznanego tekstu wejściowego za pomocą z góry zdefiniowanej etykiety reprezentującej intencję wiadomości.

### Sieci neuronowe i nowoczesni wirtualni asystenci

W ostatnich latach, technologiczna ewolucja sprzętu, zdolnego do obsługi większych ilości danych i bardziej złożonych obliczeń, zachęciła do badań nad AI, prowadząc do rozwoju zaawansowanych algorytmów uczenia maszynowego znanych jako sieci neuronowe lub algorytmy głębokiego uczenia.

Sieci neuronowe (a w szczególności Recurrent Neural Networks – RNN) znacząco poprawiły przetwarzanie języka naturalnego, umożliwiając reprezentację znaczenia tekstu w bardziej znaczący sposób, ceniąc kontekst słowa w zdaniu.

To jest technologia, która napędzała wirtualnych asystentów powstałych w pierwszej dekadzie nowego wieku, bardzo biegłych w interpretacji języka ludzkiego, identyfikacji potrzeby i wykonywaniu działania, aby ją zaspokoić – jak odpowiadanie z wcześniej zdefiniowanym skryptem lub korzystanie z usługi zewnętrznej.

### Obecnie, Generatywna AI

Tak dotarliśmy do Generatywnej AI dzisiaj, która może być postrzegana jako podzbiór głębokiego uczenia.

Po dekadach badań w dziedzinie AI, nowa architektura modelu – nazwana _Transformer_ – pokonała ograniczenia RNN, będąc zdolna do przyjmowania znacznie dłuższych sekwencji tekstu jako wejścia. Transformatory opierają się na mechanizmie uwagi, umożliwiając modelowi nadawanie różnym wagom wejściom, które otrzymuje, 'zwracając większą uwagę' tam, gdzie skoncentrowane są najbardziej istotne informacje, niezależnie od ich kolejności w sekwencji tekstu.

Większość najnowszych modeli generatywnej AI – znanych również jako Duże Modele Językowe (LLM), ponieważ pracują z tekstowymi wejściami i wyjściami – opiera się na tej architekturze. Co ciekawe, te modele – trenowane na ogromnej ilości danych nieoznaczonych z różnych źródeł, takich jak książki, artykuły i strony internetowe – mogą być dostosowane do szerokiej gamy zadań i generować gramatycznie poprawny tekst z pozorem kreatywności. Więc nie tylko znacząco zwiększyły zdolność maszyny do 'rozumienia' tekstu wejściowego, ale umożliwiły również generowanie oryginalnej odpowiedzi w języku ludzkim.

## Jak działają duże modele językowe?

W następnym rozdziale zbadamy różne typy modeli generatywnej AI, ale na razie przyjrzyjmy się, jak działają duże modele językowe, z naciskiem na modele OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizer, tekst na liczby**: Duże Modele Językowe przyjmują tekst jako wejście i generują tekst jako wyjście. Jednak, jako modele statystyczne, działają znacznie lepiej z liczbami niż sekwencjami tekstu. Dlatego każde wejście do modelu jest przetwarzane przez tokenizer, zanim zostanie użyte przez główny model. Token to fragment tekstu – składający się z różnej liczby znaków, więc głównym zadaniem tokenizera jest podzielenie wejścia na tablicę tokenów. Następnie każdy token jest mapowany z indeksem tokenu, który jest kodowaniem całkowitym oryginalnego fragmentu tekstu.

- **Przewidywanie tokenów wyjściowych**: Dla n tokenów jako wejścia (z maksymalnym n różnym dla każdego modelu), model jest w stanie przewidzieć jeden token jako wyjście. Ten token jest następnie włączany do wejścia następnej iteracji, w rozszerzającym się wzorcu okna, umożliwiając lepsze doświadczenie użytkownika, otrzymując jedno (lub więcej) zdanie jako odpowiedź. To wyjaśnia, dlaczego, jeśli kiedykolwiek bawiłeś się ChatGPT, mogłeś zauważyć, że czasami wygląda, jakby zatrzymywał się w środku zdania.

- **Proces selekcji, rozkład prawdopodobieństwa**: Token wyjściowy jest wybierany przez model w zależności od jego prawdopodobieństwa wystąpienia po bieżącej sekwencji tekstu. Dzieje się tak, ponieważ model przewiduje rozkład prawdopodobieństwa dla wszystkich możliwych 'następnych tokenów', obliczony na podstawie jego treningu. Jednak nie zawsze token o najwyższym prawdopodobieństwie jest wybierany z wynikowego rozkładu. Do tego wyboru dodawany jest stopień losowości, w taki sposób, że model działa w sposób niedeterministyczny - nie otrzymujemy dokładnie tego samego wyniku dla tego samego wejścia. Ten stopień losowości jest dodawany, aby symulować proces kreatywnego myślenia i można go dostroić za pomocą parametru modelu zwanego temperaturą.

## Jak nasz startup może wykorzystać Duże Modele Językowe?

Teraz, gdy mamy lepsze zrozumienie wewnętrznego działania dużego modelu językowego, zobaczmy kilka praktycznych przykładów najczęstszych zadań, które mogą one wykonywać całkiem dobrze, z uwzględnieniem naszego scenariusza biznesowego. Powiedzieliśmy, że główną zdolnością Dużego Modelu Językowego jest _generowanie tekstu od zera, zaczynając od tekstowego wejścia, napisanego w języku naturalnym_.

Ale jaki rodzaj tekstowego wejścia i wyjścia?
Wejście dużego modelu językowego jest znane jako prompt, podczas gdy wyjście jest znane jako completion, termin odnoszący się do mechanizmu modelu generowania następnego tokenu, aby uzupełnić bieżące wejście. Zagłębimy się w to, czym jest prompt i jak go zaprojektować w sposób, aby uzyskać jak najwięcej z naszego modelu. Ale na razie, powiedzmy tylko, że prompt może obejmować:

- **Instrukcję** określającą typ wyjścia, którego oczekujemy od modelu. Ta instrukcja czasami może zawierać przykłady lub dodatkowe dane.

  1. Podsumowanie artykułu, książki, recenzji produktów i innych, wraz z ekstrakcją wniosków z danych nieustrukturyzowanych.
  
  2. Kreatywne tworzenie i projektowanie artykułu, eseju, zadania lub więcej.

- **Pytanie**, zadane w formie rozmowy z agentem.

- Fragment **tekstu do uzupełnienia**, który implicite jest prośbą o pomoc w pisaniu.

- Fragment **kodu** wraz z prośbą o wyjaśnienie i dokumentację, lub komentarz proszący o wygenerowanie fragmentu kodu wykonującego określone zadanie.

Powyższe przykłady są dość proste i nie są przeznaczone do wyczerpującej demonstracji możliwości Dużych Modeli Językowych. Mają one na celu pokazanie potencjału wykorzystania generatywnej AI, w szczególności, ale nie tylko w kontekstach edukacyjnych.

Ponadto, wyjście modelu generatywnej AI nie jest doskonałe i czasami kreatywność modelu może działać na jego niekorzyść, skutkując wyjściem, które jest kombinacją słów, które użytkownik ludzki może interpretować jako mistyfikację rzeczywistości, lub może być obraźliwe. Generatywna AI nie jest inteligentna - przynajmniej w bardziej kompleksowej definicji inteligencji, obejmującej krytyczne i kreatywne rozumowanie czy inteligencję emocjonalną; nie jest deterministyczna i nie jest godna zaufania, ponieważ fabrykacje, takie jak błędne odniesienia, treści i stwierdzenia, mogą być łączone z poprawnymi informacjami i przedstawiane w przekonujący i pewny sposób. W kolejnych lekcjach będziemy zajmować się wszystkimi tymi ograniczeniami i zobaczymy, co możemy zrobić, aby je złagodzić.

## Zadanie

Twoim zadaniem jest przeczytanie więcej na temat [generatywnej AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) i próba zidentyfikowania obszaru, w którym dzisiaj dodałbyś generatywną AI, która jej nie posiada. Jakie byłyby różnice w porównaniu do robienia tego "starym sposobem", czy możesz zrobić coś, czego wcześniej nie mogłeś, lub czy jesteś szybszy? Napisz 300-słowowe podsumowanie, jak wyglądałby Twój wymarzony startup AI i uwzględnij nagłówki takie jak "Problem", "Jak wykorzystałbym AI", "Wpływ" i opcjonalnie plan biznesowy.

Jeśli wykonałeś to zadanie, możesz być nawet gotowy, aby aplikować do inkubatora Microsoftu, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) oferujemy kredyty zarówno na Azure, OpenAI, mentoring i wiele więcej, sprawdź to!

## Sprawdzenie wiedzy

Co jest prawdą o dużych modelach językowych?

1. Otrzymujesz dokładnie tę samą odpowiedź za każdym razem.
2. Działa perfekcyjnie, świetnie dodaje liczby, tworzy działający kod itp.
3. Odpowiedź może się różnić mimo użycia tego samego promptu. Jest również świetna w dawaniu Ci pierwszego szkicu czegoś, czy to tekstu, czy kodu. Ale musisz poprawić wyniki.

A: 3, LLM jest niedeterministyczny, odpowiedź się różni, jednak możesz kontrolować jej zmienność za pomocą ustawienia temperatury. Nie powinieneś również oczekiwać, że będzie działać perfekcyjnie, jest tu, aby wykonywać ciężką pracę za Ciebie, co często oznacza, że otrzymujesz dobry pierwszy krok do czegoś, co musisz stopniowo poprawiać.

## Świetna robota! Kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie poziomu swojej wiedzy o Generatywnej AI!

Przejdź do Lekcji 2, gdzie przyjrzymy się, jak [eksplorować i porównywać różne typy LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.