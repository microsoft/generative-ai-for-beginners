[![Avoimen lähdekoodin mallit](../../../translated_images/fi/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Johdanto

AI-agentit edustavat jännittävää kehitystä Generatiivisessa tekoälyssä, mahdollistaen suurten kielimallien (LLM) kehittymisen assistenteista agentteiksi, jotka pystyvät suorittamaan toimia. AI-agenttikehykset antavat kehittäjille mahdollisuuden luoda sovelluksia, jotka antavat LLM:ille pääsyn työkaluihin ja tilanhallintaan. Nämä kehykset parantavat myös näkyvyyttä, jolloin käyttäjät ja kehittäjät voivat seurata LLM:ien suunnittelemia toimia ja näin parantaa käyttökokemuksen hallintaa.

Oppitunti kattaa seuraavat alueet:

- Ymmärtäminen, mitä AI-agentti on - Mikä tarkalleen on AI-agentti?
- Viiden eri AI-agenttikehyksen tutkiminen - Mikä tekee niistä ainutlaatuisia?
- Näiden AI-agenttien soveltaminen erilaisiin käyttötapauksiin - Milloin meidän tulisi käyttää AI-agentteja?

## Oppimistavoitteet

Oppitunnin jälkeen pystyt:

- Selittämään, mitä AI-agentit ovat ja miten niitä voidaan käyttää.
- Ymmärtämään eroja suosittujen AI-agenttikehysten välillä ja miten ne eroavat toisistaan.
- Ymmärtämään, miten AI-agentit toimivat, jotta voit rakentaa sovelluksia niiden avulla.

## Mitä ovat AI-agentit?

AI-agentit ovat erittäin jännittävä ala generatiivisen tekoälyn maailmassa. Tämän innostuksen mukana tulee joskus terminologian ja sen sovelluksen sekaannus. Pidämme asiat yksinkertaisina ja kattavina useimmille AI-agentteihin viittaaville työkaluille käyttämällä tätä määritelmää:

AI-agentit antavat suurille kielimalleille (LLM) mahdollisuuden suorittaa tehtäviä antamalla niille pääsyn **tilaan** ja **työkaluihin**.

![Agenttimalli](../../../translated_images/fi/what-agent.21f2893bdfd01e6a.webp)

Määritellään nämä termit:

**Suuret kielimallit** - Nämä ovat kursilla käytettyjä malleja, kuten GPT-5, GPT-4o ja Llama 3.3 jne.

**Tila** - Viittaa kontekstiin, jossa LLM toimii. LLM käyttää aiempien toimien ja nykyisen kontekstin tietoja ohjatakseen päätöksentekoaan seuraavien toimien osalta. AI-agenttikehykset auttavat kehittäjiä ylläpitämään tätä kontekstia helpommin.

**Työkalut** - Suorittaakseen käyttäjän pyytämän ja LLM:n suunnitteleman tehtävän, LLM tarvitsee pääsyn työkaluihin. Esimerkkejä työkaluista voivat olla tietokanta, API, ulkoinen sovellus tai jopa toinen LLM!

Nämä määritelmät antavat toivottavasti hyvän perustan, kun tarkastelemme kuinka niitä toteutetaan. Tutkitaan muutamia eri AI-agenttikehyksiä:

## LangChain-agentit

[LangChain-agentit](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) ovat yllä esittämämme määritelmien toteutus.

Hallitakseen **tilaa** käytetään sisäänrakennettua funktiota nimeltä `AgentExecutor`. Tämä hyväksyy määritellyn `agentin` ja käytettävissä olevat `työkalut`.

`AgentExecutor` tallentaa myös keskusteluhistorian tarjotakseen keskustelun kontekstin.

![Langchain-agentit](../../../translated_images/fi/langchain-agents.edcc55b5d5c43716.webp)

LangChain tarjoaa [työkaluluettelon](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), jotka voidaan tuoda sovellukseesi, joihin LLM voi saada pääsyn. Nämä ovat tehty yhteisön ja LangChain-tiimin toimesta.

Voit sitten määritellä nämä työkalut ja antaa ne `AgentExecutorille`.

Näkyvyys on toinen tärkeä näkökulma AI-agentteja puhuttaessa. On tärkeää, että sovelluskehittäjät ymmärtävät, mitä työkalua LLM käyttää ja miksi. LangChain-tiimi on kehittänyt tätä varten LangSmithin.

## AutoGen

Seuraava AI-agenttikehys, jota käsittelemme, on [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGenin pääpaino on keskusteluissa. Agentit ovat sekä **keskustelukykyisiä** että **mukautettavia**.

**Keskustelukykyisiä** - LLM:t voivat aloittaa ja jatkaa keskustelua toisen LLM:n kanssa suorittaakseen tehtävän. Tämä tehdään luomalla `AssistantAgents` ja antamalla niille tietty järjestelmäviesti.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Mukautettavia** - Agentteja voidaan määritellä paitsi LLM:iksi, myös käyttäjiksi tai työkaluiksi. Kehittäjänä voit määritellä `UserProxyAgentin`, joka vastaa vuorovaikutuksesta käyttäjän kanssa palautteen saamiseksi tehtävän suorittamisesta. Tämä palaute voi jatkaa tehtävän suorittamista tai pysäyttää sen.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tila ja työkalut

Tilaa muuttaakseen ja hallitakseen avustava agentti luo Python-koodia tehtävän suorittamiseksi.

Tässä esimerkki prosessista:

![AutoGen](../../../translated_images/fi/autogen.dee9a25a45fde584.webp)

#### Järjestelmäviestillä määritelty LLM

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Tämä järjestelmäviesti ohjaa tämän tietyn LLM:n, mitkä toiminnot ovat tehtävän kannalta relevantteja. Muista, että AutoGenilla voit määritellä useita AssistantAgentteja eri järjestelmäviesteillä.

#### Käyttäjä aloittaa keskustelun

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Tämä viesti käyttäjäproxyltä (ihmiseltä) käynnistää agentin prosessin tutkia, mitä toimintoja sen tulisi suorittaa.

#### Funktio suoritetaan

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kun alkuperäinen keskustelu on käsitelty, agentti lähettää ehdotetun työkalun kutsuttavaksi. Tässä tapauksessa se on funktio nimeltä `get_weather`. Konfiguraatiostasi riippuen tämä funktio voidaan suorittaa automaattisesti ja lukea agentin toimesta tai suorittaa käyttäjän syötteen perusteella.

Löydät listan [AutoGenin koodiesimerkeistä](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) tutustuaksesi tarkemmin, miten pääset alkuun rakentamisessa.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) on Microsoftin avoimen lähdekoodin SDK AI-agenttien ja moniaagenttijärjestelmien rakentamiseen sekä **Pythonilla** että **.NETillä**. Se yhdistää kahden aiemman Microsoft-projektin vahvuudet — yritysominaisuudet **Semantic Kernelissä** ja moniaagenttien orkestroinnin **AutoGenissä** — yhdeksi tuetuksi kehykseksi. Jos aloitat uuden agenttiprojektin tänään, tämä on suositeltu AutoGenin seuraaja.

Kehys skaalautuu yhdestä **keskusteluagentista** aina monimutkaisiin **moniaagenttiprosesseihin** asti, ja se integroituu suoraan Microsoft Foundryn, Azure OpenAI:n ja OpenAI:n kanssa. Lisäksi se tarjoaa sisäänrakennetun havainnoitavuuden OpenTelemetryn kautta, jotta voit seurata tarkasti, mitä agenttisi tekevät.

### Tila ja työkalut

**Tila** - Kehys hallitsee keskustelukontekstia puolestasi **säikeiden** kautta. Agentti seuraa viestihistoriaa (käyttäjän pyyntöjä, työkalukutsuja ja niiden tuloksia), joten jokainen vaihe rakentuu edellisten päälle. Säikeet voidaan myös tallentaa, jolloin keskustelu voidaan keskeyttää ja jatkaa myöhemmin.

**Työkalut** - Annet agentille työkaluja välittämällä tavallisia Python-funktioita. Tyyppimerkittyjä parametreja muutetaan automaattisesti skeemaksi, jotta malli tietää, miten ja milloin kutsua niitä (funktion kutsu). Kehys tukee myös Model Context Protocol (MCP) -palvelimia ja isännöityjä työkaluja, kuten koodin tulkkia.

Tässä esimerkki yhdestä agentista, jolla on mukautettu työkalu:

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

Yhdistääksesi Microsoft Foundrystä Azure OpenAI:hin, anna päätepisteesi ja tunnistetietosi asiakkaalle:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Moniaagenttiprosessit

Kehyksen suuri vahvuus on useiden agenttien orkestroinnissa. Voit esimerkiksi suorittaa agentteja yksi toisensa jälkeen (jokainen välittää oman kontekstinsa seuraavalle) tai hajauttaa useille agenteille rinnakkain ja koota niiden tulokset yhteen:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Suorita agentit peräkkäin, kuljettamalla keskustelukonteksti ketjua pitkin
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Jaa agentteihin rinnakkain, ja kerää sitten niiden vastaukset yhteen
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Asentaaksesi kehyksen ja aloittaaksesi:

```bash
pip install agent-framework-core
# Valinnaiset integraatiot
pip install agent-framework-openai       # OpenAI ja Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Voit tutkia lisää [Microsoft Agent Frameworkin repositoriosta](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ja [virallisesta dokumentaatiosta](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Seuraava agenttikehys, jota tutustumme, on [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Se tunnetaan "koodi ensin" -agenttina, koska se työskentelee pelkkien `merkkijonojen` sijaan DataFramejen kanssa Pythonissa. Tämä on erittäin hyödyllistä data-analyysi- ja generointitehtävissä. Esimerkkejä voivat olla graafien ja kaavioiden luominen tai satunnaislukujen generointi.

### Tila ja työkalut

Keskustelun tilan hallintaan TaskWeaver käyttää `Planner`-käsitettä. `Planner` on LLM, joka ottaa käyttäjän pyynnön ja laatii tehtävät, jotka on suoritettava tämän pyynnön täyttämiseksi.

Tehtävien suorittamiseksi `Planner`ille on tarjolla kokoelma työkaluja nimeltä `Plugins`. Nämä voivat olla Python-luokkia tai yleinen koodintulkki. Nämä plugin-moduulit tallennetaan upotuksina, jotta LLM voi paremmin etsiä oikean pluginin.

![Taskweaver](../../../translated_images/fi/taskweaver.da8559999267715a.webp)

Tässä esimerkki pluginista, joka käsittelee poikkeavuuksien tunnistusta:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koodi tarkistetaan ennen suoritusta. Toinen Taskweaverin kontekstinhallintaa helpottava ominaisuus on `experience`. Kokemus mahdollistaa keskustelukontekstin pitkäaikaissäilytyksen YAML-tiedostossa. Tämä voidaan määrittää siten, että LLM paranee ajan myötä tietyissä tehtävissä, kun sille altistetaan aiempia keskusteluja.

## JARVIS

Viimeinen agenttikehys, jota tutkimme, on [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVISin ainutlaatuisuus on siinä, että se käyttää LLM:ää keskustelun `tilan` hallintaan ja `työkalut` ovat muita tekoälymalleja. Jokainen tekoälymalli on erikoistunut tiettyihin tehtäviin, kuten kohteiden tunnistukseen, puheen tekstitykseen tai kuvan kuvatekstin luomiseen.

![JARVIS](../../../translated_images/fi/jarvis.762ddbadbd1a3a33.webp)

Yleistarkoituksena mallina LLM vastaanottaa käyttäjän pyynnön ja tunnistaa tietyn tehtävän ja mahdolliset argumentit/tiedot, jotka tarvitaan tehtävän suorittamiseen.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM muotoilee pyynnön sellaiseksi, että erikoistunut tekoälymalli voi sen tulkita, esimerkiksi JSON-muodossa. Kun tekoälymalli on palauttanut ennusteensa tehtävän perusteella, LLM vastaanottaa vastauksen.

Jos tehtävän suorittamiseen tarvitaan useampi malli, LLM tulkitsee myös niiden vastaukset ennen kuin se kokoaa ne tuottaakseen vastauksen käyttäjälle.

Alla oleva esimerkki näyttää, miten tämä toimii, kun käyttäjä pyytää kuvan kohteiden kuvausta ja lukumäärää:

## Tehtävä

Jatka oppimista AI-agenttien parissa rakentamalla sovellus Microsoft Agent Frameworkilla:

- Sovellus, joka simuloi liiketoimintakokousta eri osastojen kanssa koulutusalan startupissa.
- Luo järjestelmäviestit, jotka ohjaavat LLM:ia ymmärtämään erilaisia persoonia ja prioriteetteja, ja anna käyttäjän esitellä uusi tuoteidea.
- LLM:n tulisi sitten luoda jatkokysymyksiä kustakin osastosta pitchin ja tuoteidean tarkentamiseksi ja parantamiseksi.

## Oppiminen ei lopu tähän, jatka matkaa

Tämän oppitunnin suorittamisen jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generatiivisen tekoälyn taitojen kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->