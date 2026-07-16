[![Open Source Models](../../../translated_images/pl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Wprowadzenie

Agenci AI reprezentują ekscytujący rozwój w generatywnej sztucznej inteligencji, umożliwiając dużym modelom językowym (LLMs) ewolucję z asystentów do agentów zdolnych do podejmowania działań. Ramy AI Agent umożliwiają programistom tworzenie aplikacji, które dają LLM dostęp do narzędzi i zarządzania stanem. Te ramy również zwiększają przejrzystość, pozwalając użytkownikom i programistom monitorować działania planowane przez LLM, co poprawia zarządzanie doświadczeniem.

Lekcja obejmie następujące obszary:

- Zrozumienie, czym jest AI Agent - Czym dokładnie jest AI Agent?
- Przegląd pięciu różnych ram AI Agent - Co je wyróżnia?
- Zastosowanie tych AI Agentów do różnych przypadków użycia - Kiedy powinniśmy korzystać z AI Agentów?

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wyjaśnić, czym są AI Agenci i jak można ich używać.
- Zrozumieć różnice między niektórymi popularnymi ramami AI Agent i czym się różnią.
- Rozumieć, jak działają AI Agenci, aby tworzyć z nimi aplikacje.

## Czym są AI Agenci?

AI Agenci to bardzo ekscytująca dziedzina w świecie Generatywnej AI. Z tą ekscytacją czasem wiąże się zamieszanie co do terminów i ich zastosowań. Aby zachować prostotę i uwzględnić większość narzędzi odnoszących się do AI Agentów, użyjemy tej definicji:

AI Agents pozwalają dużym modelom językowym (LLMs) wykonywać zadania, dając im dostęp do **stanu** i **narzędzi**.

![Agent Model](../../../translated_images/pl/what-agent.21f2893bdfd01e6a.webp)

Zdefiniujmy te terminy:

**Duże Modele Językowe** - To modele, o których mowa w całym kursie, takie jak GPT-3.5, GPT-4, Llama-2 itd.

**Stan** - Odnosi się do kontekstu, w którym pracuje LLM. LLM używa kontekstu swoich poprzednich działań oraz bieżącego kontekstu, kierując podejmowaniem decyzji dla kolejnych działań. Ramy AI Agent ułatwiają programistom utrzymanie tego kontekstu.

**Narzędzia** - Aby wykonać zadanie, o które prosi użytkownik i które LLM zaplanował, LLM potrzebuje dostępu do narzędzi. Przykładami narzędzi mogą być baza danych, API, zewnętrzna aplikacja lub nawet inny LLM!

Te definicje mają nadzieję, że dadzą ci solidne podstawy w dalszej części, gdy przyjrzymy się, jak są one implementowane. Sprawdźmy kilka różnych ram AI Agent:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) to implementacja powyższych definicji.

Aby zarządzać **stanem**, używa wbudowanej funkcji zwanej `AgentExecutor`. Przyjmuje ona zdefiniowanego `agenta` i dostępne dla niego `narzędzia`.

`Agent Executor` także przechowuje historię czatu, aby zapewnić kontekst rozmowy.

![Langchain Agents](../../../translated_images/pl/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferuje [katalog narzędzi](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), które można zaimportować do swojej aplikacji, do których LLM może mieć dostęp. Są one tworzone przez społeczność i zespół LangChain.

Możesz następnie zdefiniować te narzędzia i przekazać je do `Agent Executor`.

Widoczność to kolejny ważny aspekt, gdy mówimy o AI Agentach. Ważne jest, aby programiści aplikacji rozumieli, które narzędzie LLM używa i dlaczego. W tym celu zespół LangChain opracował LangSmith.

## AutoGen

Kolejną ramą AI Agent, którą omówimy, jest [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Głównym celem AutoGen są konwersacje. Agenci są zarówno **rozmowni**, jak i **dostosowywalni**.

**Rozmowni -** LLM mogą rozpocząć i kontynuować rozmowę z innym LLM, aby wykonać zadanie. Odbywa się to poprzez tworzenie `AssistantAgents` i nadawanie im konkretnej wiadomości systemowej.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Dostosowywalni** - Agenci mogą być definiowani nie tylko jako LLM, ale także jako użytkownik lub narzędzie. Jako programista możesz zdefiniować `UserProxyAgent`, który odpowiada za interakcję z użytkownikiem w celu uzyskania opinii przy wykonywaniu zadania. Ta opinia może kontynuować wykonanie zadania lub je zatrzymać.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stan i Narzędzia

Aby zmieniać i zarządzać stanem, agent asystent generuje kod Pythona do wykonania zadania.

Oto przykład tego procesu:

![AutoGen](../../../translated_images/pl/autogen.dee9a25a45fde584.webp)

#### LLM zdefiniowany wiadomością systemową

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ta wiadomość systemowa kieruje tym konkretnym LLM, które funkcje są istotne dla jego zadania. Pamiętaj, że w AutoGen możesz mieć wielu zdefiniowanych AssistantAgents z różnymi wiadomościami systemowymi.

#### Rozmowa rozpoczyna się użytkownik

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ta wiadomość od user_proxy (Człowieka) rozpocznie proces agenta do zbadania możliwych funkcji, które powinien wykonać.

#### Wywołanie funkcji

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po przetworzeniu początkowej rozmowy agent wyśle proponowane narzędzie do wywołania. W tym przypadku jest to funkcja o nazwie `get_weather`. W zależności od konfiguracji ta funkcja może być automatycznie wykonywana i odczytywana przez agenta lub wywoływana na podstawie wejścia użytkownika.

Możesz znaleźć listę [przykładów kodu AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), aby dalej eksplorować, jak zacząć budować.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) to otwartoźródłowe SDK Microsoft do tworzenia AI Agentów i systemów wieloagentowych w **Python** i **.NET**. Łączy ono zalety dwóch wcześniejszych projektów Microsoft — funkcje korporacyjne **Semantic Kernel** i orkiestrację wieloagentową **AutoGen** — w jedną, wspieraną ramę. Jeśli dziś zaczynasz nowy projekt agenta, to jest zalecany następca AutoGen.

Framework skalowalny jest od pojedynczego **agenta czatu** aż po złożone **workflowy wieloagentowe**, a także integruje się bezpośrednio z Microsoft Foundry, Azure OpenAI i OpenAI. Zapewnia też wbudowaną obserwowalność przez OpenTelemetry, abyś mógł dokładnie śledzić, co robią twoi agenci.

### Stan i Narzędzia

**Stan** - Framework zarządza kontekstem rozmowy za pomocą **wątków**. Agent śledzi historię wiadomości (żądania użytkownika, wywołania narzędzi i ich wyniki), więc każda kolejna tura opiera się na poprzednich. Wątki mogą być również zapisywane, co pozwala na wstrzymanie i wznowienie rozmowy.

**Narzędzia** - Przekazujesz agentowi narzędzia, przekazując zwykłe funkcje Pythona. Typowane parametry są automatycznie zamieniane na schemat, więc model wie, jak i kiedy je wywoływać (function calling). Framework obsługuje też serwery Model Context Protocol (MCP) oraz narzędzia hostowane, takie jak interpreter kodu.

Oto przykład pojedynczego agenta z niestandardowym narzędziem:

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

Aby połączyć się z Azure OpenAI w Microsoft Foundry, przekaż swoje punkt końcowy i dane uwierzytelniające do klienta:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Workflowy wieloagentowe

To, co wyróżnia framework, to orkiestracja kilku agentów razem. Na przykład możesz uruchamiać agentów jeden po drugim (każdy przekazuje swój kontekst następnemu) lub rozgałęziać się do kilku agentów równolegle i agregować ich wyniki:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Uruchom agentów kolejno, przekazując kontekst rozmowy wzdłuż łańcucha
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Rozgałęź do agentów równolegle, a następnie zbierz ich odpowiedzi
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Aby zainstalować framework i zacząć:

```bash
pip install agent-framework-core
# Opcjonalne integracje
pip install agent-framework-openai       # OpenAI i Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Możesz zgłębić więcej w [repozytorium Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) oraz w [oficjalnej dokumentacji](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Kolejną ramą agenta, którą omówimy, jest [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Znany jest jako agent „pierwszeństwo kodu”, ponieważ zamiast pracować wyłącznie ze `stringami`, może operować na DataFrame'ach w Pythonie. Jest to niezwykle przydatne w zadaniach analizy danych i generowania danych. Mogą to być rzeczy takie jak tworzenie wykresów i diagramów lub generowanie losowych liczb.

### Stan i Narzędzia

Aby zarządzać stanem rozmowy, TaskWeaver używa koncepcji `Plannera`. `Planner` to LLM, który przyjmuje żądanie od użytkowników i mapuje zadania, które trzeba wykonać, aby spełnić to żądanie.

Aby wykonać zadania, `Planner` ma dostęp do kolekcji narzędzi zwanych `Plugins`. Mogą to być klasy Pythona lub ogólny interpreter kodu. Te wtyczki przechowywane są jako osadzenia, aby LLM mógł lepiej wyszukiwać odpowiednią wtyczkę.

![Taskweaver](../../../translated_images/pl/taskweaver.da8559999267715a.webp)

Oto przykład wtyczki do obsługi wykrywania anomalii:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod jest weryfikowany przed wykonaniem. Kolejną funkcją do zarządzania kontekstem w Taskweaver jest `experience`. Experience pozwala na długoterminowe przechowywanie kontekstu rozmowy w pliku YAML. Można to skonfigurować tak, żeby LLM poprawiał się z czasem w pewnych zadaniach, biorąc pod uwagę wcześniejsze rozmowy.

## JARVIS

Ostatnią ramą agenta, którą omówimy, jest [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). To, co wyróżnia JARVIS, to fakt, że używa LLM do zarządzania `stanem` rozmowy, a `narzędzia` to inne modele AI. Każdy z modeli AI jest modelem specjalistycznym, który wykonuje określone zadania, takie jak wykrywanie obiektów, transkrypcja lub opisywanie obrazów.

![JARVIS](../../../translated_images/pl/jarvis.762ddbadbd1a3a33.webp)

LLM, będąc modelem ogólnego przeznaczenia, odbiera żądanie od użytkownika i identyfikuje konkretne zadanie oraz wszelkie argumenty/dane potrzebne do wykonania tego zadania.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM następnie formatuje żądanie w sposób zrozumiały dla specjalistycznego modelu AI, na przykład w JSON. Kiedy model AI zwróci swoją predykcję na podstawie zadania, LLM odbiera odpowiedź.

Jeśli do wykonania zadania wymaga się kilku modeli, LLM również interpretuje odpowiedzi tych modeli, zanim połączy je, aby wygenerować odpowiedź dla użytkownika.

Poniższy przykład pokazuje, jak to działa, gdy użytkownik prosi o opis i liczbę obiektów na zdjęciu:

## Zadanie

Aby kontynuować naukę o AI Agentach, możesz zbudować z Microsoft Agent Framework:

- Aplikację symulującą spotkanie biznesowe z różnymi działami startupu edukacyjnego.
- Utwórz wiadomości systemowe, które pomogą LLM zrozumieć różne persony i priorytety, oraz umożliwią użytkownikowi zaproponowanie nowego pomysłu na produkt.
- LLM powinien następnie wygenerować pytania uzupełniające z każdego działu, aby doprecyzować i ulepszyć prezentację i pomysł na produkt.

## Nauka nie kończy się tutaj, kontynuuj podróż

Po ukończeniu tej lekcji sprawdź naszą [kolekcję nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować rozwijanie wiedzy o generatywnej AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->