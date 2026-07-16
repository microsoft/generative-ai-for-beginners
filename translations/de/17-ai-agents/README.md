[![Open Source Modelle](../../../translated_images/de/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Einführung

KI-Agenten stellen eine spannende Entwicklung im Bereich der Generativen KI dar, die es großen Sprachmodellen (LLMs) ermöglicht, sich von Assistenten zu Agenten zu entwickeln, die in der Lage sind, Aktionen durchzuführen. KI-Agenten-Frameworks ermöglichen Entwicklern, Anwendungen zu erstellen, die LLMs Zugriff auf Werkzeuge und Zustandsverwaltung geben. Diese Frameworks verbessern auch die Sichtbarkeit, sodass Benutzer und Entwickler die von LLMs geplanten Aktionen überwachen können, wodurch das Erfahrungshandling verbessert wird.

Die Lektion behandelt folgende Bereiche:

- Verstehen, was ein KI-Agent ist – Was genau ist ein KI-Agent?
- Untersuchung von fünf verschiedenen KI-Agenten-Frameworks – Was macht sie einzigartig?
- Anwendung dieser KI-Agenten auf verschiedene Anwendungsfälle – Wann sollten wir KI-Agenten einsetzen?

## Lernziele

Nach dieser Lektion wirst du in der Lage sein:

- Erklären, was KI-Agenten sind und wie sie verwendet werden können.
- Ein Verständnis der Unterschiede zwischen einigen der beliebten KI-Agenten-Frameworks zu haben und wie sie sich unterscheiden.
- Verstehen, wie KI-Agenten funktionieren, um Anwendungen mit ihnen zu bauen.

## Was sind KI-Agenten?

KI-Agenten sind ein sehr spannendes Feld in der Welt der Generativen KI. Mit dieser Aufregung kommt manchmal auch eine Verwirrung über Begriffe und deren Anwendung. Um die Dinge einfach und inklusive der meisten Tools zu halten, die sich auf KI-Agenten beziehen, verwenden wir folgende Definition:

KI-Agenten ermöglichen es großen Sprachmodellen (LLMs), Aufgaben zu erfüllen, indem sie ihnen Zugriff auf einen **Zustand** und **Werkzeuge** geben.

![Agentenmodell](../../../translated_images/de/what-agent.21f2893bdfd01e6a.webp)

Lassen Sie uns diese Begriffe definieren:

**Große Sprachmodelle** – Das sind die Modelle, die im gesamten Kurs verwendet werden, wie GPT-3.5, GPT-4, Llama-2 usw.

**Zustand** – Dies bezieht sich auf den Kontext, in dem das LLM arbeitet. Das LLM nutzt den Kontext seiner vergangenen Aktionen und den aktuellen Kontext, um seine Entscheidungsfindung für nachfolgende Aktionen zu steuern. KI-Agenten-Frameworks ermöglichen Entwicklern, diesen Kontext einfacher zu verwalten.

**Werkzeuge** – Um die Aufgabe zu erfüllen, die der Nutzer angefordert hat und die das LLM geplant hat, benötigt das LLM Zugriff auf Werkzeuge. Beispiele für Werkzeuge können eine Datenbank, eine API, eine externe Anwendung oder sogar ein weiteres LLM sein!

Diese Definitionen sollen dir eine gute Grundlage geben, wenn wir uns ansehen, wie sie implementiert werden. Schauen wir uns einige verschiedene KI-Agenten-Frameworks an:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ist eine Umsetzung der oben gegebenen Definitionen.

Um den **Zustand** zu verwalten, verwendet es eine eingebaute Funktion namens `AgentExecutor`. Diese nimmt den definierten `Agent` und die verfügbaren `Werkzeuge` an.

Der `Agent Executor` speichert auch den Chatverlauf, um den Kontext des Chats bereitzustellen.

![Langchain Agents](../../../translated_images/de/langchain-agents.edcc55b5d5c43716.webp)

LangChain bietet einen [Werkzeugkatalog](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), der in deine Anwendung importiert werden kann, zu dem das LLM Zugriff hat. Diese werden von der Community und dem LangChain-Team erstellt.

Du kannst diese Werkzeuge definieren und an den `Agent Executor` übergeben.

Sichtbarkeit ist ein weiterer wichtiger Aspekt, wenn man über KI-Agenten spricht. Es ist wichtig für Anwendungsentwickler zu verstehen, welches Werkzeug das LLM verwendet und warum. Dafür hat das Team von LangChain LangSmith entwickelt.

## AutoGen

Das nächste KI-Agenten-Framework, das wir besprechen werden, ist [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Der Hauptfokus von AutoGen liegt auf Gesprächen. Agenten sind sowohl **gesprächsfähig** als auch **anpassbar**.

**Gesprächsfähig –** LLMs können eine Unterhaltung mit einem anderen LLM beginnen und fortführen, um eine Aufgabe zu erfüllen. Dies geschieht durch das Erstellen von `AssistantAgents` und die Vergabe einer spezifischen Systemnachricht.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Anpassbar** – Agenten können nicht nur als LLMs definiert werden, sondern auch als Benutzer oder Werkzeug. Als Entwickler kannst du einen `UserProxyAgent` definieren, der für die Interaktion mit dem Benutzer zur Rückmeldung bei der Erfüllung einer Aufgabe verantwortlich ist. Dieses Feedback kann die Ausführung der Aufgabe fortsetzen oder stoppen.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Zustand und Werkzeuge

Um den Zustand zu ändern und zu verwalten, generiert ein Assistent-Agent Python-Code, um die Aufgabe zu erledigen.

Hier ein Beispiel des Ablaufs:

![AutoGen](../../../translated_images/de/autogen.dee9a25a45fde584.webp)

#### LLM mit Systemnachricht definiert

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Diese Systemnachricht weist das spezifische LLM an, welche Funktionen für seine Aufgabe relevant sind. Denke daran, mit AutoGen kannst du mehrere definierte AssistantAgents mit unterschiedlichen Systemnachrichten haben.

#### Chat wird vom Nutzer initiiert

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

Sobald der erste Chat verarbeitet ist, sendet der Agent das vorgeschlagene Werkzeug zum Aufruf. In diesem Fall ist es eine Funktion namens `get_weather`. Je nach Konfiguration kann diese Funktion automatisch vom Agenten ausgeführt und gelesen werden oder basierend auf Nutzereingaben.

Du findest eine Liste von [AutoGen Code-Beispielen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), um weiter zu erforschen, wie man mit dem Aufbau startet.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) ist Microsofts Open-Source-SDK für den Bau von KI-Agenten und Multi-Agenten-Systemen in **Python** und **.NET**. Es vereint die Stärken von zwei früheren Microsoft-Projekten – die Unternehmensfunktionen des **Semantic Kernel** und die Multi-Agenten-Orchestrierung von **AutoGen** – in einem einzigen, unterstützten Framework. Wenn du heute ein neues Agentenprojekt startest, ist dies der empfohlene Nachfolger von AutoGen.

Das Framework skaliert von einem einzelnen **Chat-Agenten** bis hin zu komplexen **Multi-Agenten-Workflows** und integriert sich direkt mit Microsoft Foundry, Azure OpenAI und OpenAI. Es bietet auch eingebaute Beobachtbarkeit durch OpenTelemetry, sodass du genau verfolgen kannst, was deine Agenten tun.

### Zustand und Werkzeuge

**Zustand** – Das Framework verwaltet den Gesprächskontext für dich durch **Threads**. Ein Agent verfolgt die Nachrichtenhistorie (Benutzernachrichten, Werkzeugaufrufe und deren Ergebnisse), sodass jeder Schritt auf den vorherigen aufbaut. Threads können auch gespeichert werden, sodass ein Gespräch pausiert und später fortgesetzt werden kann.

**Werkzeuge** – Du gibst einem Agenten Werkzeuge, indem du einfache Python-Funktionen übergibst. Typannotierte Parameter werden automatisch in ein Schema umgewandelt, damit das Modell weiß, wie und wann es sie aufrufen soll (Funktionsaufruf). Das Framework unterstützt außerdem Model Context Protocol (MCP)-Server und gehostete Werkzeuge wie einen Code-Interpreter.

Hier ein Beispiel für einen einzelnen Agenten mit einem benutzerdefinierten Werkzeug:

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

Um stattdessen eine Verbindung zu Azure OpenAI in Microsoft Foundry herzustellen, übergibt man dem Client den Endpunkt und die Anmeldeinformationen:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Multi-Agenten-Workflows

Wo das Framework wirklich herausragt, ist die Orchestrierung mehrerer Agenten zusammen. Zum Beispiel kannst du Agenten nacheinander ausführen lassen (jeder gibt seinen Kontext an den nächsten weiter) oder in mehrere Agenten parallel aufteilen und deren Ergebnisse zusammenführen:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Führen Sie Agenten nacheinander aus und übergeben Sie den Gesprächskontext entlang der Kette
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Verzweigen Sie parallel zu Agenten und fassen Sie dann deren Antworten zusammen
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

Das nächste Agenten-Framework, das wir erkunden werden, ist [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Es ist bekannt als ein "Code-first"-Agent, weil er statt strikt mit `strings` mit DataFrames in Python arbeiten kann. Das wird besonders nützlich für Datenanalyse- und Generierungsaufgaben. Das können Dinge sein wie das Erstellen von Grafiken und Diagrammen oder das Generieren von Zufallszahlen.

### Zustand und Werkzeuge

Um den Zustand des Gesprächs zu verwalten, verwendet TaskWeaver das Konzept eines `Planners`. Der `Planner` ist ein LLM, das die Anfragen der Nutzer entgegennimmt und die Aufgaben plant, die erledigt werden müssen, um diese Anfrage zu erfüllen.

Zur Erledigung der Aufgaben hat der `Planner` Zugriff auf eine Sammlung von Werkzeugen, genannt `Plugins`. Das können Python-Klassen oder ein allgemeiner Code-Interpreter sein. Diese Plugins werden als Embeddings gespeichert, damit das LLM besser nach dem richtigen Plugin suchen kann.

![Taskweaver](../../../translated_images/de/taskweaver.da8559999267715a.webp)

Hier ein Beispiel für ein Plugin zur Anomalieerkennung:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Der Code wird vor der Ausführung überprüft. Ein weiteres Feature zur Verwaltung des Kontexts in Taskweaver ist `experience`. Experience erlaubt es, den Kontext eines Gesprächs langfristig in einer YAML-Datei zu speichern. Das kann so konfiguriert werden, dass das LLM über die Zeit bei bestimmten Aufgaben besser wird, wenn es vorangegangene Gespräche zu sehen bekommt.

## JARVIS

Das letzte Agenten-Framework, das wir erkunden, ist [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Was JARVIS einzigartig macht, ist die Nutzung eines LLM zur Verwaltung des `Zustands` des Gesprächs und die `Werkzeuge` sind andere KI-Modelle. Jedes dieser KI-Modelle sind spezialisierte Modelle, die bestimmte Aufgaben ausführen, wie Objekterkennung, Transkription oder Bildbeschriftung.

![JARVIS](../../../translated_images/de/jarvis.762ddbadbd1a3a33.webp)

Das LLM, als universelles Modell, erhält die Anfrage des Nutzers und identifiziert die spezifische Aufgabe sowie alle Argumente/Daten, die zur Erfüllung der Aufgabe benötigt werden.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Das LLM formatiert dann die Anfrage so, dass ein spezialisiertes KI-Modell sie interpretieren kann, wie zum Beispiel in JSON. Sobald das KI-Modell seine Vorhersage basierend auf der Aufgabe zurückgibt, erhält das LLM die Antwort.

Falls mehrere Modelle benötigt werden, um die Aufgabe zu erfüllen, wird das LLM auch die Antworten dieser Modelle interpretieren, bevor es sie zusammenführt und die Antwort an den Nutzer generiert.

Das folgende Beispiel zeigt, wie dies funktioniert, wenn ein Nutzer eine Beschreibung und Zählung der Objekte in einem Bild anfragt:

## Aufgabe

Um dein Lernen zu KI-Agenten fortzusetzen, kannst du mit dem Microsoft Agent Framework folgendes bauen:

- Eine Anwendung, die ein Geschäftstreffen mit verschiedenen Abteilungen eines Bildungs-Startups simuliert.
- Erstelle Systemnachrichten, die LLMs dabei helfen, unterschiedliche Personas und Prioritäten zu verstehen, und ermögliche dem Nutzer, eine neue Produktidee zu präsentieren.
- Das LLM soll dann Folgefragen von jeder Abteilung generieren, um die Präsentation und Produktidee zu verfeinern und zu verbessern.

## Lernen hört hier nicht auf, setze die Reise fort

Nach Abschluss dieser Lektion solltest du unsere [Lernsammlung Generative KI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) besuchen, um dein Wissen in Generativer KI weiter auszubauen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->