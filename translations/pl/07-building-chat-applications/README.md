# Tworzenie aplikacji czatowych zasilanych generatywną sztuczną inteligencją

[![Building Generative AI-Powered Chat Applications](../../../translated_images/pl/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Teraz, gdy zobaczyliśmy, jak możemy tworzyć aplikacje do generowania tekstu, przyjrzyjmy się aplikacjom czatowym.

Aplikacje czatowe stały się integralną częścią naszego codziennego życia, oferując znacznie więcej niż tylko sposób na swobodną rozmowę. Są one nieodłącznym elementem obsługi klienta, wsparcia technicznego, a nawet zaawansowanych systemów doradczych. Prawdopodobnie niedawno korzystałeś z pomocy aplikacji czatowej. W miarę jak integrujemy coraz bardziej zaawansowane technologie, takie jak generatywna SI, w tych platformach, rośnie ich złożoność, a wraz z nią wyzwania.

Niektóre pytania, na które musimy znaleźć odpowiedź, to:

- **Tworzenie aplikacji**. Jak efektywnie budować i bezproblemowo integrować te aplikacje zasilane SI dla konkretnych zastosowań?
- **Monitorowanie**. Po wdrożeniu, jak możemy monitorować i zapewnić, że aplikacje działają na najwyższym poziomie jakości, zarówno pod względem funkcjonalności, jak i zgodności z [sześcioma zasadami odpowiedzialnej SI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

W miarę jak wkraczamy w wiek zdefiniowany przez automatyzację i płynne interakcje człowiek-maszyna, zrozumienie, jak generatywna SI przekształca zakres, głębokość i elastyczność aplikacji czatowych, staje się niezbędne. Ta lekcja zbada aspekty architektury wspierające te złożone systemy, zgłębi metody dostrajania ich do zadań specyficznych dla dziedzin oraz oceni metryki i kwestie istotne dla zapewnienia odpowiedzialnego wdrożenia SI.

## Wprowadzenie

Ta lekcja obejmuje:

- Techniki efektywnego budowania i integrowania aplikacji czatowych.
- Jak stosować personalizację i dostrajanie aplikacji.
- Strategie i rozważania dotyczące skutecznego monitorowania aplikacji czatowych.

## Cele nauki

Pod koniec tej lekcji będziesz potrafił:

- Opisać kwestie związane z budową i integracją aplikacji czatowych z istniejącymi systemami.
- Dostosować aplikacje czatowe do konkretnych zastosowań.
- Zidentyfikować kluczowe metryki i rozważania do skutecznego monitorowania i utrzymania jakości aplikacji czatowych zasilanych SI.
- Zapewnić odpowiedzialne wykorzystanie SI w aplikacjach czatowych.

## Integracja generatywnej SI w aplikacjach czatowych

Ulepszanie aplikacji czatowych za pomocą generatywnej SI to nie tylko kwestia ich „inteligentniejszego” działania; chodzi o optymalizację architektury, wydajności i interfejsu użytkownika, aby dostarczyć wysokiej jakości doświadczenia użytkownika. Obejmuje to badanie fundamentów architektonicznych, integracji API oraz zagadnień interfejsu użytkownika. Ta sekcja ma na celu zapewnienie Ci kompleksowej mapy drogowej do poruszania się po tych złożonych obszarach, niezależnie od tego, czy podłączasz je do istniejących systemów, czy tworzysz jako samodzielne platformy.

Pod koniec tej sekcji będziesz wyposażony w wiedzę niezbędną do efektywnego konstruowania i integrowania aplikacji czatowych.

### Chatbot czy aplikacja czatowa?

Zanim przejdziemy do tworzenia aplikacji czatowych, porównajmy „chatboty” z „aplikacjami czatowymi zasilanymi SI”, które pełnią odmienne role i funkcje. Głównym celem chatbota jest automatyzacja określonych zadań konwersacyjnych, takich jak odpowiadanie na często zadawane pytania czy śledzenie przesyłki. Zazwyczaj jest on sterowany przez logikę opartą na regułach lub skomplikowane algorytmy SI. Natomiast aplikacja czatowa zasilana SI to znacznie szersze środowisko, stworzone do umożliwienia różnych form komunikacji cyfrowej, takich jak czat tekstowy, głosowy czy wideo między użytkownikami. Charakterystyczną cechą jest integracja generatywnego modelu SI, który symuluje zniuansowane, przypominające ludzkie rozmowy, generując odpowiedzi na podstawie różnorodnych danych wejściowych i kontekstu. Aplikacja czatowa z generatywną SI może prowadzić otwarte dyskusje, dostosowywać się do zmieniających się kontekstów rozmowy, a nawet tworzyć kreatywne lub złożone dialogi.

Poniższa tabela przedstawia kluczowe różnice i podobieństwa, które pomogą zrozumieć ich unikalne role w komunikacji cyfrowej.

| Chatbot                               | Aplikacja czatowa zasilana generatywną SI         |
| ------------------------------------- | ----------------------------------------------- |
| Skoncentrowany na zadaniach i oparty na regułach | Świadomy kontekstu                               |
| Często integrowany z większymi systemami          | Może obsługiwać jeden lub wiele chatbotów       |
| Ograniczony do zaprogramowanych funkcji           | Wykorzystuje modele generatywnej SI              |
| Specjalistyczne i ustrukturyzowane interakcje      | Możliwość dyskusji o otwartym zakresie tematycznym|

### Wykorzystanie gotowych funkcji poprzez SDK i API

Przy tworzeniu aplikacji czatowej świetnym pierwszym krokiem jest ocena, co już istnieje. Używanie SDK i API do budowania aplikacji czatowych to korzystna strategia z wielu powodów. Integrując dobrze udokumentowane SDK i API, strategicznie pozycjonujesz swoją aplikację na długoterminowy sukces, rozwiązując problemy skalowalności i konserwacji.

- **Przyspiesza proces rozwoju i zmniejsza nakład pracy**: Poleganie na gotowych funkcjach zamiast na kosztownym tworzeniu ich samodzielnie pozwala skupić się na innych ważniejszych aspektach aplikacji, takich jak logika biznesowa.
- **Lepsza wydajność**: Budując funkcjonalność od podstaw, z czasem zastanawiasz się „Jak to się skalować? Czy aplikacja jest w stanie obsłużyć nagły wzrost użytkowników?” Dobrze utrzymywane SDK i API często mają wbudowane rozwiązania na te problemy.
- **Łatwiejsza konserwacja**: Aktualizacje i ulepszenia są prostsze w zarządzaniu, ponieważ większość API i SDK wymaga jedynie aktualizacji biblioteki po wydaniu nowszej wersji.
- **Dostęp do najnowszych technologii**: Wykorzystanie modeli, które zostały dostrojone i wytrenowane na rozległych zbiorach danych, zapewnia Twojej aplikacji możliwości przetwarzania języka naturalnego.

Uzyskanie dostępu do funkcji SDK czy API zwykle wymaga uzyskania pozwolenia na korzystanie z oferowanych usług, często poprzez unikalny klucz lub token uwierzytelniający. Użyjemy biblioteki OpenAI w Pythonie, aby pokazać, jak to wygląda. Możesz też wypróbować samodzielnie w następujących [notatnikach dla OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) lub [notatnikach dla Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) do tej lekcji.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Powyższy przykład używa modelu GPT-5 mini z API Responses do ukończenia promptu, ale zwróć uwagę, że klucz API jest ustawiony przed tym działaniem. Bez ustawienia klucza otrzymałbyś błąd.

## Doświadczenie użytkownika (UX)

Ogólne zasady UX odnoszą się do aplikacji czatowych, ale oto kilka dodatkowych kwestii, które stają się szczególnie ważne ze względu na komponenty uczenia maszynowego.

- **Mechanizm rozwiązywania niejasności**: Modele generatywnej SI czasem generują niejasne odpowiedzi. Funkcja pozwalająca użytkownikom prosić o wyjaśnienia może być pomocna w takich sytuacjach.
- **Zachowanie kontekstu**: Zaawansowane modele genaratywnej SI potrafią pamiętać kontekst rozmowy, co może być niezwykle ważne dla UX. Danie użytkownikom możliwości kontrolowania i zarządzania kontekstem poprawia doświadczenie, ale niesie ryzyko przechowywania wrażliwych danych użytkownika. Rozważanie, jak długo te dane są przechowywane, na przykład wprowadzenie polityki retencji, może zrównoważyć potrzebę kontekstu z ochroną prywatności.
- **Personalizacja**: Dzięki zdolności do uczenia się i adaptacji, modele SI oferują spersonalizowane doświadczenie użytkownika. Dostosowanie UX przez funkcje takie jak profile użytkownika nie tylko sprawia, że użytkownik czuje się zauważony, ale także pomaga szybciej znaleźć konkretne odpowiedzi, czyniąc interakcję bardziej efektywną i satysfakcjonującą.

Przykładem takiej personalizacji są „Instrukcje niestandardowe” w ChatGPT od OpenAI. Pozwalają one podać informacje o sobie, które mogą stanowić ważny kontekst dla promptów. Oto przykład takiej instrukcji.

![Custom Instructions Settings in ChatGPT](../../../translated_images/pl/custom-instructions.b96f59aa69356fcf.webp)

Ten „profil” nakazuje ChatGPT stworzyć plan lekcji dotyczący list powiązanych. Zauważ, że ChatGPT bierze pod uwagę doświadczenie użytkownika i możliwe życzenie otrzymania bardziej szczegółowego planu.

![A prompt in ChatGPT for a lesson plan about linked lists](../../../translated_images/pl/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoftowy Framework Wiadomości Systemowej dla Dużych Modeli Językowych

[Microsoft udostępnił wytyczne](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) dotyczące pisania efektywnych wiadomości systemowych przy generowaniu odpowiedzi z dużych modeli językowych (LLM), podzielone na 4 obszary:

1. Określenie, dla kogo jest model oraz jego możliwości i ograniczenia.
2. Definiowanie formatu wyjścia modelu.
3. Dostarczanie konkretnych przykładów ilustrujących zamierzone zachowanie modelu.
4. Zapewnienie dodatkowych zabezpieczeń zachowania.

### Dostępność

Niezależnie od tego, czy użytkownik ma zaburzenia wzroku, słuchu, motoryki czy kognitywne, dobrze zaprojektowana aplikacja czatowa powinna być dostępna dla wszystkich. Poniższa lista przedstawia konkretne funkcje mające na celu zwiększenie dostępności dla różnych niepełnosprawności.

- **Funkcje dla osób z wadami wzroku**: Motywy o wysokim kontraście i możliwość zmiany rozmiaru tekstu, kompatybilność z czytnikami ekranu.
- **Funkcje dla osób z wadami słuchu**: Funkcje tekst-na-mowę i mowa-na-tekst, wizualne wskazówki dla powiadomień dźwiękowych.
- **Funkcje dla osób z wadami motorycznymi**: Obsługa nawigacji klawiaturą, polecenia głosowe.
- **Funkcje dla osób z zaburzeniami kognitywnymi**: Opcje uproszczonego języka.

## Personalizacja i dostrajanie modeli językowych specyficznych dla domeny

Wyobraź sobie aplikację czatową, która rozumie żargon twojej firmy i przewiduje konkretne pytania, które często zadają jej użytkownicy. Warto wspomnieć o kilku podejściach:

- **Wykorzystanie modeli DSL**. DSL oznacza język specyficzny dla domeny. Możesz wykorzystać model DSL wytrenowany w konkretnej dziedzinie, aby zrozumieć jej pojęcia i scenariusze.
- **Stosowanie dostrajania**. Dostrajanie to proces dalszego trenowania modelu za pomocą specyficznych danych.

## Personalizacja: korzystanie z DSL

Wykorzystanie modeli języka specyficznego dla domeny (modele DSL) może zwiększyć zaangażowanie użytkowników, zapewniając specjalistyczne, kontekstowo odpowiednie interakcje. Jest to model wytrenowany lub dostrojony, aby rozumieć i generować tekst związany z określoną dziedziną, branżą lub tematem. Opcje wykorzystania modelu DSL mogą obejmować trenowanie od podstaw lub korzystanie z istniejących przez SDK i API. Inną opcją jest dostrajanie, które polega na adaptacji istniejącego, wcześniej wytrenowanego modelu do specyficznej dziedziny.

## Personalizacja: stosowanie dostrajania

Dostrajanie często rozważa się, gdy model wstępnie wytrenowany zawodzi w specjalistycznej dziedzinie lub konkretnym zadaniu.

Na przykład, pytania medyczne są skomplikowane i wymagają wielu kontekstów. Gdy specjalista medyczny diagnozuje pacjenta, opiera się na wielu czynnikach, takich jak styl życia czy choroby współistniejące, a nawet może sięgać do najnowszych publikacji medycznych, aby potwierdzić diagnozę. W takich subtelnych sytuacjach ogólnego przeznaczenia aplikacja czatowa nie może być wiarygodnym źródłem.

### Scenariusz: aplikacja medyczna

Wyobraź sobie aplikację czatową zaprojektowaną do wspierania lekarzy poprzez szybki dostęp do wytycznych leczenia, interakcji leków czy najnowszych badań.

Model ogólnego przeznaczenia może być wystarczający do odpowiadania na podstawowe pytania medyczne lub udzielania ogólnych porad, ale może mieć problemy z:

- **Bardzo specyficznymi lub złożonymi przypadkami**. Na przykład neurolog może zapytać aplikację: „Jakie są obecne najlepsze praktyki zarządzania oporną na leki epilepsją u pacjentów pediatrycznych?”
- **Brakiem najnowszych osiągnięć**. Model ogólnego przeznaczenia może mieć trudności z podaniem aktualnej odpowiedzi uwzględniającej najnowsze osiągnięcia w neurologii i farmakologii.

W takich przypadkach dostrajanie modelu na specjalistycznym, medycznym zbiorze danych może znacząco poprawić jego zdolność do precyzyjniejszego i bardziej wiarygodnego obsługiwania tych złożonych pytań medycznych. Wymaga to dostępu do dużego i relewantnego zbioru danych, który odzwierciedla specyfikę dziedziny oraz wyzwania i pytania, które należy rozwiązać.

## Kwestie dotyczące wysokiej jakości doświadczenia czatowego opartego na SI

Ta sekcja przedstawia kryteria dla „wysokiej jakości” aplikacji czatowych, które obejmują zbieranie wymiernych metryk oraz przestrzeganie ram odpowiedzialnego wykorzystania technologii SI.

### Kluczowe metryki

Aby zachować wysoką jakość działania aplikacji, należy śledzić kluczowe metryki i czynniki. Te pomiary nie tylko zapewniają funkcjonalność aplikacji, ale także oceniają jakość modelu SI i doświadczenia użytkownika. Poniżej znajduje się lista podstawowych metryk, metryk SI i UX do rozważenia.

| Metryka                      | Definicja                                                                                                               | Rozważania dla twórcy czatu                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------- |
| **Dostępność (Uptime)**     | Mierzy czas, w którym aplikacja jest operacyjna i dostępna dla użytkowników.                                            | Jak zminimalizujesz przestoje?                                            |
| **Czas odpowiedzi**          | Czas, jaki aplikacja potrzebuje na odpowiedź na zapytanie użytkownika.                                                 | Jak możesz zoptymalizować przetwarzanie zapytań, aby przyspieszyć odpowiedź? |
| **Precyzja**                | Stosunek prawidłowych trafień pozytywnych do wszystkich prognoz pozytywnych.                                           | Jak zweryfikujesz precyzję swojego modelu?                                |
| **Czułość (Recall)**        | Stosunek prawidłowych trafień pozytywnych do rzeczywistej liczby pozytywnych przypadków.                                | Jak zmierzysz i poprawisz czułość?                                        |
| **Wynik F1**                | Średnia harmoniczna precyzji i czułości, która balansuje kompromis między nimi.                                         | Jaki będzie Twój cel w wyniku F1? Jak zrównoważysz precyzję i czułość?   |
| **Perpleksja**              | Mierzy, jak dobrze rozkład prawdopodobieństwa przewidziany przez model pokrywa się z rzeczywistym rozkładem danych.     | Jak zminimalizujesz perpleksję?                                           |
| **Metryki satysfakcji użytkownika** | Mierzą percepcję użytkownika względem aplikacji. Często zbierane przez ankiety.                                         | Jak często będziesz zbierać opinie użytkowników? Jak się do nich dostosujesz? |
| **Wskaźnik błędów**           | Wskaźnik błędów modelu w rozumieniu lub generowaniu odpowiedzi.                                                        | Jakie strategie masz na zmniejszenie liczby błędów?                       |
| **Cykl retreningu**           | Częstotliwość, z jaką model jest aktualizowany, aby uwzględnić nowe dane i wnioski.                                     | Jak często będziesz ponownie trenować model? Co wyzwala cykl retreningu? |

| **Wykrywanie anomalii**         | Narzędzia i techniki identyfikujące nietypowe wzorce, które nie odpowiadają oczekiwanym zachowaniom.                        | Jak zareagujesz na anomalie?                                        |

### Wdrażanie odpowiedzialnych praktyk AI w aplikacjach czatu

Podejście Microsoft do odpowiedzialnej AI określiło sześć zasad, które powinny kierować rozwojem i wykorzystaniem AI. Poniżej znajdują się zasady, ich definicje oraz kwestie, które deweloper czatu powinien rozważyć i dlaczego powinien traktować je poważnie.

| Zasady                | Definicja Microsoft                                   | Uwagi dla dewelopera czatu                                           | Dlaczego to ważne                                                                   |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Sprawiedliwość         | Systemy AI powinny traktować wszystkich ludzi uczciwie. | Zapewnij, że aplikacja czatu nie dyskryminuje na podstawie danych użytkownika. | Aby budować zaufanie i inkluzywność wśród użytkowników; unika konsekwencji prawnych.                |
| Niezawodność i bezpieczeństwo | Systemy AI powinny działać niezawodnie i bezpiecznie.   | Wprowadź testowanie i mechanizmy zapobiegające błędom oraz ryzyku.         | Zapewnia satysfakcję użytkownika i zapobiega potencjalnym szkodom.                                 |
| Prywatność i bezpieczeństwo | Systemy AI powinny być bezpieczne i szanować prywatność. | Wdroż silne szyfrowanie i środki ochrony danych.              | Aby chronić wrażliwe dane użytkowników i przestrzegać przepisów dotyczących prywatności.                         |
| Inkluzywność           | Systemy AI powinny wzmacniać wszystkich i angażować ludzi. | Zaprojektuj UI/UX, które jest dostępne i łatwe w obsłudze dla różnorodnych odbiorców. | Zapewnia, że szerszy zakres ludzi może skutecznie korzystać z aplikacji.                   |
| Przejrzystość          | Systemy AI powinny być zrozumiałe.                    | Dostarcz jasną dokumentację i uzasadnienie odpowiedzi AI.            | Użytkownicy bardziej ufają systemowi, jeśli mogą zrozumieć, jak podejmowane są decyzje. |
| Odpowiedzialność       | Ludzie powinni być odpowiedzialni za systemy AI.      | Ustanów jasny proces audytu i poprawy decyzji AI.     | Umożliwia stałe ulepszanie i działania korygujące w przypadku błędów.               |

## Zadanie

Zobacz [assignment](../../../07-building-chat-applications/python). Przeprowadzi Cię przez serię ćwiczeń, od uruchamiania pierwszych promptów czatu, przez klasyfikację i podsumowywanie tekstu, i więcej. Zauważ, że zadania są dostępne w różnych językach programowania!

## Świetna robota! Kontynuuj podróż

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat Generative AI!

Przejdź do Lekcji 8, aby zobaczyć jak możesz zacząć [budować aplikacje do wyszukiwania](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->