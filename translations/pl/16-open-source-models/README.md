<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-18T00:59:05+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "pl"
}
-->
[![Modele Open Source](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.pl.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Wprowadzenie

Świat otwartych modeli LLM jest ekscytujący i nieustannie się rozwija. Celem tej lekcji jest szczegółowe zapoznanie się z modelami open source. Jeśli szukasz informacji na temat porównania modeli własnościowych z modelami open source, przejdź do lekcji ["Eksploracja i porównanie różnych LLM"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). W tej lekcji omówimy również temat dostrajania modeli, ale bardziej szczegółowe wyjaśnienie znajdziesz w lekcji ["Dostrajanie LLM"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Cele nauki

- Zrozumienie modeli open source
- Poznanie korzyści wynikających z pracy z modelami open source
- Eksploracja dostępnych modeli open source na platformach Hugging Face i Azure AI Studio

## Czym są modele open source?

Oprogramowanie open source odegrało kluczową rolę w rozwoju technologii w różnych dziedzinach. Open Source Initiative (OSI) zdefiniowała [10 kryteriów dla oprogramowania](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst), aby mogło być uznane za open source. Kod źródłowy musi być otwarcie udostępniony na licencji zatwierdzonej przez OSI.

Chociaż rozwój LLM ma podobne elementy do tworzenia oprogramowania, proces ten nie jest dokładnie taki sam. W społeczności toczy się wiele dyskusji na temat definicji open source w kontekście LLM. Aby model był zgodny z tradycyjną definicją open source, następujące informacje powinny być publicznie dostępne:

- Zbiory danych użyte do trenowania modelu.
- Pełne wagi modelu jako część treningu.
- Kod oceny.
- Kod dostrajania.
- Pełne wagi modelu i metryki treningowe.

Obecnie istnieje tylko kilka modeli, które spełniają te kryteria. [Model OLMo stworzony przez Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) jest jednym z nich.

W tej lekcji będziemy odnosić się do modeli jako "otwarte modele", ponieważ mogą nie spełniać powyższych kryteriów w momencie pisania.

## Korzyści z otwartych modeli

**Wysoka personalizacja** - Ponieważ otwarte modele są udostępniane z szczegółowymi informacjami o treningu, badacze i programiści mogą modyfikować wewnętrzne elementy modelu. Umożliwia to tworzenie wysoko wyspecjalizowanych modeli dostrojonych do konkretnego zadania lub dziedziny. Przykłady obejmują generowanie kodu, operacje matematyczne i biologię.

**Koszt** - Koszt na token za użycie i wdrożenie tych modeli jest niższy niż w przypadku modeli własnościowych. Przy budowie aplikacji generatywnej AI warto rozważyć wydajność w stosunku do ceny w kontekście konkretnego zastosowania.

![Koszt modelu](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.pl.png)  
Źródło: Artificial Analysis

**Elastyczność** - Praca z otwartymi modelami pozwala na elastyczność w korzystaniu z różnych modeli lub ich łączeniu. Przykładem jest [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst), gdzie użytkownik może wybrać model używany bezpośrednio w interfejsie użytkownika:

![Wybierz model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.pl.png)

## Eksploracja różnych otwartych modeli

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), opracowany przez Meta, to otwarty model zoptymalizowany pod kątem aplikacji opartych na czacie. Jest to możliwe dzięki metodzie dostrajania, która obejmowała dużą ilość dialogów i opinii ludzkich. Dzięki tej metodzie model generuje wyniki bardziej zgodne z oczekiwaniami użytkowników, co zapewnia lepsze doświadczenie.

Przykłady dostrojonych wersji Llama to [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), specjalizujący się w języku japońskim, oraz [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ulepszona wersja modelu bazowego.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) to otwarty model skoncentrowany na wysokiej wydajności i efektywności. Wykorzystuje podejście Mixture-of-Experts, które łączy grupę wyspecjalizowanych modeli ekspertów w jeden system, gdzie w zależności od wejścia wybierane są odpowiednie modele. Dzięki temu obliczenia są bardziej efektywne, ponieważ modele zajmują się tylko tymi danymi wejściowymi, w których się specjalizują.

Przykłady dostrojonych wersji Mistral to [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), skoncentrowany na dziedzinie medycyny, oraz [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), który wykonuje obliczenia matematyczne.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) to LLM stworzony przez Technology Innovation Institute (**TII**). Falcon-40B został wytrenowany na 40 miliardach parametrów, co wykazało, że działa lepiej niż GPT-3 przy mniejszym budżecie obliczeniowym. Jest to możliwe dzięki zastosowaniu algorytmu FlashAttention i wielozapytaniowej uwagi, które pozwalają na zmniejszenie wymagań pamięciowych podczas czasu wnioskowania. Dzięki skróconemu czasowi wnioskowania Falcon-40B nadaje się do aplikacji opartych na czacie.

Przykłady dostrojonych wersji Falcon to [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), asystent oparty na otwartych modelach, oraz [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), który oferuje wyższą wydajność niż model bazowy.

## Jak wybrać

Nie ma jednej odpowiedzi na pytanie, jak wybrać otwarty model. Dobrym punktem wyjścia jest skorzystanie z funkcji filtrowania według zadania w Azure AI Studio. Pomoże to zrozumieć, do jakich zadań model został wytrenowany. Hugging Face prowadzi również LLM Leaderboard, który pokazuje najlepiej działające modele na podstawie określonych metryk.

Jeśli chcesz porównać LLM w różnych typach, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) to kolejne świetne źródło:

![Jakość modelu](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.pl.png)  
Źródło: Artificial Analysis

Jeśli pracujesz nad konkretnym przypadkiem użycia, skuteczne może być wyszukiwanie dostrojonych wersji skoncentrowanych na tej samej dziedzinie. Eksperymentowanie z wieloma otwartymi modelami, aby zobaczyć, jak sprawdzają się w Twoim przypadku i spełniają oczekiwania użytkowników, to również dobra praktyka.

## Kolejne kroki

Najlepsze w otwartych modelach jest to, że można zacząć z nimi pracować bardzo szybko. Sprawdź [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), który zawiera specjalną kolekcję Hugging Face z modelami omówionymi w tej lekcji.

## Nauka się nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji zapoznaj się z naszą [kolekcją nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o generatywnej AI!

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.