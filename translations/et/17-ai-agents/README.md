[![Avatud lähtekoodiga mudelid](../../../translated_images/et/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Sissejuhatus

Tehisintellekti agendid on põnev areng Generatiivse tehisintellekti vallas, võimaldades suurte keelemudelite (LLM) areneda assistentidest agentideks, kes suudavad tegutseda. AI agentide raamistikud võimaldavad arendajatel luua rakendusi, mis annavad LLM-idele juurdepääsu tööriistadele ja seisundi haldamisele. Need raamistikud suurendavad ka nähtavust, võimaldades kasutajatel ja arendajatel jälgida LLM-ide kavandatud toiminguid, parandades sellega kasutuskogemust.

Õppetund katab järgmisi teemasid:

- Arusaamine, mis on tehisintellekti agent – mis täpselt on AI agent?
- Viie erineva AI agentide raamistikuga tutvumine – mis teeb need unikaalseks?
- Nende AI agentide rakendamine erinevates kasutusjuhtudes – millal kasutada AI agente?

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad:

- Selgitada, mis on AI agendid ja kuidas neid saab kasutada.
- Mõista mõnede populaarsete AI agentide raamistikude erinevusi ja kuidas need erinevad.
- Mõista, kuidas AI agendid toimivad, et nendega rakendusi ehitada.

## Mis on AI agendid?

AI agendid on väga põnev valdkond generatiivse tehisintellekti maailmas. Selle põnevusega kaasneb mõnikord terminite ja nende rakenduse segadus. Selleks, et hoida asjad lihtsad ja kaasata enamik tööriistu, mis viitavad AI agentidele, kasutame järgmist määratlust:

AI agentide abil saavad suured keelemudelid (LLM-id) täita ülesandeid, andes neile juurdepääsu **seisundile** ja **tööriistadele**.

![Agendi mudel](../../../translated_images/et/what-agent.21f2893bdfd01e6a.webp)

Selgitame neid termineid:

**Suured keelemudelid** – need on selles kursuses mainitud mudelid nagu GPT-5, GPT-4o ja Llama 3.3 jne.

**Seisund** – see tähendab konteksti, milles LLM töötab. LLM kasutab oma varasemate toimingute ja praeguse konteksti infot, juhendades oma otsuseid edasiste toimingute osas. AI agentide raamistikud võimaldavad arendajatel seda konteksti lihtsamalt hallata.

**Tööriistad** – et täita kasutaja soovitud ja LLM-i kavandatud ülesandeid, vajab LLM juurdepääsu tööriistadele. Näiteks võib tööriist olla andmebaas, API, väline rakendus või isegi teine LLM!

Need määratlused annavad hopefully sulle hea aluse, kui vaatleme, kuidas neid rakendatakse. Uurime mõningaid erinevaid AI agentide raamistikke:

## LangChaini agendid

[LangChaini agendid](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) on ülaltoodud määratluste rakendus.

**Seisundi** haldamiseks kasutatakse sisseehitatud funktsiooni nimega `AgentExecutor`. See aktsepteerib määratletud `agent`i ja talle kättesaadavaid `tööriistu`.

`AgentExecutor` salvestab ka vestluse ajaloo, et pakkuda vestluse konteksti.

![Langchaini agendid](../../../translated_images/et/langchain-agents.edcc55b5d5c43716.webp)

LangChain pakub [tööriistade kataloogi](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), mida saab sinu rakendusse importida ja millele LLM pääseb ligi. Need on loodud kogukonna ja LangChaini meeskonna poolt.

Seejärel saad need tööriistad määratleda ja edastada `AgentExecutor`ile.

Nähtavus on teine oluline aspekt AI agentide juures. Rakenduste arendajatel on oluline mõista, millist tööriista LLM kasutab ja miks. Selleks on LangChaini meeskond arendanud LangSmithi.

## AutoGen

Järgmine AI agentide raamistik, mida arutame, on [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGeni peamine fookus on vestlustel. Agendid on nii **vestlusvõimelised** kui ka **kohandatavad**.

**Vestlusvõimeline** – LLM-id saavad alustada ja jätkata vestlust teise LLM-iga ülesande täitmiseks. Seda tehakse luues `AssistantAgents` ja andes neile konkreetse süsteemse sõnumi.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Kohandatav** – agendid ei pea olema määratletud ainult LLM-idena, vaid võivad olla kasutaja või tööriista rollis. Arendajana saad määratleda `UserProxyAgent`i, kes vastutab kasutajaga tagasiside saamise eest ülesande täitmisel. See tagasiside võib kas jätkata ülesande täitmist või selle peatada.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Seisund ja tööriistad

Seisundi muutmiseks ja haldamiseks loob assistendi agent Python-koodi ülesande täitmiseks.

Näide protsessist:

![AutoGen](../../../translated_images/et/autogen.dee9a25a45fde584.webp)

#### LLM määratletud süsteemisõnumiga

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

See süsteemisõnum juhendab seda konkreetset LLM-i, millised funktsioonid on tema ülesande jaoks asjakohased. Pidage meeles, et AutoGeni puhul võid sul olla mitu erineva süsteemisõnumiga AssistantAgenti.

#### Vestlus algab kasutajast

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

See sõnum kasutajaproduks (inimene) käivitab agenti protsessi uurida võimalikke funktsioone, mida ta peaks täitma.

#### Funktsioon täidetakse

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kui algne vestlus on töödeldud, annab agent edasi soovitatud tööriista kutsumiseks. Selleks on funktsioon nimega `get_weather`. Sõltuvalt konfiguratsioonist võib see funktsioon automaatselt täidetud saada ja agent seda lugeda või siis täidetakse see kasutaja sisendi põhjal.

Leidke [AutoGen'i koodinäidiste loend](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst), et rohkem uurida, kuidas ehitusega alustada.

## Microsofti agentide raamistik

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) on Microsofti avatud lähtekoodiga SDK AI agentide ja mitme agendi süsteemide loomiseks nii **Pythonis** kui ka **.NET-is**. See ühendab kahte varasemat Microsofti projekti – ettevõtte tasemel funktsioonid **Semantic Kernelis** ja mitme agendi orkestreerimise **AutoGenis** – üheks toetatud raamistikuks. Kui alustad täna uut agendi projekti, on see soovitatav AutoGeni järglane.

Raamistik skaleerub ühest **vestlusagentist** kuni keerukate **mitme agendi töövoogudeni** ning integreerub otse Microsoft Foundry, Azure OpenAI ja OpenAI-ga. Samuti pakub sisseehitatud jälgitavust OpenTelemetry vahendusel, et saaks täpselt jälgida, mida su agendid teevad.

### Seisund ja tööriistad

**Seisund** – raamistik haldab vestluse konteksti sinu eest läbi **teemade**. Agent hoiab meeles sõnumite ajalugu (kasutaja päringud, tööriistakutsed ja nende tulemused), nii et iga käik tugineb eelmistele. Teemad võivad olla salvestatud, võimaldades vestlust peatada ja hiljem jätkata.

**Tööriistad** – annad agendile tööriistad, edastades tavalisi Pythoni funktsioone. Tüübiga märgistatud parameetrid konverteeritakse automaatselt skeemiks, nii et mudel teab, kuidas ja millal neid kutsuda (funktsioonikutsed). Raamistik toetab ka Model Context Protocol (MCP) servereid ja hostitud tööriistu nagu kooditõlgendaja.

Näide ühest agendist kohandatud tööriistaga:

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

Microsoft Foundrys Azure OpenAI-le ühendamiseks edasta oma lõpp-punkt ja volitused kliendile:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Mitme agendi töövood

Raamistik tõuseb eriti esile mitme agendi orkestreerimisel. Näiteks saab agente käivitada järjestikku (kõige konteksti edastades järgmisele) või paralleelselt mitmeid agente ja nende tulemused koondada:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Käivita agendid järjest, edastades vestluse konteksti mööda ahelat
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Laienda agendid paralleelselt, seejärel koonda nende vastused kokku
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Raamistik paigaldamiseks ja alustamiseks:

```bash
pip install agent-framework-core
# Valikulised integratsioonid
pip install agent-framework-openai       # OpenAI ja Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Saad rohkem avastada [Microsoft Agent Frameworki hoidlas](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ja [ametlikus dokumentatsioonis](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Järgmine uuritav agentide raamistik on [TaskWeaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Seda tuntakse kui "koodile orienteeritud" agenti, sest ta ei tööta vaid sõnstringidega, vaid võib töötada ka DataFrame’idega Pythonis. See on eriti kasulik andmeanalüüsi ja genereerimise ülesannete jaoks. Näiteks graafikute ja diagrammide loomine või juhuslike arvude genereerimine.

### Seisund ja tööriistad

Vestluse seisundi haldamiseks kasutab TaskWeaver mõistet `Planner`. `Planner` on LLM, mis võtab kasutajate päringu ja koostab ülesannete kaardi nende täitmiseks.

Ülesannete täitmiseks on `Planner`il juurdepääs tööriistade kogule nimega `Plugins`. Need võivad olla Python class’id või üldised kooditõlgendajad. Need pluginad salvestatakse embeddings’i kujul, et LLM saaks paremini õige plugina üles leida.

![Taskweaver](../../../translated_images/et/taskweaver.da8559999267715a.webp)

Näide plugina kohta anomaaliate tuvastamiseks:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kood kontrollitakse enne täitmist. Teine TaskWeaver’i konteksti haldamise funktsioon on `experience`. Experience võimaldab vestluse konteksti pikaajaliselt YAML-faili salvestada. Seda saab seadistada nii, et LLM paraneb aja jooksul teatud ülesannetes, kuna ta puutub kokku varasemate vestlustega.

## JARVIS

Viimane uuritav agentide raamistik on [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVISi unikaalsus seisneb selles, et see kasutab LLM-i vestluse `seisundi` haldamiseks ning `tööriistadeks` on teiste AI mudelite rühm. Iga AI mudel on spetsialiseerunud ülesannetele nagu objektituvastus, transkriptsioon või piltide kirjeldamine.

![JARVIS](../../../translated_images/et/jarvis.762ddbadbd1a3a33.webp)

Üldotstarbeline LLM võtab kasutajalt päringu ja tuvastab konkreetse ülesande ning kõik argumendid/andmed, mis ülesande täitmiseks vajalikud on.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM vormindab seejärel päringu kujul, mida spetsialiseerunud AI mudel suudab tõlgendada, näiteks JSON. Kui AI mudel on ülesande alusel oma ennustuse tagastanud, saab LLM vastuse.

Kui ülesande täitmiseks on vaja mitut mudelit, tõlgendab LLM ka nende mudelite vastuseid enne, kui koondab need kasutajale edastamiseks.

Näide allpool näitab, kuidas see toimiks, kui kasutaja küsib pildi objektide kirjeldust ja loendust:

## Kodutöö

AI agentide õppimise jätkamiseks võid ehitada Microsoft Agent Frameworkiga:

- Rakenduse, mis simuleerib ärikoosolekut haridusstartup’i erinevate osakondade vahel.
- Loo süsteemisõnumid, mis juhivad LLM-e mõistma erinevaid isiksusi ja prioriteete ning võimaldavad kasutajal esitleda uut tootemõtet.
- Seejärel peaks LLM genereerima järelpärimisi igalt osakonnalt, et täpsustada ja parandada esitlust ja tooteideed.

## Õppimine siin ei lõpe, jätka teekonda

Pärast selle õppetunni lõpetamist vaata meie [Generatiivse Tehisintellekti õppimise kollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata generatiivse tehisintellekti teadlikkuse tõstmist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->