# Podstawy Inżynierii Podpowiedzi

[![Podstawy Inżynierii Podpowiedzi](../../../translated_images/pl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Wprowadzenie
Ten moduł obejmuje podstawowe pojęcia i techniki tworzenia skutecznych podpowiedzi w modelach generatywnej sztucznej inteligencji. Sposób, w jaki napiszesz swoją podpowiedź do dużego modelu językowego (LLM), również ma znaczenie. Starannie opracowana podpowiedź może zapewnić lepszą jakość odpowiedzi. Ale co dokładnie oznaczają terminy takie jak _podpowiedź_ i _inżynieria podpowiedzi_? I jak poprawić podpowiedź _wejściową_, którą wysyłam do LLM? To pytania, na które spróbujemy odpowiedzieć w tym i następnym rozdziale.

_Generatywna sztuczna inteligencja_ potrafi tworzyć nową treść (np. tekst, obrazy, dźwięk, kod itp.) w odpowiedzi na zapytania użytkownika. Osiąga to dzięki _Dużym Modelom Językowym_ takim jak seria GPT firmy OpenAI („Generative Pre-trained Transformer”), które są trenowane do używania języka naturalnego i kodu.

Użytkownicy mogą teraz wchodzić w interakcję z tymi modelami za pomocą znanych paradygmatów, jak czat, bez potrzeby posiadania wiedzy technicznej czy szkolenia. Modele są _oparte na podpowiedziach_ – użytkownicy wysyłają tekst (podpowiedź) i otrzymują odpowiedź AI (dokończenie). Mogą następnie „rozmawiać z AI” iteracyjnie, w wieloetapowych konwersacjach, dopracowując podpowiedź, aż odpowiedź spełni ich oczekiwania.

„Podpowiedzi” stają się teraz głównym _interfejsem programowania_ dla aplikacji generatywnej AI, mówiąc modelom, co mają robić i wpływając na jakość otrzymywanych odpowiedzi. „Inżynieria podpowiedzi” to szybko rozwijająca się dziedzina zajmująca się _projektowaniem i optymalizacją_ podpowiedzi, by dostarczać spójne i wysokiej jakości odpowiedzi na dużą skalę.

## Cele Nauki

W tej lekcji dowiemy się, czym jest inżynieria podpowiedzi, dlaczego jest ważna i jak tworzyć skuteczniejsze podpowiedzi dla danego modelu i celu aplikacji. Poznamy podstawowe pojęcia i najlepsze praktyki inżynierii podpowiedzi – oraz zapoznamy się z interaktywnym środowiskiem Jupyter Notebook „piaskownicą”, gdzie możemy zobaczyć zastosowanie tych koncepcji na rzeczywistych przykładach.

Na koniec tej lekcji będziemy potrafili:

1. Wyjaśnić, czym jest inżynieria podpowiedzi i dlaczego ma znaczenie.
2. Opisać elementy podpowiedzi i sposób ich użycia.
3. Poznać najlepsze praktyki i techniki inżynierii podpowiedzi.
4. Zastosować poznane techniki na prawdziwych przykładach, używając punktu końcowego OpenAI.

## Kluczowe Terminy

Inżynieria Podpowiedzi: Praktyka projektowania i udoskonalania wejść, które kierują modele AI do generowania pożądanych wyników.
Tokenizacja: Proces zamiany tekstu na mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetworzyć.
Model z dostosowaniem instrukcji (Instruction-Tuned LLM): Duże modele językowe (LLM), które zostały dostrojone za pomocą konkretnych instrukcji, aby poprawić dokładność i trafność odpowiedzi.

## Piaskownica Nauki

Inżynieria podpowiedzi jest obecnie bardziej sztuką niż nauką. Najlepszym sposobem na poprawę intuicji w tym zakresie jest _praktyka_ i przyjęcie podejścia opartego na metodzie prób i błędów, łączącego wiedzę domenową z zalecanymi technikami i optymalizacjami specyficznymi dla modelu.

Dołączony do tej lekcji Jupyter Notebook stanowi środowisko _piaskownicy_, w którym możesz wypróbować to, czego się uczysz – podczas nauki lub jako część wyzwania kodowego na końcu. Aby wykonać ćwiczenia, potrzebujesz:

1. **Klucz API Azure OpenAI** – punkt końcowy usługi dla wdrożonego LLM.
2. **Środowisko wykonawcze Pythona** – w którym Notebook może być uruchomiony.
3. **Lokalne zmienne środowiskowe** – _ukończ teraz kroki [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst), aby być gotowym_.

Notebook zawiera _startowe_ ćwiczenia – ale zachęcamy do dodawania własnych sekcji _Markdown_ (opisu) i _Code_ (żądań podpowiedzi) - by wypróbować więcej przykładów lub pomysłów – i rozwijać intuicję projektowania podpowiedzi.

## Ilustrowany Przewodnik

Chcesz zrozumieć ogólny obraz tego, co obejmuje ta lekcja, zanim zagłębisz się w szczegóły? Sprawdź ten ilustrowany przewodnik, który daje wyobrażenie o głównych tematach i kluczowych wnioskach do rozważenia w każdym z nich. Mapa lekcji prowadzi od zrozumienia podstawowych pojęć i wyzwań do radzenia sobie z nimi przy pomocy odpowiednich technik inżynierii podpowiedzi i najlepszych praktyk. Uwaga, sekcja „Zaawansowane techniki” tego przewodnika odnosi się do treści omawianych w _następnym_ rozdziale tego programu nauczania.

![Ilustrowany przewodnik po inżynierii podpowiedzi](../../../translated_images/pl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nasz Startup

Teraz porozmawiajmy, jak _ten temat_ wiąże się z misją naszego startupu, by [wprowadzić innowacje AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje oparte na AI dla _spersonalizowanego uczenia się_ – więc pomyślmy, jak różni użytkownicy naszej aplikacji mogą „projektować” podpowiedzi:

- **Administratorzy** mogą poprosić AI o _analizę danych programów nauczania w celu zidentyfikowania luk w pokryciu_. AI może podsumować wyniki lub zobrazować je za pomocą kodu.
- **Nauczyciele** mogą poprosić AI o _wygenerowanie planu lekcji dla określonej grupy odbiorców i tematu_. AI może stworzyć spersonalizowany plan w określonym formacie.
- **Uczniowie** mogą poprosić AI o _prowadzenie ich w trudnym przedmiocie_. AI może teraz prowadzić uczniów lekcjami, podpowiedziami i przykładami dostosowanymi do ich poziomu.

To dopiero wierzchołek góry lodowej. Sprawdź [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – otwartą bibliotekę podpowiedzi kuratorowaną przez ekspertów edukacyjnych – by poznać szerszy zakres możliwości! _Spróbuj uruchomić niektóre z tych podpowiedzi w piaskownicy lub używając OpenAI Playground, aby zobaczyć, co się stanie!_

<!--
SZABLON LEKCJI:
Ten rozdział powinien objąć podstawową koncepcję nr 1.
Wzmocnij koncepcję przykładami i odniesieniami.

KONCEPCJA NR 1:
Inżynieria Podpowiedzi.
Zdefiniuj i wyjaśnij, dlaczego jest potrzebna.
-->

## Czym jest Inżynieria Podpowiedzi?

Lekcję rozpoczęliśmy od zdefiniowania **Inżynierii Podpowiedzi** jako procesu _projektowania i optymalizacji_ tekstowych wejść (podpowiedzi) w celu dostarczenia spójnych i wysokiej jakości odpowiedzi (dokończeń) dla określonego celu aplikacji i modelu. Możemy to rozumieć jako proces dwuetapowy:

- _projektowanie_ początkowej podpowiedzi dla konkretnego modelu i celu
- _doprecyzowanie_ podpowiedzi iteracyjnie, by poprawić jakość odpowiedzi

Jest to niezbędnie proces metodą prób i błędów, wymagający intuicji użytkownika i wysiłku, by uzyskać optymalne wyniki. Dlaczego więc jest to ważne? Aby odpowiedzieć na to pytanie, musimy najpierw zrozumieć trzy pojęcia:

- _Tokenizacja_ = jak model „widzi” podpowiedź
- _Podstawowe LLM_ = jak model bazowy „przetwarza” podpowiedź
- _Model z dostosowaniem instrukcji_ = jak model „widzi” teraz „zadania”

### Tokenizacja

Duży Model Językowy widzi podpowiedzi jako _ciąg tokenów_, gdzie różne modele (lub wersje modelu) mogą tokenizować tę samą podpowiedź na różne sposoby. Ponieważ LLM są trenowane na tokenach (a nie na surowym tekscie), sposób tokenizacji podpowiedzi bezpośrednio wpływa na jakość wygenerowanej odpowiedzi.

Aby intuicyjnie zrozumieć, jak działa tokenizacja, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) pokazane poniżej. Wklej swoją podpowiedź – zobacz, jak zostaje przekształcona na tokeny, zwracając uwagę na to, jak traktowane są znaki białe i interpunkcyjne. Zauważ, że ten przykład pokazuje starszy model LLM (GPT-3) – wypróbowanie tego na nowszym modelu może dać inny rezultat.

![Tokenizacja](../../../translated_images/pl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Koncepcja: Modele Bazowe

Po tokenizacji podpowiedzi, główną funkcją ["Podstawowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (lub modelu bazowego) jest przewidzenie tokena w tej sekwencji. Ponieważ LLM są trenowane na ogromnych zbiorach tekstów, dobrze rozumieją statystyczne relacje między tokenami i potrafią przewidzieć kolejny token z pewnym prawdopodobieństwem. Nie rozumieją jednak _znaczenia_ słów w podpowiedzi czy tokenie; widzą jedynie wzorzec, który mogą „dopowiedzieć” kolejnym przewidywaniem. Mogą kontynuować przewidywanie sekwencji aż do przerwania przez użytkownika lub spełnienia ustalonego warunku.

Chcesz zobaczyć, jak działa dokończenie oparte na podpowiedzi? Wpisz powyższą podpowiedź w [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ze standardowymi ustawieniami. System jest skonfigurowany, by traktować podpowiedzi jako prośby o informacje – więc powinieneś zobaczyć dokończenie spełniające ten kontekst.

A co jeśli użytkownik chciałby coś konkretnego, spełniającego pewne kryteria lub cel zadania? Tutaj pojawiają się modele _dostosowane instrukcjami_.

![Dokończenie czatu na podstawowym LLM](../../../translated_images/pl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Koncepcja: Modele Dostosowane Instrukcjami

[Model z dostosowaniem instrukcji](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zaczyna od modelu bazowego i dostraja go na podstawie przykładów lub par wejście/wyjście (np. wieloetapowych „wiadomości”), które mogą zawierać wyraźne instrukcje – a odpowiedź AI próbuje się dostosować do tych instrukcji.

Wykorzystuje to techniki takie jak Uczenie ze Wzmocnieniem z Opinią Ludzką (RLHF), które mogą trenować model, by _podążał za instrukcjami_ i _uczył się na podstawie opinii_, tak aby produkował odpowiedzi lepiej dopasowane do praktycznych zastosowań i bardziej adekwatne do celów użytkownika.

Wypróbujmy to – wróć do powyższej podpowiedzi, ale teraz zmień _wiadomość systemową_, by zawierała następującą instrukcję jako kontekst:

> _Podsumuj dostarczone treści dla ucznia drugiej klasy. Zachowaj efekt w jednym akapicie z 3-5 punktami._

Zobacz, jak wynik jest teraz dostrojony, by odzwierciedlać żądany cel i format? Nauczyciel może teraz bezpośrednio użyć tej odpowiedzi na swoich slajdach dla tej lekcji.

![Dokończenie czatu modelu dostosowanego instrukcjami](../../../translated_images/pl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Dlaczego potrzebujemy Inżynierii Podpowiedzi?

Teraz, gdy wiemy, jak podpowiedzi są przetwarzane przez LLM, porozmawiajmy o _dlaczego_ potrzebujemy inżynierii podpowiedzi. Odpowiedź leży w fakcie, że obecne LLM stawiają szereg wyzwań, które utrudniają _uzyskanie niezawodnych i spójnych odpowiedzi_ bez wysiłku w konstrukcję i optymalizację podpowiedzi. Na przykład:

1. **Odpowiedzi modelu są stochastyczne.** _Ta sama podpowiedź_ prawdopodobnie wygeneruje różne odpowiedzi w różnych modelach lub wersjach modeli. Mogą też pojawić się różnice w wynikach dla _tego samego modelu_ w różnych momentach. _Techniki inżynierii podpowiedzi pomagają minimalizować te różnice, oferując lepsze ramy bezpieczeństwa_.

1. **Modele mogą fabrykować odpowiedzi.** Modele są trenowane na _ogromnych, ale skończonych_ zestawach danych, co oznacza, że nie znają pojęć spoza tego zakresu treningowego. W rezultacie mogą generować odpowiedzi nieprecyzyjne, fikcyjne lub bezpośrednio sprzeczne z znanymi faktami. _Techniki inżynierii podpowiedzi pomagają użytkownikom identyfikować i łagodzić takie fabrykacje, np. prosząc AI o cytaty lub rozumowanie_.

1. **Możliwości modeli będą się różnić.** Nowsze modele lub generacje modeli mają bogatsze możliwości, ale także posiadają unikalne cechy i kompromisy kosztowe oraz złożoności. _Inżynieria podpowiedzi pomaga opracować najlepsze praktyki i workflow, które abstrakują różnice i dostosowują się do wymagań specyficznych dla modelu w skalowalny i bezproblemowy sposób_.

Zobaczmy to w praktyce w OpenAI lub Azure OpenAI Playground:

- Użyj tej samej podpowiedzi z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) – czy zauważyłeś różnice?
- Używaj tej samej podpowiedzi wielokrotnie z _tym samym_ wdrożeniem LLM (np. playground Azure OpenAI) – jak różniły się te odpowiedzi?

### Przykład Fabrykacji

W tym kursie używamy terminu **„fabrykacja”** do opisania zjawiska, gdy LLM czasami generują nieprawdziwe informacje z powodu ograniczeń treningu lub innych ograniczeń. Możliwe, że słyszałeś to określane jako _„halucynacje”_ w popularnych artykułach lub pracach naukowych. Jednak zdecydowanie zalecamy używanie terminu _„fabrykacja”_, by nie antropomorfizować przypadkiem tego zachowania przez przypisywanie maszynowemu wynikowi cech ludzkich. Wspiera to również [wytyczne dotyczące odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z perspektywy terminologii, usuwając terminy, które mogłyby być uważane za obraźliwe lub niedostosowane w niektórych kontekstach.

Chcesz zrozumieć, jak działa fabrykacja? Pomyśl o podpowiedzi instruującej AI, by wygenerowała treść na temat nieistniejący (żeby upewnić się, że nie występuje w zbiorze treningowym). Na przykład – wypróbowałem taką podpowiedź:

> **Podpowiedź:** wygeneruj plan lekcji dotyczący Wojny Marsjańskiej w 2076 roku.

Przeszukanie internetu pokazało mi, że istnieją fikcyjne opowieści (np. seriale telewizyjne lub książki) o wojnach marsjańskich – ale żadna nie dotyczy roku 2076. Zdrowy rozsądek również podpowiada, że 2076 to _przyszłość_ i nie może być związany z prawdziwym wydarzeniem.


Co się stanie, gdy uruchomimy ten prompt z różnymi dostawcami LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/pl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/pl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Odpowiedź 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/pl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Jak można się spodziewać, każdy model (lub wersja modelu) generuje nieco różne odpowiedzi dzięki stochastycznemu zachowaniu i różnicom w możliwościach modelu. Na przykład jeden model kieruje się do odbiorców na poziomie 8 klasy szkoły podstawowej, podczas gdy inny zakłada ucznia liceum. Jednak wszystkie trzy modele wygenerowały odpowiedzi, które mogłyby przekonać nieświadomego użytkownika, że zdarzenie było prawdziwe.

Techniki inżynierii promptów, takie jak _metaprompting_ i _konfiguracja temperatury_, mogą do pewnego stopnia ograniczyć wytwarzanie przez model fałszywych informacji. Nowe _architektury_ inżynierii promptów również bezproblemowo integrują nowe narzędzia i techniki w przepływ prompta, aby złagodzić lub zmniejszyć niektóre z tych efektów.

## Studium przypadku: GitHub Copilot

Podsumujmy tę sekcję, zapoznając się z tym, jak inżynieria promptów jest wykorzystywana w rzeczywistych rozwiązaniach, przyglądając się jednemu studium przypadku: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot to Twój "AI Pair Programmer" – przekształca tekstowe prompta w uzupełnienia kodu i jest zintegrowany z Twoim środowiskiem programistycznym (np. Visual Studio Code), zapewniając płynne doświadczenie użytkownika. Jak udokumentowano w serii poniższych wpisów na blogu, najwcześniejsza wersja opierała się na modelu OpenAI Codex – inżynierowie szybko zdali sobie sprawę z potrzeby dostrojenia modelu i opracowania lepszych technik inżynierii promptów, by poprawić jakość kodu. W lipcu [wprowadzono ulepszony model AI, który wykracza poza Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), oferując jeszcze szybsze sugestie.

Przeczytaj wpisy w kolejności, aby śledzić ich drogę uczenia się.

- **Maj 2023** | [GitHub Copilot staje się lepszy w rozumieniu Twojego kodu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Inside GitHub: Praca z LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Czerwiec 2023** | [Jak pisać lepsze prompta dla GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Lipiec 2023** | [.. GitHub Copilot wykracza poza Codex dzięki ulepszonemu modelowi AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Lipiec 2023** | [Przewodnik programisty po inżynierii promptów i LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Wrzesień 2023** | [Jak zbudować aplikację LLM dla przedsiębiorstw: lekcje z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Możesz również przeglądać ich [blog inżynierski](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) po więcej wpisów, takich jak [ten](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), który pokazuje, jak te modele i techniki są _stosowane_ do napędzania rzeczywistych aplikacji.

---

<!--
SZABLON LEKCJI:
Ten rozdział powinien omawiać podstawową koncepcję #2.
Wzmocnij koncepcję przykładami i odniesieniami.

KONCEPCJA #2:
Projektowanie prompta.
Ilustrowane przykładami.
-->

## Budowa prompta

Widzieliśmy, dlaczego inżynieria promptów jest ważna – teraz zrozummy, jak prompty są _konstruowane_, aby móc ocenić różne techniki projektowania bardziej efektywnych promptów.

### Podstawowy prompt

Zacznijmy od podstawowego prompta: wejściowego tekstu wysłanego do modelu bez żadnego innego kontekstu. Oto przykład – gdy wysyłamy pierwsze kilka słów amerykańskiego hymnu narodowego do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), natychmiast _uzupełnia_ odpowiedź kolejnymi liniami, ilustrując podstawowe zachowanie przewidywania.

| Prompt (wejście)    | Uzupełnienie (wyjście)                                                                                                                     |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Wygląda na to, że zaczynasz śpiewać słowa „The Star-Spangled Banner”, hymn narodowy Stanów Zjednoczonych. Pełny tekst to…                     |

### Złożony prompt

Teraz dodajmy kontekst i instrukcje do tego podstawowego prompta. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) pozwala konstruować złożony prompt jako zbiór _wiadomości_ z:

- Par wejście/wyjście odzwierciedlających dane _użytkownika_ oraz odpowiedzi _asystenta_.
- Wiadomość systemową ustalającą kontekst zachowania lub osobowości asystenta.

Żądanie jest teraz w poniższej formie, gdzie _tokenizacja_ skutecznie uchwytuje istotne informacje z kontekstu i rozmowy. Zmiana kontekstu systemowego może mieć równie duży wpływ na jakość uzupełnień, co dostarczone dane wejściowe użytkownika.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instrukcyjny prompt

W powyższych przykładach prompt użytkownika był prostym zapytaniem tekstowym, które można interpretować jako prośbę o informacje. W przypadku promptów _instrukcyjnych_ możemy użyć tego tekstu, aby bardziej szczegółowo określić zadanie, dostarczając AI lepszych wskazówek. Oto przykład:

| Prompt (wejście)                                                                                                                                                                                                                         | Uzupełnienie (wyjście)                                                                                                        | Typ instrukcji     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napisz opis Wojny Secesyjnej                                                                                                                                                                                                           | _zwrócił prosty akapit_                                                                                                      | Prosty             |
| Napisz opis Wojny Secesyjnej. Podaj kluczowe daty i wydarzenia oraz opisz ich znaczenie                                                                                                                                                  | _zwrócił akapit, po którym następuje lista kluczowych dat wydarzeń wraz z opisami_                                          | Złożony            |
| Napisz opis Wojny Secesyjnej w 1 akapicie. Podaj 3 punkty kluczowych dat i ich znaczenie. Podaj 3 kolejne punkty z kluczowymi postaciami historycznymi i ich wkładem. Zwróć wynik jako plik JSON                                            | _zwraca bardziej obszerne informacje w polu tekstowym, sformatowane jako JSON, który można skopiować i zapisać do pliku_    | Złożony. Sformatowany. |

## Zawartość główna

W powyższych przykładach prompt był nadal dość otwarty, pozwalając LLM zdecydować, jaka część jego wstępnie wytrenowanego zbioru danych jest istotna. W wzorcu projektowym _zawartość główna_ tekst wejściowy dzieli się na dwie części:

- instrukcję (działanie)
- istotną treść (która wpływa na działanie)

Oto przykład, gdzie instrukcją jest „podsumuj to w 2 zdaniach”.

| Prompt (wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Uzupełnienie (wyjście)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy gigant o masie jednej tysięcznej masy Słońca, ale dwukrotnie większej niż suma mas pozostałych planet Układu Słonecznego. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i jest znany starożytnym cywilizacjom od czasów przed zapisaniem historii. Nazwano go na cześć rzymskiego boga Jowisza.[19] Patrząc z Ziemi, Jowisz może być na tyle jasny, że jego światło odbite rzuca widoczne cienie,[20] i jest średnio trzecim najjaśniejszym naturalnym obiektem na niebie po Księżycu i Wenus. <br/> **Podsumuj to w 2 krótkich zdaniach** | Jowisz, piąta planeta od Słońca, jest największą w Układzie Słonecznym i znany jest jako jeden z najjaśniejszych obiektów na nocnym niebie. Nazwany na cześć rzymskiego boga Jowisza, to gazowy gigant, którego masa jest dwa i pół razy większa niż suma mas wszystkich pozostałych planet Układu Słonecznego. |

Segment zawartości głównej można wykorzystać na różne sposoby, aby generować skuteczniejsze instrukcje:

- **Przykłady** – zamiast mówić modelowi, co ma zrobić za pomocą wyraźnej instrukcji, daj mu przykłady tego, co zrobić, i pozwól mu wywnioskować schemat.
- **Sygnały** – podążaj za instrukcją „sygnałem”, który wstępnie przygotowuje uzupełnienie, kierując model do bardziej odpowiednich odpowiedzi.
- **Szablony** – to powtarzalne „przepisy” na prompty z miejscami na wypełnienie (zmiennymi), które można dostosować danymi do konkretnych przypadków użycia.

Zbadajmy te techniki w praktyce.

### Używanie przykładów

To podejście polega na korzystaniu z zawartości głównej, aby „nakarmić model” przykładami pożądanego wyjścia dla danej instrukcji i pozwolić mu wywnioskować schemat pożądanego wyniku. W zależności od liczby dostarczonych przykładów, możemy mieć zero-shot prompting, one-shot prompting, few-shot prompting itd.

Prompt teraz składa się z trzech elementów:

- Opisu zadania
- Kilku przykładów pożądanego wyjścia
- Początku nowego przykładu (który staje się niejawnie opisem zadania)

| Typ uczenia   | Prompt (wejście)                                                                                                                                              | Uzupełnienie (wyjście)     |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Przetłumacz na hiszpański                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => "El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                         | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk =>         | Basketball                  |
|               |                                                                                                                                                             |                             |

Zauważ, jak w zero-shot prompting musieliśmy podać wyraźną instrukcję („Przetłumacz na hiszpański”), ale została ona wywnioskowana w przykładzie one-shot. Przykład few-shot pokazuje, jak dodanie większej liczby przykładów pozwala modelom na dokładniejsze wnioskowanie bez dodatkowych instrukcji.

### Sygnały (Prompt Cues)

Inną techniką wykorzystania zawartości głównej jest dostarczanie _sygnałów_ zamiast przykładów. W tym przypadku dajemy modelowi impuls w odpowiednim kierunku, _rozpoczynając_ od fragmentu odzwierciedlającego pożądany format odpowiedzi. Model „łapie sygnał” i kontynuuje w tym stylu.

| Liczba sygnałów | Prompt (wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Uzupełnienie (wyjście)                                                                                                                                                                                                                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0               | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy gigant o masie jednej tysięcznej masy Słońca, ale dwukrotnie większej niż suma mas pozostałych planet Układu Słonecznego. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i jest znany starożytnym cywilizacjom od czasów przed zapisaniem historii. <br/>**Podsumuj to**                                       | Jowisz jest największą planetą w naszym Układzie Słonecznym i piątą od Słońca. To gazowy gigant o masie 1/1000 masy Słońca, ale cięższy niż wszystkie inne planety razem wzięte. Starożytne cywilizacje znały Jowisza od dawna i jest on łatwo widoczny na nocnym niebie. |
| 1               | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy gigant o masie jednej tysięcznej masy Słońca, ale dwukrotnie większej niż suma mas pozostałych planet Układu Słonecznego. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i jest znany starożytnym cywilizacjom od czasów przed zapisaniem historii. <br/>**Podsumuj to** <br/> Co się dowiedzieliśmy, to że Jowisz | jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy gigant o masie jednej tysięcznej masy Słońca, ale dwukrotnie większej niż suma mas pozostałych planet razem wziętych. Jest łatwo widoczny gołym okiem i znany od czasów starożytnych.                        |

| 2              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. To gazowy gigant o masie jednej tysięcznej masy Słońca, ale dwukrotnie i pół większej niż wszystkich innych planet Układu Słonecznego razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisaniem historii. <br/>**Podsumowanie** <br/> 3 najważniejsze fakty, które poznaliśmy:         | 1. Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. <br/> 2. To gazowy gigant o masie jednej tysięcznej masy Słońca...<br/> 3. Jowisz był widoczny gołym okiem już w starożytności ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Szablony promptów

Szablon promptu to _zdefiniowany wcześniej przepis na prompt_, który można przechowywać i wykorzystywać wielokrotnie według potrzeby, aby zapewnić bardziej spójne doświadczenia użytkownika na dużą skalę. W najprostszej formie jest to po prostu zbiór przykładów promptów, takich jak [ten od OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), który dostarcza zarówno interaktywne komponenty promptu (wiadomości użytkownika i systemu), jak i format zapytania sterowanego przez API — aby wspierać ponowne użycie.

W bardziej złożonej formie, jak [ten przykład z LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), zawiera _miejsce na dane_ (placeholders), które można zastąpić danymi z różnych źródeł (wprowadzanymi przez użytkownika, kontekstem systemu, zewnętrznymi źródłami danych itd.), aby dynamicznie generować prompt. Pozwala to stworzyć bibliotekę wielokrotnego użytku promptów, które mogą być wykorzystywane do programowego tworzenia spójnych doświadczeń użytkownika na dużą skalę.

Prawdziwa wartość szablonów polega wreszcie na możliwości tworzenia i publikowania _bibliotek promptów_ dla pionowych dziedzin zastosowań — gdzie szablon promptu jest _optymalizowany_, aby odzwierciedlać kontekst specyficzny dla aplikacji lub przykłady, które sprawiają, że odpowiedzi są bardziej istotne i precyzyjne dla docelowej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest doskonałym przykładem takiego podejścia — kuratoruje bibliotekę promptów dla edukacji, ze szczególnym naciskiem na kluczowe cele jak planowanie lekcji, projektowanie programu nauczania, tutoring uczniów itd.

## Treść wspierająca

Jeśli rozumiemy konstrukcję promptu jako posiadanie instrukcji (zadania) i celu (głównej treści), to _treść wtórna_ jest jak dodatkowy kontekst, który dostarczamy, aby **jakoś wpłynąć na wynik**. Mogą to być parametry strojenia, instrukcje formatowania, taksonomie tematów itd., które pomagają modelowi _dopasować_ odpowiedź do oczekiwanych celów lub wymagań użytkownika.

Na przykład: Mając katalog kursów z obszernymi metadanymi (nazwa, opis, poziom, tagi metadanych, prowadzący itp.) dla wszystkich dostępnych kursów w programie nauczania:

- możemy zdefiniować instrukcję, aby „podsumować katalog kursów na jesień 2023”
- możemy użyć głównej treści, aby podać kilka przykładów pożądanego wyniku
- możemy użyć treści wtórnej, aby wskazać 5 najważniejszych „tagów” zainteresowania

Teraz model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów — ale jeśli wynik ma wiele tagów, może priorytetowo traktować 5 tagów zdefiniowanych w treści wtórnej.

---

<!--
SZABLON LEKCJI:
Ta jednostka powinna omawiać podstawową koncepcję nr 1.
Wzmocnij tę koncepcję przykładami i odniesieniami.

KONCEPCJA NR 3:
Techniki inżynierii promptów.
Jakie są podstawowe techniki inżynierii promptów?
Zilustruj to ćwiczeniami.
-->

## Najlepsze praktyki w promptowaniu

Teraz, gdy wiemy, jak prompt może być _zbudowany_, możemy zacząć myśleć, jak go _zaprojektować_, aby odzwierciedlić najlepsze praktyki. Możemy to rozważać dwojako — posiadając odpowiednie _nastawienie_ i stosując odpowiednie _techniki_.

### Nastawienie w inżynierii promptów

Inżynieria promptów to proces metodą prób i błędów, więc miej na uwadze trzy szerokie czynniki przewodnie:

1. **Znajomość dziedziny ma znaczenie.** Dokładność i trafność odpowiedzi zależy od _dziedziny_, w której działa dana aplikacja lub użytkownik. Stosuj intuicję i wiedzę specjalistyczną, aby jeszcze bardziej **dostosowywać techniki**. Na przykład, definiuj _osobowości charakterystyczne dla danej dziedziny_ w promptach systemowych lub używaj _szablonów specyficznych dla domeny_ w promptach użytkownika. Dostarczaj treści wtórnej, która odzwierciedla kontekst specyficzny dla dziedziny, albo używaj _wskazówek i przykładów charakterystycznych dla danej dziedziny_, aby kierować model w stronę znajomych wzorców użycia.

2. **Znajomość modelu ma znaczenie.** Wiemy, że modele mają naturę stochastyczną. Ale implementacje modeli mogą się też różnić pod względem użytego zestawu treningowego (wiedza wstępna), możliwości, które oferują (np. poprzez API lub SDK) oraz rodzaju treści, na które są zoptymalizowane (np. kod vs obrazy vs tekst). Zrozum mocne i słabe strony używanego modelu i wykorzystaj tę wiedzę, aby _priorytetyzować zadania_ lub budować _dostosowane szablony_ zoptymalizowane pod kątem możliwości modelu.

3. **Iteracja i walidacja są ważne.** Modele szybko się rozwijają, podobnie jak techniki inżynierii promptów. Jako ekspert domenowy możesz mieć dodatkowy kontekst lub kryteria dla _swojej_ konkretnej aplikacji, które nie muszą mieć zastosowania w szerszej społeczności. Używaj narzędzi i technik inżynierii promptów, aby "rozpocząć szybko" konstrukcję promptu, a potem iteruj i weryfikuj wyniki, korzystając z własnej intuicji i wiedzy specjalistycznej. Rejestruj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), którą inni mogą wykorzystywać jako nową bazę odniesienia dla szybszych kolejnych iteracji.

## Najlepsze praktyki

Spójrzmy teraz na powszechnie polecane najlepsze praktyki zalecane przez praktyków z [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) oraz [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                               | Dlaczego                                                                                                                                                                                                                                         |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Testuj najnowsze modele.          | Nowe generacje modeli prawdopodobnie mają ulepszone cechy i jakość, ale mogą też generować wyższe koszty. Oceń ich wpływ, a następnie podejmij decyzje o migracji.                                                                               |
| Oddziel instrukcje i kontekst    | Sprawdź, czy twój model/dostawca definiuje _separator-y_, aby wyraźniej odróżnić instrukcje, treść podstawową i wtórną. To może pomóc modelom precyzyjniej przypisywać wagi tokenom.                                                            |
| Bądź precyzyjny i jasny           | Podaj więcej szczegółów o oczekiwanym kontekście, rezultacie, długości, formacie, stylu itd. To poprawi zarówno jakość, jak i spójność odpowiedzi. Zapisuj przepisy w wielokrotnego użytku szablonach.                                            |
| Bądź opisowy, używaj przykładów   | Modele lepiej reagują na podejście „pokaż i powiedz”. Zacznij od podejścia `zero-shot`, gdzie dajesz instrukcję (ale bez przykładów), następnie spróbuj `few-shot` jako udoskonalenie, podając kilka przykładów pożądanego wyniku. Używaj analogii.|
| Używaj wskazówek do uruchamiania uzupełnień | Nakieruj model na oczekiwany wynik, dostarczając mu słowa lub frazy otwierające, które może wykorzystać jako punkt startowy do wygenerowania odpowiedzi.                                                                                        |
| Powtarzaj                         | Czasami trzeba powtarzać instrukcje modelowi. Podawaj instrukcje przed i po treści głównej, używaj instrukcji i wskazówek itd. Iteruj i weryfikuj, co działa najlepiej.                                                                       |
| Kolejność ma znaczenie            | Kolejność, w jakiej prezentujesz informacje modelowi, może wpływać na wynik, nawet w przykładach uczących, ze względu na efekt świeżości. Wypróbuj różne opcje, aby zobaczyć, co działa najlepiej.                                               |
| Daj modelowi „wyjście awaryjne”   | Zapewnij modelowi _zapewnienie odpowiedzi alternatywnej_, którą może podać, jeśli z jakiegokolwiek powodu nie jest w stanie wykonać zadania. To może zmniejszyć ryzyko generowania fałszywych lub wymyślonych odpowiedzi.                          |
|                                   |                                                                                                                                                                                                                                                 |

Jak w przypadku wszystkich najlepszych praktyk, pamiętaj, że _twoje doświadczenia mogą się różnić_ w zależności od modelu, zadania i dziedziny. Używaj ich jako punktu wyjścia i iteruj, aby znaleźć to, co działa najlepiej dla ciebie. Stale oceniaj na nowo swój proces inżynierii promptów, gdy pojawiają się nowe modele i narzędzia, skupiając się na skalowalności procesu i jakości odpowiedzi.

<!--
SZABLON LEKCJI:
Ta jednostka powinna zawierać wyzwanie programistyczne, jeśli to możliwe

WYZWANIE:
Link do Jupyter Notebook z samymi komentarzami w kodzie w instrukcjach (sekcje kodu są puste).

ROZWIĄZANIE:
Link do kopii tego Notebooka z uzupełnionymi i uruchomionymi promptami, pokazujący jeden przykładowy rezultat.
-->

## Zadanie

Gratulacje! Dotarłeś do końca lekcji! Czas przetestować niektóre z tych koncepcji i technik na prawdziwych przykładach!

W naszym zadaniu skorzystamy z Jupyter Notebook z ćwiczeniami, które możesz wykonywać interaktywnie. Możesz również rozszerzać Notebook o własne komórki Markdown i kodu, by samodzielnie eksplorować pomysły i techniki.

### Aby zacząć, forkuj repozytorium, a następnie

- (Zalecane) Uruchom GitHub Codespaces
- (Alternatywnie) Sklonuj repozytorium na lokalne urządzenie i korzystaj z niego za pomocą Docker Desktop
- (Alternatywnie) Otwórz Notebook w preferowanym środowisku uruchomieniowym dla notebooków.

### Następnie skonfiguruj swoje zmienne środowiskowe

- Skopiuj plik `.env.copy` z katalogu głównego repozytorium do `.env` i uzupełnij wartości `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` oraz `AZURE_OPENAI_DEPLOYMENT`. Wróć do [sekcji Learning Sandbox](#piaskownica-nauki), aby dowiedzieć się jak.

### Następnie otwórz Jupyter Notebook

- Wybierz jądro środowiska uruchomieniowego. Jeśli korzystasz z opcji 1 lub 2, po prostu wybierz domyślne jądro Python 3.10.x zapewnione przez kontener deweloperski.

Jesteś gotów do uruchomienia ćwiczeń. Zwróć uwagę, że tutaj nie ma _dobrych ani złych_ odpowiedzi — chodzi o eksplorację opcji metodą prób i błędów oraz zdobycie intuicji, co działa dla danego modelu i domeny zastosowania.

_Z tego powodu w tej lekcji nie ma segmentów z rozwiązaniami kodu. Zamiast tego Notebook zawiera komórki Markdown zatytułowane "Moje rozwiązanie:", które pokazują jeden przykładowy wynik do odniesienia._

 <!--
SZABLON LEKCJI:
Podsumuj sekcję, dodając podsumowanie i zasoby do nauki samodzielnej.
-->

## Sprawdzenie wiedzy

Który z poniższych promptów jest dobry i stosuje się do rozsądnych najlepszych praktyk?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90 zaparkowanego przy urwisku podczas zachodu słońca
3. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90

A: 2, to najlepszy prompt, ponieważ dostarcza szczegółów na temat "czego" i wchodzi w specyfikę (nie jest to zwykły samochód, lecz konkretny model i marka), a także opisuje ogólne otoczenie. 3 jest kolejnym najlepszym, bo także zawiera dużo opisu.

## 🚀 Wyzwanie

Sprawdź, czy potrafisz wykorzystać technikę "wskazówki" (cue) z promptem: Uzupełnij zdanie "Pokaż mi obraz czerwonego samochodu marki Volvo i ". Co odpowie, i jak byś to poprawił?

## Świetna robota! Kontynuuj naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach inżynierii promptów? Przejdź na [stronę dalszej nauki](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne świetne materiały na ten temat.

Przejdź do Lekcji 5, gdzie omówimy [zaawansowane techniki promptowania](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->