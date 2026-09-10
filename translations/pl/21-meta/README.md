# Budowanie z modelami rodziny Meta

## Wprowadzenie

Ta lekcja będzie obejmować:

- Eksplorację dwóch głównych modeli rodziny Meta - Llama 3.1 i Llama 3.2
- Zrozumienie przypadków użycia i scenariuszy dla każdego modelu
- Przykład kodu pokazujący unikalne cechy każdego modelu


## Rodzina modeli Meta

W tej lekcji przeanalizujemy 2 modele z rodziny Meta lub "Stado Llam" - Llama 3.1 i Llama 3.2.

Modele te występują w różnych wariantach i są dostępne w [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Uwaga:** GitHub Models zostanie wycofany pod koniec lipca 2026 roku. Oto więcej szczegółów dotyczących korzystania z [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) do prototypowania z modelami AI.

Warianty modeli:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Uwaga: Llama 3 jest również dostępna w Microsoft Foundry Models, ale nie będzie omawiana w tej lekcji*

## Llama 3.1

Posiadając 405 miliardów parametrów, Llama 3.1 mieści się w kategorii open source LLM.

Model jest ulepszeniem wcześniejszego wydania Llama 3, oferując:

- Większe okno kontekstu - 128k tokenów w porównaniu do 8k tokenów
- Większą maksymalną liczbę tokenów wyjściowych - 4096 w porównaniu do 2048
- Lepsze wsparcie wielojęzyczne - dzięki zwiększonej liczbie tokenów treningowych

To pozwala Llama 3.1 obsługiwać bardziej złożone przypadki użycia przy budowie aplikacji GenAI, w tym:
- Natywne wywoływanie funkcji - możliwość wywoływania zewnętrznych narzędzi i funkcji poza przepływem pracy LLM
- Lepsza wydajność RAG - dzięki większemu oknu kontekstu
- Generowanie danych syntetycznych - możliwość tworzenia skutecznych danych do zadań takich jak fine-tuning

### Natywne wywoływanie funkcji

Llama 3.1 została udoskonalona, by skuteczniej wykonywać wywołania funkcji lub narzędzi. Ma również dwa wbudowane narzędzia, które model może zidentyfikować jako potrzebne do użycia na podstawie polecenia użytkownika. Te narzędzia to:

- **Brave Search** - może być używany do uzyskania aktualnych informacji, takich jak pogoda, wykonując wyszukiwanie w sieci
- **Wolfram Alpha** - może być używany do bardziej złożonych obliczeń matematycznych, więc nie jest konieczne pisanie własnych funkcji

Możesz również tworzyć własne niestandardowe narzędzia, które LLM może wywoływać.

W poniższym przykładzie kodu:

- Definiujemy dostępne narzędzia (brave_search, wolfram_alpha) w poleceniu systemowym.
- Wysyłamy polecenie użytkownika z pytaniem o pogodę w określonym mieście.
- LLM odpowie wywołaniem narzędzia Brave Search, które będzie wyglądać tak: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Uwaga: ten przykład tylko wykonuje wywołanie narzędzia, jeśli chcesz uzyskać wyniki, musisz założyć darmowe konto na stronie Brave API i zdefiniować samą funkcję.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Pobierz je ze strony "Przegląd" projektu Microsoft Foundry
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Mimo że jest to LLM, jednym z ograniczeń Llama 3.1 jest brak multimodalności. To znaczy, brak możliwości użycia różnych typów wejściowych, takich jak obrazy jako polecenia, oraz udzielania odpowiedzi. Ta zdolność jest jedną z głównych cech Llama 3.2. Funkcje te obejmują również:

- Multimodalność - możliwość oceny zarówno tekstowych, jak i obrazkowych poleceń
- Warianty małe do średnich (11B i 90B) - co zapewnia elastyczne opcje wdrożenia,
- Warianty tylko tekstowe (1B i 3B) - pozwalają na wdrożenie modelu na urządzeniach edge / mobilnych i zapewniają niską latencję

Wsparcie multimodalne stanowi duży krok w świecie modeli open source. Przykład kodu poniżej przyjmuje zarówno obraz, jak i polecenie tekstowe, aby uzyskać analizę obrazu od Llama 3.2 90B.


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

# Pobierz je ze strony "Przegląd" Twojego projektu Microsoft Foundry
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## Nauka tu się nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->