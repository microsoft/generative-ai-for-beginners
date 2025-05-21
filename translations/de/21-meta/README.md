<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:05:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "de"
}
-->
# Aufbau mit den Meta-Familienmodellen

## Einführung

Diese Lektion behandelt:

- Die beiden Hauptmodelle der Meta-Familie - Llama 3.1 und Llama 3.2 - erkunden
- Die Anwendungsfälle und Szenarien für jedes Modell verstehen
- Codebeispiele, um die einzigartigen Funktionen jedes Modells zu zeigen

## Die Meta-Familie der Modelle

In dieser Lektion werden wir 2 Modelle aus der Meta-Familie oder "Llama-Herde" erkunden - Llama 3.1 und Llama 3.2

Diese Modelle gibt es in verschiedenen Varianten und sind auf dem GitHub Model-Marktplatz verfügbar. Hier finden Sie weitere Details zur Verwendung von GitHub Models zum [Prototyping mit KI-Modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianten:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Hinweis: Llama 3 ist ebenfalls auf GitHub Models verfügbar, wird jedoch in dieser Lektion nicht behandelt*

## Llama 3.1

Mit 405 Milliarden Parametern gehört Llama 3.1 zur Kategorie der Open-Source-LLM.

Das Modell ist ein Upgrade zur früheren Veröffentlichung Llama 3 und bietet:

- Größeres Kontextfenster - 128k Tokens vs. 8k Tokens
- Größere maximale Ausgabe-Tokens - 4096 vs. 2048
- Bessere mehrsprachige Unterstützung - aufgrund der Erhöhung der Trainings-Tokens

Dies ermöglicht es Llama 3.1, komplexere Anwendungsfälle beim Aufbau von GenAI-Anwendungen zu bewältigen, einschließlich:
- Native Funktionsaufrufe - die Fähigkeit, externe Tools und Funktionen außerhalb des LLM-Workflows aufzurufen
- Bessere RAG-Leistung - aufgrund des größeren Kontextfensters
- Generierung synthetischer Daten - die Fähigkeit, effektive Daten für Aufgaben wie das Fein-Tuning zu erstellen

### Native Funktionsaufrufe

Llama 3.1 wurde so optimiert, dass es effektiver bei der Ausführung von Funktions- oder Toolaufrufen ist. Es verfügt auch über zwei integrierte Tools, die das Modell als notwendig erkennen kann, basierend auf der Eingabeaufforderung des Benutzers. Diese Tools sind:

- **Brave Search** - Kann verwendet werden, um aktuelle Informationen wie das Wetter durch eine Websuche zu erhalten
- **Wolfram Alpha** - Kann für komplexere mathematische Berechnungen verwendet werden, sodass das Schreiben eigener Funktionen nicht erforderlich ist.

Sie können auch Ihre eigenen benutzerdefinierten Tools erstellen, die das LLM aufrufen kann.

Im folgenden Codebeispiel:

- Wir definieren die verfügbaren Tools (brave_search, wolfram_alpha) in der Systemaufforderung.
- Senden Sie eine Benutzeraufforderung, die nach dem Wetter in einer bestimmten Stadt fragt.
- Das LLM wird mit einem Toolaufruf an das Brave Search-Tool antworten, der wie folgt aussieht: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Hinweis: Dieses Beispiel macht nur den Toolaufruf. Wenn Sie die Ergebnisse erhalten möchten, müssen Sie ein kostenloses Konto auf der Brave API-Seite erstellen und die Funktion selbst definieren.*

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

Trotz der Tatsache, dass es ein LLM ist, hat Llama 3.1 eine Einschränkung bei der Multimodalität. Das bedeutet, dass es in der Lage ist, verschiedene Arten von Eingaben wie Bilder als Aufforderungen zu verwenden und Antworten zu geben. Diese Fähigkeit ist eines der Hauptmerkmale von Llama 3.2. Diese Funktionen umfassen auch:

- Multimodalität - hat die Fähigkeit, sowohl Text- als auch Bildaufforderungen zu bewerten
- Kleine bis mittlere Größenvariationen (11B und 90B) - dies bietet flexible Bereitstellungsoptionen,
- Nur Text-Variationen (1B und 3B) - dies ermöglicht es dem Modell, auf Edge-/Mobilgeräten bereitgestellt zu werden und bietet niedrige Latenz

Die Unterstützung für Multimodalität stellt einen großen Schritt in der Welt der Open-Source-Modelle dar. Das folgende Codebeispiel nimmt sowohl eine Bild- als auch eine Textaufforderung, um eine Analyse des Bildes von Llama 3.2 90B zu erhalten.

### Multimodale Unterstützung mit Llama 3.2

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

## Lernen hört hier nicht auf, setzen Sie die Reise fort

Nachdem Sie diese Lektion abgeschlossen haben, sehen Sie sich unsere [Generative AI Learning Collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative AI weiter zu vertiefen!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.