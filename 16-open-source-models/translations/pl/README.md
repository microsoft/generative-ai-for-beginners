[![Modele Open Source](../../images/16-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Wprowadzenie

Świat modeli LLM typu open-source jest ekscytujący i ciągle się rozwija. Ta lekcja ma na celu zapewnienie dogłębnego spojrzenia na modele open source. Jeśli szukasz informacji na temat porównania modeli zastrzeżonych z modelami open source, przejdź do lekcji ["Odkrywanie i porównywanie różnych LLM"](../../../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ta lekcja obejmie również temat dostrajania (fine-tuning), ale bardziej szczegółowe wyjaśnienie można znaleźć w lekcji ["Dostrajanie LLM"](../../../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cele nauki

- Zrozumienie modeli open source
- Zrozumienie korzyści płynących z pracy z modelami open source
- Odkrywanie otwartych modeli dostępnych na Hugging Face i w Azure AI Studio

## Czym są modele Open Source?

Oprogramowanie open source odegrało kluczową rolę we wzroście technologii w różnych dziedzinach. Open Source Initiative (OSI) zdefiniowała [10 kryteriów dla oprogramowania](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), aby mogło być sklasyfikowane jako open source. Kod źródłowy musi być otwarcie udostępniony na licencji zatwierdzonej przez OSI.

Chociaż rozwój LLM ma podobne elementy do tworzenia oprogramowania, proces nie jest dokładnie taki sam. Wniosło to wiele dyskusji w społeczności na temat definicji open source w kontekście LLM. Aby model był zgodny z tradycyjną definicją open source, następujące informacje powinny być publicznie dostępne:

- Zbiory danych użyte do trenowania modelu.
- Pełne wagi modelu jako część treningu.
- Kod ewaluacji.
- Kod dostrajania.
- Pełne wagi modelu i metryki treningu.

Obecnie tylko kilka modeli spełnia te kryteria. [Model OLMo stworzony przez Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) jest jednym z nich.

W tej lekcji będziemy odnosić się do modeli jako "otwartych modeli" (open models), ponieważ w momencie pisania mogą one nie spełniać powyższych kryteriów.

## Korzyści z Otwartych Modeli

**Wysoce konfigurowalne** - Ponieważ otwarte modele są wydawane ze szczegółowymi informacjami o treningu, badacze i programiści mogą modyfikować wewnętrzne mechanizmy modelu. Umożliwia to tworzenie wysoce wyspecjalizowanych modeli, które są dostrojone do konkretnego zadania lub obszaru badań. Niektóre przykłady to generowanie kodu, operacje matematyczne i biologia.

**Koszt** - Koszt za token przy używaniu i wdrażaniu tych modeli jest niższy niż w przypadku modeli zastrzeżonych. Podczas tworzenia aplikacji Generatywnej AI należy rozważyć stosunek wydajności do ceny podczas pracy z tymi modelami w konkretnym przypadku użycia.

![Koszt Modelu](../../images/model-price.png?WT.mc_id=academic-105485-koreyst)
Źródło: Artificial Analysis

**Elastyczność** - Praca z otwartymi modelami umożliwia elastyczność w zakresie używania różnych modeli lub ich łączenia. Przykładem tego są [Asystenci HuggingChat](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), gdzie użytkownik może wybrać model używany bezpośrednio w interfejsie użytkownika:

![Wybierz Model](../../images/choose-model.png?WT.mc_id=academic-105485-koreyst)

## Odkrywanie Różnych Otwartych Modeli

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), opracowany przez Meta, to otwarty model zoptymalizowany pod kątem aplikacji opartych na czacie. Wynika to z jego metody dostrajania, która obejmowała dużą ilość dialogów i informacji zwrotnych od ludzi. Dzięki tej metodzie model generuje więcej wyników zgodnych z oczekiwaniami ludzi, co zapewnia lepsze doświadczenie użytkownika.

Niektóre przykłady dostrojonych wersji Llama to [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), która specjalizuje się w języku japońskim, oraz [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), która jest ulepszoną wersją modelu podstawowego.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) to otwarty model z silnym naciskiem na wysoką wydajność i efektywność. Wykorzystuje podejście Mixture-of-Experts (Mieszanka Ekspertów), które łączy grupę wyspecjalizowanych modeli ekspertów w jeden system, gdzie w zależności od danych wejściowych wybierane są określone modele do użycia. To sprawia, że obliczenia są bardziej efektywne, ponieważ modele zajmują się tylko danymi wejściowymi, w których się specjalizują.

Niektóre przykłady dostrojonych wersji Mistral to [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), który koncentruje się na dziedzinie medycznej, oraz [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), który wykonuje obliczenia matematyczne.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) to LLM stworzony przez Technology Innovation Institute (**TII**). Falcon-40B został wytrenowany na 40 miliardach parametrów, co wykazało lepszą wydajność niż GPT-3 przy mniejszym budżecie obliczeniowym. Wynika to z zastosowania algorytmu FlashAttention i multiquery attention, które umożliwiają zmniejszenie wymagań pamięciowych podczas wnioskowania. Dzięki temu skróconemu czasowi wnioskowania Falcon-40B nadaje się do aplikacji czatowych.

Niektóre przykłady dostrojonych wersji Falcon to [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asystent zbudowany na otwartych modelach, oraz [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), który zapewnia wyższą wydajność niż model podstawowy.

## Jak Wybrać

Nie ma jednej odpowiedzi na pytanie, jak wybrać otwarty model. Dobrym punktem wyjścia jest skorzystanie z funkcji filtrowania według zadań w Azure AI Studio. Pomoże to zrozumieć, do jakiego rodzaju zadań model został wytrenowany. Hugging Face prowadzi również Tablicę Liderów LLM, która pokazuje najlepiej działające modele w oparciu o określone metryki.

Porównując LLM różnych typów, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) to kolejne świetne źródło:

![Jakość Modelu](../../images/model-quality.png?WT.mc_id=academic-105485-koreyst)
Źródło: Artifical Analysis

Jeśli pracujesz nad konkretnym przypadkiem użycia, poszukiwanie dostrojonych wersji skupionych na tym samym obszarze może być skuteczne. Eksperymentowanie z wieloma otwartymi modelami, aby zobaczyć, jak działają zgodnie z Twoimi oczekiwaniami i oczekiwaniami użytkowników, to kolejna dobra praktyka.

## Następne Kroki

Najlepszą częścią otwartych modeli jest to, że możesz zacząć z nimi pracować dość szybko. Sprawdź [Katalog Modeli Azure AI Studio](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), który zawiera specjalną kolekcję Hugging Face z modelami, o których tutaj dyskutowaliśmy.

## Nauka się tu nie kończy, kontynuuj Podróż

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej AI!
