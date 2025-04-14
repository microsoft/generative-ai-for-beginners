# Wprowadzenie do Małych Modeli Językowych (SLM) dla Początkujących w Generatywnej AI

Generatywna AI to fascynująca dziedzina sztucznej inteligencji, która skupia się na tworzeniu systemów zdolnych do generowania nowych treści. Treść ta może obejmować tekst, obrazy, muzykę, a nawet całe wirtualne środowiska. Jednym z najbardziej ekscytujących zastosowań generatywnej AI jest dziedzina modeli językowych.

## Czym są Małe Modele Językowe (SLM)?

Mały Model Językowy (SLM) reprezentuje pomniejszoną wersję dużego modelu językowego (LLM), wykorzystując wiele zasad architektonicznych i technik LLM, jednocześnie wykazując znacznie mniejsze zapotrzebowanie obliczeniowe.

SLM to podzbiór modeli językowych zaprojektowanych do generowania tekstu przypominającego ludzki. W przeciwieństwie do ich większych odpowiedników, takich jak GPT-4, SLM są bardziej kompaktowe i wydajne, co czyni je idealnymi do zastosowań, w których zasoby obliczeniowe są ograniczone. Mimo mniejszych rozmiarów, nadal mogą wykonywać różnorodne zadania. Zazwyczaj SLM są budowane poprzez kompresję lub destylację LLM, mając na celu zachowanie znacznej części funkcjonalności i możliwości językowych oryginalnego modelu. Ta redukcja rozmiaru modelu zmniejsza ogólną złożoność, czyniąc SLM bardziej wydajnymi pod względem zużycia pamięci i wymagań obliczeniowych. Pomimo tych optymalizacji, SLM nadal mogą wykonywać szeroki zakres zadań przetwarzania języka naturalnego (NLP):

- Generowanie tekstu: Tworzenie spójnych i kontekstowo trafnych zdań lub akapitów.
- Uzupełnianie tekstu: Przewidywanie i uzupełnianie zdań na podstawie danego promptu.
- Tłumaczenie: Konwertowanie tekstu z jednego języka na inny.
- Podsumowywanie: Skracanie długich tekstów do krótszych, bardziej przyswajalnych podsumowań.

Jednak z pewnymi kompromisami w zakresie wydajności lub głębi zrozumienia w porównaniu do ich większych odpowiedników.

## Jak działają Małe Modele Językowe?

SLM są trenowane na ogromnych ilościach danych tekstowych. Podczas treningu uczą się wzorców i struktur języka, co umożliwia im generowanie tekstu, który jest zarówno poprawny gramatycznie, jak i odpowiedni kontekstowo. Proces treningu obejmuje:

- Zbieranie danych: Gromadzenie dużych zbiorów danych tekstowych z różnych źródeł.
- Przetwarzanie wstępne: Czyszczenie i organizowanie danych, aby nadawały się do treningu.
- Trening: Używanie algorytmów uczenia maszynowego do nauczenia modelu rozumienia i generowania tekstu.
- Dostrajanie (Fine-Tuning): Dostosowywanie modelu w celu poprawy jego wydajności w określonych zadaniach.

Rozwój SLM wpisuje się w rosnące zapotrzebowanie na modele, które można wdrażać w środowiskach o ograniczonych zasobach, takich jak urządzenia mobilne czy platformy edge computing, gdzie pełnowymiarowe LLM mogą być niepraktyczne ze względu na duże zapotrzebowanie na zasoby. Skupiając się na wydajności, SLM równoważą wydajność z dostępnością, umożliwiając szersze zastosowanie w różnych dziedzinach.

![slm](../../img/slm.png?WT.mc_id=academic-105485-koreyst)

## Cele Nauki

W tej lekcji mamy nadzieję wprowadzić wiedzę na temat SLM i połączyć ją z Microsoft Phi-3, aby poznać różne scenariusze w kontekście treści tekstowych, wizji i MoE.

Po ukończeniu tej lekcji powinieneś być w stanie odpowiedzieć na następujące pytania:

- Czym jest SLM?
- Jaka jest różnica między SLM a LLM?
- Czym jest rodzina Microsoft Phi-3/3.5?
- Jak wnioskować z rodziny Microsoft Phi-3/3.5?

Gotowy? Zaczynajmy.

## Różnice między Dużymi Modelami Językowymi (LLM) a Małymi Modelami Językowymi (SLM)

Zarówno LLM, jak i SLM opierają się na fundamentalnych zasadach probabilistycznego uczenia maszynowego, stosując podobne podejścia w projektowaniu architektonicznym, metodologiach treningu, procesach generowania danych i technikach oceny modeli. Jednak kilka kluczowych czynników odróżnia te dwa typy modeli.

## Zastosowania Małych Modeli Językowych

SLM mają szeroki zakres zastosowań, w tym:

- Chatboty: Zapewnianie obsługi klienta i angażowanie użytkowników w sposób konwersacyjny.
- Tworzenie treści: Pomaganie pisarzom poprzez generowanie pomysłów lub nawet tworzenie całych artykułów.
- Edukacja: Pomaganie uczniom w zadaniach pisemnych lub nauce nowych języków.
- Dostępność: Tworzenie narzędzi dla osób z niepełnosprawnościami, takich jak systemy zamiany tekstu na mowę.

**Rozmiar**

Główna różnica między LLM a SLM leży w skali modeli. LLM, takie jak ChatGPT (GPT-4), mogą składać się z szacunkowo 1,76 biliona parametrów, podczas gdy SLM typu open-source, takie jak Mistral 7B, są projektowane ze znacznie mniejszą liczbą parametrów – około 7 miliardów. Ta rozbieżność wynika głównie z różnic w architekturze modelu i procesach treningu. Na przykład ChatGPT wykorzystuje mechanizm samouwagi (self-attention) w ramach architektury koder-dekoder, podczas gdy Mistral 7B używa uwagi okna przesuwnego (sliding window attention), co umożliwia bardziej wydajny trening w ramach modelu tylko dekodera. Ta różnorodność architektoniczna ma głębokie implikacje dla złożoności i wydajności tych modeli.

**Zrozumienie**

SLM są zazwyczaj optymalizowane pod kątem wydajności w określonych dziedzinach, co czyni je wysoce wyspecjalizowanymi, ale potencjalnie ograniczonymi w ich zdolności do zapewnienia szerokiego zrozumienia kontekstowego w wielu dziedzinach wiedzy. W przeciwieństwie do tego, LLM mają na celu symulowanie inteligencji podobnej do ludzkiej na bardziej kompleksowym poziomie. Trenowane na ogromnych, zróżnicowanych zbiorach danych, LLM są zaprojektowane do dobrego działania w różnych dziedzinach, oferując większą wszechstronność i zdolność adaptacji. W konsekwencji LLM są bardziej odpowiednie do szerszego zakresu zadań niższego szczebla, takich jak przetwarzanie języka naturalnego i programowanie.

**Obliczenia**

Trening i wdrażanie LLM to procesy wymagające dużych zasobów, często wymagające znacznej infrastruktury obliczeniowej, w tym klastrów GPU na dużą skalę. Na przykład trening modelu takiego jak ChatGPT od podstaw może wymagać tysięcy GPU przez dłuższy czas. W przeciwieństwie do tego, SLM, ze względu na mniejszą liczbę parametrów, są bardziej dostępne pod względem zasobów obliczeniowych. Modele takie jak Mistral 7B można trenować i uruchamiać na lokalnych maszynach wyposażonych w umiarkowane możliwości GPU, chociaż trening nadal wymaga kilku godzin na wielu GPU.

**Stronniczość (Bias)**

Stronniczość jest znanym problemem w LLM, głównie ze względu na charakter danych treningowych. Modele te często opierają się na surowych, ogólnodostępnych danych z internetu, które mogą niedostatecznie reprezentować lub błędnie reprezentować niektóre grupy, wprowadzać błędne etykietowanie lub odzwierciedlać stronniczość językową wynikającą z dialektu, różnic geograficznych i zasad gramatycznych. Dodatkowo złożoność architektur LLM może nieumyślnie pogłębiać stronniczość, która może pozostać niezauważona bez starannego dostrajania. Z drugiej strony, SLM, będąc trenowane na bardziej ograniczonych, specyficznych dla domeny zbiorach danych, są z natury mniej podatne na takie stronniczości, chociaż nie są na nie odporne.

**Wnioskowanie (Inference)**

Zmniejszony rozmiar SLM daje im znaczną przewagę pod względem szybkości wnioskowania, pozwalając im efektywnie generować wyniki na lokalnym sprzęcie bez potrzeby rozległego przetwarzania równoległego. W przeciwieństwie do tego, LLM, ze względu na swój rozmiar i złożoność, często wymagają znacznych równoległych zasobów obliczeniowych, aby osiągnąć akceptowalne czasy wnioskowania. Obecność wielu jednoczesnych użytkowników dodatkowo spowalnia czas odpowiedzi LLM, zwłaszcza gdy są wdrażane na dużą skalę.

Podsumowując, chociaż zarówno LLM, jak i SLM mają wspólną podstawę w uczeniu maszynowym, różnią się znacznie pod względem rozmiaru modelu, wymagań dotyczących zasobów, zrozumienia kontekstowego, podatności na stronniczość i szybkości wnioskowania. Różnice te odzwierciedlają ich odpowiednią przydatność do różnych przypadków użycia, przy czym LLM są bardziej wszechstronne, ale wymagające dużych zasobów, a SLM oferują bardziej specyficzną dla domeny wydajność przy zmniejszonych wymaganiach obliczeniowych.

**_Uwaga: W tym rozdziale przedstawimy SLM na przykładzie Microsoft Phi-3 / 3.5._**

## Przedstawienie rodziny Phi-3 / Phi-3.5

Rodzina Phi-3 / 3.5 jest głównie ukierunkowana na scenariusze zastosowań związane z tekstem, wizją i Agentem (MoE):

### Phi-3 / 3.5 Instruct

Głównie do generowania tekstu, uzupełniania czatu, ekstrakcji informacji z treści itp.

**Phi-3-mini**

Model językowy 3.8B jest dostępny w Microsoft Azure AI Studio, Hugging Face i Ollama. Modele Phi-3 znacznie przewyższają modele językowe o tej samej i większej wielkości w kluczowych benchmarkach (patrz liczby benchmarków poniżej, wyższe liczby są lepsze). Phi-3-mini przewyższa modele dwukrotnie większe, podczas gdy Phi-3-small i Phi-3-medium przewyższają większe modele, w tym GPT-3.5

**Phi-3-small & medium**

Mając zaledwie 7 mld parametrów, Phi-3-small pokonuje GPT-3.5T w różnych benchmarkach językowych, rozumowania, kodowania i matematycznych.

Phi-3-medium z 14 mld parametrów kontynuuje ten trend i przewyższa Gemini 1.0 Pro.

**Phi-3.5-mini**

Możemy go traktować jako ulepszenie Phi-3-mini. Chociaż parametry pozostają niezmienione, poprawia on zdolność obsługi wielu języków (Obsługa ponad 20 języków: arabski, chiński, czeski, duński, holenderski, angielski, fiński, francuski, niemiecki, hebrajski, węgierski, włoski, japoński, koreański, norweski, polski, portugalski, rosyjski, hiszpański, szwedzki, tajski, turecki, ukraiński) i dodaje silniejsze wsparcie dla długiego kontekstu.

Phi-3.5-mini z 3.8 mld parametrów przewyższa modele językowe tej samej wielkości i jest na równi z modelami dwukrotnie większymi.

### Phi-3 / 3.5 Vision

Możemy myśleć o modelu Instruct Phi-3/3.5 jako o zdolności Phi do rozumienia, a Vision to to, co daje Phi oczy do rozumienia świata.

**Phi-3-Vision**

Phi-3-vision, mając zaledwie 4.2 mld parametrów, kontynuuje ten trend i przewyższa większe modele, takie jak Claude-3 Haiku i Gemini 1.0 Pro V, w ogólnych zadaniach rozumowania wizualnego, OCR oraz zadaniach rozumienia tabel i diagramów.

**Phi-3.5-Vision**

Phi-3.5-Vision jest również ulepszeniem Phi-3-Vision, dodając obsługę wielu obrazów. Możesz myśleć o tym jako o poprawie widzenia, nie tylko można widzieć zdjęcia, ale także filmy.

Phi-3.5-vision przewyższa większe modele, takie jak Claude-3.5 Sonnet i Gemini 1.5 Flash, w zadaniach OCR, rozumienia tabel i wykresów oraz jest na równi w ogólnych zadaniach rozumowania opartego na wiedzy wizualnej. Obsługuje wejście wieloklatkowe, tj. wykonuje rozumowanie na wielu obrazach wejściowych.

### Phi-3.5-MoE

**_Mixture of Experts (MoE)_** umożliwia wstępne trenowanie modeli przy znacznie mniejszym zużyciu zasobów obliczeniowych, co oznacza, że można radykalnie zwiększyć rozmiar modelu lub zbioru danych przy tym samym budżecie obliczeniowym co model gęsty. W szczególności model MoE powinien osiągnąć tę samą jakość co jego gęsty odpowiednik znacznie szybciej podczas wstępnego treningu.

Phi-3.5-MoE składa się z 16 modułów eksperckich 3.8B. Phi-3.5-MoE z zaledwie 6.6 mld aktywnych parametrów osiąga podobny poziom rozumowania, rozumienia języka i matematyki co znacznie większe modele.

Możemy używać modelu rodziny Phi-3/3.5 w oparciu o różne scenariusze. W przeciwieństwie do LLM, możesz wdrożyć Phi-3/3.5-mini lub Phi-3/3.5-Vision na urządzeniach brzegowych (edge).

## Jak używać modeli rodziny Phi-3/3.5

Mamy nadzieję używać Phi-3/3.5 w różnych scenariuszach. Następnie użyjemy Phi-3/3.5 w oparciu o różne scenariusze.

![phi3](../../img/phi3.png?WT.mc_id=academic-105485-koreyst)

### Wnioskowanie z różnymi API chmurowymi

**GitHub Models**

GitHub Models to najbardziej bezpośredni sposób. Możesz szybko uzyskać dostęp do modelu Phi-3/3.5-Instruct poprzez GitHub Models. W połączeniu z Azure AI Inference SDK / OpenAI SDK, możesz uzyskać dostęp do API za pomocą kodu, aby zakończyć wywołanie Phi-3/3.5-Instruct. Możesz również testować różne efekty za pomocą Playground.

- Demo: Porównanie efektów Phi-3-mini i Phi-3.5-mini w scenariuszach chińskich

![phi3](../../img/gh1.png?WT.mc_id=academic-105485-koreyst)

![phi35](../../img/gh2.png?WT.mc_id=academic-105485-koreyst)

**Azure AI Studio**

Lub jeśli chcemy używać modeli wizji i MoE, możesz użyć Azure AI Studio, aby zakończyć wywołanie. Jeśli jesteś zainteresowany, możesz przeczytać Phi-3 Cookbook, aby dowiedzieć się, jak wywoływać Phi-3/3.5 Instruct, Vision, MoE za pośrednictwem Azure AI Studio [Kliknij ten link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)

**NVIDIA NIM**

Oprócz rozwiązań Model Catalog opartych na chmurze dostarczanych przez Azure i GitHub, możesz również użyć [Nivida NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) do wykonania powiązanych wywołań. Możesz odwiedzić NIVIDA NIM, aby zakończyć wywołania API rodziny Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) to zestaw przyspieszonych mikrousług wnioskowania zaprojektowanych, aby pomóc programistom efektywnie wdrażać modele AI w różnych środowiskach, w tym w chmurach, centrach danych i stacjach roboczych.

Oto niektóre kluczowe cechy NVIDIA NIM:

- **Łatwość wdrożenia:** NIM pozwala na wdrożenie modeli AI za pomocą jednej komendy, co ułatwia integrację z istniejącymi przepływami pracy.
- **Zoptymalizowana wydajność:** Wykorzystuje wstępnie zoptymalizowane silniki wnioskowania NVIDIA, takie jak TensorRT i TensorRT-LLM, aby zapewnić niskie opóźnienia i wysoką przepustowość.
- **Skalowalność:** NIM obsługuje automatyczne skalowanie w Kubernetes, umożliwiając efektywne obsługiwanie zmiennych obciążeń.
- **Bezpieczeństwo i kontrola:** Organizacje mogą zachować kontrolę nad swoimi danymi i aplikacjami, samodzielnie hostując mikrousługi NIM na własnej zarządzanej infrastrukturze.
- **Standardowe API:** NIM zapewnia standardowe API branżowe, co ułatwia budowanie i integrowanie aplikacji AI, takich jak chatboty, asystenci AI i inne.

NIM jest częścią NVIDIA AI Enterprise, która ma na celu uproszczenie wdrażania i operacjonalizacji modeli AI, zapewniając ich efektywne działanie na GPU NVIDIA.

- Demo: Używanie Nividia NIM do wywołania Phi-3.5-Vision-API [[Kliknij ten link](../../python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]

### Wnioskowanie Phi-3/3.5 w środowisku lokalnym

Wnioskowanie w odniesieniu do Phi-3 lub dowolnego modelu językowego, takiego jak GPT-3, odnosi się do procesu generowania odpowiedzi lub przewidywań na podstawie otrzymanych danych wejściowych. Gdy podajesz prompt lub pytanie do Phi-3, wykorzystuje on swoją wytrenowaną sieć neuronową do wnioskowania najbardziej prawdopodobnej i trafnej odpowiedzi, analizując wzorce i relacje w danych, na których został wytrenowany.

**Hugging Face Transformer**

Hugging Face Transformers to potężna biblioteka przeznaczona do przetwarzania języka naturalnego (NLP) i innych zadań uczenia maszynowego. Oto kilka kluczowych punktów na jej temat:

1. **Wstępnie wytrenowane modele**: Dostarcza tysiące wstępnie wytrenowanych modeli, które można wykorzystać do różnych zadań, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych encji, odpowiadanie na pytania, podsumowywanie, tłumaczenie i generowanie tekstu.

2. **Interoperacyjność frameworków**: Biblioteka obsługuje wiele frameworków głębokiego uczenia, w tym PyTorch, TensorFlow i JAX. Pozwala to trenować model w jednym frameworku i używać go w innym.

3. **Możliwości multimodalne**: Oprócz NLP, Hugging Face Transformers obsługuje również zadania z zakresu widzenia komputerowego (np. klasyfikacja obrazów, wykrywanie obiektów) i przetwarzania dźwięku (np. rozpoznawanie mowy, klasyfikacja dźwięku).

4. **Łatwość użycia**: Biblioteka oferuje API i narzędzia do łatwego pobierania i dostrajania modeli, dzięki czemu jest dostępna zarówno dla początkujących, jak i ekspertów.

5. **Społeczność i zasoby**: Hugging Face ma żywą społeczność oraz obszerną dokumentację, samouczki i przewodniki, które pomagają użytkownikom rozpocząć pracę i w pełni wykorzystać bibliotekę.
   [oficjalna dokumentacja](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) lub ich [repozytorium GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Jest to najczęściej stosowana metoda, ale wymaga również przyspieszenia GPU. W końcu sceny takie jak Vision i MoE wymagają wielu obliczeń, które będą bardzo ograniczone w CPU, jeśli nie zostaną skwantyzowane.

- Demo: Używanie Transformera do wywołania Phi-3.5-Instuct [[Kliknij ten link](../../python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)]

- Demo: Używanie Transformera do wywołania Phi-3.5-Vision [[Kliknij ten link](../../python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)]

- Demo: Używanie Transformera do wywołania Phi-3.5-MoE [[Kliknij ten link](../../python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)]

**Ollama**

[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) to platforma zaprojektowana, aby ułatwić uruchamianie dużych modeli językowych (LLM) lokalnie na Twojej maszynie. Obsługuje różne modele, takie jak Llama 3.1, Phi 3, Mistral i Gemma 2. Platforma upraszcza proces, łącząc wagi modelu, konfigurację i dane w jeden pakiet, co ułatwia użytkownikom dostosowywanie i tworzenie własnych modeli. Ollama jest dostępna dla systemów macOS, Linux i Windows. To świetne narzędzie, jeśli chcesz eksperymentować z LLM lub wdrażać je bez polegania na usługach chmurowych. Ollama to najbardziej bezpośredni sposób, wystarczy wykonać następujące polecenie.

```bash

ollama run phi3.5

```

**ONNX Runtime dla GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) to wieloplatformowy akcelerator wnioskowania i trenowania uczenia maszynowego. ONNX Runtime dla Generative AI (GENAI) to potężne narzędzie, które pomaga efektywnie uruchamiać modele generatywnej AI na różnych platformach.

## Czym jest ONNX Runtime?

ONNX Runtime to projekt open-source, który umożliwia wysokowydajne wnioskowanie modeli uczenia maszynowego. Obsługuje modele w formacie Open Neural Network Exchange (ONNX), który jest standardem reprezentacji modeli uczenia maszynowego. Wnioskowanie ONNX Runtime może zapewnić szybsze doświadczenia klienta i niższe koszty, obsługując modele z frameworków głębokiego uczenia, takich jak PyTorch i TensorFlow/Keras, a także klasycznych bibliotek uczenia maszynowego, takich jak scikit-learn, LightGBM, XGBoost itp. ONNX Runtime jest kompatybilny z różnymi sprzętami, sterownikami i systemami operacyjnymi oraz zapewnia optymalną wydajność, wykorzystując akceleratory sprzętowe tam, gdzie to możliwe, wraz z optymalizacjami i transformacjami grafu.

## Czym jest Generatywna AI?

Generatywna AI odnosi się do systemów AI, które mogą generować nowe treści, takie jak tekst, obrazy lub muzyka, na podstawie danych, na których zostały wytrenowane. Przykłady obejmują modele językowe, takie jak GPT-3, oraz modele generowania obrazów, takie jak Stable Diffusion. Biblioteka ONNX Runtime dla GenAI zapewnia pętlę generatywnej AI dla modeli ONNX, w tym wnioskowanie za pomocą ONNX Runtime, przetwarzanie logitów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią podręczną KV.

## ONNX Runtime dla GENAI

ONNX Runtime dla GENAI rozszerza możliwości ONNX Runtime o obsługę modeli generatywnej AI. Oto niektóre kluczowe cechy:

- **Szerokie wsparcie platform:** Działa na różnych platformach, w tym Windows, Linux, macOS, Android i iOS.
- **Wsparcie modeli:** Obsługuje wiele popularnych modeli generatywnej AI, takich jak LLaMA, GPT-Neo, BLOOM i inne.
- **Optymalizacja wydajności:** Zawiera optymalizacje dla różnych akceleratorów sprzętowych, takich jak GPU NVIDIA, GPU AMD i inne.
- **Łatwość użycia:** Dostarcza API do łatwej integracji z aplikacjami, umożliwiając generowanie tekstu, obrazów i innych treści przy minimalnym kodzie.
- Użytkownicy mogą wywołać metodę `generate()` wysokiego poziomu lub uruchomić każdą iterację modelu w pętli, generując jeden token na raz i opcjonalnie aktualizując parametry generowania wewnątrz pętli.
- ONNX Runtime obsługuje również wyszukiwanie zachłanne/wiązki (greedy/beam search) oraz próbkowanie TopP, TopK do generowania sekwencji tokenów oraz wbudowane przetwarzanie logitów, takie jak kary za powtórzenia. Można również łatwo dodać niestandardowe ocenianie.

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

model = og.Model('sciezka_do_twojego_modelu.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Witaj, jak się masz?"

input_tokens = tokenizer.encode(input_text)
```

### Demo: Używanie ONNX Runtime GenAI do wywołania Phi-3.5-Vision

```python
import onnxruntime_genai as og

model_path = './Twoja ścieżka ONNX Phi-3.5-vision-instruct'

img_path = './Twoja ścieżka do obrazu'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Twój Prompt"

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

    code += tokenizer_stream.decode(new_token)

    print(tokenizer_stream.decode(new_token), end='', flush=True)
```

**Inne**

Oprócz metod referencyjnych ONNX Runtime i Ollama, możemy również zakończyć odniesienie do modeli ilościowych w oparciu o metody referencyjne modeli dostarczane przez różnych producentów. Takich jak framework Apple MLX z Apple Metal, Qualcomm QNN z NPU, Intel OpenVINO z CPU/GPU itp. Możesz również uzyskać więcej treści z [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)

## Więcej

Poznaliśmy podstawy rodziny Phi-3/3.5, ale aby dowiedzieć się więcej o SLM, potrzebujemy więcej wiedzy. Odpowiedzi znajdziesz w Phi-3 Cookbook. Jeśli chcesz dowiedzieć się więcej, odwiedź [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).
