<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11f03c81f190d9cbafd0f977dcbede6c",
  "translation_date": "2025-06-26T00:26:37+00:00",
  "source_file": "17-ai-agents/README.md",
  "language_code": "hr"
}
-->
[![Open Source Models](../../../translated_images/17-lesson-banner.a5b918fb0920e4e6d8d391a100f5cb1d5929f4c2752c937d40392905dec82592.hr.png)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Uvod

AI Agenti predstavljaju uzbudljiv razvoj u Generativnoj AI, omogućujući Velikim Jezičnim Modelima (LLM-ovima) da se razviju od asistenata u agente sposobne za poduzimanje radnji. Okviri AI Agenta omogućuju programerima stvaranje aplikacija koje LLM-ovima daju pristup alatima i upravljanju stanjem. Ovi okviri također poboljšavaju vidljivost, omogućujući korisnicima i programerima praćenje radnji koje planiraju LLM-ovi, čime se poboljšava upravljanje iskustvom.

Lekcija će pokriti sljedeća područja:

- Razumijevanje što je AI Agent - Što točno predstavlja AI Agent?
- Istraživanje četiri različita okvira AI Agenta - Što ih čini jedinstvenima?
- Primjena ovih AI Agenta na različite slučajeve upotrebe - Kada bismo trebali koristiti AI Agente?

## Ciljevi učenja

Nakon ove lekcije, moći ćete:

- Objasniti što su AI Agenti i kako se mogu koristiti.
- Razumjeti razlike između nekih popularnih okvira AI Agenta i kako se razlikuju.
- Razumjeti kako AI Agenti funkcioniraju kako biste mogli graditi aplikacije s njima.

## Što su AI Agenti?

AI Agenti su vrlo uzbudljivo područje u svijetu Generativne AI. S ovim uzbuđenjem ponekad dolazi do zabune oko pojmova i njihove primjene. Kako bismo stvari učinili jednostavnima i uključili većinu alata koji se odnose na AI Agente, koristit ćemo ovu definiciju:

AI Agenti omogućuju Velikim Jezičnim Modelima (LLM-ovima) obavljanje zadataka dajući im pristup **stanju** i **alatima**.

![Agent Model](../../../translated_images/what-agent.21f2893bdfd01e6a7fd09b0416c2b15594d97f44bbb2ab5a1ff8bf643d2fcb3d.hr.png)

Definirajmo ove pojmove:

**Veliki Jezični Modeli** - To su modeli koji se spominju kroz cijeli ovaj tečaj, kao što su GPT-3.5, GPT-4, Llama-2, itd.

**Stanje** - Ovo se odnosi na kontekst u kojem LLM radi. LLM koristi kontekst svojih prošlih radnji i trenutni kontekst, vodeći svoju odluku za sljedeće radnje. Okviri AI Agenta omogućuju programerima lakše održavanje ovog konteksta.

**Alati** - Da bi dovršio zadatak koji je korisnik zatražio i koji je LLM isplanirao, LLM treba pristup alatima. Neki primjeri alata mogu biti baza podataka, API, vanjska aplikacija ili čak drugi LLM!

Ove definicije će vam, nadamo se, dati dobar temelj dok gledamo kako se implementiraju. Istražimo nekoliko različitih okvira AI Agenta:

## LangChain Agenti

[LangChain Agenti](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) je implementacija definicija koje smo prethodno dali.

Za upravljanje **stanjem**, koristi ugrađenu funkciju zvanu `AgentExecutor`. Ovo prihvaća definirane `agent` i `tools` koji su mu dostupni.

`Agent Executor` također pohranjuje povijest razgovora kako bi pružio kontekst razgovora.

![Langchain Agents](../../../translated_images/langchain-agents.edcc55b5d5c437169a2037211284154561183c58bcec6d4ac2f8a79046fac9af.hr.png)

LangChain nudi [katalog alata](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) koji se mogu uvesti u vašu aplikaciju u kojoj LLM može dobiti pristup. Ove alate izrađuje zajednica i tim LangChain-a.

Možete definirati ove alate i proslijediti ih `Agent Executor`.

Vidljivost je još jedan važan aspekt kada govorimo o AI Agentima. Važno je za programere aplikacija razumjeti koji alat LLM koristi i zašto. Za to je tim u LangChain-u razvio LangSmith.

## AutoGen

Sljedeći okvir AI Agenta o kojem ćemo raspravljati je [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Glavni fokus AutoGen-a su razgovori. Agenti su i **razgovorni** i **prilagodljivi**.

**Razgovorni -** LLM-ovi mogu započeti i nastaviti razgovor s drugim LLM-om kako bi dovršili zadatak. Ovo se postiže stvaranjem `AssistantAgents` i davanjem specifične sistemske poruke.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Prilagodljivi** - Agenti se mogu definirati ne samo kao LLM-ovi već i kao korisnik ili alat. Kao programer, možete definirati `UserProxyAgent` koji je odgovoran za interakciju s korisnikom radi povratnih informacija pri dovršavanju zadatka. Ova povratna informacija može ili nastaviti izvršavanje zadatka ili ga zaustaviti.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Stanje i Alati

Za promjenu i upravljanje stanjem, pomoćni Agent generira Python kod za dovršavanje zadatka.

Evo primjera procesa:

![AutoGen](../../../translated_images/autogen.dee9a25a45fde584fedd84b812a6e31de5a6464687cdb66bb4f2cb7521391856.hr.png)

#### LLM Definiran sa Sistemskom Porukom

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Ova sistemska poruka usmjerava ovaj specifični LLM prema funkcijama koje su relevantne za njegov zadatak. Zapamtite, s AutoGen-om možete imati više definiranih AssistantAgenta s različitim sistemskim porukama.

#### Razgovor Pokreće Korisnik

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Ova poruka od user_proxy (Ljudi) je ono što će pokrenuti proces Agenta da istraži moguće funkcije koje bi trebao izvršiti.

#### Funkcija se Izvršava

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Jednom kada je početni razgovor obrađen, Agent će poslati predloženi alat za poziv. U ovom slučaju, to je funkcija nazvana `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`. Ovo mogu biti Python klase ili opći tumač koda. Ovi dodaci su pohranjeni kao ugrađeni podaci kako bi LLM mogao bolje pretražiti odgovarajući dodatak.

![Taskweaver](../../../translated_images/taskweaver.da8559999267715a95b7677cf9b7d7dd8420aee6f3c484ced1833f081988dcd5.hr.png)

Ovdje je primjer dodatka za rukovanje otkrivanjem anomalija:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod se provjerava prije izvršavanja. Još jedna značajka za upravljanje kontekstom u Taskweaveru je `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` razgovora i `tools` su drugi AI modeli. Svaki od AI modela su specijalizirani modeli koji obavljaju određene zadatke kao što su prepoznavanje objekata, transkripcija ili opisivanje slika.

![JARVIS](../../../translated_images/jarvis.762ddbadbd1a3a3364d4ca3db1a7a9c0d2180060c0f8da6f7bd5b5ea2a115aa7.hr.png)

LLM, kao model opće namjene, prima zahtjev od korisnika i identificira specifičan zadatak i sve argumente/podatke potrebne za dovršavanje zadatka.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM zatim formatira zahtjev na način koji specijalizirani AI model može interpretirati, kao što je JSON. Nakon što AI model vrati svoju predikciju na temelju zadatka, LLM prima odgovor.

Ako je potrebno više modela za dovršavanje zadatka, također će interpretirati odgovor tih modela prije nego ih spoji kako bi generirao odgovor korisniku.

Primjer ispod pokazuje kako bi to funkcioniralo kada korisnik zatraži opis i broj objekata na slici:

## Zadaci

Da biste nastavili s učenjem o AI Agentima, možete graditi s AutoGen-om:

- Aplikaciju koja simulira poslovni sastanak s različitim odjelima startupa u obrazovanju.
- Kreirajte sistemske poruke koje vode LLM-ove u razumijevanju različitih persona i prioriteta, te omogućuju korisniku da predstavi novu ideju proizvoda.
- LLM bi tada trebao generirati naknadna pitanja iz svakog odjela kako bi poboljšao i unaprijedio ideju proizvoda.

## Učenje ne prestaje ovdje, nastavite putovanje

Nakon završetka ove lekcije, provjerite našu [kolekciju za učenje Generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o Generativnoj AI!

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo vas da budete svjesni da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.