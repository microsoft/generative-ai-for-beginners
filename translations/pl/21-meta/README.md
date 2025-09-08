<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:09:37+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "pl"
}
-->
# Budowanie z modelami rodziny Meta

## Wprowadzenie

W tej lekcji omówimy:

- Przegląd dwóch głównych modeli rodziny Meta – Llama 3.1 i Llama 3.2  
- Zrozumienie zastosowań i scenariuszy dla każdego modelu  
- Przykład kodu pokazujący unikalne cechy każdego modelu  

## Rodzina modeli Meta

W tej lekcji przyjrzymy się dwóm modelom z rodziny Meta, zwanej też „Llama Herd” – Llama 3.1 i Llama 3.2

Modele te występują w różnych wariantach i są dostępne na GitHub Model marketplace. Więcej informacji o korzystaniu z GitHub Models do [prototypowania z modelami AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Warianty modeli:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Uwaga: Llama 3 jest również dostępna na GitHub Models, ale nie będzie omawiana w tej lekcji*

## Llama 3.1

Z 405 miliardami parametrów, Llama 3.1 należy do kategorii otwartych modeli LLM.

Model ten jest ulepszeniem wcześniejszej wersji Llama 3, oferując:

- Większe okno kontekstu – 128k tokenów zamiast 8k tokenów  
- Większą maksymalną liczbę tokenów wyjściowych – 4096 zamiast 2048  
- Lepsze wsparcie wielojęzyczne – dzięki zwiększonej liczbie tokenów treningowych  

Dzięki temu Llama 3.1 radzi sobie z bardziej złożonymi zastosowaniami podczas tworzenia aplikacji GenAI, w tym:  
- Native Function Calling – możliwość wywoływania zewnętrznych narzędzi i funkcji poza przepływem pracy LLM  
- Lepsza wydajność RAG – dzięki większemu oknu kontekstu  
- Generowanie danych syntetycznych – możliwość tworzenia skutecznych danych do zadań takich jak fine-tuning  

### Native Function Calling

Llama 3.1 została dopracowana, aby skuteczniej wywoływać funkcje lub narzędzia. Model ma też dwa wbudowane narzędzia, które potrafi rozpoznać i użyć na podstawie zapytania użytkownika. Są to:

- **Brave Search** – może być używany do uzyskiwania aktualnych informacji, np. o pogodzie, poprzez wyszukiwanie w sieci  
- **Wolfram Alpha** – służy do bardziej złożonych obliczeń matematycznych, dzięki czemu nie trzeba pisać własnych funkcji  

Możesz także tworzyć własne niestandardowe narzędzia, które LLM może wywoływać.

W poniższym przykładzie kodu:

- Definiujemy dostępne narzędzia (brave_search, wolfram_alpha) w systemowym promptcie.  
- Wysyłamy zapytanie użytkownika dotyczące pogody w konkretnym mieście.  
- LLM odpowie wywołaniem narzędzia Brave Search, które będzie wyglądać tak: `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Uwaga: Ten przykład tylko wywołuje narzędzie, jeśli chcesz otrzymać wyniki, musisz założyć darmowe konto na stronie Brave API i zdefiniować samą funkcję*  

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

Mimo że jest to model LLM, Llama 3.1 ma ograniczenie w postaci braku multimodalności, czyli możliwości korzystania z różnych typów danych wejściowych, takich jak obrazy, oraz udzielania na nie odpowiedzi. Ta funkcja jest jedną z głównych cech Llama 3.2. Inne cechy to:

- Multimodalność – potrafi analizować zarówno tekst, jak i obrazy  
- Warianty o małej i średniej wielkości (11B i 90B) – zapewniają elastyczne opcje wdrożenia  
- Warianty tylko tekstowe (1B i 3B) – pozwalają na wdrożenie na urządzeniach brzegowych/mobilnych i oferują niskie opóźnienia  

Wsparcie multimodalne to duży krok naprzód w świecie otwartych modeli. Poniższy przykład kodu wykorzystuje zarówno obraz, jak i tekst, aby uzyskać analizę obrazu z Llama 3.2 90B.

### Wsparcie multimodalne w Llama 3.2

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

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.