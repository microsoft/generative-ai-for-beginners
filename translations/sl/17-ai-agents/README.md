[![Open Source Models](../../../translated_images/sl/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Uvod

AI agenti predstavljajo razburljiv razvoj v Generativni umetni inteligenci, saj omogočajo, da se veliki jezikovni modeli (LLM) razvijejo iz pomočnikov v agente, sposobne izvajati dejanja. Okviri za AI agente razvijalcem omogočajo ustvarjanje aplikacij, ki LLM-jem omogočajo dostop do orodij in upravljanje stanja. Ti okviri prav tako povečujejo preglednost, kar uporabnikom in razvijalcem omogoča spremljanje dejanj, ki jih LLM-ji načrtujejo, s čimer izboljšujejo upravljanje uporabniške izkušnje.

Lekcija bo zajela naslednja področja:

- Razumevanje, kaj je AI agent - Kaj natanko je AI agent?
- Raziščite pet različnih okvirov za AI agente - Kaj jih naredi edinstvene?
- Uporaba teh AI agentov v različnih primerih uporabe - Kdaj naj uporabimo AI agente?

## Cilji učenja

Po zaključeni lekciji boste znali:

- Razložiti, kaj so AI agenti in kako jih lahko uporabimo.
- Razumeti razlike med nekaterimi priljubljenimi okviri za AI agente in kako se razlikujejo.
- Razumeti, kako AI agenti delujejo, da bi lahko z njimi gradili aplikacije.

## Kaj so AI agenti?

AI agenti so zelo razburljivo področje v svetu Generativne umetne inteligence. S tem navdušenjem pride tudi včasih zmeda glede izrazov in njihove uporabe. Da ostanemo preprosti in vključujoči glede večine orodij, ki se nanašajo na AI agente, bomo uporabili to definicijo:

AI agenti omogočajo velikim jezikovnim modelom (LLM), da opravljajo naloge z omogočanjem dostopa do **stanja** in **orodij**.

![Agent Model](../../../translated_images/sl/what-agent.21f2893bdfd01e6a.webp)

Določimo te izraze:

**Veliki jezikovni modeli** - To so modeli, ki jih omenjamo skozi ta tečaj, kot so GPT-3.5, GPT-4, Llama-2 itd.

**Stanje** - Nanaša se na kontekst, v katerem LLM deluje. LLM uporablja kontekst svojih preteklih dejanj in trenutni kontekst, ki usmerja njegovo odločanje za prihodnja dejanja. Okviri za AI agente razvijalcem olajšajo vzdrževanje tega konteksta.

**Orodja** - Da bi LLM lahko izvedel nalogo, ki jo je uporabnik zahteval in ki jo je LLM načrtoval, potrebuje dostop do orodij. Nekateri primeri orodij so podatkovna baza, API, zunanja aplikacija ali celo drug LLM!

Te definicije vam bodo upamo dali dobro osnovo za nadaljnje razumevanje njihove implementacije. Raziščimo nekaj različnih okvirov za AI agente:

## LangChain agenti

[LangChain agenti](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) so implementacija zgornjih definicij.

Za upravljanje **stanja** uporablja vgrajeno funkcijo, imenovano `AgentExecutor`. Ta sprejme definiran `agent` in `orodja`, ki so mu na voljo.

`AgentExecutor` prav tako shrani zgodovino pogovora, da zagotovi kontekst pogovora.

![Langchain Agents](../../../translated_images/sl/langchain-agents.edcc55b5d5c43716.webp)

LangChain ponuja [katalog orodij](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), ki ga lahko uvozite v svojo aplikacijo, do katerih ima LLM dostop. Ta orodja ustvarjajo skupnost in ekipa LangChain.

Nato lahko ta orodja definirate in jih podate `AgentExecutor`.

Preglednost je še en pomemben vidik pri pogovoru o AI agentih. Pomembno je, da razvijalci aplikacij razumejo, katero orodje LLM uporablja in zakaj. Zaradi tega je ekipa LangChain razvila LangSmith.

## AutoGen

Naslednji okvir za AI agente, o katerem bomo govorili, je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Glavni poudarek AutoGen je na pogovorih. Agentje so tako **pogovarljivi** kot **prilagodljivi**.

**Pogovarljivi -** LLM-ji lahko začnejo in nadaljujejo pogovor z drugim LLM-jem, da dokončajo nalogo. To se izvaja z ustvarjanjem `AssistantAgents` in dodeljevanjem specifičnega sistemskega sporočila.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prilagodljivi** - Agente ni mogoče definirati samo kot LLM-je, ampak so lahko tudi uporabnik ali orodje. Kot razvijalec lahko definirate `UserProxyAgent`, ki odgovarja za interakcijo z uporabnikom za povratne informacije pri opravljanju naloge. Te povratne informacije lahko nadaljujejo izvajanje naloge ali pa jo ustavijo.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stanje in orodja

Za spremembo in upravljanje stanja asistent agent generira Python kodo za dokončanje naloge.

Tukaj je primer procesa:

![AutoGen](../../../translated_images/sl/autogen.dee9a25a45fde584.webp)

#### LLM definiran s sistemskim sporočilom

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

To sistemsko sporočilo usmerja ta specifični LLM, katera funkcija je relevantna za njegovo nalogo. Zapomnite si, da lahko pri AutoGen imate več definiranih AssistantAgentov z različnimi sistemskimi sporočili.

#### Pogovor začne uporabnik

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

To sporočilo od user_proxy (človek) bo začelo postopek, da agent razišče možne funkcije, ki jih mora izvesti.

#### Funkcija se izvede

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Ko je začetni pogovor obdelan, agent pošlje predlagano orodje za klic. V tem primeru je to funkcija `get_weather`. Glede na vašo konfiguracijo se ta funkcija lahko samodejno izvede in prebere s strani agenta ali pa se izvede na podlagi uporabnikovega vnosa.

Najdete lahko seznam [AutoGen kodnih primerov](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) za nadaljnje raziskovanje, kako začeti graditi.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je Microsoftov odprtokodni SDK za gradnjo AI agentov in sistemov z več agenti v **Python** in **.NET**. Združuje prednosti dveh prejšnjih Microsoftovih projektov — podjetniške funkcije **Semantic Kernel** in večagentno orkestracijo **AutoGen** — v en enoten, podprt okvir. Če danes začenjate nov projekt agenta, je to priporočeni naslednik AutoGen.

Okvir se razteza od enega samega **pogovornega agenta** do zapletenih **večagentnih delovnih tokov** in se neposredno povezuje z Microsoft Foundry, Azure OpenAI in OpenAI. Prav tako zagotavlja vgrajeno opazovanje prek OpenTelemetry, da lahko sledite natanko, kaj vaši agenti počnejo.

### Stanje in orodja

**Stanje** - Okvir vam upravlja kontekst pogovora s pomočjo **nitk**. Agent beleži zgodovino sporočil (zahteve uporabnika, klice orodij in njihove rezultate), tako da se vsak krog gradi na prejšnjih. Nitke je možno tudi trajno shraniti, kar omogoča premor in nadaljevanje pogovora pozneje.

**Orodja** - Agentu daste orodja z omogočanjem preprostih Python funkcij. Parametri z oznakami tipov se samodejno pretvorijo v shemo, zato model ve, kako in kdaj jih poklicati (klic funkcije). Okvir podpira tudi strežnike Model Context Protocol (MCP) in gostovana orodja, kot je interpretator kode.

Tukaj je primer enega agenta z lastnim orodjem:

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

Da se namesto tega povežete z Azure OpenAI v Microsoft Foundry, podajte končno točko in poverilnice klientu:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Večagentni delovni tokovi

Prava posebnost okvirja je orkestracija več agentov skupaj. Na primer, lahko zaženete agente enega za drugim (pri čemer vsak preda svoj kontekst naslednjemu) ali se razvežite na več agentov vzporedno in združite njihove rezultate:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Zaženi agente zaporedno, pri čemer se kontekst pogovora prenese po verigi
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Razdeli naprej na agente vzporedno, nato združi njihove odgovore
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Za namestitev okvirja in začetek:

```bash
pip install agent-framework-core
# Neobvezne integracije
pip install agent-framework-openai       # OpenAI in Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Več si lahko ogledate v [Microsoft Agent Framework repozitoriju](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) in [uradni dokumentaciji](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Naslednji okvir za agente, ki ga bomo raziskali, je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Znamenit je kot "kode-first" agent, ker namesto strogega dela z `nizi` lahko dela s podatkovnimi okviri (DataFrames) v Pythonu. To postane izredno uporabno za naloge analize podatkov in generiranja. Lahko gre za stvari, kot so ustvarjanje grafov in diagramov ali generiranje naključnih števil.

### Stanje in orodja

Za upravljanje stanja pogovora TaskWeaver uporablja koncept `Planerja`. `Planer` je LLM, ki sprejme zahtevo uporabnikov in načrtuje naloge, ki jih je treba dokončati za izpolnitev te zahteve.

Za dokončanje nalog je `Planer` izpostavljen zbirki orodij, imenovanih `Plugins`. To so lahko Python razredi ali splošni interpretator kode. Ti vtičniki so shranjeni kot vdelave (embeddings), da lahko LLM bolje išče pravilen vtičnik.

![Taskweaver](../../../translated_images/sl/taskweaver.da8559999267715a.webp)

Tukaj je primer vtičnika za zaznavanje anomalij:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koda je preverjena pred izvedbo. Še ena funkcija za upravljanje konteksta v Taskweaver je `experience`. Experience omogoča shranjevanje konteksta pogovora na dolgi rok v YAML datoteki. To je mogoče konfigurirati tako, da se LLM skozi čas izboljšuje pri določenih nalogah, saj ima dostop do prejšnjih pogovorov.

## JARVIS

Zadnji okvir za agente, ki ga bomo raziskali, je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Edinstvenost Jarvisa je v tem, da uporablja LLM za upravljanje `stanja` pogovora, medtem ko so `orodja` drugi AI modeli. Vsak od teh AI modelov je specializiran model, ki opravlja določene naloge, kot so zaznavanje objektov, prepisovanje ali opisovanje slik.

![JARVIS](../../../translated_images/sl/jarvis.762ddbadbd1a3a33.webp)

LLM, kot splošni model, prejme zahtevo uporabnika in določi specifično nalogo ter argumente/podatke, potrebne za dokončanje naloge.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM nato oblikuje zahtevo na način, ki ga specializirani AI model lahko interpretira, na primer v JSON formatu. Ko AI model vrne svojo napoved glede na nalogo, LLM prejme odgovor.

Če je za dokončanje naloge potrebnih več modelov, bo interpretiral odgovore teh modelov, preden jih združi za generiranje odgovora uporabniku.

Spodnji primer prikazuje, kako bi to delovalo, ko uporabnik zahteva opis in štetje objektov na sliki:

## Naloga

Za nadaljevanje vašega učenja o AI agentih lahko zgradite z Microsoft Agent Framework:

- Aplikacijo, ki simulira poslovni sestanek različnih oddelkov izobraževalnega zagonskega podjetja.
- Ustvarite sistemska sporočila, ki vodijo LLM-je pri razumevanju različnih osebnosti in prioritet ter uporabniku omogočijo predstavitev nove ideje za produkt.
- Nato naj LLM generira nadaljnja vprašanja iz vsakega oddelka za izboljšanje in izpilitev predstavitve in ideje za produkt.

## Učenje se tu ne konča, nadaljujte pot

Po zaključku te lekcije preverite našo [Zbirko za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z izpopolnjevanjem znanja o Generativni AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->