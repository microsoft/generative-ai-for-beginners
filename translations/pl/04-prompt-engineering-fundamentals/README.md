<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0135e6c271f3ece8699050d4debbce88",
  "translation_date": "2025-10-18T00:57:29+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pl"
}
-->
# Podstawy Inżynierii Promptów

[![Podstawy Inżynierii Promptów](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.pl.png)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Wprowadzenie
Ten moduł obejmuje podstawowe pojęcia i techniki tworzenia skutecznych promptów dla modeli generatywnej sztucznej inteligencji. Sposób, w jaki piszesz swój prompt do LLM, ma znaczenie. Starannie skonstruowany prompt może zapewnić lepszą jakość odpowiedzi. Ale co dokładnie oznaczają takie terminy jak _prompt_ i _inżynieria promptów_? I jak mogę poprawić dane wejściowe _promptu_, które wysyłam do LLM? Na te pytania spróbujemy odpowiedzieć w tym rozdziale i następnym.

_Generatywna sztuczna inteligencja_ potrafi tworzyć nową treść (np. tekst, obrazy, dźwięk, kod itp.) w odpowiedzi na zapytania użytkowników. Osiąga to za pomocą _Wielkich Modeli Językowych_ takich jak seria GPT ("Generative Pre-trained Transformer") od OpenAI, które są trenowane do pracy z językiem naturalnym i kodem.

Użytkownicy mogą teraz wchodzić w interakcje z tymi modelami za pomocą znanych interfejsów, takich jak czat, bez potrzeby posiadania specjalistycznej wiedzy technicznej czy szkolenia. Modele są oparte na _promptach_ - użytkownicy wysyłają tekst wejściowy (prompt) i otrzymują odpowiedź AI (wynik). Następnie mogą "rozmawiać z AI" w sposób iteracyjny, w wieloetapowych konwersacjach, dopracowując swój prompt, aż odpowiedź spełni ich oczekiwania.

"Prompty" stają się teraz głównym _interfejsem programistycznym_ dla aplikacji generatywnej AI, wskazując modelom, co mają robić i wpływając na jakość zwracanych odpowiedzi. "Inżynieria promptów" to szybko rozwijająca się dziedzina badań, która koncentruje się na _projektowaniu i optymalizacji_ promptów w celu uzyskania spójnych i wysokiej jakości odpowiedzi na dużą skalę.

## Cele nauki

W tej lekcji dowiemy się, czym jest inżynieria promptów, dlaczego jest ważna i jak możemy tworzyć bardziej skuteczne prompty dla danego modelu i celu aplikacji. Zrozumiemy podstawowe pojęcia i najlepsze praktyki w zakresie inżynierii promptów - oraz poznamy interaktywne środowisko "sandbox" w Jupyter Notebooks, w którym możemy zastosować te koncepcje na rzeczywistych przykładach.

Pod koniec tej lekcji będziemy w stanie:

1. Wyjaśnić, czym jest inżynieria promptów i dlaczego jest ważna.
2. Opisać elementy promptu i sposób ich wykorzystania.
3. Poznać najlepsze praktyki i techniki inżynierii promptów.
4. Zastosować poznane techniki na rzeczywistych przykładach, korzystając z punktu końcowego OpenAI.

## Kluczowe pojęcia

Inżynieria promptów: Praktyka projektowania i udoskonalania danych wejściowych w celu nakierowania modeli AI na generowanie pożądanych wyników.
Tokenizacja: Proces przekształcania tekstu w mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetworzyć.
LLM dostosowane do instrukcji: Wielkie modele językowe (LLM), które zostały dostrojone za pomocą konkretnych instrukcji w celu poprawy dokładności i trafności odpowiedzi.

## Środowisko nauki

Inżynieria promptów jest obecnie bardziej sztuką niż nauką. Najlepszym sposobem na rozwinięcie intuicji w tym zakresie jest _praktyka_ i podejście oparte na próbach i błędach, które łączy wiedzę ekspercką z zalecanymi technikami i optymalizacjami specyficznymi dla modelu.

Notatnik Jupyter towarzyszący tej lekcji zapewnia środowisko _sandbox_, w którym możesz wypróbować to, czego się uczysz - na bieżąco lub w ramach wyzwania programistycznego na końcu. Aby wykonać ćwiczenia, będziesz potrzebować:

1. **Klucza API Azure OpenAI** - punktu końcowego dla wdrożonego LLM.
2. **Środowiska uruchomieniowego Python** - w którym można uruchomić notatnik.
3. **Lokalnych zmiennych środowiskowych** - _ukończ [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) teraz, aby się przygotować_.

Notatnik zawiera ćwiczenia _startowe_ - ale zachęcamy do dodawania własnych sekcji _Markdown_ (opis) i _Code_ (zapytania promptów), aby wypróbować więcej przykładów lub pomysłów - i rozwijać intuicję w projektowaniu promptów.

## Przewodnik ilustrowany

Chcesz zrozumieć ogólny obraz tego, co obejmuje ta lekcja, zanim się zagłębisz? Sprawdź ten przewodnik ilustrowany, który daje poczucie głównych tematów i kluczowych wniosków, o których warto pomyśleć w każdym z nich. Plan lekcji prowadzi od zrozumienia podstawowych koncepcji i wyzwań do ich rozwiązania za pomocą odpowiednich technik inżynierii promptów i najlepszych praktyk. Zauważ, że sekcja "Zaawansowane techniki" w tym przewodniku odnosi się do treści omówionych w _następnym_ rozdziale tego programu nauczania.

![Przewodnik ilustrowany po inżynierii promptów](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.pl.png)

## Nasz startup

Porozmawiajmy teraz o tym, jak _ten temat_ odnosi się do naszej misji startupu, aby [wprowadzać innowacje AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje wspierane przez AI, które umożliwiają _spersonalizowaną naukę_ - więc zastanówmy się, jak różni użytkownicy naszej aplikacji mogą "projektować" prompty:

- **Administratorzy** mogą poprosić AI o _analizę danych dotyczących programu nauczania w celu zidentyfikowania luk w pokryciu tematycznym_. AI może podsumować wyniki lub przedstawić je w formie wizualnej za pomocą kodu.
- **Nauczyciele** mogą poprosić AI o _stworzenie planu lekcji dla określonej grupy docelowej i tematu_. AI może stworzyć spersonalizowany plan w określonym formacie.
- **Uczniowie** mogą poprosić AI o _pomoc w nauce trudnego przedmiotu_. AI może teraz prowadzić uczniów, oferując lekcje, wskazówki i przykłady dostosowane do ich poziomu.

To tylko wierzchołek góry lodowej. Sprawdź [Prompty dla edukacji](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otwartą bibliotekę promptów, opracowaną przez ekspertów edukacyjnych - aby uzyskać szersze spojrzenie na możliwości! _Spróbuj uruchomić niektóre z tych promptów w sandboxie lub w OpenAI Playground, aby zobaczyć, co się stanie!_

## Czym jest inżynieria promptów?

Rozpoczęliśmy tę lekcję od zdefiniowania **inżynierii promptów** jako procesu _projektowania i optymalizacji_ tekstowych danych wejściowych (promptów) w celu uzyskania spójnych i wysokiej jakości odpowiedzi (wyników) dla danego celu aplikacji i modelu. Możemy myśleć o tym jako o procesie dwustopniowym:

- _projektowanie_ początkowego promptu dla danego modelu i celu
- _udoskonalanie_ promptu w sposób iteracyjny w celu poprawy jakości odpowiedzi

Jest to proces oparty na próbach i błędach, który wymaga intuicji użytkownika i wysiłku, aby osiągnąć optymalne wyniki. Dlaczego więc jest to ważne? Aby odpowiedzieć na to pytanie, musimy najpierw zrozumieć trzy pojęcia:

- _Tokenizacja_ = jak model "widzi" prompt
- _Podstawowe LLM_ = jak model bazowy "przetwarza" prompt
- _LLM dostosowane do instrukcji_ = jak model może teraz widzieć "zadania"

### Tokenizacja

LLM widzi prompty jako _ciąg tokenów_, przy czym różne modele (lub wersje modelu) mogą tokenizować ten sam prompt w różny sposób. Ponieważ LLM są trenowane na tokenach (a nie na surowym tekście), sposób, w jaki prompty są tokenizowane, ma bezpośredni wpływ na jakość generowanej odpowiedzi.

Aby zrozumieć, jak działa tokenizacja, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) pokazane poniżej. Skopiuj swój prompt - i zobacz, jak zostaje przekształcony w tokeny, zwracając uwagę na sposób, w jaki obsługiwane są znaki odstępu i znaki interpunkcyjne. Zauważ, że ten przykład pokazuje starszy LLM (GPT-3) - więc wypróbowanie tego z nowszym modelem może dać inny wynik.

![Tokenizacja](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.pl.png)

### Koncepcja: Modele bazowe

Po tokenizacji promptu główną funkcją ["Podstawowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (lub modelu bazowego) jest przewidywanie tokenu w tym ciągu. Ponieważ LLM są trenowane na ogromnych zbiorach danych tekstowych, mają dobrą znajomość statystycznych relacji między tokenami i mogą dokonywać tego przewidywania z pewnym stopniem pewności. Należy zauważyć, że nie rozumieją _znaczenia_ słów w promptach czy tokenach; widzą jedynie wzór, który mogą "uzupełnić" kolejnym przewidywaniem. Mogą kontynuować przewidywanie ciągu, aż zostanie ono przerwane przez interwencję użytkownika lub jakiś wcześniej ustalony warunek.

Chcesz zobaczyć, jak działa uzupełnianie oparte na promptach? Wprowadź powyższy prompt do [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) w Azure OpenAI Studio z domyślnymi ustawieniami. System jest skonfigurowany tak, aby traktować prompty jako zapytania o informacje - więc powinieneś zobaczyć wynik, który spełnia ten kontekst.

Ale co, jeśli użytkownik chciałby zobaczyć coś konkretnego, co spełnia określone kryteria lub cel zadania? Właśnie tutaj wchodzą w grę _LLM dostosowane do instrukcji_.

![Uzupełnianie czatu w modelu bazowym LLM](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.pl.png)

### Koncepcja: LLM dostosowane do instrukcji

[LLM dostosowane do instrukcji](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zaczynają od modelu bazowego i dostrajają go za pomocą przykładów lub par wejście/wyjście (np. wieloetapowych "wiadomości"), które mogą zawierać jasne instrukcje - a odpowiedź AI próbuje podążać za tą instrukcją.

Wykorzystuje to techniki takie jak uczenie przez wzmocnienie z informacją zwrotną od człowieka (RLHF), które mogą trenować model do _podążania za instrukcjami_ i _uczenia się na podstawie informacji zwrotnej_, aby generował odpowiedzi lepiej dostosowane do praktycznych zastosowań i bardziej trafne w kontekście celów użytkownika.

Spróbujmy - wróć do powyższego promptu, ale teraz zmień _wiadomość systemową_, aby dostarczyć następującą instrukcję jako kontekst:

> _Podsumuj treść, którą otrzymasz, dla ucznia drugiej klasy. Ogranicz wynik do jednego akapitu z 3-5 punktami._

Zobacz, jak wynik jest teraz dostosowany do odzwierciedlenia pożądanego celu i formatu? Nauczyciel może teraz bezpośrednio wykorzystać tę odpowiedź w swoich slajdach na lekcji.

![Uzupełnianie czatu w modelu dostosowanym do instrukcji LLM](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.pl.png)

## Dlaczego potrzebujemy inżynierii promptów?

Teraz, gdy wiemy, jak prompty są przetwarzane przez LLM, porozmawiajmy o _dlaczego_ potrzebujemy inżynierii promptów. Odpowiedź leży w fakcie, że obecne LLM stawiają przed nami szereg wyzwań, które sprawiają, że _wiarygodne i spójne wyniki_ są trudniejsze do osiągnięcia bez wysiłku włożonego w konstrukcję i optymalizację promptów. Na przykład:

1. **Odpowiedzi modeli są stochastyczne.** _Ten sam prompt_ prawdopodobnie wygeneruje różne odpowiedzi w różnych modelach lub wersjach modeli. Może również generować różne wyniki w _tym samym modelu_ w różnych momentach. _Techniki inżynierii promptów mogą pomóc nam zminimalizować te różnice, zapewniając lepsze zabezpieczenia_.

1. **Modele mogą tworzyć fałszywe odpowiedzi.** Modele są wstępnie trenowane na _dużych, ale ograniczonych_ zbiorach danych, co oznacza, że brakuje im wiedzy na temat pojęć spoza zakresu tego treningu. W rezultacie mogą generować wyniki, które są nieścisłe, wymyślone lub bezpośrednio sprzeczne z znanymi faktami. _Techniki inżynierii promptów pomagają użytkownikom identyfikować i minimalizować takie fałszerstwa, np. prosząc AI o cytaty lub uzasadnienia_.

1. **Zdolności modeli będą się różnić.** Nowsze modele lub generacje modeli będą miały bogatsze możliwości, ale także wprowadzą unikalne cechy i kompromisy w kosztach i złożoności. _Inżynieria promptów może pomóc nam opracować najlepsze praktyki i przepływy pracy, które abstrahują różnice i dostosowują się do specyficznych wymagań modeli w skalowalny, płynny sposób_.

Zobaczmy to w działaniu w OpenAI lub Azure OpenAI Playground:

- Użyj tego samego promptu z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) - czy zauważyłeś różnice?
- Użyj tego samego promptu wielokrotnie z _tym samym_ wdrożeniem LLM (np. Azure OpenAI Playground) - jak różniły się te wariacje?

### Przykład fałszerstw

W tym kursie używamy terminu **"fałszerstwo"** w odniesieniu do zjawiska, w którym LLM czasami generują nieprawdziwe informacje z powodu ograniczeń w ich treningu lub innych uwarunkowań. Możesz również spotkać się z określeniem _"halucynacje"_ w popularnych artykułach lub pracach naukowych. Jednak zdecydowanie zalecamy używanie terminu _"fałszerstwo"_, aby przypadkowo nie przypisywać cech ludzkich do wyniku generowanego przez maszynę. W ten sposób wzmacniamy [wytyczne dotyczące odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z perspektywy terminologicznej, eliminując terminy, które mogą być uznane za obraźliwe lub nieinkluzywne w niektórych kontekstach.

Chcesz zrozumieć, jak działają fałszerstwa? Pomyśl o promptcie, który instruuje AI, aby wygenerowała treść na temat nieistniejącego zagadnienia (aby upewnić się, że nie znajduje się ono w zbiorze danych treningowych). Na przykład - spróbowałem tego promptu:

> **Prompt:** stwórz plan lekcji na
Wyszukiwanie w Internecie pokazało, że istnieją fikcyjne opowieści (np. seriale telewizyjne lub książki) o wojnach na Marsie - ale żadna z nich nie dotyczy roku 2076. Zdrowy rozsądek podpowiada również, że rok 2076 jest _przyszłością_ i nie może być związany z rzeczywistym wydarzeniem.

Co się więc dzieje, gdy uruchamiamy ten prompt z różnymi dostawcami LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

![Odpowiedź 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.pl.png)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

![Odpowiedź 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.pl.png)

> **Odpowiedź 3**: Hugging Face Chat Playground (LLama-2)

![Odpowiedź 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.pl.png)

Zgodnie z oczekiwaniami, każdy model (lub wersja modelu) generuje nieco inne odpowiedzi dzięki stochastycznemu zachowaniu i różnicom w możliwościach modelu. Na przykład jeden model kieruje się do odbiorców na poziomie ósmej klasy, podczas gdy inny zakłada poziom ucznia szkoły średniej. Jednak wszystkie trzy modele wygenerowały odpowiedzi, które mogłyby przekonać nieświadomego użytkownika, że wydarzenie było prawdziwe.

Techniki inżynierii promptów, takie jak _metaprompting_ i _konfiguracja temperatury_, mogą w pewnym stopniu zmniejszyć fabrykacje modelu. Nowe _architektury_ inżynierii promptów również płynnie integrują nowe narzędzia i techniki w przepływie promptów, aby złagodzić lub zmniejszyć niektóre z tych efektów.

## Studium przypadku: GitHub Copilot

Zakończmy tę sekcję, zyskując wgląd w to, jak inżynieria promptów jest wykorzystywana w rzeczywistych rozwiązaniach, przyglądając się jednemu studium przypadku: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot to Twój "AI Pair Programmer" - przekształca tekstowe prompty w uzupełnienia kodu i jest zintegrowany z Twoim środowiskiem programistycznym (np. Visual Studio Code), zapewniając płynne doświadczenie użytkownika. Jak udokumentowano w serii poniższych wpisów na blogu, najwcześniejsza wersja była oparta na modelu OpenAI Codex - inżynierowie szybko zdali sobie sprawę z potrzeby dostosowania modelu i opracowania lepszych technik inżynierii promptów, aby poprawić jakość kodu. W lipcu [zadebiutowali ulepszonym modelem AI, który wykracza poza Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), oferując jeszcze szybsze sugestie.

Przeczytaj wpisy w kolejności, aby śledzić ich drogę nauki.

- **Maj 2023** | [GitHub Copilot staje się coraz lepszy w rozumieniu Twojego kodu](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Maj 2023** | [Wewnątrz GitHub: Praca z LLM za GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Czerwiec 2023** | [Jak pisać lepsze prompty dla GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Lipiec 2023** | [.. GitHub Copilot wykracza poza Codex dzięki ulepszonemu modelowi AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Lipiec 2023** | [Przewodnik dla programistów po inżynierii promptów i LLM](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Wrzesień 2023** | [Jak zbudować aplikację LLM dla przedsiębiorstw: Lekcje z GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Możesz również przeglądać ich [blog inżynieryjny](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) w poszukiwaniu więcej wpisów, takich jak [ten](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), który pokazuje, jak te modele i techniki są _stosowane_ w celu napędzania rzeczywistych aplikacji.

---

## Konstrukcja promptów

Widzieliśmy, dlaczego inżynieria promptów jest ważna - teraz zrozummy, jak prompty są _konstruowane_, abyśmy mogli ocenić różne techniki projektowania bardziej efektywnych promptów.

### Podstawowy prompt

Zacznijmy od podstawowego promptu: tekstowego wejścia wysyłanego do modelu bez dodatkowego kontekstu. Oto przykład - gdy wysyłamy pierwsze słowa hymnu narodowego USA do OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), natychmiast _uzupełnia_ odpowiedź o kolejne linijki, ilustrując podstawowe zachowanie predykcyjne.

| Prompt (Wejście) | Completion (Wyjście)                                                                                                                        |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Wygląda na to, że zaczynasz tekst "The Star-Spangled Banner", hymnu narodowego Stanów Zjednoczonych. Pełny tekst to ... |

### Złożony prompt

Teraz dodajmy kontekst i instrukcje do tego podstawowego promptu. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) pozwala nam skonstruować złożony prompt jako kolekcję _wiadomości_ z:

- Parami wejście/wyjście odzwierciedlającymi _wejście użytkownika_ i _odpowiedź asystenta_.
- Wiadomością systemową ustawiającą kontekst dla zachowania lub osobowości asystenta.

Żądanie ma teraz poniższą formę, gdzie _tokenizacja_ skutecznie przechwytuje istotne informacje z kontekstu i rozmowy. Zmiana kontekstu systemowego może być równie wpływowa na jakość uzupełnień, jak dostarczone wejścia użytkownika.

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

### Prompt instrukcji

W powyższych przykładach prompt użytkownika był prostym zapytaniem tekstowym, które można interpretować jako prośbę o informacje. W przypadku promptów _instrukcji_ możemy użyć tego tekstu, aby bardziej szczegółowo określić zadanie, zapewniając lepsze wskazówki dla AI. Oto przykład:

| Prompt (Wejście)                                                                                                                                                                                                                         | Completion (Wyjście)                                                                                                        | Typ instrukcji      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Napisz opis wojny secesyjnej                                                                                                                                                                      | _zwrócono prosty akapit_                                                                                                   | Prosty              |
| Napisz opis wojny secesyjnej. Podaj kluczowe daty i wydarzenia oraz opisz ich znaczenie                                                                                                          | _zwrócono akapit, a następnie listę kluczowych dat wydarzeń z opisami_                                                     | Złożony             |
| Napisz opis wojny secesyjnej w jednym akapicie. Podaj 3 punkty z kluczowymi datami i ich znaczeniem. Podaj 3 kolejne punkty z kluczowymi postaciami historycznymi i ich wkładem. Zwróć wynik jako plik JSON | _zwrócono bardziej szczegółowe informacje w polu tekstowym, sformatowane jako JSON, które można skopiować i zweryfikować_ | Złożony. Sformatowany. |

## Główna treść

W powyższych przykładach prompt był nadal dość otwarty, pozwalając LLM zdecydować, która część jego wstępnie wytrenowanego zestawu danych jest istotna. W przypadku wzorca projektowego _głównej treści_ tekst wejściowy jest podzielony na dwie części:

- instrukcję (działanie)
- istotną treść (która wpływa na działanie)

Oto przykład, w którym instrukcja brzmi "podsumuj to w 2 zdaniach".

| Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completion (Wyjście)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż masa wszystkich innych planet w Układzie Słonecznym razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisaniem historii. Został nazwany na cześć rzymskiego boga Jowisza.[19] Gdy jest widoczny z Ziemi, Jowisz może być na tyle jasny, że jego odbite światło rzuca widoczne cienie,[20] i jest średnio trzecim najjaśniejszym naturalnym obiektem na nocnym niebie po Księżycu i Wenus. <br/> **Podsumuj to w 2 krótkich zdaniach** | Jowisz, piąta planeta od Słońca, jest największą w Układzie Słonecznym i znany jest jako jeden z najjaśniejszych obiektów na nocnym niebie. Nazwany na cześć rzymskiego boga Jowisza, jest gazowym olbrzymem o masie dwa i pół razy większej niż masa wszystkich innych planet w Układzie Słonecznym razem wziętych. |

Segment głównej treści może być używany na różne sposoby, aby skuteczniej kierować instrukcjami:

- **Przykłady** - zamiast mówić modelowi, co ma zrobić za pomocą wyraźnej instrukcji, podaj mu przykłady tego, co ma zrobić, i pozwól mu wywnioskować wzorzec.
- **Wskazówki** - podążaj za instrukcją z "wskazówką", która przygotowuje uzupełnienie, kierując model w stronę bardziej istotnych odpowiedzi.
- **Szablony** - są to powtarzalne 'przepisy' na prompty z miejscami na zmienne, które można dostosować za pomocą danych do konkretnych przypadków użycia.

Przyjrzyjmy się, jak to działa w praktyce.

### Użycie przykładów

To podejście polega na użyciu głównej treści do "nakarmienia modelu" kilkoma przykładami pożądanego wyniku dla danego polecenia i pozwoleniu mu na wywnioskowanie wzorca dla pożądanego wyniku. W zależności od liczby podanych przykładów możemy mieć prompty zero-shot, one-shot, few-shot itd.

Prompt składa się teraz z trzech elementów:

- Opis zadania
- Kilka przykładów pożądanego wyniku
- Początek nowego przykładu (który staje się domyślnym opisem zadania)

| Typ uczenia | Prompt (Wejście)                                                                                                                                        | Completion (Wyjście)         |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------- |
| Zero-shot   | "Słońce świeci". Przetłumacz na hiszpański                                                                                                              | "El Sol está brillando".    |
| One-shot    | "Słońce świeci" => ""El Sol está brillando". <br> "Jest zimny i wietrzny dzień" =>                                                                      | "Es un día frío y ventoso". |
| Few-shot    | Zawodnik przebiegł bazy => Baseball <br/> Zawodnik zdobył asa => Tenis <br/> Zawodnik zdobył szóstkę => Krykiet <br/> Zawodnik wykonał wsad =>          | Koszykówka                  |
|             |                                                                                                                                                         |                             |

Zauważ, że musieliśmy podać wyraźną instrukcję ("Przetłumacz na hiszpański") w przykładzie zero-shot, ale jest ona wywnioskowana w przykładzie one-shot. Przykład few-shot pokazuje, jak dodanie większej liczby przykładów pozwala modelom na bardziej precyzyjne wnioskowanie bez dodatkowych instrukcji.

### Wskazówki w promptach

Inną techniką wykorzystania głównej treści jest podanie _wskazówek_ zamiast przykładów. W tym przypadku dajemy modelowi wskazówkę w odpowiednim kierunku, _rozpoczynając_ go fragmentem, który odzwierciedla pożądany format odpowiedzi. Model następnie "podąża za wskazówką", kontynuując w tym samym stylu.

| Liczba wskazówek | Prompt (Wejście)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completion (Wyjście)                                                                                                                                                                                                                                                                                       |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie jednej tysięcznej masy Słońca, ale dwa i pół razy większej niż masa wszystkich innych planet w Układzie Słonecznym razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisaniem historii. <br/>**Podsumuj to**                                       | Jowisz jest największą planetą w naszym Układzie Słonecznym i piątą od Słońca. Jest gazowym olbrzymem o masie 1/1000 masy Słońca, ale jest cięższy niż wszystkie inne planety razem wzięte. Starożytne cywilizacje znały Jowisza od dawna, a na nocnym niebie jest łatwo widoczny. |
| 1              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie stanowiącej jedną tysięczną masy Słońca, ale dwa i pół razy większej niż masa wszystkich innych planet w Układzie Słonecznym razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisaniem historii. <br/>**Podsumuj to** <br/> Dowiedzieliśmy się, że Jowisz | jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie stanowiącej jedną tysięczną masy Słońca, ale dwa i pół razy większej niż masa wszystkich innych planet razem wziętych. Jest łatwo widoczny gołym okiem i znany od czasów starożytnych.                        |
| 2              | Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. Jest gazowym olbrzymem o masie stanowiącej jedną tysięczną masy Słońca, ale dwa i pół razy większej niż masa wszystkich innych planet w Układzie Słonecznym razem wziętych. Jowisz jest jednym z najjaśniejszych obiektów widocznych gołym okiem na nocnym niebie i był znany starożytnym cywilizacjom jeszcze przed zapisaniem historii. <br/>**Podsumuj to** <br/> Top 3 Fakty, które poznaliśmy:         | 1. Jowisz jest piątą planetą od Słońca i największą w Układzie Słonecznym. <br/> 2. Jest gazowym olbrzymem o masie stanowiącej jedną tysięczną masy Słońca...<br/> 3. Jowisz był widoczny gołym okiem od czasów starożytnych ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Szablony promptów

Szablon promptu to _z góry zdefiniowany przepis na prompt_, który można przechowywać i ponownie wykorzystywać w razie potrzeby, aby zapewnić bardziej spójne doświadczenia użytkownika na dużą skalę. W najprostszej formie jest to po prostu zbiór przykładów promptów, takich jak [ten od OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), który zawiera zarówno interaktywne komponenty promptu (wiadomości użytkownika i systemu), jak i format żądania API - wspierając ponowne użycie.

W bardziej złożonej formie, jak [ten przykład z LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), zawiera _zastępniki_, które można zastąpić danymi z różnych źródeł (wejście użytkownika, kontekst systemu, zewnętrzne źródła danych itp.), aby dynamicznie generować prompt. Pozwala to na stworzenie biblioteki wielokrotnego użytku promptów, które mogą być używane do programowego zapewnienia spójnych doświadczeń użytkownika na dużą skalę.

Ostatecznie prawdziwa wartość szablonów leży w możliwości tworzenia i publikowania _bibliotek promptów_ dla pionowych domen aplikacji - gdzie szablon promptu jest teraz _optymalizowany_ w celu odzwierciedlenia kontekstu specyficznego dla aplikacji lub przykładów, które sprawiają, że odpowiedzi są bardziej trafne i dokładne dla docelowej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest świetnym przykładem tego podejścia, kurując bibliotekę promptów dla domeny edukacyjnej z naciskiem na kluczowe cele, takie jak planowanie lekcji, projektowanie programów nauczania, korepetycje dla uczniów itp.

## Treści wspierające

Jeśli myślimy o konstrukcji promptu jako o posiadaniu instrukcji (zadania) i celu (głównej treści), to _treści drugorzędne_ są jak dodatkowy kontekst, który dostarczamy, aby **wpłynąć na wynik w jakiś sposób**. Mogą to być parametry dostrajania, instrukcje formatowania, taksonomie tematów itp., które mogą pomóc modelowi _dostosować_ swoją odpowiedź do oczekiwań lub celów użytkownika.

Na przykład: Mając katalog kursów z obszernymi metadanymi (nazwa, opis, poziom, tagi metadanych, instruktor itp.) na temat wszystkich dostępnych kursów w programie nauczania:

- możemy zdefiniować instrukcję "podsumuj katalog kursów na jesień 2023"
- możemy użyć głównej treści, aby dostarczyć kilka przykładów pożądanego wyniku
- możemy użyć treści drugorzędnych, aby zidentyfikować 5 najważniejszych "tagów" zainteresowania.

Teraz model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów - ale jeśli wynik ma wiele tagów, może priorytetyzować 5 tagów zidentyfikowanych w treści drugorzędnej.

---

<!--
SZABLON LEKCJI:
Ta jednostka powinna obejmować podstawowy koncept #1.
Wzmocnij koncept przykładami i odniesieniami.

KONCEPT #3:
Techniki inżynierii promptów.
Jakie są podstawowe techniki inżynierii promptów?
Zilustruj to ćwiczeniami.
-->

## Najlepsze praktyki tworzenia promptów

Teraz, gdy wiemy, jak można _konstruować_ prompty, możemy zacząć myśleć o tym, jak je _projektować_, aby odzwierciedlały najlepsze praktyki. Możemy to rozważyć w dwóch częściach - mając odpowiednie _nastawienie_ i stosując odpowiednie _techniki_.

### Nastawienie w inżynierii promptów

Inżynieria promptów to proces prób i błędów, więc pamiętaj o trzech szerokich czynnikach przewodnich:

1. **Zrozumienie domeny ma znaczenie.** Dokładność i trafność odpowiedzi zależy od _domeny_, w której działa aplikacja lub użytkownik. Wykorzystaj swoją intuicję i wiedzę domenową, aby **dostosować techniki**. Na przykład, zdefiniuj _osobowości specyficzne dla domeny_ w promptach systemowych lub użyj _szablonów specyficznych dla domeny_ w promptach użytkownika. Dostarcz treści drugorzędne, które odzwierciedlają konteksty specyficzne dla domeny, lub użyj _wskazówek i przykładów specyficznych dla domeny_, aby skierować model na znane wzorce użycia.

2. **Zrozumienie modelu ma znaczenie.** Wiemy, że modele są z natury stochastyczne. Ale implementacje modeli mogą również różnić się pod względem używanego zestawu danych treningowych (wiedza wstępnie wytrenowana), dostarczanych możliwości (np. za pośrednictwem API lub SDK) i rodzaju treści, do których są zoptymalizowane (np. kod, obrazy, tekst). Zrozum mocne i słabe strony modelu, którego używasz, i wykorzystaj tę wiedzę do _priorytetyzacji zadań_ lub budowy _dostosowanych szablonów_ zoptymalizowanych pod kątem możliwości modelu.

3. **Iteracja i walidacja mają znaczenie.** Modele ewoluują szybko, podobnie jak techniki inżynierii promptów. Jako ekspert domenowy możesz mieć inne konteksty lub kryteria dla _swojej_ specyficznej aplikacji, które mogą nie mieć zastosowania do szerszej społeczności. Użyj narzędzi i technik inżynierii promptów, aby "rozpocząć" konstrukcję promptu, a następnie iteruj i weryfikuj wyniki, korzystając z własnej intuicji i wiedzy domenowej. Zapisuj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), które mogą być używane jako nowa baza przez innych, aby przyspieszyć iteracje w przyszłości.

## Najlepsze praktyki

Przyjrzyjmy się teraz powszechnym najlepszym praktykom zalecanym przez [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i praktyków [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                               | Dlaczego                                                                                                                                                                                                                                               |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oceń najnowsze modele.           | Nowe generacje modeli prawdopodobnie mają ulepszone funkcje i jakość - ale mogą również wiązać się z wyższymi kosztami. Oceń ich wpływ, a następnie podejmij decyzje o migracji.                                                                        |
| Oddziel instrukcje i kontekst    | Sprawdź, czy Twój model/dostawca definiuje _delimitery_, aby wyraźniej rozróżnić instrukcje, treści główne i drugorzędne. Może to pomóc modelom dokładniej przypisywać wagi do tokenów.                                                                  |
| Bądź konkretny i jasny           | Podaj więcej szczegółów na temat pożądanego kontekstu, wyniku, długości, formatu, stylu itp. Poprawi to zarówno jakość, jak i spójność odpowiedzi. Zapisuj przepisy w szablonach wielokrotnego użytku.                                                  |
| Bądź opisowy, używaj przykładów  | Modele mogą lepiej reagować na podejście "pokaż i opowiedz". Zacznij od podejścia `zero-shot`, w którym podajesz instrukcję (ale bez przykładów), a następnie spróbuj `few-shot` jako udoskonalenie, dostarczając kilka przykładów pożądanego wyniku. Używaj analogii. |
| Używaj wskazówek do rozpoczęcia  | Skieruj model w stronę pożądanego wyniku, podając mu kilka wiodących słów lub fraz, które może wykorzystać jako punkt wyjścia do odpowiedzi.                                                                                                         |
| Powtarzaj                        | Czasami może być konieczne powtórzenie instrukcji modelowi. Podaj instrukcje przed i po głównej treści, użyj instrukcji i wskazówki itp. Iteruj i weryfikuj, aby zobaczyć, co działa.                                                                  |
| Kolejność ma znaczenie           | Kolejność, w jakiej przedstawiasz informacje modelowi, może wpłynąć na wynik, nawet w przykładach uczących, dzięki efektowi świeżości. Wypróbuj różne opcje, aby zobaczyć, co działa najlepiej.                                                          |
| Daj modelowi "wyjście"           | Daj modelowi _odpowiedź awaryjną_, którą może podać, jeśli z jakiegoś powodu nie może wykonać zadania. Może to zmniejszyć szanse na generowanie fałszywych lub wymyślonych odpowiedzi przez modele.                                                    |
|                                 |                                                                                                                                                                                                                                                       |

Jak w przypadku każdej najlepszej praktyki, pamiętaj, że _Twoje doświadczenia mogą się różnić_ w zależności od modelu, zadania i domeny. Używaj tych wskazówek jako punktu wyjścia i iteruj, aby znaleźć to, co działa najlepiej dla Ciebie. Stale oceniaj swój proces inżynierii promptów, gdy pojawiają się nowe modele i narzędzia, koncentrując się na skalowalności procesu i jakości odpowiedzi.

<!--
SZABLON LEKCJI:
Ta jednostka powinna zawierać wyzwanie kodowe, jeśli to możliwe.

WYZWANIE:
Link do Jupyter Notebook z tylko komentarzami w instrukcjach (sekcje kodu są puste).

ROZWIĄZANIE:
Link do kopii tego Notebooka z wypełnionymi i uruchomionymi promptami, pokazującymi, jak może wyglądać jeden przykład.
-->

## Zadanie

Gratulacje! Dotarłeś do końca lekcji! Czas przetestować niektóre z tych koncepcji i technik na prawdziwych przykładach!

Do naszego zadania użyjemy Jupyter Notebook z ćwiczeniami, które możesz wykonać interaktywnie. Możesz także rozszerzyć Notebook o własne komórki Markdown i kodu, aby samodzielnie eksplorować pomysły i techniki.

### Aby rozpocząć, zrób fork repozytorium, a następnie

- (Zalecane) Uruchom GitHub Codespaces
- (Alternatywnie) Sklonuj repozytorium na swoje lokalne urządzenie i użyj go z Docker Desktop
- (Alternatywnie) Otwórz Notebook w preferowanym środowisku uruchomieniowym Notebooka.

### Następnie skonfiguruj zmienne środowiskowe

- Skopiuj plik `.env.copy` w katalogu głównym repozytorium do `.env` i wypełnij wartości `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` i `AZURE_OPENAI_DEPLOYMENT`. Wróć do sekcji [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), aby dowiedzieć się jak.

### Następnie otwórz Jupyter Notebook

- Wybierz jądro uruchomieniowe. Jeśli używasz opcji 1 lub 2, po prostu wybierz domyślne jądro Python 3.10.x dostarczone przez kontener deweloperski.

Jesteś gotowy do uruchomienia ćwiczeń. Zauważ, że tutaj nie ma _dobrych i złych_ odpowiedzi - chodzi o eksplorowanie opcji metodą prób i błędów oraz budowanie intuicji, co działa w danym modelu i domenie aplikacji.

_Z tego powodu w tej lekcji nie ma segmentów z rozwiązaniami kodu. Zamiast tego Notebook będzie zawierał komórki Markdown zatytułowane "Moje rozwiązanie:", które pokazują jeden przykład wyniku dla odniesienia._

 <!--
SZABLON LEKCJI:
Zakończ sekcję podsumowaniem i zasobami do samodzielnej nauki.
-->

## Sprawdzenie wiedzy

Który z poniższych promptów jest dobry, zgodnie z rozsądnymi najlepszymi praktykami?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90 zaparkowanego przy klifie z zachodzącym słońcem
3. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90

Odpowiedź: 2, to najlepszy prompt, ponieważ dostarcza szczegółów na temat "czego" i wchodzi w szczegóły (nie tylko dowolny samochód, ale konkretną markę i model) oraz opisuje ogólne otoczenie. 3 jest następny w kolejności, ponieważ również zawiera dużo opisu.

## 🚀 Wyzwanie

Spróbuj wykorzystać technikę "wskazówki" z promptem: Uzupełnij zdanie "Pokaż mi obraz czerwonego samochodu marki Volvo i ". Co odpowiada model, i jak byś to poprawił?

## Świetna robota! Kontynuuj naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach inżynierii promptów? Przejdź na [stronę kontynuacji nauki](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne świetne zasoby na ten temat.

Przejdź do Lekcji 5, gdzie przyjrzymy się [zaawansowanym technikom promptów](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku ojczystym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.