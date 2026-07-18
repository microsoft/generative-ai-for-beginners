[![Open Source Models](../../../translated_images/pl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Wprowadzenie

Agent AI to ekscytujący rozwój w dziedzinie Generatywnej Sztucznej Inteligencji, pozwalający na ewolucję dużych modeli językowych (LLM) z asystentów w agentów zdolnych do podejmowania działań. Frameworki Agentów AI umożliwiają programistom tworzenie aplikacji, które dają LLM dostęp do narzędzi i zarządzania stanem. Te frameworki poprawiają także widoczność, pozwalając użytkownikom i programistom monitorować działania planowane przez LLM, co poprawia zarządzanie doświadczeniem.

W lekcji omówimy następujące zagadnienia:

- Zrozumienie czym jest Agent AI - Co dokładnie oznacza Agent AI?
- Przegląd pięciu różnych frameworków Agentów AI - Co je wyróżnia?
- Zastosowanie tych Agentów AI w różnych scenariuszach - Kiedy powinniśmy używać Agentów AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Wyjaśnić, czym są Agenci AI i jak można ich używać.
- Zrozumieć różnice między popularnymi frameworkami Agentów AI oraz ich odmiany.
- Zrozumieć, jak działają Agenci AI, aby móc zbudować z nimi aplikacje.

## Czym są Agenci AI?

Agenci AI to bardzo ekscytująca dziedzina w świecie Generatywnej Sztucznej Inteligencji. Z tym entuzjazmem wiąże się czasem zamieszanie terminologiczne i ich zastosowanie. Aby uprościć i objąć większość narzędzi określających się jako Agenci AI, użyjemy tej definicji:

Agenci AI pozwalają dużym modelom językowym (LLM) wykonywać zadania, dając im dostęp do **stanu** i **narzędzi**.

![Model Agenta](../../../translated_images/pl/what-agent.21f2893bdfd01e6a.webp)

Zdefiniujmy te pojęcia:

**Duże modele językowe** – to modele omawiane w tym kursie, takie jak GPT-5, GPT-4o oraz Llama 3.3 itd.

**Stan** – odnosi się do kontekstu, w którym pracuje LLM. LLM korzysta z kontekstu swoich wcześniejszych działań oraz aktualnego kontekstu, co kieruje jego podejmowaniem decyzji w kolejnych krokach. Frameworki Agentów AI ułatwiają programistom utrzymanie tego kontekstu.

**Narzędzia** – aby wykonać zadanie, które użytkownik zlecił i które LLM zaplanował, LLM potrzebuje dostępu do narzędzi. Przykładami narzędzi mogą być baza danych, API, zewnętrzna aplikacja lub nawet inny LLM!

Te definicje powinny dać Ci solidne podstawy do dalszego zgłębiania implementacji. Przyjrzyjmy się kilku różnym frameworkom Agentów AI:

## Agenci LangChain

[Agenci LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) to implementacja powyższych definicji.

Do zarządzania **stanem** używa wbudowanej funkcji `AgentExecutor`. Przyjmuje ona zdefiniowanego `agenta` oraz dostępne dla niego `narzędzia`.

`AgentExecutor` przechowuje także historię rozmowy, aby zapewnić kontekst czatu.

![Agenci Langchain](../../../translated_images/pl/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferuje [katalog narzędzi](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), które można importować do swojej aplikacji, dając LLM do nich dostęp. Są tworzone przez społeczność oraz zespół LangChain.

Możesz wtedy zdefiniować te narzędzia i przekazać je do `AgentExecutor`.

Widoczność to kolejny ważny aspekt w kontekście Agentów AI. Dla twórców aplikacji ważne jest zrozumienie, którego narzędzia LLM używa i dlaczego. Z tego powodu zespół LangChain opracował LangSmith.

## AutoGen

Kolejny framework agentów, który omówimy, to [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Głównym celem AutoGen są rozmowy. Agenci są zarówno **rozmawialni** jak i **konfigurowalni**.

**Rozmawialni -** LLM mogą rozpocząć i kontynuować rozmowę z innym LLM, aby wykonać zadanie. Odbywa się to przez tworzenie `AssistantAgents` i przypisywanie im określonej wiadomości systemowej.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Konfigurowalni** - Agenci mogą być definiowani nie tylko jako LLM, ale także jako użytkownik lub narzędzie. Jako programista możesz zdefiniować `UserProxyAgent`, który odpowiada za interakcję z użytkownikiem w celu uzyskania opinii dotyczącej realizacji zadania. Ta opinia może kontynuować wykonanie zadania lub je zatrzymać.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stan i Narzędzia

Aby zmieniać i zarządzać stanem, asystent Agent generuje kod w Pythonie do ukończenia zadania.

Oto przykład tego procesu:

![AutoGen](../../../translated_images/pl/autogen.dee9a25a45fde584.webp)

#### LLM zdefiniowany wiadomością systemową

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ta wiadomość systemowa kieruje tym konkretnym LLM, jakie funkcje są istotne dla jego zadania. Pamiętaj, że w AutoGen możesz mieć wielu zdefiniowanych AssistantAgents z różnymi wiadomościami systemowymi.

#### Rozmowa rozpoczyna się od użytkownika

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ta wiadomość od user_proxy (człowieka) rozpocznie proces, w którym agent będzie badać możliwe funkcje do wykonania.

#### Funkcja jest wykonywana

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Po przetworzeniu początkowego czatu, agent wyśle zaproponowane narzędzie do wywołania. W tym przypadku jest to funkcja o nazwie `get_weather`. W zależności od konfiguracji, funkcja ta może być wykonana automatycznie i odczytana przez agenta lub wykonywana na podstawie danych od użytkownika.

Możesz znaleźć listę [przykładów kodu AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), aby dalej eksplorować sposoby rozpoczęcia budowy.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) to otwarte SDK Microsoftu do budowy Agentów AI i systemów wieloagentowych w **Python** i **.NET**. Łączy zalety dwóch wcześniejszych projektów Microsoftu — funkcje korporacyjne **Semantic Kernel** oraz orkiestrację wieloagentową **AutoGen** — w jeden wspierany framework. Jeśli zaczynasz nowy projekt agenta dzisiaj, jest to zalecany następca AutoGen.

Framework skalowalny jest od pojedynczego **agenta czatu** aż po złożone **wieloagentowe przepływy pracy**, integruje się bezpośrednio z Microsoft Foundry, Azure OpenAI i OpenAI. Zapewnia też wbudowaną obserwowalność poprzez OpenTelemetry, dzięki czemu możesz śledzić dokładnie, co robią Twoi agenci.

### Stan i Narzędzia

**Stan** - Framework zarządza kontekstem rozmowy poprzez **wątki**. Agent śledzi historię wiadomości (żądania użytkownika, wywołania narzędzi oraz ich wyniki), dzięki czemu każde kolejne działanie opiera się na poprzednich. Wątki mogą być również zapisywane, co pozwala na wstrzymanie i wznowienie rozmowy później.

**Narzędzia** - Narzędzia dla agenta przekazujesz poprzez zwykłe funkcje Pythona. Parametry z adnotacjami typów są automatycznie przekształcane w schemat, dzięki czemu model wie, jak i kiedy je wywołać (wywołanie funkcji). Framework obsługuje również serwery Model Context Protocol (MCP) i hostowane narzędzia, takie jak interpreter kodu.

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

Aby połączyć się z Azure OpenAI w Microsoft Foundry, przekaż swoje punkty końcowe i dane uwierzytelniające do klienta:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Wieloagentowe przepływy pracy

Największą moc frameworku stanowi możliwość orkiestracji wielu agentów razem. Na przykład można uruchamiać agentów kolejno (każdy przekazuje kontekst kolejnemu) lub uruchomić kilku agentów równolegle i zbierać ich wyniki:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Uruchom agentów kolejno, przekazując kontekst rozmowy wzdłuż łańcucha
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Rozdziel na agentów równolegle, a następnie zbierz ich odpowiedzi
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Aby zainstalować framework i rozpocząć:

```bash
pip install agent-framework-core
# Opcjonalne integracje
pip install agent-framework-openai       # OpenAI i Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Możesz dowiedzieć się więcej w [repozytorium Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) oraz w [oficjalnej dokumentacji](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Kolejny framework agentów, który omówimy, to [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Znany jest jako agent „code-first”, bo zamiast stricte operować na `stringach`, potrafi działać na DataFrames w Pythonie. Jest to bardzo przydatne do analiz danych i zadań generacyjnych. Może to być tworzenie wykresów i diagramów lub generowanie liczb losowych.

### Stan i Narzędzia

Aby zarządzać stanem rozmowy, TaskWeaver wykorzystuje koncepcję `Planner`. `Planner` to LLM, który przyjmuje żądania użytkowników i planuje zadania, które muszą zostać wykonane, aby je zrealizować.

Aby ukończyć zadania, `Planner` ma dostęp do zestawu narzędzi zwanych `Plugins`. Mogą to być klasy Pythona lub ogólny interpreter kodu. Te wtyczki są przechowywane jako osadzenia, co pozwala LLM łatwiej wyszukać odpowiednią wtyczkę.

![Taskweaver](../../../translated_images/pl/taskweaver.da8559999267715a.webp)

Oto przykład wtyczki do wykrywania anomalii:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod jest weryfikowany przed wykonaniem. Inną funkcją do zarządzania kontekstem w Taskweaver jest `experience` (doświadczenie). Doświadczenie pozwala zapisywać kontekst rozmowy na dłuższy czas w pliku YAML. Można to skonfigurować tak, aby LLM z czasem poprawiał się w wykonywaniu niektórych zadań, opierając się na wcześniejszych rozmowach.

## JARVIS

Ostatni framework agentów, który omówimy, to [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Co wyróżnia JARVIS, to fakt, że do zarządzania `stanem` rozmowy wykorzystuje LLM, a `narzędzia` to inne modele AI. Każdy z tych modeli jest specjalistyczny i wykonuje określone zadania, takie jak wykrywanie obiektów, transkrypcja czy opisywanie obrazów.

![JARVIS](../../../translated_images/pl/jarvis.762ddbadbd1a3a33.webp)

LLM, będąc modelem ogólnego zastosowania, odbiera żądanie od użytkownika i identyfikuje konkretne zadanie oraz wszelkie argumenty/dane potrzebne do jego wykonania.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM następnie formatuje żądanie w sposób interpretowalny dla specjalistycznego modelu AI, np. w JSON. Gdy model AI zwraca prognozę na podstawie zadania, LLM odbiera odpowiedź.

Jeśli do wykonania zadania wymaganych jest kilka modeli, LLM interpretuje również ich odpowiedzi, po czym łączy je, generując odpowiedź dla użytkownika.

Poniższy przykład pokazuje, jak to działa, gdy użytkownik prosi o opis i policzenie obiektów na zdjęciu:

## Zadanie

Aby kontynuować naukę o Agentach AI, możesz zbudować przy użyciu Microsoft Agent Framework:

- Aplikację symulującą spotkanie biznesowe z różnymi działami firmy edukacyjnej startupu.
- Stwórz wiadomości systemowe, które pomogą LLM zrozumieć różne persony i priorytety, oraz umożliwią użytkownikowi prezentację nowego pomysłu na produkt.
- Następnie LLM powinien wygenerować pytania uzupełniające z każdego działu, aby dopracować i ulepszyć prezentację oraz pomysł na produkt.

## Nauka się tutaj nie kończy, kontynuuj podróż

Po ukończeniu tej lekcji zapoznaj się z naszą [kolekcją nauki Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generatywnej Sztucznej Inteligencji!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->