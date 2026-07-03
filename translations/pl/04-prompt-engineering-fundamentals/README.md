# Podstawy Inżynierii Promptów

[![Podstawy Inżynierii Promptów](../../../translated_images/pl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Wprowadzenie
Ten moduł obejmuje podstawowe koncepcje i techniki tworzenia skutecznych promptów w modelach AI generatywnej. Sposób, w jaki piszesz swój prompt do LLM, również ma znaczenie. Starannie zaprojektowany prompt może osiągnąć lepszą jakość odpowiedzi. Ale co dokładnie oznaczają terminy takie jak _prompt_ i _inżynieria promptów_? I jak ulepszyć _wejście_ promptu, które wysyłam do LLM? To są pytania, na które spróbujemy odpowiedzieć w tym rozdziale i kolejnym.

_Generatywna AI_ potrafi tworzyć nową zawartość (np. tekst, obrazy, dźwięk, kod itd.) w odpowiedzi na zapytania użytkownika. Osiąga to dzięki _Dużym Modelom Językowym_ takim jak seria GPT firmy OpenAI ("Generative Pre-trained Transformer"), które są trenowane do używania języka naturalnego i kodu.

Użytkownicy mogą teraz wchodzić w interakcje z tymi modelami za pomocą znanych paradygmatów, takich jak czat, bez potrzeby posiadania wiedzy technicznej czy szkolenia. Modele są _oparte na promptach_ – użytkownicy wysyłają tekstowe wejście (prompt) i otrzymują odpowiedź AI (completion). Mogą następnie iteracyjnie „rozmawiać z AI”, w wieloetapowych rozmowach, dopracowując prompt aż odpowiedź spełni ich oczekiwania.

„Prompty” stają się teraz głównym _interfejsem programistycznym_ dla aplikacji generatywnej AI, mówiąc modelom, co mają robić i wpływając na jakość zwracanych odpowiedzi. „Inżynieria promptów” to szybko rozwijająca się dziedzina badań, która skupia się na _projektowaniu i optymalizacji_ promptów, aby dostarczać spójne i jakościowe odpowiedzi na szeroką skalę.

## Cele nauki

W tej lekcji dowiemy się, czym jest Inżynieria Promptów, dlaczego ma znaczenie i jak tworzyć skuteczniejsze prompty dla danego modelu i celu aplikacji. Poznamy podstawowe koncepcje i najlepsze praktyki inżynierii promptów – a także dowiemy się o interaktywnym środowisku „sandbox” w Jupyter Notebook, gdzie możemy zobaczyć te koncepcje zastosowane na prawdziwych przykładach.

Na koniec tej lekcji będziemy potrafili:

1. Wyjaśnić, czym jest inżynieria promptów i dlaczego ma znaczenie.
2. Opisać składniki promptu i ich zastosowanie.
3. Poznać najlepsze praktyki i techniki inżynierii promptów.
4. Zastosować poznane techniki na rzeczywistych przykładach, korzystając z punktu końcowego OpenAI.

## Kluczowe terminy

Inżynieria Promptów: Praktyka projektowania i udoskonalania wejść, aby kierować modele AI ku uzyskaniu pożądanych wyników.  
Tokenizacja: Proces zamiany tekstu na mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetworzyć.  
Instrukcyjnie dostrojone LLM: Duże modele językowe (LLM), które zostały dopracowane za pomocą konkretnych instrukcji, aby poprawić dokładność i trafność ich odpowiedzi.

## Środowisko do nauki

Inżynieria promptów jest obecnie bardziej sztuką niż nauką. Najlepszym sposobem na poprawę intuicji w tym zakresie jest _ćwiczenie_ i przyjęcie metody prób i błędów łączącej wiedzę z dziedziny zastosowań z rekomendowanymi technikami i optymalizacjami specyficznymi dla modelu.

Dołączony do tej lekcji Jupyter Notebook zapewnia środowisko _sandbox_, w którym możesz wypróbować to, czego się uczysz – na bieżąco lub jako część zadania kodowego na końcu. Aby wykonać ćwiczenia, potrzebujesz:

1. **Klucz API Azure OpenAI** – punkt końcowy usługi dla wdrożonego LLM.  
2. **Środowisko uruchomieniowe Pythona** – w którym można uruchomić Notebook.  
3. **Lokalne zmienne środowiskowe** – _ukończ teraz kroki z [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst)_.

Notebook zawiera ćwiczenia _startowe_ – ale zachęcamy do dodawania własnych sekcji _Markdown_ (opisu) i _Code_ (żądania promptów), aby wypróbować więcej przykładów lub pomysłów – i budować intuicję projektową promptów.

## Ilustrowany przewodnik

Chcesz zobaczyć ogólny obraz tego, co ta lekcja obejmuje, zanim zaczniesz? Sprawdź ten ilustrowany przewodnik, który przedstawia główne omawiane tematy oraz najważniejsze wnioski do rozważenia w każdym z nich. Mapa drogowa lekcji prowadzi od zrozumienia podstawowych koncepcji i wyzwań do ich rozwiązywania za pomocą odpowiednich technik i najlepszych praktyk inżynierii promptów. Zauważ, że sekcja "Zaawansowane techniki" w tym przewodniku odnosi się do treści omawianych w _następnym_ rozdziale tego programu nauczania.

![Ilustrowany przewodnik po inżynierii promptów](../../../translated_images/pl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nasz Startup

Porozmawiajmy teraz o tym, jak _ten temat_ wiąże się z misją naszego startupu, by [wprowadzać innowacje AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje oparte na AI wspierające _personalizowaną naukę_ – pomyślmy więc, jak różni użytkownicy naszej aplikacji mogą „projektować” prompty:

- **Administratorzy** mogą poprosić AI o _analizę danych programów nauczania w celu zidentyfikowania braków w materiałach_. AI może podsumować wyniki lub zwizualizować je za pomocą kodu.  
- **Nauczyciele** mogą poprosić AI o _stworzenie planu lekcji dla określonej grupy odbiorców i tematu_. AI może zbudować spersonalizowany plan w określonym formacie.  
- **Uczniowie** mogą poprosić AI o _prowadzenie korepetycji z trudnego przedmiotu_. AI może teraz prowadzić uczniów lekcjami, wskazówkami i przykładami dostosowanymi do ich poziomu.

To tylko wierzchołek góry lodowej. Sprawdź [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – bibliotekę promptów open source kuratorowaną przez ekspertów edukacyjnych – aby uzyskać szersze pojęcie o możliwościach! _Wypróbuj niektóre z tych promptów w sandboxie lub używając OpenAI Playground, aby zobaczyć, co się stanie!_

<!--
SZABLON LEKCJI:
Ta jednostka powinna obejmować kluczową koncepcję #1.
Wzmacniaj koncepcję przykładami i odniesieniami.

KONCEPCJA #1:
Inżynieria promptów.
Zdefiniuj ją i wyjaśnij, dlaczego jest potrzebna.
-->

## Czym jest inżynieria promptów?

Rozpoczęliśmy tę lekcję od zdefiniowania **inżynierii promptów** jako procesu _projektowania i optymalizacji_ tekstowych wejść (promptów), aby dostarczać spójne i jakościowe odpowiedzi (completion) dla danego celu aplikacji i modelu. Możemy to postrzegać jako proces dwustopniowy:

- _projektowanie_ początkowego promptu dla danego modelu i celu  
- _doprecyzowywanie_ promptu iteracyjnie, by poprawić jakość odpowiedzi

Jest to nieodłącznie proces metodą prób i błędów, który wymaga intuicji użytkownika i wysiłku, by uzyskać optymalne wyniki. Dlaczego więc jest to ważne? Aby to odpowiedzieć, musimy najpierw zrozumieć trzy koncepcje:

- _Tokenizacja_ = jak model „widzi” prompt  
- _Bazowe LLM_ = jak model bazowy „przetwarza” prompt  
- _Instrukcyjnie dostrojone LLM_ = jak model teraz może rozumieć „zadania”

### Tokenizacja

LLM widzi prompty jako _ciąg tokenów_, gdzie różne modele (lub wersje tego samego modelu) mogą tokenizować ten sam prompt na różne sposoby. Ponieważ LLM-y są trenowane na tokenach (a nie na surowym tekście), sposób tokenizacji promptów ma bezpośredni wpływ na jakość generowanej odpowiedzi.

Aby zyskać intuicję, jak działa tokenizacja, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), pokazane poniżej. Wklej swój prompt – i zobacz, jak zostanie zamieniony na tokeny, zwracając uwagę na sposób traktowania znaków odstępu i znaków interpunkcyjnych. Zauważ, że ten przykład pokazuje starszy model LLM (GPT-3) – więc wypróbowanie tego z nowszym modelem może dać inny rezultat.

![Tokenizacja](../../../translated_images/pl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncepcja: Modele bazowe

Po tokenizacji promptu podstawową funkcją ["Bazowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (czyli modelu bazowego) jest przewidzenie tokenu w tym ciągu. Ponieważ LLM-y są trenowane na ogromnych zbiorach tekstu, mają dobre wyczucie statystycznych relacji między tokenami i mogą dokonać takiego przewidywania z pewnym zaufaniem. Należy zauważyć, że nie rozumieją _znaczenia_ słów w prompt lub tokenie; widzą tylko wzorzec, który mogą „uzupełnić” następnym przewidywaniem. Mogą kontynuować przewidywanie ciągu aż do momentu przerwania przez użytkownika lub spełnienia jakiegoś warunku.

Chcesz zobaczyć, jak działa uzupełnienie oparte na promptach? Wprowadź powyższy prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) z ustawieniami domyślnymi. System jest skonfigurowany do traktowania promptów jako zapytań o informacje – więc powinieneś zobaczyć odpowiedź spełniającą ten kontekst.

A co jeśli użytkownik chciałby zobaczyć coś specyficznego, co spełnia jakieś kryteria lub cel zadania? Właśnie tutaj pojawiają się _instrukcyjnie dostrojone_ LLM.

![Uzupełnienie czatu Bazowego LLM](../../../translated_images/pl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncepcja: Instrukcyjnie dostrojone LLM

[Instrukcyjnie dostrojony LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zaczyna od modelu bazowego i doprecyzowuje go na podstawie przykładów lub par wejście/wyjście (np. wieloetapowych „wiadomości”), które mogą zawierać jasne instrukcje – a odpowiedź AI próbuje tę instrukcję zastosować.

Wykorzystuje techniki takie jak uczenie ze wzmocnieniem z ludzką informacją zwrotną (RLHF), które mogą trenować model, by _podążał za instrukcjami_ i _uczył się na podstawie informacji zwrotnej_, dzięki czemu generuje odpowiedzi lepiej dopasowane do praktycznych zastosowań i bardziej relewantne względem celów użytkownika.

Wypróbujmy to – wróć do powyższego promptu, ale teraz zmień _wiadomość systemową_ tak, aby dać następującą instrukcję jako kontekst:

> _Podsumuj dostarczoną zawartość dla ucznia drugiej klasy. Zachowaj wynik w jednym akapicie z 3-5 punktami._

Zobacz, jak wynik teraz jest dostrojony, by odzwierciedlać pożądany cel i format? Nauczyciel może teraz bezpośrednio wykorzystać tę odpowiedź w swoich materiałach na tę lekcję.

![Uzupełnienie czatu Instrukcyjnie dostrojonego LLM](../../../translated_images/pl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Dlaczego potrzebujemy inżynierii promptów?

Teraz, gdy wiemy, jak LLM przetwarzają prompty, porozmawiajmy o tym, _dlaczego_ potrzebujemy inżynierii promptów. Odpowiedź leży w tym, że obecne LLM wiążą się z wieloma wyzwaniami, które utrudniają _uzyskanie niezawodnych i spójnych uzupełnień_ bez wysiłku włożonego w konstrukcję i optymalizację promptu. Na przykład:

1. **Odpowiedzi modelu są stochastyczne.** _Ten sam prompt_ prawdopodobnie wygeneruje różne odpowiedzi dla różnych modeli lub wersji modelu. Może też dać różne wyniki dla _tego samego modelu_ w różnym czasie. _Techniki inżynierii promptów mogą pomóc zminimalizować te różnice, zapewniając lepsze zabezpieczenia_.

1. **Modele mogą fabrykować odpowiedzi.** Modele są wstępnie trenowane na _dużych, ale skończonych_ zbiorach danych, co oznacza, że nie mają wiedzy o pojęciach spoza zakresu treningu. W efekcie mogą generować uzupełnienia nieścisłe, wyimaginowane lub sprzeczne z powszechnie znanymi faktami. _Techniki inżynierii promptów pomagają użytkownikom identyfikować i ograniczać takie fabrykacje, np. poprzez proszenie AI o cytaty lub uzasadnienia_.

1. **Możliwości modeli będą się różnić.** Nowsze modele lub generacje modeli mają bogatsze możliwości, ale również charakterystyczne cechy i kompromisy kosztowe oraz złożoności. _Inżynieria promptów może pomóc wypracować najlepsze praktyki i przepływy pracy, które abstrahują różnice i dostosowują się do wymagań specyficznych modeli w skalowalny i płynny sposób_.

Zobacz to w praktyce w OpenAI lub Azure OpenAI Playground:

- Użyj tego samego promptu z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) – czy zauważyłeś różnice?  
- Używaj tego samego promptu wielokrotnie z tym _samym_ wdrożeniem LLM (np. playground Azure OpenAI) – jak różniły się te odpowiedzi?

### Przykład fabrykacji

W tym kursie używamy terminu **„fabrykacja”** na oznaczenie zjawiska, w którym LLM-y czasem generują faktycznie nieprawdziwe informacje z powodu ograniczeń w treningu lub innych czynników. Możesz też spotkać się z nazwą _„halucynacje”_ w popularnych artykułach lub pracach badawczych. Jednak zdecydowanie zalecamy używanie terminu _„fabrykacja”_, aby nie antropomorfizować tego zachowania, przypisując maszynowemu wynikowi cechę ludzką. Wspiera to też [wytyczne dotyczące odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) od strony terminologii, eliminując zwroty, które mogą być uważane za obraźliwe lub wykluczające w niektórych kontekstach.

Chcesz zobaczyć, jak działają fabrykacje? Pomyśl o promptcie, który nakazuje AI wygenerować zawartość na nieistniejący temat (aby upewnić się, że nie jest on zawarty w zbiorze treningowym). Na przykład – wypróbowałem taki prompt:

> **Prompt:** wygeneruj plan lekcji dotyczący Wojny Marsjańskiej z 2076 roku.
Wyszukiwanie w sieci pokazało, że istniały fikcyjne relacje (np. seriale telewizyjne lub książki) o wojnach marsjańskich – ale żadna z nich nie dotyczyła roku 2076. Zdrowy rozsądek również podpowiada, że 2076 to _przyszłość_, więc nie może być powiązany z rzeczywistym wydarzeniem.

Co się zatem stanie, gdy uruchomimy ten prompt u różnych dostawców LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpowiedź 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Jak można się spodziewać, każdy model (lub jego wersja) generuje nieco inne odpowiedzi dzięki zachowaniom stochastycznym i różnicom w możliwościach modelu. Na przykład jeden model kieruje swoją odpowiedź do uczniów 8 klasy, a inny zakłada odbiorców na poziomie szkoły średniej. Jednak wszystkie trzy modele wygenerowały odpowiedzi, które mogłyby przekonać nieświadomego użytkownika, że wydarzenie było prawdziwe.

Techniki inżynierii promptu, takie jak _metaprompting_ oraz _konfiguracja temperatury_, mogą w pewnym stopniu zmniejszyć liczbę fikcji generowanych przez modele. Nowe _architektury_ promptów także bezszwowo integrują narzędzia i techniki w przepływ promptu, aby łagodzić lub redukować niektóre z tych efektów.

## Studium Przypadku: GitHub Copilot

Podsumujmy tę sekcję, przyglądając się, jak inżynieria promptu jest wykorzystywana w rozwiązaniach rzeczywistych, analizując jedno Studium Przypadku: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot to twój „AI Pair Programmer” - przekształca tekstowe prompty w uzupełnienia kodu i jest zintegrowany z twoim środowiskiem programistycznym (np. Visual Studio Code), zapewniając płynne doświadczenie użytkownika. Jak opisano w serii blogów poniżej, pierwsza wersja opierała się na modelu OpenAI Codex – a inżynierowie szybko dostrzegli potrzebę dopracowania modelu i opracowania lepszych technik inżynierii promptu, aby poprawić jakość kodu. W lipcu [zadebiutowali ulepszonym modelem AI, który przewyższa Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), oferując jeszcze szybsze sugestie.

Przeczytaj wpisy po kolei, aby śledzić ich proces uczenia się.

- **Maj 2023** | [GitHub Copilot lepiej rozumie twój kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Od kuchni GitHub: Praca z LLM stojącymi za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Czerwiec 2023** | [Jak pisać lepsze prompty do GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Lipiec 2023** | [.. GitHub Copilot przekracza Codex z ulepszonym modelem AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Lipiec 2023** | [Przewodnik programisty po inżynierii promptów i LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Wrzesień 2023** | [Jak zbudować korporacyjną aplikację LLM: Lekcje od GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Możesz także przeglądać ich [blog techniczny](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) po więcej wpisów takich jak [ten](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), który pokazuje jak te modele i techniki są _stosowane_ do napędzania rzeczywistych aplikacji.

---

<!--
SZABLON LEKCJI:
Ta jednostka powinna obejmować koncepcję #2.
Wzmocnij koncepcję przykładami i odniesieniami.

KONCEPCJA #2:
Projektowanie promptów.
Zilustrowane przykładami.
-->

## Budowa Promptu

Widzieliśmy, dlaczego inżynieria promptu jest ważna – teraz zrozummy, jak prompty są _konstruowane_, aby móc ocenić różne techniki dla skuteczniejszego projektowania promptów.

### Podstawowy Prompt

Zacznijmy od podstawowego promptu: tekstowego wejścia wysłanego do modelu bez dodatkowego kontekstu. Oto przykład – gdy wysyłamy pierwsze kilka słów hymnu narodowego USA do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), natychmiast _uzupełnia_ odpowiedź kolejnymi liniami, ilustrując podstawowe zachowanie predykcyjne.

| Prompt (Wejście)     | Uzupełnienie (Wyjście)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Wygląda na to, że zaczynasz tekst piosenki "The Star-Spangled Banner", hymnu narodowego Stanów Zjednoczonych. Pełne teksty to ... |

### Złożony Prompt

Teraz dodajmy do tego podstawowego promptu kontekst i instrukcje. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) pozwala nam tworzyć złożony prompt jako zbiór _wiadomości_ z:

- parami wejście/wyjście odzwierciedlającymi dane _użytkownika_ i odpowiedź _asystenta_.
- wiadomością systemową ustalającą kontekst zachowania lub osobowości asystenta.

Żądanie ma teraz poniższą formę, gdzie _tokenizacja_ skutecznie obejmuje istotne informacje z kontekstu i rozmowy. Zmiana systemowego kontekstu może mieć więc równie duży wpływ na jakość uzupełnień, co wprowadzane dane od użytkownika.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukcyjny Prompt

W powyższych przykładach prompt od użytkownika był prostym zapytaniem tekstowym, które można interpretować jako prośbę o informację. W promptach _instrukcyjnych_ możemy użyć tekstu, aby dokładniej określić zadanie, dając lepsze wskazówki AI. Oto przykład:

| Prompt (Wejście)                                                                                                                                                                                                                         | Uzupełnienie (Wyjście)                                                                                                        | Typ Instrukcji      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napisz opis Wojny Secesyjnej                                                                                                                                                                                                   | _zwrócono prosty akapit_                                                                                              | Prosty              |
| Napisz opis Wojny Secesyjnej. Podaj kluczowe daty i wydarzenia oraz opisz ich znaczenie                                                                                                                                     | _zwrócono akapit z listą kluczowych dat wydarzeń i opisami_                                             | Złożony             |
| Napisz opis Wojny Secesyjnej w 1 akapicie. Podaj 3 punkty kluczowych dat i ich znaczenie. Podaj 3 kolejne punkty z kluczowymi postaciami historycznymi i ich wkładem. Zwróć wynik jako plik JSON | _zwraca bardziej rozbudowane szczegóły w polu tekstowym, sformatowane jako JSON, które można skopiować i zweryfikować w razie potrzeby_ | Złożony. Sformatowany. |

## Główna Treść

W powyższych przykładach prompt był wciąż dość otwarty, pozwalając LLM zdecydować, jaka część wstępnie wytrenowanego zestawu danych jest istotna. W wzorcu projektowym _primary content_ tekst wejściowy jest podzielony na dwie części:

- instrukcję (akcję)
- dane kontekstowe (wpływające na wykonanie)

Oto przykład, gdzie instrukcja brzmi: „podsumuj to w 2 zdaniach”.

| Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Uzupełnienie (Wyjście)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale waży dwa i pół razy więcej niż wszystkie pozostałe planety Układu Słonecznego razem wzięte. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i znany był starożytnym cywilizacjom na długo przed zarejestrowaną historią. Nazwany jest na cześć rzymskiego boga Jowisza.[19] Widoczny z Ziemi Jowisz może być na tyle jasny, że jego odbite światło rzuca widoczne cienie,[20] i jest średnio trzecim najjaśniejszym naturalnym obiektem na nocnym niebie po Księżycu i Wenus. <br/> **Podsumuj to w 2 krótkich zdaniach** | Jowisz, piąta planeta od Słońca, jest największą w Układzie Słonecznym i znany jest jako jeden z najjaśniejszych obiektów na nocnym niebie. Nazwany na cześć rzymskiego boga Jowisza, jest gazowym olbrzymem o masie dwa i pół raza większej niż suma mas pozostałych planet Układu Słonecznego. |

Segment głównej treści można wykorzystać na różne sposoby, aby uzyskać skuteczniejsze instrukcje:

- **Przykłady** – zamiast mówić modelowi, co ma zrobić, podaj mu przykłady, aby wywnioskował wzór.
- **Wskazówki** – tuż po instrukcji dodaj „wskazówkę”, która zapoczątkuje uzupełnienie, kierując model ku bardziej odpowiednim odpowiedziom.
- **Szablony** – to powtarzalne „przepisy” na prompty z miejscami na dane (zmienne), które można dostosować do konkretnych przypadków użycia.

Przyjrzyjmy się temu w praktyce.

### Używanie Przykładów

To podejście, w którym wykorzystujesz główną treść, by „nakarmić model” przykładami oczekiwanego wyniku dla danej instrukcji i pozwolić mu wywnioskować wzór. W zależności od liczby przykładów rozróżniamy zero-shot prompting, one-shot prompting, few-shot prompting itd.

Prompt składa się teraz z trzech elementów:

- opis zadania
- kilka przykładów oczekiwanego wyniku
- rozpoczęcie nowego przykładu (który staje się implicitnym opisem zadania)

| Typ Nauki    | Prompt (Wejście)                                                                                                                                        | Uzupełnienie (Wyjście)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Przetłumacz na hiszpański                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Zauważ, że przy zero-shot prompting musieliśmy podać wyraźną instrukcję („Przetłumacz na hiszpański”), a w przykładzie one-shot jest ona domyślona. Przykład few-shot pokazuje, że dodanie większej liczby przykładów pozwala modelowi dokonywać dokładniejszych wniosków bez dodatkowych instrukcji.

### Wskazówki Promptu

Inną techniką użycia głównej treści jest podawanie _wskazówek_ zamiast przykładów. W tym przypadku dajemy modelowi „popych”, rozpoczynając od fragmentu, który odzwierciedla pożądany format odpowiedzi. Model „bierze wskazówkę” i kontynuuje w tym stylu.

| Liczba Wskazówek | Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Uzupełnienie (Wyjście)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale waży dwa i pół razy więcej niż wszystkie pozostałe planety Układu Słonecznego razem wzięte. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie, i znany był starożytnym cywilizacjom na długo przed zarejestrowaną historią. <br/>**Podsumuj to**                                       | Jowisz jest największą planetą w Układzie Słonecznym i piątą od Słońca. Jest gazowym olbrzymem o masie 1/1000 masy Słońca, ale cięższym niż wszystkie inne planety razem wzięte. Starożytne cywilizacje znały Jowisza od dawna, jest łatwo widoczny na nocnym niebie.. |
| 1              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwie i pół razy większej niż masa wszystkich pozostałych planet Układu Słonecznego razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisem historii. <br/>**Podsumowanie** <br/> Czego się dowiedzieliśmy, to że Jowisz | jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwie i pół razy większej niż masa wszystkich pozostałych planet razem wziętych. Jest łatwo widoczny gołym okiem i znany od czasów starożytnych.                        |
| 2              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwie i pół razy większej niż masa wszystkich pozostałych planet Układu Słonecznego razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisem historii. <br/>**Podsumowanie** <br/> 3 Najważniejsze Fakty, Które Poznaliśmy:         | 1. Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. <br/> 2. To gazowy olbrzym o masie jednej tysięcznej masy Słońca...<br/> 3. Jowisz był widoczny gołym okiem od czasów starożytnych...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Szablony promptów

Szablon promptu to _wstępnie zdefiniowany przepis na prompt_, który można przechowywać i używać wielokrotnie w celu zapewnienia bardziej spójnych doświadczeń użytkownika na dużą skalę. W najprostszej formie jest to po prostu zbiór przykładów promptów, takich jak [ten od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), który dostarcza zarówno interaktywne komponenty promptu (wiadomości użytkownika i systemu), jak i format żądania sterowany przez API – aby wspierać ponowne użycie.

W bardziej złożonej formie, jak [ten przykład od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), zawiera _placeholdery_, które można zastąpić danymi z różnych źródeł (wprowadzonych przez użytkownika, kontekst systemowy, zewnętrzne źródła danych itp.), aby dynamicznie generować prompt. Pozwala to na tworzenie biblioteki powtarzalnych promptów, które można stosować programatycznie do zapewnienia spójnych doświadczeń użytkownika na dużą skalę.

Ostatecznie prawdziwa wartość szablonów polega na możliwości tworzenia i publikowania _bibliotek promptów_ dla konkretnych domen zastosowań – gdzie szablon promptu jest teraz _optymalizowany_, aby odzwierciedlać kontekst lub przykłady specyficzne dla aplikacji, co sprawia, że odpowiedzi są bardziej trafne i dokładne dla wybranej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest doskonałym przykładem tego podejścia, gromadząc bibliotekę promptów dla edukacji, z naciskiem na kluczowe cele, takie jak planowanie lekcji, projektowanie programu nauczania, tutoring uczniów itd.

## Wspierające treści

Jeśli postrzegamy konstrukcję promptu jako posiadanie instrukcji (zadania) i celu (główna treść), to _treść wtórna_ działa jak dodatkowy kontekst, który dostarczamy, aby **wpłynąć na wynik w jakiś sposób**. Mogą to być parametry regulacji, instrukcje formatowania, taksonomie tematów itd., które pomagają modelowi _dopasować_ odpowiedź do zamierzonych celów lub oczekiwań użytkownika.

Na przykład: Mając katalog kursów z obszernymi metadanymi (nazwa, opis, poziom, tagi metadanych, prowadzący itp.) dotyczącymi wszystkich dostępnych kursów w programie:

- możemy zdefiniować instrukcję „podsumuj katalog kursów na jesień 2023”
- możemy użyć głównej treści do podania kilku przykładów pożądanego wyniku
- możemy użyć treści wtórnej do wskazania 5 najważniejszych „tagów” zainteresowania.

W ten sposób model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów – ale jeśli dany wynik zawiera wiele tagów, może skoncentrować się na 5 tagach wskazanych w treści wtórnej.

---

<!--
SZABLON LEKCJI:
Ten rozdział powinien obejmować podstawową koncepcję #1.
Wzmacniaj koncepcję przykładami i odniesieniami.

KONCEPCJA #3:
Techniki inżynierii promptów.
Jakie są podstawowe techniki inżynierii promptów?
Zilustruj to kilkoma ćwiczeniami.
-->

## Najlepsze praktyki przy tworzeniu promptów

Teraz gdy wiemy, jak prompt może być _budowany_, możemy zacząć myśleć o tym, jak go _projektować_, aby odzwierciedlał najlepsze praktyki. Możemy spojrzeć na to z dwóch perspektyw – posiadanie odpowiedniego _nastawienia_ i stosowanie właściwych _technik_.

### Nastawienie do inżynierii promptów

Inżynieria promptów to proces metodą prób i błędów, więc miej na uwadze trzy szerokie czynniki przewodnie:

1. **Znajomość domeny ma znaczenie.** Dokładność i trafność odpowiedzi zależy od _domeny_, w której działa aplikacja lub użytkownik. Zastosuj swoją intuicję i wiedzę dziedzinową, aby **dostosować techniki** jeszcze bardziej. Na przykład zdefiniuj _osobowości specyficzne dla domeny_ w promptach systemowych albo używaj _szablonów specyficznych dla domeny_ w promptach użytkownika. Dostarczaj treści wtórne odzwierciedlające kontekst specyficzny dla domeny lub korzystaj z _wskazówek i przykładów specyficznych dla domeny_, by skierować model ku znanym wzorcom użytkowania.

2. **Znajomość modelu ma znaczenie.** Wiemy, że modele mają charakter stochastyczny. Jednak implementacje modeli różnią się pod względem użytych zbiorów treningowych (wstępna wiedza), oferowanych możliwości (np. przez API lub SDK) i typu treści, do jakich są optymalizowane (np. kod vs obrazy vs tekst). Zrozum mocne i słabe strony używanego modelu i wykorzystaj tę wiedzę do _priorytetyzowania zadań_ lub budowy _dostosowanych szablonów_ zoptymalizowanych pod kątem możliwości modelu.

3. **Iteracja i walidacja mają znaczenie.** Modele szybko się rozwijają, podobnie jak techniki inżynierii promptów. Jako ekspert dziedzinowy możesz mieć dodatkowy kontekst lub kryteria dotyczące swojej specyficznej aplikacji, które niekoniecznie odnoszą się do szerszej społeczności. Użyj narzędzi i technik inżynierii promptów, aby „rozpocząć” konstrukcję promptu, a następnie iteruj i weryfikuj wyniki używając własnej intuicji i wiedzy dziedzinowej. Zapisuj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), która może służyć jako nowa baza odniesienia dla innych, aby przyspieszyć przyszłe iteracje.

## Najlepsze praktyki

Przyjrzyjmy się teraz powszechnym najlepszym praktykom rekomendowanym przez praktyków [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) oraz [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                               | Dlaczego                                                                                                                                                                                                                                          |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Oceń najnowsze modele.            | Nowe generacje modeli mają zwykle ulepszone funkcje i jakość – ale mogą też generować wyższe koszty. Oceń ich wpływ, a następnie podejmij decyzje o migracji.                                                                                     |
| Oddziel instrukcje i kontekst    | Sprawdź, czy Twój model/dostawca definiuje _separatory_, które wyróżniają instrukcje, treść główną i wtórną. Pomaga to modelom precyzyjniej przypisywać wagi tokenom.                                                                          |
| Bądź konkretny i jasny            | Podaj więcej szczegółów dotyczących pożądanego kontekstu, efektu, długości, formatu, stylu itp. Poprawi to zarówno jakość, jak i spójność odpowiedzi. Zapisuj przepisy w formie wielokrotnego użytku szablonów.                                   |
| Bądź opisowy, używaj przykładów  | Modele lepiej reagują na podejście typu „pokaż i opowiedz”. Zacznij od podejścia `zero-shot`, czyli instrukcji bez przykładów, a następnie wypróbuj `few-shot` jako udoskonalenie, podając kilka przykładów pożądanego wyniku. Korzystaj z analogii. |
| Używaj wskazówek do inicjacji   | Wskaż kierunek efektem kilku słów lub fraz, które model może użyć jako punkt startowy odpowiedzi.                                                                                                                                                |
| Powtarzaj, jeśli trzeba           | Czasem trzeba powtórzyć modelowi. Daj instrukcje przed i po treści głównej, użyj instrukcji i wskazówki itd. Iteruj i weryfikuj, co działa.                                                                                                    |
| Kolejność ma znaczenie            | Kolejność prezentacji informacji modelowi może wpływać na wynik ze względu na efekt świeżości. Wypróbuj różne opcje, aby znaleźć najlepszą.                                                                                                     |
| Daj modelowi „wyjście awaryjne”  | Zapewnij modelowi _domyślną_ odpowiedź, którą może podać, jeśli z jakiegoś powodu nie da rady wykonać zadania. Redukuje to ryzyko generowania fałszywych lub zmyślonych odpowiedzi.                                                             |
|                                  |                                                                                                                                                                                                                                                   |

Jak przy każdej najlepszej praktyce, pamiętaj, że _Twoje doświadczenia mogą się różnić_ w zależności od modelu, zadania i dziedziny. Używaj ich jako punktu wyjścia i iteruj, aby znaleźć to, co działa najlepiej dla Ciebie. Stale oceniaj proces inżynierii promptów, gdy pojawiają się nowe modele i narzędzia, ze szczególnym uwzględnieniem skalowalności i jakości odpowiedzi.

<!--
SZABLON LEKCJI:
Ten rozdział powinien zawierać wyzwanie kodowe, jeśli dotyczy.

WYZWANIE:
Link do Jupyter Notebooka z komentarzami w kodzie jako instrukcje (sekcje kodu puste).

ROZWIĄZANIE:
Link do kopii tego Notebooka z wypełnionymi promptami i uruchomieniem pokazującym jeden przykładowy wynik.
-->

## Zadanie

Gratulacje! Dotarłeś do końca lekcji! Teraz czas wykorzystać poznane koncepcje i techniki na prawdziwych przykładach!

Do zadania wykorzystamy Jupyter Notebook z ćwiczeniami, które można wykonywać interaktywnie. Możesz też rozszerzać Notebook o własne komórki Markdown i Kod, aby eksplorować pomysły i techniki samodzielnie.

### Aby zacząć, utwórz fork repozytorium, następnie

- (Zalecane) Uruchom GitHub Codespaces
- (Alternatywnie) Sklonuj repozytorium na swój lokalny sprzęt i używaj go z Docker Desktop
- (Alternatywnie) Otwórz Notebook w preferowanym środowisku uruchomieniowym.

### Następnie skonfiguruj zmienne środowiskowe

- Skopiuj plik `.env.copy` z katalogu głównego repo do `.env` i wypełnij wartości `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` oraz `AZURE_OPENAI_DEPLOYMENT`. Wróć do sekcji [Learning Sandbox](#środowisko-do-nauki), aby się dowiedzieć jak.

### Następnie otwórz Jupyter Notebook

- Wybierz kernel uruchomieniowy. Korzystając z opcji 1 lub 2, wystarczy wybrać domyślny kernel Python 3.10.x dostarczony przez kontener deweloperski.

Jesteś gotów do wykonania ćwiczeń. Pamiętaj, że nie ma tu odpowiedzi "dobrych" lub "złych" – chodzi o eksplorację możliwości metodą prób i błędów oraz budowanie intuicji, co działa dla danego modelu i domeny zastosowania.

_Z tego powodu w tej lekcji nie ma segmentów z rozwiązaniami kodu. Zamiast tego w Notebooku znajdziesz komórki Markdown zatytułowane "Moje rozwiązanie:", które pokazują przykładową odpowiedź jako odniesienie._

 <!--
SZABLON LEKCJI:
Podsumuj sekcję i podaj zasoby do samodzielnej nauki.
-->

## Sprawdzenie wiedzy

Który z poniższych promptów jest dobrym promptem, zgodnym z rozsądnymi najlepszymi praktykami?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90 zaparkowanego przy klifie o zachodzie słońca
3. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90

Odpowiedź: 2, to najlepszy prompt, ponieważ dostarcza szczegóły „co” i podaje konkretne informacje (nie tylko samochód, ale konkretną markę i model) oraz opisuje ogólne otoczenie. 3 jest kolejne najlepsze, bo też zawiera dużo opisu.

## 🚀 Wyzwanie

Spróbuj zastosować technikę „wskazówki” z promptem: Dokończ zdanie „Pokaż mi obraz czerwonego samochodu marki Volvo i „. Co odpowie oraz jak byś to poprawił?

## Świetna robota! Kontynuuj naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach inżynierii promptów? Przejdź do [strony dalszego kształcenia](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne doskonałe zasoby na ten temat.

Przejdź do Lekcji 5, gdzie przyjrzymy się [zaawansowanym technikom promptowania](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->