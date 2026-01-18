<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:11:31+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "pl"
}
-->
[![Otwarte Modele Źródłowe](../../../../../translated_images/pl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Dostosowywanie Twojego LLM

Używanie dużych modeli językowych do budowy generatywnych aplikacji AI wiąże się z nowymi wyzwaniami. Kluczową kwestią jest zapewnienie jakości odpowiedzi (dokładności i trafności) w treści generowanej przez model na określone zapytanie użytkownika. W poprzednich lekcjach omawialiśmy techniki takie jak inżynieria promptów oraz generowanie wspomagane wyszukiwaniem, które próbują rozwiązać problem przez _modyfikację wejścia promptu_ do istniejącego modelu.

W dzisiejszej lekcji omówimy trzecią technikę, **dostosowywanie (fine-tuning)**, która stara się rozwiązać wyzwanie przez _ponowne trenowanie samego modelu_ na dodatkowych danych. Przyjrzyjmy się szczegółom.

## Cele Nauki

Ta lekcja wprowadza koncepcję dostosowywania dla wcześniej wytrenowanych modeli językowych, bada zalety i wyzwania takiego podejścia oraz daje wskazówki, kiedy i jak używać dostosowywania, aby poprawić wydajność twoich generatywnych modeli AI.

Na koniec tej lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest dostosowywanie modeli językowych?
- Kiedy i dlaczego dostosowywanie jest przydatne?
- Jak mogę dostosować wcześniej wytrenowany model?
- Jakie są ograniczenia dostosowywania?

Gotowy? Zaczynajmy.

## Przewodnik Ilustrowany

Chcesz zobaczyć ogólny obraz tego, co omówimy, zanim zaczniemy? Sprawdź ten ilustrowany przewodnik, który opisuje ścieżkę nauki dla tej lekcji – od poznania podstawowych pojęć i motywacji do dostosowywania, po zrozumienie procesu i najlepszych praktyk realizacji zadania dostosowywania. To fascynujący temat do eksploracji, więc nie zapomnij odwiedzić strony [Zasoby](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) po dodatkowe linki wspierające twoją samodzielną naukę!

![Przewodnik Ilustrowany po Dostosowywaniu Modeli Językowych](../../../../../translated_images/pl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Czym jest dostosowywanie modeli językowych?

Z definicji, duże modele językowe są _wcześniej wytrenowane_ na dużych ilościach tekstu pochodzącego z różnych źródeł, w tym internetu. Jak dowiedzieliśmy się w poprzednich lekcjach, potrzebujemy technik takich jak _inżynieria promptów_ i _generowanie wspomagane wyszukiwaniem_, aby poprawić jakość odpowiedzi modelu na pytania użytkownika („prompty”).

Popularną techniką inżynierii promptów jest udzielanie modelowi większej ilości wskazówek, co ma znaleźć się w odpowiedzi, poprzez dostarczanie _instrukcji_ (wyraźnych wskazówek) lub _pokazywanie kilku przykładów_ (wskazówki niejawne). Nazywa się to _uczeniem na małej liczbie przykładów_ (few-shot learning), ale ma dwa ograniczenia:

- Limity tokenów modelu mogą ograniczać liczbę przykładów, które można podać, i zmniejszać efektywność.
- Koszty tokenów modelu mogą sprawić, że dodawanie przykładów do każdego promptu będzie drogie, ograniczając elastyczność.

Dostosowywanie to powszechna praktyka w systemach uczenia maszynowego, gdzie bierzemy wcześniej wytrenowany model i ponownie go trenujemy na nowych danych, aby poprawić jego wydajność w określonym zadaniu. W kontekście modeli językowych możemy dostosować wcześniej wytrenowany model _za pomocą wyselekcjonowanego zestawu przykładów dla konkretnego zadania lub domeny zastosowania_, tworząc **model dostosowany**, który może być dokładniejszy i bardziej trafny dla tego konkretnie zadania lub domeny. Dodatkowym efektem dostosowywania jest to, że może ono również zmniejszyć liczbę przykładów potrzebnych przy uczeniu na małej liczbie przykładów – zmniejszając użycie tokenów i powiązane koszty.

## Kiedy i dlaczego powinniśmy dostosowywać modele?

W _tym_ kontekście, gdy mówimy o dostosowywaniu, odnosimy się do **nadzorowanego** dostosowywania, gdzie ponowne trenowanie odbywa się przez **dodanie nowych danych**, które nie były częścią oryginalnego zestawu treningowego. To różni się od nienadzorowanego dostosowywania, gdzie model jest ponownie trenowany na oryginalnych danych, ale z różnymi hiperparametrami.

Kluczową rzeczą do zapamiętania jest to, że dostosowywanie to zaawansowana technika, która wymaga pewnego poziomu wiedzy, aby uzyskać oczekiwane rezultaty. Jeśli zostanie wykonane niepoprawnie, może nie przynieść spodziewanych ulepszeń, a nawet pogorszyć wydajność modelu w twojej docelowej domenie.

Zatem zanim nauczysz się „jak” dostosowywać modele językowe, musisz wiedzieć „dlaczego” powinieneś obrać tę ścieżkę i „kiedy” rozpocząć proces dostosowywania. Zacznij od zadania sobie tych pytań:

- **Przypadek użycia**: Jaki jest twój _przypadek użycia_ dla dostosowywania? Co chcesz poprawić w obecnym wcześniej wytrenowanym modelu?
- **Alternatywy**: Czy próbowałeś _innych technik_, aby osiągnąć pożądane wyniki? Użyj ich do stworzenia bazy do porównania.
  - Inżynieria promptów: Spróbuj technik takich jak few-shot prompting z przykładami odpowiedzi. Oceń jakość odpowiedzi.
  - Generowanie wspomagane wyszukiwaniem: Spróbuj wzbogacić prompt o wyniki zapytań uzyskanych przez wyszukiwanie w twoich danych. Oceń jakość odpowiedzi.
- **Koszty**: Czy zidentyfikowałeś koszty związane z dostosowywaniem?
  - Możliwość dostosowania – czy model wcześniej wytrenowany jest dostępny do dostosowania?
  - Nakład pracy – przygotowanie danych treningowych, ocena i dopracowanie modelu.
  - Obliczenia – przeprowadzanie zadań dostosowywania i wdrażanie modelu dostosowanego.
  - Dane – dostęp do dostatecznej jakości przykładów, aby dostosowanie miało efekt.
- **Korzyści**: Czy potwierdziłeś korzyści płynące z dostosowywania?
  - Jakość – czy model dostosowany przewyższał bazę?
  - Koszty – czy zmniejsza zużycie tokenów przez uproszczenie promptów?
  - Rozszerzalność – czy możesz wykorzystać model bazowy dla nowych domen?

Odpowiadając na te pytania, powinieneś móc zdecydować, czy dostosowywanie jest właściwym podejściem dla twojego przypadku użycia. Idealnie, podejście ma sens tylko wtedy, gdy korzyści przewyższają koszty. Gdy już zdecydujesz się kontynuować, czas pomyśleć o tym, _jak_ możesz dostosować wcześniej wytrenowany model.

Chcesz uzyskać więcej informacji na temat procesu podejmowania decyzji? Obejrzyj [Dostosować czy nie dostosować](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Jak możemy dostosować wcześniej wytrenowany model?

Aby dostosować wcześniej wytrenowany model, potrzebujesz:

- wcześniej wytrenowanego modelu do dostosowania
- zbioru danych do wykorzystania w dostosowywaniu
- środowiska treningowego do uruchomienia zadania dostosowywania
- środowiska hostingowego do wdrożenia modelu dostosowanego

## Dostosowywanie w Praktyce

Poniższe zasoby dostarczają samouczków krok po kroku, które przeprowadzą cię przez rzeczywisty przykład z wybranym modelem i wyselekcjonowanym zbiorem danych. Aby skorzystać z tych samouczków, potrzebujesz konta u konkretnego dostawcy, wraz z dostępem do odpowiednich modeli i zbiorów danych.

| Dostawca    | Samouczek                                                                                                                                                                     | Opis                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI      | [Jak dostosować modele czatu](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Naucz się dostosowywać `gpt-35-turbo` do konkretnej domeny („asystent przepisów”) poprzez przygotowanie danych treningowych, uruchomienie zadania dostosowywania oraz wykorzystanie modelu dostosowanego do wnioskowania.                                                                                                                                                                                                        |
| Azure OpenAI| [Samouczek dostosowywania GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Naucz się jak dostosować model `gpt-35-turbo-0613` **na platformie Azure** przechodząc przez etapy tworzenia i przesyłania danych treningowych, uruchamiania zadania dostosowywania, wdrożenia i użycia nowego modelu.                                                                                                                                                                                                              |
| Hugging Face| [Dostosowywanie LLM z Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                              | Ten wpis na blogu przeprowadza cię przez dostosowywanie _otwartego LLM_ (np. `CodeLlama 7B`) z użyciem biblioteki [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) oraz [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) z otwartymi [zbiorami danych](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) na Hugging Face. |
|             |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain| [Dostosowywanie LLM z AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (lub AutoTrain Advanced) to biblioteka Pythona opracowana przez Hugging Face, która umożliwia dostosowywanie dla wielu różnych zadań, w tym dostosowywanie LLM. AutoTrain to rozwiązanie bez kodu, a dostosowywanie można przeprowadzić w swojej własnej chmurze, na Hugging Face Spaces lub lokalnie. Obsługuje zarówno interfejs webowy, CLI, jak i trening przez pliki konfiguracyjne yaml.                                               |
|             |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth  | [Dostosowywanie LLM z Unsloth](https://github.com/unslothai/unsloth)                                                                                                         | Unsloth to otwartoźródłowy framework wspierający dostosowywanie LLM i uczenie ze wzmocnieniem (RL). Unsloth usprawnia lokalne trenowanie, ocenę i wdrażanie z gotowymi do użycia [notatnikami](https://github.com/unslothai/notebooks). Obsługuje również syntezę mowy (TTS), BERT oraz modele multimodalne. Aby zacząć, przeczytaj ich krok po kroku [Przewodnik po dostosowywaniu LLM](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).             |
|             |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Zadanie

Wybierz jeden z powyższych samouczków i przejdź go krok po kroku. _Możemy przygotować wersję tych samouczków w notatnikach Jupyter w tym repozytorium wyłącznie dla odniesienia. Prosimy korzystaj bezpośrednio z oryginalnych źródeł, aby uzyskać najnowsze wersje_.

## Świetna praca! Kontynuuj naukę.

Po ukończeniu tej lekcji, sprawdź naszą kolekcję [Generatywnej Sztucznej Inteligencji](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generatywnej AI!

Gratulacje!! Ukończyłeś ostatnią lekcję z serii v2 tego kursu! Nie przestawaj się uczyć i tworzyć. **Sprawdź stronę [ZASOBY](RESOURCES.md?WT.mc_id=academic-105485-koreyst) z listą dodatkowych sugestii właśnie na ten temat.

Nasza seria lekcji v1 również została zaktualizowana o więcej zadań i koncepcji. Poświęć chwilę, aby odświeżyć swoją wiedzę – i prosimy, [dziel się swoimi pytaniami i opiniami](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst), aby pomóc nam ulepszać te lekcje dla społeczności.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrzeczenie się odpowiedzialności**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->