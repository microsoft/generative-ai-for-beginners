[![Open Source Models](../../../translated_images/sl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Uvod

AI agenti predstavljajo razburljiv razvoj na področju generativne umetne inteligence, ki omogoča velikim jezikovnim modelom (LLM), da se razvijejo iz pomočnikov v agente, sposobne izvajanja dejanj. Okviri za AI agente razvijalcem omogočajo ustvarjanje aplikacij, ki LLM-jem omogočajo dostop do orodij in upravljanje stanja. Ti okviri prav tako izboljšujejo vidnost, kar omogoča uporabnikom in razvijalcem spremljanje dejanj, ki jih načrtujejo LLM-ji, s čimer izboljšujejo upravljanje izkušenj.

Lekcija bo obravnavala naslednja področja:

- Razumevanje, kaj je AI agent - Kaj pravzaprav je AI agent?
- Raziskovanje petih različnih okvirjev za AI agente - Kaj jih ločuje?
- Uporaba teh AI agentov v različnih primerih uporabe - Kdaj naj uporabimo AI agente?

## Cilji učenja

Po končani tej lekciji boste lahko:

- Pojasnili, kaj so AI agenti in kako jih lahko uporabimo.
- Razumeli razlike med nekaterimi priljubljenimi okviri za AI agente in njihova odstopanja.
- Razumeli, kako AI agenti delujejo, da boste lahko z njimi gradili aplikacije.

## Kaj so AI agenti?

AI agenti so zelo razburljivo področje v svetu generativne umetne inteligence. S to razburljivostjo včasih pride tudi zmeda glede terminologije in njihove uporabe. Da ostanemo preprosti in vključujoči večino orodij, ki se nanašajo na AI agente, bomo uporabili to definicijo:

AI agenti omogočajo velikim jezikovnim modelom (LLM), da opravljajo naloge tako, da jim omogočajo dostop do **stanja** in **orodij**.

![Agent Model](../../../translated_images/sl/what-agent.21f2893bdfd01e6a.webp)

Definirajmo te pojme:

**Veliki jezikovni modeli** - To so modeli, omenjeni v tem tečaju, kot so GPT-5, GPT-4o in Llama 3.3 itd.

**Stanje** - Nanaša se na kontekst, v katerem LLM deluje. LLM uporablja kontekst preteklih dejanj in trenutni kontekst, kar vodi njegovo odločanje za naslednja dejanja. Okviri za AI agente omogočajo razvijalcem lažje ohranjanje tega konteksta.

**Orodja** - Da bi izpolnil nalogo, ki jo je zahteval uporabnik in jo je LLM načrtoval, mora imeti LLM dostop do orodij. Nekateri primeri orodij so baza podatkov, API, zunanja aplikacija ali celo drug LLM!

Te definicije vam bodo upam, da dale dobro izhodišče, ko bomo pogledali, kako so ti agenti implementirani. Raziskujmo nekaj različnih okvirjev za AI agente:

## LangChain Agenti

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) so implementacija zgornjih definicij.

Za upravljanje **stanja** uporablja vgrajeno funkcijo z imenom `AgentExecutor`. Ta sprejme definiran `agent` in `orodja`, ki so mu na voljo.

`Agent Executor` prav tako shranjuje zgodovino pogovora, da zagotovi kontekst pogovora.

![Langchain Agents](../../../translated_images/sl/langchain-agents.edcc55b5d5c43716.webp)

LangChain ponuja [katalog orodij](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), ki jih lahko uvozite v svojo aplikacijo, do katerih lahko dostopa LLM. Ta so izdelana s strani skupnosti in ekipe LangChain.

Nato lahko ta orodja definirate in jih posredujete `Agent Executorju`.

Vidnost je še en pomemben vidik pri razpravi o AI agentih. Pomembno je, da razvijalci aplikacij razumejo, katero orodje LLM uporablja in zakaj. Za to je ekipa LangChain razvila LangSmith.

## AutoGen

Naslednji okvir za AI agente, o katerem bomo govorili, je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Glavni fokus AutoGen-a so pogovori. Agenti so tako **pogovorljivi** kot tudi **prilagodljivi**.

**Pogovorljivi -** LLM-ji lahko začnejo in nadaljujejo pogovor z drugim LLM, da dokončajo nalogo. To se izvaja s ustvarjanjem `AssistantAgents` in dajanjem specifičnega sistemskega sporočila.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prilagodljivi** - Agente ni mogoče definirati samo kot LLM, ampak lahko predstavijo tudi uporabnika ali orodje. Kot razvijalec lahko definirate `UserProxyAgent`, ki je odgovoren za interakcijo z uporabnikom za povratne informacije pri dokončanju naloge. Te povratne informacije lahko nadaljujejo izvajanje naloge ali jo ustavijo.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stanje in Orodja

Za spreminjanje in upravljanje stanja pomočnik agent generira Python kodo za dokončanje naloge.

Tukaj je primer procesa:

![AutoGen](../../../translated_images/sl/autogen.dee9a25a45fde584.webp)

#### LLM definiran s sistemskim sporočilom

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

To sistemsko sporočilo usmerja določen LLM, katere funkcije so pomembne za njegovo nalogo. Zapomnite si, da lahko z AutoGen imate več definiranih AssistantAgentov z različnimi sistemskimi sporočili.

#### Pogovor sproži uporabnik

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

To sporočilo od user_proxy (človeka) bo sprožilo postopek, da agent raziskuje možne funkcije, ki bi jih moral izvesti.

#### Funkcija se izvede

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Ko je začetni pogovor obdelan, bo agent poslal predlagano orodje za klic. V tem primeru je to funkcija z imenom `get_weather`. Glede na vašo konfiguracijo se ta funkcija lahko samodejno izvede in jo agent prebere ali se izvede na podlagi uporabnikovega vnosa.

Našli boste seznam [primerov kode AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), da še naprej raziskujete, kako začeti z gradnjo.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je odprtokodni SDK podjetja Microsoft za gradnjo AI agentov in večagentnih sistemov tako v **Pythonu** kot v **.NET**. Združuje prednosti dveh prejšnjih Microsoftovih projektov — enterprise funkcionalnosti **Semantic Kernel** in večagentno orkestracijo **AutoGen** — v en sam, podprti okvir. Če danes začenjate nov projekt agenata, je to priporočeni naslednik AutoGen.

Okvir se prilagaja od enega **chat agenta** do kompleksnih **večagentnih delovnih tokov** in se neposredno povezuje z Microsoft Foundry, Azure OpenAI in OpenAI. Prav tako nudi vgrajeno opazovalnost prek OpenTelemetry, tako da lahko natančno sledite, kaj vaši agenti počnejo.

### Stanje in Orodja

**Stanje** - Okvir vam upravlja kontekst pogovora skozi **nitke**. Agent spremlja zgodovino sporočil (zahteve uporabnika, klice orodij in njihove rezultate), tako da se vsak korak gradi na prejšnjih. Nitke je mogoče tudi trajno shranjevati, kar omogoča, da se pogovor začasno ustavi in nadaljuje pozneje.

**Orodja** - Agentu daste orodja tako, da posredujete preproste Python funkcije. Parametri z anotacijami tipov se samodejno pretvorijo v shemo, zato model ve, kako in kdaj jih poklicati (funkcijsko klicanje). Okvir prav tako podpira strežnike Model Context Protocol (MCP) in gostovana orodja, kot je tolmač kode.

Tukaj je primer enega agenta s prilagojenim orodjem:

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

Za povezavo z Azure OpenAI v Microsoft Foundry namesto tega posredujte svoj konec in poverilnice odjemalcu:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Večagentni delovni tokovi

Okvir se zares izkaže pri orkestraciji več agentov skupaj. Na primer, lahko zaženete agente enega za drugim (pri čemer vsak posreduje svoj kontekst naslednjemu) ali jih usmerjate do več agentov vzporedno in združujete njihove rezultate:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Zaženi agente zaporedno, pri čemer se kontekst pogovora prenaša skozi verigo
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Razširi nalogo na agente vzporedno, nato združi njihove odgovore
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Za namestitev okvira in začetek:

```bash
pip install agent-framework-core
# Neobvezne integracije
pip install agent-framework-openai       # OpenAI in Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Več si lahko ogledate v [Microsoft Agent Framework repozitoriju](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) in v [uradni dokumentaciji](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Naslednji okvir za agente, ki ga bomo raziskovali, je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Poznan je kot "code-first" agent, saj namesto dela izključno z `nizi` lahko dela s podatkovnimi okvirji (DataFrames) v Pythonu. To je izredno koristno za naloge analize podatkov in generiranja. To so lahko stvari, kot so ustvarjanje grafov in diagramov ali generiranje naključnih števil.

### Stanje in Orodja

Za upravljanje stanja pogovora TaskWeaver uporablja koncept `Planner` (načrtovalca). `Planner` je LLM, ki sprejme zahtevo uporabnika in načrtuje naloge, ki jih je treba izpolniti, da se zahteva uresniči.

Da dokonča naloge, je `Planner` izpostavljen zbirki orodij, imenovani `Plugins`. To so lahko Python razredi ali splošni tolmač kode. Ti vtičniki so shranjeni kot vstavki (embeddings), da lahko LLM bolje išče pravi vtičnik.

![Taskweaver](../../../translated_images/sl/taskweaver.da8559999267715a.webp)

Tukaj je primer vtičnika za obravnavo odkrivanja anomalij:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koda je preverjena pred izvajanjem. Še ena funkcija za upravljanje konteksta v Taskweaver je `experience` (izkušnja). Izkušnja omogoča, da se kontekst pogovora shrani za daljše obdobje v datoteko YAML. To je mogoče konfigurirati tako, da se LLM skozi čas izboljšuje pri določenih nalogah, če ima dostop do preteklih pogovorov.

## JARVIS

Zadnji okvir za agente, ki ga bomo raziskovali, je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Posebnost JARVIS-a je, da uporablja LLM za upravljanje `stanja` pogovora, medtem ko so `orodja` drugi modeli AI. Vsak od AI modelov je specializiran model, ki izvaja določene naloge, kot so zaznavanje predmetov, prepisovanje ali opisovanje slik.

![JARVIS](../../../translated_images/sl/jarvis.762ddbadbd1a3a33.webp)

LLM, kot model splošnega namena, prejme zahtevo uporabnika in določi specifično nalogo ter kakršnekoli argumente/podatke, potrebne za dokončanje naloge.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM nato oblikuje zahtevo na način, ki ga specializirani AI model lahko interpretira, na primer kot JSON. Ko AI model vrne svojo napoved glede na nalogo, LLM prejme odgovor.

Če je za dokončanje naloge potrebnih več modelov, bo tudi interpretiral odzive od teh modelov, preden jih združi za generiranje odgovora uporabniku.

Primer spodaj prikazuje, kako bi to delovalo, ko uporabnik zahteva opis in štetje predmetov na sliki:

## Domača naloga

Za nadaljevanje učenja o AI agentih lahko ustvarite z Microsoft Agent Framework:

- Aplikacijo, ki simulira poslovni sestanek z različnimi oddelki izobraževalnega zagonskega podjetja.
- Ustvarite sistemska sporočila, ki vodijo LLM-je pri razumevanju različnih osebnosti in prioritet ter omogočajo uporabniku predstavitev nove ideje izdelka.
- LLM naj nato generira nadaljnja vprašanja iz vsakega oddelka, da izboljša predstavitev in idejo izdelka.

## Učenje tukaj se ne konča, nadaljujte pot

Po končani tej lekciji si oglejte našo [Zbirko za učenje generativne umetne inteligence](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->