[![Modele Open Source](../../../translated_images/pl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Dostrajanie Twojego LLM

Wykorzystanie dużych modeli językowych do budowy aplikacji generatywnej sztucznej inteligencji wiąże się z nowymi wyzwaniami. Kluczowym problemem jest zapewnienie jakości odpowiedzi (dokładności i trafności) w treści generowanej przez model na podstawie konkretnego zapytania użytkownika. W poprzednich lekcjach omawialiśmy techniki takie jak inżynieria promptów i generacja wzbogacona o wyszukiwanie, które próbują rozwiązać problem poprzez _modyfikację wejściowego promptu_ do istniejącego modelu.

W dzisiejszej lekcji omówimy trzecią technikę, **dostrajanie**, która stara się rozwiązać to wyzwanie przez _ponowne trenowanie samego modelu_ z użyciem dodatkowych danych. Zagłębmy się w szczegóły.

## Cele nauki

Ta lekcja wprowadza koncept dostrajania wstępnie wytrenowanych modeli językowych, bada zalety i wyzwania tego podejścia oraz dostarcza wskazówek, kiedy i jak stosować dostrajanie, aby poprawić wydajność swoich modeli generatywnej AI.

Pod koniec tej lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest dostrajanie modeli językowych?
- Kiedy i dlaczego dostrajanie jest przydatne?
- Jak mogę dostroić wstępnie wytrenowany model?
- Jakie są ograniczenia dostrajania?

Gotowy? Zaczynamy.

## Ilustrowany przewodnik

Chcesz uzyskać ogólny obraz tego, co omówimy, zanim przejdziemy do szczegółów? Sprawdź ten ilustrowany przewodnik, który opisuje ścieżkę nauki tej lekcji - od poznania podstawowych koncepcji i motywacji dostrajania, po zrozumienie procesu i najlepszych praktyk wykonywania zadania dostrajania. To fascynujący temat do eksploracji, więc nie zapomnij zajrzeć na stronę [Zasoby](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) po dodatkowe linki wspierające twoją samodzielną naukę!

![Ilustrowany przewodnik po dostrajaniu modeli językowych](../../../translated_images/pl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Czym jest dostrajanie modeli językowych?

Z definicji, duże modele językowe są _wstępnie wytrenowane_ na dużych ilościach tekstu pochodzącego z różnych źródeł, w tym internetu. Jak nauczyliśmy się w poprzednich lekcjach, potrzebujemy technik takich jak _inżynieria promptów_ i _generacja wzbogacona o wyszukiwanie_, aby poprawić jakość odpowiedzi modelu na pytania użytkownika ("prompty").

Popularna technika inżynierii promptów polega na dawaniu modelowi większych wskazówek, czego oczekuje się w odpowiedzi, poprzez dostarczanie _instrukcji_ (wskazówki explicite) lub _podawanie kilku przykładów_ (wskazówki implicite). Nazywa się to _uczeniem z niewielką ilością przykładów_ (few-shot learning), ale ma ona dwie ograniczenia:

- Limity tokenów modelu mogą ograniczać liczbę przykładów, które możesz podać, i ograniczać skuteczność.
- Koszty tokenów modelu mogą sprawić, że dodawanie przykładów do każdego promptu będzie drogie i ograniczy elastyczność.

Dostrajanie jest powszechną praktyką w systemach uczenia maszynowego, gdzie bierzemy wstępnie wytrenowany model i ponownie trenujemy go na nowych danych, aby poprawić jego wydajność na określone zadanie. W kontekście modeli językowych możemy dostroić wstępnie wytrenowany model _za pomocą wyselekcjonowanego zestawu przykładów dla danego zadania lub domeny aplikacji_, aby stworzyć **model niestandardowy**, który może być dokładniejszy i bardziej trafny dla tego konkretnego zadania lub domeny. Dodatkowym efektem dostrajania jest redukcja liczby przykładów potrzebnych do uczenia się z niewielką ilością przykładów — zmniejszając zużycie tokenów i związane z tym koszty.

## Kiedy i dlaczego warto dostrajać modele?

W _tym_ kontekście, kiedy mówimy o dostrajaniu, odnosi się to do **nadzorowanego** dostrajania, gdzie ponowne trenowanie odbywa się przez **dodawanie nowych danych**, które nie były częścią oryginalnego zbioru treningowego. To różni się od podejścia niesuperwizowanego dostrajania, gdzie model jest ponownie trenowany na oryginalnych danych, ale z innymi hiperparametrami.

Kluczową rzeczą do zapamiętania jest to, że dostrajanie to zaawansowana technika wymagająca pewnego poziomu wiedzy, aby uzyskać pożądane rezultaty. Jeśli zostanie wykonane niewłaściwie, może nie przynieść oczekiwanych usprawnień, a nawet pogorszyć wydajność modelu w docelowej domenie.

Dlatego zanim nauczysz się "jak" dostrajać modele językowe, musisz wiedzieć "dlaczego" warto pójść tą drogą i "kiedy" rozpocząć proces dostrajania. Zacznij od zadania sobie tych pytań:

- **Przypadek użycia**: Jaki jest twój _przypadek użycia_ do dostrajania? Jaki aspekt obecnego wstępnie wytrenowanego modelu chcesz poprawić?
- **Alternatywy**: Czy próbowałeś _innych technik_, by osiągnąć oczekiwane rezultaty? Użyj ich jako punktu odniesienia do porównań.
  - Inżynieria promptów: Wypróbuj techniki takie jak few-shot z przykładami odpowiedzi. Oceń jakość odpowiedzi.
  - Generacja wzbogacona o wyszukiwanie: Spróbuj wzbogacić prompt wyniki zapytań pozyskane przez przeszukiwanie twoich danych. Oceń jakość odpowiedzi.
- **Koszty**: Czy zidentyfikowałeś koszty dostrajania?
  - Możliwość dostrajania - czy wstępnie wytrenowany model jest dostępny do dostrajania?
  - Wysiłek - na przygotowanie danych treningowych, ocenę i udoskonalanie modelu.
  - Obliczenia - na uruchomienie pracy dostrajania i wdrożenie dostrojonego modelu.
  - Dane - dostęp do wystarczającej jakości przykładów do wpływu dostrajania.
- **Korzyści**: Czy potwierdziłeś korzyści z dostrajania?
  - Jakość - czy dostrojony model przewyższył punkt odniesienia?
  - Koszt - czy zmniejsza zużycie tokenów poprzez uproszczenie promptów?
  - Rozszerzalność - czy możesz ponownie wykorzystać bazowy model do nowych domen?

Odpowiadając na te pytania, powinieneś być w stanie zdecydować, czy dostrajanie to właściwe podejście dla twojego przypadku użycia. Idealnie, podejście jest uzasadnione tylko wtedy, gdy korzyści przewyższają koszty. Gdy zdecydujesz się iść dalej, czas pomyśleć o _tym, jak_ możesz dostroić wstępnie wytrenowany model.

Chcesz uzyskać więcej informacji na temat procesu podejmowania decyzji? Obejrzyj [Dostrajanie czy nie dostrajanie](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak możemy dostroić wstępnie wytrenowany model?

Aby dostroić wstępnie wytrenowany model, potrzebujesz:

- wstępnie wytrenowanego modelu do dostrojenia
- zbioru danych do dostrajania
- środowiska treningowego do uruchomienia zadania dostrajania
- środowiska hostingowego do wdrożenia dostrojonego modelu

## Dostrajanie w akcji

> **Uwaga:** `gpt-35-turbo` / `gpt-3.5-turbo`, o którym wspomniano w niektórych poniższych samouczkach, został wycofany zarówno do inferencji, jak i dostrajania. Jeśli zaczynasz nową pracę dostrajania dzisiaj, celuj w aktualnie wspierany model — na przykład `gpt-4o-mini` lub `gpt-4.1-mini`. Zobacz [Listę modeli do dostrajania](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) dla aktualnego zestawu modeli możliwych do dostrojenia. Koncepcje i kroki w tych samouczkach są nadal aktualne.

Następujące zasoby dostarczają instrukcje krok po kroku, które przeprowadzą cię przez prawdziwy przykład z użyciem wybranego modelu i wyselekcjonowanego zbioru danych. Aby przejść przez te samouczki, potrzebujesz konta u konkretnego dostawcy, wraz z dostępem do odpowiedniego modelu i zbiorów danych.

| Dostawca    | Samouczek                                                                                                                                                                       | Opis                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jak dostroić modele czatu](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                     | Naucz się dostrajać `gpt-35-turbo` dla konkretnej domeny ("asystent przepisów") przez przygotowanie danych treningowych, uruchomienie pracy dostrajania i używanie dostrojonego modelu do inferencji.                                                                                                                                                                                                                              |
| Azure OpenAI | [Samouczek dostrajania GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)  | Naucz się dostrajać model `gpt-35-turbo-0613` **na platformie Azure** wykonując kroki tworzenia i przesyłania danych treningowych, uruchamiania pracy dostrajania. Wdrażaj i używaj nowego modelu.                                                                                                                                                                                                                                     |
| Hugging Face | [Dostrajanie LLM z Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                                    | Ten wpis na blogu przeprowadza przez dostrajanie _otwartego LLM_ (np. `CodeLlama 7B`) przy użyciu biblioteki [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) i [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) z otwartymi [zbiorami danych](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [Dostrajanie LLM z AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                              | AutoTrain (lub AutoTrain Advanced) to biblioteka w Pythonie rozwijana przez Hugging Face, która pozwala na dostrajanie dla wielu różnych zadań, w tym dostrajanie LLM. AutoTrain to rozwiązanie bez kodu i dostrajanie można wykonać we własnej chmurze, na Hugging Face Spaces lub lokalnie. Obsługuje zarówno interfejs WWW, CLI oraz trening za pomocą plików konfiguracyjnych yaml.                                                                                                |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth | [Dostrajanie LLM z Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                         | Unsloth to otwartoźródłowy framework wspierający dostrajanie LLM oraz uczenie przez wzmacnianie (RL). Unsloth usprawnia lokalne trenowanie, ocenę i wdrożenie z gotowymi [notebookami](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Obsługuje też syntezę mowy (TTS), modele BERT i multimodalne. Aby zacząć, przeczytaj ich krok po kroku [Przewodnik po dostrajaniu LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                              |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## Zadanie

Wybierz jeden z powyższych samouczków i przejdź przez niego. _Możemy sporządzić wersję tych samouczków w Jupyter Notebooks w tym repozytorium wyłącznie jako odniesienie. Proszę korzystaj bezpośrednio z oryginalnych źródeł, aby uzyskać najnowsze wersje_.

## Świetna robota! Kontynuuj naukę.

Po ukończeniu tej lekcji, zajrzyj do naszej [kolekcji nauki GenAI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę z zakresu generatywnej sztucznej inteligencji!

Gratulacje!! Ukończyłeś ostatnią lekcję z serii v2 tego kursu! Nie przestawaj się uczyć i tworzyć. \*\*Sprawdź stronę [ZASOBY](RESOURCES.md?WT.mc_id=academic-105485-koreyst) dla listy dodatkowych propozycji dotyczących tego tematu.

Nasza seria lekcji v1 również została zaktualizowana o więcej zadań i koncepcji. Poświęć chwilę, by odświeżyć swoją wiedzę – i prosimy, [dziel się swoimi pytaniami i opiniami](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby pomóc nam ulepszyć te lekcje dla społeczności.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->