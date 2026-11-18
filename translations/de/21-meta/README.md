# Arbeiten mit den Meta-Familienmodellen 

## Einführung 

Diese Lektion behandelt: 

- Erforschung der beiden Hauptmodelle der Meta-Familie - Llama 3.1 und Llama 3.2 sowie der derzeit verfügbaren Alternativen, die in den Codebeispielen verwendet werden (Llama 3.3 und Llama 4) 
- Verständnis der Anwendungsfälle und Szenarien für jedes Modell 
- Codebeispiel zur Darstellung der einzigartigen Funktionen jedes Modells 


## Die Meta-Familie von Modellen 

In dieser Lektion werden wir 2 Modelle aus der Meta-Familie oder "Llama Herd" erkunden – Llama 3.1 und Llama 3.2. Die ausführbaren Codebeispiele verwenden Llama 3.3 und Llama 4, die derzeit verfügbare Alternativen im Microsoft Foundry Models-Katalog sind.

Diese Modelle gibt es in verschiedenen Varianten und sie sind im [Microsoft Foundry Models-Katalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) verfügbar.

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. Hier finden Sie weitere Informationen zur Verwendung von [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) zum Prototyping mit KI-Modellen.

> **Hinweis:** Die spezifischen Modellversionen, für die diese Lektion ursprünglich verfasst wurde (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct), wurden mittlerweile aus dem Microsoft Foundry Models-Katalog zurückgezogen. Die unten stehenden Codebeispiele verwenden `Llama-3.3-70B-Instruct` und `Llama-4-Scout-17B-16E-Instruct` als aktuell verfügbare Alternativen im Microsoft Foundry Models-Katalog, sodass sie weiterhin ausführbar sind.

Modellvarianten (wie ursprünglich in dieser Lektion behandelt): 
- Llama 3.1 - 70B Instruct (ausgemustert) 
- Llama 3.1 - 405B Instruct (ausgemustert) 
- Llama 3.2 - 11B Vision Instruct (ausgemustert) 
- Llama 3.2 - 90B Vision Instruct (ausgemustert) 

Derzeit verfügbare Alternativen, die in den Codebeispielen verwendet werden: 
- Llama 3.3 - 70B Anweisung (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Anweisung (`Llama-4-Scout-17B-16E-Instruct`) 

*Hinweis: Die oben erwähnten Llama 3 Varianten werden aus historischen Gründen beibehalten und sind in den Microsoft Foundry Models nicht mehr verfügbar.*

## Llama 3.1 

Mit 405 Milliarden Parametern gehört Llama 3.1 zur Kategorie der Open-Source-LLMs. 

Das Modell ist eine Weiterentwicklung der früheren Version Llama 3 und bietet: 

- Größeres Kontextfenster – 128k Tokens vs. 8k Tokens 
- Größere maximale Ausgabetokenanzahl – 4096 vs. 2048 
- Bessere Mehrsprachigkeit – durch erhöhte Anzahl an Trainings-Tokens 

Diese Verbesserungen ermöglichen es Llama 3.1, komplexere Anwendungsfälle bei der Entwicklung von GenAI-Anwendungen zu bewältigen, darunter: 
- Native Funktionsaufrufe – die Fähigkeit, externe Werkzeuge und Funktionen außerhalb des LLM-Workflows aufzurufen 
- Bessere RAG-Leistung – durch das größere Kontextfenster 
- Synthetische Datenerzeugung – die Fähigkeit, effektive Daten für Aufgaben wie Feintuning zu erzeugen 

### Native Funktionsaufrufe 

Llama 3.1 wurde darauf feinjustiert, Funktions- oder Werkzeugaufrufe effektiver zu machen. Es verfügt außerdem über zwei integrierte Werkzeuge, die das Modell aufgrund des Benutzerprompts als nötig erkennen kann. Diese Werkzeuge sind: 

- **Brave Search** – Kann verwendet werden, um aktuelle Informationen wie Wetterdaten durch eine Websuche zu erhalten 
- **Wolfram Alpha** – Kann für komplexere mathematische Berechnungen genutzt werden, sodass das Schreiben eigener Funktionen nicht notwendig ist. 

Sie können auch Ihre eigenen benutzerdefinierten Werkzeuge erstellen, die das LLM aufrufen kann. 

Im folgenden Codebeispiel: 

- Definieren wir die verfügbaren Werkzeuge (brave_search, wolfram_alpha) im Systemprompt. 
- Senden eine Benutzeranfrage, die nach dem Wetter in einer bestimmten Stadt fragt. 
- Das LLM wird mit einem Werkzeugaufruf an das Brave Search Tool antworten, der so aussehen wird `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Hinweis: Dieses Beispiel führt nur den Werkzeugaufruf aus. Wenn Sie die Ergebnisse erhalten möchten, müssen Sie ein kostenloses Konto auf der Brave API-Seite anlegen und die Funktion selbst definieren.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Trotz der Zugehörigkeit zu den LLMs hat Llama 3.1 eine Einschränkung: die fehlende Multimodalität. Also die Unfähigkeit, verschiedene Eingabearten wie Bilder als Prompts zu verwenden und darauf zu reagieren. Diese Fähigkeit ist eine der Hauptmerkmale von Llama 3.2. Zu den Features gehören außerdem: 

- Multimodalität – Fähigkeit, sowohl Text- als auch Bildprompts zu verarbeiten 
- Kleine bis mittelgroße Varianten (11B und 90B) – bietet flexible Bereitstellungsoptionen 
- Nur-Text-Varianten (1B und 3B) – ermöglichen die Bereitstellung auf Edge-/Mobilgeräten mit niedriger Latenz 

Die multimodale Unterstützung stellt einen großen Schritt in der Welt der Open-Source-Modelle dar. Das untenstehende Codebeispiel nimmt sowohl ein Bild als auch einen Text-Prompt, um eine Analyse des Bildes zu erhalten. Da Llama 3.2 90B Vision Instruct eingestellt wurde, verwendet das Beispiel `Llama-4-Scout-17B-16E-Instruct`, eine derzeit verfügbare nativ multimodale Alternative. 


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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Das Lernen endet hier nicht, setzen Sie die Reise fort

Nach Abschluss dieser Lektion schauen Sie sich unsere [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um Ihr Wissen über Generative KI weiter auszubauen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->