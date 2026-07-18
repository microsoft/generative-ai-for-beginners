# Wprowadzenie do Małych Modeli Językowych dla Generatywnej AI dla Początkujących
Generatywna AI to fascynująca dziedzina sztucznej inteligencji, która koncentruje się na tworzeniu systemów zdolnych do generowania nowych treści. Te treści mogą obejmować teksty i obrazy, muzykę, a nawet całe wirtualne środowiska. Jednym z najbardziej ekscytujących zastosowań generatywnej AI są modele językowe.

## Czym Są Małe Modele Językowe?

Mały Model Językowy (SLM) to zmniejszona wersja dużego modelu językowego (LLM), wykorzystująca wiele zasad architektonicznych i technik LLM, jednocześnie wykazując znacznie mniejsze zapotrzebowanie na moc obliczeniową.

SLM to podzbiór modeli językowych zaprojektowanych do generowania tekstu przypominającego ludzki. W przeciwieństwie do ich większych odpowiedników, takich jak GPT-4, SLM są bardziej kompaktowe i wydajne, co czyni je idealnymi do zastosowań, gdzie zasoby obliczeniowe są ograniczone. Mimo mniejszego rozmiaru potrafią wykonywać różnorodne zadania. Zazwyczaj SLM są tworzone przez kompresję lub destylację LLM, dążąc do zachowania znacznej części oryginalnej funkcjonalności i zdolności językowych modelu. Zmniejszenie rozmiaru modelu redukuje ogólną złożoność, czyniąc SLM bardziej wydajnymi zarówno pod względem użycia pamięci, jak i wymagań obliczeniowych. Pomimo tych optymalizacji, SLM mogą wykonywać szeroki zakres zadań przetwarzania języka naturalnego (NLP):

- Generowanie tekstu: Tworzenie spójnych i kontekstowo odpowiednich zdań lub akapitów.
- Uzupełnianie tekstu: Przewidywanie i uzupełnianie zdań na podstawie podanego promptu.
- Tłumaczenie: Przekładanie tekstu z jednego języka na inny.
- Streszczanie: Skracanie długich fragmentów tekstu do krótszych, bardziej przystępnych streszczeń.

Choć z pewnymi kompromisami w wydajności lub głębokości rozumienia w porównaniu do ich większych odpowiedników.

## Jak Działają Małe Modele Językowe?
SLM są trenowane na ogromnych zbiorach danych tekstowych. Podczas treningu uczą się wzorców i struktur języka, co pozwala im generować tekst zarówno gramatycznie poprawny, jak i kontekstowo odpowiedni. Proces treningu obejmuje:

- Zbieranie danych: Gromadzenie dużych zestawów tekstowych z różnych źródeł.
- Wstępne przetwarzanie: Czyszczenie i organizowanie danych, aby były odpowiednie do treningu.
- Trening: Wykorzystanie algorytmów uczenia maszynowego do nauczania modelu rozumienia i generowania tekstu.
- Fine-tuning: Dostosowywanie modelu w celu poprawy jego wydajności w konkretnych zadaniach.

Rozwój SLM odpowiada rosnącemu zapotrzebowaniu na modele, które można wdrażać w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy platformy edge computing, gdzie pełne modele LLM mogą być niepraktyczne ze względu na duże wymagania zasobowe. Skupiając się na wydajności, SLM balansują między wydajnością a dostępnością, umożliwiając szersze zastosowanie w różnych dziedzinach.

![slm](../../../translated_images/pl/slm.4058842744d0444a.webp)

## Cele Nauki

W tej lekcji mamy nadzieję wprowadzić wiedzę na temat SLM i połączyć ją z Microsoft Phi-3, aby poznać różne scenariusze w generowaniu tekstu, wizji i MoE.

Pod koniec lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest SLM?
- Jaka jest różnica między SLM a LLM?
- Czym jest rodzina Microsoft Phi-3/3.5?
- Jak uruchomić inferencję z użyciem rodziny Microsoft Phi-3/3.5?

Gotowy? Zaczynajmy.

## Różnice między Dużymi Modelami Językowymi (LLM) a Małymi Modelami Językowymi (SLM)

Zarówno LLM, jak i SLM opierają się na podstawowych zasadach probabilistycznego uczenia maszynowego, stosując podobne podejścia do projektowania architektury, metod treningowych, procesów generowania danych oraz technik oceny modeli. Jednak kilka kluczowych czynników odróżnia te dwa typy modeli.

## Zastosowania Małych Modeli Językowych

SLM mają szeroki zakres zastosowań, w tym:

- Chatboty: Zapewnianie wsparcia klienta i interakcja z użytkownikami w formie konwersacji.
- Tworzenie treści: Pomoc pisarzom poprzez generowanie pomysłów lub nawet tworzenie całych artykułów.
- Edukacja: Pomoc uczniom w zadaniach pisemnych lub nauce nowych języków.
- Dostępność: Tworzenie narzędzi dla osób z niepełnosprawnościami, takich jak systemy zamiany tekstu na mowę.

**Rozmiar**
  
Podstawowa różnica między LLM i SLM leży w skali modeli. LLM, takie jak ChatGPT (GPT-4), mogą składać się z około 1,76 biliona parametrów, podczas gdy otwarte modele SLM, takie jak Mistral 7B, zaprojektowane są z znacznie mniejszą liczbą parametrów — około 7 miliardów. Ta różnica wynika głównie z odmienności architektury i procesów treningowych modelu. Na przykład ChatGPT wykorzystuje mechanizm self-attention w strukturze enkoder-dekoder, podczas gdy Mistral 7B używa uwagi z przesuwanym oknem (sliding window attention), co umożliwia bardziej efektywny trening w modelu tylko-dekoderowym. Ta różnica w architekturze ma głęboki wpływ na złożoność i wydajność tych modeli.

**Zrozumienie**

SLM są zazwyczaj zoptymalizowane pod kątem wydajności w określonych dziedzinach, co czyni je bardzo wyspecjalizowanymi, ale potencjalnie ograniczonymi w zdolności do szerokiego rozumienia kontekstu w wielu dziedzinach wiedzy. Dla kontrastu, LLM dążą do symulacji inteligencji na bardziej kompleksowym poziomie. Trening na ogromnych, zróżnicowanych zbiorach danych pozwala LLM dobrze funkcjonować w różnych domenach, oferując większą wszechstronność i zdolność adaptacji. W konsekwencji, LLM są bardziej odpowiednie do szerszego zakresu zadań końcowych, takich jak przetwarzanie języka naturalnego i programowanie.

**Moc obliczeniowa**

Trening i wdrażanie LLM to zasobożerne procesy, często wymagające znacznej infrastruktury obliczeniowej, w tym dużych klastrów GPU. Na przykład trening modelu takiego jak ChatGPT od podstaw może wymagać tysięcy GPU przez długi czas. Natomiast SLM, mając mniejszą liczbę parametrów, są bardziej dostępne pod względem zasobów obliczeniowych. Modele takie jak Mistral 7B można trenować i uruchamiać na lokalnych maszynach wyposażonych w umiarkowane możliwości GPU, choć trening nadal wymaga kilku godzin na wielu GPU.

**Stronniczość**

Stronniczość jest znanym problemem w LLM, głównie ze względu na charakter danych treningowych. Modele te często opierają się na surowych, publicznie dostępnych danych z internetu, które mogą niedoreprezentować lub błędnie przedstawiać pewne grupy, wprowadzać błędne oznaczenia lub odzwierciedlać lingwistyczne uprzedzenia wynikające z dialektu, różnic geograficznych i zasad gramatycznych. Ponadto złożoność architektur LLM może nieświadomie potęgować stronniczość, która może zostać niezauważona bez starannego dostrajania. Z kolei SLM, trenowane na węższych, specyficznych dla domeny zbiorach danych, są z natury mniej podatne na takie uprzedzenia, choć nie są od nich całkowicie wolne.

**Inferencja**

Zmniejszony rozmiar SLM daje im znaczną przewagę pod względem szybkości inferencji, pozwalając na efektywne generowanie wyników na lokalnym sprzęcie bez potrzeby rozległego przetwarzania równoległego. W przeciwieństwie do tego, LLM, ze względu na rozmiar i złożoność, często wymagają dużych równoległych zasobów obliczeniowych, by osiągnąć akceptowalne czasy inferencji. Obecność wielu jednoczesnych użytkowników dodatkowo spowalnia czas odpowiedzi LLM, zwłaszcza gdy są wdrażane na dużą skalę.

Podsumowując, chociaż LLM i SLM dzielą wspólne podstawy uczenia maszynowego, znacząco różnią się pod względem wielkości modelu, wymagań zasobowych, rozumienia kontekstu, podatności na stronniczość i szybkości inferencji. Te różnice odzwierciedlają ich odpowiednie zastosowania: LLM są bardziej wszechstronne, lecz zasobożerne, podczas gdy SLM oferują efektywność specyficzną dla domeny przy zmniejszonych wymaganiach obliczeniowych.

***Uwaga: W tej lekcji wprowadzimy SLM na przykładzie Microsoft Phi-3 / 3.5.***

## Wprowadzenie do Rodziny Phi-3 / Phi-3.5

Rodzina Phi-3 / 3.5 głównie celuje w scenariusze zastosowań związane z tekstem, wizją oraz Agentem (MoE):

### Phi-3 / 3.5 Instruct

Głównie do generowania tekstu, uzupełniania czatu i ekstrakcji informacji z treści itp.

**Phi-3-mini**

Model językowy o rozmiarze 3.8B jest dostępny na Microsoft Foundry, Hugging Face i Ollama. Modele Phi-3 znacząco przewyższają modele językowe o równoważnej i większej wielkości na kluczowych benchmarkach (patrz liczby benchmarków poniżej, wyższe liczby oznaczają lepsze wyniki). Phi-3-mini przewyższa modele dwukrotnie większe, podczas gdy Phi-3-small i Phi-3-medium przewyższają większe modele, w tym GPT-3.5.

**Phi-3-small & medium**

Zaledwie z 7 miliardami parametrów, Phi-3-small przewyższa GPT-3.5T w różnych benchmarkach dotyczących języka, rozumowania, kodowania i matematyki.

Phi-3-medium z 14 miliardami parametrów podtrzymuje ten trend i przewyższa Gemini 1.0 Pro.

**Phi-3.5-mini**

Możemy go traktować jako ulepszoną wersję Phi-3-mini. Chociaż liczba parametrów pozostaje niezmieniona, poprawia zdolność wspierania wielu języków (obsługując ponad 20 języków: arabski, chiński, czeski, duński, niderlandzki, angielski, fiński, francuski, niemiecki, hebrajski, węgierski, włoski, japoński, koreański, norweski, polski, portugalski, rosyjski, hiszpański, szwedzki, tajski, turecki, ukraiński) i dodaje silniejsze wsparcie dla długiego kontekstu.

Phi-3.5-mini z 3.8 miliardami parametrów przewyższa modele tej samej wielkości i jest porównywalny z modelami dwukrotnie większymi.

### Phi-3 / 3.5 Vision

Model Instruct Phi-3/3.5 można uznać za zdolność Phi do rozumienia, a Vision to oczy Phi, które pozwalają mu rozumieć świat.


**Phi-3-Vision**

Phi-3-vision, mający tylko 4.2 miliarda parametrów, kontynuuje ten trend i przewyższa większe modele, takie jak Claude-3 Haiku i Gemini 1.0 Pro V, w ogólnych zadaniach związanych z rozumieniem wizualnym, OCR oraz analizą tabel i diagramów.


**Phi-3.5-Vision**

Phi-3.5-Vision jest również ulepszeniem Phi-3-Vision, dodającym wsparcie dla wielu obrazów. Można to traktować jako poprawę widzenia – nie tylko można oglądać obrazy, ale także filmy.

Phi-3.5-vision przewyższa większe modele, takie jak Claude-3.5 Sonnet i Gemini 1.5 Flash, w zadaniach OCR, rozumienia tabel i wykresów, a także jest porównywalny w ogólnych zadaniach z rozumieniem wiedzy wizualnej. Wspiera wieloklatkowe wejścia, tj. wykonywanie rozumowania na wielu obrazach wejściowych.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** umożliwia trenowanie modeli z dużo mniejszym zużyciem mocy obliczeniowej, co oznacza, że możesz znacznie zwiększyć rozmiar modelu lub zbioru danych przy tym samym budżecie obliczeniowym co model gęsty. W szczególności model MoE powinien szybciej osiągnąć tę samą jakość co jego gęsty odpowiednik podczas pretreningu.

Phi-3.5-MoE składa się z 16 modułów ekspertów po 3.8 miliarda parametrów każdy. Phi-3.5-MoE zaledwie z 6.6 miliardami aktywnych parametrów osiąga podobny poziom rozumowania, rozumienia języka i matematyki jak znacznie większe modele.

Możemy używać modeli z rodziny Phi-3/3.5 w różnych scenariuszach. W przeciwieństwie do LLM, Phi-3/3.5-mini lub Phi-3/3.5-Vision można wdrażać na urządzeniach brzegowych.


## Jak używać modeli z rodziny Phi-3/3.5

Chcemy używać Phi-3/3.5 w różnych scenariuszach. Następnie posłużymy się Phi-3/3.5 w różnych scenariuszach.

![phi3](../../../translated_images/pl/phi3.655208c3186ae381.webp)

### Inferencja przez chmurowe API

**Microsoft Foundry Models**

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) jest jego bezpośrednim zamiennikiem.

Microsoft Foundry Models to najbardziej bezpośredni sposób. Możesz szybko dostać się do modelu Phi-3/3.5-Instruct przez katalog modeli Foundry. W połączeniu z Azure AI Inference SDK / OpenAI SDK masz dostęp do API przez kod, umożliwiając wykonanie wywołania Phi-3/3.5-Instruct. Możesz także przetestować różne efekty poprzez Playground.

- Demo: Porównanie efektów Phi-3-mini i Phi-3.5-mini w scenariuszach chińskich

![phi3](../../../translated_images/pl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Jeśli chcemy korzystać z modeli wizji i MoE, możemy użyć Microsoft Foundry do wykonania wywołań. Jeśli jesteś zainteresowany, możesz przeczytać Phi-3 Cookbook, aby dowiedzieć się, jak wywołać Phi-3/3.5 Instruct, Vision, MoE przez Microsoft Foundry [Kliknij ten link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Oprócz chmurowego katalogu Microsoft Foundry Models, możesz również użyć [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) do wykonania powiązanych wywołań. Możesz odwiedzić NVIDIA NIM, aby wykonać wywołania API rodziny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) to zestaw przyspieszonych mikroserwisów inferencyjnych zaprojektowanych, aby pomóc deweloperom w efektywnym wdrażaniu modeli AI w różnych środowiskach, w tym w chmurze, centrach danych i na stacjach roboczych.

Oto kilka kluczowych cech NVIDIA NIM:

- **Łatwość wdrażania:** NIM umożliwia wdrożenie modeli AI za pomocą jednego polecenia, co pozwala na łatwą integrację z istniejącymi przepływami pracy.

- **Zoptymalizowana wydajność:** Wykorzystuje zoptymalizowane silniki inferencyjne NVIDIA, takie jak TensorRT i TensorRT-LLM, aby zapewnić niskie opóźnienia i dużą przepustowość.
- **Skalowalność:** NIM obsługuje autoskalowanie w Kubernetes, co umożliwia skuteczne radzenie sobie z różnymi obciążeniami.
- **Bezpieczeństwo i kontrola:** Organizacje mogą zachować kontrolę nad swoimi danymi i aplikacjami, hostując usługi mikroserwisowe NIM na własnej zarządzanej infrastrukturze.
- **Standardowe API:** NIM zapewnia branżowe standardowe API, ułatwiając budowę i integrację aplikacji AI, takich jak chatboty, asystenci AI i inne.

NIM jest częścią NVIDIA AI Enterprise, którego celem jest uproszczenie wdrażania i operacjonalizacji modeli AI, zapewniając ich efektywne działanie na GPU NVIDIA.

- Demo: Użycie NVIDIA NIM do wywołania Phi-3.5-Vision-API  [[Kliknij ten link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Lokalna praca z Phi-3/3.5
Inferencja w odniesieniu do Phi-3 lub dowolnego modelu językowego, takiego jak GPT-3, oznacza proces generowania odpowiedzi lub predykcji na podstawie otrzymanego inputu. Gdy podasz prompt lub pytanie Phi-3, wykorzystuje on swą wytrenowaną sieć neuronową, aby wnioskować najbardziej prawdopodobną i odpowiednią odpowiedź, analizując wzorce oraz zależności w danych, na których był trenowany.

**Hugging Face Transformer**
Hugging Face Transformers to potężna biblioteka zaprojektowana do przetwarzania języka naturalnego (NLP) i innych zadań uczenia maszynowego. Oto kilka kluczowych punktów:

1. **Modele wstępnie wytrenowane:** Dostarcza tysiące modeli wstępnie wytrenowanych, które można wykorzystać do różnych zadań, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych jednostek, odpowiadanie na pytania, streszczanie, tłumaczenie i generowanie tekstu.

2. **Interoperacyjność frameworków:** Biblioteka obsługuje wiele frameworków uczenia głębokiego, w tym PyTorch, TensorFlow i JAX. Pozwala to trenować model w jednym frameworku i używać go w innym.

3. **Możliwości multimodalne:** Oprócz NLP, Hugging Face Transformers wspiera również zadania w zakresie wizji komputerowej (np. klasyfikacja obrazów, wykrywanie obiektów) oraz przetwarzania audio (np. rozpoznawanie mowy, klasyfikacja dźwięku).

4. **Łatwość użycia:** Biblioteka oferuje API i narzędzia umożliwiające łatwe pobieranie i dostrajanie modeli, co czyni ją przystępną zarówno dla początkujących, jak i ekspertów.

5. **Społeczność i zasoby:** Hugging Face ma żywą społeczność oraz bogatą dokumentację, samouczki i przewodniki, które pomagają użytkownikom rozpocząć pracę i w pełni wykorzystać bibliotekę.
[oficjalną dokumentację](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) lub ich [repozytorium GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

To jest najczęściej używana metoda, ale wymaga również przyspieszenia GPU. W końcu scenariusze takie jak Vision i MoE wymagają dużo obliczeń, które będą bardzo powolne na CPU, jeśli nie są skwantowane.


- Demo: Użycie Transformera do wywołania Phi-3.5-Instruct [Kliknij ten link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Użycie Transformera do wywołania Phi-3.5-Vision [Kliknij ten link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Użycie Transformera do wywołania Phi-3.5-MoE [Kliknij ten link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) to platforma zaprojektowana, aby ułatwić uruchamianie dużych modeli językowych (LLM) lokalnie na twoim komputerze. Wspiera różne modele, takie jak Llama 3.1, Phi 3, Mistral i Gemma 2, między innymi. Platforma upraszcza ten proces, łącząc wagi modeli, konfigurację i dane w pojedynczy pakiet, czyniąc go bardziej dostępnym dla użytkowników, którzy chcą dostosowywać i tworzyć własne modele. Ollama jest dostępna dla macOS, Linux i Windows. To świetne narzędzie, jeśli chcesz eksperymentować lub wdrażać LLM bez polegania na usługach chmurowych. Ollama to najprostsza metoda, wystarczy wykonać następujące polecenie.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) to offline'owe, lokalne środowisko wykonawcze Microsoft do uruchamiania modeli takich jak Phi całkowicie na własnym sprzęcie - bez konieczności subskrypcji Azure, klucza API czy połączenia sieciowego. Automatycznie wybiera najlepszego dostępnego dostawcę wykonania (NPU, GPU lub CPU) i udostępnia punkt końcowy kompatybilny z OpenAI, dzięki czemu istniejący kod `openai`/Azure AI Inference SDK może na niego wskazywać z minimalnymi zmianami. Zobacz [dokumentację Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), aby rozpocząć.

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

**ONNX Runtime dla GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) to wieloplatformowy akcelerator inferencji i treningu uczenia maszynowego. ONNX Runtime dla Generative AI (GENAI) to potężne narzędzie, które pomaga efektywnie uruchamiać modele generatywnej AI na różnych platformach.

## Co to jest ONNX Runtime?
ONNX Runtime to projekt open-source umożliwiający wysokowydajną inferencję modeli uczenia maszynowego. Obsługuje modele w formacie Open Neural Network Exchange (ONNX), który jest standardem reprezentacji modeli uczenia maszynowego. Inferencja ONNX Runtime może zapewniać szybsze doświadczenia użytkownika i obniżone koszty, wspierając modele z frameworków głębokiego uczenia, takich jak PyTorch i TensorFlow/Keras, a także klasyczne biblioteki uczenia maszynowego, jak scikit-learn, LightGBM, XGBoost itd. ONNX Runtime jest kompatybilny z różnym sprzętem, sterownikami i systemami operacyjnymi, zapewniając optymalną wydajność dzięki wykorzystaniu akceleratorów sprzętowych tam, gdzie to możliwe, oraz optymalizacjom i transformacjom grafu.

## Co to jest Generatywna AI?
Generatywna AI odnosi się do systemów AI potrafiących generować nowe treści, takie jak tekst, obrazy czy muzyka, na podstawie danych, na których były trenowane. Przykłady to modele językowe takie jak GPT-3 oraz modele generowania obrazów, np. Stable Diffusion. Biblioteka ONNX Runtime dla GenAI zapewnia pętlę generatywnej AI dla modeli ONNX, w tym inferencję z ONNX Runtime, przetwarzanie logitów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią KV cache.

## ONNX Runtime dla GENAI
ONNX Runtime dla GENAI rozszerza możliwości ONNX Runtime o wsparcie dla modeli generatywnej AI. Oto kilka kluczowych funkcji:

- **Szerokie wsparcie platform:** Działa na różnych platformach, w tym Windows, Linux, macOS, Android i iOS.
- **Wsparcie modeli:** Obsługuje wiele popularnych modeli generatywnej AI, takich jak LLaMA, GPT-Neo, BLOOM i inne.
- **Optymalizacja wydajności:** Zawiera optymalizacje dla różnych akceleratorów sprzętowych, takich jak GPU NVIDIA, GPU AMD i innych.
- **Łatwość użycia:** Zapewnia API do łatwej integracji z aplikacjami, umożliwiając generowanie tekstu, obrazów i innych treści przy minimalnej ilości kodu.
- Użytkownicy mogą wywołać metodę generate() na wysokim poziomie lub wykonywać każdą iterację modelu w pętli, generując jeden token na raz i opcjonalnie aktualizując parametry generowania w trakcie pętli.
- ONNX Runtime obsługuje także greedy/beam search oraz próbkowanie TopP, TopK do generowania sekwencji tokenów oraz wbudowane przetwarzanie logitów, takie jak kary za powtórzenia. Możesz również łatwo dodać własne oceny.

## Pierwsze kroki
Aby rozpocząć pracę z ONNX Runtime dla GENAI, możesz wykonać następujące kroki:

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

Oprócz metod referencyjnych ONNX Runtime, Ollama i Foundry Local możemy również uzupełnić referencję modeli kwantyfikowanych w oparciu o metody referencyjne modeli dostarczane przez różnych producentów. Na przykład framework Apple MLX z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO z CPU/GPU itp. Więcej treści znajdziesz także w [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Więcej

Poznaliśmy podstawy rodziny Phi-3/3.5, ale aby dowiedzieć się więcej o SLM potrzebujemy większej wiedzy. Odpowiedzi znajdziesz w Phi-3 Cookbook. Jeśli chcesz dowiedzieć się więcej, odwiedź [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->