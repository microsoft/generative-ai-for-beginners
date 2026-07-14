# Podstawy Inżynierii Promptów

[![Podstawy Inżynierii Promptów](../../../translated_images/pl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Wprowadzenie
Ten moduł obejmuje podstawowe koncepcje i techniki tworzenia skutecznych promptów w generatywnych modelach AI. Sposób, w jaki napiszesz swój prompt do LLM, również ma znaczenie. Starannie opracowany prompt może przynieść lepszą jakość odpowiedzi. Ale co dokładnie oznaczają terminy takie jak _prompt_ i _inżynieria promptów_? I jak poprawić _wejście promptu_, które wysyłam do LLM? Na te pytania spróbujemy odpowiedzieć w tym rozdziale i następnym.

_Generatywna AI_ jest zdolna do tworzenia nowych treści (np. tekstu, obrazów, audio, kodu itd.) w odpowiedzi na żądania użytkownika. Osiąga to dzięki _Dużym Modelom Językowym_ (Large Language Models) takim jak seria GPT firmy OpenAI ("Generative Pre-trained Transformer"), które są trenowane do pracy z językiem naturalnym i kodem.

Użytkownicy mogą teraz wchodzić w interakcje z tymi modelami za pomocą znanych paradygmatów, takich jak czat, bez konieczności posiadania wiedzy technicznej czy szkolenia. Modele są _oparte na promptach_ – użytkownicy wysyłają tekstowe wejście (prompt) i otrzymują odpowiedź AI (completion). Następnie mogą „rozmawiać z AI” iteracyjnie, w wieloetapowych rozmowach, dopracowując prompt, aż odpowiedź spełni ich oczekiwania.

„Prompty” stają się teraz głównym _interfejsem programistycznym_ dla aplikacji generatywnej AI, mówiąc modelom, co mają robić i wpływając na jakość zwracanych odpowiedzi. „Inżynieria promptów” to szybko rozwijająca się dziedzina, która koncentruje się na _projektowaniu i optymalizacji_ promptów, aby dostarczać spójne i wysokiej jakości odpowiedzi na dużą skalę.

## Cele nauki

W tej lekcji nauczymy się, czym jest inżynieria promptów, dlaczego ma znaczenie i jak tworzyć bardziej skuteczne prompty dla danego modelu i celu aplikacji. Zrozumiemy podstawowe koncepcje i najlepsze praktyki w inżynierii promptów – oraz poznamy interaktywny „sandbox” w środowisku Jupyter Notebook, gdzie zobaczymy te koncepcje zastosowane w praktyce.

Pod koniec tej lekcji będziemy potrafili:

1. Wyjaśnić, czym jest inżynieria promptów i dlaczego jest ważna.
2. Opisać składniki promptu i jak są wykorzystywane.
3. Poznać najlepsze praktyki i techniki inżynierii promptów.
4. Zastosować poznane techniki na rzeczywistych przykładach, korzystając z punktu końcowego OpenAI.

## Kluczowe pojęcia

Inżynieria promptów: Praktyka projektowania i udoskonalania danych wejściowych, aby prowadzić modele AI do generowania pożądanych wyników.
Tokenizacja: Proces zamiany tekstu na mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetwarzać.
Instrukcyjnie dostrojone LLM: Duże modele językowe (LLM), które zostały wstępnie dostrojone na podstawie konkretnych instrukcji w celu poprawy dokładności i trafności odpowiedzi.

## Środowisko do nauki

Inżynieria promptów to obecnie bardziej sztuka niż nauka. Najlepszym sposobem na poprawę intuicji jest _praktyka_ i przyjęcie podejścia metodą prób i błędów, które łączy wiedzę specjalistyczną z zalecanymi technikami oraz optymalizacjami specyficznymi dla modelu.

Dołączony do tej lekcji Jupyter Notebook zapewnia środowisko _sandbox_, gdzie możesz wypróbować to, czego się uczysz – na bieżąco lub jako część wyzwania kodowego na końcu. Aby wykonać ćwiczenia, potrzebujesz:

1. **Klucz API Azure OpenAI** – punkt końcowy usługi dla wdrożonego LLM.
2. **Środowisko wykonawcze Pythona** – w którym Notebook może być uruchomiony.
3. **Lokalne zmienne środowiskowe** – _ukończ teraz kroki [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), aby się przygotować_.

Notebook zawiera _wstępne_ ćwiczenia – ale zachęcamy do dodawania własnych sekcji _Markdown_ (opis) i _Code_ (zapytania prompt) w celu wypróbowania więcej przykładów lub pomysłów – i zbudowania intuicji do projektowania promptów.

## Ilustrowany przewodnik

Chcesz najpierw zobaczyć ogólny obraz tego, co obejmuje ta lekcja? Sprawdź ten ilustrowany przewodnik, który daje poczucie głównych tematów i kluczowych wniosków, o których warto pomyśleć w każdej sekcji. Mapa lekcji prowadzi od zrozumienia kluczowych koncepcji i wyzwań po rozwiązanie ich za pomocą odpowiednich technik inżynierii promptów i najlepszych praktyk. Zwróć uwagę, że sekcja „Zaawansowane Techniki” w tym przewodniku odnosi się do treści zawartych w _następnym_ rozdziale tego programu.

![Ilustrowany przewodnik po inżynierii promptów](../../../translated_images/pl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nasz startup

Porozmawiajmy teraz, jak _ten temat_ wiąże się z misją naszego startupu, aby [wprowadzić innowacje AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje zasilane AI do _spersonalizowanego uczenia się_ – zastanówmy się, jak różni użytkownicy naszej aplikacji mogą „projektować” prompty:

- **Administratorzy** mogą poprosić AI o _analizę danych programów nauczania w celu zidentyfikowania luk w materiałach_. AI może podsumować wyniki lub zwizualizować je za pomocą kodu.
- **Edukatorzy** mogą poprosić AI o _wygenerowanie planu lekcji dla docelowej grupy i tematu_. AI może stworzyć spersonalizowany plan w określonym formacie.
- **Uczniowie** mogą poprosić AI o _prowadzenie ich w trudnym przedmiocie_. AI może teraz prowadzić uczniów poprzez lekcje, podpowiedzi i przykłady dostosowane do ich poziomu.

To tylko wierzchołek góry lodowej. Sprawdź [Prompty dla Edukacji](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – otwartoźródłową bibliotekę promptów stworzoną przez ekspertów edukacyjnych – aby lepiej poznać możliwości! _Spróbuj wykonać niektóre z tych promptów w sandboxie lub używając OpenAI Playground, aby zobaczyć, co się stanie!_

<!--
SZABLON LEKCJI:
Ten moduł powinien obejmować podstawową koncepcję nr 1.
Wzmocnij koncepcję przykładami i odniesieniami.

KONCEPCJA NR 1:
Inżynieria promptów.
Zdefiniuj i wyjaśnij, dlaczego jest potrzebna.
-->

## Czym jest inżynieria promptów?

Rozpoczęliśmy tę lekcję od zdefiniowania **Inżynierii promptów** jako procesu _projektowania i optymalizacji_ tekstowych danych wejściowych (promptów), aby dostarczać spójne i wysokiej jakości odpowiedzi (kompletacje) dla danego celu aplikacji i modelu. Możemy to rozumieć jako proces dwuetapowy:

- _projektowanie_ początkowego promptu dla konkretnego modelu i celu
- _udoskonalanie_ promptu iteracyjnie, aby poprawić jakość odpowiedzi

Jest to proces oparty na próbach i błędach, który wymaga intuicji i wysiłku użytkownika, aby osiągnąć optymalne wyniki. Dlaczego jest to ważne? Aby odpowiedzieć na to pytanie, najpierw musimy zrozumieć trzy koncepcje:

- _Tokenizacja_ = jak model „widzi” prompt
- _Podstawowe LLM_ = jak model bazowy „przetwarza” prompt
- _Instrukcyjnie dostrojone LLM_ = jak model teraz widzi „zadania”

### Tokenizacja

LLM postrzega prompty jako _sekwencję tokenów_, gdzie różne modele (lub wersje modelu) mogą tokenizować ten sam prompt na różne sposoby. Ponieważ LLM są trenowane na tokenach (a nie na surowym tekście), sposób tokenizacji promptów ma bezpośredni wpływ na jakość generowanej odpowiedzi.

Aby lepiej zrozumieć, jak działa tokenizacja, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) pokazane poniżej. Wklej swój prompt – i zobacz, jak zostaje on przekształcony w tokeny, zwracając uwagę na sposób traktowania znaków białych i znaków interpunkcyjnych. Zauważ, że przykład pokazuje starszy model LLM (GPT-3) – więc wypróbowanie tego z nowszym modelem może dać inny wynik.

![Tokenizacja](../../../translated_images/pl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncepcja: Modele Bazowe

Po tokenizacji promptu główną funkcją ["Podstawowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (lub modelu bazowego) jest przewidywanie kolejnego tokenu w tej sekwencji. Ponieważ LLM są trenowane na ogromnych zbiorach tekstów, mają dobre rozeznanie w statystycznych zależnościach między tokenami i mogą przewidzieć kolejny token z pewnym prawdopodobieństwem. Należy zauważyć, że nie rozumieją _znaczenia_ słów w promptach czy tokenach; widzą jedynie wzory, które mogą „uzupełnić” kolejnym przewidywaniem. Mogą kontynuować przewidywanie sekwencji, aż użytkownik przerwie proces lub zostanie spełniony jakiś wcześniej ustalony warunek.

Chcesz zobaczyć, jak działa uzupełnianie oparte na promptach? Wpisz powyższy prompt do [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) z ustawieniami domyślnymi. System jest skonfigurowany tak, aby traktować prompty jako zapytania o informacje – więc powinieneś zobaczyć uzupełnienie odpowiadające temu kontekstowi.

Ale co jeśli użytkownik chciałby zobaczyć coś konkretnego, co spełnia pewne kryteria lub cel zadania? W tym miejscu pojawiają się _instrukcyjnie dostrojone_ LLM.

![Uzupełnienie czatu w podstawowym LLM](../../../translated_images/pl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncepcja: Instrukcyjnie dostrojone LLM

[Instrukcyjnie dostrojony LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zaczyna od modelu bazowego i dostraja go za pomocą przykładów lub par wejście/wyjście (np. wieloetapowe „wiadomości”), które mogą zawierać jasne instrukcje – a odpowiedź AI stara się podążać za tymi instrukcjami.

Wykorzystuje techniki takie jak Uczenie ze Wzmocnieniem z Informacją Zwrotną od Człowieka (RLHF), które uczą model „podążać za instrukcjami” i „uczyć się z informacji zwrotnej”, dzięki czemu generuje lepiej dopasowane odpowiedzi do praktycznych zastosowań i bardziej odpowiednie dla celów użytkownika.

Wypróbuj to – wróć do powyższego promptu, ale zmień _wiadomość systemową_, aby dostarczyć następującą instrukcję jako kontekst:

> _Podsumuj treść, którą otrzymujesz, dla ucznia drugiej klasy. Ogranicz wynik do jednego akapitu z 3–5 punktami._

Zobacz, jak wynik został teraz dostrojony, aby odzwierciedlać pożądany cel i format? Edukator może teraz bezpośrednio użyć tej odpowiedzi na swoich slajdach na tę lekcję.

![Uzupełnienie czatu w instrukcyjnie dostrojonym LLM](../../../translated_images/pl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Dlaczego potrzebujemy inżynierii promptów?

Teraz, gdy wiemy, jak prompty są przetwarzane przez LLM, porozmawiajmy o tym, _dlaczego_ potrzebujemy inżynierii promptów. Odpowiedź leży w tym, że obecne modele LLM mają wiele wyzwań, które utrudniają uzyskanie _wiarygodnych i spójnych tekstów uzupełniających_ bez poświęcenia wysiłku na konstrukcję i optymalizację promptów. Na przykład:

1. **Odpowiedzi modelu są stochastyczne.** _Ten sam prompt_ może generować różne odpowiedzi w zależności od modelu lub wersji modelu. Nawet w tym samym modelu wyniki mogą się różnić w różnych momentach czasu. _Techniki inżynierii promptów pomagają nam minimalizować te różnice, zapewniając lepsze zabezpieczenia_.

1. **Modele mogą wymyślać odpowiedzi.** Modele są wstępnie trenowane na _ogromnych, ale ostatecznych_ zbiorach danych, co oznacza, że nie mają wiedzy o pojęciach spoza zakresu treningu. W rezultacie mogą generować odpowiedzi niedokładne, wymyślone lub sprzeczne z znanymi faktami. _Techniki inżynierii promptów pomagają użytkownikom identyfikować i ograniczać takie wymysły np. poprzez proszenie AI o cytaty lub uzasadnienia_.

1. **Możliwości modeli będą się różnić.** Nowsze modele lub generacje modeli mają bogatsze możliwości, ale także unikalne cechy i kompromisy w kosztach oraz złożoności. _Inżynieria promptów pomaga opracować najlepsze praktyki i procesy, które abstrahują różnice i dostosowują się do wymagań specyficznych modeli w sposób skalowalny i płynny_.

Zobaczmy to w działaniu w OpenAI lub Azure OpenAI Playground:

- Użyj tego samego promptu z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) – czy zauważyłeś różnice?
- Użyj tego samego promptu wielokrotnie z _tym samym_ wdrożeniem LLM (np. Azure OpenAI playground) – jak różniły się te wyniki?

### Przykład wymyśleń (fabrications)

W tym kursie używamy terminu **„wymyślenie” (fabrication)** w odniesieniu do zjawiska, kiedy LLM czasem generują nieprawdziwe informacje z powodu ograniczeń w treningu lub innych uwarunkowań. Możliwe, że słyszałeś to określane jako _„halucynacje”_ w popularnych artykułach lub publikacjach naukowych. Jednak zdecydowanie zalecamy używanie terminu _„wymyślenie”_, aby nie antropomorfizować zachowania, przypisując cechę ludzką maszynowemu wynikowi. Wspiera to także [wytyczne dotyczące odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) od strony terminologii, usuwając słowa, które mogą być uważane za obraźliwe lub nieinkluztywne w pewnych kontekstach.

Chcesz zrozumieć, jak działają wymyślenia? Pomyśl o promptcie, który nakazuje AI wygenerować treść na nieistniejący temat (aby upewnić się, że nie występuje w zbiorze treningowym). Na przykład – wypróbowałem taki prompt:

> **Prompt:** wygeneruj plan lekcji o Marsjańskiej wojnie roku 2076.

Wyszukiwanie w sieci pokazało, że istnieją fikcyjne relacje (np. seriale lub książki) o wojnach marsjańskich – ale żadnej o roku 2076. Zdrowy rozsądek mówi też, że rok 2076 to _przyszłość_ i nie może być przypisany do rzeczywistego wydarzenia.


Co się dzieje, gdy uruchomimy to zapytanie z różnymi dostawcami LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpowiedź 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Zgodnie z oczekiwaniami każdy model (lub jego wersja) generuje nieco inne odpowiedzi dzięki zachowaniom losowym i różnicom w możliwościach modeli. Na przykład jeden model jest skierowany do odbiorców na poziomie 8 klasy, a inny zakłada ucznia szkoły średniej. Jednak wszystkie trzy modele wygenerowały odpowiedzi, które mogłyby przekonać niezaznajomionego użytkownika, że wydarzenie było prawdziwe.

Techniki inżynierii promptów, takie jak _metaprompting_ i _konfiguracja temperatury_, mogą w pewnym stopniu zmniejszać ilość zmyśleń modele. Nowe _architektury_ inżynierii promptów również bezproblemowo integrują nowe narzędzia i techniki w przepływie promptu, aby łagodzić lub redukować niektóre z tych efektów.

## Studium przypadku: GitHub Copilot

Podsumujmy tę sekcję, żeby zrozumieć, jak inżynieria promptów jest wykorzystywana w rzeczywistych rozwiązaniach, patrząc na jedno Studium przypadku: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot to twój „AI Pair Programmer” – przekształca tekstowe prompta w uzupełnienia kodu i jest zintegrowany ze środowiskiem programistycznym (np. Visual Studio Code) dla płynnego doświadczenia użytkownika. Jak udokumentowano w serii poniższych blogów, najwcześniejsza wersja opierała się na modelu OpenAI Codex – inżynierowie szybko zdali sobie sprawę z potrzeby dostrojenia modelu i opracowania lepszych technik inżynierii promptów, aby poprawić jakość kodu. W lipcu zaprezentowano [ulepszony model AI, który wychodzi poza Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), oferujący jeszcze szybsze sugestie.

Przeczytaj wpisy po kolei, aby podążać za ich procesem uczenia się.

- **Maj 2023** | [GitHub Copilot coraz lepiej rozumie twój kod](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [W środku GitHub: Praca z LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Czerwiec 2023** | [Jak pisać lepsze prompty dla GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Lipiec 2023** | [.. GitHub Copilot wychodzi poza Codex z ulepszonym modelem AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Lipiec 2023** | [Przewodnik programisty po inżynierii promptów i LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Wrzesień 2023** | [Jak zbudować aplikację LLM dla przedsiębiorstw: Lekcje z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Możesz także przeglądać ich [blog inżynierski](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) po więcej wpisów takich jak [ten](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), który pokazuje, jak te modele i techniki są _stosowane_ do napędzania aplikacji w rzeczywistym świecie.

---

<!--
SZABLON LEKCJI:
Ta jednostka powinna obejmować podstawową koncepcję nr 2.
Wzmocnij koncepcję poprzez przykłady i odniesienia.

KONCEPCJA NR 2:
Projektowanie Promptów.
Ilustrowane przykładami.
-->

## Budowa Promptu

Widzieliśmy, dlaczego inżynieria promptów jest ważna – teraz zrozummy, jak prompt jest _budowany_, abyśmy mogli ocenić różne techniki bardziej efektywnego projektowania promptów.

### Podstawowy Prompt

Zacznijmy od podstawowego promptu: tekstowego wejścia wysłanego do modelu bez żadnego innego kontekstu. Oto przykład – gdy wysyłamy pierwsze kilka słów amerykańskiego hymnu narodowego do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), natychmiast _uzupełnia_ odpowiedź kolejnymi kilkoma wersami, ilustrując podstawowe zachowanie predykcyjne.

| Prompt (Wejście)   | Uzupełnienie (Wyjście)                                                                                                                     |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Wygląda na to, że zaczynasz śpiewać "The Star-Spangled Banner", hymn narodowy Stanów Zjednoczonych. Pełny tekst to ...                    |

### Złożony Prompt

Teraz dodajmy kontekst i instrukcje do tego podstawowego promptu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) pozwala nam zbudować złożony prompt jako zbiór _wiadomości_ z:

- Par input/output odzwierciedlających wejście _użytkownika_ oraz odpowiedź _asystenta_.
- Wiadomości systemowej ustalającej kontekst zachowania lub osobowości asystenta.

Zapytanie ma teraz poniższą formę, gdzie _tokenizacja_ skutecznie wyłapuje istotne informacje z kontekstu i rozmowy. Zmiana kontekstu systemowego może mieć tak samo duży wpływ na jakość uzupełnień, jak dane wejściowe użytkownika.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukcyjny Prompt

W powyższych przykładach prompt użytkownika był prostym zapytaniem tekstowym, które można interpretować jako prośbę o informacje. Przy promptach _instrukcyjnych_ możemy użyć tego tekstu, aby określić zadanie szczegółowiej, dostarczając lepsze wskazówki AI. Oto przykład:

| Prompt (Wejście)                                                                                                                                                                                                                         | Uzupełnienie (Wyjście)                                                                                                       | Typ Instrukcji      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napisz opis wojny secesyjnej                                                                                                                                                                                                             | _zwrócono prosty akapit_                                                                                                      | Prosta              |
| Napisz opis wojny secesyjnej. Podaj kluczowe daty i wydarzenia oraz opisz ich znaczenie                                                                                                                                                   | _zwrócono akapit, a potem listę kluczowych dat wydarzeń z opisami_                                                           | Złożona             |
| Napisz opis wojny secesyjnej w 1 akapicie. Podaj 3 punkty kluczowych dat i ich znaczenia. Podaj 3 dodatkowe punkty dotyczące ważnych postaci historycznych i ich wkładu. Zwróć wynik jako plik JSON                                  | _zwraca bardziej obszerne szczegóły w polu tekstowym, sformatowane jako JSON, które można skopiować do pliku i w razie potrzeby zweryfikować_ | Złożony. Formatowany. |

## Główny Zawartość

W powyższych przykładach prompt był nadal dość otwarty, pozwalając LLM zdecydować, która część pretrenowanego zestawu danych ma znaczenie. W wzorcu projektowym _głównej zawartości_, tekst wejściowy jest dzielony na dwie części:

- instrukcję (akcję)
- odpowiednią treść (która wpływa na akcję)

Oto przykład, w którym instrukcją jest „podsumuj to w 2 zdaniach”.

| Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Uzupełnienie (Wyjście)                                                                                                                                                                                                                                                                           |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwukrotnie i pół większą niż suma mas wszystkich pozostałych planet Układu Słonecznego. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie, znanym starożytnym cywilizacjom od czasów przedhistorycznych. Nazwany został na cześć rzymskiego boga Jowisza.[19] Patrząc z Ziemi, Jowisz może być na tyle jasny, że jego odbite światło rzuca widoczne cienie,[20] i jest średnio trzecim najjaśniejszym naturalnym obiektem na nocnym niebie po Księżycu i Wenus. <br/> **Podsumuj to w 2 krótkich zdaniach** | Jowisz, piąta planeta od Słońca, jest największą w Układzie Słonecznym i znany jest jako jeden z najjaśniejszych obiektów na nocnym niebie. Nazwany na cześć rzymskiego boga Jowisza, jest gazowym olbrzymem, którego masa jest dwukrotnie i pół większa niż suma mas wszystkich innych planet w Układzie Słonecznym. |

Segment głównej zawartości można wykorzystać na różne sposoby, by prowadzić skuteczniejsze instrukcje:

- **Przykłady** – zamiast mówić modelowi co ma zrobić za pomocą wyraźnej instrukcji, podaj mu przykłady co ma zrobić i pozwól mu wywnioskować wzór.
- **Podpowiedzi** – po instrukcji podaj „podpowiedź”, która inicjuje uzupełnienie, prowadząc model do bardziej trafnych odpowiedzi.
- **Szablony** – to powtarzalne „przepisy” na prompty z placeholderami (zmiennymi), które można dostosować danymi do konkretnych zastosowań.

Sprawdźmy to w praktyce.

### Używanie Przykładów

To podejście, w którym korzystając z głównej zawartości „karmimy model” przykładami pożądanego wyniku dla danej instrukcji i pozwalamy mu wywnioskować wzór pożądanego wyniku. W zależności od liczby podanych przykładów mamy zero-shot prompting, one-shot prompting, few-shot prompting itd.

Prompt składa się teraz z trzech składników:

- Opis zadania
- Kilka przykładów pożądanego wyjścia
- Początek nowego przykładu (który staje się niejawnie opisem zadania)

| Typ uczenia   | Prompt (Wejście)                                                                                                                                        | Uzupełnienie (Wyjście)     |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | „The Sun is Shining”. Przetłumacz na hiszpański                                                                                                       | „El Sol está brillando”.    |
| One-shot      | „The Sun is Shining” => „El Sol está brillando”. <br> „It's a Cold and Windy Day” =>                                                                   | „Es un día frío y ventoso”. |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk =>   | Basketball                  |
|               |                                                                                                                                                       |                             |

Zauważ, że w zero-shot prompting musieliśmy podać wyraźną instrukcję („Przetłumacz na hiszpański”), ale w two-shot promptingu jest ona domyślna. Przykład few-shot pokazuje, jak dodanie większej liczby przykładów pozwala modelom wyciągać trafniejsze wnioski bez dodatkowych instrukcji.

### Podpowiedzi w Prompcie

Inną techniką wykorzystania głównej zawartości jest podawanie _podpowiedzi_ zamiast przykładów. W tym przypadku dajemy modelowi „nakierowanie” w odpowiednim kierunku, _startując go_ fragmentem odzwierciedlającym pożądany format odpowiedzi. Model „bierze podpowiedź” i kontynuuje w tym stylu.

| Liczba Podpowiedzi | Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                           | Uzupełnienie (Wyjście)                                                                                                                                                                                                                                                                                    |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                  | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwukrotnie i pół większą niż suma mas wszystkich pozostałych planet Układu Słonecznego. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie, znanym starożytnym cywilizacjom od czasów przedhistorycznych. <br/>**Podsumuj to**                                       | Jowisz jest największą planetą w naszym Układzie Słonecznym i piątą od Słońca. Jest gazowym olbrzymem o masie 1/1000 masy Słońca, ale cięższym niż wszystkie inne planety razem wzięte. Starożytne cywilizacje znały Jowisza od dawna, a planeta jest łatwo widoczna na nocnym niebie. |
| 1                  | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwukrotnie i pół większą niż suma mas wszystkich pozostałych planet Układu Słonecznego. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie, znanym starożytnym cywilizacjom od czasów przedhistorycznych. <br/>**Podsumuj to** <br/> Co się dowiedzieliśmy, to że Jowisz | jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwukrotnie i pół większą niż suma mas wszystkich innych planet razem wziętych. Jest łatwo widoczny gołym okiem i znany od czasów starożytnych.                      |

| 2              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy olbrzym o masie jednej tysięcznej masy Słońca, ale dwukrotnie i pół większej niż masa wszystkich pozostałych planet Układu Słonecznego razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom na długo przed zapisem historii. <br/>**Podsumowanie** <br/> Top 3 Fakty, które się dowiedzieliśmy:         | 1. Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. <br/> 2. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca...<br/> 3. Jowisz był widoczny gołym okiem od czasów starożytnych ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Szablony promptów

Szablon promptu to _wcześniej zdefiniowany przepis na prompt_, który można przechowywać i używać ponownie w razie potrzeby, aby zapewnić bardziej spójne doświadczenia użytkownika na dużą skalę. W najprostszej formie jest to po prostu zbiór przykładów promptów, takich jak [ten od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), który dostarcza zarówno elementy interaktywnego promptu (wiadomości użytkownika i systemu), jak i format żądania API - do wsparcia ponownego użycia.

W bardziej złożonej formie, jak [ten przykład od LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), zawiera _miejsca na dane_ (placeholders), które można zastąpić danymi z różnych źródeł (wejście użytkownika, kontekst systemu, zewnętrzne źródła danych itd.), aby wygenerować prompt dynamicznie. Pozwala to na stworzenie biblioteki wielokrotnego użytku promptów, które mogą służyć do programowego tworzenia spójnych doświadczeń użytkownika na dużą skalę.

Ostatecznie prawdziwa wartość szablonów tkwi w możliwości tworzenia i publikowania _bibliotek promptów_ dla konkretnych domen aplikacji – gdzie szablon promptu jest teraz _optymalizowany_, aby odzwierciedlać kontekst specyficzny dla aplikacji lub przykłady czyniące odpowiedzi bardziej trafnymi i dokładnymi dla docelowej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest świetnym przykładem takiego podejścia, gromadząc bibliotekę promptów z naciskiem na kluczowe cele, takie jak planowanie lekcji, projektowanie programów nauczania, korepetycje itp.

## Wspierające treści

Jeśli pomyślimy o tworzeniu promptu jako o posiadaniu instrukcji (zadania) oraz celu (głównej treści), to _treść wtórna_ jest jak dodatkowy kontekst, który dostarczamy, aby **w jakiś sposób wpłynąć na wynik**. Może to być dopasowanie parametrów, instrukcje formatowania, taksonomie tematów itd., które pomagają modelowi _dostosować_ odpowiedź, aby spełniała oczekiwane cele lub wymagania użytkownika.

Na przykład: Mając katalog kursów z rozbudowanymi metadanymi (nazwa, opis, poziom, tagi metadanych, instruktor itp.) wszystkich dostępnych kursów w programie nauczania:

- możemy zdefiniować instrukcję, aby "streścić katalog kursów na jesień 2023"
- możemy użyć głównej treści, aby dostarczyć kilka przykładów oczekiwanego wyniku
- możemy użyć treści wtórnej do wskazania pięciu najważniejszych „tagów” zainteresowania.

Teraz model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów - ale jeśli wynik zawiera wiele tagów, może priorytetyzować 5 tagów wskazanych w treści wtórnej.

---

<!--
SZABLON LEKCJI:
Ta jednostka powinna obejmować kluczową koncepcję #1.
Wzmacniaj koncepcję przykładami i odniesieniami.

KONCEPCJA #3:
Techniki inżynierii promptów.
Jakie są podstawowe techniki inżynierii promptów?
Zilustruj to kilkoma ćwiczeniami.
-->

## Najlepsze praktyki w tworzeniu promptów

Skoro już wiemy, jak można _konstrukować_ prompty, możemy zacząć myśleć o tym, jak je _projektować_, aby odzwierciedlały najlepsze praktyki. Możemy rozważyć to w dwóch częściach – mieć właściwy _stan umysłu_ oraz zastosować odpowiednie _techniki_.

### Stan umysłu inżynierii promptów

Inżynieria promptów to proces metodą prób i błędów, więc miej na uwadze trzy szerokie czynniki przewodnie:

1. **Znajomość domeny ma znaczenie.** Dokładność i trafność odpowiedzi zależy od _domeny_, w której działa dana aplikacja lub użytkownik. Stosuj swoją intuicję i wiedzę specjalistyczną, by **dalsze dostosowywać techniki**. Na przykład, definiuj _osobowości domenowe_ w promptach systemowych lub używaj _specyficznych dla domeny szablonów_ w promptach użytkownika. Dostarczaj treść wtórną, która odzwierciedla kontekst specyficzny dla domeny, lub używaj _wskazówek i przykładów domenowych_, by nakierować model na znane wzorce użycia.

2. **Znajomość modelu ma znaczenie.** Wiemy, że modele są z natury stochastyczne. Jednak implementacje modeli mogą różnić się pod kątem używanego zbioru treningowego (wiedza wstępnie wytrenowana), możliwości (np. przez API lub SDK) oraz typu zawartości, na którą są zoptymalizowane (np. kod vs obrazy vs tekst). Zrozum mocne i słabe strony używanego modelu i używaj tej wiedzy, by _priorytetyzować zadania_ lub budować _dostosowane szablony_ zoptymalizowane pod możliwości modelu.

3. **Iteracja i weryfikacja mają znaczenie.** Modele szybko się rozwijają, podobnie jak techniki inżynierii promptów. Jako ekspert dziedzinowy możesz mieć inne konteksty lub kryteria dotyczące _Twojej_ specyficznej aplikacji, które mogą nie obowiązywać szerszą społeczność. Używaj narzędzi i technik inżynierii promptów, aby „przyspieszyć” konstrukt promptów, potem wprowadzaj iteracje i weryfikuj wyniki korzystając z własnej intuicji i wiedzy specjalistycznej. Zapisuj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), którą inni mogą wykorzystać jako nową bazę wyjściową, aby przyspieszyć przyszłe iteracje.

## Najlepsze praktyki

Przyjrzyjmy się teraz powszechnie polecanym najlepszym praktykom przez praktyków [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                               | Dlaczego                                                                                                                                                                                                                                            |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ocenić najnowsze modele.          | Nowe generacje modeli prawdopodobnie mają lepsze funkcje i jakość – ale mogą także wiązać się z wyższymi kosztami. Oceń ich wpływ, a następnie podejmij decyzję o migracji.                                                                          |
| Oddziel instrukcje od kontekstu   | Sprawdź, czy Twój model/dostawca definiuje _separatorzy_, aby wyraźniej rozróżnić instrukcje, główną i wtórną treść. To pomaga modelom dokładniej przypisywać wagi do tokenów.                                                                    |
| Bądź konkretny i jasny             | Podaj więcej szczegółów dotyczących oczekiwanego kontekstu, efektu, długości, formatu, stylu itp. To poprawi jakość i spójność odpowiedzi. Zapisuj przepisy w wielokrotnie używanych szablonach.                                                     |
| Bądź opisowy, używaj przykładów    | Modele mogą lepiej odpowiadać na podejście „pokaż i opowiedz”. Zacznij od podejścia `zero-shot`, gdzie dajesz instrukcję (ale bez przykładów), następnie spróbuj `few-shot` dla dopracowania, podając kilka przykładów oczekiwanego wyniku. Używaj analogii. |
| Używaj wskazówek do rozpoczęcia odpowiedzi | Nakieruj model na oczekiwany rezultat, podając początkowe słowa lub zwroty, które może użyć jako punkt startowy odpowiedzi.                                                                                                                         |
| Powtórz, jeśli potrzeba             | Czasem trzeba powtórzyć się modelowi. Daj instrukcje przed i po głównej treści, użyj instrukcji i wskazówki itd. Iteruj i weryfikuj, co działa najlepiej.                                                                                              |
| Kolejność ma znaczenie             | Kolejność, w jakiej przedstawiasz informacje modelowi, może wpływać na efekt, nawet w przykładach uczących, ze względu na efekt świeżości. Wypróbuj różne opcje, aby zobaczyć, co działa najlepiej.                                                   |
| Daj modelowi „wyjście awaryjne”    | Zapewnij modelowi _alternatywną_ odpowiedź, którą może udzielić, jeśli z jakiegokolwiek powodu nie może wykonać zadania. To może zmniejszyć prawdopodobieństwo generowania fałszywych lub sfabrykowanych odpowiedzi.                               |
|                                   |                                                                                                                                                                                                                                                    |

Jak z każdą najlepszą praktyką, pamiętaj, że _Twoje doświadczenia mogą się różnić_ w zależności od modelu, zadania i domeny. Używaj ich jako punktu wyjścia i wprowadzaj iteracje, by znaleźć to, co działa najlepiej dla Ciebie. Stale oceniaj swój proces tworzenia promptów w miarę pojawiania się nowych modeli i narzędzi, koncentrując się na skalowalności procesu i jakości odpowiedzi.

<!--
SZABLON LEKCJI:
Ta jednostka powinna zawierać wyzwanie programistyczne, jeśli ma zastosowanie

WYZWANIE:
Link do Jupyter Notebooka z instrukcjami zawierającymi tylko komentarze w kodzie (sekcje kodu są puste).

ROZWIĄZANIE:
Link do kopii tego Notebooka z wypełnionymi promptami i wykonaną sesją, pokazujący przykład odpowiedzi.
-->

## Zadanie

Gratulacje! Dotarłeś do końca lekcji! Czas przetestować niektóre z tych koncepcji i technik na prawdziwych przykładach!

Do naszego zadania użyjemy Jupyter Notebooka z ćwiczeniami, które możesz wykonywać interaktywnie. Możesz także rozbudować Notebook o własne komórki Markdown i kodu, aby samodzielnie eksplorować pomysły i techniki.

### Aby zacząć, utwórz fork repozytorium, a następnie

- (Zalecane) Uruchom GitHub Codespaces
- (Alternatywnie) Sklonuj repozytorium na swój lokalny komputer i użyj go z Docker Desktop
- (Alternatywnie) Otwórz Notebook w preferowanym środowisku runtime Notebooka.

### Następnie skonfiguruj zmienne środowiskowe

- Skopiuj plik `.env.copy` z katalogu głównego repozytorium do `.env` i uzupełnij wartości `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` oraz `AZURE_OPENAI_DEPLOYMENT`. Powróć do sekcji [Learning Sandbox](#środowisko-do-nauki), aby dowiedzieć się jak.

### Następnie otwórz Jupyter Notebook

- Wybierz jądro do uruchomienia. Jeśli używasz opcji 1 lub 2, po prostu wybierz domyślne jądro Python 3.10.x dostarczone przez kontener deweloperski.

Jesteś gotowy, aby uruchomić ćwiczenia. Pamiętaj, że tutaj nie ma _poprawnych i błędnych_ odpowiedzi – chodzi o eksplorację metodą prób i błędów oraz budowanie intuicji, co działa dla danego modelu i domeny zastosowania.

_Z tego powodu w tej lekcji nie ma segmentów z rozwiązaniem kodu. Zamiast tego, w Notebooku będą komórki Markdown zatytułowane "Moje rozwiązanie:", które pokażą jeden przykład odpowiedzi dla odniesienia._

 <!--
SZABLON LEKCJI:
Podsumuj sekcję i dodaj zasoby do samodzielnej nauki.
-->

## Sprawdzenie wiedzy

Który z poniższych promptów jest dobrym przykładem stosującym rozsądne najlepsze praktyki?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90 zaparkowanego przy klifie o zachodzie słońca
3. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90

Odp: 2, to najlepszy prompt, ponieważ podaje szczegóły „co” i wchodzi w detale (nie dowolny samochód, lecz konkretna marka i model) oraz opisuje całe otoczenie. 3 jest kolejnym najlepszym, ponieważ również zawiera dużo opisu.

## 🚀 Wyzwanie

Sprawdź, czy możesz użyć techniki „wskazówki” z promptem: Uzupełnij zdanie „Pokaż mi obraz czerwonego samochodu marki Volvo i …”. Jak odpowiada model i jak byś to ulepszył?

## Świetna robota! Kontynuuj naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach inżynierii promptów? Przejdź do [strony kontynuacji nauki](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne świetne zasoby na ten temat.

Przejdź do Lekcji 5, gdzie przyjrzymy się [zaawansowanym technikom promptów](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->