<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:59:39+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "nl"
}
-->
# Basisprincipes van Prompt Engineering

## Inleiding
Deze module behandelt essentiële concepten en technieken voor het maken van effectieve prompts in generatieve AI-modellen. De manier waarop je je prompt schrijft naar een LLM is ook belangrijk. Een zorgvuldig samengestelde prompt kan een betere kwaliteit van respons opleveren. Maar wat betekenen termen als _prompt_ en _prompt engineering_ precies? En hoe verbeter ik de prompt _input_ die ik naar de LLM stuur? Dit zijn de vragen die we in dit hoofdstuk en het volgende zullen proberen te beantwoorden.

_Generatieve AI_ is in staat om nieuwe inhoud te creëren (bijv. tekst, afbeeldingen, audio, code enz.) als reactie op gebruikersverzoeken. Het bereikt dit met behulp van _Grote Taalmodellen_ zoals de GPT ("Generative Pre-trained Transformer") serie van OpenAI die zijn getraind om natuurlijke taal en code te gebruiken.

Gebruikers kunnen nu met deze modellen communiceren via vertrouwde paradigma's zoals chat, zonder technische expertise of training nodig te hebben. De modellen zijn _prompt-gebaseerd_ - gebruikers sturen een tekstinvoer (prompt) en krijgen de AI-respons (voltooiing) terug. Ze kunnen vervolgens "chatten met de AI" in iteratieve, meerturn-conversaties, waarbij ze hun prompt verfijnen totdat de respons aan hun verwachtingen voldoet.

"Prompts" worden nu de primaire _programmeersinterface_ voor generatieve AI-apps, die de modellen vertellen wat te doen en de kwaliteit van de teruggestuurde reacties beïnvloeden. "Prompt Engineering" is een snelgroeiend studiegebied dat zich richt op het _ontwerpen en optimaliseren_ van prompts om consistente en kwalitatieve reacties op schaal te leveren.

## Leerdoelen

In deze les leren we wat Prompt Engineering is, waarom het belangrijk is en hoe we effectievere prompts kunnen maken voor een bepaald model en toepassingsdoel. We zullen kernconcepten en best practices voor prompt engineering begrijpen - en leren over een interactieve Jupyter Notebooks "sandbox" omgeving waar we deze concepten kunnen toepassen op echte voorbeelden.

Aan het einde van deze les zullen we in staat zijn om:

1. Uitleggen wat prompt engineering is en waarom het belangrijk is.
2. De componenten van een prompt beschrijven en hoe ze worden gebruikt.
3. Best practices en technieken voor prompt engineering leren.
4. De geleerde technieken toepassen op echte voorbeelden, met behulp van een OpenAI-endpoint.

## Belangrijke termen

Prompt Engineering: De praktijk van het ontwerpen en verfijnen van inputs om AI-modellen te sturen naar het produceren van gewenste outputs.
Tokenisatie: Het proces van het omzetten van tekst in kleinere eenheden, genaamd tokens, die een model kan begrijpen en verwerken.
Instructie-afgestemde LLMs: Grote Taalmodellen (LLMs) die zijn fijn afgestemd met specifieke instructies om hun nauwkeurigheid en relevantie van reacties te verbeteren.

## Leer Sandbox

Prompt engineering is momenteel meer kunst dan wetenschap. De beste manier om onze intuïtie ervoor te verbeteren is door _meer te oefenen_ en een trial-and-error aanpak te hanteren die expertise in het toepassingsdomein combineert met aanbevolen technieken en modelspecifieke optimalisaties.

De Jupyter Notebook die bij deze les hoort, biedt een _sandbox_ omgeving waarin je kunt uitproberen wat je leert - terwijl je gaat of als onderdeel van de code-uitdaging aan het einde. Om de oefeningen uit te voeren, heb je nodig:

1. **Een Azure OpenAI API-sleutel** - het service-endpoint voor een ingezet LLM.
2. **Een Python-runtime** - waarin de Notebook kan worden uitgevoerd.
3. **Lokale omgevingsvariabelen** - _voltooi de [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) stappen nu om je voor te bereiden_.

De notebook wordt geleverd met _starter_ oefeningen - maar je wordt aangemoedigd om je eigen _Markdown_ (beschrijving) en _Code_ (promptverzoeken) secties toe te voegen om meer voorbeelden of ideeën uit te proberen - en je intuïtie voor promptontwerp op te bouwen.

## Geïllustreerde gids

Wil je een overzicht krijgen van wat deze les behandelt voordat je erin duikt? Bekijk deze geïllustreerde gids, die je een idee geeft van de belangrijkste onderwerpen die worden behandeld en de belangrijkste leerpunten om over na te denken in elk van hen. De lesroutekaart neemt je mee van het begrijpen van de kernconcepten en uitdagingen naar het aanpakken ervan met relevante prompt engineering technieken en best practices. Merk op dat het gedeelte "Geavanceerde technieken" in deze gids verwijst naar inhoud die wordt behandeld in het _volgende_ hoofdstuk van dit curriculum.

## Onze Startup

Laten we nu eens praten over hoe _dit onderwerp_ verband houdt met onze startup-missie om [AI-innovatie naar het onderwijs te brengen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). We willen AI-gestuurde applicaties voor _gepersonaliseerd leren_ bouwen - dus laten we nadenken over hoe verschillende gebruikers van onze applicatie prompts zouden kunnen "ontwerpen":

- **Beheerders** kunnen de AI vragen om _curriculumgegevens te analyseren om hiaten in dekking te identificeren_. De AI kan resultaten samenvatten of ze visualiseren met code.
- **Onderwijzers** kunnen de AI vragen om _een lesplan te genereren voor een specifieke doelgroep en onderwerp_. De AI kan het gepersonaliseerde plan in een gespecificeerd formaat opbouwen.
- **Studenten** kunnen de AI vragen om _hen te begeleiden in een moeilijk vak_. De AI kan nu studenten begeleiden met lessen, hints & voorbeelden die zijn afgestemd op hun niveau.

Dat is slechts het topje van de ijsberg. Bekijk [Prompts Voor Onderwijs](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - een open-source promptbibliotheek samengesteld door onderwijsdeskundigen - om een breder gevoel te krijgen van de mogelijkheden! _Probeer enkele van die prompts in de sandbox of gebruik de OpenAI Playground om te zien wat er gebeurt!_

## Wat is Prompt Engineering?

We begonnen deze les met het definiëren van **Prompt Engineering** als het proces van _ontwerpen en optimaliseren_ van tekstinputs (prompts) om consistente en kwalitatieve reacties (voltooiingen) te leveren voor een gegeven toepassingsdoel en model. We kunnen dit zien als een proces in twee stappen:

- het _ontwerpen_ van de initiële prompt voor een gegeven model en doel
- het _verfijnen_ van de prompt iteratief om de kwaliteit van de respons te verbeteren

Dit is noodzakelijkerwijs een trial-and-error proces dat gebruikersintuïtie en inspanning vereist om optimale resultaten te behalen. Waarom is het dan belangrijk? Om die vraag te beantwoorden, moeten we eerst drie concepten begrijpen:

- _Tokenisatie_ = hoe het model de prompt "ziet"
- _Basis LLMs_ = hoe het basis model een prompt "verwerkt"
- _Instructie-afgestemde LLMs_ = hoe het model nu "taken" kan zien

### Tokenisatie

Een LLM ziet prompts als een _reeks van tokens_ waarbij verschillende modellen (of versies van een model) dezelfde prompt op verschillende manieren kunnen tokeniseren. Omdat LLMs zijn getraind op tokens (en niet op ruwe tekst), heeft de manier waarop prompts worden getokeniseerd een directe invloed op de kwaliteit van de gegenereerde respons.

Om een intuïtie te krijgen voor hoe tokenisatie werkt, probeer tools zoals de [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) hieronder getoond. Kopieer je prompt - en zie hoe dat wordt omgezet in tokens, waarbij je let op hoe spaties en leestekens worden behandeld. Merk op dat dit voorbeeld een ouder LLM (GPT-3) laat zien - dus het proberen met een nieuwer model kan een ander resultaat opleveren.

### Concept: Basis Modellen

Zodra een prompt is getokeniseerd, is de primaire functie van het ["Basis LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (of Basis model) om de token in die reeks te voorspellen. Omdat LLMs zijn getraind op enorme tekstdatasets, hebben ze een goed gevoel voor de statistische relaties tussen tokens en kunnen ze die voorspelling met enige zekerheid maken. Merk op dat ze de _betekenis_ van de woorden in de prompt of token niet begrijpen; ze zien gewoon een patroon dat ze kunnen "voltooien" met hun volgende voorspelling. Ze kunnen doorgaan met het voorspellen van de reeks totdat ze worden beëindigd door gebruikersinterventie of een vooraf vastgestelde voorwaarde.

Wil je zien hoe prompt-gebaseerde voltooiing werkt? Voer de bovenstaande prompt in de Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) in met de standaardinstellingen. Het systeem is geconfigureerd om prompts te behandelen als verzoeken om informatie - dus je zou een voltooiing moeten zien die aan deze context voldoet.

Maar wat als de gebruiker iets specifieks wilde zien dat aan bepaalde criteria of taakdoelstellingen voldeed? Dit is waar _instructie-afgestemde_ LLMs in beeld komen.

### Concept: Instructie-afgestemde LLMs

Een [Instructie-afgestemde LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) begint met het basis model en verfijnt het met voorbeelden of input/output paren (bijv. meerturn "berichten") die duidelijke instructies kunnen bevatten - en de respons van de AI probeert die instructie te volgen.

Dit maakt gebruik van technieken zoals Reinforcement Learning met Human Feedback (RLHF) die het model kunnen trainen om _instructies te volgen_ en _van feedback te leren_ zodat het reacties produceert die beter geschikt zijn voor praktische toepassingen en relevanter zijn voor gebruikersdoelen.

Laten we het uitproberen - herbekijk de bovenstaande prompt, maar verander nu het _systeembericht_ om de volgende instructie als context te geven:

> _Vat de inhoud samen die je krijgt voor een leerling in groep twee. Beperk het resultaat tot één alinea met 3-5 opsommingstekens._

Zie je hoe het resultaat nu is afgestemd om het gewenste doel en formaat weer te geven? Een onderwijzer kan deze reactie nu direct gebruiken in hun dia's voor die klas.

## Waarom hebben we Prompt Engineering nodig?

Nu we weten hoe prompts worden verwerkt door LLMs, laten we praten over _waarom_ we prompt engineering nodig hebben. Het antwoord ligt in het feit dat huidige LLMs een aantal uitdagingen met zich meebrengen die het moeilijker maken om _betrouwbare en consistente voltooiingen_ te bereiken zonder inspanning te leveren in het construeren en optimaliseren van prompts. Bijvoorbeeld:

1. **Modelreacties zijn stochastisch.** De _zelfde prompt_ zal waarschijnlijk verschillende reacties opleveren met verschillende modellen of modelversies. En het kan zelfs verschillende resultaten opleveren met hetzelfde model op verschillende momenten. _Prompt engineering technieken kunnen ons helpen deze variaties te minimaliseren door betere vangrails te bieden_.

2. **Modellen kunnen reacties verzinnen.** Modellen zijn voorgetraind met _grote maar eindige_ datasets, wat betekent dat ze geen kennis hebben over concepten buiten dat trainingsbereik. Als gevolg hiervan kunnen ze voltooiingen produceren die onnauwkeurig, denkbeeldig of direct in tegenspraak zijn met bekende feiten. _Prompt engineering technieken helpen gebruikers dergelijke verzinsels te identificeren en te verminderen, bijvoorbeeld door AI om citaten of redeneringen te vragen_.

3. **Modelmogelijkheden variëren.** Nieuwere modellen of modelgeneraties zullen rijkere mogelijkheden hebben, maar ook unieke eigenaardigheden en afwegingen in kosten & complexiteit met zich meebrengen. _Prompt engineering kan ons helpen best practices en workflows te ontwikkelen die verschillen abstraheren en zich aanpassen aan modelspecifieke vereisten op schaalbare, naadloze manieren_.

Laten we dit in actie zien in de OpenAI of Azure OpenAI Playground:

- Gebruik dezelfde prompt met verschillende LLM-implementaties (bijv. OpenAI, Azure OpenAI, Hugging Face) - zag je de variaties?
- Gebruik dezelfde prompt herhaaldelijk met dezelfde LLM-implementatie (bijv. Azure OpenAI Playground) - hoe verschilden deze variaties?

### Voorbeeld van Verzinsels

In deze cursus gebruiken we de term **"verzinsel"** om te verwijzen naar het fenomeen waarbij LLMs soms feitelijk onjuiste informatie genereren vanwege beperkingen in hun training of andere beperkingen. Je hebt dit misschien ook gehoord als _"hallucinaties"_ in populaire artikelen of onderzoeksartikelen. We raden echter sterk aan om _"verzinsel"_ als de term te gebruiken, zodat we het gedrag niet per ongeluk antropomorfiseren door een menselijke eigenschap toe te schrijven aan een machinaal aangedreven resultaat. Dit versterkt ook [Verantwoordelijke AI-richtlijnen](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) vanuit een terminologieperspectief, waarbij termen worden verwijderd die in sommige contexten ook als beledigend of niet-inclusief kunnen worden beschouwd.

Wil je een idee krijgen van hoe verzinsels werken? Bedenk een prompt die de AI instrueert om inhoud te genereren voor een niet-bestaand onderwerp (om ervoor te zorgen dat het niet in de trainingsdataset wordt gevonden). Bijvoorbeeld - ik probeerde deze prompt:

> **Prompt:** genereer een lesplan over de Mars-oorlog van 2076.

Een webzoekopdracht liet me zien dat er fictieve verhalen waren (bijv. televisieseries of boeken) over Mars-oorlogen - maar geen in 2076. Gezond verstand vertelt ons ook dat 2076 _in de toekomst_ ligt en dus niet geassocieerd kan worden met een echt evenement.

Dus wat gebeurt er als we deze prompt uitvoeren met verschillende LLM-providers?

Zoals verwacht, produceert elk model (of modelversie) enigszins verschillende reacties dankzij stochastisch gedrag en variaties in modelmogelijkheden. Bijvoorbeeld, een model richt zich op een 8e klas publiek, terwijl de andere een middelbare scholier aanneemt. Maar alle drie de modellen genereerden reacties die een niet-geïnformeerde gebruiker zouden kunnen overtuigen dat het evenement echt was.

Prompt engineering technieken zoals _metaprompting_ en _temperatuurconfiguratie_ kunnen modelverzinsels tot op zekere hoogte verminderen. Nieuwe prompt engineering _architecturen_ integreren ook naadloos nieuwe tools en technieken in de promptflow, om sommige van deze effecten te verminderen of te verminderen.

## Case Study: GitHub Copilot

Laten we dit gedeelte afsluiten door een idee te krijgen van hoe prompt engineering wordt gebruikt in oplossingen uit de echte wereld door te kijken naar één Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot is je "AI Pair Programmer" - het converteert tekstprompts naar codevoltooiingen en is geïntegreerd in je ontwikkelomgeving (bijv. Visual Studio Code) voor een naadloze gebruikerservaring. Zoals gedocumenteerd in de reeks blogs hieronder, was de vroegste versie gebaseerd op het OpenAI Codex-model - met ingenieurs die snel de noodzaak realiseerden om het model te verfijnen en betere prompt engineering technieken te ontwikkelen, om de codekwaliteit te verbeteren. In juli debuteerden ze [een verbeterd AI-model dat verder gaat dan Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) voor nog snellere suggesties.

Lees de berichten in volgorde om hun leerreis te volgen.

Je kunt ook hun [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) doorbladeren voor meer berichten zoals [deze](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) die laat zien hoe deze modellen en technieken worden _toegepast_ om toepassingen uit de echte wereld aan te sturen.

## Promptconstructie

We hebben gezien waarom prompt engineering belangrijk is - laten we nu begrijpen hoe prompts worden _geconstrueerd_ zodat we verschillende technieken kunnen evalueren voor effectiever promptontwerp.

### Basis Prompt

Laten we beginnen met de basisprompt: een tekstinvoer die naar het model wordt gestuurd zonder andere context. Hier is een voorbeeld - wanneer we de eerste paar woorden van het Amerikaanse volkslied naar de OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) sturen, voltooit het onmiddellijk de reactie met de volgende paar regels, wat het basis voorspellingsgedrag illustreert.

### Complexe Prompt

Laten we nu context en instructies toevoegen aan die basisprompt. De [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) stelt ons in staat om een complexe prompt te construeren als een verzameling _berichten_ met:

- Input/output paren die _gebruikers_ input en _assistent_ reactie weerspiegelen.
- Systeembericht dat de context voor assistentgedrag of persoonlijkheid instelt.

Het verzoek is nu in de onderstaande vorm, waarbij de _tokenisatie_ effectief relevante informatie uit context en conversatie vastlegt. Nu kan het veranderen van de systeemcontext net zo'n grote impact hebben op de kwaliteit van de voltooiingen als de gebruikersinvoer die wordt gegeven.

### Instructie Prompt

In de bovenstaande voorbeelden was de gebruikersprompt een eenvoudige tekstquery die kon worden geïnterpreteerd als een verzoek om informatie. Met _instructie_ prompts kunnen we die tekst gebruiken om een taak in meer detail te specificeren, wat betere begeleiding biedt aan de AI. Hier is een voorbeeld:

### Primaire Inhoud

In de bovenstaande voorbeelden was de prompt nog steeds vrij open, waardoor de LLM kon beslissen welk deel van zijn voorgetrainde dataset relevant was. Met het _primaire inhoud_ ontwerp patroon wordt de invoertekst in twee delen verdeeld:

- een instructie (actie)
- relevante inhoud (die de actie beïnvloedt)

Hier is een voorbeeld waarbij de instructie is om "dit samen te vatten in 2 zinnen".

Het primaire inhoudssegment kan op verschillende manieren worden gebruikt om
De echte waarde van sjablonen ligt uiteindelijk in het vermogen om _promptbibliotheken_ te creëren en te publiceren voor verticale toepassingsdomeinen - waar het promptsjabloon nu is _geoptimaliseerd_ om toepassingsspecifieke context of voorbeelden te weerspiegelen die de reacties relevanter en nauwkeuriger maken voor de beoogde gebruikersgroep. De [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository is een goed voorbeeld van deze benadering, met een verzameling prompts voor het onderwijsdomein met nadruk op belangrijke doelen zoals lesplanning, curriculumontwerp, studentbegeleiding, enz.

## Ondersteunende Inhoud

Als we nadenken over het opstellen van prompts als het hebben van een instructie (taak) en een doel (primaire inhoud), dan is _secundaire inhoud_ als extra context die we bieden om **op een bepaalde manier de output te beïnvloeden**. Het kan gaan om het afstemmen van parameters, formatteringsinstructies, onderwerpen taxonomieën, enz. die het model kunnen helpen om zijn reactie _aan te passen_ aan de gewenste gebruikersdoelen of verwachtingen.

Bijvoorbeeld: Gegeven een cursuscatalogus met uitgebreide metadata (naam, beschrijving, niveau, metadata-tags, docent, enz.) over alle beschikbare cursussen in het curriculum:

- we kunnen een instructie definiëren om "de cursuscatalogus voor herfst 2023 samen te vatten"
- we kunnen de primaire inhoud gebruiken om een paar voorbeelden van de gewenste output te geven
- we kunnen de secundaire inhoud gebruiken om de top 5 "tags" van interesse te identificeren.

Nu kan het model een samenvatting geven in het formaat dat wordt getoond door de paar voorbeelden - maar als een resultaat meerdere tags heeft, kan het prioriteit geven aan de 5 tags die in de secundaire inhoud zijn geïdentificeerd.

---

## Beste Praktijken voor Prompting

Nu we weten hoe prompts kunnen worden _geconstrueerd_, kunnen we beginnen na te denken over hoe we ze kunnen _ontwerpen_ om de beste praktijken te weerspiegelen. We kunnen hier op twee manieren over nadenken - het hebben van de juiste _mindset_ en het toepassen van de juiste _technieken_.

### Mindset voor Prompt Engineering

Prompt Engineering is een proces van vallen en opstaan, dus houd drie brede leidende factoren in gedachten:

1. **Inzicht in het Domein is Belangrijk.** De nauwkeurigheid en relevantie van de reactie is een functie van het _domein_ waarin die toepassing of gebruiker opereert. Pas je intuïtie en domeinexpertise toe om **technieken verder aan te passen**. Definieer bijvoorbeeld _domeinspecifieke persoonlijkheden_ in je systeemprompts, of gebruik _domeinspecifieke sjablonen_ in je gebruikersprompts. Bied secundaire inhoud die domeinspecifieke contexten weerspiegelt, of gebruik _domeinspecifieke aanwijzingen en voorbeelden_ om het model te leiden naar bekende gebruikspatronen.

2. **Inzicht in het Model is Belangrijk.** We weten dat modellen van nature stochastisch zijn. Maar modelimplementaties kunnen ook variëren in termen van de trainingsdataset die ze gebruiken (vooraf getrainde kennis), de mogelijkheden die ze bieden (bijv. via API of SDK) en het type inhoud waarvoor ze zijn geoptimaliseerd (bijv. code versus afbeeldingen versus tekst). Begrijp de sterke en zwakke punten van het model dat je gebruikt, en gebruik die kennis om _taken te prioriteren_ of _aangepaste sjablonen_ te bouwen die zijn geoptimaliseerd voor de mogelijkheden van het model.

3. **Iteratie & Validatie zijn Belangrijk.** Modellen evolueren snel, en dat geldt ook voor de technieken voor prompt engineering. Als domeinexpert heb je misschien andere context of criteria voor _jouw_ specifieke toepassing, die mogelijk niet van toepassing zijn op de bredere gemeenschap. Gebruik prompt engineering tools & technieken om promptconstructie te "starten", en herhaal en valideer vervolgens de resultaten met je eigen intuïtie en domeinexpertise. Leg je inzichten vast en creëer een **kennisbasis** (bijv. promptbibliotheken) die door anderen kan worden gebruikt als een nieuwe basislijn voor snellere iteraties in de toekomst.

## Beste Praktijken

Laten we nu kijken naar veelvoorkomende beste praktijken die worden aanbevolen door [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) en [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) beoefenaars.

| Wat                               | Waarom                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evalueer de nieuwste modellen.    | Nieuwe modelgeneraties hebben waarschijnlijk verbeterde functies en kwaliteit - maar kunnen ook hogere kosten met zich meebrengen. Evalueer ze op impact en neem dan migratiebeslissingen.                                                            |
| Scheid instructies & context      | Controleer of je model/provider _afscheidingen_ definieert om instructies, primaire en secundaire inhoud duidelijker te onderscheiden. Dit kan modellen helpen om nauwkeuriger gewichten toe te kennen aan tokens.                                    |
| Wees specifiek en duidelijk       | Geef meer details over de gewenste context, uitkomst, lengte, formaat, stijl, enz. Dit verbetert zowel de kwaliteit als de consistentie van reacties. Leg recepten vast in herbruikbare sjablonen.                                                    |
| Wees beschrijvend, gebruik voorbeelden | Modellen kunnen beter reageren op een "laten zien en vertellen" benadering. Start met een `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` waarden. Ga terug naar [Learning Sandbox sectie](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) om te leren hoe.

### Open nu de Jupyter Notebook

- Selecteer de runtime kernel. Als je optie 1 of 2 gebruikt, selecteer dan eenvoudig de standaard Python 3.10.x kernel die door de dev-container wordt geleverd.

Je bent helemaal klaar om de oefeningen uit te voeren. Let op dat er hier geen _goede en foute_ antwoorden zijn - alleen het verkennen van opties door vallen en opstaan en het ontwikkelen van intuïtie voor wat werkt voor een gegeven model en toepassingsdomein.

_Om deze reden zijn er in deze les geen Code Solution segmenten. In plaats daarvan zal de Notebook Markdown-cellen hebben getiteld "My Solution:" die één voorbeeldoutput als referentie toont._

## Kenniscontrole

Welke van de volgende is een goede prompt volgens enkele redelijke beste praktijken?

1. Laat me een afbeelding zien van een rode auto
2. Laat me een afbeelding zien van een rode auto van het merk Volvo en model XC90 geparkeerd bij een klif met de zonsondergang
3. Laat me een afbeelding zien van een rode auto van het merk Volvo en model XC90

A: 2, het is de beste prompt omdat het details geeft over "wat" en in detail treedt (niet zomaar een auto, maar een specifiek merk en model) en het beschrijft ook de algehele setting. 3 is de volgende beste optie omdat het ook veel beschrijving bevat.

## 🚀 Uitdaging

Kijk of je de "aanwijzing" techniek kunt gebruiken met de prompt: Voltooi de zin "Laat me een afbeelding zien van een rode auto van het merk Volvo en ". Wat geeft het als antwoord, en hoe zou je het verbeteren?

## Geweldig Werk! Ga Door Met Leren

Wil je meer leren over verschillende Prompt Engineering concepten? Ga naar de [voortgezette leersite](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om andere geweldige bronnen over dit onderwerp te vinden.

Ga naar Les 5 waar we zullen kijken naar [geavanceerde prompting technieken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in zijn oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.