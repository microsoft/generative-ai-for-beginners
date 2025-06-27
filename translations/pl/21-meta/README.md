<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:30:32+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "pl"
}
-->
# Budowanie z modelami rodziny Meta

## Wprowadzenie

Ta lekcja obejmie:

- Badanie dwóch głównych modeli rodziny Meta - Llama 3.1 i Llama 3.2
- Zrozumienie przypadków użycia i scenariuszy dla każdego modelu
- Przykład kodu pokazujący unikalne cechy każdego modelu

## Rodzina modeli Meta

W tej lekcji przyjrzymy się 2 modelom z rodziny Meta, zwanej "Stadko Llam" - Llama 3.1 i Llama 3.2.

Modele te występują w różnych wariantach i są dostępne na rynku modeli GitHub. Oto więcej szczegółów na temat korzystania z modeli GitHub do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Warianty modeli:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Uwaga: Llama 3 jest również dostępna na GitHub Models, ale nie będzie omawiana w tej lekcji*

## Llama 3.1

Z 405 miliardami parametrów, Llama 3.1 mieści się w kategorii open source LLM.

Model ten jest ulepszeniem wcześniejszej wersji Llama 3, oferując:

- Większe okno kontekstowe - 128k tokenów vs 8k tokenów
- Większa maksymalna liczba tokenów wyjściowych - 4096 vs 2048
- Lepsze wsparcie dla wielu języków - dzięki zwiększeniu liczby tokenów treningowych

Te cechy pozwalają Llama 3.1 radzić sobie z bardziej złożonymi przypadkami użycia przy budowaniu aplikacji GenAI, w tym:
- Natychmiastowe wywoływanie funkcji - możliwość wywoływania zewnętrznych narzędzi i funkcji poza przepływem pracy LLM
- Lepsza wydajność RAG - dzięki większemu oknu kontekstowemu
- Generowanie danych syntetycznych - możliwość tworzenia skutecznych danych do zadań takich jak dostrajanie

### Natychmiastowe wywoływanie funkcji

Llama 3.1 została dostrojona, aby być bardziej efektywna w wywoływaniu funkcji lub narzędzi. Posiada również dwa wbudowane narzędzia, które model może zidentyfikować jako wymagające użycia na podstawie podpowiedzi użytkownika. Te narzędzia to:

- **Brave Search** - Może być używane do uzyskiwania aktualnych informacji, takich jak pogoda, poprzez wykonywanie wyszukiwania w sieci
- **Wolfram Alpha** - Może być używane do bardziej złożonych obliczeń matematycznych, więc nie trzeba pisać własnych funkcji.

Możesz również stworzyć własne narzędzia, które LLM może wywołać.

W poniższym przykładzie kodu:

- Definiujemy dostępne narzędzia (brave_search, wolfram_alpha) w podpowiedzi systemowej.
- Wysyłamy podpowiedź użytkownika, która pyta o pogodę w określonym mieście.
- LLM odpowie wywołaniem narzędzia Brave Search, które będzie wyglądać tak: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Uwaga: Ten przykład tylko wywołuje narzędzie, jeśli chcesz uzyskać wyniki, musisz utworzyć darmowe konto na stronie Brave API i zdefiniować samą funkcję*

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

Pomimo bycia LLM, jednym z ograniczeń Llama 3.1 jest multimodalność. To znaczy, możliwość używania różnych typów wejść, takich jak obrazy jako podpowiedzi i dostarczanie odpowiedzi. Ta zdolność jest jedną z głównych cech Llama 3.2. Te cechy obejmują również:

- Multimodalność - ma zdolność oceny zarówno tekstowych, jak i obrazowych podpowiedzi
- Warianty małe do średnich (11B i 90B) - zapewniają elastyczne opcje wdrażania,
- Warianty tylko tekstowe (1B i 3B) - pozwalają na wdrożenie modelu na urządzeniach krawędziowych/mobilnych i zapewniają niską latencję

Wsparcie multimodalne stanowi duży krok w świecie modeli open source. Poniższy przykład kodu przyjmuje zarówno obraz, jak i podpowiedź tekstową, aby uzyskać analizę obrazu od Llama 3.2 90B.

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

Po ukończeniu tej lekcji, sprawdź naszą [Kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę na temat Generative AI!

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku ojczystym powinien być uznawany za autorytatywne źródło. W przypadku istotnych informacji zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.