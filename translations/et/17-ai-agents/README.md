[![Avatud lähtekoodiga mudelid](../../../translated_images/et/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Sissejuhatus

Tehisintellekti agendid tähistavad põnevat arengut generatiivses tehisintellektis, võimaldades suurte keelemudelitel (LLMid) areneda assistentidest agentideks, kes suudavad tegutseda. AI agentide raamistikud võimaldavad arendajatel luua rakendusi, mis annavad LLM-idele ligipääsu tööriistadele ja oleku haldamisele. Need raamistikud suurendavad ka nähtavust, võimaldades kasutajatel ja arendajatel jälgida LLM-ide kavandatud tegevusi, parandades sellega kasutajakogemuse haldamist.

Õppetund hõlmab järgmisi valdkondi:

- AI agendi mõistmine – mis täpselt on AI agent?
- Viie erineva AI agendi raamistikuga tutvumine – mis teeb need ainulaadseks?
- Nende AI agentide rakendamine erinevates kasutusjuhtudes – millal peaksime kasutama AI agente?

## Õpieesmärgid

Pärast selle õppetunni läbimist suudad:

- Selgitada, mis on AI agendid ja kuidas neid saab kasutada.
- Mõista mõningate populaarsete AI agentide raamistikude erinevusi ja nende omapära.
- Mõista, kuidas AI agendid toimivad, et nendega rakendusi ehitada.

## Mis on AI Agendid?

AI agendid on väga põnev valdkond generatiivse tehisintellekti maailmas. Selle põnevusega kaasneb mõnikord terminite ja nende rakenduste segadus. Lihtsuse ja enamikule AI agenditele viitavate tööriistade kaasamiseks kasutame järgmist definitsiooni:

AI agendid võimaldavad suurte keelemudelite (LLM-idel) täita ülesandeid, andes neile ligipääsu **olekule** ja **tööriistadele**.

![Agent Model](../../../translated_images/et/what-agent.21f2893bdfd01e6a.webp)

Määratleme need terminid:

**Suured keelemudelid** – need on selle kursuse jooksul viidatud mudelid, nagu GPT-3.5, GPT-4, Llama-2 jpt.

**Olek** – See viitab kontekstile, milles LLM töötab. LLM kasutab oma varasemate tegevuste konteksti ja käesolevat konteksti, suunates oma otsuste tegemist järgmiste tegevuste puhul. AI agentide raamistikud võimaldavad arendajatel selle konteksti hõlpsamini hallata.

**Tööriistad** – Et täita kasutaja soovitud ülesannet ja mille LLM on planeerinud, vajab LLM ligipääsu tööriistadele. Mõned tööriistade näited võivad olla andmebaas, API, väline rakendus või isegi mõni teine LLM!

Need määratlused annavad sulle loodanavalt hea aluse edasi liikudes, kui vaatame neid rakendamas. Uurime mõningaid erinevaid AI agentide raamistikke:

## LangChaini agendid

[LangChaini agendid](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) on ülaltoodud määratluste rakendus.

**Olek** haldamiseks kasutatakse sisseehitatud funktsiooni nimega `AgentExecutor`. See aktsepteerib defineeritud `agenti` ja saadaval olevaid `tööriistu`.

`AgentExecutor` salvestab ka vestluse ajaloo, et pakkuda vestluse konteksti.

![Langchain Agents](../../../translated_images/et/langchain-agents.edcc55b5d5c43716.webp)

LangChain pakub [tööriistade kataloogi](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), mida saab sinu rakendusse importida, millele LLM saab ligipääsu. Need on loodud kogukonna ja LangChaini meeskonna poolt.

Saad need tööriistad defineerida ja need seejärel ette anda `AgentExecutor`-ile.

Nähtavus on teine oluline aspekt AI agentidest rääkides. Rakenduse arendajatel on oluline mõista, millist tööriista LLM kasutab ja miks. Selleks on LangChaini meeskond välja töötanud LangSmithi.

## AutoGen

Järgmine AI agentide raamistik, mida käsitleme, on [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGeni peamine fookus on vestlustel. Agendid on nii **vestlevad** kui ka **kohandatavad**.

**Vestlevad** – LLM-id saavad alustada ja jätkata vestlust teise LLM-iga, et ülesanne täita. Seda tehakse `AssistantAgents` loomisega ja neile konkreetse süsteemisõnumi andmisega.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Kohandatavad** – Agente saab defineerida mitte ainult LLM-idena, vaid ka kasutajana või tööriistana. Arendajana saad defineerida `UserProxyAgent`i, kes vastutab kasutajaga suhtlemise eest tagasiside saamiseks ülesande täitmisel. See tagasiside võib kas jätkata ülesande täitmist või selle peatada.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Olek ja tööriistad

Oleku muutmiseks ja haldamiseks genereerib assistent-agent Python-koodi ülesande täitmiseks.

Siin on protsessi näide:

![AutoGen](../../../translated_images/et/autogen.dee9a25a45fde584.webp)

#### LLM defineeritud süsteemisõnumiga

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

See süsteemisõnum juhib seda konkreetset LLM-i, millised funktsioonid on tema ülesande jaoks olulised. Pidage meeles, et AutoGeniga võid määratleda mitu erineva süsteemisõnumiga AssistantAgenti.

#### Vestlus algatatakse kasutaja poolt

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

See sõnum user_proxy (inimene) poolt alustab agendi protsessi uurida, milliseid funktsioone võiks käivitada.

#### Funktsioon täidetakse

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kui algse vestluse töötlemine lõpeb, saadab agent soovitatud tööriista kutse. Antud juhul on see funktsioon nimega `get_weather`. Sõltuvalt sinu seadistusest saab seda funktsiooni automaatselt täita ja lugeda agendi poolt või täita kasutaja sisendi põhjal.

Saad [AutoGeni koodi näidiseid](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) uurida, et õppida ehitamisega alustamist.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) on Microsofti avatud lähtekoodiga SDK AI agentide ja mitmeagendi süsteemide loomiseks nii **Pythonis** kui **.NETis**. See ühendab kahe varasema Microsofti projekti tugevused — ettevõtete funktsioonid **Semantic Kernel**-ist ja mitmeagendi orkestreerimise **AutoGen**-ist — üheks toetatud raamistikuks. Kui alustad täna uut agendiprojekti, on see AutoGeni soovitatud asendus.

Raamistik skaleerub ühest **vestlusagendist** kuni keerukate **mitmeagendi töövoodeni**, ning see integreerub otse Microsoft Foundry, Azure OpenAI ja OpenAI-ga. See pakub ka sisseehitatud jälgitavust OpenTelemetry kaudu, et saaksid täpselt jälgida, mida su agendid teevad.

### Olek ja tööriistad

**Olek** – raamistik haldab vestluse konteksti sinu eest **liinide** kaudu. Agent jälgib sõnumite ajalugu (kasutaja päringud, tööriistakutsed ja nende tulemused), nii et iga käik loob aluse eelnevatele. Liine saab salvestada, võimaldades vestlust peatada ja hiljem jätkata.

**Tööriistad** – Sa annad agendile tööriistad, edastades tavalisi Pythoni funktsioone. Tüübimärgistusega parameetrid teisendatakse automaatselt skeemiks, nii et mudel teab, kuidas ja millal neid kutsuda (funktsioonikutsed). Raamistik toetab ka Model Context Protocol (MCP) servereid ja hostitud tööriistu, näiteks kooditõlgendajat.

Siin on näide ühest agendist kohandatud tööriistaga:

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

Microsoft Foundry-s Azure OpenAI-iga ühenduse loomiseks edasta kliendile oma endpoint ja mandaadid:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Mitmeagendi töövood

Raamistik silma paistab eriti mitme agendi koos orkestrimisel. Näiteks võid käivitada agente ükshaaval (igaüks annab üle oma konteksti järgmisele) või vallata mitme agendi peale paralleelselt ja koguda nende tulemusi:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Käivitage agendid järjestikku, edastades vestluse konteksti koos kettaga
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Jaotage agendid paralleelselt, seejärel koguge nende vastused kokku
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Raamistik paigaldamiseks ja alustamiseks:

```bash
pip install agent-framework-core
# Valikulised integratsioonid
pip install agent-framework-openai       # OpenAI ja Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Rohkem saad uurida [Microsoft Agent Frameworki hoidlas](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ja [ametlikus dokumentatsioonis](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Järgmine agentide raamistik, mida uurime, on [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Seda tuntakse kui "koodi-esimene" agenti, sest ta ei kasuta rangelt `strings`, vaid suudab töötada Pythonis DataFrame’idega. See muutub äärmiselt kasulikuks andmeanalüüsi ja genereerimistööde jaoks, nagu graafikute ja diagrammide loomine või juhuslike arvude genereerimine.

### Olek ja tööriistad

Vestluse oleku haldamiseks kasutab TaskWeaver `Planner`i kontseptsiooni. `Planner` on LLM, mis võtab kasutajate päringu ja kaardistab ülesanded, mis tuleb selle päringu täitmiseks lõpule viia.

Ülesannete täitmiseks on `Planner`il ligipääs tööriistade kogule nimega `Plugins`. Need võivad olla Python klassid või üldine kooditõlk. Need pluginad salvestatakse embed’itena, et LLM saaks paremini leida õiget pluginat.

![Taskweaver](../../../translated_images/et/taskweaver.da8559999267715a.webp)

Näide ainult lisandmoodulist anomaaliate tuvastamiseks:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kood kontrollitakse enne täitmist üle. Teine Taskweaveri konteksti haldamise funktsioon on `experience`. Experience võimaldab vestluse konteksti pikemas perspektiivis YAML-faili salvestada. See saab olla seadistatav nii, et LLM paraneb aja jooksul teatud ülesannetes, kui ta on varasematele vestlustele ligipääsuga.

## JARVIS

Viimane agentide raamistik, mida uurime, on [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVISi unuikaalsus seisneb selles, et ta kasutab LLM-i vestluse `oleku` haldamiseks ja `tööriistad` on teised AI mudelid. Iga AI mudel on spetsialiseerunud konkreetsele ülesandele, nagu objektide tuvastamine, transkriptsioon või pildikirjeldus.

![JARVIS](../../../translated_images/et/jarvis.762ddbadbd1a3a33.webp)

LLM, olles üldotstarbeline mudel, võtab vastu kasutaja päringu, tuvastab konkreetse ülesande ja kõik argumendid/andmed, mis on ülesande täitmiseks vajalikud.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Seejärel vormindab LLM päringu selliselt, et spetsialiseeritud AI mudel seda mõistaks, näiteks JSON-vormingus. Kui AI mudel on ülesande põhjal oma prognoosi tagastanud, saab sellest vastuse LLM.

Kui ülesande täitmiseks on vajalik mitu mudelit, tõlgib LLM ka nende mudelite vastused, enne kui toob need kokku ja genereerib vastuse kasutajale.

Järgmine näide näitab, kuidas see toimiks, kui kasutaja soovib kirjeldust ja objektide arvu pildil:

## Ülesanne

AI agentide õppimise jätkamiseks võid luua Microsoft Agent Frameworkiga:

- Rakendus, mis simuleerib ärikoosolekut haridusstartup’i erinevate osakondade vahel.
- Loo süsteemisõnumeid, mis juhendavad LLM-e erinevate isiksuste ja prioriteetide mõistmisel ning võimaldavad kasutajal esitada uue tooteidee.
- LLM peaks seejärel genereerima iga osakonna poolt järgnevaid küsimusi, et täiustada ja parandada pakkumist ja tooteideed.

## Õppimine siin ei peatu, jätka teekonda

Pärast selle õppetunni lõpetamist vaata meie [Generatiivse AI õppimiskogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse AI teadmiste arendamist!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->