<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:05:52+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "de"
}
-->
# Arbeiten mit den Meta Family Modellen

## Einführung

Diese Lektion behandelt:

- Die beiden Hauptmodelle der Meta-Familie kennenlernen – Llama 3.1 und Llama 3.2  
- Anwendungsfälle und Szenarien für jedes Modell verstehen  
- Codebeispiel, das die besonderen Funktionen jedes Modells zeigt  

## Die Meta-Familie der Modelle

In dieser Lektion betrachten wir 2 Modelle aus der Meta-Familie oder „Llama Herd“ – Llama 3.1 und Llama 3.2

Diese Modelle gibt es in verschiedenen Varianten und sie sind auf dem GitHub Model Marketplace verfügbar. Hier findest du weitere Informationen zur Nutzung von GitHub Models, um [Prototypen mit KI-Modellen zu erstellen](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Modellvarianten:  
- Llama 3.1 – 70B Instruct  
- Llama 3.1 – 405B Instruct  
- Llama 3.2 – 11B Vision Instruct  
- Llama 3.2 – 90B Vision Instruct  

*Hinweis: Llama 3 ist ebenfalls auf GitHub Models verfügbar, wird in dieser Lektion aber nicht behandelt*

## Llama 3.1

Mit 405 Milliarden Parametern gehört Llama 3.1 zur Kategorie der Open-Source-LLMs.

Das Modell ist ein Upgrade der früheren Version Llama 3 und bietet:

- Größeres Kontextfenster – 128k Tokens statt 8k Tokens  
- Größere maximale Ausgabelänge – 4096 statt 2048 Tokens  
- Bessere mehrsprachige Unterstützung – durch mehr Trainingsdaten  

Dadurch kann Llama 3.1 komplexere Anwendungsfälle bei der Entwicklung von GenAI-Anwendungen bewältigen, darunter:  
- Native Function Calling – die Möglichkeit, externe Tools und Funktionen außerhalb des LLM-Workflows aufzurufen  
- Verbesserte RAG-Leistung – dank des größeren Kontextfensters  
- Generierung synthetischer Daten – um effektive Daten für Aufgaben wie Fine-Tuning zu erstellen  

### Native Function Calling

Llama 3.1 wurde speziell darauf trainiert, Funktions- oder Tool-Aufrufe effektiver auszuführen. Es verfügt außerdem über zwei integrierte Tools, die das Modell je nach Nutzereingabe automatisch erkennt und verwendet. Diese Tools sind:

- **Brave Search** – kann verwendet werden, um aktuelle Informationen wie das Wetter durch eine Websuche abzurufen  
- **Wolfram Alpha** – eignet sich für komplexere mathematische Berechnungen, sodass eigene Funktionen nicht geschrieben werden müssen  

Du kannst auch eigene benutzerdefinierte Tools erstellen, die das LLM aufrufen kann.

Im folgenden Codebeispiel:

- Definieren wir die verfügbaren Tools (brave_search, wolfram_alpha) im System-Prompt.  
- Senden eine Nutzereingabe, die nach dem Wetter in einer bestimmten Stadt fragt.  
- Das LLM antwortet mit einem Tool-Aufruf an Brave Search, der so aussehen wird: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Hinweis: Dieses Beispiel führt nur den Tool-Aufruf aus. Wenn du die Ergebnisse erhalten möchtest, musst du ein kostenloses Konto auf der Brave API-Seite erstellen und die Funktion selbst definieren.*

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

Obwohl Llama 3.1 ein LLM ist, hat es eine Einschränkung: die fehlende Multimodalität. Das heißt, es kann keine verschiedenen Eingabetypen wie Bilder als Prompts verarbeiten und darauf antworten. Diese Fähigkeit ist eine der Hauptfunktionen von Llama 3.2. Weitere Merkmale sind:

- Multimodalität – kann sowohl Text- als auch Bild-Prompts auswerten  
- Kleine bis mittelgroße Varianten (11B und 90B) – bieten flexible Einsatzmöglichkeiten  
- Nur-Text-Varianten (1B und 3B) – ermöglichen den Einsatz auf Edge- oder Mobilgeräten mit geringer Latenz  

Die multimodale Unterstützung stellt einen großen Fortschritt im Bereich der Open-Source-Modelle dar. Das folgende Codebeispiel verwendet sowohl ein Bild als auch einen Text-Prompt, um eine Analyse des Bildes mit Llama 3.2 90B zu erhalten.

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

## Lernen hört hier nicht auf – setze deine Reise fort

Nach Abschluss dieser Lektion schau dir unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um dein Wissen über Generative AI weiter auszubauen!

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.