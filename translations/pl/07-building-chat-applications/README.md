<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-18T00:56:27+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "pl"
}
-->
# Tworzenie aplikacji czatowych zasilanych przez generatywną sztuczną inteligencję

[![Tworzenie aplikacji czatowych zasilanych przez generatywną sztuczną inteligencję](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.pl.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

Teraz, gdy zobaczyliśmy, jak można budować aplikacje generujące tekst, przyjrzyjmy się aplikacjom czatowym.

Aplikacje czatowe stały się integralną częścią naszego codziennego życia, oferując coś więcej niż tylko możliwość prowadzenia swobodnych rozmów. Są kluczowym elementem obsługi klienta, wsparcia technicznego, a nawet zaawansowanych systemów doradczych. Prawdopodobnie niedawno skorzystałeś z pomocy aplikacji czatowej. W miarę jak integrujemy bardziej zaawansowane technologie, takie jak generatywna sztuczna inteligencja, z tymi platformami, rośnie zarówno ich złożoność, jak i wyzwania.

Niektóre pytania, na które musimy znaleźć odpowiedzi, to:

- **Budowa aplikacji**. Jak efektywnie budować i płynnie integrować te aplikacje zasilane przez AI dla konkretnych przypadków użycia?
- **Monitorowanie**. Po wdrożeniu, jak możemy monitorować i zapewnić, że aplikacje działają na najwyższym poziomie jakości, zarówno pod względem funkcjonalności, jak i zgodności z [sześcioma zasadami odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

W miarę jak wkraczamy w erę zdefiniowaną przez automatyzację i płynne interakcje człowiek-maszyna, zrozumienie, jak generatywna sztuczna inteligencja przekształca zakres, głębię i adaptacyjność aplikacji czatowych, staje się kluczowe. Ta lekcja zbada aspekty architektury wspierającej te złożone systemy, zagłębi się w metody dostosowywania ich do zadań specyficznych dla danej dziedziny oraz oceni metryki i kwestie istotne dla zapewnienia odpowiedzialnego wdrożenia AI.

## Wprowadzenie

Ta lekcja obejmuje:

- Techniki efektywnego budowania i integracji aplikacji czatowych.
- Jak zastosować dostosowanie i dopasowanie aplikacji.
- Strategie i kwestie dotyczące skutecznego monitorowania aplikacji czatowych.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Opisać kwestie związane z budową i integracją aplikacji czatowych z istniejącymi systemami.
- Dostosować aplikacje czatowe do konkretnych przypadków użycia.
- Zidentyfikować kluczowe metryki i kwestie dotyczące skutecznego monitorowania i utrzymania jakości aplikacji czatowych zasilanych przez AI.
- Zapewnić, że aplikacje czatowe odpowiedzialnie wykorzystują sztuczną inteligencję.

## Integracja generatywnej AI w aplikacjach czatowych

Podnoszenie jakości aplikacji czatowych za pomocą generatywnej AI nie polega tylko na uczynieniu ich bardziej inteligentnymi; chodzi o optymalizację ich architektury, wydajności i interfejsu użytkownika, aby zapewnić wysoką jakość doświadczenia użytkownika. Obejmuje to badanie podstaw architektonicznych, integracji API oraz rozważań dotyczących interfejsu użytkownika. Ta sekcja ma na celu dostarczenie kompleksowej mapy drogowej do poruszania się po tych złożonych obszarach, niezależnie od tego, czy integrujesz je z istniejącymi systemami, czy budujesz jako samodzielne platformy.

Po zakończeniu tej sekcji będziesz wyposażony w wiedzę potrzebną do efektywnego konstruowania i włączania aplikacji czatowych.

### Chatbot czy aplikacja czatowa?

Zanim zagłębimy się w budowę aplikacji czatowych, porównajmy „chatboty” z „aplikacjami czatowymi zasilanymi przez AI”, które pełnią różne role i funkcje. Głównym celem chatbota jest automatyzacja określonych zadań konwersacyjnych, takich jak odpowiadanie na często zadawane pytania czy śledzenie przesyłek. Zazwyczaj działa on na zasadzie logiki opartej na regułach lub złożonych algorytmach AI. Z kolei aplikacja czatowa zasilana przez AI to znacznie bardziej rozbudowane środowisko zaprojektowane do obsługi różnych form komunikacji cyfrowej, takich jak czaty tekstowe, głosowe i wideo między użytkownikami. Jej cechą charakterystyczną jest integracja modelu generatywnej AI, który symuluje subtelne, ludzkie rozmowy, generując odpowiedzi na podstawie szerokiej gamy danych wejściowych i wskazówek kontekstowych. Aplikacja czatowa zasilana przez generatywną AI może prowadzić rozmowy na dowolny temat, dostosowywać się do zmieniających się kontekstów konwersacyjnych, a nawet tworzyć kreatywne lub złożone dialogi.

Poniższa tabela przedstawia kluczowe różnice i podobieństwa, które pomagają zrozumieć ich unikalne role w komunikacji cyfrowej.

| Chatbot                               | Aplikacja czatowa zasilana generatywną AI |
| ------------------------------------- | ----------------------------------------- |
| Skoncentrowany na zadaniach i oparty na regułach | Świadomy kontekstu                        |
| Często zintegrowany z większymi systemami | Może obsługiwać jeden lub wiele chatbotów |
| Ograniczony do zaprogramowanych funkcji | Zawiera modele generatywnej AI            |
| Specjalistyczne i strukturalne interakcje | Zdolny do rozmów na dowolny temat         |

### Wykorzystanie gotowych funkcji za pomocą SDK i API

Podczas budowy aplikacji czatowej dobrym pierwszym krokiem jest ocena dostępnych rozwiązań. Wykorzystanie SDK i API do budowy aplikacji czatowych to korzystna strategia z wielu powodów. Integrując dobrze udokumentowane SDK i API, strategicznie pozycjonujesz swoją aplikację na długoterminowy sukces, rozwiązując problemy związane ze skalowalnością i utrzymaniem.

- **Przyspiesza proces rozwoju i zmniejsza koszty**: Korzystanie z gotowych funkcji zamiast kosztownego procesu ich budowy pozwala skupić się na innych aspektach aplikacji, które mogą być ważniejsze, takich jak logika biznesowa.
- **Lepsza wydajność**: Budując funkcjonalność od podstaw, w końcu zadasz sobie pytanie: „Jak to się skaluje? Czy aplikacja jest w stanie obsłużyć nagły napływ użytkowników?” Dobrze utrzymane SDK i API często mają wbudowane rozwiązania dla tych problemów.
- **Łatwiejsze utrzymanie**: Aktualizacje i ulepszenia są łatwiejsze do zarządzania, ponieważ większość API i SDK wymaga jedynie aktualizacji biblioteki po wydaniu nowszej wersji.
- **Dostęp do najnowszych technologii**: Wykorzystanie modeli, które zostały dopracowane i przeszkolone na obszernych zestawach danych, zapewnia Twojej aplikacji możliwości przetwarzania języka naturalnego.

Dostęp do funkcji SDK lub API zazwyczaj wymaga uzyskania zgody na korzystanie z udostępnionych usług, co często odbywa się za pomocą unikalnego klucza lub tokena uwierzytelniającego. Użyjemy biblioteki OpenAI Python Library, aby zobaczyć, jak to wygląda. Możesz również samodzielnie wypróbować to w następującym [notebooku dla OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) lub [notebooku dla Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) w ramach tej lekcji.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Powyższy przykład używa modelu GPT-3.5 Turbo do uzupełnienia podpowiedzi, ale zauważ, że klucz API jest ustawiony przed wykonaniem tego kroku. Jeśli nie ustawisz klucza, otrzymasz błąd.

## Doświadczenie użytkownika (UX)

Ogólne zasady UX mają zastosowanie do aplikacji czatowych, ale istnieją dodatkowe kwestie, które stają się szczególnie istotne ze względu na komponenty uczenia maszynowego.

- **Mechanizm rozwiązywania niejasności**: Modele generatywnej AI czasami generują niejasne odpowiedzi. Funkcja umożliwiająca użytkownikom zadawanie pytań uzupełniających może być pomocna w takich sytuacjach.
- **Zachowanie kontekstu**: Zaawansowane modele generatywnej AI mają zdolność zapamiętywania kontekstu w rozmowie, co może być niezbędnym atutem dla doświadczenia użytkownika. Dając użytkownikom możliwość kontrolowania i zarządzania kontekstem, poprawiamy ich doświadczenie, ale wprowadzamy ryzyko przechowywania wrażliwych informacji. Rozważania dotyczące czasu przechowywania tych informacji, takie jak wprowadzenie polityki retencji, mogą zrównoważyć potrzebę zachowania kontekstu z ochroną prywatności.
- **Personalizacja**: Dzięki zdolności do uczenia się i adaptacji, modele AI oferują spersonalizowane doświadczenie dla użytkownika. Dostosowanie doświadczenia użytkownika poprzez funkcje takie jak profile użytkowników nie tylko sprawia, że użytkownik czuje się zrozumiany, ale także pomaga mu w szybkim znajdowaniu konkretnych odpowiedzi, tworząc bardziej efektywną i satysfakcjonującą interakcję.

Jednym z przykładów personalizacji są ustawienia „Instrukcje niestandardowe” w ChatGPT od OpenAI. Pozwalają one na podanie informacji o sobie, które mogą być ważnym kontekstem dla Twoich podpowiedzi. Oto przykład instrukcji niestandardowej.

![Ustawienia instrukcji niestandardowych w ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.pl.png)

Ten „profil” skłania ChatGPT do stworzenia planu lekcji na temat list powiązanych. Zauważ, że ChatGPT bierze pod uwagę, że użytkownik może chcieć bardziej szczegółowego planu lekcji na podstawie swojego doświadczenia.

![Podpowiedź w ChatGPT dotycząca planu lekcji o listach powiązanych](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.pl.png)

### Framework wiadomości systemowych Microsoft dla dużych modeli językowych

[Microsoft udostępnił wskazówki](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) dotyczące pisania skutecznych wiadomości systemowych podczas generowania odpowiedzi z LLM, podzielone na 4 obszary:

1. Określenie, dla kogo jest model, jego możliwości i ograniczenia.
2. Określenie formatu wyjściowego modelu.
3. Podanie konkretnych przykładów, które demonstrują zamierzone zachowanie modelu.
4. Zapewnienie dodatkowych zabezpieczeń behawioralnych.

### Dostępność

Niezależnie od tego, czy użytkownik ma problemy ze wzrokiem, słuchem, motoryką czy poznawcze, dobrze zaprojektowana aplikacja czatowa powinna być dostępna dla wszystkich. Poniższa lista przedstawia konkretne funkcje mające na celu poprawę dostępności dla różnych rodzajów niepełnosprawności użytkowników.

- **Funkcje dla osób z zaburzeniami wzroku**: Motywy o wysokim kontraście i możliwość zmiany rozmiaru tekstu, kompatybilność z czytnikami ekranu.
- **Funkcje dla osób z zaburzeniami słuchu**: Funkcje zamiany tekstu na mowę i mowy na tekst, wizualne wskazówki dla powiadomień dźwiękowych.
- **Funkcje dla osób z zaburzeniami motorycznymi**: Obsługa nawigacji za pomocą klawiatury, polecenia głosowe.
- **Funkcje dla osób z zaburzeniami poznawczymi**: Opcje uproszczonego języka.

## Dostosowanie i dopasowanie do modeli językowych specyficznych dla danej dziedziny

Wyobraź sobie aplikację czatową, która rozumie żargon Twojej firmy i przewiduje specyficzne pytania, które mogą zadawać jej użytkownicy. Istnieje kilka podejść, które warto rozważyć:

- **Wykorzystanie modeli DSL**. DSL oznacza język specyficzny dla danej dziedziny. Możesz wykorzystać tak zwany model DSL, który został przeszkolony w określonej dziedzinie, aby zrozumieć jej koncepcje i scenariusze.
- **Zastosowanie dopasowania**. Dopasowanie to proces dalszego szkolenia modelu za pomocą określonych danych.

## Dostosowanie: Wykorzystanie DSL

Wykorzystanie modeli językowych specyficznych dla danej dziedziny (DSL Models) może zwiększyć zaangażowanie użytkowników, zapewniając specjalistyczne, kontekstowo odpowiednie interakcje. Jest to model, który został przeszkolony lub dopasowany do generowania tekstu związanego z określoną dziedziną, branżą lub tematem. Opcje korzystania z modelu DSL mogą się różnić od szkolenia od podstaw, przez korzystanie z już istniejących modeli za pośrednictwem SDK i API, po dopasowanie, które polega na dostosowaniu istniejącego modelu wstępnie przeszkolonego do konkretnej dziedziny.

## Dostosowanie: Zastosowanie dopasowania

Dopasowanie jest często rozważane, gdy model wstępnie przeszkolony nie spełnia oczekiwań w specjalistycznej dziedzinie lub konkretnym zadaniu.

Na przykład, zapytania medyczne są skomplikowane i wymagają dużej ilości kontekstu. Kiedy lekarz diagnozuje pacjenta, opiera się na różnych czynnikach, takich jak styl życia czy istniejące schorzenia, a nawet na najnowszych publikacjach medycznych, aby potwierdzić swoją diagnozę. W takich złożonych scenariuszach ogólny model AI czatowy nie może być wiarygodnym źródłem.

### Scenariusz: aplikacja medyczna

Rozważmy aplikację czatową zaprojektowaną do wspierania lekarzy poprzez szybkie dostarczanie informacji o wytycznych dotyczących leczenia, interakcjach leków czy najnowszych wynikach badań.

Ogólny model może być wystarczający do odpowiadania na podstawowe pytania medyczne lub udzielania ogólnych porad, ale może mieć trudności z następującymi kwestiami:

- **Bardzo specyficzne lub złożone przypadki**. Na przykład neurolog może zapytać aplikację: „Jakie są obecne najlepsze praktyki w zarządzaniu lekooporną padaczką u dzieci?”
- **Brak najnowszych osiągnięć**. Ogólny model może mieć trudności z udzieleniem aktualnej odpowiedzi uwzględniającej najnowsze osiągnięcia w dziedzinie neurologii i farmakologii.

W takich przypadkach dopasowanie modelu za pomocą specjalistycznego zestawu danych medycznych może znacznie poprawić jego zdolność do radzenia sobie z tymi skomplikowanymi zapytaniami medycznymi w sposób bardziej precyzyjny i wiarygodny. Wymaga to dostępu do dużego i odpowiedniego zestawu danych, który odzwierciedla wyzwania i pytania specyficzne dla danej dziedziny.

## Kwestie dotyczące wysokiej jakości doświadczenia z AI w aplikacjach czatowych

Ta sekcja przedstawia kryteria „wysokiej jakości” aplikacji czatowych, które obejmują zbieranie mierzalnych danych oraz przestrzeganie zasad odpowiedzialnego wykorzystania technologii AI.

### Kluczowe metryki

Aby utrzymać wysoką jakość działania aplikacji, konieczne jest śledzenie kluczowych metryk i rozważenie istotnych kwestii. Te pomiary nie tylko zapewniają funkcjonalność aplikacji, ale także oceniają jakość modelu AI i doświadczenie użytkownika. Poniżej znajduje się lista obejmująca podstawowe metryki, metryki AI oraz metryki doświadczenia użytkownika, które warto wziąć pod uwagę.

| Metryka                     | Definicja                                                                                  | Kwestie dla twórcy aplikacji                                              |
| --------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **Czas działania**          | Mierzy czas, przez który aplikacja jest operacyjna i dostępna dla użytkowników.             | Jak zminimalizujesz czas przestoju?                                       |
| **Czas odpowiedzi**         | Czas potrzebny aplikacji na odpowiedź na zapytanie użytkownika.                            | Jak możesz zoptymalizować przetwarzanie zap
| **Wykrywanie anomalii**       | Narzędzia i techniki identyfikacji nietypowych wzorców, które nie odpowiadają oczekiwanym zachowaniom.                     | Jak zareagujesz na anomalie?                                              |

### Wdrażanie odpowiedzialnych praktyk AI w aplikacjach czatu

Podejście Microsoftu do Odpowiedzialnej AI opiera się na sześciu zasadach, które powinny kierować rozwojem i wykorzystaniem AI. Poniżej znajdują się zasady, ich definicje oraz rzeczy, które powinien rozważyć twórca aplikacji czatu, a także dlaczego są one istotne.

| Zasady                 | Definicja Microsoftu                                  | Rozważania dla twórcy aplikacji czatu                                  | Dlaczego to ważne                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Sprawiedliwość         | Systemy AI powinny traktować wszystkich ludzi równo.  | Upewnij się, że aplikacja czatu nie dyskryminuje na podstawie danych użytkownika. | Aby budować zaufanie i inkluzywność wśród użytkowników; unika problemów prawnych.       |
| Niezawodność i bezpieczeństwo | Systemy AI powinny działać niezawodnie i bezpiecznie. | Wprowadź testy i mechanizmy zabezpieczające, aby zminimalizować błędy i ryzyko. | Zapewnia satysfakcję użytkowników i zapobiega potencjalnym szkodom.                    |
| Prywatność i bezpieczeństwo | Systemy AI powinny być bezpieczne i szanować prywatność. | Wprowadź silne szyfrowanie i środki ochrony danych.                    | Aby chronić wrażliwe dane użytkowników i przestrzegać przepisów dotyczących prywatności. |
| Inkluzywność           | Systemy AI powinny wspierać wszystkich i angażować ludzi. | Projektuj interfejsy UI/UX dostępne i łatwe w użyciu dla różnych grup odbiorców. | Zapewnia, że szeroka grupa osób może efektywnie korzystać z aplikacji.                 |
| Przejrzystość          | Systemy AI powinny być zrozumiałe.                     | Zapewnij jasną dokumentację i wyjaśnienia dotyczące odpowiedzi AI.     | Użytkownicy są bardziej skłonni zaufać systemowi, jeśli rozumieją, jak podejmowane są decyzje. |
| Odpowiedzialność       | Ludzie powinni być odpowiedzialni za systemy AI.       | Ustanów jasny proces audytu i poprawy decyzji AI.                      | Umożliwia ciągłe doskonalenie i podejmowanie działań naprawczych w przypadku błędów.    |

## Zadanie

Zobacz [zadanie](../../../07-building-chat-applications/python). Przeprowadzi Cię ono przez serię ćwiczeń, od uruchomienia pierwszych zapytań czatu, przez klasyfikację i podsumowywanie tekstu, aż po inne zadania. Zauważ, że zadania są dostępne w różnych językach programowania!

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat generatywnej AI!

Przejdź do Lekcji 8, aby dowiedzieć się, jak zacząć [budować aplikacje wyszukiwania](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.