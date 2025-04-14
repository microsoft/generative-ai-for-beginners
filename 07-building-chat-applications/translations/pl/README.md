# Budowanie Aplikacji Czatowych Opartych na Generatywnej Sztucznej Inteligencji

[![Budowanie Aplikacji Czatowych Opartych na Generatywnej Sztucznej Inteligencji](../../images/07-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lessons7-gh?WT.mc_id=academic-105485-koreyst)

> _(Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji)_

Teraz, gdy zobaczyliśmy, jak możemy budować aplikacje generujące tekst, przyjrzyjmy się aplikacjom czatowym.

Aplikacje czatowe stały się integralną częścią naszego codziennego życia, oferując więcej niż tylko środek do prowadzenia swobodnych rozmów. Są one nieodłącznymi elementami obsługi klienta, wsparcia technicznego, a nawet zaawansowanych systemów doradczych. Istnieje duże prawdopodobieństwo, że niedawno otrzymałeś pomoc od aplikacji czatowej. Wraz z integracją bardziej zaawansowanych technologii, takich jak generatywna sztuczna inteligencja, w te platformy, złożoność wzrasta, a wraz z nią wyzwania.

Niektóre pytania, na które musimy znaleźć odpowiedzi, to:

- **Budowanie aplikacji**. Jak efektywnie budować i bezproblemowo integrować te aplikacje wykorzystujące sztuczną inteligencję dla konkretnych przypadków użycia?
- **Monitorowanie**. Po wdrożeniu, jak możemy monitorować i zapewnić, że aplikacje działają na najwyższym poziomie jakości, zarówno pod względem funkcjonalności, jak i zgodności z [sześcioma zasadami odpowiedzialnej sztucznej inteligencji](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

W miarę jak wkraczamy w erę zdefiniowaną przez automatyzację i bezproblemowe interakcje człowiek-maszyna, zrozumienie, jak generatywna sztuczna inteligencja przekształca zakres, głębię i adaptowalność aplikacji czatowych staje się niezbędne. Ta lekcja zbada aspekty architektury, które wspierają te złożone systemy, zagłębi się w metodologie ich dostosowywania do zadań specyficznych dla danej domeny oraz oceni metryki i względy związane z zapewnieniem odpowiedzialnego wdrażania sztucznej inteligencji.

## Wprowadzenie

Ta lekcja obejmuje:

- Techniki efektywnego budowania i integrowania aplikacji czatowych.
- Jak stosować dostosowanie i fine-tuning do aplikacji.
- Strategie i rozważania dotyczące efektywnego monitorowania aplikacji czatowych.

## Cele nauki

Po zakończeniu tej lekcji będziesz w stanie:

- Opisać rozważania dotyczące budowania i integrowania aplikacji czatowych z istniejącymi systemami.
- Dostosować aplikacje czatowe do konkretnych przypadków użycia.
- Zidentyfikować kluczowe metryki i rozważania w celu efektywnego monitorowania i utrzymania jakości aplikacji czatowych opartych na sztucznej inteligencji.
- Zapewnić, że aplikacje czatowe wykorzystują sztuczną inteligencję w odpowiedzialny sposób.

## Integracja Generatywnej Sztucznej Inteligencji w Aplikacje Czatowe

Podnoszenie poziomu aplikacji czatowych poprzez generatywną sztuczną inteligencję nie koncentruje się wyłącznie na tym, aby były one inteligentniejsze; chodzi o optymalizację ich architektury, wydajności i interfejsu użytkownika, aby zapewnić jakościowe doświadczenie użytkownika. Wymaga to zbadania podstaw architektonicznych, integracji API i rozważań dotyczących interfejsu użytkownika. Celem tej sekcji jest zaoferowanie kompleksowej mapy drogowej do nawigacji po tych złożonych krajobrazach, niezależnie od tego, czy włączasz je do istniejących systemów, czy budujesz je jako samodzielne platformy.

Po zakończeniu tej sekcji będziesz wyposażony w wiedzę niezbędną do efektywnego konstruowania i włączania aplikacji czatowych.

### Chatbot czy aplikacja czatowa?

Zanim zagłębimy się w budowanie aplikacji czatowych, porównajmy 'chatboty' z 'aplikacjami czatowymi opartymi na sztucznej inteligencji', które pełnią odrębne role i funkcje. Głównym celem chatbota jest automatyzacja określonych zadań konwersacyjnych, takich jak odpowiadanie na często zadawane pytania lub śledzenie paczki. Zazwyczaj jest on regulowany przez logikę opartą na regułach lub złożone algorytmy sztucznej inteligencji. W przeciwieństwie do tego, aplikacja czatowa oparta na sztucznej inteligencji to znacznie bardziej rozbudowane środowisko zaprojektowane do ułatwiania różnych form komunikacji cyfrowej, takich jak czaty tekstowe, głosowe i wideo między ludzkimi użytkownikami. Jej cechą charakterystyczną jest integracja generatywnego modelu sztucznej inteligencji, który symuluje niuansowe, ludzkie rozmowy, generując odpowiedzi w oparciu o szeroką gamę danych wejściowych i wskazówek kontekstowych. Aplikacja czatowa oparta na generatywnej sztucznej inteligencji może angażować się w dyskusje otwartej domeny, dostosowywać się do zmieniających się kontekstów konwersacyjnych, a nawet tworzyć kreatywne lub złożone dialogi.

Poniższa tabela przedstawia kluczowe różnice i podobieństwa, aby pomóc nam zrozumieć ich unikalne role w komunikacji cyfrowej.

| Chatbot                                        | Aplikacja Czatowa oparta na Generatywnej SI |
| ---------------------------------------------- | ------------------------------------------- |
| Skupiony na zadaniach i oparty na regułach     | Świadomy kontekstu                          |
| Często zintegrowany z większymi systemami      | Może obsługiwać jednego lub wiele chatbotów |
| Ograniczony do zaprogramowanych funkcji        | Integruje generatywne modele SI             |
| Wyspecjalizowane i ustrukturyzowane interakcje | Zdolny do dyskusji otwartej domeny          |

### Wykorzystanie gotowych funkcjonalności za pomocą SDK i API

Przy budowaniu aplikacji czatowej świetnym pierwszym krokiem jest ocena tego, co już istnieje. Korzystanie z SDK i API do budowania aplikacji czatowych jest korzystną strategią z różnych powodów. Integrując dobrze udokumentowane SDK i API, strategicznie pozycjonujesz swoją aplikację na długoterminowy sukces, adresując problemy skalowalności i konserwacji.

- **Przyspiesza proces rozwoju i zmniejsza nakłady**: Poleganie na gotowych funkcjonalnościach zamiast kosztownego procesu budowania ich samodzielnie pozwala skupić się na innych aspektach aplikacji, które mogą być dla Ciebie ważniejsze, takich jak logika biznesowa.
- **Lepsza wydajność**: Budując funkcjonalność od podstaw, w końcu zadasz sobie pytanie "Jak to się skaluje? Czy ta aplikacja jest w stanie obsłużyć nagły napływ użytkowników?" Dobrze utrzymywane SDK i API często mają wbudowane rozwiązania tych problemów.
- **Łatwiejsza konserwacja**: Aktualizacje i ulepszenia są łatwiejsze do zarządzania, ponieważ większość API i SDK wymaga jedynie aktualizacji biblioteki, gdy zostanie wydana nowsza wersja.
- **Dostęp do najnowocześniejszych technologii**: Wykorzystanie modeli, które zostały dostrojone i wytrenowane na obszernych zbiorach danych, zapewnia Twojej aplikacji możliwości przetwarzania języka naturalnego.

Dostęp do funkcjonalności SDK lub API zazwyczaj wymaga uzyskania pozwolenia na korystanie z dostarczanych usług, co często odbywa się poprzez użycie unikalnego klucza lub tokenu uwierzytelniającego. Użyjemy Biblioteki Python OpenAI, aby zobaczyć, jak to wygląda. Możesz także spróbować samodzielnie w następującym [notatniku dla OpenAI](../../python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) lub [notatniku dla Usług Azure OpenAI](../../python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) do tej lekcji.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Zaproponuj dwa tytuły dla instruktażowej lekcji o aplikacjach czatowych dla generatywnej SI."}])
```

Powyższy przykład używa modelu GPT-3.5 Turbo do uzupełnienia promptu, ale zauważ, że klucz API jest ustawiony przed tym. Otrzymałbyś błąd, gdybyś nie ustawił klucza.

## Doświadczenie Użytkownika (UX)

Ogólne zasady UX mają zastosowanie do aplikacji czatowych, ale oto kilka dodatkowych rozważań, które stają się szczególnie ważne ze względu na zaangażowane komponenty uczenia maszynowego.

- **Mechanizm do adresowania niejednoznaczności**: Generatywne modele SI czasami generują niejednoznaczne odpowiedzi. Funkcja, która pozwala użytkownikom prosić o wyjaśnienie, może być pomocna, jeśli napotkają ten problem.
- **Zapamiętywanie kontekstu**: Zaawansowane generatywne modele SI mają zdolność zapamiętywania kontekstu w ramach rozmowy, co może być niezbędnym atutem dla doświadczenia użytkownika. Danie użytkownikom możliwości kontrolowania i zarządzania kontekstem poprawia doświadczenie użytkownika, ale wprowadza ryzyko przechowywania wrażliwych informacji o użytkowniku. Rozważania dotyczące tego, jak długo te informacje są przechowywane, takie jak wprowadzenie polityki przechowywania, mogą zrównoważyć potrzebę kontekstu z prywatnością.
- **Personalizacja**: Dzięki zdolności do uczenia się i adaptacji, modele SI oferują zindywidualizowane doświadczenie dla użytkownika. Dostosowanie doświadczenia użytkownika poprzez funkcje takie jak profile użytkownika nie tylko sprawia, że użytkownik czuje się zrozumiany, ale także pomaga mu w poszukiwaniu konkretnych odpowiedzi, tworząc bardziej efektywną i satysfakcjonującą interakcję.

Jednym z takich przykładów personalizacji są ustawienia "Instrukcje niestandardowe" w ChatGPT od OpenAI. Pozwala to na dostarczenie informacji o sobie, które mogą być ważnym kontekstem dla Twoich promptów. Oto przykład niestandardowej instrukcji.

![Ustawienia Instrukcji Niestandardowych w ChatGPT](../../images/custom-instructions.png?WT.mc_id=academic-105485-koreyst)

Ten "profil" skłania ChatGPT do stworzenia planu lekcji na temat list powiązanych. Zauważ, że ChatGPT bierze pod uwagę, że użytkownik może chcieć bardziej szczegółowego planu lekcji w oparciu o jej doświadczenie.

![Prompt w ChatGPT dotyczący planu lekcji o listach powiązanych](../../images/lesson-plan-prompt.png?WT.mc_id=academic-105485-koreyst)

### Struktura Komunikatów Systemowych Microsoft dla Dużych Modeli Językowych

[Microsoft dostarczył wytyczne](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) dotyczące pisania efektywnych komunikatów systemowych podczas generowania odpowiedzi z LLM, podzielone na 4 obszary:

1. Definiowanie dla kogo jest model, a także jego możliwości i ograniczenia.
2. Definiowanie formatu wyjściowego modelu.
3. Dostarczanie konkretnych przykładów, które demonstrują zamierzone zachowanie modelu.
4. Dostarczanie dodatkowych barier zachowania.

### Dostępność

Niezależnie od tego, czy użytkownik ma upośledzenia wzroku, słuchu, motoryki czy poznawcze, dobrze zaprojektowana aplikacja czatowa powinna być użyteczna dla wszystkich. Poniższa lista przedstawia konkretne funkcje mające na celu poprawę dostępności dla różnych upośledzeń użytkowników.

- **Funkcje dla Osób z Upośledzeniem Wzroku**: Motywy o wysokim kontraście i tekst o zmiennym rozmiarze, kompatybilność z czytnikami ekranu.
- **Funkcje dla Osób z Upośledzeniem Słuchu**: Funkcje zamiany tekstu na mowę i mowy na tekst, wizualne wskazówki dla powiadomień dźwiękowych.
- **Funkcje dla Osób z Upośledzeniem Motoryki**: Wsparcie dla nawigacji klawiaturą, komendy głosowe.
- **Funkcje dla Osób z Upośledzeniem Poznawczym**: Opcje uproszczonego języka.

## Dostosowanie i Fine-tuning dla Modeli Językowych Specyficznych dla Domeny

Wyobraź sobie aplikację czatową, która rozumie żargon Twojej firmy i przewiduje konkretne zapytania, które często ma jej baza użytkowników. Istnieje kilka podejść wartych wspomnienia:

- **Wykorzystanie modeli DSL**. DSL oznacza język specyficzny dla domeny. Możesz wykorzystać tak zwany model DSL wytrenowany w konkretnej domenie, aby zrozumieć jej koncepcje i scenariusze.
- **Zastosowanie fine-tuningu**. Fine-tuning to proces dalszego trenowania modelu za pomocą konkretnych danych.

## Dostosowanie: Używanie DSL

Wykorzystanie modeli języka specyficznego dla domeny (modele DSL) może zwiększyć zaangażowanie użytkowników, zapewniając wyspecjalizowane, kontekstowo istotne interakcje. Jest to model, który jest trenowany lub dostrajany, aby zrozumieć i generować tekst związany z konkretnym obszarem, branżą lub tematem. Opcje używania modelu DSL mogą się różnić od trenowania go od podstaw, po korzystanie z istniejących poprzez SDK i API. Inną opcją jest fine-tuning, który polega na wzięciu istniejącego wstępnie wytrenowanego modelu i dostosowaniu go do konkretnej domeny.

## Dostosowanie: Zastosowanie fine-tuningu

Fine-tuning jest często rozważany, gdy wstępnie wytrenowany model nie spełnia wymagań w wyspecjalizowanej domenie lub konkretnym zadaniu.

Na przykład, zapytania medyczne są złożone i wymagają dużo kontekstu. Kiedy lekarz diagnozuje pacjenta, opiera się na różnych czynnikach, takich jak styl życia czy istniejące wcześniej schorzenia, a nawet może polegać na najnowszych czasopismach medycznych, aby zweryfikować swoją diagnozę. W tak niuansowych scenariuszach, ogólna aplikacja czatowa SI nie może być niezawodnym źródłem.

### Scenariusz: aplikacja medyczna

Rozważ aplikację czatową zaprojektowaną, aby pomóc pracownikom medycznym, zapewniając szybkie odniesienia do wytycznych leczenia, interakcji leków lub najnowszych wyników badań.

Model ogólnego przeznaczenia może być odpowiedni do odpowiadania na podstawowe pytania medyczne lub udzielania ogólnych porad, ale może mieć trudności z następującymi kwestiami:

- **Bardzo konkretne lub złożone przypadki**. Na przykład, neurolog może zapytać aplikację: "Jakie są obecnie najlepsze praktyki w zarządzaniu lekoopornymi epilepsjami u pacjentów pediatrycznych?"
- **Brak najnowszych postępów**. Model ogólnego przeznaczenia może mieć trudności z dostarczeniem aktualnej odpowiedzi, która uwzględnia najnowsze postępy w neurologii i farmakologii.

W takich przypadkach dostrojenie modelu za pomocą wyspecjalizowanego zbioru danych medycznych może znacznie poprawić jego zdolność do obsługi tych złożonych zapytań medycznych bardziej dokładnie i niezawodnie. Wymaga to dostępu do dużego i odpowiedniego zbioru danych, który reprezentuje wyzwania i pytania specyficzne dla domeny, które muszą być zaadresowane.

## Rozważania dla Wysokiej Jakości Doświadczenia Czatowego Opartego na SI

Ta sekcja przedstawia kryteria dla "wysokiej jakości" aplikacji czatowych, które obejmują przechwytywanie przydatnych metryk i przestrzeganie ram, które odpowiedzialnie wykorzystują technologię SI.

### Kluczowe Metryki

Aby utrzymać wysoką jakość działania aplikacji, niezbędne jest śledzenie kluczowych metryk i rozważań. Te pomiary nie tylko zapewniają funkcjonalność aplikacji, ale także oceniają jakość modelu SI i doświadczenia użytkownika. Poniżej znajduje się lista, która obejmuje podstawowe metryki, metryki SI i doświadczenia użytkownika, które należy rozważyć.

| Metryka                             | Definicja                                                                                                       | Rozważania dla Dewelopera Czatu                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Czas działania**                  | Mierzy czas, w którym aplikacja jest operacyjna i dostępna dla użytkowników.                                    | Jak zminimalizujesz przestoje?                                                        |
| **Czas odpowiedzi**                 | Czas, jaki aplikacja potrzebuje, aby odpowiedzieć na zapytanie użytkownika.                                     | Jak zoptymalizujesz przetwarzanie zapytań, aby poprawić czas odpowiedzi?              |
| **Precyzja**                        | Stosunek prawdziwie pozytywnych przewidywań do całkowitej liczby pozytywnych przewidywań                        | Jak zwalidować precyzję swojego modelu?                                               |
| **Recall (Czułość)**                | Stosunek prawdziwie pozytywnych przewidywań do rzeczywistej liczby pozytywów                                    | Jak zmierzysz i poprawisz czułość?                                                    |
| **Wskaźnik F1**                     | Średnia harmoniczna precyzji i czułości, która równoważy kompromis między nimi.                                 | Jaki jest Twój docelowy wskaźnik F1? Jak zrównoważysz precyzję i czułość?             |
| **Perplexity**                      | Mierzy, jak dobrze rozkład prawdopodobieństwa przewidziany przez model pasuje do rzeczywistego rozkładu danych. | Jak zminimalizujesz perplexity?                                                       |
| **Metryki satysfakcji użytkownika** | Mierzy percepcję aplikacji przez użytkownika. Często przechwytywane przez ankiety.                              | Jak często będziesz zbierać opinie użytkowników? Jak się dostosujesz w oparciu o nie? |
| **Częstość błędów**                 | Częstość, z jaką model popełnia błędy w zrozumieniu lub wynikach.                                               | Jakie strategie masz na miejscu, aby zmniejszyć częstość błędów?                      |
| **Cykle ponownego trenowania**      | Częstotliwość, z jaką model jest aktualizowany, aby uwzględnić nowe dane i spostrzeżenia.                       | Jak często będziesz ponownie trenować model? Co wyzwala cykl ponownego trenowania?    |
| **Wykrywanie anomalii**             | Narzędzia i techniki do identyfikacji niezwykłych wzorców, które nie są zgodne z oczekiwanym zachowaniem.       | Jak zareagujesz na anomalie?                                                          |

### Wdrażanie Praktyk Odpowiedzialnej SI w Aplikacjach Czatowych

Podejście Microsoftu do Odpowiedzialnej SI zidentyfikowało sześć zasad, które powinny kierować rozwojem i wykorzystaniem SI. Poniżej znajdują się zasady, ich definicja oraz rzeczy, które deweloper czatu powinien rozważyć i dlaczego powinien je traktować poważnie.

| Zasady                        | Definicja Microsoftu                                         | Rozważania dla Dewelopera Czatu                                                     | Dlaczego To Jest Ważne                                                                |
| ----------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Sprawiedliwość                | Systemy SI powinny traktować wszystkich ludzi sprawiedliwie. | Upewnij się, że aplikacja czatowa nie dyskryminuje na podstawie danych użytkownika. | Aby budować zaufanie i inkluzywność wśród użytkowników; unikać konsekwencji prawnych. |
| Niezawodność i Bezpieczeństwo | Systemy SI powinny działać niezawodnie i bezpiecznie.        | Wdrażaj testy i zabezpieczenia, aby zminimalizować błędy i ryzyka.                  | Zapewnia satysfakcję użytkownika i zapobiega potencjalnym szkodom.                    |
| Prywatność i Bezpieczeństwo   | Systemy SI powinny być bezpieczne i szanować prywatność.     | Wdrażaj silne szyfrowanie i środki ochrony danych.                                  | Aby chronić wrażliwe dane użytkowników i przestrzegać praw prywatności.               |
| Inkluzywność                  | Systemy SI powinny wzmacniać wszystkich i angażować ludzi.   | Projektuj UI/UX, które jest dostępne i łatwe w użyciu dla różnorodnych odbiorców.   | Zapewnia, że szerszy zakres osób może efektywnie korzystać z aplikacji.               |
| Przejrzystość                 | Systemy SI powinny być zrozumiałe.                           | Zapewnij jasną dokumentację i uzasadnienie dla odpowiedzi SI.                       | Użytkownicy bardziej ufają systemowi, jeśli rozumieją, jak podejmowane są decyzje.    |
| Odpowiedzialność              | Ludzie powinni być odpowiedzialni za systemy SI.             | Ustanów jasny proces audytu i poprawy decyzji SI.                                   | Umożliwia ciągłe udoskonalanie i środki korygujące w przypadku błędów.                |

## Zadanie

Zobacz [zadanie](../../python?WT.mc_id=academic-105485-koreyst), które przeprowadzi Cię przez serię ćwiczeń od uruchomienia pierwszych promptów czatowych, po klasyfikację i podsumowywanie tekstu i więcej. Zauważ, że zadania są dostępne w różnych językach programowania!

## Świetna Praca! Kontynuuj Podróż

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję Edukacyjną Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby nadal podnosić swoją wiedzę o Generatywnej SI!

Przejdź do Lekcji 8, aby zobaczyć, jak możesz zacząć [budować aplikacje wyszukiwania](../../../08-building-search-applications/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
