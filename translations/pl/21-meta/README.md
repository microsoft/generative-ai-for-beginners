# Budowanie z modelami rodziny Meta

## Wprowadzenie

Ta lekcja obejmie:

- Eksplorację dwóch głównych modeli rodziny Meta - Llama 3.1 i Llama 3.2
- Zrozumienie zastosowań i scenariuszy dla każdego modelu
- Przykład kodu pokazujący unikalne cechy każdego modelu

## Rodzina modeli Meta

W tej lekcji zapoznamy się z 2 modelami z rodziny Meta lub "stada Llama" - Llama 3.1 i Llama 3.2.

Modele te dostępne są w różnych wariantach i można je znaleźć na rynku modeli GitHub. Oto więcej szczegółów na temat korzystania z modeli GitHub, aby [prototypować z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Warianty modeli:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Uwaga: Llama 3 jest również dostępna w modelach GitHub, ale nie będzie omawiana w tej lekcji*

## Llama 3.1

Przy 405 miliardach parametrów, Llama 3.1 mieści się w kategorii otwartych modeli LLM.

Model jest ulepszeniem wcześniejszej wersji Llama 3, oferując:

- Większe okno kontekstowe - 128k tokenów vs 8k tokenów
- Większą maksymalną liczbę tokenów wyjściowych - 4096 vs 2048
- Lepsze wsparcie wielojęzyczne - dzięki zwiększonej liczbie tokenów treningowych

To pozwala Llama 3.1 radzić sobie z bardziej złożonymi przypadkami użycia podczas budowy aplikacji GenAI, w tym:
- Natywne wywoływanie funkcji - możliwość wywoływania zewnętrznych narzędzi i funkcji poza przepływem LLM
- Lepsza wydajność RAG - dzięki większemu oknu kontekstowemu
- Generowanie danych syntetycznych - możliwość tworzenia efektywnych danych do zadań takich jak fine-tuning

### Natywne wywoływanie funkcji

Llama 3.1 została dostrojona tak, aby efektywniej wykonywać wywołania funkcji lub narzędzi. Posiada również dwa wbudowane narzędzia, które model potrafi rozpoznać jako konieczne do użycia na podstawie zapytania użytkownika. Narzędzia te to:

- **Brave Search** - może być używane do pobierania aktualnych informacji, takich jak pogoda, wykonując wyszukiwanie w sieci
- **Wolfram Alpha** - może być używane do bardziej zaawansowanych obliczeń matematycznych, więc nie jest wymagane pisanie własnych funkcji.

Możesz także tworzyć własne niestandardowe narzędzia, które LLM może wywoływać.

W przykładzie kodu poniżej:

- Definiujemy dostępne narzędzia (brave_search, wolfram_alpha) w podpowiedzi systemowej.
- Wysyłamy zapytanie użytkownika dotyczące pogody w określonym mieście.
- LLM odpowie wywołaniem narzędzia Brave Search, które będzie wyglądać tak: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Uwaga: Ten przykład wykonuje tylko wywołanie narzędzia, jeśli chcesz uzyskać wyniki, musisz założyć darmowe konto na stronie Brave API i samodzielnie zdefiniować funkcję.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Pomimo bycia modelem LLM, jedną z ograniczeń Llama 3.1 jest brak multimodalności. To znaczy, brak możliwości używania różnych rodzajów danych wejściowych, takich jak obrazy, jako podpowiedzi oraz udzielania na nie odpowiedzi. Ta funkcja jest jedną z głównych cech Llama 3.2. Inne cechy obejmują:

- Multimodalność - zdolność do oceny zarówno tekstowych, jak i obrazowych podpowiedzi
- Warianty o rozmiarach od małych do średnich (11B i 90B) - zapewniają elastyczne opcje wdrożeniowe,
- Warianty tylko tekstowe (1B i 3B) - pozwalają na wdrożenie modelu na urządzeniach edge / mobilnych i zapewniają niskie opóźnienia

Wsparcie multimodalne to duży krok naprzód w świecie otwartych modeli. Przykład kodu poniżej bierze zarówno obraz, jak i podpowiedź tekstową, aby uzyskać analizę obrazu z Llama 3.2 90B.

### Wsparcie multimodalne z Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Nauka nie kończy się tutaj, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat Generatywnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonywanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->