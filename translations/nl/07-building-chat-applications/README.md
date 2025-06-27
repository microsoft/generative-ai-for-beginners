<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea4bbe640847aafbbba14dae4625e9af",
  "translation_date": "2025-06-25T15:42:10+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "nl"
}
-->
# Generatieve AI-gestuurde Chattoepassingen Bouwen

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Nu we hebben gezien hoe we tekstgeneratie-apps kunnen bouwen, laten we eens kijken naar chattoepassingen.

Chattoepassingen zijn geïntegreerd in ons dagelijks leven en bieden meer dan alleen een middel voor informele gesprekken. Ze zijn essentiële onderdelen van klantenservice, technische ondersteuning en zelfs geavanceerde adviesystemen. Waarschijnlijk heb je niet zo lang geleden hulp gekregen van een chattoepassing. Naarmate we geavanceerdere technologieën zoals generatieve AI in deze platforms integreren, neemt de complexiteit toe en daarmee ook de uitdagingen.

Enkele vragen die we moeten beantwoorden zijn:

- **Het bouwen van de app**. Hoe bouwen we efficiënt en integreren we naadloos deze AI-gestuurde toepassingen voor specifieke gebruikssituaties?
- **Monitoring**. Hoe kunnen we, eenmaal geïmplementeerd, monitoren en ervoor zorgen dat de toepassingen op het hoogste kwaliteitsniveau functioneren, zowel qua functionaliteit als met inachtneming van de [zes principes van verantwoordelijke AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Naarmate we verder gaan in een tijdperk dat wordt gekenmerkt door automatisering en naadloze interacties tussen mens en machine, wordt het essentieel te begrijpen hoe generatieve AI de reikwijdte, diepgang en aanpasbaarheid van chattoepassingen transformeert. Deze les zal de aspecten van architectuur onderzoeken die deze complexe systemen ondersteunen, ingaan op de methodologieën voor het afstemmen ervan op domeinspecifieke taken en de meetwaarden en overwegingen evalueren die relevant zijn om verantwoordelijke AI-implementatie te waarborgen.

## Introductie

Deze les behandelt:

- Technieken voor het efficiënt bouwen en integreren van chattoepassingen.
- Hoe maatwerk en afstemming op toepassingen kunnen worden toegepast.
- Strategieën en overwegingen om chattoepassingen effectief te monitoren.

## Leerdoelen

Aan het einde van deze les kun je:

- Overwegingen beschrijven voor het bouwen en integreren van chattoepassingen in bestaande systemen.
- Chattoepassingen aanpassen voor specifieke gebruikssituaties.
- Belangrijke meetwaarden en overwegingen identificeren om de kwaliteit van AI-gestuurde chattoepassingen effectief te monitoren en te behouden.
- Ervoor zorgen dat chattoepassingen AI op verantwoorde wijze benutten.

## Integratie van Generatieve AI in Chattoepassingen

Het verbeteren van chattoepassingen met generatieve AI draait niet alleen om ze slimmer te maken; het gaat om het optimaliseren van hun architectuur, prestaties en gebruikersinterface om een kwalitatieve gebruikerservaring te bieden. Dit omvat het onderzoeken van de architectonische fundamenten, API-integraties en overwegingen voor de gebruikersinterface. Dit gedeelte is bedoeld om je een uitgebreide routekaart te bieden voor het navigeren door deze complexe landschappen, of je ze nu in bestaande systemen integreert of ze als zelfstandige platforms bouwt.

Aan het einde van dit gedeelte beschik je over de expertise die nodig is om chattoepassingen efficiënt te bouwen en te integreren.

### Chatbot of Chattoepassing?

Voordat we beginnen met het bouwen van chattoepassingen, laten we 'chatbots' vergelijken met 'AI-gestuurde chattoepassingen', die verschillende rollen en functionaliteiten vervullen. Het belangrijkste doel van een chatbot is het automatiseren van specifieke gesprekstaken, zoals het beantwoorden van veelgestelde vragen of het volgen van een pakket. Het wordt meestal aangestuurd door regelgebaseerde logica of complexe AI-algoritmen. Daarentegen is een AI-gestuurde chattoepassing een veel uitgebreidere omgeving die is ontworpen om verschillende vormen van digitale communicatie te vergemakkelijken, zoals tekst-, spraak- en videochats tussen menselijke gebruikers. Het kenmerkende kenmerk is de integratie van een generatief AI-model dat genuanceerde, mensachtige gesprekken simuleert en reacties genereert op basis van een breed scala aan invoer en contextuele signalen. Een generatieve AI-gestuurde chattoepassing kan deelnemen aan open domeindiscussies, zich aanpassen aan evoluerende gespreksscenario's en zelfs creatieve of complexe dialogen produceren.

De onderstaande tabel schetst de belangrijkste verschillen en overeenkomsten om ons te helpen hun unieke rollen in digitale communicatie te begrijpen.

| Chatbot                               | Generatieve AI-gestuurde Chattoepassing |
| ------------------------------------- | --------------------------------------- |
| Taakgericht en regelgebaseerd         | Contextbewust                           |
| Vaak geïntegreerd in grotere systemen | Kan één of meerdere chatbots hosten     |
| Beperkt tot geprogrammeerde functies  | Integreert generatieve AI-modellen      |
| Gespecialiseerde & gestructureerde interacties | In staat tot open domeindiscussies |

### Gebruikmaken van vooraf gebouwde functionaliteiten met SDK's en API's

Bij het bouwen van een chattoepassing is een geweldige eerste stap om te beoordelen wat er al beschikbaar is. Het gebruik van SDK's en API's om chattoepassingen te bouwen is een voordelige strategie om verschillende redenen. Door goed gedocumenteerde SDK's en API's te integreren, positioneer je je toepassing strategisch voor langdurig succes en pak je schaalbaarheids- en onderhoudsproblemen aan.

- **Versnelt het ontwikkelingsproces en vermindert overhead**: Door te vertrouwen op vooraf gebouwde functionaliteiten in plaats van het dure proces om ze zelf te bouwen, kun je je concentreren op andere aspecten van je toepassing die je misschien belangrijker vindt, zoals bedrijfslogica.
- **Betere prestaties**: Wanneer je functionaliteit vanaf nul bouwt, zul je jezelf uiteindelijk de vraag stellen: "Hoe schaalt het? Is deze toepassing in staat om een plotselinge toestroom van gebruikers aan te kunnen?" Goed onderhouden SDK's en API's hebben vaak ingebouwde oplossingen voor deze zorgen.
- **Eenvoudiger onderhoud**: Updates en verbeteringen zijn gemakkelijker te beheren, aangezien de meeste API's en SDK's eenvoudigweg een update van een bibliotheek vereisen wanneer een nieuwere versie wordt uitgebracht.
- **Toegang tot geavanceerde technologie**: Door modellen te gebruiken die zijn afgestemd en getraind op uitgebreide datasets, biedt je toepassing natuurlijke taalvaardigheden.

Toegang krijgen tot de functionaliteit van een SDK of API omvat meestal het verkrijgen van toestemming om de aangeboden diensten te gebruiken, wat vaak gebeurt via een unieke sleutel of authenticatietoken. We zullen de OpenAI Python Library gebruiken om te verkennen hoe dit eruit ziet. Je kunt het ook zelf proberen in het volgende [notebook voor OpenAI](../../../07-building-chat-applications/python/oai-assignment.ipynb) of [notebook voor Azure OpenAI Services](../../../07-building-chat-applications/python/aoai-assignment.ipynb) voor deze les.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Het bovenstaande voorbeeld gebruikt het GPT-3.5 Turbo-model om de prompt te voltooien, maar merk op dat de API-sleutel vooraf wordt ingesteld. Je zou een foutmelding ontvangen als je de sleutel niet instelt.

## Gebruikerservaring (UX)

Algemene UX-principes zijn van toepassing op chattoepassingen, maar hier zijn enkele aanvullende overwegingen die bijzonder belangrijk worden vanwege de betrokken machine learning-componenten.

- **Mechanisme voor het adresseren van ambiguïteit**: Generatieve AI-modellen genereren af en toe dubbelzinnige antwoorden. Een functie waarmee gebruikers om verduidelijking kunnen vragen kan nuttig zijn als ze met dit probleem worden geconfronteerd.
- **Contextbehoud**: Geavanceerde generatieve AI-modellen hebben de mogelijkheid om context binnen een gesprek te onthouden, wat een noodzakelijke troef kan zijn voor de gebruikerservaring. Gebruikers de mogelijkheid geven om context te beheren en te controleren verbetert de gebruikerservaring, maar introduceert het risico van het behouden van gevoelige gebruikersinformatie. Overwegingen over hoe lang deze informatie wordt opgeslagen, zoals het invoeren van een bewaarbeleid, kunnen de behoefte aan context in balans brengen met privacy.
- **Personalisatie**: Met het vermogen om te leren en zich aan te passen, bieden AI-modellen een gepersonaliseerde ervaring voor een gebruiker. Het afstemmen van de gebruikerservaring door middel van functies zoals gebruikersprofielen zorgt er niet alleen voor dat de gebruiker zich begrepen voelt, maar helpt ook bij hun zoektocht naar specifieke antwoorden, waardoor een efficiëntere en bevredigende interactie ontstaat.

Een voorbeeld van personalisatie is de "Aangepaste instructies" instellingen in OpenAI's ChatGPT. Hiermee kun je informatie over jezelf verstrekken die belangrijke context kan zijn voor je prompts. Hier is een voorbeeld van een aangepaste instructie.

### Microsoft's Systeembericht Framework voor Grote Taalmodellen

[Microsoft heeft richtlijnen gegeven](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) voor het schrijven van effectieve systeemberichten bij het genereren van reacties van LLM's, onderverdeeld in 4 gebieden:

1. Bepalen voor wie het model is, evenals zijn mogelijkheden en beperkingen.
2. Het outputformaat van het model definiëren.
3. Specifieke voorbeelden geven die het beoogde gedrag van het model demonstreren.
4. Extra gedragsregels bieden.

### Toegankelijkheid

Of een gebruiker nu visuele, auditieve, motorische of cognitieve beperkingen heeft, een goed ontworpen chattoepassing moet door iedereen bruikbaar zijn. De volgende lijst verdeelt specifieke functies die gericht zijn op het verbeteren van de toegankelijkheid voor verschillende gebruikersbeperkingen.

- **Functies voor Visuele Beperkingen**: Hoog contrast thema's en schaalbare tekst, compatibiliteit met schermlezers.
- **Functies voor Auditieve Beperkingen**: Tekst-naar-spraak en spraak-naar-tekst functies, visuele aanwijzingen voor audio meldingen.
- **Functies voor Motorische Beperkingen**: Ondersteuning voor navigatie met het toetsenbord, spraakopdrachten.
- **Functies voor Cognitieve Beperkingen**: Opties voor vereenvoudigde taal.

## Aanpassing en Fijnafstemming voor Domeinspecifieke Taalmodellen

Stel je een chattoepassing voor die de jargon van je bedrijf begrijpt en de specifieke vragen van zijn gebruikersbasis anticipeert. Er zijn een paar benaderingen die het vermelden waard zijn:

- **Gebruikmaken van DSL-modellen**. DSL staat voor domeinspecifieke taal. Je kunt een zogenaamd DSL-model gebruiken dat is getraind op een specifiek domein om zijn concepten en scenario's te begrijpen.
- **Fijnafstemming toepassen**. Fijnafstemming is het proces van verdere training van je model met specifieke gegevens.

## Aanpassing: Gebruikmaken van een DSL

Gebruikmaken van domeinspecifieke taalmodellen (DSL-modellen) kan de gebruikersbetrokkenheid verbeteren door gespecialiseerde, contextueel relevante interacties te bieden. Het is een model dat is getraind of fijngestemd om tekst te begrijpen en genereren die verband houdt met een specifiek vakgebied, industrie of onderwerp. Opties voor het gebruik van een DSL-model kunnen variëren van het trainen van een model vanaf nul tot het gebruik van reeds bestaande modellen via SDK's en API's. Een andere optie is fijnafstemming, wat inhoudt dat een bestaand voorgetraind model wordt aangepast voor een specifiek domein.

## Aanpassing: Fijnafstemming toepassen

Fijnafstemming wordt vaak overwogen wanneer een voorgetraind model tekortschiet in een gespecialiseerd domein of specifieke taak.

Bijvoorbeeld, medische vragen zijn complex en vereisen veel context. Wanneer een medisch professional een patiënt diagnosticeert, is dat gebaseerd op een verscheidenheid aan factoren zoals levensstijl of bestaande aandoeningen, en kan zelfs vertrouwen op recente medische tijdschriften om hun diagnose te valideren. In dergelijke genuanceerde scenario's kan een algemeen AI-chattoepassing geen betrouwbare bron zijn.

### Scenario: een medische toepassing

Overweeg een chattoepassing die is ontworpen om medische professionals te helpen door snelle verwijzingen naar behandelingsrichtlijnen, geneesmiddelinteracties of recente onderzoeksbevindingen te bieden.

Een algemeen model kan voldoende zijn voor het beantwoorden van basis medische vragen of het geven van algemeen advies, maar het kan moeite hebben met het volgende:

- **Zeer specifieke of complexe gevallen**. Bijvoorbeeld, een neuroloog kan de toepassing vragen: "Wat zijn de huidige beste praktijken voor het beheren van geneesmiddelresistente epilepsie bij pediatrische patiënten?"
- **Ontbrekende recente ontwikkelingen**. Een algemeen model kan moeite hebben om een actueel antwoord te geven dat de meest recente ontwikkelingen in neurologie en farmacologie omvat.

In dergelijke gevallen kan het fijnafstemmen van het model met een gespecialiseerd medisch dataset de mogelijkheid aanzienlijk verbeteren om deze complexe medische vragen nauwkeuriger en betrouwbaarder af te handelen. Dit vereist toegang tot een grote en relevante dataset die de domeinspecifieke uitdagingen en vragen vertegenwoordigt die moeten worden aangepakt.

## Overwegingen voor een Hoge Kwaliteit AI-gedreven Chatervaring

Dit gedeelte schetst de criteria voor "hoogwaardige" chattoepassingen, waaronder het vastleggen van bruikbare meetwaarden en het naleven van een kader dat AI-technologie op verantwoorde wijze benut.

### Belangrijke Meetwaarden

Om de hoogwaardige prestaties van een toepassing te behouden, is het essentieel om belangrijke meetwaarden en overwegingen bij te houden. Deze metingen zorgen niet alleen voor de functionaliteit van de toepassing, maar beoordelen ook de kwaliteit van het AI-model en de gebruikerservaring. Hieronder staat een lijst met basis-, AI- en gebruikerservaringsmetingen om te overwegen.

| Metric                        | Definitie                                                                                                             | Overwegingen voor Chatontwikkelaar                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Meet de tijd dat de toepassing operationeel en toegankelijk is voor gebruikers.                                        | Hoe minimaliseer je downtime?                                           |
| **Reactietijd**               | De tijd die de toepassing nodig heeft om te reageren op een gebruikersvraag.                                           | Hoe kun je de verwerking van vragen optimaliseren om de reactietijd te verbeteren? |
| **Precisie**                  | De verhouding van echte positieve voorspellingen tot het totale aantal positieve voorspellingen                        | Hoe ga je de precisie van je model valideren?                        |
| **Recall (Gevoeligheid)**     | De verhouding van echte positieve voorspellingen tot het werkelijke aantal positieven                                  | Hoe ga je recall meten en verbeteren?                                  |
| **F1 Score**                  | Het harmonisch gemiddelde van precisie en recall, dat de balans tussen beide in evenwicht houdt.                        | Wat is je doel F1 Score? Hoe ga je precisie en recall in balans houden?  |
| **Perplexiteit**              | Meet hoe goed de kansverdeling voorspeld door het model overeenkomt met de werkelijke verdeling van de data.            | Hoe ga je perplexiteit minimaliseren?                                         |
| **Gebruikerstevredenheid Meetwaarden** | Meet de perceptie van de gebruiker van de toepassing. Vaak vastgelegd via enquêtes.                                     | Hoe vaak ga je gebruikersfeedback verzamelen? Hoe ga je je aanpassen op basis daarvan? |
| **Foutpercentage**            | Het percentage fouten dat het model maakt in begrip of output.                                                          | Welke strategieën heb je in plaats om foutpercentages te verminderen?               |
| **Hercycli van retraining**   | De frequentie waarmee het model wordt bijgewerkt om nieuwe data en inzichten te integreren.                             | Hoe vaak ga je het model opnieuw trainen? Wat triggert een hertrainingscyclus?   |
| **Anomaliedetectie**          | Tools en technieken voor het identificeren van ongebruikelijke patronen die niet voldoen aan verwacht gedrag.           | Hoe ga je reageren op anomalieën?                                        |

### Implementatie van Verantwoordelijke AI-praktijken in Chattoepassingen

Microsoft's benadering van Verantwoordelijke AI heeft zes principes geïdentificeerd die AI-ontwikkeling en -gebruik zouden moeten leiden. Hieronder staan de principes, hun definitie en dingen die een chatontwikkelaar zou moeten overwegen en waarom ze belangrijk zijn.

| Principes             | Microsoft's Definitie                                | Overwegingen voor Chatontwikkelaar                                      | Waarom Het Belangrijk Is                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Eerlijkheid            | AI-systemen moeten alle mensen eerlijk behandelen.    | Zorg ervoor dat de chattoepassing niet discrimineert op basis van gebruikersdata.  | Om vertrouwen en inclusiviteit onder gebruikers op te bouwen; vermijdt juridische gevolgen.                |
| Betrouwbaarheid en Veiligheid | AI-systemen moeten betrouwbaar en veilig presteren.        | Implementeer testen en fail-safes om fouten en risico's te minimaliseren.         | Zorgt voor gebruikers tevredenheid en voorkomt mogelijke schade.                                 |
| Privacy en Veiligheid | AI-systemen moeten veilig zijn en privacy respecteren. | Implementeer sterke encryptie en databeveiligingsmaatregelen.              | Om gevoelige gebruikersdata te beschermen en te voldoen aan privacywetten.                         |
| Inclusiviteit          | AI-systemen moeten iedereen in staat stellen en mensen betrekken. | Ontwerp UI/UX die toegankelijk en gebruiksvriendelijk is voor diverse doelgroepen. | Zorgt ervoor dat een breder scala aan mensen de toepassing effectief kan gebruiken.                   |
| Transparantie          | AI-systemen moeten begrijpelijk zijn.                  | Bied duidelijke documentatie en redenering voor AI-antwoorden.            | Gebruikers hebben meer vertrouwen in een systeem als ze kunnen begrijpen hoe beslissingen worden genomen. |
| Verantwoordelijkheid   | Mensen moeten verantwoordelijk zijn voor AI-systemen.  | Stel een duidelijk proces in voor het auditen en verbeteren van AI-beslissingen.     | Maakt voortdurende verbetering en corrigerende maatregelen mogelijk in geval van fouten.               |

## Opdracht

Zie [opdracht](../../../07-building-chat-applications/python) het zal je door een reeks oefeningen leiden, van het uitvoeren van je eerste chatprompts tot het classificeren en samenvatten van tekst en meer. Merk op dat de opdrachten beschikbaar zijn in verschillende programmeertalen!

## Geweldig Werk! Ga Verder met de Reis

Na het voltooien van deze les, bekijk onze [Generatieve AI Leercollectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder te verdiepen!

Ga naar Les 8 om te zien hoe je kunt beginnen met [zoektoepassingen bouwen](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.