# Eksploracja i porównywanie różnych LLM

[![Eksploracja i porównywanie różnych LLM](../../../translated_images/pl/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji_

W poprzedniej lekcji zobaczyliśmy, jak Generatywna AI zmienia krajobraz technologiczny, jak działają duże modele językowe (LLM) i jak firma – taka jak nasz startup – może je zastosować w swoich przypadkach użycia i rozwijać się! W tym rozdziale chcemy porównać i skontrastować różne typy dużych modeli językowych (LLM), aby zrozumieć ich zalety i wady.

Następnym krokiem na ścieżce startupu jest eksploracja aktualnego krajobrazu LLM i zrozumienie, które z nich nadają się do naszego przypadku użycia.

## Wprowadzenie

Ta lekcja obejmie:

- Różne typy LLM w obecnym krajobrazie.
- Testowanie, iterację i porównywanie różnych modeli dla twojego przypadku użycia w Azure.
- Jak wdrożyć LLM.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wybrać odpowiedni model dla swojego przypadku użycia.
- Zrozumieć, jak testować, iterować i poprawiać wydajność swojego modelu.
- Wiedzieć, jak firmy wdrażają modele.

## Zrozumienie różnych typów LLM

LLM mogą mieć wiele kategorii w zależności od ich architektury, danych treningowych i przypadku użycia. Zrozumienie tych różnic pomoże naszemu startupowi wybrać odpowiedni model na daną sytuację oraz zrozumieć, jak testować, iterować i poprawiać wydajność.

Istnieje wiele różnych typów modeli LLM, a wybór modelu zależy od tego, do czego planujesz ich używać, twoich danych, ile jesteś gotów zapłacić i innych czynników.

W zależności od tego, czy chcesz używać modeli do tekstu, dźwięku, wideo, generowania obrazów i innych, możesz wybrać inny typ modelu.

- **Rozpoznawanie dźwięku i mowy**. Modele w stylu Whisper wciąż są użytecznymi, ogólnego przeznaczenia modelami rozpoznawania mowy, ale obecnie w produkcji wybór obejmuje również nowsze modele zamiany mowy na tekst, takie jak `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` oraz warianty diarizacji. Oceń pokrycie językowe, diarizację, wsparcie w czasie rzeczywistym, opóźnienia i koszt dla twojego scenariusza. Dowiedz się więcej z [dokumentacji OpenAI do zamiany mowy na tekst](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Generowanie obrazów**. DALL-E i Midjourney to znane opcje generowania obrazów, ale obecne API OpenAI koncentrują się na modelach GPT Image takich jak `gpt-image-2`, podczas gdy Stable Diffusion, Imagen, Flux i inne rodziny modeli są również powszechnymi wyborami. Porównaj zgodność promptu, wsparcie edycji, kontrolę stylu, wymagania bezpieczeństwa i licencjonowanie. Dowiedz się więcej z [przewodnika po generowaniu obrazów OpenAI](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) oraz rozdziału 9 tego programu nauczania.

- **Generowanie tekstu**. Modele tekstowe obecnie obejmują modele czołowe, modele rozumowania, mniejsze modele o niskiej latencji oraz modele otwarto-wagowe. Obecne przykłady to modele OpenAI GPT-5.x, modele Anthropic Claude 4.x, modele Google Gemini 3.x, modele Meta Llama 4 oraz modele Mistral. Nie wybieraj tylko według daty wydania lub ceny; porównaj jakość wykonywanych zadań, opóźnienie, długość kontekstu, użycie narzędzi, zachowanie bezpieczeństwa, dostępność regionalną oraz całkowity koszt. [Katalog modeli Microsoft Foundry](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) to dobre miejsce do porównania modeli dostępnych na Azure.

- **Multi-modalność**. Wiele obecnych modeli może przetwarzać więcej niż tekst. Niektóre akceptują obrazy, dźwięk lub wejścia wideo; niektóre mogą wywoływać narzędzia; a modele specjalistyczne mogą generować obrazy, dźwięk lub wideo. Na przykład obecne modele OpenAI obsługują wejście tekstowe i obrazowe, modele Gemini mogą obsługiwać tekst, kod, obraz, dźwięk i wideo w zależności od wariantu, a Llama 4 Scout i Maverick to nativnie multimodalne modele o otwartych wagach. Zawsze sprawdzaj kartę modelu pod kątem obsługiwanych modalności wejścia i wyjścia przed budowaniem na niej przepływu pracy.

Wybór modelu oznacza, że masz podstawowe możliwości, które jednak mogą nie być wystarczające. Często masz dane specyficzne dla firmy, o których w jakiś sposób musisz poinformować LLM. Istnieje kilka różnych sposobów, aby to zrobić, więcej na ten temat w nadchodzących sekcjach.

### Modele bazowe versus LLM

Termin Model Bazowy został [ukuty przez badaczy ze Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) i zdefiniowany jako model AI, który spełnia pewne kryteria, takie jak:

- **Trenują się przy użyciu uczenia niesuperwizowanego lub samonadzorowanego**, co oznacza, że są trenowane na nieoznaczonych danych multimodalnych i nie wymagają ludzkiej anotacji ani etykietowania danych do procesu treningu.
- **Są bardzo dużymi modelami**, opartymi na bardzo głębokich sieciach neuronowych trenowanych na miliardach parametrów.
- **Zwykle przeznaczone są do służenia jako ‘podstawa’ dla innych modeli**, co oznacza, że mogą być wykorzystane jako punkt startowy dla budowy innych modeli, co można osiągnąć poprzez dostrajanie (fine-tuning).

![Modele bazowe versus LLM](../../../translated_images/pl/FoundationModel.e4859dbb7a825c94.webp)

Źródło obrazu: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Aby jeszcze bardziej wyjaśnić to rozróżnienie, weźmy ChatGPT jako historyczny przykład. Wczesne wersje ChatGPT wykorzystywały GPT-3.5 jako model bazowy. OpenAI następnie użyło danych specyficznych dla czatu i technik dostrajania, aby stworzyć wersję dopasowaną, która działała lepiej w scenariuszach konwersacyjnych, takich jak chatboty. Nowoczesne usługi AI często korzystają z kilku wariantów modeli, więc nazwa usługi i nazwa podstawowego modelu nie zawsze są tym samym.

![Model bazowy](../../../translated_images/pl/Multimodal.2c389c6439e0fc51.webp)

Źródło obrazu: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modele otwarte (open-weight/open-source) versus modele własnościowe

Innym sposobem kategoryzacji LLM jest podział na modele otwarto-wagowe, otwarto-źródłowe lub własnościowe.

Modele open-source i open-weight udostępniają artefakty modeli do inspekcji, pobrania lub dostosowania, ale ich licencje się różnią. Niektóre są w pełni open source, podczas gdy inne to modele open-weight z ograniczeniami użycia. Mogą być użyteczne, gdy firma potrzebuje większej kontroli nad wdrożeniem, lokalizacją danych, kosztami lub dostosowaniem. Jednak zespoły muszą jeszcze przejrzeć warunki licencji, koszty obsługi, utrzymanie, aktualizacje bezpieczeństwa i jakość ewaluacji przed użyciem ich w produkcji. Przykłady to [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), niektóre [modele Mistral](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) oraz wiele modeli hostowanych na [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Modele własnościowe są własnością dostawcy i są hostowane przez niego. Modele te często są zoptymalizowane do zarządzania w środowisku produkcyjnym i mogą oferować silne wsparcie, systemy bezpieczeństwa, integrację z narzędziami oraz skalowalność. Jednak klienci zwykle nie mogą przeglądać ani modyfikować wag modelu i muszą sprawdzać warunki dostawcy dotyczące prywatności, retencji, zgodności i akceptowalnego użycia. Przykłady to [modele OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) i [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus generowanie obrazów versus generowanie tekstu i kodu

LLM można również sklasyfikować według rodzaju generowanego wyjścia.

Embeddingi to zestaw modeli, które mogą konwertować tekst na formę numeryczną, zwaną embeddingiem, czyli numeryczną reprezentację tekstu wejściowego. Embeddingi ułatwiają maszynom rozumienie relacji między słowami lub zdaniami i mogą być wykorzystywane jako dane wejściowe dla innych modeli, takich jak modele klasyfikacyjne lub modele klastrowania, które osiągają lepsze wyniki na danych numerycznych. Modele embeddingowe są często używane w transfer learning, gdzie buduje się model dla zadania zastępczego, dla którego jest dużo danych, a następnie wagi modelu (embeddingi) są ponownie używane do innych zadań downstream. Przykładem tej kategorii są [embeddingi OpenAI](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/pl/Embedding.c3708fe988ccf760.webp)

Modele generowania obrazów to modele, które generują obrazy. Często są używane do edycji obrazów, syntezy obrazów oraz translacji obrazów. Modele generowania obrazów są zazwyczaj trenowane na dużych zbiorach danych obrazów, takich jak [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), i mogą generować nowe obrazy lub edytować istniejące za pomocą technik takich jak inpainting, super-rozdzielczość i kolorowanie. Przykłady to [modele GPT Image](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [modele Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) oraz modele Imagen.

![Generowanie obrazów](../../../translated_images/pl/Image.349c080266a763fd.webp)

Modele generowania tekstu i kodu to modele, które generują tekst lub kod. Często są używane do podsumowywania tekstów, tłumaczeń i udzielania odpowiedzi na pytania. Modele generowania tekstu są zwykle trenowane na dużych zbiorach tekstów, takich jak [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst) i mogą generować nowy tekst lub odpowiadać na pytania. Modele generowania kodu, jak [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), są często trenowane na dużych zbiorach kodu, takich jak GitHub, i potrafią generować nowy kod lub naprawiać błędy w istniejącym kodzie.

![Generowanie tekstu i kodu](../../../translated_images/pl/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Tylko Decoder

Aby omówić różne architektury LLM, użyjmy analogii.

Wyobraź sobie, że twój menedżer zadał ci napisanie quizu dla uczniów. Masz dwóch współpracowników; jeden zajmuje się tworzeniem treści, a drugi ich przeglądem.

Twórca treści jest jak model tylko decoder: może spojrzeć na temat, zobaczyć, co już napisałeś, a następnie dalej generować treść na podstawie tego kontekstu. Są bardzo dobrzy w pisaniu angażujących i informacyjnych treści, ale nie zawsze są najlepszym wyborem, gdy zadanie wymaga tylko klasyfikacji, wyszukiwania lub kodowania informacji. Przykładami modeli tylko decoder są rodziny modeli GPT i Llama.

Recenzent jest jak model tylko encoder, przygląda się napisanemu kursowi i odpowiedziom, dostrzega relacje między nimi i rozumie kontekst, ale nie jest dobry w generowaniu treści. Przykładem modelu tylko encoder byłby BERT.

Wyobraź sobie, że możemy mieć kogoś, kto może zarówno tworzyć, jak i przeglądać quiz – to jest model Encoder-Decoder. Przykłady to BART i T5.

### Usługa versus Model

Teraz porozmawiajmy o różnicy między usługą a modelem. Usługa to produkt oferowany przez Dostawcę Usług Chmurowych i często jest kombinacją modeli, danych i innych komponentów. Model jest kluczowym komponentem usługi i często jest modelem bazowym, takim jak LLM.

Usługi często są zoptymalizowane do produkcyjnego użytku i często łatwiejsze w użyciu niż modele, za pomocą interfejsu graficznego. Jednak usługi nie zawsze są dostępne za darmo i mogą wymagać subskrypcji lub płatności w zamian za korzystanie ze sprzętu i zasobów właściciela usługi, optymalizację kosztów i łatwe skalowanie. Przykładem usługi jest [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), która oferuje model płatności pay-as-you-go, co oznacza, że użytkownicy są obciążani proporcjonalnie do korzystania z usługi. Azure OpenAI Service oferuje również zabezpieczenia klasy korporacyjnej i ramy odpowiedzialnej AI na bazie możliwości modeli.

Modele to artefakty sieci neuronowych: parametry, wagi, architektura, tokenizer oraz konfiguracja wspierająca. Uruchomienie modelu lokalnie lub w środowisku prywatnym wymaga odpowiedniego sprzętu, infrastruktury serwującej, monitoringu oraz kompatybilnej licencji open-source/open-weight lub licencji komercyjnej. Modele open-weight, takie jak Llama 4 lub modele Mistral, można hostować samodzielnie, ale nadal potrzebują mocy obliczeniowej i wiedzy operacyjnej.

## Jak testować i iterować z różnymi modelami, aby zrozumieć wydajność na Azure


Gdy nasz zespół przeanalizuje aktualny krajobraz LLM i zidentyfikuje kilka dobrych kandydatów do swoich scenariuszy, kolejnym krokiem jest testowanie ich na własnych danych i obciążeniu. To proces iteracyjny, realizowany przez eksperymenty i pomiary.
Większość modeli, o których wspomnieliśmy we wcześniejszych akapitach (modele OpenAI, modele o otwartych wagach, takie jak Llama 4 i Mistral, oraz modele Hugging Face) jest dostępna w [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), dawniej Azure AI Studio/Azure AI Foundry, to zintegrowana platforma Azure do tworzenia aplikacji i agentów AI. Pomaga deweloperom zarządzać cyklem życia od eksperymentowania i ewaluacji po wdrażanie, monitorowanie i zarządzanie. Katalog modeli w Microsoft Foundry umożliwia użytkownikowi:

- Znalezienie interesującego modelu podstawowego w katalogu, w tym modeli sprzedawanych przez Azure oraz modeli od partnerów i dostawców społeczności. Użytkownicy mogą filtrować według zadania, dostawcy, licencji, opcji wdrożenia lub nazwy.

![Model catalog](../../../translated_images/pl/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Przejrzenie karty modelu, która zawiera szczegółowy opis zamierzonego zastosowania i danych treningowych, przykłady kodu oraz wyniki oceny z wewnętrznej biblioteki ewaluacyjnej.

![Model card](../../../translated_images/pl/ModelCard.598051692c6e400d.webp)

- Porównanie benchmarków pomiędzy modelami i dostępnymi w branży zestawami danych, aby ocenić, który spełnia wymagania biznesowe, za pomocą panelu [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Model benchmarks](../../../translated_images/pl/ModelBenchmarks.254cb20fbd06c03a.webp)

- Dostosowanie wspieranych modeli do danych treningowych niestandardowych celem poprawy wydajności modelu na konkretnym obciążeniu, wykorzystując możliwości eksperymentowania i śledzenia w Microsoft Foundry.

![Model fine-tuning](../../../translated_images/pl/FineTuning.aac48f07142e36fd.webp)

- Wdrożenie oryginalnego modelu uprzednio wytrenowanego lub wersji dostrojonej do zdalnego punktu końcowego inferencji w czasie rzeczywistym, przy użyciu zarządzanych opcji obliczeniowych lub bezserwerowych, aby umożliwić aplikacjom jego wykorzystanie.

![Model deployment](../../../translated_images/pl/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Nie wszystkie modele w katalogu są obecnie dostępne do dostrajania i/lub wdrażania na zasadzie pay-as-you-go. Sprawdź kartę modelu, aby poznać szczegóły dotyczące możliwości i ograniczeń modelu.

## Poprawa wyników LLM

Razem z naszym zespołem startupowym zbadaliśmy różne rodzaje LLM oraz platformę chmurową (Microsoft Foundry), która umożliwia porównanie różnych modeli, ocenę ich na danych testowych, poprawę wydajności i wdrożenie ich na punktach końcowych inferencji.

Ale kiedy powinni rozważyć dostrajanie modelu zamiast używania modelu uprzednio wytrenowanego? Czy istnieją inne podejścia do poprawy wydajności modelu na specyficznych obciążeniach?

Biznes może wykorzystać kilka podejść, aby uzyskać potrzebne wyniki z LLM. Można wybrać różne typy modeli o różnych stopniach treningu przy wdrażaniu LLM w produkcji, o różnym poziomie złożoności, kosztów i jakości. Oto niektóre z podejść:

- **Inżynieria promptów z kontekstem**. Idea polega na dostarczeniu wystarczającej ilości kontekstu podczas promptowania, aby otrzymać potrzebne odpowiedzi.

- **Retrieval Augmented Generation, RAG**. Twoje dane mogą istnieć na przykład w bazie danych lub punkcie końcowym sieciowym; aby zapewnić, że te dane lub ich podzbiór są uwzględnione w czasie promptowania, możesz pobrać odpowiednie dane i dołączyć je do promptu użytkownika.

- **Model dostrojony**. Tutaj model został dodatkowo wytrenowany na twoich własnych danych, co spowodowało, że model jest bardziej precyzyjny i lepiej odpowiada na Twoje potrzeby, ale może to być kosztowne.

![LLMs deployment](../../../translated_images/pl/Deploy.18b2d27412ec8c02.webp)

Źródło obrazu: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Inżynieria promptów z kontekstem

LLM wytrenowane uprzednio działają bardzo dobrze w uogólnionych zadaniach z językiem naturalnym, nawet wywoływane krótkim promptem, jak zdanie do dokończenia lub pytanie – tak zwane uczenie „zero-shot”.

Jednak im bardziej użytkownik potrafi sformułować swoje zapytanie, z dokładnym żądaniem i przykładami – czyli z Kontekstem – tym odpowiedź będzie dokładniejsza i bliższa oczekiwaniom użytkownika. W tym przypadku mówimy o „one-shot” learning, jeśli prompt zawiera tylko jeden przykład, oraz o „few-shot learning”, jeśli zawiera wiele przykładów.
Inżynieria promptów z kontekstem to najbardziej opłacalne podejście na start.

### Retrieval Augmented Generation (RAG)

LLM mają ograniczenie, że mogą używać tylko danych, które zostały wykorzystane podczas ich treningu do generowania odpowiedzi. Oznacza to, że nie znają faktów, które zdarzyły się po procesie treningu, i nie mogą uzyskać dostępu do informacji niepublicznych (jak dane firmy).
To można obejść za pomocą RAG, techniki, która wzbogaca prompt o zewnętrzne dane w formie fragmentów dokumentów, z uwzględnieniem limitu długości promptu. Technikę tę wspierają narzędzia baz danych wektorowych (takie jak [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), które pobierają użyteczne fragmenty z różnych zdefiniowanych źródeł danych i dodają je do Kontekstu promptu.

Ta technika jest bardzo pomocna, gdy biznes nie ma wystarczająco dużo danych, czasu lub zasobów na dostrajanie LLM, ale nadal chce poprawić wydajność na konkretnym obciążeniu i zmniejszyć ryzyko udzielania wymyślonych, przestarzałych lub niepopartych odpowiedzi.

### Model dostrojony

Dostrajanie to proces wykorzystujący transfer learning do „dostosowania” modelu do zadania końcowego lub rozwiązania konkretnego problemu. W przeciwieństwie do uczenia few-shot i RAG, skutkuje to wygenerowaniem nowego modelu, z zaktualizowanymi wagami i biasami. Wymaga zestawu przykładów treningowych składającego się z wejścia (promptu) oraz związanego z nim wyjścia (dokończenia).
To byłoby preferowane podejście, jeśli:

- **Używasz mniejszych modeli specyficznych dla zadania**. Biznes chce dostroić mniejszy model do wąskiego zadania zamiast wielokrotnie wywoływać większy model frontiera, co skutkuje bardziej opłacalnym i szybszym rozwiązaniem.

- **Bierze pod uwagę opóźnienia**. Opóźnienia są ważne dla określonego przypadku użycia, więc nie można użyć bardzo długich promptów lub liczba przykładów, które model ma się nauczyć, nie mieści się w limicie długości promptu.

- **Adaptuje stabilne zachowanie**. Biznes ma wiele wysokiej jakości przykładów i chce, aby model konsekwentnie stosował wzór zadania, format wyjścia, ton lub styl specyficzny dla domeny. Jeśli głównym problemem są świeże fakty lub prywatna wiedza, która często się zmienia, użyj RAG zamiast polegać wyłącznie na dostrajaniu.

### Model wytrenowany

Trenowanie LLM od podstaw jest bez wątpienia najtrudniejszym i najbardziej złożonym podejściem do przyjęcia, wymagającym ogromnej ilości danych, wykwalifikowanych zasobów oraz odpowiedniej mocy obliczeniowej. Opcję tę należy rozważyć tylko w scenariuszu, w którym biznes ma domenowy przypadek użycia i dużą ilość danych skoncentrowanych na domenie.

## Sprawdzenie wiedzy

Jakie podejście może być dobre do poprawy wyników dokończeń LLM?

1. Inżynieria promptów z kontekstem
1. RAG
1. Model dostrojony

O: Wszystkie trzy mogą pomóc. Zacznij od inżynierii promptów i kontekstu dla szybkich usprawnień oraz użyj RAG, gdy model potrzebuje aktualnych faktów lub prywatnych danych biznesowych. Wybierz dostrajanie, gdy masz wystarczająco dużo wysokiej jakości przykładów i potrzebujesz, aby model konsekwentnie stosował wzorzec zadania, format, ton lub domenę.

## 🚀 Wyzwanie

Dowiedz się więcej o tym, jak możesz [używać RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) w swoim biznesie.

## Świetna robota, kontynuuj naukę

Po ukończeniu tej lekcji zobacz naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

Przejdź do Lekcji 3, gdzie omówimy, jak [budować z Generative AI odpowiedzialnie](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->