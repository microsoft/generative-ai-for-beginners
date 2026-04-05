# Arbeiten mit den Meta-Familienmodellen

## Einführung

Diese Lektion behandelt:

- Erkundung der beiden Hauptmodelle der Meta-Familie – Llama 3.1 und Llama 3.2
- Verständnis der Anwendungsfälle und Szenarien für jedes Modell
- Codebeispiel zur Darstellung der einzigartigen Funktionen jedes Modells

## Die Meta-Familie der Modelle

In dieser Lektion werden wir 2 Modelle aus der Meta-Familie oder „Llama-Herde“ erkunden – Llama 3.1 und Llama 3.2.

Diese Modelle sind in verschiedenen Varianten verfügbar und finden sich im GitHub Model-Marktplatz. Hier sind weitere Details zur Verwendung von GitHub Models zum [Prototyping mit KI-Modellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianten:
- Llama 3.1 – 70B Instruct
- Llama 3.1 – 405B Instruct
- Llama 3.2 – 11B Vision Instruct
- Llama 3.2 – 90B Vision Instruct

*Hinweis: Llama 3 ist ebenfalls auf GitHub Models verfügbar, wird aber in dieser Lektion nicht behandelt.*

## Llama 3.1

Mit 405 Milliarden Parametern gehört Llama 3.1 zur Kategorie der Open-Source-LLMs.

Das Modell ist ein Upgrade des früheren Releases Llama 3 und bietet:

- Größeres Kontextfenster – 128k Tokens statt 8k Tokens
- Größere maximale Ausgabelänge – 4096 statt 2048 Tokens
- Bessere Mehrsprachigkeitsunterstützung – aufgrund der erhöhten Trainings-Tokens

Diese Verbesserungen ermöglichen Llama 3.1 die Bewältigung komplexerer Anwendungsfälle beim Erstellen von GenAI-Anwendungen, einschließlich:
- Native Funktionsaufrufe – die Fähigkeit, externe Werkzeuge und Funktionen außerhalb des LLM-Workflows aufzurufen
- Bessere RAG-Leistung – durch das größere Kontextfenster
- Generierung synthetischer Daten – die Fähigkeit, effektive Daten für Aufgaben wie Feintuning zu erstellen

### Native Funktionsaufrufe

Llama 3.1 wurde darauf feinjustiert, Funktionen oder Werkzeugaufrufe effektiver auszuführen. Es verfügt außerdem über zwei integrierte Werkzeuge, die das Modell als notwendig erkennen kann, basierend auf dem Nutzerprompt. Diese Werkzeuge sind:

- **Brave Search** – Kann verwendet werden, um aktuelle Informationen wie Wetterdaten durch Websuchen abzurufen
- **Wolfram Alpha** – Kann für komplexere mathematische Berechnungen verwendet werden, so dass das Schreiben eigener Funktionen nicht notwendig ist.

Sie können auch eigene benutzerdefinierte Werkzeuge erstellen, die das LLM aufrufen kann.

Im folgenden Codebeispiel:

- Definieren wir die verfügbaren Werkzeuge (brave_search, wolfram_alpha) im Systemprompt.
- Senden einen Nutzerprompt, der nach dem Wetter in einer bestimmten Stadt fragt.
- Das LLM antwortet mit einem Werkzeugaufruf an das Brave Search Werkzeug, der so aussehen wird `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Hinweis: Dieses Beispiel führt nur den Werkzeugaufruf aus. Wenn Sie die Ergebnisse erhalten möchten, müssen Sie ein kostenloses Konto auf der Brave API-Seite erstellen und die Funktion selbst definieren.*

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

Obwohl Llama 3.1 ein LLM ist, besteht eine Einschränkung in seiner fehlenden Multimodalität. Das heißt, es kann keine verschiedenen Eingabetypen wie Bilder als Prompt verwenden und darauf antworten. Diese Fähigkeit ist eine der Hauptmerkmale von Llama 3.2. Diese Features umfassen auch:

- Multimodalität – die Fähigkeit, sowohl Text- als auch Bild-Prompts zu bewerten
- Kleine bis mittlere Varianten (11B und 90B) – bieten flexible Bereitstellungsoptionen
- Nur-Text-Varianten (1B und 3B) – erlauben die Bereitstellung auf Edge- oder Mobilgeräten bei niedriger Latenz

Die Unterstützung multimodaler Eingaben stellt einen großen Fortschritt in der Welt der Open-Source-Modelle dar. Das folgende Codebeispiel verwendet sowohl ein Bild als auch einen Text-Prompt, um eine Analyse des Bildes von Llama 3.2 90B zu erhalten.

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

## Lernen hört hier nicht auf, setze die Reise fort

Nach Abschluss dieser Lektion sehen Sie sich unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter zu vertiefen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, können automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->