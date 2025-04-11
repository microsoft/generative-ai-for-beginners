# Eksploracja i porównywanie różnych modeli LLM

[![Eksploracja i porównywanie różnych modeli LLM](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji_

W poprzedniej lekcji zobaczyliśmy, jak Generatywna SI zmienia krajobraz technologiczny, jak działają Duże Modele Językowe (LLM) oraz jak firma - taka jak nasz startup - może je zastosować w swoich przypadkach użycia i rozwijać się! W tym rozdziale porównamy różne typy dużych modeli językowych (LLM), aby zrozumieć ich wady i zalety.

Kolejnym krokiem w podróży naszego startupu jest eksploracja obecnego krajobrazu modeli LLM i zrozumienie, które z nich są odpowiednie do naszego przypadku użycia.

## Wprowadzenie

Ta lekcja obejmie:

- Różne typy modeli LLM w obecnym krajobrazie.
- Testowanie, iterowanie i porównywanie różnych modeli dla konkretnego przypadku użycia w Azure.
- Jak wdrażać model LLM.

## Cele Nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Wybrać odpowiedni model dla swojego przypadku użycia.
- Zrozumieć, jak testować, iterować i poprawiać wydajność swojego modelu.
- Wiedzieć, jak firmy wdrażają modele.

## Zrozumienie różnych typów modeli LLM

Modele LLM mogą mieć wiele kategoryzacji opartych na ich architekturze, danych treningowych i przypadkach użycia. Zrozumienie tych różnic pomoże naszemu startupowi wybrać odpowiedni model dla danego scenariusza oraz zrozumieć, jak testować, iterować i poprawiać wydajność.

Istnieje wiele różnych typów modeli LLM, a wybór modelu zależy od tego, do czego zamierzasz go użyć, od twoich danych, ile jesteś gotów zapłacić i więcej.

W zależności od tego, czy zamierzasz używać modeli do generowania tekstu, dźwięku, wideo, obrazów i tak dalej, możesz wybrać inny typ modelu.

- **Rozpoznawanie audio i mowy**. W tym celu modele typu Whisper są doskonałym wyborem, ponieważ są ogólnego przeznaczenia i skierowane na rozpoznawanie mowy. Są trenowane na różnorodnym materiale audio i mogą wykonywać wielojęzyczne rozpoznawanie mowy. Dowiedz się więcej o [modelach typu Whisper tutaj](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Generowanie obrazów**. Do generowania obrazów DALL-E i Midjourney są dwoma bardzo dobrze znanymi wyborami. DALL-E jest oferowany przez Azure OpenAI. [Przeczytaj więcej o DALL-E tutaj](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) oraz w Rozdziale 9 tego kursu.

- **Generowanie tekstu**. Większość modeli jest trenowana na generowaniu tekstu i masz duży wybór od GPT-3.5 do GPT-4. Mają one różne koszty, przy czym GPT-4 jest najdroższy. Warto zajrzeć do [playground Azure OpenAI](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst), aby ocenić, które modele najlepiej pasują do twoich potrzeb pod względem możliwości i kosztów.

- **Multimodalność**. Jeśli szukasz obsługi wielu typów danych na wejściu i wyjściu, warto zajrzeć do modeli takich jak [gpt-4 turbo z funkcją vision lub gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) - najnowszych wersji modeli OpenAI - które są zdolne do łączenia przetwarzania języka naturalnego ze zrozumieniem wizualnym, umożliwiając interakcje poprzez interfejsy multimodalne.

Wybór modelu oznacza, że otrzymujesz pewne podstawowe możliwości, które jednak mogą nie być wystarczające. Często masz firmowe dane, o których musisz jakoś poinformować model LLM. Istnieje kilka różnych sposobów podejścia do tego problemu, więcej na ten temat w nadchodzących sekcjach.

### Modele Fundamentalne a Modele LLM

Termin Model Fundamentalny został [ukuty przez badaczy ze Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) i zdefiniowany jako model SI, który spełnia pewne kryteria, takie jak:

- **Są trenowane przy użyciu uczenia nienadzorowanego lub uczenia samodzielnego**, co oznacza, że są trenowane na nieoznakowanych danych multimodalnych i nie wymagają ludzkiej adnotacji ani oznaczania danych do ich procesu treningu.
- **Są to bardzo duże modele**, oparte na bardzo głębokich sieciach neuronowych trenowanych na miliardach parametrów.
- **Zwykle mają służyć jako 'fundament' dla innych modeli**, co oznacza, że mogą być używane jako punkt wyjścia dla innych modeli budowanych na ich podstawie, co można zrobić poprzez dostrojenie (fine-tuning).

![Modele Fundamentalne a Modele LLM](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Źródło obrazu: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Aby bardziej wyjaśnić to rozróżnienie, weźmy ChatGPT jako przykład. Aby zbudować pierwszą wersję ChatGPT, model o nazwie GPT-3.5 służył jako model fundamentalny. Oznacza to, że OpenAI użyło pewnych danych specyficznych dla czatu, aby stworzyć dostrojoną wersję GPT-3.5, która była wyspecjalizowana w dobrym działaniu w scenariuszach konwersacyjnych, takich jak chatboty.

![Model Fundamentalny](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Źródło obrazu: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modele Open Source a Modele Własnościowe

Innym sposobem kategoryzacji modeli LLM jest to, czy są one open source czy własnościowe.

Modele open source są modelami, które są udostępniane publicznie i mogą być używane przez każdego. Są one często udostępniane przez firmę, która je stworzyła, lub przez społeczność badawczą. Modele te mogą być sprawdzane, modyfikowane i dostosowywane do różnych przypadków użycia w LLM. Jednak nie zawsze są zoptymalizowane do użytku produkcyjnego i mogą nie być tak wydajne jak modele własnościowe. Ponadto finansowanie dla modeli open source może być ograniczone i mogą one nie być utrzymywane długoterminowo lub mogą nie być aktualizowane o najnowsze badania. Przykładami popularnych modeli open source są [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) i [LLaMA](https://llama.meta.com).

Modele własnościowe są modelami, które są własnością firmy i nie są udostępniane publicznie. Modele te są często zoptymalizowane do użytku produkcyjnego. Jednak nie mogą być sprawdzane, modyfikowane ani dostosowywane do różnych przypadków użycia. Ponadto nie zawsze są dostępne za darmo i mogą wymagać subskrypcji lub płatności za użytkowanie. Ponadto użytkownicy nie mają kontroli nad danymi, które są używane do trenowania modelu, co oznacza, że muszą powierzyć właścicielowi modelu zapewnienie zobowiązania do ochrony prywatności danych i odpowiedzialnego używania SI. Przykładami popularnych modeli własnościowych są [modele OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) lub [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding vs Generowanie Obrazów vs Generowanie Tekstu i Kodu

Modele LLM można również kategoryzować według generowanego przez nie wyjścia.

Embeddingi to zestaw modeli, które mogą przekształcić tekst w formę numeryczną, zwaną embeddingiem, która jest numeryczną reprezentacją tekstu wejściowego. Embeddingi ułatwiają maszynom zrozumienie relacji między słowami lub zdaniami i mogą być wykorzystywane jako dane wejściowe przez inne modele, takie jak modele klasyfikacyjne lub modele klastrowania, które mają lepszą wydajność na danych numerycznych. Modele embeddingu są często używane do uczenia transferowego, gdzie model jest budowany dla zadania zastępczego, dla którego istnieje obfitość danych, a następnie wagi modelu (embeddingi) są ponownie wykorzystywane do innych zadań. Przykładem tej kategorii są [embeddingi OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Modele generowania obrazów to modele, które generują obrazy. Modele te są często używane do edycji obrazów, syntezy obrazów i tłumaczenia obrazów. Modele generowania obrazów są często trenowane na dużych zbiorach danych obrazów, takich jak [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), i mogą być używane do generowania nowych obrazów lub do edycji istniejących obrazów za pomocą technik inpainting, super-resolution i koloryzacji. Przykłady obejmują [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) i [modele Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generowanie obrazów](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Modele generowania tekstu i kodu to modele, które generują tekst lub kod. Modele te są często używane do podsumowywania tekstu, tłumaczenia i odpowiadania na pytania. Modele generowania tekstu są często trenowane na dużych zbiorach danych tekstowych, takich jak [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), i mogą być używane do generowania nowego tekstu lub do odpowiadania na pytania. Modele generowania kodu, jak [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), są często trenowane na dużych zbiorach danych kodu, takich jak GitHub, i mogą być używane do generowania nowego kodu lub do naprawiania błędów w istniejącym kodzie.

![Generowanie tekstu i kodu](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Encoder-Decoder vs Tylko Decoder

Aby porozmawiać o różnych typach architektur modeli LLM, użyjmy analogii.

Wyobraź sobie, że twój menedżer przydzielił ci zadanie napisania quizu dla studentów. Masz dwóch kolegów; jeden nadzoruje tworzenie treści, a drugi nadzoruje ich przegląd.

Twórca treści jest jak model wyłącznie Decoder, może spojrzeć na temat i zobaczyć, co już napisałeś, a następnie może napisać kurs na tej podstawie. Są bardzo dobrzy w pisaniu angażujących i pouczających treści, ale nie są bardzo dobrzy w zrozumieniu tematu i celów nauczania. Przykładami modeli Decoder są modele z rodziny GPT, takie jak GPT-3.

Recenzent jest jak model wyłącznie Encoder, patrzą na napisany kurs i odpowiedzi, zauważając relacje między nimi i rozumiejąc kontekst, ale nie są dobrzy w generowaniu treści. Przykładem modelu wyłącznie Encoder byłby BERT.

Wyobraź sobie, że możemy mieć kogoś, kto mógłby zarówno tworzyć, jak i recenzować quiz, to jest model Encoder-Decoder. Przykładami byłyby BART i T5.

### Usługa vs Model

Teraz porozmawiajmy o różnicy między usługą a modelem. Usługa to produkt oferowany przez Dostawcę Usług Chmurowych i często jest kombinacją modeli, danych i innych komponentów. Model jest podstawowym komponentem usługi i często jest modelem fundamentalnym, takim jak LLM.

Usługi są często zoptymalizowane do użytku produkcyjnego i często łatwiejsze w użyciu niż modele, dzięki graficznemu interfejsowi użytkownika. Jednak usługi nie zawsze są dostępne za darmo i mogą wymagać subskrypcji lub płatności za użytkowanie, w zamian za wykorzystanie sprzętu i zasobów właściciela usługi, optymalizację wydatków i łatwe skalowanie. Przykładem usługi jest [Usługa Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), która oferuje plan opłat pay-as-you-go, co oznacza, że użytkownicy są obciążani proporcjonalnie do tego, ile korzystają z usługi. Ponadto Usługa Azure OpenAI oferuje bezpieczeństwo klasy korporacyjnej i odpowiedzialny framework sztucznej inteligencji oprócz możliwości modeli.

Modele to tylko Sieć Neuronowa, z parametrami, wagami i innymi elementami. Pozwalają firmom na uruchamianie lokalnie, jednak będą musiały kupić sprzęt, zbudować strukturę do skalowania i kupić licencję lub użyć modelu open-source. Model taki jak LLaMA jest dostępny do użytku, wymagając mocy obliczeniowej do uruchomienia modelu.

## Jak testować i iterować z różnymi modelami, aby zrozumieć wydajność w Azure

Gdy nasz zespół zbadał już obecny krajobraz modeli LLM i zidentyfikował kilku dobrych kandydatów do swoich scenariuszy, kolejnym krokiem jest przetestowanie ich na swoich danych i na swoim obciążeniu. Jest to proces iteracyjny, przeprowadzany przez eksperymenty i pomiary.
Większość modeli, które wspomnieliśmy w poprzednich paragrafach (modele OpenAI, modele open source jak Llama2 i transformery Hugging Face), jest dostępna w [Katalogu Modeli](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) w [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) to Platforma Chmurowa zaprojektowana dla deweloperów do budowania aplikacji generatywnej SI i zarządzania całym cyklem życia rozwoju - od eksperymentowania do ewaluacji - poprzez połączenie wszystkich usług Azure AI w jednym hubie z wygodnym interfejsem GUI. Katalog Modeli w Azure AI Studio umożliwia użytkownikowi:

- Znalezienie interesującego Modelu Fundamentalnego w katalogu - zarówno własnościowego, jak i open source, filtrując według zadania, licencji lub nazwy. Aby poprawić wyszukiwalność, modele są zorganizowane w kolekcje, takie jak kolekcja Azure OpenAI, kolekcja Hugging Face i więcej.

![Katalog modeli](../../images/AzureAIStudioModelCatalog.png?WT.mc_id=academic-105485-koreyst)

- Przegląd karty modelu, w tym szczegółowego opisu zamierzonego użycia i danych treningowych, przykładów kodu i wyników ewaluacji na wewnętrznej bibliotece ewaluacji.

![Karta modelu](../../images/ModelCard.png?WT.mc_id=academic-105485-koreyst)

- Porównanie benchmarków między modelami i zbiorami danych dostępnymi w branży, aby ocenić, który z nich spełnia scenariusz biznesowy, poprzez panel [Benchmarki Modeli](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Benchmarki modeli](../../images/ModelBenchmarks.png?WT.mc_id=academic-105485-koreyst)

- Dostrojenie modelu na niestandardowych danych treningowych, aby poprawić wydajność modelu w konkretnym obciążeniu, wykorzystując możliwości eksperymentowania i śledzenia Azure AI Studio.

![Dostrajanie modelu](../../images/FineTuning.png?WT.mc_id=academic-105485-koreyst)

- Wdrożenie oryginalnego wstępnie wytrenowanego modelu lub dostrojonej wersji do zdalnej analizy w czasie rzeczywistym - zarządzanego obliczenia - lub bezserwerowego punktu końcowego API - [pay-as-you-go](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - aby umożliwić aplikacjom korzystanie z niego.

![Wdrożenie modelu](../../images/ModelDeploy.png?WT.mc_id=academic-105485-koreyst)

> [!NOTE]
> Nie wszystkie modele w katalogu są obecnie dostępne do dostrajania i/lub wdrażania pay-as-you-go. Sprawdź kartę modelu, aby uzyskać szczegółowe informacje na temat możliwości i ograniczeń modelu.

## Poprawianie wyników LLM

Zbadaliśmy z naszym zespołem startupowym różne rodzaje modeli LLM i Platformę Chmurową (Azure Machine Learning) umożliwiającą nam porównanie różnych modeli, ocenę ich na danych testowych, poprawę wydajności i wdrożenie ich na punktach końcowych analizy.

Ale kiedy powinni rozważyć dostrojenie modelu zamiast używania wstępnie wytrenowanego? Czy istnieją inne podejścia do poprawy wydajności modelu w konkretnych obciążeniach?

Istnieje kilka podejść, które firma może wykorzystać, aby uzyskać potrzebne wyniki z LLM. Możesz wybrać różne typy modeli o różnych stopniach treningu podczas wdrażania LLM w produkcji, o różnych poziomach złożoności, kosztach i jakości. Oto kilka różnych podejść:

- **Inżynieria promptów z kontekstem**. Pomysł polega na dostarczeniu wystarczającego kontekstu podczas promptowania, aby zapewnić uzyskanie potrzebnych odpowiedzi.

- **Retrieval Augmented Generation, RAG**. Twoje dane mogą istnieć na przykład w bazie danych lub w punkcie końcowym sieci, aby zapewnić, że te dane lub ich podzbiór są uwzględnione w momencie promptowania, możesz pobrać odpowiednie dane i uczynić je częścią promptu użytkownika.

- **Dostrojony model**. Tutaj, dalej trenowałeś model na własnych danych, co doprowadziło do tego, że model jest bardziej dokładny i reaktywny na twoje potrzeby, ale może być kosztowny.

![Wdrażanie LLM](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Źródło obrazu: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Inżynieria Promptów z Kontekstem

Wstępnie wytrenowane modele LLM działają bardzo dobrze na ogólnych zadaniach języka naturalnego, nawet przy wywołaniu ich krótkim promptem, jak zdanie do uzupełnienia lub pytanie – tak zwane uczenie "zero-shot".

Jednak im bardziej użytkownik może sformułować swoje zapytanie, ze szczegółowym żądaniem i przykładami – Kontekstem – tym bardziej dokładna i bliższa oczekiwaniom użytkownika będzie odpowiedź. W tym przypadku mówimy o uczeniu "one-shot", jeśli prompt zawiera tylko jeden przykład, i uczeniu "few-shot", jeśli zawiera wiele przykładów.
Inżynieria promptów z kontekstem jest najbardziej ekonomicznym podejściem na początek.

### Retrieval Augmented Generation (RAG)

Modele LLM mają ograniczenie, że mogą wykorzystywać tylko dane, które zostały użyte podczas ich treningu do generowania odpowiedzi. Oznacza to, że nie wiedzą nic o faktach, które miały miejsce po ich procesie treningu, i nie mogą uzyskać dostępu do niepublicznych informacji (takich jak dane firmowe).
Można to przezwyciężyć dzięki RAG, technice, która wzbogaca prompt o zewnętrzne dane w postaci fragmentów dokumentów, biorąc pod uwagę limity długości promptu. Jest to wspierane przez narzędzia baz danych wektorowych (takie jak [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), które pobierają użyteczne fragmenty z różnych predefiniowanych źródeł danych i dodają je do Kontekstu promptu.

Ta technika jest bardzo pomocna, gdy firma nie ma wystarczających danych, wystarczająco dużo czasu lub zasobów do dostrojenia LLM, ale nadal chce poprawić wydajność w konkretnym obciążeniu i zmniejszyć ryzyko zmyśleń, tj. mistyfikacji rzeczywistości lub szkodliwych treści.

### Dostrojony model

Dostrajanie to proces, który wykorzystuje uczenie transferowe, aby 'dostosować' model do zadania podrzędnego lub rozwiązania konkretnego problemu. W przeciwieństwie do uczenia few-shot i RAG, skutkuje wygenerowaniem nowego modelu, z aktualizowanymi wagami i stronniczością. Wymaga zestawu przykładów treningowych składających się z pojedynczego wejścia (promptu) i powiązanego wyjścia (uzupełnienia).
Byłoby to preferowane podejście, jeśli:

- **Używanie dostrojonych modeli**. Firma chciałaby używać dostrojonych mniej zaawansowanych modeli (jak modele embeddingu) zamiast modeli o wysokiej wydajności, co skutkuje bardziej ekonomicznym i szybkim rozwiązaniem.

- **Rozważanie opóźnienia**. Opóźnienie jest ważne dla konkretnego przypadku użycia, więc nie jest możliwe użycie bardzo długich promptów lub liczba przykładów, których model powinien się nauczyć, nie mieści się w limicie długości promptu.

- **Utrzymywanie aktualności**. Firma ma dużo wysokiej jakości danych i etykiet prawdy, a także zasoby wymagane do utrzymania tych danych na bieżąco.

### Wytrenowany model

Trenowanie LLM od podstaw jest bez wątpienia najtrudniejszym i najbardziej złożonym podejściem do przyjęcia, wymagającym ogromnych ilości danych, wykwalifikowanych zasobów i odpowiedniej mocy obliczeniowej. Tę opcję należy rozważyć tylko w scenariuszu, w którym firma ma przypadek użycia specyficzny dla domeny i dużą ilość danych skoncentrowanych na domenie.

## Sprawdzenie wiedzy

Jakie mogłoby być dobre podejście do poprawy wyników uzupełnień LLM?

1. Inżynieria promptów z kontekstem
1. RAG
1. Dostrojony model

A:3, jeśli masz czas, zasoby i wysokiej jakości dane, dostrajanie jest lepszą opcją, aby być na bieżąco. Jednak jeśli chcesz poprawić rzeczy, a brakuje ci czasu, warto najpierw rozważyć RAG.

## 🚀 Wyzwanie

Przeczytaj więcej o tym, jak możesz [używać RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) dla swojego biznesu.

## Świetna Praca, Kontynuuj Naukę

Po ukończeniu tej lekcji, sprawdź naszą [kolekcję materiałów do nauki Generatywnej SI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy o Generatywnej SI!

Przejdź do Lekcji 3, gdzie przyjrzymy się [budowaniu z Generatywną SI w sposób odpowiedzialny](../../../03-using-generative-ai-responsibly/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
