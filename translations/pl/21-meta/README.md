<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:10:50+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "pl"
}
-->
# Budowanie z modelami rodziny Meta

## Wprowadzenie

Ta lekcja obejmie:

- Eksplorację dwóch głównych modeli rodziny Meta - Llama 3.1 i Llama 3.2
- Zrozumienie przypadków użycia i scenariuszy dla każdego modelu
- Przykład kodu pokazujący unikalne cechy każdego modelu

## Rodzina modeli Meta

W tej lekcji zbadamy 2 modele z rodziny Meta lub "Stado Llam" - Llama 3.1 i Llama 3.2

Modele te występują w różnych wariantach i są dostępne na rynku modeli GitHub. Oto więcej szczegółów na temat korzystania z modeli GitHub do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Warianty modeli:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Uwaga: Llama 3 jest również dostępna na GitHub Models, ale nie będzie omawiana w tej lekcji*

## Llama 3.1

Z 405 miliardami parametrów, Llama 3.1 mieści się w kategorii otwartoźródłowych LLM.

Model jest ulepszeniem wcześniejszego wydania Llama 3 oferując:

- Większe okno kontekstu - 128k tokenów vs 8k tokenów
- Większa maksymalna liczba tokenów wyjściowych - 4096 vs 2048
- Lepsze wsparcie wielojęzyczne - dzięki zwiększeniu liczby tokenów treningowych

To umożliwia Llama 3.1 obsługę bardziej złożonych przypadków użycia przy budowaniu aplikacji GenAI, w tym:
- Natywne wywoływanie funkcji - możliwość wywoływania zewnętrznych narzędzi i funkcji poza przepływem pracy LLM
- Lepsza wydajność RAG - dzięki większemu oknu kontekstu
- Generowanie danych syntetycznych - możliwość tworzenia efektywnych danych do zadań takich jak dopasowywanie

### Natywne wywoływanie funkcji

Llama 3.1 została dostrojona do bardziej efektywnego wywoływania funkcji lub narzędzi. Posiada również dwa wbudowane narzędzia, które model może zidentyfikować jako potrzebne do użycia na podstawie podpowiedzi od użytkownika. Te narzędzia to:

- **Brave Search** - Może być używane do uzyskiwania aktualnych informacji, takich jak pogoda, poprzez przeszukiwanie internetu
- **Wolfram Alpha** - Może być używane do bardziej skomplikowanych obliczeń matematycznych, dzięki czemu nie trzeba pisać własnych funkcji.

Możesz również stworzyć własne niestandardowe narzędzia, które LLM może wywoływać.

W poniższym przykładzie kodu:

- Definiujemy dostępne narzędzia (brave_search, wolfram_alpha) w systemowym prompt.
- Wysyłamy prompt użytkownika, który pyta o pogodę w określonym mieście.
- LLM odpowie wywołaniem narzędzia Brave Search, które będzie wyglądać tak: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Uwaga: Ten przykład jedynie wykonuje wywołanie narzędzia, jeśli chcesz uzyskać wyniki, musisz stworzyć darmowe konto na stronie Brave API i zdefiniować samą funkcję`

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

Pomimo bycia LLM, jednym z ograniczeń Llama 3.1 jest multimodalność. To znaczy, możliwość użycia różnych typów wejścia, takich jak obrazy jako podpowiedzi i dostarczanie odpowiedzi. Ta umiejętność jest jedną z głównych cech Llama 3.2. Te cechy obejmują również:

- Multimodalność - posiada zdolność oceny zarówno tekstowych, jak i obrazowych podpowiedzi
- Warianty od małych do średnich (11B i 90B) - to zapewnia elastyczne opcje wdrożenia,
- Warianty tylko tekstowe (1B i 3B) - to pozwala na wdrożenie modelu na urządzeniach krawędziowych / mobilnych i zapewnia niską latencję

Wsparcie multimodalne stanowi duży krok w świecie modeli otwartoźródłowych. Poniższy przykład kodu przyjmuje zarówno obraz, jak i tekst jako podpowiedź, aby uzyskać analizę obrazu od Llama 3.2 90B.

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

Po ukończeniu tej lekcji, zapoznaj się z naszą [kolekcją nauki o generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować pogłębianie wiedzy na temat generatywnej AI!

**Zrzeczenie się odpowiedzialności**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.