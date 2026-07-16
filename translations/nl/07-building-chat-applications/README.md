# Het bouwen van chatapplicaties aangedreven door generatieve AI

[![Het bouwen van chatapplicaties aangedreven door generatieve AI](../../../translated_images/nl/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Nu we hebben gezien hoe we tekstgeneratie-apps kunnen bouwen, laten we eens kijken naar chatapplicaties.

Chatapplicaties zijn geïntegreerd in ons dagelijks leven en bieden meer dan alleen een middel voor informele gesprekken. Ze maken integraal deel uit van klantenservice, technische ondersteuning en zelfs geavanceerde adviserende systemen. Het is waarschijnlijk dat je onlangs nog hulp hebt gekregen van een chatapplicatie. Naarmate we geavanceerdere technologieën zoals generatieve AI in deze platforms integreren, neemt de complexiteit toe en daarmee ook de uitdagingen.

Enkele vragen die beantwoord moeten worden zijn:

- **Het bouwen van de app**. Hoe bouwen en integreren we deze AI-gestuurde applicaties efficiënt en naadloos voor specifieke gebruikssituaties?
- **Monitoring**. Hoe kunnen we na uitrol de applicaties monitoren en ervoor zorgen dat ze van de hoogste kwaliteit zijn, zowel qua functionaliteit als in overeenstemming met de [zes principes van verantwoord AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Nu we verder gaan in een tijdperk dat wordt gekenmerkt door automatisering en naadloze mens-machine-interacties, wordt het essentieel om te begrijpen hoe generatieve AI de reikwijdte, diepgang en aanpasbaarheid van chatapplicaties verandert. Deze les onderzoekt de architectonische aspecten die deze complexe systemen ondersteunen, de methoden om ze fijn af te stemmen voor domeinspecifieke taken, en de relevante meetwaarden en overwegingen voor verantwoord gebruik van AI.

## Introductie

Deze les behandelt:

- Technieken om chatapplicaties efficiënt te bouwen en te integreren.
- Hoe aanpassing en fijn afstemmen toe te passen op applicaties.
- Strategieën en overwegingen om chatapplicaties effectief te monitoren.

## Leerdoelen

Aan het einde van deze les kun je:

- Overwegingen beschrijven voor het bouwen en integreren van chatapplicaties in bestaande systemen.
- Chatapplicaties aanpassen voor specifieke gebruikssituaties.
- Belangrijke meetwaarden en overwegingen identificeren om AI-gestuurde chatapplicaties effectief te monitoren en de kwaliteit te waarborgen.
- Ervoor zorgen dat chatapplicaties AI op een verantwoorde manier gebruiken.

## Generatieve AI integreren in chatapplicaties

Het verbeteren van chatapplicaties met generatieve AI draait niet alleen om ze slimmer maken; het gaat om het optimaliseren van de architectuur, prestaties en gebruikersinterface om een kwalitatieve gebruikerservaring te leveren. Dit omvat het onderzoeken van de architectonische fundamenten, API-integraties en overwegingen voor de gebruikersinterface. Deze sectie biedt je een uitgebreide routekaart om door deze complexe landschappen te navigeren, of je ze nu aansluit op bestaande systemen of als zelfstandige platforms bouwt.

Aan het einde van deze sectie ben je uitgerust met de expertise om chatapplicaties efficiënt te bouwen en te integreren.

### Chatbot of chatapplicatie?

Voordat we duiken in het bouwen van chatapplicaties, laten we 'chatbots' vergelijken met 'AI-gestuurde chatapplicaties', die verschillende rollen en functionaliteiten hebben. Het hoofddoel van een chatbot is het automatiseren van specifieke conversatietaken, zoals het beantwoorden van veelgestelde vragen of het volgen van een pakket. Het wordt typisch aangedreven door regelgebaseerde logica of complexe AI-algoritmes. Daarentegen is een AI-gestuurde chatapplicatie een veel uitgebreidere omgeving die verschillende vormen van digitale communicatie mogelijk maakt, zoals tekst-, spraak- en videogesprekken tussen menselijke gebruikers. Het onderscheidende kenmerk is de integratie van een generatief AI-model dat genuanceerde, mensachtige gesprekken simuleert, en respons genereert op basis van een brede variëteit aan input en contextuele aanwijzingen. Een generatief AI-gestuurde chatapplicatie kan open domein gesprekken voeren, zich aanpassen aan evoluerende conversatiecontexten en zelfs creatieve of complexe dialogen produceren.

De onderstaande tabel geeft de belangrijkste verschillen en overeenkomsten weer om hun unieke rollen in digitale communicatie te begrijpen.

| Chatbot                               | Generatieve AI-Gestuurde Chatapplicatie |
| ------------------------------------- | -------------------------------------- |
| Taakgericht en regelgebaseerd         | Contextbewust                           |
| Vaak geïntegreerd in grotere systemen | Kan één of meerdere chatbots hosten    |
| Beperkt tot geprogrammeerde functies  | Integreert generatieve AI-modellen     |
| Gespecialiseerde en gestructureerde interacties | In staat tot open-domein discussies    |

### Gebruikmaken van vooraf gebouwde functionaliteiten met SDK's en API's

Bij het bouwen van een chatapplicatie is een goede eerste stap beoordelen wat er al bestaat. Het gebruik van SDK's en API's om chatapplicaties te bouwen is een voordelige strategie om verschillende redenen. Door goed gedocumenteerde SDK's en API's te integreren, positioneer je je applicatie strategisch voor langdurig succes, waarbij schaalbaarheid en onderhoud aan bod komen.

- **Versnelt het ontwikkelproces en vermindert overhead**: Vertrouwen op vooraf gebouwde functionaliteiten in plaats van ze zelf te ontwikkelen stelt je in staat om je te richten op andere aspecten van je applicatie die je belangrijker vindt, zoals bedrijfslogica.
- **Betere prestaties**: Bij het bouwen van functionaliteit vanaf nul vraag je je uiteindelijk af "Hoe schaalt dit? Is deze applicatie in staat om een plotselinge toestroom van gebruikers aan?" Goed onderhouden SDK's en API's hebben vaak ingebouwde oplossingen voor deze zorgen.
- **Gemakkelijker onderhoud**: Updates en verbeteringen zijn eenvoudiger te beheren, omdat de meeste API's en SDK's simpelweg een update van een bibliotheek vereisen wanneer er een nieuwe versie uitkomt.
- **Toegang tot geavanceerde technologie**: Gebruikmaken van modellen die zijn aangepast en getraind op uitgebreide datasets levert je applicatie natuurlijke taalvaardigheden op.

Toegang krijgen tot functionaliteiten van een SDK of API vereist doorgaans toestemming om de aangeboden diensten te gebruiken, vaak via een unieke sleutel of authenticatietoken. We gebruiken de OpenAI Python Library om te zien hoe dit eruitziet. Je kunt het zelf ook uitproberen in het volgende [notebook voor OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) of [notebook voor Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) voor deze les.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Het bovenstaande voorbeeld gebruikt het GPT-4o mini-model met de Responses API om de prompt te voltooien, maar let op dat de API-sleutel vooraf is ingesteld. Je krijgt een foutmelding als je de sleutel niet instelt.

## Gebruikerservaring (UX)

Algemene UX-principes zijn van toepassing op chatapplicaties, maar hier zijn enkele extra overwegingen die bijzonder belangrijk worden door de betrokken machine learning-componenten.

- **Mechanisme voor het aanpakken van ambiguïteit**: Generatieve AI-modellen genereren af en toe dubbelzinnige antwoorden. Een functie waarmee gebruikers om verduidelijking kunnen vragen kan nuttig zijn als ze dit probleem tegenkomen.
- **Contextbehoud**: Geavanceerde generatieve AI-modellen kunnen context binnen een gesprek onthouden, wat een noodzakelijk voordeel kan zijn voor de gebruikerservaring. Gebruikers de mogelijkheid geven om context te beheren verbetert de ervaring, maar brengt ook het risico met zich mee van het bewaren van gevoelige gebruikersinformatie. Overwegingen over hoe lang deze informatie wordt opgeslagen, zoals het invoeren van een bewaarbeleid, kunnen de behoefte aan context afwegen tegen privacy.
- **Personalisatie**: Met het vermogen om te leren en zich aan te passen, bieden AI-modellen een individuele ervaring voor een gebruiker. Het afstemmen van de gebruikerservaring via functies zoals gebruikersprofielen zorgt er niet alleen voor dat de gebruiker zich begrepen voelt, maar helpt ook bij het vinden van specifieke antwoorden, wat leidt tot een efficiëntere en bevredigende interactie.

Een voorbeeld van personalisatie is de instelling "Aangepaste instructies" in OpenAI's ChatGPT. Hiermee kun je informatie over jezelf geven die belangrijke context kan zijn voor je prompts. Hier is een voorbeeld van een aangepaste instructie.

![Aangepaste Instructies Instellingen in ChatGPT](../../../translated_images/nl/custom-instructions.b96f59aa69356fcf.webp)

Dit "profiel" vraagt ChatGPT om een lesplan over gekoppelde lijsten te maken. Merk op dat ChatGPT rekening houdt met het feit dat de gebruiker mogelijk een diepgaander lesplan wil, op basis van haar ervaring.

![Een prompt in ChatGPT voor een lesplan over gekoppelde lijsten](../../../translated_images/nl/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsofts System Message Framework voor Grote Taalmodellen

[Microsoft heeft richtlijnen gegeven](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) voor het schrijven van effectieve systeemberichten bij het genereren van antwoorden van LLM's, onderverdeeld in 4 gebieden:

1. Definiëren voor wie het model bedoeld is, evenals de mogelijkheden en beperkingen.
2. Het outputformaat van het model definiëren.
3. Specifieke voorbeelden geven die het beoogde gedrag van het model demonstreren.
4. Extra gedragslijnen bieden.

### Toegankelijkheid

Of een gebruiker nu visuele, auditieve, motorische of cognitieve beperkingen heeft, een goed ontworpen chatapplicatie moet door iedereen te gebruiken zijn. De volgende lijst specificeert kenmerken die gericht zijn op het verbeteren van toegankelijkheid voor diverse gebruikersbeperkingen.

- **Kenmerken voor visuele beperking**: Thema's met hoog contrast en aanpasbare tekst, schermlezer-compatibiliteit.
- **Kenmerken voor auditieve beperking**: Tekst-naar-spraak en spraak-naar-tekst functies, visuele aanwijzingen voor audio meldingen.
- **Kenmerken voor motorische beperking**: Ondersteuning voor navigatie via toetsenbord, spraakopdrachten.
- **Kenmerken voor cognitieve beperking**: Opties voor vereenvoudigde taal.

## Aanpassingen en fijn afstemmen voor domeinspecifieke taalmodellen

Stel je een chatapplicatie voor die de jargon van jouw bedrijf begrijpt en de specifieke vragen voorspelt die de gebruikers vaak stellen. Er zijn een paar benaderingen die de moeite waard zijn om te noemen:

- **Gebruik maken van DSL-modellen**. DSL staat voor domeinspecifieke taal. Je kunt een DSL-model gebruiken dat is getraind op een bepaald domein om de concepten en scenario's ervan te begrijpen.
- **Fijn afstemmen toepassen**. Fijn afstemmen is het proces van het verder trainen van je model met specifieke data.

## Aanpassing: Gebruik maken van een DSL

Het gebruik van domeinspecifieke taalmodellen (DSL-modellen) kan de gebruikersbetrokkenheid vergroten door gespecialiseerde, contextueel relevante interacties te bieden. Het is een model dat getraind of fijn afgestemd is om tekst te begrijpen en te genereren gerelateerd aan een specifiek vakgebied, industrie of onderwerp. Opties voor het gebruik van een DSL-model variëren van het trainen van een model vanaf nul, tot het gebruiken van bestaande via SDK's en API's. Een andere optie is fijn afstemmen, waarbij een bestaand voorgetraind model wordt aangepast voor een specifiek domein.

## Aanpassing: Fijn afstemmen toepassen

Fijn afstemmen wordt vaak overwogen wanneer een voorgetraind model tekortschiet in een gespecialiseerd domein of specifieke taak.

Bijvoorbeeld, medische vragen zijn complex en vereisen veel context. Wanneer een medisch professional een patiënt diagnosticeert, baseert die zich op diverse factoren zoals levensstijl of bestaande aandoeningen, en kan zelfs recente medische tijdschriften gebruiken om de diagnose te valideren. In zulke genuanceerde scenario's kan een AI-chatapplicatie voor algemeen gebruik geen betrouwbare bron zijn.

### Scenario: een medische applicatie

Denk aan een chatapplicatie ontworpen om medische beoefenaars te helpen door snelle verwijzingen te bieden naar behandelingsrichtlijnen, medicijninteracties of recente onderzoeksresultaten.

Een algemeen model kan geschikt zijn voor het beantwoorden van basisvragen over gezondheid of het geven van algemeen advies, maar kan moeite hebben met het volgende:

- **Zeer specifieke of complexe gevallen**. Bijvoorbeeld, een neuroloog kan de applicatie vragen: "Wat zijn de huidige beste praktijken voor het behandelen van medicijnresistente epilepsie bij pediatrische patiënten?"
- **Ontbreken van recente ontwikkelingen**. Een algemeen model kan moeite hebben om een actueel antwoord te geven dat de nieuwste ontwikkelingen in neurologie en farmacologie integreert.

In dergelijke gevallen kan het fijn afstemmen van het model met een gespecialiseerde medische dataset de nauwkeurigheid en betrouwbaarheid waarmee het complexe medische vragen behandelt aanzienlijk verbeteren. Dit vereist toegang tot een grote en relevante dataset die de domeinspecifieke uitdagingen en vragen vertegenwoordigt die moeten worden aangepakt.

## Overwegingen voor een hoogwaardige AI-aangedreven chatervaring

Deze sectie beschrijft de criteria voor "hoogwaardige" chatapplicaties, waaronder het vastleggen van bruikbare meetwaarden en het naleven van een raamwerk dat AI-technologie verantwoord inzet.

### Belangrijke meetwaarden

Om de hoge kwaliteit van een applicatie te behouden, is het essentieel om sleutelmetrieken en overwegingen bij te houden. Deze metingen waarborgen niet alleen de functionaliteit van de applicatie, maar evalueren ook de kwaliteit van het AI-model en de gebruikerservaring. Hieronder staat een lijst met basis-, AI- en gebruikerservaringsmetingen om te overwegen.

| Metriek                      | Definitie                                                                                                         | Overwegingen voor de Chat Ontwikkelaar                           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Uptime**                   | Meet de tijd dat de applicatie operationeel en toegankelijk is voor gebruikers.                                  | Hoe minimaliseer je uitvaltijd?                                  |
| **Reactietijd**              | De tijd die de applicatie nodig heeft om te reageren op een gebruikersvraag.                                    | Hoe optimaliseer je queryverwerking om de reactietijd te verbeteren? |
| **Precisie**                 | De verhouding van ware positieve voorspellingen tot het totale aantal positieve voorspellingen.                  | Hoe valideren je de precisie van je model?                       |
| **Recall (Gevoeligheid)**    | De verhouding van ware positieve voorspellingen tot het daadwerkelijke aantal positieven.                         | Hoe meet en verbeter je recall?                                  |
| **F1-score**                 | De harmonische gemiddelde van precisie en recall, die het compromis tussen beide balanceert.                      | Wat is je streef-F1-score? Hoe balanceer je precisie en recall? |
| **Perplexity**               | Meet hoe goed de waarschijnlijkheidsverdeling voorspeld door het model overeenkomt met de daadwerkelijke data.   | Hoe minimaliseer je perplexity?                                 |
| **Gebruikerstevredenheidsmetingen** | Meet de perceptie van de gebruiker over de applicatie. Vaak vastgelegd via enquêtes.                         | Hoe vaak verzamel je gebruikersfeedback? Hoe pas je hierop aan? |
| **Foutpercentage**           | Het percentage fouten dat het model maakt in begrip of output.                                                   | Welke strategieën heb je om foutpercentages te verminderen?      |
| **Hertrainingscycli**        | De frequentie waarmee het model wordt bijgewerkt met nieuwe data en inzichten.                                  | Hoe vaak train je het model opnieuw? Wat triggert een hertrainingscyclus? |

| **Anomaliedetectie**         | Hulpmiddelen en technieken voor het identificeren van ongewone patronen die niet overeenkomen met verwacht gedrag.              | Hoe ga je reageren op anomalieën?                                        |

### Verantwoordelijke AI-praktijken implementeren in chatapplicaties

De aanpak van Microsoft voor Verantwoordelijke AI heeft zes principes vastgesteld die de ontwikkeling en het gebruik van AI moeten sturen. Hieronder staan de principes, hun definitie, en zaken waar een chatontwikkelaar rekening mee moet houden en waarom ze dit serieus moeten nemen.

| Principes              | Definitie van Microsoft                               | Overwegingen voor Chatontwikkelaar                                    | Waarom het belangrijk is                                                            |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Eerlijkheid            | AI-systemen moeten alle mensen eerlijk behandelen.   | Zorg ervoor dat de chatapplicatie niet discrimineert op basis van gebruikersgegevens. | Om vertrouwen en inclusiviteit onder gebruikers op te bouwen; vermijdt juridische gevolgen. |
| Betrouwbaarheid en Veiligheid | AI-systemen moeten betrouwbaar en veilig presteren.      | Implementeer tests en failsafes om fouten en risico’s te minimaliseren. | Zorgt voor tevredenheid bij gebruikers en voorkomt mogelijke schade.                |
| Privacy en Veiligheid  | AI-systemen moeten veilig zijn en privacy respecteren. | Implementeer sterke encryptie en gegevensbeschermingsmaatregelen.    | Om gevoelige gebruikersgegevens te beschermen en te voldoen aan privacywetgeving.  |
| Inclusiviteit          | AI-systemen moeten iedereen in staat stellen en mensen betrekken. | Ontwerp een UI/UX die toegankelijk en gebruiksvriendelijk is voor diverse doelgroepen. | Zorgt ervoor dat een bredere groep mensen de applicatie effectief kan gebruiken.    |
| Transparantie          | AI-systemen moeten begrijpelijk zijn.                 | Zorg voor duidelijke documentatie en uitleg bij AI-reacties.         | Gebruikers vertrouwen een systeem sneller als ze begrijpen hoe beslissingen worden genomen. |
| Verantwoordingsplicht   | Mensen moeten verantwoordelijk zijn voor AI-systemen. | Stel een duidelijk proces vast voor het auditen en verbeteren van AI-beslissingen. | Maakt voortdurende verbetering en corrigerende maatregelen mogelijk bij fouten.    |

## Opdracht

Zie de [opdracht](../../../07-building-chat-applications/python). Deze leidt je door een reeks oefeningen, van het uitvoeren van je eerste chatprompts tot het classificeren en samenvatten van tekst en meer. Let op: de opdrachten zijn beschikbaar in verschillende programmeertalen!

## Goed gedaan! Ga door met de reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning-collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder te vergroten!

Ga naar Les 8 om te zien hoe je kunt beginnen met [het bouwen van zoekapplicaties](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->