# Wprowadzenie do Małych Modeli Językowych dla Generatywnej AI dla Początkujących
Generatywna AI to fascynująca dziedzina sztucznej inteligencji, która skupia się na tworzeniu systemów zdolnych do generowania nowych treści. Treści te mogą obejmować teksty, obrazy, muzykę, a nawet całe wirtualne środowiska. Jednym z najbardziej ekscytujących zastosowań generatywnej AI są modele językowe.

## Czym Są Małe Modele Językowe?

Mały Model Językowy (SLM) to pomniejszona wersja dużego modelu językowego (LLM), wykorzystująca wiele zasad architektonicznych i technik stosowanych w LLM, przy jednocześnie znacznie zmniejszonym zapotrzebowaniu na moc obliczeniową. 

SLM to podzbiór modeli językowych zaprojektowanych do generowania tekstu przypominającego ludzki. W przeciwieństwie do swoich większych odpowiedników, takich jak GPT-4, SLM są bardziej kompaktowe i efektywne, co czyni je idealnymi do zastosowań, gdzie zasoby obliczeniowe są ograniczone. Pomimo mniejszego rozmiaru, mogą wykonywać różnorodne zadania. Zazwyczaj SLM powstają poprzez kompresję lub destylację LLM, dążąc do zachowania znaczącej części funkcjonalności i zdolności językowych oryginalnego modelu. Zmniejszenie rozmiaru modelu obniża ogólną złożoność, czyniąc SLM bardziej wydajnymi pod względem użycia pamięci i wymagań obliczeniowych. Pomimo tych optymalizacji, SLM nadal mogą wykonywać szeroki zakres zadań przetwarzania języka naturalnego (NLP):

- Generowanie tekstu: Tworzenie spójnych i kontekstowo odpowiednich zdań lub akapitów.
- Uzupełnianie tekstu: Przewidywanie i uzupełnianie zdań na podstawie podanego polecenia.
- Tłumaczenie: Przekład tekstu z jednego języka na inny.
- Streszczanie: Skracanie długich tekstów do krótszych, łatwiejszych do przyswojenia podsumowań.

Jednak z pewnymi kompromisami w zakresie wydajności lub głębokości rozumienia w porównaniu do ich większych odpowiedników. 

## Jak Działają Małe Modele Językowe?
SLM są trenowane na ogromnych ilościach danych tekstowych. Podczas treningu uczą się wzorców i struktur języka, co pozwala im generować teksty poprawne gramatycznie i odpowiednie kontekstowo. Proces treningowy obejmuje:

- Zbieranie danych: Gromadzenie dużych zbiorów tekstowych z różnych źródeł.
- Wstępne przetwarzanie: Czyszczenie i organizowanie danych, aby nadawały się do treningu.
- Trening: Wykorzystanie algorytmów uczenia maszynowego do nauczenia modelu zrozumienia i generowania tekstu.
- Dostosowywanie: Modyfikowanie modelu w celu poprawy jego wydajności w określonych zadaniach.

Rozwój SLM odpowiada na rosnące zapotrzebowanie na modele, które mogą być wdrażane w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy platformy edge computing, gdzie pełnowymiarowe LLM mogą być niepraktyczne ze względu na wysokie wymagania zasobowe. Koncentrując się na efektywności, SLM równoważą wydajność z dostępnością, umożliwiając szersze zastosowanie w różnych dziedzinach.

![slm](../../../translated_images/pl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Cele Nauki

W tej lekcji chcemy wprowadzić wiedzę o SLM i połączyć ją z Microsoft Phi-3, aby omówić różne scenariusze w zakresie treści tekstowych, wizji i MoE.

Pod koniec tej lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest SLM?
- Jaka jest różnica między SLM a LLM?
- Czym jest rodzina Microsoft Phi-3/3.5?
- Jak wykonać wnioskowanie z użyciem rodziny Microsoft Phi-3/3.5?

Gotowy? Zaczynajmy.

## Różnice między Dużymi Modelami Językowymi (LLM) a Małymi Modelami Językowymi (SLM)

Zarówno LLM, jak i SLM opierają się na podstawowych zasadach probabilistycznego uczenia maszynowego, stosując podobne podejścia w projektowaniu architektury, metodach treningu, procesach generacji danych i technikach oceny modeli. Jednak kilka kluczowych czynników odróżnia te dwa typy modeli.

## Zastosowania Małych Modeli Językowych

SLM mają szerokie zastosowanie, w tym:

- Chatboty: Zapewnianie wsparcia klienta i angażowanie użytkowników w rozmowę.
- Tworzenie treści: Wspomaganie pisarzy poprzez generowanie pomysłów lub nawet pisanie całych artykułów.
- Edukacja: Pomoc uczniom w pisaniu prac domowych lub nauce nowych języków.
- Dostępność: Tworzenie narzędzi dla osób niepełnosprawnych, takich jak systemy text-to-speech.

**Rozmiar**
  
Główną różnicą między LLM a SLM jest skala modeli. LLM, takie jak ChatGPT (GPT-4), mogą mieć około 1,76 biliona parametrów, podczas gdy modele open-source SLM, takie jak Mistral 7B, zostały zaprojektowane z znacznie mniejszą liczbą parametrów — około 7 miliardów. Ta różnica wynika głównie z odmienności w architekturze i procesach treningowych. Na przykład ChatGPT używa mechanizmu samo-uwagi w ramach modelu typu encoder-decoder, podczas gdy Mistral 7B stosuje uwagą przesuwne (sliding window attention), co umożliwia bardziej efektywny trening w modelu typu decoder-only. Ta architektoniczna różnica ma duże znaczenie dla złożoności i wydajności tych modeli.

**Zrozumienie**

SLM są zwykle optymalizowane pod kątem wydajności w określonych dziedzinach, co czyni je wysoce wyspecjalizowanymi, ale potencjalnie ograniczonymi w zdolności do zapewniania szerokiego kontekstowego rozumienia w wielu obszarach wiedzy. W przeciwieństwie do tego, LLM dążą do symulacji inteligencji podobnej do ludzkiej na bardziej kompleksowym poziomie. Wytrenowane na ogromnych, zróżnicowanych zbiorach danych, LLM są zaprojektowane tak, aby dobrze radzić sobie w różnych domenach, oferując większą wszechstronność i adaptowalność. W konsekwencji LLM są bardziej odpowiednie do szerokiego zakresu zastosowań, takich jak przetwarzanie języka naturalnego i programowanie.

**Zasoby obliczeniowe**

Trening i wdrożenie LLM to procesy wymagające dużych zasobów, często wymagające rozbudowanej infrastruktury obliczeniowej, w tym dużych klastrów GPU. Na przykład trening modelu takiego jak ChatGPT od podstaw może wymagać tysięcy GPU przez dłuższy czas. W porównaniu z tym, SLM ze znacznie mniejszą liczbą parametrów są bardziej dostępne pod względem zasobów obliczeniowych. Modele takie jak Mistral 7B mogą być trenowane i uruchamiane na lokalnych komputerach wyposażonych w umiarkowane możliwości GPU, choć trening nadal wymaga kilku godzin na wielu GPU.

**Stronniczość**

Stronniczość to znany problem w LLM, głównie ze względu na charakter danych treningowych. Modele te często bazują na surowych, ogólnodostępnych danych z internetu, które mogą niedostatecznie reprezentować niektóre grupy, wprowadzać błędne oznaczenia lub odzwierciedlać językowe uprzedzenia związane z dialektem, różnicami geograficznymi i regułami gramatycznymi. Dodatkowo złożoność architektury LLM może niezamierzenie pogłębiać stronniczość, która może pozostać niezauważona bez starannego dostrajania. Z kolei SLM, trenowane na bardziej ograniczonych, specyficznych dla danej dziedziny zbiorach danych, są z natury mniej podatne na takie stronniczości, chociaż nie są od nich całkowicie wolne.

**Wnioskowanie**

Mniejszy rozmiar SLM daje im znaczącą przewagę pod względem szybkości wnioskowania, pozwalając na efektywne generowanie wyników na lokalnym sprzęcie bez potrzeby rozległego równoległego przetwarzania. Z kolei LLM, ze względu na swoją wielkość i złożoność, często wymagają znacznych zasobów równoległych do osiągnięcia akceptowalnego czasu odpowiedzi. Obecność wielu jednoczesnych użytkowników dodatkowo spowalnia czasy reakcji LLM, zwłaszcza przy wdrożeniu na dużą skalę.

Podsumowując, chociaż zarówno LLM, jak i SLM mają podstawy w uczeniu maszynowym, różnią się znacznie pod względem rozmiaru modelu, wymagań zasobowych, rozumienia kontekstu, podatności na stronniczość oraz szybkości wnioskowania. Te różnice odzwierciedlają ich odpowiednią przydatność do różnych zastosowań, gdzie LLM są bardziej wszechstronne, ale zasobożerne, a SLM oferują większą efektywność domenową przy zmniejszonych wymaganiach obliczeniowych.

***Uwaga: W tej lekcji wprowadzimy SLM na przykładzie Microsoft Phi-3 / 3.5.***

## Wprowadzenie Rodziny Phi-3 / Phi-3.5

Rodzina Phi-3 / 3.5 głównie koncentruje się na scenariuszach aplikacyjnych związanych z tekstem, wizją oraz Agentem (MoE):

### Phi-3 / 3.5 Instruct

Głównie do generowania tekstu, uzupełniania rozmów i ekstrakcji informacji z treści itd.

**Phi-3-mini**

Model językowy 3.8B jest dostępny na Microsoft Foundry, Hugging Face i Ollama. Modele Phi-3 znacznie przewyższają modele językowe o podobnej i większej wielkości na kluczowych benchmarkach (zobacz liczby benchmarków poniżej, wyższe oznaczają lepsze). Phi-3-mini przewyższa modele o podwójnej wielkości, podczas gdy Phi-3-small i Phi-3-medium przewyższają większe modele, w tym GPT-3.5.

**Phi-3-small & medium**

Mając zaledwie 7 miliardów parametrów, Phi-3-small pokonuje GPT-3.5T w różnych benchmarkach językowych, logicznych, kodowania i matematyki.

Phi-3-medium z 14 miliardami parametrów kontynuuje ten trend i przewyższa Gemini 1.0 Pro.

**Phi-3.5-mini**

Możemy go traktować jako ulepszenie Phi-3-mini. Choć liczba parametrów pozostaje bez zmian, poprawia możliwość wsparcia wielu języków (obsługuje ponad 20 języków: arabski, chiński, czeski, duński, niderlandzki, angielski, fiński, francuski, niemiecki, hebrajski, węgierski, włoski, japoński, koreański, norweski, polski, portugalski, rosyjski, hiszpański, szwedzki, tajski, turecki, ukraiński) oraz dodaje silniejsze wsparcie dla długiego kontekstu.

Phi-3.5-mini z 3.8 miliardami parametrów przewyższa modele o tym samym rozmiarze i dorównuje modelom o podwójnej wielkości.

### Phi-3 / 3.5 Vision

Możemy traktować model Instruct Phi-3/3.5 jako zdolność Phi do rozumienia, a Vision to oczy Phi, które pozwalają zrozumieć świat.


**Phi-3-Vision**

Phi-3-vision, posiadający tylko 4.2 miliarda parametrów, kontynuuje ten trend i przewyższa większe modele, takie jak Claude-3 Haiku i Gemini 1.0 Pro V w zadaniach ogólnego rozumowania wizualnego, OCR oraz zadań związanych z tabelami i diagramami.


**Phi-3.5-Vision**

Phi-3.5-Vision jest również ulepszeniem Phi-3-Vision, dodającym wsparcie dla wielu obrazów. Możemy to traktować jako ulepszenie w wizji: nie tylko widzi obrazy, ale także filmy.

Phi-3.5-vision przewyższa większe modele, takie jak Claude-3.5 Sonnet oraz Gemini 1.5 Flash w zadaniach OCR, rozumienia tabel i wykresów, a w zadaniach ogólnego rozumienia wizualnego jest na równi. Wspiera jednoczesne wprowadzanie wielu klatek, czyli umożliwia rozumowanie na podstawie wielu obrazów wejściowych.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** pozwala na pretrenowanie modeli przy znacznie mniejszym zużyciu zasobów obliczeniowych, co oznacza, że można dramatycznie zwiększyć rozmiar modelu lub zbioru danych przy tym samym budżecie mocy obliczeniowej, co w modelu gęstym. W szczególności model MoE powinien osiągnąć taką samą jakość, jak jego gęsty odpowiednik, dużo szybciej podczas pretrenowania.

Phi-3.5-MoE składa się z 16 modułów ekspertów 3.8B. Phi-3.5-MoE z jedynie 6.6 miliardami aktywnych parametrów osiąga podobny poziom rozumowania, zrozumienia języka i matematyki jak znacznie większe modele.

Możemy stosować modele rodziny Phi-3/3.5 w zależności od scenariusza. W przeciwieństwie do LLM, Phi-3/3.5-mini lub Phi-3/3.5-Vision można wdrożyć na urządzeniach edge.


## Jak korzystać z modeli rodziny Phi-3/3.5

Chcemy używać Phi-3/3.5 w różnych scenariuszach. Następnie pokażemy użycie Phi-3/3.5 w różnych sytuacjach.

![phi3](../../../translated_images/pl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Wnioskowanie poprzez API w chmurze

**Modele Microsoft Foundry**

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) to bezpośredni zamiennik.

Modele Microsoft Foundry to najprostszy sposób. Możesz szybko uzyskać dostęp do modelu Phi-3/3.5-Instruct przez katalog modeli Foundry. W połączeniu z Azure AI Inference SDK / OpenAI SDK możesz wywołać API przez kod, aby wykonać wywołanie Phi-3/3.5-Instruct. Możesz także testować różne efekty na Playground.

- Demo: Porównanie efektów Phi-3-mini i Phi-3.5-mini w scenariuszach chińskich

![phi3](../../../translated_images/pl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/pl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jeśli chcemy korzystać z modeli wizji i MoE, możemy użyć Microsoft Foundry do wykonania wywołania. Jeśli jesteś zainteresowany, możesz przeczytać Phi-3 Cookbook, aby dowiedzieć się, jak wywoływać Phi-3/3.5 Instruct, Vision i MoE przez Microsoft Foundry [Kliknij ten link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Oprócz katalogu modeli w chmurze Microsoft Foundry, możesz również skorzystać z [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst), by wykonać odpowiednie wywołania. Możesz odwiedzić NVIDIA NIM, aby wykonać wywołania API modeli rodziny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) to zestaw przyspieszonych mikroserwisów inferencyjnych zaprojektowanych, aby pomóc deweloperom efektywnie wdrażać modele AI w różnych środowiskach, w tym w chmurze, centrach danych i stacjach roboczych.

Oto kilka kluczowych cech NVIDIA NIM:

- **Łatwość wdrożenia:** NIM umożliwia wdrożenie modeli AI za pomocą jednego polecenia, ułatwiając integrację z istniejącymi procesami.
- **Optymalizacja wydajności:** Wykorzystuje preoptymalizowane silniki inferencyjne NVIDIA, takie jak TensorRT i TensorRT-LLM, zapewniając niskie opóźnienia i wysoką przepustowość.
- **Skalowalność:** NIM obsługuje autoskalowanie na Kubernetes, skutecznie zarządzając zmiennym obciążeniem.
- **Bezpieczeństwo i kontrola:** Organizacje mogą zachować kontrolę nad swoimi danymi i aplikacjami, samodzielnie hostując mikroserwisy NIM na własnej zarządzanej infrastrukturze.
- **Standardowe API:** NIM zapewnia standardowe w branży API, co ułatwia budowanie i integrowanie aplikacji AI, takich jak chatboty, asystenci AI i inne.

NIM jest częścią NVIDIA AI Enterprise, której celem jest uproszczenie wdrażania i operacjonalizacji modeli AI, zapewniając ich efektywne działanie na GPU NVIDIA.

- Demo: Używanie NVIDIA NIM do wywołania Phi-3.5-Vision-API  [[Kliknij ten link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Uruchamianie Phi-3/3.5 lokalnie
Inferencja w kontekście Phi-3 lub dowolnego modelu językowego, takiego jak GPT-3, odnosi się do procesu generowania odpowiedzi lub przewidywań na podstawie otrzymanego wejścia. Gdy podajesz pytanie lub zapytanie do Phi-3, wykorzystuje on wytrenowaną sieć neuronową, aby wywnioskować najbardziej prawdopodobną i istotną odpowiedź poprzez analizę wzorców i zależności w danych, na których był trenowany.

**Hugging Face Transformer**
Hugging Face Transformers to potężna biblioteka zaprojektowana do przetwarzania języka naturalnego (NLP) i innych zadań uczenia maszynowego. Oto kilka kluczowych informacji na jej temat:

1. **Wstępnie wytrenowane modele:** Dostarcza tysiące wstępnie wytrenowanych modeli, które można wykorzystać do różnych zadań, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych bytów, odpowiadanie na pytania, streszczanie, tłumaczenie czy generowanie tekstu.

2. **Interoperacyjność frameworków:** Biblioteka wspiera wiele frameworków uczenia głębokiego, w tym PyTorch, TensorFlow i JAX. Pozwala to na wytrenowanie modelu w jednym frameworku i użycie go w innym.

3. **Możliwości multimodalne:** Poza NLP, Hugging Face Transformers wspiera również zadania w zakresie wizji komputerowej (np. klasyfikacja obrazów, wykrywanie obiektów) oraz przetwarzania dźwięku (np. rozpoznawanie mowy, klasyfikacja dźwięku).

4. **Łatwość użycia:** Biblioteka oferuje API i narzędzia do łatwego pobierania i dostrajania modeli, co czyni ją dostępną zarówno dla początkujących, jak i ekspertów.

5. **Społeczność i zasoby:** Hugging Face posiada aktywną społeczność, obszerną dokumentację, samouczki i przewodniki, które pomagają użytkownikom zacząć i w pełni wykorzystać bibliotekę.
[oficjalna dokumentacja](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) lub ich [repozytorium GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To jest najczęściej używana metoda, ale wymaga także akceleracji przez GPU. W końcu scenariusze takie jak Vision i MoE wymagają wielu obliczeń, które na CPU będą bardzo powolne, jeśli nie zostaną pocięte na kwanty.


- Demo: Użycie Transformer do wywołania Phi-3.5-Instruct [Kliknij ten link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Użycie Transformer do wywołania Phi-3.5-Vision [Kliknij ten link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Użycie Transformer do wywołania Phi-3.5-MoE [Kliknij ten link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) to platforma zaprojektowana, aby ułatwić uruchamianie dużych modeli językowych (LLM) lokalnie na twoim komputerze. Obsługuje różne modele, takie jak Llama 3.1, Phi 3, Mistral i Gemma 2, między innymi. Platforma upraszcza proces, łącząc wagi modeli, konfigurację i dane w jeden pakiet, co ułatwia użytkownikom dostosowywanie i tworzenie własnych modeli. Ollama jest dostępna na macOS, Linux i Windows. To świetne narzędzie, jeśli chcesz eksperymentować z LLM lub wdrożyć je bez polegania na usługach chmurowych. Ollama jest najprostszą drogą, wystarczy wykonać następujące polecenie.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) to środowisko uruchomieniowe offline na urządzeniu firmy Microsoft do uruchamiania modeli takich jak Phi całkowicie na twoim sprzęcie — bez subskrypcji Azure, klucza API czy połączenia sieciowego. Automatycznie wybiera najlepszy dostępny dostawca wykonania (NPU, GPU lub CPU) i udostępnia zgodny z OpenAI endpoint, dzięki czemu istniejący kod `openai`/Azure AI Inference SDK może z niego korzystać przy minimalnych zmianach. Zobacz [dokumentację Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), aby zacząć.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Lub użyj SDK bezpośrednio w Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime dla GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) to wieloplatformowy akcelerator inferencji i treningu uczenia maszynowego. ONNX Runtime dla Generative AI (GENAI) to potężne narzędzie, które pomaga efektywnie uruchamiać modele generatywnej AI na różnych platformach.

## Czym jest ONNX Runtime?
ONNX Runtime to projekt open-source umożliwiający wysokowydajną inferencję modeli uczenia maszynowego. Obsługuje modele w formacie Open Neural Network Exchange (ONNX), który jest standardem reprezentacji modeli uczenia maszynowego. Inferencja za pomocą ONNX Runtime może zapewnić szybsze doświadczenia dla klientów i niższe koszty, wspierając modele z głębokich frameworków uczenia, takich jak PyTorch i TensorFlow/Keras, a także klasyczne biblioteki uczenia maszynowego, takie jak scikit-learn, LightGBM, XGBoost itd. ONNX Runtime jest kompatybilny z różnym sprzętem, sterownikami i systemami operacyjnymi, i zapewnia optymalną wydajność, wykorzystując przy tym akceleratory sprzętowe tam, gdzie to możliwe, wraz z optymalizacjami grafu i transformacjami.

## Czym jest Generative AI?
Generative AI odnosi się do systemów AI, które potrafią generować nowe treści, takie jak tekst, obrazy czy muzyka, na podstawie danych, na których zostały wytrenowane. Przykładami są modele językowe takie jak GPT-3 oraz modele generowania obrazów, na przykład Stable Diffusion. Biblioteka ONNX Runtime dla GenAI zapewnia pętlę generatywnej AI dla modeli ONNX, włączając inferencję z ONNX Runtime, przetwarzanie logitów, wyszukiwanie i próbkowanie, oraz zarządzanie pamięcią KV cache.

## ONNX Runtime dla GENAI
ONNX Runtime dla GENAI rozszerza możliwości ONNX Runtime o wsparcie dla modeli generatywnej AI. Oto kilka kluczowych cech:

- **Szerokie wsparcie platform:** Działa na różnych platformach, w tym Windows, Linux, macOS, Android i iOS.
- **Wsparcie modeli:** Obsługuje wiele popularnych modeli generatywnej AI, takich jak LLaMA, GPT-Neo, BLOOM i inne.
- **Optymalizacja wydajności:** Zawiera optymalizacje dla różnych akceleratorów sprzętowych, takich jak GPU NVIDIA, GPU AMD i inne2.
- **Łatwość użycia:** Zapewnia API do prostej integracji z aplikacjami, pozwalając generować tekst, obrazy i inne treści przy minimalnym kodzie.
- Użytkownicy mogą wywoływać wysokopoziomową metodę generate(), lub wykonywać każdą iterację modelu w pętli, generując jeden token na raz i opcjonalnie aktualizując parametry generowania wewnątrz pętli.
- ONNX runtime obsługuje również zachłanne/wyszukiwanie wiązkowe oraz próbkowanie TopP, TopK do generowania sekwencji tokenów i wbudowane przetwarzanie logitów, takie jak kary za powtórzenia. Można też łatwo dodać własne ocenianie.

## Zaczynamy
Aby zacząć korzystać z ONNX Runtime dla GENAI, wykonaj następujące kroki:

### Zainstaluj ONNX Runtime:
```Python
pip install onnxruntime
```
### Zainstaluj rozszerzenia Generative AI:
```Python
pip install onnxruntime-genai
```

### Uruchom model: Oto prosty przykład w Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Używanie ONNX Runtime GenAI do wywołania Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Inne**

Oprócz metod referencyjnych ONNX Runtime, Ollama i Foundry Local, możemy również uzupełnić odniesienia do modeli kwantowych na podstawie metod referencyjnych modeli dostarczanych przez różnych producentów. Takich jak Apple MLX framework z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO z CPU/GPU itp. Więcej treści znajdziesz także w [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Więcej

Poznaliśmy podstawy rodziny Phi-3/3.5, ale aby dowiedzieć się więcej o SLM potrzebujemy większej wiedzy. Odpowiedzi znajdziesz w Phi-3 Cookbook. Jeśli chcesz dowiedzieć się więcej, odwiedź [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->