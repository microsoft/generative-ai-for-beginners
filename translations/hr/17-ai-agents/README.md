[![Open Source Models](../../../translated_images/hr/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Uvod

AI agenti predstavljaju uzbudljiv razvoj u Generativnoj AI, omogućujući Velikim jezičnim modelima (LLM) da evoluiraju od pomoćnika u agente sposobne za poduzimanje radnji. Okviri za AI agente omogućuju programerima stvaranje aplikacija koje daju LLM-ovima pristup alatima i upravljanje stanjem. Ovi okviri također poboljšavaju vidljivost, dopuštajući korisnicima i programerima nadzirati planirane radnje LLM-ova, čime se poboljšava upravljanje iskustvom.

Lekcija će obraditi sljedeća područja:

- Razumijevanje što je AI agent - Što točno znači AI agent?
- Istraživanje pet različitih okvira za AI agente - Što ih čini jedinstvenima?
- Primjena ovih AI agenata u različitim slučajevima upotrebe - Kada bismo trebali koristiti AI agente?

## Ciljevi učenja

Nakon ove lekcije moći ćete:

- Objasniti što su AI agenti i kako se mogu koristiti.
- Razumjeti razlike između nekih popularnih okvira za AI agente i kako se razlikuju.
- Shvatiti kako AI agenti funkcioniraju kako biste mogli graditi aplikacije s njima.

## Što su AI agenti?

AI agenti su vrlo uzbudljivo polje u svijetu Generativne AI. Ta uzbuđenja ponekad donose i zbunjenost pojmova i njihove primjene. Da bismo pojednostavili i obuhvatili većinu alata koji se odnose na AI agente, koristit ćemo sljedeću definiciju:

AI agenti omogućuju Velikim jezičnim modelima (LLM) da obavljaju zadatke dajući im pristup **stanju** i **alatima**.

![Agent Model](../../../translated_images/hr/what-agent.21f2893bdfd01e6a.webp)

Definirajmo ove pojmove:

**Veliki jezični modeli** - To su modeli o kojima se govori u ovom tečaju kao što su GPT-5, GPT-4o i Llama 3.3 itd.

**Stanje** - Ovo se odnosi na kontekst u kojem LLM radi. LLM koristi kontekst svojih prethodnih radnji i trenutni kontekst, usmjeravajući donošenje odluka za sljedeće radnje. Okviri za AI agente olakšavaju programerima održavanje ovog konteksta.

**Alati** - Za izvršenje zadatka koji je korisnik zatražio i koji je LLM planirao, LLM treba pristup alatima. Neki primjeri alata mogu biti baza podataka, API, vanjska aplikacija ili čak drugi LLM!

Ove definicije se nadamo da će vam pružiti dobar temelj za daljnje proučavanje implementacija. Pogledajmo nekoliko različitih okvira za AI agente:

## LangChain Agenti

[LangChain Agenti](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) su implementacija definicija koje smo dali gore.

Za upravljanje **stanjem** koristi ugrađenu funkciju nazvanu `AgentExecutor`. Ona prihvaća definirani `agent` i `alate` koji su mu dostupni.

`AgentExecutor` također pohranjuje povijest razgovora kako bi pružio kontekst chata.

![Langchain Agents](../../../translated_images/hr/langchain-agents.edcc55b5d5c43716.webp)

LangChain nudi [katalog alata](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) koje možete uvesti u svoju aplikaciju i kojima LLM može pristupiti. Ti alati su izrađeni od strane zajednice i LangChain tima.

Možete zatim definirati te alate i proslijediti ih `AgentExecutoru`.

Vidljivost je još jedan važan aspekt kada govorimo o AI agentima. Važno je da programeri aplikacija razumiju koji alat LLM koristi i zašto. Za to, tim LangChain-a razvio je LangSmith.

## AutoGen

Sljedeći okvir za AI agente o kojem ćemo govoriti je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Glavni fokus AutoGen-a su razgovori. Agenti su i **razgovorni** i **prilagodljivi**.

**Razgovorni -** LLM-ovi mogu započeti i nastaviti razgovor s drugim LLM-om kako bi završili zadatak. To se radi stvaranjem `AssistantAgents` i davanjem određenih sustavnih poruka.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prilagodljivi** - Agente nije moguće definirati samo kao LLM-ove već i kao korisnike ili alate. Kao programer, možete definirati `UserProxyAgent` koji je zadužen za interakciju s korisnikom za povratne informacije prilikom izvršavanja zadatka. Ove povratne informacije mogu nastaviti izvršavanje zadatka ili ga zaustaviti.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stanje i alati

Za promjenu i upravljanje stanjem, pomoćni Agent generira Python kod za izvršenje zadatka.

Evo primjera postupka:

![AutoGen](../../../translated_images/hr/autogen.dee9a25a45fde584.webp)

#### LLM definiran sustavnom porukom

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ova sustavna poruka usmjerava ovaj specifični LLM na funkcije relevantne za njegov zadatak. Zapamtite, s AutoGen-om možete imati više definiranih AssistantAgents s različitim sustavnim porukama.

#### Chat započinje korisnik

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ova poruka od user_proxy (čovjek) će pokrenuti proces Agenta da istraži moguće funkcije koje treba izvršiti.

#### Funkcija se izvršava

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kad se obradi početni chat, Agent šalje predloženi alat koji treba nazvati. U ovom slučaju, to je funkcija nazvana `get_weather`. Ovisno o postavkama, ova funkcija može biti automatski izvršena i pročitana od strane Agenta ili može biti izvršena na temelju korisničkog unosa.

Možete pronaći popis [AutoGen kod primjera](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) za daljnje istraživanje kako započeti s izradom.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) je Microsoftov open-source SDK za izgradnju AI agenata i sustava s više agenata kako u **Pythonu** tako i u **.NET-u**. On objedinuje snage dvaju ranijih Microsoftovih projekata — poduzećne značajke **Semantic Kernel** i orkestraciju više agenata **AutoGen** — u jedan, podržani okvir. Ako danas započinjete novi agent projekt, ovo je preporučeni nasljednik AutoGen-a.

Okvir se može koristiti od jednog **chat agenta** sve do složenih **višestrukih agentnih tokova rada**, i integrira se izravno s Microsoft Foundry, Azure OpenAI i OpenAI. Također pruža ugrađeno promatranje kroz OpenTelemetry kako biste mogli pratiti točno što vaši agenti rade.

### Stanje i alati

**Stanje** - Okvir za vas upravlja kontekstom razgovora kroz **threadove**. Agent prati povijest poruka (zahtjeve korisnika, pozive alata i njihove rezultate), tako da se svaki korak nadovezuje na prethodne. Threadovi također mogu biti sačuvani, dopuštajući pauziranje i nastavak razgovora.

**Alati** - Agentu dajete alate prosljeđivanjem običnih Python funkcija. Parametri s tipovima automatski se pretvaraju u shemu, tako da model zna kako i kada ih pozivati (pozivanje funkcija). Okvir također podržava Model Context Protocol (MCP) servere i hostane alate poput interpretatora koda.

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

Da biste se umjesto toga povezali na Azure OpenAI u Microsoft Foundry-ju, proslijedite svoju krajnju točku i vjerodajnice klijentu:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Tokovi rada s više agenata

Gdje okvir doista dolazi do izražaja jest orkestracija nekoliko agenata zajedno. Na primjer, možete pokretati agente jedan za drugim (svaki prosljeđuje svoj kontekst sljedećem) ili paralelno rasporediti više agenata i objediniti njihove rezultate:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Pokreni agente jedan za drugim, prosljeđujući kontekst razgovora nizom
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Pokreni agente paralelno, zatim objedini njihove odgovore
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

Sljedeći okvir za agente koji ćemo istražiti je [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Poznat je kao "kod-prvo" agent jer umjesto strogo rada sa `stringovima`, može raditi s DataFrameovima u Pythonu. Ovo postaje izuzetno korisno za zadatke analize i generiranja podataka. To mogu biti stvari poput stvaranja grafova i dijagrama ili generiranje slučajnih brojeva.

### Stanje i alati

Za upravljanje stanjem razgovora, TaskWeaver koristi koncept `Planera`. `Planer` je LLM koji prima zahtjev od korisnika i mapira zadatke koje treba obaviti da bi ispunio taj zahtjev.

Za izvršenje zadataka, `Planer` ima pristup kolekciji alata nazvanih `Plugins`. To mogu biti Python klase ili opći interpretator koda. Ovi pluginovi se pohranjuju kao embeddingi kako bi LLM mogao bolje potražiti odgovarajući plugin.

![Taskweaver](../../../translated_images/hr/taskweaver.da8559999267715a.webp)

Evo primjera plugina za detekciju anomalija:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod se provjerava prije izvršenja. Još jedna značajka za upravljanje kontekstom u Taskweaveru je `experience`. Experience omogućuje pohranu konteksta razgovora dugoročno u YAML datoteku. To je moguće konfigurirati tako da se LLM tijekom vremena poboljšava na određenim zadacima pod uvjetom da je izložen prethodnim razgovorima.

## JARVIS

Posljednji okvir za agente koji ćemo istražiti je [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Ono što JARVIS čini jedinstvenim je da koristi LLM za upravljanje `stanjem` razgovora, a `alatima` su drugi AI modeli. Svaki od AI modela su specijalizirani modeli koji obavljaju određene zadatke poput detekcije objekata, transkripcije ili opisivanja slika.

![JARVIS](../../../translated_images/hr/jarvis.762ddbadbd1a3a33.webp)

LLM, kao model opće namjene, prima zahtjev od korisnika i identificira specifičan zadatak i sve argumente/podatke potrebne za izvršenje zadatka.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM zatim formatira zahtjev na način koji specijalizirani AI model može interpretirati, poput JSON-a. Kada AI model vrati svoju predikciju na osnovi zadatka, LLM prima odgovor.

Ako je potrebno više modela za izvršenje zadatka, također će interpretirati odgovore tih modela prije nego ih objedini kako bi generirao odgovor korisniku.

Donji primjer pokazuje kako bi to funkcioniralo kad korisnik zatraži opis i broj objekata na slici:

## Zadatak

Za nastavak učenja o AI agentima možete izgraditi s Microsoft Agent Frameworkom:

- Aplikaciju koja simulira poslovni sastanak s različitim odjelima edukativnog startupa.
- Kreirajte sustavne poruke koje usmjeravaju LLM-ove u razumijevanju različitih persona i prioriteta, te omogućuju korisniku predstavljanje nove ideje proizvoda.
- LLM bi zatim trebao generirati pitanja za svaki odjel radi dodatnog usavršavanja i poboljšanja ideje i prezentacije proizvoda.

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, pogledajte našu [Generativnu AI kolekciju za učenje](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili s usavršavanjem svojih znanja o Generativnoj AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->