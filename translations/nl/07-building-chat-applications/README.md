<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-17T19:56:16+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "nl"
}
-->
# Generatieve AI-gestuurde chatapplicaties bouwen

[![Generatieve AI-gestuurde chatapplicaties bouwen](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.nl.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Nu we hebben gezien hoe we tekstgeneratie-apps kunnen bouwen, laten we eens kijken naar chatapplicaties.

Chatapplicaties zijn een integraal onderdeel van ons dagelijks leven geworden en bieden meer dan alleen een middel voor informele gesprekken. Ze zijn essentieel voor klantenservice, technische ondersteuning en zelfs geavanceerde adviesdiensten. Waarschijnlijk heb je niet zo lang geleden hulp gekregen van een chatapplicatie. Naarmate we meer geavanceerde technologieën zoals generatieve AI in deze platforms integreren, neemt de complexiteit toe, evenals de uitdagingen.

Enkele vragen die we moeten beantwoorden zijn:

- **De app bouwen**. Hoe bouwen en integreren we deze AI-gestuurde applicaties efficiënt voor specifieke toepassingen?
- **Monitoring**. Hoe kunnen we, eenmaal geïmplementeerd, ervoor zorgen dat de applicaties op het hoogste kwaliteitsniveau functioneren, zowel qua functionaliteit als in overeenstemming met de [zes principes van verantwoordelijke AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Nu we verder gaan in een tijdperk dat wordt gekenmerkt door automatisering en naadloze interacties tussen mens en machine, wordt het essentieel om te begrijpen hoe generatieve AI de reikwijdte, diepgang en aanpasbaarheid van chatapplicaties transformeert. Deze les onderzoekt de aspecten van architectuur die deze complexe systemen ondersteunen, verdiept zich in de methodologieën voor het afstemmen ervan op specifieke domeintaken en evalueert de statistieken en overwegingen die relevant zijn voor het waarborgen van een verantwoorde AI-implementatie.

## Introductie

Deze les behandelt:

- Technieken voor het efficiënt bouwen en integreren van chatapplicaties.
- Hoe maatwerk en afstemming op applicaties toe te passen.
- Strategieën en overwegingen om chatapplicaties effectief te monitoren.

## Leerdoelen

Aan het einde van deze les kun je:

- Overwegingen beschrijven voor het bouwen en integreren van chatapplicaties in bestaande systemen.
- Chatapplicaties aanpassen voor specifieke toepassingen.
- Belangrijke statistieken en overwegingen identificeren om de kwaliteit van AI-gestuurde chatapplicaties effectief te monitoren en te behouden.
- Zorgen dat chatapplicaties AI op een verantwoorde manier benutten.

## Generatieve AI integreren in chatapplicaties

Het verbeteren van chatapplicaties met generatieve AI draait niet alleen om het slimmer maken ervan; het gaat ook om het optimaliseren van hun architectuur, prestaties en gebruikersinterface om een kwalitatieve gebruikerservaring te bieden. Dit omvat het onderzoeken van de architectonische fundamenten, API-integraties en gebruikersinterface-overwegingen. Dit gedeelte biedt een uitgebreide routekaart om deze complexe landschappen te navigeren, of je ze nu in bestaande systemen integreert of als zelfstandige platforms bouwt.

Aan het einde van dit gedeelte ben je uitgerust met de expertise die nodig is om chatapplicaties efficiënt te bouwen en te integreren.

### Chatbot of chatapplicatie?

Voordat we ingaan op het bouwen van chatapplicaties, laten we 'chatbots' vergelijken met 'AI-gestuurde chatapplicaties', die verschillende rollen en functionaliteiten vervullen. Het belangrijkste doel van een chatbot is het automatiseren van specifieke gesprekstaken, zoals het beantwoorden van veelgestelde vragen of het volgen van een pakket. Het wordt meestal aangestuurd door regelgebaseerde logica of complexe AI-algoritmen. Een AI-gestuurde chatapplicatie daarentegen is een veel uitgebreider platform dat verschillende vormen van digitale communicatie faciliteert, zoals tekst-, spraak- en videochats tussen menselijke gebruikers. Het onderscheidende kenmerk is de integratie van een generatief AI-model dat genuanceerde, mensachtige gesprekken simuleert en reacties genereert op basis van een breed scala aan input en contextuele aanwijzingen. Een generatieve AI-gestuurde chatapplicatie kan deelnemen aan open domeindiscussies, zich aanpassen aan evoluerende gesprekscontexten en zelfs creatieve of complexe dialogen produceren.

De onderstaande tabel schetst de belangrijkste verschillen en overeenkomsten om ons te helpen hun unieke rollen in digitale communicatie te begrijpen.

| Chatbot                               | Generatieve AI-gestuurde chatapplicatie |
| ------------------------------------- | -------------------------------------- |
| Taakgericht en regelgebaseerd         | Contextbewust                          |
| Vaak geïntegreerd in grotere systemen | Kan één of meerdere chatbots hosten    |
| Beperkt tot geprogrammeerde functies  | Integreert generatieve AI-modellen     |
| Gespecialiseerde & gestructureerde interacties | In staat tot open domeindiscussies     |

### Gebruik maken van vooraf gebouwde functionaliteiten met SDK's en API's

Bij het bouwen van een chatapplicatie is een goede eerste stap om te beoordelen wat er al beschikbaar is. Het gebruik van SDK's en API's om chatapplicaties te bouwen is een voordelige strategie om verschillende redenen. Door goed gedocumenteerde SDK's en API's te integreren, positioneer je je applicatie strategisch voor langdurig succes en pak je schaalbaarheids- en onderhoudsproblemen aan.

- **Versnelt het ontwikkelproces en vermindert overhead**: Door te vertrouwen op vooraf gebouwde functionaliteiten in plaats van het dure proces om ze zelf te bouwen, kun je je richten op andere aspecten van je applicatie die je belangrijker vindt, zoals bedrijfslogica.
- **Betere prestaties**: Bij het zelf bouwen van functionaliteit vraag je je uiteindelijk af: "Hoe schaalbaar is het? Kan deze applicatie een plotselinge toestroom van gebruikers aan?" Goed onderhouden SDK's en API's hebben vaak ingebouwde oplossingen voor deze zorgen.
- **Eenvoudiger onderhoud**: Updates en verbeteringen zijn gemakkelijker te beheren, aangezien de meeste API's en SDK's simpelweg een update van een bibliotheek vereisen wanneer een nieuwere versie wordt uitgebracht.
- **Toegang tot geavanceerde technologie**: Door gebruik te maken van modellen die zijn afgestemd en getraind op uitgebreide datasets, krijgt je applicatie natuurlijke taalvaardigheden.

Toegang krijgen tot de functionaliteit van een SDK of API houdt meestal in dat je toestemming krijgt om de aangeboden diensten te gebruiken, vaak via een unieke sleutel of authenticatietoken. We gebruiken de OpenAI Python Library om te verkennen hoe dit eruitziet. Je kunt dit ook zelf proberen in de volgende [notebook voor OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) of [notebook voor Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) voor deze les.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Het bovenstaande voorbeeld gebruikt het GPT-3.5 Turbo-model om de prompt te voltooien, maar let op dat de API-sleutel vooraf wordt ingesteld. Je zou een foutmelding krijgen als je de sleutel niet instelt.

## Gebruikerservaring (UX)

Algemene UX-principes zijn van toepassing op chatapplicaties, maar hier zijn enkele aanvullende overwegingen die bijzonder belangrijk worden vanwege de machine learning-componenten.

- **Mechanisme om ambiguïteit aan te pakken**: Generatieve AI-modellen genereren soms dubbelzinnige antwoorden. Een functie waarmee gebruikers om verduidelijking kunnen vragen, kan nuttig zijn als ze dit probleem tegenkomen.
- **Contextbehoud**: Geavanceerde generatieve AI-modellen hebben de mogelijkheid om context binnen een gesprek te onthouden, wat een noodzakelijke troef kan zijn voor de gebruikerservaring. Gebruikers de mogelijkheid geven om context te beheren en te controleren verbetert de gebruikerservaring, maar introduceert het risico van het bewaren van gevoelige gebruikersinformatie. Overwegingen over hoe lang deze informatie wordt opgeslagen, zoals het introduceren van een retentiebeleid, kunnen de behoefte aan context in balans brengen met privacy.
- **Personalisatie**: Met de mogelijkheid om te leren en zich aan te passen, bieden AI-modellen een geïndividualiseerde ervaring voor een gebruiker. Het aanpassen van de gebruikerservaring via functies zoals gebruikersprofielen zorgt er niet alleen voor dat de gebruiker zich begrepen voelt, maar helpt ook bij het vinden van specifieke antwoorden, waardoor een efficiëntere en bevredigende interactie ontstaat.

Een voorbeeld van personalisatie is de instelling "Aangepaste instructies" in OpenAI's ChatGPT. Hiermee kun je informatie over jezelf verstrekken die mogelijk belangrijke context is voor je prompts. Hier is een voorbeeld van een aangepaste instructie.

![Instellingen voor aangepaste instructies in ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.nl.png)

Dit "profiel" vraagt ChatGPT om een lesplan te maken over linked lists. Merk op dat ChatGPT rekening houdt met het feit dat de gebruiker mogelijk een meer diepgaand lesplan wil op basis van haar ervaring.

![Een prompt in ChatGPT voor een lesplan over linked lists](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.nl.png)

### Microsoft's System Message Framework voor grote taalmodellen

[Microsoft heeft richtlijnen gegeven](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) voor het schrijven van effectieve systeemberichten bij het genereren van reacties van LLM's, onderverdeeld in 4 gebieden:

1. Definieer voor wie het model is, evenals zijn mogelijkheden en beperkingen.
2. Definieer het uitvoerformaat van het model.
3. Geef specifieke voorbeelden die het beoogde gedrag van het model demonstreren.
4. Bied aanvullende gedragsrichtlijnen.

### Toegankelijkheid

Of een gebruiker nu visuele, auditieve, motorische of cognitieve beperkingen heeft, een goed ontworpen chatapplicatie moet door iedereen bruikbaar zijn. De volgende lijst geeft specifieke functies weer die gericht zijn op het verbeteren van de toegankelijkheid voor verschillende gebruikersbeperkingen.

- **Functies voor visuele beperking**: Thema's met hoog contrast en schaalbare tekst, compatibiliteit met schermlezers.
- **Functies voor auditieve beperking**: Tekst-naar-spraak en spraak-naar-tekst functies, visuele aanwijzingen voor audiomeldingen.
- **Functies voor motorische beperking**: Ondersteuning voor navigatie via het toetsenbord, spraakopdrachten.
- **Functies voor cognitieve beperking**: Opties voor vereenvoudigde taal.

## Aanpassing en afstemming voor domeinspecifieke taalmodellen

Stel je een chatapplicatie voor die de jargon van je bedrijf begrijpt en anticipeert op de specifieke vragen die de gebruikers vaak hebben. Er zijn een paar benaderingen die het vermelden waard zijn:

- **Gebruik maken van DSL-modellen**. DSL staat voor domeinspecifieke taal. Je kunt een zogenaamd DSL-model gebruiken dat is getraind op een specifiek domein om de concepten en scenario's ervan te begrijpen.
- **Afstemming toepassen**. Afstemming is het proces van verdere training van je model met specifieke gegevens.

## Aanpassing: Gebruik maken van een DSL

Het gebruik van domeinspecifieke taalmodellen (DSL-modellen) kan de gebruikersbetrokkenheid verbeteren door gespecialiseerde, contextueel relevante interacties te bieden. Het is een model dat is getraind of afgestemd om tekst te begrijpen en te genereren die verband houdt met een specifiek vakgebied, industrie of onderwerp. Opties voor het gebruik van een DSL-model kunnen variëren van het trainen van een model vanaf nul tot het gebruik van bestaande modellen via SDK's en API's. Een andere optie is afstemming, waarbij een bestaand voorgetraind model wordt aangepast voor een specifiek domein.

## Aanpassing: Afstemming toepassen

Afstemming wordt vaak overwogen wanneer een voorgetraind model tekortschiet in een gespecialiseerd domein of specifieke taak.

Bijvoorbeeld, medische vragen zijn complex en vereisen veel context. Wanneer een medisch professional een patiënt diagnosticeert, is dat gebaseerd op verschillende factoren zoals levensstijl of bestaande aandoeningen, en kan zelfs afhankelijk zijn van recente medische tijdschriften om hun diagnose te valideren. In dergelijke genuanceerde scenario's kan een AI-chatapplicatie voor algemeen gebruik geen betrouwbare bron zijn.

### Scenario: een medische applicatie

Overweeg een chatapplicatie die is ontworpen om medische professionals te ondersteunen door snelle referenties te bieden voor behandelingsrichtlijnen, medicijninteracties of recente onderzoeksresultaten.

Een model voor algemeen gebruik kan geschikt zijn voor het beantwoorden van basis medische vragen of het geven van algemeen advies, maar het kan moeite hebben met het volgende:

- **Zeer specifieke of complexe gevallen**. Bijvoorbeeld, een neuroloog kan de applicatie vragen: "Wat zijn de huidige beste praktijken voor het beheren van medicijnresistente epilepsie bij pediatrische patiënten?"
- **Ontbreken van recente ontwikkelingen**. Een model voor algemeen gebruik kan moeite hebben om een actueel antwoord te geven dat de meest recente ontwikkelingen in neurologie en farmacologie omvat.

In dergelijke gevallen kan het afstemmen van het model met een gespecialiseerde medische dataset de mogelijkheid om deze complexe medische vragen nauwkeuriger en betrouwbaarder te behandelen aanzienlijk verbeteren. Dit vereist toegang tot een grote en relevante dataset die de domeinspecifieke uitdagingen en vragen vertegenwoordigt die moeten worden aangepakt.

## Overwegingen voor een hoogwaardige AI-gestuurde chatervaring

Dit gedeelte schetst de criteria voor "hoogwaardige" chatapplicaties, waaronder het vastleggen van bruikbare statistieken en het naleven van een kader dat AI-technologie op een verantwoorde manier benut.

### Belangrijke statistieken

Om de hoogwaardige prestaties van een applicatie te behouden, is het essentieel om belangrijke statistieken en overwegingen bij te houden. Deze metingen zorgen niet alleen voor de functionaliteit van de applicatie, maar beoordelen ook de kwaliteit van het AI-model en de gebruikerservaring. Hieronder staat een lijst met basis-, AI- en gebruikerservaringsstatistieken om te overwegen.

| Statistiek                     | Definitie                                                                                                             | Overwegingen voor chatontwikkelaar                                       |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Uptime**                     | Meet de tijd dat de applicatie operationeel en toegankelijk is voor gebruikers.                                       | Hoe minimaliseer je downtime?                                            |
| **Reactietijd**                | De tijd die de applicatie nodig heeft om te reageren op een gebruikersvraag.                                          | Hoe kun je de verwerking van vragen optimaliseren om de reactietijd te verbeteren? |
| **Precisie**                   | De verhouding van echte positieve voorspellingen tot het totale aantal positieve voorspellingen.                      | Hoe valideer je de precisie van je model?                                |
| **Recall (gevoeligheid)**      | De verhouding van echte positieve voorspellingen tot het werkelijke aantal positieven.                                | Hoe meet en verbeter je de recall?                                       |
| **F1-score**                   | Het harmonisch gemiddelde van precisie en recall, dat de afweging tussen beide in balans brengt.                      | Wat is je doel-F1-score? Hoe balanceer je precisie en recall?            |
| **Perplexiteit**               | Meet hoe goed de kansverdeling voorspeld door het model overeenkomt met de werkelijke verdeling van de gegevens.      | Hoe minimaliseer je perplexiteit?                                        |
| **Gebruikerservaringsstatistieken** | Meet de perceptie van de gebruiker over de applicatie. Vaak vastgelegd via enquêtes.                                | Hoe vaak verzamel je gebruikersfeedback? Hoe pas je je aan op basis daarvan? |
| **Foutpercentage**             | Het percentage fouten dat het model maakt bij het begrijpen of genereren van output.                                 | Welke strategieën heb je om foutpercentages te verminderen?              |
| **Hertrainingscycli**          | De frequentie waarmee het model wordt bijgewerkt om nieuwe gegevens en inzichten te integreren.                      | Hoe vaak hertrain je het model? Wat triggert een hertrainingscyclus?     |
| **Detectie van anomalieën**   | Tools en technieken om ongebruikelijke patronen te identificeren die niet overeenkomen met verwacht gedrag.             | Hoe ga je reageren op anomalieën?                                           |

### Verantwoordelijke AI-praktijken implementeren in chatapplicaties

De aanpak van Microsoft voor Verantwoordelijke AI heeft zes principes geïdentificeerd die AI-ontwikkeling en -gebruik zouden moeten begeleiden. Hieronder staan de principes, hun definitie, en zaken waar een chatontwikkelaar rekening mee moet houden en waarom ze belangrijk zijn.

| Principes               | Definitie van Microsoft                              | Overwegingen voor de chatontwikkelaar                                 | Waarom het belangrijk is                                                                |
| ----------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Eerlijkheid             | AI-systemen moeten alle mensen eerlijk behandelen.   | Zorg ervoor dat de chatapplicatie niet discrimineert op basis van gebruikersgegevens. | Om vertrouwen en inclusiviteit onder gebruikers op te bouwen; voorkomt juridische gevolgen. |
| Betrouwbaarheid en Veiligheid | AI-systemen moeten betrouwbaar en veilig functioneren. | Voer tests uit en implementeer noodmaatregelen om fouten en risico's te minimaliseren. | Zorgt voor gebruikerstevredenheid en voorkomt mogelijke schade.                         |
| Privacy en Beveiliging  | AI-systemen moeten veilig zijn en privacy respecteren. | Implementeer sterke encryptie en maatregelen voor gegevensbescherming. | Om gevoelige gebruikersgegevens te beschermen en te voldoen aan privacywetten.          |
| Inclusiviteit           | AI-systemen moeten iedereen in staat stellen en mensen betrekken. | Ontwerp een UI/UX die toegankelijk en gebruiksvriendelijk is voor diverse doelgroepen. | Zorgt ervoor dat een breder scala aan mensen de applicatie effectief kan gebruiken.     |
| Transparantie           | AI-systemen moeten begrijpelijk zijn.                | Zorg voor duidelijke documentatie en uitleg over AI-antwoorden.       | Gebruikers hebben meer vertrouwen in een systeem als ze begrijpen hoe beslissingen worden genomen. |
| Verantwoordelijkheid    | Mensen moeten verantwoordelijk zijn voor AI-systemen. | Stel een duidelijk proces op voor het controleren en verbeteren van AI-beslissingen. | Maakt voortdurende verbetering en corrigerende maatregelen mogelijk in geval van fouten. |

## Opdracht

Zie [opdracht](../../../07-building-chat-applications/python). Deze neemt je mee door een reeks oefeningen, van het uitvoeren van je eerste chatprompts tot het classificeren en samenvatten van tekst en meer. Let op dat de opdrachten beschikbaar zijn in verschillende programmeertalen!

## Goed gedaan! Ga verder met je reis

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis over Generatieve AI verder te verdiepen!

Ga naar Les 8 om te zien hoe je kunt beginnen met [het bouwen van zoekapplicaties](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.