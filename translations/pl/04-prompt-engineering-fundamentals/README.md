<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:36:38+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "pl"
}
-->
# Podstawy inżynierii promptów

## Wprowadzenie
Ten moduł obejmuje podstawowe pojęcia i techniki tworzenia skutecznych promptów w modelach generatywnej AI. Sposób, w jaki napiszesz swój prompt do LLM, również ma znaczenie. Starannie opracowany prompt może zapewnić lepszą jakość odpowiedzi. Ale co dokładnie oznaczają terminy takie jak _prompt_ i _inżynieria promptów_? I jak poprawić _input_ promptu, który wysyłam do LLM? To są pytania, na które spróbujemy odpowiedzieć w tym rozdziale i następnym.

_Generatywna AI_ jest zdolna do tworzenia nowej treści (np. tekstu, obrazów, dźwięku, kodu itp.) w odpowiedzi na żądania użytkownika. Osiąga to dzięki _Large Language Models_, takim jak seria GPT ("Generative Pre-trained Transformer") od OpenAI, które są szkolone do korzystania z języka naturalnego i kodu.

Użytkownicy mogą teraz wchodzić w interakcje z tymi modelami za pomocą znanych paradygmatów, takich jak czat, bez potrzeby posiadania wiedzy technicznej czy szkolenia. Modele są oparte na _promptach_ - użytkownicy wysyłają wejście tekstowe (prompt) i otrzymują odpowiedź AI (uzupełnienie). Mogą następnie "rozmawiać z AI" iteracyjnie, w wieloetapowych rozmowach, dopracowując swój prompt, aż odpowiedź spełni ich oczekiwania.

"Prompty" stają się teraz głównym _interfejsem programowania_ dla aplikacji generatywnej AI, mówiąc modelom, co mają robić i wpływając na jakość zwracanych odpowiedzi. "Inżynieria promptów" to szybko rozwijająca się dziedzina badań, która koncentruje się na _projektowaniu i optymalizacji_ promptów, aby dostarczać spójne i jakościowe odpowiedzi na dużą skalę.

## Cele nauki

W tej lekcji dowiemy się, czym jest inżynieria promptów, dlaczego ma znaczenie i jak możemy tworzyć bardziej efektywne prompty dla danego modelu i celu aplikacji. Zrozumiemy podstawowe pojęcia i najlepsze praktyki dotyczące inżynierii promptów - i poznamy interaktywne środowisko "sandbox" Jupyter Notebooks, w którym możemy zobaczyć te pojęcia zastosowane w rzeczywistych przykładach.

Pod koniec tej lekcji będziemy w stanie:

1. Wyjaśnić, czym jest inżynieria promptów i dlaczego ma znaczenie.
2. Opisać elementy promptu i sposób ich użycia.
3. Poznać najlepsze praktyki i techniki inżynierii promptów.
4. Zastosować poznane techniki do rzeczywistych przykładów, korzystając z punktu końcowego OpenAI.

## Kluczowe terminy

Inżynieria promptów: Praktyka projektowania i doskonalenia wejść w celu kierowania modelami AI do generowania pożądanych wyników.
Tokenizacja: Proces przekształcania tekstu w mniejsze jednostki, zwane tokenami, które model może zrozumieć i przetworzyć.
LLM dostosowane do instrukcji: Duże modele językowe (LLM), które zostały dostrojone z określonymi instrukcjami w celu poprawy dokładności i trafności ich odpowiedzi.

## Sandbox nauki

Inżynieria promptów jest obecnie bardziej sztuką niż nauką. Najlepszym sposobem na poprawę naszej intuicji w tej dziedzinie jest _ćwiczenie_ i przyjęcie podejścia prób i błędów, które łączy wiedzę z zakresu aplikacji z zalecanymi technikami i optymalizacjami specyficznymi dla modelu.

Notatnik Jupyter towarzyszący tej lekcji zapewnia środowisko _sandbox_, w którym można wypróbować to, czego się uczysz - na bieżąco lub jako część wyzwania kodowego na końcu. Aby wykonać ćwiczenia, będziesz potrzebować:

1. **Klucz API Azure OpenAI** - punkt końcowy usługi dla wdrożonego LLM.
2. **Środowisko wykonawcze Pythona** - w którym można uruchomić Notatnik.
3. **Lokalne zmienne środowiskowe** - _ukończ teraz kroki [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst), aby się przygotować_.

Notatnik zawiera ćwiczenia _startowe_ - ale zachęcamy do dodawania własnych sekcji _Markdown_ (opis) i _Code_ (żądania promptów), aby wypróbować więcej przykładów lub pomysłów - i zbudować swoją intuicję w projektowaniu promptów.

## Ilustrowany przewodnik

Chcesz uzyskać ogólny obraz tego, co obejmuje ta lekcja, zanim się zagłębisz? Sprawdź ten ilustrowany przewodnik, który daje ci poczucie głównych tematów poruszanych w lekcji i kluczowych wniosków, o których powinieneś myśleć przy każdym z nich. Mapa drogowa lekcji prowadzi cię od zrozumienia podstawowych pojęć i wyzwań do ich rozwiązania za pomocą odpowiednich technik inżynierii promptów i najlepszych praktyk. Zauważ, że sekcja "Zaawansowane techniki" w tym przewodniku odnosi się do treści omówionych w _następnym_ rozdziale tego programu nauczania.

## Nasz startup

Teraz porozmawiajmy o tym, jak _ten temat_ odnosi się do naszej misji startupowej [wprowadzenia innowacji AI do edukacji](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Chcemy budować aplikacje AI wspierające _spersonalizowane uczenie się_ - więc zastanówmy się, jak różni użytkownicy naszej aplikacji mogą "projektować" prompty:

- **Administratorzy** mogą poprosić AI o _analizę danych programowych w celu zidentyfikowania luk w pokryciu_. AI może podsumować wyniki lub przedstawić je wizualnie za pomocą kodu.
- **Nauczyciele** mogą poprosić AI o _stworzenie planu lekcji dla określonej grupy odbiorców i tematu_. AI może zbudować spersonalizowany plan w określonym formacie.
- **Uczniowie** mogą poprosić AI o _pomoc w trudnym przedmiocie_. AI może teraz prowadzić uczniów za pomocą lekcji, wskazówek i przykładów dostosowanych do ich poziomu.

To tylko wierzchołek góry lodowej. Sprawdź [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - otwartą bibliotekę promptów kuratorowaną przez ekspertów edukacyjnych - aby uzyskać szersze pojęcie o możliwościach! _Spróbuj uruchomić niektóre z tych promptów w sandboxie lub użyj OpenAI Playground, aby zobaczyć, co się stanie!_

## Co to jest inżynieria promptów?

Zaczęliśmy tę lekcję od zdefiniowania **inżynierii promptów** jako procesu _projektowania i optymalizacji_ wejść tekstowych (promptów) w celu dostarczania spójnych i jakościowych odpowiedzi (uzupełnień) dla danego celu aplikacji i modelu. Możemy myśleć o tym jako o 2-etapowym procesie:

- _projektowanie_ początkowego promptu dla danego modelu i celu
- _doskonalenie_ promptu iteracyjnie w celu poprawy jakości odpowiedzi

Jest to niezbędny proces prób i błędów, który wymaga intuicji i wysiłku użytkownika, aby uzyskać optymalne wyniki. Dlaczego więc jest to ważne? Aby odpowiedzieć na to pytanie, musimy najpierw zrozumieć trzy pojęcia:

- _Tokenizacja_ = jak model "widzi" prompt
- _Podstawowe LLM_ = jak model bazowy "przetwarza" prompt
- _LLM dostosowane do instrukcji_ = jak model może teraz widzieć "zadania"

### Tokenizacja

LLM widzi prompty jako _sekwencję tokenów_, gdzie różne modele (lub wersje modelu) mogą tokenizować ten sam prompt na różne sposoby. Ponieważ LLM są szkolone na tokenach (a nie na surowym tekście), sposób, w jaki prompty są tokenizowane, ma bezpośredni wpływ na jakość generowanej odpowiedzi.

Aby uzyskać intuicję na temat działania tokenizacji, wypróbuj narzędzia takie jak [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) pokazane poniżej. Skopiuj swój prompt - i zobacz, jak jest konwertowany na tokeny, zwracając uwagę na sposób, w jaki obsługiwane są znaki białe i znaki interpunkcyjne. Zauważ, że ten przykład pokazuje starszy LLM (GPT-3) - więc wypróbowanie tego z nowszym modelem może dać inny wynik.

### Koncepcja: Modele bazowe

Gdy prompt jest tokenizowany, główną funkcją ["Podstawowego LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (lub modelu bazowego) jest przewidywanie tokenu w tej sekwencji. Ponieważ LLM są szkolone na ogromnych zestawach danych tekstowych, mają dobre wyczucie statystycznych relacji między tokenami i mogą dokonać tego przewidywania z pewnym poziomem pewności. Należy zauważyć, że nie rozumieją _znaczenia_ słów w promptu lub tokenie; po prostu widzą wzorzec, który mogą "uzupełnić" swoim następnym przewidywaniem. Mogą kontynuować przewidywanie sekwencji, aż zostaną zakończone przez interwencję użytkownika lub jakieś ustalone wcześniej warunki.

Chcesz zobaczyć, jak działa uzupełnianie oparte na promptach? Wprowadź powyższy prompt do Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) z domyślnymi ustawieniami. System jest skonfigurowany do traktowania promptów jako żądań informacji - więc powinieneś zobaczyć uzupełnienie, które zaspokaja ten kontekst.

Ale co, jeśli użytkownik chciałby zobaczyć coś konkretnego, co spełnia pewne kryteria lub cel zadania? To tutaj do gry wchodzą _LLM dostosowane do instrukcji_.

### Koncepcja: LLM dostosowane do instrukcji

[LLM dostosowane do instrukcji](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) rozpoczynają się od modelu bazowego i dostrajają go za pomocą przykładów lub par wejście/wyjście (np. wieloetapowych "wiadomości"), które mogą zawierać jasne instrukcje - a odpowiedź AI stara się te instrukcje przestrzegać.

Wykorzystuje to techniki takie jak Reinforcement Learning with Human Feedback (RLHF), które mogą szkolić model do _przestrzegania instrukcji_ i _uczenia się na podstawie opinii_, dzięki czemu generuje odpowiedzi lepiej dostosowane do praktycznych zastosowań i bardziej odpowiednie do celów użytkownika.

Wypróbujmy to - wróć do powyższego promptu, ale teraz zmień _wiadomość systemową_, aby dostarczyć następującą instrukcję jako kontekst:

> _Podsumuj dostarczoną treść dla ucznia drugiej klasy. Utrzymaj wynik w jednym akapicie z 3-5 punktami wypunktowanymi._

Zobacz, jak wynik jest teraz dostosowany do odzwierciedlenia pożądanego celu i formatu? Nauczyciel może teraz bezpośrednio użyć tej odpowiedzi w swoich slajdach na tę lekcję.

## Dlaczego potrzebujemy inżynierii promptów?

Teraz, gdy wiemy, jak prompty są przetwarzane przez LLM, porozmawiajmy o _dlaczego_ potrzebujemy inżynierii promptów. Odpowiedź leży w fakcie, że obecne LLM stawiają wiele wyzwań, które sprawiają, że _wiarygodne i spójne uzupełnienia_ są trudniejsze do osiągnięcia bez wysiłku włożonego w konstrukcję i optymalizację promptu. Na przykład:

1. **Odpowiedzi modelu są stochastyczne.** _Ten sam prompt_ prawdopodobnie da różne odpowiedzi z różnymi modelami lub wersjami modeli. Może nawet dać różne wyniki z _tym samym modelem_ w różnym czasie. _Techniki inżynierii promptów mogą pomóc nam zminimalizować te wariacje, zapewniając lepsze zabezpieczenia_.

2. **Modele mogą fabrykować odpowiedzi.** Modele są wstępnie szkolone na _dużych, ale skończonych_ zbiorach danych, co oznacza, że brakuje im wiedzy na temat koncepcji spoza tego zakresu szkoleniowego. W rezultacie mogą generować uzupełnienia, które są nieprawidłowe, wymyślone lub bezpośrednio sprzeczne z znanymi faktami. _Techniki inżynierii promptów pomagają użytkownikom identyfikować i minimalizować takie fabrykacje, np. prosząc AI o cytaty lub rozumowanie_.

3. **Możliwości modeli będą się różnić.** Nowsze modele lub generacje modeli będą miały bogatsze możliwości, ale także przyniosą unikalne dziwactwa i kompromisy w kosztach i złożoności. _Inżynieria promptów może pomóc nam w opracowaniu najlepszych praktyk i przepływów pracy, które abstrahują różnice i dostosowują się do specyficznych wymagań modelu w sposób skalowalny i bezproblemowy_.

Zobaczmy to w akcji w OpenAI lub Azure OpenAI Playground:

- Użyj tego samego promptu z różnymi wdrożeniami LLM (np. OpenAI, Azure OpenAI, Hugging Face) - czy widziałeś wariacje?
- Użyj tego samego promptu wielokrotnie z _tym samym_ wdrożeniem LLM (np. Azure OpenAI playground) - jak te wariacje się różniły?

### Przykład fabrykacji

W tym kursie używamy terminu **"fabrykacja"**, aby odnieść się do zjawiska, w którym LLM czasami generują nieprawdziwe informacje z powodu ograniczeń w swoim szkoleniu lub innych ograniczeń. Możesz również spotkać się z tym określeniem jako _"halucynacje"_ w popularnych artykułach lub pracach naukowych. Jednak zdecydowanie zalecamy używanie _"fabrykacja"_ jako terminu, aby nie przypisywać maszynie cechy ludzkiej poprzez antropomorfizację zachowania. To również wzmacnia [wytyczne dotyczące odpowiedzialnej AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) z perspektywy terminologii, usuwając terminy, które mogą być również uznawane za obraźliwe lub nieinkluzwne w niektórych kontekstach.

Chcesz zobaczyć, jak działają fabrykacje? Pomyśl o promptcie, który instruuje AI do generowania treści na temat nieistniejącego tematu (aby upewnić się, że nie znajduje się w zestawie danych szkoleniowych). Na przykład - spróbowałem tego promptu:

> **Prompt:** wygeneruj plan lekcji na temat Wojny Marsjańskiej z 2076 roku.

Wyszukiwanie w sieci pokazało mi, że istnieją fikcyjne relacje (np. seriale telewizyjne lub książki) o wojnach marsjańskich - ale żadna z 2076 roku. Zdrowy rozsądek również mówi nam, że 2076 rok jest _w przyszłości_ i dlatego nie może być związany z prawdziwym wydarzeniem.

Co się stanie, gdy uruchomimy ten prompt z różnymi dostawcami LLM?

> **Odpowiedź 1**: OpenAI Playground (GPT-35)

> **Odpowiedź 2**: Azure OpenAI Playground (GPT-35)

> **Odpowiedź 3**: : Hugging Face Chat Playground (LLama-2)

Jak się spodziewano, każdy model (lub wersja modelu) generuje nieco inne odpowiedzi dzięki stochastycznemu zachowaniu i różnicom w możliwościach modelu. Na przykład jeden model celuje w ucznia ósmej klasy, podczas gdy drugi zakłada ucznia szkoły średniej. Ale wszystkie trzy modele wygenerowały odpowied
Ostateczna wartość szablonów tkwi w zdolności do tworzenia i publikowania _bibliotek promptów_ dla pionowych domen aplikacji - gdzie szablon promptu jest teraz _optymalizowany_ tak, aby odzwierciedlać kontekst specyficzny dla aplikacji lub przykłady, które czynią odpowiedzi bardziej istotnymi i dokładnymi dla docelowej grupy użytkowników. Repozytorium [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) jest doskonałym przykładem tego podejścia, gromadząc bibliotekę promptów dla domeny edukacyjnej z naciskiem na kluczowe cele, takie jak planowanie lekcji, projektowanie programu nauczania, korepetycje dla uczniów itp.

## Wspierająca treść

Jeśli myślimy o konstrukcji promptu jako mającej instrukcję (zadanie) i cel (główna treść), to _treść wtórna_ jest jak dodatkowy kontekst, który dostarczamy, aby **w jakiś sposób wpłynąć na wynik**. Mogą to być parametry dostrajania, instrukcje formatowania, taksonomie tematów itp., które mogą pomóc modelowi _dostosować_ swoją odpowiedź do pożądanych celów lub oczekiwań użytkownika.

Na przykład: Mając katalog kursów z rozbudowanymi metadanymi (nazwa, opis, poziom, tagi metadanych, instruktor itp.) na temat wszystkich dostępnych kursów w programie nauczania:

- możemy zdefiniować instrukcję "podsumuj katalog kursów na jesień 2023"
- możemy użyć głównej treści, aby dostarczyć kilka przykładów pożądanego wyniku
- możemy użyć treści wtórnej, aby zidentyfikować 5 najważniejszych "tagów" zainteresowania.

Teraz model może dostarczyć podsumowanie w formacie pokazanym przez kilka przykładów - ale jeśli wynik ma wiele tagów, może priorytetować 5 tagów zidentyfikowanych w treści wtórnej.

---

## Najlepsze praktyki w tworzeniu promptów

Teraz, gdy wiemy, jak można _konstruować_ prompty, możemy zacząć myśleć o tym, jak je _projektować_, aby odzwierciedlały najlepsze praktyki. Możemy myśleć o tym w dwóch częściach - posiadanie odpowiedniego _nastawienia_ i stosowanie odpowiednich _technik_.

### Nastawienie do inżynierii promptów

Inżynieria promptów to proces prób i błędów, więc pamiętaj o trzech szerokich czynnikach przewodnich:

1. **Zrozumienie domeny ma znaczenie.** Dokładność i trafność odpowiedzi jest funkcją _domeny_, w której działa dana aplikacja lub użytkownik. Zastosuj swoją intuicję i wiedzę domenową, aby **dostosować techniki** dalej. Na przykład, zdefiniuj _osobowości specyficzne dla domeny_ w swoich promptach systemowych lub używaj _szablonów specyficznych dla domeny_ w swoich promptach użytkownika. Dostarczaj treści wtórne, które odzwierciedlają konteksty specyficzne dla domeny, lub używaj _wskazówek i przykładów specyficznych dla domeny_, aby kierować model w stronę znanych wzorców użycia.

2. **Zrozumienie modelu ma znaczenie.** Wiemy, że modele są z natury stochastyczne. Ale implementacje modeli mogą również różnić się pod względem zbioru danych treningowych, które wykorzystują (wiedza wstępnie wytrenowana), możliwości, które oferują (np. za pośrednictwem API lub SDK) oraz rodzaju treści, do których są zoptymalizowane (np. kod vs. obrazy vs. tekst). Zrozum mocne i słabe strony modelu, którego używasz, i wykorzystaj tę wiedzę, aby _priorytetyzować zadania_ lub budować _dostosowane szablony_, które są zoptymalizowane dla możliwości modelu.

3. **Iteracja i walidacja ma znaczenie.** Modele szybko się rozwijają, podobnie jak techniki inżynierii promptów. Jako ekspert domenowy możesz mieć inne konteksty lub kryteria _dla swojej_ specyficznej aplikacji, które mogą nie mieć zastosowania do szerszej społeczności. Używaj narzędzi i technik inżynierii promptów, aby "rozpocząć" konstrukcję promptów, a następnie iteruj i waliduj wyniki, korzystając z własnej intuicji i wiedzy domenowej. Zapisuj swoje spostrzeżenia i twórz **bazę wiedzy** (np. biblioteki promptów), która może być używana jako nowa podstawa przez innych, dla szybszych iteracji w przyszłości.

## Najlepsze praktyki

Przyjrzyjmy się teraz powszechnym najlepszym praktykom, które są zalecane przez praktyków [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) i [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Co                                 | Dlaczego                                                                                                                                                                                                                                        |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Oceń najnowsze modele.             | Nowe generacje modeli prawdopodobnie będą miały ulepszone funkcje i jakość - ale mogą także generować wyższe koszty. Oceń je pod kątem wpływu, a następnie podejmij decyzje migracyjne.                                                         |
| Oddziel instrukcje i kontekst      | Sprawdź, czy twój model/dostawca definiuje _rozgraniczenia_, aby wyraźniej odróżnić instrukcje, treść główną i wtórną. To może pomóc modelom dokładniej przypisywać wagi do tokenów.                                                              |
| Bądź precyzyjny i jasny            | Podaj więcej szczegółów na temat pożądanego kontekstu, wyniku, długości, formatu, stylu itp. To poprawi zarówno jakość, jak i spójność odpowiedzi. Zapisz przepisy w szablonach do ponownego użycia.                                          |
| Bądź opisowy, używaj przykładów    | Modele mogą lepiej reagować na podejście "pokaż i opowiedz". Zacznij od `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Wybierz jądro runtime. Jeśli korzystasz z opcji 1 lub 2, po prostu wybierz domyślne jądro Python 3.10.x dostarczone przez kontener deweloperski.

Jesteś gotowy do uruchomienia ćwiczeń. Zauważ, że tutaj nie ma _dobrych i złych_ odpowiedzi - po prostu eksplorowanie opcji metodą prób i błędów oraz budowanie intuicji na temat tego, co działa dla danego modelu i domeny aplikacji.

_Z tego powodu w tej lekcji nie ma segmentów z rozwiązaniami kodu. Zamiast tego Notebook będzie miał komórki Markdown zatytułowane "Moje rozwiązanie:", które pokazują jeden przykład wyniku jako odniesienie._

## Sprawdzenie wiedzy

Który z poniższych to dobry prompt zgodnie z rozsądnymi najlepszymi praktykami?

1. Pokaż mi obraz czerwonego samochodu
2. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90 zaparkowanego przy klifie z zachodzącym słońcem
3. Pokaż mi obraz czerwonego samochodu marki Volvo i modelu XC90

A: 2, to najlepszy prompt, ponieważ dostarcza szczegóły na temat "czego" i przechodzi do szczegółów (nie tylko jakikolwiek samochód, ale konkretną markę i model) i opisuje ogólne otoczenie. 3 jest następny najlepszy, ponieważ również zawiera wiele opisów.

## 🚀 Wyzwanie

Zobacz, czy możesz wykorzystać technikę "wskazówki" z promptem: Uzupełnij zdanie "Pokaż mi obraz czerwonego samochodu marki Volvo i ". Jak na to odpowiada i jak byś to poprawił?

## Świetna robota! Kontynuuj naukę

Chcesz dowiedzieć się więcej o różnych koncepcjach inżynierii promptów? Przejdź na [stronę kontynuacji nauki](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby znaleźć inne świetne zasoby na ten temat.

Przejdź do Lekcji 5, gdzie przyjrzymy się [zaawansowanym technikom promptów](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku ojczystym powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.