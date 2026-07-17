[![Open Source Models](../../../translated_images/de/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Einführung

KI-Agenten stellen eine aufregende Entwicklung im Bereich der Generativen KI dar, die es großen Sprachmodellen (LLMs) ermöglicht, sich von Assistenten zu Agenten zu entwickeln, die in der Lage sind, Aktionen auszuführen. KI-Agenten-Frameworks ermöglichen Entwicklern die Erstellung von Anwendungen, die LLMs Zugang zu Werkzeugen und Zustandsverwaltung geben. Diese Frameworks verbessern auch die Sichtbarkeit, sodass Benutzer und Entwickler die von LLMs geplanten Aktionen überwachen können, was das Erlebnismanagement verbessert.

Die Lektion behandelt folgende Bereiche:

- Verständnis, was ein KI-Agent ist – Was genau ist ein KI-Agent?
- Erforschung von fünf verschiedenen KI-Agenten-Frameworks – Was macht sie einzigartig?
- Anwendung dieser KI-Agenten auf verschiedene Anwendungsfälle – Wann sollten wir KI-Agenten verwenden?

## Lernziele

Nach Abschluss dieser Lektion wirst du in der Lage sein:

- Erklären, was KI-Agenten sind und wie sie verwendet werden können.
- Ein Verständnis der Unterschiede zwischen einigen der populären KI-Agenten-Frameworks zu haben und wie sie sich unterscheiden.
- Zu verstehen, wie KI-Agenten funktionieren, um Anwendungen mit ihnen zu bauen.

## Was sind KI-Agenten?

KI-Agenten sind ein sehr spannendes Feld in der Welt der Generativen KI. Diese Aufregung geht manchmal mit einer Verwirrung über Begriffe und deren Anwendung einher. Um es einfach zu halten und die meisten Werkzeuge einzubeziehen, die sich auf KI-Agenten beziehen, verwenden wir die folgende Definition:

KI-Agenten ermöglichen es großen Sprachmodellen (LLMs), Aufgaben auszuführen, indem sie ihnen Zugang zu einem **Zustand** und **Werkzeugen** geben.

![Agenten-Modell](../../../translated_images/de/what-agent.21f2893bdfd01e6a.webp)

Lassen Sie uns diese Begriffe definieren:

**Große Sprachmodelle** – Dies sind die Modelle, die im gesamten Kurs erwähnt werden, wie GPT-5, GPT-4o und Llama 3.3 usw.

**Zustand** – Dies bezieht sich auf den Kontext, in dem das LLM arbeitet. Das LLM nutzt den Kontext seiner vergangenen Aktionen und den aktuellen Kontext, um seine Entscheidungsfindung für nachfolgende Aktionen zu leiten. KI-Agenten-Frameworks erleichtern Entwicklern die Verwaltung dieses Kontexts.

**Werkzeuge** – Um die Aufgabe zu erfüllen, die der Benutzer angefordert hat und die das LLM geplant hat, benötigt das LLM Zugriff auf Werkzeuge. Einige Beispiele für Werkzeuge können eine Datenbank, eine API, eine externe Anwendung oder sogar ein anderes LLM sein!

Diese Definitionen sollen dir hoffentlich eine gute Grundlage geben, während wir uns ansehen, wie sie implementiert werden. Lass uns einige verschiedene KI-Agenten-Frameworks erkunden:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ist eine Umsetzung der oben gegebenen Definitionen.

Zur Verwaltung des **Zustands** verwendet es eine eingebaute Funktion namens `AgentExecutor`. Diese akzeptiert den definierten `agent` und die `tools`, die ihm zur Verfügung stehen.

Der `AgentExecutor` speichert auch die Chat-Historie, um den Kontext des Chats bereitzustellen.

![LangChain Agents](../../../translated_images/de/langchain-agents.edcc55b5d5c43716.webp)

LangChain bietet einen [Werkzeugkatalog](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), der in deine Anwendung importiert werden kann und auf den das LLM zugreifen kann. Diese werden von der Community und dem LangChain-Team erstellt.

Du kannst diese Werkzeuge dann definieren und an den `AgentExecutor` übergeben.

Sichtbarkeit ist ein weiterer wichtiger Aspekt, wenn es um KI-Agenten geht. Es ist wichtig für Anwendungsentwickler zu verstehen, welches Werkzeug das LLM verwendet und warum. Dafür hat das Team von LangChain LangSmith entwickelt.

## AutoGen

Das nächste KI-Agenten-Framework, das wir besprechen, ist [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Der Hauptfokus von AutoGen liegt auf Konversationen. Agenten sind sowohl **sprechbar** als auch **anpassbar**.

**Sprechbar –** LLMs können eine Konversation mit einem anderen LLM beginnen und fortsetzen, um eine Aufgabe zu erledigen. Dies geschieht durch die Erstellung von `AssistantAgents` und die Vergabe einer bestimmten Systemnachricht.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Anpassbar** – Agenten können nicht nur als LLM definiert werden, sondern auch als Benutzer oder Werkzeug. Als Entwickler kannst du einen `UserProxyAgent` definieren, der dafür verantwortlich ist, mit dem Benutzer wegen Feedback zur Erfüllung einer Aufgabe zu interagieren. Dieses Feedback kann entweder die Ausführung der Aufgabe fortsetzen oder stoppen.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Zustand und Werkzeuge

Um den Zustand zu ändern und zu verwalten, generiert ein Assistenzagent Python-Code, um die Aufgabe zu erfüllen.

Hier ist ein Beispiel für den Ablauf:

![AutoGen](../../../translated_images/de/autogen.dee9a25a45fde584.webp)

#### LLM definiert mit einer Systemnachricht

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Diese Systemnachricht weist dieses spezifische LLM an, welche Funktionen für seine Aufgabe relevant sind. Denk daran, mit AutoGen kannst du mehrere definierte AssistantAgents mit unterschiedlichen Systemnachrichten haben.

#### Chat wird vom Benutzer gestartet

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Diese Nachricht vom user_proxy (Mensch) startet den Prozess des Agenten, die möglichen Funktionen zu erkunden, die er ausführen sollte.

#### Funktion wird ausgeführt

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Sobald der anfängliche Chat verarbeitet ist, wird der Agent das vorgeschlagene Werkzeug aufrufen. In diesem Fall ist das eine Funktion namens `get_weather`. Je nach Konfiguration kann diese Funktion automatisch vom Agenten ausgeführt und gelesen werden oder basierend auf Benutzereingabe ausgeführt werden.

Du findest eine Liste von [AutoGen Code-Beispielen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), um weiter zu erkunden, wie man baut.

## Microsoft Agent Framework

Das [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) ist das Open-Source-SDK von Microsoft zum Erstellen von KI-Agenten und Multi-Agenten-Systemen sowohl in **Python** als auch in **.NET**. Es vereint die Stärken zweier früherer Microsoft-Projekte – die Unternehmensfunktionen von **Semantic Kernel** und die Multi-Agent-Orchestrierung von **AutoGen** – in einem einzigen, unterstützten Framework. Wenn du heute ein neues Agentenprojekt startest, ist dies der empfohlene Nachfolger von AutoGen.

Das Framework skaliert von einem einzelnen **Chat-Agenten** bis hin zu komplexen **Multi-Agenten-Workflows** und integriert sich direkt mit Microsoft Foundry, Azure OpenAI und OpenAI. Es bietet auch eingebaute Beobachtbarkeit durch OpenTelemetry, sodass du genau nachverfolgen kannst, was deine Agenten tun.

### Zustand und Werkzeuge

**Zustand** – Das Framework verwaltet den Gesprächskontext für dich durch **Threads**. Ein Agent verfolgt die Nachrichtenhistorie (Benutzeranfragen, Werkzeugaufrufe und deren Ergebnisse), sodass jeder Schritt auf den vorherigen aufbaut. Threads können auch persistiert werden, was erlaubt, ein Gespräch zu pausieren und später fortzusetzen.

**Werkzeuge** – Du gibst einem Agenten Werkzeuge, indem du einfache Python-Funktionen übergibst. Typannotierte Parameter werden automatisch in ein Schema umgewandelt, sodass das Modell weiß, wie und wann es diese aufrufen soll (Function Calling). Das Framework unterstützt auch Model Context Protocol (MCP) Server und gehostete Werkzeuge wie einen Code-Interpreter.

Hier ein Beispiel für einen einzelnen Agenten mit einem kundenspezifischen Werkzeug:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Um stattdessen eine Verbindung zu Azure OpenAI in Microsoft Foundry herzustellen, übergib einfach deinen Endpunkt und die Anmeldedaten an den Client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-Agenten-Workflows

Wo das Framework wirklich heraussticht, ist die Orchestrierung mehrerer Agenten zusammen. Zum Beispiel kannst du Agenten nacheinander ausführen (jeder übergibt seinen Kontext an den nächsten) oder parallel mehrere Agenten starten und deren Ergebnisse zusammenführen:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Führen Sie Agenten nacheinander aus und übergeben Sie den Gesprächskontext entlang der Kette
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Fächern Sie zu Agenten parallel auf und aggregieren Sie dann ihre Antworten
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Um das Framework zu installieren und loszulegen:

```bash
pip install agent-framework-core
# Optionale Integrationen
pip install agent-framework-openai       # OpenAI und Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Du kannst mehr im [Microsoft Agent Framework Repository](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) und in der [offiziellen Dokumentation](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) erkunden.

## Taskweaver

Das nächste Agenten-Framework, das wir erkunden, ist [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Es wird als "code-first"-Agent bezeichnet, weil es statt strikt mit `Strings` zu arbeiten, mit DataFrames in Python arbeiten kann. Das ist äußerst nützlich für Datenanalyse- und Generierungsaufgaben. Dies können Dinge wie das Erstellen von Grafiken und Diagrammen oder das Erzeugen von Zufallszahlen sein.

### Zustand und Werkzeuge

Um den Zustand des Gesprächs zu verwalten, verwendet TaskWeaver das Konzept eines `Planner`. Der `Planner` ist ein LLM, das die Anfrage der Benutzer entgegennimmt und die Aufgaben abbildet, die zur Erfüllung der Anfrage erledigt werden müssen.

Zur Erledigung der Aufgaben wird der `Planner` der Sammlung von Werkzeugen namens `Plugins` ausgesetzt. Dies können Python-Klassen oder ein allgemeiner Code-Interpreter sein. Diese Plugins werden als Einbettungen gespeichert, damit das LLM besser das richtige Plugin suchen kann.

![Taskweaver](../../../translated_images/de/taskweaver.da8559999267715a.webp)

Hier ein Beispiel für ein Plugin zur Behandlung der Anomalieerkennung:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Der Code wird vor der Ausführung überprüft. Eine weitere Funktion zur Kontextverwaltung in TaskWeaver ist `Experience`. Experience ermöglicht es, den Kontext eines Gesprächs langfristig in einer YAML-Datei zu speichern. Dies kann so konfiguriert werden, dass das LLM im Laufe der Zeit bei bestimmten Aufgaben besser wird, da es vorherige Gespräche berücksichtigt.

## JARVIS

Das letzte Agenten-Framework, das wir erkunden, ist [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Was JARVIS einzigartig macht, ist, dass es ein LLM verwendet, um den `Zustand` des Gesprächs zu verwalten, und die `Werkzeuge` sind andere KI-Modelle. Jedes der KI-Modelle ist ein spezialisiertes Modell, das bestimmte Aufgaben wie Objekterkennung, Transkription oder Bildunterschriften übernimmt.

![JARVIS](../../../translated_images/de/jarvis.762ddbadbd1a3a33.webp)

Das LLM, als allgemein einsetzbares Modell, erhält die Anfrage des Benutzers und identifiziert die spezifische Aufgabe und alle Argumente/Daten, die zur Erfüllung der Aufgabe benötigt werden.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Das LLM formatiert dann die Anfrage so, dass das spezialisierte KI-Modell sie interpretieren kann, z.B. als JSON. Sobald das KI-Modell seine Vorhersage basierend auf der Aufgabe zurückgegeben hat, erhält das LLM die Antwort.

Wenn mehrere Modelle zur Erfüllung der Aufgabe benötigt werden, interpretiert es auch die Antworten dieser Modelle, bevor es sie zusammenführt, um die Antwort an den Benutzer zu generieren.

Das folgende Beispiel zeigt, wie dies funktioniert, wenn ein Benutzer eine Beschreibung und Zählung der Objekte auf einem Bild anfordert:

## Aufgabe

Um dein Lernen über KI-Agenten fortzusetzen, kannst du mit dem Microsoft Agent Framework Folgendes erstellen:

- Eine Anwendung, die ein Geschäftstreffen mit verschiedenen Abteilungen eines Bildungs-Startups simuliert.
- Erstelle Systemnachrichten, die LLMs dabei helfen, unterschiedliche Personas und Prioritäten zu verstehen, und ermögliche dem Benutzer, eine neue Produktidee zu präsentieren.
- Das LLM soll dann Folgefragen aus jeder Abteilung generieren, um die Präsentation und Produktidee zu verfeinern und zu verbessern.

## Lernen hört hier nicht auf, setze die Reise fort

Nach Abschluss dieser Lektion schau dir unsere [Generative AI Learning Sammlung](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) an, um dein Wissen in Generativer KI weiter auszubauen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->