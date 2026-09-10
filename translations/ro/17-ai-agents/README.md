[![Open Source Models](../../../translated_images/ro/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introducere

Agenții AI reprezintă o dezvoltare interesantă în AI Generativă, permițând modelelor mari de limbaj (LLMs) să evolueze de la asistenți la agenți capabili să întreprindă acțiuni. Cadrele pentru Agenții AI permit dezvoltatorilor să creeze aplicații care oferă LLM-urilor acces la unelte și gestionarea stării. Aceste cadre îmbunătățesc și vizibilitatea, permițând utilizatorilor și dezvoltatorilor să monitorizeze acțiunile planificate de LLM-uri, îmbunătățind astfel gestionarea experienței.

Lecția va acoperi următoarele aspecte:

- Înțelegerea ce este un Agent AI - Ce este exact un Agent AI?
- Explorarea a cinci cadre diferite pentru Agenți AI - Ce le face unice?
- Aplicarea acestor Agenți AI în diferite cazuri de utilizare - Când ar trebui să folosim Agenți AI?

## Obiective de învățare

După parcurgerea acestei lecții, vei putea să:

- Explici ce sunt Agenții AI și cum pot fi folosiți.
- Înțelegi diferențele între unele dintre cadrele populare pentru Agenți AI și cum diferă acestea.
- Înțelegi cum funcționează Agenții AI pentru a putea construi aplicații cu ei.

## Ce sunt Agenții AI?

Agenții AI reprezintă un domeniu foarte interesant în lumea AI Generativă. Odată cu această entuziasmare apare uneori o confuzie privind termenii și aplicațiile lor. Pentru a menține lucrurile simple și incluzive pentru majoritatea uneltelor care se referă la Agenți AI, vom folosi această definiție:

Agenții AI permit modelelor mari de limbaj (LLMs) să execute sarcini oferindu-le acces la un **stare** și **unelte**.

![Agent Model](../../../translated_images/ro/what-agent.21f2893bdfd01e6a.webp)

Să definim acești termeni:

**Modele Mari de Limbaj** - Acestea sunt modelele menționate pe parcursul acestui curs, cum ar fi GPT-5, GPT-4o și Llama 3.3, etc.

**Stare** - Aceasta se referă la contextul în care lucrează LLM-ul. LLM-ul folosește contextul acțiunilor sale anterioare și contextul curent pentru a-și ghida luarea deciziilor pentru acțiunile următoare. Cadrele pentru Agenți AI permit dezvoltatorilor să întrețină mai ușor acest context.

**Unelte** - Pentru a îndeplini sarcina solicitată de utilizator și planificată de LLM, acesta are nevoie de acces la unelte. Exemple de unelte pot fi o bază de date, o API, o aplicație externă sau chiar un alt LLM!

Aceste definiții sperăm să îți ofere o bază bună pe măsură ce vom vedea cum sunt implementate. Să explorăm câteva cadre diferite pentru Agenți AI:

## Agenții LangChain

[Agenții LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) reprezintă o implementare a definițiilor oferite mai sus.

Pentru a gestiona **starea**, folosește o funcție încorporată numită `AgentExecutor`. Aceasta acceptă agenții definiți și `uneltele` disponibile.

`AgentExecutor` stochează și istoricul conversațiilor pentru a oferi contextul discuției.

![Langchain Agents](../../../translated_images/ro/langchain-agents.edcc55b5d5c43716.webp)

LangChain oferă un [catalog de unelte](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) care pot fi importate în aplicația ta și la care LLM-ul poate avea acces. Acestea sunt create de comunitate și de echipa LangChain.

Poți apoi defini aceste unelte și să le transmiți către `AgentExecutor`.

Vizibilitatea este un alt aspect important când vorbim despre Agenți AI. Este esențial pentru dezvoltatorii aplicațiilor să înțeleagă ce unealtă folosește LLM-ul și de ce. Pentru asta, echipa LangChain a creat LangSmith.

## AutoGen

Următorul cadru pentru Agenți AI despre care vom discuta este [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Accentul principal al AutoGen îl reprezintă conversațiile. Agenții sunt atât **conversabili** cât și **personalizabili**.

**Conversabili -** LLM-urile pot începe și continua o conversație cu un alt LLM pentru a îndeplini o sarcină. Acest lucru se face prin crearea de `AssistantAgents` și oferindu-le un mesaj de sistem specific.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizabili** - Agenții pot fi definiți nu doar ca LLM-uri, ci pot fi utilizatori sau unelte. Ca dezvoltator, poți defini un `UserProxyAgent` responsabil de interacțiunea cu utilizatorul pentru feedback în îndeplinirea unei sarcini. Acest feedback poate continua execuția sarcinii sau o poate opri.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stare și Unelte

Pentru a modifica și gestiona starea, un Agent asistent generează cod Python pentru a îndeplini sarcina.

Iată un exemplu al procesului:

![AutoGen](../../../translated_images/ro/autogen.dee9a25a45fde584.webp)

#### LLM definit cu un mesaj de sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Acest mesaj de sistem direcționează acest LLM specific către funcțiile relevante pentru sarcina sa. Reține, cu AutoGen poți avea mai multe AssistantAgents definiți, fiecare cu mesaje de sistem diferite.

#### Conversația este inițiată de utilizator

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Acest mesaj din partea user_proxy (uman) este ceea ce va începe procesul Agentului de a explora funcțiile posibile pe care ar trebui să le execute.

#### Funcția este executată

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Odată ce conversația inițială este procesată, Agentul va sugera unealta de apelat. În acest caz, este o funcție numită `get_weather`. În funcție de configurația ta, această funcție poate fi executată automat și citită de Agent sau executată în baza inputului utilizatorului.

Poți găsi o listă de [exemple de cod AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) pentru a explora mai mult începutul construirii de aplicații.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) este SDK-ul open-source de la Microsoft pentru crearea de Agenți AI și sisteme multi-agent în **Python** și **.NET**. Reunește punctele forte ale două proiecte Microsoft anterioare — funcționalitățile enterprise ale **Semantic Kernel** și orchestrarea multi-agent a **AutoGen** — într-un singur cadru susținut. Dacă începi un nou proiect de agent astăzi, acesta este succesorul recomandat al AutoGen.

Cadrul scalează de la un singur **agent de chat** până la fluxuri de lucru complexe **multi-agent**, și se integrează direct cu Microsoft Foundry, Azure OpenAI și OpenAI. De asemenea, oferă observabilitate încorporată prin OpenTelemetry, astfel încât poți urmări exact ce fac agenții tăi.

### Stare și Unelte

**Stare** - cadrul gestionează contextul conversației pentru tine prin intermediul **firelor**. Un agent păstrează istoricul mesajelor (cererile utilizatorului, apelurile uneltelor și rezultatele lor), astfel fiecare schimb continuă pe baza celor anterioare. Firele pot fi și persistente, permițând conversației să fie întreruptă și reluată mai târziu.

**Unelte** - îi oferi agentului unelte trecând funcții Python simple. Parametrii cu tipuri adnotate sunt transformați automat într-un schemă, astfel modelul știe cum și când să le apeleze (apelarea funcțiilor). Cadrul suportă și servere Model Context Protocol (MCP) și unelte gazduite, cum ar fi un interpret de cod.

Iată un exemplu de agent unic cu o unealtă personalizată:

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

Pentru a te conecta la Azure OpenAI în Microsoft Foundry în schimb, transmite punctul tău final și acreditările către client:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Fluxuri de lucru multi-agent

Acolo unde cadrul iese cu adevărat în evidență este orchestrarea mai multor agenți împreună. De exemplu, poți rula agenți unul după altul (fiecare transferând contextul său următorului) sau poți ramifica la mai mulți agenți în paralel și agrega rezultatele lor:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Rulați agenții în secvență, trecând contextul conversației de-a lungul lanțului
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Distribuiți către agenți în paralel, apoi agregați răspunsurile lor
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Pentru a instala cadrul și a începe:

```bash
pip install agent-framework-core
# Integrări opționale
pip install agent-framework-openai       # OpenAI și Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Poți explora mai mult în [repositorul Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) și în [documentația oficială](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Următorul cadru pentru agenți pe care îl vom explora este [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Este cunoscut ca un agent "code-first" deoarece în loc să lucreze strict cu `șiruri de caractere` , poate lucra cu DataFrames în Python. Acesta devine extrem de util pentru sarcini de analiză și generare de date. Poate fi vorba despre crearea de grafice și diagrame sau generarea de numere aleatoare.

### Stare și Unelte

Pentru a gestiona starea conversației, TaskWeaver folosește conceptul de `Planner`. `Planner` este un LLM care preia cererea utilizatorilor și trasează sarcinile ce trebuie îndeplinite pentru a satisface această cerere.

Pentru a îndeplini sarcinile, `Planner` este conectat la colecția de unelte numite `Plugins`. Acestea pot fi clase Python sau un interpret general de cod. Aceste pluginuri sunt stocate ca embeddings pentru ca LLM să poată căuta mai bine pluginul corect.

![Taskweaver](../../../translated_images/ro/taskweaver.da8559999267715a.webp)

Iată un exemplu de plugin pentru gestionarea detectării de anomalii:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Codul este verificat înainte de executare. O altă caracteristică de gestionare a contextului în Taskweaver este `experience`. Experiența permite ca contextul unei conversații să fie salvat pe termen lung într-un fișier YAML. Acest lucru poate fi configurat astfel încât LLM să se îmbunătățească în timp pentru anumite sarcini, având acces la conversațiile anterioare.

## JARVIS

Ultimul cadru pentru agenți pe care îl vom explora este [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ce face JARVIS unic este că folosește un LLM pentru a gestiona `starea` conversației, iar `uneltele` sunt alte modele AI. Fiecare model AI este un model specializat care realizează anumite sarcini, cum ar fi detectarea obiectelor, transcrierea sau generarea de subtitrări pentru imagini.

![JARVIS](../../../translated_images/ro/jarvis.762ddbadbd1a3a33.webp)

LLM-ul, fiind un model cu scop general, primește cererea utilizatorului și identifică sarcina specifică și orice argumente/date necesare pentru îndeplinirea sarcinii.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM-ul formatează apoi cererea într-un mod pe care modelul AI specializat îl poate interpreta, cum ar fi JSON. După ce modelul AI returnează predicția sa bazată pe sarcină, LLM-ul primește răspunsul.

Dacă sunt necesare mai multe modele pentru îndeplinirea sarcinii, LLM-ul va interpreta și răspunsurile acestora înainte de a le aduce împreună pentru a genera răspunsul către utilizator.

Exemplul de mai jos arată cum ar funcționa asta când un utilizator cere o descriere și numărarea obiectelor dintr-o imagine:

## Temă

Pentru a continua învățarea despre Agenții AI, poți construi cu Microsoft Agent Framework:

- O aplicație care simulează o întâlnire de afaceri cu diferite departamente ale unei startup educaționale.
- Crează mesaje de sistem care ghidează LLM-urile în înțelegerea diferitelor persoane și priorități și permite utilizatorului să propună o idee nouă de produs.
- LLM-ul ar trebui apoi să genereze întrebări de urmărire de la fiecare departament pentru a rafina și îmbunătăți pitch-ul și ideea produsului.

## Învățarea nu se oprește aici, continuă Călătoria

După ce finalizezi această lecție, verifică colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți crești cunoștințele despre AI Generativ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->