<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T09:37:05+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pl"
}
-->
# Podstawy Inżynierii Promptów

## Wprowadzenie
Ten moduł obejmuje kluczowe pojęcia i techniki tworzenia skutecznych promptów w modelach generatywnej AI. Sposób, w jaki piszesz prompt do LLM, ma znaczenie. Starannie opracowany prompt może przynieść lepszą jakość odpowiedzi. Ale co dokładnie oznaczają terminy takie jak _prompt_ i _inżynieria promptów_? I jak mogę poprawić _wejście promptu_, które wysyłam do LLM? To są pytania, na które spróbujemy odpowiedzieć w tym rozdziale i następnym.

_Generatywna AI_ potrafi tworzyć nową zawartość (np. tekst, obrazy, dźwięki, kod itp.) w odpowiedzi na zapytania użytkowników. Osiąga to za pomocą _Modeli Językowych Wielkiej Skali_ takich jak seria GPT ("Generative Pre-trained Transformer") firmy OpenAI, które są trenowane do używania języka naturalnego i kodu.

Użytkownicy mogą teraz wchodzić w interakcje z tymi modelami za pomocą znanych paradygmatów, takich jak czat, bez potrzeby posiadania wiedzy technicznej czy szkolenia. Modele są _oparte na promptach_ - użytkownicy wysyłają wejście tekstowe (prompt) i otrzymują odpowiedź AI (uzupełnienie). Mogą następnie "rozmawiać z AI" w sposób iteracyjny, w wieloetapowych konwersacjach, udoskonalając swój prompt, aż odpowiedź spełni ich oczekiwania.

"Prompty" stają się teraz podstawowym _interfejsem programowania_ dla aplikacji generatywnej AI, wskazując modelom, co mają robić i wpływając na jakość zwracanych odpowiedzi. "Inżynieria Promptów" to szybko rozwijająca się dziedzina badań, która koncentruje się na _projektowaniu i optymalizacji_ promptów w celu dostarczania spójnych i wysokiej jakości odpowiedzi na dużą skalę.

## Cele Nauki

W tej lekcji dowiemy się, czym jest Inżynieria Promptów, dlaczego ma znaczenie i jak możemy tworzyć bardziej efektywne prompty dla danego modelu i celu aplikacji. Zrozumiemy podstawowe pojęcia i najlepsze praktyki w inżynierii promptów - oraz poznamy interaktywne środowisko "piaskownicy" Jupyter Notebooks, w którym możemy zobaczyć zastosowanie tych pojęć w praktycznych przykładach.

Pod koniec tej lekcji będziemy w stanie:

1. Wyjaśnić, czym jest inżynieria promptów i dlaczego jest ważna.
2. Opisać składniki promptu i sposób ich użycia.
3. Poznać najlepsze praktyki i techniki inżynierii promptów.
4. Zastosować poznane techniki do rzeczywistych przykładów, używając punktu końcowego OpenAI.

## Kluczowe Pojęcia

Inżynieria Promptów: Praktyka projektowania i udoskonalania wejść, aby skierować modele AI do generowania pożądanych wyników.
Tokenizacja: Proces przekształcania tekstu w mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetworzyć.
LLM-y dostosowane do instrukcji: Modele Językowe Wielkiej Skali (LLM), które zostały dostosowane do konkretnych instrukcji w celu poprawy dokładności i trafności ich odpowiedzi.

## Piaskownica Nauki

Inżynieria promptów jest obecnie bardziej sztuką niż nauką. Najlepszym sposobem na poprawę naszej intuicji w tym zakresie jest _praktyka_ i przyjęcie podejścia prób i błędów, które łączy wiedzę dziedzinową z zalecanymi technikami i optymalizacjami specyficznymi dla modelu.

Jupyter Notebook towarzyszący tej lekcji zapewnia środowisko _piaskownicy_, w którym możesz wypróbować to, czego się nauczysz - na bieżąco lub jako część wyzwania kodowego na końcu. Aby wykonać ćwiczenia, będziesz potrzebować:

1. **Klucz API Azure OpenAI** - punkt końcowy usługi dla wdrożonego LLM.
2. **Środowisko wykonawcze Pythona** - w którym można uruchomić Notebook.
3. **Lokalne zmienne środowiskowe** - _ukończ kroki [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst), aby się przygotować_.

Notebook zawiera ćwiczenia _startowe_ - ale zachęcamy do dodania własnych sekcji _Markdown_ (opis) i _Code_ (żądania promptów), aby wypróbować więcej przykładów lub pomysłów - i budować swoją intuicję dotyczącą projektowania promptów.

## Przewodnik Ilustrowany

Chcesz zobaczyć ogólny obraz tego, co obejmuje ta lekcja, zanim się zagłębisz? Sprawdź ten przewodnik ilustrowany, który daje ci wyobrażenie o głównych tematach omówionych i kluczowych wnioskach, które powinieneś przemyśleć w każdym z nich. Plan lekcji prowadzi cię od zrozumienia podstawowych pojęć i wyzwań do ich rozwiązania za pomocą odpowiednich technik inżynierii promptów i najlepszych praktyk. Zauważ, że sekcja "Zaawansowane Techniki" w tym przewodniku odnosi się do treści omówionych w _następnym_ rozdziale tego programu nauczania.

## Nasz Startup

Teraz porozmawiajmy o tym, jak _ten temat_ odnosi się do naszej misji startupowej, aby [przynieść innowacje AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje AI wspomagające _spersonalizowane uczenie się_ - więc zastanówmy się, jak różni użytkownicy naszej aplikacji mogą "projektować" prompty:

- **Administratorzy** mogą poprosić AI o _analizę danych programu nauczania w celu zidentyfikowania luk w pokryciu_. AI może podsumować wyniki lub przedstawić je w formie wizualnej za pomocą kodu.
- **Nauczyciele** mogą poprosić AI o _wygenerowanie planu lekcji dla docelowej grupy odbiorców i tematu_. AI może zbudować spersonalizowany plan w określonym formacie.
- **Studenci** mogą poprosić AI o _nauczanie ich trudnego przedmiotu_. AI może teraz prowadzić uczniów za pomocą lekcji, wskazówek i przykładów dostosowanych do ich poziomu.

To tylko wierzchołek góry lodowej. Sprawdź [Prompty dla Edukacji](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otwartą bibliotekę promptów kuratorowaną przez ekspertów edukacyjnych - aby uzyskać szersze pojęcie o możliwościach! _Spróbuj uruchomić niektóre z tych promptów w piaskownicy lub używając OpenAI Playground, aby zobaczyć, co się stanie!_

## Co to jest Inżynieria Promptów?

Zaczęliśmy tę lekcję od zdefiniowania **Inżynierii Promptów** jako procesu _projektowania i optymalizacji_ tekstowych wejść (promptów) w celu dostarczania spójnych i wysokiej jakości odpowiedzi (uzupełnień) dla danego celu aplikacji i modelu. Możemy myśleć o tym jako o procesie dwustopniowym:

- _projektowanie_ początkowego promptu dla danego modelu i celu
- _udoskonalanie_ promptu iteracyjnie w celu poprawy jakości odpowiedzi

Jest to koniecznie proces prób i błędów, który wymaga intuicji użytkownika i wysiłku, aby osiągnąć optymalne wyniki. Dlaczego jest to ważne? Aby odpowiedzieć na to pytanie, musimy najpierw zrozumieć trzy pojęcia:

- _Tokenizacja_ = jak model "widzi" prompt
- _Podstawowe LLM-y_ = jak model bazowy "przetwarza" prompt
- _LLM-y dostosowane do instrukcji_ = jak model może teraz widzieć "zadania"

### Tokenizacja

LLM widzi prompty jako _sekwencję tokenów_, gdzie różne modele (lub wersje modelu) mogą tokenizować ten sam prompt na różne sposoby. Ponieważ LLM-y są trenowane na tokenach (a nie na surowym tekście), sposób, w jaki prompty są tokenizowane, ma bezpośredni wpływ na jakość generowanej odpowiedzi.

Aby uzyskać intuicję na temat tego, jak działa tokenizacja, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) pokazane poniżej. Skopiuj swój prompt - i zobacz, jak to zostaje przekształcone w tokeny, zwracając uwagę na to, jak traktowane są znaki białe i znaki interpunkcyjne. Zauważ, że ten przykład pokazuje starszy LLM (GPT-3) - więc wypróbowanie tego z nowszym modelem może dać inny wynik.

### Pojęcie: Modele Bazowe

Gdy prompt zostanie tokenizowany, główną funkcją ["Podstawowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (lub modelu bazowego) jest przewidywanie tokenu w tej sekwencji. Ponieważ LLM-y są trenowane na ogromnych zbiorach danych tekstowych, mają dobrą znajomość statystycznych relacji między tokenami i mogą dokonać tego przewidywania z pewnym stopniem pewności. Zauważ, że nie rozumieją _znaczenia_ słów w promptach czy tokenach; widzą tylko wzór, który mogą "uzupełnić" swoją następną przewidywaną wartością. Mogą kontynuować przewidywanie sekwencji aż do przerwania przez interwencję użytkownika lub jakąś wcześniej ustaloną warunek.

Chcesz zobaczyć, jak działa uzupełnianie oparte na promptach? Wprowadź powyższy prompt do [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) w Azure OpenAI Studio z domyślnymi ustawieniami. System jest skonfigurowany do traktowania promptów jako żądań informacji - więc powinieneś zobaczyć uzupełnienie, które spełnia ten kontekst.

Ale co, jeśli użytkownik chciałby zobaczyć coś konkretnego, co spełnia pewne kryteria lub cel zadania? Tutaj wkraczają _LLM-y dostosowane do instrukcji_.

### Pojęcie: LLM-y Dostosowane do Instrukcji

[LLM Dostosowany do Instrukcji](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) zaczyna się od modelu bazowego i dostraja go za pomocą przykładów lub par wejście/wyjście (np. wieloetapowych "wiadomości"), które mogą zawierać jasne instrukcje - a odpowiedź AI próbuje podążać za tą instrukcją.

Używa to technik takich jak Uczenie się przez Wzmocnienie z Informacją Zwrotną od Człowieka (RLHF), które mogą trenować model do _podążania za instrukcjami_ i _uczenia się na podstawie informacji zwrotnej_, aby generował odpowiedzi lepiej dostosowane do praktycznych zastosowań i bardziej trafne dla celów użytkownika.

Spróbujmy - odwiedź ponownie powyższy prompt, ale teraz zmień _wiadomość systemową_, aby dostarczyć następującą instrukcję jako kontekst:

> _Podsumuj treść, którą Ci dostarczono, dla ucznia drugiej klasy. Zachowaj wynik w jednym akapicie z 3-5 punktami._

Zobacz, jak wynik jest teraz dostosowany, aby odzwierciedlać pożądany cel i format? Nauczyciel może teraz bezpośrednio użyć tej odpowiedzi w swoich slajdach dla tej klasy.

## Dlaczego potrzebujemy Inżynierii Promptów?

Teraz, gdy wiemy, jak prompty są przetwarzane przez LLM-y, porozmawiajmy o _dlaczego_ potrzebujemy inżynierii promptów. Odpowiedź leży w fakcie, że obecne LLM-y stawiają szereg wyzwań, które sprawiają, że _wiarygodne i spójne uzupełnienia_ są trudniejsze do osiągnięcia bez włożenia wysiłku w konstrukcję i optymalizację promptów. Na przykład:

1. **Odpowiedzi modeli są stochastyczne.** _Ten sam prompt_ prawdopodobnie wygeneruje różne odpowiedzi w różnych modelach lub wersjach modeli. Może również generować różne wyniki z _tym samym modelem_ w różnych momentach. _Techniki inżynierii promptów mogą pomóc nam zminimalizować te wariacje, zapewniając lepsze ograniczenia_.

1. **Modele mogą fabrykować odpowiedzi.** Modele są wstępnie trenowane na _dużych, ale skończonych_ zbiorach danych, co oznacza, że brakuje im wiedzy na temat pojęć spoza tego zakresu treningowego. W rezultacie mogą generować uzupełnienia, które są niedokładne, fikcyjne lub bezpośrednio sprzeczne z znanymi faktami. _Techniki inżynierii promptów pomagają użytkownikom zidentyfikować i zminimalizować takie fabrykacje, np. prosząc AI o cytaty lub rozumowanie_.

1. **Zdolności modeli będą się różnić.** Nowsze modele lub generacje modeli będą miały bogatsze zdolności, ale także wprowadzą unikalne cechy i kompromisy w zakresie kosztów i złożoności. _Inżynieria promptów może pomóc nam opracować najlepsze praktyki i przepływy pracy, które abstrahują różnice i dostosowują się do wymagań specyficznych dla modelu w skalowalny, bezproblemowy sposób_.

Zobaczmy to w działaniu w OpenAI lub Azure OpenAI Playground:

- Użyj tego samego promptu z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) - czy zauważyłeś różnice?
- Użyj tego samego promptu wielokrotnie z _tym samym_ wdrożeniem LLM (np. Azure OpenAI playground) - jak te różnice się różniły?

### Przykład Fabrykacji

W tym kursie używamy terminu **"fabrykacja"** do odniesienia się do zjawiska, w którym LLM-y czasami generują faktycznie niepoprawne informacje z powodu ograniczeń w ich treningu lub innych ograniczeń. Możesz również słyszeć o tym jako _"halucynacje"_ w popularnych artykułach lub pracach badawczych. Jednak zdecydowanie zalecamy używanie terminu _"fabrykacja"_, aby nie przypisywać zachowaniu cechy ludzkiej, przypisując wynikowi generowanemu przez maszynę cechę przypisywaną człowiekowi. To także wzmacnia [Zasady Odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z perspektywy terminologii, eliminując terminy, które mogą być uznane za obraźliwe lub nieinkluzywne w niektórych kontekstach.

Chcesz zobaczyć, jak działają fabrykacje? Pomyśl o promptcie, który instruuje AI, aby wygenerowała treść na temat nieistniejącego tematu (aby upewnić się, że nie znajduje się w zbiorze danych treningowych). Na przykład - spróbowałem tego promptu:

> **Prompt:** wygeneruj plan lekcji na temat Wojny Marsjańskiej z 2076 roku.

Wyszukiwanie w sieci pokazało mi, że istnieją fikcyjne opowieści (np. seriale telewizyjne lub książki) o wojnach marsjańskich - ale żadna w 2076 roku. Zdrowy rozsądek również mówi nam, że 2076 rok jest _w przyszłości_ i dlatego nie może być związany z prawdziwym wydarzeniem.

Więc co się dzieje, gdy uruchamiamy ten prompt z różnymi dostawcami LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

> **Odpowiedź 3**: : Hugging Face Chat Playground (LLama-2)

Jak można się spodziewać, każdy model (lub wersja modelu) generuje nieco inne odpowiedzi dzięki zachowaniu st
Ostateczna wartość szablonów leży w możliwości tworzenia i publikowania _bibliotek promptów_ dla pionowych domen aplikacji - gdzie szablon promptu jest teraz _optymalizowany_, aby odzwierciedlać kontekst aplikacji lub przykłady, które sprawiają, że odpowiedzi są bardziej trafne i dokładne dla docelowej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest doskonałym przykładem tego podejścia, zbierając bibliotekę promptów dla domeny edukacyjnej z naciskiem na kluczowe cele, takie jak planowanie lekcji, projektowanie programów nauczania, korepetycje dla studentów itd.

## Wspierająca treść

Jeśli myślimy o konstruowaniu promptów jako o posiadaniu instrukcji (zadania) i celu (głównej treści), to _treść wtórna_ jest jak dodatkowy kontekst, który dostarczamy, aby **wpłynąć na wynik w jakiś sposób**. Może to być dostrajanie parametrów, instrukcje formatowania, taksonomie tematów itd., które mogą pomóc modelowi _dostosować_ swoją odpowiedź do oczekiwanych celów użytkownika.

Na przykład: Mając katalog kursów z rozbudowanymi metadanymi (nazwa, opis, poziom, tagi metadanych, instruktor itd.) dotyczącymi wszystkich dostępnych kursów w programie nauczania:

- możemy zdefiniować instrukcję "podsumuj katalog kursów na jesień 2023"
- możemy użyć głównej treści, aby dostarczyć kilka przykładów pożądanego wyniku
- możemy użyć treści wtórnej, aby zidentyfikować 5 najważniejszych "tagów" zainteresowania.

Teraz model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów - ale jeśli wynik ma wiele tagów, może priorytetyzować 5 tagów zidentyfikowanych w treści wtórnej.

---

<!--
SZABLON LEKCJI:
Ta jednostka powinna obejmować podstawową koncepcję #1.
Wzmocnij koncepcję przykładami i odniesieniami.

KONCEPCJA #3:
Techniki inżynierii promptów.
Jakie są podstawowe techniki inżynierii promptów?
Zilustruj to za pomocą ćwiczeń.
-->

## Najlepsze praktyki w tworzeniu promptów

Teraz, gdy wiemy, jak można _konstruować_ prompty, możemy zacząć myśleć o tym, jak je _projektować_, aby odzwierciedlały najlepsze praktyki. Możemy rozważyć to w dwóch częściach - posiadanie odpowiedniego _nastawienia_ i zastosowanie odpowiednich _technik_.

### Nastawienie do inżynierii promptów

Inżynieria promptów to proces prób i błędów, więc miej na uwadze trzy szerokie czynniki przewodnie:

1. **Zrozumienie domeny ma znaczenie.** Dokładność i trafność odpowiedzi jest funkcją _domeny_, w której działa aplikacja lub użytkownik. Zastosuj swoją intuicję i wiedzę domenową, aby **dostosować techniki** dalej. Na przykład, zdefiniuj _osobowości specyficzne dla domeny_ w swoich promptach systemowych lub użyj _szablonów specyficznych dla domeny_ w swoich promptach użytkownika. Dostarcz treść wtórną, która odzwierciedla konteksty specyficzne dla domeny lub użyj _wskazówek i przykładów specyficznych dla domeny_, aby poprowadzić model w kierunku znanych wzorców użytkowania.

2. **Zrozumienie modelu ma znaczenie.** Wiemy, że modele są z natury stochastyczne. Ale implementacje modeli mogą również różnić się pod względem używanego zestawu danych treningowych (wiedza wstępnie trenowana), możliwości, które oferują (np. przez API lub SDK) i rodzaju treści, do których są optymalizowane (np. kod vs. obrazy vs. tekst). Zrozumienie mocnych stron i ograniczeń modelu, którego używasz, i użycie tej wiedzy do _priorytetyzacji zadań_ lub budowania _dostosowanych szablonów_, które są optymalizowane pod kątem możliwości modelu.

3. **Iteracja i walidacja ma znaczenie.** Modele szybko się rozwijają, podobnie jak techniki inżynierii promptów. Jako ekspert domeny, możesz mieć inne konteksty lub kryteria _swojej_ specyficznej aplikacji, które mogą nie mieć zastosowania do szerszej społeczności. Użyj narzędzi i technik inżynierii promptów, aby "rozpocząć" konstrukcję promptów, a następnie iteruj i waliduj wyniki, używając swojej intuicji i wiedzy domenowej. Zapisuj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), która może być używana jako nowa baza przez innych, dla szybszych iteracji w przyszłości.

## Najlepsze praktyki

Teraz przyjrzyjmy się powszechnym najlepszym praktykom zalecanym przez praktyków [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                               | Dlaczego                                                                                                                                                                                                                                               |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Oceń najnowsze modele.           | Nowe generacje modeli prawdopodobnie mają ulepszone funkcje i jakość - ale mogą również generować wyższe koszty. Oceń je pod kątem wpływu, a następnie podejmij decyzje o migracji.                                                                     |
| Oddziel instrukcje i kontekst    | Sprawdź, czy twój model/dostawca definiuje _oddzielacze_, aby wyraźniej rozróżniać instrukcje, treść główną i wtórną. To może pomóc modelom przypisywać wagi bardziej dokładnie do tokenów.                                                              |
| Bądź konkretny i jasny           | Podaj więcej szczegółów dotyczących pożądanego kontekstu, wyniku, długości, formatu, stylu itd. To poprawi zarówno jakość, jak i spójność odpowiedzi. Zapisz przepisy w szablonach do ponownego użycia.                                                  |
| Bądź opisowy, używaj przykładów  | Modele mogą lepiej reagować na podejście "pokaż i powiedz". Zacznij od `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` wartości. Wróć do sekcji [Learning Sandbox](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), aby dowiedzieć się więcej.

### Następnie otwórz Jupyter Notebook

- Wybierz jądro runtime. Jeśli używasz opcji 1 lub 2, po prostu wybierz domyślne jądro Python 3.10.x dostarczone przez kontener deweloperski.

Jesteś gotowy do wykonania ćwiczeń. Zauważ, że nie ma tutaj _dobrych i złych_ odpowiedzi - po prostu eksplorowanie opcji metodą prób i błędów i budowanie intuicji dotyczącej tego, co działa dla danego modelu i domeny aplikacji.

_Z tego powodu w tej lekcji nie ma segmentów z rozwiązaniami kodu. Zamiast tego, Notebook będzie miał komórki Markdown zatytułowane "Moje rozwiązanie:", które pokazują jeden przykładowy wynik jako odniesienie._

 <!--
SZABLON LEKCJI:
Zakończ sekcję podsumowaniem i zasobami do samodzielnego uczenia się.
-->

## Sprawdzenie wiedzy

Który z poniższych jest dobrym promptem, zgodnym z rozsądnymi najlepszymi praktykami?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90 zaparkowanego przy klifie z zachodzącym słońcem
3. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90

A: 2, to najlepszy prompt, ponieważ dostarcza szczegółów na temat "czego" i wchodzi w szczegóły (nie tylko jakikolwiek samochód, ale konkretną markę i model) oraz opisuje ogólną scenerię. 3 jest następny najlepszy, ponieważ również zawiera wiele opisów.

## 🚀 Wyzwanie

Zobacz, czy możesz wykorzystać technikę "wskazówki" z promptem: Ukończ zdanie "Pokaż mi obraz czerwonego samochodu marki Volvo i ". Jak na to odpowiada, i jak byś to poprawił?

## Świetna praca! Kontynuuj naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach inżynierii promptów? Przejdź do [strony kontynuowanej nauki](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne świetne zasoby na ten temat.

Przejdź do Lekcji 5, gdzie przyjrzymy się [zaawansowanym technikom promptów](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za autorytatywne źródło. W przypadku krytycznych informacji zalecane jest profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.