[![Open Source Models](../../../translated_images/pl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Dostrajenie Twojego LLM

Wykorzystanie dużych modeli językowych do budowania generatywnych aplikacji AI wiąże się z nowymi wyzwaniami. Kluczową kwestią jest zapewnienie jakości odpowiedzi (dokładności i relewantności) w generowanych przez model treściach na podstawie konkretnego zapytania użytkownika. W poprzednich lekcjach omawialiśmy techniki takie jak inżynieria promptów i generowanie wspomagane wyszukiwaniem, które starają się rozwiązać problem poprzez _modyfikację danych wejściowych promptu_ do istniejącego modelu.

W dzisiejszej lekcji omówimy trzecią technikę, **dostrajenie**, która próbuje rozwiązać wyzwanie poprzez _ponowne trenowanie samego modelu_ przy użyciu dodatkowych danych. Zagłębmy się w szczegóły.

## Cele nauki

Ta lekcja wprowadza pojęcie dostrajania modeli językowych wstępnie wytrenowanych, przedstawia korzyści i wyzwania związane z tym podejściem oraz dostarcza wskazówek, kiedy i jak używać dostrajania, aby poprawić wydajność twoich generatywnych modeli AI.

Po zakończeniu tej lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest dostrajanie modeli językowych?
- Kiedy i dlaczego dostrajanie jest użyteczne?
- Jak mogę dostroić wstępnie wytrenowany model?
- Jakie są ograniczenia dostrajania?

Gotowy? Zaczynamy.

## Przewodnik ilustrowany

Chcesz zobaczyć ogólny obraz materiału, zanim zagłębisz się w szczegóły? Sprawdź ten ilustrowany przewodnik, który opisuje ścieżkę nauki dla tej lekcji – od poznania podstawowych koncepcji i motywacji do dostrajania, po zrozumienie procesu i najlepszych praktyk realizacji zadania dostrajania. To fascynujący temat do eksploracji, więc nie zapomnij zajrzeć na stronę [Zasoby](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) po dodatkowe linki wspierające samodzielną naukę!

![Ilustrowany przewodnik do dostrajania modeli językowych](../../../translated_images/pl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Czym jest dostrajanie modeli językowych?

Z definicji, duże modele językowe są _wstępnie wytrenowane_ na dużych ilościach tekstów pochodzących z różnych źródeł, w tym z internetu. Jak dowiedzieliśmy się w poprzednich lekcjach, potrzebujemy technik takich jak _inżynieria promptów_ i _generowanie wspomagane wyszukiwaniem_ aby poprawić jakość odpowiedzi modelu na pytania użytkownika („prompty”).

Popularna technika inżynierii promptów polega na dawaniu modelowi bardziej precyzyjnych wskazówek, czego oczekujemy w odpowiedzi, albo przez dostarczenie _instrukcji_ (jawne wskazówki), albo _kilku przykładów_ (ukrytych wskazówek). Nazywa się to _uczeniem z niewielką liczbą przykładów_ (few-shot learning), ale ma dwie ograniczenia:

- Limity tokenów modelu mogą ograniczać liczbę przykładów, które możesz dostarczyć, i zmniejszają skuteczność.
- Koszty tokenów modelu mogą uczynić dodanie przykładów do każdego promptu kosztownym, ograniczając elastyczność.

Dostrajanie to powszechnie stosowana praktyka w systemach uczenia maszynowego, gdzie bierzemy wstępnie wytrenowany model i ponownie trenujemy go na nowych danych, aby poprawić jego wydajność na konkretnym zadaniu. W kontekście modeli językowych możemy dostroić taki model _za pomocą wyselekcjonowanego zbioru przykładów dla określonego zadania lub dziedziny zastosowania_, tworząc **model niestandardowy**, który może być dokładniejszy i bardziej relewantny dla tego specyficznego zadania lub dziedziny. Dodatkową zaletą dostrajania jest to, że może zmniejszyć liczbę przykładów potrzebnych do uczenia z niewielką liczbą przykładów – redukując użycie tokenów i powiązane koszty.

## Kiedy i dlaczego warto dostrajać modele?

W _tym_ kontekście, gdy mówimy o dostrajaniu, mamy na myśli **nadzorowane** dostrajanie, gdzie ponowne trenowanie polega na **dodaniu nowych danych**, które nie były częścią oryginalnego zbioru treningowego. To różni się od nienadzorowanego dostrajania, gdzie model jest trenowany ponownie na oryginalnych danych, ale z innymi hiperparametrami.

Kluczową rzeczą do zapamiętania jest to, że dostrajanie to zaawansowana technika, która wymaga pewnego poziomu wiedzy, aby osiągnąć oczekiwane rezultaty. Jeśli zostanie wykonana niepoprawnie, może nie przynieść oczekiwanych ulepszeń, a nawet pogorszyć wydajność modelu w twojej docelowej dziedzinie.

Zatem zanim nauczysz się „jak” dostrajać modele językowe, musisz wiedzieć „dlaczego” powinieneś pójść tą drogą oraz „kiedy” rozpocząć proces dostrajania. Zacznij od zadania sobie tych pytań:

- **Przypadek użycia**: Jaki jest twój _przypadek użycia_ dla dostrajania? Co chcesz poprawić w obecnym wstępnie wytrenowanym modelu?
- **Alternatywy**: Czy próbowałeś _innych technik_ aby osiągnąć pożądane efekty? Użyj ich, aby stworzyć punkt odniesienia do porównania.
  - Inżynieria promptów: Wypróbuj techniki takie jak few-shot prompting z przykładami odpowiednich reakcji. Oceń jakość odpowiedzi.
  - Generowanie wspomagane wyszukiwaniem: Spróbuj wzbogacić prompty o wyniki zapytań wyszukiwanych w twoich danych. Oceń jakość odpowiedzi.
- **Koszty**: Czy zidentyfikowałeś koszty dostrajania?
  - Możliwość dostrajania – czy model wstępnie wytrenowany jest dostępny do dostrajania?
  - Wysiłek – przygotowanie danych treningowych, ocena i dopracowywanie modelu.
  - Obliczenia – uruchamianie zadań dostrajania i wdrożenie dostrojonego modelu.
  - Dane – dostęp do wystarczającej liczby jakościowych przykładów wpływających na dostrajanie.
- **Korzyści**: Czy potwierdziłeś korzyści płynące z dostrajania?
  - Jakość – czy dostrojony model przewyższył punkt odniesienia?
  - Koszt – czy zmniejsza zużycie tokenów upraszczając prompty?
  - Rozszerzalność – czy możesz przystosować model bazowy do nowych dziedzin?

Odpowiadając na te pytania, powinieneś być w stanie zdecydować, czy dostrajanie jest odpowiednim podejściem dla twojego przypadku użycia. Najlepiej, jeśli podejście jest ważne tylko wtedy, gdy korzyści przewyższają koszty. Gdy zdecydujesz się kontynuować, czas pomyśleć o _tym, jak_ możesz dostroić wstępnie wytrenowany model.

Chcesz uzyskać więcej informacji na temat procesu podejmowania decyzji? Obejrzyj [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak możemy dostroić wstępnie wytrenowany model?

Aby dostroić wstępnie wytrenowany model, potrzebujesz:

- model wstępnie wytrenowany do dostrajania
- zbiór danych do wykorzystania w dostrajaniu
- środowisko treningowe do uruchomienia zadania dostrajania
- środowisko do hostowania wdrożonego dostrojonego modelu

## Dostrajenie na Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) to miejsce, gdzie dziś możesz dostroić, wdrożyć i zarządzać niestandardowymi modelami na Azure (łączy to, co dawniej było Azure OpenAI Studio i Azure AI Studio). Zanim rozpoczniesz zadanie, warto zrozumieć dostępne opcje w Foundry – i najlepsze praktyki zalecane przez platformę. Under the hood, Foundry uses **LoRA (low-rank adaptation)** to fine-tune models efficiently, which keeps training faster and more affordable than retraining every weight.

### Krok 1: Wybierz technikę treningu

Foundry obsługuje trzy techniki dostrajania. **Zacznij od SFT** - pokrywa najszerszy zakres scenariuszy.

| Technika | Co robi | Kiedy ją używać |
| --- | --- | --- |
| **Nadzorowane dostrajanie (SFT)** | Trenuje na parach przykładów wejście/wyjście, aby model nauczył się generować oczekiwane odpowiedzi. | Domyślne dla większości zadań: specjalizacja dziedziny, wyniki zadania, styl i ton, realizacja instrukcji, adaptacja językowa. |
| **Bezpośrednia optymalizacja preferencji (DPO)** | Uczy się na podstawie par odpowiedzi _preferowanych vs. niepreferowanych_, aby dostosować output do preferencji ludzkich. | Poprawa jakości odpowiedzi, bezpieczeństwa i zgodności, gdy masz informacje zwrotne porównawcze. |
| **Dostrajenie z wzmocnieniem (RFT)** | Wykorzystuje sygnały nagród od _oceniających_ do optymalizacji złożonych zachowań za pomocą uczenia ze wzmocnieniem. | Obiektywne, logicznie złożone dziedziny (matematyka, chemia, fizyka) z wyraźnie poprawnymi błędnymi odpowiedziami. Wymaga większej wiedzy ML. |

### Krok 2: Wybierz poziom treningu

Foundry pozwala wybrać, jak i gdzie będzie przeprowadzany trening:

- **Standard** - trenuje w regionie zasobu i gwarantuje lokalizację danych. Używaj, gdy dane muszą pozostać w określonym regionie.
- **Globalny** - tańszy i szybszy dzięki wykorzystaniu pojemności poza twoim regionem (dane i wagi są kopiowane do regionu treningowego). Dobre domyślne, gdy lokalizacja danych nie jest wymagana.
- **Deweloperski** - najniższy koszt, wykorzystujący nieaktywne zasoby bez gwarancji opóźnienia/SLA (zadania mogą być wstrzymane i wznowione). Idealny do eksperymentów.

### Krok 3: Wybierz model bazowy

Modele możliwe do dostrojenia to m.in. OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` i `gpt-4.1-nano` (SFT; rodzina 4o/4.1 obsługuje też DPO), modele rozumowania `o4-mini` i `gpt-5` (RFT), plus modele open source takie jak `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` i `gpt-oss-20b` (SFT na zasobach Foundry). Zawsze sprawdzaj aktualną [listę modeli do dostrajania](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) dla obsługiwanych metod, regionów i dostępności.

> Foundry oferuje dwa tryby: **serverless** (rozliczanie za zużycie, brak konieczności zarządzania przydziałem GPU, modele OpenAI i wybrane inne) oraz **zarządzane obliczenia** (własne maszyny wirtualne przez Azure Machine Learning dla najszerszego wyboru modeli). Większość użytkowników powinna zacząć od trybu serverless.

### Najlepsze praktyki Foundry

- **Najpierw ustal punkt odniesienia.** Zmierz model bazowy przy pomocy inżynierii promptów i RAG _przed_ dostrajaniem, aby udowodnić wzrost efektywności.
- **Zacznij od małej ilości, potem zwiększaj.** Rozpocznij od 50-100 wysokiej jakości przykładów, aby zweryfikować podejście, potem rozbuduj do 500+ dla produkcji. Jakość jest ważniejsza niż ilość – usuwaj niskiej jakości przykłady.
- **Poprawnie formatuj dane.** Pliki treningowe i walidacyjne muszą być w formacie JSONL, UTF-8 **z BOM**, poniżej 512 MB, używając formatu wiadomości chat-completions. Zawsze dołącz plik walidacyjny, aby obserwować przeuczenie.
- **Zachowaj komunikat systemowy podczas inferencji.** Używaj tego samego komunikatu systemowego, którego użyłeś podczas treningu, gdy wywołujesz model.
- **Oceniaj punkty kontrolne - nie wdrażaj ślepo ostatniego.** Foundry przechowuje ostatnie trzy epoki jako punkty kontrolne do wdrożenia; wybierz ten, który generalizuje najlepiej, obserwując `train_loss` / `valid_loss` i dokładność tokenów.
- **Mierz koszt tokenów wraz z jakością** podczas porównywania modelu dostrojonego z bazowym.
- **Iteruj przez ciągłe dostrajanie.** Możesz dostrajać już dostrojony model na nowych danych (obsługiwane dla modeli OpenAI).
- **Pamiętaj o kosztach hostingu.** Wdrożony model niestandardowy jest rozliczany godzinowo, a nieaktywny deployment jest usuwany po 15 dniach – sprzątaj, czego nie potrzebujesz.

Przejdź przez kompletny przewodnik w [Dostrajaniu modelu](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) i zapoznaj się z instrukcjami dla [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) i [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) gdy będziesz gotowy na inne techniki.

## Dostrajenie w praktyce

Następujące zasoby zapewniają przewodniki krok po kroku, które prowadzą przez realny przykład na obecnie obsługiwanym modelu z wyselekcjonowanym zestawem danych. Aby z nich skorzystać, potrzebujesz konta u konkretnego dostawcy oraz dostępu do odpowiednich modeli i zbiorów danych.

| Dostawca     | Samouczek                                                                                                                                                                       | Opis                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jak dostroić modele chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naucz się dostrajania najnowszego modelu chat OpenAI do konkretnej dziedziny („asystent przepisów”) przez przygotowanie danych treningowych, uruchomienie zadania dostrajania i korzystanie z dostrojonego modelu do inferencji.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Dostosuj model przez dostrajanie](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Naucz się dostrajania obecnie obsługiwanego modelu takiego jak `gpt-4.1-mini` **na Azure** za pomocą Microsoft Foundry: przygotuj i załaduj dane treningowe i walidacyjne, uruchom zadanie dostrajania, następnie wdroż i używaj nowego modelu.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Dostrajanie LLM z Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ten wpis na blogu przeprowadza Cię przez proces dostrajania _otwartego LLM_ (np. `CodeLlama 7B`) za pomocą biblioteki [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) oraz [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) z wykorzystaniem otwartych [datasetów](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Dostrajanie LLM z AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (lub AutoTrain Advanced) to biblioteka Pythona opracowana przez Hugging Face, która umożliwia dostrajanie dla wielu różnych zadań, w tym dostrajanie LLM. AutoTrain to rozwiązanie bez kodu, a dostrajanie można wykonywać w chmurze, na Hugging Face Spaces lub lokalnie. Wspiera zarówno interfejs webowy GUI, CLI oraz trening za pomocą plików konfiguracyjnych yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Dostrajanie LLM z Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth to otwartoźródłowy framework, który wspiera dostrajanie LLM oraz uczenie ze wzmocnieniem (RL). Unsloth upraszcza lokalne trenowanie, ocenę i wdrażanie dzięki gotowym do użycia [notatnikom](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Wspiera także syntezę mowy (TTS), modele BERT oraz multimodalne. Aby zacząć, przeczytaj ich krok po kroku [Przewodnik po dostrajaniu LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Zadanie

Wybierz jeden z powyższych tutoriali i przejdź przez niego. _Możemy odtworzyć wersję tych tutoriali w notatnikach Jupyter w tym repozytorium wyłącznie dla odniesienia. Prosimy o korzystanie bezpośrednio z oryginalnych źródeł, aby uzyskać najnowsze wersje_.

## Świetna robota! Kontynuuj naukę.

Po zakończeniu tej lekcji, sprawdź naszą kolekcję [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generatywnej Sztucznej Inteligencji!

Gratulacje!! Ukończyłeś ostatnią lekcję z serii v2 tego kursu! Nie przestawaj się uczyć i budować. \*\*Sprawdź stronę [ZASOBY](RESOURCES.md?WT.mc_id=academic-105485-koreyst) z listą dodatkowych sugestii dotyczącą właśnie tego tematu.

Nasza seria lekcji v1 została również zaktualizowana o dodatkowe zadania i koncepcje. Poświęć chwilę, aby odświeżyć swoją wiedzę - i prosimy [podziel się swoimi pytaniami i opiniami](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby pomóc nam ulepszyć te lekcje dla całej społeczności.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->