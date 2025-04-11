[![Dostrajanie LLM](../../img/18-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson18-gh?WT.mc_id=academic-105485-koreyst)

# Dostrajanie Twojego LLM

Używanie dużych modeli językowych do tworzenia aplikacji generatywnej AI wiąże się z nowymi wyzwaniami. Kluczową kwestią jest zapewnienie jakości odpowiedzi (dokładności i trafności) w treści generowanej przez model dla danego żądania użytkownika. W poprzednich lekcjach omawialiśmy techniki takie jak inżynieria promptów i retrieval-augmented generation, które próbują rozwiązać problem poprzez _modyfikację danych wejściowych promptu_ do istniejącego modelu.

W dzisiejszej lekcji omawiamy trzecią technikę, **dostrajanie (fine-tuning)**, która próbuje sprostać wyzwaniu poprzez _ponowne trenowanie samego modelu_ z dodatkowymi danymi. Zagłębmy się w szczegóły.

## Cele Nauki

Ta lekcja wprowadza pojęcie dostrajania dla wstępnie wytrenowanych modeli językowych, bada korzyści i wyzwania tego podejścia oraz dostarcza wskazówek, kiedy i jak używać dostrajania do poprawy wydajności Twoich modeli generatywnej AI.

Po ukończeniu tej lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest dostrajanie dla modeli językowych?
- Kiedy i dlaczego dostrajanie jest przydatne?
- Jak mogę dostroić wstępnie wytrenowany model?
- Jakie są ograniczenia dostrajania?

Gotowy? Zaczynajmy.

## Ilustrowany Przewodnik

Chcesz zobaczyć ogólny obraz tego, co omówimy, zanim zagłębimy się w temat? Sprawdź ten ilustrowany przewodnik, który opisuje podróż edukacyjną tej lekcji - od nauki podstawowych koncepcji i motywacji do dostrajania, po zrozumienie procesu i najlepszych praktyk wykonywania zadania dostrajania. To fascynujący temat do eksploracji, więc nie zapomnij sprawdzić strony [Zasoby](./RESOURCES.md?WT.mc_id=academic-105485-koreyst), aby znaleźć dodatkowe linki wspierające Twoją samodzielną podróż edukacyjną!

![Ilustrowany Przewodnik po Dostrajaniu Modeli Językowych](../../img/18-fine-tuning-sketchnote.png?WT.mc_id=academic-105485-koreyst)

## Czym jest dostrajanie dla modeli językowych?

Z definicji, duże modele językowe są _wstępnie trenowane_ na dużych ilościach tekstu pochodzącego z różnorodnych źródeł, w tym z internetu. Jak nauczyliśmy się w poprzednich lekcjach, potrzebujemy technik takich jak _inżynieria promptów_ i _retrieval-augmented generation_, aby poprawić jakość odpowiedzi modelu na pytania użytkownika ("prompty").

Popularna technika inżynierii promptów polega na dawaniu modelowi więcej wskazówek na temat tego, czego oczekuje się w odpowiedzi, albo poprzez dostarczanie _instrukcji_ (jawne wskazówki), albo _podawanie mu kilku przykładów_ (niejawne wskazówki). Nazywa się to _uczeniem few-shot_, ale ma ono dwa ograniczenia:

- Limity tokenów modelu mogą ograniczać liczbę przykładów, które możesz podać, i ograniczać skuteczność.
- Koszty tokenów modelu mogą sprawić, że dodawanie przykładów do każdego promptu będzie drogie i ograniczy elastyczność.

Dostrajanie jest powszechną praktyką w systemach uczenia maszynowego, gdzie bierzemy wstępnie wytrenowany model i ponownie go trenujemy z nowymi danymi, aby poprawić jego wydajność w konkretnym zadaniu. W kontekście modeli językowych możemy dostroić wstępnie wytrenowany model _za pomocą wyselekcjonowanego zestawu przykładów dla danego zadania lub domeny aplikacji_, aby stworzyć **model niestandardowy**, który może być bardziej dokładny i trafny dla tego konkretnego zadania lub domeny. Dodatkową korzyścią z dostrajania jest to, że może ono również zmniejszyć liczbę przykładów potrzebnych do uczenia few-shot - redukując zużycie tokenów i związane z tym koszty.

## Kiedy i dlaczego powinniśmy dostrajać modele?

W _tym_ kontekście, gdy mówimy o dostrajaniu, mamy na myśli **nadzorowane** dostrajanie, gdzie ponowne trenowanie odbywa się poprzez **dodanie nowych danych**, które nie były częścią oryginalnego zbioru danych treningowych. Różni się to od podejścia nienadzorowanego dostrajania, gdzie model jest ponownie trenowany na oryginalnych danych, ale z innymi hiperparametrami.

Kluczową rzeczą do zapamiętania jest to, że dostrajanie jest zaawansowaną techniką, która wymaga pewnego poziomu wiedzy, aby uzyskać pożądane rezultaty. Jeśli zostanie wykonane nieprawidłowo, może nie przynieść oczekiwanych ulepszeń, a nawet może pogorszyć wydajność modelu dla Twojej docelowej domeny.

Więc zanim dowiesz się, "jak" dostrajać modele językowe, musisz wiedzieć, "dlaczego" powinieneś wybrać tę drogę i "kiedy" rozpocząć proces dostrajania. Zacznij od zadania sobie tych pytań:

- **Przypadek użycia**: Jaki jest Twój _przypadek użycia_ dla dostrajania? Jaki aspekt obecnego wstępnie wytrenowanego modelu chcesz poprawić?
- **Alternatywy**: Czy próbowałeś _innych technik_, aby osiągnąć pożądane wyniki? Użyj ich do stworzenia punktu odniesienia do porównania.
  - Inżynieria promptów: Wypróbuj techniki takie jak prompting few-shot z przykładami trafnych odpowiedzi na prompty. Oceń jakość odpowiedzi.
  - Retrieval Augmented Generation: Spróbuj wzbogacać prompty wynikami zapytań uzyskanymi poprzez przeszukiwanie Twoich danych. Oceń jakość odpowiedzi.
- **Koszty**: Czy zidentyfikowałeś koszty dostrajania?
  - Możliwość dostrojenia - czy wstępnie wytrenowany model jest dostępny do dostrajania?
  - Wysiłek - przygotowanie danych treningowych, ocena i udoskonalanie modelu.
  - Obliczenia - uruchamianie zadań dostrajania i wdrażanie dostrojonego modelu
  - Dane - dostęp do wystarczającej jakości przykładów, aby dostrajanie miało wpływ
- **Korzyści**: Czy potwierdziłeś korzyści płynące z dostrajania?
  - Jakość - czy dostrojony model przewyższył punkt odniesienia?
  - Koszt - czy redukuje zużycie tokenów poprzez uproszczenie promptów?
  - Rozszerzalność - czy możesz ponownie wykorzystać model podstawowy dla nowych domen?

Odpowiadając na te pytania, powinieneś być w stanie zdecydować, czy dostrajanie jest właściwym podejściem dla Twojego przypadku użycia. Idealnie, podejście jest zasadne tylko wtedy, gdy korzyści przewyższają koszty. Gdy zdecydujesz się kontynuować, nadszedł czas, aby pomyśleć o tym, _jak_ możesz dostroić wstępnie wytrenowany model.

Chcesz uzyskać więcej informacji na temat procesu podejmowania decyzji? Obejrzyj [Dostrajać czy nie dostrajać](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak możemy dostroić wstępnie wytrenowany model?

Aby dostroić wstępnie wytrenowany model, potrzebujesz:

- wstępnie wytrenowanego modelu do dostrojenia
- zbioru danych do użycia do dostrajania
- środowiska treningowego do uruchomienia zadania dostrajania
- środowiska hostingowego do wdrożenia dostrojonego modelu

## Dostrajanie w Akcji

Poniższe zasoby zawierają samouczki krok po kroku, które przeprowadzą Cię przez rzeczywisty przykład przy użyciu wybranego modelu z wyselekcjonowanym zbiorem danych. Aby przejść przez te samouczki, potrzebujesz konta u określonego dostawcy, wraz z dostępem do odpowiedniego modelu i zbiorów danych.

| Dostawca     | Samouczek                                                                                                                                                                       | Opis                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jak dostrajać modele czatu](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                   | Naucz się dostrajać `gpt-35-turbo` dla konkretnej domeny ("asystent przepisów") poprzez przygotowanie danych treningowych, uruchomienie zadania dostrajania i użycie dostrojonego modelu do wnioskowania.                                                                                                                                                                                                                                                                 |
| Azure OpenAI | [Samouczek dostrajania GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Naucz się dostrajać model `gpt-35-turbo-0613` **na Azure**, wykonując kroki tworzenia i przesyłania danych treningowych, uruchamiania zadania dostrajania. Wdróż i używaj nowego modelu.                                                                                                                                                                                                                                                                                  |
| Hugging Face | [Dostrajanie LLM za pomocą Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                            | Ten wpis na blogu przeprowadzi Cię przez proces dostrajania _otwartego LLM_ (np. `CodeLlama 7B`) przy użyciu biblioteki [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) i [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) z otwartymi [zbiorami danych](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 🤗 AutoTrain | [Dostrajanie LLM za pomocą AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                      | AutoTrain (lub AutoTrain Advanced) to biblioteka Pythona opracowana przez Hugging Face, która umożliwia dostrajanie dla wielu różnych zadań, w tym dostrajanie LLM. AutoTrain to rozwiązanie bez kodu, a dostrajanie można wykonać we własnej chmurze, na Hugging Face Spaces lub lokalnie. Obsługuje zarówno graficzny interfejs użytkownika oparty na sieci Web, CLI, jak i trenowanie za pomocą plików konfiguracyjnych yaml.                                          |
|              |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Zadanie

Wybierz jeden z powyższych samouczków i przejdź przez niego. _Możemy zreplikować wersję tych samouczków w Jupyter Notebooks w tym repozytorium tylko w celach informacyjnych. Prosimy o bezpośrednie korzystanie z oryginalnych źródeł, aby uzyskać najnowsze wersje_.

## Świetna Robota! Kontynuuj Naukę.

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej AI!

Gratulacje!! Ukończyłeś ostatnią lekcję z serii v2 tego kursu! Nie przestawaj się uczyć i budować. \*\*Sprawdź stronę [ZASOBY](RESOURCES.md?WT.mc_id=academic-105485-koreyst), aby znaleźć listę dodatkowych sugestii dotyczących tego tematu.

Nasza seria lekcji v1 również została zaktualizowana o więcej zadań i koncepcji. Poświęć więc chwilę na odświeżenie wiedzy - i proszę [podziel się swoimi pytaniami i opiniami](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby pomóc nam ulepszyć te lekcje dla społeczności.
