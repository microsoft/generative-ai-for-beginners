# Basisprincipes van Prompt Engineering

[![Basisprincipes van Prompt Engineering](../../../translated_images/nl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introductie
Deze module behandelt essentiële concepten en technieken voor het maken van effectieve prompts in generatieve AI-modellen. De manier waarop je je prompt aan een LLM schrijft, doet er ook toe. Een zorgvuldig gemaakte prompt kan een betere kwaliteit van antwoord opleveren. Maar wat betekenen termen als _prompt_ en _prompt engineering_ precies? En hoe verbeter ik de prompt _input_ die ik naar de LLM stuur? Dit zijn de vragen die we binnen dit hoofdstuk en het volgende proberen te beantwoorden.

_Generatieve AI_ is in staat nieuwe inhoud te creëren (bijv. tekst, afbeeldingen, audio, code enz.) als reactie op gebruikersverzoeken. Dit bereikt het met behulp van _Grote Taalmodellen_ zoals OpenAI's GPT ("Generative Pre-trained Transformer") serie die getraind zijn om natuurlijke taal en code te gebruiken.

Gebruikers kunnen nu met deze modellen interacteren via bekende paradigma's zoals chat, zonder technische expertise of training nodig te hebben. De modellen zijn _prompt-based_ - gebruikers sturen een tekstinvoer (prompt) en krijgen de AI-reactie (completion) terug. Ze kunnen vervolgens iteratief "chatten met de AI" in meer-ronde gesprekken, waarbij ze hun prompt verfijnen totdat de reactie voldoet aan hun verwachtingen.

"Prompts" worden nu de primaire _programmeersinterface_ voor generatieve AI-apps, die tegen de modellen zeggen wat ze moeten doen en de kwaliteit van de teruggegeven antwoorden beïnvloeden. "Prompt Engineering" is een snelgroeiend vakgebied dat zich richt op het _ontwerpen en optimaliseren_ van prompts om consistente en kwalitatieve antwoorden op grote schaal te leveren.

## Leerdoelen

In deze les leren we wat Prompt Engineering is, waarom het belangrijk is en hoe we effectievere prompts kunnen maken voor een bepaald model en toepassingsdoel. We begrijpen kernconcepten en best practices voor prompt engineering - en leren over een interactieve Jupyter Notebooks "sandbox" omgeving waarin we deze concepten op echte voorbeelden kunnen toepassen.

Aan het einde van deze les zullen we in staat zijn om:

1. Uit te leggen wat prompt engineering is en waarom het belangrijk is.
2. De componenten van een prompt te beschrijven en hoe deze worden gebruikt.
3. Best practices en technieken voor prompt engineering te leren.
4. Toegepaste technieken toe te passen op echte voorbeelden, met gebruik van een OpenAI endpoint.

## Belangrijke termen

Prompt Engineering: De praktijk van het ontwerpen en verfijnen van invoer om AI-modellen te sturen richting het produceren van gewenste uitkomsten.
Tokenisatie: Het proces waarbij tekst wordt omgezet in kleinere eenheden, zogenaamde tokens, die een model kan begrijpen en verwerken.
Instruction-Tuned LLMs: Grote taalmodellen (LLM's) die zijn bijgesteld met specifieke instructies om hun responsnauwkeurigheid en relevantie te verbeteren.

## Leer Sandbox

Prompt engineering is momenteel meer kunst dan wetenschap. De beste manier om onze intuïtie erin te verbeteren is door _meer te oefenen_ en een trial-and-error benadering te hanteren waarin domeinkennis gecombineerd wordt met aanbevolen technieken en modelspecifieke optimalisaties.

De bijbehorende Jupyter Notebook bij deze les biedt een _sandbox_ omgeving waar je kunt uitproberen wat je leert - tijdens het leren of als onderdeel van de code-uitdaging aan het einde. Om de oefeningen uit te voeren heb je nodig:

1. **Een Azure OpenAI API-sleutel** - de service endpoint voor een geïmplementeerd LLM.
2. **Een Python-runtime** - waarin de Notebook kan worden uitgevoerd.
3. **Lokale omgevingsvariabelen** - _voltooi nu de [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) stappen om klaar te zijn_.

De notebook wordt geleverd met _startende_ oefeningen - maar je wordt aangemoedigd om je eigen _Markdown_ (beschrijving) en _Code_ (prompt verzoeken) secties toe te voegen om meer voorbeelden of ideeën uit te proberen - en je intuïtie voor promptontwerp te ontwikkelen.

## Geïllustreerde Gids

Wil je een overzicht van wat deze les behandelt voordat je erin duikt? Bekijk dan deze geïllustreerde gids, die je een indruk geeft van de belangrijkste onderwerpen en de kernpunten om over na te denken in elk ervan. Het lesplan leidt je van het begrijpen van kernconcepten en uitdagingen naar het aanpakken ervan met relevante promptengineering-technieken en best practices. Let op dat de sectie "Geavanceerde technieken" in deze gids verwijst naar inhoud die in het _volgende_ hoofdstuk van dit leertraject behandeld wordt.

![Geïllustreerde Gids Prompt Engineering](../../../translated_images/nl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Onze Startup

Laten we nu bespreken hoe _dit onderwerp_ zich verhoudt tot onze startupmissie om [AI-innovatie naar het onderwijs te brengen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). We willen AI-aangedreven toepassingen bouwen voor _gepersonaliseerd leren_ - dus laten we nadenken over hoe verschillende gebruikers van onze applicatie prompts kunnen "ontwerpen":

- **Beheerders** kunnen de AI vragen om _curriculumgegevens te analyseren om hiaten in de dekking te identificeren_. De AI kan resultaten samenvatten of visualiseren met code.
- **Docenten** kunnen de AI vragen om _een lesplan te genereren voor een doelgroep en onderwerp_. De AI kan het gepersonaliseerde plan in een opgegeven formaat maken.
- **Studenten** kunnen de AI vragen om _hen te begeleiden bij een lastig vak_. De AI kan studenten nu begeleiden met lessen, hints en voorbeelden op hun niveau.

Dat is nog maar het topje van de ijsberg. Bekijk [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - een open-source promptbibliotheek samengesteld door onderwijsdeskundigen - om een bredere indruk te krijgen van de mogelijkheden! _Probeer enkele van die prompts uit in de sandbox of met de OpenAI Playground om te zien wat er gebeurt!_

<!--
LESSON TEMPLATE:
Deze eenheid zou kernconcept #1 moeten behandelen.
Versterk het concept met voorbeelden en verwijzingen.

CONCEPT #1:
Prompt Engineering.
Definieer het en leg uit waarom het nodig is.
-->

## Wat is Prompt Engineering?

We begonnen deze les met het definiëren van **Prompt Engineering** als het proces van het _ontwerpen en optimaliseren_ van tekstinvoer (prompts) om consistente en kwalitatieve antwoorden (completions) te leveren voor een gegeven toepassingsdoel en model. We kunnen dit zien als een 2-stappenproces:

- _ontwerpen_ van de initiële prompt voor een gegeven model en doel
- _verfijnen_ van de prompt iteratief om de kwaliteit van het antwoord te verbeteren

Dit is per definitie een trial-and-error proces dat gebruikersintuïtie en inspanning vereist om optimale resultaten te bereiken. Dus waarom is het belangrijk? Om die vraag te beantwoorden, moeten we eerst drie concepten begrijpen:

- _Tokenisatie_ = hoe het model de prompt "ziet"
- _Basis LLM's_ = hoe het fundamentmodel een prompt "verwerkt"
- _Instruction-Tuned LLM's_ = hoe het model nu "taken" kan zien

### Tokenisatie

Een LLM ziet prompts als een _reeks tokens_ waarbij verschillende modellen (of versies van een model) dezelfde prompt op verschillende manieren kunnen tokeniseren. Aangezien LLM's getraind zijn op tokens (en niet op ruwe tekst), heeft de manier waarop prompts getokeniseerd worden een directe impact op de kwaliteit van het gegenereerde antwoord.

Om een intuïtie te krijgen over hoe tokenisatie werkt, probeer tools zoals de [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) hieronder getoond. Kopieer je prompt erin - en zie hoe deze wordt omgezet in tokens, let daarbij op hoe witruimtes en leestekens worden behandeld. Let op dat dit voorbeeld een ouder LLM (GPT-3) laat zien - dus proberen met een nieuwer model kan een andere uitkomst geven.

![Tokenisatie](../../../translated_images/nl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concept: Fundamentmodellen

Zodra een prompt getokeniseerd is, is de primaire functie van de ["Basis LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (of fundamentmodel) het voorspellen van het token in die reeks. Aangezien LLM's getraind zijn op enorme datasets tekst, hebben ze een goed gevoel voor de statistische relaties tussen tokens en kunnen die voorspelling met enige mate van vertrouwen maken. Let op: ze begrijpen niet de _betekenis_ van de woorden in de prompt of token; ze zien alleen een patroon dat ze kunnen "voltooien" met hun volgende voorspelling. Ze kunnen de reeks blijven voorspellen totdat deze wordt beëindigd door gebruikersinterventie of een vooraf ingestelde voorwaarde.

Wil je zien hoe prompt-gebaseerde completie werkt? Voer de bovenstaande prompt in op de [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) met de standaardinstellingen. Het systeem is geconfigureerd om prompts als informatieverzoeken te behandelen - dus je zou een antwoord moeten zien dat bij deze context past.

Maar wat als de gebruiker iets specifieks wil zien dat aan bepaalde criteria of taakdoelen voldoet? Hier komen _instruction-tuned_ LLM's om de hoek kijken.

![Basis LLM Chat Completion](../../../translated_images/nl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concept: Instruction Tuned LLM's

Een [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) begint met het fundamentmodel en stemt dit af met voorbeelden of input/output paren (bijv. multi-turn "berichten") die duidelijke instructies kunnen bevatten - en de reactie van de AI tracht die instructie te volgen.

Dit gebruikt technieken zoals Reinforcement Learning met Menselijke Feedback (RLHF) die het model kunnen trainen om _instructies te volgen_ en _te leren van feedback_ zodat het reacties produceert die beter geschikt zijn voor praktische toepassingen en relevanter zijn voor de doelstellingen van gebruikers.

Laten we het uitproberen - herhaal de bovenstaande prompt, maar verander nu het _systeembericht_ om de volgende instructie als context te geven:

> _Vat de inhoud samen die je krijgt voor een leerling van groep 4. Houd het resultaat tot één alinea met 3-5 opsommingstekens._

Zie je hoe het resultaat nu afgestemd is om het gewenste doel en formaat te weerspiegelen? Een docent kan deze reactie nu direct gebruiken in hun slides voor die les.

![Instruction Tuned LLM Chat Completion](../../../translated_images/nl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Waarom hebben we Prompt Engineering nodig?

Nu we weten hoe prompts door LLM's worden verwerkt, laten we het hebben over _waarom_ we prompt engineering nodig hebben. Het antwoord ligt in het feit dat huidige LLM's een aantal uitdagingen met zich meebrengen die het moeilijker maken om _betrouwbare en consistente completions_ te bereiken zonder moeite te steken in het bouwen en optimaliseren van prompts. Bijvoorbeeld:

1. **Modelreacties zijn stochastisch.** De _zelfde prompt_ zal waarschijnlijk verschillende reacties opleveren met verschillende modellen of modelversies. En het kan zelfs andere resultaten geven met hetzelfde model op verschillende momenten. _Prompt engineering technieken kunnen ons helpen deze variaties te minimaliseren door betere veiligheidsmarges te bieden_.

1. **Modellen kunnen reacties verzinnen.** Modellen zijn voorgetraind met _grote maar eindige_ datasets, wat betekent dat ze geen kennis hebben over concepten buiten dat trainingsbereik. Daardoor kunnen ze completions produceren die onjuist, verzonnen of zelfs tegengesteld aan bekende feiten zijn. _Prompt engineering technieken helpen gebruikers zulke verzinsels te identificeren en te beperken, bijvoorbeeld door AI om bronvermelding of redenering te vragen_.

1. **Modelcapaciteiten zullen variëren.** Nieuwere modellen of modelgeneraties hebben rijkere mogelijkheden maar brengen ook unieke eigenaardigheden en afwegingen mee op het gebied van kosten & complexiteit. _Prompt engineering helpt ons om best practices en workflows te ontwikkelen die verschillen abstraheren en zich aanpassen aan modelspecifieke vereisten op schaalbare, naadloze manieren_.

Laten we dit in actie zien in de OpenAI of Azure OpenAI Playground:

- Gebruik dezelfde prompt met verschillende LLM-implementaties (bijv. OpenAI, Azure OpenAI, Hugging Face) - zag je de variaties?
- Gebruik dezelfde prompt herhaaldelijk met dezelfde LLM-implementatie (bijv. Azure OpenAI playground) - hoe verschilden deze variaties?

### Voorbeeld van Verzinsels

In deze cursus gebruiken we de term **"verzinsel"** om het fenomeen te beschrijven waarbij LLM's soms feitelijk onjuiste informatie genereren vanwege beperkingen in hun training of andere beperkingen. Je hebt dit misschien ook gehoord als _"hallucinaties"_ in populaire artikelen of onderzoeksdocumenten. We raden echter sterk aan om _"verzinsel"_ te gebruiken als term zodat we het gedrag niet per ongeluk antropomorfiseren door het een mensachtige eigenschap toe te dichten aan een machinaal resultaat. Dit versterkt ook de [Verantwoorde AI-richtlijnen](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) vanuit een terminologieperspectief, door termen te verwijderen die in sommige contexten ook als kwetsend of niet-inclusief kunnen worden beschouwd.

Wil je een indruk krijgen van hoe verzinsels werken? Denk aan een prompt die de AI instrueert om inhoud te genereren over een niet-bestaand onderwerp (om zeker te zijn dat het niet in de trainingsdataset voorkomt). Bijvoorbeeld - ik probeerde deze prompt:

> **Prompt:** genereer een lesplan over de Marsoorlog van 2076.

Een zoekactie op het web liet me zien dat er fictieve verhalen zijn (bijv. televisieseries of boeken) over Marsoorlogen - maar niet in 2076. Gezonde verstand vertelt ons ook dat 2076 _in de toekomst_ ligt en dus niet kan worden geassocieerd met een echte gebeurtenis.


Wat gebeurt er dus als we deze prompt uitvoeren met verschillende LLM-providers?

> **Antwoord 1**: OpenAI Playground (GPT-35)

![Antwoord 1](../../../translated_images/nl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Antwoord 2**: Azure OpenAI Playground (GPT-35)

![Antwoord 2](../../../translated_images/nl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Antwoord 3**: : Hugging Face Chat Playground (LLama-2)

![Antwoord 3](../../../translated_images/nl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Zoals verwacht produceert elk model (of modelversie) licht verschillende antwoorden dankzij stochastisch gedrag en variaties in modelcapaciteiten. Bijvoorbeeld, het ene model richt zich op een publiek van groep 8 terwijl het andere uitgaat van een middelbare scholier. Maar alle drie de modellen genereerden antwoorden die een niet-ingewijde gebruiker konden overtuigen dat het evenement echt was.

Prompt engineering-technieken zoals _metaprompting_ en _temperatuurinstelling_ kunnen de fabricaties van het model tot op zekere hoogte verminderen. Nieuwe prompt engineering _architecturen_ integreren ook naadloos nieuwe tools en technieken in de promptstroom, om enkele van deze effecten te verzachten of te verminderen.

## Case Study: GitHub Copilot

Laten we deze sectie afsluiten door een indruk te krijgen van hoe prompt engineering wordt gebruikt in oplossingen uit de echte wereld door te kijken naar een Case Study: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot is je "AI Pair Programmer" - het zet tekstprompts om in codevervolledigingen en is geïntegreerd in je ontwikkelomgeving (bijv. Visual Studio Code) voor een naadloze gebruikerservaring. Zoals gedocumenteerd in de onderstaande reeks blogs, was de vroegste versie gebaseerd op het OpenAI Codex-model - met engineers die snel het belang inzagen van het fijn afstemmen van het model en het ontwikkelen van betere prompt engineering-technieken om de codekwaliteit te verbeteren. In juli lanceerden ze een verbeterd AI-model dat verder gaat dan Codex voor nog snellere suggesties.

Lees de berichten op volgorde om hun leertraject te volgen.

- **Mei 2023** | [GitHub Copilot wordt beter in het begrijpen van je code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Binnen GitHub: Werken met de LLMs achter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Hoe schrijf je betere prompts voor GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot gaat verder dan Codex met verbeterd AI-model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Een ontwikkelaarsgids voor prompt engineering en LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hoe bouw je een enterprise LLM-app: lessen van GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Je kunt ook hun [Engineering blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) doorbladeren voor meer posts zoals [deze](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) die laten zien hoe deze modellen en technieken worden _toegepast_ voor het aandrijven van toepassingen in de echte wereld.

---

<!--
LESSEN TEMPLATE:
Deze eenheid moet kernconcept #2 behandelen.
Versterk het concept met voorbeelden en verwijzingen.

CONCEPT #2:
Prompt ontwerp.
Geïllustreerd met voorbeelden.
-->

## Prompt Constructie

We hebben gezien waarom prompt engineering belangrijk is - laten we nu begrijpen hoe prompts worden _geconstrueerd_ zodat we verschillende technieken kunnen evalueren voor effectiever prompt ontwerp.

### Basisprompt

Laten we beginnen met de basisprompt: een tekstinvoer die naar het model wordt gestuurd zonder verdere context. Hier is een voorbeeld - wanneer we de eerste paar woorden van het Amerikaanse volkslied naar de OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) sturen, voltooit het direct de respons met de volgende regels, wat het basisvoorspellingsgedrag illustreert.

| Prompt (Input)     | Voltooiing (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Het klinkt alsof je de tekst van "The Star-Spangled Banner", het volkslied van de Verenigde Staten, begint. De volledige tekst is ... |

### Complexe prompt

Laten we nu context en instructies toevoegen aan die basisprompt. De [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) stelt ons in staat een complexe prompt op te bouwen als een verzameling van _berichten_ met:

- Input/output-paren die _gebruikers_ input en _assistent_ reactie weergeven.
- Systeembericht dat de context voor het gedrag of de persoonlijkheid van de assistent zet.

Het verzoek heeft nu de onderstaande vorm, waarbij de _tokenisatie_ effectief relevante informatie uit de context en het gesprek opvangt. Het veranderen van de systeemcontext kan nu zo'n grote impact hebben op de kwaliteit van de voltooiingen als de gegeven gebruikersinvoer.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instructieprompt

In de bovenstaande voorbeelden was de gebruikersprompt een eenvoudige tekstvraag die geïnterpreteerd kan worden als een informatieverzoek. Met _instructie_ prompts kunnen we die tekst gebruiken om een taak gedetailleerder te specificeren, waardoor de AI beter wordt geleid. Hier is een voorbeeld:

| Prompt (Input)                                                                                                                                                                                                                         | Voltooiing (Output)                                                                                                        | Instructietype      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Schrijf een beschrijving van de Burgeroorlog                                                                                                                                                                                          | _keerde een eenvoudige alinea terug_                                                                                       | Simpel              |
| Schrijf een beschrijving van de Burgeroorlog. Geef belangrijke data en gebeurtenissen en beschrijf hun betekenis                                                                                                                     | _keerde een alinea gevolgd door een lijst van belangrijke data met beschrijvingen terug_                                   | Complex             |
| Schrijf een beschrijving van de Burgeroorlog in 1 alinea. Geef 3 opsommingstekens met belangrijke data en hun betekenis. Geef 3 meer opsommingstekens met belangrijke historische figuren en hun bijdragen. Geef de output terug als een JSON-bestand | _geeft uitgebreidere details terug in een tekstvak, geformatteerd als JSON die je kunt kopiëren en plakken in een bestand en indien nodig valideren_ | Complex. Geformatteerd. |

## Primaire inhoud

In de bovenstaande voorbeelden was de prompt nog vrij open, waardoor het LLM kon bepalen welk deel van de voorgetrainde dataset relevant was. Met het ontwerp patroon _primaire inhoud_ wordt de invoertekst verdeeld in twee delen:

- een instructie (actie)
- relevante inhoud (die de actie beïnvloedt)

Hier is een voorbeeld waarbij de instructie is om "dit in 2 zinnen samen te vatten".

| Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Voltooiing (Output)                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa die één duizendste is van die van de zon, maar tweeënhalf keer zo groot als alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog zichtbaar zijn aan de nachtelijke hemel, en is bekend bij oude beschavingen sinds vóór de geschiedenis werd opgetekend. Het is vernoemd naar de Romeinse god Jupiter.[19] Wanneer vanaf de aarde gezien, kan Jupiter zo helder zijn dat het gereflecteerde licht zichtbare schaduwen werpt,[20] en is gemiddeld het derde helderste natuurlijke object aan de nachtelijke hemel na de maan en Venus. <br/> **Vat dit samen in 2 korte zinnen** | Jupiter, de vijfde planeet vanaf de zon, is de grootste in het zonnestelsel en staat bekend als een van de helderste objecten aan de nachtelijke hemel. Genoemd naar de Romeinse god Jupiter, is het een gasreus met een massa die tweeënhalf keer zo groot is als die van alle andere planeten in het zonnestelsel samen. |

Het primaire inhoudsegment kan op verschillende manieren worden gebruikt om effectievere instructies te geven:

- **Voorbeelden** - geef het model in plaats van een expliciete instructie voorbeelden van wat het moet doen en laat het patroon afleiden.
- **Hints** - volg de instructie met een "hint" die de voltooiing primeert, en het model richting meer relevante antwoorden leidt.
- **Templates** - dit zijn herhaalbare 'recepten' voor prompts met plaatsaanduidingen (variabelen) die kunnen worden aangepast met data voor specifieke gebruikssituaties.

Laten we deze in de praktijk verkennen.

### Gebruik van voorbeelden

Dit is een aanpak waarbij je de primaire inhoud gebruikt om het model voorbeelden te "voeden" van de gewenste output bij een gegeven instructie, en het model het patroon laat afleiden voor de gewenste output. Afhankelijk van het aantal gegeven voorbeelden spreken we van zero-shot prompting, one-shot prompting, few-shot prompting, enzovoort.

De prompt bestaat nu uit drie componenten:

- Een taakbeschrijving
- Een paar voorbeelden van de gewenste output
- Het begin van een nieuw voorbeeld (dat een impliciete taakbeschrijving wordt)

| Type leren   | Prompt (Input)                                                                                                                                        | Voltooiing (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Vertaal naar het Spaans                                                                                                       | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketbal                  |
|               |                                                                                                                                                       |                             |

Merk op dat we bij zero-shot prompting een expliciete instructie moesten geven ("Vertaal naar het Spaans"), maar dat deze bij het one-shot prompting voorbeeld werd afgeleid. Het few-shot voorbeeld laat zien hoe het toevoegen van meer voorbeelden modellen in staat stelt nauwkeurigere inferenties te maken zonder extra instructies.

### Prompt hints

Een andere techniek om primaire inhoud te gebruiken is het geven van _hints_ in plaats van voorbeelden. In dit geval geven we het model een duwtje in de goede richting door het _te starten_ met een fragment dat het gewenste responsformaat weerspiegelt. Het model "pakt het hint" om zo verder te gaan.

| Aantal hints | Prompt (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Voltooiing (Output)                                                                                                                                                                                                                                                                               |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0              | Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa die één duizendste is van die van de zon, maar tweeënhalf keer zo groot als alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog zichtbaar zijn aan de nachtelijke hemel, en is bekend bij oude beschavingen sinds vóór de geschiedenis werd opgetekend. <br/>**Vat dit samen**                                         | Jupiter is de grootste planeet in ons zonnestelsel en de vijfde vanaf de zon. Het is een gasreus met een massa van 1/1000 van de zon, maar zwaarder dan alle andere planeten samen. Oude beschavingen kennen Jupiter al lang, en hij is gemakkelijk zichtbaar in de nachtelijke hemel. |
| 1              | Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa die één duizendste is van die van de zon, maar tweeënhalf keer zo groot als alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog zichtbaar zijn aan de nachtelijke hemel, en is bekend bij oude beschavingen sinds vóór de geschiedenis werd opgetekend. <br/>**Vat dit samen** <br/> Wat we leerden is dat Jupiter | is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa die één duizendste is van die van de zon, maar tweeënhalf keer zo groot als alle andere planeten samen. Het is goed zichtbaar met het blote oog en al bekend sinds de oudheid.                    |

| 2              | Jupiter is de vijfde planeet vanaf de Zon en de grootste in het Zonnestelsel. Het is een gasreus met een massa die een duizendste is van die van de Zon, maar tweeënhalf keer die van alle andere planeten in het Zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog zichtbaar zijn aan de nachtelijke hemel en is al bekend bij oude beschavingen sinds vóór de geschreven geschiedenis. <br/>**Samenvatting** <br/> Top 3 Feiten die We Hebben Geleerd:         | 1. Jupiter is de vijfde planeet vanaf de Zon en de grootste in het Zonnestelsel. <br/> 2. Het is een gasreus met een massa die een duizendste is van die van de Zon...<br/> 3. Jupiter is sinds de oudheid met het blote oog zichtbaar ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt-sjablonen

Een prompt-sjabloon is een _vooraf gedefinieerd recept voor een prompt_ dat kan worden opgeslagen en hergebruikt indien nodig, om meer consistente gebruikerservaringen op schaal te creëren. In de eenvoudigste vorm is het simpelweg een verzameling promptvoorbeelden zoals [dit van OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) die zowel de interactieve promptcomponenten (gebruikers- en systeemberichten) als het API-gestuurde aanvraagformaat biedt - ter ondersteuning van hergebruik.

In een complexere vorm zoals [dit voorbeeld van LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) bevat het _plaatsaanduiders_ die kunnen worden vervangen door gegevens uit diverse bronnen (gebruikersinvoer, systeemcontext, externe databronnen, enz.) om een prompt dynamisch te genereren. Dit stelt ons in staat een bibliotheek te creëren van herbruikbare prompts die **programmeerbaar** op schaal kunnen worden ingezet om consistente gebruikerservaringen te sturen.

Ten slotte ligt de echte waarde van sjablonen in het vermogen om _promptbibliotheken_ te creëren en publiceren voor verticale toepassingsdomeinen - waarbij het prompt-sjabloon nu _geoptimaliseerd_ is om toepassingsspecifieke context of voorbeelden weer te geven die de reacties relevanter en nauwkeuriger maken voor de doelgroep. De [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository is een uitstekend voorbeeld van deze aanpak, met een bibliotheek van prompts voor het onderwijsdomein gericht op belangrijke doelen zoals lesplanning, curriculumontwerp, studentbegeleiding, enz.

## Ondersteunende Inhoud

Als we promptconstructie zien als het hebben van een instructie (taak) en een doel (primaire inhoud), dan is _secundaire inhoud_ als extra context die we toevoegen om de output op een bepaalde manier te **beïnvloeden**. Dat kunnen afstemmingsparameters, opmaakinstructies, onderwerpentaxonomieën, enz. zijn die het model helpen zijn reactie af te stemmen op de gewenste gebruikersdoelen of verwachtingen.

Bijvoorbeeld: Gegeven een cursuscatalogus met uitgebreide metadata (naam, beschrijving, niveau, metadata-tags, docent, enz.) over alle beschikbare cursussen in het curriculum:

- kunnen we een instructie definiëren om "de cursuscatalogus voor Herfst 2023 samen te vatten"
- kunnen we de primaire inhoud gebruiken om een paar voorbeelden van de gewenste output te geven
- kunnen we de secundaire inhoud gebruiken om de top 5 "tags" van belang te identificeren.

Nu kan het model een samenvatting geven in het formaat dat de voorbeelden tonen - maar als een resultaat meerdere tags heeft, kan het prioriteit geven aan de 5 tags die in de secundaire inhoud zijn aangegeven.

---

<!--
LESSON TEMPLATE:
Deze eenheid moet kernconcept #1 behandelen.
Versterk het concept met voorbeelden en verwijzingen.

CONCEPT #3:
Prompt Engineering Technieken.
Wat zijn enkele basistechnieken voor prompt engineering?
Illustreer dit met wat oefeningen.
-->

## Beste praktijken voor prompten

Nu we weten hoe prompts kunnen worden _geconstrueerd_, kunnen we gaan nadenken over hoe ze te _ontwerpen_ om de beste praktijken te weerspiegelen. We kunnen dit in twee delen denken - de juiste _mindset_ hebben en de juiste _technieken_ toepassen.

### Mindset voor Prompt Engineering

Prompt Engineering is een trial-and-error proces, houd drie brede leidende factoren in gedachten:

1. **Domeinbegrip is belangrijk.** De nauwkeurigheid en relevantie van de respons is een functie van het _domein_ waarin die toepassing of gebruiker opereert. Pas je intuïtie en domeinkennis toe om de technieken verder te **customizen**. Definieer bijvoorbeeld _domeinspecifieke persoonlijkheden_ in je systeem prompts, of gebruik _domeinspecifieke sjablonen_ in je gebruikersprompts. Lever secundaire inhoud die domeinspecifieke contexten reflecteert, of gebruik _domeinspecifieke aanwijzingen en voorbeelden_ om het model te sturen naar bekende gebruikspatronen.

2. **Modelbegrip is belangrijk.** We weten dat modellen van nature stochastisch zijn. Maar modelimplementaties kunnen ook verschillen in de trainingsdataset die ze gebruiken (vooraf getrainde kennis), de mogelijkheden die ze bieden (bijv. via API of SDK) en het type inhoud waarvoor ze geoptimaliseerd zijn (bijv. code vs. afbeeldingen vs. tekst). Begrijp de sterke en zwakke punten van het model dat je gebruikt, en gebruik die kennis om taken te _prioriteren_ of _aangepaste sjablonen_ te bouwen die geoptimaliseerd zijn voor de mogelijkheden van het model.

3. **Iteratie & Validatie is belangrijk.** Modellen ontwikkelen zich snel en dat geldt ook voor de technieken voor prompt engineering. Als domeinexpert heb je misschien een andere context of criteria voor *jouw* specifieke toepassing die niet gelden voor de bredere gemeenschap. Gebruik prompt engineering gereedschappen & technieken om promptconstructie "kickstart" te geven, en iterereer en valideer de resultaten met je eigen intuïtie en domeinkennis. Leg je inzichten vast en creëer een **kennisbasis** (bijv. promptbibliotheken) die door anderen als nieuwe basislijn kan worden gebruikt, voor snellere iteraties in de toekomst.

## Beste praktijken

Laten we nu kijken naar gangbare beste praktijken die worden aanbevolen door [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) en [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) professionals.

| Wat                              | Waarom                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Beoordeel de nieuwste modellen.       | Nieuwe modelgeneraties hebben waarschijnlijk verbeterde functies en kwaliteit - maar kunnen ook hogere kosten met zich meebrengen. Beoordeel hun impact, en neem dan migratiebeslissingen.                                                                                |
| Scheid instructies & context   | Controleer of jouw model/provider _afbakeningstekens_ definieert om instructies, primaire en secundaire inhoud duidelijker te onderscheiden. Dit kan modellen helpen om tokens nauwkeuriger te wegen.                                                         |
| Wees specifiek en duidelijk             | Geef meer details over de gewenste context, uitkomst, lengte, formaat, stijl, enz. Dit verbetert zowel de kwaliteit als de consistentie van reacties. Leg recepten vast in herbruikbare sjablonen.                                                          |
| Wees beschrijvend, gebruik voorbeelden      | Modellen reageren mogelijk beter op een "show en vertel" benadering. Begin met een `zero-shot` aanpak waarbij je een instructie geeft (maar geen voorbeelden), en probeer dan `few-shot` als verfijning, waarbij je een paar voorbeelden van de gewenste output geeft. Gebruik analogieën. |
| Gebruik aanwijzingen om de afhandeling te starten | Zet het model aan tot een gewenste uitkomst door het een paar leidende woorden of zinnen te geven die het als startpunt voor de reactie kan gebruiken.                                                                                                               |
| Herhaal indien nodig                       | Soms moet je jezelf herhalen aan het model. Geef instructies voor en na je primaire inhoud, gebruik een instructie en een aanwijzing, enz. Itereer & valideer om te zien wat werkt.                                                         |
| Volgorde is belangrijk                     | De volgorde waarin je informatie aan het model presenteert kan de output beïnvloeden, ook in de leervoorbeelden, vanwege recency bias. Probeer verschillende opties om te zien wat het beste werkt.                                                               |
| Geef het model een “uitweg”           | Geef het model een _fallback_ completion response die het kan geven als het om een of andere reden de taak niet kan voltooien. Dit kan de kans verkleinen dat modellen onjuiste of gefabriceerde antwoorden genereren.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Zoals bij elke beste praktijk geldt, dat _jouw ervaring kan variëren_ afhankelijk van het model, de taak en het domein. Gebruik deze als startpunt en iterereer om te vinden wat het beste voor jou werkt. Evalueer je prompt engineering proces voortdurend opnieuw naarmate nieuwe modellen en tools beschikbaar komen, met focus op schaalbaarheid van het proces en kwaliteit van reacties.

<!--
LESSON TEMPLATE:
Deze eenheid moet een code uitdaging bevatten indien van toepassing

UITDAGING:
Link naar een Jupyter Notebook met alleen de codecommentaar in de instructies (code-delen zijn leeg).

OPLOSSING:
Link naar een kopie van dat Notebook met de prompts ingevuld en uitgevoerd, ter illustratie van een voorbeeld.
-->

## Opdracht

Gefeliciteerd! Je hebt het einde van de les bereikt! Het is tijd om enkele van die concepten en technieken te testen met echte voorbeelden!

Voor onze opdracht gebruiken we een Jupyter Notebook met oefeningen die je interactief kunt voltooien. Je kunt het Notebook ook uitbreiden met je eigen Markdown- en Code-cellen om zelfstandig ideeën en technieken te verkennen.

### Om te beginnen, fork de repo, daarna

- (Aanbevolen) Start GitHub Codespaces
- (Alternatief) Clone de repo naar je lokale apparaat en gebruik het met Docker Desktop
- (Alternatief) Open het Notebook met je favoriete Notebook-runtimeomgeving.

### Configureer vervolgens je omgevingsvariabelen

- Kopieer het `.env.copy` bestand in de root van de repo naar `.env` en vul de waarden `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` en `AZURE_OPENAI_DEPLOYMENT` in. Ga terug naar de [Learning Sandbox sectie](#leer-sandbox) om te leren hoe.

### Open daarna het Jupyter Notebook

- Selecteer de runtime kernel. Als je optie 1 of 2 gebruikt, selecteer dan simpelweg de standaard Python 3.10.x kernel die wordt geleverd door de dev container.

Je bent klaar om de oefeningen uit te voeren. Merk op dat er hier geen _goede en foute_ antwoorden zijn - alleen het verkennen van mogelijkheden door middel van trial-and-error om intuïtie op te bouwen voor wat werkt voor een gegeven model en toepassingsdomein.

_Daarom zijn er in deze les geen Code Oplossing segmenten. In plaats daarvan heeft het Notebook Markdown-cellen met de titel "Mijn Oplossing:" die één voorbeeldoutput tonen ter referentie._

 <!--
LESSON TEMPLATE:
Sluit de sectie af met een samenvatting en bronnen voor zelfgestuurd leren.
-->

## Kennischeck

Welke van de volgende is een goede prompt die redelijke beste praktijken volgt?

1. Laat me een afbeelding zien van een rode auto
2. Laat me een afbeelding zien van een rode auto van het merk Volvo en model XC90 geparkeerd bij een klif met de zonsondergang
3. Laat me een afbeelding zien van een rode auto van het merk Volvo en model XC90

A: 2, het is de beste prompt omdat het details geeft over "wat" en ingang geeft in specifics (niet zomaar een auto maar een specifiek merk en model) en beschrijft ook de algehele situatie. 3 is de volgende beste omdat het ook veel beschrijving bevat.

## 🚀 Uitdaging

Kijk of je de "aanwijzing" techniek kunt gebruiken met de prompt: Voltooi de zin "Laat me een afbeelding zien van een rode auto van het merk Volvo en ". Wat antwoordt het, en hoe zou jij het verbeteren?

## Geweldig werk! Ga door met leren

Wil je meer leren over verschillende Prompt Engineering concepten? Ga naar de [pagina voor verder leren](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om andere geweldige bronnen over dit onderwerp te vinden.

Ga naar Les 5 waar we kijken naar [geavanceerde prompting technieken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->