# Prompt Engineering Fundamentals

[![Prompt Engineering Fundamentals](../../../translated_images/nl/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Inleiding
Deze module behandelt essentiële concepten en technieken voor het maken van effectieve prompts in generatieve AI-modellen. De manier waarop je je prompt schrijft aan een LLM doet er ook toe. Een zorgvuldig opgestelde prompt kan een betere kwaliteit van respons opleveren. Maar wat betekenen termen als _prompt_ en _prompt engineering_ precies? En hoe verbeter ik de prompt _input_ die ik naar de LLM stuur? Dit zijn de vragen die we in dit hoofdstuk en het volgende proberen te beantwoorden.

_Generatieve AI_ kan nieuwe inhoud maken (bijv. tekst, afbeeldingen, audio, code enz.) als reactie op gebruikersverzoeken. Dit wordt bereikt met behulp van _Large Language Models_ zoals de GPT ("Generative Pre-trained Transformer")-serie van OpenAI, die getraind zijn om natuurlijke taal en code te gebruiken.

Gebruikers kunnen nu met deze modellen communiceren via vertrouwde methoden zoals chatten, zonder technische kennis of training nodig te hebben. De modellen zijn _prompt-gebaseerd_ - gebruikers sturen een tekstinvoer (prompt) en krijgen de AI-respons (completion) terug. Ze kunnen dan herhaaldelijk "chatten met de AI" in meertrapsconversaties, hun prompt verfijnen totdat de respons aansluit bij hun verwachtingen.

"Prompts" worden nu de primaire _programmeersinterface_ voor generatieve AI-apps, waarmee de modellen wordt verteld wat ze moeten doen en waarbij de kwaliteit van de teruggegeven reacties wordt beïnvloed. "Prompt Engineering" is een snelgroeiend onderzoeksgebied dat zich richt op het _ontwerpen en optimaliseren_ van prompts om consistente en kwalitatieve reacties op schaal te leveren.

## Leerdoelen

In deze les leren we wat Prompt Engineering is, waarom het belangrijk is en hoe we effectievere prompts kunnen maken voor een bepaald model en toepassingdoel. We begrijpen kernconcepten en best practices voor prompt engineering - en leren over een interactieve Jupyter Notebooks "sandbox"-omgeving waarin we deze concepten kunnen toepassen op echte voorbeelden.

Aan het einde van deze les kunnen we:

1. Uitleggen wat prompt engineering is en waarom het belangrijk is.
2. De componenten van een prompt beschrijven en hoe ze worden gebruikt.
3. Best practices en technieken voor prompt engineering leren.
4. Toegepaste technieken op echte voorbeelden gebruiken, met een OpenAI-endpoint.

## Belangrijke termen

Prompt Engineering: De praktijk van het ontwerpen en verfijnen van invoer om AI-modellen te sturen naar het produceren van gewenste output.
Tokenisatie: Het proces waarbij tekst wordt omgezet in kleinere eenheden, tokens genaamd, die een model kan begrijpen en verwerken.
Instruction-Tuned LLMs: Large Language Models (LLM's) die zijn fijn afgesteld met specifieke instructies om de nauwkeurigheid en relevantie van hun respons te verbeteren.

## Leer Sandbox

Prompt engineering is momenteel meer kunst dan wetenschap. De beste manier om er meer gevoel voor te krijgen is door _meer te oefenen_ en een trial-and-error aanpak aan te houden die domeinexpertise combineert met aanbevolen technieken en model-specifieke optimalisaties.

De Jupyter Notebook die bij deze les hoort, biedt een _sandbox_-omgeving waar je kunt experimenteren met wat je leert - tijdens het leren of als onderdeel van de code-uitdaging aan het einde. Om de oefeningen uit te voeren heb je nodig:

1. **Een Azure OpenAI API-sleutel** - de service-endpoint voor een inzetbare LLM.
2. **Een Python-runtime** - waarin de Notebook kan worden uitgevoerd.
3. **Lokale omgevingsvariabelen** - _voltooi nu de [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) stappen om klaar te zijn_.

De notebook bevat _starters_ oefeningen - maar je wordt aangemoedigd om zelf ook _Markdown_ (beschrijving) en _Code_ (prompt-aanvragen) toe te voegen om meer voorbeelden of ideeën te proberen - en zo je gevoel voor promptontwerp te ontwikkelen.

## Geïllustreerde gids

Wil je eerst het grote geheel zien van wat deze les behandelt voordat je erin duikt? Bekijk dan deze geïllustreerde gids, die je een idee geeft van de hoofdonderwerpen en de belangrijkste punten om over na te denken bij elk onderwerp. De lesroutekaart leidt je van het begrijpen van kernconcepten en uitdagingen naar het aanpakken ervan met relevante prompt engineering-technieken en best practices. Merk op dat het gedeelte "Geavanceerde technieken" in deze gids verwijst naar inhoud die aan bod komt in het _volgende_ hoofdstuk van deze cursus.

![Geïllustreerde gids voor Prompt Engineering](../../../translated_images/nl/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Onze Startup

Laten we nu bespreken hoe _dit onderwerp_ aansluit bij onze startup-missie om [AI-innovatie naar het onderwijs te brengen](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). We willen AI-gestuurde toepassingen van _gepersonaliseerd leren_ bouwen - dus laten we nadenken over hoe verschillende gebruikers van onze applicatie prompts kunnen "ontwerpen":

- **Beheerders** kunnen de AI vragen _curriculumgegevens te analyseren om hiaten in dekking te identificeren_. De AI kan resultaten samenvatten of visualiseren met code.
- **Onderwijzers** kunnen de AI vragen _een lesplan te genereren voor een doelgroep en onderwerp_. De AI kan het gepersonaliseerde plan in een gespecificeerd formaat bouwen.
- **Studenten** kunnen de AI vragen _hen te begeleiden in een moeilijk vak_. De AI kan studenten nu begeleiden met lessen, hints en voorbeelden, afgestemd op hun niveau.

Dit is nog maar het topje van de ijsberg. Bekijk [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - een open-source promptbibliotheek samengesteld door onderwijsdeskundigen - om een bredere indruk van de mogelijkheden te krijgen! _Probeer enkele van die prompts uit in de sandbox of met de OpenAI Playground en kijk wat er gebeurt!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Wat is Prompt Engineering?

We begonnen deze les met het definiëren van **Prompt Engineering** als het proces van _ontwerpen en optimaliseren_ van tekstinvoer (prompts) om consistente en kwalitatieve reacties (completions) te leveren voor een bepaalde toepassing en model. We kunnen dit zien als een 2-stappenproces:

- het _ontwerpen_ van de initiële prompt voor een bepaald model en doel
- het _verbeteren_ van de prompt iteratief om de kwaliteit van de respons te verhogen

Dit is per definitie een trial-and-errorproces dat intuïtie en moeite van de gebruiker vereist om optimale resultaten te verkrijgen. Waarom is het belangrijk? Om die vraag te beantwoorden moeten we eerst drie concepten begrijpen:

- _Tokenisatie_ = hoe het model de prompt "ziet"
- _Basis LLM's_ = hoe het fundatiemodel een prompt "verwerkt"
- _Instruction-Tuned LLM's_ = hoe het model nu "taken" kan zien

### Tokenisatie

Een LLM ziet prompts als een _sequentie van tokens_ waarbij verschillende modellen (of versies van een model) dezelfde prompt op verschillende manieren kunnen tokeniseren. Omdat LLM's getraind zijn op tokens (en niet op ruwe tekst), heeft de manier waarop prompts worden getokeniseerd directe invloed op de kwaliteit van de gegenereerde respons.

Om een idee te krijgen van hoe tokenisatie werkt, probeer tools zoals de [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) hieronder. Kopieer je prompt en zie hoe deze wordt omgezet in tokens, let op hoe spaties en leestekens worden verwerkt. Let op dat dit voorbeeld een ouder LLM (GPT-3) toont - bij het proberen met een nieuwer model kan het resultaat verschillen.

![Tokenisatie](../../../translated_images/nl/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concept: Foundation Models

Zodra een prompt is getokeniseerd, is de primaire functie van de ["Basis LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (of foundation model) het voorspellen van het volgende token in die reeks. Omdat LLM's zijn getraind op gigantische tekstdatasets, hebben ze een goed gevoel voor statistische relaties tussen tokens en kunnen ze die voorspelling met vertrouwen maken. Let op: ze _begrijpen_ de betekenis van de woorden in de prompt of token niet; ze zien alleen een patroon dat ze kunnen "aanvullen" met hun volgende voorspelling. Ze kunnen de sequentie blijven voorspellen totdat het wordt stopgezet door gebruikersinterventie of een vooraf bepaalde condition.

Wil je zien hoe prompt-based completie werkt? Voer bovenstaande prompt in bij de Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) met de standaardinstellingen. Het systeem is geconfigureerd om prompts als informatieverzoeken te behandelen - dus je zou een completion moeten zien die bij deze context past.

Maar wat als de gebruiker iets specifieks wil zien dat aan bepaalde criteria of taakdoel voldoet? Hier komen _instruction-tuned_ LLM's in beeld.

![Base LLM Chat Completion](../../../translated_images/nl/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concept: Instruction Tuned LLMs

Een [Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) begint met het foundation model en stelt het bij met voorbeelden of input/output-paren (bijv. meertraps "berichten") die duidelijke instructies kunnen bevatten - en de AI probeert die instructie te volgen in de reactie.

Dit gebruikt technieken zoals Reinforcement Learning met Human Feedback (RLHF) die het model kunnen trainen om _instructies te volgen_ en _te leren van feedback_, zodat het reacties produceert die beter passen bij praktische toepassingen en relevanter zijn voor gebruikersdoelen.

Laten we het proberen - bekijk de prompt hierboven opnieuw, maar verander nu het _systeembericht_ om de volgende instructie als context te geven:

> _Vat de content samen die je krijgt voor een leerling in groep 4. Hou het resultaat tot één alinea met 3-5 bullet points._

Zie je hoe het resultaat nu is afgestemd op het gewenste doel en format? Een docent kan deze respons nu direct in de dia’s voor die les gebruiken.

![Instruction Tuned LLM Chat Completion](../../../translated_images/nl/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Waarom hebben we Prompt Engineering nodig?

Nu we weten hoe prompts door LLM's worden verwerkt, laten we bespreken _waarom_ we prompt engineering nodig hebben. Het antwoord ligt in het feit dat huidige LLM's een aantal uitdagingen kennen waardoor _betrouwbare en consistente completion_ moeilijker te behalen is zonder inspanning voor promptconstructie en optimalisatie. Bijvoorbeeld:

1. **Modelresponsen zijn stochastisch.** De _zelfde prompt_ zal waarschijnlijk verschillende antwoorden opleveren bij verschillende modellen of modelversies. En het kan zelfs verschillende resultaten geven met het _zelfde model_ op verschillende momenten. _Prompt engineering technieken kunnen ons helpen deze variaties te minimaliseren door betere richtlijnen te bieden_.

2. **Modellen kunnen antwoorden verzinnen.** Modellen zijn getraind met _grote maar beperkte_ datasets, wat betekent dat ze geen kennis hebben buiten die trainingsscope. Daardoor kunnen ze reacties genereren die onnauwkeurig, verzonnen of direct tegenstrijdig zijn met bekende feiten. _Prompt engineering helpt gebruikers zulke verzinsels te identificeren en te beperken, bijvoorbeeld door AI om bronnen of redeneringen te vragen_.

3. **Modelcapaciteiten variëren.** Nieuwere modellen of modelgeneraties beschikken over rijkere capaciteiten maar brengen ook unieke eigenaardigheden en afwegingen in kosten en complexiteit met zich mee. _Prompt engineering helpt ons best practices en workflows te ontwikkelen die verschillen abstraheren en model-specifieke vereisten op schaal en naadloos aanpakken_.

Laten we dit in actie zien in de OpenAI of Azure OpenAI Playground:

- Gebruik dezelfde prompt bij verschillende LLM-inzettingen (bijv. OpenAI, Azure OpenAI, Hugging Face) - zag je variaties?
- Gebruik dezelfde prompt herhaaldelijk bij dezelfde LLM-inzetting (bijv. Azure OpenAI playground) - hoe verschillen die variaties?

### Voorbeeld van verzinsels

In deze cursus gebruiken we de term **"verzinsel"** om te verwijzen naar het fenomeen waarbij LLM's soms feitelijk onjuiste informatie genereren vanwege beperkingen in hun training of andere beperkingen. Je hebt dit misschien ook wel eens "hallucinaties" horen noemen in populaire artikelen of onderzoeksrapporten. Wij raden echter sterk aan de term _"verzinsel"_ te gebruiken zodat we het gedrag niet per ongeluk antropomorfiseren door er een menselijk kenmerk aan toe te schrijven. Dit ondersteunt ook de [Responsible AI-richtlijnen](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) vanuit terminologieperspectief, door termen te vermijden die mogelijk aanstootgevend of niet-inclusief zijn in sommige contexten.

Wil je een idee krijgen van hoe verzinsels werken? Denk aan een prompt die de AI instructies geeft om content te genereren over een niet-bestaand onderwerp (zodat het niet voorkomt in de trainingsdata). Bijvoorbeeld - ik probeerde deze prompt:

> **Prompt:** genereer een lesplan over de Marsoorlog van 2076.
Een webzoekopdracht toonde aan dat er fictieve verslagen waren (bijvoorbeeld televisieseries of boeken) over Marsoorlogen - maar niet in 2076. Gezond verstand vertelt ons ook dat 2076 _in de toekomst_ ligt en dus niet verbonden kan worden aan een echte gebeurtenis.

Wat gebeurt er dus als we deze prompt uitvoeren bij verschillende LLM-aanbieders?

> **Reactie 1**: OpenAI Playground (GPT-35)

![Reactie 1](../../../translated_images/nl/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Reactie 2**: Azure OpenAI Playground (GPT-35)

![Reactie 2](../../../translated_images/nl/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Reactie 3**: : Hugging Face Chat Playground (LLama-2)

![Reactie 3](../../../translated_images/nl/04-fabrication-huggingchat.faf82a0a51278956.webp)

Zoals verwacht produceert elk model (of modelversie) iets verschillende antwoorden dankzij stochastisch gedrag en variaties in modelcapabilities. Zo richt het ene model zich op een 8e klas publiek terwijl het andere uitgaat van een middelbare scholier. Maar alle drie de modellen genereerden reacties die een ongeïnformeerde gebruiker zouden kunnen overtuigen dat de gebeurtenis echt was.

Prompt engineering-technieken zoals _metaprompting_ en _temperatuursinstelling_ kunnen modelfabricaties tot op zekere hoogte verminderen. Nieuwe prompt engineering _architecturen_ integreren ook naadloos nieuwe tools en technieken in de promptstroom, om sommige van deze effecten tegen te gaan of te verminderen.

## Case Study: GitHub Copilot

We ronden deze sectie af met een beeld van hoe prompt engineering wordt toegepast in reële oplossingen door naar een Case Study te kijken: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot is je "AI Pair Programmer" - het zet tekstprompts om in code-aanvullingen en is geïntegreerd in je ontwikkelomgeving (bijvoorbeeld Visual Studio Code) voor een naadloze gebruikerservaring. Zoals gedocumenteerd in onderstaande reeks blogs, was de vroegste versie gebaseerd op het OpenAI Codex-model - waarbij ingenieurs snel het belang van het fijn afstemmen van het model en het ontwikkelen van betere prompt engineering-technieken beseften om de codekwaliteit te verbeteren. In juli [introduceerden ze een verbeterd AI-model dat verder gaat dan Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) voor nog snellere suggesties.

Lees de berichten op volgorde om hun leertraject te volgen.

- **Mei 2023** | [GitHub Copilot wordt beter in het begrijpen van je code](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mei 2023** | [Binnen GitHub: Werken met de LLMs achter GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jun 2023** | [Hoe schrijf je betere prompts voor GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Jul 2023** | [.. GitHub Copilot gaat verder dan Codex met verbeterd AI-model](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Jul 2023** | [Een handleiding voor ontwikkelaars over prompt engineering en LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sep 2023** | [Hoe bouw je een zakelijke LLM-app: lessen van GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Je kunt ook hun [Engineering-blog](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) doorzoeken voor meer berichten zoals [deze](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) die laten zien hoe deze modellen en technieken worden _toegepast_ om real-world toepassingen aan te sturen.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Promptconstructie

We hebben gezien waarom prompt engineering belangrijk is – laten we nu begrijpen hoe prompts worden _geconstrueerd_ zodat we verschillende technieken kunnen evalueren voor effectievere promptontwerpen.

### Basisprompt

Laten we beginnen met de basisprompt: een tekstinvoer die naar het model wordt gestuurd zonder verdere context. Hier is een voorbeeld - als we de eerste paar woorden van het Amerikaanse volkslied naar de OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) sturen, wordt het antwoord direct _afgemaakt_ met de volgende regels, wat het basale voorspellend gedrag illustreert.

| Prompt (Invoer)       | Aanvulling (Uitvoer)                                                                                                                        |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see    | Het klinkt alsof je de tekst van "The Star-Spangled Banner," het volkslied van de Verenigde Staten, begint. De volledige tekst is ...       |

### Complexe Prompt

Laten we nu context en instructies toevoegen aan die basisprompt. De [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) stelt ons in staat een complexe prompt te maken als een verzameling van _berichten_ met:

- Invoer/uitvoerparen die _gebruikers_ invoer en _assistent_ reactie reflecteren.
- Systeembericht dat de context voor het gedrag of de persoonlijkheid van de assistent bepaalt.

De aanvraag is nu in de volgende vorm, waarbij de _tokenisatie_ effectief relevante informatie uit context en conversatie vastlegt. Door de systeemcontext te wijzigen kan de kwaliteit van de aanvullingen net zo sterk beïnvloed worden als door de gebruiker ingevoerde input.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Instructieprompt

In bovenstaande voorbeelden was de gebruikersprompt een eenvoudige tekstvraag die geïnterpreteerd kan worden als een verzoek om informatie. Met _instructiep prompts_ kunnen we die tekst gebruiken om een taak gedetailleerder te specificeren, waardoor de AI betere richtlijnen krijgt. Dit is een voorbeeld:

| Prompt (Invoer)                                                                                                                                                                                                                         | Aanvulling (Uitvoer)                                                                                                      | Instructietype      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Schrijf een beschrijving van de Amerikaanse Burgeroorlog                                                                                                                                                                                | _teruggegeven een eenvoudige paragraaf_                                                                                   | Simpel              |
| Schrijf een beschrijving van de Amerikaanse Burgeroorlog. Geef belangrijke data en gebeurtenissen en beschrijf hun betekenis                                                                                                        | _teruggegeven een paragraaf gevolgd door een lijst van belangrijke datums met beschrijvingen_                              | Complex             |
| Schrijf een beschrijving van de Amerikaanse Burgeroorlog in 1 alinea. Geef 3 opsommingstekens met belangrijke data en hun betekenis. Geef 3 opsommingstekens met belangrijke historische figuren en hun bijdragen. Retourneer het resultaat als een JSON-bestand | _levert uitgebreidere details op in een tekstvak, geformatteerd als JSON dat je kunt kopiëren naar een bestand en valideren_ | Complex. Geformatteerd. |

## Primaire inhoud

In de voorgaande voorbeelden was de prompt nog vrij open, waardoor het LLM zelf kon bepalen welk deel van de voorgetrainde dataset relevant was. Met het ontwerp-patroon _primaire inhoud_ wordt de invoertekst verdeeld in twee delen:

- een instructie (actie)
- relevante inhoud (die de actie beïnvloedt)

Hier is een voorbeeld waar de instructie is: "vat dit samen in 2 zinnen".

| Prompt (Invoer)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Aanvulling (Uitvoer)                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa van een duizendste van die van de zon, maar twee en een half keer die van alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog in de nachtelijke hemel zichtbaar zijn en is sinds voor de geschreven geschiedenis bekend bij oude beschavingen. Het is genoemd naar de Romeinse god Jupiter.[19] Als je vanaf de aarde naar Jupiter kijkt, kan het licht dat het reflecteert helder genoeg zijn om zichtbare schaduwen te werpen,[20] en is het gemiddeld het derde helderste natuurlijke object aan de nachtelijke hemel na de maan en Venus. <br/> **Vat dit samen in 2 korte zinnen.** | Jupiter, de vijfde planeet vanaf de zon, is de grootste in het zonnestelsel en staat bekend als een van de helderste objecten in de nachtelijke hemel. Genoemd naar de Romeinse god Jupiter, is het een gasreus met een massa die twee en een half keer groter is dan die van alle andere planeten samen. |

Het segment primaire inhoud kan op verschillende manieren worden gebruikt om effectievere instructies aan te sturen:

- **Voorbeelden** – in plaats van het model met een expliciete instructie te vertellen wat het moet doen, geef je voorbeelden van wat het moet doen en laat je het patroon afleiden.
- **Aanwijzingen** – volg de instructie met een "aanwijzing" die de aanvulling stimuleert en het model in een relevante richting wijst.
- **Sjablonen** – dit zijn herhaalbare 'recepten' voor prompts met placeholders (variabelen) die op maat kunnen worden gemaakt met data voor specifieke toepassingen.

Laten we deze in de praktijk bekijken.

### Voorbeelden gebruiken

Dit is een aanpak waarbij je de primaire inhoud gebruikt om het model "te voeden" met voorbeelden van de gewenste output voor een gegeven instructie, en het het patroon laat afleiden van de gewenste output. Afhankelijk van het aantal gegeven voorbeelden kunnen we zero-shot prompting, one-shot prompting, few-shot prompting etc. toepassen.

De prompt bestaat nu uit drie componenten:

- Een taakbeschrijving
- Een paar voorbeelden van de gewenste output
- Het begin van een nieuw voorbeeld (dat een impliciete taakbeschrijving wordt)

| Leerstijl   | Prompt (Invoer)                                                                                                                             | Aanvulling (Uitvoer)         |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| Zero-shot   | "De zon schijnt". Vertaal naar Spaans                                                                                                     | "El Sol está brillando".      |
| One-shot    | "De zon schijnt" => "El Sol está brillando". <br> "Het is een koude en winderige dag" =>                                                   | "Es un día frío y ventoso".   |
| Few-shot    | De speler rende de honken => Honkbal <br/> De speler sloeg een ace => Tennis <br/> De speler sloeg een zes => Cricket <br/> De speler maakte een slam-dunk => | Basketbal                    |
|             |                                                                                                                                              |                              |

Merk op dat we expliciete instructie ("Vertaal naar Spaans") moesten geven bij zero-shot prompting, maar dat die wordt afgeleid in het one-shot voorbeeld. Het few-shot voorbeeld toont hoe meer voorbeelden toevoegen modellen in staat stelt nauwkeurigere afleidingen te maken zonder extra instructies.

### Promptaanwijzingen

Een andere techniek om primaire inhoud te gebruiken is door _aanwijzingen_ te geven in plaats van voorbeelden. In dit geval geven we het model een zetje in de juiste richting door _het te starten_ met een fragment dat het gewenste antwoordformaat weergeeft. Het model "pakt dan de aanwijzing" om in die trant verder te gaan.

| Aantal aanwijzingen | Prompt (Invoer)                                                                                                                                                                                                                                                                                                                                                                                    | Aanvulling (Uitvoer)                                                                                                                                                                                                                                                                             |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                   | Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa van een duizendste van die van de zon, maar twee en een half keer die van alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog in de nachtelijke hemel zichtbaar zijn en is sinds voor de geschreven geschiedenis bekend bij oude beschavingen. <br/>**Vat dit samen**                                   | Jupiter is de grootste planeet in ons zonnestelsel en de vijfde vanaf de zon. Het is een gasreus met een massa van 1/1000 van de zon, maar zwaarder dan alle andere planeten samen. Oude beschavingen kennen Jupiter al lang, en het is gemakkelijk zichtbaar aan de nachtelijke hemel. |
| 1              | Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa van één duizendste van die van de zon, maar tweeënhalf keer die van alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog zichtbaar zijn aan de nachtelijke hemel en is sinds de oudheid bekend bij beschavingen, lang voor de geschreven geschiedenis. <br/>**Samenvatting** <br/> Wat we geleerd hebben is dat Jupiter | de vijfde planeet vanaf de zon is en de grootste in het zonnestelsel. Het is een gasreus met een massa van één duizendste van die van de zon, maar tweeënhalf keer die van alle andere planeten samen. Het is gemakkelijk zichtbaar met het blote oog en is sinds de oudheid bekend.                        |
| 2              | Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. Het is een gasreus met een massa van één duizendste van die van de zon, maar tweeënhalf keer die van alle andere planeten in het zonnestelsel samen. Jupiter is een van de helderste objecten die met het blote oog zichtbaar zijn aan de nachtelijke hemel en is sinds de oudheid bekend bij beschavingen, lang voor de geschreven geschiedenis. <br/>**Samenvatting** <br/> Top 3 Feiten Die We Hebben Geleerd:         | 1. Jupiter is de vijfde planeet vanaf de zon en de grootste in het zonnestelsel. <br/> 2. Het is een gasreus met een massa van één duizendste van die van de zon...<br/> 3. Jupiter is sinds de oudheid met het blote oog zichtbaar ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompt Templates

Een prompttemplate is een _voorgeprogrammeerd recept voor een prompt_ dat kan worden opgeslagen en hergebruikt indien nodig, om consistentere gebruikerservaringen op grote schaal te ondersteunen. In zijn eenvoudigste vorm is het gewoon een verzameling voorbeelden van prompts zoals [deze van OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) die zowel de interactieve promptcomponenten (berichten van gebruiker en systeem) als het API-gestuurde aanvraagformaat bieden - voor hergebruik.

In een complexere vorm zoals [dit voorbeeld van LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) bevat het _plaatsaanduidingen_ die kunnen worden vervangen door gegevens uit verschillende bronnen (gebruikersinvoer, systeemcontext, externe databronnen etc.) om de prompt dynamisch te genereren. Dit stelt ons in staat om een bibliotheek van herbruikbare prompts te maken die **programmatig** gebruikt kunnen worden voor consistente gebruikerservaringen op grote schaal.

Ten slotte ligt de echte waarde van templates in het vermogen om _promptbibliotheken_ te creëren en publiceren voor verticale toepassingsdomeinen - waarbij het prompttemplate nu _geoptimaliseerd_ is om context of voorbeelden te bevatten die relevant en accuraat zijn voor de doelgroep. De [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository is een uitstekend voorbeeld van deze aanpak, met een verzameling prompts voor het onderwijsdomein met nadruk op belangrijke doelen zoals lesplanning, curriculumontwerp, studentbegeleiding enz.

## Ondersteunende Content

Als we promptconstructie zien als het hebben van een instructie (taak) en een doel (primaire inhoud), dan is _secundaire content_ als extra context die we geven om de uitvoer op een bepaalde manier te **beïnvloeden**. Dit kan zijn afstemmingsparameters, formatteringsinstructies, onderwerpen-taxonomieën etc. die het model helpen de respons beter aan te passen aan de gewenste gebruikersdoelen of verwachtingen.

Bijvoorbeeld: Gegeven een cursuscatalogus met uitgebreide metadata (naam, beschrijving, niveau, metadata-tags, docent etc.) over alle beschikbare cursussen in het curriculum:

- kunnen we een instructie definiëren om "de cursuscatalogus voor herfst 2023 samen te vatten"
- kunnen we de primaire content gebruiken om enkele voorbeelden van de gewenste output te geven
- kunnen we de secundaire content gebruiken om de top 5 "tags" van belang te identificeren.

Nu kan het model een samenvatting geven in het formaat getoond door de voorbeelden - maar als een resultaat meerdere tags bevat, kan het prioriteit geven aan de 5 tags die in de secundaire content zijn aangegeven.

---

<!--
LESSON TEMPLATE:
Deze unit behandelt kernconcept #1.
Versterk het concept met voorbeelden en verwijzingen.

CONCEPT #3:
Prompttechnieken.
Wat zijn enkele basistechnieken voor promptontwerp?
Illustreer met oefeningen.
-->

## Beste Praktijken voor Prompts

Nu we weten hoe prompts gebouwd kunnen worden, kunnen we nadenken over hoe we ze _ontwerpen_ volgens beste praktijken. We kunnen dit in twee delen splitsen - de juiste _mindset_ hebben en de juiste _technieken_ toepassen.

### Mindset voor Prompt Engineering

Prompt Engineering is een proces van trial-and-error, dus houd drie algemene richtlijnen in gedachten:

1. **Domeinbegrip is belangrijk.** De nauwkeurigheid en relevantie van reacties is afhankelijk van het _domein_ waarin die app of gebruiker opereert. Pas je intuïtie en domeinexpertise toe om **technieken verder aan te passen**. Definieer bijvoorbeeld _domeinspecifieke persoonlijkheden_ in je systeem prompts, of gebruik _domeinspecifieke templates_ in je gebruikersprompts. Lever secundaire content die domeinspecifieke contexten weerspiegelt, of gebruik _domeinspecifieke aanwijzingen en voorbeelden_ om het model naar vertrouwde patronen te leiden.

2. **Modelbegrip is belangrijk.** We weten dat modellen van nature stochastisch zijn. Maar implementaties kunnen verschillen qua trainingsdata (voorgetrainde kennis), functionaliteiten (via API of SDK) en contentsoorten waarvoor ze geoptimaliseerd zijn (bijv. code vs afbeeldingen vs tekst). Begrijp de sterke en zwakke punten van het model dat je gebruikt, en gebruik die kennis om _taken te prioriteren_ of _aangepaste templates_ te bouwen die geoptimaliseerd zijn voor dat model.

3. **Iteratie & Validatie zijn belangrijk.** Modellen ontwikkelen zich snel, net als prompttechnieken. Als domeinexpert heb je mogelijk andere context of criteria voor _jouw_ specifieke toepassing die niet voor iedereen gelden. Gebruik prompt engineering tools en technieken om snel prompts te bouwen, daarna te itereren en de resultaten te valideren met je intuïtie en kennis. Leg je inzichten vast en maak een **kennisbank** (zoals promptbibliotheken) die anderen als nieuwe basis kunnen gebruiken voor snellere iteraties.

## Beste Praktijken

Laten we nu kijken naar veelgebruikte beste praktijken die worden aanbevolen door [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) en [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) experts.

| Wat                              | Waarom                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evalueer de nieuwste modellen.       | Nieuwe modelgeneraties hebben waarschijnlijk verbeterde functionaliteiten en kwaliteit - maar kunnen ook hogere kosten met zich meebrengen. Evalueer de impact en maak migratiekeuzes.                                                                                |
| Scheid instructies & context   | Controleer of jouw model/provider _scheidingstekens_ gebruikt om instructies, primaire en secundaire content duidelijker te onderscheiden. Dit helpt modellen om beter gewichten toe te kennen aan tokens.                                                         |
| Wees specifiek en duidelijk             | Geef meer details over de gewenste context, uitkomst, lengte, opmaak, stijl etc. Dit verbetert zowel kwaliteit als consistentie van antwoorden. Leg recepten vast in herbruikbare templates.                                                          |
| Wees beschrijvend, gebruik voorbeelden      | Modellen reageren vaak beter op een "show and tell" aanpak. Begin met een `zero-shot` instructie (geen voorbeelden) en verfijn met een `few-shot` aanpak, waarbij je enkele voorbeelden van de gewenste output geeft. Gebruik analogieën. |
| Gebruik aanwijzingen om antwoorden te starten | Zet het model op het goede spoor door een aanzet te geven met woorden of zinnen die het als beginpunt kan gebruiken.                                                                                                               |
| Herhaal waar nodig                       | Soms moet je het model herhalen, bijv. instructies voor en na de primaire content geven, of met een instructie én een cue werken. Itereer en valideer wat werkt.                                                         |
| Volgorde doet ertoe                     | De volgorde waarin informatie wordt gepresenteerd, kan de output beïnvloeden door recency bias. Probeer verschillende volgordes om te zien wat het beste werkt.                                                               |
| Geef het model een "uitweg"           | Geef het model een _fallback_ antwoord dat het kan geven als het de taak om welke reden dan ook niet kan voltooien. Dit verkleint de kans op onjuiste of verzonnen antwoorden.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Zoals bij elke beste praktijk geldt dat _jouw ervaring kan verschillen_ afhankelijk van model, taak en domein. Gebruik dit als startpunt en blijf itereren om te ontdekken wat voor jou het beste werkt. Evalueer continu je prompt engineering proces als er nieuwe modellen en tools verschijnen, met focus op schaalbaarheid en kwaliteit van antwoorden.

<!--
LESSON TEMPLATE:
Deze unit kan een programmeeruitdaging bevatten indien relevant.

UITDAGING:
Link naar een Jupyter Notebook waarin de programmeermodules leeg zijn, alleen instructies in commentaar.

OPLOSSING:
Link naar een ingevulde versie van dat Notebook met prompts en werkend resultaat, als voorbeeld.
-->

## Opdracht

Gefeliciteerd! Je bent aan het einde van de les gekomen! Tijd om een aantal concepten en technieken te testen met echte voorbeelden!

We gebruiken een Jupyter Notebook met oefeningen die je interactief kunt doorlopen. Je kunt het Notebook ook uitbreiden met eigen Markdown- en codecellen om zelfstandig ideeën en technieken te verkennen.

### Om te beginnen, fork de repo en

- (Aanbevolen) Start GitHub Codespaces
- (Alternatief) Clone de repo naar je lokale apparaat en gebruik Docker Desktop
- (Alternatief) Open het Notebook in je favoriete Notebook-runtime omgeving.

### Configureer daarna je omgevingsvariabelen

- Kopieer het `.env.copy` bestand in de root van de repo naar `.env` en vul de waarden in voor `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` en `AZURE_OPENAI_DEPLOYMENT`. Kom terug naar de [Learning Sandbox sectie](#leer-sandbox) om te leren hoe.

### Open nu het Jupyter Notebook

- Kies de runtime kernel. Als je optie 1 of 2 gebruikt, kies dan de standaard Python 3.10.x-kernel die in de dev container zit.

Je bent klaar om de oefeningen te doen. Er zijn hier geen _juiste of foute_ antwoorden - het gaat om uitproberen en ervaring opdoen met wat werkt voor een model en toepassingsdomein.

_Voor deze reden zijn er geen codeoplossingen in deze les. In plaats daarvan bevat het Notebook Markdown-cellen met de titel "Mijn Oplossing:" die een voorbeeldrespons tonen ter referentie._

 <!--
LESSON TEMPLATE:
Sluit de sectie af met een samenvatting en bronnen voor zelfstudie.
-->

## Kenniscontrole

Welke van de volgende is een goede prompt die redelijk goede best practices volgt?

1. Toon mij een afbeelding van een rode auto
2. Toon mij een afbeelding van een rode auto van het merk Volvo en model XC90 geparkeerd bij een klif met de zonsondergang
3. Toon mij een afbeelding van een rode auto van het merk Volvo en model XC90

A: 2 is de beste prompt omdat het details geeft over "wat" en in detail gaat (niet zomaar een auto, maar een specifiek merk en model) en ook de setting beschrijft. 3 is de tweede beste omdat het ook veel omschrijving bevat.

## 🚀 Uitdaging

Bekijk of je de "cue"-techniek kunt gebruiken met de prompt: Maak de zin af "Toon mij een afbeelding van een rode auto van het merk Volvo en ". Wat geeft het als antwoord, en hoe zou je dat verbeteren?

## Goed gedaan! Ga Door met Leren

Wil je meer weten over verschillende Prompt Engineering concepten? Ga naar de [vervolgpaginapagina](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om andere waardevolle bronnen over dit onderwerp te vinden.

Ga vervolgens naar les 5, waar we kijken naar [gevorderde prompttechnieken](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->