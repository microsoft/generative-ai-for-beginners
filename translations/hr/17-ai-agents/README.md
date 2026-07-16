[![Open Source Models](../../../translated_images/hr/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Uvod

AI agenti predstavljaju uzbudljiv razvoj u Generativnoj AI, omogućavajući Velikim jezičnim modelima (LLM) da se razviju iz asistenata u agente sposobne za poduzimanje radnji. Okviri za AI agente omogućuju programerima stvaranje aplikacija koje daju LLM-ovima pristup alatima i upravljanju stanjem. Ti okviri također poboljšavaju vidljivost, dopuštajući korisnicima i programerima da prate radnje koje LLM planira, čime se poboljšava upravljanje iskustvom.

Lekcija će obuhvatiti sljedeća područja:

- Razumijevanje što je AI agent - Što točno znači AI agent?
- Istraživanje pet različitih okvira za AI agente - Što ih čini jedinstvenima?
- Primjena ovih AI agenata na različite slučajeve upotrebe - Kada bismo trebali koristiti AI agente?

## Ciljevi učenja

Nakon ove lekcije, moći ćete:

- Objasniti što su AI agenti i kako se mogu koristiti.
- Razumjeti razlike između nekih popularnih okvira za AI agente i kako se razlikuju.
- Razumjeti kako AI agenti funkcioniraju kako biste mogli graditi aplikacije s njima.

## Što su AI Agenti?

AI agenti su vrlo uzbudljivo područje u svijetu Generativne AI. Sa ovim uzbuđenjem ponekad dolazi i do zbunjenosti u terminima i njihovoj primjeni. Kako bismo stvari pojednostavili i uključili većinu alata koji se odnose na AI agente, koristit ćemo ovu definiciju:

AI agenti omogućuju Velikim jezičnim modelima (LLM) da izvršavaju zadatke tako što im daju pristup **stanju** i **alatima**.

![Agent Model](../../../translated_images/hr/what-agent.21f2893bdfd01e6a.webp)

Definirajmo ove pojmove:

**Veliki jezični modeli** - To su modeli na koje se poziva tijekom ovog tečaja, poput GPT-3.5, GPT-4, Llama-2 i slično.

**Stanje** - Odnosi se na kontekst u kojem LLM radi. LLM koristi kontekst svojih prethodnih radnji i trenutni kontekst kako bi usmjerio donošenje odluka za daljnje radnje. Okviri za AI agente olakšavaju programerima održavanje tog konteksta.

**Alati** - Za dovršetak zadatka koji je korisnik zatražio i koji je LLM isplanirao, LLM treba pristup alatima. Neki primjeri alata mogu biti baza podataka, API, vanjska aplikacija ili čak drugi LLM!

Ove definicije će vam, nadamo se, dati dobru osnovu za dalje dok ćemo gledati kako se implementiraju. Pogledajmo nekoliko različitih okvira za AI agente:

## LangChain Agenti

[LangChain Agenti](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) su implementacija gore navedenih definicija.

Za upravljanje **stanjima** koristi ugrađenu funkciju nazvanu `AgentExecutor`. Ona prihvaća definirani `agent` i `alate` koji su mu dostupni.

`Agent Executor` također pohranjuje povijest chata kako bi pružio kontekst razgovora.

![Langchain Agents](../../../translated_images/hr/langchain-agents.edcc55b5d5c43716.webp)

LangChain nudi [katalog alata](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) koji se mogu uvesti u vašu aplikaciju kojima LLM može pristupiti. Ti alati su izrađeni od strane zajednice i tima LangChaina.

Zatim možete definirati te alate i poslati ih `Agent Executor-u`.

Vidljivost je još jedan važan aspekt kada govorimo o AI agentima. Važno je da programeri aplikacija razumiju koji alat LLM koristi i zašto. Za to je tim LangChain razvio LangSmith.

## AutoGen

Sljedeći okvir za AI agente koji ćemo razmotriti je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Glavni fokus AutoGena su razgovori. Agenti su i **razgovorni** i **prilagodljivi**.

**Razgovorni -** LLM može započeti i nastaviti razgovor s drugim LLM-om kako bi dovršio zadatak. Ovo se radi stvaranjem `AssistantAgents` i davanjem im određene sistemske poruke.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prilagodljivi** - Agenti se mogu definirati ne samo kao LLM-ovi nego i kao korisnik ili alat. Kao programer, možete definirati `UserProxyAgent` koji je odgovoran za interakciju s korisnikom radi povratne informacije u izvršavanju zadatka. Ta povratna informacija može ili nastaviti izvršenje zadatka ili ga zaustaviti.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stanje i alati

Za promjenu i upravljanje stanjem, pomoćni agent generira Python kod za dovršavanje zadatka.

Evo primjera procesa:

![AutoGen](../../../translated_images/hr/autogen.dee9a25a45fde584.webp)

#### LLM definiran s sistemskom porukom

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ova sistemska poruka usmjerava ovaj specifični LLM na koje su funkcije relevantne za njegov zadatak. Zapamtite, kod AutoGena možete imati više definiranih AssistantAgents s različitim sistemskim porukama.

#### Razgovor pokreće korisnik

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ova poruka od user_proxyja (ljudske osobe) pokreće proces da agent istraži moguće funkcije koje treba izvršiti.

#### Funkcija se izvršava

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Nakon što se obradi početni razgovor, agent će poslati predloženi alat za poziv. U ovom slučaju, to je funkcija nazvana `get_weather`. Ovisno o vašoj konfiguraciji, ta se funkcija može automatski izvršiti i pročitati od strane agenta ili se može izvršiti na temelju korisničkog unosa.

Možete pronaći popis [AutoGen primjera koda](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) za dublje proučavanje kako započeti gradnju.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je Microsoftov open-source SDK za gradnju AI agenata i sustava s više agenata u **Python** i **.NET**. Spaja snage dvaju ranijih Microsoftovih projekata — enterprise značajke **Semantic Kernela** i orkestraciju više agenata **AutoGena** — u jedinstveni, podržani okvir. Ako danas započinjete novi projekt agenata, ovo je preporučeni nasljednik AutoGena.

Okvir se proteže od jednoga **chat agenta** do složenih **višestrukih tijekova rada agenata**, te se izravno integrira s Microsoft Foundry, Azure OpenAI i OpenAI. Također pruža ugrađenu vidljivost kroz OpenTelemetry tako da možete pratiti točno što vaši agenti rade.

### Stanje i alati

**Stanje** - Okvir upravlja kontekstom razgovora za vas kroz **niti**. Agent prati povijest poruka (zahtjeve korisnika, pozive alata i njihove rezultate), tako da svaki slijedeći korak nadograđuje prethodne. Niti se također mogu pohraniti, što omogućuje pauziranje i nastavak razgovora kasnije.

**Alati** - Davate agentu alate tako što mu prosljeđujete obične Python funkcije. Parametri s tipovima automatski se pretvaraju u shemu, tako da model zna kako i kada ih pozvati (pozivanje funkcija). Okvir također podržava Model Context Protocol (MCP) servere i ugrađene alate poput interpretatora koda.

Evo primjera jednog agenta s prilagođenim alatom:

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

Za povezivanje s Azure OpenAI u Microsoft Foundry umjesto toga, proslijedite svoj endpoint i vjerodajnice klijentu:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Tijekovi rada s više agenata

Okvir zaista dolazi do izražaja u orkestraciji nekoliko agenata zajedno. Na primjer, možete pokretati agente jedan za drugim (svaki prenoseći svoj kontekst na sljedećeg) ili ih paralelno rasporediti na nekoliko agenata i objediniti njihove rezultate:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Pokrenite agente uzastopno, prosljeđujući kontekst razgovora duž lanca
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Raspodijelite na agente paralelno, zatim objedinite njihove odgovore
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Za instalaciju okvira i početak rada:

```bash
pip install agent-framework-core
# Opcionalne integracije
pip install agent-framework-openai       # OpenAI i Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Više možete istražiti u [Microsoft Agent Framework spremištu](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) i [službenoj dokumentaciji](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Sljedeći okvir za agente koji ćemo istražiti je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Poznat je kao "code-first" agent jer, umjesto strogo rada s `stringovima`, može raditi s DataFrameovima u Pythonu. Ovo postaje iznimno korisno za zadatke analize i generiranja podataka. To mogu biti stvari poput izrade grafova i dijagrama ili generiranje nasumičnih brojeva.

### Stanje i alati

Za upravljanje stanjem razgovora, TaskWeaver koristi koncept `Plannera`. `Planner` je LLM koji prima zahtjev od korisnika i mapira zadatke koje treba dovršiti da bi se taj zahtjev ispunio.

Da bi dovršio zadatke, `Planner` je izložen zbirci alata nazvanih `Plugins`. To mogu biti Python klase ili opći interpretator koda. Ti plugini se pohranjuju kao ugnežđenja (embeddings) kako bi LLM bolje pretraživao ispravan plugin.

![Taskweaver](../../../translated_images/hr/taskweaver.da8559999267715a.webp)

Evo primjera plugina za otkrivanje anomalija:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod se provjerava prije izvršenja. Još jedna značajka za upravljanje kontekstom u Taskweaveru je `experience`. Experience omogućuje da se kontekst razgovora pohrani na dulje vrijeme u YAML datoteku. To se može konfigurirati tako da LLM s vremenom poboljšava određene zadatke, pod uvjetom da je izložen prethodnim razgovorima.

## JARVIS

Posljednji okvir za agente koji ćemo istražiti je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ono što JARVIS čini jedinstvenim jest da koristi LLM za upravljanje `stanjem` razgovora, a `alati` su drugi AI modeli. Svaki od AI modela su specijalizirani modeli koji obavljaju određene zadatke poput detekcije objekata, transkripcije ili pisanja opisa slika.

![JARVIS](../../../translated_images/hr/jarvis.762ddbadbd1a3a33.webp)

LLM, kao model opće namjene, prima zahtjev od korisnika i identificira specifični zadatak i bilo koje argumente/podatke potrebne za dovršetak zadatka.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM zatim formatira zahtjev na način koji specijalizirani AI model može interpretirati, poput JSON-a. Kada AI model vrati svoje predviđanje na temelju zadatka, LLM prima odgovor.

Ako je potrebno više modela da dovrše zadatak, također će interpretirati odgovore tih modela prije nego što ih spoji da bi generirao odgovor za korisnika.

Slijedeći primjer pokazuje kako bi to funkcioniralo kada korisnik traži opis i broj objekata na slici:

## Zadatak

Da nastavite s učenjem o AI agentima, možete izgraditi s Microsoft Agent Framework:

- Aplikaciju koja simulira poslovni sastanak s različitim odjelima obrazovnog startupa.
- Kreirati sistemske poruke koje vode LLM-ove u razumijevanju različitih persona i prioriteta, i omogućavaju korisniku da predstavi novu ideju za proizvod.
- LLM bi zatim trebao generirati slijedna pitanja iz svakog odjela za usavršavanje i poboljšanje ideje i proizvoda.

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [kolekciju za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili nadograđivati svoje znanje o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->