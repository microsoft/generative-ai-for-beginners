[![Avoimen lähdekoodin mallit](../../../translated_images/fi/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Johdanto

AI-agentit edustavat jännittävää kehityssuuntaa generatiivisessa tekoälyssä, mahdollistaen suurten kielimallien (LLM) kehittymisen assistenteista toimijoiksi, jotka kykenevät suorittamaan toimintoja. AI-agenttikehykset antavat kehittäjille mahdollisuuden luoda sovelluksia, jotka antavat LLM:ille pääsyn työkaluihin ja tilan hallintaan. Nämä kehykset parantavat myös näkyvyyttä, jolloin käyttäjät ja kehittäjät voivat seurata LLM:ien suunnittelemia toimintoja, parantaen siten käyttökokemuksen hallintaa.

Oppitunti kattaa seuraavat alueet:

- Mitä AI-agentti tarkalleen ottaen on?
- Viiden eri AI-agenttikehyksen tutkiminen - Mikä tekee niistä ainutlaatuisia?
- Näiden AI-agenttien soveltaminen erilaisiin käyttötapauksiin - Milloin meidän tulisi käyttää AI-agentteja?

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Selittää, mitä AI-agentit ovat ja miten niitä voidaan käyttää.
- Ymmärtää eroja suosittujen AI-agenttikehysten välillä.
- Ymmärtää, miten AI-agentit toimivat sovellusten rakentamiseksi niiden avulla.

## Mitä ovat AI-agentit?

AI-agentit ovat hyvin jännittävä ala generatiivisen tekoälyn maailmassa. Tämän jännityksen mukana tulee toisinaan käsitteiden ja sovellusten sekavuutta. Yksinkertaisuuden ja suurimman osan AI-agentteihin viittaavien työkalujen kattamiseksi käytämme seuraavaa määritelmää:

AI-agentit mahdollistavat suurten kielimallien (LLM) suorittaa tehtäviä antamalla niille pääsyn **tilaan** ja **työkaluihin**.

![Agenttimalli](../../../translated_images/fi/what-agent.21f2893bdfd01e6a.webp)

Määritellään nämä termit:

**Suuret kielimallit** - Näitä ovat kurssin aikana käsitellyt mallit, kuten GPT-3.5, GPT-4, Llama-2 jne.

**Tila** - Viittaa kontekstiin, jossa LLM toimii. LLM käyttää aiempien toimintojensa ja nykyisen kontekstin tietoja ohjatakseen päätöksentekoaan seuraavien toimintojen osalta. AI-agenttikehykset helpottavat kehittäjiä ylläpitämään tätä kontekstia.

**Työkalut** - Suorittaakseen käyttäjän pyytämän ja LLM:n suunnitteleman tehtävän LLM tarvitsee pääsyn työkaluihin. Esimerkkejä työkaluista voivat olla tietokanta, API, ulkoinen sovellus tai jopa toinen LLM!

Nämä määritelmät toivottavasti antavat hyvän pohjan jatkaa, kun tarkastelemme niiden toteutusta. Tutkitaan muutamia eri AI-agenttikehyksiä:

## LangChain-agentit

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) toteuttaa yllä antamamme määritelmät.

Tilan hallintaan se käyttää sisäänrakennettua funktiota nimeltä `AgentExecutor`. Tämä ottaa vastaan määritellyn `agent`in ja käytettävissä olevat `tools`.

`Agent Executor` tallentaa myös chat-historian tarjotakseen keskustelun kontekstin.

![LangChain-agentit](../../../translated_images/fi/langchain-agents.edcc55b5d5c43716.webp)

LangChain tarjoaa [työkaluluettelon](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst), jonka voit tuoda sovellukseesi ja johon LLM pääsee käsiksi. Näitä tekevät yhteisö ja LangChain-tiimi.

Voit määritellä nämä työkalut ja välittää ne `Agent Executor`ille.

Näkyvyys on toinen tärkeä aspekti AI-agentteja puhuttaessa. On tärkeää, että sovelluskehittäjät ymmärtävät, mitä työkalua LLM käyttää ja miksi. Tätä varten LangChain-tiimi on kehittänyt LangSmithin.

## AutoGen

Seuraava AI-agenttikehys, jota käsittelemme, on [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). AutoGenin päätavoitteena ovat keskustelut. Agentit ovat sekä **keskusteltavissa** että **muokattavissa**.

**Keskusteltavissa** - LLM:t voivat aloittaa ja jatkaa keskustelua toisen LLM:n kanssa suorittaakseen tehtävän. Tämä tehdään luomalla `AssistantAgents` ja antamalla niille tietty järjestelmäviesti.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Muokattavissa** - Agentit voivat olla määriteltyjä ei vain LLM:inä, vaan myös käyttäjinä tai työkaluina. Kehittäjänä voit määritellä `UserProxyAgent`in, joka vastaa vuorovaikutuksesta käyttäjän kanssa palautteen saamiseksi tehtävän suorittamisesta. Tämä palaute voi joko jatkaa tehtävän suorittamista tai lopettaa sen.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Tila ja työkalut

Avustava agentti generoituu Python-koodia hallitakseen ja muuttaakseen tilaa suorittaessaan tehtävää.

Tässä esimerkki prosessista:

![AutoGen](../../../translated_images/fi/autogen.dee9a25a45fde584.webp)

#### LLM määritelty järjestelmäviestillä

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Tämä järjestelmäviesti ohjaa tätä tiettyä LLM:ää siihen, mitkä toiminnot ovat olennaisia sen tehtävälle. Muista, että AutoGenissa voit määritellä useita AssistantAgentteja erilaisilla järjestelmäviesteillä.

#### Keskustelu käynnistyy käyttäjän toimesta

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Tämä käyttäjä_proxy:n (ihmisen) viesti käynnistää agentin prosessin tutkia mahdollisia suoritettavia toimintoja.

#### Funktio suoritetaan

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Kun alkuperäinen keskustelu on käsitelty, agentti ehdottaa käytettävää työkalua. Tässä tapauksessa se on `get_weather`-funktio. Kokoonpanostasi riippuen tätä toimintoa voi suorittaa agentti automaattisesti tai se voidaan suorittaa käyttäjän syötteen perusteella.

Löydät lisätietoja ja [AutoGen-koodiesimerkkejä](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) tutustuaksesi siihen, miten pääset alkuun rakentamisessa.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) on Microsoftin avoimen lähdekoodin SDK AI-agenttien ja monitoimijajärjestelmien rakentamiseen sekä **Python**- että **.NET**-ympäristöissä. Se yhdistää kahden aiemman Microsoftin projektin vahvuudet — yritysominaisuudet **Semantic Kernelissä** ja monitoimijaorchesteroinnin **AutoGenissä** — yhdeksi tuetuksi kehyksi. Jos aloitat tänään uuden agenttiprojektin, tämä on suositeltu AutoGenin seuraaja.

Kehys skaalautuu yhdestä **chat-agentista** monimutkaisiin **monitoimijatyönkulkuihin** ja integroituu suoraan Microsoft Foundryyn, Azure OpenAI:hin ja OpenAI:hin. Se tarjoaa myös sisäänrakennetun havaittavuuden OpenTelemetryn kautta, jotta voit tarkasti jäljittää agenttien toimia.

### Tila ja työkalut

**Tila** - Kehys hallitsee keskustelukontekstia puolestasi **keskusteluketjujen** avulla. Agentti seuraa viestihistoriaa (käyttäjän pyynnöt, työkalukutsut ja niiden tulokset), joten jokainen vuoro rakentuu edellisen varaan. Keskusteluketjuja voidaan myös tallentaa, mikä mahdollistaa keskustelun tauottamisen ja jatkamisen myöhemmin.

**Työkalut** - Annet agentille työkaluja välittämällä sille tavallisia Python-funktioita. Typetettyjä parametrejä muunnetaan automaattisesti skeemaksi, joten malli tietää, miten ja milloin kutsua niitä (funktion kutsu). Kehys tukee myös Model Context Protocol (MCP) -palvelimia ja isännöityjä työkaluja, kuten kooditulkkia.

Tässä esimerkki yksittäisestä agentista, jolla on mukautettu työkalu:

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

Jos haluat yhdistää Microsoft Foundryssä Azure OpenAI:hin, välitä päätepiste ja tunnistetiedot asiakkaalle:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Monitoimijatyönkulut

Kehyksen erityinen vahvuus on monien agenttien orkestraatiossa. Esimerkiksi voit ajaa agentteja peräkkäin (jokainen välittää kontekstinsa seuraavalle) tai hajauttaa useille agentteille rinnakkain ja yhdistää niiden tulokset:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Suorita agentit peräkkäin, siirtäen keskustelun kontekstin ketjussa eteenpäin
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Hajauta agentteihin rinnakkain, ja tee sitten vastausten yhdistäminen
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Kehyksen asentamiseksi ja käytön aloittamiseksi:

```bash
pip install agent-framework-core
# Valinnaiset integraatiot
pip install agent-framework-openai       # OpenAI ja Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Voit tutustua lisää [Microsoft Agent Framework -arkistoon](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) ja [viralliseen dokumentaatioon](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Seuraava agenttikehys, jota tutkitaan, on [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). sitä kutsutaan "koodi ensin" -agentiksi, koska se ei työskentele pelkästään `merkkijonojen` kanssa, vaan voi käsitellä Pythonin DataFrameja. Tämä on erittäin hyödyllistä data-analyysi- ja luontitehtävissä, kuten kaavioiden ja graafien luomisessa tai satunnaislukujen generoinnissa.

### Tila ja työkalut

Keskustelun tilan hallintaan TaskWeaver käyttää `Planner`-käsitettä. `Planner` on LLM, joka ottaa käyttäjän pyynnön ja suunnittelee tarvittavat tehtävät tämän pyynnön toteuttamiseksi.

Tehtävien suorittamiseksi `Planner` pääsee käsiksi työkalukokoelmaan nimeltä `Plugins`. Nämä voivat olla Python-luokkia tai yleinen koodin tulkki. Nämä pluginien tiedot tallennetaan upotuksina, jotta LLM voi paremmin hakea oikeaa pluginiä.

![Taskweaver](../../../translated_images/fi/taskweaver.da8559999267715a.webp)

Tässä esimerkki pluginitoteutuksesta poikkeamien tunnistamiseen:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Koodi tarkastetaan ennen suoritusta. Toinen Taskweaverin kontekstinhallintafunktio on `experience`. Experience mahdollistaa keskustelukontekstin tallentamisen pitkällä aikavälillä YAML-tiedostoon. Tämä voidaan konfiguroida niin, että LLM paranee ajan myötä tiettyjen tehtävien suorittamisessa, kun se pääsee käsiksi aiempiin keskusteluihin.

## JARVIS

Viimeinen agenttikehys, jota tutkimme, on [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). JARVISin ainutlaatuisuus on siinä, että se käyttää LLM:ää keskustelun `tilan` hallintaan ja `työkalut` ovat muita tekoälymalleja. Jokainen tekoälymalli on erikoistunut suorittamaan tiettyjä tehtäviä, kuten esineiden tunnistusta, puheen tekstiksi muuntamista tai kuvan kuvatekstitystä.

![JARVIS](../../../translated_images/fi/jarvis.762ddbadbd1a3a33.webp)

LLM, ollen yleiskäyttöinen malli, saa käyttäjän pyynnön, tunnistaa tehtävän ja tarvittavat argumentit/tiedot tehtävän suorittamiseen.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM muotoilee pyynnön mallille luettavaksi muodossa, kuten JSON. Kun tekoälymalli on palauttanut ennusteen tehtävän perusteella, LLM saa vastauksen.

Jos tehtävän suorittamiseen tarvitaan useita malleja, LLM tulkitsee myös näiden mallien vastaukset ennen vastausten yhdistämistä käyttäjälle.

Alla oleva esimerkki näyttää, miten tämä toimisi, kun käyttäjä pyytää kuvan esineiden kuvausta ja määritystä:

## Tehtävä

Jatkaaksesi AI-agenttien oppimista voit rakentaa Microsoft Agent Frameworkilla:

- Sovelluksen, joka simuloi liiketapaamista eri koulutusalan startupin osastojen välillä.
- Luo järjestelmäviestejä, jotka ohjaavat LLM:ää ymmärtämään erilaisia persoonia ja prioriteetteja, ja mahdollistavat käyttäjän ehdottaa uutta tuoteideaa.
- LLM:n tulisi sitten generoida jokaisen osaston jatkokysymyksiä myynnin ja tuoteidean kehittämiseksi ja parantamiseksi.

## Oppiminen ei lopu tähän, jatka matkaa

Oppitunnin jälkeen tutustu Generative AI -oppimiskokoelmaamme [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->