# Budowanie z modelami rodziny Meta

## Wprowadzenie

Ta lekcja obejmie:

- Odkrywanie dwóch głównych modeli rodziny Meta - Llama 3.1 i Llama 3.2
- Zrozumienie przypadków użycia i scenariuszy dla każdego modelu
- Przykład kodu pokazujący unikalne cechy każdego modelu

## Rodzina Modeli Meta

W tej lekcji omówimy 2 modele z rodziny Meta lub "Stada Llama" - Llama 3.1 i Llama 3.2

Modele te występują w różnych wariantach i są dostępne na rynku modeli GitHub. Oto więcej szczegółów na temat używania modeli GitHub do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Warianty modeli:

- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

_Uwaga: Llama 3 jest również dostępna na GitHub Models, ale nie zostanie omówiona w tej lekcji_

## Llama 3.1

Mając 405 miliardów parametrów, Llama 3.1 mieści się w kategorii otwartych modeli LLM.

Model ten jest ulepszeniem wcześniejszej wersji Llama 3, oferując:

- Większe okno kontekstowe - 128k tokenów vs 8k tokenów
- Większą maksymalną liczbę tokenów wyjściowych - 4096 vs 2048
- Lepsze wsparcie wielojęzyczne - dzięki zwiększeniu liczby tokenów treningowych

Umożliwia to Llama 3.1 obsługę bardziej złożonych przypadków użycia podczas tworzenia aplikacji GenAI, w tym:

- Natywne wywoływanie funkcji - możliwość wywoływania zewnętrznych narzędzi i funkcji poza przepływem pracy LLM
- Lepsza wydajność RAG - dzięki większemu oknu kontekstowemu
- Generowanie danych syntetycznych - możliwość tworzenia efektywnych danych do zadań takich jak dostrajanie

### Natywne wywoływanie funkcji

Llama 3.1 została dostrojona, aby być bardziej efektywna w wywoływaniu funkcji lub narzędzi. Posiada również dwa wbudowane narzędzia, które model może zidentyfikować jako potrzebne do użycia na podstawie promptu użytkownika. Te narzędzia to:

- **Brave Search** - Może być używane do uzyskiwania aktualnych informacji, takich jak pogoda, poprzez wyszukiwanie w sieci
- **Wolfram Alpha** - Może być używane do bardziej złożonych obliczeń matematycznych, więc pisanie własnych funkcji nie jest wymagane.

Możesz również tworzyć własne niestandardowe narzędzia, które LLM może wywoływać.

W poniższym przykładzie kodu:

- Definiujemy dostępne narzędzia (brave_search, wolfram_alpha) w prompcie systemowym.
- Wysyłamy prompt użytkownika, który pyta o pogodę w określonym mieście.
- LLM odpowie wywołaniem narzędzia Brave Search, które będzie wyglądać tak: `<|python_tag|>brave_search.call(query="Stockholm weather")`

\*Uwaga: Ten przykład tylko wykonuje wywołanie narzędzia, jeśli chcesz uzyskać wyniki, musisz utworzyć darmowe konto na stronie Brave API i zdefiniować samą funkcję`

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

Środowisko: ipython
Narzędzia: brave_search, wolfram_alpha
Data odcięcia wiedzy: Grudzień 2023
Dzisiejsza data: 23 Lipiec 2024

Jesteś pomocnym asystentem<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="Jaka jest pogoda w Sztokholmie?"),
]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Mimo że jest to LLM, jednym z ograniczeń Llama 3.1 jest multimodalność. Oznacza to zdolność do używania różnych typów danych wejściowych, takich jak obrazy, jako prompty i dostarczania odpowiedzi. Ta zdolność jest jedną z głównych cech Llama 3.2. Cechy te obejmują również:

- Multimodalność - ma zdolność do oceny zarówno promptów tekstowych, jak i obrazowych
- Warianty o małym i średnim rozmiarze (11B i 90B) - zapewnia to elastyczne opcje wdrażania
- Warianty tylko tekstowe (1B i 3B) - pozwala to na wdrażanie modelu na urządzeniach brzegowych/mobilnych i zapewnia niskie opóźnienia

Wsparcie multimodalne stanowi duży krok w świecie otwartych modeli. Poniższy przykład kodu przyjmuje zarówno obraz, jak i prompt tekstowy, aby uzyskać analizę obrazu z Llama 3.2 90B.

### Wsparcie Multimodalne z Llama 3.2

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
            content="Jesteś pomocnym asystentem, który szczegółowo opisuje obrazy."
        ),
        UserMessage(
            content=[
                TextContentItem(text="Co jest na tym obrazie?"),
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

## Nauka się tu nie kończy, kontynuuj Podróż

Po ukończeniu tej lekcji sprawdź naszą [Kolekcję Nauki o Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej podnosić swoją wiedzę o Generatywnej AI!
