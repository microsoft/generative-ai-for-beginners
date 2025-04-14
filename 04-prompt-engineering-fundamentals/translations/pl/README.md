# Podstawy Inżynierii Promptów

[![Podstawy Inżynierii Promptów](../../images/04-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Wprowadzenie

Ten moduł obejmuje podstawowe koncepcje i techniki tworzenia skutecznych promptów dla modeli generatywnej sztucznej inteligencji. Sposób, w jaki piszesz prompt do modelu LLM, ma duże znaczenie. Starannie opracowany prompt może zapewnić lepszą jakość odpowiedzi. Ale co dokładnie oznaczają terminy takie jak _prompt_ i _inżynieria promptów_? I jak mogę ulepszyć _dane wejściowe_ prompta, które wysyłam do LLM? To pytania, na które postaramy się odpowiedzieć w tym rozdziale i następnym.

_Generatywna sztuczna inteligencja_ jest zdolna do tworzenia nowych treści (np. tekstu, obrazów, dźwięku, kodu itp.) w odpowiedzi na prośby użytkownika. Osiąga to za pomocą _Dużych Modeli Językowych_, takich jak seria GPT firmy OpenAI ("Generative Pre-trained Transformer"), które są trenowane do używania języka naturalnego i kodu.

Użytkownicy mogą teraz wchodzić w interakcje z tymi modelami, korzystając z dobrze znanych paradygmatów, takich jak czat, bez konieczności posiadania wiedzy technicznej czy specjalistycznego szkolenia. Modele te są _oparte na promptach_ - użytkownicy wysyłają wejście tekstowe (prompt) i otrzymują odpowiedź AI (uzupełnienie). Następnie mogą "rozmawiać z AI" iteracyjnie, w wieloturowych konwersacjach, dopracowując swój prompt, aż odpowiedź będzie zgodna z ich oczekiwaniami.

"Prompty" stają się teraz głównym _interfejsem programistycznym_ dla aplikacji generatywnej AI, mówiąc modelom, co mają robić i wpływając na jakość zwracanych odpowiedzi. "Inżynieria Promptów" to szybko rozwijająca się dziedzina badań, która koncentruje się na _projektowaniu i optymalizacji_ promptów w celu dostarczania spójnych i jakościowych odpowiedzi na dużą skalę.

## Cele Nauki

W tej lekcji dowiemy się, czym jest inżynieria promptów, dlaczego jest ważna i jak możemy tworzyć bardziej efektywne prompty dla danego modelu i celu aplikacji. Zrozumiemy podstawowe koncepcje i najlepsze praktyki w inżynierii promptów - oraz poznamy interaktywne środowisko Jupyter Notebooks "sandbox", w którym zobaczymy zastosowanie tych koncepcji na prawdziwych przykładach.

Do końca tej lekcji będziemy potrafili:

1. Wyjaśnić, czym jest inżynieria promptów i dlaczego jest ważna.
2. Opisać komponenty promptu i sposób ich wykorzystania.
3. Poznać najlepsze praktyki i techniki inżynierii promptów.
4. Zastosować poznane techniki na rzeczywistych przykładach, korzystając z punktu końcowego OpenAI.

## Kluczowe Pojęcia

Inżynieria Promptów: Praktyka projektowania i udoskonalania danych wejściowych w celu naprowadzania modeli AI na generowanie pożądanych wyników.
Tokenizacja: Proces konwersji tekstu na mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetwarzać.
LLM dostrojone instrukcyjnie: Duże Modele Językowe (LLM), które zostały dostrojone za pomocą określonych instrukcji w celu poprawy dokładności i trafności ich odpowiedzi.

## Sandbox do Nauki

Inżynieria promptów jest obecnie bardziej sztuką niż nauką. Najlepszym sposobem na poprawę naszej intuicji w tej dziedzinie jest _więcej praktyki_ i przyjęcie podejścia prób i błędów, które łączy wiedzę ekspercką z zakresu dziedziny zastosowania z zalecanymi technikami i optymalizacjami specyficznymi dla modelu.

Notebook Jupyter towarzyszący tej lekcji zapewnia środowisko _sandbox_, w którym możesz wypróbować to, czego się uczysz - w trakcie nauki lub jako część wyzwania kodowego na końcu. Aby wykonać ćwiczenia, będziesz potrzebować:

1. **Klucza API Azure OpenAI** - punktu końcowego usługi dla wdrożonego LLM.
2. **Środowiska Wykonawczego Python** - w którym można uruchomić Notebook.
3. **Lokalnych Zmiennych Środowiskowych** - _wykonaj teraz kroki [SETUP](../../../00-course-setup/translations/pl/SETUP.md?WT.mc_id=academic-105485-koreyst), aby być gotowym_.

Notebook zawiera ćwiczenia _startowe_ - ale zachęcamy do dodawania własnych sekcji _Markdown_ (opis) i _Code_ (żądania promptów), aby wypróbować więcej przykładów lub pomysłów - i zbudować swoją intuicję dotyczącą projektowania promptów.

## Ilustrowany Przewodnik

Chcesz poznać ogólny obraz tego, co obejmuje ta lekcja, zanim się w nią zagłębisz? Sprawdź ten ilustrowany przewodnik, który daje ci pojęcie o głównych tematach i kluczowych wnioskach do przemyślenia w każdym z nich. Mapa lekcji prowadzi cię od zrozumienia podstawowych koncepcji i wyzwań do rozwiązywania ich za pomocą odpowiednich technik inżynierii promptów i najlepszych praktyk. Zauważ, że sekcja "Zaawansowane Techniki" w tym przewodniku odnosi się do treści zawartych w _następnym_ rozdziale tego programu nauczania.

![Ilustrowany Przewodnik do Inżynierii Promptów](../../images/04-prompt-engineering-sketchnote.png?WT.mc_id=academic-105485-koreyst)

## Nasz Startup

Teraz porozmawiajmy o tym, jak _ten temat_ odnosi się do misji naszego startupu [wprowadzania innowacji AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje AI wspomagające _spersonalizowane uczenie się_ - zastanówmy się więc, jak różni użytkownicy naszej aplikacji mogliby "projektować" prompty:

- **Administratorzy** mogliby poprosić AI o _analizę danych programowych w celu identyfikacji luk w zakresie materiału_. AI może podsumować wyniki lub wizualizować je za pomocą kodu.
- **Edukatorzy** mogliby poprosić AI o _wygenerowanie planu lekcji dla określonej grupy docelowej i tematu_. AI może stworzyć spersonalizowany plan w określonym formacie.
- **Studenci** mogliby poprosić AI o _pomoc w trudnym przedmiocie_. AI może teraz prowadzić studentów poprzez lekcje, wskazówki i przykłady dostosowane do ich poziomu.

To tylko wierzchołek góry lodowej. Sprawdź [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - bibliotekę promptów open-source, stworzoną przez ekspertów edukacyjnych - aby uzyskać szersze pojęcie o możliwościach! _Spróbuj uruchomić niektóre z tych promptów w sandboxie lub korzystając z OpenAI Playground, aby zobaczyć, co się stanie!_

## Czym jest Inżynieria Promptów?

Rozpoczęliśmy tę lekcję od zdefiniowania **Inżynierii Promptów** jako procesu _projektowania i optymalizacji_ wejść tekstowych (promptów) w celu dostarczania spójnych i jakościowych odpowiedzi (uzupełnień) dla danego celu aplikacji i modelu. Możemy myśleć o tym jako o procesie 2-etapowym:

- _projektowanie_ początkowego promptu dla danego modelu i celu
- _doskonalenie_ promptu iteracyjnie w celu poprawy jakości odpowiedzi

Jest to z konieczności proces prób i błędów, który wymaga intuicji i wysiłku użytkownika, aby uzyskać optymalne wyniki. Dlaczego więc jest to ważne? Aby odpowiedzieć na to pytanie, musimy najpierw zrozumieć trzy koncepcje:

- _Tokenizacja_ = jak model "widzi" prompt
- _Bazowe LLM_ = jak model podstawowy "przetwarza" prompt
- _LLM Dostrojone Instrukcyjnie_ = jak model może teraz widzieć "zadania"

### Tokenizacja

LLM widzi prompty jako _sekwencję tokenów_, gdzie różne modele (lub wersje modelu) mogą tokenizować ten sam prompt na różne sposoby. Ponieważ LLM są trenowane na tokenach (a nie na surowym tekście), sposób tokenizacji promptów ma bezpośredni wpływ na jakość generowanej odpowiedzi.

Aby zrozumieć intuicyjnie, jak działa tokenizacja, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) pokazany poniżej. Skopiuj swój prompt - i zobacz, jak zostaje on przekształcony w tokeny, zwracając uwagę na to, jak są obsługiwane znaki białych spacji i znaki interpunkcyjne. Zauważ, że ten przykład pokazuje starszy LLM (GPT-3) - więc wypróbowanie tego z nowszym modelem może dać inny wynik.

![Tokenizacja](../../images/04-tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

### Koncepcja: Modele Podstawowe

Po tokenizacji promptu, główną funkcją ["Bazowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (lub modelu podstawowego) jest przewidywanie tokenu w tej sekwencji. Ponieważ LLM są trenowane na ogromnych zbiorach danych tekstowych, mają dobre zrozumienie statystycznych relacji między tokenami i mogą dokonywać tych przewidywań z pewnym stopniem pewności. Zauważ, że nie rozumieją one _znaczenia_ słów w promptcie lub tokenie; widzą jedynie wzorzec, który mogą "uzupełnić" swoją następną prognozą. Mogą kontynuować przewidywanie sekwencji, aż do zakończenia przez interwencję użytkownika lub jakiś wcześniej ustalony warunek.

Chcesz zobaczyć, jak działa uzupełnianie oparte na promptach? Wprowadź powyższy prompt do [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) w Azure OpenAI Studio z domyślnymi ustawieniami. System jest skonfigurowany do traktowania promptów jako próśb o informacje - więc powinieneś zobaczyć uzupełnienie, które spełnia ten kontekst.

Ale co jeśli użytkownik chciałby zobaczyć coś konkretnego, co spełnia pewne kryteria lub cel zadania? Tutaj do gry wchodzą _LLM dostrojone instrukcyjnie_.

![Uzupełnianie Chatu Bazowego LLM](../../images/04-playground-chat-base.png?WT.mc_id=academic-105485-koreyst)

### Koncepcja: LLM Dostrojone Instrukcyjnie

[LLM Dostrojone Instrukcyjnie](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zaczyna od modelu podstawowego i dostosowuje go za pomocą przykładów lub par wejście/wyjście (np. wieloturowych "wiadomości"), które mogą zawierać jasne instrukcje - a odpowiedź AI stara się podążać za tą instrukcją.

Wykorzystuje to techniki takie jak Uczenie się przez Wzmacnianie z Ludzkim Feedbackiem (RLHF), które mogą trenować model do _podążania za instrukcjami_ i _uczenia się z feedbacku_, dzięki czemu generuje odpowiedzi, które są lepiej dostosowane do praktycznych zastosowań i bardziej odpowiednie dla celów użytkownika.

Wypróbujmy to - wróć do powyższego promptu, ale teraz zmień _wiadomość systemową_, aby zapewnić następującą instrukcję jako kontekst:

> _Podsumuj dostarczony Ci materiał dla ucznia drugiej klasy. Ogranicz wynik do jednego akapitu z 3-5 punktami._

Zobacz, jak wynik jest teraz dostosowany do pożądanego celu i formatu? Nauczyciel może teraz bezpośrednio użyć tej odpowiedzi w swoich slajdach dla tej klasy.

![Uzupełnianie Chatu LLM Dostrojonego Instrukcyjnie](../../images/04-playground-chat-instructions.png?WT.mc_id=academic-105485-koreyst)

## Dlaczego potrzebujemy Inżynierii Promptów?

Teraz, gdy wiemy, jak prompty są przetwarzane przez LLM, porozmawiajmy o tym, _dlaczego_ potrzebujemy inżynierii promptów. Odpowiedź leży w fakcie, że obecne LLM stawiają przed nami szereg wyzwań, które czynią _uzyskiwanie wiarygodnych i spójnych uzupełnień_ trudniejsze bez wysiłku włożonego w konstrukcję i optymalizację promptów. Na przykład:

1. **Odpowiedzi modeli są stochastyczne.** _Ten sam prompt_ prawdopodobnie wygeneruje różne odpowiedzi z różnymi modelami lub wersjami modelu. A może nawet generować różne wyniki z _tym samym modelem_ w różnym czasie. _Techniki inżynierii promptów mogą pomóc nam zminimalizować te wariacje, zapewniając lepsze zabezpieczenia_.

1. **Modele mogą wymyślać odpowiedzi.** Modele są wstępnie trenowane na _dużych, ale skończonych_ zbiorach danych, co oznacza, że brakuje im wiedzy o koncepcjach spoza zakresu tego treningu. W rezultacie mogą generować uzupełnienia, które są niedokładne, zmyślone lub bezpośrednio sprzeczne ze znanymi faktami. _Techniki inżynierii promptów pomagają użytkownikom zidentyfikować i złagodzić takie zmyślenia, np. prosząc AI o cytaty lub uzasadnienie_.

1. **Możliwości modeli będą się różnić.** Nowsze modele lub generacje modeli będą miały bogatsze możliwości, ale również przyniosą unikalne dziwactwa i kompromisy w zakresie kosztów i złożoności. _Inżynieria promptów może pomóc nam opracować najlepsze praktyki i przepływy pracy, które abstrahują od różnic i dostosowują się do wymagań specyficznych dla modelu w skalowalny, bezproblemowy sposób_.

Zobaczmy to w akcji w OpenAI lub Azure OpenAI Playground:

- Użyj tego samego promptu z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) - czy zauważyłeś różnice?
- Użyj wielokrotnie tego samego promptu z _tym samym_ wdrożeniem LLM (np. Azure OpenAI playground) - jak różniły się te wariacje?

### Przykład Konfabulacji

W tym kursie używamy terminu **"konfabulacja"** do określenia zjawiska, gdzie LLM czasami generują informacje faktycznie niepoprawne z powodu ograniczeń w ich treningu lub innych ograniczeń. Być może słyszałeś o tym zjawisku jako o _"halucynacjach"_ w popularnych artykułach lub pracach badawczych. Jednak zdecydowanie zalecamy używanie terminu _"konfabulacja"_, abyśmy przypadkowo nie przypisywali maszynie cech ludzkich. Wzmacnia to również [wytyczne Odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z perspektywy terminologicznej, usuwając terminy, które mogą być również uznane za obraźliwe lub niewłączające w niektórych kontekstach.

Chcesz zrozumieć, jak działają konfabulacje? Wymyśl prompt, który instruuje AI do generowania treści na nieistniejący temat (aby upewnić się, że nie znajduje się on w zestawie treningowym). Na przykład - wypróbowałem ten prompt:

> **Prompt:** wygeneruj plan lekcji o Wojnie Marsjańskiej z 2076 roku.

Wyszukiwanie w sieci pokazało mi, że istniały fikcyjne opowieści (np. seriale telewizyjne lub książki) o wojnach marsjańskich - ale żadne w 2076 roku. Zdrowy rozsądek również mówi nam, że rok 2076 jest _w przyszłości_, a więc nie może być związany z rzeczywistym wydarzeniem.

Co więc się dzieje, gdy uruchamiamy ten prompt z różnymi dostawcami LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

![Odpowiedź 1](../../images/04-fabrication-oai.png?WT.mc_id=academic-105485-koreyst)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

![Odpowiedź 2](../../images/04-fabrication-aoai.png?WT.mc_id=academic-105485-koreyst)

> **Odpowiedź 3**: : Hugging Face Chat Playground (LLama-2)

![Odpowiedź 3](../../images/04-fabrication-huggingchat.png?WT.mc_id=academic-105485-koreyst)

Zgodnie z oczekiwaniami, każdy model (lub wersja modelu) generuje nieco inne odpowiedzi dzięki zachowaniom stochastycznym i różnicom w możliwościach modelu. Na przykład jeden model celuje w audytorium 8 klasy, podczas gdy inny zakłada ucznia liceum. Ale wszystkie trzy modele wygenerowały odpowiedzi, które mogłyby przekonać niepoinformowanego użytkownika, że wydarzenie było prawdziwe.

Techniki inżynierii promptów, takie jak _metaprompting_ i _konfiguracja temperatury_, mogą w pewnym stopniu zmniejszyć konfabulacje modelu. Nowe _architektury_ inżynierii promptów również bezproblemowo włączają nowe narzędzia i techniki do przepływu promptów, aby złagodzić lub zmniejszyć niektóre z tych efektów.

## Studium Przypadku: GitHub Copilot

Podsumujmy tę sekcję, zyskując poczucie, jak inżynieria promptów jest wykorzystywana w rozwiązaniach ze świata rzeczywistego, patrząc na jedno studium przypadku: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot to twój "Programista Partnerski AI" - przekształca tekstowe prompty w uzupełnienia kodu i jest zintegrowany z twoim środowiskiem programistycznym (np. Visual Studio Code) dla płynnego doświadczenia użytkownika. Jak udokumentowano w serii blogów poniżej, najwcześniejsza wersja była oparta na modelu OpenAI Codex - a inżynierowie szybko zdali sobie sprawę z potrzeby dostrojenia modelu i opracowania lepszych technik inżynierii promptów, aby poprawić jakość kodu. W lipcu [zadebiutowali z ulepszonym modelem AI, który wykracza poza Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) dla jeszcze szybszych sugestii.

Przeczytaj posty w kolejności, aby śledzić ich podróż edukacyjną.

- **Maj 2023** | [GitHub Copilot staje się lepszy w rozumieniu twojego kodu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Wewnątrz GitHub: Praca z LLM stojącymi za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Czerwiec 2023** | [Jak pisać lepsze prompty dla GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Lipiec 2023** | [.. GitHub Copilot wykracza poza Codex z ulepszonym modelem AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Lipiec 2023** | [Przewodnik Developera po Inżynierii Promptów i LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Wrzesień 2023** | [Jak zbudować aplikację LLM dla przedsiębiorstw: Lekcje z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Możesz również przeglądać ich [blog inżynieryjny](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) w poszukiwaniu postów takich jak [ten](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), który pokazuje, jak te modele i techniki są _stosowane_ do napędzania aplikacji ze świata rzeczywistego.

---

## Konstrukcja Promptu

Zobaczyliśmy, dlaczego inżynieria promptów jest ważna - teraz zrozummy, jak prompty są _konstruowane_, abyśmy mogli ocenić różne techniki dla bardziej efektywnego projektowania promptów.

### Podstawowy Prompt

Zacznijmy od podstawowego promptu: wejścia tekstowego wysłanego do modelu bez żadnego innego kontekstu. Oto przykład - gdy wysyłamy pierwsze kilka słów amerykańskiego hymnu narodowego do [API Completion](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) OpenAI, natychmiast _uzupełnia_ ono odpowiedź kolejnymi kilkoma wersami, ilustrując podstawowe zachowanie predykcyjne.

| Prompt (Wejście)   | Uzupełnienie (Wyjście)                                                                                                  |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Wygląda na to, że zaczynasz tekst "The Star-Spangled Banner", hymnu narodowego Stanów Zjednoczonych. Pełny tekst to ... |

### Złożony Prompt

Teraz dodajmy kontekst i instrukcje do tego podstawowego promptu. [API Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) pozwala nam konstruować złożony prompt jako zbiór _wiadomości_ z:

- Pary wejście/wyjście odzwierciedlające dane wejściowe _użytkownika_ i odpowiedź _asystenta_.
- Wiadomość systemowa ustalająca kontekst dla zachowania lub osobowości asystenta.

Zapytanie jest teraz w formie poniżej, gdzie _tokenizacja_ skutecznie przechwytuje istotne informacje z kontekstu i konwersacji. Teraz zmiana kontekstu systemowego może mieć równie istotny wpływ na jakość uzupełnień, jak dane wejściowe użytkownika.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Jesteś pomocnym asystentem."},
        {"role": "user", "content": "Kto wygrał mistrzostwa świata w 2020?"},
        {"role": "assistant", "content": "Los Angeles Dodgers wygrali World Series w 2020 roku."},
        {"role": "user", "content": "Gdzie były rozgrywane?"}
    ]
)
```

### Prompt Instrukcyjny

W powyższych przykładach, prompt użytkownika był prostym zapytaniem tekstowym, które może być interpretowane jako prośba o informacje. Z promptami _instrukcyjnymi_, możemy użyć tego tekstu do bardziej szczegółowego określenia zadania, dostarczając lepsze wskazówki dla AI. Oto przykład:

| Prompt (Wejście)                                                                                                                                                                                       | Uzupełnienie (Wyjście)                                                                                                                                  | Typ Instrukcji         |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------- |
| Napisz opis wojny secesyjnej                                                                                                                                                                           | _zwrócił prosty akapit_                                                                                                                                 | Proste                 |
| Napisz opis wojny secesyjnej. Podaj kluczowe daty i wydarzenia oraz opisz ich znaczenie                                                                                                                | _zwrócił akapit, a następnie listę kluczowych dat wydarzeń z opisami_                                                                                   | Złożone                |
| Napisz opis wojny secesyjnej w 1 akapicie. Podaj 3 punkty z kluczowymi datami i ich znaczeniem. Podaj 3 kolejne punkty z kluczowymi postaciami historycznymi i ich wkładem. Zwróć wynik jako plik JSON | _zwraca bardziej obszerne szczegóły w polu tekstowym, sformatowane jako JSON, które możesz skopiować i wkleić do pliku i zweryfikować w razie potrzeby_ | Złożone. Sformatowane. |

## Główna Treść

W powyższych przykładach prompt był nadal dość otwarty, pozwalając LLM zdecydować, która część jego wstępnie wytrenowanego zbioru danych była istotna. Przy wzorcu projektowym _głównej treści_, tekst wejściowy jest podzielony na dwie części:

- instrukcja (działanie)
- istotna treść (która wpływa na działanie)

Oto przykład, gdzie instrukcją jest "podsumuj to w 2 zdaniach".

| Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Uzupełnienie (Wyjście)                                                                                                                                                                                                                                                                                                        |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest to gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż wszystkie inne planety w Układzie Słonecznym razem wzięte. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom od czasów sprzed zapisanej historii. Został nazwany na cześć rzymskiego boga Jowisza.[19] Widziany z Ziemi, Jowisz może być na tyle jasny, że jego odbite światło rzuca widoczne cienie,[20] i średnio jest trzecim najjaśniejszym naturalnym obiektem na nocnym niebie po Księżycu i Wenus. <br/> **Podsumuj to w 2 krótkich zdaniach** | Jowisz, piąta planeta od Słońca, jest największą w Układzie Słonecznym i jest znany z bycia jednym z najjaśniejszych obiektów na nocnym niebie. Nazwany na cześć rzymskiego boga Jowisza, jest gazowym olbrzymem, którego masa jest dwa i pół razy większa niż wszystkich innych planet w Układzie Słonecznym razem wziętych. |

Segment głównej treści może być używany na różne sposoby, aby napędzać bardziej efektywne instrukcje:

- **Przykłady** - zamiast mówić modelowi, co ma robić za pomocą jawnej instrukcji, daj mu przykłady tego, co ma robić i pozwól mu wywnioskować wzorzec dla pożądanego wyjścia.
- **Wskazówki** - podążaj za instrukcją z "wskazówką", która nakierowuje uzupełnienie, prowadząc model w kierunku bardziej odpowiednich odpowiedzi.
- **Szablony** - są to powtarzalne 'przepisy' na prompty z elementami zastępczymi (zmiennymi), które mogą być dostosowane za pomocą danych dla konkretnych przypadków użycia.

Przyjrzyjmy się im w działaniu.

### Używanie Przykładów

Jest to podejście, w którym używasz głównej treści, aby "podać modelowi" kilka przykładów pożądanego wyjścia dla danej instrukcji i pozwolić mu wywnioskować wzorzec dla pożądanego wyjścia. W zależności od liczby podanych przykładów możemy mieć prompt zero-shot, one-shot, few-shot itp.

Prompt składa się teraz z trzech składników:

- Opis zadania
- Kilka przykładów pożądanego wyjścia
- Początek nowego przykładu (który staje się niejawnym opisem zadania)

| Typ Uczenia | Prompt (Wejście)                                                                                                                                        | Uzupełnienie (Wyjście)      |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------- |
| Zero-shot   | "The Sun is Shining". Przetłumacz na hiszpański                                                                                                         | "El Sol está brillando".    |
| One-shot    | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                   | "Es un día frío y ventoso". |
| Few-shot    | Zawodnik przebiegł bazy => Baseball <br/> Zawodnik zaserwował asa => Tenis <br/> Zawodnik zdobył szóstkę => Krykiet <br/> Zawodnik wykonał slam-dunk => | Koszykówka                  |
|             |                                                                                                                                                         |                             |

Zauważ, jak musieliśmy podać jawną instrukcję ("Przetłumacz na hiszpański") w promptowaniu zero-shot, ale jest ona wywnioskowana w przykładzie promptowania one-shot. Przykład few-shot pokazuje, jak dodanie większej liczby przykładów pozwala modelom na bardziej dokładne wnioskowanie bez dodatkowych instrukcji.

### Wskazówki w Promptach

Inną techniką wykorzystania głównej treści jest podawanie _wskazówek_ zamiast przykładów. W tym przypadku dajemy modelowi wskazówkę we właściwym kierunku, _rozpoczynając_ od fragmentu, który odzwierciedla pożądany format odpowiedzi. Model następnie "bierze wskazówkę", aby kontynuować w tym duchu.

| Liczba wskazówek | Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Uzupełnienie (Wyjście)                                                                                                                                                                                                                                                             |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest to gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż wszystkie inne planety w Układzie Słonecznym razem wzięte. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom od czasów sprzed zapisanej historii. <br/>**Podsumuj To**                                                          | Jowisz to największa planeta w naszym Układzie Słonecznym i piąta od Słońca. Jest gazowym olbrzymem o masie 1/1000 masy Słońca, ale jest cięższy niż wszystkie inne planety razem wzięte. Starożytne cywilizacje znały Jowisza od dawna i jest on łatwo widoczny na nocnym niebie. |
| 1                | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest to gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż wszystkie inne planety w Układzie Słonecznym razem wzięte. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom od czasów sprzed zapisanej historii. <br/>**Podsumuj To** <br/> Czego się dowiedzieliśmy, to że Jowisz             | jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż wszystkie inne planety razem wzięte. Jest łatwo widoczny gołym okiem i był znany od czasów starożytnych.            |
| 2                | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest to gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż wszystkie inne planety w Układzie Słonecznym razem wzięte. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom od czasów sprzed zapisanej historii. <br/>**Podsumuj To** <br/> 3 Najważniejsze Fakty, Których Się Dowiedzieliśmy: | 1. Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. <br/> 2. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca...<br/> 3. Jowisz jest widoczny gołym okiem od czasów starożytnych ...                                                            |
|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                    |

### Szablony Promptów

Szablon promptu to _predefiniowany przepis na prompt_, który może być przechowywany i ponownie używany w razie potrzeby, aby napędzać bardziej spójne doświadczenia użytkownika na dużą skalę. W najprostszej formie jest to po prostu kolekcja przykładów promptów, takich jak [ten od OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), który zapewnia zarówno interaktywne komponenty promptu (wiadomości użytkownika i systemu), jak i format żądania oparty na API - aby wspierać ponowne użycie.

W bardziej złożonej formie, takiej jak [ten przykład z LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), zawiera _elementy zastępcze_, które mogą być zastąpione danymi z różnych źródeł (dane wejściowe użytkownika, kontekst systemu, zewnętrzne źródła danych itp.), aby dynamicznie generować prompt. Pozwala to nam stworzyć bibliotekę wielokrotnego użytku promptów, które mogą być używane do napędzania spójnych doświadczeń użytkownika **programistycznie** na dużą skalę.

Ostatecznie, prawdziwa wartość szablonów leży w możliwości tworzenia i publikowania _bibliotek promptów_ dla pionowych domen aplikacji - gdzie szablon promptu jest teraz _zoptymalizowany_, aby odzwierciedlać kontekst specyficzny dla aplikacji lub przykłady, które czynią odpowiedzi bardziej odpowiednimi i dokładnymi dla docelowej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest świetnym przykładem tego podejścia, kuratorując bibliotekę promptów dla dziedziny edukacji z naciskiem na kluczowe cele, takie jak planowanie lekcji, projektowanie programu nauczania, korepetycje dla studentów itp.

## Treść Wspierająca

Jeśli myślimy o konstrukcji promptu jako mającej instrukcję (zadanie) i cel (główna treść), to _treść drugorzędna_ jest jak dodatkowy kontekst, który zapewniamy, aby **wpłynąć na wynik w jakiś sposób**. Mogą to być parametry dostrajające, instrukcje formatowania, taksonomie tematów itp., które mogą pomóc modelowi _dostosować_ jego odpowiedź, aby odpowiadała pożądanym celom lub oczekiwaniom użytkownika.

Na przykład: Mając katalog kursów z obszernymi metadanymi (nazwa, opis, poziom, tagi metadanych, instruktor itp.) na temat wszystkich dostępnych kursów w programie:

- możemy zdefiniować instrukcję, aby "podsumować katalog kursów na jesień 2023"
- możemy użyć głównej treści, aby podać kilka przykładów pożądanego wyjścia
- możemy użyć treści drugorzędnej, aby zidentyfikować 5 najważniejszych "tagów" zainteresowania.

Teraz model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów - ale jeśli wynik ma wiele tagów, może priorytetowo traktować 5 tagów zidentyfikowanych w treści drugorzędnej.

## Najlepsze Praktyki Promptowania

Teraz, gdy wiemy, jak prompty mogą być _konstruowane_, możemy zacząć myśleć o tym, jak je _projektować_, aby odzwierciedlały najlepsze praktyki. Możemy myśleć o tym w dwóch częściach - mając właściwe _podejście_ i stosując właściwe _techniki_.

### Podejście do Inżynierii Promptów

Inżynieria Promptów to proces prób i błędów, więc miej na uwadze trzy ogólne czynniki przewodnie:

1. **Zrozumienie Domeny Ma Znaczenie.** Dokładność i trafność odpowiedzi jest funkcją _domeny_, w której działa dana aplikacja lub użytkownik. Zastosuj swoją intuicję i wiedzę dziedzinową, aby **dostosować techniki** dalej. Na przykład zdefiniuj _osobowości specyficzne dla domeny_ w twoich promptach systemowych lub użyj _szablonów specyficznych dla domeny_ w twoich promptach użytkownika. Dostarcz treści drugorzędne, które odzwierciedlają konteksty specyficzne dla domeny, lub użyj _wskazówek i przykładów specyficznych dla domeny_, aby prowadzić model w kierunku znanych wzorców użycia.

2. **Zrozumienie Modelu Ma Znaczenie.** Wiemy, że modele są z natury stochastyczne. Ale implementacje modeli mogą również różnić się pod względem zestawu danych treningowych, których używają (wstępnie wytrenowana wiedza), możliwości, które zapewniają (np. za pośrednictwem API lub SDK) oraz rodzaju treści, do których są zoptymalizowane (np. kod vs obrazy vs tekst). Zrozum mocne i słabe strony używanego modelu i wykorzystaj tę wiedzę do _priorytetyzacji zadań_ lub budowania _dostosowanych szablonów_, które są zoptymalizowane pod kątem możliwości modelu.

3. **Iteracja i Walidacja Mają Znaczenie.** Modele ewoluują szybko, podobnie jak techniki inżynierii promptów. Jako ekspert w danej dziedzinie, możesz mieć inny kontekst lub kryteria dla _swojej_ konkretnej aplikacji, które mogą nie dotyczyć szerszej społeczności. Wykorzystaj narzędzia i techniki inżynierii promptów, aby "przyspieszyć" konstrukcję promptów, a następnie iteruj i waliduj wyniki, używając własnej intuicji i wiedzy dziedzinowej. Zapisuj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), która może być używana jako nowy punkt wyjścia przez innych, dla szybszych iteracji w przyszłości.

## Najlepsze Praktyki

Przyjrzyjmy się teraz wspólnym najlepszym praktykom, które są zalecane przez praktyków [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                                         | Dlaczego                                                                                                                                                                                                                                                            |
| :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Oceniaj najnowsze modele.                  | Nowe generacje modeli prawdopodobnie będą miały ulepszone funkcje i jakość - ale mogą również wiązać się z wyższymi kosztami. Oceń je pod kątem wpływu, a następnie podejmij decyzje o migracji.                                                                    |
| Oddzielaj instrukcje i kontekst            | Sprawdź, czy twój model/dostawca definiuje _ograniczniki_, aby wyraźniej odróżnić instrukcje, treść główną i treść drugorzędną. Może to pomóc modelom dokładniej przypisywać wagi do tokenów.                                                                       |
| Bądź konkretny i jasny                     | Podaj więcej szczegółów dotyczących pożądanego kontekstu, wyniku, długości, formatu, stylu itp. Poprawi to zarówno jakość, jak i spójność odpowiedzi. Zapisuj przepisy w szablonach wielokrotnego użytku.                                                           |
| Bądź opisowy, używaj przykładów            | Modele mogą lepiej reagować na podejście "pokaż i powiedz". Zacznij od podejścia `zero-shot`, gdzie dajesz mu instrukcję (ale bez przykładów), a następnie spróbuj `few-shot` jako udoskonalenie, dostarczając kilka przykładów pożądanego wyniku. Używaj analogii. |
| Używaj wskazówek do rozpoczęcia uzupełnień | Nakieruj go na pożądany wynik, dając mu kilka wiodących słów lub fraz, które może wykorzystać jako punkt wyjścia dla odpowiedzi.                                                                                                                                    |
| Podwójnie wzmacniaj                        | Czasami może być potrzebne powtórzenie się modelowi. Dawaj instrukcje przed i po głównej treści, używaj instrukcji i wskazówki itp. Iteruj i waliduj, aby zobaczyć, co działa.                                                                                      |
| Kolejność Ma Znaczenie                     | Kolejność, w jakiej prezentujesz informacje modelowi, może wpływać na wynik, nawet w przykładach uczenia się, dzięki tendencyjności do faworyzowania ostatnich informacji. Wypróbuj różne opcje, aby zobaczyć, co działa najlepiej.                                 |
| Daj modelowi "wyjście"                     | Daj modelowi _awaryjną_ odpowiedź uzupełniającą, którą może dostarczyć, jeśli z jakiegokolwiek powodu nie może wykonać zadania. Może to zmniejszyć szanse, że modele generują fałszywe lub zmyślone odpowiedzi.                                                     |
|                                            |                                                                                                                                                                                                                                                                     |

Jak w przypadku każdej najlepszej praktyki, pamiętaj, że _twoje wyniki mogą się różnić_ w zależności od modelu, zadania i domeny. Wykorzystaj je jako punkt wyjścia i iteruj, aby znaleźć to, co działa najlepiej dla ciebie. Stale ponownie oceniaj swój proces inżynierii promptów w miarę, jak nowe modele i narzędzia stają się dostępne, skupiając się na skalowalności procesu i jakości odpowiedzi.

## Zadanie

Gratulacje! Dotarłeś do końca lekcji! Czas przetestować niektóre z tych koncepcji i technik na prawdziwych przykładach!

W ramach naszego zadania będziemy używać Notebooka Jupyter z ćwiczeniami, które możesz wykonać interaktywnie. Możesz również rozszerzyć Notebook o własne komórki Markdown i Code, aby eksplorować pomysły i techniki na własną rękę.

### Aby rozpocząć, sforkuj repozytorium, a następnie

- (Zalecane) Uruchom GitHub Codespaces
- (Alternatywnie) Sklonuj repozytorium na swoje lokalne urządzenie i użyj go z Docker Desktop
- (Alternatywnie) Otwórz Notebook za pomocą preferowanego środowiska wykonawczego Notebook.

### Następnie skonfiguruj swoje zmienne środowiskowe

- Skopiuj plik `.env.copy` w głównym katalogu repozytorium do `.env` i wypełnij wartości `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` i `AZURE_OPENAI_DEPLOYMENT`. Wróć do sekcji [Learning Sandbox](./04-prompt-engineering-fundamentals#learning-sandbox), aby dowiedzieć się jak.

### Następnie otwórz Notebook Jupyter

- Wybierz kernel środowiska wykonawczego. Jeśli używasz opcji 1 lub 2, po prostu wybierz domyślny kernel Python 3.10.x dostarczony przez kontener dev.

Jesteś gotowy do uruchomienia ćwiczeń. Zauważ, że nie ma tu _właściwych i niewłaściwych_ odpowiedzi - chodzi o eksplorowanie opcji metodą prób i błędów oraz budowanie intuicji, co działa dla danego modelu i domeny aplikacji.

_Z tego powodu w tej lekcji nie ma segmentów Code Solution. Zamiast tego, Notebook będzie miał komórki Markdown zatytułowane "Moje Rozwiązanie:", które pokazują jeden przykładowy wynik jako odniesienie._

## Test wiedzy

Który z poniższych jest dobrym promptem, zgodnym z rozsądnymi najlepszymi praktykami?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo model XC90 zaparkowanego przy klifie z zachodzącym słońcem
3. Pokaż mi obraz czerwonego samochodu marki Volvo model XC90

Odp: 2, to najlepszy prompt, ponieważ zawiera szczegóły dotyczące "czego" i wchodzi w szczegóły (nie tylko dowolny samochód, ale konkretna marka i model) oraz opisuje ogólne otoczenie. 3 jest następny najlepszy, ponieważ również zawiera dużo opisu.

## 🚀 Wyzwanie

Spróbuj wykorzystać technikę "wskazówki" z promptem: Dokończ zdanie "Pokaż mi obraz czerwonego samochodu marki Volvo i ". Co odpowiada i jak byś to ulepszył?

## Świetna Praca! Kontynuuj Naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach Inżynierii Promptów? Przejdź do [strony kontynuacji nauki](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne świetne zasoby na ten temat.

Przejdź do Lekcji 5, gdzie przyjrzymy się [zaawansowanym technikom promptowania](../../../05-advanced-prompts/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
