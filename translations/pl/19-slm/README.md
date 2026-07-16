# Wprowadzenie do Małych Modeli Językowych dla Generatywnej AI dla Początkujących
Generatywna AI to fascynująca dziedzina sztucznej inteligencji, która skupia się na tworzeniu systemów zdolnych do generowania nowej treści. Treść ta może obejmować teksty, obrazy, muzykę, a nawet całe wirtualne środowiska. Jednym z najbardziej ekscytujących zastosowań generatywnej AI są modele językowe.

## Czym są Małe Modele Językowe?

Mały Model Językowy (SLM) to mniejsza wersja dużego modelu językowego (LLM), wykorzystująca wiele architektonicznych zasad i technik LLM, jednocześnie charakteryzująca się znacznie mniejszym zapotrzebowaniem na zasoby obliczeniowe.

SLM to podzbiór modeli językowych zaprojektowanych do generowania tekstu przypominającego ludzki. W przeciwieństwie do swoich większych odpowiedników, takich jak GPT-4, SLM są bardziej kompaktowe i efektywne, co czyni je idealnymi do zastosowań, w których zasoby obliczeniowe są ograniczone. Mimo mniejszego rozmiaru, mogą wykonywać różnorodne zadania. Typowo SLM powstają poprzez kompresję lub destylację LLM, starając się zachować znaczną część funkcjonalności i zdolności językowych oryginalnego modelu. Zmniejszenie rozmiaru modelu redukuje jego złożoność, co sprawia, że SLM są bardziej efektywne pod względem wykorzystania pamięci i wymagań obliczeniowych. Pomimo tych optymalizacji, SLM mogą realizować szeroki zakres zadań przetwarzania języka naturalnego (NLP):

- Generowanie Tekstu: Tworzenie spójnych i kontekstowo odpowiednich zdań lub akapitów.
- Uzupełnianie Tekstu: Przewidywanie i uzupełnianie zdań na podstawie podanego promptu.
- Tłumaczenie: Konwersja tekstu z jednego języka na inny.
- Streszczanie: Kondensowanie długich tekstów do krótszych, łatwiejszych do przyswojenia podsumowań.

Choć wiąże się to z pewnymi kompromisami w zakresie wydajności lub głębokości rozumienia w porównaniu do większych modeli.

## Jak działają Małe Modele Językowe?
SLM są trenowane na ogromnych zbiorach danych tekstowych. Podczas treningu uczą się wzorców i struktur języka, co umożliwia im generowanie tekstu poprawnego gramatycznie i odpowiedniego kontekstowo. Proces treningu obejmuje:

- Zbiór danych: Gromadzenie dużych zbiorów tekstów z różnych źródeł.
- Wstępna obróbka: Czyszczenie i organizowanie danych, aby były odpowiednie do treningu.
- Trening: Uczenie modelu za pomocą algorytmów uczenia maszynowego, jak rozumieć i generować tekst.
- Dostosowywanie: Dopasowywanie modelu w celu poprawy jego wyników w określonych zadaniach.

Rozwój SLM odpowiada na rosnącą potrzebę modeli, które mogą być wdrażane w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy platformy edge computing, gdzie LLM na pełną skalę mogą być niepraktyczne z powodu dużych wymagań zasobowych. Skupiając się na efektywności, SLM łączą wydajność z dostępnością, umożliwiając szersze zastosowanie w różnych dziedzinach.

![slm](../../../translated_images/pl/slm.4058842744d0444a.webp)

## Cele Nauki

W tej lekcji chcemy wprowadzić wiedzę o SLM i połączyć ją z Microsoft Phi-3, aby poznać różne scenariusze w tekstach, wizji i MoE.

Po zakończeniu tej lekcji powinieneś umieć odpowiedzieć na następujące pytania:

- Czym jest SLM?
- Jaka jest różnica między SLM a LLM?
- Czym jest rodzina Microsoft Phi-3/3.5?
- Jak przeprowadzić inferencję z rodziną Microsoft Phi-3/3.5?

Gotowy? Zaczynajmy.

## Różnice między Dużymi Modelami Językowymi (LLM) a Małymi Modelami Językowymi (SLM)

Zarówno LLM, jak i SLM opierają się na podstawowych zasadach probabilistycznego uczenia maszynowego, stosując podobne podejścia w architekturze, metodach treningu, procesach generowania danych i technikach oceny modeli. Jednak kilka kluczowych czynników wyróżnia te dwa typy modeli.

## Zastosowania Małych Modeli Językowych

SLM znajdują szerokie zastosowania, w tym:

- Chatboty: Zapewnianie wsparcia klienta i komunikacja z użytkownikami w formie rozmowy.
- Tworzenie treści: Wspomaganie pisarzy w generowaniu pomysłów lub nawet tworzeniu całych artykułów.
- Edukacja: Pomoc uczniom w zadaniach pisemnych lub nauce nowych języków.
- Dostępność: Tworzenie narzędzi dla osób z niepełnosprawnościami, takich jak systemy tekst-na-mowę.

**Rozmiar**
  
Podstawową różnicą między LLM a SLM jest skala modeli. LLM, takie jak ChatGPT (GPT-4), mogą mieć około 1,76 biliona parametrów, podczas gdy otwarte SLM jak Mistral 7B mają znacznie mniej parametrów — około 7 miliardów. Ta różnica wynika głównie z różnic w architekturze modelu i procesach treningowych. Na przykład ChatGPT stosuje mechanizm samo-uwagi w ramach architektury encoder-decoder, podczas gdy Mistral 7B korzysta z uwagi na przesuwanym oknie, co pozwala na bardziej efektywny trening w modelu typu decoder-only. Ta architektoniczna odmiana ma głęboki wpływ na złożoność i wydajność tych modeli.

**Rozumienie**

SLM są zwykle optymalizowane pod kątem wydajności w określonych domenach, przez co są wysoce wyspecjalizowane, ale mogą mieć ograniczoną zdolność do szerokiego rozumienia kontekstów w wielu dziedzinach wiedzy. W przeciwieństwie do nich LLM dążą do symulacji inteligencji na bardziej wszechstronnym poziomie. Trenowane na ogromnych, zróżnicowanych zbiorach danych, LLM są zaprojektowane, by dobrze działać w wielu dziedzinach, oferując większą wszechstronność i adaptowalność. W konsekwencji LLM nadają się do szerszego zakresu zadań końcowych, takich jak przetwarzanie języka naturalnego i programowanie.

**Obliczenia**

Trening i wdrożenie LLM to zasobochłonne procesy, często wymagające dużej infrastruktury obliczeniowej, w tym klastrów GPU na dużą skalę. Na przykład trenowanie modelu takiego jak ChatGPT od podstaw może wymagać tysięcy GPU przez długi czas. W przeciwieństwie do tego SLM, z mniejszą liczbą parametrów, są bardziej dostępne pod względem zasobów obliczeniowych. Modele takie jak Mistral 7B mogą być trenowane i uruchamiane na lokalnych maszynach wyposażonych w umiarkowane możliwości GPU, choć trening nadal wymaga kilku godzin na wielu GPU.

**Stronniczość**

Stronniczość jest znanym problemem LLM, głównie ze względu na charakter danych treningowych. Modele te często opierają się na surowych, publicznie dostępnych danych z internetu, które mogą niedostatecznie reprezentować lub niewłaściwie przedstawiać niektóre grupy, wprowadzać błędne oznakowanie lub odzwierciedlać lingwistyczne uprzedzenia wynikające z dialektów, różnic geograficznych i zasad gramatycznych. Dodatkowo złożoność architektur LLM może niezamierzenie zwiększać stronniczość, która może pozostać niezauważona bez dokładnego dostrajania. Natomiast SLM, trenowane na ograniczonych, specyficznych dla domeny zbiorach danych, są z natury mniej podatne na takie uprzedzenia, choć nie są ich całkowicie wolne.

**Inferencja**

Mniejszy rozmiar SLM daje im znaczącą przewagę w szybkości inferencji, pozwalając na efektywne generowanie wyników na lokalnym sprzęcie bez potrzeby intensywnego przetwarzania równoległego. W przeciwieństwie do tego LLM, ze względu na ich rozmiar i złożoność, często wymagają dużych zasobów obliczeniowych działających równolegle, aby osiągnąć akceptowalne czasy inferencji. Obecność wielu jednoczesnych użytkowników dodatkowo spowalnia czas odpowiedzi LLM, zwłaszcza przy wdrożeniu na dużą skalę.

Podsumowując, chociaż zarówno LLM, jak i SLM mają wspólne podstawy w uczeniu maszynowym, różnią się znacznie pod względem rozmiaru modelu, wymagań zasobowych, rozumienia kontekstu, podatności na stronniczość i szybkości inferencji. Różnice te odzwierciedlają ich odpowiednią przydatność do różnych zastosowań, przy czym LLM są bardziej uniwersalne, ale zasobochłonne, a SLM oferują większą efektywność w określonych domenach przy mniejszych wymaganiach obliczeniowych.

***Uwaga: W tej lekcji wprowadzimy SLM na przykładzie Microsoft Phi-3 / 3.5.***

## Przedstawienie rodziny Phi-3 / Phi-3.5

Rodzina Phi-3 / 3.5 koncentruje się głównie na scenariuszach zastosowań związanych z tekstem, wizją i Agentem (MoE):

### Phi-3 / 3.5 Instruct

Głównie do generowania tekstu, uzupełniania rozmów i ekstrakcji informacji z treści itp.

**Phi-3-mini**

Model językowy o 3,8 miliardach parametrów jest dostępny na Microsoft Foundry, Hugging Face i Ollama. Modele Phi-3 znacząco przewyższają modele językowe o równej lub większej wielkości w kluczowych benchmarkach (patrz poniższe wyniki benchmarków, wyższe liczby oznaczają lepsze wyniki). Phi-3-mini przewyższa modele dwukrotnie większe, podczas gdy Phi-3-small i Phi-3-medium wygrywają z większymi modelami, w tym GPT-3.5.

**Phi-3-small & medium**

Przy zaledwie 7 miliardach parametrów, Phi-3-small pokonuje GPT-3.5T w różnych benchmarkach językowych, rozumowania, kodowania i matematyki.

Phi-3-medium z 14 miliardami parametrów kontynuuje ten trend i przewyższa Gemini 1.0 Pro.

**Phi-3.5-mini**

Możemy go traktować jako ulepszoną wersję Phi-3-mini. Chociaż liczba parametrów pozostaje bez zmian, model poprawia wsparcie dla wielu języków (obsługuje ponad 20 języków: arabski, chiński, czeski, duński, holenderski, angielski, fiński, francuski, niemiecki, hebrajski, węgierski, włoski, japoński, koreański, norweski, polski, portugalski, rosyjski, hiszpański, szwedzki, tajski, turecki, ukraiński) oraz dodaje silniejsze wsparcie dla długiego kontekstu.

Phi-3.5-mini z 3,8 miliarda parametrów przewyższa modele o tym samym rozmiarze i jest porównywalny do modeli dwukrotnie większych.

### Phi-3 / 3.5 Vision

Możemy traktować model Instruct Phi-3/3.5 jako zdolność Phi do rozumienia, a Vision to oczy Phi umożliwiające zrozumienie świata.


**Phi-3-Vision**

Phi-3-vision, zaledwie z 4,2 miliardami parametrów, kontynuuje ten trend i przewyższa większe modele takie jak Claude-3 Haiku i Gemini 1.0 Pro V w zadaniach ogólnego rozumowania wizualnego, OCR oraz rozumienia tabel i diagramów.


**Phi-3.5-Vision**

Phi-3.5-Vision jest również ulepszeniem Phi-3-Vision, dodając obsługę wielu obrazów. Można go traktować jako ulepszenie wizji, pozwalając widzieć nie tylko obrazy, ale także filmy.

Phi-3.5-vision przewyższa większe modele takie jak Claude-3.5 Sonnet i Gemini 1.5 Flash w zadaniach OCR, rozumienia tabel i wykresów oraz jest porównywalny w zadaniach ogólnego rozumienia wizualnego. Obsługuje wieloklatkowe wejście, czyli umożliwia rozumowanie na podstawie wielu obrazów.


### Phi-3.5-MoE

***Mieszanka ekspertów (MoE)*** pozwala na trenowanie modeli z dużo mniejszym zapotrzebowaniem na obliczenia, co oznacza, że można dramatycznie zwiększać rozmiar modelu lub zbioru danych przy tym samym budżecie obliczeniowym co model gęsty. W szczególności model MoE powinien osiągnąć tę samą jakość co jego odpowiednik gęsty znacznie szybciej podczas wstępnego treningu.

Phi-3.5-MoE składa się z 16x3,8 miliardowych modułów ekspertów. Phi-3.5-MoE z zaledwie 6,6 miliardami aktywnych parametrów osiąga poziom rozumowania, rozumienia języka i matematyki porównywalny z dużo większymi modelami.

Możemy używać modeli rodziny Phi-3/3.5 w różnych scenariuszach. W przeciwieństwie do LLM, Phi-3/3.5-mini lub Phi-3/3.5-Vision można wdrażać na urządzeniach brzegowych.


## Jak korzystać z modeli rodziny Phi-3/3.5

Chcemy używać Phi-3/3.5 w różnych scenariuszach. Następnie wykorzystamy Phi-3/3.5 w zależności od sytuacji.

![phi3](../../../translated_images/pl/phi3.655208c3186ae381.webp)

### Inferencja przez API w chmurze

**Modele Microsoft Foundry**

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) są bezpośrednim zamiennikiem.

Microsoft Foundry Models to najbardziej bezpośrednia metoda. Możesz szybko uzyskać dostęp do modelu Phi-3/3.5-Instruct poprzez katalog modeli Foundry. W połączeniu z Azure AI Inference SDK / OpenAI SDK, możesz wywołać API przez kod, aby wykonać zapytanie do Phi-3/3.5-Instruct. Możesz także testować różne efekty za pomocą Playground.

- Demo: Porównanie efektów Phi-3-mini i Phi-3.5-mini w scenariuszach chińskich

![phi3](../../../translated_images/pl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Jeśli chcemy korzystać z modeli wizji i MoE, możemy skorzystać z Microsoft Foundry do wykonania wywołania. Jeśli jesteś zainteresowany, możesz przeczytać Phi-3 Cookbook, by dowiedzieć się, jak wywoływać Phi-3/3.5 Instruct, Vision, MoE przez Microsoft Foundry [Kliknij ten link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Oprócz katalogu chmurowych modeli Microsoft Foundry, możesz również używać [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) do wykonania odpowiednich wywołań. Możesz odwiedzić NVIDIA NIM, aby wywołać API z rodziny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) to zestaw przyspieszonych mikroserwisów inferencyjnych, zaprojektowanych, by pomóc deweloperom w efektywnym wdrażaniu modeli AI w różnych środowiskach, w tym w chmurach, centrach danych i stacjach roboczych.

Oto kilka kluczowych cech NVIDIA NIM:

- **Łatwość wdrożenia:** NIM pozwala na wdrożenie modeli AI z użyciem jednego polecenia, co ułatwia integrację z istniejącymi procesami.

- **Optymalna wydajność:** Wykorzystuje wstępnie zoptymalizowane silniki inferencyjne NVIDIA, takie jak TensorRT i TensorRT-LLM, aby zapewnić niskie opóźnienia i wysoką przepustowość.
- **Skalowalność:** NIM obsługuje autoskalowanie na Kubernetes, co umożliwia efektywne radzenie sobie z różnymi obciążeniami.
- **Bezpieczeństwo i kontrola:** Organizacje mogą zachować kontrolę nad swoimi danymi i aplikacjami, korzystając z samodzielnego hostowania mikrousług NIM na własnej zarządzanej infrastrukturze.
- **Standardowe API:** NIM oferuje branżowe standardowe API, co ułatwia tworzenie i integrację aplikacji AI, takich jak chatboty, asystenci AI i inne.

NIM jest częścią NVIDIA AI Enterprise, którego celem jest uproszczenie wdrażania i eksploatacji modeli AI, zapewniając ich efektywne działanie na GPU NVIDIA.

- Demo: Korzystanie z NVIDIA NIM do wywołania Phi-3.5-Vision-API [[Kliknij ten link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Uruchamianie Phi-3/3.5 lokalnie
Inferencja w odniesieniu do Phi-3 lub dowolnego modelu językowego, takiego jak GPT-3, to proces generowania odpowiedzi lub prognoz na podstawie otrzymanego wejścia. Gdy dostarczasz zapytanie lub polecenie Phi-3, wykorzystuje on swoją wytrenowaną sieć neuronową do inferencji najbardziej prawdopodobnej i istotnej odpowiedzi, analizując wzorce i relacje w danych, na których był trenowany.

**Hugging Face Transformer**
Hugging Face Transformers to potężna biblioteka zaprojektowana do przetwarzania języka naturalnego (NLP) oraz innych zadań związanych z uczeniem maszynowym. Oto kilka kluczowych informacji na jej temat:

1. **Modele wstępnie wytrenowane:** Udostępnia tysiące modeli wstępnie wytrenowanych, które można wykorzystać do różnych zadań, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych encji, odpowiadanie na pytania, streszczanie, tłumaczenie i generowanie tekstu.

2. **Interoperacyjność frameworków:** Biblioteka obsługuje wiele frameworków uczenia głębokiego, w tym PyTorch, TensorFlow i JAX. Pozwala to na trenowanie modelu w jednym frameworku i używanie go w innym.

3. **Możliwości multimodalne:** Poza NLP, Hugging Face Transformers wspiera również zadania z dziedziny wizji komputerowej (np. klasyfikacja obrazów, wykrywanie obiektów) oraz przetwarzania dźwięku (np. rozpoznawanie mowy, klasyfikacja audio).

4. **Łatwość użycia:** Biblioteka oferuje API i narzędzia do łatwego pobierania i dostrajania modeli, co czyni ją dostępną zarówno dla początkujących, jak i ekspertów.

5. **Społeczność i zasoby:** Hugging Face ma aktywną społeczność oraz obszerne dokumentacje, samouczki i przewodniki, które pomagają użytkownikom rozpocząć pracę i maksymalnie wykorzystać bibliotekę.
[oficjalna dokumentacja](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) lub ich [repozytorium GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To jest najczęściej używana metoda, ale wymaga ona akceleracji GPU. W końcu scenariusze takie jak Vision i MoE wymagają wielu obliczeń, które będą bardzo wolne na CPU, jeśli nie są kwantyzowane.


- Demo: Korzystanie z Transformer do wywołania Phi-3.5-Instruct [Kliknij ten link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korzystanie z Transformer do wywołania Phi-3.5-Vision [Kliknij ten link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Korzystanie z Transformer do wywołania Phi-3.5-MoE [Kliknij ten link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) to platforma zaprojektowana, aby ułatwić uruchamianie dużych modeli językowych (LLM) lokalnie na twoim komputerze. Obsługuje różne modele, takie jak Llama 3.1, Phi 3, Mistral i Gemma 2, między innymi. Platforma upraszcza proces, łącząc wagi modelu, konfigurację i dane w jeden pakiet, co ułatwia użytkownikom dostosowywanie i tworzenie własnych modeli. Ollama jest dostępna dla macOS, Linux i Windows. To świetne narzędzie, jeśli chcesz eksperymentować z LLM lub wdrażać je bez korzystania z usług chmurowych. Ollama jest najprostszą metodą, wystarczy wykonać następujące polecenie.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) to offline’owe środowisko uruchomieniowe Microsoft do wykonywania modeli takich jak Phi całkowicie na własnym sprzęcie – bez potrzeby subskrypcji Azure, klucza API czy połączenia sieciowego. Automatycznie wybiera najlepszego dostępnego dostawcę wykonania (NPU, GPU lub CPU) i udostępnia punkt końcowy kompatybilny z OpenAI, aby istniejący kod `openai`/Azure AI Inference SDK mógł być używany bez większych zmian. Zobacz [dokumentację Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), aby zacząć.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Lub użyj SDK bezpośrednio w Pythonie:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) to wieloplatformowy akcelerator inferencji i trenowania uczenia maszynowego. ONNX Runtime for Generative AI (GENAI) to potężne narzędzie, które pomaga efektywnie uruchamiać modele generatywnej AI na różnych platformach.

## Co to jest ONNX Runtime?
ONNX Runtime to projekt open-source umożliwiający wysokowydajną inferencję modeli uczenia maszynowego. Obsługuje modele w formacie Open Neural Network Exchange (ONNX), który jest standardem do reprezentacji modeli uczenia maszynowego. Inferencja z użyciem ONNX Runtime może przyspieszyć doświadczenia klientów i obniżyć koszty, wspierając modele z frameworków uczenia głębokiego, takich jak PyTorch i TensorFlow/Keras, a także klasyczne biblioteki uczenia maszynowego, takie jak scikit-learn, LightGBM, XGBoost itd. ONNX Runtime jest kompatybilny z różnym sprzętem, sterownikami i systemami operacyjnymi, zapewniając optymalną wydajność dzięki wykorzystaniu akceleratorów sprzętowych tam, gdzie to możliwe, wraz z optymalizacjami i przekształceniami grafów.

## Co to jest Generative AI?
Generatywna AI odnosi się do systemów AI, które potrafią generować nowe treści, takie jak tekst, obrazy czy muzyka, na podstawie danych, na których były trenowane. Przykładami są modele językowe takie jak GPT-3 oraz modele generowania obrazów, takie jak Stable Diffusion. Biblioteka ONNX Runtime for GenAI zapewnia pętlę generatywnej AI dla modeli ONNX, włączając inferencję z ONNX Runtime, przetwarzanie logitsów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią podręczną KV.

## ONNX Runtime dla GENAI
ONNX Runtime for GENAI rozszerza możliwości ONNX Runtime, aby obsługiwać modele generatywnej AI. Oto kilka kluczowych funkcji:

- **Szerokie wsparcie platform:** Działa na różnych platformach, w tym Windows, Linux, macOS, Android i iOS.
- **Wsparcie modeli:** Obsługuje wiele popularnych modeli generatywnej AI, takich jak LLaMA, GPT-Neo, BLOOM i inne.
- **Optymalizacja wydajności:** Zawiera optymalizacje dla różnych akceleratorów sprzętowych, takich jak GPU NVIDIA, GPU AMD i więcej.
- **Łatwość użycia:** Udostępnia API do łatwej integracji z aplikacjami, umożliwiając generowanie tekstu, obrazów i innych treści przy minimalnym kodzie.
- Użytkownicy mogą wywołać metodę generate() na wysokim poziomie, lub uruchamiać każdą iterację modelu w pętli, generując po jednym tokenie na raz oraz opcjonalnie aktualizując parametry generowania w pętli.
- ONNX Runtime obsługuje również wyszukiwanie zachłanne, beam search oraz próbkowanie TopP, TopK do generowania sekwencji tokenów oraz wbudowane przetwarzanie logitsów, takie jak kary za powtarzanie. Można także łatwo dodać własne metryki oceny.

## Rozpoczęcie pracy
Aby rozpocząć pracę z ONNX Runtime dla GENAI, można postępować zgodnie z następującymi krokami:

### Zainstaluj ONNX Runtime:
```Python
pip install onnxruntime
```
### Zainstaluj rozszerzenia Generative AI:
```Python
pip install onnxruntime-genai
```

### Uruchom model: Oto prosty przykład w Pythonie:
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
### Demo: Użycie ONNX Runtime GenAI do wywołania Phi-3.5-Vision


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

Oprócz ONNX Runtime, Ollama i Foundry Local jako metod referencyjnych, możemy również uzupełnić referencje modeli kwantowanych na podstawie metod referencyjnych dostarczonych przez różnych producentów. Na przykład framework Apple MLX z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO z CPU/GPU itd. Więcej treści znajdziesz również w [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Więcej

Poznaliśmy podstawy rodziny Phi-3/3.5, ale aby dowiedzieć się więcej o SLM, potrzebujemy większej wiedzy. Odpowiedzi znajdziesz w Phi-3 Cookbook. Jeśli chcesz dowiedzieć się więcej, odwiedź [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->