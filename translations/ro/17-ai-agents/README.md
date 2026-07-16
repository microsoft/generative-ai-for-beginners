[![Open Source Models](../../../translated_images/ro/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introducere

Agenții AI reprezintă o evoluție interesantă în AI Generativ, permițând modelelor de limbaj de talie mare (LLM-uri) să treacă de la asistenți la agenți capabili să întreprindă acțiuni. Framework-urile pentru agenți AI permit dezvoltatorilor să creeze aplicații ce oferă LLM-urilor acces la unelte și gestionarea stării. Aceste framework-uri sporesc, de asemenea, vizibilitatea, permițând utilizatorilor și dezvoltatorilor să monitorizeze acțiunile planificate de LLM-uri, îmbunătățind astfel managementul experienței.

Lecția va acoperi următoarele domenii:

- Înțelegerea a ceea ce este un Agent AI - Ce este exact un Agent AI?
- Explorarea a cinci framework-uri diferite pentru Agenți AI - Ce le face unice?
- Aplicarea acestor Agenți AI în diferite cazuri de utilizare - Când ar trebui să folosim Agenți AI?

## Obiective de învățare

După ce parcurgi această lecție, vei putea:

- Explica ce sunt Agenții AI și cum pot fi folosiți.
- Să ai o înțelegere a diferențelor dintre unele dintre cele mai populare framework-uri pentru Agenți AI și cum diferă acestea.
- Să înțelegi cum funcționează Agenții AI pentru a construi aplicații cu ei.

## Ce sunt Agenții AI?

Agenții AI sunt un domeniu foarte interesant în lumea AI Generativ. Odată cu acest entuziasm apare uneori o confuzie a termenilor și a aplicării lor. Pentru a păstra lucrurile simple și incluzive pentru majoritatea uneltelor care se referă la Agenți AI, vom folosi această definiție:

Agenții AI permit modelelor de limbaj de talie mare (LLM-uri) să execute sarcini oferindu-le acces la un **statut** și **unelte**.

![Agent Model](../../../translated_images/ro/what-agent.21f2893bdfd01e6a.webp)

Să definim acești termeni:

**Modele de limbaj de talie mare** - Acestea sunt modelele menționate pe parcursul acestui curs, cum ar fi GPT-3.5, GPT-4, Llama-2 etc.

**Statut** - Acesta se referă la contextul în care LLM-ul lucrează. LLM-ul folosește contextul acțiunilor sale anterioare și contextul curent, ghidându-și luarea de decizii pentru acțiunile ulterioare. Framework-urile pentru Agenți AI permit dezvoltatorilor să mențină acest context mai ușor.

**Unelte** - Pentru a îndeplini sarcina solicitată de utilizator și planificată de LLM, LLM-ul are nevoie de acces la unelte. Unele exemple de unelte pot fi o bază de date, un API, o aplicație externă sau chiar alt LLM!

Aceste definiții sperăm să-ți ofere o bază solidă pe măsură ce explorăm modul în care sunt implementate. Să explorăm câteva framework-uri diferite pentru Agenții AI:

## Agenții LangChain

[Agenții LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) sunt o implementare a definițiilor oferite mai sus.

Pentru a gestiona **statutul**, folosește o funcție încorporată numită `AgentExecutor`. Aceasta acceptă `agentul` definit și `uneltele` disponibile pentru acesta.

`Agent Executor` stochează, de asemenea, istoricul chat-ului pentru a furniza contextul conversației.

![Langchain Agents](../../../translated_images/ro/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferă un [catalog de unelte](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) care pot fi importate în aplicația ta și la care LLM-ul poate avea acces. Acestea sunt create de comunitate și de echipa LangChain.

Poți apoi să definești aceste unelte și să le pasezi către `Agent Executor`.

Vizibilitatea este un alt aspect important când vorbim despre Agenți AI. Este important ca dezvoltatorii de aplicații să înțeleagă ce unealtă folosește LLM-ul și de ce. Pentru acest lucru, echipa LangChain a dezvoltat LangSmith.

## AutoGen

Următorul framework pentru Agenți AI pe care îl vom discuta este [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Principalul focus al AutoGen este conversațiile. Agenții sunt atât **conversabili**, cât și **personalizabili**.

**Conversabil -** LLM-urile pot iniția și continua o conversație cu un alt LLM pentru a îndeplini o sarcină. Acest lucru se realizează prin crearea de `AssistantAgents` și oferindu-le un mesaj specific de sistem.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizabil** - Agenții pot fi definiți nu numai ca LLM-uri, ci și ca utilizatori sau unelte. Ca dezvoltator, poți defini un `UserProxyAgent` responsabil pentru interacțiunea cu utilizatorul pentru feedback în îndeplinirea unei sarcini. Acest feedback poate fie să continue execuția sarcinii, fie să o oprească.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Statut și Unelte

Pentru a schimba și gestiona statutul, un Agent asistent generează cod Python pentru a îndeplini sarcina.

Iată un exemplu al procesului:

![AutoGen](../../../translated_images/ro/autogen.dee9a25a45fde584.webp)

#### LLM definit cu un mesaj de sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Acest mesaj de sistem direcționează acest LLM specific către funcțiile relevante pentru sarcina sa. Amintește-ți, cu AutoGen poți avea mai mulți AssistantAgents definiți cu mesaje diferite de sistem.

#### Chat-ul este inițiat de utilizator

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Acest mesaj de la user_proxy (om) este ceea ce va începe procesul Agentului de a explora posibilele funcții pe care ar trebui să le execute.

#### Funcția este executată

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Odată ce chatul inițial este procesat, Agentul va trimite unealta sugerată pentru a fi apelată. În acest caz, este o funcție numită `get_weather`. În funcție de configurația ta, această funcție poate fi executată automat și citită de Agent sau poate fi executată pe baza inputului utilizatorului.

Poți găsi o listă de [exemple de cod AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) pentru a explora mai departe cum să începi să construiești.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) este SDK-ul open-source al Microsoft pentru construirea de Agenți AI și sisteme multi-agent în **Python** și **.NET**. Adună punctele forte ale două proiecte anterioare Microsoft — funcționalitățile enterprise ale **Semantic Kernel** și orchestrarea multi-agent a **AutoGen** — într-un singur framework susținut. Dacă începi astăzi un nou proiect cu agenți, acesta este succesorul recomandat al AutoGen.

Framework-ul se scalează de la un singur **agent de chat** până la fluxuri de lucru complexe **multi-agent** și se integrează direct cu Microsoft Foundry, Azure OpenAI și OpenAI. Oferă, de asemenea, observabilitate încorporată prin OpenTelemetry, astfel încât poți urmări exact ce fac agenții tăi.

### Statut și Unelte

**Statut** - Framework-ul gestionează contextul conversației pentru tine prin **fire**. Un agent ține evidența istoricului mesajelor (cererile utilizatorului, apelurile către unelte și rezultatele acestora), astfel încât fiecare pas se bazează pe cele anterioare. Firele pot fi, de asemenea, păstrate, permițând ca o conversație să fie întreruptă și reluată mai târziu.

**Unelte** - Oferi un agent unelte trecând funcții Python simple. Parametrii tipizați sunt automat transformați într-un schelet, astfel încât modelul să știe cum și când să le apeleze (apelarea funcțiilor). Framework-ul suportă, de asemenea, servere Model Context Protocol (MCP) și unelte găzduite precum un interpret de cod.

Iată un exemplu de agent simplu cu o unealtă personalizată:

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

Pentru a te conecta la Azure OpenAI în Microsoft Foundry în schimb, transmite endpoint-ul și acreditările clientului:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Fluxuri multi-agent

Acolo unde framework-ul iese în evidență este orchestrarea mai multor agenți împreună. De exemplu, poți rula agenți unul după altul (fiecare trecându-și contextul următorului) sau poți desfășura mai mulți agenți în paralel și agrega rezultatele lor:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Rulați agenții în secvență, transmitând contextul conversației de-a lungul lanțului
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribuiți către agenți în paralel, apoi agregați răspunsurile lor
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Pentru a instala framework-ul și a începe:

```bash
pip install agent-framework-core
# Integrări opționale
pip install agent-framework-openai       # OpenAI și Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Poți explora mai mult în [repositorul Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) și în [documentația oficială](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Următorul framework pentru agenți pe care îl vom explora este [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Este cunoscut ca un agent „code-first” deoarece, în loc să lucreze strict cu `șiruri de caractere`, poate lucra cu DataFrame-uri în Python. Acest lucru devine extrem de util pentru sarcini de analiză și generare de date. Pot fi lucruri precum crearea de grafice și diagrame sau generarea de numere aleatorii.

### Statut și Unelte

Pentru a gestiona statutul conversației, TaskWeaver folosește conceptul de `Planner`. `Planner` este un LLM care preia cererea utilizatorilor și trasează sarcinile ce trebuie îndeplinite pentru a satisface această cerere.

Pentru a îndeplini sarcinile, `Planner` are acces la colecția de unelte numită `Plugins`. Acestea pot fi clase Python sau un interpret general de cod. Aceste plugin-uri sunt stocate ca embeddings astfel încât LLM-ul să poată căuta mai bine plugin-ul corect.

![Taskweaver](../../../translated_images/ro/taskweaver.da8559999267715a.webp)

Iată un exemplu de plugin pentru detecția anomaliilor:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Codul este verificat înainte de execuție. O altă caracteristică pentru gestionarea contextului în Taskweaver este `experience`. Experiența permite stocarea pe termen lung a contextului unei conversații într-un fișier YAML. Aceasta poate fi configurată astfel încât LLM-ul să se îmbunătățească în timp la anumite sarcini, având acces la conversațiile anterioare.

## JARVIS

Ultimul framework pentru agenți pe care îl vom explora este [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ce îl face unic pe JARVIS este că folosește un LLM pentru a gestiona `statutul` conversației, iar `uneltele` sunt alte modele AI. Fiecare model AI este un model specializat care realizează anumite sarcini precum detecția obiectelor, transcrierea sau generarea de descrieri pentru imagini.

![JARVIS](../../../translated_images/ro/jarvis.762ddbadbd1a3a33.webp)

LLM-ul, fiind un model cu scop general, primește cererea utilizatorului și identifică sarcina specifică și eventualii parametri/date necesare îndeplinirii sarcinii.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM-ul formatează apoi cererea într-un mod pe care modelul AI specializat îl poate interpreta, cum ar fi JSON. După ce modelul AI oferă predicția bazată pe sarcină, LLM-ul primește răspunsul.

Dacă sunt necesare mai multe modele pentru a îndeplini sarcina, LLM-ul va interpreta și răspunsurile acestora înainte de a le combina pentru a genera răspunsul către utilizator.

Exemplul de mai jos arată cum ar funcționa atunci când un utilizator cere o descriere și numărul obiectelor dintr-o imagine:

## Tema

Pentru a continua să înveți despre Agenții AI poți construi cu Microsoft Agent Framework:

- O aplicație care simulează o întâlnire de afaceri cu diferite departamente ale unei startup educaționale.
- Creează mesaje de sistem care să ghideze LLM-urile în înțelegerea diferitelor persoane și priorități, și să permită utilizatorului să propună o idee de nou produs.
- LLM-ul ar trebui să genereze apoi întrebări de urmărire de la fiecare departament pentru a rafina și îmbunătăți prezentarea și ideea produsului.

## Învățarea nu se oprește aici, continuă Călătoria

După ce termini această lecție, consultă colecția noastră de [Învățare AI Generativ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a-ți continua dezvoltarea în domeniul AI Generativ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->