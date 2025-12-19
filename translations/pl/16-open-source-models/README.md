<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T14:47:53+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "pl"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.pl.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Wprowadzenie

Świat otwartych modeli LLM jest ekscytujący i nieustannie się rozwija. Ta lekcja ma na celu dostarczenie dogłębnego spojrzenia na modele open source. Jeśli szukasz informacji o tym, jak modele własnościowe wypadają na tle modeli open source, przejdź do lekcji ["Exploring and Comparing Different LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Ta lekcja obejmie również temat fine-tuningu, ale bardziej szczegółowe wyjaśnienie znajdziesz w lekcji ["Fine-Tuning LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cele nauki

- Zdobycie wiedzy na temat modeli open source
- Zrozumienie korzyści płynących z pracy z modelami open source
- Poznanie dostępnych modeli open na Hugging Face i w Azure AI Studio

## Czym są modele Open Source?

Oprogramowanie open source odegrało kluczową rolę w rozwoju technologii w różnych dziedzinach. Inicjatywa Open Source (OSI) zdefiniowała [10 kryteriów dla oprogramowania](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), które musi spełniać, aby zostać zaklasyfikowane jako open source. Kod źródłowy musi być otwarcie udostępniony na licencji zatwierdzonej przez OSI.

Chociaż rozwój LLM ma podobne elementy do tworzenia oprogramowania, proces ten nie jest dokładnie taki sam. Wywołało to wiele dyskusji w społeczności na temat definicji open source w kontekście LLM. Aby model był zgodny z tradycyjną definicją open source, następujące informacje powinny być publicznie dostępne:

- Zbiory danych użyte do trenowania modelu.
- Pełne wagi modelu jako część treningu.
- Kod ewaluacji.
- Kod fine-tuningu.
- Pełne wagi modelu i metryki treningowe.

Obecnie istnieje tylko kilka modeli spełniających te kryteria. [Model OLMo stworzony przez Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) jest jednym z nich.

W tej lekcji będziemy odnosić się do modeli jako "otwarte modele", ponieważ mogą one nie spełniać powyższych kryteriów w momencie pisania.

## Korzyści z otwartych modeli

**Wysoka możliwość dostosowania** – Ponieważ otwarte modele są udostępniane z szczegółowymi informacjami o treningu, badacze i deweloperzy mogą modyfikować ich wnętrze. Umożliwia to tworzenie wysoce wyspecjalizowanych modeli, które są dostrajane do konkretnego zadania lub dziedziny. Przykładami są generowanie kodu, operacje matematyczne i biologia.

**Koszt** – Koszt za token przy używaniu i wdrażaniu tych modeli jest niższy niż w przypadku modeli własnościowych. Budując aplikacje Generative AI, warto rozważyć stosunek wydajności do ceny przy pracy z tymi modelami w swoim przypadku użycia.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.pl.png)
Źródło: Artificial Analysis

**Elastyczność** – Praca z otwartymi modelami pozwala na elastyczność w zakresie używania różnych modeli lub ich łączenia. Przykładem są [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), gdzie użytkownik może wybrać model bezpośrednio w interfejsie użytkownika:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.pl.png)

## Przegląd różnych otwartych modeli

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), opracowany przez Meta, to otwarty model zoptymalizowany do zastosowań czatowych. Wynika to z metody fine-tuningu, która obejmowała dużą ilość dialogów i opinii ludzkich. Dzięki temu model generuje wyniki bardziej zgodne z oczekiwaniami ludzi, co zapewnia lepsze doświadczenie użytkownika.

Przykładami wersji fine-tuned Llama są [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), specjalizujący się w języku japońskim, oraz [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ulepszona wersja modelu bazowego.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) to otwarty model z silnym naciskiem na wysoką wydajność i efektywność. Wykorzystuje podejście Mixture-of-Experts, które łączy grupę wyspecjalizowanych modeli ekspertów w jeden system, gdzie w zależności od wejścia wybierane są odpowiednie modele. Sprawia to, że obliczenia są bardziej efektywne, ponieważ modele zajmują się tylko tymi danymi, w których są specjalistami.

Przykładami wersji fine-tuned Mistral są [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), skoncentrowany na medycynie, oraz [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), który wykonuje obliczenia matematyczne.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) to LLM stworzony przez Technology Innovation Institute (**TII**). Falcon-40B został wytrenowany na 40 miliardach parametrów i wykazuje lepszą wydajność niż GPT-3 przy mniejszym budżecie obliczeniowym. Wynika to z zastosowania algorytmu FlashAttention oraz multiquery attention, które zmniejszają wymagania pamięciowe podczas inferencji. Dzięki temu Falcon-40B nadaje się do zastosowań czatowych.

Przykładami wersji fine-tuned Falcon są [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asystent zbudowany na otwartych modelach, oraz [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), który oferuje wyższą wydajność niż model bazowy.

## Jak wybrać

Nie ma jednej odpowiedzi na wybór otwartego modelu. Dobrym punktem startowym jest użycie funkcji filtrowania według zadania w Azure AI Studio. Pomoże to zrozumieć, do jakich typów zadań model był trenowany. Hugging Face prowadzi również ranking LLM, który pokazuje najlepiej działające modele według określonych metryk.

Przy porównywaniu LLM różnych typów, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) jest kolejnym świetnym źródłem:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.pl.png)
Źródło: Artificial Analysis

Pracując nad konkretnym przypadkiem użycia, warto poszukać wersji fine-tuned skoncentrowanych na tej samej dziedzinie. Eksperymentowanie z wieloma otwartymi modelami, aby zobaczyć, jak spełniają oczekiwania twoje i twoich użytkowników, to również dobra praktyka.

## Kolejne kroki

Najlepszą częścią otwartych modeli jest to, że można zacząć z nimi pracować dość szybko. Sprawdź [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), który zawiera specjalną kolekcję Hugging Face z modelami omówionymi tutaj.

## Nauka nie kończy się tutaj, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [kolekcję Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->